"""Build a shared, source-aware AI catalog directly from the current protocol pages."""
import json
from pathlib import Path

try:
    from .provenance import build_provenance
except ImportError:
    from provenance import build_provenance

_records = {}
_valid_urls = set()
DETAIL_FIELDS = ('position', 'patient_prep', 'npo', 'contrast', 'tech_params', 'series',
                 'recons', 'sequences', 'coils_hardware', 'centering', 'breathing',
                 'sid_dff', 'standard_views', 'transducers_equipment', 'technical_settings',
                 'acquisition_steps', 'fluoro_params', 'quality_criteria', 'safety',
                 'safety_considerations', 'contraindications', 'radiation_safety')


def catalog_record(meta, src_uri, url):
    provenance = build_provenance(meta, src_uri)
    if not provenance:
        return None
    return {
        'title': str(meta.get('title') or Path(src_uri).stem), 'url': url,
        'modality': src_uri.split('/')[0], 'category': str(meta.get('category') or ''),
        'indications': meta.get('clinical_indications') or [], 'synonyms': meta.get('synonyms') or [],
        'details': {key: meta[key] for key in DETAIL_FIELDS if meta.get(key)},
        'sources': [{key: source[key] for key in ('title', 'url', 'edition', 'locator', 'relationship')}
                    for source in provenance['sources']],
        'review': {'fidelity': provenance['fidelity']['label'], 'medical': provenance['medical']['label'],
                   'publication': provenance['publication'], 'updated': provenance['updated'],
                   'version': provenance['version']},
    }


def on_pre_build(config):
    _records.clear()


def on_files(files, config):
    _valid_urls.clear()
    _valid_urls.update(f.url for f in files if f.is_documentation_page())


def on_page_markdown(markdown, page, config, files):
    record = catalog_record(page.meta, page.file.src_uri, page.url)
    if record:
        _records[page.file.src_uri] = record
    return markdown


def on_post_build(config):
    target = Path(config['site_dir']) / 'javascripts' / 'ai-library.json'
    # A dirty build may skip unchanged pages; retain their entries, replacing changed ones.
    if target.exists():
        previous = json.loads(target.read_text(encoding='utf-8'))
        by_url = {record['url']: record for record in previous.get('protocols', []) if record['url'] in _valid_urls}
    else:
        by_url = {}
    by_url.update({record['url']: record for record in _records.values()})
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({'schema_version': 1, 'protocols': sorted(by_url.values(), key=lambda r: r['url'])},
                                ensure_ascii=False, separators=(',', ':'), default=str), encoding='utf-8')


_live_cache = {}


def search_catalog(query, mode='all'):
    """Read current front matter, with an mtime cache so edits invalidate records."""
    import re
    import unicodedata
    import yaml
    from urllib.parse import urljoin
    if mode == 'iris':
        return []
    def norm(text):
        return ''.join(c for c in unicodedata.normalize('NFD', str(text).lower()) if not unicodedata.combining(c))
    stop = set('ce care cum este sunt pentru despre protocol protocoale examinare cauta arata explica vreau din dupa sau si de la cu pe in sa un o ct irm rmn mri rx eco us radiografie ecografie fluoroscopie'.split())
    words = [w for w in re.findall(r'[a-z0-9]+', norm(query)) if len(w) > 1 and w not in stop]
    if not words:
        return []
    root = Path(__file__).resolve().parent.parent / 'docs'
    scored = []
    for modality in ('ct', 'irm', 'rx', 'eco', 'fluoro'):
        if mode != 'all' and mode != modality:
            continue
        for path in (root / modality).rglob('*.md'):
            stamp = path.stat().st_mtime_ns
            cached = _live_cache.get(path)
            if not cached or cached[0] != stamp:
                raw = path.read_text(encoding='utf-8-sig')
                pieces = raw.split('---', 2)
                meta = yaml.safe_load(pieces[1]) if raw.startswith('---') and len(pieces) == 3 else {}
                uri = path.relative_to(root).as_posix()
                record = catalog_record(meta or {}, uri, urljoin('https://protocoale.co.uk/', uri[:-3] + '/'))
                _live_cache[path] = (stamp, record)
            record = _live_cache[path][1]
            if not record:
                continue
            title = norm(record['title'])
            haystack = norm([record['title'], record['category'], record['indications'], record['synonyms']])
            hits = [w for w in words if w in haystack]
            if hits:
                score = len(hits) / len(words) * 30 + sum(12 if w in title else 2 for w in hits)
                scored.append((score, record))
    scored.sort(key=lambda item: (-item[0], item[1]['title']))
    return [dict(record) for _, record in scored[:5]]
