"""test_render_eco_protocol.py — Teste unitare pentru generatorul de documente Ecografie/Ultrasonografie."""

import os
import sys

import pytest
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from render_eco_protocol import render_eco_document


@pytest.fixture
def sample_eco_fm():
    return {
        "title": "Ecografie Abdomen Total",
        "slug": "eco-abdomen-total",
        "category": "abdomen-pelvis",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Durere abdominală acută sau cronică",
            "Hepatomegalie și evaluare steatoză",
            "Litiaza biliară și colică biliară",
        ],
        "contraindications": [
            "Lipsă fereastră acustică adecvată din cauza meteorismului abdominal sever",
            "Pansamente ocluzive abdominale întinse",
        ],
        "patient_prep": "À jeun (post alimentar) minimum 6 ore anterior examinării; vezică urinară în repleție moderată.",
        "transducers_equipment": {
            "transducer_types": "Sondă Convexă 3.5 - 5.0 MHz (screening de adâncime) și Sondă Liniară 7.5 - 12.0 MHz (perete/apendice)",
            "patient_position": "Decubit dorsal, completat cu decubit lateral stâng pentru hil hepatic și splină",
            "gel_acoustic_window": "Gel ecografic apos hipoalergenic în cantitate suficientă",
        },
        "technical_settings": {
            "preset": "Abdomen General",
            "modes": "Mod B (2D grayscale) + Doppler Color (CFM) + Doppler Pulsat (PW)",
            "focus_depth": "Focar ajustat la nivelul lobului hepatic drept (8-12 cm)",
            "gain_thi": "THI (Tissue Harmonic Imaging) activat pentru optimizarea raportului semnal/zgomot",
            "measurements_criteria": "Diametru craniocaudal lob drept hepatic (<150 mm), grosime perete colecist (<3 mm), ax lung renal (100-120 mm)",
        },
        "standard_views": [
            {
                "view": "Secțiune longitudinală subcostală",
                "anatomical_target": "Lob hepatic stâng și aortă",
                "landmarks": "Lobul stâng anterior de aorta abdominală și trunchiul celiac",
                "normal_aspect": "Ecostructură fină omogenă, bord ascuțit, calibru aortic normal",
            },
            {
                "view": "Secțiune oblică recurentă intercostală",
                "anatomical_target": "Colecist și hil hepatic",
                "landmarks": "Vena portă, cale biliară principală și arteră hepatică",
                "normal_aspect": "Colecist alitiazic, perete subțire <3 mm, CBP <6 mm",
            }
        ],
        "quality_criteria": [
            "Vizualizarea completă a contururilor hepatice și a diafragmului",
            "Penetrare acustică optimă până la nivelul peretelui posterior al organelor retroperitoneale",
            "Absența zonelor oarbe prin utilizarea ferestrelor intercostale și a apneei în inspir profund",
        ],
        "safety_and_limitations": [
            "Indice mecanic (MI) < 1.0 și indice termic (TIB/TIS) < 1.0 conform principiului ALARA",
            "Limitare prin interpoziție gazoasă digestivă și atenuare acustică la pacienți obezi",
        ],
        "iris_reference": {
            "chapter": "Aparat Digestiv & Abdomen",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "În caz de suspiciune de colecistită acută se testează semnul Murphy ecografic la compresia directă cu sonda.",
    }


def test_render_eco_document_contains_yaml_frontmatter(sample_eco_fm):
    doc = render_eco_document(sample_eco_fm)
    assert doc.startswith("---\n")
    end = doc.find("\n---\n", 3)
    assert end != -1
    yaml_str = doc[3:end]
    parsed_yaml = yaml.safe_load(yaml_str)
    assert parsed_yaml["title"] == "Ecografie Abdomen Total"
    assert parsed_yaml["modality"] == "eco"
    assert parsed_yaml["category"] == "abdomen-pelvis"
    assert len(parsed_yaml["standard_views"]) == 2


def test_render_eco_document_sections_and_iris(sample_eco_fm):
    doc = render_eco_document(sample_eco_fm)
    assert "# Ecografie Abdomen Total" in doc
    assert "📡 Ecografie &amp; Ultrasonografie (US)" in doc
    assert "Durere abdominală acută sau cronică" in doc
    assert "Sondă Convexă 3.5 - 5.0 MHz" in doc
    assert "Abdomen General" in doc
    assert "Secțiune longitudinală subcostală" in doc
    assert "Ghid Național IRIS" in doc
    assert "Aparat Digestiv & Abdomen" in doc
    assert "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)" in doc
    assert "semnul Murphy ecografic" in doc


def test_render_eco_document_empty_views():
    fm = {
        "title": "Ecografie Test Minimal",
        "slug": "eco-test-minimal",
        "category": "parti-moi-endocrin",
        "modality": "eco",
        "standard_views": [],
    }
    doc = render_eco_document(fm)
    assert "# Ecografie Test Minimal" in doc
    assert "Conform tehnicii de scanare standard" in doc
