"""test_admin.py — Teste automate pentru interfața backend Flask de administrare protocoale."""

import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from admin import (
    CT_CATEGORIES,
    ECO_CATEGORIES,
    FLUORO_CATEGORIES,
    IRM_CATEGORIES,
    RX_CATEGORIES,
    app,
    form_to_eco_frontmatter,
    form_to_fluoro_frontmatter,
    form_to_frontmatter,
    form_to_irm_frontmatter,
    form_to_rx_frontmatter,
    _parse_form_images,
    load_all_protocols,
)


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_admin_index(client):
    """Pagina principală a admin-ului listează protocoalele cu badge-uri de modalitate."""
    res = client.get("/")
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert "Administrare Protocoale Radiologie" in html
    assert "📷 Rx" in html
    assert "⚡ CT" in html
    assert "rx-torace-pa" in html
    assert "ct-abdomen-pelvis-with-contrast" in html


def test_admin_edit_rx_displays_rx_categories(client):
    """La editarea unui protocol Rx, trebuie să apară categoriile Rx, NU cele de la CT."""
    res = client.get("/edit/rx-torace-pa")
    assert res.status_code == 200
    html = res.get_data(as_text=True)

    # Verifică badge-ul de modalitate
    assert "Radiografie Convențională (Rx)" in html

    # Verifică prezența categoriilor Rx în opțiuni
    for cat in RX_CATEGORIES:
        assert f'value="{cat}"' in html, f"Categoria Rx '{cat}' lipsește din select-ul de editare Rx!"

    # Categoriile exclusive de CT NU trebuie să apară ca opțiuni disponibile pentru Rx
    ct_exclusive = ["cardiac", "neuro", "trauma", "vascular"]
    for ct_cat in ct_exclusive:
        assert f'value="{ct_cat}"' not in html, (
            f"Categoria CT '{ct_cat}' a apărut eronat în select-ul pentru un protocol Rx!"
        )

    # Verifică prezența câmpurilor specifice Rx
    assert 'name="centering"' in html
    assert 'name="breathing"' in html
    assert 'name="sid_dff"' in html
    assert 'name="quality_criteria"' in html
    assert 'name="protection"' in html
    assert 'name="iris_chapter"' in html
    assert 'name="iris_grade"' in html
    assert 'name="iris_dose"' in html


def test_admin_edit_ct_displays_ct_categories(client):
    """La editarea unui protocol CT, trebuie să apară categoriile CT și secțiunile CT."""
    res = client.get("/edit/ct-abdomen-pelvis-with-contrast")
    assert res.status_code == 200
    html = res.get_data(as_text=True)

    # Verifică badge-ul de modalitate
    assert "Tomografie Computerizată (CT)" in html

    # Verifică prezența categoriilor CT
    for cat in CT_CATEGORIES:
        assert f'value="{cat}"' in html, f"Categoria CT '{cat}' lipsește din select-ul de editare CT!"

    # Verifică prezența câmpurilor specifice CT
    assert 'name="contrast_agent"' in html
    assert 'name="contrast_volume"' in html
    assert 'name="series_json"' in html
    assert 'name="recons_json"' in html


def test_form_to_rx_frontmatter():
    """Funcția de parsare a formularului Rx produce dicționarul frontmatter corect."""
    dummy_form = {
        "title": "Rx Test Titlu",
        "slug": "rx-test-titlu",
        "category": "coloana",
        "author": "Dr. Test",
        "position": "Decubit dorsal",
        "centering": "Nivel L3",
        "breathing": "Apnee",
        "sid_dff": "115 cm",
        "tech_kv": "80",
        "tech_mas": "20",
        "tech_grid": "Da",
        "tech_focal_spot": "Focar Mic",
        "tech_aec_chambers": "Camera centrală",
        "tech_collimation": "Colimare strânsă",
        "tech_filtration": "Standard",
        "indications_json_rx": "Durere lombară\nTraumatism",
        "quality_criteria": "Criteriu 1\nCriteriu 2",
        "protection": "Protecție gonade",
        "iris_chapter": "Coloană vertebrală",
        "iris_grade": "Grad B",
        "iris_dose": "Clasa 2",
        "notes_rx": "Notă tehnică importantă",
    }
    fm = form_to_rx_frontmatter(dummy_form)
    assert fm["title"] == "Rx Test Titlu"
    assert fm["category"] == "coloana"
    assert fm["modality"] == "rx"
    assert fm["sid_dff"] == "115 cm"
    assert fm["centering"] == "Nivel L3"
    assert fm["clinical_indications"] == ["Durere lombară", "Traumatism"]
    assert fm["quality_criteria"] == ["Criteriu 1", "Criteriu 2"]
    assert fm["protection"] == ["Protecție gonade"]
    assert fm["tech_params"]["kv"] == "80"
    assert fm["tech_params"]["aec_chambers"] == "Camera centrală"
    assert fm["iris_reference"]["chapter"] == "Coloană vertebrală"
    assert fm["notes"] == "Notă tehnică importantă"


