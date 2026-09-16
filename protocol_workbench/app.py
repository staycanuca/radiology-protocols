"""Run: python -m protocol_workbench.app [--repo PATH] [--port 5180]."""
from __future__ import annotations

import argparse
import hashlib
import html
import io
import ipaddress
import json
import re
import secrets
import socket
import subprocess
import sys
import threading
import unicodedata
import uuid
import time
import difflib
from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, quote

import requests
import yaml
from flask import Flask, jsonify, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.exceptions import Conflict
from PIL import Image
from protocol_workbench.american_sources import AmericanSearch, provenance
from protocol_workbench.smart_extractor import sync_body_parameters
from protocol_workbench.completion import complete, fingerprint, leaves, get_field, set_field, SUMMARY_START, SUMMARY_END
from protocol_workbench.image_search import search_images

CATEGORIES = {
    'ct': ['abdomen', 'cardiac', 'chest', 'msk', 'neuro', 'trauma', 'vascular'],
    'rx': ['torace', 'abdomen', 'coloana', 'craniu-saf', 'membru-superior', 'membru-inferior', 'pediatrie'],
    'irm': ['neuro', 'msk', 'abdomen-pelvis', 'cardiac', 'san'],
    'eco': ['abdomen-pelvis', 'parti-moi-endocrin', 'vascular-doppler', 'msk', 'san', 'pediatrie'],
    'fluoro': ['digestiv', 'urinar', 'c-arm', 'pediatrie'],
}
TERMS = {'ct': 'computed tomography', 'rx': 'radiography', 'irm': 'magnetic resonance imaging', 'eco': 'ultrasound', 'fluoro': 'fluoroscopy'}
STRUCTURES = {
    'ct': {'tech_params': dict, 'series': list},
    'rx': {'tech_params': dict, 'quality_criteria': list, 'protection': list},
    'irm': {'coils_hardware': dict, 'sequences': list, 'safety_considerations': list},
    'eco': {'transducers_equipment': dict, 'technical_settings': dict, 'standard_views': list},
    'fluoro': {'positioning_equipment': dict, 'fluoro_params': dict, 'acquisition_steps': list, 'radiation_safety': list},
}
DEFAULT_LIMIT_MB = 100
LIMIT = DEFAULT_LIMIT_MB * 1024 * 1024


def now():
    return datetime.now(timezone.utc).isoformat()


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(text)).lower() if not unicodedata.combining(c))


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', normalize(text)).strip('-')[:100]


def public_url(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password or parsed.port not in (None, 443):
        raise ValueError('Este necesar un URL HTTPS public, fără autentificare sau port special.')
    for entry in socket.getaddrinfo(parsed.hostname, 443, type=socket.SOCK_STREAM):
        if not ipaddress.ip_address(entry[4][0]).is_global:
            raise ValueError('Adresele locale/private nu sunt permise ca surse externe.')
    return url


def _fetch(url, params=None):
    """Bounded downloads; validate every redirect and refuse private destinations."""
    for _ in range(5):
        public_url(url)
        with requests.get(url, params=params, timeout=(8, 25), stream=True, allow_redirects=False,
                          headers={'User-Agent': 'RadiologyProtocolWorkbench/0.1 (local research tool)'}) as response:
            params = None
            if response.is_redirect:
                url = urljoin(response.url, response.headers['Location'])
                continue
            response.raise_for_status()
            chunks, size = [], 0
            for chunk in response.iter_content(65536):
                size += len(chunk)
                if size > LIMIT:
                    raise ValueError(f'Fișierul depășește limita permisă de {LIMIT // (1024 * 1024)} MB.')
                chunks.append(chunk)
            return b''.join(chunks), response.headers.get('Content-Type', ''), response.url
    raise ValueError('Prea multe redirecționări.')


def fetch(url, params=None):
    try:
        return _fetch(url, params)
    except requests.exceptions.ProxyError as exc:
        raise ValueError(
            'Conexiunea este blocată de proxy-ul cu care a pornit serverul. '
            'Oprește unealta și pornește start-workbench.bat din Windows sau '
            'start-workbench.ps1 din terminalul tău. Dacă folosești un proxy instituțional, '
            'verifică disponibilitatea și configurarea lui. Ciornele salvate rămân intacte.'
        ) from exc


def remote_json(url, params):
    return json.loads(fetch(url, params)[0])


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.hidden = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.parts.append(data.strip())


def plain(text):
    parser = TextExtractor()
    parser.feed(text)
    return '\n'.join(parser.parts)


def extract_text_from_file(raw: bytes, filename: str) -> tuple[str, str]:
    """Extrage textul și detectează tipul documentului (PDF, DOCX, TXT, MD, DOC)."""
    ext = Path(filename).suffix.lower()
    text = ''
    kind = 'Document local'
    if ext == '.pdf' or raw.startswith(b'%PDF'):
        kind = 'Document local (PDF)'
        try:
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(raw))
            text = '\n'.join(page.extract_text() or '' for page in reader.pages[:100])
        except Exception:
            text = ''
    elif ext == '.docx':
        kind = 'Document local (DOCX)'
        try:
            import zipfile
            import xml.etree.ElementTree as ET
            with zipfile.ZipFile(io.BytesIO(raw)) as zf:
                xml_content = zf.read('word/document.xml')
                tree = ET.fromstring(xml_content)
                paragraphs = []
                for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                    texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
                    if texts:
                        paragraphs.append(''.join(texts))
                text = '\n'.join(paragraphs)
        except Exception:
            text = ''
    elif ext in ('.txt', '.md', '.csv', '.json', '.xml', '.html', '.htm'):
        kind = f"Fișier text ({ext.lstrip('.').upper()})"
        text = plain(raw.decode('utf-8', errors='replace'))
    elif ext == '.doc':
        kind = 'Document local (DOC)'
        try:
            runs = re.findall(rb'[\x20-\x7e\t\n\r]{4,}', raw)
            text = '\n'.join(r.decode('ascii', errors='ignore') for r in runs if len(r) > 10)
        except Exception:
            text = ''
    else:
        try:
            text = plain(raw.decode('utf-8'))
            kind = 'Fișier text'
        except Exception:
            text = ''
            kind = f"Fișier local ({ext.lstrip('.').upper() or 'binar'})"
    return text, kind


def frontmatter(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)(.*)\Z', text, re.S)
    if not match:
        raise ValueError('Documentul trebuie să înceapă cu metadate YAML între linii ---.')
    fm = yaml.safe_load(match[1])
    if not isinstance(fm, dict):
        raise ValueError('Metadatele YAML trebuie să fie un obiect.')
    return fm, match[2].strip()


