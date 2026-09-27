import urllib.request
import urllib.parse
import sys
import json
import fitz
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

catalog = json.load(open('data/medford_catalog.json', encoding='utf-8'))

# Map url to metadata
url_meta = {}
for sec, items in catalog.items():
    for it in items:
        u = it['url']
        if u.endswith('.pdf') or 'pdf' in u.lower():
            if u not in url_meta:
                url_meta[u] = {'url': u, 'title': it['title'], 'sections': [sec]}
            else:
                if sec not in url_meta[u]['sections']:
                    url_meta[u]['sections'].append(sec)

print(f"Total unique PDF documents to process: {len(url_meta)}", flush=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_and_parse(item):
    u = item['url']
    title = item['title']
    sections = item['sections']
    
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            
        if data[:4] != b'%PDF':
            return u, {'error': 'Not a PDF', 'title': title, 'sections': sections}
            
        doc = fitz.open(stream=data, filetype='pdf')
        pages_text = [page.get_text() for page in doc]
        full_text = "\n".join(pages_text)
        
        return u, {
            'url': u,
            'title': title,
            'sections': sections,
            'pages_count': len(doc),
            'full_text': full_text,
            'text_lines': [line.strip() for line in full_text.splitlines() if line.strip()]
        }
    except Exception as e:
        return u, {'error': str(e), 'title': title, 'sections': sections}

results = {}
count = 0
total = len(url_meta)

with ThreadPoolExecutor(max_workers=6) as executor:
    futures = {executor.submit(fetch_and_parse, item): item for item in url_meta.values()}
    for future in as_completed(futures):
        u, res = future.result()
        results[u] = res
        count += 1
        if count % 20 == 0 or count == total:
            ok = sum(1 for v in results.values() if 'error' not in v)
            err = sum(1 for v in results.values() if 'error' in v)
            print(f"[{count}/{total}] Downloaded: {ok} OK, {err} errors", flush=True)

os.makedirs('data', exist_ok=True)
with open('data/medford_extracted_protocols.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

valid_count = sum(1 for v in results.values() if 'error' not in v)
print(f"\nCompleted! Successfully extracted {valid_count} PDF protocols into data/medford_extracted_protocols.json", flush=True)