def test_admin_new_get_modalities(client):
    """Ruta /new afișează corect categoriile în funcție de parametrul modality."""
    res_rx = client.get("/new?modality=rx")
    assert res_rx.status_code == 200
    html_rx = res_rx.get_data(as_text=True)
    assert 'value="torace"' in html_rx
    assert 'value="pediatrie"' in html_rx

    res_ct = client.get("/new?modality=ct")
    assert res_ct.status_code == 200
    html_ct = res_ct.get_data(as_text=True)
    assert 'value="cardiac"' in html_ct
    assert 'value="vascular"' in html_ct


def test_save_rx_protocol_via_post(client, tmp_path, monkeypatch):
    """Salvarea unui protocol Rx prin POST utilizează render_rx_document și păstrează structura Rx."""
    import admin

    # Facem o copie temporară a fișierului rx-torace-pa pentru a nu modifica fișierul de producție în test
    repo_root = Path(__file__).parent.parent
    orig_file = repo_root / "docs" / "rx" / "torace" / "rx-torace-pa.md"
    orig_content = orig_file.read_text(encoding="utf-8")

    temp_file = tmp_path / "rx-torace-pa.md"
    temp_file.write_text(orig_content, encoding="utf-8")

    # Mock la find_protocol pentru a returna fișierul temporar
    original_find = admin.find_protocol
    def mock_find(slug):
        item = original_find(slug)
        if item and slug == "rx-torace-pa":
            return {"filepath": temp_file, "fm": item["fm"]}
        return item

    monkeypatch.setattr(admin, "find_protocol", mock_find)
    monkeypatch.setattr(admin, "rebuild_indexes", lambda: [])

    post_data = {
        "title": "Rx Torace PA Modificat",
        "slug": "rx-torace-pa",
        "category": "torace",
        "modality": "rx",
        "author": "Dr. Radiolog Test",
        "position": "Ortostatism PA modificat",
        "centering": "Nivel T7 modificat",
        "breathing": "Apnee în inspir",
        "sid_dff": "180 cm",
        "tech_kv": "125",
        "tech_mas": "2.5",
        "tech_grid": "Cu grilă Bucky",
        "tech_focal_spot": "Focar Mare",
        "tech_aec_chambers": "Camere laterale",
        "tech_collimation": "Colimare strictă",
        "tech_filtration": "Standard",
        "indications_json_rx": "Indicație nouă de test",
        "quality_criteria": "Criteriu calitativ nou",
        "protection": "Șorț plumb nou",
        "iris_chapter": "Torace & Pulmon",
        "iris_grade": "Grad A",
        "iris_dose": "Clasa 1",
        "notes_rx": "Notă suplimentară test",
    }

    res = client.post("/edit/rx-torace-pa", data=post_data)
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert data.get("success") is True

    # Verificăm conținutul fișierului salvat
    saved_text = temp_file.read_text(encoding="utf-8")
    assert "# Rx Torace PA Modificat" in saved_text
    assert "Nivel T7 modificat" in saved_text
    assert "Indicație nouă de test" in saved_text
    assert "Criteriu calitativ nou" in saved_text
    assert "Ghid Național IRIS" in saved_text