_LIBRARY_CACHE = {}
_LIBRARY_LOCK = threading.Lock()


def library(repo):
    repo = Path(repo).resolve()
    docs = repo / 'docs'
    if not docs.exists():
        return []
    mtimes = []
    for modality in CATEGORIES:
        md = docs / modality
        if md.exists():
            try:
                mtimes.extend((p.as_posix(), p.stat().st_mtime_ns, p.stat().st_size) for p in sorted(md.rglob('*.md')))
            except OSError:
                pass
    cache_key = str(repo)
    mtime_sig = tuple(mtimes)
    with _LIBRARY_LOCK:
        cached = _LIBRARY_CACHE.get(cache_key)
        if cached and cached[0] == mtime_sig:
            return cached[1]

    result = []
    for modality in CATEGORIES:
        mod_dir = docs / modality
        if not mod_dir.exists():
            continue
        for path in sorted(mod_dir.rglob('*.md')):
            if path.name in ('index.md', 'compare.md'):
                continue
            try:
                fm, body = frontmatter(path.read_text(encoding='utf-8'))
                if fm.get('slug'):
                    result.append({'path': path.relative_to(repo).as_posix(), 'fm': fm, 'body': body})
            except (ValueError, yaml.YAMLError):
                continue
    with _LIBRARY_LOCK:
        _LIBRARY_CACHE[cache_key] = (mtime_sig, result)
    return result


def invalidate_library_cache(repo=None):
    with _LIBRARY_LOCK:
        if repo:
            _LIBRARY_CACHE.pop(str(Path(repo).resolve()), None)
        else:
            _LIBRARY_CACHE.clear()


def seed(modality, title):
    modality = {'us': 'eco', 'flouro': 'fluoro', 'mri': 'irm'}.get(modality, modality)
    if modality not in CATEGORIES:
        raise ValueError('Modalitate necunoscută.')
    fm = {'title': title, 'slug': slugify(title), 'modality': modality, 'category': CATEGORIES[modality][0],
          'author': '', 'last_updated': str(date.today()), 'clinical_indications': [], 'position': '', 'images': []}
    specifics = {'ct': {'contrast': {}, 'tech_params': {}, 'series': [], 'recons': []},
                 'rx': {'centering': '', 'sid_dff': '', 'tech_params': {}, 'quality_criteria': [], 'protection': []},
                 'irm': {'coils_hardware': {}, 'sequences': [], 'contrast': {}, 'safety_considerations': []},
                 'eco': {'transducers_equipment': {}, 'technical_settings': {}, 'standard_views': [], 'quality_criteria': []},
                 'fluoro': {'positioning_equipment': {}, 'fluoro_params': {}, 'acquisition_steps': [], 'contrast': {}, 'radiation_safety': []}}
    fm.update(specifics[modality])
    return '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n# ' + title + '\n\n' + SUMMARY_START + '\n' + SUMMARY_END + '\n\n## Pregătire\n\n## Achiziție\n\n## Criterii de calitate\n\n## Siguranță și contraindicații\n'


