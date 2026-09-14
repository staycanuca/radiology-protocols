"""ai_service.py — Modul de Asistență AI Clinică și Autentificare (Gemini & OpenAI)

Include:
- Autentificare prietenoasă: Google Sign-In (OAuth 2.0 JWT) & Autentificare Clinică Rapidă
- Motor Dual AI: Google Gemini (Flash / Pro) & OpenAI (GPT-4o / GPT-4o-mini)
- Context clinic hibrid RAG bazat pe:
  1. Ghidul Național IRIS (Ordinul MS 1342/2012) — 790 situații clinice, 1655 recomandări
  2. Indexul Protocoalelor CT — 87 protocoale cu parametri tehnici și contrast
- Fallback clinic inteligent local (funcționează chiar și când API-urile externe sunt offline/expirate)
"""

from __future__ import annotations

import base64
import json
import os
import re
from pathlib import Path
from typing import Any

from flask import Blueprint, jsonify, request, session

# Încercare încărcare dotenv
try:
    from dotenv import load_dotenv
    REPO_ROOT = Path(__file__).parent.parent
    load_dotenv(REPO_ROOT / ".env")
except Exception:
    pass

ai_bp = Blueprint("ai", __name__, url_prefix="/api/ai")

REPO_ROOT = Path(__file__).parent.parent
IRIS_DATA_FILE = REPO_ROOT / "docs" / "javascripts" / "iris-data.js"
PROTOCOL_INDEX_FILE = REPO_ROOT / "docs" / "javascripts" / "protocol-comparison-index.json"

# Cache pentru datele clinice locale
_IRIS_CACHE: dict[str, Any] | None = None
_PROTOCOLS_CACHE: list[dict[str, Any]] | None = None


def _safe_log(msg: str) -> None:
    """Afișează mesaje în consolă fără riscul de UnicodeEncodeError pe Windows."""
    try:
        print(msg)
    except Exception:
        try:
            print(msg.encode("ascii", "replace").decode("ascii"))
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Încărcare & Căutare Cunoștințe Clinice Locale
# ---------------------------------------------------------------------------

def _load_iris_data() -> dict[str, Any]:
    global _IRIS_CACHE
    if _IRIS_CACHE is not None:
        return _IRIS_CACHE
    try:
        if IRIS_DATA_FILE.exists():
            content = IRIS_DATA_FILE.read_text(encoding="utf-8")
            for prefix in ("window.IRIS_DATA =", "window.IRIS_DATA=", "window.IRIS =", "window.IRIS="):
                if prefix in content:
                    idx = content.find(prefix)
                    json_str = content[idx + len(prefix):].rstrip("; \n\r")
                    _IRIS_CACHE = json.loads(json_str)
                    return _IRIS_CACHE
    except Exception as e:
        _safe_log(f"[AI Service] Eroare la încărcarea IRIS data: {e}")
    return {"chapters": [], "situations": [], "recommendations": []}


def _load_protocol_data() -> list[dict[str, Any]]:
    global _PROTOCOLS_CACHE
    if _PROTOCOLS_CACHE is not None:
        return _PROTOCOLS_CACHE
    try:
        if PROTOCOL_INDEX_FILE.exists():
            raw = PROTOCOL_INDEX_FILE.read_text(encoding="utf-8")
            _PROTOCOLS_CACHE = json.loads(raw)
            return _PROTOCOLS_CACHE
    except Exception as e:
        _safe_log(f"[AI Service] Eroare la încărcarea Protocoalelor: {e}")
    return []


_RX_CACHE: list[dict[str, Any]] | None = None

def _load_rx_data() -> list[dict[str, Any]]:
    global _RX_CACHE
    if _RX_CACHE is not None:
        return _RX_CACHE
    results = []
    docs_rx = REPO_ROOT / "docs" / "rx"
    if docs_rx.exists():
        import yaml
        for md_file in docs_rx.rglob("*.md"):
            if md_file.name == "index.md":
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                if content.startswith("---"):
                    end = content.find("\n---\n", 3)
                    if end != -1:
                        fm = yaml.safe_load(content[3:end]) or {}
                        if fm.get("slug"):
                            results.append(fm)
            except Exception:
                pass
    _RX_CACHE = results
    return _RX_CACHE


_FLUORO_CACHE: list[dict[str, Any]] | None = None

def _load_fluoro_data() -> list[dict[str, Any]]:
    global _FLUORO_CACHE
    if _FLUORO_CACHE is not None:
        return _FLUORO_CACHE
    results = []
    docs_fluoro = REPO_ROOT / "docs" / "fluoro"
    if docs_fluoro.exists():
        import yaml
        for md_file in docs_fluoro.rglob("*.md"):
            if md_file.name == "index.md":
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                if content.startswith("---"):
                    end = content.find("\n---\n", 3)
                    if end != -1:
                        fm = yaml.safe_load(content[3:end]) or {}
                        if fm.get("slug"):
                            results.append(fm)
            except Exception:
                pass
    _FLUORO_CACHE = results
    return _FLUORO_CACHE


_IRM_CACHE: list[dict[str, Any]] | None = None

def _load_irm_data() -> list[dict[str, Any]]:
    global _IRM_CACHE
    if _IRM_CACHE is not None:
        return _IRM_CACHE
    results = []
    docs_irm = REPO_ROOT / "docs" / "irm"
    if docs_irm.exists():
        import yaml
        for md_file in docs_irm.rglob("*.md"):
            if md_file.name == "index.md":
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                if content.startswith("---"):
                    end = content.find("\n---\n", 3)
                    if end != -1:
                        fm = yaml.safe_load(content[3:end]) or {}
                        if fm.get("slug"):
                            results.append(fm)
            except Exception:
                pass
    _IRM_CACHE = results
    return _IRM_CACHE