def test_admin_index_shows_fluoro(client):
    """Pagina de start admin include badge-ul Fluoro și protocoalele de fluoroscopie."""
    res = client.get("/")
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert "✨ Fluoro" in html
    assert "tranzit-esofago-gastro-duodenal-tegd" in html
    assert "c-arm-osteosinteza-trauma-ortopedie" in html


def test_admin_edit_fluoro_displays_fluoro_categories(client):
    """La editarea unui protocol Fluoro, trebuie să apară categoriile Fluoro și câmpurile specifice."""
    res = client.get("/edit/tranzit-esofago-gastro-duodenal-tegd")
    assert res.status_code == 200
    html = res.get_data(as_text=True)

    # Verifică badge-ul de modalitate
    assert "Fluoroscopie &amp; C-Arm" in html or "Fluoroscopie & C-Arm" in html

    # Verifică categoriile de fluoroscopie
    for cat in FLUORO_CATEGORIES:
        assert f'value="{cat}"' in html, f"Categoria Fluoro '{cat}' lipsește din select!"

    # Categoriile exclusive de CT nu trebuie să apară
    for ct_cat in ["cardiac", "neuro", "trauma", "vascular"]:
        assert f'value="{ct_cat}"' not in html

    # Câmpuri specifice fluoroscopiei
    assert 'name="indications_json_fluoro"' in html
    assert 'name="contraindications"' in html
    assert 'name="patient_prep"' in html
    assert 'name="contrast_agent_fluoro"' in html
    assert 'name="fluoro_mode"' in html
    assert 'name="equipment_setup_fluoro"' in html
    assert 'name="quality_criteria_fluoro"' in html
    assert 'name="radiation_safety_fluoro"' in html


def test_admin_new_get_modality_fluoro(client):
    """Ruta /new?modality=fluoro încarcă categoriile și secțiunile de fluoroscopie."""
    res = client.get("/new?modality=fluoro")
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert 'value="digestiv"' in html
    assert 'value="c-arm"' in html
    assert 'name="indications_json_fluoro"' in html


def test_save_fluoro_protocol_via_post(client, tmp_path, monkeypatch):
    """Salvarea unui protocol de fluoroscopie utilizează render_fluoro_document."""
    import admin

    repo_root = Path(__file__).parent.parent
    orig_file = repo_root / "docs" / "fluoro" / "digestiv" / "tranzit-esofagian.md"
    orig_content = orig_file.read_text(encoding="utf-8")

    temp_file = tmp_path / "tranzit-esofagian.md"
    temp_file.write_text(orig_content, encoding="utf-8")

    original_find = admin.find_protocol
    def mock_find(slug):
        item = original_find(slug)
        if item and slug == "tranzit-esofagian":
            return {"filepath": temp_file, "fm": item["fm"]}
        return item

    monkeypatch.setattr(admin, "find_protocol", mock_find)
    monkeypatch.setattr(admin, "rebuild_indexes", lambda: [])

    post_data = {
        "title": "Tranzit Baritat Esofagian Modificat",
        "slug": "tranzit-esofagian",
        "category": "digestiv",
        "modality": "fluoro",
        "author": "Dr. Fluoro Test",
        "last_updated": "2026-09-13",
        "indications_json_fluoro": "Disfagie severă de test",
        "contraindications": "Suspiciune perforație - interzis bariu",
        "patient_prep": "À jeun 6 ore",
        "contrast_agent_fluoro": "Sulfat de Bariu 200%",
        "contrast_route_fluoro": "Orală",
        "contrast_volume_fluoro": "150 ml",
        "contrast_instructions_fluoro": "Înghițire la comandă",
        "patient_position_fluoro": "Ortostatism OAD 35°",
        "equipment_setup_fluoro": "Masă basculantă 90°",
        "sid_fluoro": "100 cm",
        "fluoro_mode": "Pulsat 7.5 fps",
        "fluoro_kv": "95",
        "fluoro_ma": "2.0 mA",
        "fluoro_grid": "Cu grilă",
        "fluoro_filtration": "Standard Al+Cu",
        "fluoro_target_time": "< 2 min",
        "fluoro_lih": "Activ",
        "quality_criteria_fluoro": "Tapetare uniformă",
        "radiation_safety_fluoro": "Colimare strictă",
        "iris_chapter": "Tub Digestiv & Esofag",
        "iris_grade": "Grad A",
        "iris_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        "notes_fluoro": "Notă fluoroscopie test",
    }

    res = client.post("/edit/tranzit-esofagian", data=post_data)
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert data.get("success") is True

    saved_text = temp_file.read_text(encoding="utf-8")
    assert "# Tranzit Baritat Esofagian Modificat" in saved_text
    assert "✨ Fluoroscopie & C-Arm" in saved_text
    assert "Disfagie severă de test" in saved_text
    assert "Ortostatism OAD 35°" in saved_text
    assert "Tub Digestiv & Esofag" in saved_text


