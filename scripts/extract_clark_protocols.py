#!/usr/bin/env python3
"""extract_clark_protocols.py — Extrage protocoale radiografice din tratatul
'Clark's Positioning in Radiography' (Ed. 12) în formatul standard al aplicației.

Funcționalități:
- Scanează cele 532 de pagini ale manualului Clark (Ed. 12).
- Detectează paginile de poziționare radiologică și unește paginile de continuare (2-page spreads).
- Extrage secțiunile structurate: Poziție pacient, Rază centrală (CR), Criterii de calitate, Note, Radioprotecție, Parametri tehnici (FFD/SID, kVp, grilă, focar).
- Traduce terminologia medicală și radiologică în limba română folosind dicționarul medical integrat (+ suport opțional --ai prin Antigravity CLI).
- Extrage fotografiile de poziționare și radiografiile clinice în docs/assets/images/protocols/clark/<slug>/
- Folosește șablonul aplicației (render_rx_document) și salvează fișierele Markdown în docs/rx/<categorie>/<slug>.md.
- Leagă sursa PDF la copia internă din docs/assets/protocols/sources/ pentru zero avertismente MkDocs.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

# Asigură codificarea UTF-8 pe terminalele Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

try:
    from render_rx_protocol import render_rx_document
except ImportError:
    render_rx_document = None

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

# ---------------------------------------------------------------------------
# Dicționar Terminologic Medical Engleză -> Română
# ---------------------------------------------------------------------------

DICTIONARY_TERMS = [
    # Proiecții și orientări radiografice
    (r'\bPOSTERO-ANTERIOR\b', 'Postero-Anterior (PA)'),
    (r'\bANTERO-POSTERIOR\b', 'Antero-Posterior (AP)'),
    (r'\bLATERAL\b', 'Profil (Lateral)'),
    (r'\bANTERIOR OBLIQUE\b', 'Oblică Anterioară'),
    (r'\bPOSTERIOR OBLIQUE\b', 'Oblică Posterioară'),
    (r'\bOBLIQUE\b', 'Oblică'),
    (r'\bAXIAL\b', 'Axială'),
    (r'\bINFERO-SUPERIOR\b', 'Infero-Superioară (Axială)'),
    (r'\bSUPERO-INFERIOR\b', 'Supero-Inferioară'),
    (r'\bSUBMENTOVERTICAL\b', 'Submentoverticală (SMV)'),
    (r'\bVERTICOSUBMENTAL\b', 'Verticosubmentală'),
    (r'\bTANGENTIAL\b', 'Tangențială'),
    (r'\bDORSI-PALMAR\b', 'Dorso-Palmară'),
    (r'\bDORSI-PLANTAR\b', 'Dorso-Plantară'),
    (r'\bPLANTODORSAL\b', 'Planto-Dorsală'),
    (r'\bLATEROMEDIAL\b', 'Latero-Medială'),
    (r'\bMEDIOLATERAL\b', 'Medio-Laterală'),
    (r'\bLORDOTIC\b', 'Lordotică'),
    (r'\bAPICES\b', 'Vârfuri Pulmonare (Apexuri)'),
    (r'\bTRANSORAL\b', 'Transorală (Gură Deschisă)'),

    # Poziții pacient & deviații
    (r'\bERECT\b', 'Ortostatism'),
    (r'\bSUPINE\b', 'Decubit Dorsal'),
    (r'\bPRONE\b', 'Decubit Ventral'),
    (r'\bSEMI-ERECT\b', 'Semi-Ortostatism'),
    (r'\bSEMI-RECUMBENT\b', 'Semi-Șezând'),
    (r'\bSITTING\b', 'Poziție Șezândă'),
    (r'\bHORIZONTAL BEAM\b', 'Fascicul Orizontal'),
    (r'\bLATERAL DECUBITUS\b', 'Decubit Lateral'),
    (r'\bLEFT LATERAL DECUBITUS\b', 'Decubit Lateral Stâng'),
    (r'\bRIGHT LATERAL DECUBITUS\b', 'Decubit Lateral Drept'),
    (r'\bULNAR DEVIATION\b', 'Deviație Ulnară'),
    (r'\bRADIAL DEVIATION\b', 'Deviație Radială'),
    (r'\bWEIGHT-BEARING\b', 'În Încărcare (Ortostatism)'),
    (r'\bWEIGHT[\s\-]+BEARING\b', 'În Încărcare (Ortostatism)'),
    (r'\bBOTH HANDS\b', 'Ambele Mâini'),
    (r'\bBOTH KNEES\b', 'Ambii Genunchi'),
    (r'\bBOTH FEET\b', 'Ambele Picioare'),
    (r'\bBALL CATCHER(?:’|\')?S\b', 'Metoda Norgaard (Ball-Catcher)'),

    # Regiuni anatomice
    (r'\bLUNGS\b', 'Torace (Câmpuri Pulmonare)'),
    (r'\bTHORAX: PHARYNX AND LARYNX\b', 'Căi Aeriene Superioare (Faringe și Laringe)'),
    (r'\bTHORAX: TRACHEA\b', 'Trahee și Strâmtoare Toracică Superioară'),
    (r'\bTHORAX\b', 'Torace'),
    (r'\bHEART\b', 'Cord și Siluetă Cardiovasculară'),
    (r'\bRIBS\b', 'Coaste (Grilaj Costal)'),
    (r'\bSTERNUM\b', 'Stern'),
    (r'\bHAND\b', 'Mână'),
    (r'\bFINGERS\b', 'Degete Mână'),
    (r'\bTHUMB\b', 'Police'),
    (r'\bWRIST\b', 'Pumn (Articulație Radiocarpiană)'),
    (r'\bSCAPHOID\b', 'Scafoid Carpian'),
    (r'\bFOREARM\b', 'Antebraț (Radius și Ulna)'),
    (r'\bELBOW\b', 'Cot'),
    (r'\bHUMERUS\b', 'Humerus'),
    (r'\bSHOULDER\b', 'Umăr'),
    (r'\bCLAVICLE\b', 'Claviculă'),
    (r'\bACROMIOCLAVICULAR JOINTS\b', 'Articulații Acromioclaviculare'),
    (r'\bSCAPULA\b', 'Omoplat (Scapulă)'),
    (r'\bTOES\b', 'Degete Picior'),
    (r'\bFOOT\b', 'Picior'),
    (r'\bCALCANEUM\b', 'Calcaneu'),
    (r'\bANKLE\b', 'Gleznă (Articulație Talocrurală)'),
    (r'\bTIBIA AND FIBULA\b', 'Gambă (Tibie și Peroneu)'),
    (r'\bKNEE JOINT\b', 'Genunchi'),
    (r'\bKNEE\b', 'Genunchi'),
    (r'\bPATELLA\b', 'Rotulă (Patelă)'),
    (r'\bFEMUR\b', 'Femur'),
    (r'\bPELVIS\b', 'Bazin (Pelvis)'),
    (r'\bHIP JOINT\b', 'Șold (Articulație Coxofemurală)'),
    (r'\bHIP\b', 'Șold'),
    (r'\bSACRO-ILIAC JOINTS\b', 'Articulații Sacroiliace'),
    (r'\bCERVICAL VERTEBRAE\b', 'Coloană Cervicală'),
    (r'\bTHORACIC VERTEBRAE\b', 'Coloană Toracală'),
    (r'\bLUMBAR VERTEBRAE\b', 'Coloană Lombară'),
    (r'\bSACRUM AND COCCYX\b', 'Sacru și Coccis'),
    (r'\bSACRUM\b', 'Sacru'),
    (r'\bCOCCYX\b', 'Coccis'),
    (r'\bVERTEBRAL COLUMN\b', 'Coloană Vertebrală'),
    (r'\bSKULL\b', 'Craniu'),
    (r'\bCRANIUM\b', 'Craniu'),
    (r'\bFACIAL BONES\b', 'Masiv Facial (Oase ale Feței)'),
    (r'\bNASAL BONES\b', 'Oase Proprii Nazale (OPN)'),
    (r'\bPARANASAL SINUSES\b', 'Sinusuri Paranazale (SAF)'),
    (r'\bSINUSES\b', 'Sinusuri Paranazale (SAF)'),
    (r'\bMANDIBLE\b', 'Mandibulă'),
    (r'\bTEMPORO-MANDIBULAR JOINTS\b', 'Articulații Temporomandibulare (ATM)'),
    (r'\bABDOMEN AND PELVIC CAVITY\b', 'Abdomen și Cavitate Pelviană'),
    (r'\bABDOMEN\b', 'Abdomen'),
    (r'\bBREAST\b', 'Sân (Mamografie)'),
    (r'\bMAMMOGRAPHY\b', 'Mamografie'),

    # Nomenclatură extinsă tratat Clark
    (r'\bHIP JOINT, UPPER THIRD OF FEMUR AND PELVIS\b', 'Șold și Bazin (Trecime Superioară Femur)'),
    (r'\bHIP JOINT AND UPPER THIRD OF FEMUR\b', 'Articulație Coxofemurală (Șold)'),
    (r'\bHIP JOINT, UPPER THIRD OF\b', 'Articulație Coxofemurală (Șold)'),
    (r'\bHIP JOINT AND UPPER THIRD\b', 'Articulație Coxofemurală (Șold)'),
    (r'\bNECK OF FEMUR\b', 'Col Femural'),
    (r'\bSHAFT OF FEMUR\b', 'Diafiză Femurală'),
    (r'\bFRACTURED FEMUR\b', 'Fractură Femur'),
    (r'\bFRACTURED FEMUR - PAEDIATRIC\b', 'Fractură Femur Pediatric'),
    (r'\bFRACTURED LOWER LIMBS AND PELVIS\b', 'Membru Inferior și Bazin (Fracturi / Politraumă)'),
    (r'\bFRACTURED LOWER LIMBS AND\b', 'Membru Inferior și Bazin (Fracturi)'),
    (r'\bTHORAX: TRACHEA \(INCLUDING THORACIC INLET\)\b', 'Trahee și Strâmtoare Toracică Superioară'),
    (r'\bTHORAX: TRACHEA \(INCLUDING\b', 'Trahee și Strâmtoare Toracică Superioară'),
    (r'\bLATERAL OBLIQUE OF THE MANDIBLE AND MAXILLA\b', 'Mandibulă și Maxilar (Oblică Laterală)'),
    (r'\bLATERAL OBLIQUE OF THE RAMUS OF THE MANDIBLE\b', 'Ram Mandibular (Oblică Laterală)'),
    (r'\bLATERAL OBLIQUE OF THE\b', 'Mandibulă și Maxilar (Oblică Laterală)'),
    (r'\bOUTLET PROJECTIONS\b', 'Incidență Outlet (Subacromială Neer)'),
    (r'\bOUTLET PROJECTION\b', 'Incidență Outlet (Subacromială Neer)'),
    (r'\bRECURRENT DISLOCATION\b', 'Luxație Recurentă Umăr'),
    (r'\bSTRYKER(?:’|\')?S\b', 'Metoda Stryker'),
    (r'\bVON ROSEN PROJECTION\b', 'Incidența Von Rosen (Displazie Șold)'),
    (r'\bNORGAARD\b', 'Incidența Norgaard (Ball-Catcher)'),
    (r'\bBICIPITAL GROOVE\b', 'Culisa Bicipitală (Șanț Intertubercular)'),
    (r'\bHUMERUS - BICIPITAL GROOVE\b', 'Humerus (Culisa Bicipitală)'),
    (r'\bHUMERUS - NECK\b', 'Humerus Proximal (Col Chirurgical)'),
    (r'\bHUMERUS - SHAFT\b', 'Diafiză Humerală'),
    (r'\bHUMERUS - SUPRACONDYLAR\b', 'Humerus Distal (Regiune Supracondiliană)'),
    (r'\bSPINE - SCOLIOSIS\b', 'Coloană Vertebrală (Bilanț Scolioză)'),
    (r'\bPOST - NASAL SPACE\b', 'Rinofaringe (Vegetații Adenoide)'),
    (r'\bLEG LENGTH ASSESSMENT\b', 'Măsurare Lungime Membre Inferioare (Telemetrie)'),
    (r'\bLEG ALIGNMENT\b', 'Axa Membrelor Inferioare (Ortostatism)'),
    (r'\bCARPAL TUNNEL\b', 'Canal Carpian'),
    (r'\bSUBTALAR JOINTS\b', 'Articulații Subtalare'),
    (r'\bSTERNOCLAVICULAR JOINTS\b', 'Articulații Sternoclaviculare'),
    (r'\bCORACOID PROCESS\b', 'Proces Coracoid'),
    (r'\bBITEWING RADIOGRAPHY\b', 'Radiografie Dentară Bite-Wing (Interproximală)'),
    (r'\bPERIAPICAL RADIOGRAPHY\b', 'Radiografie Dentară Retroalveolară (Periapicală)'),
    (r'\bOCCLUSAL RADIOGRAPHY\b', 'Radiografie Dentară Ocluzală'),
    (r'\bCEPHALOMETRY\b', 'Teleradiografie Craniană (Cefalometrie)'),
    (r'\bTOMOGRAPHY\b', 'Tomografie Liniară Convențională'),
    (r'\bCRANIUM: NON - ISOCENTRIC\b', 'Craniu (Incidențe Neizocentrice)'),
    (r'\bCERVICO - THORACIC VERTEBRAE\b', 'Coloană Cervico-Toracală (Joncțiune C7-T1)'),
    (r'\bLUMBO - SACRAL JUNCTION\b', 'Joncțiune Lombo-Sacrată (L5-S1)'),
    (r'\bCHEST - POST - NEONATAL\b', 'Torace Pediatric (Post-Neonatal)'),
    (r'\bCHEST - NEONATAL\b', 'Torace Neonatal (Nou-Născut)'),
    (r'\bBASIC PROJECTIONS\b', 'Incidențe Standard de Bază'),
    (r'\bCONVENTIONAL FILM/SCREEN METHOD\b', 'Metoda Convențională Film/Ecran'),
    (r'\bSINGLE EXPOSURE METHOD\b', 'Metoda Expunere Unică (Format Lung)'),
    (r'\bUPPER RIBS\b', 'Coaste Superioare (Grilaj Costal Supradiafragmatic)'),
    (r'\bLOWER RIBS\b', 'Coaste Inferioare (Grilaj Costal Subdiafragmatic)'),
    (r'\bURINARY TRACT\b', 'Tract Urinar (Aparatul Renal)'),
    (r'\bURINARY BLADDER\b', 'Vezică Urinară'),
    (r'\bBILIARY SYSTEM\b', 'Aparat Biliar'),
    (r'\bHEART AND AORTA\b', 'Siluetă Cardiovasculară și Aortă'),
    (r'\bHEART AND LUNGS - FLUID LEVELS\b', 'Torace (Nivele Hidroaerice Pleuro-Pulmonare)'),
    (r'\bHEART AND LUNGS\b', 'Torace (Cord și Câmpuri Pulmonare)'),
    (r'\bKIDNEYS\b', 'Aparat Renal (Rinichi)'),
    (r'\bLARYNX\b', 'Laringe'),
    (r'\bEXTENDED CRANIO - CAUDAL\b', 'Cranio-Caudală Extinsă (Mamografie)'),
    (r'\bLATERALLY ROTATED\b', 'Rotație Externă (Laterală)'),
    (r'\bMEDIO - LATERAL\b', 'Medio-Laterală'),
    (r'\bLATERO - MEDIAL\b', 'Latero-Medială'),
    (r'\bLATERAL PROJECTIONS\b', 'Incidențe de Profil (Laterale)'),
]

PHRASE_TRANSLATIONS = [
    (r'fractures and dislocation(?:s)?', 'fracturi și luxații / subluxații'),
    (r'fracture(?:s)?', 'suspiciune de fractură'),
    (r'dislocation(?:s)?', 'luxație articulară'),
    (r'foreign bod(?:y|ies)', 'corp străin radiopac'),
    (r'rheumatoid arthritis', 'poliartrită reumatoidă / artropatie inflamatorie'),
    (r'osteoarthritis', 'artroză / modificări degenerative articulare'),
    (r'pleural effusion', 'revărsat pleural (pleurezie)'),
    (r'pneumothorax', 'pneumotorax'),
    (r'pneumonia', 'pneumonie / infiltrate pulmonare'),
    (r'atelectasis', 'atelectazie pulmonară'),
    (r'intestinal obstruction', 'ocluzie intestinală (nivele hidroaerice)'),
    (r'renal calculi|calculi', 'litiază urinară / calculi radiopaci'),
    (r'free gas|subdiaphragmatic gas', 'pneumoperitoneu (aer liber subdiafragmatic)'),
    (r'calcification(?:s)?', 'calcificări patologice'),
    (r'soft-tissue swelling', 'edem / tumefiere de părți moi'),
    (r'infection', 'proces infecțios / inflamator'),
    (r'neoplasm|tumour(?:s)?', 'proces proliferativ tumoral'),

    # Comenzi de respirație
    (r'Exposure is made in full normal arrested inspiration', 'Apnee în inspir profund complet'),
    (r'arrested respiration(?:, usually)? after full expiration', 'Apnee la sfârșitul expirului complet (diafragm ridicat)'),
    (r'full expiration', 'expir profund complet'),
    (r'full inspiration', 'inspir profund complet'),
    (r'suspended respiration', 'apnee pe durata expunerii'),

    # Criterii de calitate
    (r'Full lung fields with the scapulae projected laterally', 'Câmpuri pulmonare complet vizibile, cu scapulele proiectate în afara ariei pulmonare'),
    (r'No rotation', 'Absența rotației anatomice (simetrie bilaterală perfectă)'),
    (r'sharp reproduction of the bones', 'Contururi osoase nete, fără estompare cinetică'),
    (r'All phalanges(?:, including soft-tissue fingertips)?', 'Toate falangele vizibile integral, inclusiv părțile moi ale pulpei degetelor'),
    (r'visualize small or low-opacity stones', 'Diferențiere tisulară adecvată pentru vizualizarea calculilor de dimensiuni reduse'),
]

# Mapare Capitole Clark -> Categorie aplicație
CHAPTER_CATEGORY_RANGES = [
    (52, 91, 'membru-superior'),      # Cap 2 The Upper Limb
    (92, 119, 'membru-superior'),     # Cap 3 The Shoulder
    (120, 155, 'membru-inferior'),    # Cap 4 The Lower Limb
    (156, 177, 'membru-inferior'),    # Cap 5 The Hip, Pelvis and Sacro-iliac Joints
    (178, 207, 'coloana'),            # Cap 6 The Vertebral Column
    (208, 243, 'torace'),             # Cap 7 The Thorax and Upper Airways
    (244, 273, 'craniu-saf'),         # Cap 8 The Skull
    (274, 293, 'craniu-saf'),         # Cap 9 The Facial Bones and Sinuses
    (294, 345, 'craniu-saf'),         # Cap 10 Dental Radiography
    (346, 365, 'abdomen'),            # Cap 11 The Abdomen and Pelvic Cavity
    (366, 395, 'ward'),               # Cap 12-13 Ward / Theatre
    (396, 449, 'pediatrie'),          # Cap 14 Paediatric Radiography
    (450, 479, 'torace'),             # Cap 15 Mammography
]


def remove_diacritics(text: str) -> str:
    """Elimină diacriticele românești pentru generarea slug-urilor curate."""
    mapping = {
        'ă': 'a', 'Ă': 'A', 'â': 'a', 'Â': 'A',
        'î': 'i', 'Î': 'I',
        'ș': 's', 'Ș': 'S', 'ş': 's', 'Ş': 'S',
        'ț': 't', 'Ț': 'T', 'ţ': 't', 'Ţ': 'T',
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text


def slugify(text: str) -> str:
    """Transformă un titlu într-un slug conform sistemului de fișiere."""
    text = remove_diacritics(text.lower().strip())
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def clean_text(text: str) -> str:
    """Normalizează spațiile, cratimele de despărțire în silabe și ligaturile."""
    if not text:
        return ""
    text = text.replace('\ufb01', 'fi').replace('\ufb02', 'fl')
    text = re.sub(r'(\w+)[-—–]\n(\w+)', r'\1\2', text)
    text = text.replace('•', '\n• ')
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('•') or line.startswith('-') or line.startswith('*'):
            lines.append(line)
        else:
            if lines and not lines[-1].endswith((':', '.')):
                lines[-1] = f"{lines[-1]} {line}"
            else:
                lines.append(line)
    text = '\n'.join(lines)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def translate_text(text: str) -> str:
    """Traduce un fragment de text folosind dicționarul integrat."""
    if not text:
        return ""
    translated = text
    for pattern, rep in DICTIONARY_TERMS:
        translated = re.sub(pattern, rep, translated, flags=re.IGNORECASE)
    for pattern, rep in PHRASE_TRANSLATIONS:
        translated = re.sub(pattern, rep, translated, flags=re.IGNORECASE)
    return translated


def parse_bullets(text: str) -> list[str]:
    """Extrage liniile bullet din text."""
    if not text:
        return []
    items = []
    current_item = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('•') or line.startswith('-') or line.startswith('*'):
            if current_item:
                items.append(' '.join(current_item).strip())
                current_item = []
            cleaned = re.sub(r'^[•\-\*]\s*', '', line).strip()
            if cleaned:
                current_item.append(cleaned)
        else:
            current_item.append(line)
    if current_item:
        items.append(' '.join(current_item).strip())
    return [translate_text(it) for it in items if it]


# ---------------------------------------------------------------------------
# Structura de Protocol Clark
# ---------------------------------------------------------------------------

@dataclass
class ClarkPageData:
    page_num: int
    anatomy: str
    projection: str
    category: str
    sections: dict[str, str] = field(default_factory=dict)
    text: str = ""


def detect_clark_category(page_num: int, text: str) -> str:
    """Determină categoria radiologică pe baza capitolelor sau a anatomiei."""
    if page_num >= 480:
        t = text.lower()
        if any(k in t for k in ['kidney', 'renal', 'abdomen', 'urinary', 'pelvic']):
            return 'abdomen'
        elif any(k in t for k in ['larynx', 'pharynx', 'chest', 'lung', 'trachea']):
            return 'torace'
        elif any(k in t for k in ['mandible', 'skull', 'facial', 'temporo', 'dental']):
            return 'craniu-saf'
        elif any(k in t for k in ['spine', 'vertebra']):
            return 'coloana'
        return 'torace'

    for start, end, cat in CHAPTER_CATEGORY_RANGES:
        if start <= page_num <= end:
            if cat == 'ward':
                t = text.lower()
                if any(k in t for k in ['chest', 'thorax', 'lungs']):
                    return 'torace'
                elif any(k in t for k in ['abdomen', 'pelvis']):
                    return 'abdomen'
                elif any(k in t for k in ['femur', 'hip', 'knee', 'leg']):
                    return 'membru-inferior'
                elif any(k in t for k in ['humerus', 'arm', 'elbow', 'shoulder']):
                    return 'membru-superior'
                elif any(k in t for k in ['cervical', 'spine', 'vertebrae']):
                    return 'coloana'
                return 'torace'
            return cat
    return 'torace'


def extract_clark_header(page_text: str, page_num: int | None = None) -> tuple[str, str]:
    """Extrage regiunea anatomică și denumirea incidenței din antetul paginii Clark."""
    lines = [l.strip() for l in page_text.splitlines() if l.strip()]
    lines_clean = [
        l for l in lines
        if not l.isdigit()
        and not l.startswith('Section ')
        and not l.startswith('Chapter ')
    ]
    if not lines_clean:
        return 'Radiografie', 'Incidență Standard'

    # Extragere anatomie
    l0 = lines_clean[0]
    m0 = re.match(r'^(\d+)\s+(.*)$', l0)
    if m0 and len(m0.group(1)) <= 2:
        anat = m0.group(2).strip()
        rem_lines = lines_clean[1:]
    else:
        anat = l0
        rem_lines = lines_clean[1:]

    # Continuare anatomie pe linia următoare dacă e împărțită pe două rânduri
    if rem_lines and (
        anat.endswith(('and', 'of', 'for', 'the', 'including', 'with', 'in', ','))
        or rem_lines[0].startswith(('of ', 'and ', 'femur', 'pelvis', 'mandible', 'lumbar', 'thoracic inlet)'))
    ):
        anat = f"{anat} {rem_lines[0]}".strip()
        rem_lines = rem_lines[1:]

    # Override cazuri particulare din tratatul Clark
    if 'bicipital groove' in anat.lower() or 'intertuberous sulcus' in anat.lower():
        anat = 'Humerus - Bicipital groove'
    elif 'outlet projections' in anat.lower():
        anat = 'Shoulder - Outlet'
    elif 'recurrent dislocation' in anat.lower():
        anat = 'Shoulder - Recurrent dislocation'
    elif 'common paediatric' in anat.lower() or page_num == 405:
        anat = 'Chest - neonatal'
        return anat, 'Antero-posterior - supine'
    elif page_num == 421:
        anat = 'Sinuses - Post-nasal space'
        return anat, 'Lateral - supine'
    elif 'feet' in anat.lower() and 'supported' in anat.lower():
        anat = 'Foot'
        return anat, 'Weight-bearing projections'
    elif 'heart and lungs - fluid levels' in anat.lower() or page_num == 370:
        anat = 'Heart and lungs'
        return anat, 'Lateral decubitus (fluid levels)'
    elif page_num == 329:
        anat = 'Mandible and maxilla'
        return anat, 'Lateral oblique of the body of the mandible and maxilla'
    elif page_num in (331, 332):
        anat = 'Mandible and maxilla'
        return anat, 'Lateral oblique of the ramus of the mandible'

    anat = re.sub(r'[\u2010-\u2015\u2013\u2014\-–—]+', ' - ', anat)
    anat = re.sub(r'\s+', ' ', anat).strip(' -')

    # Căutare 'Position of patient'
    pos_idx = -1
    for i, l in enumerate(lines):
        if re.search(r'position of patient', l, re.I):
            pos_idx = i
            break

    proj = ''
    proj_candidate_top = rem_lines[0] if rem_lines else ''
    is_valid_top = False
    if proj_candidate_top and len(proj_candidate_top) <= 50 and not proj_candidate_top.endswith('.'):
        if not any(k in proj_candidate_top.lower() for k in [
            'introduction', 'practice', 'obtain', 'radiography', 'common', 'patient',
            'conjunction', 'demonstrate', 'selected', 'referral criteria', 'modification', 'the position'
        ]):
            is_valid_top = True

    if is_valid_top:
        proj = proj_candidate_top
        if len(rem_lines) > 1:
            next_l = rem_lines[1]
            if (next_l.startswith('(') and next_l.endswith(')')) or (next_l.lower() in ['oblique', 'view', 'projection', 'positions']):
                proj = f"{proj} {next_l}"
    else:
        # Căutare în sus de la 'Position of patient' până la începutul paginii
        if pos_idx > 0:
            for j in range(pos_idx - 1, 0, -1):
                cand = lines[j].strip()
                if not cand or len(cand) > 60 or cand.endswith('.'):
                    continue
                if any(k in cand.lower() for k in [
                    'antero', 'postero', 'lateral', 'oblique', 'axial', 'tangential', 'outlet',
                    'method', 'erect', 'supine', 'prone', 'decubitus', 'view', 'projection',
                    'basic', 'alternative', 'supplementary', 'caudad', 'cephalad', 'space',
                    'single exposure', 'alignment', 'standing', 'sitting', 'stryker', 'norgaard',
                    'stenver', 'tunnel', 'sulcus', 'inversion', 'eversion', 'abduction', 'adduction', 'rotat',
                    'latero-medial', 'medio-lateral', 'cranio-caudal', 'occlusal', 'panoramic'
                ]):
                    proj = cand
                    break
        if not proj and rem_lines:
            proj = rem_lines[0][:50]

    proj = re.sub(r'[\u2010-\u2015\u2013\u2014\-–—]+', ' - ', proj)
    proj = re.sub(r'\s+', ' ', proj).strip(' -')
    return re.sub(r'\s+', ' ', anat).strip(' -'), re.sub(r'\s+', ' ', proj).strip(' -')


def parse_clark_page_sections(page_text: str) -> dict[str, str]:
    """Parsează secțiunile structurate dintr-o pagină Clark."""
    patterns = [
        ('patient_pos', r'Position of patient(?:\s+and\s+cassette)?'),
        ('cr', r'Direction and centring(?:\s+of\s+the\s+X-ray\s+beam)?'),
        ('criteria', r'Essential image characteristics'),
        ('faults', r'Common faults and remedies'),
        ('radiological', r'Radiological considerations'),
        ('notes', r'(?:Notes|Note\b|Expiration technique)'),
        ('protection', r'Radiation protection'),
    ]

    lines = [l.strip() for l in page_text.splitlines() if l.strip()]
    sections = {'intro': []}
    curr = 'intro'

    for line in lines:
        matched = False
        for sec_name, pat in patterns:
            if re.match(r'^' + pat, line, re.IGNORECASE):
                curr = sec_name
                sections[curr] = []
                matched = True
                break
        if not matched:
            low = line.lower()
            if curr == 'cr' and low in ['of the x-ray beam', 'x-ray beam', 'of x-ray beam', 'of the central ray']:
                continue
            if curr == 'patient_pos' and low in ['and cassette', 'of patient and cassette']:
                continue
            sections[curr].append(line)

    return {k: clean_text('\n'.join(v)) for k, v in sections.items() if v}


def parse_tech_factors_clark(text: str) -> tuple[str, dict]:
    """Extrage parametrii tehnici: FFD/SID, kVp, grilă, focar, AEC din text."""
    params = {}

    # SID / FFD
    sid = "100 cm"
    ffd_m = re.search(r'(?:FFD|SID)\s*(?:of|is|[:=—–\-])*\s*(\d+(?:\s*[–\-]\s*\d+)?)\s*cm', text, re.I)
    if ffd_m:
        sid_raw = ffd_m.group(1).replace('–', '-').strip()
        sid = f"{sid_raw} cm"
    elif '180 cm' in text or '150-180' in text:
        sid = "180 cm"
    elif '115 cm' in text or '100-115' in text:
        sid = "115 cm"

    # kVp
    kv_m = re.search(r'(\d+\s*(?:[–\-]\s*\d+)?)\s*kVp?', text, re.I)
    if kv_m:
        params['kv'] = kv_m.group(1).replace('–', '-').strip()
    else:
        params['kv'] = "DE CONFIGURAT PE APARAT"

    params['mas'] = "Conform AEC / grosime anatomică"

    # Grilă
    if re.search(r'moving grid|bucky|anti-scatter grid', text, re.I):
        params['grid'] = "Cu grilă antidifuzoare Bucky"
    elif re.search(r'non-grid|direct exposure|without grid', text, re.I):
        params['grid'] = "Fără grilă (expunere directă)"
    else:
        params['grid'] = "Conform grosimii anatomice (> 10-12 cm cu grilă)"

    # Focar
    if '1.3 mm' in text or 'broad focus' in text or 'large focus' in text or '180 cm' in sid:
        params['focal_spot'] = "Focar Mare (1.0 - 1.2 mm)"
    else:
        params['focal_spot'] = "Focar Mic (0.6 mm)"

    # AEC
    if re.search(r'central and right upper lateral|both chambers', text, re.I):
        params['aec_chambers'] = "Camera centrală și camera laterală superioară"
    elif re.search(r'central chamber', text, re.I):
        params['aec_chambers'] = "Camera centrală"
    elif 'Bucky' in params['grid']:
        params['aec_chambers'] = "Camerele laterale (sau camera centrală funcție de regiune)"
    else:
        params['aec_chambers'] = "DE CONFIGURAT PE APARAT"

    params['filtration'] = "Totală ≥ 2.5 mm Al echivalent (conform Clark: 3.0 mm Al eq.)"

    # Caseta / Colimare
    cas_m = re.search(r'(\d+\s*[\u0002\x02x×]\s*\d+)\s*[- ]?cm\s*(?:cassette|film|grid)?', text, re.I)
    if cas_m:
        cas_dim = cas_m.group(1).replace('\x02', 'x').replace('×', 'x').strip()
        params['collimation'] = f"Colimare strictă adaptată pe receptor {cas_dim} cm"
    else:
        params['collimation'] = "Colimare strictă la aria anatomică de interes diagnostic"

    return sid, params


def extract_clark_page_figures(doc: fitz.Document, page_num: int, output_dir: Path, slug: str, start_index: int = 1) -> list[dict]:
    """Extrage imaginile de pe pagina dată din PDF și le asociază legende."""
    page = doc[page_num - 1]
    image_infos = page.get_image_info(xrefs=True)
    text = page.get_text()

    # Caută legende la finalul textului sau după tipare de radiografii
    caption_candidates = []
    for line in text.splitlines():
        line = line.strip()
        if re.search(r'radiograph|showing|normal|appearance|fracture|calcification|inter-phalangeal|joint space|pneumothorax', line, re.I) and len(line) > 15:
            if not any(k in line.lower() for k in ['position of patient', 'direction and centring', 'essential image', 'this projection', 'common faults', 'radiological considerations']):
                caption_candidates.append(line)

    valid_imgs = [info for info in image_infos if info['width'] >= 100 and info['height'] >= 100]
    valid_imgs.sort(key=lambda x: x['bbox'][1])  # sortare verticală de sus în jos

    figures_out = []
    target_img_dir = output_dir / slug
    target_img_dir.mkdir(parents=True, exist_ok=True)

    for idx, info in enumerate(valid_imgs):
        fig_idx = start_index + idx
        xref = info['xref']
        img_data = doc.extract_image(xref)
        ext = img_data['ext']
        img_bytes = img_data['image']

        filename = f"fig_{fig_idx}.{ext}"
        file_path = target_img_dir / filename
        file_path.write_bytes(img_bytes)

        raw_cap = caption_candidates[idx] if idx < len(caption_candidates) else f"Figura {fig_idx}: Aspect radiografic / Poziționare (Clark Ed. 12)"
        trans_cap = translate_text(raw_cap)

        desc = "Aspect radiografic / ghid de poziționare conform tratatului Clark (Ed. 12)"
        if fig_idx == 1:
            desc = "Poziționare pacient și centrare fascicul conform Clark (Ed. 12)"

        figures_out.append({
            'url': f"assets/images/protocols/clark/{slug}/{filename}",
            'caption': trans_cap,
            'description': desc,
        })

    return figures_out


def build_clark_protocol_frontmatter(
    page_data: ClarkPageData,
    continuation_sections: dict[str, str],
    sid: str,
    tech_params: dict,
    figures: list[dict],
    protocol_title: str,
    slug: str,
    sources_pdf_rel: str,
    use_ai: bool = False
) -> dict:
    """Construiește structura YAML frontmatter conform standardului aplicației."""
    secs = dict(page_data.sections)
    for k, v in continuation_sections.items():
        if k in secs:
            secs[k] = f"{secs[k]}\n\n{v}"
        else:
            secs[k] = v

    # 1. Poziție
    pos_raw = secs.get('patient_pos', '')
    pos_str = translate_text(pos_raw) if pos_raw else "Pacient poziționat conform reperelor anatomice standard."

    # 2. Centrare rază centrală
    cr_raw = secs.get('cr', '')
    cr_str = translate_text(cr_raw) if cr_raw else "Raza centrală perpendiculară pe centrul receptorului de imagine."

    # 3. Respirație
    resp_raw = ""
    resp_match = re.search(r'(?:exposure is made|respiration)[^.\n]+', page_data.text + " " + secs.get('cr', ''), re.I)
    if resp_match:
        resp_raw = resp_match.group(0)
    elif 'respiration' in secs.get('notes', '').lower():
        resp_raw = "Apnee completă pe durata expunerii."
    else:
        resp_raw = "Apnee pe durata expunerii (apnee în inspir pentru torace; expir pentru abdomen/bazin)."
    breathing_str = translate_text(resp_raw)

    # 4. Indicații clinice
    ind_raw = secs.get('radiological', '')
    if not ind_raw and secs.get('intro', ''):
        # Filtrează liniile introductive de antet sau instrucțiuni pur tehnice de casetă
        clean_intro_lines = []
        for l in secs['intro'].splitlines():
            l_str = l.strip()
            if not l_str:
                continue
            if re.match(r'^\d+\s+[A-Za-z]', l_str) or any(k in l_str.lower() for k in [
                'basic projection', 'recommended projection', 'cassette with', 'lead-rubber mask',
                'section ', 'chapter '
            ]):
                continue
            clean_intro_lines.append(l_str)
        ind_raw = '\n'.join(clean_intro_lines)

    ind_bullets = parse_bullets(ind_raw)
    if not ind_bullets or (len(ind_bullets) == 1 and len(ind_bullets[0]) < 45):
        ind_bullets = [
            f"Evaluare radiografică a regiunii {translate_text(page_data.anatomy)} ({translate_text(page_data.projection)}).",
            "Suspiciune de leziuni traumatice (fracturi, luxații sau diastazis articular).",
            "Bilanț osteoarticular / visceral conform recomandării medicale de trimitere."
        ]

    # 5. Criterii de calitate
    crit_raw = secs.get('criteria', '')
    crit_bullets = parse_bullets(crit_raw)
    if 'faults' in secs:
        faults_bullets = parse_bullets(secs['faults'])
        crit_bullets.extend([f"Erori de evitat / remedii: {fb}" for fb in faults_bullets[:3]])
    if not crit_bullets:
        crit_bullets = [
            f"Vizualizarea clară a întregii arii anatomice ({translate_text(page_data.anatomy)}).",
            "Absența artefactelor de mișcare; trabeculație osoasă și contururi nete.",
            "Densitate optică și contrast adecvate pentru diferențierea țesuturilor moi de structurile osoase."
        ]

    # 6. Radioprotecție ALARA
    prot_raw = secs.get('protection', '')
    prot_bullets = parse_bullets(prot_raw)
    prot_bullets.extend([
        "Ecranare gonadică cu șorț plumbat dacă gonadele sunt în apropierea fasciculului util (regula ALARA).",
        "Colimare precisă la dimensiunea anatomică strict necesară pentru reducerea dozei și a radiației difuze.",
        "Verificarea posibilității unei sarcini la pacientele de vârstă fertilă înainte de expunere."
    ])

    # 7. Note clinice
    notes_raw = secs.get('notes', '')
    notes_str = translate_text(notes_raw) if notes_raw else "Pregătirea pacientului prin îndepărtarea tuturor accesoriilor radio-opace."

    fm = {
        'title': protocol_title,
        'slug': slug,
        'category': page_data.category,
        'modality': 'rx',
        'author': 'Departamentul de Radiologie / Referință Clark (Ed. 12)',
        'last_updated': '2026-09-16',
        'clinical_indications': ind_bullets,
        'position': pos_str,
        'centering': cr_str,
        'sid_dff': sid,
        'breathing': breathing_str,
        'tech_params': tech_params,
        'quality_criteria': crit_bullets,
        'protection': prot_bullets,
        'notes': notes_str,
        'images': figures,
        'sources': [
            {
                'title': f"Clark's Positioning in Radiography (Ed. 12), Pagina {page_data.page_num}",
                'url': f"{sources_pdf_rel}#page={page_data.page_num}"
            }
        ]
    }

    if use_ai and shutil.which('agy'):
        try:
            from extract_bontrager_protocols import enrich_with_ai
            fm = enrich_with_ai(fm)
        except Exception:
            pass

    return fm


def format_clark_title(anat_raw: str, proj_raw: str, page_num: int | None = None) -> tuple[str, str]:
    """Formatează titlul în stilul aplicației: Rx [Anatomie] [Proiecție] (Clark) și generează slug-ul."""
    t_anat = translate_text(anat_raw)
    t_proj = translate_text(proj_raw)

    title = f"Rx {t_anat} {t_proj}".strip()
    title = re.sub(r'\bRx\s+Rx\b', 'Rx', title)
    title = re.sub(r'\s+', ' ', title).strip()

    slug_base = slugify(remove_diacritics(title))[:110].strip('-')
    if not slug_base.startswith('rx-'):
        slug_base = f"rx-{slug_base}"

    if page_num:
        slug = f"{slug_base}-p{page_num}-clark"
    else:
        if not slug_base.endswith('-clark'):
            slug = f"{slug_base}-clark"
        else:
            slug = slug_base
    return title, slug


# ---------------------------------------------------------------------------
# Procesul de Extracție
# ---------------------------------------------------------------------------

def find_clark_positioning_pages(doc: fitz.Document) -> list[int]:
    """Descoperă paginile care conțin instrucțiuni de poziționare în manualul Clark."""
    pages = []
    for pno in range(len(doc)):
        if pno + 1 == 451:  # Pagină introductivă mamografie fără proiecție specifică
            continue
        text = doc[pno].get_text()
        if re.search(r'Position of patient(?:\s+and\s+cassette)?', text, re.I) and (
            'centring' in text.lower() or 'central ray' in text.lower() or 'direction' in text.lower()
        ):
            # Exclude pagini pur introductive sau tabele de sumar
            if 'RECOMMENDED PROJECTIONS' in text and 'Section ' in text:
                continue
            pages.append(pno + 1)
    return pages


def process_clark(
    pdf_path: Path,
    output_dir: Path,
    images_base_dir: Path,
    category_filter: str | None = None,
    page_selection: list[int] | None = None,
    limit: int | None = None,
    use_ai: bool = False,
    dry_run: bool = False,
    overwrite: bool = True
) -> list[Path]:
    """Execută extracția completă a protocoalelor din manualul Clark."""
    doc = fitz.open(pdf_path)
    all_pos_pages = find_clark_positioning_pages(doc)

    if page_selection:
        target_pages = [p for p in all_pos_pages if p in page_selection]
    else:
        target_pages = all_pos_pages

    print(f"Manual Clark deschis: {pdf_path.name} ({len(doc)} pagini).")
    print(f"Identificate {len(target_pages)} pagini de poziționare active.")

    generated_files = []
    count = 0
    consumed_pages: set[int] = set()

    # Cale relativă către fișierul sursă PDF din docs/assets/protocols/sources/
    sources_dir = ROOT_DIR / 'docs/assets/protocols/sources'
    target_source_pdf = sources_dir / pdf_path.name
    if not target_source_pdf.exists():
        matches = list(sources_dir.glob('*Clark*.pdf'))
        if matches:
            target_source_pdf = matches[0]

    for pno in target_pages:
        if pno in consumed_pages:
            continue
        if limit and count >= limit:
            break

        text = doc[pno - 1].get_text()
        cat = detect_clark_category(pno, text)

        if category_filter and category_filter != 'all' and cat != category_filter:
            continue

        anat, proj = extract_clark_header(text, pno)
        sections = parse_clark_page_sections(text)

        # Verifică dacă pagina următoare este o continuare (pno + 1)
        continuation_sections = {}
        next_pno = pno + 1
        if next_pno <= len(doc):
            next_text = doc[next_pno - 1].get_text()
            is_cont = False
            if any(w in next_text for w in ['(contd)', '(cont’d)', '(cont\'d)', 'Common faults and remedies', 'Radiological considerations']):
                is_cont = True
            elif not re.search(r'position of patient', next_text, re.I) and any(w in next_text for w in ['Essential image characteristics', 'Notes', 'Radiation protection']):
                is_cont = True

            if is_cont:
                continuation_sections = parse_clark_page_sections(next_text)
                consumed_pages.add(next_pno)

        count += 1
        print(f"\n[{count}] Procesare Pagina {pno}: {anat} — {proj} (Categorie: {cat})")

        # Formatare titlu și slug
        protocol_title, slug = format_clark_title(anat, proj, pno)

        # Parametri tehnici
        combined_text = text + " " + " ".join(continuation_sections.values())
        sid, tech_params = parse_tech_factors_clark(combined_text)

        # Extragere imagini
        if not dry_run:
            figures = extract_clark_page_figures(doc, pno, images_base_dir, slug)
            if continuation_sections:
                figures_cont = extract_clark_page_figures(doc, next_pno, images_base_dir, slug, start_index=len(figures) + 1)
                figures.extend(figures_cont)
            print(f"  -> Extrase {len(figures)} figuri/imagini")
        else:
            figures = []
            print("  -> Dry run: extragere imagini omisă")

        # Calcul cale relativă către PDF
        target_category_dir = output_dir / cat
        pdf_rel = Path(os.path.relpath(target_source_pdf, target_category_dir)).as_posix()

        page_data = ClarkPageData(
            page_num=pno,
            anatomy=anat,
            projection=proj,
            category=cat,
            sections=sections,
            text=text
        )

        # Construire frontmatter
        fm = build_clark_protocol_frontmatter(
            page_data=page_data,
            continuation_sections=continuation_sections,
            sid=sid,
            tech_params=tech_params,
            figures=figures,
            protocol_title=protocol_title,
            slug=slug,
            sources_pdf_rel=pdf_rel,
            use_ai=use_ai
        )

        # Randare Markdown cu șablonul aplicației
        if render_rx_document:
            markdown_content = render_rx_document(fm)
        else:
            import yaml
            markdown_content = "---\n" + yaml.dump(fm, allow_unicode=True) + "---\n# " + fm['title'] + "\n"

        target_file = target_category_dir / f"{slug}.md"

        if dry_run:
            print(f"  -> [DRY RUN] Destinație: {target_file}")
            print(f"  -> Titlu: {fm['title']}")
            print(f"  -> SID: {fm['sid_dff']} | kV: {fm['tech_params'].get('kv')}")
        else:
            if target_file.exists() and not overwrite:
                print(f"  -> Fișierul {target_file.name} există deja. Omis (--no-overwrite).")
            else:
                target_file.parent.mkdir(parents=True, exist_ok=True)
                target_file.write_text(markdown_content, encoding='utf-8')
                print(f"  -> Generat cu succes: {target_file}")
                generated_files.append(target_file)

    return generated_files


def main():
    parser = argparse.ArgumentParser(description="Extrage protocoale radiografice din tratatul Clark în formatul aplicației.")
    parser.add_argument('--pdf', type=str, default='Clark___Positioning_in_Radiography__12th_edition.pdf',
                        help='Calea către fișierul PDF al manualului Clark.')
    parser.add_argument('--output-dir', type=str, default='docs/rx',
                        help='Directorul rădăcină pentru salvarea protocoalelor Rx.')
    parser.add_argument('--images-dir', type=str, default='docs/assets/images/protocols/clark',
                        help='Directorul rădăcină pentru salvarea imaginilor extrase.')
    parser.add_argument('--category', type=str, default=None,
                        help='Filtrează după categorie: torace, abdomen, coloana, membru-superior, membru-inferior, craniu-saf, pediatrie, sau all.')
    parser.add_argument('--pages', type=str, default=None,
                        help='Listă sau interval de pagini (ex: "55,57" sau "55-65").')
    parser.add_argument('--limit', type=int, default=None,
                        help='Număr maxim de protocoale de generat.')
    parser.add_argument('--ai', action='store_true',
                        help='Activează rafinarea traducerii prin Antigravity CLI (agy).')
    parser.add_argument('--dry-run', action='store_true',
                        help='Afișează simularea fără a scrie pe disc.')
    parser.add_argument('--no-overwrite', dest='overwrite', action='store_false',
                        help='Nu suprascrie fișierele deja existente.')

    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.is_file():
        alt_path = ROOT_DIR / 'docs/assets/protocols/sources' / pdf_path.name
        if alt_path.is_file():
            pdf_path = alt_path
        else:
            raise SystemExit(f"Eroare: Nu s-a găsit fișierul PDF Clark: {args.pdf}")

    if not fitz:
        raise SystemExit("Eroare: Pachetul PyMuPDF ('fitz') nu este instalat. Rulează: pip install pymupdf")

    output_dir = Path(args.output_dir).resolve()
    images_dir = Path(args.images_dir).resolve()

    selected_pages = None
    if args.pages:
        selected_pages = []
        for p in args.pages.split(','):
            if '-' in p:
                s, e = p.split('-', 1)
                selected_pages.extend(range(int(s), int(e) + 1))
            else:
                selected_pages.append(int(p.strip()))

    generated = process_clark(
        pdf_path=pdf_path,
        output_dir=output_dir,
        images_base_dir=images_dir,
        category_filter=args.category,
        page_selection=selected_pages,
        limit=args.limit,
        use_ai=args.ai,
        dry_run=args.dry_run,
        overwrite=args.overwrite
    )

    print(f"\nFinalizat: Au fost generate {len(generated)} protocoale radiografice Markdown din manualul Clark.")


if __name__ == '__main__':
    main()
