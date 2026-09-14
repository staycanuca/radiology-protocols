"""smart_extractor.py — Extracție inteligentă a parametrilor clinici și tehnici din surse.

Analizează textul surselor (locale sau online) conform structurii și șablonului
fiecărei modalități radiologice (Rx, CT, IRM, Eco, Fluoro) și identifică:
- Parametrii tehnici specifici (kV, mAs, DFF/SID, focar, grilă, pitch, secvențe, contrast, etc.)
- Diferențele față de valorile curente din protocolul deschis
- Particularitățile anatomice relevante pentru protocolul curent
"""

from __future__ import annotations

import re
import unicodedata
from typing import Any
import yaml


# Dictionar de sinonime anatomice pentru focalizarea căutării în documente multi-protocol
ANATOMY_SYNONYMS = {
    'toracala': ['toracal', 'dorsal', 'thoracic', 'dorsale', 't-spine', 'coloana toracala', 'coloana dorsala'],
    'cervicala': ['cervical', 'gat', 'c-spine', 'coloana cervicala'],
    'lombara': ['lombar', 'l-spine', 'lombo-sacrata', 'coloana lombara'],
    'torace': ['torace', 'pulmonar', 'plamani', 'chest', 'thorax', 'pleura', 'mediastin'],
    'abdomen': ['abdomen', 'abdominal', 'pelvis', 'pelvin', 'abdomino-pelvin', 'ficat', 'rinichi'],
    'craniu': ['craniu', 'cerebral', 'cap', 'head', 'brain', 'skull', 'neurocraniu'],
    'sinusuri': ['sinusuri', 'saf', 'sinus', 'paranasal'],
    'genunchi': ['genunchi', 'knee'],
    'umar': ['umar', 'shoulder', 'scapulo-humerala'],
    'cot': ['cot', 'elbow'],
    'pumn': ['pumn', 'wrist', 'mana', 'carpiene'],
    'bazin': ['bazin', 'sold', 'coxo-femurala', 'pelvis', 'hip'],
    'glezna': ['glezna', 'ankle', 'picior', 'foot'],
}


def normalize_text(text: str) -> str:
    """Normalizează textul eliminând diacriticele și convertind la litere mici."""
    if not text:
        return ""
    return "".join(
        c for c in unicodedata.normalize("NFKD", str(text)).lower()
        if not unicodedata.combining(c)
    )


def extract_relevant_segment(text: str, protocol_title: str) -> str:
    """Identifică segmentul cel mai relevant din text pentru protocolul specificat.
    
    Dacă documentul conține mai multe protocoale (ex: un ghid complet de radiologie),
    se extrage secțiunea corespunzătoare anatomiei din titlu. Dacă nu se găsește o
    secțiune specifică, se returnează întregul text.
    """
    if not text or not protocol_title:
        return text or ""

    norm_title = normalize_text(protocol_title)
    
    # Găsește cuvintele cheie anatomice relevante
    matched_keywords = []
    for key, syns in ANATOMY_SYNONYMS.items():
        if key in norm_title or any(s in norm_title for s in syns):
            matched_keywords.extend(syns)

    if not matched_keywords:
        return text

    # Caută paragrafe sau secțiuni ce conțin cuvintele cheie
    lines = text.splitlines()
    best_start = -1
    for i, line in enumerate(lines):
        norm_line = normalize_text(line)
        if any(kw in norm_line for kw in matched_keywords):
            # Prioritizează dacă linia pare a fi un titlu / subtitlu
            if len(norm_line) < 80 or norm_line.startswith(('#', '*', '-', '1', '2', '3', '4', '5', 'capitol', 'sectiune')):
                best_start = i
                break

    if best_start >= 0:
        # Extrage o fereastră generoasă în jurul secțiunii găsite (aprox 100 de linii)
        start_idx = max(0, best_start - 5)
        end_idx = min(len(lines), best_start + 120)
        segment = "\n".join(lines[start_idx:end_idx])
        if len(segment.strip()) > 150:
            return segment

    return text


