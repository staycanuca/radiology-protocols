"""Build both search indexes from current files; keep page content untouched."""
from __future__ import annotations
import html
import hashlib
import json
import re
from pathlib import Path
try:
    from .search_catalog import collect, expand_aliases, normalize, strings, write_index
except ImportError:
    from search_catalog import collect, expand_aliases, normalize, strings, write_index

_page_synonyms = {}
_pages = {}
_records = {}
_valid_urls = None
_worker_name = None
_worker_source = None


def on_config(config):
    global _worker_name, _worker_source
    prelude = (Path(__file__).resolve().parents[1] / 'docs/javascripts/native-search-query.js').read_text(encoding='utf-8')
    worker = next((p for directory in config.theme.dirs for p in (Path(directory) / 'assets/javascripts/workers').glob('search.*.min.js')), None)
    if worker is None:
        raise RuntimeError('Material search worker not found; verify the installed theme before building.')
    _worker_source = prelude + '\n' + worker.read_text(encoding='utf-8')
    fingerprint = hashlib.sha256(_worker_source.encode('utf-8')).hexdigest()[:12]
    _worker_name = f'protocol-search.{fingerprint}.js'
    return config


def on_post_page(output, page, config):
    if not _worker_name: return output
    return re.sub(r'("search"\s*:\s*"[^"<>]*assets/javascripts/workers/)search\.[^"<>]+\.min\.js(")',
                  lambda m: m[1] + _worker_name + m[2], output)


def on_post_template(output, template_name, config):
    # Static templates such as 404.html do not emit on_post_page.
    return on_post_page(output, None, config)


def normalize_ro(text):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', str(text or '')) if not unicodedata.combining(c))


def on_pre_build(config):
    global _valid_urls
    _page_synonyms.clear()
    _pages.clear()
    _records.clear()
    _valid_urls = None


def on_files(files, config):
    global _valid_urls
    urls = {f.src_uri: f.url for f in files if f.is_documentation_page()}
    records, pages = collect(config['docs_dir'], urls)
    _pages.update(pages)
    _records.update({r['url']: r for r in records})
    _valid_urls = set(urls.values())
    return files


def on_page_content(html, page, config, files):
    meta = getattr(page, 'meta', {}) or {}
    url = getattr(page, 'url', '') or ''
    _pages[url] = meta
    _page_synonyms[url] = ' '.join(strings(meta.get('synonyms')))
    return html


def plain(value):
    return html.unescape(re.sub(r'<[^>]*>', ' ', str(value or '')))


def terms(value):
    return list(dict.fromkeys(re.findall(r'\w+', normalize(plain(value)))))


def enhance(data):
    docs = []
    for original in data.get('docs', []):
        doc = dict(original)
        location = doc.get('location', '')
        url, _, anchor = location.partition('#')
        meta = _pages.get(url, {})
        if _valid_urls is not None and url not in _valid_urls: continue
        if isinstance(meta.get('search'), dict) and meta['search'].get('exclude'): continue
        if anchor == 'protocol-provenance-title': continue
        title, body = plain(doc.get('title')), doc.get('text') or ''
        record = _records.get(url)
        metadata = []
        if not anchor:
            metadata.extend(strings(meta.get('synonyms')))
            metadata.extend(strings(meta.get('tags')))
            if record:
                for key in ('modality', 'category_label', 'segment', 'aliases', 'sources', 'source_terms', 'equipment', 'synonyms'):
                    metadata.extend(strings(record.get(key)))
        tags = terms(' '.join([title, *metadata, *expand_aliases(title)]))
        doc['keywords'] = ' '.join(t for t in tags if len(t) > 1 and t not in {'amp', 'quot', 'apos', 'nbsp', 'si', 'de', 'cu', 'la'})
        doc['title_terms'] = ' '.join(terms(title + ' ' + ' '.join(expand_aliases(title))))
        # Generated keywords are indexed fields, not hundreds of visible tag chips.
        if meta.get('tags'):
            doc['tags'] = [html.escape(t) for t in strings(meta['tags'])]
        else:
            doc.pop('tags', None)
        existing = set(re.findall(r'\w+', plain(body).lower()))
        additions = [word for word in terms(title + ' ' + body) if word not in existing]
        doc['text'] = body + ('\n' + ' '.join(additions) if additions else '')
        if not record and url and url.count('/') <= 2 and any(url.startswith(m + '/') for m in ('rx','ct','irm','eco','fluoro')):
            doc.setdefault('boost', 0.25)
        docs.append(doc)
    data['docs'] = docs
    return data


def on_post_build(config):
    site = Path(config['site_dir'])
    if _valid_urls is not None:
        write_index(site / 'javascripts/omnisearch-index.json', list(_records.values()))
    path = site / 'search/search_index.json'
    if not path.exists(): return
    data = enhance(json.loads(path.read_text(encoding='utf-8')))
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    temporary.replace(path)
    if _worker_name and _worker_source:
        worker = site / 'assets/javascripts/workers' / _worker_name
        worker.parent.mkdir(parents=True, exist_ok=True)
        worker.write_text(_worker_source, encoding='utf-8')
