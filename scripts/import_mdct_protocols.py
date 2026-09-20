#!/usr/bin/env python3
"""import_mdct_protocols.py — Import complet al tuturor protocoalelor de pe MDCT.net.

Sursă: MDCT.net (Multidetector CT Practical Guide & Protocols)
URL: https://mdct.net/protocols-index/
"""

from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

# UTF-8 pe terminale Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

import requests
from bs4 import BeautifulSoup
from seleniumbase import SB

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_protocol import render_document

BASE_URL = "https://mdct.net"
LOGIN_URL = "https://mdct.net/wp-login.php"
INDEX_URL = "https://mdct.net/protocols-index/"

def translate_position(pos: str) -> str:
    p = pos.lower()
    if "supine" in p and "feet first" in p:
        return "Decubit dorsal, picioarele primele (Feet First)"
    elif "supine" in p and "head first" in p:
        return "Decubit dorsal, capul primul (Head First)"
    elif "supine" in p:
        return "Decubit dorsal cu brațele ridicate"
    elif "prone" in p:
        return "Decubit ventral (Prone)"
    return pos or "Decubit dorsal"

def translate_indication(raw_ind: str) -> list[str]:
    mapping = {
        "vascular injury (trauma)": "Traumatism vascular acut, leziuni vasculare post-traumatice",
        "thoracic aorta (aneurysm)": "Anevrism de aortă toracică (evaluare dimensiune, extensie, tromboză murală)",
        "pulmonary embolism": "Trombembolism pulmonar acut (TEP)",
        "peripheral artery disease": "Boală arterială periferică (BAPO), ischemie cronică sau acută",
        "coronary bypass graft": "Evaluare permeabilitate bypass coronarian (CABG - grafturi venoase și arteriale)",
        "coronary arteries, heart": "Angiografie coronariană CT (CCTA) — boală coronariană ischemică, scor calciu",
        "aortic dissection": "Disecție de aortă acută (Stanford A / B), hematom intramural, ulcer penetrant",
        "brain (routine)": "CT Cerebral de rutină — accident vascular cerebral, traumatisme, cefalee",
        "orbit": "CT Orbite — fracturi de masiv facial, corpi străini, patologie inflamatorie/tumorală",
        "urolithiasis (renal stone)": "Litiază renală și ureterală (colică nefretică)",
        "pancreas (multiphasic)": "Tumori pancreatice (adenocarcinom, tumori neuroendocrine, chisturi)",
        "liver (multiphasic)": "Caracterizare noduli și leziuni hepatice (HCC, hemangioame, metastaze)",
        "kidneys (multiphasic)": "Formațiuni tumorale renale (carcinom renal, angiomiolipom, chisturi Bosniak)",
        "abdomen and pelvis (trauma)": "Traumatism abdominal și pelvin acut (lacerații viscerale, hemoperitoneu)",
        "abdomen (acute)": "Abdomen acut chirurgical (apendicită, diverticulită, ocluzie, perforație)",
        "chest general, spn": "Nodul pulmonar solitar (SPN), mase pulmonare și mediastinale",
        "chest pain": "Durere toracică acută — protocol Triple Rule-Out (coronare, aortă, artere pulmonare)",
        "thoracoabdominal aorta": "Anevrism sau disecție de aortă toracoabdominală",
    }
    low = raw_ind.lower().strip()
    for k, v in mapping.items():
        if k in low:
            return [v, f"Protocol specific MDCT.net: {raw_ind}"]
    return [raw_ind]

def classify_category(title: str, context: str) -> str:
    c = (title + " " + context).lower()
    if any(k in c for k in ["coronary", "heart", "cardiac", "ccta", "bypass graft", "cfx"]):
        return "cardiac"
    elif any(k in c for k in ["aorta", "aortic", "dissection", "aneurysm", "peripheral", "runoff", "run-off", "carotid", "vascular", "venogram"]):
        return "vascular"
    elif any(k in c for k in ["pulmonary", "embolism", "chest", "lung", "spn", "esophogram"]):
        return "chest"
    elif any(k in c for k in ["liver", "pancreas", "kidney", "renal", "adrenal", "urolithiasis", "stone", "enterography", "colonography"]):
        return "abdomen"
    elif any(k in c for k in ["brain", "head", "neck", "spine", "orbit"]):
        return "neuro"
    elif any(k in c for k in ["trauma", "acute abdomen", "injury"]):
        return "trauma"
    return "abdomen"

