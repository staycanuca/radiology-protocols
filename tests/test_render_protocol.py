"""Unit tests for scripts/render_protocol.py — written before implementation (TDD)."""
import sys
import os
import copy

import pytest
import yaml

# Allow importing from scripts/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from render_protocol import render_document


# ---------------------------------------------------------------------------
# Shared fixture — a complete, valid front matter dict
# ---------------------------------------------------------------------------

@pytest.fixture
def base_fm():
    return {
        'title': 'CT PE',
        'slug': 'ct-pe',
        'category': 'chest',
        'protocol_type': 'contrast-enhanced',
        'last_updated': '2026-01-01',
        'author': 'Dr. Smith',
        'synonyms': [],
        'clinical_indications': ['Suspected PE', 'Acute dyspnea'],
        'position': 'Supine feet-first',
        'npo': 'NPO 2 hours',
        'premedication': 'Metoprolol 5mg IV',
        'contrast': {
            'agent': 'Isovue 370',
            'volume': '1.3 mL/kg',
            'flow_rate': '5 mL/s',
            'duration': '15 - 20s',
            'timing': 'Bolus Tracking',
            'roi': 'Main PA',
            'trigger': '100 HU',
        },
        'series': [
            {
                'name': 'PA Phase',
                'start': 'Lung apices',
                'end': 'Costophrenic angles',
                'delay': 'Bolus tracked',
                'thickness': '0.625 mm',
                'notes': '',
            }
        ],
        'recons': [
            {
                'plane': 'Axial',
                'acquisition': 'Angiogram',
                'fov': 'Chest',
                'thickness_increment': '1.25 mm/1.25 mm',
                'kernel': 'Standard',
                'ir_strength': '3',
                'notes': '',
            }
        ],
        'notes': {
            'tech': 'Coach breath hold',
            'nursing': '20G IV',
            'rad': 'Assess RV/LV',
            'tips': 'Arms raised',
        },
        'safety': {
            'renal': 'eGFR > 30',
            'allergy': 'Check iodine',
        },
    }


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_document_starts_with_frontmatter_fence(base_fm):
    """Document must start with --- YAML fence."""
    doc = render_document(base_fm)
    assert doc.startswith('---\n')


def test_document_contains_closing_fence_and_title(base_fm):
    """Document must contain closing YAML fence and H1 title."""
    doc = render_document(base_fm)
    assert '\n---\n' in doc
    assert '# CT PE' in doc


def test_frontmatter_roundtrips_through_yaml(base_fm):
    """YAML front matter block must round-trip: slug and contrast.agent preserved."""
    doc = render_document(base_fm)
    # Extract the YAML block between the first --- and the closing ---
    parts = doc.split('---\n', 2)
    # parts[0] == '' (before first ---\n), parts[1] == yaml text, parts[2] == rest
    assert len(parts) >= 3, 'Expected at least two --- fences'
    parsed = yaml.safe_load(parts[1])
    assert parsed['slug'] == 'ct-pe'
    assert parsed['contrast']['agent'] == 'Isovue 370'


def test_contrast_section_rendered_when_present(base_fm):
    """When contrast agent is present, Injection Parameters table must appear."""
    doc = render_document(base_fm)
    assert 'Parametri de Injectare' in doc
    assert 'Isovue 370' in doc
    assert '5 mL/s' in doc


def test_no_contrast_message_when_agent_is_na(base_fm):
    """When contrast.agent == 'N/A', render no-contrast info block."""
    fm = copy.deepcopy(base_fm)
    fm['contrast']['agent'] = 'N/A'
    doc = render_document(fm)
    assert 'Fără Contrast Intravenos' in doc
    assert 'Parametri de Injectare' not in doc


def test_series_table_row_present(base_fm):
    """Series table row must contain series name and start location."""
    doc = render_document(base_fm)
    assert 'PA Phase' in doc
    assert 'Lung apices' in doc


def test_recons_table_row_present(base_fm):
    """Recons table row must contain thickness/increment and notes when provided."""
    fm = copy.deepcopy(base_fm)
    fm['recons'][0]['notes'] = 'Mediastinal window'
    doc = render_document(fm)
    assert '1.25 mm/1.25 mm' in doc
    assert 'Mediastinal window' in doc


def test_clinical_indications_rendered(base_fm):
    """All clinical indications must appear as list items."""
    doc = render_document(base_fm)
    assert 'Suspected PE' in doc
    assert 'Acute dyspnea' in doc


def test_notes_sections_rendered(base_fm):
    """All four notes fields must appear in the document."""
    doc = render_document(base_fm)
    assert 'Coach breath hold' in doc
    assert '20G IV' in doc
    assert 'Assess RV/LV' in doc
    assert 'Arms raised' in doc


def test_safety_in_nursing_tab(base_fm):
    """Safety renal and allergy fields must appear in the document."""
    doc = render_document(base_fm)
    assert 'eGFR > 30' in doc
    assert 'Check iodine' in doc


def test_premedication_pipe_separated_renders_as_bullets(base_fm):
    """Pipe-separated premedication string must be split into individual bullets."""
    fm = copy.deepcopy(base_fm)
    fm['premedication'] = 'Metoprolol 5mg IV | Check contraindications'
    doc = render_document(fm)
    assert 'Metoprolol 5mg IV' in doc
    assert 'Check contraindications' in doc


def test_empty_premedication_renders_none_required(base_fm):
    """Empty premedication field must render as 'Nu este necesară'."""
    fm = copy.deepcopy(base_fm)
    fm['premedication'] = ''
    doc = render_document(fm)
    assert 'Nu este necesară' in doc


