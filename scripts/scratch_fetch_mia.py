import urllib.request
import re
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://miaradmodalitywiki.powerappsportals.com"

sections = [
    "/CT",
    "/MG",
    "/MRI",
    "/RF",
    "/US-Main/",
    "/X-RAY",
    "/Radiology_Results_and_Critical_Communications"
]

results = {}

for sec in sections:
    url = BASE_URL + sec
    print(f"\nFetching {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        
        title = " ".join(soup.title.string.split()) if soup.title else "No Title"
        h1s = [" ".join(h.get_text().split()) for h in soup.find_all(["h1", "h2", "h3"])]
        
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            text = " ".join(a.get_text().split())
            if href and not href.startswith("#") and not href.startswith("javascript:") and href != "~/":
                links.append({"href": href, "text": text})
                
        # Also check for tables or lists
        tables = len(soup.find_all("table"))
        cards = len(soup.find_all(class_=re.compile(r"card", re.I)))
        
        results[sec] = {
            "title": title,
            "headings": h1s[:15],
            "links": links,
            "tables": tables,
            "cards": cards,
            "html_length": len(html)
        }
        print(f"  Headings: {len(h1s)}, Links: {len(links)}, Tables: {tables}, Cards: {cards}")
        for l in links[:10]:
            print(f"    {l['href']} -> {l['text']}")
            
        time.sleep(0.5)
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        results[sec] = {"error": str(e)}

with open("mia_sections.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print("\nSaved all to mia_sections.json")