def extract_rx_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii specifici radiografiei convenționale (Rx)."""
    segment = extract_relevant_segment(text, protocol_title)
    norm = normalize_text(segment)
    
    params: dict[str, Any] = {
        'tech_params': {},
    }

    # 1. Tensiune (kV)
    # Căutare particularizată pentru Față vs Profil dacă există
    fata_kv_match = re.search(r'(?:fa[tț][aă]|fata|ap|pa|antero-posterior)[^\n.:;]{0,40}?(?:kv|tensiune)?[^\n.:;]{0,15}?(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:k[Vv]p?)?', segment, re.I)
    profil_kv_match = re.search(r'(?:profil|lat|lateral|ll)[^\n.:;]{0,40}?(?:kv|tensiune)?[^\n.:;]{0,15}?(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:k[Vv]p?)?', segment, re.I)

    if fata_kv_match and profil_kv_match:
        f_val = fata_kv_match.group(1).strip()
        p_val = profil_kv_match.group(1).strip()
        params['tech_params']['kv'] = f"{f_val} (Față); {p_val} (Profil)"
    else:
        # Căutare generală kV
        kv_patterns = [
            r'(?:tensiune|voltage|potential|kvp?|kv)\s*[:=]?\s*(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:k[Vv]p?)?',
            r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*k[Vv]p?\b',
        ]
        for pat in kv_patterns:
            m = re.search(pat, segment, re.I)
            if m:
                val = m.group(1).replace(' ', '')
                # Verifică plauzibilitatea pentru Rx (40 - 150 kV)
                parts = [int(p) for p in re.findall(r'\d+', val)]
                if parts and all(40 <= p <= 150 for p in parts):
                    params['tech_params']['kv'] = f"{val} kV" if 'kv' not in val.lower() else val
                    break

    # 2. Produs curent-timp (mAs)
    mas_patterns = [
        r'(?:sarcina|mas|curent)\s*[:=]?\s*(\d{1,3}(?:\s*[-–—/]\s*\d{1,3})?)\s*(?:m[Aa]s)?',
        r'(\d{1,3}(?:\s*[-–—/]\s*\d{1,3})?)\s*m[Aa]s\b',
    ]
    for pat in mas_patterns:
        m = re.search(pat, segment, re.I)
        if m:
            val = re.sub(r'\s*[-–—/]\s*', ' - ', m.group(1).strip())
            parts = [int(p) for p in re.findall(r'\d+', val)]
            if parts and all(1 <= p <= 400 for p in parts):
                is_aec = bool(re.search(r'\b(?:aec|automat|camera)\b', segment, re.I))
                suffix = " (AEC)" if is_aec else ""
                params['tech_params']['mas'] = f"{val} mAs{suffix}"
                break

    # 3. Distanță focar-film (SID / DFF)
    dff_match = re.search(r'\b(?:dff|sid|distanta\s+focar|distance)\b\s*[:=]?\s*(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:cm|in|inch|\")?', segment, re.I)
    if not dff_match:
        dff_match = re.search(r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*cm\s*(?:dff|sid|\bfocal\b)?', segment, re.I)
    if dff_match:
        dff_val = re.sub(r'\s*[-–—/]\s*', ' - ', dff_match.group(1).strip())
        parts = [int(p) for p in re.findall(r'\d+', dff_val)]
        if parts and all(80 <= p <= 250 for p in parts):
            params['sid_dff'] = f"{dff_val} cm"

    # 4. Focar (mic / mare)
    if re.search(r'\b(?:focar\s+mic|small\s+focus|focal\s+spot\s+small|0\.6\s*mm)\b', segment, re.I):
        params['tech_params']['focal_spot'] = 'Focar Mic'
    elif re.search(r'\b(?:focar\s+mare|large\s+focus|focal\s+spot\s+large|1\.2\s*mm)\b', segment, re.I):
        params['tech_params']['focal_spot'] = 'Focar Mare'
    elif re.search(r'\b(?:focar\s+mic\s+sau\s+mare|mic/mare)\b', segment, re.I):
        params['tech_params']['focal_spot'] = 'Focar Mare sau Mic'

    # 5. Grilă antidifuzoare
    if re.search(r'\b(?:fara\s+grila|without\s+grid|non-grid)\b', segment, re.I):
        params['tech_params']['grid'] = 'Fără grilă antidifuzoare'
    elif re.search(r'\b(?:cu\s+grila|bucky|cu\s+grila\s+antidifuzoare|grid\s+ratio)\b', segment, re.I):
        params['tech_params']['grid'] = 'Cu grilă antidifuzoare Bucky'

    # 6. Filtrare
    filt_match = re.search(r'\b(?:filtrare|filtration)\b\s*[:=]?\s*([≥>=]?\s*\d+(?:\.\d+)?\s*mm\s*Al[^\n.;]*)', segment, re.I)
    if filt_match:
        params['tech_params']['filtration'] = filt_match.group(1).strip()

    # 7. Camere AEC
    aec_match = re.search(r'camer[aă]\s+(central[aă]|lateral[aă]|toate[^\n.;]*)', segment, re.I)
    if aec_match:
        params['tech_params']['aec_chambers'] = f"Camera {aec_match.group(1).strip()} activată"

    # 8. Centrare fascicul
    cent_match = re.search(r'\b(?:punct\s+de\s+centrare|centrare|raza\s+central[aă]|central\s+ray|\bcr\b)\b\s*[:=]?\s*([^\n.;]{6,120})', segment, re.I)
    if cent_match:
        params['centering'] = cent_match.group(1).strip()

    # 9. Poziția pacientului
    pos_match = re.search(r'\b(?:pozi[tț]ie\s+pacient|pozi[tț]ionare|patient\s+position|positioning)\b\s*[:=]?\s*([^\n.;]{6,120})', segment, re.I)
    if pos_match:
        params['position'] = pos_match.group(1).strip()

    # 10. Respirație
    resp_match = re.search(r'\b(?:comand[aă]\s+respiratorie|respira[tț]ie|apnee|breathing|apnea)\b\s*[:=]?\s*([^\n.;]{6,120})', segment, re.I)
    if resp_match:
        params['breathing'] = resp_match.group(1).strip()

    # 11. Protecție radiologică
    prot_matches = re.findall(r'(?:sort\s+de\s+plumb[^\n.;]*|guler\s+tiroidian[^\n.;]*|colimare\s+stransa[^\n.;]*|protectie\s+gonade[^\n.;]*)', segment, re.I)
    if prot_matches:
        params['protection'] = [p.strip().capitalize() for p in prot_matches[:3]]

    # 12. Criterii de calitate
    qual_matches = re.findall(r'(?:vizualizare[^\n.;]{10,80}|includere[^\n.;]{10,80}|fara\s+rotatie[^\n.;]{10,80})', segment, re.I)
    if qual_matches:
        params['quality_criteria'] = [q.strip().capitalize() for q in qual_matches[:4]]

    return params


def extract_ct_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii specifici Computer Tomografiei (CT)."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'tech_params': {},
        'contrast': {},
    }

    # 1. Tensiune tub kV
    kv_patterns = [
        r'(?:tensiune|kvp?|kv)\s*[:=]?\s*(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:k[Vv]p?)?',
        r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*k[Vv]p?\b',
    ]
    for pat in kv_patterns:
        m = re.search(pat, segment, re.I)
        if m:
            val = re.sub(r'\s*[-–—/]\s*', ' - ', m.group(1).strip())
            parts = [int(p) for p in re.findall(r'\d+', val)]
            if parts and all(70 <= p <= 160 for p in parts):
                params['tech_params']['kv'] = val
                break

    # 2. Mod mA / mAs
    mas_match = re.search(r'(?:mas|curent)\s*[:=]?\s*(\d{2,3}\s*[-–—/]\s*\d{2,3}|\d{2,3})\s*m[Aa]s\b', segment, re.I)
    if not mas_match:
        mas_match = re.search(r'(\d{2,3}\s*[-–—/]\s*\d{2,3}|\d{2,3})\s*m[Aa]s\b', segment, re.I)
    if mas_match:
        val = re.sub(r'\s*[-–—/]\s*', ' - ', mas_match.group(1).strip())
        params['tech_params']['mas'] = val
    if re.search(r'\b(?:care\s*dose\s*4d|smart\s*ma|autom[aă]|aec|modulare\s+doza)\b', segment, re.I):
        if 'mas' not in params['tech_params']:
            params['tech_params']['mas'] = 'Auto (AEC)'
        params['tech_params']['aec'] = 'Activat (Modulare automată 3D)'

    # 3. Pitch
    pitch_match = re.search(r'pitch\s*[:=]?\s*(\d+(?:\.\d+)?(?:\s*[-–—/]\s*\d+(?:\.\d+)?)?)', segment, re.I)
    if pitch_match:
        params['tech_params']['pitch'] = re.sub(r'\s*[-–—/]\s*', ' - ', pitch_match.group(1).strip())

    # 4. Grosime slice / reconstrucție
    slice_match = re.search(r'(?:grosime|slice|colimare|collimation)\s*[:=]?\s*([^\n.;]{5,60})', segment, re.I)
    if slice_match:
        params['tech_params']['collimation'] = slice_match.group(1).strip()

    # 5. Timp rotație
    rot_match = re.search(r'(?:timp\s+rota[tț]ie|rotation\s+time)\s*[:=]?\s*(\d+(?:\.\d+)?\s*s)', segment, re.I)
    if rot_match:
        params['tech_params']['rotation_time'] = rot_match.group(1).strip()

    # 6. Substanță de contrast (agent, volum, debit, delay)
    if re.search(r'\b(?:contrast|iodat|iohexol|iopamidol|iomeron|ultravist|omnipaque)\b', segment, re.I):
        params['contrast']['agent'] = 'Substanță de contrast iodată non-ionică (350 - 370 mg I/ml)'
        vol_match = re.search(r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*ml\b', segment, re.I)
        if vol_match:
            params['contrast']['volume'] = f"{vol_match.group(1).strip()} ml"
        flow_match = re.search(r'(\d+(?:\.\d+)?(?:\s*[-–—/]\s*\d+(?:\.\d+)?)?)\s*ml/s', segment, re.I)
        if flow_match:
            params['contrast']['flow_rate'] = f"{flow_match.group(1).strip()} ml/s"
        delay_match = re.search(r'(?:delay|intarziere|arterial|venos|tardiv)\s*[:=]?\s*([^\n.;]{5,60})', segment, re.I)
        if delay_match:
            params['contrast']['timing'] = delay_match.group(1).strip()

    return params


def extract_irm_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii specifici Rezonanței Magnetice (IRM/RMN)."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'coils_hardware': {},
        'sequences': [],
    }

    # Identificare antenă
    coil_match = re.search(r'(?:antena|coil)\s*[:=]?\s*([^\n.;]{5,80})', segment, re.I)
    if coil_match:
        params['coils_hardware']['coil_type'] = coil_match.group(1).strip()

    # Identificare secvențe tipice (T1, T2, FLAIR, DWI, etc.)
    found_seqs = []
    seq_patterns = [
        (r'\bt1\s*(?:se|tse|fse|vibe|mprage)?\s*(?:ax|cor|sag|axial|coronal|sagital)?\b', 'T1'),
        (r'\bt2\s*(?:tse|fse|spair|dixon)?\s*(?:ax|cor|sag|axial|coronal|sagital)?\b', 'T2'),
        (r'\bflair\s*(?:ax|cor|sag)?\b', 'FLAIR'),
        (r'\bstir\s*(?:ax|cor|sag)?\b', 'STIR'),
        (r'\bdwi\s*(?:b0|b1000)?\b', 'DWI (b=0, b=1000) + ADC'),
        (r'\b(?:t2\*|gre|swi)\b', 'T2* / SWI'),
    ]
    for pat, label in seq_patterns:
        if re.search(pat, segment, re.I):
            found_seqs.append({'name': label})

    if found_seqs:
        params['sequences'] = found_seqs

    # Contrast paramagnetic Gadoliniu
    if re.search(r'\b(?:gadoliniu|gadovist|dotarem|clariscan|contrast\s+paramagnetic)\b', segment, re.I):
        params['contrast'] = {
            'agent': 'Contrast paramagnetic pe bază de Gadoliniu',
            'dose': '0.1 mmol/kg (aprox. 0.2 ml/kg)',
        }

    return params


def extract_eco_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii specifici Ecografiei (ECO / Ultrasonografie)."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'transducers_equipment': {},
        'technical_settings': {},
    }

    # Transductor / Frecvență
    freq_match = re.search(r'(\d+(?:\.\d+)?(?:\s*[-–—/]\s*\d+(?:\.\d+)?)?)\s*mhz', segment, re.I)
    if re.search(r'\b(?:convexa|convex)\b', segment, re.I):
        val = f"Sondă convexă ({freq_match.group(1)} MHz)" if freq_match else "Sondă convexă (3.5 - 5.0 MHz)"
        params['transducers_equipment']['transducer_type'] = val
    elif re.search(r'\b(?:liniara|linear)\b', segment, re.I):
        val = f"Sondă liniară ({freq_match.group(1)} MHz)" if freq_match else "Sondă liniară (7.5 - 12.0 MHz)"
        params['transducers_equipment']['transducer_type'] = val

    # Armonică / Doppler
    if re.search(r'\b(?:doppler|color|spectral|pw)\b', segment, re.I):
        params['technical_settings']['doppler'] = 'Mod Doppler Color și Spectral activat'
    if re.search(r'\b(?:thi|armonica|tissue\s+harmonic)\b', segment, re.I):
        params['technical_settings']['harmonic'] = 'Armonică tisulară (THI) activată'

    return params


def extract_fluoro_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii specifici Radioscopiei (Fluoro)."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'fluoro_params': {},
        'contrast': {},
    }

    kv_match = re.search(r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*k[Vv]p?', segment, re.I)
    if kv_match:
        params['fluoro_params']['kv'] = f"{kv_match.group(1).replace(' ', '')} kV"

    if re.search(r'\b(?:bariu|sulfat\s+de\s+bariu|gastrografin)\b', segment, re.I):
        params['contrast']['agent'] = 'Sulfat de bariu sau substanță hidrosolubilă (Gastrografin)'

    return params


def extract_parameters_by_modality(text: str, modality: str, protocol_title: str = "") -> dict[str, Any]:
    """Dispecerizează extragerea către parserul dedicat modalității."""
    mod = modality.lower()
    if mod == 'rx':
        return extract_rx_parameters(text, protocol_title)
    elif mod == 'ct':
        return extract_ct_parameters(text, protocol_title)
    elif mod in ('irm', 'mri'):
        return extract_irm_parameters(text, protocol_title)
    elif mod in ('eco', 'us'):
        return extract_eco_parameters(text, protocol_title)
    elif mod == 'fluoro':
        return extract_fluoro_parameters(text, protocol_title)
    return {}


def diff_parameters(current_fm: dict[str, Any], extracted: dict[str, Any], parent_key: str = "") -> list[dict[str, Any]]:
    """Compară parametrii extrași cu valorile existente din YAML frontmatter."""
    diffs = []
    
    for key, new_val in extracted.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        old_val = current_fm.get(key)
        
        if isinstance(new_val, dict) and isinstance(old_val, dict):
            diffs.extend(diff_parameters(old_val, new_val, full_key))
        elif isinstance(new_val, list):
            # Dacă este listă și old_val este gol sau diferit
            if not old_val or old_val != new_val:
                diffs.append({
                    'field': full_key,
                    'label': full_key.replace('_', ' ').capitalize(),
                    'old_value': old_val or '(gol)',
                    'new_value': new_val,
                    'is_new': not bool(old_val),
                })
        else:
            if new_val and str(new_val).strip() != str(old_val or '').strip():
                diffs.append({
                    'field': full_key,
                    'label': full_key.replace('_', ' ').capitalize(),
                    'old_value': str(old_val or '(gol)'),
                    'new_value': str(new_val),
                    'is_new': not bool(old_val),
                })
                
    return diffs


def apply_extracted_to_frontmatter(fm: dict[str, Any], extracted: dict[str, Any]) -> dict[str, Any]:
    """Aplică recursiv valorile extrase peste dicționarul frontmatter existent."""
    for key, val in extracted.items():
        if isinstance(val, dict):
            if key not in fm or not isinstance(fm[key], dict):
                fm[key] = {}
            apply_extracted_to_frontmatter(fm[key], val)
        elif isinstance(val, list):
            if not fm.get(key):
                fm[key] = val
            elif isinstance(fm[key], list):
                # Fuzionează elementele noi fără duplicate
                for item in val:
                    if item not in fm[key]:
                        fm[key].append(item)
        else:
            if val:
                fm[key] = val
    return fm


def sync_body_parameters(body: str, extracted: dict[str, Any], modality: str) -> str:
    """Actualizează tabelele și listele de parametri din corpul Markdown dacă există."""
    if not body or not extracted:
        return body

    tech = extracted.get('tech_params', {})

    # 1. Tensiune Tub (kV)
    if 'kv' in tech:
        kv_val = str(tech['kv'])
        body = re.sub(
            r'(\|\s*\*\*Tensiune Tub\s*\(kV\)\*\*\s*\|\s*)([^|\n]+)(\|)',
            rf'\g<1> {kv_val} \g<3>',
            body,
            flags=re.I
        )
        body = re.sub(
            r'(\*\*(?:kV|Tensiune Tub|Tensiune)\s*(?:\(kV\))?:\*\*\s*)([^\n]+)',
            rf'\g<1>{kv_val}',
            body,
            flags=re.I
        )

    # 2. Sarcină / mAs
    if 'mas' in tech:
        mas_val = str(tech['mas'])
        body = re.sub(
            r'(\|\s*\*\*(?:Sarcin[aă]\s*/\s*Produs\s*Curent-Timp|mAs)\s*\(mAs\)\*\*\s*\|\s*)([^|\n]+)(\|)',
            rf'\g<1> {mas_val} \g<3>',
            body,
            flags=re.I
        )
        body = re.sub(
            r'(\*\*(?:mAs|Sarcin[aă]|Produs Curent-Timp)\s*(?:\(mAs\))?:\*\*\s*)([^\n]+)',
            rf'\g<1>{mas_val}',
            body,
            flags=re.I
        )

    # 3. Distanță Focar-Film (DFF / SID)
    if 'sid_dff' in extracted:
        sid_val = str(extracted['sid_dff'])
        body = re.sub(
            r'(\|\s*\*\*Distan[tț][aă]\s*Focar-Film\s*\(DFF\s*/\s*SID\)\*\*\s*\|\s*)([^|\n]+)(\|)',
            rf'\g<1> {sid_val} \g<3>',
            body,
            flags=re.I
        )
        body = re.sub(
            r'(\*\*(?:Distan[tț][aă]\s*Focar-Film|DFF\s*/\s*SID|SID)\s*(?:\(DFF\s*/\s*SID\))?:\*\*\s*)([^\n]+)',
            rf'\g<1>{sid_val}',
            body,
            flags=re.I
        )

    # 4. Focar
    if 'focal_spot' in tech:
        foc_val = str(tech['focal_spot'])
        body = re.sub(
            r'(\|\s*\*\*Dimensiune\s*Focar\*\*\s*\|\s*)([^|\n]+)(\|)',
            rf'\g<1> {foc_val} \g<3>',
            body,
            flags=re.I
        )

    # 5. Grilă antidifuzoare
    if 'grid' in tech:
        grid_val = str(tech['grid'])
        body = re.sub(
            r'(\|\s*\*\*Gril[aă]\s*Antidifuzoare[^\*]*\*\*\s*\|\s*)([^|\n]+)(\|)',
            rf'\g<1> {grid_val} \g<3>',
            body,
            flags=re.I
        )

    # 6. Camere AEC
    if 'aec_chambers' in tech:
        aec_val = str(tech['aec_chambers'])
        body = re.sub(
            r'(\|\s*\*\*Camere\s*de\s*Ionizare\s*AEC\*\*\s*\|\s*)([^|\n]+)(\|)',
            rf'\g<1> {aec_val} \g<3>',
            body,
            flags=re.I
        )

    # 7. Poziție pacient
    if 'position' in extracted:
        pos_val = str(extracted['position'])
        body = re.sub(
            r'(\*\*Pozi[tț]ie\s*Pacient:\*\*\s*)([^\n]+)',
            rf'\g<1>{pos_val}',
            body,
            flags=re.I
        )

    # 8. Punct de centrare
    if 'centering' in extracted:
        cent_val = str(extracted['centering'])
        body = re.sub(
            r'(\*\*Punct\s*de\s*Centrare\s*Fascicul:\*\*\s*)([^\n]+)',
            rf'\g<1>{cent_val}',
            body,
            flags=re.I
        )

    # 9. Comandă respiratorie
    if 'breathing' in extracted:
        resp_val = str(extracted['breathing'])
        body = re.sub(
            r'(\*\*Comand[aă]\s*Respiratorie:\*\*\s*)([^\n]+)',
            rf'\g<1>{resp_val}',
            body,
            flags=re.I
        )

    return body


def smart_extract_and_apply(document_text: str, source_text: str, source_title: str = "") -> tuple[str, list[dict[str, Any]]]:
    """Extrage parametrii inteligenți din textul sursei și actualizează documentul protocolului."""
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)(.*)\Z', document_text, re.S)
    if not match:
        return document_text, []

    try:
        fm = yaml.safe_load(match[1])
        if not isinstance(fm, dict):
            return document_text, []
    except Exception:
        return document_text, []

    body = match[2]
    modality = str(fm.get('modality', 'rx')).lower()
    title = str(fm.get('title', ''))

    # 1. Extrage parametrii specifici
    extracted = extract_parameters_by_modality(source_text, modality, title)
    if not extracted:
        return document_text, []

    # 2. Calculează diferențele
    diffs = diff_parameters(fm, extracted)
    if not diffs:
        return document_text, []

    # 3. Aplică parametrii peste frontmatter
    fm = apply_extracted_to_frontmatter(fm, extracted)

    # 4. Sincronizează și tabelele / listele din corpul Markdown
    updated_body = sync_body_parameters(body, extracted, modality)

    # 5. Reconstruiește documentul YAML
    updated_doc = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + updated_body.strip() + '\n'
    return updated_doc, diffs
