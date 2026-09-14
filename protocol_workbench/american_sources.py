"""Search public US institutional catalog links, without recursively crawling sites."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import threading
import time
import unicodedata
from urllib.parse import urljoin, urlparse, unquote


UT = 'https://www.utsouthwestern.edu/departments/radiology/protocols/'
CATALOGS = [
    {'id': 'utsw', 'name': 'UT Southwestern', 'kind': 'Protocol instituțional',
     'pages': {'ct': UT + 'ct.html', 'irm': UT + 'mr.html', 'eco': UT + 'us.html',
               'rx': UT + 'diagnostic.html', 'fluoro': UT + 'diagnostic.html'},
     'hosts': ['utsouthwestern.edu', 'utsw.edu'], 'pattern': r'/protocols/assets/.*\.pdf$'},
    {'id': 'ohsu', 'name': 'OHSU', 'kind': 'Protocol instituțional IRM',
     'pages': {'irm': 'https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols'},
     'hosts': ['ohsu.edu'], 'pattern': r'/(?:mr-|mri-)[^/]+protocol[^/]*$|/sites/default/files/.*\.pdf$'},
    {'id': 'aapm', 'name': 'AAPM', 'kind': 'Protocol / resursă tehnică CT',
     'pages': {'ct': 'https://www.aapm.org/pubs/ctprotocols/'},
     'hosts': ['aapm.org'], 'pattern': r'/pubs/ctprotocols/documents/.*\.pdf$'},
    {'id': 'aium', 'name': 'AIUM', 'kind': 'Parametru de practică US',
     'pages': {'eco': 'https://www.aium.org/resources/practice-parameters'},
     'hosts': ['aium.org', 'doi.org', 'onlinelibrary.wiley.com'],
     'pattern': r'/docs/.*\.pdf$|/10\.1002/|/10\.7863/|/doi/'},
]
PORTALS = [
    {'name': 'ACR — Appropriateness Criteria',
     'url': 'https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria',
     'description': 'Alegerea investigației în funcție de situația clinică. Consultare pe portalul ACR.'},
    {'name': 'ACR — Practice Parameters and Technical Standards',
     'url': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards',
     'description': 'Parametri de practică și standarde tehnice. Consultare pe portalul ACR.'},
]
# Limited, explicit anatomy aliases; queries are not translated by a clinical model.
ALIASES = {
    'genunchi': 'knee', 'torace': 'chest', 'craniu': 'head', 'creier': 'brain',
    'cerebral': 'brain', 'ficat': 'liver', 'renal': 'renal kidney', 'rinichi': 'kidney renal',
    'umar': 'shoulder', 'sold': 'hip', 'glezna': 'ankle', 'tiroida': 'thyroid',
    'san': 'breast', 'coloana': 'spine', 'bazin': 'pelvis', 'sinusuri': 'sinus',
    'esofag': 'esophagram esophagus', 'carotide': 'carotid',
    'pancreas': 'pancreas pancreatic', 'aorta': 'aorta aortic', 'bila': 'biliary gallbladder',
    'colecist': 'gallbladder biliary', 'vezica': 'bladder urinary', 'urinar': 'urinary urology bladder renal',
    'ureter': 'ureter urinary', 'cot': 'elbow', 'pumn': 'wrist', 'mana': 'hand wrist',
    'picior': 'foot ankle leg', 'coapsa': 'femur thigh', 'gamba': 'tibia fibula calf',
    'gat': 'neck cervical soft tissue', 'cervical': 'cervical neck spine', 'lombara': 'lumbar spine',
    'dorsala': 'thoracic spine', 'inima': 'cardiac heart', 'cardiac': 'cardiac heart',
    'pediatrie': 'pediatric peds child', 'pediatric': 'pediatric peds child', 'copil': 'pediatric peds child',
    'copii': 'pediatric peds child', 'orbita': 'orbit eye', 'stomac': 'stomach gastric',
    'intestin': 'bowel intestinal enterography', 'colon': 'colon colonography',
    'prostata': 'prostate', 'uter': 'uterus pelvic', 'ovare': 'ovary ovarian',
}
STOP = set('ct rx irm us mri mr protocol protocols protocoale protocolul imaging scan acquisition radiografie ecografie fluoroscopie flouro fluoro de si pentru cu fara contrast'.split())


def words(text):
    text = ''.join(c for c in unicodedata.normalize('NFKD', text.lower()) if not unicodedata.combining(c))
    return re.findall(r'[a-z0-9]+', text)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.href, self.label = [], None, []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.href = dict(attrs).get('href')
            self.label = []

    def handle_data(self, data):
        if self.href is not None:
            self.label.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.href is not None:
            self.links.append((self.href, ' '.join(' '.join(self.label).split())))
            self.href = None


def parse_catalog(raw, final_url, catalog):
    parser = Links()
    parser.feed(raw.decode('utf-8', errors='replace'))
    results, seen = [], set()
    for href, title in parser.links:
        url = urljoin(final_url, href).split('#')[0]
        parsed = urlparse(url)
        host = parsed.hostname or ''
        if parsed.scheme != 'https' or not any(host == h or host.endswith('.' + h) for h in catalog['hosts']):
            continue
        if not re.search(catalog['pattern'], unquote(parsed.path), re.I) or url in seen:
            continue
        seen.add(url)
        results.append({'title': title or unquote(parsed.path.rsplit('/', 1)[-1]), 'url': url,
                        'provider': catalog['name'], 'kind': catalog['kind'], 'country': 'US',
                        'catalog_url': final_url, 'year': '', 'authors': catalog['name'],
                        'summary': 'Document identificat în catalogul instituției. Deschide originalul pentru ediție, conținut și condiții de utilizare.'})
    return results


class AmericanSearch:
    def __init__(self, fetch, cache_dir=None):
        self.fetch, self.cache, self.lock = fetch, {}, threading.Lock()
        self.cache_dir = Path(cache_dir) if cache_dir else None
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            self._load_disk_cache()

    def _disk_cache_file(self):
        return self.cache_dir / 'catalogs_cache.json' if self.cache_dir else None

    def _load_disk_cache(self):
        f = self._disk_cache_file()
        if f and f.exists():
            try:
                data = json.loads(f.read_text(encoding='utf-8'))
                now_ts = time.time()
                for url, item in data.items():
                    if now_ts - item.get('saved_at', 0) < 86400:
                        self.cache[url] = (time.monotonic() - (now_ts - item['saved_at']), item['results'])
            except Exception:
                pass

    def _save_disk_cache(self):
        f = self._disk_cache_file()
        if not f:
            return
        try:
            data = {}
            now_ts = time.time()
            now_mono = time.monotonic()
            with self.lock:
                for url, (mono_ts, results) in self.cache.items():
                    elapsed = now_mono - mono_ts
                    data[url] = {'saved_at': now_ts - elapsed, 'results': results}
            f.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
        except Exception:
            pass

    def catalog(self, config, modality):
        url = config['pages'][modality]
        with self.lock:
            cached = self.cache.get(url)
        if cached and time.monotonic() - cached[0] < 3600:
            return cached[1]
        raw, mime, final_url = self.fetch(url)
        if 'html' not in mime:
            raise ValueError('Catalogul nu a returnat HTML.')
        results = parse_catalog(raw, final_url, config)
        if not results:
            raise ValueError('Nu au fost identificate documente; pagina poate necesita acces interactiv sau și-a schimbat structura.')
        checked = datetime.now(timezone.utc).isoformat()
        for result in results:
            result['catalog_checked_at'] = checked
        with self.lock:
            self.cache[url] = (time.monotonic(), results)
        self._save_disk_cache()
        return results

    def search(self, query, modality, institution='all'):
        if institution not in {'all', *(c['id'] for c in CATALOGS)}:
            raise ValueError('Instituție necunoscută.')
        configs = [c for c in CATALOGS if modality in c['pages'] and institution in ('all', c['id'])]
        groups = [set(words(ALIASES.get(w, w))) for w in words(query) if w not in STOP]
        results, statuses = [], []

        def get(config):
            try:
                entries = self.catalog(config, modality)
                return config, entries, None
            except Exception as exc:
                return config, [], str(exc)

        with ThreadPoolExecutor(max_workers=4) as pool:
            for config, entries, error in pool.map(get, configs):
                if not groups:
                    matches = list(entries)
                else:
                    exact_matches = []
                    partial_matches = []
                    for entry in entries:
                        haystack = set(words(entry['title'] + ' ' + unquote(urlparse(entry['url']).path.rsplit('/', 1)[-1])))
                        score = sum(1 for group in groups if group & haystack)
                        if score == len(groups):
                            exact_matches.append(entry)
                        elif len(groups) > 1 and score >= max(1, len(groups) - 1):
                            partial_matches.append((score, entry))
                    if len(exact_matches) < 25 and partial_matches:
                        partial_matches.sort(key=lambda x: -x[0])
                        exact_urls = {e['url'] for e in exact_matches}
                        combined = list(exact_matches)
                        for _, entry in partial_matches:
                            if entry['url'] not in exact_urls:
                                combined.append(entry)
                                exact_urls.add(entry['url'])
                        matches = combined
                    else:
                        matches = exact_matches
                results.extend(matches)
                statuses.append({'name': config['name'], 'url': config['pages'][modality], 'ok': error is None,
                                 'indexed': len(entries), 'matches': len(matches), 'error': error})
        results.sort(key=lambda r: (r['provider'], r['title'].lower()))
        return {'results': results[:100], 'total': len(results), 'catalogs': statuses, 'portals': PORTALS,
                'note': 'Căutare în titluri și nume de fișiere din cataloage SUA; nu în textul integral. '
                        'RX și fluoroscopia folosesc catalogul comun UT Southwestern. '
                        'Accesul public nu implică drept de republicare; revizuirea înainte de import rămâne obligatorie.'}


def provenance(url):
    host = urlparse(url).hostname or ''
    for config in CATALOGS:
        # DOI/Wiley hosting alone cannot identify the issuing institution.
        for domain in config['hosts']:
            if domain in ('doi.org', 'onlinelibrary.wiley.com'):
                continue
            if host == domain or host.endswith('.' + domain):
                return {'institution': config['name'], 'source_region': 'US'}
    if host == 'acr.org' or host.endswith('.acr.org'):
        return {'institution': 'ACR', 'source_region': 'US'}
    return {}
