#!/usr/bin/env python3
"""extract_bontrager_protocols.py

Extrage protocoale radiografice din manualul:
"Textbook of Radiographic Positioning and Related Anatomy" (Bontrager & Lampignano),
le traduce în limba română folosind terminologie medicală standardizată,
extrage figurile/imaginile radiografice corespunzătoare și generează documentele Markdown
conform șablonului aplicației (render_rx_protocol).

Utilizare:
    python scripts/extract_bontrager_protocols.py --pages 102,104
    python scripts/extract_bontrager_protocols.py --category torace --limit 5
    python scripts/extract_bontrager_protocols.py --category all
    python scripts/extract_bontrager_protocols.py --pages 102 --ai
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Asigură importul render_rx_protocol din scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from render_rx_protocol import render_rx_document
except ImportError:
    render_rx_document = None

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

# Dicționar terminologic medical și radiologic Engleză -> Română
DICTIONARY_TERMS = [
    # Proiecții și poziții
    (r'\bPA PROJECTION\b', 'Incidență Postero-Anterioară (PA)'),
    (r'\bAP PROJECTION\b', 'Incidență Antero-Posterioară (AP)'),
    (r'\bLATERAL POSITION\b', 'Incidență de Profil (Lateral)'),
    (r'\bLATERAL PROJECTION\b', 'Incidență de Profil (Lateral)'),
    (r'\bOBLIQUE POSITION\b', 'Incidență Oblică'),
    (r'\bOBLIQUE PROJECTION\b', 'Incidență Oblică'),
    (r'\bAP AXIAL PROJECTION\b', 'Incidență AP Axială'),
    (r'\bPA AXIAL PROJECTION\b', 'Incidență PA Axială'),
    (r'\bLATERAL DECUBITUS POSITION\b', 'Incidență Decubit Lateral'),
    (r'\bDORSAL DECUBITUS POSITION\b', 'Incidență Decubit Dorsal'),
    (r'\bVENTRAL DECUBITUS POSITION\b', 'Incidență Decubit Ventral'),
    (r'\bAP LORDOTIC PROJECTION\b', 'Incidență Lordotică (AP)'),
    (r'\bTOWNE METHOD\b', 'Incidență AP Axială (Metoda Towne)'),
    (r'\bWATERS METHOD\b', 'Incidență Occipito-Mentonieră (Metoda Waters)'),
    (r'\bCALDWELL METHOD\b', 'Incidență Occipito-Frontală (Metoda Caldwell)'),
    (r'\bSTECHER METHOD\b', 'Incidență Scafoid (Metoda Stecher)'),
    (r'\bFERGUSON METHOD\b', 'Incidență Scolioză / Joncțiune L5-S1 (Metoda Ferguson)'),
    (r'\bOPEN MOUTH PROJECTION\b', 'Incidență Transorală (Gură Deschisă C1-C2)'),

    # Regiuni anatomice
    (r'\bCHEST\b', 'Torace'),
    (r'\bABDOMEN\b', 'Abdomen'),
    (r'\bUPPER AIRWAY\b', 'Căi Aeriene Superioare'),
    (r'\bHAND\b', 'Mână'),
    (r'\bWRIST\b', 'Pumn (Articulație Radiocarpiană)'),
    (r'\bFOREARM\b', 'Antebraț'),
    (r'\bELBOW\b', 'Cot'),
    (r'\bHUMERUS\b', 'Humerus'),
    (r'\bSHOULDER\b', 'Umăr'),
    (r'\bCLAVICLE\b', 'Claviculă'),
    (r'\bSCAPULA\b', 'Omoplat (Scapulă)'),
    (r'\bAC JOINTS\b', 'Articulații Acromioclaviculare'),
    (r'\bFINGERS\b', 'Degete Mână'),
    (r'\bTHUMB\b', 'Police'),
    (r'\bTOES\b', 'Degete Picior'),
    (r'\bFOOT\b', 'Picior'),
    (r'\bCALCANEUS\b', 'Calcaneu'),
    (r'\bANKLE\b', 'Gleznă (Articulație Talocrurală)'),
    (r'\bLOWER LEG\b', 'Gambă'),
    (r'\bKNEE\b', 'Genunchi'),
    (r'\bPATELLA\b', 'Rotulă (Patelă)'),
    (r'\bFEMUR\b', 'Femur'),
    (r'\bPELVIS\b', 'Bazin (Pelvis)'),
    (r'\bPELVIC GIRDLE\b', 'Centură Pelviană'),
    (r'\bHIP\b', 'Șold'),
    (r'\bCERVICAL SPINE\b', 'Coloană Cervicală'),
    (r'\bTHORACIC SPINE\b', 'Coloană Toracală'),
    (r'\bLUMBAR SPINE\b', 'Coloană Lombară'),
    (r'\bSACRUM AND COCCYX\b', 'Sacru și Coccis'),
    (r'\bSACRUM\b', 'Sacru'),
    (r'\bCOCCYX\b', 'Coccis'),
    (r'\bBONY THORAX\b', 'Grilaj Costal și Stern'),
    (r'\bSTERNUM\b', 'Stern'),
    (r'\bRIBS\b', 'Coaste (Grilaj Costal)'),
    (r'\bSKULL\b', 'Craniu'),
    (r'\bCRANIUM\b', 'Craniu'),
    (r'\bFACIAL BONES\b', 'Masiv Facial (Oase ale Feței)'),
    (r'\bPARANASAL SINUSES\b', 'Sinusuri Paranazale (SAF)'),
    (r'\bNASAL BONES\b', 'Oase Proprii Nazale (OPN)'),
    (r'\bORBITS\b', 'Orbite'),
    (r'\bMANDIBLE\b', 'Mandibulă'),
    (r'\bTMJ\b', 'Articulații Temporomandibulare (ATM)'),

    # Proceduri speciale și tract digestiv / urinar
    (r'\bESOPHAGOGRAPHY\b', 'Tranzit Esofagian (Esofagobaritat)'),
    (r'\bUPPER GI SERIES\b', 'Tranzit Baritat Gastro-Duodenal (TBGD)'),
    (r'\bSMALL BOWEL SERIES\b', 'Tranzit Intestinal Baritat'),
    (r'\bBARIUM ENEMA\b', 'Irigografie (Clismă Baritată)'),
    (r'\bINTRAVENOUS \(EXCRETORY\) UROGRAPHY\b', 'Urografie Intravenoasă (UIV)'),
    (r'\bVOIDING - CYSTOURETHROGRAPHY\b', 'Cistouretrografie Micțională'),
    (r'\bCYSTOURETHROGRAPHY\b', 'Cistouretrografie'),
    (r'\bBREAST\b', 'Mamografie (Sân)'),
    (r'\bMAMMOGRAPHY\b', 'Mamografie'),
    (r'\bPOSTVOID\b', 'Post-Micțional'),
    (r'\bURETERIC COMPRESSION\b', 'Compresie Ureterală'),
    (r'\bWEIGHT[\s\-]+BEARING\b', 'În Încărcare (Ortostatism)'),
    (r'\bNON[\s\-]+TRAUMA\b', 'Non-Traumă'),
    (r'\bLAWRENCE METHOD\b', 'Metoda Lawrence'),
    (r'\bCLEMENTS MODIFICATION\b', 'Modificarea Clements'),
    (r'\bROSENBERG METHOD\b', 'Metoda Rosenberg'),
    (r'\bCAMP COVENTRY METHOD\b', 'Metoda Camp-Coventry'),
    (r'\bHOLMBLAD METHOD\b', 'Metoda Holmblad'),
    (r'\bHUGHSTON METHOD\b', 'Metoda Hughston'),
    (r'\bSETTEGAST METHOD\b', 'Metoda Settegast'),
    (r'\bMERCHANT METHOD\b', 'Metoda Merchant'),
    (r'\bNEER METHOD\b', 'Metoda Neer'),
    (r'\bFISK MODIFICATION\b', 'Modificarea Fisk'),
    (r'\bHAAS METHOD\b', 'Metoda Haas'),

    # Tipuri pacient
    (r'\bNON[\s\-]+AMBULATORY PATIENT\b', 'Pacient Nedeplasabil / Cărucior / Targă'),
    (r'\bAMBULATORY PATIENT\b', 'Pacient Mobil / Cooperant (Ortostatism)'),
    (r'\bTRAUMA\b', 'Traumatism / Regim Urgență'),
    (r'\bERECT\b', 'Ortostatism'),
    (r'\bSUPINE\b', 'Decubit Dorsal'),
    (r'\bPRONE\b', 'Decubit Ventral'),
    (r'\bRECUMBENT\b', 'Decubit'),
    (r'\bSEATED\b', 'Poziție Șezândă'),
]

PHRASE_TRANSLATIONS = [
    # Indicații clinice
    (r'pleural effusion', 'revărsat pleural (pleurezie)'),
    (r'pneumothorax', 'pneumotorax'),
    (r'atelectasis', 'atelectazie pulmonară'),
    (r'signs of infection', 'semne de infecție respiratorie (pneumonie, bronhopneumonie)'),
    (r'pulmonary edema', 'edem pulmonar acut / congestie'),
    (r'cardiomegaly', 'cardiomegalie'),
    (r'foreign body', 'prezență corp străin radiopac'),
    (r'fracture(?:s)?', 'suspiciune de fractură'),
    (r'dislocation(?:s)?', 'luxație / subluxație articulară'),
    (r'osteoarthritis', 'artroză / modificări degenerative articulare'),
    (r'osteomyelitis', 'osteomielită / leziuni inflamatorii osoase'),
    (r'bone neoplasm(?:s)?', 'procese proliferative / leziuni tumorale osoase'),
    (r'bowel obstruction', 'ocluzie intestinală (nivele hidroaerice)'),
    (r'ileus', 'ileus dinamic sau mecanic'),
    (r'perforation', 'pneumoperitoneu (perforație organ cavitar)'),
    (r'free air', 'aer liber intraperitoneal'),
    (r'renal calculi', 'litiază renală radiopacă'),
    (r'scoliosis', 'scolioză / vicii de postură ale coloanei'),
    (r'trauma', 'traumatism acut'),

    # Poziționare și tehnică
    (r'Patient erect', 'Pacient în ortostatism'),
    (r'Patient supine', 'Pacient în decubit dorsal'),
    (r'Patient prone', 'Pacient în decubit ventral'),
    (r'Patient seated', 'Pacient în poziție șezândă la capătul mesei'),
    (r'feet spread slightly', 'picioarele ușor depărtate pentru stabilitate'),
    (r'weight equally distributed on both feet', 'greutatea distribuită egal pe ambele picioare'),
    (r'Chin raised, resting against IR', 'Bărbia ridicată și sprijinită pe stativul receptorului'),
    (r'Hands on lower hips', 'Mâinile poziționate pe șolduri'),
    (r'palms out', 'palmele orientate spre exterior'),
    (r'elbows partially flexed', 'coatele parțial flectate'),
    (r'Shoulders rotated forward against IR', 'Umerii rotiți anterior spre receptor pentru degajarea omoplaților'),
    (r'shoulders depressed downward', 'umerii coborâți pentru eliberarea apexurilor pulmonare'),
    (r'Align midsagittal plane with CR', 'Alinierea planului medio-sagital cu raza centrală'),
    (r'Ensure no rotation of thorax', 'Asigurarea lipsei rotației toracelui (simetrie bilaterală)'),
    (r'midcoronal plane parallel to the IR', 'planul medio-coronal paralel cu receptorul de imagine'),
    (r'CR perpendicular to IR', 'Raza centrală (RC) perpendiculară pe receptorul de imagine'),
    (r'CR perpendicular', 'Raza centrală perpendiculară'),
    (r'centered to midsagittal plane at level of T7', 'centrată pe linia medio-sagitală la nivelul vertebrei T7'),
    (r'inferior angle of scapula', 'unghiul inferior al omoplatului (scapulei)'),
    (r'vertebra prominens', 'vertebra proeminentă (apofiza spinoasă C7)'),
    (r'jugular notch', 'incizura jugulară (manubriul sternal)'),
    (r'iliac crest', 'creasta iliacă (corespunzător L4-L5)'),
    (r'greater trochanter', 'marele trohanter'),
    (r'symphysis pubis', 'simfiza pubiană'),
    (r'third MCP joint', 'a treia articulație metacarpofalangiană (MCP 3)'),
    (r'midcarpal area', 'aria medio-carpiană'),
    (r'midshaft', 'treimea medie a diafizei'),

    # Respirație
    (r'Exposure is made at end of second full inspiration', 'Apnee la sfârșitul celui de-al doilea inspir profund complet'),
    (r'Make exposure at end of second full inspiration', 'Apnee în inspir profund complet (după a doua inspirație)'),
    (r'Make the exposure at the end of expiration', 'Apnee la sfârșitul expirului complet (diafragmul ridicat)'),
    (r'Suspended respiration', 'Apnee pe durata expunerii'),
    (r'Shallow breathing technique', 'Respirație superficială lentă pe durata expunerii (tehnică de estompare a coastelor)'),

    # Criterii de calitate
    (r'Both lungs from apices to costophrenic angles', 'Vizualizarea completă a ambelor câmpuri pulmonare, de la apexuri până la unghiurile costodiafragmatice'),
    (r'No rotation', 'Absența rotației anatomice: clavicule echidistante față de linia apofizelor spinoase'),
    (r'Scapulae projected outside lung fields', 'Omoplații proiectați în afara câmpurilor pulmonare'),
    (r'Full inspiration', 'Inspir profund adecvat: minim 9-10 arcuri costale posterioare vizibile'),
    (r'Sharp bony trabecular markings', 'Contururi osoase și travee trabeculare nete, fără artefacte de mișcare'),
    (r'Open joint spaces', 'Spații articulare deschise, vizibile fără suprapuneri'),
]

# Cartografiere capitole -> Categorie protocol aplicație
CHAPTER_CATEGORY_MAP = {
    'chest': 'torace',
    'bony thorax': 'torace',
    'sternum': 'torace',
    'ribs': 'torace',
    'breast': 'torace',
    'mammography': 'torace',
    'abdomen': 'abdomen',
    'biliary': 'abdomen',
    'gastrointestinal': 'abdomen',
    'esophagography': 'abdomen',
    'small bowel': 'abdomen',
    'barium enema': 'abdomen',
    'urinary': 'abdomen',
    'urography': 'abdomen',
    'upper limb': 'membru-superior',
    'forearm': 'membru-superior',
    'humerus': 'membru-superior',
    'shoulder': 'membru-superior',
    'clavicle': 'membru-superior',
    'scapula': 'membru-superior',
    'hand': 'membru-superior',
    'wrist': 'membru-superior',
    'elbow': 'membru-superior',
    'lower limb': 'membru-inferior',
    'femur': 'membru-inferior',
    'pelvic': 'membru-inferior',
    'pelvis': 'membru-inferior',
    'foot': 'membru-inferior',
    'knee': 'membru-inferior',
    'ankle': 'membru-inferior',
    'calcaneus': 'membru-inferior',
    'cervical': 'coloana',
    'thoracic spine': 'coloana',
    'lumbar': 'coloana',
    'sacrum': 'coloana',
    'coccyx': 'coloana',
    'cranium': 'craniu-saf',
    'facial': 'craniu-saf',
    'sinuses': 'craniu-saf',
    'skull': 'craniu-saf',
    'orbits': 'craniu-saf',
    'mandible': 'craniu-saf',
    'pediatric': 'pediatrie',
}


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
    """Transformă un titlu într-un slug compatibil URL și sistem de fișiere."""
    text = remove_diacritics(text.lower().strip())
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text


def clean_text(text: str) -> str:
    """Normalizează caracterele spațiale și diacriticele / ligaturile din textul PDF."""
    if not text:
        return ""
    text = text.replace('\ufb01', 'fi').replace('\ufb02', 'fl')
    # Reunește cuvintele despărțite în silabe la capăt de rând (ex: costo-\nphrenic -> costophrenic)
    text = re.sub(r'(\w+)[-—–]\n(\w+)', r'\1\2', text)
    text = text.replace('•', '\n•')
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()


def translate_text(text: str) -> str:
    """Traduce un fragment de text în română folosind dicționarul integrat."""
    if not text:
        return ""
    translated = text
    for pattern, rep in DICTIONARY_TERMS:
        translated = re.sub(pattern, rep, translated, flags=re.IGNORECASE)
    for pattern, rep in PHRASE_TRANSLATIONS:
        translated = re.sub(pattern, rep, translated, flags=re.IGNORECASE)
    return translated


def parse_page_sections(page_text: str) -> dict:
    """Extrage secțiunile structurate ale paginii de poziționare din Bontrager."""
    lines = [l.strip() for l in page_text.splitlines() if l.strip()]

    # 1. Detectează titlul proiecției și eventualele subtitluri/metode
    title_idx = -1
    for idx, l in enumerate(lines[:12]):
        if any(k in l for k in ['PROJECTION', 'POSITION', 'METHOD']) and not any(k in l for k in ['CHAPTER', 'Chapter', 'RADIOGRAPHIC', 'Principles', 'SUMMARY']):
            title_idx = idx
            break
    if title_idx == -1 and len(lines) > 3:
        title_idx = 3

    title = lines[title_idx] if 0 <= title_idx < len(lines) else ""
    # Dacă linia anterioară se termina cu cratimă (ex: AP WEIGHT-)
    if title_idx > 0 and lines[title_idx - 1].endswith('-'):
        title = lines[title_idx - 1] + title
    # Dacă linia următoare este un subtitlu / metodă specifică (ex: AMBULATORY PATIENT, LAWRENCE METHOD)
    if title_idx + 1 < len(lines):
        next_line = lines[title_idx + 1]
        if not re.match(r'^(?:Clinical Indications|Pathology|Technical|WARninG|Radiation|Shielding)', next_line, re.I):
            if any(k in next_line for k in ['METHOD', 'MODIFICATION', 'PATIENT', 'VIEW', 'PROJECTION', 'POSITION', 'POSTVOID', 'COMPRESSION', 'CALDWELL', 'HAAS', 'WATERS']) or (next_line.isupper() and len(next_line) > 3):
                title = f"{title} - {next_line}"

    # Curățare titlu
    title = re.sub(r'[\u2010-\u2015\u2013\u2014–—]+', ' - ', title)
    title = re.sub(r'\s*-\s*', ' - ', title)
    title = re.sub(r'\bNON\s*-\s*AMBULATORY\b', 'NON-AMBULATORY', title, flags=re.I)
    title = re.sub(r'\bWEIGHT\s*-\s*BEARING\b', 'WEIGHT-BEARING', title, flags=re.I)
    title = re.sub(r'\bNON\s*-\s*TRAUMA\b', 'NON-TRAUMA', title, flags=re.I)
    title = re.sub(r'\s+', ' ', title).strip(' -')

    # 2. Definiție antete secțiuni
    section_patterns = [
        ('indications', r'(?:Clinical Indications|Pathology Demonstrated)'),
        ('tech', r'Technical Factors'),
        ('shielding', r'(?:Shielding|Radiation Protection)'),
        ('patient_pos', r'Patient Position'),
        ('part_pos', r'Part Position'),
        ('cr', r'(?:Central Ray|CR\b)'),
        ('collimation', r'(?:Recommended Collimation|Collimation)'),
        ('respiration', r'(?:Respiration|Breathing)'),
        ('criteria', r'(?:Evaluation Criteria|evaluation Criteria|Anatomy Demonstrated)'),
        ('notes', r'NOTE(?:\s*\d+)?\:?'),
    ]

    sections = {'header': []}
    current_sec = 'header'

    for line in lines:
        matched = False
        for sec_name, pat in section_patterns:
            if re.match(r'^' + pat, line, re.IGNORECASE):
                current_sec = sec_name
                sections[current_sec] = []
                rem = re.sub(r'^' + pat + r'[:\s—–-]*', '', line, flags=re.IGNORECASE).strip()
                if rem:
                    sections[current_sec].append(rem)
                matched = True
                break
        if not matched:
            sections[current_sec].append(line)

    # Colectează conținutul
    result = {'title': title}
    for k, v in sections.items():
        result[k] = clean_text('\n'.join(v))

    return result


def parse_bullets(text: str) -> list[str]:
    """Extrage liniile de tip bullet dintr-un bloc de text."""
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
            if current_item:
                current_item.append(line)
            else:
                current_item.append(line)
    if current_item:
        items.append(' '.join(current_item).strip())
    return [translate_text(it) for it in items if it]


def format_protocol_title(raw_title: str) -> tuple[str, str]:
    """Formatează titlul în stilul aplicației: Rx [Anatomie] [Proiecție] și generează slug-ul."""
    raw = raw_title.replace('—', ' - ').replace('–', ' - ')
    parts = [p.strip() for p in re.split(r'\s+-\s+|:\s*', raw) if p.strip()]

    title_projections = [
        (r'\bPA PROJECTION\b', 'PA (Postero-Anterior)'),
        (r'\bAP PROJECTION\b', 'AP (Antero-Posterior)'),
        (r'\bLATERAL POSITION\b', 'Profil (Lateral)'),
        (r'\bLATERAL PROJECTION\b', 'Profil (Lateral)'),
        (r'\bOBLIQUE POSITION\b', 'Oblică'),
        (r'\bOBLIQUE PROJECTION\b', 'Oblică'),
        (r'\bAP AXIAL PROJECTION\b', 'AP Axială'),
        (r'\bPA AXIAL PROJECTION\b', 'PA Axială'),
        (r'\bAP LORDOTIC PROJECTION\b', 'Lordotică (AP)'),
        (r'\bSUPINE POSITION\b', 'Decubit Dorsal'),
        (r'\bERECT POSITION\b', 'Ortostatism'),
        (r'\bOPEN MOUTH PROJECTION\b', 'Transorală (Gură Deschisă C1-C2)'),
    ]

    def translate_proj(txt):
        res = txt
        for pat, rep in title_projections:
            res = re.sub(pat, rep, res, flags=re.I)
        return translate_text(res)

    if len(parts) == 1:
        title = f"Rx {translate_proj(raw_title)}"
    elif len(parts) == 2:
        if any(k in parts[0].upper() for k in ['PROJECTION', 'POSITION', 'METHOD', 'VIEW']):
            proj_part = translate_proj(parts[0])
            anat_part = translate_text(parts[1])
            title = f"Rx {anat_part} {proj_part}"
        else:
            anat_part = translate_text(parts[0])
            proj_part = translate_proj(parts[1])
            title = f"Rx {anat_part} {proj_part}"
    else:
        proj_part = translate_proj(parts[0])
        anat_part = translate_text(parts[1])
        mod_parts = [translate_text(p) for p in parts[2:] if p.strip()]
        modifier = " - ".join(mod_parts)
        if modifier:
            title = f"Rx {anat_part} {proj_part} ({modifier})"
        else:
            title = f"Rx {anat_part} {proj_part}"

    # Curățare repetiții
    title = re.sub(r'\bRx\s+Rx\b', 'Rx', title)
    title = re.sub(r'\s+', ' ', title).strip()

    slug_base = slugify(remove_diacritics(title))
    if not slug_base.startswith('rx-'):
        slug_base = f"rx-{slug_base}"
    if not slug_base.endswith('-bontrager'):
        slug = f"{slug_base}-bontrager"
    else:
        slug = slug_base
    return title, slug


def parse_tech_factors(text: str) -> tuple[str, dict]:
    """Extrage parametrii de expunere (kV, mAs, SID, grilă, focar)."""
    params = {}

    # SID
    sid = "100 cm"
    cm_m = re.search(r'\((\d+)\s*cm\)', text)
    if cm_m:
        sid = f"{cm_m.group(1)} cm"
    else:
        sid_m = re.search(r'SID[—\-\s:]+([^\n•]+)', text, re.I)
        if sid_m:
            sid_raw = sid_m.group(1).strip()
            cm_m2 = re.search(r'(\d+)\s*cm', sid_raw, re.I)
            if cm_m2:
                sid = f"{cm_m2.group(1)} cm"
            else:
                in_m = re.search(r'(\d+)\s*in', sid_raw, re.I)
                if in_m:
                    sid = f"{round(int(in_m.group(1)) * 2.54)} cm"

    # kVp
    kv_m = re.search(r'kVp(?:\s*range)?[\s:—–\-]+(\d+(?:\s*[–\-]\s*\d+)?)', text, re.I)
    if not kv_m:
        kv_m = re.search(r'(\d+\s*[–\-]\s*\d+)\s*kVp?', text, re.I)
    if kv_m:
        params['kv'] = kv_m.group(1).replace('–', '-').replace('—', '-').strip()
    else:
        params['kv'] = 'DE CONFIGURAT PE APARAT'

    # mAs
    mas_m = re.search(r'mAs[—\-\s:]*(\d+(?:\.\d+)?(?:\s*[–\-]\s*\d+(?:\.\d+)?)?)', text, re.I)
    if mas_m:
        params['mas'] = mas_m.group(1).replace('–', '-').strip()
    else:
        params['mas'] = 'DE CONFIGURAT PE APARAT'

    # Grilă
    if re.search(r'non[\-\s]*grid|without\s+grid', text, re.I):
        params['grid'] = 'Fără grilă (expunere directă)'
    elif re.search(r'\bgrid\b|\bbucky\b', text, re.I):
        params['grid'] = 'Cu grilă antidifuzoare Bucky'
    else:
        params['grid'] = 'Conform grosimii anatomice (> 10 cm cu grilă)'

    # Focar
    try:
        sid_num = int(re.search(r'\d+', sid).group(0))
    except Exception:
        sid_num = 100

    if sid_num >= 150 or ('kv' in params and any(int(x) >= 90 for x in re.findall(r'\d+', str(params['kv'])))):
        params['focal_spot'] = 'Focar Mare (1.0 - 1.2 mm)'
    else:
        params['focal_spot'] = 'Focar Mic (0.6 mm)'

    params['filtration'] = 'Totală ≥ 2.5 mm Al echivalent'
    params['aec_chambers'] = 'Camerele laterale (sau camera centrală funcție de regiune)' if 'Bucky' in params['grid'] else 'DE CONFIGURAT PE APARAT'

    return sid, params


def extract_page_figures(doc: fitz.Document, page_num: int, output_dir: Path, slug: str) -> list[dict]:
    """Extrage imaginile de pe pagina dată din PDF și le salvează în folderul de protocol."""
    page = doc[page_num - 1]
    image_infos = page.get_image_info(xrefs=True)
    text = page.get_text()

    # Căutare linii de titlu pentru figuri (ex. Fig. 2.52 PA chest.)
    fig_captions = [l.strip() for l in text.splitlines() if re.match(r'^Fig(?:ure|\.)\s*\d+\.\d+', l.strip(), re.I)]

    # Filtrează imagini semnificative (ignoră logo-uri/pictograme mici)
    valid_imgs = [info for info in image_infos if info['width'] >= 100 and info['height'] >= 100]
    valid_imgs.sort(key=lambda x: x['bbox'][1])  # sortare de sus în jos

    figures_out = []
    target_img_dir = output_dir / slug
    target_img_dir.mkdir(parents=True, exist_ok=True)

    for idx, info in enumerate(valid_imgs):
        xref = info['xref']
        img_data = doc.extract_image(xref)
        ext = img_data['ext']
        img_bytes = img_data['image']

        filename = f"fig_{idx + 1}.{ext}"
        file_path = target_img_dir / filename
        file_path.write_bytes(img_bytes)

        # Asociere legendă
        raw_cap = fig_captions[idx] if idx < len(fig_captions) else f"Figura {idx + 1}"
        cap_trans = translate_text(raw_cap)
        role = "Poziționare pacient" if idx == 0 else "Aspect radiografic de referință"
        description = f"{role} conform Ghidului Bontrager ({raw_cap})"

        figures_out.append({
            'url': f"assets/images/protocols/bontrager/{slug}/{filename}",
            'caption': cap_trans,
            'description': description
        })

    return figures_out


def clean_multiline(text: str) -> str:
    """Curăță gloanțele, liniile goale și paraziții tipografici dintr-un text continuu."""
    if not text:
        return ""
    # Elimină artefacte izolate de tip dimensiuni casetă (ex. '35\n43\nL')
    cleaned_lines = []
    for l in text.splitlines():
        l_str = l.strip().lstrip('•-* ').strip()
        if not l_str:
            continue
        if re.match(r'^(?:\d+|[RL]|\d+\s+\d+\s+[RL])$', l_str):
            continue
        cleaned_lines.append(l_str)
    res = ' '.join(cleaned_lines)
    return re.sub(r'\s+', ' ', res).strip()


def build_protocol_frontmatter(
    parsed: dict,
    category: str,
    sid: str,
    tech_params: dict,
    figures: list[dict],
    page_num: int,
    protocol_title: str,
    slug: str,
    use_ai: bool = False
) -> dict:
    """Construiește structura YAML frontmatter gata pentru randare."""
    # Poziționare: combină poziția pacientului și poziția piesei anatomice
    patient_p = clean_multiline(parsed.get('patient_pos', ''))
    part_p = clean_multiline(parsed.get('part_pos', ''))
    pos_combined = []
    if patient_p:
        pos_combined.append(f"Pacient: {translate_text(patient_p)}")
    if part_p:
        pos_combined.append(f"Regiune anatomică: {translate_text(part_p)}")
    position_str = "; ".join(pos_combined) if pos_combined else "Conform incidenței standard descrise"

    # Centrare
    cr_raw = clean_multiline(parsed.get('cr', ''))
    centering_str = translate_text(cr_raw) if cr_raw else "Perpendicular pe centrul ariei de interes"

    # Respirație
    resp_raw = clean_multiline(parsed.get('respiration', ''))
    breathing_str = translate_text(resp_raw) if resp_raw else "Apnee pe durata expunerii (sau conform cooperării pacientului)"

    # Colimare
    collim_raw = clean_multiline(parsed.get('collimation', ''))
    if collim_raw:
        tech_params['collimation'] = translate_text(collim_raw)
    else:
        tech_params['collimation'] = "Strictă pe regiunea de interes anatomic"

    # Indicații clinice
    ind_list = parse_bullets(parsed.get('indications', ''))
    if not ind_list:
        ind_list = ["Investigație diagnostică inițială sau de control pentru regiunea anatomică selectată"]

    # Criterii de calitate
    crit_list = parse_bullets(parsed.get('criteria', ''))
    if not crit_list:
        crit_list = [
            "Vizualizarea completă a regiunii anatomice explorate",
            "Absența artefactelor de mișcare sau a suprapunerilor neadecvate",
            "Contrast și penetrare optime pentru decelarea structurilor osoase și a părților moi"
        ]

    # Radioprotecție
    protection_list = [
        "Ecranare gonadică și a organelor radiosensibile conform procedurilor locale de radioprotecție ALARA.",
        "Colimare strictă la aria de interes pentru limitarea radiației difuze.",
        "Verificarea posibilității unei sarcini la pacientele de vârstă fertilă înainte de expunere."
    ]

    # Observații clinice
    notes_raw = clean_multiline(parsed.get('notes', ''))
    notes_str = translate_text(notes_raw) if notes_raw else ""

    fm = {
        'title': protocol_title,
        'slug': slug,
        'category': category,
        'modality': 'rx',
        'author': 'Departamentul de Radiologie / Referință Bontrager',
        'last_updated': '2026-09-15',
        'clinical_indications': ind_list,
        'position': position_str,
        'centering': centering_str,
        'sid_dff': sid,
        'breathing': breathing_str,
        'tech_params': tech_params,
        'quality_criteria': crit_list,
        'protection': protection_list,
        'notes': notes_str,
        'images': figures,
        'sources': [
            {
                'title': f"Bontrager's Textbook of Radiographic Positioning (Ed. 9/10), Pagina {page_num}",
                'url': "https://www.elsevier.com/books/textbook-of-radiographic-positioning-and-related-anatomy/lampignano/978-0-323-65367-1"
            }
        ]
    }

    # Opțional: Îmbunătățire AI cu Antigravity CLI (agy)
    if use_ai and shutil.which('agy'):
        fm = enrich_with_ai(fm)

    return fm


def enrich_with_ai(fm: dict) -> dict:
    """Trimite schița protocolului către Antigravity CLI (agy) pentru a rafina traducerea și contextul medical."""
    prompt = f"""Ești un radiolog expert. Rafinează și adaptează următorul protocol radiografic extras în limba română medicală standard.