def inject_source_into_document(document: str, source_title: str, text: str, institution: str = "") -> str:
    cleaned = (text or "").strip()
    if not cleaned:
        return document

    cleaned = re.sub(r'\r\n|\r', '\n', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

    stitle = str(source_title or 'Sursă').strip()
    sinst = str(institution or '').strip()
    header_info = f" ({sinst})" if sinst else ""

    section_title = f"## Conținut preluat: {stitle}{header_info}"

    if f"## Conținut preluat: {stitle}" in document:
        return document

    doc_trimmed = document.rstrip()
    return f"{doc_trimmed}\n\n{section_title}\n\n{cleaned}\n"


def create_app(repo=None, state=None, max_upload_mb=DEFAULT_LIMIT_MB):
    app = Flask(__name__)
    repo = Path(repo or Path(__file__).resolve().parents[1]).resolve()
    state = Path(state or repo / '.protocol-workbench').resolve()
    state.mkdir(parents=True, exist_ok=True)
    (state / 'images').mkdir(exist_ok=True)
    (state / 'sources').mkdir(exist_ok=True)
    (state / 'cache').mkdir(exist_ok=True)
    token = secrets.token_urlsafe(32)
    lock = threading.RLock()
    image_cache = {}
    american_search = AmericanSearch(lambda url: fetch(url), cache_dir=state / 'cache')
    limit_bytes = max_upload_mb * 1024 * 1024
    app.config.update(MAX_CONTENT_LENGTH=limit_bytes, REPO=repo, STATE=state, MAX_UPLOAD_MB=max_upload_mb)

    def draft_path(identifier):
        if not re.fullmatch(r'[a-f0-9]{32}', identifier):
            raise ValueError('Identificator invalid.')
        return state / (identifier + '.json')

    def draft_paths():
        # The state directory also contains JSON metadata, such as the source catalog.
        return sorted(p for p in state.glob('*.json') if re.fullmatch(r'[a-f0-9]{32}', p.stem))

    def read(identifier):
        draft = json.loads(draft_path(identifier).read_text(encoding='utf-8'))
        expected = request.headers.get('X-Workbench-Revision')
        if request.method != 'GET' and expected is not None and expected != str(draft.get('revision', 0)):
            raise Conflict('Dosarul a fost modificat între timp. Redeschide-l înainte de continuare.')
        return draft

    def save(draft):
        path = draft_path(draft['id'])
        previous = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
        if draft.get('status') != 'imported':
            fm, _ = frontmatter(draft['document'])
            if isinstance(fm.get('modality'), str) and fm['modality'] in CATEGORIES:
                complete(draft, frontmatter, seed(fm['modality'], str(fm.get('title', ''))))
        changed = [key for key in ('document', 'sources', 'images', 'status', 'manual_fields', 'completion_decisions') if previous.get(key) != draft.get(key)]
        draft['revision'] = previous.get('revision', 0) + bool(changed)
        if changed and previous:
            old_fm, _ = frontmatter(previous['document'])
            new_fm, _ = frontmatter(draft['document'])
            fields = sorted(set(dict(leaves(old_fm))) | set(dict(leaves(new_fm))))
            entry = {'at': now(), 'revision': draft['revision'], 'changed': changed,
                'document_diff': '\n'.join(difflib.unified_diff(previous['document'].splitlines(), draft['document'].splitlines(),
                    fromfile='înainte', tofile='după', lineterm=''))[:16000],
                'fields': [{'field': field, 'old_value': get_field(old_fm, field), 'new_value': get_field(new_fm, field)}
                           for field in fields if get_field(old_fm, field) != get_field(new_fm, field)]}
            old_sources = {s['id']: s for s in previous.get('sources', [])}
            new_sources = {s['id']: s for s in draft.get('sources', [])}
            entry['source_changes'] = [{'title': (new_sources.get(sid) or old_sources[sid]).get('title'),
                'old_sha256': old_sources.get(sid, {}).get('sha256'), 'new_sha256': new_sources.get(sid, {}).get('sha256')}
                for sid in sorted(set(old_sources) | set(new_sources))
                if old_sources.get(sid, {}).get('sha256') != new_sources.get(sid, {}).get('sha256')]
            draft['history'] = (previous.get('history', []) + [entry])[-100:]
        draft['updated_at'] = now()
        temporary = path.with_suffix('.tmp')
        temporary.write_text(json.dumps(draft, ensure_ascii=False, indent=2, default=str), encoding='utf-8')
        temporary.replace(path)

    def load_local_sources_catalog():
        catalog_file = state / 'local_sources_catalog.json'
        catalog = {}
        if catalog_file.exists():
            try:
                catalog = json.loads(catalog_file.read_text(encoding='utf-8'))
            except Exception:
                catalog = {}

        sources_dir = state / 'sources'
        sources_dir.mkdir(parents=True, exist_ok=True)

        # Scan existing drafts in state to populate catalog
        for p in draft_paths():
            try:
                d = json.loads(p.read_text(encoding='utf-8'))
                for s in d.get('sources', []):
                    ref = s.get('local_file_ref')
                    if ref and ref not in catalog:
                        fpath = sources_dir / ref
                        fsize = fpath.stat().st_size if fpath.exists() else 0
                        catalog[ref] = {
                            'title': s.get('title') or s.get('local_filename') or ref,
                            'institution': s.get('institution', 'Document instituțional intern'),
                            'kind': s.get('kind', 'Document local'),
                            'local_filename': s.get('local_filename', ref),
                            'local_file_ref': ref,
                            'sha256': s.get('sha256', ''),
                            'excerpt': s.get('excerpt', ''),
                            'size_bytes': fsize,
                            'uploaded_at': s.get('checked_at', now()),
                        }
            except Exception:
                pass

        # Scan docs/assets/protocols/sources
        doc_sources_dir = repo / 'docs' / 'assets' / 'protocols' / 'sources'
        if doc_sources_dir.exists():
            for f in doc_sources_dir.glob('*'):
                if f.is_file() and f.name not in catalog:
                    if not (sources_dir / f.name).exists():
                        (sources_dir / f.name).write_bytes(f.read_bytes())
                    clean_title = re.sub(r'^[a-f0-9]{12}_', '', f.name)
                    catalog[f.name] = {
                        'title': clean_title,
                        'institution': 'Arhivă protocoale bibliotecă',
                        'kind': f'Document local ({f.suffix.lstrip(".").upper() or "fișier"})',
                        'local_filename': clean_title,
                        'local_file_ref': f.name,
                        'sha256': hashlib.sha256(f.read_bytes()).hexdigest(),
                        'excerpt': f"Document din biblioteca aplicației ({f.name}).",
                        'size_bytes': f.stat().st_size,
                        'uploaded_at': now(),
                    }
        return catalog

    def save_local_sources_catalog(catalog):
        catalog_file = state / 'local_sources_catalog.json'
        temporary = catalog_file.with_suffix('.tmp')
        temporary.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding='utf-8')
        temporary.replace(catalog_file)

    @app.before_request
    def protect():
        if request.host.split(':')[0] not in ('127.0.0.1', 'localhost', '[::1]'):
            return jsonify(error='Gazdă nepermisă.'), 403
        if request.method != 'GET' and not secrets.compare_digest(request.headers.get('X-Workbench-Token', ''), token):
            return jsonify(error='Sesiune invalidă. Reîncarcă pagina.'), 403

    @app.errorhandler(Exception)
    def error(exc):
        from werkzeug.exceptions import HTTPException
        if isinstance(exc, HTTPException):
            return jsonify(error=exc.description), exc.code
        if isinstance(exc, FileNotFoundError):
            return jsonify(error='Dosarul sau fișierul nu există.'), 404
        if isinstance(exc, (ValueError, yaml.YAMLError, requests.RequestException, OSError)):
            return jsonify(error=str(exc)), 400
        app.logger.exception('Workbench error')
        return jsonify(error='Eroare internă. Consultă consola uneltei.'), 500

    @app.get('/')
    def index():
        return render_template('index.html', token=token, repo=str(repo))

    @app.get('/api/library')
    def get_library():
        q, modality = normalize(request.args.get('q', '')), request.args.get('modality', '')
        return jsonify([p for p in library(repo) if (not modality or p['path'].split('/')[1] == modality)
                        and q in normalize(json.dumps(p, ensure_ascii=False, default=str))])

    @app.get('/api/drafts')
    def get_drafts():
        return jsonify([json.loads(p.read_text(encoding='utf-8')) for p in draft_paths()])

    @app.post('/api/drafts')
    def new_draft():
        data = request.get_json()
        title = str(data.get('title', '')).strip()
        if not title:
            raise ValueError('Completează titlul protocolului.')
        draft = {'id': uuid.uuid4().hex, 'document': seed(data.get('modality', 'ct'), title),
                 'sources': [], 'images': [], 'created_at': now(), 'status': 'draft'}
        with lock:
            save(draft)
        return jsonify(draft)

    @app.put('/api/drafts/<identifier>')
    def update_draft(identifier):
        data = request.get_json()
        frontmatter(data['document'])
        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosarul a fost importat; creează un dosar nou pentru alt protocol.')
            if 'revision' in data and data['revision'] != draft.get('revision', 0):
                return jsonify(error='Dosarul a fost modificat între timp. Redeschide-l înainte de salvare.'), 409
            old_fm, old_body = frontmatter(draft['document'])
            new_fm, new_body = frontmatter(data['document'])
            if old_body != new_body:
                draft['manual_body'] = True
            fields = set(dict(leaves(old_fm))) | set(dict(leaves(new_fm)))
            draft['manual_fields'] = sorted(set(draft.get('manual_fields', [])) |
                {field for field in fields if get_field(old_fm, field) != get_field(new_fm, field)})
            draft['document'] = data['document']
            save(draft)
        return jsonify(draft)

    @app.delete('/api/drafts/<identifier>')
    def delete_draft(identifier):
        with lock:
            path = draft_path(identifier)
            if not path.exists():
                raise FileNotFoundError('Dosarul nu există.')
            try:
                draft = json.loads(path.read_text(encoding='utf-8'))
                for img in draft.get('images', []):
                    img_file = state / 'images' / img.get('file', '')
                    if img_file.exists():
                        try:
                            img_file.unlink()
                        except OSError:
                            pass
            except Exception:
                pass
            path.unlink()
        return jsonify(ok=True, id=identifier)

    def load_protocol_to_draft(rel_path, mode='revision'):
        rel_posix = Path(rel_path).as_posix()
        target = (repo / rel_posix).resolve()
        docs_root = (repo / 'docs').resolve()
        if not target.is_relative_to(docs_root) or not target.exists() or not target.is_file():
            raise ValueError(f'Protocolul nu a fost găsit în docs/: {rel_path}')
        if target.name in ('index.md', 'compare.md'):
            raise ValueError('Fișierele index nu pot fi importate ca protocoale.')

        raw_content = target.read_text(encoding='utf-8')
        fm, body = frontmatter(raw_content)

        parts = Path(rel_posix).parts
        inferred_modality = None
        for i, p in enumerate(parts):
            if p == 'docs' and i + 1 < len(parts):
                inferred_modality = parts[i + 1]
                break

        if 'modality' not in fm or fm['modality'] not in CATEGORIES:
            fm['modality'] = inferred_modality if inferred_modality in CATEGORIES else 'ct'

        if 'category' not in fm or fm['category'] not in CATEGORIES.get(fm['modality'], []):
            for cat in CATEGORIES.get(fm['modality'], []):
                if f'/{cat}/' in rel_posix or f'\\{cat}\\' in rel_path:
                    fm['category'] = cat
                    break

        if not fm.get('author') or not str(fm['author']).strip():
            fm['author'] = 'Departamentul de Radiologie'

        if not fm.get('position') or not str(fm['position']).strip():
            coils_pos = fm.get('coils_hardware', {}).get('positioning') if isinstance(fm.get('coils_hardware'), dict) else None
            eq_pos = fm.get('positioning_equipment', {}).get('patient_position') if isinstance(fm.get('positioning_equipment'), dict) else None
            if coils_pos:
                fm['position'] = coils_pos
            elif eq_pos:
                fm['position'] = eq_pos
            elif fm.get('patient_prep') and isinstance(fm['patient_prep'], str):
                fm['position'] = 'Decubit dorsal adaptat ferestrei acustice / pregătire: ' + fm['patient_prep'][:80]
            else:
                fm['position'] = 'Decubit dorsal conform procedurii standard'

        body_cleaned = re.split(r'\n## (?:Imagini reprezentative|Surse și revizuire)', body)[0].strip()

        draft_sources = []
        for s in fm.pop('sources', []):
            if isinstance(s, dict) and (s.get('url') or s.get('title')):
                s_url = s.get('url', '')
                local_fref = s.get('local_file_ref', '')
                local_fname = s.get('local_filename', '')
                if not local_fref and s_url.startswith('assets/protocols/sources/'):
                    local_fref = Path(s_url).name
                    local_fname = local_fname or local_fref
                if local_fref:
                    src_origin = repo / 'docs' / s_url
                    if src_origin.exists() and not (state / 'sources' / local_fref).exists():
                        (state / 'sources').mkdir(parents=True, exist_ok=True)
                        (state / 'sources' / local_fref).write_bytes(src_origin.read_bytes())
                draft_sources.append({
                    'id': s.get('id') or uuid.uuid4().hex,
                    'title': s.get('title', s_url),
                    'url': s_url,
                    'resolved_url': s.get('resolved_url', s_url),
                    'checked_at': s.get('checked_at', now()),
                    'sha256': s.get('sha256', hashlib.sha256(s_url.encode()).hexdigest()),
                    'excerpt': s.get('excerpt', f"Sursă extrasă din {rel_posix}."),
                    'institution': s.get('institution', ''),
                    'source_region': s.get('source_region', ''),
                    'kind': s.get('kind', ''),
                    'local_filename': local_fname,
                    'local_file_ref': local_fref,
                })

        draft_images = []
        for img in fm.pop('images', []):
            if isinstance(img, dict) and img.get('url'):
                img_url = img['url']
                candidate_paths = [
                    (repo / 'docs' / img_url).resolve(),
                    (repo / img_url).resolve(),
                    (repo / 'docs' / 'assets' / 'images' / 'protocols' / 'workbench' / Path(img_url).name).resolve()
                ]
                found_path = next((p for p in candidate_paths if p.exists() and p.is_file()), None)
                if found_path:
                    img_bytes = found_path.read_bytes()
                    img_sha = hashlib.sha256(img_bytes).hexdigest()
                    img_file = img_sha + '.jpg'
                    (state / 'images' / img_file).write_bytes(img_bytes)
                    draft_images.append({
                        'file': img_file,
                        'sha256': img_sha,
                        'caption': img.get('caption', found_path.stem),
                        'author': img.get('author', 'Arhivă clinică'),
                        'license': img.get('license', 'Uz instituțional'),
                        'source_url': img.get('source_url', img_url),
                        'license_url': img.get('license_url', '')
                    })

        fm['images'] = []
        fm.pop('workbench_review', None)

        if mode == 'clone':
            fm['title'] = str(fm.get('title', '')) + ' (Adaptat)'
            orig_slug = str(fm.get('slug', 'protocol'))
            fm['slug'] = slugify(orig_slug + '-adaptat')[:100]
            is_rev = False
            orig_p = None
        else:
            is_rev = True
            orig_p = rel_posix

        new_doc = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + body_cleaned + '\n'

        draft = {
            'id': uuid.uuid4().hex,
            'document': new_doc,
            'sources': draft_sources,
            'images': draft_images,
            'created_at': now(),
            'status': 'draft',
            'origin_path': orig_p,
            'origin_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
            'is_revision': is_rev,
            'manual_body': True,
        }
        return draft

    @app.post('/api/drafts/from-library')
    def draft_from_library():
        data = request.get_json() or {}
        path = str(data.get('path', '')).strip()
        mode = data.get('mode', 'revision')
        draft = load_protocol_to_draft(path, mode)
        with lock:
            save(draft)
        return jsonify(draft)

    @app.post('/api/drafts/import-bulk')
    def import_bulk():
        data = request.get_json() or {}
        modality = data.get('modality')
        mode = data.get('mode', 'revision')
        all_protocols = library(repo)

        existing_draft_origins = set()
        for p in draft_paths():
            try:
                d = json.loads(p.read_text(encoding='utf-8'))
                if d.get('origin_path'):
                    existing_draft_origins.add(d['origin_path'])
            except Exception:
                pass

        created = []
        with lock:
            for p in all_protocols:
                p_path = p['path']
                parts = Path(p_path).parts
                p_mod = parts[1] if len(parts) > 1 else ''
                if modality and modality != 'all' and p_mod != modality:
                    continue
                if p_path in existing_draft_origins:
                    continue
                try:
                    d = load_protocol_to_draft(p_path, mode)
                    save(d)
                    existing_draft_origins.add(p_path)
                    created.append({'id': d['id'], 'title': p['fm'].get('title'), 'path': p_path})
                except Exception as exc:
                    app.logger.warning(f"Could not import {p_path}: {exc}")
        return jsonify(count=len(created), drafts=created)

    @app.get('/api/search')
    def search():
        query = request.args.get('q', '').strip()
        modality = request.args.get('modality', 'ct')
        if modality not in TERMS:
            raise ValueError('Introdu o modalitate validă.')
        provider = request.args.get('provider', 'europepmc')
        if provider == 'us':
            return jsonify(american_search.search(query, modality, request.args.get('institution', 'all')))
        if provider != 'europepmc':
            raise ValueError('Furnizor necunoscut.')
        if not query:
            return jsonify(results=[], note='Introdu un termen de căutare.')
        terms = query + ' ' + TERMS[modality]
        data = remote_json('https://www.ebi.ac.uk/europepmc/webservices/rest/search',
                           {'query': terms + ' (protocol OR guideline OR consensus)', 'format': 'json', 'pageSize': 12, 'resultType': 'core'})
        results = []
        for item in data.get('resultList', {}).get('result', []):
            results.append({'title': item.get('title', ''), 'year': item.get('pubYear', ''),
                            'authors': item.get('authorString', ''), 'summary': plain(item.get('abstractText', ''))[:2400],
                            'url': 'https://europepmc.org/article/' + quote(item['source']) + '/' + quote(item['id'])})
        return jsonify(results=results, note='Rezultate bibliografice; relevanța și recomandările se verifică în documentul original.')

    @app.post('/api/drafts/<identifier>/sources')
    def add_source(identifier):
        data = request.get_json()
        manual = str(data.get('manual_excerpt') or data.get('excerpt') or '').strip()
        url = data.get('url', '').strip()
        raw, mime, final_url = fetch(url)
        if 'pdf' in mime or raw.startswith(b'%PDF'):
            try:
                from pypdf import PdfReader
                reader = PdfReader(io.BytesIO(raw))
                text = '\n'.join(page.extract_text() or '' for page in reader.pages[:100])
            except ImportError:
                if len(manual) < 50:
                    raise ValueError('Pentru PDF instalează dependențele din protocol_workbench/requirements.txt.')
                text = ''
            except Exception:
                text = ''
        elif 'html' in mime or mime.startswith('text/'):
            text = plain(raw.decode('utf-8', errors='replace'))
        else:
            raise ValueError('Sursa trebuie să fie o pagină HTML, text sau PDF.')
        manual = str(data.get('manual_excerpt') or data.get('excerpt') or '').strip()
        if len(text.strip()) < 100:
            if len(manual) >= 50:
                text = f"[Extras manual / PDF scanat]\n{manual}"
            else:
                raise ValueError('Nu s-a putut extrage suficient text. PDF-ul poate necesita OCR.')
        source = {'id': uuid.uuid4().hex, 'title': str(data.get('title') or url), 'url': url, 'resolved_url': final_url,
                  'checked_at': now(), 'sha256': hashlib.sha256(raw).hexdigest(), 'excerpt': text[:20000]}
        source.update(provenance(final_url))
        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            existing = next((s for s in draft['sources'] if s['url'] == url), None)
            if existing:
                source['id'] = existing['id']
            draft['sources'] = [s for s in draft['sources'] if s['url'] != url] + [source]
            save(draft)
        return jsonify(draft)

    @app.post('/api/drafts/<identifier>/sources/upload')
    def upload_local_source(identifier):
        if 'file' not in request.files:
            raise ValueError('Selectează un fișier pentru încărcare.')
        file = request.files['file']
        if not file.filename:
            raise ValueError('Fișier invalid.')
        orig_name = Path(file.filename).name
        sec_name = secure_filename(orig_name) or 'document'
        limit_bytes = app.config.get('MAX_CONTENT_LENGTH', LIMIT)
        raw = file.read(limit_bytes)
        if len(raw) >= limit_bytes:
            raise ValueError(f'Fișierul depășește limita permisă de {app.config.get("MAX_UPLOAD_MB", DEFAULT_LIMIT_MB)} MB.')

        title = str(request.form.get('title') or '').strip() or Path(orig_name).stem
        institution = str(request.form.get('institution') or '').strip() or 'Document instituțional intern'
        kind_param = str(request.form.get('kind') or '').strip()
        manual = str(request.form.get('manual_excerpt') or '').strip()

        extracted_text, detected_kind = extract_text_from_file(raw, orig_name)
        kind = kind_param or detected_kind

        if len(extracted_text.strip()) < 50:
            if len(manual) >= 30:
                extracted_text = f"[Extras manual / Document local]\n{manual}"
            else:
                raise ValueError('Nu s-a putut extrage text din document (poate fi un fișier scanat sau format binar vechi). Introdu un extras manual de minim 30 caractere în formular.')

        sha256 = hashlib.sha256(raw).hexdigest()
        sources_dir = state / 'sources'
        sources_dir.mkdir(parents=True, exist_ok=True)
        saved_name = f"{sha256[:12]}_{sec_name}"
        (sources_dir / saved_name).write_bytes(raw)

        source = {
            'id': uuid.uuid4().hex,
            'title': title,
            'url': f'local://{sec_name}',
            'resolved_url': f'local://{sec_name}',
            'institution': institution,
            'source_region': 'Local / Instituțional',
            'kind': kind,
            'local_filename': orig_name,
            'local_file_ref': saved_name,
            'checked_at': now(),
            'sha256': sha256,
            'excerpt': extracted_text[:20000]
        }

        catalog = load_local_sources_catalog()
        catalog[saved_name] = {
            'title': title,
            'institution': institution,
            'kind': kind,
            'local_filename': orig_name,
            'local_file_ref': saved_name,
            'sha256': sha256,
            'excerpt': extracted_text[:20000],
            'size_bytes': len(raw),
            'uploaded_at': now(),
        }
        save_local_sources_catalog(catalog)

        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            draft['sources'] = [s for s in draft['sources'] if s.get('sha256') != sha256] + [source]
            save(draft)
        return jsonify(draft)

    @app.get('/api/sources/local-library')
    def get_local_sources_library():
        catalog = load_local_sources_catalog()
        items = sorted(catalog.values(), key=lambda x: x.get('uploaded_at', ''), reverse=True)
        return jsonify(items)

    @app.post('/api/drafts/<identifier>/sources/attach-local')
    def attach_existing_local_source(identifier):
        data = request.get_json() or {}
        ref = str(data.get('local_file_ref') or '').strip()
        if not ref:
            raise ValueError('Selectează un document din biblioteca locală.')
        catalog = load_local_sources_catalog()
        item = catalog.get(ref)
        if not item:
            raise ValueError('Documentul selectat nu a fost găsit în catalogul local.')

        sources_dir = state / 'sources'
        fpath = sources_dir / ref
        if not fpath.exists():
            doc_fpath = repo / 'docs' / 'assets' / 'protocols' / 'sources' / ref
            if doc_fpath.exists():
                sources_dir.mkdir(parents=True, exist_ok=True)
                fpath.write_bytes(doc_fpath.read_bytes())
            else:
                raise ValueError('Fișierul fizic nu a fost găsit pe disc.')

        sec_name = secure_filename(item.get('local_filename', ref)) or ref
        source = {
            'id': uuid.uuid4().hex,
            'title': item['title'],
            'url': f'local://{sec_name}',
            'resolved_url': f'local://{sec_name}',
            'institution': item.get('institution', 'Document instituțional intern'),
            'source_region': 'Local / Instituțional',
            'kind': item.get('kind', 'Document local'),
            'local_filename': item.get('local_filename', ref),
            'local_file_ref': ref,
            'checked_at': now(),
            'sha256': item.get('sha256') or hashlib.sha256(fpath.read_bytes()).hexdigest(),
            'excerpt': item.get('excerpt', '')
        }

        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            draft['sources'] = [s for s in draft['sources'] if s.get('local_file_ref') != ref] + [source]
            save(draft)
        return jsonify(draft)

    @app.get('/api/drafts/<identifier>/sources/<source_id>/file')
    def get_source_file(identifier, source_id):
        draft = read(identifier)
        source = next((s for s in draft['sources'] if s['id'] == source_id), None)
        if not source or not source.get('local_file_ref'):
            raise ValueError('Fișierul sursă local nu a fost găsit.')
        sources_dir = state / 'sources'
        ref = source['local_file_ref']
        if (sources_dir / ref).exists():
            return send_from_directory(sources_dir, ref, as_attachment=False)
        doc_sources_dir = repo / 'docs' / 'assets' / 'protocols' / 'sources'
        if (doc_sources_dir / ref).exists():
            return send_from_directory(doc_sources_dir, ref, as_attachment=False)
        raise ValueError('Fișierul sursă local nu a fost găsit pe disc.')

    @app.post('/api/drafts/<identifier>/sources/<source_id>/smart-extract')
    def smart_extract_source_parameters(identifier, source_id):
        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            source = next((s for s in draft['sources'] if s['id'] == source_id), None)
            if not source:
                raise ValueError('Sursa nu a fost găsită în dosar.')

            text_to_analyze = source.get('excerpt', '')
            if source.get('local_file_ref'):
                fpath = state / 'sources' / source['local_file_ref']
                if not fpath.exists():
                    fpath = repo / 'docs' / 'assets' / 'protocols' / 'sources' / source['local_file_ref']
                if fpath.exists():
                    try:
                        full_text, _ = extract_text_from_file(fpath.read_bytes(), source.get('local_filename', source['local_file_ref']))
                        if len(full_text.strip()) > len(text_to_analyze):
                            text_to_analyze = full_text
                    except Exception:
                        pass

            source['excerpt'] = text_to_analyze[:200000]
            save(draft)
            diffs = [dict(d, label=d['field']) for d in draft['completion']['changes']]

            return jsonify({
                'draft': draft,
                'diffs': diffs,
                'count': len(diffs),
                'source_title': source.get('title', 'Sursă')
            })

    @app.get('/api/images/search')
    def image_search():
        query = request.args.get('q', '').strip()
        if not query:
            raise ValueError('Introdu termenii pentru imagini.')
        modality, provider = request.args.get('modality', ''), request.args.get('provider', 'all')
        key = (normalize(query), modality, provider)
        with lock:
            cached = image_cache.get(key)
        if cached and time.monotonic() - cached[0] < 300:
            result = cached[1]
        else:
            result = search_images(remote_json, plain, query, modality, provider)
            if not any(p['error'] for p in result['providers']):
                with lock:
                    if len(image_cache) >= 32:
                        image_cache.pop(next(iter(image_cache)))
                    image_cache[key] = (time.monotonic(), result)
        return jsonify(result if request.args.get('details') == '1' else result['results'])

    @app.post('/api/drafts/<identifier>/complete')
    def complete_draft(identifier):
        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            save(draft)
            return jsonify(draft)

    @app.post('/api/drafts/<identifier>/completion/resolve')
    def resolve_completion(identifier):
        data = request.get_json()
        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            if data.get('revision') != draft.get('revision', 0):
                return jsonify(error='Dosarul s-a modificat. Reanalizează sursele.'), 409
            conflict = next((c for c in draft.get('completion', {}).get('conflicts', []) if c['field'] == data.get('field')), None)
            if not conflict:
                raise ValueError('Conflictul nu mai există. Reanalizează sursele.')
            candidate = next((c for c in conflict['candidates'] if c['source_id'] == data.get('source_id')), None)
            if data.get('keep_current') is True:
                candidate = {'value': conflict['current'], 'source_id': None}
            if not candidate:
                raise ValueError('Sursă necunoscută pentru acest câmp.')
            fm, body = frontmatter(draft['document'])
            draft.setdefault('completion_decisions', {})[conflict['field']] = {
                'candidates': fingerprint(conflict['candidates']), 'value': candidate['value'], 'source_id': candidate['source_id']}
            set_field(fm, conflict['field'], candidate['value'])
            accepted = {}
            set_field(accepted, conflict['field'], candidate['value'])
            if not data.get('keep_current'):
                body = sync_body_parameters(body, accepted, fm['modality'])
            if candidate['source_id']:
                draft['completion']['provenance'][conflict['field']] = {'value': candidate['value'],
                    'context': draft['completion']['context'], 'sources': [candidate]}
            draft['manual_fields'] = sorted(set(draft.get('manual_fields', [])) | {conflict['field']})
            draft['document'] = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + body.strip() + '\n'
            save(draft)
            return jsonify(draft)

    @app.post('/api/drafts/<identifier>/images')
    def attach_image(identifier):
        data = request.form.to_dict() if request.files else request.get_json()
        for key in ('caption', 'author', 'license', 'source_url'):
            if not str(data.get(key, '')).strip():
                raise ValueError('Imaginea necesită legendă, autor, licență și sursă.')
        limit_bytes = app.config.get('MAX_CONTENT_LENGTH', LIMIT)
        if request.files:
            raw = request.files['file'].read(limit_bytes + 1)
        else:
            raw = fetch(data['url'])[0]
        if len(raw) > limit_bytes:
            raise ValueError(f'Imaginea depășește limita permisă de {app.config.get("MAX_UPLOAD_MB", DEFAULT_LIMIT_MB)} MB.')
        with Image.open(io.BytesIO(raw)) as img:
            if img.width * img.height > 40000000:
                raise ValueError('Rezoluție prea mare (maximum 40 megapixeli).')
            img.load()
            output = io.BytesIO()
            img.convert('RGB').save(output, format='JPEG', quality=92)
        # Re-encode to strip EXIF; burned-in identifiers still require human review.
        content = output.getvalue()
        name = hashlib.sha256(content).hexdigest() + '.jpg'
        image_data = {key: str(data.get(key, '')) for key in ('caption', 'author', 'license', 'source_url', 'license_url')}
        image_data.update(file=name, sha256=hashlib.sha256(content).hexdigest())
        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            (state / 'images' / name).write_bytes(content)
            draft['images'] = [i for i in draft['images'] if i['file'] != name] + [image_data]
            save(draft)
        return jsonify(draft)

    @app.delete('/api/drafts/<identifier>/<kind>/<item_id>')
    def remove_attachment(identifier, kind, item_id):
        if kind not in ('images', 'sources'):
            raise ValueError('Tip invalid.')
        with lock:
            draft = read(identifier)
            if draft['status'] == 'imported':
                raise ValueError('Dosar deja importat.')
            key = 'file' if kind == 'images' else 'id'
            draft[kind] = [i for i in draft[kind] if i[key] != item_id]
            save(draft)
        return jsonify(draft)

    @app.get('/images/<name>')
    def local_image(name):
        return send_from_directory(state / 'images', name)

    def validate(draft):
        errors, warnings = [], []
        completion = draft.get('completion', {})
        for conflict in completion.get('conflicts', []):
            warnings.append('Valori diferite între protocol și surse: ' + conflict['field'])
        for field in completion.get('stale_fields', []):
            warnings.append('Proveniență de reverificat (sursă/context modificat): ' + field)
        fm, body = frontmatter(draft['document'])
        if draft.get('is_revision') and draft.get('origin_sha256'):
            origin = (repo / draft['origin_path']).resolve()
            if not origin.is_relative_to(repo / 'docs') or not origin.is_file() or hashlib.sha256(origin.read_bytes()).hexdigest() != draft['origin_sha256']:
                errors.append('Protocolul original a fost modificat în bibliotecă. Compară versiunea actuală înainte de import.')
        modality = fm.get('modality')
        pending = fm.get('review_required_fields', [])
        if not isinstance(pending, list):
            errors.append('review_required_fields trebuie să fie o listă YAML.')
        elif pending:
            errors.extend('De rezolvat la revizuire: ' + str(field) for field in pending)
        if fm.get('clinical_status') == 'draft_not_for_clinical_use':
            errors.append('Ciorna este marcată neutilizabilă clinic; finalizează revizuirea înainte de import.')
        if 'DE CONFIGURAT PE APARAT' in yaml.safe_dump(fm, allow_unicode=True):
            errors.append('Au rămas parametri marcați DE CONFIGURAT PE APARAT.')
        if not isinstance(modality, str):
            raise ValueError('modality trebuie să fie text: ct, rx, irm, eco sau fluoro.')
        if modality not in CATEGORIES:
            errors.append('Modalitate: ct, rx, irm, eco (US) sau fluoro.')
        elif fm.get('category') not in CATEGORIES[modality]:
            errors.append('Categorie permisă: ' + ', '.join(CATEGORIES[modality]))
        for key, expected in STRUCTURES.get(modality, {}).items():
            if not isinstance(fm.get(key), expected) or not fm[key]:
                errors.append('Completează ' + key + (' ca listă YAML.' if expected is list else ' ca obiect YAML.'))
        for key in ('series', 'recons', 'sequences', 'standard_views', 'acquisition_steps'):
            if key in fm and (not isinstance(fm[key], list) or any(not isinstance(v, dict) for v in fm[key])):
                errors.append(key + ' trebuie să conțină obiecte YAML, nu texte simple.')
        if 'contrast' in fm and not isinstance(fm['contrast'], dict):
            errors.append('contrast trebuie să fie un obiect YAML.')
        elif isinstance(fm.get('contrast'), dict) and 'agent' in fm['contrast'] and not isinstance(fm['contrast']['agent'], str):
            errors.append('contrast.agent trebuie să fie text.')
        for key in ('title', 'author', 'position'):
            if not isinstance(fm.get(key), str) or not fm[key].strip():
                errors.append('Câmp obligatoriu: ' + key)
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(fm.get('slug', ''))) or len(str(fm.get('slug', ''))) > 100:
            errors.append('Slug invalid (litere mici, cifre și cratime; maximum 100 caractere).')
        if re.fullmatch(r'con|prn|aux|nul|com[1-9]|lpt[1-9]', str(fm.get('slug', '')), re.I):
            errors.append('Slug rezervat de Windows; alege un nume mai descriptiv.')
        if (not isinstance(fm.get('clinical_indications'), list) or not fm.get('clinical_indications')
                or any(not isinstance(v, str) or not v.strip() for v in fm.get('clinical_indications', []))):
            errors.append('Completează lista clinical_indications.')
        try:
            updated = date.fromisoformat(str(fm.get('last_updated', '')))
            if updated > date.today():
                errors.append('Data actualizării este în viitor.')
        except ValueError:
            errors.append('last_updated trebuie să fie o dată YYYY-MM-DD.')
        if len(re.sub(r'(?m)^#+.*$', '', body).strip()) < 120:
            errors.append('Completează corpul protocolului cu instrucțiunile revizuite.')
        if re.search(r'<\s*(script|iframe|object|embed)|javascript:|data:text/html', draft['document'], re.I):
            errors.append('Conținut activ HTML/JavaScript nepermis.')
        if fm.get('images'):
            errors.append('Adaugă imaginile prin secțiunea dedicată; păstrează images: [] în editor.')
        for p in library(repo):
            is_self = draft.get('is_revision') and draft.get('origin_path') == p['path']
            if p['fm'].get('slug') == fm.get('slug') and not is_self:
                errors.append('Există deja un protocol cu acest slug: ' + p['path'])
            elif normalize(p['fm'].get('title')) == normalize(fm.get('title')) and not is_self:
                warnings.append('Titlu identic în bibliotecă: ' + p['path'])
        if not draft['sources']:
            errors.append('Adaugă cel puțin o sursă verificată online.')
        for source in draft['sources']:
            if (datetime.now(timezone.utc) - datetime.fromisoformat(source['checked_at'])).days > 30:
                errors.append('Reverifică sursa mai veche de 30 zile: ' + source['title'])
        if not draft['images']:
            if draft.get('is_revision'):
                warnings.append('Protocolul din bibliotecă nu conține imagini atașate; se recomandă adăugarea uneia reprezentative.')
            else:
                errors.append('Adaugă cel puțin o imagine reprezentativă cu atribuire.')
        for item in draft['images']:
            path = state / 'images' / item['file']
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
                errors.append('Imagine lipsă sau modificată: ' + item['caption'])
        warnings.append('Verificarea automată nu confirmă corectitudinea clinică, actualitatea recomandărilor sau relevanța imaginilor.')
        return {'errors': errors, 'warnings': warnings, 'valid': not errors}

    @app.post('/api/drafts/<identifier>/validate')
    def check(identifier):
        return jsonify(validate(read(identifier)))

    def reindex():
        logs = []
        for name in ('generate_comparison_index.py', 'generate_sitemap.py', 'generate_forms_index.py'):
            try:
                result = subprocess.run([sys.executable, str(repo / 'scripts' / name)], cwd=repo,
                                        capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=90)
                logs.append({'script': name, 'ok': result.returncode == 0, 'output': (result.stdout + result.stderr)[-2500:]})
            except (OSError, subprocess.TimeoutExpired) as exc:
                logs.append({'script': name, 'ok': False, 'output': str(exc)})
        return logs

    @app.post('/api/reindex')
    def rebuild():
        with lock:
            return jsonify(logs=reindex())

    @app.post('/api/drafts/<identifier>/import')
    def import_draft(identifier):
        data = request.get_json()
        reviewer = str(data.get('reviewer', '')).strip()
        if not reviewer or any(data.get(key) is not True for key in ('clinical_review', 'image_review', 'rights_review')):
            raise ValueError('Completează numele recenzorului și confirmă revizuirea clinică, imaginile și drepturile de utilizare.')
        with lock:
            draft = read(identifier)
            report = validate(draft)
            if not report['valid']:
                return jsonify(error='Import blocat de verificări.', **report), 400
            fm, body = frontmatter(draft['document'])
            # YAML dates are allowed in the editor; app indices expect JSON-compatible scalars.
            fm = json.loads(json.dumps(fm, default=str))
            target = repo / 'docs' / fm['modality'] / fm['category'] / (fm['slug'] + '.md')
            if not target.resolve().is_relative_to((repo / 'docs').resolve()):
                raise ValueError('Destinație invalidă.')
            target.parent.mkdir(parents=True, exist_ok=True)
            assets = repo / 'docs' / 'assets' / 'images' / 'protocols' / 'workbench'
            assets.mkdir(parents=True, exist_ok=True)
            fm['images'] = []
            gallery = '\n\n## Imagini reprezentative\n' if draft['images'] else ''
            for item in draft['images']:
                destination = assets / item['file']
                destination.write_bytes((state / 'images' / item['file']).read_bytes())
                url = 'assets/images/protocols/workbench/' + item['file']
                attribution = item['author'] + ' · ' + item['license'] + ' · ' + item['source_url']
                fm['images'].append({'url': url, 'caption': item['caption'], 'description': attribution,
                                     'author': item['author'], 'license': item['license'], 'source_url': item['source_url']})
                caption = html.escape(item['caption']).replace('[', '&#91;').replace(']', '&#93;')
                gallery += '\n![' + caption + '](../../' + url + ')\n\n' + html.escape(attribution) + '\n'
            ref_sources = []
            for s in draft['sources']:
                item = {k: v for k, v in s.items() if k != 'excerpt'}
                if s.get('local_file_ref'):
                    src_dest = repo / 'docs' / 'assets' / 'protocols' / 'sources'
                    src_dest.mkdir(parents=True, exist_ok=True)
                    src_file = state / 'sources' / s['local_file_ref']
                    if src_file.exists():
                        (src_dest / s['local_file_ref']).write_bytes(src_file.read_bytes())
                    item['url'] = 'assets/protocols/sources/' + s['local_file_ref']
                    item['resolved_url'] = 'assets/protocols/sources/' + s['local_file_ref']
                ref_sources.append(item)
            fm['sources'] = ref_sources
            fm['workbench_provenance'] = draft.get('completion', {}).get('provenance', {})
            fm['workbench_review'] = {'reviewer': reviewer, 'reviewed_at': now(), 'draft_id': identifier,
                                       'clinical_review': True, 'image_review': True, 'rights_review': True}
            ref_lines = []
            for s in ref_sources:
                stitle = html.escape(s.get('title', 'Sursă'))
                sinst = html.escape(s.get('institution', ''))
                skind = html.escape(s.get('kind', ''))
                if s.get('local_file_ref'):
                    rel_url = '../../assets/protocols/sources/' + s['local_file_ref']
                    fname = html.escape(s.get('local_filename', 'document'))
                    desc = f" ({skind}: {fname})" if skind else f" ({fname})"
                    extra = f" — *{sinst}*" if sinst else ""
                    ref_lines.append(f"- [{stitle}]({rel_url}){desc}{extra}")
                else:
                    extra = f" — *{sinst}*" if sinst else ""
                    ref_lines.append(f"- [{stitle}]({s['url']}){extra}")
            references = '\n\n## Surse și revizuire\n\n' + '\n'.join(ref_lines)
            references += '\n\nRevizuit de: ' + html.escape(reviewer) + ' · ' + str(date.today()) + '\n'
            document = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + body + gallery + references
            # Exclusive creation protects existing protocols, unless revising the exact origin file.
            mode_flag = 'w' if (draft.get('is_revision') and draft.get('origin_path') == target.relative_to(repo).as_posix()) else 'x'
            with target.open(mode_flag, encoding='utf-8') as handle:
                handle.write(document)
            invalidate_library_cache(repo)
            draft.update(status='imported', imported_path=target.relative_to(repo).as_posix(), review=fm['workbench_review'])
            save(draft)
            logs = reindex()
        return jsonify(path=draft['imported_path'], logs=logs, indexed=all(log['ok'] for log in logs))

    return app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Protocol Workbench — standalone local')
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--port', type=int, default=5180)
    parser.add_argument('--max-upload-mb', type=int, default=DEFAULT_LIMIT_MB,
                        help=f'Limita maximă de încărcare fișiere în MB (implicit: {DEFAULT_LIMIT_MB} MB)')
    args = parser.parse_args()
    create_app(args.repo, max_upload_mb=args.max_upload_mb).run(host='127.0.0.1', port=args.port, debug=False)
