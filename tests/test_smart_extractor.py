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
    Indicații clinice:
    - Dorsalgii cronice și cifoză accentuată
    - Suspiciune tasare vertebrală osteoporotică
    - Traumatism toracic dorsal
    Tensiune generator: Față 75 - 80 kV, Profil 80 - 95 kV.
    Sarcină expunere: 30 - 50 mAs cu camera centrală AEC activată.
    Distanță focar-film: 115 cm.
    Dimensiune focar: Focar mare.
    Grilă antidifuzoare: Bucky prezentă.
    Punct de centrare: Nivel T7 la 8 cm sub manubriul sternal.
    Poziție pacient: Decubit dorsal pe față și decubit lateral pe profil.
    Comandă respiratorie: Apnee în expir.
    Criterii de calitate:
    - Includerea completă a tuturor celor 12 vertebre toracale
    - Spații discale deschise fără rotație
    Protecție radiologică:
    - Șorț de plumb pelvin și guler tiroidian
    - Colimare laterală strânsă
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
    
    # Verifică aspectele clinice, de calitate și radioprotecție
    assert 'clinical_indications' in params
    assert len(params['clinical_indications']) >= 2
    assert any('Dorsalgii' in ind or 'tasare' in ind for ind in params['clinical_indications'])

    assert 'quality_criteria' in params
    assert len(params['quality_criteria']) >= 2

    assert 'protection' in params
    assert any('plumb' in p.lower() for p in params['protection'])


def test_extract_ct_parameters():
    source = """
    CT Abdomen și Pelvis cu contrast:
    Indicații:
    - Dureri abdominale acute de cauză neelucidată
    - Suspiciune abces sau colecție intraabdominală
    Pregătire pacient:
    Repaus alimentar: 4 - 6 ore înainte de examinare.
    Premedicație: Hidratare orală 1000 ml apă necarbogazoasă.
    Poziție: Decubit dorsal cu brațele ridicate deasupra capului.
    Parametri achiziție: 120 kV, 180 mAs (AEC CareDose activat). Mod elicoidal.
    Pitch: 0.984, colimare 128 x 0.6 mm. Timp rotație 0.5 s.
    Substanță de contrast: Iohexol 350 mg I/ml, volum 90 ml, debit 4 ml/s, delay venos 70s, declanșator 150 HU.
    Siguranță: Funcție renală: eGFR > 30 mL/min necesară.
    """
    params = extract_parameters_by_modality(source, 'ct', 'CT Abdomen și Pelvis')
    assert 'tech_params' in params
    assert '120' in params['tech_params']['kv']
    assert '180' in params['tech_params']['mas']
    assert '0.984' in params['tech_params']['pitch']
    assert '0.5' in params['tech_params']['rotation_time']
    assert 'Elicoidal' in params['tech_params']['scan_mode']

    # Aspecte clinice și pregătire
    assert 'clinical_indications' in params
    assert len(params['clinical_indications']) >= 2
    assert '4 - 6 ore' in params['npo']
    assert 'Hidratare' in params['premedication']
    assert 'Decubit dorsal' in params['position']

    # Contrast
    assert 'contrast' in params
    assert 'Iohexol' in params['contrast']['agent']
    assert '90 mL' in params['contrast']['volume']
    assert '4 mL/s' in params['contrast']['flow_rate']
    assert '70s' in params['contrast']['timing']
    assert '150 HU' in params['contrast']['trigger']

    # Siguranță renală
    assert 'safety' in params
    assert 'eGFR > 30' in params['safety']['renal']


