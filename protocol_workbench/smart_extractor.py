"""smart_extractor.py — Extracție inteligentă a parametrilor clinici și tehnici din surse.

Analizează textul surselor (locale sau online) conform structurii și șablonului
fiecărei modalități radiologice (Rx, CT, IRM, Eco, Fluoro) și identifică:
- Indicații clinice relevante
- Pregătire pacient, repaus alimentar (NPO), premedicație
- Substanțe de contrast (agent, volum/doză, debit, temporizare, ROI, trigger, cale de administrare)
- Poziționare pacient, centrare fascicul, antene/transductori/echipament
- Parametri tehnici specifici (kV, mAs, DFF/SID, focar, grilă, pitch, timp rotație, THI, LIH, etc.)
- Secvențe RM, serii CT, reconstrucții, incidențe ecografice standard, pași de fluoroscopie
- Criterii de calitate a imaginii
- Siguranță clinică, contraindicații și radioprotecție (ALARA)
- Sincronizează ambele niveluri: YAML Frontmatter și corpul Markdown
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
        start_idx = max(0, best_start - 5)
        end_idx = min(len(lines), best_start + 140)
        segment = "\n".join(lines[start_idx:end_idx])
        if len(segment.strip()) > 150:
            return segment

    return text


def _clean_bullet_text(item: str) -> str:
    """Curăță un element de tip listă de marcatori și spații inutile."""
    cleaned = re.sub(r'^[ \t]*[-*•\d.)\]]+[ \t]*', '', item).strip()
    cleaned = re.sub(r'[;.]+$', '', cleaned).strip()
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned


def extract_section_bullets(segment: str, header_regex: str, max_items: int = 8) -> list[str]:
    """Extrage elementele de tip listă asociate unui subtitlu sau antet dintr-un segment de text."""
    pattern = rf'(?:{header_regex})\s*[:\n]\s*([^\n]+(?:\n(?:[ \t]*[-*•\d.)][^\n]+|[^\n:]{{10,120}}))*)'
    match = re.search(pattern, segment, re.I)
    if not match:
        return []

    block = match.group(1).strip()
    lines = block.splitlines()
    items: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Dacă linia conține alt header cu două puncte la final, oprește
        if re.match(r'^[A-ZȘȚÎÂĂa-zșțîâă\s]{3,35}\s*:', stripped) and not stripped.startswith(('-', '*', '•')):
            break

        # Verifică dacă linia are marcator de listă
        if re.match(r'^[ \t]*[-*•\d.)]', line):
            cleaned = _clean_bullet_text(line)
            if len(cleaned) >= 5 and cleaned not in items:
                items.append(cleaned)
        elif not items and (';' in stripped or ',' in stripped):
            # Dacă este o enumerare pe o singură linie separată prin punct și virgulă
            subparts = re.split(r'[;,]', stripped)
            for sp in subparts:
                cl = _clean_bullet_text(sp)
                if len(cl) >= 5 and cl not in items:
                    items.append(cl)
        elif len(stripped) >= 10 and not items:
            cleaned = _clean_bullet_text(stripped)
            if cleaned and cleaned not in items:
                items.append(cleaned)

        if len(items) >= max_items:
            break

    return items[:max_items]


def extract_clinical_indications(segment: str) -> list[str]:
    """Extrage indicațiile clinice din textul sursei."""
    header_regex = r'(?:indica[tț]ii(?:\s+clinice)?|diagnostic|patolog(?:ie|ii)|clinical\s+indications?|indications?|scopul\s+examin[aă]rii)'
    bullets = extract_section_bullets(segment, header_regex, max_items=6)
    if bullets:
        return bullets

    # Căutare contextuală dacă nu există o listă formală
    fallback_items = []
    susp_matches = re.findall(r'\b(?:suspiciune\s+(?:de\s+)?[^\n,.;]{5,60}|evaluare\s+(?:a\s+)?[^\n,.;]{5,60}|durere\s+[^\n,.;]{5,50}|traumatism\s+[^\n,.;]{5,50})', segment, re.I)
    for m in susp_matches:
        cl = _clean_bullet_text(m)
        if len(cl) >= 8 and cl not in fallback_items:
            fallback_items.append(cl)
        if len(fallback_items) >= 4:
            break

    return fallback_items


def extract_contraindications(segment: str, modality: str) -> list[str]:
    """Extrage contraindicațiile și screeningul de securitate adaptat modalității."""
    header_regex = r'(?:contraindica[tț]ii(?:\s+(?:absolute|relative|specifice|rm))?|contraindications?|screening\s+securitate)'
    bullets = extract_section_bullets(segment, header_regex, max_items=5)
    if bullets:
        return bullets

    found: list[str] = []
    mod = modality.lower()
    
    if mod in ('irm', 'mri'):
        if re.search(r'\b(?:pacemaker|defibrilator|stimulator\s+cardiac)\b', segment, re.I):
            found.append('Pacemaker cardiac sau defibrilator implantabil non-RM condițional')
        if re.search(r'\b(?:clip(?:uri)?\s+anevrismal|clips\s+feromagnetic)\b', segment, re.I):
            found.append('Clipsuri anevrismale intracraniene feromagnetice')
        if re.search(r'\b(?:corp(?:i)?\s+str[aă]in(?:i)?\s+intraocular|metal\s+ocular)\b', segment, re.I):
            found.append('Corpi străini metalici intraoculari sau intraorbitari')
        if re.search(r'\b(?:neurostimulator|pomp[aă]\s+insulin[aă]|implant\s+cohlear)\b', segment, re.I):
            found.append('Implanturi active (neurostimulatoare, pompe de perfuzie, implant cohlear)')
        if re.search(r'\b(?:claustrofobie|claustrophobia)\b', segment, re.I):
            found.append('Claustrofobie severă (necesită sedare sau pregătire anxiolitică)')
    elif mod == 'fluoro':
        if re.search(r'\b(?:perfora[tț]ie|fistul[aă]|suspiciune\s+de\s+perfora[tț]ie)\b', segment, re.I):
            found.append('Suspiciune certă de perforație de tub digestiv (contraindicație absolută pentru Bariu - se va utiliza contrast hidrosolubil non-ionic)')
        if re.search(r'\b(?:sarcin[aă]|pregnant|gravid[aă])\b', segment, re.I):
            found.append('Sarcină confirmată (contraindicație relativă / expunere strict la indicație vitală)')
    elif mod in ('eco', 'us'):
        if re.search(r'\b(?:meteorism|gaze\s+intestinale)\b', segment, re.I):
            found.append('Interpoziție masivă gazoasă digestivă ce limitează fereastra acustică')
        if re.search(r'\b(?:pansamente|arsuri|leziuni\s+cutanate)\b', segment, re.I):
            found.append('Pansamente ocluzive sau leziuni cutanate extinse în aria de scanare')
    elif mod == 'ct':
        if re.search(r'\b(?:alergie\s+sever[aă]|anafilax(?:ie|ie)|reactie\s+la\s+contrast)\b', segment, re.I):
            found.append('Reacție alergică severă prealabilă la substanța de contrast iodată')

    return found


def extract_quality_criteria(segment: str, modality: str) -> list[str]:
    """Extrage criteriile de calitate și reușită a imaginii."""
    header_regex = r'(?:criterii\s+(?:de\s+)?calitate(?:\s+[sș]i\s+reu[sș]it[aă])?|calitatea\s+imaginii|image\s+quality|quality\s+criteria)'
    bullets = extract_section_bullets(segment, header_regex, max_items=5)
    if bullets:
        return bullets

    # Căutare după expresii tipice de calitate
    qual_matches = re.findall(r'\b(?:vizualizare[^\n.;]{10,90}|includere[^\n.;]{10,90}|f[aă]r[aă]\s+rotatie[^\n.;]{10,90}|absen[tț]a\s+artefactelor[^\n.;]{10,90}|rezolu[tț]ie\s+[^\n.;]{10,90})', segment, re.I)
    items = []
    for q in qual_matches:
        cl = _clean_bullet_text(q)
        if len(cl) >= 12 and cl not in items:
            items.append(cl)
        if len(items) >= 4:
            break
    return items


def extract_patient_prep(segment: str, modality: str) -> dict[str, Any]:
    """Extrage instrucțiunile de pregătire a pacientului (NPO, dietă, hidratare, premedicație)."""
    prep_data: dict[str, Any] = {}
    
    # Repaus alimentar / NPO
    npo_match = re.search(r'\b(?:repaus\s+alimentar|npo|[aà]\s+jeun|fasting|nemancat)\b\s*[:=]?\s*([^\n.;]{4,70})', segment, re.I)
    if npo_match:
        val = npo_match.group(1).strip()
        if not re.search(r'repaus\s+alimentar|[aà]\s+jeun', val, re.I):
            prep_data['npo'] = f"Repaus alimentar {val}"
        else:
            prep_data['npo'] = val[0].upper() + val[1:]

    # Premedicație / hidratare
    premed_match = re.search(r'\b(?:premedica[tț]ie|hidratare|contrast\s+oral)\b\s*[:=]?\s*([^\n.;]{6,100})', segment, re.I)
    if premed_match:
        prep_data['premedication'] = premed_match.group(1).strip()

    # Pregătire generală
    gen_prep_match = re.search(r'\b(?:preg[aă]tire\s+pacient|preg[aă]tirea?\s+prealabil[aă]|patient\s+preparation)\b\s*[:=]?\s*([^\n.]{8,150})', segment, re.I)
    if gen_prep_match:
        prep_data['patient_prep'] = gen_prep_match.group(1).strip()
    elif prep_data.get('npo'):
        prep_data['patient_prep'] = prep_data['npo']

    return prep_data


def extract_contrast(segment: str, modality: str) -> dict[str, Any]:
    """Extrage detaliile specifice administrării substanței de contrast."""
    contrast: dict[str, Any] = {}
    mod = modality.lower()

    if mod == 'ct':
        if re.search(r'\b(?:contrast|iodat|iohexol|iopamidol|iomeron|ultravist|omnipaque|isovue|optiray)\b', segment, re.I):
            # Caută linia sau propoziția specifică contrastului pentru a nu confunda cu hidratarea (ex: 1000 ml apă)
            c_scope_m = re.search(r'(?:substan[tț][aă]\s+de\s+contrast|contrast\s*iv|contrast)[^\n.:;]*[:=]?[^\n]+', segment, re.I)
            contrast_scope = c_scope_m.group(0) if c_scope_m else segment

            # Nume agent
            agent_m = re.search(r'\b(iohexol|iopamidol|iomeron|ultravist|omnipaque|isovue|optiray|visipaque)\s*(?:3[0-7]0)?\b', contrast_scope, re.I)
            if not agent_m:
                agent_m = re.search(r'\b(iohexol|iopamidol|iomeron|ultravist|omnipaque|isovue|optiray|visipaque)\s*(?:3[0-7]0)?\b', segment, re.I)
            if agent_m:
                contrast['agent'] = f"{agent_m.group(0).capitalize()} (350 - 370 mg I/ml)"
            else:
                contrast['agent'] = 'Substanță de contrast iodată non-ionică (350 - 370 mg I/ml)'

            # Volum
            vol_per_kg = re.search(r'\b(\d+(?:\.\d+)?)\s*m[lL]/kg\b', contrast_scope, re.I)
            if not vol_per_kg:
                vol_per_kg = re.search(r'\b(\d+(?:\.\d+)?)\s*m[lL]/kg\b', segment, re.I)

            vol_match = re.search(r'\b(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*m[lL]\b', contrast_scope, re.I)
            if not vol_match:
                vol_match = re.search(r'\b(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*m[lL]\b', segment, re.I)

            if vol_per_kg:
                contrast['volume'] = f"{vol_per_kg.group(1)} mL/kg (aprox. 80 - 100 mL)"
            elif vol_match:
                contrast['volume'] = f"{vol_match.group(1).strip()} mL"

            # Rată de flux (debit)
            flow_match = re.search(r'\b(\d+(?:\.\d+)?(?:\s*[-–—/]\s*\d+(?:\.\d+)?)?)\s*m[lL]/s(?:ec)?\b', contrast_scope, re.I)
            if not flow_match:
                flow_match = re.search(r'\b(\d+(?:\.\d+)?(?:\s*[-–—/]\s*\d+(?:\.\d+)?)?)\s*m[lL]/s(?:ec)?\b', segment, re.I)
            if flow_match:
                contrast['flow_rate'] = f"{flow_match.group(1).strip()} mL/s"

            # Durată injectare
            dur_match = re.search(r'\b(?:durat[aă]|duration)\b\s*[:=]?\s*(\d{1,3}\s*s(?:ec)?)', contrast_scope, re.I)
            if dur_match:
                contrast['duration'] = dur_match.group(1).strip()

            # Temporizare / Delay / Bolus tracking
            delay_match = re.search(r'\b(?:delay|temporizare|timing|bolus\s+tracking|faza\s+arterial[aă]|faza\s+venoas[aă])\b\s*[:=]?\s*([^\n.;]{5,80})', contrast_scope, re.I)
            if not delay_match:
                delay_match = re.search(r'\b(?:delay|temporizare|timing|bolus\s+tracking|faza\s+arterial[aă]|faza\s+venoas[aă])\b\s*[:=]?\s*([^\n.;]{5,80})', segment, re.I)
            if delay_match:
                contrast['timing'] = delay_match.group(1).strip()
            elif re.search(r'\bbolus\s+tracking\b', contrast_scope, re.I):
                contrast['timing'] = 'Bolus tracking (declanșare automată conform pragului HU)'

            # ROI
            roi_match = re.search(r'\b(?:roi|regiune\s+de\s+interes)\b\s*[:=]?\s*([^\n.;]{4,60})', segment, re.I)
            if roi_match:
                contrast['roi'] = roi_match.group(1).strip()

            # Trigger HU
            trig_match = re.search(r'\b(?:declan[sș]ator|trigger|prag)\b\s*[:=]?\s*(\d{2,3}\s*HU)', segment, re.I)
            if trig_match:
                contrast['trigger'] = trig_match.group(1).strip()

    elif mod in ('irm', 'mri'):
        if re.search(r'\b(?:gadoliniu|gadovist|dotarem|clariscan|multihance|primovist|contrast\s+paramagnetic)\b', segment, re.I):
            agent_m = re.search(r'\b(gadovist|dotarem|clariscan|multihance|primovist|gadobutrol|acid\s+gadoteric)\b', segment, re.I)
            if agent_m:
                contrast['agent'] = f"Chelat de Gadoliniu macrociclic ({agent_m.group(0).capitalize()})"
            else:
                contrast['agent'] = 'Chelat de Gadoliniu macrociclic hidrosolubil'

            # Doză
            dose_m = re.search(r'(\d+(?:\.\d+)?\s*mmol/kg|\d+(?:\.\d+)?\s*ml/kg[^\n.;]*)', segment, re.I)
            if dose_m:
                contrast['dose'] = dose_m.group(1).strip()
            else:
                contrast['dose'] = '0.1 mmol/kg corp (0.1 - 0.2 ml/kg corp)'

            # Debit
            flow_m = re.search(r'(\d+(?:\.\d+)?\s*ml/s[^\n.;]*)', segment, re.I)
            if flow_m:
                contrast['flow_rate'] = flow_m.group(1).strip()

            # Timing faze
            timing_m = re.search(r'\b(?:timing|faze\s+dinamice|temporizare)\b\s*[:=]?\s*([^\n.;]{6,90})', segment, re.I)
            if timing_m:
                contrast['timing'] = timing_m.group(1).strip()

            # eGFR / filtrare
            egfr_m = re.search(r'\b(?:egfr|filtrare\s+renal[aă]|precau[tț]ii)\b\s*[:=]?\s*([^\n.;]{6,90})', segment, re.I)
            if egfr_m:
                contrast['notes'] = egfr_m.group(1).strip()

    elif mod == 'fluoro':
        if re.search(r'\b(?:bariu|sulfat\s+de\s+bariu|gastrografin|contrast\s+hidrosolubil)\b', segment, re.I):
            if re.search(r'\bgastrografin|hidrosolubil\b', segment, re.I):
                contrast['agent'] = 'Substanță de contrast iodată hidrosolubilă (Gastrografin / Omnipaque)'
            else:
                contrast['agent'] = 'Sulfat de Bariu suspensie 100% - 250% w/v (sau hidrosolubil în caz de suspiciune de perforație)'

            # Cale de administrare
            if re.search(r'\b(?:per\s+os|oral[aă]|inghitire|inghitit)\b', segment, re.I):
                contrast['route'] = 'Orală (per os), înghițire voluntară sub ecran'
            elif re.search(r'\b(?:rectal[aă]|clism[aă]|irigoscopie)\b', segment, re.I):
                contrast['route'] = 'Rectală (retrogradă pe canulă de clismă)'
            elif re.search(r'\b(?:cateter|fistul[aă]|fistulografie)\b', segment, re.I):
                contrast['route'] = 'Injectare directă pe cateter / canulă'

            # Volum
            vol_m = re.search(r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*ml\b', segment, re.I)
            if vol_m:
                contrast['volume'] = f"{vol_m.group(1).strip()} ml"

            # Instrucțiuni
            inst_m = re.search(r'\b(?:instruc[tț]iuni|administrare|recomandare)\b\s*[:=]?\s*([^\n.;]{6,100})', segment, re.I)
            if inst_m:
                contrast['instructions'] = inst_m.group(1).strip()

    return contrast


def extract_safety_and_protection(segment: str, modality: str) -> dict[str, Any]:
    """Extrage elementele de securitate clinică, protecție și reguli ALARA."""
    result: dict[str, Any] = {}
    mod = modality.lower()

    if mod == 'rx':
        prot_matches = re.findall(r'\b(?:[sș]or[tț]\s+de\s+plumb[^\n.;]*|guler\s+tiroidian[^\n.;]*|colimare\s+str[aâ]ns[aă][^\n.;]*|protec[tț]ie\s+gonade[^\n.;]*|ecran\s+plumbuit[^\n.;]*)', segment, re.I)
        bullets = extract_section_bullets(segment, r'(?:protec[tț]ie(?:\s+radiologic[aă])?|radioprotec[tț]ie|alara)', max_items=4)
        merged = []
        for b in bullets + [_clean_bullet_text(p) for p in prot_matches]:
            if b and b not in merged:
                merged.append(b)
        if merged:
            result['protection'] = merged[:4]

    elif mod == 'ct':
        safety: dict[str, str] = {}
        renal_m = re.search(r'\b(?:func[tț]ie\s+renal[aă]|egfr|creatinin[aă])\b\s*[:=]?\s*([^\n.;]{6,90})', segment, re.I)
        if renal_m:
            safety['renal'] = renal_m.group(1).strip()
        elif re.search(r'\begfr\s*[><=]?\s*30\b', segment, re.I):
            safety['renal'] = 'Verificare obligatorie eGFR > 30 mL/min/1.73m² anterior administrării de contrast'

        allergy_m = re.search(r'\b(?:alergii|teren\s+atopic|premedica[tț]ie\s+antialergic[aă])\b\s*[:=]?\s*([^\n.;]{6,90})', segment, re.I)
        if allergy_m:
            safety['allergy'] = allergy_m.group(1).strip()
        elif re.search(r'\b(?:alergie|atopic)\b', segment, re.I):
            safety['allergy'] = 'Verificare antecedente alergice; premedicație cu corticosteroizi și antihistaminice la nevoie'

        if safety:
            result['safety'] = safety

    elif mod in ('irm', 'mri'):
        sc_bullets = extract_section_bullets(segment, r'(?:securitate\s+rm|siguran[tț][aă]\s+rm|limit[aă]\s+sar|mr\s+safety|safety\s+considerations)', max_items=4)
        if sc_bullets:
            result['safety_considerations'] = sc_bullets
        else:
            defaults = []
            if re.search(r'\bsar\b', segment, re.I):
                defaults.append('Monitorizare SAR corp întreg < 2.0 W/kg (Mod Normal de Operare)')
            if re.search(r'\b(?:c[aă][sș]ti|acustic|zgomot|dopuri)\b', segment, re.I):
                defaults.append('Protecție auditivă obligatorie cu căști fonice sau dopuri auditive (atenuare > 25 dB)')
            if re.search(r'\b(?:mr\s*conditional|implant)\b', segment, re.I):
                defaults.append('Verificare riguroasă a statusului MR Conditional pentru toate implanturile medicale')
            if defaults:
                result['safety_considerations'] = defaults

    elif mod in ('eco', 'us'):
        bullets = extract_section_bullets(segment, r'(?:securitate\s+acustic[aă]|limite\s+tehnice|acoustic\s+safety|safety\s+and\s+limitations)', max_items=4)
        if bullets:
            result['safety_and_limitations'] = bullets
        else:
            defaults = []
            if re.search(r'\b(?:indice\s+mecanic|indice\s+termic|\bmi\b|\bti\b)\b', segment, re.I):
                defaults.append('Indice Mecanic (MI) < 1.0 și Indice Termic (TI) < 1.0 conform principiului ALARA')
            if re.search(r'\b(?:gaz|meteorism|aer)\b', segment, re.I):
                defaults.append('Atenuare acustică limitată de interpoziția aerică; recomandare ferestre alternative')
            if defaults:
                result['safety_and_limitations'] = defaults

    elif mod == 'fluoro':
        bullets = extract_section_bullets(segment, r'(?:radioprotec[tț]ie(?:\s+[sș]i\s+dozimetrie)?|protec[tț]ie\s+radiologic[aă]|radiation\s+safety|alara)', max_items=4)
        if bullets:
            result['radiation_safety'] = bullets
        else:
            defaults = []
            if re.search(r'\b(?:[sș]or[tț]|plumb|guler)\b', segment, re.I):
                defaults.append('Echipament individual plumbuit obligatoriu (șorț ≥ 0.35 mm Pb, guler tiroidian, ochelari plumbuiți)')
            if re.search(r'\b(?:pulsat[aă]|lih|last\s+image\s+hold)\b', segment, re.I):
                defaults.append('Utilizarea regimului de fluoroscopie pulsată joasă și a funcției Last Image Hold (LIH)')
            if defaults:
                result['radiation_safety'] = defaults

    return result


def extract_rx_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii clinici și tehnici specifici Radiografiei convenționale (Rx)."""
    segment = extract_relevant_segment(text, protocol_title)
    
    params: dict[str, Any] = {
        'tech_params': {},
    }

    # Indicații clinice
    indications = extract_clinical_indications(segment)
    if indications:
        params['clinical_indications'] = indications

    # 1. Tensiune (kV)
    fata_kv_match = re.search(r'(?:fa[tț][aă]|fata|ap|pa|antero-posterior)[^\n.:;]{0,40}?(?:kv|tensiune)?[^\n.:;]{0,15}?(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:k[Vv]p?)?', segment, re.I)
    profil_kv_match = re.search(r'(?:profil|lat|lateral|ll)[^\n.:;]{0,40}?(?:kv|tensiune)?[^\n.:;]{0,15}?(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:k[Vv]p?)?', segment, re.I)

    if fata_kv_match and profil_kv_match:
        f_val = fata_kv_match.group(1).strip()
        p_val = profil_kv_match.group(1).strip()
        params['tech_params']['kv'] = f"{f_val} (Față); {p_val} (Profil)"
    else:
        kv_patterns = [
            r'(?:tensiune|voltage|potential|kvp?|kv)\s*[:=]?\s*(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*(?:k[Vv]p?)?',
            r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*k[Vv]p?\b',
        ]
        for pat in kv_patterns:
            m = re.search(pat, segment, re.I)
            if m:
                val = m.group(1).replace(' ', '')
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

    # 4. Focar
    if re.search(r'\b(?:focar\s+mic|small\s+focus|focal\s+spot\s+small|0\.6\s*mm)\b', segment, re.I):
        params['tech_params']['focal_spot'] = 'Focar Mic'
    elif re.search(r'\b(?:focar\s+mare|large\s+focus|focal\s+spot\s+large|1\.2\s*mm)\b', segment, re.I):
        params['tech_params']['focal_spot'] = 'Focar Mare'
    elif re.search(r'\b(?:focar\s+mic\s+sau\s+mare|mic/mare)\b', segment, re.I):
        params['tech_params']['focal_spot'] = 'Focar Mare sau Mic'

    # 5. Grilă
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

    # 8. Poziționare, Centrare, Respirație
    pos_match = re.search(r'\b(?:pozi[tț]ie\s+pacient|pozi[tț]ionare|patient\s+position|positioning)\b\s*[:=]?\s*([^\n.;]{6,120})', segment, re.I)
    if pos_match:
        params['position'] = pos_match.group(1).strip()

    cent_match = re.search(r'\b(?:punct\s+de\s+centrare|centrare|raza\s+central[aă]|central\s+ray|\bcr\b)\b\s*[:=]?\s*([^\n.;]{6,120})', segment, re.I)
    if cent_match:
        params['centering'] = cent_match.group(1).strip()

    resp_match = re.search(r'\b(?:comand[aă]\s+respiratorie|respira[tț]ie|apnee|breathing|apnea)\b\s*[:=]?\s*([^\n.;]{6,120})', segment, re.I)
    if resp_match:
        params['breathing'] = resp_match.group(1).strip()

    # 9. Criterii de calitate
    qual = extract_quality_criteria(segment, 'rx')
    if qual:
        params['quality_criteria'] = qual

    # 10. Protecție radiologică
    safe = extract_safety_and_protection(segment, 'rx')
    if 'protection' in safe:
        params['protection'] = safe['protection']

    return params


