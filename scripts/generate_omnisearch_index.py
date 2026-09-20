#!/usr/bin/env python3
"""generate_omnisearch_index.py — Generare index complet de căutare pentru OmniSearch (Opțiunea 1).

Scanează toate modalitățile (CT, IRM, RX, ECO, FLUORO) și produce
docs/javascripts/omnisearch-index.json pentru căutare și filtrare instantanee în browser.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = REPO_ROOT / "docs" / "javascripts" / "omnisearch-index.json"

MODALITIES = [
    ("ct", REPO_ROOT / "docs" / "ct"),
    ("irm", REPO_ROOT / "docs" / "irm"),
    ("rx", REPO_ROOT / "docs" / "rx"),
    ("eco", REPO_ROOT / "docs" / "eco"),
    ("fluoro", REPO_ROOT / "docs" / "fluoro"),
]

def parse_frontmatter(content: str) -> dict:
    if not content.startswith("---"):
        return {}
    end = content.find("\n---\n", 3)
    if end == -1:
        end = content.find("\n---", 3)
        if end == -1:
            return {}
    try:
        return yaml.safe_load(content[3:end]) or {}
    except Exception:
        return {}

def normalize_category(cat: str) -> str:
    c = str(cat).lower().strip()
    if any(k in c for k in ["cardiac", "cord", "coronar"]):
        return "cardiac"
    elif any(k in c for k in ["vascul", "aorta", "angio"]):
        return "vascular"
    elif any(k in c for k in ["torac", "chest", "pulmon"]):
        return "chest"
    elif any(k in c for k in ["abdom", "pelvis", "digestiv"]):
        return "abdomen"
    elif any(k in c for k in ["neuro", "craniu", "cerebr", "cap", "gat", "coloana", "spine"]):
        return "neuro"
    elif any(k in c for k in ["msk", "locomotor", "articul", "os", "membru", "musculo"]):
        return "msk"
    elif any(k in c for k in ["trauma", "urgent"]):
        return "trauma"
    elif any(k in c for k in ["pediatr"]):
        return "pediatrie"
    return c or "general"

def extract_scanner_or_author(title: str, author: str, fm: dict) -> str:
    # Check scanner in title (e.g. "Canon AquilionOne", "Siemens Definition", "Philips Brilliance")
    match = re.search(r"\(([^)]+)\)$", title)
    if match:
        return match.group(1).strip()
    if author and author != "Departamentul de Radiologie":
        return author
    return "Standard"

def generate_omnisearch_index() -> None:
    print(">>> Generare index OmniSearch (omnisearch-index.json)...")
    protocols = []
    
    for mod_name, mod_dir in MODALITIES:
        if not mod_dir.exists():
            continue
            
        for f in mod_dir.rglob("*.md"):
            if f.name in ("index.md", "compare.md", "radioprotectie.md"):
                continue
                
            try:
                content = f.read_text(encoding="utf-8")
                fm = parse_frontmatter(content)
                if not fm:
                    continue
                    
                title = fm.get("title", f.stem)
                slug = fm.get("slug") or f.stem
                raw_cat = fm.get("category", "")
                cat_norm = normalize_category(raw_cat)
                author = fm.get("author", "")
                
                # Check contrast
                ptype = fm.get("protocol_type", "")
                contrast_obj = fm.get("contrast", {})
                is_contrast = False
                if ptype == "contrast-enhanced":
                    is_contrast = True
                elif isinstance(contrast_obj, dict) and contrast_obj.get("agent"):
                    ag = str(contrast_obj.get("agent")).upper()
                    if ag not in ("N/A", "NONE", "FĂRĂ", "FARA", ""):
                        is_contrast = True
                
                # Relative URL from site root
                rel_dir = f.parent.relative_to(REPO_ROOT / "docs").as_posix()
                url = f"{rel_dir}/{f.stem}/"
                
                scanner = extract_scanner_or_author(title, author, fm)
                
                # Indications & keywords
                indications = fm.get("clinical_indications", [])
                if isinstance(indications, str):
                    indications = [indications]
                synonyms = fm.get("synonyms", [])
                if isinstance(synonyms, str):
                    synonyms = [synonyms]
                
                protocols.append({
                    "title": title,
                    "slug": slug,
                    "modality": mod_name,
                    "category": cat_norm,
                    "raw_category": raw_cat,
                    "url": url,
                    "contrast": is_contrast,
                    "scanner": scanner,
                    "author": author,
                    "indications": indications[:4] if indications else [],
                    "synonyms": synonyms[:3] if synonyms else [],
                })
            except Exception as e:
                pass
                
    protocols.sort(key=lambda x: (x["modality"], x["category"], x["title"]))
    
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(protocols, f, ensure_ascii=False, indent=1)
        
    print(f"✔ Index OmniSearch creat cu succes: {len(protocols)} protocoale salvate în {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_omnisearch_index()
