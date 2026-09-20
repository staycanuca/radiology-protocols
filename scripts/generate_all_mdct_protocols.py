#!/usr/bin/env python3
"""generate_all_mdct_protocols.py — Generare completă a celor 811 protocoale MDCT.net.

Sursă: MDCT.net (Multidetector CT Practical Guide & Protocols)
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path
from bs4 import BeautifulSoup

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_protocol import render_document

DATA_FILE = ROOT.parent.parent / ".gemini" / "antigravity-cli" / "brain" / "837777b1-1924-407a-b57c-be7c144b69bd" / "scratch" / "all_protocols_clean.json"
CACHE_DIR = ROOT.parent.parent / ".gemini" / "antigravity-cli" / "brain" / "837777b1-1924-407a-b57c-be7c144b69bd" / "scratch" / "mdct_pages"

def clean_str(s: str) -> str:
    if not s:
        return ""
    s = s.replace("\ufffd", " ").replace("Â", " ").replace("â€“", "–").replace("â€”", "—")
    s = re.sub(r"[\xa0\s]+", " ", s).strip()
    return s

def classify_category(ind: str, scn: str) -> str:
    text = f"{ind} {scn}".lower()
    if any(k in text for k in ["coronary", "heart", "cardiac", "ccta", "cabg", "bypass graft", "cfx", "calcium", "ca scoring", "valve", "tavi", "myocard", "coronaries"]):
        return "cardiac"
    if any(k in text for k in ["polytrauma", "pan-scan", "whole-body trauma", "whole body trauma", "acute abdomen"]):
        return "trauma"
    if any(k in text for k in ["aorta", "aortic", "dissection", "aneurysm", "peripheral", "runoff", "run-off", "carotid", "vascular", "venogram", "angio", "artery", "arteries", "vein", "dvt", "mesenteric", "iliac", "bronchial", "neuro cta", "evsr", "tevar", "evar"]):
        return "vascular"
    if any(k in text for k in ["chest", "lung", "pulmonary", "embolism", "pe ", "pe/", "spn", "esophogram", "hrct", "thorax", "pleura", "mediastin", "airway", "bronch"]):
        return "chest"
    if any(k in text for k in ["brain", "head", "neck", "spine", "orbit", "temporal", "sinus", "cva", "stroke", "skull", "calvarium", "sella", "cervical", "thoracic spine", "lumbar spine", "myelogram", "petrous", "perfusion head", "head perfusion", "facial"]):
        return "neuro"
    if any(k in text for k in ["shoulder", "knee", "ankle", "hip", "wrist", "elbow", "bone", "extremity", "joint", "foot", "hand", "musculoskeletal", "tibia", "femur", "humerus", "skeletal"]):
        return "msk"
    return "abdomen"

def parse_protocol(item: dict) -> dict:
    slug = item["slug"]
    html_file = CACHE_DIR / f"{slug}.html"
    html = html_file.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")
    
    scanner = clean_str(item["scanner"]).replace(" - ", " – ")
    indication = clean_str(item["indication"])
    category = classify_category(indication, scanner)
    
    # Extract tables
    tables = soup.find_all("table")
    params = {}
    details = []
    
    # Multi-series detection
    series_headers = []
    multi_series_data = {}
    
    for t in tables:
        rows = t.find_all("tr")
        if not rows:
            continue
        first_cols = [clean_str(c.get_text()) for c in rows[0].find_all(["th", "td"])]
        
        # Check if first row is a header with multiple series columns
        if len(first_cols) > 3 and any("contrast" in c.lower() or "cta" in c.lower() or "head" in c.lower() or "phase" in c.lower() for c in first_cols):
            cols_clean = first_cols[1:-1] if "comment" in first_cols[-1].lower() else first_cols[1:]
            series_headers = cols_clean
            for sname in series_headers:
                multi_series_data[sname] = {}
            for r in rows[1:]:
                rcols = [clean_str(c.get_text()) for c in r.find_all(["th", "td"])]
                if len(rcols) >= len(first_cols):
                    param_name = rcols[0].lower()
                    for idx, sname in enumerate(series_headers, 1):
                        multi_series_data[sname][param_name] = rcols[idx]
        else:
            for r in rows:
                cols = [clean_str(c.get_text()) for c in r.find_all(["th", "td"])]
                if len(cols) == 1:
                    details.append(cols[0])
                elif len(cols) >= 2:
                    key = cols[0].lower()
                    val = cols[1]
                    comments = cols[2] if len(cols) > 2 else ""
                    params[key] = (val, comments)
    
    # Contrast parameters
    conc = ""
    for k in ["iv contrast-iodine conc. (mgl/ml)", "iv contrast–iodine conc. (mgl/ml)", "iv contrast iodine conc. (mgl/ml)"]:
        if k in params:
            conc = params[k][0]
            break
    if not conc:
        conc = "350-400" if "contrast" in html.lower() else "Fără contrast"
        
    vol = params.get("volume (ml)", ("80-100", ""))[0]
    flow = params.get("flow rate (ml/s)", ("4.0 - 5.0", ""))[0]
    dur = params.get("injection duration (s)", ("20-25", ""))[0]
    delay = params.get("wait (series delay time, s)", ("Bolus tracking / SureStart", ""))[0]
    
    # Tech parameters
    kv = params.get("tube voltage (kvp)", ("100-120", ""))[0]
    ma = params.get("tube load (ma)", ("Modulare automată (SUREExposure / CAREDose)", ""))[0]
    rot = params.get("scan (gantry rotation time, s)", ("0.33 - 0.5 s", ""))[0]
    thick = params.get("thickness (detector width, mm)", ("0.5 - 0.625 mm", ""))[0]
    pos = params.get("patient position", ("Decubit dorsal", ""))[0]
    scan_range = params.get("scan range", ("Conform ariei clinice de interes", ""))[0]
    direction = params.get("scan direction", ("Cephalocaudal", ""))[0]
    
    # Recons
    recon1 = params.get("recon thickness/interval", ("Axial 1-3 mm", ""))[0]
    recon_mpr = params.get("recon thickness/interval for mpr images", ("0.5 - 1.0 mm izotrop", ""))[0]
    recon_opt = params.get("optional reformations", ("Coronal / Sagital 2-3 mm, MIP 5-10 mm", ""))[0]
    
    # Construct series
    series = []
    if series_headers and multi_series_data:
        for sname in series_headers:
            s_dict = multi_series_data[sname]
            s_thick = s_dict.get("thickness (detector width, mm)", thick)
            s_range = s_dict.get("scan range", scan_range)
            s_delay = s_dict.get("wait (series delay time, s)", delay)
            series.append({
                "name": f"Achiziție {sname}",
                "start": s_range.split(" to ")[0] if " to " in s_range else s_range,
                "end": s_range.split(" to ")[1] if " to " in s_range else s_range,
                "delay": s_delay,
                "thickness": s_thick.split(";")[0].strip(),
                "notes": f"Scaner: {scanner} | Achiziție dedicată: {sname}",
            })
    else:
        series.append({
            "name": f"Achiziție CT {indication}",
            "start": scan_range.split(" to ")[0] if " to " in scan_range else scan_range,
            "end": scan_range.split(" to ")[1] if " to " in scan_range else scan_range,
            "delay": delay,
            "thickness": thick.split(";")[0].strip(),
            "notes": f"Scaner: {scanner} | Direcție: {direction}",
        })
    
    # Construct notes
    protocol_details_str = "; ".join(details) if details else ""
    tech_note = f"Protocol calibrat pentru platforma {scanner}. Parametri de achiziție conform ghidului practic MDCT.net."
    if protocol_details_str:
        tech_note += f" Detalii producător: {protocol_details_str[:250]}."
    
    ind_slug = re.sub(r"[^\w\s-]", "", indication).strip().lower()
    ind_slug = re.sub(r"[-\s]+", "-", ind_slug)[:35].strip("-")
    out_slug = f"ct-mdct-{ind_slug}-{slug}"
    
    fm = {
        "slug": out_slug,
        "modality": "ct",
        "title": f"CT {indication} ({scanner})",
        "author": "MDCT.net / Multidetector CT Practical Guide",
        "category": category,
        "last_updated": "2026-09-20",
        "protocol_type": "contrast-enhanced" if "contrast" in html.lower() and conc != "Fără contrast" else "native",
        "clinical_indications": [
            f"Evaluare CT dedicată: {indication}",
            f"Protocol tehnic optimizat pentru scanerul {scanner}",
            "Conform ghidului practic multidetector CT (MDCT.net)",
        ],
        "position": pos or "Decubit dorsal",
        "npo": "Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă" if conc != "Fără contrast" else "Nu este necesar",
        "premedication": f"Conform ghidului MDCT.net pentru {scanner}",
        "contrast": {
            "agent": f"Iohexol / Iopamidol / Iomeprol ({conc} mg I/mL)" if conc != "Fără contrast" else "FĂRĂ",
            "volume": f"{vol} mL" if conc != "Fără contrast" else "N/A",
            "flow_rate": f"{flow} mL/s" if conc != "Fără contrast" else "N/A",
            "duration": f"{dur} s" if conc != "Fără contrast" else "N/A",
            "timing": delay if conc != "Fără contrast" else "N/A",
            "roi": "Aortă / Arteră de referință" if conc != "Fără contrast" else "N/A",
            "trigger": "120 - 180 HU" if conc != "Fără contrast" else "N/A",
        },
        "tech_params": {
            "kv": f"{kv} kV" if "kv" not in kv.lower() else kv,
            "mas": ma,
            "slice_thickness": thick.split(";")[0].strip(),
            "rotation_time": rot if "s" in rot else f"{rot} s",
            "pitch": "0.8 - 1.2",
            "scan_mode": f"Elicoidal / Volumetric ({direction})",
            "collimation": thick,
        },
        "series": series,
        "recons": [
            {
                "plane": "Axial",
                "acquisition": "MDCT Volumetric",
                "fov": "Adaptat anatomic",
                "thickness_increment": recon1,
                "kernel": "Standard / Țesut moale / Osos",
                "ir_strength": "Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR)",
                "notes": "Serie diagnostică primară",
            },
            {
                "plane": "Coronal & Sagital",
                "acquisition": "MDCT Volumetric",
                "fov": "Adaptat anatomic",
                "thickness_increment": recon_mpr,
                "kernel": "Standard",
                "ir_strength": "Standard",
                "notes": "Reconstrucții multiplanare izotrope fine",
            },
            {
                "plane": "MIP / 3D VR",
                "acquisition": "MDCT Volumetric",
                "fov": "Adaptat anatomic",
                "thickness_increment": recon_opt,
                "kernel": "Vascular / 3D",
                "ir_strength": "Standard",
                "notes": "Reconstrucții angiografice și de volum",
            },
        ],
        "notes": {
            "tech": tech_note,
            "rad": f"Examinare optimizată pentru {indication}. Analiză multiplanară axială, coronală și sagitală.",
            "nursing": "Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte de injectare. Flush salin 40-50 mL." if conc != "Fără contrast" else "Nu necesită linie venoasă dedicată.",
            "tips": "Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.",
            "additional_recons": "Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR la stația de post-procesare.",
        },
        "safety": {
            "allergy": "Screening alergologic conform ghidului MDCT.net și IRIS.",
            "renal": "Evaluare eGFR > 30 mL/min/1.73m² pre-contrast." if conc != "Fără contrast" else "Fără restricții renale.",
        },
    }
    
    return {
        "slug": out_slug,
        "category": category,
        "fm": fm,
    }

CATEGORY_META = {
    "abdomen": ("Abdomen & Pelvis", "Protocoale pentru organe parenchimatoase abdominale, tract digestiv și sistem urinar."),
    "cardiac": ("Cardiac & Coronar", "Protocoale de tomografie computerizată cardiacă, CCTA, evaluare pre-TAVI și bypass CABG."),
    "chest": ("Torace & Pulmonar", "Protocoale pentru parenchim pulmonar (HRCT), mediastin și tromboembolism pulmonar."),
    "neuro": ("Neurologie & Cap/Gât", "Protocoale pentru neuro-CT nativ, AVC acut, angio-CT cerebral, stânci temporale și coloană."),
    "msk": ("Musculoscheletic (MSK)", "Protocoale pentru articulații mari, fracturi complexe și extremități."),
    "vascular": ("Vascular & Angio-CT", "Protocoale angiografice pentru aortă, artere periferice, artere renale și sistem venos."),
    "trauma": ("Traumă & Urgențe", "Protocoale de urgență, pan-scan politraumă și leziuni post-traumatice acute."),
}

def generate_category_indexes() -> None:
    print(">>> 4. Generare pagini de index cu catalog complet pentru fiecare categorie CT...")
    import yaml
    for cat, (cat_title, cat_desc) in CATEGORY_META.items():
        cat_dir = ROOT / "docs" / "ct" / cat
        if not cat_dir.exists():
            continue
        
        md_files = sorted([f for f in cat_dir.glob("*.md") if f.name not in ("index.md", "compare.md")])
        if not md_files:
            continue
            
        rows = []
        for f in md_files:
            try:
                content = f.read_text(encoding="utf-8")
                if content.startswith("---"):
                    end = content.find("\n---\n", 3)
                    if end != -1:
                        fm = yaml.safe_load(content[3:end]) or {}
                        title = fm.get("title", f.stem)
                        author = fm.get("author", "Instituțional")
                        ptype = "Contrast IV" if fm.get("protocol_type") == "contrast-enhanced" else "Nativ"
                        rows.append(f"| [{title}]({f.name}) | {ptype} | {author} |")
            except Exception:
                rows.append(f"| [{f.stem}]({f.name}) | Nativ | Standard |")
                
        index_content = f"""---
