import urllib.request
import urllib.parse
import sys
import json
import fitz
import re
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://miaradmodalitywiki.powerappsportals.com'

# Load initial links
discovered = json.load(open('mia_discovered_links.json', encoding='utf-8'))

leaf_urls = set()
for sec, val in discovered.items():
    for l in val.get('links', []):
        h = l.get('href', '').replace('\u200b', '').strip()
        leaf_urls.add(h)

sub_pages = [
    '/CT-Organ-Specific-Protocols', '/CT-BRAIN', '/CT-SPINE', '/CT-HEAD-AND-NECK',
    '/CT-Angio-Chest-Body', '/CT-Angio-Neuro', '/CT-Abdomen-Pelvis',
    '/CTA-Chest-Abdomen-Pelvis-Aorta-Endograft', '/CT-CTA-Chest-Aorta-Endograft', '/CT-CTA-Abdomen-and-Pelvis-Aorta-Endograft'
]
leaf_urls.update(sub_pages)

print(f"Phase 1: Finding PDF download links across {len(leaf_urls)} pages...", flush=True)

def fetch_html_and_find_pdfs(path):
    clean = path.replace('\\', '/').replace('\u200b', '').strip()
    if not clean.startswith('/'):
        clean = '/' + clean
    url = BASE + urllib.parse.quote(clean, safe='/:?=&')
    pdf_targets = []
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            ct = resp.headers.get('Content-Type', '')
            data = resp.read()
        if 'application/pdf' in ct or data[:4] == b'%PDF':
            pdf_targets.append({'pdf_path': clean, 'label': clean, 'direct_data': data})
            return pdf_targets
        
        soup = BeautifulSoup(data.decode('utf-8', errors='ignore'), 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href'].strip()
            text = ' '.join(a.get_text().split())
            if not href or href == '~/' or href.startswith('#') or href.startswith('javascript:'):
                continue
            if 'download' in text.lower() or href.startswith('\\') or href.endswith('.pdf') or 'worksheet' in text.lower() or 'form' in text.lower():
                clean_href = href.replace('\\', '/').replace('\u200b', '').strip()
                if not clean_href.startswith('/'):
                    clean_href = '/' + clean_href
                pdf_targets.append({'pdf_path': clean_href, 'label': text or clean_href, 'direct_data': None})
    except Exception as e:
        # print(f"Error checking {path}: {e}", flush=True)
        pass
    return pdf_targets

all_found_pdfs = {}
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch_html_and_find_pdfs, u): u for u in leaf_urls}
    for future in as_completed(futures):
        for item in future.result():
            p = item['pdf_path']
            if p not in all_found_pdfs:
                all_found_pdfs[p] = item

print(f"\nPhase 1 Complete! Found {len(all_found_pdfs)} unique PDF protocol links.", flush=True)

print("Phase 2: Downloading & parsing PDF protocols...", flush=True)

def download_and_parse_pdf(item):
    p = item['pdf_path']
    label = item['label']
    data = item['direct_data']
    if data is None:
        url = BASE + urllib.parse.quote(p, safe='/:?=&')
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
        except Exception as e:
            return p, {'error': str(e), 'label': label}
            
    if data[:4] != b'%PDF':
        return p, {'error': 'Not a PDF file', 'label': label}
        
    try:
        doc = fitz.open(stream=data, filetype='pdf')
        pages_text = [page.get_text() for page in doc]
        full_text = "\n".join(pages_text)
        return p, {
            'path': p,
            'label': label,
            'pages_count': len(doc),
            'full_text': full_text,
            'text_lines': [line.strip() for line in full_text.splitlines() if line.strip()]
        }
    except Exception as e:
        return p, {'error': f'fitz parse error: {e}', 'label': label}

parsed_catalog = {}
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(download_and_parse_pdf, item): item for item in all_found_pdfs.values()}
    for future in as_completed(futures):
        path, result = future.result()
        parsed_catalog[path] = result
        if 'error' not in result:
            print(f"  [OK] {path} ({result['pages_count']} pages)", flush=True)
        else:
            print(f"  [SKIP] {path}: {result['error']}", flush=True)

os.makedirs('data', exist_ok=True)
with open('data/mia_extracted_protocols.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_catalog, f, indent=2, ensure_ascii=False)

valid_count = sum(1 for v in parsed_catalog.values() if 'error' not in v)
print(f"\nAll done! Successfully extracted {valid_count} PDF protocols into data/mia_extracted_protocols.json!", flush=True)