def test_admin_index_shows_irm(client):
    """Pagina de start admin include badge-ul IRM și protocoalele IRM."""
    res = client.get("/")
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert "🧲 IRM" in html
    assert "irm-cerebral-nativ-si-cu-contrast" in html
    assert "irm-genunchi" in html


def test_admin_edit_irm_displays_irm_categories_and_sequences(client):
    """La editarea unui protocol IRM, trebuie să apară categoriile IRM și secțiunile RM."""
    res = client.get("/edit/irm-cerebral-nativ-si-cu-contrast")
    assert res.status_code == 200
    html = res.get_data(as_text=True)

    # Verifică badge-ul de modalitate
    assert "Rezonanță Magnetică (IRM)" in html

    # Verifică prezența categoriilor IRM
    for cat in IRM_CATEGORIES:
        assert f'value="{cat}"' in html, f"Categoria IRM '{cat}' lipsește din select!"

    # Categoriile exclusive de Rx sau Fluoro nu trebuie să apară în select
    for other_cat in ["digestiv", "pediatrie", "torace", "c-arm"]:
        assert f'value="{other_cat}"' not in html

    # Câmpuri specifice IRM
    assert 'name="coil_irm"' in html
    assert 'name="field_strength_irm"' in html
    assert 'name="positioning_irm"' in html
    assert 'name="contrast_agent_irm"' in html
    assert 'name="contrast_dose_irm"' in html
    assert 'name="sequences_json"' in html
    assert 'name="safety_considerations_irm"' in html


def test_admin_new_get_modality_irm(client):
    """Ruta /new?modality=irm încarcă categoriile și secțiunile de IRM."""
    res = client.get("/new?modality=irm")
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert 'value="neuro"' in html
    assert 'value="msk"' in html
    assert 'value="abdomen-pelvis"' in html
    assert 'value="cardiac"' in html
    assert 'value="san"' in html
    assert 'name="coil_irm"' in html


def test_form_to_irm_frontmatter():
    """Funcția de parsare a formularului IRM produce dicționarul frontmatter corect."""
    dummy_form = {
        "title": "IRM Cerebral Test",
        "slug": "irm-cerebral-test",
        "category": "neuro",
        "author": "Dr. RM Test",
        "patient_prep_irm": "Screening metalic riguros",
        "coil_irm": "Head 32ch",
        "field_strength_irm": "3.0 Tesla",
        "positioning_irm": "Decubit dorsal",
        "contrast_agent_irm": "Gadovist",
        "contrast_dose_irm": "0.1 mmol/kg",
        "contrast_flow_rate_irm": "2 ml/s",
        "contrast_timing_irm": "Post-contrast imediat",
        "contrast_notes_irm": "Verificare eGFR",
        "indications_json_irm": "Cefalee cronică\nDeficit neurologic",
        "contraindications_irm": "Stimulator cardiac incompatibil",
        "quality_criteria_irm": "Fără artefacte de mișcare",
        "safety_considerations_irm": "Zonă de siguranță 4",
        "sequences_json": json.dumps([
            {"name": "T2 TSE", "plane": "Axial", "tr_te": "4000/100", "slice_gap": "4mm", "fov_matrix": "230/320", "fat_sat": "Nu", "notes": "Standard"}
        ]),
        "iris_chapter": "SNC și Neuro-IRM",
        "iris_grade": "Grad A",
        "iris_dose": "Clasa 0",
        "notes_irm": "Notă IRM clinică",
    }
    fm = form_to_irm_frontmatter(dummy_form)
    assert fm["title"] == "IRM Cerebral Test"
    assert fm["category"] == "neuro"
    assert fm["modality"] == "irm"
    assert fm["coils_hardware"]["coil"] == "Head 32ch"
    assert fm["coils_hardware"]["field_strength"] == "3.0 Tesla"
    assert fm["contrast"]["agent"] == "Gadovist"
    assert len(fm["sequences"]) == 1
    assert fm["sequences"][0]["name"] == "T2 TSE"
    assert fm["clinical_indications"] == ["Cefalee cronică", "Deficit neurologic"]
    assert fm["safety_considerations"] == ["Zonă de siguranță 4"]