_ECO_CACHE: list[dict[str, Any]] | None = None

def _load_eco_data() -> list[dict[str, Any]]:
    global _ECO_CACHE
    if _ECO_CACHE is not None:
        return _ECO_CACHE
    results = []
    docs_eco = REPO_ROOT / "docs" / "eco"
    if docs_eco.exists():
        import yaml
        for md_file in docs_eco.rglob("*.md"):
            if md_file.name == "index.md":
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                if content.startswith("---"):
                    end = content.find("\n---\n", 3)
                    if end != -1:
                        fm = yaml.safe_load(content[3:end]) or {}
                        if fm.get("slug"):
                            results.append(fm)
            except Exception:
                pass
    _ECO_CACHE = results
    return _ECO_CACHE



# ---------------------------------------------------------------------------
# Dicționar Anatomic & Normalizare Lingvistică
# ---------------------------------------------------------------------------

def strip_diacritics(text: str) -> str:
    """Elimină diacriticele românești pentru potrivire robustă."""
    if not text:
        return ""
    trans = str.maketrans("ăâîșşțţĂÂÎȘŞȚŢ", "aaissttAAISSTT")
    return text.translate(trans)


ANATOMICAL_DOMAINS: dict[str, dict[str, Any]] = {
    "neuro": {
        "label": "Neuro / Craniu / Cap",
        "stems": ["cran", "cerebr", "encefal", "cap", "creier", "intracran", "mening", "sella", "hipofiz", "orbita", "sinus", "saf", "stanca", "cervic", "gat"],
        "iris_chapters": {"c-cap", "c-gat-parti-moi"},
        "ct_categories": {"neuro", "trauma"},
        "rx_categories": {"craniu-saf", "coloana"},
        "irm_categories": {"neuro"},
        "eco_categories": set(),
    },
    "torace": {
        "label": "Torace / Cardio-Pulmonar",
        "stems": ["torac", "pulmon", "plaman", "pleur", "mediastin", "card", "cord", "coronar", "tuse", "dispnee", "pneumon", "hemoptiz", "coaste", "grilaj"],
        "iris_chapters": {"c-torace", "c-aparat-cardiovascular"},
        "ct_categories": {"chest", "cardiac", "vascular"},
        "rx_categories": {"torace"},
        "irm_categories": {"cardiac"},
        "eco_categories": set(),
    },
    "abdomen": {
        "label": "Abdomen / Pelvis / Digestiv / Uro",
        "stems": ["abdom", "pelv", "ficat", "hepat", "splin", "renal", "rinichi", "pancrea", "bili", "colecist", "vezic", "stomac", "colon", "rect", "digest", "uro", "supraren", "apendic", "fosa iliac", "ileus", "prostat", "endometr", "mrcp"],
        "iris_chapters": {"c-aparat-digestiv", "c-aparat-uro-genital-si-glande-suprarenale", "c-obstetrica-si-ginecologie"},
        "ct_categories": {"abdomen", "vascular"},
        "rx_categories": {"abdomen"},
        "irm_categories": {"abdomen-pelvis"},
        "eco_categories": {"abdomen-pelvis"},
    },
    "coloana": {
        "label": "Coloană Vertebrală",
        "stems": ["coloan", "vertebr", "cervic", "toracal", "dorsal", "lombar", "sacr", "coccis", "rahis", "spondil", "lumbag", "sciatica"],
        "iris_chapters": {"c-coloana-vertebrala"},
        "ct_categories": {"neuro", "msk", "trauma"},
        "rx_categories": {"coloana"},
        "irm_categories": {"neuro", "msk"},
        "eco_categories": set(),
    },
    "musculoscheletal": {
        "label": "Aparat Locomotor / Membre",
        "stems": ["membru", "umar", "clavicul", "brat", "humerus", "cot", "antebrat", "radius", "cubitus", "ulna", "pumn", "mana", "scafoid", "deget", "bazin", "sold", "coxofemur", "femur", "genunchi", "rotul", "patel", "gamba", "tibie", "peroneu", "glezna", "picior", "calcanei", "articulat", "fractur", "entorsa", "menisc", "ligament", "achil"],
        "iris_chapters": {"c-aparat-locomotor"},
        "ct_categories": {"msk", "trauma"},
        "rx_categories": {"membru-superior", "membru-inferior"},
        "irm_categories": {"msk"},
        "eco_categories": {"msk"},
    },
    "parti_moi": {
        "label": "Părți Moi / Endocrinologie / Tiroidă",
        "stems": ["tiroid", "paratiroid", "ganglion", "limfatic", "adenopati", "salivar", "parotid", "submandibular", "lipom", "chist", "colectie", "parti moi", "muscular", "subcutanat"],
        "iris_chapters": {"c-gat-parti-moi"},
        "ct_categories": {"neuro", "msk"},
        "rx_categories": set(),
        "irm_categories": {"neuro", "msk"},
        "eco_categories": {"parti-moi-endocrin"},
    },
    "vascular": {
        "label": "Vascular / Doppler",
        "stems": ["doppler", "arter", "ven", "tromboz", "tvp", "carotid", "vertebral", "aort", "anevrism", "stenoz", "ischemi", "insuficienta venoasa"],
        "iris_chapters": {"c-aparat-cardiovascular"},
        "ct_categories": {"vascular"},
        "rx_categories": set(),
        "irm_categories": set(),
        "eco_categories": {"vascular-doppler"},
    },
    "san": {
        "label": "Senologie / Sân",
        "stems": ["san", "mamar", "mamelon", "nodul mamar", "birads", "bi-rads"],
        "iris_chapters": {"c-obstetrica-si-ginecologie"},
        "ct_categories": set(),
        "rx_categories": set(),
        "irm_categories": {"san"},
        "eco_categories": {"san"},
    },
    "pediatrie": {
        "label": "Pediatrie",
        "stems": ["copil", "pediatr", "sugar", "nou-nascut", "neonat", "fontanel", "invagin", "pilor"],
        "iris_chapters": {"c-pediatrie"},
        "ct_categories": set(),
        "rx_categories": {"pediatrie"},
        "irm_categories": set(),
        "eco_categories": {"pediatrie"},
    },
}