def test_extract_irm_parameters():
    source = """
    Protocol IRM Genunchi:
    Indicații clinice:
    - Ruptură de ligament încrucișat anterior (LIA)
    - Leziuni de menisc intern și extern
    - Condropatie femuro-patelară
    Contraindicații RM:
    - Pacemaker cardiac non-RM condițional
    - Clipurile anevrismale feromagnetice
    Pregătire pacient: Îndepărtare bijuterii și machiaj, genunchi în extensie relaxată.
    Echipament: Câmp 3.0 Tesla, Antenă dedicată genunchi 16 canale.
    Poziționare: Decubit dorsal cu picioarele înainte în izocentru.
    Secvențe: T1 SE, T2 TSE, STIR, DWI.
    Substanță de contrast: Gadovist, doză 0.1 mmol/kg, debit 2 ml/s.
    Criterii de calitate:
    - Supresie de grăsime omogenă pe întregul FOV
    - Absența artefactelor de mișcare
    Securitate RM: Monitorizare limită SAR corp întreg < 2.0 W/kg.
    """
    params = extract_parameters_by_modality(source, 'irm', 'IRM Genunchi')
    assert 'clinical_indications' in params
    assert len(params['clinical_indications']) >= 2
    assert 'contraindications' in params
    assert len(params['contraindications']) >= 1

    assert 'patient_prep' in params
    assert 'bijuterii' in params['patient_prep']

    assert 'coils_hardware' in params
    assert '3.0 Tesla' in params['coils_hardware']['field_strength']
    assert 'genunchi' in params['coils_hardware']['coil'].lower()
    assert 'Decubit dorsal' in params['position']

    assert 'sequences' in params
    seq_names = [s['name'] for s in params['sequences']]
    assert any('T1' in n for n in seq_names)
    assert any('T2' in n for n in seq_names)
    assert any('STIR' in n for n in seq_names)

    assert 'contrast' in params
    assert 'Gadovist' in params['contrast']['agent']
    assert '0.1 mmol/kg' in params['contrast']['dose']

    assert 'quality_criteria' in params
    assert len(params['quality_criteria']) >= 1
    assert 'safety_considerations' in params
    assert any('SAR' in s for s in params['safety_considerations'])


def test_extract_eco_parameters():
    source = """
    Protocol Ecografie Abdomen Total:
    Indicații clinice:
    - Dureri în hipocondrul drept și colică biliară
    - Suspiciune de litiază biliară sau renală
    - Hepatomegalie și steatoză hepatică
    Contraindicații:
    - Interpoziție masivă de gaze intestinale (meteorism)
    Pregătire pacient: À jeun minim 6 ore înainte de examinare; vezică urinară în repleție.
    Transductori: Sondă convexă 3.5 - 5.0 MHz.
    Poziționare: Decubit dorsal completat cu decubit lateral stâng.
    Setări: Preset Abdomen General, mod Doppler Color și Spectral, armonică tisulară (THI) activată.
    Criterii de calitate:
    - TGC reglat optim pentru vizualizare clară la adâncime
    - Vizualizarea întregii cupole diafragmatice
    Securitate acustică: Indice mecanic MI < 1.0 și indice termic TI < 1.0 conform ALARA.
    """
    params = extract_parameters_by_modality(source, 'eco', 'Ecografie Abdominală Totală')
    assert 'clinical_indications' in params
    assert len(params['clinical_indications']) >= 2
    assert 'contraindications' in params
    assert 'patient_prep' in params
    assert 'repaus alimentar' in params['patient_prep'].lower() or 'jeun' in params['patient_prep'].lower()

    assert 'transducers_equipment' in params
    assert 'convex' in params['transducers_equipment']['transducer_types'].lower()
    assert 'Decubit' in params['transducers_equipment']['patient_position']

    assert 'technical_settings' in params
    assert 'Abdomen' in params['technical_settings']['preset']
    assert 'Doppler' in params['technical_settings']['modes']
    assert 'THI' in params['technical_settings']['gain_thi']

    assert 'quality_criteria' in params
    assert len(params['quality_criteria']) >= 1
    assert 'safety_and_limitations' in params
    assert any('MI' in s or 'TI' in s or 'ALARA' in s for s in params['safety_and_limitations'])


def test_extract_fluoro_parameters():
    source = """
    Protocol Tranzit Esofagian Fluoroscopie:
    Indicații clinice:
    - Disfagie orofaringiană și esofagiană
    - Suspiciune de acalazie a cardiei
    - Reflux gastro-esofagian sever
    Contraindicații:
    - Suspiciune de perforație acută a tubului digestiv
    Pregătire pacient: Repaus alimentar minim 6 ore înainte de procedură.
    Contrast: Sulfat de Bariu suspensie 200% w/v, administrare pe cale orală, volum 150 ml.
    Poziție: Ortostatism în incidență oblică anterioară dreaptă (OAD).
    Parametri scopie: Fluoroscopie pulsată, 95 kV, curent 2.0 mA.
    Criterii de calitate:
    - Urmărirea continuă a deglutiției în timp real
    - Evidențierea clară a pliurilor mucoasei
    Radioprotecție: Șorț de plumb 0.5 mm Pb, utilizare Last Image Hold (LIH).
    """
    params = extract_parameters_by_modality(source, 'fluoro', 'Tranzit Esofagian')
    assert 'clinical_indications' in params
    assert len(params['clinical_indications']) >= 2
    assert 'contraindications' in params
    assert 'perforație' in params['contraindications'][0].lower() or 'perforatie' in params['contraindications'][0].lower()

    assert 'patient_prep' in params
    assert 'repaus alimentar' in params['patient_prep'].lower()

    assert 'contrast' in params
    assert 'Bariu' in params['contrast']['agent']
    assert 'Orală' in params['contrast']['route']
    assert '150 ml' in params['contrast']['volume']

    assert 'fluoro_params' in params
    assert '95 kV' in params['fluoro_params']['kv']
    assert '2.0 mA' in params['fluoro_params']['ma_range']
    assert 'pulsată' in params['fluoro_params']['mode'].lower()

    assert 'quality_criteria' in params
    assert len(params['quality_criteria']) >= 1
    assert 'radiation_safety' in params
    assert any('plumb' in s.lower() or 'LIH' in s for s in params['radiation_safety'])


