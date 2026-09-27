"""Inventory MCB modality catalogs and download explicitly selected documents."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import requests
from bs4 import BeautifulSoup
import fitz

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/mcb-modalities'
BASE = 'https://ref.mcbradiology.com/'
PREFIX = 'Protocols,%20Policies,%20Worksheets%20&%20Forms/'
SEEDS = [PREFIX + x for x in ['CT/CT.html', 'Xray/Xray.html', 'US/US.html']] + ['Breast/Breast.html', 'IR/IR.html', 'DEXA/DEXA.html', 'Nucs/Nucs.html']

def get(url):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r

def inventory():
    DATA.mkdir(parents=True, exist_ok=True)
    pending = {BASE + p for p in SEEDS}
    seen, pages, documents = set(), [], {}
    while pending:
        batch = sorted(pending - seen)
        if not batch:
            break
        pending = set()
        def read(url):
            try:
                response = get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                links = []
                for a in soup.select('a[href]'):
                    label = a.get_text(' ', strip=True)
                    href = urljoin(url, a['href']).split('#')[0]
                    if label and urlsplit(href).hostname == 'ref.mcbradiology.com':
                        links.append({'label': label, 'url': href})
                return {'url': url, 'title': soup.title.get_text() if soup.title else '', 'links': links}
            except Exception as exc:
                return {'url': url, 'error': str(exc), 'links': []}
        with ThreadPoolExecutor(max_workers=5) as pool:
            results = list(pool.map(read, batch))
        for page in results:
            seen.add(page['url'])
            pages.append(page)
            for link in page['links']:
                path = unquote(urlsplit(link['url']).path)
                if '/MRI/' in path:
                    continue
                if path.lower().endswith(('.html', '.htm')) and link['url'] not in seen:
                    pending.add(link['url'])
                elif path.lower().endswith(('.pdf', '.doc', '.docx', '.xlsx', '.xls')):
                    doc = documents.setdefault(link['url'], {'url': link['url'], 'labels': [], 'catalogs': []})
                    if link['label'] not in doc['labels']: doc['labels'].append(link['label'])
                    if page['url'] not in doc['catalogs']: doc['catalogs'].append(page['url'])
        print(f'Pages {len(seen)}, documents {len(documents)}', flush=True)
    (DATA / 'inventory.json').write_text(json.dumps({'pages': pages, 'documents': list(documents.values())}, ensure_ascii=False, indent=2), encoding='utf-8')

def download():
    selected = json.loads((DATA / 'selection.json').read_text(encoding='utf-8'))
    def fetch(record):
        filename = hashlib.sha256(record['url'].encode()).hexdigest()[:16] + '.pdf'
        target = DATA / 'pdfs' / filename
        target.parent.mkdir(exist_ok=True)
        try:
            if not target.exists():
                content = get(record['url']).content
                if not content.startswith(b'%PDF'): raise ValueError('Not a PDF')
                target.write_bytes(content)
            record['file'] = 'pdfs/' + filename
            record['sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
        except Exception as exc:
            record['error'] = str(exc)
        return record
    with ThreadPoolExecutor(max_workers=5) as pool:
        records = list(pool.map(fetch, selected))
    for record in records:
        if 'file' in record:
            with fitz.open(DATA / record['file']) as pdf:
                record['pages'] = [p.get_text(sort=True) for p in pdf]
    (DATA / 'manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'downloaded':sum('file' in r for r in records), 'errors':[{'url':r['url'],'error':r['error']} for r in records if 'error' in r]}, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--download', action='store_true')
    args = parser.parse_args()
    download() if args.download else inventory()