def test_save_irm_protocol_via_post(client, tmp_path, monkeypatch):
    """Salvarea unui protocol IRM utilizează render_irm_document."""
    import admin

    repo_root = Path(__file__).parent.parent
    orig_file = repo_root / "docs" / "irm" / "neuro" / "irm-cerebral-nativ-si-cu-contrast.md"
    orig_content = orig_file.read_text(encoding="utf-8")

    temp_file = tmp_path / "irm-cerebral-nativ-si-cu-contrast.md"
    temp_file.write_text(orig_content, encoding="utf-8")

    original_find = admin.find_protocol
    def mock_find(slug):
        item = original_find(slug)
        if item and slug == "irm-cerebral-nativ-si-cu-contrast":
            return {"filepath": temp_file, "fm": item["fm"]}
        return item

    monkeypatch.setattr(admin, "find_protocol", mock_find)
    monkeypatch.setattr(admin, "rebuild_indexes", lambda: [])

    post_data = {
        "title": "IRM Cerebral Nativ și cu Contrast Modificat",
        "slug": "irm-cerebral-nativ-si-cu-contrast",
        "category": "neuro",
        "modality": "irm",
        "author": "Dr. RM Senior",
        "last_updated": "2026-09-13",
        "patient_prep_irm": "Pregătire specifică test",
        "coil_irm": "Antenă Head/Neck 64 canale",
        "field_strength_irm": "3.0 Tesla",
        "positioning_irm": "Decubit dorsal cu suport cap",
        "contrast_agent_irm": "Acid gadoteric (Dotarem)",
        "contrast_dose_irm": "0.1 mmol/kg",
        "contrast_flow_rate_irm": "2 ml/s",
        "contrast_timing_irm": "T1 post-contrast",
        "contrast_notes_irm": "eGFR > 30 ml/min",
        "indications_json_irm": "Leziune demielinizantă de test",
        "contraindications_irm": "Implant feromagnetic neomologat",
        "quality_criteria_irm": "Rezoluție înaltă",
        "safety_considerations_irm": "Protecție fonică cu căști",
        "sequences_json": json.dumps([
            {"name": "3D T1 MPRAGE", "plane": "Sagital", "tr_te": "2000/2.5", "slice_gap": "1mm izotrop", "fov_matrix": "256/256", "fat_sat": "Nu", "notes": "Volum 3D"},
            {"name": "Axial FLAIR", "plane": "Axial", "tr_te": "9000/120", "slice_gap": "4mm", "fov_matrix": "220/320", "fat_sat": "Nu", "notes": "TI 2500ms"}
        ]),
        "iris_chapter": "Neuroradiologie IRM",
        "iris_grade": "Grad A",
        "iris_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        "notes_irm": "Notă salvare IRM test",
    }

    res = client.post("/edit/irm-cerebral-nativ-si-cu-contrast", data=post_data)
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert data.get("success") is True

    saved_text = temp_file.read_text(encoding="utf-8")
    assert "# IRM Cerebral Nativ și cu Contrast Modificat" in saved_text
    assert "🧲 Imagistică prin Rezonanță Magnetică (IRM)" in saved_text
    assert "3D T1 MPRAGE" in saved_text
    assert "Antenă Head/Neck 64 canale" in saved_text
    assert "Leziune demielinizantă de test" in saved_text
    assert "Neuroradiologie IRM" in saved_text


