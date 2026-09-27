"""Fetch the linked MCB MRI PDFs and preserve an auditable local source snapshot."""
from __future__ import annotations

import hashlib
import json
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit

import requests
from bs4 import BeautifulSoup
import fitz

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'data' / 'mcb-mri'
BASE = 'https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/'
GROUPS = ['Body', 'Neuro', 'MSK', 'Breast', 'Vascular & IR']


def fetch():
    CACHE.mkdir(parents=True, exist_ok=True)
    records = {}
    for group in GROUPS:
        url = BASE + quote(group + ' MRI Protocols.html')
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        (CACHE / (group.replace(' & ', '-') + '.html')).write_text(response.text, encoding='utf-8')
        for link in BeautifulSoup(response.content, 'html.parser').select('a[href]'):
            label = link.get_text(' ', strip=True)
            href = urljoin(url, link['href'])
            if not label or not urlsplit(href).path.lower().endswith('.pdf') or 'COMBINED' in label:
                continue
            record = records.setdefault(href, {'url': href, 'labels': [], 'catalogs': []})
            if label not in record['labels']:
                record['labels'].append(label)
            if group not in record['catalogs']:
                record['catalogs'].append(group)

    def download(record):
        rel = unquote(record['url'][len(BASE):])
        path = CACHE / rel
        try:
            response = requests.get(record['url'], timeout=90)
            response.raise_for_status()
            if not response.content.startswith(b'%PDF'):
                raise ValueError('Response is not a PDF')
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(response.content)
            record['file'] = rel
            record['sha256'] = hashlib.sha256(response.content).hexdigest()
        except Exception as exc:
            record['error'] = str(exc)
        return record

    with ThreadPoolExecutor(max_workers=6) as pool:
        result = list(pool.map(download, records.values()))
    (CACHE / 'manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'downloaded': sum('file' in r for r in result), 'errors': [r for r in result if 'error' in r]}, indent=2))


def extract():
    manifest = CACHE / 'manifest.json'
    records = json.loads(manifest.read_text(encoding='utf-8'))
    # PyMuPDF must run sequentially: its table finder shares process state.
    for record in records:
        rel = unquote(record['url'][len(BASE):])
        path = CACHE / rel
        if not path.exists():
            continue
        with fitz.open(path) as doc:
            record['pages'] = [page.get_text(sort=True) for page in doc]
            record['tables'] = [[table.extract() for table in page.find_tables().tables] for page in doc]
        record['file'] = rel
        record['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        record.pop('error', None)
    manifest.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Extracted {sum('file' in r for r in records)} PDFs")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract-only', action='store_true')
    args = parser.parse_args()
    if not args.extract_only:
        fetch()
    extract()
