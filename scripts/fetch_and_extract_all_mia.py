import urllib.request
import urllib.parse
import sys
import json
import fitz
import re
import time
import os

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://miaradmodalitywiki.powerappsportals.com'

# Load initial links
discovered = json.load(open('mia_discovered_links.json', encoding='utf-8'))

to_check = set()
for sec, val in discovered.items():
    for l in val.get('links', []):
        h = l.get('href', '').replace('\u200b', '').strip()
        to_check.add(h)

sub_pages = [
    '/CT-Organ-Specific-Protocols', '/CT-BRAIN', '/CT-SPINE', '/CT-HEAD-AND-NECK',
    '/CT-Angio-Chest-Body', '/CT-Angio-Neuro', '/CT-Abdomen-Pelvis',
    '/CTA-Chest-Abdomen-Pelvis-Aorta-Endograft', '/CT-CTA-Chest-Aorta-Endograft', '/CT-CTA-Abdomen-and-Pelvis-Aorta-Endograft'
]
to_check.update(sub_pages)

pdf_urls = set()
visited_pages = set()

print(f"Resolving {len(to_check)} candidate URLs...")

for path in sorted(to_check):
    clean = path.replace('\\', '/').replace('\u200b', '').strip()
    if not clean.startswith('/'):
        clean = '/' + clean
    if clean in visited_pages:
        continue
    visited_pages.add(clean)
    
    url = BASE + urllib.parse.quote(clean, safe='/:?=&')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            ct = resp.headers.get('Content-Type', '')
            data = resp.read()
            
        if 'application/pdf' in ct or data[:4] == b'%PDF':
            pdf_urls.add((clean, clean, data))
            print(f"  [DIRECT PDF] {clean} ({len(data)} bytes)")
        else:
            # HTML page, look for PDF links or sub-links
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(data.decode('utf-8', errors='ignore'), 'html.parser')
            for a in soup.find_all('a', href=True):
                href = a['href'].replace('\\', '/').replace('\u200b', '').strip()
                text = ' '.join(a.get_text().split())
                if any(x in text.lower() for x in ['download pdf', 'download worksheet', 'download form']) or href.endswith('.pdf') or 'pdf' in href.lower() or ('/' in href and not any(x in href.lower() for x in ['signin', 'register', 'account', '_services', 'javascript:', '#', '~/'])):
                    if not href.startswith('/'):
                        href = '/' + href
                    if any(x in text.lower() for x in ['download', 'form', 'worksheet', 'sheet']) or not href.startswith('/CT/') and not href.startswith('/MRI/') and not href.startswith('/US-Main/'):
                        # Test if this link is a PDF
                        sub_url = BASE + urllib.parse.quote(href, safe='/:?=&')
                        try:
                            req2 = urllib.request.Request(sub_url, headers={'User-Agent': 'Mozilla/5.0'})
                            with urllib.request.urlopen(req2, timeout=15) as resp2:
                                ct2 = resp2.headers.get('Content-Type', '')
                                data2 = resp2.read()
                            if 'application/pdf' in ct2 or data2[:4] == b'%PDF':
                                pdf_urls.add((href, text or href, data2))
                                print(f"    [FOUND PDF] {href} -> {text} ({len(data2)} bytes)")
                        except Exception as e:
                            pass
    except Exception as e:
        print(f"  [ERROR] {clean}: {e}")

print(f"\nExtracted {len(pdf_urls)} PDF documents in total.")

parsed_protocols = {}
for path, label, pdf_data in pdf_urls:
    try:
        doc = fitz.open(stream=pdf_data, filetype='pdf')
        pages_text = [page.get_text() for page in doc]
        full_text = "\n".join(pages_text)
        
        parsed_protocols[path] = {
            'path': path,
            'label': label,
            'pages_count': len(doc),
            'full_text': full_text,
            'text_lines': [line.strip() for line in full_text.splitlines() if line.strip()]
        }
    except Exception as e:
        print(f"Error parsing PDF for {path}: {e}")

os.makedirs('data', exist_ok=True)
with open('data/mia_extracted_protocols.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_protocols, f, indent=2, ensure_ascii=False)

print(f"Saved {len(parsed_protocols)} parsed protocols to data/mia_extracted_protocols.json!")