def test_admin_edit_eco_displays_eco_categories(client):
    """La editarea unui protocol Ecografie, trebuie să apară categoriile Eco și secțiunile specifice US."""
    res = client.get("/edit/eco-abdomen-total")
    assert res.status_code == 200
    html = res.get_data(as_text=True)

    # Verifică badge-ul de modalitate
    assert "Ecografie &amp; Ultrasonografie (US)" in html

    # Verifică prezența categoriilor Eco
    for cat in ECO_CATEGORIES:
        assert f'value="{cat}"' in html, f"Categoria Eco '{cat}' lipsește din select-ul de editare Eco!"

    # Categoriile exclusive CT nu trebuie să apară
    for ct_exclusive in ["cardiac", "chest", "trauma"]:
        assert f'value="{ct_exclusive}"' not in html

    # Verifică prezența câmpurilor specifice Eco
    assert 'name="transducers_types_eco"' in html
    assert 'name="patient_position_eco"' in html
    assert 'name="gel_acoustic_window_eco"' in html
    assert 'name="preset_eco"' in html
    assert 'name="modes_eco"' in html
    assert 'name="focus_depth_eco"' in html
    assert 'name="gain_thi_eco"' in html
    assert 'name="measurements_criteria_eco"' in html
    assert 'name="views_json"' in html
    assert 'name="quality_criteria_eco"' in html
    assert 'name="safety_and_limitations_eco"' in html
    assert 'name="iris_chapter_eco"' in html
    assert 'name="notes_eco"' in html


def test_form_to_eco_frontmatter():
    """Funcția de parsare a formularului Eco produce dicționarul frontmatter corect."""
    dummy_form = {
        "title": "Ecografie Test Abdomen",
        "slug": "eco-test-abdomen",
        "category": "abdomen-pelvis",
        "modality": "eco",
        "author": "Dr. Eco Specialist",
        "last_updated": "2026-09-13",
        "indications_json_eco": "Hepatomegalie\nDurere hipocondru drept",
        "contraindications_eco": "Obezitate extremă\nInterpoziție masivă de gaze",
        "patient_prep_eco": "Repaus alimentar 6 ore",
        "transducers_types_eco": "Sondă Convexă 3.5 MHz",
        "patient_position_eco": "Decubit dorsal",
        "gel_acoustic_window_eco": "Gel standard",
        "preset_eco": "Abdomen General",
        "modes_eco": "Mod B + Doppler Color",
        "focus_depth_eco": "Focalizare 8-12 cm",
        "gain_thi_eco": "THI activ",
        "measurements_criteria_eco": "Diametru craniocaudal hepatic",
        "views_json": json.dumps([
            {"view": "Sagital Ficat", "anatomical_target": "Lob drept", "landmarks": "Vena cavă inferioară", "normal_aspect": "Omogen"}
        ]),
        "quality_criteria_eco": "Penetrare acustică bună",
        "safety_and_limitations_eco": "Respectare indice termic TI < 1.0",
        "iris_chapter_eco": "Ecografie Abdominală",
        "iris_grade_eco": "Grad A",
        "iris_dose_eco": "Clasa 0",
        "notes_eco": "Notă Eco clinică",
    }
    fm = form_to_eco_frontmatter(dummy_form)
    assert fm["title"] == "Ecografie Test Abdomen"
    assert fm["category"] == "abdomen-pelvis"
    assert fm["modality"] == "eco"
    assert fm["transducers_equipment"]["transducer_types"] == "Sondă Convexă 3.5 MHz"
    assert fm["technical_settings"]["preset"] == "Abdomen General"
    assert len(fm["standard_views"]) == 1
    assert fm["standard_views"][0]["view"] == "Sagital Ficat"
    assert fm["clinical_indications"] == ["Hepatomegalie", "Durere hipocondru drept"]
    assert fm["safety_and_limitations"] == ["Respectare indice termic TI < 1.0"]


