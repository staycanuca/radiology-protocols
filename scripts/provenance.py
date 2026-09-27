"""Expose recorded provenance without treating references or imports as medical approval."""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import csv
from datetime import date, datetime
from html import escape
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urlencode, urlsplit

from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml

ROOT = Path(__file__).resolve().parents[1]
ENV = Environment(loader=FileSystemLoader(ROOT / 'overrides'),
                  autoescape=select_autoescape(['html']))
TEMPLATE = ENV.get_template('partials/provenance.html')
MODALITIES = {'ct', 'irm', 'rx', 'eco', 'fluoro', 'mn', 'ir'}
EDITORIAL_KEYS = {'sources', 'source_pages', 'source_sections', 'source_mapping',
                  'workbench_review', 'workbench_transfer', 'provenance',
                  'status', 'clinical_status', 'review_required_fields'}


def preserve_provenance_on_edit(original, edited):
    """Keep fields absent from the form and flag existing reviews after content edits."""
    result = dict(edited)
    for key in EDITORIAL_KEYS:
        if key in original:
            result[key] = deepcopy(original[key])
    changed = any(value != original.get(key) for key, value in edited.items()
                  if key not in EDITORIAL_KEYS | {'last_updated', 'author'})
    provenance = result.get('provenance')
    if changed and isinstance(provenance, dict) and (provenance.get('source_verification') or provenance.get('medical_review')):
        provenance['review_required'] = True
    return result


def text(value):
    if value is None or isinstance(value, (dict, list, bool)):
        return ''
    return ' '.join(str(value).split())


def values(value):
    return [text(item) for item in (value if isinstance(value, list) else [value]) if text(item)]


def recorded_date(value):
    try:
        if isinstance(value, datetime):
            parsed = value.date()
        elif isinstance(value, date):
            parsed = value
        else:
            parsed = datetime.fromisoformat(str(value).replace('Z', '+00:00')).date()
        return parsed.isoformat() if parsed <= date.today() else ''
    except (ValueError, TypeError):
        return ''


def safe_url(value):
    url = text(value)
    try:
        parsed = urlsplit(url)
        if parsed.scheme in {'https', 'http'} and parsed.hostname and not parsed.username and not parsed.password:
            return url
    except ValueError:
        pass
    return ''


def is_protocol(src_uri, meta):
    path = PurePosixPath(src_uri)
    return (path.parts[0] in MODALITIES and path.name not in {'index.md', 'compare.md'}
            and bool(meta.get('slug') or ('category' in meta and 'clinical_indications' in meta)))


def source_record(raw):
    source = raw if isinstance(raw, dict) else {'title': raw}
    title = text(source.get('title'))
    # Parse only explicit bibliographic text, never infer an edition from a publisher URL.
    edition = re.search(r'\b(?:Ed\.?|Edition|Ediția)\s*(\d+(?:/\d+)?)', title, re.I)
    pages = re.search(r'\b(?:Pagina|Pagini|Pages?|pp?\.)\s*([\d,\s–—-]+)', title, re.I)
    edition_text = text(source.get('edition')) or (edition[1] if edition else '')
    locator = text(source.get('section')) or text(source.get('chapter'))
    source_pages = ', '.join(values(source.get('pages'))) or (pages[1].strip() if pages else '')
    if source_pages:
        locator = ' · '.join(filter(None, [locator, 'Pagini: ' + source_pages]))
    return {
        'title': title or 'Titlu neprecizat', 'institution': text(source.get('institution')),
        'url': safe_url(source.get('url')), 'edition': edition_text,
        'edition_ambiguous': bool('/' in edition_text),
        'version': text(source.get('version')) or text(source.get('year')),
        'locator': locator, 'consulted_on': recorded_date(source.get('consulted_on')),
        'recorded_on': recorded_date(source.get('checked_at')),
        'relationship': text(source.get('relationship')),
        'has_title': bool(title),
    }


def review_record(raw, version, medical=False):
    record = raw if isinstance(raw, dict) else {}
    result = {'state': 'missing', 'label': 'Nedocumentată',
              'reviewer': text(record.get('reviewer')), 'date': recorded_date(record.get('reviewed_on')),
              'scope': text(record.get('scope')), 'qualification': text(record.get('qualification')),
              'version': text(record.get('version')), 'profile_url': safe_url(record.get('profile_url'))}
    if not record:
        return result
    complete = all(result[k] for k in ['reviewer', 'date', 'scope', 'version']) and bool(version)
    if medical:
        complete = complete and bool(result['qualification'])
    if complete and result['version'] != version:
        result.update(state='outdated', label='Înregistrată pentru altă versiune')
    elif complete:
        result.update(state='recorded', label='Înregistrată pentru versiunea curentă')
    else:
        result.update(state='incomplete', label='Înregistrare incompletă')
    return result