def extract_ct_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii clinici și tehnici specifici Computer Tomografiei (CT)."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'tech_params': {},
        'contrast': {},
    }

    # Indicații clinice
    indications = extract_clinical_indications(segment)
    if indications:
        params['clinical_indications'] = indications

    # Pregătire pacient (NPO, premedicație)
    prep = extract_patient_prep(segment, 'ct')
    if 'npo' in prep:
        params['npo'] = prep['npo']
    if 'premedication' in prep:
        params['premedication'] = prep['premedication']

    # Poziționare
    pos_match = re.search(r'\b(?:pozi[tț]ie|positioning|patient\s+position)\b\s*[:=]?\s*([^\n.;]{6,100})', segment, re.I)
    if pos_match:
        params['position'] = pos_match.group(1).strip()

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

    # 6. Mod scanare
    if re.search(r'\b(?:elicoidal|helical|spiral)\b', segment, re.I):
        params['tech_params']['scan_mode'] = 'Elicoidal (Helical)'
    elif re.search(r'\b(?:secven[tț]ial|axial|step\s*and\s*shoot)\b', segment, re.I):
        params['tech_params']['scan_mode'] = 'Secvențial (Axial)'

    # 7. Substanță de contrast
    contrast = extract_contrast(segment, 'ct')
    if contrast:
        params['contrast'] = contrast

    # 8. Siguranță renală & alergii
    safety = extract_safety_and_protection(segment, 'ct')
    if 'safety' in safety:
        params['safety'] = safety['safety']

    return params


