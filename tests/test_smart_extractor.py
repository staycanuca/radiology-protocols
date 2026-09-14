import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from protocol_workbench.smart_extractor import (
    extract_parameters_by_modality,
    diff_parameters,
    smart_extract_and_apply,
    sync_body_parameters,
)


def test_extract_rx_parameters():
    source = """
    Norme tehnice radiologie:
    Examinare Rx Coloană Toracală / Dorsală:
    Tensiune generator: Față 75 - 80 kV, Profil 80 - 95 kV.
    Sarcină expunere: 30 - 50 mAs cu camera centrală AEC activată.
    Distanță focar-film: 115 cm.
    Dimensiune focar: Focar mare.
    Grilă antidifuzoare: Bucky prezentă.
    Punct de centrare: Nivel T7 la 8 cm sub manubriul sternal.
    Poziție pacient: Decubit dorsal pe față și decubit lateral pe profil.
    Comandă respiratorie: Apnee în expir.
    """
    params = extract_parameters_by_modality(source, 'rx', 'Rx Coloană Toracală (Față & Profil)')
    assert 'tech_params' in params
    tech = params['tech_params']
    assert 'Față' in tech['kv'] and 'Profil' in tech['kv']
    assert '75 - 80' in tech['kv']
    assert '80 - 95' in tech['kv']
    assert '30 - 50' in tech['mas']
    assert '115 cm' in params['sid_dff']
    assert tech['focal_spot'] == 'Focar Mare'
    assert 'Bucky' in tech['grid']
    assert 'T7' in params['centering']
    assert 'Decubit' in params['position']
    assert 'expir' in params['breathing'].lower()


def test_extract_ct_parameters():
    source = """
    CT Torace Nativ protocol:
    Parametri achiziție: 120 kV, 180 mAs (AEC CareDose activat).
    Pitch: 0.984, colimare 128 x 0.6 mm. Timp rotație 0.5 s.
    Substanță de contrast: Iohexol 350 mg I/ml, volum 90 ml, debit 4 ml/s, delay arterial 25s.
    """
    params = extract_parameters_by_modality(source, 'ct', 'CT Torace Nativ')
    assert 'tech_params' in params
    assert '120' in params['tech_params']['kv']
    assert '180' in params['tech_params']['mas']
    assert '0.984' in params['tech_params']['pitch']
    assert '0.5' in params['tech_params']['rotation_time']
    assert 'contrast' in params
    assert '90 ml' in params['contrast']['volume']
    assert '4 ml/s' in params['contrast']['flow_rate']


def test_smart_extract_and_apply_detects_and_updates_diffs():
    doc = """---
title: Rx Coloană Toracală (Față & Profil)
modality: rx
tech_params:
  kv: 75 - 85 (Față); 80 - 90 (Profil)
  mas: 25 - 50 (AEC)
sid_dff: 100 - 115 cm
---

# Rx Coloană Toracală

| Parametru Tehnic | Valoare Configurare Generator / Tub |
|:-----------------|:-------------------------------------|
| **Tensiune Tub (kV)** | 75 - 85 (Față); 80 - 90 (Profil) kV |
| **Sarcină / Produs Curent-Timp (mAs)** | 25 - 50 (AEC) |
| **Distanță Focar-Film (DFF / SID)** | 100 - 115 cm |
"""

    source = """
    Pentru coloana toracala:
    Tensiune tub: Față 75 - 80 kV; Profil 80 - 95 kV.
    mAs: 35 - 60 mAs.
    DFF: 120 cm.
    Focar mare.
    """

    updated_doc, diffs = smart_extract_and_apply(doc, source, 'Rx Coloană Toracală')
    assert len(diffs) >= 3
    fields = [d['field'] for d in diffs]
    assert 'tech_params.kv' in fields
    assert 'tech_params.mas' in fields
    assert 'sid_dff' in fields

    # Check updated YAML frontmatter
    assert '75 - 80 (Față); 80 - 95 (Profil)' in updated_doc
    assert '35 - 60' in updated_doc
    assert '120 cm' in updated_doc

    # Check that body table was also synchronized
    assert '|  75 - 80 (Față); 80 - 95 (Profil) |' in updated_doc
    assert '|  35-60 mAs |' in updated_doc or '|  35 - 60' in updated_doc
    assert '|  120 cm |' in updated_doc


def test_no_diffs_when_source_has_no_parameters():
    doc = """---
title: Protocol General
modality: rx
tech_params:
  kv: 75 kV
---

# Titlu
"""
    source = "Un text descriptiv fără valori numerice sau parametri tehnici expliciti."
    updated_doc, diffs = smart_extract_and_apply(doc, source, 'Protocol General')
    assert len(diffs) == 0
    assert updated_doc == doc
