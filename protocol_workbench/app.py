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
from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, quote

import requests
import yaml
from flask import Flask, jsonify, render_template, request, send_from_directory
from PIL import Image
from protocol_workbench.american_sources import AmericanSearch, provenance

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
LIMIT = 16 * 1024 * 1024


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
                    raise ValueError('Fișierul depășește limita de 16 MB.')
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
                mtimes.append(md.stat().st_mtime_ns)
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
    return '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n# ' + title + '\n\n## Pregătire\n\n## Achiziție\n\n## Criterii de calitate\n\n## Siguranță și contraindicații\n'


def create_app(repo=None, state=None):
    app = Flask(__name__)
    repo = Path(repo or Path(__file__).resolve().parents[1]).resolve()
    state = Path(state or repo / '.protocol-workbench').resolve()
    state.mkdir(parents=True, exist_ok=True)
    (state / 'images').mkdir(exist_ok=True)
    (state / 'cache').mkdir(exist_ok=True)
    token = secrets.token_urlsafe(32)
    lock = threading.RLock()
    american_search = AmericanSearch(lambda url: fetch(url), cache_dir=state / 'cache')
    app.config.update(MAX_CONTENT_LENGTH=LIMIT, REPO=repo, STATE=state)

    def draft_path(identifier):
        if not re.fullmatch(r'[a-f0-9]{32}', identifier):
            raise ValueError('Identificator invalid.')
        return state / (identifier + '.json')

    def read(identifier):
        return json.loads(draft_path(identifier).read_text(encoding='utf-8'))

    def save(draft):
        draft['updated_at'] = now()
        path = draft_path(draft['id'])
        temporary = path.with_suffix('.tmp')
        temporary.write_text(json.dumps(draft, ensure_ascii=False, indent=2), encoding='utf-8')
        temporary.replace(path)

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
        return jsonify([json.loads(p.read_text(encoding='utf-8')) for p in sorted(state.glob('*.json'))])

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
            if isinstance(s, dict) and s.get('url'):
                draft_sources.append({
                    'id': s.get('id') or uuid.uuid4().hex,
                    'title': s.get('title', s['url']),
                    'url': s['url'],
                    'resolved_url': s.get('resolved_url', s['url']),
                    'checked_at': s.get('checked_at', now()),
                    'sha256': s.get('sha256', hashlib.sha256(s['url'].encode()).hexdigest()),
                    'excerpt': s.get('excerpt', f"Sursă extrasă din {rel_posix}."),
                    'institution': s.get('institution', ''),
                    'source_region': s.get('source_region', '')
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
            'is_revision': is_rev,
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
        for p in state.glob('*.json'):
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
        url = data.get('url', '').strip()
        raw, mime, final_url = fetch(url)
        if 'pdf' in mime or raw.startswith(b'%PDF'):
            try:
                from pypdf import PdfReader
                reader = PdfReader(io.BytesIO(raw))
                text = '\n'.join(page.extract_text() or '' for page in reader.pages[:100])
            except ImportError:
                raise ValueError('Pentru PDF instalează dependențele din protocol_workbench/requirements.txt.')
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
            draft['sources'] = [s for s in draft['sources'] if s['url'] != url] + [source]
            save(draft)
        return jsonify(draft)

    @app.get('/api/images/search')
    def image_search():
        query = request.args.get('q', '').strip()
        if not query:
            raise ValueError('Introdu termenii pentru imagini.')
        data = remote_json('https://commons.wikimedia.org/w/api.php', {
            'action': 'query', 'generator': 'search', 'gsrsearch': query + ' filetype:bitmap',
            'gsrnamespace': 6, 'gsrlimit': 12, 'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'iiurlwidth': 500, 'format': 'json'})
        images = []
        for page in data.get('query', {}).get('pages', {}).values():
            info = page.get('imageinfo', [{}])[0]
            metadata = info.get('extmetadata', {})
            get = lambda key: plain(metadata.get(key, {}).get('value', ''))
            images.append({'url': info.get('url', ''), 'thumbnail': info.get('thumburl', info.get('url', '')),
                           'source_url': info.get('descriptionurl', ''), 'caption': page['title'],
                           'author': get('Artist'), 'license': get('LicenseShortName'), 'license_url': get('LicenseUrl')})
        return jsonify(images)

    @app.post('/api/drafts/<identifier>/images')
    def attach_image(identifier):
        data = request.form.to_dict() if request.files else request.get_json()
        for key in ('caption', 'author', 'license', 'source_url'):
            if not str(data.get(key, '')).strip():
                raise ValueError('Imaginea necesită legendă, autor, licență și sursă.')
        public_url(data['source_url'])
        if request.files:
            raw = request.files['file'].read(LIMIT + 1)
        else:
            raw = fetch(data['url'])[0]
        if len(raw) > LIMIT:
            raise ValueError('Imaginea este prea mare.')
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
        fm, body = frontmatter(draft['document'])
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
            fm['sources'] = [{k: v for k, v in s.items() if k != 'excerpt'} for s in draft['sources']]
            fm['workbench_review'] = {'reviewer': reviewer, 'reviewed_at': now(), 'draft_id': identifier,
                                       'clinical_review': True, 'image_review': True, 'rights_review': True}
            references = '\n\n## Surse și revizuire\n\n' + '\n'.join('- ' + html.escape(s['title']) + ' — <' + s['url'] + '>' for s in draft['sources'])
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
    args = parser.parse_args()
    create_app(args.repo).run(host='127.0.0.1', port=args.port, debug=False)
