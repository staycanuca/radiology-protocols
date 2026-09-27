import urllib.request
import urllib.parse
import sys
import json
import fitz
import time
import os

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://miaradmodalitywiki.powerappsportals.com'

# Read links from mia_full_crawl.json
full = json.load(open('mia_full_crawl.json', encoding='utf-8'))
all_downloads = {}
for page_path, page_data in full.items():
    if 'error' in page_data:
        continue
    for l in page_data.get('links', []):
        href = l.get('href', '').replace('\u200b', '').strip()
        text = l.get('text', '').replace('\u200b', '').strip()
        if href.startswith('\\') or any(x in text.lower() for x in ['download', 'worksheet', 'sheet', 'form']) or href.endswith('.pdf'):
            clean_href = href.replace('\\', '/').strip()
            if not clean_href.startswith('/'):
                clean_href = '/' + clean_href
            if clean_href not in all_downloads:
                all_downloads[clean_href] = {'from_page': page_path, 'text': text}

print(f"Total unique PDF targets to fetch: {len(all_downloads)}")

results = {}
for i, (path, meta) in enumerate(all_downloads.items(), 1):
    clean_p = path.replace('\u200b', '').strip()
    url = BASE + urllib.parse.quote(clean_p, safe='/:?=&')
    print(f"[{i}/{len(all_downloads)}] Fetching {clean_p}...", end=' ', flush=True)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        if data[:4] == b'%PDF':
            doc = fitz.open(stream=data, filetype='pdf')
            full_text = "\n".join(page.get_text() for page in doc)
            results[clean_p] = {
                'path': clean_p,
                'from_page': meta['from_page'],
                'label': meta['text'],
                'pages_count': len(doc),
                'full_text': full_text,
                'text_lines': [line.strip() for line in full_text.splitlines() if line.strip()]
            }
            print(f"OK ({len(doc)} pages)", flush=True)
        else:
            print("Not a PDF (HTML returned)", flush=True)
    except Exception as e:
        print(f"ERROR: {e}", flush=True)
    time.sleep(0.15)

os.makedirs('data', exist_ok=True)
with open('data/mia_extracted_protocols.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nFinished! Extracted {len(results)} PDF protocols into data/mia_extracted_protocols.json.")