def extract_irm_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii clinici și tehnici specifici Rezonanței Magnetice (IRM/RMN)."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'coils_hardware': {},
    }

    # Indicații clinice & Contraindicații
    indications = extract_clinical_indications(segment)
    if indications:
        params['clinical_indications'] = indications

    contraindications = extract_contraindications(segment, 'irm')
    if contraindications:
        params['contraindications'] = contraindications

    # Pregătire pacient
    prep = extract_patient_prep(segment, 'irm')
    if 'patient_prep' in prep:
        params['patient_prep'] = prep['patient_prep']

    # Câmp magnetic
    if re.search(r'\b3(?:\.0)?\s*t(?:esla)?\b', segment, re.I) and re.search(r'\b1\.5\s*t(?:esla)?\b', segment, re.I):
        params['coils_hardware']['field_strength'] = '1.5T sau 3.0T'
    elif re.search(r'\b3(?:\.0)?\s*t(?:esla)?\b', segment, re.I):
        params['coils_hardware']['field_strength'] = '3.0 Tesla'
    elif re.search(r'\b1\.5\s*t(?:esla)?\b', segment, re.I):
        params['coils_hardware']['field_strength'] = '1.5 Tesla'

    # Antenă (Coil)
    coil_match = re.search(r'(?:anten[aă]|coil)\s*[:=]?\s*([^\n.;]{5,80})', segment, re.I)
    if coil_match:
        params['coils_hardware']['coil'] = coil_match.group(1).strip()
        params['coils_hardware']['coil_type'] = coil_match.group(1).strip()

    # Poziționare
    pos_match = re.search(r'\b(?:pozi[tț]ionare|pozi[tț]ie|positioning)\b\s*[:=]?\s*([^\n.;]{6,100})', segment, re.I)
    if pos_match:
        pos_val = pos_match.group(1).strip()
        params['position'] = pos_val
        params['coils_hardware']['positioning'] = pos_val

    # Secvențe RM
    found_seqs = []
    seq_patterns = [
        (r'\bt1\s*(?:se|tse|fse|vibe|mprage)?\s*(?:ax|cor|sag|axial|coronal|sagital)?\b', 'T1 SE/TSE', 'Axial'),
        (r'\bt2\s*(?:tse|fse|spair|dixon)?\s*(?:ax|cor|sag|axial|coronal|sagital)?\b', 'T2 TSE', 'Axial'),
        (r'\bflair\s*(?:ax|cor|sag)?\b', 'FLAIR', 'Axial'),
        (r'\bstir\s*(?:ax|cor|sag)?\b', 'STIR', 'Coronal'),
        (r'\bdwi\s*(?:b0|b1000)?\b', 'DWI (b=0, b=1000) + ADC', 'Axial'),
        (r'\b(?:t2\*|gre|swi)\b', 'T2* / SWI', 'Axial'),
    ]
    for pat, label, def_plane in seq_patterns:
        if re.search(pat, segment, re.I):
            found_seqs.append({
                'name': label,
                'plane': def_plane,
                'tr_te': '-',
                'slice_gap': '3.0 - 4.0 mm',
                'fov_matrix': 'FOV adecvat / matrice 320x256',
                'fat_sat': 'Da' if 'stir' in label.lower() or 'dwi' in label.lower() else 'Nu',
                'notes': 'Achiziție de înaltă rezoluție',
            })

    if found_seqs:
        params['sequences'] = found_seqs

    # Substanță de contrast
    contrast = extract_contrast(segment, 'irm')
    if contrast:
        params['contrast'] = contrast

    # Criterii de calitate
    qual = extract_quality_criteria(segment, 'irm')
    if qual:
        params['quality_criteria'] = qual

    # Securitate RM & SAR
    safe = extract_safety_and_protection(segment, 'irm')
    if 'safety_considerations' in safe:
        params['safety_considerations'] = safe['safety_considerations']

    return params


