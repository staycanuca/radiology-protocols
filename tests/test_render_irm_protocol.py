"""test_render_irm_protocol.py — Teste unitare pentru generatorul de protocoale IRM."""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from render_irm_protocol import render_irm_document


@pytest.fixture
def base_irm_fm():
    return {
        "title": "IRM Cerebral Nativ și cu Substanță de Contrast",
        "slug": "irm-cerebral-nativ-si-cu-contrast",
        "category": "neuro",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Cefalee cronică persistentă cu caractere de alarmă",
            "Suspiciune de leziune expansivă intracraniană (tumoare, metastază)",
            "Patologie demielinizantă (scleroză multiplă)",
        ],
        "contraindications": [
            "Stimulator cardiac sau defibrilator implantabil non-MR Conditional",
            "Clipurilor anevrismale intracraniene feromagnetice",
            "Corpi străini metalici intraoculari",
        ],
        "patient_prep": "Completare chestionar securitate RM; îndepărtare bijuterii, lentile de contact",
        "coils_hardware": {
            "coil": "Antenă Head/Neck 32 sau 64 canale",
            "field_strength": "1.5 Tesla / 3.0 Tesla",
            "positioning": "Decubit dorsal, capul fixat în antenă cu pernuțe de spumă, centrare nasion",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic (ex. Gadobutrol / Gadoterat)",
            "dose": "0.1 mmol/kg corp",
            "flow_rate": "1.5 - 2.0 ml/s + flush 20 ml ser fiziologic",
            "timing": "Secvențe post-contrast T1 la 2-5 minute după injectare",
            "notes": "Verificare eGFR > 30 ml/min/1.73m² conform ghidului ESUR",
        },
        "sequences": [
            {
                "name": "Sagital T1 SE / TSE",
                "plane": "Sagital",
                "tr_te": "TR 500 ms / TE 10 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Anatomie linia mediană, corp calos",
            },
            {
                "name": "Axial T2 TSE",
                "plane": "Axial",
                "tr_te": "TR 4500 ms / TE 100 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 384x288",
                "fat_sat": "Nu",
                "notes": "Aliniere la linia CA-CP",
            },
            {
                "name": "Axial FLAIR",
                "plane": "Axial",
                "tr_te": "TR 9000 ms / TE 90 ms / TI 2500 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 320x224",
                "fat_sat": "Nu",
                "notes": "Atenuare semnal LCR liber",
            },
            {
                "name": "Axial DWI (b=0, 1000) + ADC",
                "plane": "Axial",
                "tr_te": "TR 3500 ms / TE 70 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 192x192",
                "fat_sat": "FatSat",
                "notes": "Restricție de difuzie în AVC ischemic acut sau abces",
            },
            {
                "name": "3D T1 GRE + Contrast (MPRAGE)",
                "plane": "3D Sagital Izotrop",
                "tr_te": "TR 1900 ms / TE 2.5 ms / TI 900 ms",
                "slice_gap": "1.0 mm izotrop",
                "fov_matrix": "FOV 256 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Reconstrucții multiplanare MPR subțiri",
            },
        ],
        "quality_criteria": [
            "Raport semnal-zgomot (SNR) înalt cu delimitare netă a substanței albe de cea cenușie",
            "Absența artefactelor de mișcare ale pacientului sau de pulsație vasculară",
            "Acoperire completă de la vertex până la foramen magnum",
        ],
        "safety_considerations": [
            "SAR în mod normal de operare (< 2.0 W/kg)",
            "Protecție fonică obligatorie cu căști auditive",
            "Supraveghere vizuală și comunicare prin interfon",
        ],
        "iris_reference": {
            "chapter": "Sistem Nervos Central - Neuroimagistică",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "În suspiciunea de scleroză multiplă se adaugă Sagital 3D FLAIR.",
    }


def test_render_irm_document_contains_yaml_and_structure(base_irm_fm):
    md = render_irm_document(base_irm_fm)
    assert md.startswith("---\n")
    assert "modality: irm" in md
    assert "title: IRM Cerebral Nativ și cu Substanță de Contrast" in md
    assert "# IRM Cerebral Nativ și cu Substanță de Contrast" in md
    assert "🧲 Imagistică prin Rezonanță Magnetică (IRM)" in md


def test_render_irm_document_contains_sequences_table(base_irm_fm):
    md = render_irm_document(base_irm_fm)
    assert "Axial T2 TSE" in md
    assert "Axial FLAIR" in md
    assert "Axial DWI" in md
    assert "3D T1 GRE + Contrast (MPRAGE)" in md
    assert "TR 4500 ms / TE 100 ms" in md
    assert "1.0 mm izotrop" in md


def test_render_irm_document_contains_iris_and_safety(base_irm_fm):
    md = render_irm_document(base_irm_fm)
    assert "Ghidul Național IRIS" in md
    assert "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)" in md
    assert "Screening Feromagnetic Riguros (Zona III -> Zona IV)" in md
    assert "Rată Specifică de Absorbție (SAR)" in md


def test_render_irm_document_empty_sequences_fallback():
    fm = {
        "title": "IRM Test",
        "slug": "irm-test",
        "category": "neuro",
        "modality": "irm",
        "sequences": [],
    }
    md = render_irm_document(fm)
    assert "Secvență Achiziție" in md
    assert "Conform protocolului specific" in md
