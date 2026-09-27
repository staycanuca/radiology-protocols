import urllib.request
import re
from bs4 import BeautifulSoup
import json
import time
import os
import sys

# Ensure UTF-8 output on Windows terminal
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_URL = "https://miaradmodalitywiki.powerappsportals.com"

discovered = set()
to_visit = [
    "/CT",
    "/MG",
    "/MRI",
    "/RF",
    "/US-Main/",
    "/X-RAY",
    "/Radiology_Results_and_Critical_Communications"
]

all_pages = {}

while to_visit:
    path = to_visit.pop(0)
    if path in discovered:
        continue
    discovered.add(path)
    
    # Normalize URL
    if path.startswith("http"):
        url = path
    else:
        if not path.startswith("/"):
            path = "/" + path
        url = BASE_URL + path
        
    print(f"Visiting [{len(discovered)}/{len(discovered)+len(to_visit)}]: {path}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        
        title = " ".join(soup.title.string.split()) if soup.title else ""
        main_content = soup.find(id="mainContent") or soup.find("main") or soup.find("body")
        
        # Extract headings
        headings = [" ".join(h.get_text().split()) for h in (main_content or soup).find_all(["h1", "h2", "h3", "h4"])]
        
        # Extract all links
        page_links = []
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            text = " ".join(a.get_text().split())
            if not href or href.startswith("#") or href.startswith("javascript:") or href == "~/":
                continue
            page_links.append({"href": href, "text": text})
            
            # If internal link under the portal and not visited, queue it
            clean_href = href.replace("\\", "/")
            if clean_href.startswith("/"):
                # Avoid search / login / account links
                if not any(x in clean_href.lower() for x in ["_services", "signin", "register", "login", "account", "profile"]):
                    if clean_href not in discovered and clean_href not in to_visit:
                        to_visit.append(clean_href)
                        
        # Extract tables if any (protocols often in tables)
        tables_data = []
        for table in (main_content or soup).find_all("table"):
            rows = []
            for tr in table.find_all("tr"):
                cells = [" ".join(td.get_text().split()) for td in tr.find_all(["td", "th"])]
                if cells:
                    rows.append(cells)
            if rows:
                tables_data.append(rows)
                
        # Extract text paragraphs
        paragraphs = [" ".join(p.get_text().split()) for p in (main_content or soup).find_all("p") if p.get_text().strip()]
        
        all_pages[path] = {
            "url": url,
            "title": title,
            "headings": headings,
            "links": page_links,
            "paragraphs": paragraphs[:20],
            "tables": tables_data,
            "raw_text_snippet": " ".join((main_content or soup).get_text().split())[:500]
        }
        time.sleep(0.3)
    except Exception as e:
        print(f"  Error on {path}: {e}")
        all_pages[path] = {"error": str(e), "url": url}

with open("mia_full_crawl.json", "w", encoding="utf-8") as f:
    json.dump(all_pages, f, indent=2, ensure_ascii=False)
    
print(f"\nCrawled {len(all_pages)} pages! Saved to mia_full_crawl.json")