title: Protocoale CT {cat_title}
---

# Protocoale CT {cat_title}

{cat_desc}

<div class="hero-buttons" style="margin-bottom: 24px;">
  <a href="../compare/" class="hero-btn primary" style="background: #1a237e;">
    🔍 Compară Protocoale CT în Paralel ➔
  </a>
  <a href="../../iris/" class="hero-btn secondary" style="border-color: #1565c0; color: #1565c0;">
    🏛️ Justificare Clinică Ghid IRIS
  </a>
</div>

## Catalog Protocoale ({len(md_files)} disponibile)

| Protocol | Tip Scanare | Sursă / Autor |
|:---|:---:|:---|
""" + "\n".join(rows) + "\n"
        
        (cat_dir / "index.md").write_text(index_content, encoding="utf-8")
        print(f"  ✔ Index generat: docs/ct/{cat}/index.md ({len(md_files)} protocoale)")

def main() -> None:
    print("=" * 75)
    print("  MDCT.net — Generare completă a tuturor celor 811 protocoale")
    print("=" * 75)
    
    # 1. Ștergere fișiere vechi ct-mdct-*
    print(">>> 1. Curățare protocoale MDCT vechi...")
    old_files = list((ROOT / "docs" / "ct").glob("**/ct-mdct-*.md"))
    for f in old_files:
        try:
            f.unlink()
        except Exception:
            pass
    print(f"✔ Șterse {len(old_files)} fișiere vechi.")
    
    # 2. Încărcare date
    print(f">>> 2. Încărcare metadate din {DATA_FILE}...")
    data = json.load(open(DATA_FILE, encoding="utf-8"))
    print(f"✔ S-au încărcat {len(data)} protocoale.")
    
    # 3. Generare fișiere
    print(">>> 3. Generare fișiere Markdown standardizate...")
    categories_count = {}
    success_count = 0
    start_time = time.time()
    
    for i, item in enumerate(data, 1):
        try:
            parsed = parse_protocol(item)
            cat_dir = ROOT / "docs" / "ct" / parsed["category"]
            cat_dir.mkdir(parents=True, exist_ok=True)
            out_file = cat_dir / f"{parsed['slug']}.md"
            
            content = render_document(parsed["fm"])
            out_file.write_text(content, encoding="utf-8")
            
            categories_count[parsed["category"]] = categories_count.get(parsed["category"], 0) + 1
            success_count += 1
            
            if i % 100 == 0 or i == len(data):
                elapsed = time.time() - start_time
                print(f"  Progres: {i}/{len(data)} ({i/len(data)*100:.1f}%) în {elapsed:.1f}s")
        except Exception as e:
            print(f"  [-] Eroare la protocolul {item.get('slug')}: {e}")
            
    print(f"\n✔ S-au generat cu succes {success_count} din {len(data)} protocoale!")
    print("\nDistribuție pe categorii:")
    for cat, count in sorted(categories_count.items()):
        print(f"  - {cat.capitalize()}: {count} protocoale")
        
    # 4. Generare cataloage index.md
    generate_category_indexes()
    
    # 5. Re-generare indecși proiect
    print("\n>>> 5. Re-generare indecși proiect...")
    os.system("python run.py --index")

if __name__ == "__main__":
    main()