def test_tech_params_section_rendered(base_fm):
    """Technical parameters card must be rendered with all key technical fields."""
    doc = render_document(base_fm)
    assert '4. Parametri Tehnici Achiziție' in doc
    assert 'Tensiune Tub (kV)' in doc
    assert 'Curent Tub (mAs)' in doc
    assert 'Control Automat al Expunerii (AEC)' in doc
    assert 'Grosime Secțiune Achiziție (Slice)' in doc
    assert 'Timp de Rotație' in doc
    assert 'Pitch (Factor Pas)' in doc
    assert 'Mod Scanare' in doc


def test_tech_params_custom_values(base_fm):
    """Custom technical parameters in front matter must appear in the rendered table."""
    fm = copy.deepcopy(base_fm)
    fm['tech_params'] = {
        'kv': '100',
        'mas': 'Auto (ref 180)',
        'aec': 'Care Dose 4D activat',
        'slice_thickness': '0.6 mm',
        'collimation': '128 x 0.6 mm',
        'rotation_time': '0.33s',
        'pitch': '0.8',
        'scan_mode': 'Elicoidal rapid',
    }
    doc = render_document(fm)
    assert '100 kV' in doc
    assert 'Auto (ref 180)' in doc
    assert 'Care Dose 4D activat' in doc
    assert '0.6 mm' in doc
    assert '128 x 0.6 mm' in doc
    assert '0.33 s' in doc
    assert '0.8' in doc
    assert 'Elicoidal rapid' in doc


def test_iris_guide_tab_rendered(base_fm):
    """IRIS National Guide reference tab must appear in Card 1."""
    doc = render_document(base_fm)
    assert 'Ghid Național IRIS' in doc
    assert 'Ordinul MS 1342/2012' in doc
    assert 'Torace & Pulmon' in doc
    assert '../../iris.md' in doc


def test_images_section_not_rendered_when_empty(base_fm):
    """When images list is missing or empty, images section must NOT appear in the rendered document."""
    fm = copy.deepcopy(base_fm)
    assert "images" not in fm
    doc = render_document(fm)
    assert "### 🖼️ Imagini" not in doc
    assert "protocol-gallery" not in doc
    assert "protocol-image-card" not in doc

    fm["images"] = []
    doc_empty = render_document(fm)
    assert "### 🖼️ Imagini" not in doc_empty
    assert "protocol-gallery" not in doc_empty
    assert "protocol-image-card" not in doc_empty


def test_images_section_rendered_when_present(base_fm):
    """When images are present, images section must render gallery and cards with proper URLs."""
    fm = copy.deepcopy(base_fm)
    fm["images"] = [
        {
            "url": "assets/images/protocols/pe_angio.png",
            "caption": "Angio-CT Trunchi Pulmonar",
            "description": "Opacifiere optimă a arterelor pulmonare fără artefacte de mișcare",
        },
        {
            "url": "https://example.com/external_scan.jpg",
            "caption": "Reconstrucție Coronală",
            "description": "",
        },
    ]
    doc = render_document(fm)
    assert "### 🖼️ Imagini" in doc
    assert '<div class="protocol-gallery" markdown>' in doc
    assert '<figure class="protocol-image-card" markdown>' in doc
    assert "![Angio-CT Trunchi Pulmonar](../../assets/images/protocols/pe_angio.png)" in doc
    assert "![Reconstrucție Coronală](https://example.com/external_scan.jpg)" in doc
    assert "<strong>Angio-CT Trunchi Pulmonar</strong> — <span>Opacifiere optimă a arterelor pulmonare fără artefacte de mișcare</span>" in doc
    assert "<strong>Reconstrucție Coronală</strong>" in doc


def test_images_section_across_all_modalities():
    """All 5 modalities (CT, RX, Fluoro, IRM, Eco) support the conditional images section."""
    from render_rx_protocol import render_rx_document
    from render_fluoro_protocol import render_fluoro_document
    from render_irm_protocol import render_irm_document
    from render_eco_protocol import render_eco_document

    img_data = [{"url": "assets/images/protocols/sample.png", "caption": "Imagine Mostră", "description": "Aspect"}]

    rx_fm = {"title": "Rx Test", "slug": "rx-test", "category": "torace", "modality": "rx"}
    assert "protocol-gallery" not in render_rx_document(rx_fm)
    rx_fm["images"] = img_data
    assert "protocol-gallery" in render_rx_document(rx_fm)
    assert "![Imagine Mostră](../../assets/images/protocols/sample.png)" in render_rx_document(rx_fm)

    fl_fm = {"title": "Fluoro Test", "slug": "fl-test", "category": "digestiv", "modality": "fluoro"}
    assert "protocol-gallery" not in render_fluoro_document(fl_fm)
    fl_fm["images"] = img_data
    assert "protocol-gallery" in render_fluoro_document(fl_fm)

    irm_fm = {"title": "IRM Test", "slug": "irm-test", "category": "neuro", "modality": "irm"}
    assert "protocol-gallery" not in render_irm_document(irm_fm)
    irm_fm["images"] = img_data
    assert "protocol-gallery" in render_irm_document(irm_fm)

    eco_fm = {"title": "Eco Test", "slug": "eco-test", "category": "abdomen-pelvis", "modality": "eco"}
    assert "protocol-gallery" not in render_eco_document(eco_fm)
    eco_fm["images"] = img_data
    assert "protocol-gallery" in render_eco_document(eco_fm)


