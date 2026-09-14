"""test_render_rx_protocol.py — Teste unitare pentru generatorul de protocoale Rx."""

import os
import sys

import pytest
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from render_rx_protocol import render_rx_document


@pytest.fixture
def base_rx_fm():
    return {
        "title": "Rx Torace PA",
        "slug": "rx-torace-pa",
        "modality": "rx",
        "category": "torace",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Suspiciune pneumonie sau infecție respiratorie",
            "Dispnee acută",
        ],
        "position": "Ortostatism cu fața anterioară a toracelui lipită de detectorul vertical",
        "sid_dff": "180 cm",
        "centering": "Nivel T7 (unghiul inferior al omoplaților)",
        "breathing": "Apnee în inspir profund susținut",
        "tech_params": {
            "kv": "125",
            "mas": "2.5",
            "grid": "Cu grilă antidifuzoare (Bucky)",
            "focal_spot": "Focar Mare (1.2 mm)",
            "aec_chambers": "Camerele laterale activate",
            "collimation": "De la apexuri la unghiurile costodiafragmatice",
        },
        "quality_criteria": [
            "Vizualizare completă de la apexuri la sinusuri costodiafragmatice",
            "Inspir corect (9-10 arcuri costale posterioare)",
            "Omoplați proiectați în afara câmpurilor pulmonare",
        ],
        "protection": [
            "Șorț de plumb pe abdomen și bazin",
            "Colimare strictă conform ALARA",
        ],
        "iris_reference": {
            "chapter": "Torace & Pulmon",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.1 mSv)",
        },
    }


def test_rx_document_starts_with_fence(base_rx_fm):
    doc = render_rx_document(base_rx_fm)
    assert doc.startswith("---\n")
    assert "slug: rx-torace-pa" in doc


def test_rx_document_title_and_cards(base_rx_fm):
    doc = render_rx_document(base_rx_fm)
    assert "# Rx Torace PA" in doc
    assert "1. Rezumat Clinic & Indicații" in doc
    assert "2. Poziționare & Centrare Fascicul" in doc
    assert "3. Parametri Tehnici Expunere" in doc
    assert "4. Criterii de Calitate & Reușită Imagine" in doc
    assert "5. Protecție Radiologică (ALARA)" in doc


def test_rx_tech_params_table(base_rx_fm):
    doc = render_rx_document(base_rx_fm)
    assert "125 kV" in doc
    assert "2.5 mAs" in doc
    assert "180 cm" in doc
    assert "Cu grilă antidifuzoare (Bucky)" in doc
    assert "Focar Mare (1.2 mm)" in doc


def test_rx_iris_guide_reference(base_rx_fm):
    doc = render_rx_document(base_rx_fm)
    assert "Ghid Național IRIS" in doc
    assert "Torace & Pulmon" in doc
    assert "Grad A" in doc
    assert "Clasa 1 (Minimă < 0.1 mSv)" in doc