def test_save_eco_protocol_via_post(client, tmp_path, monkeypatch):
    """Salvarea unui protocol Eco utilizează render_eco_document."""
    import admin

    repo_root = Path(__file__).parent.parent
    orig_file = repo_root / "docs" / "eco" / "abdomen-pelvis" / "eco-abdomen-total.md"
    orig_content = orig_file.read_text(encoding="utf-8")

    temp_file = tmp_path / "eco-abdomen-total.md"
    temp_file.write_text(orig_content, encoding="utf-8")

    original_find = admin.find_protocol
    def mock_find(slug):
        item = original_find(slug)
        if item and slug == "eco-abdomen-total":
            return {"filepath": temp_file, "fm": item["fm"]}
        return item

    monkeypatch.setattr(admin, "find_protocol", mock_find)
    monkeypatch.setattr(admin, "rebuild_indexes", lambda: [])

    post_data = {
        "title": "Ecografie Abdomen Total Modificat Test",
        "slug": "eco-abdomen-total",
        "category": "abdomen-pelvis",
        "modality": "eco",
        "author": "Dr. US Senior",
        "last_updated": "2026-09-13",
        "patient_prep_eco": "Repaus alimentar strict 6-8 ore",
        "transducers_types_eco": "Sondă convexă multifrecvență 3.5-5.0 MHz",
        "patient_position_eco": "Decubit dorsal și decubite laterale",
        "gel_acoustic_window_eco": "Gel ecografic abundent",
        "preset_eco": "Abdomen Total Rutină",
        "modes_eco": "Mod B (2D) + CFM + PW Doppler",
        "focus_depth_eco": "Focalizare dinamică",
        "gain_thi_eco": "THI activat",
        "measurements_criteria_eco": "Măsurători biometrice complete",
        "indications_json_eco": "Hepatopatie cronică test",
        "contraindications_eco": "Interpoziție aerică severă",
        "quality_criteria_eco": "Diferențiere cortico-medulară renală netă",
        "safety_and_limitations_eco": "Index mecanic MI < 0.7",
        "views_json": json.dumps([
            {"view": "Secțiune Subcostală Transversală", "anatomical_target": "Lob hepatic stâng", "landmarks": "Aorta", "normal_aspect": "Ecostructură fină"}
        ]),
        "iris_chapter_eco": "Ecografie Abdomen",
        "iris_grade_eco": "Grad A",
        "iris_dose_eco": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        "notes_eco": "Notă salvare Eco test",
    }

    res = client.post("/edit/eco-abdomen-total", data=post_data)
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert data.get("success") is True

    saved_text = temp_file.read_text(encoding="utf-8")
    assert "# Ecografie Abdomen Total Modificat Test" in saved_text
    assert "📡 Ecografie &amp; Ultrasonografie (US)" in saved_text
    assert "Secțiune Subcostală Transversală" in saved_text
    assert "Hepatopatie cronică test" in saved_text
    assert "Sondă convexă multifrecvență" in saved_text


def test_admin_new_renders_base_protocols(client):
    """Pagina /new conține selectorul de protocoale de bază cu optgroups și maparea ALL_PROTOCOLS fără erori de sintaxă."""
    res = client.get("/new")
    assert res.status_code == 200
    html = res.get_data(as_text=True)

    # Verifică prezența selectorului de bază și a butonului Încarcă
    assert 'id="base-select"' in html
    assert 'onclick="loadBase()"' in html
    assert 'id="base-load-status"' in html

    # Verifică gruparea pe modalități
    assert 'optgroup label="⚡ CT' in html
    assert 'optgroup label="🧲 IRM' in html
    assert 'optgroup label="📷 RX' in html
    assert 'optgroup label="📡 US' in html
    assert 'optgroup label="✨ FLOURO' in html

    # Verifică prezența dicționarului ALL_PROTOCOLS și validitatea JSON-ului injectat
    assert "const ALL_PROTOCOLS = {" in html
    assert "toLines" in html
    # Asigură-te că nu există erori de sintaxă cu newline în string literal
    assert ".join('" not in html