def extract_eco_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii clinici și tehnici specifici Ecografiei / Ultrasonografiei (US)."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'transducers_equipment': {},
        'technical_settings': {},
    }

    # Indicații clinice & Contraindicații
    indications = extract_clinical_indications(segment)
    if indications:
        params['clinical_indications'] = indications

    contraindications = extract_contraindications(segment, 'eco')
    if contraindications:
        params['contraindications'] = contraindications

    # Pregătire pacient
    prep = extract_patient_prep(segment, 'eco')
    if 'patient_prep' in prep:
        params['patient_prep'] = prep['patient_prep']

    # Transductor / Frecvență
    freq_match = re.search(r'(\d+(?:\.\d+)?(?:\s*[-–—/]\s*\d+(?:\.\d+)?)?)\s*mhz', segment, re.I)
    norm_seg = normalize_text(segment)
    if 'convex' in norm_seg:
        val = f"Sondă convexă ({freq_match.group(1)} MHz)" if freq_match else "Sondă convexă (3.5 - 5.0 MHz)"
        params['transducers_equipment']['transducer_types'] = val
        params['transducers_equipment']['transducer_type'] = val
    elif 'liniar' in norm_seg or 'linear' in norm_seg:
        val = f"Sondă liniară ({freq_match.group(1)} MHz)" if freq_match else "Sondă liniară (7.5 - 12.0 MHz)"
        params['transducers_equipment']['transducer_types'] = val
        params['transducers_equipment']['transducer_type'] = val
    elif freq_match:
        val = f"Sondă ecografică ({freq_match.group(1)} MHz)"
        params['transducers_equipment']['transducer_types'] = val
        params['transducers_equipment']['transducer_type'] = val

    # Poziționare & mediu cuplare
    pos_match = re.search(r'\b(?:pozi[tț]ionare|pozi[tț]ie\s+pacient)\b\s*[:=]?\s*([^\n.;]{6,100})', segment, re.I)
    if pos_match:
        params['transducers_equipment']['patient_position'] = pos_match.group(1).strip()

    # Setări tehnice: Moduri, Armonică, Măsurători
    if re.search(r'\b(?:doppler|color|spectral|pw)\b', segment, re.I):
        params['technical_settings']['modes'] = 'Mod B (2D) + Doppler Color (CFM) + Doppler Pulsat (PW)'
    if re.search(r'\b(?:thi|armonica|tissue\s+harmonic)\b', segment, re.I):
        params['technical_settings']['gain_thi'] = 'Armonică tisulară (THI) activată; ajustare dinamică TGC'
        params['technical_settings']['harmonic'] = 'Armonică tisulară (THI) activată'

    preset_match = re.search(r'\b(?:preset|aplica[tț]ie)\b\s*[:=]?\s*([^\n.;]{4,60})', segment, re.I)
    if preset_match:
        params['technical_settings']['preset'] = preset_match.group(1).strip()

    # Criterii de calitate
    qual = extract_quality_criteria(segment, 'eco')
    if qual:
        params['quality_criteria'] = qual

    # Securitate acustică & limitări
    safe = extract_safety_and_protection(segment, 'eco')
    if 'safety_and_limitations' in safe:
        params['safety_and_limitations'] = safe['safety_and_limitations']

    return params