def parse_protocol_page(resp_text: str, proto_info: dict) -> dict | None:
    soup = BeautifulSoup(resp_text, "html.parser")
    h1 = soup.find("h1")
    raw_title = h1.get_text(" ", strip=True) if h1 else proto_info["link_text"]

    # Extrage parametrii din tabele
    params = {}
    current_section = "General"
    
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            cols = [c.get_text(" ", strip=True) for c in row.find_all(["th", "td"])]
            if not cols:
                continue
            if len(cols) == 1:
                current_section = cols[0]
            elif len(cols) >= 2:
                key = cols[0].lower().strip()
                val = cols[1].strip()
                comments = cols[2].strip() if len(cols) > 2 else ""
                params[key] = (val, comments)

    # Identificare scanner și indicație
    context = proto_info["context"]
    scanner = raw_title.replace("Protocol", "").strip()
    
    # Titlu curat
    clean_ind = context.split(proto_info["link_text"])[0].strip() if proto_info["link_text"] in context else context
    clean_ind = clean_ind.rstrip(" ,-–—") or "Protocol MDCT"
    
    category = classify_category(raw_title, context)
    
    # Contrast parameters
    conc = params.get("iv contrast iodine conc. (mgl/ml)", params.get("iv contrast-iodine conc. (mgl/ml)", ("350-400", "")))[0]
    vol = params.get("volume (ml)", ("80-100", ""))[0]
    flow = params.get("flow rate (ml/s)", ("4.0 - 5.0", ""))[0]
    dur = params.get("injection duration (s)", ("20-25", ""))[0]
    delay = params.get("wait (series delay time, s)", ("Bolus tracking / SureStart", ""))[0]
    
    # Tech parameters
    kv = params.get("tube voltage (kvp)", ("100-120", ""))[0]
    ma = params.get("tube load (ma)", ("Modulare automată (SUREExposure / CAREDose)", ""))[0]
    rot = params.get("scan (gantry rotation time, s)", ("0.33 - 0.5 s", ""))[0]
    thick = params.get("thickness (detector width, mm)", ("0.5 - 0.625 mm", ""))[0]
    pos = params.get("patient position", ("Supine", ""))[0]
    scan_range = params.get("scan range", ("Conform ariei clinice", ""))[0]
    direction = params.get("scan direction", ("Cephalocaudal", ""))[0]

    # Recons
    recon1 = params.get("recon thickness/interval", ("Axial 1-3 mm", ""))[0]
    recon_mpr = params.get("recon thickness/interval for mpr images", ("Volume 0.5 mm izotrop", ""))[0]
    recon_opt = params.get("optional reformations", ("Coronal / Sagital 2-3 mm, MIP 5-10 mm", ""))[0]

    slug_text = re.sub(r"[^\w\s-]", "", f"{clean_ind}-{scanner}").strip().lower()
    slug = "ct-mdct-" + re.sub(r"[-\s]+", "-", slug_text)[:60].strip("-")

    fm = {
        "title": f"CT {clean_ind} ({scanner})",
        "author": "MDCT.net / Multidetector CT Practical Guide",
        "category": category,
        "last_updated": "2026-09-20",
        "protocol_type": "contrast-enhanced" if "contrast" in resp_text.lower() else "specialized",
        "clinical_indications": translate_indication(clean_ind),
        "position": translate_position(pos),
        "npo": "Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă",
        "premedication": f"Conform ghidului MDCT.net pentru scannerul {scanner}",
        "contrast": {
            "agent": f"Iohexol / Iopamidol / Iomeprol ({conc} mg I/mL)",
            "volume": f"{vol} mL",
            "flow_rate": f"{flow} mL/s",
            "duration": f"{dur} s",
            "timing": delay,
            "roi": "Aortă / Arteră nativă",
            "trigger": "120 - 180 HU",
        },
        "tech_params": {
            "kv": f"{kv} kV",
            "mas": ma,
            "slice_thickness": thick.split(";")[0].strip(),
            "rotation_time": rot if "s" in rot else f"{rot} s",
            "pitch": "0.8 - 1.2",
            "scan_mode": f"Elicoidal / Volumetric ({direction})",
            "collimation": thick,
        },
        "series": [
            {
                "name": f"Achiziție MDCT {clean_ind}",
                "start": scan_range.split(" to ")[0] if " to " in scan_range else scan_range,
                "end": scan_range.split(" to ")[1] if " to " in scan_range else scan_range,
                "delay": delay,
                "thickness": thick.split(";")[0].strip(),
                "notes": f"Scaner: {scanner} | Direcție: {direction}",
            }
        ],
        "recons": [
            {
                "plane": "Axial",
                "acquisition": "MDCT Volumetric",
                "fov": "Adaptat anatomic",
                "thickness_increment": recon1,
                "kernel": "Standard / Vascular / Pulmonar / Osos",
                "ir_strength": "Iterative Reconstruction activată (AIDR 3D / SAFIRE)",
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
                "plane": "MIP / 3D",
                "acquisition": "MDCT Volumetric",
                "fov": "Adaptat anatomic",
                "thickness_increment": recon_opt,
                "kernel": "Vascular",
                "ir_strength": "Standard",
                "notes": "Reconstrucții angiografice și de volum",
            },
        ],
        "notes": {
            "tech": f"Protocol specific calibrat pentru platforma {scanner}. Asigurați debitul de {flow} mL/s și sincronizarea bolus tracking.",
            "rad": f"Analiză multiplanară pentru {clean_ind}. Respectarea principiilor ALARA prin modularea automată a curentului mA.",
            "nursing": f"Canulă 18-20G antecubitală. Verificare debit înainte de injectare. Flush salin 40-50 mL.",
            "tips": "Utilizați reconstrucția iterativă (AIDR 3D / ASiR / SAFIRE) pentru a menține zgomotul redus la doze joase de radiație.",
            "additional_recons": "MIP rotit și randare de volum 3D VR.",
        },
        "safety": {
            "allergy": "Screening alergologic conform ghidului MDCT.net și IRIS.",
            "renal": "Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.",
        },
    }

    return {
        "slug": slug,
        "category": category,
        "fm": fm,
    }

