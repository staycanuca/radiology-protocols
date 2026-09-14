#!/usr/bin/env python3
"""
enrich_existing_sources.py — Îmbogățirea protocoalelor existente cu surse clinice/tehnice oficiale.

Atribuie automat fiecărui protocol din docs/ sursele de referință corespunzătoare
modalității și categoriei anatomice (EUR 16260, ACR-SPR, AAPM, AIUM, Image Gently, UTSW, OHSU, IAEA).
Populează antetul YAML cu `sources: [...]` și adaugă secțiunea `## Surse și revizuire` în corpul documentului.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import sys
import yaml


SOURCE_CATALOG = {
    # -------------------------------------------------------------------------
    # Radiografie Convențională (Rx)
    # -------------------------------------------------------------------------
    'rx': {
        '_default': [
            {
                'title': 'Comisia Europeană (EUR 16260) — Criterii de calitate în radiodiagnostic',
                'url': 'https://op.europa.eu/en/publication-detail/-/publication/d3d77212-5290-414e-8e37-27fde43b5925',
                'institution': 'Comisia Europeană',
                'source_region': 'UE',
                'kind': 'Ghid european oficial (EUR 16260)',
            },
            {
                'title': 'ACR-SPR Practice Parameter for General Radiography (Digital Radiography)',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/GeneralRad.pdf',
                'institution': 'ACR',
                'source_region': 'US',
                'kind': 'Standard de practică clinică',
            },
            {
                'title': 'Radiopaedia — X-ray Positioning and Projections Reference',
                'url': 'https://radiopaedia.org/articles/x-ray-positioning-and-projections-1',
                'institution': 'Radiopaedia',
                'source_region': 'Internațional',
                'kind': 'Ghid tehnic de poziționare',
            },
        ],
        'pediatrie': [
            {
                'title': 'Image Gently — Pediatric Digital Radiography Protocols',
                'url': 'https://www.imagegently.org/Procedures/Digital-Radiography',
                'institution': 'Image Gently Alliance',
                'source_region': 'US',
                'kind': 'Ghid pediatric de reducere a dozei',
            },
            {
                'title': 'Comisia Europeană (EUR 16260 / EUR 16261) — Criterii de calitate în radiologia pediatrică',
                'url': 'https://op.europa.eu/en/publication-detail/-/publication/d3d77212-5290-414e-8e37-27fde43b5925',
                'institution': 'Comisia Europeană',
                'source_region': 'UE',
                'kind': 'Ghid european oficial',
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Computer Tomograf (CT)
    # -------------------------------------------------------------------------
    'ct': {
        '_default': [
            {
                'title': 'AAPM — Working Group on Standardization of CT Nomenclature and Protocols',
                'url': 'https://www.aapm.org/pubs/ctprotocols/',
                'institution': 'AAPM',
                'source_region': 'US',
                'kind': 'Protocol / resursă tehnică CT',
            },
            {
                'title': 'UT Southwestern Radiology — CT Clinical Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'chest': [
            {
                'title': 'AAPM CT Protocols — Routine Adult Chest CT',
                'url': 'https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf',
                'institution': 'AAPM',
                'source_region': 'US',
                'kind': 'Protocol tehnic standardizat',
            },
            {
                'title': 'UT Southwestern Radiology — CT Chest Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'abdomen': [
            {
                'title': 'AAPM CT Protocols — Adult Abdomen/Pelvis CT',
                'url': 'https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf',
                'institution': 'AAPM',
                'source_region': 'US',
                'kind': 'Protocol tehnic standardizat',
            },
            {
                'title': 'UT Southwestern Radiology — CT Abdomen & Pelvis Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'neuro': [
            {
                'title': 'AAPM CT Protocols — Adult Routine Head CT',
                'url': 'https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf',
                'institution': 'AAPM',
                'source_region': 'US',
                'kind': 'Protocol tehnic standardizat',
            },
            {
                'title': 'UT Southwestern Radiology — CT Neuro / Head Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'cardiac': [
            {
                'title': 'SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf',
                'institution': 'ACR / SCCT',
                'source_region': 'US',
                'kind': 'Standard de practică cardiovasculară',
            },
            {
                'title': 'UT Southwestern Radiology — Cardiovascular CT Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'vascular': [
            {
                'title': 'ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf',
                'institution': 'ACR / NASCI / SIR',
                'source_region': 'US',
                'kind': 'Standard de practică angio-CT',
            },
            {
                'title': 'UT Southwestern Radiology — CTA & Vascular CT Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'trauma': [
            {
                'title': 'ACR Appropriateness Criteria — Major Blunt Trauma',
                'url': 'https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria',
                'institution': 'ACR',
                'source_region': 'US',
                'kind': 'Criterii de oportunitate clinică',
            },
            {
                'title': 'UT Southwestern Radiology — Trauma Whole-Body CT Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'msk': [
            {
                'title': 'ACR-SSR Practice Parameter for Musculoskeletal CT',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf',
                'institution': 'ACR / SSR',
                'source_region': 'US',
                'kind': 'Standard de practică MSK',
            },
            {
                'title': 'UT Southwestern Radiology — Musculoskeletal CT Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional',
            },
        ],
        'pediatrie': [
            {
                'title': 'Image Gently — Pediatric CT Protocols & Radiation Safety',
                'url': 'https://www.imagegently.org/Procedures/Computed-Tomography',
                'institution': 'Image Gently Alliance',
                'source_region': 'US',
                'kind': 'Ghid pediatric de reducere a dozei CT',
            },
            {
                'title': 'AAPM — Pediatric CT Protocols',
                'url': 'https://www.aapm.org/pubs/ctprotocols/',
                'institution': 'AAPM',
                'source_region': 'US',
                'kind': 'Protocol tehnic pediatric',
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Rezonanță Magnetică (IRM)
    # -------------------------------------------------------------------------
    'irm': {
        '_default': [
            {
                'title': 'OHSU Diagnostic Radiology — MRI Protocols',
                'url': 'https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols',
                'institution': 'OHSU',
                'source_region': 'US',
                'kind': 'Protocol instituțional IRM',
            },
            {
                'title': 'UT Southwestern Radiology — Magnetic Resonance Imaging Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional IRM',
            },
            {
                'title': 'ACR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI)',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Perf.pdf',
                'institution': 'ACR',
                'source_region': 'US',
                'kind': 'Standard de practică IRM',
            },
        ],
        'neuro': [
            {
                'title': 'OHSU Diagnostic Radiology — Brain & Spine MRI Protocols',
                'url': 'https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols',
                'institution': 'OHSU',
                'source_region': 'US',
                'kind': 'Protocol instituțional IRM',
            },
            {
                'title': 'ACR-ASNR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Brain',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Brain.pdf',
                'institution': 'ACR / ASNR',
                'source_region': 'US',
                'kind': 'Standard de practică IRM',
            },
        ],
        'msk': [
            {
                'title': 'OHSU Diagnostic Radiology — Musculoskeletal MRI Protocols',
                'url': 'https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols',
                'institution': 'OHSU',
                'source_region': 'US',
                'kind': 'Protocol instituțional IRM',
            },
            {
                'title': 'ACR-SSR Practice Parameter for the Performance of Musculoskeletal Magnetic Resonance Imaging',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Musculoskeletal.pdf',
                'institution': 'ACR / SSR',
                'source_region': 'US',
                'kind': 'Standard de practică IRM',
            },
        ],
        'abdomen-pelvis': [
            {
                'title': 'UT Southwestern Radiology — Abdomen & Pelvis MRI Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional IRM',
            },
            {
                'title': 'ACR-SAR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Abdomen and Pelvis',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Abd-Pel.pdf',
                'institution': 'ACR / SAR',
                'source_region': 'US',
                'kind': 'Standard de practică IRM',
            },
        ],
        'cardiac': [
            {
                'title': 'SCMR / ACR-NASCI Practice Parameter for the Performance of Cardiac Magnetic Resonance Imaging',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CMR.pdf',
                'institution': 'ACR / SCMR',
                'source_region': 'US',
                'kind': 'Standard de practică IRM cardiovascular',
            },
            {
                'title': 'UT Southwestern Radiology — Cardiac MR Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional IRM',
            },
        ],
        'san': [
            {
                'title': 'ACR-SBI Practice Parameter for the Performance of Contrast-Enhanced Magnetic Resonance Imaging (MRI) of the Breast',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/mr-breast.pdf',
                'institution': 'ACR / SBI',
                'source_region': 'US',
                'kind': 'Standard de practică IRM mamar',
            },
            {
                'title': 'UT Southwestern Radiology — Breast MRI Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional IRM',
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Ecografie (ECO)
    # -------------------------------------------------------------------------
    'eco': {
        '_default': [
            {
                'title': 'AIUM Practice Parameters — Clinical Ultrasound Practice Guidelines',
                'url': 'https://www.aium.org/resources/practice-parameters',
                'institution': 'AIUM',
                'source_region': 'US',
                'kind': 'Parametru de practică US',
            },
            {
                'title': 'UT Southwestern Radiology — Ultrasound Clinical Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/us.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional US',
            },
            {
                'title': 'ACR Practice Parameter for the Performance of Diagnostic Ultrasound',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/US-Perf.pdf',
                'institution': 'ACR',
                'source_region': 'US',
                'kind': 'Standard de practică ecografică',
            },
        ],
        'abdomen-pelvis': [
            {
                'title': 'AIUM Practice Parameter for the Performance of an Ultrasound Examination of the Abdomen and/or Retroperitoneum',
                'url': 'https://www.aium.org/resources/practice-parameters',
                'institution': 'AIUM',
                'source_region': 'US',
                'kind': 'Parametru de practică US abdomen',
            },
            {
                'title': 'UT Southwestern Radiology — Abdominal Ultrasound Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/us.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional US',
            },
        ],
        'vascular-doppler': [
            {
                'title': 'AIUM-ACR-SRU Practice Parameter for the Performance of Peripheral Arterial and Venous Ultrasound',
                'url': 'https://www.aium.org/resources/practice-parameters',
                'institution': 'AIUM / ACR / SRU',
                'source_region': 'US',
                'kind': 'Parametru de practică Doppler vascular',
            },
            {
                'title': 'UT Southwestern Radiology — Vascular Doppler Ultrasound Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/us.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional US',
            },
        ],
        'msk': [
            {
                'title': 'AIUM-ACR-SPR-SRU Practice Parameter for the Performance of a Musculoskeletal Ultrasound Examination',
                'url': 'https://www.aium.org/resources/practice-parameters',
                'institution': 'AIUM / ACR',
                'source_region': 'US',
                'kind': 'Parametru de practică US musculoscheletic',
            },
            {
                'title': 'UT Southwestern Radiology — Musculoskeletal Ultrasound Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/us.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional US',
            },
        ],
        'parti-moi-endocrin': [
            {
                'title': 'AIUM Practice Parameter for the Performance of a Thyroid and Neck Ultrasound Examination',
                'url': 'https://www.aium.org/resources/practice-parameters',
                'institution': 'AIUM',
                'source_region': 'US',
                'kind': 'Parametru de practică US tiroidă și părți moi',
            },
            {
                'title': 'UT Southwestern Radiology — Thyroid and Soft Tissue Ultrasound',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/us.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional US',
            },
        ],
        'san': [
            {
                'title': 'AIUM-ACR Practice Parameter for the Performance of a Breast Ultrasound Examination',
                'url': 'https://www.aium.org/resources/practice-parameters',
                'institution': 'AIUM / ACR',
                'source_region': 'US',
                'kind': 'Parametru de practică ecografie mamară',
            },
            {
                'title': 'UT Southwestern Radiology — Breast Ultrasound Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/us.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional US',
            },
        ],
        'pediatrie': [
            {
                'title': 'AIUM-ACR-SPR Practice Parameter for the Performance of Pediatric Ultrasound Examinations',
                'url': 'https://www.aium.org/resources/practice-parameters',
                'institution': 'AIUM / ACR / SPR',
                'source_region': 'US',
                'kind': 'Parametru de practică ecografie pediatrică',
            },
            {
                'title': 'UT Southwestern Radiology — Pediatric Ultrasound Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/us.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional US',
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Fluoroscopie (Fluoro)
    # -------------------------------------------------------------------------
    'fluoro': {
        '_default': [
            {
                'title': 'ACR-SPR Practice Parameter for the Performance of Fluoroscopy',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf',
                'institution': 'ACR / SPR',
                'source_region': 'US',
                'kind': 'Standard de practică fluoroscopică',
            },
            {
                'title': 'UT Southwestern Radiology — Diagnostic Fluoroscopy Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/diagnostic.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional fluoroscopie',
            },
        ],
        'digestiv': [
            {
                'title': 'ACR-SAR-SPR Practice Parameter for the Performance of Gastrointestinal Fluoroscopy in Adults',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf',
                'institution': 'ACR / SAR / SPR',
                'source_region': 'US',
                'kind': 'Standard de practică fluoroscopie digestivă',
            },
            {
                'title': 'UT Southwestern Radiology — Diagnostic Fluoroscopy Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/diagnostic.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional fluoroscopie',
            },
        ],
        'urinar': [
            {
                'title': 'ACR-SPR Practice Parameter for the Performance of Voiding Cystourethrography and Urogenital Fluoroscopy',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf',
                'institution': 'ACR / SPR',
                'source_region': 'US',
                'kind': 'Standard de practică fluoroscopie urinară',
            },
            {
                'title': 'UT Southwestern Radiology — Urogenital Diagnostic Fluoroscopy Protocols',
                'url': 'https://www.utsouthwestern.edu/departments/radiology/protocols/diagnostic.html',
                'institution': 'UT Southwestern',
                'source_region': 'US',
                'kind': 'Protocol instituțional fluoroscopie',
            },
        ],
        'c-arm': [
            {
                'title': 'ACR-AAPM Technical Standard for Management of the Fluoroscopic Step in Interventional Procedures (C-Arm)',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf',
                'institution': 'ACR / AAPM',
                'source_region': 'US',
                'kind': 'Standard tehnic fluoroscopie C-Arm',
            },
            {
                'title': 'IAEA — Radiation Protection in Fluoroscopically Guided Procedures',
                'url': 'https://www.iaea.org/resources/rpop/health-professionals/radiology/fluoroscopy',
                'institution': 'IAEA',
                'source_region': 'Internațional',
                'kind': 'Standard internațional de radioprotecție',
            },
        ],
        'pediatrie': [
            {
                'title': 'Image Gently — Pediatric Fluoroscopy Protocols & Radiation Safety',
                'url': 'https://www.imagegently.org/Procedures/Fluoroscopy',
                'institution': 'Image Gently Alliance',
                'source_region': 'US',
                'kind': 'Ghid pediatric de reducere a dozei fluoroscopie',
            },
            {
                'title': 'ACR-SPR Practice Parameter for the Performance of Pediatric Fluoroscopy',
                'url': 'https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf',
                'institution': 'ACR / SPR',
                'source_region': 'US',
                'kind': 'Standard de practică fluoroscopie pediatrică',
            },
        ],
    },
}


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extrage (frontmatter, body) dintr-un fișier Markdown delimitat prin ---."""
    if not content.startswith('---\n'):
        return {}, content
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 5:]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def get_sources_for_protocol(modality: str, category: str, slug: str, title: str, timestamp: str) -> list[dict]:
    """Selectează sursele oficiale relevante pentru protocol pe baza modalității și anatomiei."""
    mod_cat = SOURCE_CATALOG.get(modality, {})

    # Detectare pediatrie trans-categorii
    is_pediatric = (
        category == 'pediatrie'
        or 'pediatric' in slug.lower()
        or 'sugari' in slug.lower()
        or 'copil' in slug.lower()
        or 'pediatric' in title.lower()
    )

    if is_pediatric and 'pediatrie' in mod_cat:
        selected = mod_cat['pediatrie']
    elif category in mod_cat:
        selected = mod_cat[category]
    elif '_default' in mod_cat:
        selected = mod_cat['_default']
    else:
        selected = SOURCE_CATALOG['ct']['_default']

    sources = []
    for s in selected:
        url = s['url']
        sha256 = hashlib.sha256(url.encode('utf-8')).hexdigest()
        sources.append({
            'title': s['title'],
            'url': url,
            'institution': s.get('institution', ''),
            'source_region': s.get('source_region', 'Internațional'),
            'kind': s.get('kind', 'Standard / Ghid de referință'),
            'checked_at': timestamp,
            'sha256': sha256,
        })
    return sources