Menține structura JSON exactă cu cheile: title, position, centering, breathing, clinical_indications (listă), quality_criteria (listă), notes.
Date de intrare:
{json.dumps(fm, ensure_ascii=False, indent=2)}

Răspunde exclusiv cu obiectul JSON rezultat, fără comentarii suplimentare."""

    try:
        p = subprocess.Popen(
            ['agy', '--input-format', 'text', '--output-format', 'json', '--disable-slash-commands', '--effort', 'low'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8'
        )
        stdout, _ = p.communicate(prompt, timeout=60)
        if p.returncode == 0 and stdout:
            res_obj = json.loads(stdout)
            resp_text = res_obj.get('response', '')
            match = re.search(r'\{.*\}', resp_text, re.DOTALL)
            if match:
                refined = json.loads(match.group(0))
                for key in ['title', 'position', 'centering', 'breathing', 'clinical_indications', 'quality_criteria', 'notes']:
                    if key in refined and refined[key]:
                        fm[key] = refined[key]
    except Exception as exc:
        print(f"  [Avertisment AI] Rafinarea AI a eșuat ({exc}); se folosește traducerea deterministă integrată.")

    return fm


def detect_page_category(doc: fitz.Document, page_num: int) -> str:
    """Detectează categoria radiologică pe baza capitolelor sau a textului din pagină."""
    text = doc[page_num - 1].get_text()[:600].lower()
    for kw, cat in CHAPTER_CATEGORY_MAP.items():
        if kw in text:
            return cat

    # Fallback bazat pe pagina curentă
    if 81 <= page_num <= 114:
        return 'torace'
    elif 115 <= page_num <= 136:
        return 'abdomen'
    elif 137 <= page_num <= 224:
        return 'membru-superior'
    elif 225 <= page_num <= 312:
        return 'membru-inferior'
    elif 313 <= page_num <= 378:
        return 'coloana'
    elif 379 <= page_num <= 398:
        return 'torace'
    elif 399 <= page_num <= 470:
        return 'craniu-saf'
    elif 504 <= page_num <= 590:
        return 'abdomen'
    elif 591 <= page_num <= 640:
        if any(k in text for k in ['spine', 'cervical', 'thoracic', 'lumbar']):
            return 'coloana'
        elif any(k in text for k in ['pelvis', 'femur', 'hip', 'knee']):
            return 'membru-inferior'
        elif any(k in text for k in ['chest', 'thorax']):
            return 'torace'
        elif any(k in text for k in ['shoulder', 'humerus', 'elbow', 'forearm']):
            return 'membru-superior'
        elif any(k in text for k in ['skull', 'cranium', 'facial']):
            return 'craniu-saf'
        return 'torace'
    elif 641 <= page_num <= 674:
        return 'pediatrie'
    elif 780 <= page_num <= 800:
        return 'torace'
    return 'torace'


def find_positioning_pages(doc: fitz.Document) -> list[int]:
    """Scanează întreg documentul și găsește paginile dedicate incidențelor radiografice."""
    positioning_pages = []
    for pno in range(len(doc)):
        text = doc[pno].get_text()
        if 'Technical Factors' in text and ('Clinical Indications' in text or 'Patient Position' in text or 'CR' in text):
            # Exclude pagini pur teoretice
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            has_proj = any('PROJECTION' in l or 'POSITION' in l or 'METHOD' in l for l in lines[:12])
            if has_proj:
                positioning_pages.append(pno + 1)
    return positioning_pages


def process_pages(
    pdf_path: Path,
    pages: list[int],
    output_dir: Path,
    images_base_dir: Path,
    category_filter: str | None = None,
    limit: int | None = None,
    use_ai: bool = False,
    dry_run: bool = False,
    overwrite: bool = True
) -> list[Path]:
    """Extrage, traduce și generează protocoalele Markdown pentru paginile specificate."""
    doc = fitz.open(pdf_path)
    generated_files = []
    count = 0

    print(f"Deschidere manual: {pdf_path.name} ({len(doc)} pagini)")
    print(f"Paginile de analizat: {len(pages)}")

    for page_num in pages:
        if limit and count >= limit:
            break

        cat = detect_page_category(doc, page_num)
        if category_filter and category_filter != 'all' and cat != category_filter:
            continue

        page_text = doc[page_num - 1].get_text()
        parsed = parse_page_sections(page_text)
        if not parsed.get('title'):
            continue

        count += 1
        print(f"\n[{count}] Procesare Pagina {page_num}: {parsed['title']} (Categorie: {cat})")

        # Parametri tehnici
        sid, tech_params = parse_tech_factors(parsed.get('tech', ''))

        # Formatare titlu și slug oficial
        protocol_title, slug = format_protocol_title(parsed['title'])

        # Extragere imagini
        if not dry_run:
            figures = extract_page_figures(doc, page_num, images_base_dir, slug)
            print(f"  -> Extrase {len(figures)} figuri/imagini")
        else:
            figures = []
            print("  -> Dry run: extragere imagini omisă")

        # Construire frontmatter
        fm = build_protocol_frontmatter(
            parsed=parsed,
            category=cat,
            sid=sid,
            tech_params=tech_params,
            figures=figures,
            page_num=page_num,
            protocol_title=protocol_title,
            slug=slug,
            use_ai=use_ai
        )

        # Randare Markdown cu șablonul aplicației
        if render_rx_document:
            markdown_content = render_rx_document(fm)
        else:
            import yaml
            markdown_content = "---\n" + yaml.dump(fm, allow_unicode=True) + "---\n# " + fm['title'] + "\n"

        target_file = output_dir / cat / f"{slug}.md"

        if dry_run:
            print(f"  -> [DRY RUN] Documentul ar fi salvat în: {target_file}")
            print(f"  -> Titlu: {fm['title']}")
            print(f"  -> SID: {fm['sid_dff']} | kV: {fm['tech_params'].get('kv')}")
        else:
            if target_file.exists() and not overwrite:
                print(f"  -> Fișierul {target_file} există deja. Omis (--no-overwrite).")
                continue
            target_file.parent.mkdir(parents=True, exist_ok=True)
            target_file.write_text(markdown_content, encoding='utf-8')
            print(f"  -> Generat cu succes: {target_file}")
            generated_files.append(target_file)

    return generated_files


def main():
    parser = argparse.ArgumentParser(description="Extrage protocoale radiografice din manualul Bontrager în formatul aplicației.")
    parser.add_argument('--pdf', type=str, default='Textbook_of_Radiographic_Positioning_and_Related_Anatomy{John_P.pdf',
                        help='Calea către fișierul PDF al manualului.')
    parser.add_argument('--output-dir', type=str, default='docs/rx',
                        help='Directorul rădăcină pentru salvarea protocoalelor Rx.')
    parser.add_argument('--images-dir', type=str, default='docs/assets/images/protocols/bontrager',
                        help='Directorul rădăcină pentru salvarea imaginilor extrase.')
    parser.add_argument('--category', type=str, default=None,
                        help='Filtrează după categorie: torace, abdomen, coloana, membru-superior, membru-inferior, craniu-saf, pediatrie, sau all.')
    parser.add_argument('--pages', type=str, default=None,
                        help='Listă sau interval de pagini (ex: "102,104" sau "102-110").')
    parser.add_argument('--limit', type=int, default=None,
                        help='Număr maxim de protocoale de generat.')
    parser.add_argument('--ai', action='store_true',
                        help='Activează rafinarea traducerii și a contextului prin Antigravity CLI (agy).')
    parser.add_argument('--dry-run', action='store_true',
                        help='Afișează simularea fără a scrie pe disc.')
    parser.add_argument('--no-overwrite', dest='overwrite', action='store_false',
                        help='Nu suprascrie fișierele deja existente.')

    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.is_file():
        # Căutare în descărcări dacă nu e găsit în directorul curent
        alt_path = Path.home() / 'Downloads' / pdf_path.name
        if alt_path.is_file():
            pdf_path = alt_path
        else:
            raise SystemExit(f"Eroare: Nu s-a găsit fișierul PDF: {args.pdf}")

    if not fitz:
        raise SystemExit("Eroare: Pachetul PyMuPDF ('fitz') nu este instalat. Rulează: pip install pymupdf")

    output_dir = Path(args.output_dir).resolve()
    images_dir = Path(args.images_dir).resolve()

    doc = fitz.open(pdf_path)

    # Determinare pagini țintă
    if args.pages:
        target_pages = []
        parts = args.pages.split(',')
        for p in parts:
            if '-' in p:
                start, end = p.split('-', 1)
                target_pages.extend(range(int(start), int(end) + 1))
            else:
                target_pages.append(int(p.strip()))
    else:
        print("Scanare pagini dedicate poziționării din manual...")
        target_pages = find_positioning_pages(doc)

    print(f"Identificate {len(target_pages)} pagini de poziționare în PDF.")

    generated = process_pages(
        pdf_path=pdf_path,
        pages=target_pages,
        output_dir=output_dir,
        images_base_dir=images_dir,
        category_filter=args.category,
        limit=args.limit,
        use_ai=args.ai,
        dry_run=args.dry_run,
        overwrite=args.overwrite
    )

    print(f"\nFinalizat: Au fost generate {len(generated)} protocoale radiografice Markdown.")


if __name__ == '__main__':
    main()