def test_smart_extract_and_apply_full_sync():
    doc = """---
title: Rx Coloană Toracală (Față & Profil)
modality: rx
clinical_indications:
- Nicio indicație specificată
position: Conform incidenței standard
sid_dff: 100 cm
tech_params:
  kv: 75 kV
  mas: 25 mAs
quality_criteria:
- Criterii standard
protection:
- Măsuri standard
---

# Rx Coloană Toracală (Față & Profil)

<div class="grid cards" markdown>

-   __1. Rezumat Clinic & Indicații__

    ---

    === "Indicații Clinice"

        - Nicio indicație specificată

-   __2. Poziționare & Centrare Fascicul__

    ---

    - **Poziție Pacient:** Conform incidenței standard
    - **Punct de Centrare Fascicul:** Pe centrul ariei
    - **Distanță Focar-Film (DFF / SID):** 100 cm
    - **Comandă Respiratorie:** Apnee

-   __3. Parametri Tehnici Expunere__

    ---

    | Parametru Tehnic | Valoare Configurare Generator / Tub |
    |:-----------------|:-------------------------------------|
    | **Tensiune Tub (kV)** | 75 kV |
    | **Sarcină / Produs Curent-Timp (mAs)** | 25 mAs |
    | **Distanță Focar-Film (DFF / SID)** | 100 cm |

-   __4. Criterii de Calitate & Reușită Imagine__

    ---

    - Criterii standard

-   __5. Protecție Radiologică (ALARA)__

    ---

    - Măsuri standard
</div>
"""

    source = """
    Protocol clinic:
    Indicații clinice:
    - Dorsalgii persistente și suspiciune hernie
    - Tasare vertebrală osteoporotică
    Poziție pacient: Decubit dorsal cu suport lombar
    Centrare: Nivel T7 sub incizura jugulară
    Comandă respiratorie: Apnee în expir
    Distanță focar-film: 115 cm
    Tensiune tub: 80 kV
    mAs: 40 mAs
    Criterii de calitate:
    - Vizualizarea clară a tuturor celor 12 vertebre
    - Absența artefactelor respiratorii
    Protecție radiologică:
    - Șorț de plumb gonade și guler tiroidian
    - Colimare strictă
    """

    updated_doc, diffs = smart_extract_and_apply(doc, source, 'Rx Coloană Toracală')
    assert len(diffs) >= 6

    # Frontmatter verificat
    assert 'Dorsalgii persistente' in updated_doc
    assert '80 kV' in updated_doc
    assert '40 mAs' in updated_doc
    assert '115 cm' in updated_doc
    assert 'Decubit dorsal cu suport lombar' in updated_doc
    assert 'T7' in updated_doc

    # Corp Markdown verificat
    assert 'Dorsalgii persistente' in updated_doc
    assert '**Poziție Pacient:** Decubit dorsal cu suport lombar' in updated_doc
    assert '|  80 kV |' in updated_doc or '| 80 kV |' in updated_doc
    assert '|  40 mAs |' in updated_doc or '| 40 mAs |' in updated_doc
    assert '|  115 cm |' in updated_doc or '| 115 cm |' in updated_doc
    assert 'Vizualizarea clară a tuturor celor 12 vertebre' in updated_doc
    assert 'Șorț de plumb gonade' in updated_doc


def test_no_diffs_when_source_has_no_parameters():
    doc = """---
title: Protocol General
modality: rx
tech_params:
  kv: 75 kV
---

# Titlu
"""
    source = "Un text pur descriptiv fără valori sau parametri tehnici."
    updated_doc, diffs = smart_extract_and_apply(doc, source, 'Protocol General')
    assert len(diffs) == 0
    assert updated_doc == doc
