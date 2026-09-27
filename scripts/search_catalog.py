"""Current metadata shared by Omnisearch and Material's native search hook."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
import yaml

try:
    from .provenance import build_provenance
except ImportError:
    from provenance import build_provenance

ROOT = Path(__file__).resolve().parents[1]
MODALITIES = ('ct', 'irm', 'rx', 'eco', 'fluoro', 'mn', 'ir')
ALIASES = json.loads((ROOT / 'data/search-aliases.json').read_text(encoding='utf-8'))
REGIONS = {
    'abdomen': 'Abdomen și pelvis', 'chest': 'Torace', 'cardiac': 'Cardiac', 'neuro': 'Cap și neurologie',
    'spine': 'Coloană', 'upper': 'Membru superior', 'lower': 'Membru inferior', 'msk': 'Musculoscheletic',
    'breast': 'Sân și mamografie', 'soft': 'Părți moi și endocrin', 'vascular': 'Vascular',
    'pediatrie': 'Pediatrie', 'trauma': 'Traumă', 'urinary': 'Aparat urinar',
    'interventional': 'Intervențional / C-arm', 'general': 'Alte categorii',
    'pulmonar': 'Pulmonar', 'digestiv': 'Digestiv', 'osos': 'Sistem osos',
    'endocrin': 'Endocrin', 'oncologie': 'Oncologie', 'infectie': 'Infecții',
}


def normalize(value):
    return ''.join(c for c in unicodedata.normalize('NFD', str(value or '').lower()) if not unicodedata.combining(c))


def strings(value):
    if value is None:
        return []
    if isinstance(value, dict):
        return [s for v in value.values() for s in strings(v)]
    if isinstance(value, list):
        return [s for v in value for s in strings(v)]
    return [' '.join(str(value).split())] if str(value).strip() else []


def read_metadata(path):
    raw = path.read_text(encoding='utf-8-sig')
    match = re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|$)', raw, re.S)
    meta = yaml.safe_load(match[1]) if match else {}
    return meta if isinstance(meta, dict) else {}


def navigation_segments(directory):
    path = directory / '.pages'
    data = yaml.safe_load(path.read_text(encoding='utf-8')) if path.exists() else {}
    data = data if isinstance(data, dict) else {}
    found = {}
    def visit(items, labels=()):
        for item in items if isinstance(items, list) else []:
            if isinstance(item, str) and item.endswith('.md'):
                found[item] = ' / '.join(labels)
            elif isinstance(item, dict):
                for label, children in item.items():
                    visit(children, (*labels, str(label)))
    visit(data.get('nav'))
    return str(data.get('title') or directory.name.replace('-', ' ').title()), found


def region_for(category):
    c = normalize(category)
    if 'membru-superior' in c: return 'upper'
    if 'membru-inferior' in c: return 'lower'
    if 'coloana' in c or 'spine' in c: return 'spine'
    if c in ('san', 'mamografie'): return 'breast'
    if 'parti-moi' in c or 'endocrin' in c: return 'soft'
    if 'pediatr' in c: return 'pediatrie'
    if 'trauma' in c: return 'trauma'
    if 'urinar' in c: return 'urinary'
    if 'c-arm' in c: return 'interventional'
    if any(k in c for k in ('cardiac', 'coronar')): return 'cardiac'
    if any(k in c for k in ('vascul', 'aorta', 'angio')): return 'vascular'
    if any(k in c for k in ('torac', 'chest', 'pulmon')): return 'chest'
    if any(k in c for k in ('abdom', 'pelvis', 'digestiv')): return 'abdomen'
    if any(k in c for k in ('neuro', 'craniu', 'cerebr')): return 'neuro'
    if any(k in c for k in ('msk', 'musculoschelet', 'locomotor')): return 'msk'
    return 'general'


def contrast_state(meta):
    """Search labels reflect explicit metadata, not inferred clinical technique."""
    kind = normalize(meta.get('protocol_type'))
    title = normalize(meta.get('title'))
    contrast = meta.get('contrast')
    agent = normalize(contrast.get('agent')) if isinstance(contrast, dict) else normalize(contrast)
    if any(term in agent for term in ('optional', 'la indicatie', 'dupa caz', 'in functie', 'daca')):
        return 'variable'
    if re.search(r'nativ.*(?:si cu|\+|post).*contrast|with and without|cu si fara', title):
        return 'variable'
    title_native = bool(re.search(r'\bnon[- ]contrast\b|without (?:iv )?contrast|fara (?:substanta de )?contrast', title))
    native = title_native or kind in ('native', 'non-contrast', 'noncontrast') or bool(re.search(r'\b(fara|none|no contrast|nativ|nu se administreaza)\b', agent))
    unknown = not re.search(r'[a-z0-9]', agent) or bool(re.search(r'neprecizat|nespecificat|not specified|^n/a$|^na$', agent))
    enhanced = kind == 'contrast-enhanced' or bool(not unknown and not native)
    if native and kind == 'contrast-enhanced': return 'variable'
    if native: return 'native'
    if enhanced: return 'contrast'
    return 'unknown'


def expand_aliases(text):
    words = ' ' + re.sub(r'[^a-z0-9]+', ' ', normalize(text)).strip() + ' '
    result = []
    for group in ALIASES:
        if any(' ' + re.sub(r'[^a-z0-9]+', ' ', normalize(term)).strip() + ' ' in words for term in group):
            result.extend(group)
    return list(dict.fromkeys(result))


def source_family(title):
    value = normalize(title)
    for key, label in [('clark', 'Clark'), ('merrill', 'Merrill'), ('bontrager', 'Bontrager'),
                       ('dartmouth', 'Dartmouth'), ('ohsu', 'OHSU'), ('radiopaedia', 'Radiopaedia'),
                       ('radiology assistant', 'Radiology Assistant'), ('mcb', 'MCB Radiology'),
                       ('mia', 'MIA Radiology'), ('medford', 'Medford Radiology'),
                       ('mrg', 'Medford Radiology')]:
        if key in value: return label
    return title


def record_for(meta, uri, url, category_label='', segment=''):
    provenance = build_provenance(meta, uri)
    search = meta.get('search') or {}
    if not provenance or (isinstance(search, dict) and search.get('exclude')):
        return None
    source_titles = [s['title'] for s in provenance['sources'] if s['has_title']]
    source_terms = [s for source in provenance['sources'] for s in strings({k: source[k] for k in ('title', 'edition', 'locator')})]
    title = ' '.join(str(meta.get('title') or Path(uri).stem).split())
    category = str(meta.get('category') or Path(uri).parent.name)
    modality = uri.split('/')[0]
    synonyms = strings(meta.get('synonyms'))
    indications = strings(meta.get('clinical_indications'))
    # Equipment is independent of authorship and bibliographic origin.
    equipment = strings(meta.get('scanner')) + strings(meta.get('equipment')) + strings(meta.get('coils_hardware', {}).get('field_strength') if isinstance(meta.get('coils_hardware'), dict) else None)
    match = re.search(r'\(([^)]+)\)$', title)
    if match and re.search(r'canon|siemens|philips|toshiba|aquilion|ge |lightspeed|brilliance|discovery', normalize(match[1])):
        equipment.append(match[1])
    aliases = expand_aliases(' '.join([title, modality, category_label, segment, *synonyms, *source_titles]))
    return {'title': title, 'url': url, 'slug': str(meta.get('slug') or Path(uri).stem),
            'modality': modality, 'category': category, 'category_label': category_label or category,
            'region': region_for(category), 'segment': segment, 'contrast': contrast_state(meta),
            'equipment': list(dict.fromkeys(equipment)), 'indications': indications, 'synonyms': synonyms,
            'aliases': aliases, 'title_aliases': expand_aliases(title), 'sources': source_titles, 'source_terms': source_terms,
            'source_filters': list(dict.fromkeys(source_family(s) for s in source_titles)),
            'publication': provenance['publication'], 'medical_review': provenance['medical']['label'],
            'fidelity': provenance['fidelity']['label'], 'updated': str(meta.get('last_updated') or '')}


def collect(docs_dir, urls=None):
    root = Path(docs_dir)
    records, pages, navigation = [], {}, {}
    paths = [root / uri for uri in urls] if urls is not None else sorted(root.rglob('*.md'))
    for path in paths:
        if not path.is_file(): continue
        uri = path.relative_to(root).as_posix()
        meta = read_metadata(path)
        url = urls[uri] if urls is not None else (uri[:-8] if uri.endswith('index.md') else uri[:-3] + '/')
        pages[url] = meta
        if uri.split('/')[0] not in MODALITIES: continue
        if path.parent not in navigation: navigation[path.parent] = navigation_segments(path.parent)
        label, segments = navigation[path.parent]
        record = record_for(meta, uri, url, label, segments.get(path.name, ''))
        if record: records.append(record)
    records.sort(key=lambda r: (r['modality'], normalize(r['title']), r['url']))
    return records, pages


def write_index(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps({'schema_version': 2, 'regions': REGIONS, 'protocols': records},
                                    ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    temporary.replace(path)