_REC_PRIORITY: dict[str, int] = {
    "indicat": 1,
    "investigatie recomandata": 1,
    "investigație recomandată": 1,
    "doar in cazuri particulare": 2,
    "doar în cazuri particulare": 2,
    "doar cu aviz specializat": 3,
    "neindicat": 4,
}


def search_clinical_context(query: str, top_k: int = 4) -> dict[str, Any]:
    """Caută cele mai relevante recomandări IRIS și protocoale CT/Rx pentru interogare."""
    q_norm = strip_diacritics(query.lower())
    q_tokens = set(re.findall(r"\w+", q_norm))
    # Exclude cuvinte comune de legătură
    stop_words = {"si", "sau", "de", "la", "in", "cu", "un", "o", "pe", "pentru", "este", "ce", "cum", "al", "ai", "ale", "se"}
    q_tokens = {t for t in q_tokens if len(t) > 2 and t not in stop_words}

    # Detecție domenii anatomice active din query
    active_domains = [d for d, info in ANATOMICAL_DOMAINS.items() if any(s in q_norm for s in info["stems"])]

    iris_data = _load_iris_data()
    protocols = _load_protocol_data()
    rx_protocols = _load_rx_data()

    recs_by_sit = {}
    for r in iris_data.get("recommendations", []):
        sit_id = r.get("situationId")
        recs_by_sit.setdefault(sit_id, []).append(r)

    # 1. Căutare în situații IRIS cu filtrare și ancorare anatomică
    scored_sits = []
    seen_sit_names = set()
    for sit in iris_data.get("situations", []):
        if sit.get("placeholder"):
            continue
        sit_name_raw = sit.get("name", "")
        sit_name = strip_diacritics(sit_name_raw.lower())
        chap_id = sit.get("chapterId", "")

        # Punctaj lexical de bază pe titlu
        score = sum(4 for t in q_tokens if t in sit_name)

        # Filtrare și ponderare anatomică
        if active_domains:
            has_active_stem = any(any(s in sit_name for s in ANATOMICAL_DOMAINS[d]["stems"]) for d in active_domains)
            in_active_chap = any(chap_id in ANATOMICAL_DOMAINS[d]["iris_chapters"] for d in active_domains)

            has_foreign_stem = False
            in_foreign_chap = False
            for d, info in ANATOMICAL_DOMAINS.items():
                if d not in active_domains:
                    if any(s in sit_name for s in info["stems"]):
                        has_foreign_stem = True
                    if chap_id in info["iris_chapters"]:
                        in_foreign_chap = True

            if has_active_stem:
                score += 25
            elif has_foreign_stem:
                score -= 35
            elif in_active_chap:
                score += 15
            elif in_foreign_chap:
                score -= 30

        # Punctaj plafonat din comentariile recomandărilor (evită spam-ul)
        recs = recs_by_sit.get(sit.get("id"), [])
        comb_text = strip_diacritics(" ".join(f"{r.get('exam', '')} {r.get('comments', '')}" for r in recs).lower())
        rec_matches = sum(1 for t in q_tokens if t in comb_text)
        score += min(rec_matches, 3)

        norm_name = re.sub(r"\s+", " ", sit_name.strip())
        if score > 0 and norm_name not in seen_sit_names:
            seen_sit_names.add(norm_name)
            scored_sits.append((score, sit, recs))

    scored_sits.sort(key=lambda x: x[0], reverse=True)

    # De-duplicare și ierarhizare clinică a recomandărilor IRIS
    top_iris = []
    for score, sit, recs in scored_sits[:top_k]:
        seen_recs = set()
        clean_recs = []
        for r in recs:
            exam_c = (r.get("exam") or "").strip()
            ind_c = (r.get("indication") or "").strip()
            comm_c = (r.get("comments") or "").strip()
            if not exam_c:
                continue
            # Cheie de de-duplicare normalizată
            k = (
                re.sub(r"\s+", " ", exam_c.lower()),
                re.sub(r"\s+", " ", ind_c.lower()),
                re.sub(r"\s+", " ", strip_diacritics(comm_c[:40].lower()))
            )
            if k not in seen_recs:
                seen_recs.add(k)
                clean_recs.append(r)

        # Ordonare clinică: Indicat -> Cazuri particulare -> Aviz specializat -> Neindicat
        def _prio(rec: dict[str, Any]) -> int:
            ind = strip_diacritics((rec.get("indication") or "").strip().lower())
            return _REC_PRIORITY.get(ind, 5)

        clean_recs.sort(key=_prio)

        top_iris.append({
            "situation": sit.get("name"),
            "chapterId": sit.get("chapterId"),
            "recommendations": [
                {
                    "exam": r.get("exam"),
                    "indication": r.get("indication"),
                    "grade": r.get("grade"),
                    "doseMin": r.get("doseMin"),
                    "doseMax": r.get("doseMax"),
                    "comments": r.get("comments"),
                    "otherInfo": r.get("otherInfo"),
                }
                for r in clean_recs[:6]
            ],
        })

    # 2. Căutare în Protocoale CT cu filtrare de categorie și domeniu anatomic
    scored_ct = []
    for proto in protocols:
        title_raw = proto.get("title", "")
        title = strip_diacritics(title_raw.lower())
        cat = proto.get("category", "").lower()
        slug = proto.get("slug", "").lower()
        summary_val = proto.get("summary", [])
        summary_text = strip_diacritics(json.dumps(summary_val, ensure_ascii=False).lower())

        score = sum(4 for t in q_tokens if t in title)
        score += sum(2 for t in q_tokens if t in cat or t in slug)
        score += sum(1 for t in q_tokens if t in summary_text)

        if active_domains:
            allowed_cats = set().union(*[ANATOMICAL_DOMAINS[d]["ct_categories"] for d in active_domains])
            has_active_stem = any(any(s in title for s in ANATOMICAL_DOMAINS[d]["stems"]) for d in active_domains)

            if cat in allowed_cats:
                if cat == "trauma":
                    # Politraumatismul se păstrează doar dacă titlul specifică regiunea anatomică cerută
                    if has_active_stem:
                        score += 20
                    else:
                        score = 0
                else:
                    score += 15 if has_active_stem else 5
            else:
                score = 0

        if score > 0:
            scored_ct.append((score, proto))

    scored_ct.sort(key=lambda x: x[0], reverse=True)
    top_ct = []
    for score, proto in scored_ct[:top_k]:
        contrast = proto.get("contrast", {})
        tech = proto.get("tech_params", {})
        top_ct.append({
            "title": proto.get("title"),
            "category": proto.get("category"),
            "slug": proto.get("slug"),
            "url": f"../ct/{proto.get('category')}/{proto.get('slug')}/",
            "contrast_agent": contrast.get("agent", "N/A"),
            "contrast_timing": contrast.get("timing", "N/A"),
            "kv": tech.get("kv", "120"),
            "mas": tech.get("mas", "Auto"),
            "slice": tech.get("slice_thickness", "0.625 mm"),
            "series": [s.get("name") for s in proto.get("series", []) if s.get("name")],
        })

    # 3. Căutare în Protocoale Radiologie Clasică (Rx) cu corelare anatomică
    scored_rx = []
    for rx in rx_protocols:
        title_raw = rx.get("title", "")
        title = strip_diacritics(title_raw.lower())
        cat = rx.get("category", "").lower()
        slug = rx.get("slug", "").lower()
        inds = strip_diacritics(" ".join(rx.get("clinical_indications", [])).lower())
        pos = strip_diacritics(rx.get("position", "").lower())

        score = sum(4 for t in q_tokens if t in title)
        score += sum(2 for t in q_tokens if t in inds)
        score += sum(1 for t in q_tokens if t in cat or t in slug or t in pos)
        if any(w in q_tokens for w in ("rx", "radiografie", "radiografii")):
            score += 2

        if active_domains:
            allowed_rx_cats = set().union(*[ANATOMICAL_DOMAINS[d]["rx_categories"] for d in active_domains])
            has_active_stem = any(any(s in title for s in ANATOMICAL_DOMAINS[d]["stems"]) for d in active_domains)
            if cat in allowed_rx_cats:
                # La neuro/craniu, permitem coloana doar dacă este cervicală
                if "neuro" in active_domains and "coloana" not in active_domains:
                    if cat == "coloana" and "cervic" not in title:
                        score = 0
                    else:
                        score += 15 if has_active_stem else 5
                else:
                    score += 15 if has_active_stem else 5
            else:
                score = 0

        if score > 0:
            scored_rx.append((score, rx))

    scored_rx.sort(key=lambda x: x[0], reverse=True)
    top_rx = []
    for score, rx in scored_rx[:top_k]:
        tp = rx.get("tech_params", {})
        top_rx.append({
            "title": rx.get("title"),
            "category": rx.get("category"),
            "slug": rx.get("slug"),
            "url": f"../rx/{rx.get('category')}/{rx.get('slug')}/",
            "position": rx.get("position"),
            "sid_dff": rx.get("sid_dff"),
            "kv": tp.get("kv"),
            "mas": tp.get("mas"),
            "grid": tp.get("grid"),
            "focal_spot": tp.get("focal_spot"),
        })

    # 4. Căutare în Protocoale Fluoroscopie & C-Arm
    scored_fluoro = []
    fluoro_protocols = _load_fluoro_data()
    for fl in fluoro_protocols:
        title_raw = fl.get("title", "")
        title = strip_diacritics(title_raw.lower())
        cat = fl.get("category", "").lower()
        slug = fl.get("slug", "").lower()
        inds = strip_diacritics(" ".join(fl.get("clinical_indications", [])).lower())
        prep = strip_diacritics(fl.get("patient_prep", "").lower())
        c_info = strip_diacritics(fl.get("contrast", {}).get("agent", "").lower())

        score = sum(4 for t in q_tokens if t in title)
        score += sum(2 for t in q_tokens if t in inds)
        score += sum(2 for t in q_tokens if t in cat or t in slug)
        score += sum(1 for t in q_tokens if t in prep or t in c_info)

        if "c-arm" in q_norm or "arc" in q_norm:
            if cat == "c-arm":
                score += 20
        if any(w in q_norm for w in ["barit", "bariu", "tegd", "tranzit", "esofag"]):
            if "tranzit" in slug or "esofag" in slug:
                score += 15
        if any(w in q_norm for w in ["cisto", "mictional", "ucr", "cum", "reflux", "rvu"]):
            if "cisto" in slug:
                score += 15
        if any(w in q_norm for w in ["dezinvagin", "invagin"]):
            if "dezinvaginare" in slug:
                score += 20

        if score > 0:
            scored_fluoro.append((score, fl))

    scored_fluoro.sort(key=lambda x: x[0], reverse=True)
    top_fluoro = []
    for score, fl in scored_fluoro[:top_k]:
        fp = fl.get("fluoro_params", {})
        contr = fl.get("contrast", {})
        top_fluoro.append({
            "title": fl.get("title"),
            "category": fl.get("category"),
            "slug": fl.get("slug"),
            "url": f"../fluoro/{fl.get('category')}/{fl.get('slug')}/",
            "contrast_agent": contr.get("agent", "N/A"),
            "mode": fp.get("mode", "Pulsat"),
            "kv": fp.get("kv", "Standard"),
            "time": fp.get("target_fluoro_time", "< 3 min"),
        })

    # 5. Căutare în Protocoale Imagistică prin Rezonanță Magnetică (IRM)
    scored_irm = []
    irm_protocols = _load_irm_data()
    for rm in irm_protocols:
        title_raw = rm.get("title", "")
        title = strip_diacritics(title_raw.lower())
        cat = rm.get("category", "").lower()
        slug = rm.get("slug", "").lower()
        inds = strip_diacritics(" ".join(rm.get("clinical_indications", [])).lower())
        seq_names = " ".join(s.get("name", "") for s in rm.get("sequences", []) if isinstance(s, dict))
        seqs_norm = strip_diacritics(seq_names.lower())

        score = sum(4 for t in q_tokens if t in title)
        score += sum(2 for t in q_tokens if t in inds)
        score += sum(2 for t in q_tokens if t in cat or t in slug)
        score += sum(1 for t in q_tokens if t in seqs_norm)

        if any(w in q_norm for w in ["irm", "rmn", "mri", "rezonanta", "magnetic"]):
            score += 6
        if any(w in q_norm for w in ["dwi", "adc", "flair", "mrcp", "pirads", "pi-rads", "gadoliniu", "stir", "lge"]):
            score += 10

        if active_domains:
            allowed_irm_cats = set().union(*[ANATOMICAL_DOMAINS[d].get("irm_categories", set()) for d in active_domains])
            has_active_stem = any(any(s in title for s in ANATOMICAL_DOMAINS[d]["stems"]) for d in active_domains)
            if cat in allowed_irm_cats:
                score += 15 if has_active_stem else 5
            else:
                # Menținem doar dacă s-a cerut explicit IRM sau potrivire de stem
                if not any(w in q_norm for w in ["irm", "rmn", "mri", "rezonanta"]):
                    score = 0

        if score > 0:
            scored_irm.append((score, rm))

    scored_irm.sort(key=lambda x: x[0], reverse=True)
    top_irm = []
    for score, rm in scored_irm[:top_k]:
        hw = rm.get("coils_hardware", {})
        contr = rm.get("contrast", {})
        seqs = [s.get("name") for s in rm.get("sequences", []) if isinstance(s, dict) and s.get("name")]
        top_irm.append({
            "title": rm.get("title"),
            "category": rm.get("category"),
            "slug": rm.get("slug"),
            "url": f"../irm/{rm.get('category')}/{rm.get('slug')}/",
            "field": hw.get("field_strength", "1.5T / 3.0T"),
            "coil": hw.get("coil", "Antenă dedicată"),
            "contrast_agent": contr.get("agent", "Nativ / Fără contrast"),
            "sequences": seqs[:4],
        })

    # 6. Căutare în Protocoale Ecografie & Ultrasonografie (US)
    scored_eco = []
    eco_protocols = _load_eco_data()
    for ec in eco_protocols:
        title_raw = ec.get("title", "")
        title = strip_diacritics(title_raw.lower())
        cat = ec.get("category", "").lower()
        slug = ec.get("slug", "").lower()
        inds = strip_diacritics(" ".join(ec.get("clinical_indications", [])).lower())
        equip = strip_diacritics(json.dumps(ec.get("transducers_equipment", {}), ensure_ascii=False).lower())
        tech = strip_diacritics(json.dumps(ec.get("technical_settings", {}), ensure_ascii=False).lower())

        score = sum(4 for t in q_tokens if t in title)
        score += sum(2 for t in q_tokens if t in inds)
        score += sum(2 for t in q_tokens if t in cat or t in slug)
        score += sum(1 for t in q_tokens if t in equip or t in tech)

        if any(w in q_norm for w in ["eco", "ecograf", "ultrasonograf", "ultrasunet", "sonda", "transductor"]):
            score += 6
        if any(w in q_norm for w in ["doppler", "tirads", "ti-rads", "birads", "bi-rads", "fast", "e-fast", "graf", "transfontanelar"]):
            score += 8

        if active_domains:
            allowed_eco_cats = set().union(*[ANATOMICAL_DOMAINS[d].get("eco_categories", set()) for d in active_domains])
            has_active_stem = any(any(s in title for s in ANATOMICAL_DOMAINS[d]["stems"]) for d in active_domains)
            if cat in allowed_eco_cats:
                score += 15 if has_active_stem else 5
            else:
                if not any(w in q_norm for w in ["eco", "ecograf", "ultrasonograf", "doppler"]):
                    score = 0

        if score > 0:
            scored_eco.append((score, ec))

    scored_eco.sort(key=lambda x: x[0], reverse=True)
    top_eco = []
    for score, ec in scored_eco[:top_k]:
        te = ec.get("transducers_equipment", {})
        ts = ec.get("technical_settings", {})
        views = [v.get("view") for v in ec.get("standard_views", []) if isinstance(v, dict) and v.get("view")]
        top_eco.append({
            "title": ec.get("title"),
            "category": ec.get("category"),
            "slug": ec.get("slug"),
            "url": f"../eco/{ec.get('category')}/{ec.get('slug')}/",
            "transducers": te.get("transducer_types", "Sondă Convexă / Liniară"),
            "modes": ts.get("modes", "Mod B + Doppler Color"),
            "preset": ts.get("preset", "Standard"),
            "views": views[:3],
        })

    return {"iris": top_iris, "protocols": top_ct, "rx": top_rx, "fluoro": top_fluoro, "irm": top_irm, "eco": top_eco}