def build_references_section(sources: list[dict]) -> str:
    """Generează secțiunea Markdown curată pentru bibliografie."""
    lines = ['\n\n## Surse și revizuire\n']
    for s in sources:
        title = s['title']
        url = s['url']
        inst = s.get('institution') or s.get('kind') or ''
        region = s.get('source_region', '')
        extra = f" — *{inst}* ({region})" if inst and region else (f" — *{inst}*" if inst else "")
        lines.append(f"- [{title}]({url}){extra}")
    return '\n'.join(lines) + '\n'


def enrich_protocol_file(file_path: Path, timestamp: str, force: bool = False, dry_run: bool = False) -> dict:
    """Îmbogățește un fișier individual de protocol."""
    content = file_path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)

    if not fm:
        return {'status': 'skipped', 'reason': 'Lipsă antet YAML'}

    existing_sources = fm.get('sources')
    if existing_sources and not force:
        return {'status': 'skipped', 'reason': 'Are deja surse configurate'}

    modality = fm.get('modality') or file_path.parent.parent.name
    category = fm.get('category') or file_path.parent.name
    slug = fm.get('slug') or file_path.stem
    title = fm.get('title') or slug

    sources = get_sources_for_protocol(modality, category, slug, title, timestamp)
    fm['sources'] = sources

    # Normalizare metadate obligatorii (autor și poziție) dacă lipsesc
    if not fm.get('author') or not str(fm['author']).strip():
        fm['author'] = 'Departamentul de Radiologie'

    if not fm.get('position') or not str(fm['position']).strip():
        coils_pos = fm.get('coils_hardware', {}).get('positioning') if isinstance(fm.get('coils_hardware'), dict) else None
        eq_pos = fm.get('positioning_equipment', {}).get('patient_position') if isinstance(fm.get('positioning_equipment'), dict) else None
        if coils_pos:
            fm['position'] = coils_pos
        elif eq_pos:
            fm['position'] = eq_pos
        elif fm.get('patient_prep') and isinstance(fm['patient_prep'], str):
            fm['position'] = 'Decubit dorsal adaptat ferestrei acustice / pregătire: ' + fm['patient_prep'][:80]
        else:
            fm['position'] = 'Decubit dorsal conform procedurii standard'

    # Curățare corp existent dacă conținea deja o secțiune anterioară de surse
    clean_body = re.split(r'\n## Surse și revizuire', body)[0].rstrip()
    references_md = build_references_section(sources)
    new_body = clean_body + references_md

    # Serializare curată YAML
    new_doc = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + new_body.lstrip('\n')

    if not dry_run:
        file_path.write_text(new_doc, encoding='utf-8')

    return {
        'status': 'updated',
        'modality': modality,
        'category': category,
        'slug': slug,
        'sources_count': len(sources),
    }


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

    parser = argparse.ArgumentParser(description='Enrich existing protocols with authoritative sources.')
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1],
                        help='Calea către rădăcina proiectului.')
    parser.add_argument('--modality', choices=['ct', 'rx', 'irm', 'eco', 'fluoro', 'all'], default='all',
                        help='Modalitatea de procesat (implicit: all).')
    parser.add_argument('--force', action='store_true',
                        help='Suprascrie sursele existente chiar dacă sunt deja populate.')
    parser.add_argument('--dry-run', action='store_true',
                        help='Simulează fără modificarea fișierelor pe disc.')
    args = parser.parse_args()

    docs_dir = args.repo / 'docs'
    if not docs_dir.exists():
        print(f"Eroare: Directorul docs nu a fost găsit la {docs_dir}", file=sys.stderr)
        sys.exit(1)

    now_iso = datetime.now(timezone.utc).isoformat()
    files = sorted([
        p for p in docs_dir.glob('*/*/*.md')
        if p.name not in ('index.md', 'compare.md')
    ])

    updated_count = 0
    skipped_count = 0
    stats_by_modality: dict[str, int] = {}

    for file_path in files:
        rel = file_path.relative_to(docs_dir)
        mod = rel.parts[0]
        if args.modality != 'all' and mod != args.modality:
            continue

        res = enrich_protocol_file(file_path, now_iso, force=args.force, dry_run=args.dry_run)
        if res['status'] == 'updated':
            updated_count += 1
            stats_by_modality[mod] = stats_by_modality.get(mod, 0) + 1
        else:
            skipped_count += 1

    mode_str = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode_str}Procesare finalizată.")
    print(f"  Protocoale actualizate: {updated_count}")
    print(f"  Protocoale omise: {skipped_count}")
    print("  Defalcare pe modalități:")
    for mod, count in sorted(stats_by_modality.items()):
        print(f"    - {mod.upper()}: {count}")


if __name__ == '__main__':
    main()