def build_provenance(meta, src_uri):
    if not is_protocol(src_uri, meta):
        return None
    raw = meta.get('provenance')
    editorial = raw if isinstance(raw, dict) else {}
    raw_sources = meta.get('sources') or []
    if not isinstance(raw_sources, list):
        raw_sources = [raw_sources]
    sources = [source_record(s) for s in raw_sources if s]
    version = text(editorial.get('version'))
    fidelity = review_record(editorial.get('source_verification'), version)
    medical = review_record(editorial.get('medical_review'), version, medical=True)
    if editorial.get('review_required') is True:
        for record in [fidelity, medical]:
            if record['state'] != 'missing':
                record.update(state='needs_review', label='De reverificat după modificare')
    legacy = meta.get('workbench_review') or {}
    legacy = legacy if isinstance(legacy, dict) else {}
    legacy_note = ''
    if legacy.get('clinical_review') is True:
        legacy_note = 'Există o înregistrare anterioară de revizuire în instrumentul de import.'
        if text(legacy.get('reviewer')):
            legacy_note += ' Identificator declarat: ' + text(legacy['reviewer']) + '.'
        if recorded_date(legacy.get('reviewed_at')):
            legacy_note += ' Data: ' + recorded_date(legacy['reviewed_at']) + '.'
        legacy_note += ' Competența, întinderea revizuirii și legătura cu versiunea curentă necesită documentare.'
        if medical['state'] == 'missing':
            medical.update(state='incomplete', label='Înregistrare anterioară incompletă')
    status = str(meta.get('clinical_status') or meta.get('status') or '').lower()
    publication = ('Ciornă — nu se utilizează clinic' if status == 'draft_not_for_clinical_use'
                   else 'Ciornă pentru revizuire' if status == 'draft'
                   else 'Retras / în reevaluare' if status in {'withdrawn', 'retired'} else '')
    gaps = []
    if not sources:
        gaps.append('missing_sources')
    if sources and any(not s['url'] for s in sources):
        gaps.append('missing_source_link')
    if sources and any(not s['locator'] for s in sources):
        gaps.append('missing_source_locator')
    if sources and any(not s['edition'] and not s['version'] for s in sources):
        gaps.append('missing_source_version')
    if any(s['edition_ambiguous'] for s in sources):
        gaps.append('ambiguous_edition')
    if sources and any(not s['relationship'] for s in sources):
        gaps.append('missing_source_relationship')
    if not editorial.get('processing'):
        gaps.append('missing_processing')
    if not editorial.get('adaptations'):
        gaps.append('missing_adaptations')
    if fidelity['state'] != 'recorded':
        gaps.append('source_verification_' + fidelity['state'])
    if medical['state'] != 'recorded':
        gaps.append('medical_review_' + medical['state'])
    return {
        'sources': sources, 'source_label': ('1 referință declarată' if len(sources) == 1 else f'{len(sources)} referințe declarate') if sources else 'Sursa exactă lipsește',
        'version': version, 'fidelity': fidelity, 'medical': medical, 'legacy_note': legacy_note,
        'publication': publication, 'processing': values(editorial.get('processing')),
        'adaptations': values(editorial.get('adaptations')), 'editor': text(editorial.get('editor')),
        'existing_attribution': text(meta.get('author')), 'source_pages': ', '.join(values(meta.get('source_pages'))),
        'updated': recorded_date(meta.get('last_updated')), 'gaps': gaps,
    }


def on_page_content(html, page, config, files):
    data = build_provenance(page.meta, page.file.src_uri)
    if data is None:
        return html
    page.meta['provenance_display'] = data
    base = config['site_url'].rstrip('/')
    links = {'methodology': base + '/despre-proiect/',
             'feedback': base + '/request-change/?' + urlencode({'protocol': page.meta.get('slug') or PurePosixPath(page.file.src_uri).stem})}
    card = TEMPLATE.render(provenance=data, links=links)
    heading = re.search(r'</h1\s*>', html, re.I)
    if heading:
        return html[:heading.end()] + card + html[heading.end():]
    return '<h1>' + escape(text(page.meta.get('title') or page.title)) + '</h1>' + card + html


def audit(docs_dir):
    rows = []
    for modality in sorted(MODALITIES):
        for path in sorted((docs_dir / modality).rglob('*.md')):
            content = path.read_text(encoding='utf-8')
            match = re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|$)', content, re.S)
            meta = (yaml.safe_load(match[1]) or {}) if match else {}
            src = path.relative_to(docs_dir).as_posix()
            data = build_provenance(meta, src)
            if data:
                rows.append({'path': src, 'title': text(meta.get('title')), 'modality': modality,
                             'source_count': len(data['sources']), 'sources': data['sources'],
                             'fidelity': data['fidelity']['state'], 'medical_review': data['medical']['state'],
                             'publication': data['publication'], 'gaps': data['gaps']})
    counts = Counter(gap for row in rows for gap in row['gaps'])
    return {'protocols': len(rows), 'with_sources': sum(bool(r['source_count']) for r in rows),
            'gaps': dict(sorted(counts.items())), 'by_modality': dict(Counter(r['modality'] for r in rows)),
            'note': 'Audit al metadatelor existente; nu verifică documentele externe sau validitatea medicală.',
            'records': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit', type=Path, default=ROOT / 'reports' / 'provenance-audit')
    args = parser.parse_args()
    report = audit(ROOT / 'docs')
    args.audit.parent.mkdir(parents=True, exist_ok=True)
    args.audit.with_suffix('.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with args.audit.with_suffix('.csv').open('w', encoding='utf-8-sig', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=['path', 'title', 'modality', 'source_count', 'fidelity', 'medical_review', 'publication', 'gaps'])
        writer.writeheader()
        for row in report['records']:
            writer.writerow({key: '; '.join(row[key]) if key == 'gaps' else row[key] for key in writer.fieldnames})
    print(json.dumps({key: value for key, value in report.items() if key != 'records'}, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()