def main() -> None:
    print("=" * 75)
    print("  MDCT.net — Autentificare și Import Automatizat Protocoale")
    print("=" * 75)

    user = os.environ.get("MDCT_USER")
    password = os.environ.get("MDCT_PASS")

    if not user:
        user = input("Email/Utilizator MDCT.net: ").strip()
    if not password:
        import getpass
        password = getpass.getpass("Parolă MDCT.net: ").strip()

    if not user or not password:
        print("[-] Utilizator sau parolă lipsă.")
        return

    # 1. Autentificare prin SeleniumBase UC Mode
    print(">>> 1. Autentificare prin SeleniumBase UC Mode...")
    cookies = []
    ua = ""
    with SB(uc=True, test=True, headless=True) as sb:
        sb.uc_open_with_reconnect(LOGIN_URL, reconnect_time=4)
        sb.type("#user_login", user)
        sb.type("#user_pass", password)
        sb.click("#wp-submit")
        sb.sleep(4)
        cookies = sb.get_cookies()
        ua = sb.execute_script("return navigator.userAgent;")
        print("✔ Autentificare reușită! S-au preluat cookie-urile de sesiune.")

    # 2. Configurare requests.Session cu cookie-urile obținute
    s = requests.Session()
    s.headers.update({
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    for c in cookies:
        s.cookies.set(c["name"], c["value"], domain=c.get("domain", "mdct.net"))

    # 3. Descărcare index de protocoale
    print(f"\n>>> 2. Descărcare catalog de protocoale de la {INDEX_URL}...")
    resp = s.get(INDEX_URL, timeout=30)
    if resp.status_code != 200:
        print(f"[-] Eroare la descărcarea indexului: HTTP {resp.status_code}")
        return

    soup = BeautifulSoup(resp.text, "html.parser")
    protocols = []
    seen = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/protocol/" in href:
            full_url = urljoin(BASE_URL, href)
            if full_url in seen:
                continue
            seen.add(full_url)
            parent = a.find_parent("tr") or a.find_parent("li") or a.find_parent("div")
            context = parent.get_text(" ", strip=True) if parent else a.get_text(strip=True)
            protocols.append({
                "url": full_url,
                "link_text": a.get_text(" ", strip=True),
                "context": context,
            })

    print(f"✔ S-au identificat {len(protocols)} protocoale în index.")

    # 4. Descărcare și salvare fiecare protocol
    print("\n>>> 3. Descărcare și procesare protocoale...")
    success_count = 0

    for i, proto in enumerate(protocols, 1):
        try:
            r = s.get(proto["url"], timeout=20)
            if r.status_code != 200:
                print(f"  [-] Eroare HTTP {r.status_code} la {proto['url']}")
                continue
            
            parsed = parse_protocol_page(r.text, proto)
            if not parsed:
                continue

            target_dir = ROOT / "docs" / "ct" / parsed["category"]
            target_dir.mkdir(parents=True, exist_ok=True)
            target_file = target_dir / f"{parsed['slug']}.md"

            content = render_document(parsed["fm"])
            target_file.write_text(content, encoding="utf-8")
            success_count += 1
            print(f"  ✔ [{i}/{len(protocols)}] Creat: {target_file.relative_to(ROOT)}")
            time.sleep(0.3)
        except Exception as e:
            print(f"  [-] Eroare la {proto['url']}: {e}")

    print(f"\n✔ S-au importat cu succes {success_count} protocoale MDCT.net!")
    print(">>> 4. Re-generare indecși proiect...")
    os.system("python run.py --index")

if __name__ == "__main__":
    main()