# ---------------------------------------------------------------------------
# Fallback Clinic Inteligent (Local RAG)
# ---------------------------------------------------------------------------

def _format_indication_badge(indication: str) -> str:
    """Returnează badge vizual intuitiv pentru statusul recomandării."""
    ind_norm = strip_diacritics((indication or "").strip().lower())
    if "indicat" in ind_norm and "neindicat" not in ind_norm:
        return f"🟢 **{indication}**"
    elif "particulare" in ind_norm:
        return f"🟡 **{indication}**"
    elif "specializat" in ind_norm:
        return f"🟠 **{indication}**"
    elif "neindicat" in ind_norm:
        return f"🔴 **{indication}**"
    return f"**{indication}**"


def generate_local_clinical_reply(query: str, context: dict[str, Any]) -> str:
    """Generează un răspuns clinic structurat bazat pe cunoștințele locale IRIS, Eco, IRM, Rx, Fluoroscopie & CT."""
    iris_matches = context.get("iris", [])
    eco_matches = context.get("eco", [])
    irm_matches = context.get("irm", [])
    ct_matches = context.get("protocols", [])
    rx_matches = context.get("rx", [])
    fluoro_matches = context.get("fluoro", [])

    lines = []
    lines.append("### 🩺 Evaluare Clinică & Recomandare Ghid Național IRIS\n")

    if iris_matches:
        lines.append("Conform **Ghidului de utilizare a investigațiilor radiologice (Ordinul MS nr. 1342/2012)**:\n")
        for item in iris_matches:
            lines.append(f"#### Situație Clinică: **{item['situation']}**")
            for r in item["recommendations"]:
                dose = r.get("doseMax", r.get("doseMin", 0))
                dose_sym = "●" * min(dose, 4) + "○" * (4 - min(dose, 4)) if dose > 0 else "○○○○ (Fără iradiere)"
                grade_str = f"**Grad {r.get('grade')}**" if r.get("grade") else ""
                badge = _format_indication_badge(r.get("indication", ""))
                lines.append(
                    f"- {badge} — **{r['exam']}** {grade_str} | Iradiere: `{dose_sym}`\n"
                    f"  > {r.get('comments', '')} {r.get('otherInfo', '')}".strip()
                )
            lines.append("")
    else:
        lines.append(
            "Nu a fost găsită o corespondență exactă în Ghidul IRIS pentru termenii căutați. "
            "Puteți consulta direct [Ghidul Național IRIS](../iris/) sau rafinați simptomele.\n"
        )

    if eco_matches:
        lines.append("### 📡 Protocoale Ecografie & Ultrasonografie (US) Recomandate\n")
        for p in eco_matches:
            views_str = ", ".join(p.get("views", [])) if p.get("views") else "Incidențe standard conform ghidului"
            lines.append(
                f"- [**{p['title']}**]({p['url']})\n"
                f"  - **Transductori & Aplicație:** {p.get('transducers', 'Sondă Convexă / Liniară')} | Preset: `{p.get('preset', 'Standard')}`\n"
                f"  - **Moduri de Lucru:** {p.get('modes', 'Mod B + Doppler')}\n"
                f"  - **Incidențe Recomandate:** {views_str}\n"
            )

    if irm_matches:
        lines.append("### 🧲 Protocoale Rezonanță Magnetică (IRM) Recomandate\n")
        for p in irm_matches:
            seq_str = ", ".join(p.get("sequences", [])) if p.get("sequences") else "Secvențe specifice conform protocolului"
            lines.append(
                f"- [**{p['title']}**]({p['url']})\n"
                f"  - **Câmp & Antenă:** {p.get('field', '1.5T / 3.0T')} | {p.get('coil', 'Antenă dedicată')}\n"
                f"  - **Substanță Contrast (Gadoliniu):** {p.get('contrast_agent', 'Nativ / La indicație')}\n"
                f"  - **Secvențe Cheie:** {seq_str}\n"
            )

    if rx_matches:
        lines.append("### 📷 Protocoale Radiologie Clasică (Rx) Recomandate\n")
        for p in rx_matches:
            lines.append(
                f"- [**{p['title']}**]({p['url']})\n"
                f"  - **Poziție:** {p['position']}\n"
                f"  - **Parametri Tehnici:** {p['kv']} kV | {p['mas']} mAs | DFF: {p['sid_dff']} | {p['grid']}\n"
            )

    if fluoro_matches:
        lines.append("### ✨ Protocoale Fluoroscopie & C-Arm Recomandate\n")
        for p in fluoro_matches:
            lines.append(
                f"- [**{p['title']}**]({p['url']})\n"
                f"  - **Categorie:** `{p['category']}` | **Regim:** {p.get('mode', 'Pulsat')}\n"
                f"  - **Substanță Contrast:** {p.get('contrast_agent', 'N/A')}\n"
                f"  - **Parametri Expunere:** {p.get('kv', 'Standard')} | Timp Țintă: {p.get('time', '< 3 min')}\n"
            )

    if ct_matches:
        lines.append("### ⚡ Protocoale Tomografie Computerizată (CT) Asociate\n")
        for p in ct_matches:
            series_list = ", ".join(p["series"]) if p["series"] else "Achiziție standard"
            lines.append(
                f"- [**{p['title']}**]({p['url']})\n"
                f"  - **Contrast:** {p['contrast_agent']} ({p['contrast_timing']})\n"
                f"  - **Parametri Tehnici:** {p['kv']} kV | {p['mas']} mAs | Slice: {p['slice']}\n"
                f"  - **Serii:** {series_list}\n"
            )
    else:
        lines.append(
            "\n💡 Pentru explorarea completă a parametrilor tehnici imagistici, accesați "
            "[Catalogul de Protocoale](../ct/) sau [Instrumentul de Comparare](../ct/compare/).\n"
        )

    lines.append(
        "\n> [!NOTE]\n"
        "> Răspuns sintetizat automat pe baza Ghidului Național IRIS (Ministerul Sănătății) "
        "și a Bazei Locale de Protocoale (Ecografie US, IRM, CT, Rx, Fluoroscopie). Consultați întotdeauna judecata clinică la patul pacientului."
    )

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Apelare Google Gemini
# ---------------------------------------------------------------------------

