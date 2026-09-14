"""test_render_fluoro_protocol.py — Teste unitare pentru generatorul de protocoale de Fluoroscopie și C-Arm."""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from render_fluoro_protocol import render_fluoro_document


@pytest.fixture
def base_fluoro_fm():
    return {
        "title": "Tranzit Esofago-Gastro-Duodenal (TEGD) - Dublu Contrast",
        "slug": "tranzit-esofago-gastro-duodenal-tegd",
        "category": "digestiv",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Reflux gastro-esofagian cronic și hernie hiatală",
            "Suspiciune ulcer gastric sau bulbar",
        ],
        "contraindications": [
            "Suspiciune de perforație (contraindicație pentru Sulfatul de Bariu)",
        ],
        "patient_prep": "À jeun minim 8 ore; fără fumat sau gumă de mestecat",
        "contrast": {
            "agent": "Sulfat de Bariu densitate înaltă 200-250% w/v + granule efervescente",
            "route": "Orală (per os)",
            "volume": "150 - 200 ml",
            "instructions": "Pacientul înghite granulele și nu eructează",
        },
        "positioning_equipment": {
            "patient_position": "Ortostatism urmat de decubit dorsal și Trendelenburg 15°",
            "equipment_setup": "Masă telecomandată basculantă 90°/15°",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată 7.5 - 15 fps + LIH",
            "kv": "90 - 105 kV",
            "ma_range": "1.5 - 4.0 mA",
            "grid": "Cu grilă antidifuzoare",
            "filtration": "≥ 3.0 mm Al + 0.1 mm Cu",
            "target_fluoro_time": "< 3.5 minute",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {"phase": "Fază Esofagiană", "description": "Pasaj în OAD 35-40°"},
            {"phase": "Dublu Contrast Gastric", "description": "Rotire 360° a pacientului"},
        ],
        "quality_criteria": [
            "Distensie gazoasă gastrică optimă fără colabare",
            "Tapetare fină continuă cu bariu pe falduri",
        ],
        "radiation_safety": [
            "Scopie pulsată joasă",
            "Timp total de scopie < 3.5 minute",
            "DAP < 15 Gy·cm²",
        ],
        "iris_reference": {
            "chapter": "Stomac & Duoden",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "notes": "În caz de stomac operat se verifică ansa eferentă.",
    }


def test_fluoro_document_starts_with_fence(base_fluoro_fm):
    doc = render_fluoro_document(base_fluoro_fm)
    assert doc.startswith("---\n")
    assert "slug: tranzit-esofago-gastro-duodenal-tegd" in doc
    assert "modality: fluoro" in doc


def test_fluoro_document_structure_and_cards(base_fluoro_fm):
    doc = render_fluoro_document(base_fluoro_fm)
    assert "# Tranzit Esofago-Gastro-Duodenal (TEGD) - Dublu Contrast" in doc
    assert "✨ Fluoroscopie & C-Arm" in doc
    assert "1. Rezumat Clinic, Indicații & Contraindicații" in doc
    assert "2. Pregătire Pacient & Substanță de Contrast" in doc
    assert "3. Poziționare & Configurare Echipament (Masă / C-Arm)" in doc
    assert "4. Parametri Tehnici Scopie & Expunere" in doc
    assert "5. Secvență Achiziție & Incidențe Seriate" in doc
    assert "6. Criterii de Calitate & Diagnostic" in doc
    assert "7. Radioprotecție & Dozimetrie (ALARA)" in doc
    assert "Ghid Rapid de Execuție & Siguranță Fluoroscopică" in doc


def test_fluoro_document_contrast_and_params(base_fluoro_fm):
    doc = render_fluoro_document(base_fluoro_fm)
    assert "Sulfat de Bariu densitate înaltă" in doc
    assert "90 - 105 kV" in doc
    assert "Fluoroscopie Pulsată 7.5 - 15 fps + LIH" in doc
    assert "100 - 115 cm" in doc


def test_fluoro_document_iris_reference(base_fluoro_fm):
    doc = render_fluoro_document(base_fluoro_fm)
    assert "Ghid Național IRIS" in doc
    assert "Stomac & Duoden" in doc
    assert "Grad A" in doc
    assert "Clasa 2 (Medie 1 - 5 mSv)" in doc
