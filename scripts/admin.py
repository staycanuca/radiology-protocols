"""admin.py — Flask admin app for editing CT protocol Markdown files.

Run with:
    python scripts/admin.py
from the repo root.
"""

from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import webbrowser
from datetime import date
from pathlib import Path

import yaml
from flask import Flask, jsonify, redirect, render_template_string, request, send_from_directory, url_for
from flask_cors import CORS

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
DOCS_CT = REPO_ROOT / "docs" / "ct"
DOCS_RX = REPO_ROOT / "docs" / "rx"
DOCS_FLUORO = REPO_ROOT / "docs" / "fluoro"
DOCS_IRM = REPO_ROOT / "docs" / "irm"
DOCS_ECO = REPO_ROOT / "docs" / "eco"
DOCS_ASSETS_IMAGES_PROTOCOLS = REPO_ROOT / "docs" / "assets" / "images" / "protocols"
SCRIPTS_DIR = REPO_ROOT / "scripts"

sys.path.insert(0, str(SCRIPTS_DIR))
from render_protocol import render_document  # noqa: E402
from render_rx_protocol import render_rx_document  # noqa: E402
from render_fluoro_protocol import render_fluoro_document  # noqa: E402
from render_irm_protocol import render_irm_document  # noqa: E402
from render_eco_protocol import render_eco_document  # noqa: E402
from ai_service import ai_bp  # noqa: E402

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "radiology-protocols-dev-key-clinical-2026")
CORS(app)
app.register_blueprint(ai_bp)

CT_CATEGORIES = ["abdomen", "cardiac", "chest", "msk", "neuro", "trauma", "vascular"]
RX_CATEGORIES = ["torace", "abdomen", "coloana", "craniu-saf", "membru-superior", "membru-inferior", "pediatrie"]
FLUORO_CATEGORIES = ["digestiv", "urinar", "c-arm", "pediatrie"]
IRM_CATEGORIES = ["neuro", "msk", "abdomen-pelvis", "cardiac", "san"]
ECO_CATEGORIES = ["abdomen-pelvis", "parti-moi-endocrin", "vascular-doppler", "msk", "san", "pediatrie"]
CATEGORIES = CT_CATEGORIES

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Return (fm_dict, body_str) or ({}, content) if no front matter."""
    if not content.startswith("---"):
        return {}, content
    # Find closing ---
    end = content.find("\n---\n", 3)
    if end == -1:
        # Try end of file variant
        end = content.find("\n---", 3)
        if end == -1:
            return {}, content
    yaml_str = content[3:end].strip()
    body = content[end + 4:]
    try:
        fm = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def load_all_protocols() -> list[dict]:
    """Return [{filepath: Path, fm: dict}] sorted by (modality, category, title)."""
    results = []
    for base_dir in (DOCS_CT, DOCS_RX, DOCS_FLUORO, DOCS_IRM, DOCS_ECO):
        if not base_dir.exists():
            continue
        for md_file in base_dir.rglob("*.md"):
            if md_file.name in ("index.md", "compare.md"):
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                fm, _ = parse_frontmatter(content)
                if fm and fm.get("slug"):
                    results.append({"filepath": md_file, "fm": fm})
            except Exception:
                pass
    results.sort(key=lambda x: (x["fm"].get("modality", "ct"), x["fm"].get("category", ""), x["fm"].get("title", "")))
    return results


def find_protocol(slug: str) -> dict | None:
    """Find protocol by slug from load_all_protocols()."""
    for item in load_all_protocols():
        if item["fm"].get("slug") == slug:
            return item
    return None


def _parse_form_images(form) -> list[dict]:
    """Parse images_json from form into list of image dicts."""
    raw = form.get("images_json", "[]")
    if not raw or not str(raw).strip():
        return []
    try:
        data = json.loads(raw)
        if not isinstance(data, list):
            return []
        cleaned = []
        for item in data:
            if isinstance(item, dict):
                url = str(item.get("url", "")).strip()
                caption = str(item.get("caption", "")).strip()
                desc = str(item.get("description", "")).strip()
                if url:
                    cleaned.append({
                        "url": url,
                        "caption": caption,
                        "description": desc,
                    })
            elif isinstance(item, str) and item.strip():
                cleaned.append({
                    "url": item.strip(),
                    "caption": "",
                    "description": "",
                })
        return cleaned
    except Exception:
        return []


def form_to_frontmatter(form) -> dict:
    """Parse Flask form POST data into YAML fm dict."""
    indications_raw = form.get("indications_json", "")
    indications = [line.strip() for line in indications_raw.splitlines() if line.strip()]

    series_raw = form.get("series_json", "[]")
    try:
        series = json.loads(series_raw)
    except (json.JSONDecodeError, ValueError):
        series = []

    recons_raw = form.get("recons_json", "[]")
    try:
        recons = json.loads(recons_raw)
    except (json.JSONDecodeError, ValueError):
        recons = []

    last_updated = form.get("last_updated", "").strip()
    if not last_updated:
        last_updated = str(date.today())

    synonyms_raw = form.get("synonyms", "")
    synonyms = [s.strip() for s in synonyms_raw.splitlines() if s.strip()]

    kv_val = (form.get("tech_kv_ct") or form.get("tech_kv", "")).strip()
    mas_val = (form.get("tech_mas_ct") or form.get("tech_mas", "")).strip()
    collimation_val = (form.get("tech_collimation_ct") or form.get("tech_collimation", "")).strip()
    position_val = (form.get("position_ct") or form.get("position", "")).strip()

    fm = {
        "title": form.get("title", "").strip(),
        "slug": form.get("slug", "").strip(),
        "category": form.get("category", "").strip(),
        "protocol_type": form.get("protocol_type", "").strip(),
        "last_updated": last_updated,
        "author": form.get("author", "").strip(),
        "synonyms": synonyms,
        "clinical_indications": indications,
        "position": position_val,
        "npo": form.get("npo", "").strip(),
        "premedication": form.get("premedication", "").strip(),
        "contrast": {
            "agent": form.get("contrast_agent", "").strip(),
            "volume": form.get("contrast_volume", "").strip(),
            "flow_rate": form.get("contrast_flow_rate", "").strip(),
            "duration": form.get("contrast_duration", "").strip(),
            "timing": form.get("contrast_timing", "").strip(),
            "roi": form.get("contrast_roi", "").strip(),
            "trigger": form.get("contrast_trigger", "").strip(),
        },
        "tech_params": {
            "kv": kv_val,
            "mas": mas_val,
            "aec": form.get("tech_aec", "").strip(),
            "slice_thickness": form.get("tech_slice", "").strip(),
            "collimation": collimation_val,
            "rotation_time": form.get("tech_rotation_time", "").strip(),
            "pitch": form.get("tech_pitch", "").strip(),
            "scan_mode": form.get("tech_scan_mode", "").strip(),
        },
        "series": series,
        "recons": recons,
        "images": _parse_form_images(form),
        "notes": {
            "tech": form.get("notes_tech", "").strip(),
            "nursing": form.get("notes_nursing", "").strip(),
            "rad": form.get("notes_rad", "").strip(),
            "tips": form.get("notes_tips", "").strip(),
        },
        "safety": {
            "renal": form.get("safety_renal", "").strip(),
            "allergy": form.get("safety_allergy", "").strip(),
        },
    }
    return fm


def form_to_rx_frontmatter(form) -> dict:
    """Parse Flask form POST data into Rx YAML frontmatter dict."""
    inds_raw = form.get("indications_json_rx") or form.get("indications_json", "")
    indications = [line.strip() for line in inds_raw.splitlines() if line.strip()]

    qual_raw = form.get("quality_criteria", "")
    quality = [line.strip() for line in qual_raw.splitlines() if line.strip()]

    prot_raw = form.get("protection", "")
    protection = [line.strip() for line in prot_raw.splitlines() if line.strip()]

    last_updated = form.get("last_updated", "").strip() or str(date.today())
    notes_val = form.get("notes_rx") or form.get("notes", "")
    if isinstance(notes_val, dict):
        notes_val = ""

    return {
        "title": form.get("title", "").strip(),
        "slug": form.get("slug", "").strip(),
        "category": form.get("category", "").strip() or "torace",
        "modality": "rx",
        "author": form.get("author", "").strip() or "Departamentul de Radiologie",
        "last_updated": last_updated,
        "position": form.get("position", "").strip(),
        "centering": form.get("centering", "").strip(),
        "breathing": form.get("breathing", "").strip(),
        "sid_dff": form.get("sid_dff", "").strip(),
        "tech_params": {
            "kv": form.get("tech_kv", "").strip(),
            "mas": form.get("tech_mas", "").strip(),
            "grid": form.get("tech_grid", "").strip(),
            "focal_spot": form.get("tech_focal_spot", "").strip(),
            "aec_chambers": form.get("tech_aec_chambers", "").strip(),
            "collimation": form.get("tech_collimation", "").strip(),
            "filtration": form.get("tech_filtration", "").strip(),
        },
        "clinical_indications": indications,
        "quality_criteria": quality,
        "protection": protection,
        "iris_reference": {
            "chapter": form.get("iris_chapter", "").strip(),
            "recommendation_grade": form.get("iris_grade", "").strip() or "Grad A",
            "radiation_dose": form.get("iris_dose", "").strip() or "Clasa 1 (Minimă < 1 mSv)",
        },
        "images": _parse_form_images(form),
        "notes": notes_val.strip(),
    }


def form_to_fluoro_frontmatter(form) -> dict:
    """Parse Flask form POST data into Fluoro YAML frontmatter dict."""
    inds_raw = form.get("indications_json_fluoro") or form.get("indications_json", "")
    indications = [line.strip() for line in inds_raw.splitlines() if line.strip()]

    contra_raw = form.get("contraindications", "")
    contraindications = [line.strip() for line in contra_raw.splitlines() if line.strip()]

    qual_raw = form.get("quality_criteria_fluoro") or form.get("quality_criteria", "")
    quality = [line.strip() for line in qual_raw.splitlines() if line.strip()]

    safety_raw = form.get("radiation_safety_fluoro") or form.get("radiation_safety", "")
    safety = [line.strip() for line in safety_raw.splitlines() if line.strip()]

    last_updated = form.get("last_updated", "").strip() or str(date.today())
    notes_val = form.get("notes_fluoro") or form.get("notes", "")
    if isinstance(notes_val, dict):
        notes_val = ""

    return {
        "title": form.get("title", "").strip(),
        "slug": form.get("slug", "").strip(),
        "category": form.get("category", "").strip() or "digestiv",
        "modality": "fluoro",
        "author": form.get("author", "").strip() or "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": last_updated,
        "clinical_indications": indications,
        "contraindications": contraindications,
        "patient_prep": form.get("patient_prep", "").strip(),
        "contrast": {
            "agent": form.get("contrast_agent_fluoro", "").strip(),
            "route": form.get("contrast_route_fluoro", "").strip(),
            "volume": form.get("contrast_volume_fluoro", "").strip(),
            "instructions": form.get("contrast_instructions_fluoro", "").strip(),
        },
        "positioning_equipment": {
            "patient_position": form.get("patient_position_fluoro", "").strip(),
            "equipment_setup": form.get("equipment_setup_fluoro", "").strip(),
            "sid": form.get("sid_fluoro", "").strip(),
        },
        "fluoro_params": {
            "mode": form.get("fluoro_mode", "").strip(),
            "kv": form.get("fluoro_kv", "").strip(),
            "ma_range": form.get("fluoro_ma", "").strip(),
            "grid": form.get("fluoro_grid", "").strip(),
            "filtration": form.get("fluoro_filtration", "").strip(),
            "target_fluoro_time": form.get("fluoro_target_time", "").strip(),
            "lih": form.get("fluoro_lih", "").strip(),
        },
        "acquisition_steps": [],
        "quality_criteria": quality,
        "radiation_safety": safety,
        "iris_reference": {
            "chapter": form.get("iris_chapter", "").strip(),
            "recommendation_grade": form.get("iris_grade", "").strip() or "Grad A",
            "radiation_dose": form.get("iris_dose", "").strip() or "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "images": _parse_form_images(form),
        "notes": notes_val.strip(),
    }


def form_to_irm_frontmatter(form) -> dict:
    """Parse Flask form POST data into IRM YAML frontmatter dict."""
    inds_raw = form.get("indications_json_irm") or form.get("indications_json", "")
    indications = [line.strip() for line in inds_raw.splitlines() if line.strip()]

    contra_raw = form.get("contraindications_irm") or form.get("contraindications", "")
    contraindications = [line.strip() for line in contra_raw.splitlines() if line.strip()]

    qual_raw = form.get("quality_criteria_irm") or form.get("quality_criteria", "")
    quality = [line.strip() for line in qual_raw.splitlines() if line.strip()]

    safety_raw = form.get("safety_considerations_irm") or form.get("safety_considerations", "")
    safety = [line.strip() for line in safety_raw.splitlines() if line.strip()]

    seqs_raw = form.get("sequences_json", "[]")
    try:
        sequences = json.loads(seqs_raw)
    except (json.JSONDecodeError, ValueError):
        sequences = []

    last_updated = form.get("last_updated", "").strip() or str(date.today())
    notes_val = form.get("notes_irm") or form.get("notes", "")
    if isinstance(notes_val, dict):
        notes_val = ""

    return {
        "title": form.get("title", "").strip(),
        "slug": form.get("slug", "").strip(),
        "category": form.get("category", "").strip() or "neuro",
        "modality": "irm",
        "author": form.get("author", "").strip() or "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": last_updated,
        "clinical_indications": indications,
        "contraindications": contraindications,
        "patient_prep": form.get("patient_prep_irm", "").strip(),
        "coils_hardware": {
            "coil": form.get("coil_irm", "").strip(),
            "field_strength": form.get("field_strength_irm", "").strip() or "1.5 Tesla / 3.0 Tesla",
            "positioning": form.get("positioning_irm", "").strip(),
        },
        "contrast": {
            "agent": form.get("contrast_agent_irm", "").strip(),
            "dose": form.get("contrast_dose_irm", "").strip(),
            "flow_rate": form.get("contrast_flow_rate_irm", "").strip(),
            "timing": form.get("contrast_timing_irm", "").strip(),
            "notes": form.get("contrast_notes_irm", "").strip(),
        },
        "sequences": sequences,
        "quality_criteria": quality,
        "safety_considerations": safety,
        "iris_reference": {
            "chapter": form.get("iris_chapter_irm") or form.get("iris_chapter", "").strip(),
            "recommendation_grade": form.get("iris_grade_irm") or form.get("iris_grade", "").strip() or "Grad A",
            "radiation_dose": form.get("iris_dose_irm") or form.get("iris_dose", "").strip() or "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "images": _parse_form_images(form),
        "notes": notes_val.strip(),
    }


def form_to_eco_frontmatter(form) -> dict:
    """Parse Flask form POST data into Ecography YAML frontmatter dict."""
    inds_raw = form.get("indications_json_eco") or form.get("indications_json", "")
    indications = [line.strip() for line in inds_raw.splitlines() if line.strip()]

    contra_raw = form.get("contraindications_eco") or form.get("contraindications", "")
    contraindications = [line.strip() for line in contra_raw.splitlines() if line.strip()]

    qual_raw = form.get("quality_criteria_eco") or form.get("quality_criteria", "")
    quality = [line.strip() for line in qual_raw.splitlines() if line.strip()]

    safety_raw = form.get("safety_and_limitations_eco") or form.get("safety_and_limitations", "")
    safety = [line.strip() for line in safety_raw.splitlines() if line.strip()]

    views_raw = form.get("views_json", "[]")
    try:
        views = json.loads(views_raw)
    except (json.JSONDecodeError, ValueError):
        views = []

    last_updated = form.get("last_updated", "").strip() or str(date.today())
    notes_val = form.get("notes_eco") or form.get("notes", "")
    if isinstance(notes_val, dict):
        notes_val = ""

    return {
        "title": form.get("title", "").strip(),
        "slug": form.get("slug", "").strip(),
        "category": form.get("category", "").strip() or "abdomen-pelvis",
        "modality": "eco",
        "author": form.get("author", "").strip() or "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": last_updated,
        "clinical_indications": indications,
        "contraindications": contraindications,
        "patient_prep": form.get("patient_prep_eco", "").strip(),
        "transducers_equipment": {
            "transducer_types": form.get("transducers_types_eco", "").strip(),
            "patient_position": form.get("patient_position_eco", "").strip(),
            "gel_acoustic_window": form.get("gel_acoustic_window_eco", "").strip(),
        },
        "technical_settings": {
            "preset": form.get("preset_eco", "").strip(),
            "modes": form.get("modes_eco", "").strip(),
            "focus_depth": form.get("focus_depth_eco", "").strip(),
            "gain_thi": form.get("gain_thi_eco", "").strip(),
            "measurements_criteria": form.get("measurements_criteria_eco", "").strip(),
        },
        "standard_views": views,
        "quality_criteria": quality,
        "safety_and_limitations": safety,
        "iris_reference": {
            "chapter": form.get("iris_chapter_eco") or form.get("iris_chapter", "").strip(),
            "recommendation_grade": form.get("iris_grade_eco") or form.get("iris_grade", "").strip() or "Grad A",
            "radiation_dose": form.get("iris_dose_eco") or form.get("iris_dose", "").strip() or "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "images": _parse_form_images(form),
        "notes": notes_val.strip(),
    }




def apply_changes_to_fm(fm: dict, changes: dict) -> tuple[dict, set]:
    """Overlay a flat changesMap (field_name -> value) onto an fm dict.

    Returns (updated_fm, highlighted_fields) where highlighted_fields is the set
    of form field names that were changed.
    """
    CONTRAST_FIELDS = {
        "contrast_agent": "agent", "contrast_volume": "volume",
        "contrast_flow_rate": "flow_rate", "contrast_duration": "duration",
        "contrast_timing": "timing", "contrast_roi": "roi", "contrast_trigger": "trigger",
    }
    TECH_FIELDS = {
        "tech_kv": "kv", "tech_mas": "mas", "tech_aec": "aec",
        "tech_slice": "slice_thickness", "tech_collimation": "collimation",
        "tech_rotation_time": "rotation_time", "tech_pitch": "pitch",
        "tech_scan_mode": "scan_mode",
    }
    NOTES_FIELDS = {
        "notes_tech": "tech", "notes_nursing": "nursing",
        "notes_rad": "rad", "notes_tips": "tips",
    }
    SAFETY_FIELDS = {"safety_renal": "renal", "safety_allergy": "allergy"}

    highlighted = set()
    for key, value in changes.items():
        if key in CONTRAST_FIELDS:
            fm.setdefault("contrast", {})[CONTRAST_FIELDS[key]] = value
            highlighted.add(key)
        elif key in TECH_FIELDS:
            fm.setdefault("tech_params", {})[TECH_FIELDS[key]] = value
            highlighted.add(key)
        elif key in NOTES_FIELDS:
            fm.setdefault("notes", {})[NOTES_FIELDS[key]] = value
            highlighted.add(key)
        elif key in SAFETY_FIELDS:
            fm.setdefault("safety", {})[SAFETY_FIELDS[key]] = value
            highlighted.add(key)
        elif key == "indications_json":
            fm["clinical_indications"] = [l.strip() for l in value.splitlines() if l.strip()]
            highlighted.add(key)
        elif key == "series_json":
            try:
                fm["series"] = json.loads(value)
            except (json.JSONDecodeError, ValueError):
                pass
            highlighted.add(key)
        elif key == "images_json":
            try:
                fm["images"] = json.loads(value)
            except (json.JSONDecodeError, ValueError):
                pass
            highlighted.add(key)
        elif key in ("title", "category", "protocol_type", "position", "npo", "premedication", "author"):
            fm[key] = value
            highlighted.add(key)
    return fm, highlighted


def rebuild_indexes() -> list[str]:
    """Run index-generation scripts via subprocess. Returns list of failure messages."""
    scripts = [
        "generate_comparison_index.py",
        "generate_sitemap.py",
        "generate_forms_index.py",
    ]
    failures = []
    for script in scripts:
        script_path = SCRIPTS_DIR / script
        if script_path.exists():
            try:
                result = subprocess.run(
                    [sys.executable, str(script_path)],
                    cwd=str(REPO_ROOT),
                    timeout=30,
                    check=False,
                    capture_output=True,
                    text=True,
                )
                if result.returncode != 0:
                    failures.append(f"{script} failed: {result.stderr.strip() or 'non-zero exit'}")
            except Exception as exc:
                failures.append(f"{script} error: {exc}")
    return failures


def trigger_background_build():
    """Trigger mkdocs build in background thread to keep site/ up to date."""
    import threading

    def _build():
        try:
            subprocess.run(
                [sys.executable, "-m", "mkdocs", "build"],
                cwd=str(REPO_ROOT),
                timeout=60,
                capture_output=True,
            )
        except Exception:
            pass

    threading.Thread(target=_build, daemon=True).start()


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

LIST_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Protocol Manager Admin</title>
<style>
  *, *::before, *::after { box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
         margin: 0; background: #f5f5f5; color: #222; }
  .navbar { background: #1a237e; color: white; padding: 0.75rem 1.5rem;
            display: flex; align-items: center; justify-content: space-between; }
  .navbar h1 { margin: 0; font-size: 1.25rem; font-weight: 600; }
  .btn { display: inline-block; padding: 0.45rem 1rem; border-radius: 4px;
         text-decoration: none; font-size: 0.9rem; cursor: pointer; border: none; }
  .btn-primary { background: #1565c0; color: white; }
  .btn-primary:hover { background: #0d47a1; }
  .btn-sm { padding: 0.3rem 0.7rem; font-size: 0.82rem; }
  .btn-outline { background: transparent; border: 1px solid #1565c0;
                 color: #1565c0; }
  .btn-outline:hover { background: #e3f2fd; }
  .content { max-width: 1100px; margin: 1.5rem auto; padding: 0 1rem; }
  .search-bar { margin-bottom: 1rem; }
  .search-bar input { width: 100%; padding: 0.5rem 0.75rem; border: 1px solid #ccc;
                      border-radius: 4px; font-size: 1rem; }
  table { width: 100%; border-collapse: collapse; background: white;
          border-radius: 6px; overflow: hidden;
          box-shadow: 0 1px 3px rgba(0,0,0,.1); }
  th { background: #e8eaf6; text-align: left; padding: 0.7rem 1rem;
       font-size: 0.85rem; text-transform: uppercase; letter-spacing: .04em; }
  td { padding: 0.65rem 1rem; border-bottom: 1px solid #f0f0f0; font-size: 0.95rem; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafafa; }
  .badge { display: inline-block; padding: 0.2em 0.6em; border-radius: 3px;
           font-size: 0.78rem; font-weight: 600; background: #e8eaf6; color: #3949ab; }
  .count { color: #777; font-size: 0.9rem; margin-bottom: 0.5rem; }
</style>
</head>
<body>
<nav class="navbar">
  <h1>Administrare Protocoale Radiologie</h1>
  <div style="display: flex; gap: 0.75rem; align-items: center;">
    <a href="http://localhost:8000/radiology-protocols/" target="_blank" class="btn btn-outline" style="color: white; border-color: rgba(255,255,255,0.6); font-size: 0.85rem;">📖 Deschide Ghidul (Port 8000) ↗</a>
    <a href="/new" class="btn btn-primary">+ Protocol Nou</a>
  </div>
</nav>
<div class="content">
  <div class="search-bar">
    <input type="text" id="search" placeholder="Caută protocoale după titlu…" oninput="filterTable()">
  </div>
  <p class="count" id="count">{{ protocols|length }} protocoale</p>
  <table id="proto-table">
    <thead>
      <tr>
        <th style="width: 110px;">Modalitate</th>
        <th>Titlu</th>
        <th>Categorie</th>
        <th>Ultima Actualizare</th>
        <th>Acțiuni</th>
      </tr>
    </thead>
    <tbody>
      {% for p in protocols %}
      <tr>
        <td>
          {% if p.fm.modality == 'eco' %}
          <span class="badge" style="background:#f7fee7; color:#3f6212; border:1px solid #bef264;">📡 Eco</span>
          {% elif p.fm.modality == 'irm' %}
          <span class="badge" style="background:#f0fdfa; color:#0f766e; border:1px solid #99f6e4;">🧲 IRM</span>
          {% elif p.fm.modality == 'fluoro' %}
          <span class="badge" style="background:#ecfdf5; color:#047857; border:1px solid #a7f3d0;">✨ Fluoro</span>
          {% elif p.fm.modality == 'rx' %}
          <span class="badge" style="background:#e0f2fe; color:#0369a1; border:1px solid #bae6fd;">📷 Rx</span>
          {% else %}
          <span class="badge" style="background:#ede7f6; color:#4527a0; border:1px solid #d1c4e9;">⚡ CT</span>
          {% endif %}
        </td>
        <td><strong>{{ p.fm.title }}</strong></td>
        <td><span class="badge">{{ p.fm.category }}</span></td>
        <td>{{ p.fm.last_updated }}</td>
        <td style="white-space: nowrap;">
          <a href="/edit/{{ p.fm.slug }}" class="btn btn-sm btn-outline">Editează</a>
          <a href="http://localhost:8000/radiology-protocols/{{ p.fm.modality or 'ct' }}/{{ p.fm.category }}/{{ p.fm.slug }}/" target="_blank" class="btn btn-sm btn-outline" style="margin-left: 4px;" title="Deschide în Ghidul de Protocoale (Port 8000)">👁️ Ghid ↗</a>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
<script>
function filterTable() {
  const q = document.getElementById('search').value.toLowerCase();
  const rows = document.querySelectorAll('#proto-table tbody tr');
  let visible = 0;
  rows.forEach(row => {
    const text = row.textContent.toLowerCase();
    const show = text.includes(q);
    row.style.display = show ? '' : 'none';
    if (show) visible++;
  });
  document.getElementById('count').textContent = visible + ' protocoale';
}
</script>
</body>
</html>"""