def call_gemini(user_query: str, system_prompt: str, context: dict[str, Any], history: list = None) -> tuple[str, str]:
    """Apelează Google Gemini dacă este disponibil; returnează (text, model_name)."""
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY nu este configurat.")

    import google.generativeai as genai
    genai.configure(api_key=api_key)

    context_str = json.dumps(context, ensure_ascii=False, indent=2)
    full_prompt = (
        f"{system_prompt}\n\n"
        f"--- BAZA DE CUNOȘTINȚE CLINICE ASOCIATĂ (IRIS & PROTOCOALE CT) ---\n"
        f"{context_str}\n\n"
        f"--- ÎNTREBARE CLINICĂ MEDIC / TEHNICIAN ---\n"
        f"{user_query}"
    )

    # Modele suportate în ordinea priorității
    candidate_models = [
        "gemini-flash-latest",
        "gemini-2.5-flash",
        "gemini-3.6-flash",
        "gemini-1.5-flash",
        "gemini-pro-latest",
    ]

    last_err = None
    for model_name in candidate_models:
        try:
            model = genai.GenerativeModel(model_name)
            resp = model.generate_content(full_prompt)
            if resp and resp.text:
                return resp.text, model_name
        except Exception as e:
            last_err = e
            continue

    raise RuntimeError(f"Niciun model Gemini nu a putut răspunde: {last_err}")