def extract_fluoro_parameters(text: str, protocol_title: str = "") -> dict[str, Any]:
    """Extrage parametrii clinici și tehnici specifici Fluoroscopiei / Radioscopiei & C-Arm."""
    segment = extract_relevant_segment(text, protocol_title)
    params: dict[str, Any] = {
        'fluoro_params': {},
        'positioning_equipment': {},
    }

    # Indicații clinice & Contraindicații
    indications = extract_clinical_indications(segment)
    if indications:
        params['clinical_indications'] = indications

    contraindications = extract_contraindications(segment, 'fluoro')
    if contraindications:
        params['contraindications'] = contraindications

    # Pregătire pacient
    prep = extract_patient_prep(segment, 'fluoro')
    if 'patient_prep' in prep:
        params['patient_prep'] = prep['patient_prep']

    # Parametri tehnici generator/scopie
    kv_match = re.search(r'(\d{2,3}(?:\s*[-–—/]\s*\d{2,3})?)\s*k[Vv]p?', segment, re.I)
    if kv_match:
        params['fluoro_params']['kv'] = f"{kv_match.group(1).replace(' ', '')} kV"

    ma_match = re.search(r'(\d+(?:\.\d+)?(?:\s*[-–—/]\s*\d+(?:\.\d+)?)?)\s*mA\b', segment, re.I)
    if ma_match:
        params['fluoro_params']['ma_range'] = f"{ma_match.group(1).strip()} mA (AEC automat)"

    if re.search(r'\b(?:pulsat[aă]|pulsed)\b', segment, re.I):
        params['fluoro_params']['mode'] = 'Fluoroscopie pulsată (7.5 - 15 fps) + LIH'

    # Poziționare & Echipament
    pos_match = re.search(r'\b(?:pozi[tț]ie|pozi[tț]ionare)\b\s*[:=]?\s*([^\n.;]{6,100})', segment, re.I)
    if pos_match:
        params['positioning_equipment']['patient_position'] = pos_match.group(1).strip()

    # Contrast
    contrast = extract_contrast(segment, 'fluoro')
    if contrast:
        params['contrast'] = contrast

    # Criterii de calitate
    qual = extract_quality_criteria(segment, 'fluoro')
    if qual:
        params['quality_criteria'] = qual

    # Radioprotecție
    safe = extract_safety_and_protection(segment, 'fluoro')
    if 'radiation_safety' in safe:
        params['radiation_safety'] = safe['radiation_safety']

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
        old_val = current_fm.get(key) if isinstance(current_fm, dict) else None
        
        if isinstance(new_val, dict):
            if isinstance(old_val, dict):
                diffs.extend(diff_parameters(old_val, new_val, full_key))
            else:
                diffs.extend(diff_parameters({}, new_val, full_key))
        elif isinstance(new_val, list):
            if not old_val:
                diffs.append({
                    'field': full_key,
                    'label': full_key.replace('_', ' ').capitalize(),
                    'old_value': '(gol)',
                    'new_value': new_val,
                    'is_new': True,
                })
            elif isinstance(old_val, list):
                new_items = [item for item in new_val if item not in old_val]
                if new_items:
                    diffs.append({
                        'field': full_key,
                        'label': full_key.replace('_', ' ').capitalize(),
                        'old_value': f"{len(old_val)} elemente",
                        'new_value': f"{len(old_val) + len(new_items)} elemente (+{len(new_items)} noi)",
                        'is_new': False,
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
            old_list = fm.get(key)
            if not old_list or not isinstance(old_list, list):
                fm[key] = list(val)
            else:
                for item in val:
                    if item not in old_list:
                        old_list.append(item)
                fm[key] = old_list
        else:
            if val:
                fm[key] = val
    return fm


def sync_body_parameters(body: str, extracted: dict[str, Any], modality: str) -> str:
    """Actualizează toate tabelele, listele și secțiunile relevante din corpul Markdown."""
    if not body or not extracted:
        return body

    # 1. Indicații Clinice
    if 'clinical_indications' in extracted and extracted['clinical_indications']:
        ind_bullets = ''.join(f'        - {item}\n' for item in extracted['clinical_indications'])
        body = re.sub(
            r'(===\s*"Indica[tț]ii Clinice"\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{ind_bullets}',
            body,
            flags=re.I
        )

    # 2. Contraindicații
    if 'contraindications' in extracted and extracted['contraindications']:
        c_bullets = ''.join(f'        - {item}\n' for item in extracted['contraindications'])
        body = re.sub(
            r'(===\s*"Contraindica[tț]ii[^"]*"\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{c_bullets}',
            body,
            flags=re.I
        )

    # 3. Pregătire Pacient & NPO
    if 'npo' in extracted:
        body = re.sub(r'(\*\*Repaus Alimentar\s*\(NPO\):\*\*\s*)([^\n]+)', rf'\g<1>{extracted["npo"]}', body, flags=re.I)
    if 'premedication' in extracted:
        items = [it.strip() for it in str(extracted['premedication']).split('|') if it.strip()]
        pm_bullets = ''.join(f'        - {it}\n' for it in items)
        body = re.sub(
            r'(\*\*Premedica[tț]ie\s*/\s*Preg[aă]tire:\*\*\s*\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{pm_bullets}',
            body,
            flags=re.I
        )
    if 'patient_prep' in extracted:
        body = re.sub(r'(\*\*Preg[aă]tire\s*(?:Prealabil[aă]|Pacientului?|Pacient)?:\*\*\s*)([^\n]+)', rf'\g<1>{extracted["patient_prep"]}', body, flags=re.I)

    # 4. Poziționare & Centrare
    if 'position' in extracted:
        body = re.sub(r'(\*\*Pozi[tț]ie(?:\s*Pacient)?:\*\*\s*)([^\n]+)', rf'\g<1>{extracted["position"]}', body, flags=re.I)
    if 'centering' in extracted:
        body = re.sub(r'(\*\*Punct\s*de\s*Centrare\s*Fascicul:\*\*\s*)([^\n]+)', rf'\g<1>{extracted["centering"]}', body, flags=re.I)
    if 'breathing' in extracted:
        body = re.sub(r'(\*\*Comand[aă]\s*Respiratorie:\*\*\s*)([^\n]+)', rf'\g<1>{extracted["breathing"]}', body, flags=re.I)
    if 'sid_dff' in extracted:
        sid_val = str(extracted['sid_dff'])
        body = re.sub(r'(\|\s*\*\*Distan[tț][aă]\s*Focar-Film\s*\(DFF\s*/\s*SID\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {sid_val} \g<3>', body, flags=re.I)
        body = re.sub(r'(\*\*(?:Distan[tț][aă]\s*Focar-Film|DFF\s*/\s*SID|SID)\s*(?:\(DFF\s*/\s*SID\))?:\*\*\s*)([^\n]+)', rf'\g<1>{sid_val}', body, flags=re.I)

    # 5. Criterii de calitate
    if 'quality_criteria' in extracted and extracted['quality_criteria']:
        q_bullets_4 = ''.join(f'    - {item}\n' for item in extracted['quality_criteria'])
        body = re.sub(
            r'(__\d+\.\s*Criterii de Calitate[^\n_]*__\s*\n\n\s*---\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{q_bullets_4}',
            body,
            flags=re.I
        )
        q_bullets_8 = ''.join(f'        - {item}\n' for item in extracted['quality_criteria'])
        body = re.sub(
            r'(===\s*"Criterii de Calitate[^\n"]*"\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{q_bullets_8}',
            body,
            flags=re.I
        )

    # 6. Protecție & Siguranță
    if 'protection' in extracted and extracted['protection']:
        p_bullets_4 = ''.join(f'    - {item}\n' for item in extracted['protection'])
        body = re.sub(
            r'(__\d+\.\s*Protec[tț]ie Radiologic[aă][^\n_]*__\s*\n\n\s*---\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{p_bullets_4}',
            body,
            flags=re.I
        )
    if 'radiation_safety' in extracted and extracted['radiation_safety']:
        rs_bullets_4 = ''.join(f'    - {item}\n' for item in extracted['radiation_safety'])
        body = re.sub(
            r'(__\d+\.\s*Radioprotec[tț]ie[^\n_]*__\s*\n\n\s*---\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{rs_bullets_4}',
            body,
            flags=re.I
        )
    if 'safety_considerations' in extracted and extracted['safety_considerations']:
        sc_bullets_4 = ''.join(f'    - {item}\n' for item in extracted['safety_considerations'])
        body = re.sub(
            r'(__\d+\.\s*Securitate RM[^\n_]*__\s*\n\n\s*---\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{sc_bullets_4}',
            body,
            flags=re.I
        )
    if 'safety_and_limitations' in extracted and extracted['safety_and_limitations']:
        sl_bullets_8 = ''.join(f'        - {item}\n' for item in extracted['safety_and_limitations'])
        body = re.sub(
            r'(===\s*"Securitate Acustic[aă][^\n"]*"\s*\n\n)(?:[ \t]*-[^\n]*\n?)+',
            rf'\g<1>{sl_bullets_8}',
            body,
            flags=re.I
        )
    if 'safety' in extracted and isinstance(extracted['safety'], dict):
        safe = extracted['safety']
        if 'renal' in safe:
            body = re.sub(r'(\*\*Func[tț]ie Renal[aă]:\*\*\s*)([^\n]+)', rf'\g<1>{safe["renal"]}', body, flags=re.I)
        if 'allergy' in safe:
            body = re.sub(r'(\*\*Alergii:\*\*\s*)([^\n]+)', rf'\g<1>{safe["allergy"]}', body, flags=re.I)

    # 7. Substanță de contrast
    contrast = extracted.get('contrast', {})
    if isinstance(contrast, dict) and contrast:
        # Mod CT (Tabel injectare)
        if 'agent' in contrast:
            body = re.sub(r'(\|\s*Agent\s*\|\s*)([^|\n]+)(\|)', rf'\g<1>{contrast["agent"]} \g<3>', body, flags=re.I)
            body = re.sub(r'(\*\*Agent de Contrast:\*\*\s*)([^\n]+)', rf'\g<1>{contrast["agent"]}', body, flags=re.I)
        if 'volume' in contrast:
            body = re.sub(r'(\|\s*Volum\s*\|\s*)([^|\n]+)(\|)', rf'\g<1>{contrast["volume"]} \g<3>', body, flags=re.I)
            body = re.sub(r'(\*\*Volum\s*&\s*Dilu[tț]ie:\*\*\s*)([^\n]+)', rf'\g<1>{contrast["volume"]}', body, flags=re.I)
        if 'flow_rate' in contrast:
            body = re.sub(r'(\|\s*Rat[aă] de Flux\s*\|\s*)([^|\n]+)(\|)', rf'\g<1>{contrast["flow_rate"]} \g<3>', body, flags=re.I)
            body = re.sub(r'(\*\*Rat[aă] de Injectare\s*\(Debit\):\*\*\s*)([^\n]+)', rf'\g<1>{contrast["flow_rate"]}', body, flags=re.I)
        if 'duration' in contrast:
            body = re.sub(r'(\|\s*Durat[aă]\s*\|\s*)([^|\n]+)(\|)', rf'\g<1>{contrast["duration"]} \g<3>', body, flags=re.I)
        if 'timing' in contrast:
            body = re.sub(r'(\|\s*Metod[aă] Temporizare\s*\|\s*)([^|\n]+)(\|)', rf'\g<1>{contrast["timing"]} \g<3>', body, flags=re.I)
            body = re.sub(r'(\*\*Temporizare\s*&\s*Faze Dinamice:\*\*\s*)([^\n]+)', rf'\g<1>{contrast["timing"]}', body, flags=re.I)
        if 'roi' in contrast:
            body = re.sub(r'(\|\s*Pozi[tț]ionare ROI\s*\|\s*)([^|\n]+)(\|)', rf'\g<1>{contrast["roi"]} \g<3>', body, flags=re.I)
        if 'trigger' in contrast:
            body = re.sub(r'(\|\s*Declan[sș]ator\s*\(HU\)\s*\|\s*)([^|\n]+)(\|)', rf'\g<1>{contrast["trigger"]} \g<3>', body, flags=re.I)
        if 'dose' in contrast:
            body = re.sub(r'(\*\*Doz[aă] Recomandat[aă]:\*\*\s*)([^\n]+)', rf'\g<1>{contrast["dose"]}', body, flags=re.I)
        if 'notes' in contrast:
            body = re.sub(r'(\*\*Filtrare Renal[aă]\s*&\s*Precau[tț]ii:\*\*\s*)([^\n]+)', rf'\g<1>{contrast["notes"]}', body, flags=re.I)
        if 'route' in contrast:
            body = re.sub(r'(\*\*Cale de Administrare:\*\*\s*)([^\n]+)', rf'\g<1>{contrast["route"]}', body, flags=re.I)
        if 'instructions' in contrast:
            body = re.sub(r'(\*\*Instruc[tț]iuni Specifice:\*\*\s*)([^\n]+)', rf'\g<1>{contrast["instructions"]}', body, flags=re.I)

    # 8. Parametri Tehnici (Rx & CT)
    tech = extracted.get('tech_params', {})
    if isinstance(tech, dict) and tech:
        if 'kv' in tech:
            kv_val = str(tech['kv'])
            body = re.sub(r'(\|\s*\*\*Tensiune Tub\s*\(kV\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {kv_val} \g<3>', body, flags=re.I)
            body = re.sub(r'(\*\*(?:kV|Tensiune Tub|Tensiune)\s*(?:\(kV\))?:\*\*\s*)([^\n]+)', rf'\g<1>{kv_val}', body, flags=re.I)
        if 'mas' in tech:
            mas_val = str(tech['mas'])
            body = re.sub(r'(\|\s*\*\*(?:Sarcin[aă]\s*/\s*Produs\s*Curent-Timp|mAs|Curent Tub)\s*(?:\(mAs\))?\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {mas_val} \g<3>', body, flags=re.I)
            body = re.sub(r'(\*\*(?:mAs|Sarcin[aă]|Produs Curent-Timp|Curent Tub)\s*(?:\(mAs\))?:\*\*\s*)([^\n]+)', rf'\g<1>{mas_val}', body, flags=re.I)
        if 'focal_spot' in tech:
            body = re.sub(r'(\|\s*\*\*Dimensiune\s*Focar\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["focal_spot"]} \g<3>', body, flags=re.I)
        if 'grid' in tech:
            body = re.sub(r'(\|\s*\*\*Gril[aă]\s*Antidifuzoare[^\*]*\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["grid"]} \g<3>', body, flags=re.I)
        if 'aec_chambers' in tech:
            body = re.sub(r'(\|\s*\*\*Camere\s*de\s*Ionizare\s*AEC\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["aec_chambers"]} \g<3>', body, flags=re.I)
        if 'aec' in tech:
            body = re.sub(r'(\|\s*\*\*Control Automat al Expunerii\s*\(AEC\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["aec"]} \g<3>', body, flags=re.I)
        if 'collimation' in tech:
            body = re.sub(r'(\|\s*\*\*(?:Colimare\s*Fascicul|Colimare\s*Detector|Grosime Sec[tț]iune Achizi[tț]ie\s*\(Slice\))\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["collimation"]} \g<3>', body, flags=re.I)
        if 'rotation_time' in tech:
            body = re.sub(r'(\|\s*\*\*Timp de Rota[tț]ie\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["rotation_time"]} \g<3>', body, flags=re.I)
        if 'pitch' in tech:
            body = re.sub(r'(\|\s*\*\*Pitch\s*\(Factor Pas\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["pitch"]} \g<3>', body, flags=re.I)
        if 'scan_mode' in tech:
            body = re.sub(r'(\|\s*\*\*Mod Scanare\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {tech["scan_mode"]} \g<3>', body, flags=re.I)

    # 9. Hardware & Setări IRM
    hw = extracted.get('coils_hardware', {})
    if isinstance(hw, dict) and hw:
        if 'field_strength' in hw:
            body = re.sub(r'(\*\*Putere C[aâ]mp Magnetic:\*\*\s*)([^\n]+)', rf'\g<1>{hw["field_strength"]}', body, flags=re.I)
        if 'coil' in hw or 'coil_type' in hw:
            c_name = hw.get('coil') or hw.get('coil_type')
            body = re.sub(r'(\*\*Anten[aă] de Recep[tț]ie\s*\(Coil\):\*\*\s*)([^\n]+)', rf'\g<1>{c_name}', body, flags=re.I)
        if 'positioning' in hw:
            body = re.sub(r'(\*\*Pozi[tț]ie Pacient\s*&\s*Centrare:\*\*\s*)([^\n]+)', rf'\g<1>{hw["positioning"]}', body, flags=re.I)

    # 10. Hardware & Setări Ecografie
    eq = extracted.get('transducers_equipment', {})
    if isinstance(eq, dict) and eq:
        if 'transducer_types' in eq:
            body = re.sub(r'(\*\*Sonde\s*/\s*Transductori Utiliza[tț]i:\*\*\s*)([^\n]+)', rf'\g<1>{eq["transducer_types"]}', body, flags=re.I)
        if 'patient_position' in eq:
            body = re.sub(r'(\*\*Pozi[tț]ionare Pacient:\*\*\s*)([^\n]+)', rf'\g<1>{eq["patient_position"]}', body, flags=re.I)
        if 'gel_acoustic_window' in eq:
            body = re.sub(r'(\*\*Mediu de Cuplare\s*&\s*Fereastr[aă] Acustic[aă]:\*\*\s*)([^\n]+)', rf'\g<1>{eq["gel_acoustic_window"]}', body, flags=re.I)

    ts = extracted.get('technical_settings', {})
    if isinstance(ts, dict) and ts:
        if 'preset' in ts:
            body = re.sub(r'(\*\*Preset\s*/\s*Aplica[tț]ie Clinic[aă]:\*\*\s*)([^\n]+)', rf'\g<1>{ts["preset"]}', body, flags=re.I)
        if 'modes' in ts:
            body = re.sub(r'(\*\*Moduri de Lucru Active:\*\*\s*)([^\n]+)', rf'\g<1>{ts["modes"]}', body, flags=re.I)
        if 'focus_depth' in ts:
            body = re.sub(r'(\*\*Focalizare\s*&\s*Ad[aâ]ncime\s*\(Depth\):\*\*\s*)([^\n]+)', rf'\g<1>{ts["focus_depth"]}', body, flags=re.I)
        if 'gain_thi' in ts:
            body = re.sub(r'(\*\*C[aâ][sș]tig\s*\(Gain\)\s*&\s*Armonice Tisulare\s*\(THI\):\*\*\s*)([^\n]+)', rf'\g<1>{ts["gain_thi"]}', body, flags=re.I)
        if 'measurements_criteria' in ts:
            body = re.sub(r'(\*\*Criterii\s*&\s*M[aă]sur[aă]tori Standard:\*\*\s*)([^\n]+)', rf'\g<1>{ts["measurements_criteria"]}', body, flags=re.I)

    # 11. Hardware & Setări Fluoroscopie
    pe = extracted.get('positioning_equipment', {})
    if isinstance(pe, dict) and pe:
        if 'patient_position' in pe:
            body = re.sub(r'(\*\*Pozi[tț]ie Ini[tț]ial[aă] Pacient:\*\*\s*)([^\n]+)', rf'\g<1>{pe["patient_position"]}', body, flags=re.I)
        if 'equipment_setup' in pe:
            body = re.sub(r'(\*\*Configurare Bra[tț] C\s*/\s*Echipament:\*\*\s*)([^\n]+)', rf'\g<1>{pe["equipment_setup"]}', body, flags=re.I)
        if 'sid' in pe:
            body = re.sub(r'(\*\*Distan[tț][aă] Focar-Receptor:\*\*\s*)([^\n]+)', rf'\g<1>{pe["sid"]}', body, flags=re.I)

    fp = extracted.get('fluoro_params', {})
    if isinstance(fp, dict) and fp:
        if 'mode' in fp:
            body = re.sub(r'(\|\s*\*\*Regim Fluoroscopie\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["mode"]} \g<3>', body, flags=re.I)
        if 'kv' in fp:
            body = re.sub(r'(\|\s*\*\*Tensiune Tub\s*\(kV\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["kv"]} \g<3>', body, flags=re.I)
        if 'ma_range' in fp:
            body = re.sub(r'(\|\s*\*\*Curent Tub Scopie\s*\(mA\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["ma_range"]} \g<3>', body, flags=re.I)
        if 'sid' in fp:
            body = re.sub(r'(\|\s*\*\*Distan[tț][aă] Focar-Receptor\s*\(SID\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["sid"]} \g<3>', body, flags=re.I)
        if 'grid' in fp:
            body = re.sub(r'(\|\s*\*\*Gril[aă] Antidifuzoare\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["grid"]} \g<3>', body, flags=re.I)
        if 'filtration' in fp:
            body = re.sub(r'(\|\s*\*\*Filtrare Suplimentar[aă]\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["filtration"]} \g<3>', body, flags=re.I)
        if 'target_fluoro_time' in fp:
            body = re.sub(r'(\|\s*\*\*Timp [TȚ]int[aă] Scopie\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["target_fluoro_time"]} \g<3>', body, flags=re.I)
        if 'lih' in fp:
            body = re.sub(r'(\|\s*\*\*Last Image Hold\s*\(LIH\)\*\*\s*\|\s*)([^|\n]+)(\|)', rf'\g<1> {fp["lih"]} \g<3>', body, flags=re.I)

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

    # 2. Calculează diferențele față de valorile actuale
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