FORM_TEMPLATE = """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ page_title }} — Protocol Manager</title>
<style>
  *, *::before, *::after { box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
         margin: 0; background: #f5f5f5; color: #222; }
  .navbar { background: #1a237e; color: white; padding: 0.75rem 1.5rem;
            display: flex; align-items: center; gap: 1rem; }
  .navbar h1 { margin: 0; font-size: 1.15rem; font-weight: 600; }
  .navbar a { color: rgba(255,255,255,.75); text-decoration: none; font-size: 0.9rem; }
  .navbar a:hover { color: white; }
  .content { max-width: 940px; margin: 1.5rem auto; padding: 0 1rem 3rem; }
  .section { background: white; border-radius: 6px; padding: 1.25rem 1.5rem;
             margin-bottom: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,.08); }
  .section h2 { margin: 0 0 1rem; font-size: 1rem; font-weight: 700;
                color: #1a237e; text-transform: uppercase; letter-spacing: .04em;
                border-bottom: 2px solid #e8eaf6; padding-bottom: 0.5rem; display: flex; align-items: center; justify-content: space-between; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem 1rem; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.75rem 1rem; }
  .grid-4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 0.75rem 1rem; }
  .span-full { grid-column: 1 / -1; }
  label { display: block; font-size: 0.82rem; font-weight: 600; color: #555;
          margin-bottom: 0.25rem; }
  input[type=text], input[type=date], select, textarea {
    width: 100%; padding: 0.4rem 0.6rem; border: 1px solid #d0d0d0;
    border-radius: 4px; font-size: 0.92rem; font-family: inherit;
    background: white; transition: border-color .15s; }
  input:focus, select:focus, textarea:focus {
    outline: none; border-color: #1565c0; box-shadow: 0 0 0 2px rgba(21,101,192,.15); }
  input[readonly] { background: #f5f5f5; color: #777; }
  textarea { resize: vertical; }
  /* Dynamic rows */
  .dynamic-row { border: 1px solid #e0e0e0; border-radius: 4px; padding: 0.75rem;
                 margin-bottom: 0.6rem; background: #fafafa; position: relative; }
  .dynamic-row .row-grid { display: grid; gap: 0.5rem 0.75rem; }
  .series-row-grid { grid-template-columns: 2fr 1fr 1fr 1fr 1fr; }
  .recon-row-grid { grid-template-columns: 1fr 1fr 1fr 1fr 1fr; }
  .recon-row-grid2 { grid-template-columns: 1fr 1fr 1fr; margin-top: 0.5rem; }
  .row-actions { position: absolute; top: 0.5rem; right: 0.5rem;
                 display: flex; gap: 0.25rem; }
  .remove-btn { background: #fbe9e7; color: #c62828; border: 1px solid #ef9a9a;
                border-radius: 3px; padding: 0.15rem 0.5rem; cursor: pointer;
                font-size: 0.78rem; }
  .remove-btn:hover { background: #ffcdd2; }
  .move-btn { background: #eeeeee; color: #444; border: 1px solid #bdbdbd;
              border-radius: 3px; padding: 0.15rem 0.4rem; cursor: pointer;
              font-size: 0.75rem; line-height: 1; }
  .move-btn:hover { background: #e0e0e0; }
  .add-btn { background: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7;
             border-radius: 4px; padding: 0.35rem 0.85rem; cursor: pointer;
             font-size: 0.85rem; margin-top: 0.4rem; }
  .add-btn:hover { background: #c8e6c9; }
  .action-bar { display: flex; align-items: center; gap: 1rem; margin-top: 1.5rem; }
  .btn-save { background: #1565c0; color: white; border: none; border-radius: 4px;
              padding: 0.6rem 1.75rem; font-size: 1rem; cursor: pointer; font-weight: 600; }
  .btn-save:hover { background: #0d47a1; }
  #status { font-size: 0.92rem; font-weight: 500; }
  .ok { color: #2e7d32; }
  .err { color: #c62828; }
  /* Base protocol picker */
  .base-picker { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; }
  .base-picker select { flex: 1; }
  .base-picker button { white-space: nowrap; background: #e3f2fd; color: #1565c0;
                        border: 1px solid #90caf9; border-radius: 4px;
                        padding: 0.4rem 0.85rem; cursor: pointer; font-size: 0.88rem; }
  .badge { display: inline-block; padding: 0.2em 0.6em; border-radius: 3px;
           font-size: 0.8rem; font-weight: 600; }
  /* Change request review */
  .apply-highlight { background: #fffbe6 !important; border-color: #f0ad00 !important; }
  .review-banner { background: #fff8e1; border: 1px solid #f0ad00; border-radius: 6px;
                   padding: 0.75rem 1.25rem; margin-bottom: 1.25rem; font-size: 0.92rem;
                   color: #5c4000; }
  .review-banner strong { color: #3d2a00; }
</style>
</head>
<body>
<nav class="navbar">
  <a href="/">← Înapoi la Listă</a>
  <h1>{{ page_title }}</h1>
  {% if not is_new and frontend_url %}
  <a href="{{ frontend_url }}" target="_blank" class="btn btn-outline" style="color: white; border-color: rgba(255,255,255,0.6); margin-left: auto; text-decoration: none; font-size: 0.85rem;" title="Deschide pagina în Ghidul de Protocoale (Port 8000)">👁️ Previzualizează în Ghid (Port 8000) ↗</a>
  {% endif %}
  {% if is_eco %}
  <span class="badge" style="{% if is_new or not frontend_url %}margin-left:auto;{% endif %} background:#f7fee7; color:#3f6212; font-size:0.85rem; padding:0.35rem 0.8rem; border:1px solid #bef264;">📡 Ecografie &amp; Ultrasonografie (US)</span>
  {% elif is_irm %}
  <span class="badge" style="{% if is_new or not frontend_url %}margin-left:auto;{% endif %} background:#f0fdfa; color:#0f766e; font-size:0.85rem; padding:0.35rem 0.8rem; border:1px solid #99f6e4;">🧲 Rezonanță Magnetică (IRM)</span>
  {% elif is_fluoro %}
  <span class="badge" style="{% if is_new or not frontend_url %}margin-left:auto;{% endif %} background:#ecfdf5; color:#047857; font-size:0.85rem; padding:0.35rem 0.8rem; border:1px solid #a7f3d0;">✨ Fluoroscopie &amp; C-Arm</span>
  {% elif is_rx %}
  <span class="badge" style="{% if is_new or not frontend_url %}margin-left:auto;{% endif %} background:#e0f2fe; color:#0369a1; font-size:0.85rem; padding:0.35rem 0.8rem; border:1px solid #bae6fd;">📷 Radiografie Convențională (Rx)</span>
  {% else %}
  <span class="badge" style="{% if is_new or not frontend_url %}margin-left:auto;{% endif %} background:#ede7f6; color:#4527a0; font-size:0.85rem; padding:0.35rem 0.8rem; border:1px solid #d1c4e9;">⚡ Tomografie Computerizată (CT)</span>
  {% endif %}
</nav>
<div class="content">

{% if reviewing_request == true %}
<div class="review-banner">
  <strong>Examinare propunere de modificare</strong> — câmpurile evidențiate conțin valorile propuse. Verificați și apăsați Salvează pentru aplicare.
</div>
{% elif reviewing_request %}
<div class="review-banner" style="background:#fff3cd;border-color:#ffc107;color:#664d03;">
  <strong>Atenție:</strong> {{ reviewing_request }}
</div>
{% endif %}

{% if is_new %}
<div class="section">
  <h2>Protocol de Bază (șablon opțional)</h2>
  <p style="font-size: 0.88rem; color: #666; margin-top: -0.5rem; margin-bottom: 0.75rem;">
    Puteți alege un protocol existent din orice modalitate pentru a pre-completa automat parametrii tehnici și secțiunile clinice.
  </p>
  <div class="base-picker">
    <select id="base-select" style="max-width: 600px;">
      <option value="">— începe de la zero (sau alege un protocol pentru clonare) —</option>
      <optgroup label="⚡ CT — Tomografie Computerizată">
        {% for p in all_protocols if (p.fm.modality or 'ct') == 'ct' %}
        <option value="{{ p.fm.slug }}">{{ p.fm.title }}</option>
        {% endfor %}
      </optgroup>
      <optgroup label="🧲 IRM — Rezonanță Magnetică">
        {% for p in all_protocols if p.fm.modality == 'irm' %}
        <option value="{{ p.fm.slug }}">{{ p.fm.title }}</option>
        {% endfor %}
      </optgroup>
      <optgroup label="📷 RX — Radiografie Convențională">
        {% for p in all_protocols if p.fm.modality == 'rx' %}
        <option value="{{ p.fm.slug }}">{{ p.fm.title }}</option>
        {% endfor %}
      </optgroup>
      <optgroup label="📡 US — Ecografie &amp; Ultrasonografie">
        {% for p in all_protocols if p.fm.modality == 'eco' %}
        <option value="{{ p.fm.slug }}">{{ p.fm.title }}</option>
        {% endfor %}
      </optgroup>
      <optgroup label="✨ FLOURO — Fluoroscopie &amp; C-Arm">
        {% for p in all_protocols if p.fm.modality == 'fluoro' %}
        <option value="{{ p.fm.slug }}">{{ p.fm.title }}</option>
        {% endfor %}
      </optgroup>
    </select>
    <button type="button" class="btn btn-primary" onclick="loadBase()">Încarcă</button>
    <span id="base-load-status" style="font-size: 0.88rem; font-weight: 600; margin-left: 0.5rem;"></span>
  </div>
</div>
{% endif %}

<form id="proto-form">

<div class="section">
  <h2>Identificare Protocol</h2>
  <div class="grid-2">
    <div>
      <label for="title">Titlu Protocol</label>
      <input type="text" id="title" name="title" value="{{ fm.title }}"
             class="{{ 'apply-highlight' if 'title' in highlighted else '' }}"
             oninput="{% if is_new %}autoSlug(){% endif %}">
    </div>
    <div>
      <label for="slug">Identificator URL (Slug)</label>
      <input type="text" id="slug" name="slug" value="{{ fm.slug }}"
             {% if not is_new %}readonly{% endif %}>
    </div>
    <div>
      <label for="category">Categorie Diagnostică</label>
      <select id="category" name="category" class="{{ 'apply-highlight' if 'category' in highlighted else '' }}">
        {% for cat in categories %}
        <option value="{{ cat }}" {% if fm.category == cat %}selected{% endif %}>{{ cat }}</option>
        {% endfor %}
      </select>
    </div>
    <div>
      <label>Modalitate Radiologică</label>
      {% if is_new %}
      <div style="display:flex; gap:1.25rem; margin-top:0.4rem; flex-wrap:wrap;">
        <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
          <input type="radio" name="modality_radio" value="ct" {% if not is_rx and not is_fluoro and not is_irm and not is_eco %}checked{% endif %} onchange="switchModality('ct')">
          <span class="badge" style="background:#ede7f6; color:#4527a0;">⚡ Tomografie (CT)</span>
        </label>
        <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
          <input type="radio" name="modality_radio" value="rx" {% if is_rx %}checked{% endif %} onchange="switchModality('rx')">
          <span class="badge" style="background:#e0f2fe; color:#0369a1;">📷 Radiografie (Rx)</span>
        </label>
        <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
          <input type="radio" name="modality_radio" value="fluoro" {% if is_fluoro %}checked{% endif %} onchange="switchModality('fluoro')">
          <span class="badge" style="background:#ecfdf5; color:#047857;">✨ Fluoroscopie &amp; C-Arm</span>
        </label>
        <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
          <input type="radio" name="modality_radio" value="irm" {% if is_irm %}checked{% endif %} onchange="switchModality('irm')">
          <span class="badge" style="background:#f0fdfa; color:#0f766e;">🧲 Rezonanță Magnetică (IRM)</span>
        </label>
        <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
          <input type="radio" name="modality_radio" value="eco" {% if is_eco %}checked{% endif %} onchange="switchModality('eco')">
          <span class="badge" style="background:#f7fee7; color:#3f6212;">📡 Ecografie (US)</span>
        </label>
      </div>
      <input type="hidden" name="modality" id="modality" value="{{ 'eco' if is_eco else ('irm' if is_irm else ('fluoro' if is_fluoro else ('rx' if is_rx else 'ct'))) }}">
      {% else %}
      <input type="hidden" name="modality" id="modality" value="{{ 'eco' if is_eco else ('irm' if is_irm else ('fluoro' if is_fluoro else ('rx' if is_rx else 'ct'))) }}">
      <input type="text" readonly value="{{ '📡 Ecografie & Ultrasonografie (US)' if is_eco else ('🧲 Rezonanță Magnetică (IRM)' if is_irm else ('✨ Fluoroscopie & C-Arm' if is_fluoro else ('📷 Radiografie Convențională (Rx)' if is_rx else '⚡ Tomografie Computerizată (CT)'))) }}">
      {% endif %}
    </div>
    <div>
      <label for="last_updated">Ultima Actualizare</label>
      <input type="date" id="last_updated" name="last_updated" value="{{ fm.last_updated }}">
    </div>
    <div>
      <label for="author">Autor / Departament</label>
      <input type="text" id="author" name="author" value="{{ fm.author }}">
    </div>
    <div id="ct-ident-type" style="{% if is_rx or is_fluoro or is_irm or is_eco %}display:none;{% endif %}">
      <label for="protocol_type">Tip Protocol CT</label>
      <input type="text" id="protocol_type" name="protocol_type" value="{{ fm.protocol_type }}">
    </div>
    <div id="ct-ident-syn" class="span-full" style="{% if is_rx or is_fluoro or is_irm or is_eco %}display:none;{% endif %}">
      <label for="synonyms">Sinonime (unul pe linie)</label>
      <textarea id="synonyms" name="synonyms" rows="2">{{ fm.synonyms | join('\n') if fm.synonyms else '' }}</textarea>
    </div>
  </div>
</div>

<!-- ======================= SECTIUNI RX ======================= -->
<div id="rx-fields" style="{% if not is_rx %}display:none;{% endif %}">
  <div class="section">
    <h2>Poziționare &amp; Centrare Fascicul (Rx)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="position">Poziție Pacient &amp; Incidență</label>
        <textarea id="position" name="position" rows="3">{{ fm.position if is_rx else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="centering">Punct de Centrare Fascicul Raze X</label>
        <textarea id="centering" name="centering" rows="2">{{ fm.centering if is_rx else '' }}</textarea>
      </div>
      <div>
        <label for="sid_dff">Distanță Focar-Film (DFF / SID)</label>
        <input type="text" id="sid_dff" name="sid_dff" value="{{ fm.sid_dff if is_rx else '' }}" placeholder="ex. 100 - 115 cm sau 150 - 180 cm">
      </div>
      <div>
        <label for="breathing">Comandă Respiratorie</label>
        <input type="text" id="breathing" name="breathing" value="{{ fm.breathing if is_rx else '' }}" placeholder="ex. Apnee în inspir profund / expir / liniștit">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Parametri Tehnici Expunere (Rx)</h2>
    <div class="grid-3">
      <div>
        <label for="tech_kv">Tensiune Tub (kV)</label>
        <input type="text" id="tech_kv" name="tech_kv" value="{{ fm.tech_params.kv if is_rx and fm.tech_params else '' }}" placeholder="ex. 75 - 85">
      </div>
      <div>
        <label for="tech_mas">Sarcină Curent-Timp (mAs)</label>
        <input type="text" id="tech_mas" name="tech_mas" value="{{ fm.tech_params.mas if is_rx and fm.tech_params else '' }}" placeholder="ex. 20 - 35 (AEC)">
      </div>
      <div>
        <label for="tech_grid">Grilă Antidifuzoare</label>
        <input type="text" id="tech_grid" name="tech_grid" value="{{ fm.tech_params.grid if is_rx and fm.tech_params else '' }}" placeholder="ex. Cu grilă antidifuzoare Bucky / Fără grilă">
      </div>
      <div>
        <label for="tech_focal_spot">Dimensiune Focar</label>
        <input type="text" id="tech_focal_spot" name="tech_focal_spot" value="{{ fm.tech_params.focal_spot if is_rx and fm.tech_params else '' }}" placeholder="ex. Focar Mare (1.0 - 1.2 mm) / Focar Mic">
      </div>
      <div>
        <label for="tech_aec_chambers">Camere de Ionizare AEC</label>
        <input type="text" id="tech_aec_chambers" name="tech_aec_chambers" value="{{ fm.tech_params.aec_chambers if is_rx and fm.tech_params else '' }}" placeholder="ex. Camerele laterale / Centrală">
      </div>
      <div>
        <label for="tech_collimation">Colimare Fascicul</label>
        <input type="text" id="tech_collimation" name="tech_collimation" value="{{ fm.tech_params.collimation if is_rx and fm.tech_params else '' }}" placeholder="ex. Strictă pe regiunea de interes anatomic">
      </div>
      <div class="span-full">
        <label for="tech_filtration">Filtrare Tub</label>
        <input type="text" id="tech_filtration" name="tech_filtration" value="{{ fm.tech_params.filtration if is_rx and fm.tech_params else '' }}" placeholder="ex. Totală ≥ 2.5 mm Al echivalent">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Clinic &amp; Referință Ghid Național IRIS (Rx)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="indications_json_rx">Indicații Clinice (una pe linie)</label>
        <textarea id="indications_json_rx" name="indications_json_rx" rows="4">{{ fm.clinical_indications | join('\n') if is_rx else '' }}</textarea>
      </div>
      <div>
        <label for="iris_chapter">Capitol Ghid Național IRIS</label>
        <input type="text" id="iris_chapter" name="iris_chapter" value="{{ fm.iris_reference.chapter if is_rx and fm.iris_reference else '' }}" placeholder="ex. Torace, Coloană, Membre">
      </div>
      <div>
        <label for="iris_grade">Grad de Recomandare IRIS</label>
        <input type="text" id="iris_grade" name="iris_grade" value="{{ fm.iris_reference.recommendation_grade if is_rx and fm.iris_reference else '' }}" placeholder="ex. Grad A / Grad B">
      </div>
      <div class="span-full">
        <label for="iris_dose">Nivel Iradiere Estimată (Ghid IRIS)</label>
        <input type="text" id="iris_dose" name="iris_dose" value="{{ fm.iris_reference.radiation_dose if is_rx and fm.iris_reference else '' }}" placeholder="ex. Clasa 1 (Minimă < 0.1 mSv)">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Criterii de Calitate &amp; Radioprotecție ALARA (Rx)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="quality_criteria">Criterii de Calitate a Imaginii (una pe linie)</label>
        <textarea id="quality_criteria" name="quality_criteria" rows="4">{{ fm.quality_criteria | join('\n') if is_rx else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="protection">Măsuri de Radioprotecție ALARA (una pe linie)</label>
        <textarea id="protection" name="protection" rows="3">{{ fm.protection | join('\n') if is_rx else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="notes_rx">Observații &amp; Notițe Clinico-Tehnice</label>
        <textarea id="notes_rx" name="notes_rx" rows="2">{{ fm.notes if is_rx and fm.notes is string else '' }}</textarea>
      </div>
    </div>
  </div>
</div>

<!-- ======================= SECTIUNI FLUORO & C-ARM ======================= -->
<div id="fluoro-fields" style="{% if not is_fluoro %}display:none;{% endif %}">
  <div class="section">
    <h2>Clinic, Indicații &amp; Contraindicații (Fluoroscopie &amp; C-Arm)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="indications_json_fluoro">Indicații Clinice (una pe linie)</label>
        <textarea id="indications_json_fluoro" name="indications_json_fluoro" rows="4">{{ fm.clinical_indications | join('\n') if is_fluoro else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="contraindications">Contraindicații &amp; Atenționări Speciale (una pe linie)</label>
        <textarea id="contraindications" name="contraindications" rows="3">{{ fm.contraindications | join('\n') if is_fluoro else '' }}</textarea>
      </div>
      <div>
        <label for="iris_chapter_fluoro">Capitol Ghid Național IRIS</label>
        <input type="text" id="iris_chapter_fluoro" name="iris_chapter" value="{{ fm.iris_reference.chapter if is_fluoro and fm.iris_reference else '' }}" placeholder="ex. Tub Digestiv, Aparat Urinar, Traumatologie">
      </div>
      <div>
        <label for="iris_grade_fluoro">Grad de Recomandare IRIS</label>
        <input type="text" id="iris_grade_fluoro" name="iris_grade" value="{{ fm.iris_reference.recommendation_grade if is_fluoro and fm.iris_reference else '' }}" placeholder="ex. Grad A / Grad B">
      </div>
      <div class="span-full">
        <label for="iris_dose_fluoro">Nivel Iradiere Estimată (Ghid IRIS)</label>
        <input type="text" id="iris_dose_fluoro" name="iris_dose" value="{{ fm.iris_reference.radiation_dose if is_fluoro and fm.iris_reference else '' }}" placeholder="ex. Clasa 1 (< 1 mSv) / Clasa 2 (1 - 5 mSv)">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Pregătire Pacient &amp; Substanță de Contrast (Fluoroscopie)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="patient_prep">Pregătire Pacient (À jeun, lavaj, toaletă antiseptică)</label>
        <textarea id="patient_prep" name="patient_prep" rows="2">{{ fm.patient_prep if is_fluoro else '' }}</textarea>
      </div>
      <div>
        <label for="contrast_agent_fluoro">Agent de Contrast</label>
        <input type="text" id="contrast_agent_fluoro" name="contrast_agent_fluoro" value="{{ fm.contrast.agent if is_fluoro and fm.contrast else '' }}" placeholder="ex. Sulfat de Bariu / Iodat hidrosolubil non-ionic">
      </div>
      <div>
        <label for="contrast_route_fluoro">Cale de Administrare</label>
        <input type="text" id="contrast_route_fluoro" name="contrast_route_fluoro" value="{{ fm.contrast.route if is_fluoro and fm.contrast else '' }}" placeholder="ex. Orală / Retrogradă vezicală / Pe cateter">
      </div>
      <div>
        <label for="contrast_volume_fluoro">Volum &amp; Diluție</label>
        <input type="text" id="contrast_volume_fluoro" name="contrast_volume_fluoro" value="{{ fm.contrast.volume if is_fluoro and fm.contrast else '' }}" placeholder="ex. 150 - 250 ml / diluat 1:1 cu ser fiziologic">
      </div>
      <div>
        <label for="contrast_instructions_fluoro">Instrucțiuni Specifice Contrast</label>
        <input type="text" id="contrast_instructions_fluoro" name="contrast_instructions_fluoro" value="{{ fm.contrast.instructions if is_fluoro and fm.contrast else '' }}" placeholder="ex. Fără bule de aer / încălzit la 37°C">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Poziționare Pacient &amp; Configurare Echipament (Masă / C-Arm)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="patient_position_fluoro">Poziție Pacient</label>
        <textarea id="patient_position_fluoro" name="patient_position_fluoro" rows="2">{{ fm.positioning_equipment.patient_position if is_fluoro and fm.positioning_equipment else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="equipment_setup_fluoro">Configurare Echipament / Braț C Mobil</label>
        <textarea id="equipment_setup_fluoro" name="equipment_setup_fluoro" rows="2">{{ fm.positioning_equipment.equipment_setup if is_fluoro and fm.positioning_equipment else '' }}</textarea>
      </div>
      <div>
        <label for="sid_fluoro">Distanță Focar-Receptor (SID)</label>
        <input type="text" id="sid_fluoro" name="sid_fluoro" value="{{ fm.positioning_equipment.sid if is_fluoro and fm.positioning_equipment else '' }}" placeholder="ex. ≥ 100 cm">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Parametri Tehnici Scopie &amp; Expunere (Fluoroscopie)</h2>
    <div class="grid-3">
      <div>
        <label for="fluoro_mode">Regim Scopie</label>
        <input type="text" id="fluoro_mode" name="fluoro_mode" value="{{ fm.fluoro_params.mode if is_fluoro and fm.fluoro_params else '' }}" placeholder="ex. Scopie Pulsată 7.5 fps">
      </div>
      <div>
        <label for="fluoro_kv">Tensiune Tub (kV)</label>
        <input type="text" id="fluoro_kv" name="fluoro_kv" value="{{ fm.fluoro_params.kv if is_fluoro and fm.fluoro_params else '' }}" placeholder="ex. 75 - 90">
      </div>
      <div>
        <label for="fluoro_ma">Curent Tub Scopie (mA)</label>
        <input type="text" id="fluoro_ma" name="fluoro_ma" value="{{ fm.fluoro_params.ma_range if is_fluoro and fm.fluoro_params else '' }}" placeholder="ex. 1.0 - 2.5 mA">
      </div>
      <div>
        <label for="fluoro_grid">Grilă Antidifuzoare</label>
        <input type="text" id="fluoro_grid" name="fluoro_grid" value="{{ fm.fluoro_params.grid if is_fluoro and fm.fluoro_params else '' }}" placeholder="ex. Cu grilă / Fără grilă (Pediatrie)">
      </div>
      <div>
        <label for="fluoro_filtration">Filtrare Suplimentară</label>
        <input type="text" id="fluoro_filtration" name="fluoro_filtration" value="{{ fm.fluoro_params.filtration if is_fluoro and fm.fluoro_params else '' }}" placeholder="ex. ≥ 3.0 mm Al + 0.1 mm Cu">
      </div>
      <div>
        <label for="fluoro_target_time">Timp Țintă Scopie</label>
        <input type="text" id="fluoro_target_time" name="fluoro_target_time" value="{{ fm.fluoro_params.target_fluoro_time if is_fluoro and fm.fluoro_params else '' }}" placeholder="ex. < 2 minute">
      </div>
      <div>
        <label for="fluoro_lih">Last Image Hold (LIH)</label>
        <input type="text" id="fluoro_lih" name="fluoro_lih" value="{{ fm.fluoro_params.lih if is_fluoro and fm.fluoro_params else '' }}" placeholder="ex. Activ">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Criterii de Calitate &amp; Radioprotecție ALARA (Fluoroscopie)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="quality_criteria_fluoro">Criterii de Calitate &amp; Reușită (una pe linie)</label>
        <textarea id="quality_criteria_fluoro" name="quality_criteria_fluoro" rows="3">{{ fm.quality_criteria | join('\n') if is_fluoro else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="radiation_safety_fluoro">Măsuri de Radioprotecție &amp; Dozimetrie (una pe linie)</label>
        <textarea id="radiation_safety_fluoro" name="radiation_safety_fluoro" rows="3">{{ fm.radiation_safety | join('\n') if is_fluoro else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="notes_fluoro">Observații &amp; Notițe Clinico-Tehnice</label>
        <textarea id="notes_fluoro" name="notes_fluoro" rows="2">{{ fm.notes if is_fluoro and fm.notes is string else '' }}</textarea>
      </div>
    </div>
  </div>
</div>

<!-- ======================= SECTIUNI IRM ======================= -->
<div id="irm-fields" style="{% if not is_irm %}display:none;{% endif %}">
  <div class="section">
    <h2>Clinic, Indicații &amp; Contraindicații (IRM)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="indications_json_irm">Indicații Clinice (una pe linie)</label>
        <textarea id="indications_json_irm" name="indications_json_irm" rows="4">{{ fm.clinical_indications | join('\n') if is_irm else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="contraindications_irm">Contraindicații &amp; Screening Feromagnetic (una pe linie)</label>
        <textarea id="contraindications_irm" name="contraindications_irm" rows="3">{{ fm.contraindications | join('\n') if is_irm else '' }}</textarea>
      </div>
      <div>
        <label for="iris_chapter_irm">Capitol Ghid Național IRIS</label>
        <input type="text" id="iris_chapter_irm" name="iris_chapter" value="{{ fm.iris_reference.chapter if is_irm and fm.iris_reference else '' }}" placeholder="ex. Neuroimagistică, Musculoscheletal, Abdomen">
      </div>
      <div>
        <label for="iris_grade_irm">Grad de Recomandare IRIS</label>
        <input type="text" id="iris_grade_irm" name="iris_grade" value="{{ fm.iris_reference.recommendation_grade if is_irm and fm.iris_reference else '' }}" placeholder="ex. Grad A / Grad B">
      </div>
      <div class="span-full">
        <label for="iris_dose_irm">Nivel Iradiere Estimată (Ghid IRIS)</label>
        <input type="text" id="iris_dose_irm" name="iris_dose" value="{{ fm.iris_reference.radiation_dose if is_irm and fm.iris_reference else '' }}" placeholder="ex. Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Pregătire Pacient &amp; Securitate Feromagnetică (IRM)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="patient_prep_irm">Pregătire Pacient (Chestionar, repaus NPO, antispastic, antifoane)</label>
        <textarea id="patient_prep_irm" name="patient_prep_irm" rows="2">{{ fm.patient_prep if is_irm else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="safety_considerations_irm">Măsuri de Securitate RM, Limită SAR &amp; Artefacte (una pe linie)</label>
        <textarea id="safety_considerations_irm" name="safety_considerations_irm" rows="3">{{ fm.safety_considerations | join('\n') if is_irm and fm.safety_considerations else '' }}</textarea>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Echipament, Câmp Magnetic &amp; Antene (Coils)</h2>
    <div class="grid-3">
      <div>
        <label for="field_strength_irm">Putere Câmp Magnetic</label>
        <input type="text" id="field_strength_irm" name="field_strength_irm" value="{{ fm.coils_hardware.field_strength if is_irm and fm.coils_hardware else '' }}" placeholder="ex. 1.5 Tesla / 3.0 Tesla">
      </div>
      <div>
        <label for="coil_irm">Antenă de Recepție (Coil)</label>
        <input type="text" id="coil_irm" name="coil_irm" value="{{ fm.coils_hardware.coil if is_irm and fm.coils_hardware else '' }}" placeholder="ex. Antenă Head/Neck 32-ch / Body Phased-Array">
      </div>
      <div>
        <label for="positioning_irm">Poziție Pacient &amp; Centrare</label>
        <input type="text" id="positioning_irm" name="positioning_irm" value="{{ fm.coils_hardware.positioning if is_irm and fm.coils_hardware else '' }}" placeholder="ex. Decubit dorsal, centrare nasion">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Substanță de Contrast Paramagnetic (Gadoliniu)</h2>
    <div class="grid-4">
      <div>
        <label for="contrast_agent_irm">Agent de Contrast</label>
        <input type="text" id="contrast_agent_irm" name="contrast_agent_irm" value="{{ fm.contrast.agent if is_irm and fm.contrast else '' }}" placeholder="ex. Chelat de Gadoliniu macrociclic">
      </div>
      <div>
        <label for="contrast_dose_irm">Doză Recomandată</label>
        <input type="text" id="contrast_dose_irm" name="contrast_dose_irm" value="{{ fm.contrast.dose if is_irm and fm.contrast else '' }}" placeholder="ex. 0.1 mmol/kg corp (0.1 - 0.2 ml/kg)">
      </div>
      <div>
        <label for="contrast_flow_rate_irm">Rată Injectare (Debit)</label>
        <input type="text" id="contrast_flow_rate_irm" name="contrast_flow_rate_irm" value="{{ fm.contrast.flow_rate if is_irm and fm.contrast else '' }}" placeholder="ex. 1.5 - 2.5 ml/s + 20 ml ser fiziologic">
      </div>
      <div>
        <label for="contrast_timing_irm">Temporizare / Faze</label>
        <input type="text" id="contrast_timing_irm" name="contrast_timing_irm" value="{{ fm.contrast.timing if is_irm and fm.contrast else '' }}" placeholder="ex. Arterial 20s, Portal 60s, Tardiv">
      </div>
      <div class="span-full">
        <label for="contrast_notes_irm">Precauții Renale &amp; Risc NSF (eGFR)</label>
        <input type="text" id="contrast_notes_irm" name="contrast_notes_irm" value="{{ fm.contrast.notes if is_irm and fm.contrast else '' }}" placeholder="ex. Verificare eGFR conform ghidului ESUR; risc minim NSF pentru agenți macrociclici">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Protocol Secvențe RM (Parametri Tehnici)</h2>
    <div id="sequences-container"></div>
    <button type="button" class="add-btn" onclick="addSequenceRow({})">+ Adaugă Secvență</button>
    <input type="hidden" name="sequences_json" id="sequences_json">
  </div>

  <div class="section">
    <h2>Criterii de Calitate &amp; Note Clinice (IRM)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="quality_criteria_irm">Criterii de Calitate a Imaginii (una pe linie)</label>
        <textarea id="quality_criteria_irm" name="quality_criteria_irm" rows="3">{{ fm.quality_criteria | join('\n') if is_irm else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="notes_irm">Observații, Recomandări Practice &amp; Capcane</label>
        <textarea id="notes_irm" name="notes_irm" rows="2">{{ fm.notes if is_irm and fm.notes is string else '' }}</textarea>
      </div>
    </div>
  </div>
</div>

<!-- ======================= SECTIUNI ECO ======================= -->
<div id="eco-fields" style="{% if not is_eco %}display:none;{% endif %}">
  <div class="section">
    <h2>Clinic &amp; Pregătire Pacient (Ecografie)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="indications_json_eco">Indicații Clinice &amp; Obiective Diagnostice (una pe linie)</label>
        <textarea id="indications_json_eco" name="indications_json_eco" rows="3">{{ fm.clinical_indications | join('\n') if is_eco else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="contraindications_eco">Contraindicații &amp; Limite Tehnice (una pe linie)</label>
        <textarea id="contraindications_eco" name="contraindications_eco" rows="2">{{ fm.contraindications | join('\n') if is_eco else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="patient_prep_eco">Pregătire Prealabilă Pacient</label>
        <input type="text" id="patient_prep_eco" name="patient_prep_eco" value="{{ fm.patient_prep if is_eco else '' }}" placeholder="ex. Repaus alimentar 6 ore / Repleție vezicală 500-750 ml apă / Fără pregătire">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Echipament &amp; Sonde / Transductori (US)</h2>
    <div class="grid-3">
      <div>
        <label for="transducers_types_eco">Sonde / Transductori Utilizați</label>
        <input type="text" id="transducers_types_eco" name="transducers_types_eco" value="{{ fm.transducers_equipment.transducer_types if is_eco and fm.transducers_equipment else '' }}" placeholder="ex. Sondă Convexă 3.5 - 5.0 MHz / Sondă Liniară 7.5 - 14.0 MHz">
      </div>
      <div>
        <label for="patient_position_eco">Poziționare Pacient</label>
        <input type="text" id="patient_position_eco" name="patient_position_eco" value="{{ fm.transducers_equipment.patient_position if is_eco and fm.transducers_equipment else '' }}" placeholder="ex. Decubit dorsal; decubit lateral stâng/drept la nevoie">
      </div>
      <div>
        <label for="gel_acoustic_window_eco">Mediu Cuplare &amp; Fereastră Acustică</label>
        <input type="text" id="gel_acoustic_window_eco" name="gel_acoustic_window_eco" value="{{ fm.transducers_equipment.gel_acoustic_window if is_eco and fm.transducers_equipment else '' }}" placeholder="ex. Gel ecografic hipoalergenic în cantitate suficientă">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Reglaje Tehnice Ecograf &amp; Optimizare Imagine</h2>
    <div class="grid-3">
      <div>
        <label for="preset_eco">Preset / Aplicație Clinică</label>
        <input type="text" id="preset_eco" name="preset_eco" value="{{ fm.technical_settings.preset if is_eco and fm.technical_settings else '' }}" placeholder="ex. Abdomen General / Tiroidă / Vascular Carotidian">
      </div>
      <div>
        <label for="modes_eco">Moduri Active de Lucru</label>
        <input type="text" id="modes_eco" name="modes_eco" value="{{ fm.technical_settings.modes if is_eco and fm.technical_settings else '' }}" placeholder="ex. Mod B (2D) + Doppler Color (CFM) + Doppler Pulsat (PW)">
      </div>
      <div>
        <label for="focus_depth_eco">Focalizare &amp; Adâncime (Depth)</label>
        <input type="text" id="focus_depth_eco" name="focus_depth_eco" value="{{ fm.technical_settings.focus_depth if is_eco and fm.technical_settings else '' }}" placeholder="ex. Focar la nivelul zonei de interes; adâncime adaptată">
      </div>
      <div>
        <label for="gain_thi_eco">Câștig (Gain) &amp; THI (Armonice)</label>
        <input type="text" id="gain_thi_eco" name="gain_thi_eco" value="{{ fm.technical_settings.gain_thi if is_eco and fm.technical_settings else '' }}" placeholder="ex. THI activat; TGC reglat optim">
      </div>
      <div class="span-full">
        <label for="measurements_criteria_eco">Criterii Standard &amp; Măsurători</label>
        <input type="text" id="measurements_criteria_eco" name="measurements_criteria_eco" value="{{ fm.technical_settings.measurements_criteria if is_eco and fm.technical_settings else '' }}" placeholder="ex. Măsurători biometrice în două axe ortogonale; indici Doppler (IR/IP/Vmax)">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Protocol de Scanare &amp; Incidențe Standard</h2>
    <div id="views-container"></div>
    <button type="button" class="add-btn" onclick="addEcoViewRow({})">+ Adaugă Incidență / Plan Ecografic</button>
    <input type="hidden" name="views_json" id="views_json">
  </div>

  <div class="section">
    <h2>Criterii de Calitate &amp; Securitate Acustică ALARA</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="quality_criteria_eco">Criterii de Calitate a Imaginii (una pe linie)</label>
        <textarea id="quality_criteria_eco" name="quality_criteria_eco" rows="3">{{ fm.quality_criteria | join('\n') if is_eco else '' }}</textarea>
      </div>
      <div class="span-full">
        <label for="safety_and_limitations_eco">Securitate Acustică ALARA &amp; Capcane / Artefacte (una pe linie)</label>
        <textarea id="safety_and_limitations_eco" name="safety_and_limitations_eco" rows="3">{{ fm.safety_and_limitations | join('\n') if is_eco and fm.safety_and_limitations else '' }}</textarea>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Referință Ghid Național IRIS &amp; Recomandări Practice</h2>
    <div class="grid-3">
      <div>
        <label for="iris_chapter_eco">Capitol Ghid IRIS</label>
        <input type="text" id="iris_chapter_eco" name="iris_chapter_eco" value="{{ fm.iris_reference.chapter if is_eco and fm.iris_reference else '' }}" placeholder="ex. Ecografie &amp; Ultrasonografie">
      </div>
      <div>
        <label for="iris_grade_eco">Grad Recomandare IRIS</label>
        <select id="iris_grade_eco" name="iris_grade_eco">
          {% for g in ['Grad A', 'Grad B', 'Grad C'] %}
          <option value="{{ g }}" {% if is_eco and fm.iris_reference and fm.iris_reference.recommendation_grade == g %}selected{% endif %}>{{ g }}</option>
          {% endfor %}
        </select>
      </div>
      <div>
        <label for="iris_dose_eco">Nivel Iradiere Ghid IRIS</label>
        <input type="text" id="iris_dose_eco" name="iris_dose_eco" value="{{ fm.iris_reference.radiation_dose if is_eco and fm.iris_reference else 'Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)' }}" readonly>
      </div>
      <div class="span-full">
        <label for="notes_eco">Observații, Recomandări Practice &amp; Note Finale</label>
        <textarea id="notes_eco" name="notes_eco" rows="2">{{ fm.notes if is_eco and fm.notes is string else '' }}</textarea>
      </div>
    </div>
  </div>
</div>

<!-- ======================= SECTIUNI CT ======================= -->
<div id="ct-fields" style="{% if is_rx or is_fluoro or is_irm or is_eco %}display:none;{% endif %}">
  <div class="section">
    <h2>Clinic (CT)</h2>
    <div class="grid-2">
      <div class="span-full">
        <label for="indications_json">Indicații Clinice (una pe linie)</label>
        <textarea id="indications_json" name="indications_json" rows="4" class="{{ 'apply-highlight' if 'indications_json' in highlighted else '' }}">{{ fm.clinical_indications | join('\n') if (not is_rx and not is_fluoro and not is_irm and not is_eco) else '' }}</textarea>
      </div>
      <div>
        <label for="position_ct">Poziție Pacient</label>
        <input type="text" id="position_ct" name="position_ct" value="{{ fm.position if (not is_rx and not is_fluoro and not is_irm and not is_eco) else '' }}" class="{{ 'apply-highlight' if 'position' in highlighted else '' }}">
      </div>
      <div>
        <label for="npo">Repaus Alimentar (NPO)</label>
        <input type="text" id="npo" name="npo" value="{{ fm.npo if (not is_rx and not is_fluoro and not is_irm and not is_eco) else '' }}" class="{{ 'apply-highlight' if 'npo' in highlighted else '' }}">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Pregătire</h2>
    <div>
      <label for="premedication">Premedicație</label>
      <textarea id="premedication" name="premedication" rows="3" class="{{ 'apply-highlight' if 'premedication' in highlighted else '' }}">{{ fm.premedication if (not is_rx and not is_fluoro and not is_irm and not is_eco) else '' }}</textarea>
    </div>
  </div>

  <div class="section">
    <h2>Substanță de Contrast IV</h2>
    <div class="grid-4">
      <div>
        <label>Agent</label>
        <input type="text" name="contrast_agent" value="{{ fm.contrast.agent if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.contrast) else '' }}" class="{{ 'apply-highlight' if 'contrast_agent' in highlighted else '' }}">
      </div>
      <div>
        <label>Volum</label>
        <input type="text" name="contrast_volume" value="{{ fm.contrast.volume if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.contrast) else '' }}" class="{{ 'apply-highlight' if 'contrast_volume' in highlighted else '' }}">
      </div>
      <div>
        <label>Rată de Flux</label>
        <input type="text" name="contrast_flow_rate" value="{{ fm.contrast.flow_rate if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.contrast) else '' }}" class="{{ 'apply-highlight' if 'contrast_flow_rate' in highlighted else '' }}">
      </div>
      <div>
        <label>Durată</label>
        <input type="text" name="contrast_duration" value="{{ fm.contrast.duration if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.contrast) else '' }}" class="{{ 'apply-highlight' if 'contrast_duration' in highlighted else '' }}">
      </div>
      <div>
        <label>Metodă Temporizare</label>
        <input type="text" name="contrast_timing" value="{{ fm.contrast.timing if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.contrast) else '' }}" class="{{ 'apply-highlight' if 'contrast_timing' in highlighted else '' }}">
      </div>
      <div>
        <label>ROI</label>
        <input type="text" name="contrast_roi" value="{{ fm.contrast.roi if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.contrast) else '' }}" class="{{ 'apply-highlight' if 'contrast_roi' in highlighted else '' }}">
      </div>
      <div>
        <label>Declanșator (HU)</label>
        <input type="text" name="contrast_trigger" value="{{ fm.contrast.trigger if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.contrast) else '' }}" class="{{ 'apply-highlight' if 'contrast_trigger' in highlighted else '' }}">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Parametri Tehnici Achiziție (CT)</h2>
    <div class="grid-4">
      <div>
        <label>Tensiune Tub (kV)</label>
        <input type="text" name="tech_kv_ct" value="{{ fm.tech_params.kv if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_kv' in highlighted else '' }}" placeholder="ex. 100 / 120">
      </div>
      <div>
        <label>Curent Tub (mAs)</label>
        <input type="text" name="tech_mas_ct" value="{{ fm.tech_params.mas if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_mas' in highlighted else '' }}" placeholder="ex. Auto (referință 200)">
      </div>
      <div>
        <label>Modulare Doză (AEC)</label>
        <input type="text" name="tech_aec" value="{{ fm.tech_params.aec if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_aec' in highlighted else '' }}" placeholder="ex. Activat (Modulare 3D)">
      </div>
      <div>
        <label>Grosime Strat (Slice)</label>
        <input type="text" name="tech_slice" value="{{ fm.tech_params.slice_thickness if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_slice' in highlighted else '' }}" placeholder="ex. 0.625 mm">
      </div>
      <div>
        <label>Colimare Detector</label>
        <input type="text" name="tech_collimation_ct" value="{{ fm.tech_params.collimation if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_collimation' in highlighted else '' }}" placeholder="ex. Sub-milimetrică">
      </div>
      <div>
        <label>Timp Rotație (s)</label>
        <input type="text" name="tech_rotation_time" value="{{ fm.tech_params.rotation_time if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_rotation_time' in highlighted else '' }}" placeholder="ex. 0.5 s">
      </div>
      <div>
        <label>Pitch (Factor Pas)</label>
        <input type="text" name="tech_pitch" value="{{ fm.tech_params.pitch if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_pitch' in highlighted else '' }}" placeholder="ex. 1.0 - 1.2">
      </div>
      <div>
        <label>Mod Scanare</label>
        <input type="text" name="tech_scan_mode" value="{{ fm.tech_params.scan_mode if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.tech_params) else '' }}" class="{{ 'apply-highlight' if 'tech_scan_mode' in highlighted else '' }}" placeholder="ex. Elicoidal">
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Achiziție Serii (CT)</h2>
    <div id="series-container"></div>
    <button type="button" class="add-btn" onclick="addSeriesRow({})">+ Adaugă Serie</button>
    <input type="hidden" name="series_json" id="series_json">
  </div>

  <div class="section">
    <h2>Post-procesare Reconstrucții (CT)</h2>
    <div id="recon-container"></div>
    <button type="button" class="add-btn" onclick="addReconRow({})">+ Adaugă Reconstrucție</button>
    <input type="hidden" name="recons_json" id="recons_json">
  </div>

  <div class="section">
    <h2>Note Clinice &amp; Tehnice (CT)</h2>
    <div class="grid-2">
      <div>
        <label>Note Tehnician</label>
        <textarea name="notes_tech" rows="3" class="{{ 'apply-highlight' if 'notes_tech' in highlighted else '' }}">{{ fm.notes.tech if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.notes is mapping) else '' }}</textarea>
      </div>
      <div>
        <label>Note Asistent</label>
        <textarea name="notes_nursing" rows="3" class="{{ 'apply-highlight' if 'notes_nursing' in highlighted else '' }}">{{ fm.notes.nursing if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.notes is mapping) else '' }}</textarea>
      </div>
      <div>
        <label>Note Radiolog</label>
        <textarea name="notes_rad" rows="3" class="{{ 'apply-highlight' if 'notes_rad' in highlighted else '' }}">{{ fm.notes.rad if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.notes is mapping) else '' }}</textarea>
      </div>
      <div>
        <label>Sfaturi &amp; Recomandări</label>
        <textarea name="notes_tips" rows="3" class="{{ 'apply-highlight' if 'notes_tips' in highlighted else '' }}">{{ fm.notes.tips if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.notes is mapping) else '' }}</textarea>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Siguranță &amp; Precauții (CT)</h2>
    <div class="grid-2">
      <div>
        <label>Considerații Renale</label>
        <input type="text" name="safety_renal" value="{{ fm.safety.renal if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.safety) else '' }}" class="{{ 'apply-highlight' if 'safety_renal' in highlighted else '' }}">
      </div>
      <div>
        <label>Considerații Alergii</label>
        <input type="text" name="safety_allergy" value="{{ fm.safety.allergy if (not is_rx and not is_fluoro and not is_irm and not is_eco and fm.safety) else '' }}" class="{{ 'apply-highlight' if 'safety_allergy' in highlighted else '' }}">
      </div>
    </div>
  </div>
</div>

  <div class="section" id="images-section">
    <h2>🖼️ Imagini</h2>
    <p style="font-size: 0.88rem; color: #555; margin-top: -0.5rem; margin-bottom: 0.85rem;">
      Atașați imagini clinice de referință (planuri anatomice, repere de centrare, poziționare pacient sau achiziții reprezentative).
      <strong>Notă:</strong> Dacă nu adăugați imagini, această secțiune nu va fi afișată în documentația protocolului.
    </p>
    <div id="images-container"></div>
    <button type="button" class="add-btn" onclick="addImageRow({})">+ Adaugă Imagine</button>
    <input type="hidden" name="images_json" id="images_json">
  </div>

<div class="action-bar">
  <button type="button" class="btn-save" onclick="submitForm()">Salvează Protocolul</button>
  {% if not is_new and frontend_url %}
  <a href="{{ frontend_url }}" target="_blank" class="btn btn-outline" style="padding: 0.6rem 1.25rem; font-size: 0.95rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem;" title="Deschide pagina în Ghidul de Protocoale (Port 8000)">👁️ Deschide în Ghid (Port 8000) ↗</a>
  {% endif %}
  <span id="status"></span>
</div>

</form>
</div>

<script>
const INITIAL_SERIES = {{ series_json | safe }};
const INITIAL_RECONS = {{ recons_json | safe }};
const INITIAL_IMAGES = {{ images_json | safe }};
const IS_NEW = {{ 'true' if is_new else 'false' }};
const SAVE_URL = {{ save_url | tojson }};
const FRONTEND_URL = {{ frontend_url | tojson }};
const CT_CATEGORIES = {{ ct_categories | tojson }};
const RX_CATEGORIES = {{ rx_categories | tojson }};
const FLUORO_CATEGORIES = {{ fluoro_categories | tojson }};
const IRM_CATEGORIES = {{ irm_categories | tojson }};
const ECO_CATEGORIES = {{ eco_categories | tojson }};
const INITIAL_SEQUENCES = {{ sequences_json | safe }};
const INITIAL_VIEWS = {{ views_json | safe }};
const ALL_PROTOCOLS = {{ protocols_map_json | safe }};

function switchModality(mod) {
  const catSelect = document.getElementById('category');
  const rxFields = document.getElementById('rx-fields');
  const fluoroFields = document.getElementById('fluoro-fields');
  const irmFields = document.getElementById('irm-fields');
  const ecoFields = document.getElementById('eco-fields');
  const ctFields = document.getElementById('ct-fields');
  const ctSyn = document.getElementById('ct-ident-syn');
  const ctType = document.getElementById('ct-ident-type');
  const modInput = document.getElementById('modality');

  if (modInput) modInput.value = mod;

  const currentVal = catSelect.value;
  catSelect.innerHTML = '';

  let cats = CT_CATEGORIES;
  if (mod === 'rx') cats = RX_CATEGORIES;
  else if (mod === 'fluoro') cats = FLUORO_CATEGORIES;
  else if (mod === 'irm') cats = IRM_CATEGORIES;
  else if (mod === 'eco') cats = ECO_CATEGORIES;

  cats.forEach(c => {
    const opt = document.createElement('option');
    opt.value = c;
    opt.textContent = c;
    if (c === currentVal) opt.selected = true;
    catSelect.appendChild(opt);
  });

  if (mod === 'rx') {
    if (rxFields) rxFields.style.display = '';
    if (fluoroFields) fluoroFields.style.display = 'none';
    if (irmFields) irmFields.style.display = 'none';
    if (ecoFields) ecoFields.style.display = 'none';
    if (ctFields) ctFields.style.display = 'none';
    if (ctSyn) ctSyn.style.display = 'none';
    if (ctType) ctType.style.display = 'none';
  } else if (mod === 'fluoro') {
    if (rxFields) rxFields.style.display = 'none';
    if (fluoroFields) fluoroFields.style.display = '';
    if (irmFields) irmFields.style.display = 'none';
    if (ecoFields) ecoFields.style.display = 'none';
    if (ctFields) ctFields.style.display = 'none';
    if (ctSyn) ctSyn.style.display = 'none';
    if (ctType) ctType.style.display = 'none';
  } else if (mod === 'irm') {
    if (rxFields) rxFields.style.display = 'none';
    if (fluoroFields) fluoroFields.style.display = 'none';
    if (irmFields) irmFields.style.display = '';
    if (ecoFields) ecoFields.style.display = 'none';
    if (ctFields) ctFields.style.display = 'none';
    if (ctSyn) ctSyn.style.display = 'none';
    if (ctType) ctType.style.display = 'none';
  } else if (mod === 'eco') {
    if (rxFields) rxFields.style.display = 'none';
    if (fluoroFields) fluoroFields.style.display = 'none';
    if (irmFields) irmFields.style.display = 'none';
    if (ecoFields) ecoFields.style.display = '';
    if (ctFields) ctFields.style.display = 'none';
    if (ctSyn) ctSyn.style.display = 'none';
    if (ctType) ctType.style.display = 'none';
  } else {
    if (rxFields) rxFields.style.display = 'none';
    if (fluoroFields) fluoroFields.style.display = 'none';
    if (irmFields) irmFields.style.display = 'none';
    if (ecoFields) ecoFields.style.display = 'none';
    if (ctFields) ctFields.style.display = '';
    if (ctSyn) ctSyn.style.display = '';
    if (ctType) ctType.style.display = '';
  }
}

function moveRow(el, dir) {
  const parent = el.parentNode;
  if (dir === 'up' && el.previousElementSibling) {
    parent.insertBefore(el, el.previousElementSibling);
  } else if (dir === 'down' && el.nextElementSibling) {
    parent.insertBefore(el.nextElementSibling, el);
  }
}

function addSeriesRow(s) {
  s = s || {};
  const container = document.getElementById('series-container');
  if (!container) return;
  const div = document.createElement('div');
  div.className = 'dynamic-row series-row';
  div.innerHTML = `
    <div class="row-actions">
      <button type="button" class="move-btn" title="Mută sus" onclick="moveRow(this.closest('.dynamic-row'),'up')">▲</button>
      <button type="button" class="move-btn" title="Mută jos" onclick="moveRow(this.closest('.dynamic-row'),'down')">▼</button>
      <button type="button" class="remove-btn" onclick="this.closest('.dynamic-row').remove()">Șterge</button>
    </div>
    <div class="row-grid series-row-grid">
      <div><label>Nume</label><input type="text" data-field="name" value="${esc(s.name)}"></div>
      <div><label>Început</label><input type="text" data-field="start" value="${esc(s.start)}"></div>
      <div><label>Sfârșit</label><input type="text" data-field="end" value="${esc(s.end)}"></div>
      <div><label>Întârziere</label><input type="text" data-field="delay" value="${esc(s.delay)}"></div>
      <div><label>Grosime</label><input type="text" data-field="thickness" value="${esc(s.thickness)}"></div>
    </div>
    <div style="margin-top:0.5rem">
      <label>Note</label>
      <input type="text" data-field="notes" value="${esc(s.notes)}" style="width:100%">
    </div>`;
  container.appendChild(div);
}

function addReconRow(r) {
  r = r || {};
  const container = document.getElementById('recon-container');
  if (!container) return;
  const div = document.createElement('div');
  div.className = 'dynamic-row recon-row';
  div.innerHTML = `
    <div class="row-actions">
      <button type="button" class="move-btn" title="Mută sus" onclick="moveRow(this.closest('.dynamic-row'),'up')">▲</button>
      <button type="button" class="move-btn" title="Mută jos" onclick="moveRow(this.closest('.dynamic-row'),'down')">▼</button>
      <button type="button" class="remove-btn" onclick="this.closest('.dynamic-row').remove()">Șterge</button>
    </div>
    <div class="row-grid recon-row-grid">
      <div><label>Plan</label><input type="text" data-field="plane" value="${esc(r.plane)}"></div>
      <div><label>Achiziție</label><input type="text" data-field="acquisition" value="${esc(r.acquisition)}"></div>
      <div><label>FOV</label><input type="text" data-field="fov" value="${esc(r.fov)}"></div>
      <div><label>Grosime/Inc</label><input type="text" data-field="thickness_increment" value="${esc(r.thickness_increment)}"></div>
      <div><label>Filtru (Kernel)</label><input type="text" data-field="kernel" value="${esc(r.kernel)}"></div>
    </div>
    <div class="row-grid recon-row-grid2" style="margin-top:0.5rem">
      <div><label>Putere IR</label><input type="text" data-field="ir_strength" value="${esc(r.ir_strength)}"></div>
      <div class="span-full"><label>Note</label><input type="text" data-field="notes" value="${esc(r.notes)}" style="width:100%"></div>
    </div>`;
  container.appendChild(div);
}

function addSequenceRow(s) {
  s = s || {};
  const container = document.getElementById('sequences-container');
  if (!container) return;
  const div = document.createElement('div');
  div.className = 'dynamic-row sequence-row';
  div.innerHTML = `
    <div class="row-actions">
      <button type="button" class="move-btn" title="Mută sus" onclick="moveRow(this.closest('.dynamic-row'),'up')">▲</button>
      <button type="button" class="move-btn" title="Mută jos" onclick="moveRow(this.closest('.dynamic-row'),'down')">▼</button>
      <button type="button" class="remove-btn" onclick="this.closest('.dynamic-row').remove()">Șterge</button>
    </div>
    <div class="row-grid" style="grid-template-columns: 2fr 1fr 1.5fr 1.5fr 1.5fr 1fr; gap: 0.5rem;">
      <div><label>Nume Secvență</label><input type="text" data-field="name" value="${esc(s.name)}" placeholder="ex. T2 FSE, DWI, FLAIR"></div>
      <div><label>Plan</label><input type="text" data-field="plane" value="${esc(s.plane)}" placeholder="Axial / Cor / Sag / 3D"></div>
      <div><label>TR / TE</label><input type="text" data-field="tr_te" value="${esc(s.tr_te)}" placeholder="ex. TR: 3500-4500 / TE: 90-100"></div>
      <div><label>Grosime / Gap</label><input type="text" data-field="slice_gap" value="${esc(s.slice_gap)}" placeholder="ex. 4 mm / gap 10%"></div>
      <div><label>FOV / Matrice</label><input type="text" data-field="fov_matrix" value="${esc(s.fov_matrix)}" placeholder="ex. FOV 220 / 320x256"></div>
      <div><label>FatSat</label><input type="text" data-field="fat_sat" value="${esc(s.fat_sat)}" placeholder="Nu / Da / STIR / SPAIR"></div>
    </div>
    <div style="margin-top:0.5rem">
      <label>Observații / Ponderație / Valori b</label>
      <input type="text" data-field="notes" value="${esc(s.notes)}" style="width:100%" placeholder="ex. Ponderație T2 înaltă, b=0, 500, 1000 s/mm²">
    </div>`;
  container.appendChild(div);
}

function addEcoViewRow(v) {
  v = v || {};
  const container = document.getElementById('views-container');
  if (!container) return;
  const div = document.createElement('div');
  div.className = 'dynamic-row eco-view-row';
  div.innerHTML = `
    <div class="row-actions">
      <button type="button" class="move-btn" title="Mută sus" onclick="moveRow(this.closest('.dynamic-row'),'up')">▲</button>
      <button type="button" class="move-btn" title="Mută jos" onclick="moveRow(this.closest('.dynamic-row'),'down')">▼</button>
      <button type="button" class="remove-btn" onclick="this.closest('.dynamic-row').remove()">Șterge</button>
    </div>
    <div class="row-grid" style="grid-template-columns: 1fr 1fr 1.2fr 1.2fr; gap: 0.5rem;">
      <div><label>Incidență / Plan Ecografic</label><input type="text" data-field="view" value="${esc(v.view || '')}" placeholder="ex. Secțiune Sagitală / Ax Lung"></div>
      <div><label>Structură Anatomică Țintă</label><input type="text" data-field="anatomical_target" value="${esc(v.anatomical_target || '')}" placeholder="ex. Lob hepatic drept / Colecist"></div>
      <div><label>Repere &amp; Tehnica de Scanare</label><input type="text" data-field="landmarks" value="${esc(v.landmarks || '')}" placeholder="ex. Abord subcostal / intercostal în inspir"></div>
      <div><label>Aspect Ecografic Normal</label><input type="text" data-field="normal_aspect" value="${esc(v.normal_aspect || '')}" placeholder="ex. Ecostructură omogenă, calibru normal"></div>
    </div>`;
  container.appendChild(div);
}

function esc(v) {
  if (v == null) return '';
  return String(v).replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function collectRows(containerSelector, rowClass) {
  const rows = document.querySelectorAll(containerSelector + ' .' + rowClass);
  return Array.from(rows).map(row => {
    const obj = {};
    row.querySelectorAll('[data-field]').forEach(inp => {
      obj[inp.dataset.field] = inp.value;
    });
    return obj;
  });
}

function resolvePreviewUrl(url) {
  if (!url) return '';
  url = String(url).trim();
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) {
    return url;
  }
  while (url.startsWith('../')) {
    url = url.substring(3);
  }
  if (url.startsWith('./')) {
    url = url.substring(2);
  }
  if (!url.startsWith('/')) {
    url = '/' + url;
  }
  return url;
}

function updateImagePreview(input) {
  const row = input.closest('.image-row');
  if (!row) return;
  const imgEl = row.querySelector('.img-preview');
  const noPrev = row.querySelector('.no-preview-text');
  const url = input.value.trim();
  if (url) {
    imgEl.src = resolvePreviewUrl(url);
    imgEl.style.display = 'block';
    if (noPrev) noPrev.style.display = 'none';
  } else {
    imgEl.src = '';
    imgEl.style.display = 'none';
    if (noPrev) noPrev.style.display = 'block';
  }
}

function uploadImageFile(fileInput) {
  const row = fileInput.closest('.image-row');
  if (!row) return;
  const statusEl = row.querySelector('.upload-status');
  const urlInput = row.querySelector('[data-field="url"]');
  const file = fileInput.files && fileInput.files[0];
  if (!file) return;

  if (statusEl) {
    statusEl.textContent = 'Se încarcă fișierul...';
    statusEl.style.color = '#0284c7';
  }

  const fd = new FormData();
  fd.append('file', file);

  fetch('/api/upload_image', {
    method: 'POST',
    body: fd
  })
  .then(r => r.json())
  .then(res => {
    if (res.success) {
      if (urlInput) {
        urlInput.value = res.url;
        updateImagePreview(urlInput);
      }
      if (statusEl) {
        statusEl.textContent = '✓ Imagine încărcată (' + res.filename + ')';
        statusEl.style.color = '#16a34a';
      }
    } else {
      if (statusEl) {
        statusEl.textContent = 'Eroare încărcare: ' + (res.error || 'Eroare');
        statusEl.style.color = '#dc2626';
      }
    }
  })
  .catch(err => {
    if (statusEl) {
      statusEl.textContent = 'Eroare la încărcare: ' + err;
      statusEl.style.color = '#dc2626';
    }
  });
}

function addImageRow(img) {
  img = img || {};
  const container = document.getElementById('images-container');
  if (!container) return;
  const div = document.createElement('div');
  div.className = 'dynamic-row image-row';
  const urlVal = esc(img.url || '');
  const capVal = esc(img.caption || '');
  const descVal = esc(img.description || '');
  const previewSrc = resolvePreviewUrl(img.url || '');
  const hasUrl = Boolean(img.url);

  div.innerHTML = `
    <div class="row-actions">
      <button type="button" class="move-btn" title="Mută sus" onclick="moveRow(this.closest('.dynamic-row'),'up')">▲</button>
      <button type="button" class="move-btn" title="Mută jos" onclick="moveRow(this.closest('.dynamic-row'),'down')">▼</button>
      <button type="button" class="remove-btn" onclick="this.closest('.dynamic-row').remove()">Șterge</button>
    </div>
    <div style="display: flex; gap: 1rem; align-items: flex-start; flex-wrap: wrap;">
      <div style="width: 140px; height: 105px; min-width: 140px; background: #0f172a; border-radius: 6px; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 1px solid #cbd5e1; box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);">
        <img class="img-preview" src="${previewSrc}" alt="Previzualizare" style="max-width: 100%; max-height: 100%; object-fit: contain; display: ${hasUrl ? 'block' : 'none'};" onerror="this.style.display='none'; if(this.nextElementSibling) this.nextElementSibling.style.display='block';">
        <span class="no-preview-text" style="color: #94a3b8; font-size: 0.75rem; text-align: center; padding: 6px; display: ${hasUrl ? 'none' : 'block'};">Fără imagine</span>
      </div>
      <div style="flex: 1; min-width: 280px; display: flex; flex-direction: column; gap: 0.5rem;">
        <div>
          <label style="font-size: 0.8rem; font-weight: 600; color: #475569; margin-bottom: 0.2rem;">Cale Imagine / URL</label>
          <div style="display: flex; gap: 0.5rem; align-items: center;">
            <input type="text" data-field="url" value="${urlVal}" placeholder="ex. assets/images/protocols/nume-fisier.png sau https://..." oninput="updateImagePreview(this)" style="flex: 1;">
            <label class="btn btn-sm btn-outline" style="white-space: nowrap; margin: 0; cursor: pointer; display: inline-flex; align-items: center; gap: 0.3rem;">
              📁 Încarcă Fișier
              <input type="file" accept="image/*" style="display: none;" onchange="uploadImageFile(this)">
            </label>
          </div>
          <div class="upload-status" style="font-size: 0.78rem; color: #64748b; margin-top: 0.2rem;"></div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
          <div>
            <label style="font-size: 0.8rem; font-weight: 600; color: #475569; margin-bottom: 0.2rem;">Legendă / Titlu Imagine</label>
            <input type="text" data-field="caption" value="${capVal}" placeholder="ex. Achiziție coronală T2 / Centrare Rx">
          </div>
          <div>
            <label style="font-size: 0.8rem; font-weight: 600; color: #475569; margin-bottom: 0.2rem;">Descriere Clinică / Notă (opțional)</label>
            <input type="text" data-field="description" value="${descVal}" placeholder="ex. Repere anatomice și contrast optim">
          </div>
        </div>
      </div>
    </div>
  `;
  container.appendChild(div);
}

function collectImageRows() {
  const container = document.getElementById('images-container');
  if (!container) return [];
  const rows = container.querySelectorAll('.image-row');
  const result = [];
  rows.forEach(row => {
    const url = (row.querySelector('[data-field="url"]')?.value || '').trim();
    const caption = (row.querySelector('[data-field="caption"]')?.value || '').trim();
    const description = (row.querySelector('[data-field="description"]')?.value || '').trim();
    if (url) {
      result.push({ url, caption, description });
    }
  });
  return result;
}

function submitForm() {
  const mod = document.getElementById('modality') ? document.getElementById('modality').value : 'ct';
  if (mod === 'ct') {
    const series = collectRows('#series-container', 'series-row');
    const recons = collectRows('#recon-container', 'recon-row');
    const serInput = document.getElementById('series_json');
    const recInput = document.getElementById('recons_json');
    if (serInput) serInput.value = JSON.stringify(series);
    if (recInput) recInput.value = JSON.stringify(recons);
  } else if (mod === 'irm') {
    const sequences = collectRows('#sequences-container', 'sequence-row');
    const seqInput = document.getElementById('sequences_json');
    if (seqInput) seqInput.value = JSON.stringify(sequences);
  } else if (mod === 'eco') {
    const views = collectRows('#views-container', 'eco-view-row');
    const vInput = document.getElementById('views_json');
    if (vInput) vInput.value = JSON.stringify(views);
  }

  const images = collectImageRows();
  const imgInput = document.getElementById('images_json');
  if (imgInput) imgInput.value = JSON.stringify(images);

  const formEl = document.getElementById('proto-form');
  const data = new FormData(formEl);

  const statusEl = document.getElementById('status');
  statusEl.textContent = 'Se salvează…';
  statusEl.className = '';

  fetch(SAVE_URL, { method: 'POST', body: data })
    .then(r => r.json())
    .then(res => {
      if (res.success) {
        if (FRONTEND_URL) {
          statusEl.innerHTML = '✔ Salvat cu succes! <a href="' + FRONTEND_URL + '" target="_blank" style="color:#1565c0; font-weight:600; text-decoration:underline; margin-left:8px;">Deschide în Ghid (Port 8000) ↗</a>';
        } else {
          statusEl.textContent = '✔ Salvat cu succes.';
        }
        statusEl.className = 'ok';
        if (res.redirect) {
          setTimeout(() => { window.location.href = res.redirect; }, 800);
        }
      } else {
        statusEl.textContent = 'Eroare: ' + (res.error || 'Eroare necunoscută');
        statusEl.className = 'err';
      }
    })
    .catch(e => {
      statusEl.textContent = 'Eroare de rețea: ' + e;
      statusEl.className = 'err';
    });
}

function autoSlug() {
  if (!IS_NEW) return;
  const title = document.getElementById('title').value;
  document.getElementById('slug').value = title.toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

function loadBase() {
  const sel = document.getElementById('base-select');
  const statusEl = document.getElementById('base-load-status');
  if (!sel) return;
  const slug = sel.value;
  if (!slug) {
    if (statusEl) {
      statusEl.textContent = 'Vă rugăm să selectați un protocol din listă înainte de a apăsa Încarcă.';
      statusEl.className = 'err';
    } else {
      alert('Vă rugăm să selectați un protocol din listă înainte de a apăsa Încarcă.');
    }
    return;
  }

  const item = (typeof ALL_PROTOCOLS !== 'undefined' && ALL_PROTOCOLS) ? ALL_PROTOCOLS[slug] : null;
  if (!item || !item.fm) {
    if (statusEl) {
      statusEl.textContent = 'Eroare: Nu s-au putut încărca datele protocolului selectat.';
      statusEl.className = 'err';
    }
    return;
  }

  const fm = item.fm;
  const mod = item.modality || fm.modality || 'ct';

  const radio = document.querySelector(`input[name=modality_radio][value="${mod}"]`);
  if (radio) {
    radio.checked = true;
  }
  switchModality(mod);

  const setVal = (id, val) => { const el = document.getElementById(id); if (el) el.value = val || ''; };
  const setQuery = (selStr, val) => { const el = document.querySelector(selStr); if (el) el.value = val || ''; };
  const toLines = arr => Array.isArray(arr) ? arr.join(String.fromCharCode(10)) : (typeof arr === 'string' ? arr : '');

  setVal('title', fm.title ? `${fm.title} (Copie)` : '');
  if (typeof autoSlug === 'function') autoSlug();
  setVal('category', fm.category);
  setVal('author', fm.author || 'Departamentul de Radiologie');
  setVal('last_updated', new Date().toISOString().split('T')[0]);

  if (mod === 'rx') {
    setVal('position', fm.position);
    setVal('centering', fm.centering);
    setVal('sid_dff', fm.sid_dff);
    setVal('breathing', fm.breathing);
    const tp = fm.tech_params || {};
    setVal('tech_kv', tp.kv);
    setVal('tech_mas', tp.mas);
    setVal('tech_grid', tp.grid);
    setVal('tech_focal_spot', tp.focal_spot);
    setVal('tech_aec_chambers', tp.aec_chambers);
    setVal('tech_collimation', tp.collimation);
    setVal('tech_filtration', tp.filtration);
    setVal('indications_json_rx', toLines(fm.clinical_indications));
    const ir = fm.iris_reference || {};
    setVal('iris_chapter', ir.chapter);
    setVal('iris_grade', ir.recommendation_grade);
    setVal('iris_dose', ir.radiation_dose);
    setVal('quality_criteria', toLines(fm.quality_criteria));
    setVal('protection', toLines(fm.protection));
    setVal('notes_rx', typeof fm.notes === 'string' ? fm.notes : '');
  } else if (mod === 'fluoro') {
    setVal('indications_json_fluoro', toLines(fm.clinical_indications));
    setVal('contraindications', toLines(fm.contraindications));
    setVal('patient_prep', fm.patient_prep);
    const c = fm.contrast || {};
    setVal('contrast_agent_fluoro', c.agent);
    setVal('contrast_route_fluoro', c.route);
    setVal('contrast_volume_fluoro', c.volume);
    setVal('contrast_instructions_fluoro', c.instructions);
    const pe = fm.positioning_equipment || {};
    setVal('patient_position_fluoro', pe.patient_position);
    setVal('equipment_setup_fluoro', pe.equipment_setup);
    setVal('sid_fluoro', pe.sid);
    const fp = fm.fluoro_params || {};
    setVal('fluoro_mode', fp.mode);
    setVal('fluoro_kv', fp.kv);
    setVal('fluoro_ma', fp.ma_range);
    setVal('fluoro_grid', fp.grid);
    setVal('fluoro_filtration', fp.filtration);
    setVal('fluoro_target_time', fp.target_fluoro_time);
    setVal('fluoro_lih', fp.lih);
    const ir = fm.iris_reference || {};
    setVal('iris_chapter_fluoro', ir.chapter);
    setVal('iris_grade_fluoro', ir.recommendation_grade);
    setVal('iris_dose_fluoro', ir.radiation_dose);
    setVal('quality_criteria_fluoro', toLines(fm.quality_criteria));
    setVal('radiation_safety_fluoro', toLines(fm.radiation_safety));
    setVal('notes_fluoro', typeof fm.notes === 'string' ? fm.notes : '');
  } else if (mod === 'irm') {
    setVal('indications_json_irm', toLines(fm.clinical_indications));
    setVal('contraindications_irm', toLines(fm.contraindications));
    setVal('safety_considerations_irm', toLines(fm.safety_considerations));
    setVal('patient_prep_irm', fm.patient_prep);
    const hw = fm.coils_hardware || {};
    setVal('field_strength_irm', hw.field_strength);
    setVal('coil_irm', hw.coil);
    setVal('positioning_irm', hw.positioning);
    const c = fm.contrast || {};
    setVal('contrast_agent_irm', c.agent);
    setVal('contrast_dose_irm', c.dose);
    setVal('contrast_flow_rate_irm', c.flow_rate);
    setVal('contrast_timing_irm', c.timing);
    setVal('contrast_notes_irm', c.notes);
    const ir = fm.iris_reference || {};
    setVal('iris_chapter_irm', ir.chapter);
    setVal('iris_grade_irm', ir.recommendation_grade);
    setVal('iris_dose_irm', ir.radiation_dose);
    setVal('quality_criteria_irm', toLines(fm.quality_criteria));
    setVal('notes_irm', typeof fm.notes === 'string' ? fm.notes : '');
    const sCont = document.getElementById('sequences-container');
    if (sCont) {
      sCont.innerHTML = '';
      (fm.sequences || []).forEach(row => addSequenceRow(row));
    }
  } else if (mod === 'eco') {
    setVal('indications_json_eco', toLines(fm.clinical_indications));
    setVal('contraindications_eco', toLines(fm.contraindications));
    setVal('patient_prep_eco', fm.patient_prep);
    const te = fm.transducers_equipment || {};
    setVal('transducers_types_eco', te.transducer_types);
    setVal('patient_position_eco', te.patient_position);
    setVal('gel_acoustic_window_eco', te.gel_acoustic_window);
    const ts = fm.technical_settings || {};
    setVal('preset_eco', ts.preset);
    setVal('modes_eco', ts.modes);
    setVal('focus_depth_eco', ts.focus_depth);
    setVal('gain_thi_eco', ts.gain_thi);
    setVal('measurements_criteria_eco', ts.measurements_criteria);
    const ir = fm.iris_reference || {};
    setVal('iris_chapter_eco', ir.chapter);
    setVal('iris_grade_eco', ir.recommendation_grade);
    setVal('iris_dose_eco', ir.radiation_dose);
    setVal('quality_criteria_eco', toLines(fm.quality_criteria));
    setVal('safety_and_limitations_eco', toLines(fm.safety_and_limitations));
    setVal('notes_eco', typeof fm.notes === 'string' ? fm.notes : '');
    const vCont = document.getElementById('views-container');
    if (vCont) {
      vCont.innerHTML = '';
      (fm.standard_views || []).forEach(row => addEcoViewRow(row));
    }
  } else {
    setVal('protocol_type', fm.protocol_type);
    setVal('position_ct', fm.position);
    setVal('npo', fm.npo);
    setVal('premedication', fm.premedication);
    const c = fm.contrast || {};
    setQuery('[name=contrast_agent]', c.agent);
    setQuery('[name=contrast_volume]', c.volume);
    setQuery('[name=contrast_flow_rate]', c.flow_rate);
    setQuery('[name=contrast_duration]', c.duration);
    setQuery('[name=contrast_timing]', c.timing);
    setQuery('[name=contrast_roi]', c.roi);
    setQuery('[name=contrast_trigger]', c.trigger);
    const tp = fm.tech_params || {};
    setQuery('[name=tech_kv_ct]', tp.kv);
    setQuery('[name=tech_mas_ct]', tp.mas);
    setQuery('[name=tech_aec]', tp.aec);
    setQuery('[name=tech_slice]', tp.slice_thickness);
    setQuery('[name=tech_collimation_ct]', tp.collimation);
    setQuery('[name=tech_rotation_time]', tp.rotation_time);
    setQuery('[name=tech_pitch]', tp.pitch);
    setQuery('[name=tech_scan_mode]', tp.scan_mode);
    setVal('indications_json', toLines(fm.clinical_indications));
    const n = fm.notes || {};
    setQuery('[name=notes_tech]', n.tech);
    setQuery('[name=notes_nursing]', n.nursing);
    setQuery('[name=notes_rad]', n.rad);
    setQuery('[name=notes_tips]', n.tips);
    const s = fm.safety || {};
    setQuery('[name=safety_renal]', s.renal);
    setQuery('[name=safety_allergy]', s.allergy);
    const sCont = document.getElementById('series-container');
    if (sCont) { sCont.innerHTML = ''; (fm.series || []).forEach(row => addSeriesRow(row)); }
    const rCont = document.getElementById('recon-container');
    if (rCont) { rCont.innerHTML = ''; (fm.recons || []).forEach(row => addReconRow(row)); }
  }

  const imgCont = document.getElementById('images-container');
  if (imgCont && Array.isArray(fm.images)) {
    imgCont.innerHTML = '';
    fm.images.forEach(img => addImageRow(img));
  }

  if (statusEl) {
    statusEl.textContent = `✓ Protocolul „${fm.title}” a fost încărcat cu succes ca șablon!`;
    statusEl.className = 'ok';
    setTimeout(() => {
      if (statusEl.className === 'ok') statusEl.textContent = '';
    }, 5000);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  INITIAL_SERIES.forEach(s => addSeriesRow(s));
  INITIAL_RECONS.forEach(r => addReconRow(r));
  if (typeof INITIAL_SEQUENCES !== 'undefined' && Array.isArray(INITIAL_SEQUENCES)) {
    INITIAL_SEQUENCES.forEach(s => addSequenceRow(s));
  }
  if (typeof INITIAL_VIEWS !== 'undefined' && Array.isArray(INITIAL_VIEWS)) {
    INITIAL_VIEWS.forEach(v => addEcoViewRow(v));
  }
  if (typeof INITIAL_IMAGES !== 'undefined' && Array.isArray(INITIAL_IMAGES)) {
    INITIAL_IMAGES.forEach(img => addImageRow(img));
  }
});
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Empty FM templates
# ---------------------------------------------------------------------------

EMPTY_FM: dict = {
    "title": "",
    "slug": "",
    "category": "abdomen",
    "protocol_type": "",
    "last_updated": str(date.today()),
    "author": "",
    "synonyms": [],
    "clinical_indications": [],
    "position": "",
    "npo": "",
    "premedication": "",
    "contrast": {
        "agent": "", "volume": "", "flow_rate": "",
        "duration": "", "timing": "", "roi": "", "trigger": "",
    },
    "series": [],
    "recons": [],
    "images": [],
    "notes": {"tech": "", "nursing": "", "rad": "", "tips": ""},
    "safety": {"renal": "", "allergy": ""},
    "tech_params": {
        "kv": "", "mas": "", "aec": "", "slice_thickness": "",
        "collimation": "", "rotation_time": "", "pitch": "", "scan_mode": "",
    },
    "coils_hardware": {"coil": "", "field_strength": "", "positioning": ""},
    "sequences": [],
    "safety_considerations": [],
    "positioning_equipment": {"patient_position": "", "equipment_setup": "", "sid": ""},
    "fluoro_params": {"mode": "", "kv": "", "ma_range": "", "grid": "", "filtration": "", "target_fluoro_time": "", "lih": ""},
    "transducers_equipment": {"transducer_types": "", "patient_position": "", "gel_acoustic_window": ""},
    "technical_settings": {"preset": "", "modes": "", "focus_depth": "", "gain_thi": "", "measurements_criteria": ""},
    "standard_views": [],
    "safety_and_limitations": [],
    "iris_reference": {"chapter": "", "recommendation_grade": "Grad A", "radiation_dose": ""},
}

EMPTY_RX_FM: dict = {
    "title": "",
    "slug": "",
    "category": "torace",
    "modality": "rx",
    "author": "Departamentul de Radiologie",
    "last_updated": str(date.today()),
    "position": "",
    "centering": "",
    "breathing": "",
    "sid_dff": "100 cm",
    "tech_params": {
        "kv": "", "mas": "", "grid": "Cu grilă antidifuzoare Bucky",
        "focal_spot": "Focar Mare (1.0 mm)", "aec_chambers": "Camera centrală activată",
        "collimation": "Strictă pe regiunea de interes", "filtration": "Totală ≥ 2.5 mm Al echivalent",
    },
    "clinical_indications": [],
    "contrast": {"agent": "", "volume": "", "flow_rate": "", "duration": "", "timing": "", "roi": "", "trigger": ""},
    "safety": {"renal": "", "allergy": ""},
    "positioning_equipment": {"patient_position": "", "equipment_setup": "", "sid": ""},
    "fluoro_params": {"mode": "", "kv": "", "ma_range": "", "grid": "", "filtration": "", "target_fluoro_time": "", "lih": ""},
    "coils_hardware": {"coil": "", "field_strength": "", "positioning": ""},
    "sequences": [],
    "safety_considerations": [],
    "quality_criteria": [],
    "protection": [],
    "transducers_equipment": {"transducer_types": "", "patient_position": "", "gel_acoustic_window": ""},
    "technical_settings": {"preset": "", "modes": "", "focus_depth": "", "gain_thi": "", "measurements_criteria": ""},
    "standard_views": [],
    "safety_and_limitations": [],
    "images": [],
    "iris_reference": {
        "chapter": "", "recommendation_grade": "Grad A", "radiation_dose": "Clasa 1 (Minimă < 1 mSv)",
    },
    "notes": "",
}

EMPTY_FLUORO_FM: dict = {
    "title": "",
    "slug": "",
    "category": "digestiv",
    "modality": "fluoro",
    "author": "Departamentul de Radiologie și Imagistică Medicală",
    "last_updated": str(date.today()),
    "position": "",
    "clinical_indications": [],
    "contraindications": [],
    "patient_prep": "",
    "contrast": {"agent": "", "route": "", "volume": "", "instructions": ""},
    "positioning_equipment": {"patient_position": "", "equipment_setup": "", "sid": "100 - 115 cm"},
    "fluoro_params": {
        "mode": "Fluoroscopie Pulsată (7.5 - 15 fps) + LIH",
        "kv": "", "ma_range": "", "grid": "Cu grilă antidifuzoare",
        "filtration": "Totală ≥ 3.0 mm Al + 0.1 mm Cu", "target_fluoro_time": "< 3 minute", "lih": "Activ",
    },
    "tech_params": {
        "kv": "", "mas": "", "aec": "", "slice_thickness": "",
        "collimation": "", "rotation_time": "", "pitch": "", "scan_mode": "",
    },
    "safety": {"renal": "", "allergy": ""},
    "coils_hardware": {"coil": "", "field_strength": "", "positioning": ""},
    "sequences": [],
    "safety_considerations": [],
    "acquisition_steps": [],
    "quality_criteria": [],
    "radiation_safety": [],
    "transducers_equipment": {"transducer_types": "", "patient_position": "", "gel_acoustic_window": ""},
    "technical_settings": {"preset": "", "modes": "", "focus_depth": "", "gain_thi": "", "measurements_criteria": ""},
    "standard_views": [],
    "safety_and_limitations": [],
    "images": [],
    "iris_reference": {"chapter": "", "recommendation_grade": "Grad A", "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)"},
    "notes": "",
}

EMPTY_IRM_FM: dict = {
    "title": "",
    "slug": "",
    "category": "neuro",
    "modality": "irm",
    "author": "Departamentul de Radiologie și Imagistică Medicală",
    "last_updated": str(date.today()),
    "clinical_indications": [],
    "contraindications": [],
    "patient_prep": "",
    "coils_hardware": {
        "coil": "",
        "field_strength": "1.5 Tesla / 3.0 Tesla",
        "positioning": "",
    },
    "contrast": {
        "agent": "",
        "dose": "0.1 mmol/kg corp",
        "flow_rate": "",
        "timing": "",
        "notes": "",
    },
    "sequences": [],
    "quality_criteria": [],
    "safety_considerations": [],
    "iris_reference": {
        "chapter": "Imagistică prin Rezonanță Magnetică (IRM)",
        "recommendation_grade": "Grad A",
        "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
    },
    "notes": "",
    "position": "",
    "tech_params": {
        "kv": "", "mas": "", "aec": "", "slice_thickness": "",
        "collimation": "", "rotation_time": "", "pitch": "", "scan_mode": "",
    },
    "positioning_equipment": {"patient_position": "", "equipment_setup": "", "sid": ""},
    "fluoro_params": {"mode": "", "kv": "", "ma_range": "", "grid": "", "filtration": "", "target_fluoro_time": "", "lih": ""},
    "safety": {"renal": "", "allergy": ""},
    "transducers_equipment": {"transducer_types": "", "patient_position": "", "gel_acoustic_window": ""},
    "technical_settings": {"preset": "", "modes": "", "focus_depth": "", "gain_thi": "", "measurements_criteria": ""},
    "standard_views": [],
    "safety_and_limitations": [],
    "images": [],
}

EMPTY_ECO_FM: dict = {
    "title": "",
    "slug": "",
    "category": "abdomen-pelvis",
    "modality": "eco",
    "author": "Departamentul de Radiologie și Imagistică Medicală",
    "last_updated": str(date.today()),
    "clinical_indications": [],
    "contraindications": [],
    "patient_prep": "",
    "transducers_equipment": {
        "transducer_types": "Sondă Convexă 3.5 - 5.0 MHz / Sondă Liniară 7.5 - 14.0 MHz",
        "patient_position": "Decubit dorsal",
        "gel_acoustic_window": "Gel ecografic hipoalergenic",
    },
    "technical_settings": {
        "preset": "Abdomen General",
        "modes": "Mod B (2D) + Doppler Color (CFM) + Doppler Pulsat (PW)",
        "focus_depth": "Focalizare automată adaptată organului țintă",
        "gain_thi": "THI activat, reglaj TGC uniform",
        "measurements_criteria": "Măsurători biometrice în două axe perpendiculare",
    },
    "standard_views": [],
    "quality_criteria": [],
    "safety_and_limitations": [],
    "iris_reference": {
        "chapter": "Ecografie & Ultrasonografie",
        "recommendation_grade": "Grad A",
        "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
    },
    "notes": "",
    "position": "",
    "tech_params": {
        "kv": "", "mas": "", "aec": "", "slice_thickness": "",
        "collimation": "", "rotation_time": "", "pitch": "", "scan_mode": "",
    },
    "contrast": {"agent": "", "volume": "", "flow_rate": "", "duration": "", "timing": "", "roi": "", "trigger": "", "dose": "", "notes": ""},
    "safety": {"renal": "", "allergy": ""},
    "positioning_equipment": {"patient_position": "", "equipment_setup": "", "sid": ""},
    "fluoro_params": {"mode": "", "kv": "", "ma_range": "", "grid": "", "filtration": "", "target_fluoro_time": "", "lih": ""},
    "coils_hardware": {"coil": "", "field_strength": "", "positioning": ""},
    "sequences": [],
    "safety_considerations": [],
    "images": [],
    "series": [],
    "recons": [],
}


def _ensure_fm_keys(fm: dict, modality: str = "ct") -> dict:
    """Merge fm with defaults so templates never get KeyError."""
    if modality == "eco" or fm.get("modality") == "eco":
        result = {}
        for key, default in EMPTY_ECO_FM.items():
            val = fm.get(key, default)
            if isinstance(default, dict) and not isinstance(val, dict):
                val = default.copy()
            elif isinstance(default, list) and not isinstance(val, list):
                val = default.copy()
            result[key] = val
        for sub in ("transducers_equipment", "technical_settings", "iris_reference", "contrast", "tech_params", "safety", "coils_hardware", "positioning_equipment", "fluoro_params"):
            if not isinstance(result.get(sub), dict):
                result[sub] = {}
            default_sub = EMPTY_ECO_FM.get(sub, {})
            if isinstance(default_sub, dict):
                for k, v in default_sub.items():
                    result[sub].setdefault(k, v)
        for sub in ("clinical_indications", "contraindications", "standard_views", "quality_criteria", "safety_and_limitations", "sequences", "safety_considerations"):
            if not isinstance(result.get(sub), list):
                result[sub] = []
        if not isinstance(result.get("images"), list):
            result["images"] = []
        if not isinstance(result.get("notes"), str):
            result["notes"] = ""
        result.setdefault("position", "")
        return result
    elif modality == "irm" or fm.get("modality") == "irm":
        result = {}
        for key, default in EMPTY_IRM_FM.items():
            val = fm.get(key, default)
            if isinstance(default, dict) and not isinstance(val, dict):
                val = default.copy()
            elif isinstance(default, list) and not isinstance(val, list):
                val = default.copy()
            result[key] = val
        for sub in ("coils_hardware", "contrast", "iris_reference", "tech_params", "positioning_equipment", "fluoro_params", "safety"):
            if not isinstance(result.get(sub), dict):
                result[sub] = {}
            default_sub = EMPTY_IRM_FM.get(sub, {})
            if isinstance(default_sub, dict):
                for k, v in default_sub.items():
                    result[sub].setdefault(k, v)
        for sub in ("clinical_indications", "contraindications", "sequences", "quality_criteria", "safety_considerations"):
            if not isinstance(result.get(sub), list):
                result[sub] = []
        if not isinstance(result.get("images"), list):
            result["images"] = []
        if not isinstance(result.get("notes"), str):
            result["notes"] = ""
        result.setdefault("position", "")
        return result
    elif modality == "fluoro" or fm.get("modality") == "fluoro":
        result = {}
        for key, default in EMPTY_FLUORO_FM.items():
            val = fm.get(key, default)
            if isinstance(default, dict) and not isinstance(val, dict):
                val = default.copy()
            elif isinstance(default, list) and not isinstance(val, list):
                val = default.copy()
            result[key] = val
        for sub in ("contrast", "positioning_equipment", "fluoro_params", "iris_reference", "tech_params", "safety", "coils_hardware"):
            if not isinstance(result.get(sub), dict):
                result[sub] = {}
            default_sub = EMPTY_FLUORO_FM.get(sub, {})
            if isinstance(default_sub, dict):
                for k, v in default_sub.items():
                    result[sub].setdefault(k, v)
        for sub in ("clinical_indications", "contraindications", "acquisition_steps", "quality_criteria", "radiation_safety", "sequences", "safety_considerations"):
            if not isinstance(result.get(sub), list):
                result[sub] = []
        if not isinstance(result.get("images"), list):
            result["images"] = []
        if not isinstance(result.get("notes"), str):
            result["notes"] = ""
        result.setdefault("position", "")
        return result
    elif modality == "rx" or fm.get("modality") == "rx":
        result = {}
        for key, default in EMPTY_RX_FM.items():
            val = fm.get(key, default)
            if isinstance(default, dict) and not isinstance(val, dict):
                val = default.copy()
            elif isinstance(default, list) and not isinstance(val, list):
                val = default.copy()
            result[key] = val
        for sub in ("tech_params", "iris_reference", "contrast", "safety", "positioning_equipment", "fluoro_params", "coils_hardware"):
            if not isinstance(result.get(sub), dict):
                result[sub] = {}
            default_sub = EMPTY_RX_FM.get(sub, {})
            if isinstance(default_sub, dict):
                for k, v in default_sub.items():
                    result[sub].setdefault(k, v)
        for sub in ("clinical_indications", "quality_criteria", "protection", "sequences", "safety_considerations"):
            if not isinstance(result.get(sub), list):
                result[sub] = []
        if not isinstance(result.get("images"), list):
            result["images"] = []
        if not isinstance(result.get("notes"), str):
            result["notes"] = ""
        result.setdefault("position", "")
        return result
    else:
        result = {}
        for key, default in EMPTY_FM.items():
            val = fm.get(key, default)
            if isinstance(default, dict) and not isinstance(val, dict):
                val = default.copy()
            elif isinstance(default, list) and not isinstance(val, list):
                val = default.copy()
            result[key] = val
        for sub in ("contrast", "notes", "safety", "tech_params", "coils_hardware", "positioning_equipment", "fluoro_params", "iris_reference"):
            if not isinstance(result.get(sub), dict):
                result[sub] = {}
            default_sub = EMPTY_FM.get(sub, {})
            if isinstance(default_sub, dict):
                for k, v in default_sub.items():
                    result[sub].setdefault(k, v)
        result.setdefault("position", "")
        if not isinstance(result.get("clinical_indications"), list):
            result["clinical_indications"] = []
        if not isinstance(result.get("synonyms"), list):
            result["synonyms"] = []
        if not isinstance(result.get("sequences"), list):
            result["sequences"] = []
        if not isinstance(result.get("safety_considerations"), list):
            result["safety_considerations"] = []
        if not isinstance(result.get("images"), list):
            result["images"] = []
        return result


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.route("/assets/<path:path>")
def serve_assets(path):
    return send_from_directory(REPO_ROOT / "docs" / "assets", path)


@app.route("/docs/assets/<path:path>")
def serve_docs_assets(path):
    return send_from_directory(REPO_ROOT / "docs" / "assets", path)


@app.route("/api/upload_image", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"success": False, "error": "Niciun fișier nu a fost încărcat."})
    file = request.files["file"]
    if not file or not file.filename:
        return jsonify({"success": False, "error": "Numele fișierului este vid."})

    import re
    import time

    ext = Path(file.filename).suffix.lower()
    allowed = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"}
    if ext not in allowed:
        return jsonify({"success": False, "error": f"Format nepermis ({ext}). Folosiți PNG, JPG, JPEG, WEBP, SVG sau GIF."})

    stem = Path(file.filename).stem
    safe_stem = re.sub(r"[^a-zA-Z0-9_-]", "_", stem).strip("_") or "image"
    safe_name = f"{int(time.time())}_{safe_stem}{ext}"

    DOCS_ASSETS_IMAGES_PROTOCOLS.mkdir(parents=True, exist_ok=True)
    target_file = DOCS_ASSETS_IMAGES_PROTOCOLS / safe_name
    file.save(str(target_file))

    rel_url = f"assets/images/protocols/{safe_name}"
    return jsonify({
        "success": True,
        "filename": safe_name,
        "url": rel_url,
    })


@app.route("/")
def index():
    protocols = load_all_protocols()
    return render_template_string(LIST_TEMPLATE, protocols=protocols)


@app.route("/edit/<slug>", methods=["GET", "POST"])
def edit(slug: str):
    item = find_protocol(slug)
    if item is None:
        return f"Protocol '{slug}' not found.", 404

    is_eco = item["fm"].get("modality") == "eco" or "docs/eco" in str(item["filepath"]).replace("\\", "/")
    is_irm = (not is_eco) and (item["fm"].get("modality") == "irm" or "docs/irm" in str(item["filepath"]).replace("\\", "/"))
    is_fluoro = (not is_eco) and (not is_irm) and (item["fm"].get("modality") == "fluoro" or "docs/fluoro" in str(item["filepath"]).replace("\\", "/"))
    is_rx = (not is_eco) and (not is_irm) and (not is_fluoro) and (item["fm"].get("modality") == "rx" or "docs/rx" in str(item["filepath"]).replace("\\", "/"))

    if request.method == "POST":
        try:
            original_fm = item["fm"]
            default_mod = "eco" if is_eco else ("irm" if is_irm else ("fluoro" if is_fluoro else ("rx" if is_rx else "ct")))
            modality_posted = request.form.get("modality", default_mod).lower()
            if modality_posted == "eco" or is_eco:
                fm = form_to_eco_frontmatter(request.form)
                fm["slug"] = slug
                fm["modality"] = "eco"
                md_content = render_eco_document(fm)
            elif modality_posted == "irm" or is_irm:
                fm = form_to_irm_frontmatter(request.form)
                fm["slug"] = slug
                fm["modality"] = "irm"
                md_content = render_irm_document(fm)
            elif modality_posted == "fluoro" or is_fluoro:
                fm = form_to_fluoro_frontmatter(request.form)
                fm["slug"] = slug
                fm["modality"] = "fluoro"
                md_content = render_fluoro_document(fm)
            elif modality_posted == "rx" or is_rx:
                fm = form_to_rx_frontmatter(request.form)
                fm["slug"] = slug
                fm["modality"] = "rx"
                md_content = render_rx_document(fm)
            else:
                fm = form_to_frontmatter(request.form)
                fm["slug"] = slug
                if "tech_params" in original_fm:
                    merged_tp = original_fm["tech_params"].copy()
                    for k, v in fm.get("tech_params", {}).items():
                        if v:
                            merged_tp[k] = v
                    fm["tech_params"] = merged_tp
                if original_fm.get("notes", {}).get("additional_recons"):
                    fm.setdefault("notes", {})["additional_recons"] = original_fm["notes"]["additional_recons"]
                md_content = render_document(fm)

            item["filepath"].write_text(md_content, encoding="utf-8")
            failures = rebuild_indexes()
            trigger_background_build()
            if failures:
                return jsonify({"success": True, "warnings": failures})
            return jsonify({"success": True})
        except Exception as exc:
            return jsonify({"success": False, "error": str(exc)})

    mod_str = "eco" if is_eco else ("irm" if is_irm else ("fluoro" if is_fluoro else ("rx" if is_rx else "ct")))
    fm = _ensure_fm_keys(item["fm"], modality=mod_str)
    category_val = fm.get("category", "")
    frontend_url = f"http://localhost:8000/radiology-protocols/{mod_str}/{category_val}/{slug}/"
    highlighted = set()
    reviewing_request = False
    apply_param = request.args.get("apply", "")
    if apply_param:
        try:
            padding = "=" * ((4 - len(apply_param) % 4) % 4)
            apply_changes = json.loads(base64.b64decode(apply_param + padding))
            fm, highlighted = apply_changes_to_fm(fm, apply_changes)
            reviewing_request = True
        except Exception as exc:
            reviewing_request = f"Could not decode change request link: {exc}"

    categories = ECO_CATEGORIES if is_eco else (IRM_CATEGORIES if is_irm else (FLUORO_CATEGORIES if is_fluoro else (RX_CATEGORIES if is_rx else CT_CATEGORIES)))
    return render_template_string(
        FORM_TEMPLATE,
        page_title=f"Editează: {fm['title']}",
        fm=fm,
        frontend_url=frontend_url,
        is_rx=is_rx,
        is_fluoro=is_fluoro,
        is_irm=is_irm,
        is_eco=is_eco,
        categories=categories,
        eco_categories=ECO_CATEGORIES,
        irm_categories=IRM_CATEGORIES,
        fluoro_categories=FLUORO_CATEGORIES,
        rx_categories=RX_CATEGORIES,
        ct_categories=CT_CATEGORIES,
        is_new=False,
        save_url=url_for("edit", slug=slug),
        series_json=json.dumps(fm.get("series", []) if (not is_rx and not is_fluoro and not is_irm and not is_eco) else []),
        recons_json=json.dumps(fm.get("recons", []) if (not is_rx and not is_fluoro and not is_irm and not is_eco) else []),
        sequences_json=json.dumps(fm.get("sequences", []) if is_irm else []),
        views_json=json.dumps(fm.get("standard_views", []) if is_eco else []),
        images_json=json.dumps(fm.get("images", [])),
        all_protocols=[],
        protocols_map_json="{}",
        highlighted=highlighted,
        reviewing_request=reviewing_request,
    )


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        import re as _re
        try:
            modality = request.form.get("modality", "ct").lower()
            if modality == "eco":
                fm = form_to_eco_frontmatter(request.form)
                cats = ECO_CATEGORIES
                base_dir = DOCS_ECO
                render_fn = render_eco_document
            elif modality == "irm":
                fm = form_to_irm_frontmatter(request.form)
                cats = IRM_CATEGORIES
                base_dir = DOCS_IRM
                render_fn = render_irm_document
            elif modality == "fluoro":
                fm = form_to_fluoro_frontmatter(request.form)
                cats = FLUORO_CATEGORIES
                base_dir = DOCS_FLUORO
                render_fn = render_fluoro_document
            elif modality == "rx":
                fm = form_to_rx_frontmatter(request.form)
                cats = RX_CATEGORIES
                base_dir = DOCS_RX
                render_fn = render_rx_document
            else:
                fm = form_to_frontmatter(request.form)
                cats = CT_CATEGORIES
                base_dir = DOCS_CT
                render_fn = render_document

            slug = fm.get("slug", "").strip()
            if not slug:
                return jsonify({"success": False, "error": "Slug is required."})
            if not _re.fullmatch(r'[a-z0-9][a-z0-9-]*', slug):
                return jsonify({"success": False, "error": "Slug must contain only lowercase letters, digits, and hyphens."})
            category = fm.get("category", cats[0])
            if category not in cats:
                return jsonify({"success": False, "error": f"Invalid category: {category}"})
            target_path = base_dir / category / f"{slug}.md"
            if not str(target_path.resolve()).startswith(str(base_dir.resolve())):
                return jsonify({"success": False, "error": "Invalid path."})
            if target_path.exists():
                return jsonify({"success": False, "error": f"File already exists: {target_path.relative_to(REPO_ROOT)}"})
            target_path.parent.mkdir(parents=True, exist_ok=True)
            md_content = render_fn(fm)
            target_path.write_text(md_content, encoding="utf-8")
            failures = rebuild_indexes()
            trigger_background_build()
            if failures:
                return jsonify({"success": True, "redirect": url_for("edit", slug=slug), "warnings": failures})
            return jsonify({"success": True, "redirect": url_for("edit", slug=slug)})
        except Exception as exc:
            return jsonify({"success": False, "error": str(exc)})

    modality = request.args.get("modality", "ct").lower()
    is_eco = modality == "eco"
    is_irm = (not is_eco) and (modality == "irm")
    is_fluoro = (not is_eco) and (not is_irm) and (modality == "fluoro")
    is_rx = (not is_eco) and (not is_irm) and (not is_fluoro) and (modality == "rx")
    categories = ECO_CATEGORIES if is_eco else (IRM_CATEGORIES if is_irm else (FLUORO_CATEGORIES if is_fluoro else (RX_CATEGORIES if is_rx else CT_CATEGORIES)))
    fm = _ensure_fm_keys({}, modality=modality)
    all_protocols = load_all_protocols()
    protocols_map = {
        p["fm"]["slug"]: {
            "modality": p["fm"].get("modality", "ct"),
            "category": p["fm"].get("category", ""),
            "title": p["fm"].get("title", ""),
            "fm": p["fm"],
        }
        for p in all_protocols
        if p["fm"].get("slug")
    }
    protocols_map_json = json.dumps(protocols_map, default=str)
    return render_template_string(
        FORM_TEMPLATE,
        page_title="Protocol Nou",
        fm=fm,
        frontend_url="",
        is_rx=is_rx,
        is_fluoro=is_fluoro,
        is_irm=is_irm,
        is_eco=is_eco,
        categories=categories,
        eco_categories=ECO_CATEGORIES,
        irm_categories=IRM_CATEGORIES,
        fluoro_categories=FLUORO_CATEGORIES,
        rx_categories=RX_CATEGORIES,
        ct_categories=CT_CATEGORIES,
        is_new=True,
        save_url=url_for("new"),
        series_json="[]",
        recons_json="[]",
        sequences_json="[]",
        views_json="[]",
        images_json="[]",
        all_protocols=all_protocols,
        protocols_map_json=protocols_map_json,
        highlighted=set(),
        reviewing_request=False,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = 5173
    url = f"http://localhost:{port}"
    print(f"Starting Protocol Manager Admin at {url}")
    # Open browser after a short delay so Flask is ready
    import threading
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(host="127.0.0.1", port=port, debug=False)