# ---------------------------------------------------------------------------
# Apelare OpenAI
# ---------------------------------------------------------------------------

def call_openai(user_query: str, system_prompt: str, context: dict[str, Any], history: list = None) -> tuple[str, str]:
    """Apelează OpenAI (GPT-4o / GPT-4o-mini); returnează (text, model_name)."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY nu este configurat.")

    import openai
    client = openai.OpenAI(api_key=api_key)

    context_str = json.dumps(context, ensure_ascii=False, indent=2)
    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "system",
            "content": f"Baza de cunoștințe clinice asociată (IRIS & Protocoale CT):\n{context_str}",
        },
    ]

    # Include istoric scurt
    if history:
        for h in history[-4:]:
            role = "user" if h.get("role") == "user" else "assistant"
            messages.append({"role": role, "content": h.get("content", "")})

    messages.append({"role": "user", "content": user_query})

    # Încearcă gpt-4o-mini apoi gpt-4o
    for m in ["gpt-4o-mini", "gpt-4o"]:
        try:
            resp = client.chat.completions.create(
                model=m,
                messages=messages,
                temperature=0.2,
            )
            text = resp.choices[0].message.content
            return text, m
        except Exception as e:
            continue

    raise RuntimeError("OpenAI API nu a putut genera răspunsul.")


# ---------------------------------------------------------------------------
# Decodare JWT Google Sign-In fără dependențe grele
# ---------------------------------------------------------------------------

def decode_google_jwt(credential: str) -> dict[str, Any]:
    """Decodifică payload-ul JWT returnat de Google Identity Services."""
    parts = credential.split(".")
    if len(parts) != 3:
        raise ValueError("Token JWT Google invalid.")
    payload_b64 = parts[1]
    # Padding base64
    rem = len(payload_b64) % 4
    if rem > 0:
        payload_b64 += "=" * (4 - rem)
    decoded_bytes = base64.urlsafe_b64decode(payload_b64)
    return json.loads(decoded_bytes.decode("utf-8"))


# ---------------------------------------------------------------------------
# Rute API Flask
# ---------------------------------------------------------------------------

@ai_bp.route("/auth/status", methods=["GET"])
def auth_status():
    """Returnează starea configurării (furnizori disponibili, utilizator curent)."""
    gemini_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")
    google_cid = os.environ.get("GOOGLE_CLIENT_ID", "")

    user = session.get("user")

    return jsonify({
        "ok": True,
        "providers": {
            "gemini": bool(gemini_key),
            "openai": bool(openai_key),
        },
        "google_client_id": google_cid or None,
        "user": user,
    })


@ai_bp.route("/auth/google", methods=["POST"])
def auth_google():
    """Autentificare prin Google Sign-In (credential JWT)."""
    data = request.get_json() or {}
    cred = data.get("credential")
    if not cred:
        return jsonify({"ok": False, "error": "Lipsește tokenul credential Google."}), 400

    try:
        payload = decode_google_jwt(cred)
        user_info = {
            "name": payload.get("name", "Medic Utilizator"),
            "email": payload.get("email", ""),
            "picture": payload.get("picture", ""),
            "sub": payload.get("sub", ""),
            "auth_type": "google",
        }
        session["user"] = user_info
        return jsonify({"ok": True, "user": user_info})
    except Exception as e:
        return jsonify({"ok": False, "error": f"Eroare la decodare token: {e}"}), 400


@ai_bp.route("/auth/quick", methods=["POST"])
def auth_quick():
    """Autentificare clinică rapidă (Doctor/Radiolog/Tehnician) fără OAuth extern."""
    data = request.get_json() or {}
    role = data.get("role", "Medic Radiolog")
    name = data.get("name", "Dr. Utilizator")

    user_info = {
        "name": name,
        "email": f"{name.lower().replace(' ', '.')}@radiologie.spital.ro",
        "picture": "https://api.dicebear.com/7.x/bottts/svg?seed=" + name,
        "role": role,
        "auth_type": "quick",
    }
    session["user"] = user_info
    return jsonify({"ok": True, "user": user_info})


@ai_bp.route("/auth/logout", methods=["POST"])
def auth_logout():
    """Deconectare utilizator."""
    session.pop("user", None)
    return jsonify({"ok": True})


@ai_bp.route("/chat", methods=["POST"])
def chat():
    """Punct de acces principal pentru asistentul AI."""
    data = request.get_json() or {}
    query = (data.get("message") or "").strip()
    provider = (data.get("provider") or "gemini").lower()
    mode = data.get("mode", "all")
    history = data.get("history", [])

    if not query:
        return jsonify({"ok": False, "error": "Mesajul nu poate fi gol."}), 400

    # Verificare context clinic relevant
    context = search_clinical_context(query)

    system_prompt = (
        "Ești Asistentul AI Clinic al Departamentului de Radiologie Medicală, specializat în Ghidul "
        "Național IRIS (Ordinul MS 1342/2012) și Protocoalele Imagistice Medicale (Ecografie & Ultrasonografie US, IRM / RMN, CT, Radiografie clasică Rx, Fluoroscopie & C-Arm).\n"
        "Reguli obligatorii:\n"
        "1. Răspunde exclusiv în limba română, calm, profesional, concis și structurat.\n"
        "2. Respectă principiul ALARA: indică întotdeauna dacă ecografia sau IRM-ul sunt prioritare fără iradiere.\n"
        "3. Când recomanzi o examinare, menționează explicit gradul de recomandare (Grad A, B sau C) și nivelul de iradiere (Clasa 0 până la 4).\n"
        "4. Când menționezi protocoale de Ecografie (US), include detalii despre transductori (convex, liniar), moduri de lucru (Mod B, Doppler Color CFM, Pulsat PW) și repere / incidențe standard.\n"
        "5. Când menționezi protocoale IRM, include detalii despre antene, secvențe cheie (T1, T2, FLAIR, DWI, STIR) și agenți de contrast paramagnetic (Gadoliniu) dacă sunt relevante.\n"
        "6. Când menționezi protocoale CT, include detalii despre timpii de contrast, faze, kV, mAs și AEC dacă sunt relevante.\n"
        "7. Include link-uri markdown formatate către protocoalele menționate (ex: [Ecografie Abdominală](/radiology-protocols/eco/abdomen-pelvis/eco-abdomen-total/) sau [IRM Cerebral](/radiology-protocols/irm/neuro/irm-cerebral-nativ-si-cu-contrast/))."
    )

    reply_text = None
    engine_used = None

    # Încercare apel API extern conform furnizorului ales
    if provider == "gemini":
        try:
            reply_text, engine_used = call_gemini(query, system_prompt, context, history)
        except Exception as e:
            _safe_log(f"[AI Chat] Gemini API unavailable or failed: {e}")
            # Încercare cu OpenAI dacă e configurat
            try:
                reply_text, engine_used = call_openai(query, system_prompt, context, history)
            except Exception:
                pass
    elif provider == "openai":
        try:
            reply_text, engine_used = call_openai(query, system_prompt, context, history)
        except Exception as e:
            _safe_log(f"[AI Chat] OpenAI API unavailable or failed: {e}")
            try:
                reply_text, engine_used = call_gemini(query, system_prompt, context, history)
            except Exception:
                pass

    # Dacă apelurile externe eșuează sau cheile nu sunt valide, folosim fallback-ul clinic inteligent
    if not reply_text:
        reply_text = generate_local_clinical_reply(query, context)
        engine_used = "Baza Clinică Locală (IRIS, Eco, IRM, CT, Rx, Fluoro)"

    return jsonify({
        "ok": True,
        "reply": reply_text,
        "engine": engine_used,
        "context_matches": {
            "iris_count": len(context.get("iris", [])),
            "protocols_count": len(context.get("protocols", [])),
            "eco_count": len(context.get("eco", [])),
            "irm_count": len(context.get("irm", [])),
            "rx_count": len(context.get("rx", [])),
            "fluoro_count": len(context.get("fluoro", [])),
        },
    })
