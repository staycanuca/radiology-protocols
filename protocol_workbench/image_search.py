"""Federated, context-ranked image candidates; no claim of clinical suitability."""
from concurrent.futures import ThreadPoolExecutor
import re
from urllib.parse import urlsplit, unquote, urljoin
from .smart_extractor import normalize_text

MODALITIES = {'ct': ['ct', 'computed tomography'], 'rx': ['radiograph', 'radiography', 'x ray', 'xray'],
    'irm': ['mri', 'magnetic resonance'], 'eco': ['ultrasound', 'sonography', 'sonogram'],
    'fluoro': ['fluoroscopy', 'fluoroscopic', 'esophagram']}
TRANSLATIONS = {'torace': 'chest', 'craniu': 'head', 'cerebral': 'brain', 'genunchi': 'knee',
    'umar': 'shoulder', 'cot': 'elbow', 'pumn': 'wrist', 'glezna': 'ankle', 'sold': 'hip',
    'coloana': 'spine', 'cervicala': 'cervical', 'lombara': 'lumbar', 'toracala': 'thoracic',
    'ficat': 'liver', 'rinichi': 'kidney', 'tiroida': 'thyroid', 'san': 'breast',
    'radiografie': 'radiograph', 'irm': 'mri', 'ecografie': 'ultrasound', 'rx': 'radiograph',
    'pediatric': 'pediatric', 'copil': 'child', 'copii': 'children'}
STOP = {'protocol', 'protocolul', 'de', 'si', 'cu', 'pentru', 'the', 'of', 'and'}


def words(text):
    return [TRANSLATIONS.get(w, w) for w in re.findall(r'[a-z0-9]+', normalize_text(text)) if w not in STOP]


def contains(text, phrase):
    return bool(re.search(r'\b' + re.escape(phrase) + r'\b', text))


def rank_images(items, query, modality):
    terms = set(words(query))
    ranked, seen = [], set()
    for item in items:
        url = item.get('url', '')
        if not url.startswith('https://') or not item.get('source_url', '').startswith('https://'):
            continue
        identity = unquote(urlsplit(url)._replace(query='', fragment='').geturl()).lower()
        if identity in seen:
            continue
        text = ' '.join(words(item.get('caption', '') + ' ' + item.get('description', '')))
        hits = sorted(t for t in terms if contains(text, t))
        matches_modality = any(contains(text, t) for t in MODALITIES.get(modality, []))
        others = any(any(contains(text, t) for t in aliases) for mod, aliases in MODALITIES.items() if mod != modality)
        score = 10 * len(hits) + (16 if matches_modality else -12 if others and modality else 0)
        if terms and not hits and not matches_modality:
            continue
        reasons = ['Termeni: ' + ', '.join(hits)] if hits else []
        if matches_modality:
            reasons.append('Modalitate compatibilă')
        if item.get('license') and item.get('author'):
            score += 2
        if min(item.get('width') or 0, item.get('height') or 0) >= 500:
            score += 2
        if any(contains(text, t) for t in ['logo', 'scanner', 'equipment', 'machine']):
            score -= 15
        item = dict(item, score=score, relevance=reasons)
        ranked.append(item)
        seen.add(identity)
    return sorted(ranked, key=lambda x: (-x['score'], x['caption']))[:36]


def search_images(remote_json, plain, query, modality='', provider='all'):
    if provider not in ('all', 'commons', 'openverse', 'openi'):
        raise ValueError('Sursă de imagini necunoscută.')
    if modality and modality not in MODALITIES:
        raise ValueError('Modalitate necunoscută.')
    translated = ' '.join(dict.fromkeys(words(query)))[:240]
    aliases = MODALITIES.get(modality, [])
    effective = translated
    if aliases and not any(contains(translated, alias) for alias in aliases):
        effective += ' ' + aliases[0]

    def commons():
        data = remote_json('https://commons.wikimedia.org/w/api.php', {'action': 'query', 'generator': 'search',
            'gsrsearch': effective + ' filetype:bitmap', 'gsrnamespace': 6, 'gsrlimit': 40,
            'prop': 'imageinfo', 'iiprop': 'url|extmetadata|size|mime', 'iiurlwidth': 500, 'format': 'json'})
        if data.get('error'):
            raise ValueError('Wikimedia: ' + str(data['error'].get('info', 'eroare API')))
        result = []
        for page in data.get('query', {}).get('pages', {}).values():
            info = (page.get('imageinfo') or [{}])[0]
            if info.get('mime') and info['mime'] not in ('image/jpeg', 'image/png', 'image/webp'):
                continue
            metadata = info.get('extmetadata', {})
            get = lambda key: plain(metadata.get(key, {}).get('value', ''))
            result.append({'url': info.get('url', ''), 'thumbnail': info.get('thumburl', info.get('url', '')),
                'source_url': info.get('descriptionurl', ''), 'caption': page.get('title', '').removeprefix('File:'),
                'description': get('ImageDescription')[:1600], 'author': get('Artist'), 'license': get('LicenseShortName'),
                'license_url': get('LicenseUrl'), 'width': info.get('width'), 'height': info.get('height'), 'provider': 'Commons'})
        return result

    def openverse():
        data = remote_json('https://api.openverse.org/v1/images/', {'q': effective, 'page_size': 40})
        return [{'url': i.get('url', ''), 'thumbnail': i.get('thumbnail', ''),
            'source_url': i.get('foreign_landing_url', ''), 'caption': i.get('title') or 'Imagine',
            'description': ' '.join(t.get('name', '') for t in i.get('tags', [])),
            'author': i.get('creator') or '', 'license': ' '.join(filter(None, [i.get('license'), i.get('license_version')])),
            'license_url': i.get('license_url', ''), 'width': i.get('width'), 'height': i.get('height'),
            'provider': 'Openverse / ' + (i.get('source') or '')} for i in data.get('results', [])]

    def openi():
        base = 'https://openi.nlm.nih.gov'
        # The biomedical API can be slow for large result windows.
        data = remote_json(base + '/api/search', {'query': effective, 'm': 1, 'n': 6})
        found = []
        for entry in data.get('list', []):
            caption = plain((entry.get('image') or {}).get('caption') or entry.get('title', ''))
            pmcid = str(entry.get('pmcid', '')).removeprefix('PMC')
            landing = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC' + pmcid + '/' if pmcid.isdigit() else urljoin(base, entry.get('detailedQueryURL', '/'))
            if not entry.get('imgLarge'):
                continue
            found.append({'url': urljoin(base, entry['imgLarge']), 'thumbnail': urljoin(base, entry.get('imgThumbLarge') or entry['imgLarge']),
                'source_url': landing, 'caption': caption, 'description': plain(entry.get('title', '')),
                'author': entry.get('authors') or '', 'license': '', 'license_url': '', 'provider': 'NLM Open-i',
                'rights_note': 'Verifică licența articolului și drepturile figurii înainte de atașare.'})
        return found

    providers = {'commons': commons, 'openverse': openverse, 'openi': openi}
    selected = {name: providers[name] for name in ('commons', 'openi')} if provider == 'all' else {provider: providers[provider]}
    images, statuses = [], []
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs = {name: pool.submit(fn) for name, fn in selected.items()}
        for name, job in jobs.items():
            try:
                found = job.result()
                images.extend(found)
                statuses.append({'provider': name, 'count': len(found), 'error': None})
            except Exception as exc:
                statuses.append({'provider': name, 'count': 0, 'error': str(exc)})
    return {'results': rank_images(images, query, modality), 'providers': statuses, 'query': effective}