def test_parse_form_images():
    """_parse_form_images parses json list and strips empty items."""
    # Empty cases
    assert _parse_form_images({}) == []
    assert _parse_form_images({"images_json": ""}) == []
    assert _parse_form_images({"images_json": "[]"}) == []
    assert _parse_form_images({"images_json": "invalid-json"}) == []

    # Valid dict cases
    raw = json.dumps([
        {"url": "assets/images/protocols/scan1.png", "caption": "Scan 1", "description": "Desc 1"},
        {"url": "", "caption": "Empty URL", "description": "Should be ignored"},
        {"url": "https://external.org/scan2.jpg", "caption": "Scan 2", "description": ""},
    ])
    res = _parse_form_images({"images_json": raw})
    assert len(res) == 2
    assert res[0]["url"] == "assets/images/protocols/scan1.png"
    assert res[0]["caption"] == "Scan 1"
    assert res[0]["description"] == "Desc 1"
    assert res[1]["url"] == "https://external.org/scan2.jpg"
    assert res[1]["caption"] == "Scan 2"
    assert res[1]["description"] == ""

    # String items case
    raw_strings = json.dumps(["assets/images/protocols/direct.jpg"])
    res_str = _parse_form_images({"images_json": raw_strings})
    assert len(res_str) == 1
    assert res_str[0]["url"] == "assets/images/protocols/direct.jpg"


def test_admin_includes_images_section(client):
    """Admin edit and new templates include the images section and controls."""
    res_edit = client.get("/edit/ct-abdomen-pelvis-with-contrast")
    assert res_edit.status_code == 200
    html_edit = res_edit.get_data(as_text=True)
    assert 'id="images-section"' in html_edit
    assert 'id="images-container"' in html_edit
    assert 'name="images_json"' in html_edit
    assert 'addImageRow(' in html_edit
    assert 'uploadImageFile(' in html_edit

    res_new = client.get("/new?modality=rx")
    assert res_new.status_code == 200
    html_new = res_new.get_data(as_text=True)
    assert 'id="images-section"' in html_new
    assert 'id="images-container"' in html_new


def test_api_upload_image(client):
    """POST /api/upload_image saves uploaded image and returns proper relative url."""
    import io

    # Missing file
    res_err = client.post("/api/upload_image")
    assert res_err.status_code == 200
    assert res_err.get_json()["success"] is False

    # Disallowed extension
    data_bad = {"file": (io.BytesIO(b"fake executable"), "malicious.exe")}
    res_bad = client.post("/api/upload_image", data=data_bad, content_type="multipart/form-data")
    assert res_bad.status_code == 200
    assert res_bad.get_json()["success"] is False

    # Valid image upload
    data_ok = {"file": (io.BytesIO(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"), "test_image.png")}
    res_ok = client.post("/api/upload_image", data=data_ok, content_type="multipart/form-data")
    assert res_ok.status_code == 200
    res_data = res_ok.get_json()
    assert res_data["success"] is True
    assert "assets/images/protocols/" in res_data["url"]
    assert res_data["filename"].endswith(".png")

    saved_path = Path(__file__).parent.parent / "docs" / "assets" / "images" / "protocols" / res_data["filename"]
    try:
        # Serving the asset
        res_serve = client.get(f"/{res_data['url']}")
        assert res_serve.status_code == 200
        res_serve.close()
    finally:
        try:
            saved_path.unlink(missing_ok=True)
        except Exception:
            pass


def test_form_to_frontmatter_includes_images():
    """All 5 modality form parsers include the parsed images key."""
    img_json = json.dumps([{"url": "assets/images/protocols/sample.png", "caption": "Cap", "description": "Desc"}])
    dummy_form = {
        "title": "Test Title",
        "slug": "test-slug",
        "category": "chest",
        "images_json": img_json,
    }

    fm_ct = form_to_frontmatter(dummy_form)
    assert len(fm_ct["images"]) == 1
    assert fm_ct["images"][0]["url"] == "assets/images/protocols/sample.png"

    fm_rx = form_to_rx_frontmatter(dummy_form)
    assert len(fm_rx["images"]) == 1

    fm_fluoro = form_to_fluoro_frontmatter(dummy_form)
    assert len(fm_fluoro["images"]) == 1

    fm_irm = form_to_irm_frontmatter(dummy_form)
    assert len(fm_irm["images"]) == 1

    fm_eco = form_to_eco_frontmatter(dummy_form)
    assert len(fm_eco["images"]) == 1





