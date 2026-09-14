"""render_fluoro_protocol.py — Generator și renderer de documente Markdown pentru Protocoalele de Fluoroscopie și C-Arm.

Public API:
-----------
render_fluoro_document(fm: dict) -> str
    Preia dicționarul YAML frontmatter și generează documentul Markdown complet (front matter + body).
"""

from __future__ import annotations

import yaml


def _yaml_block(fm: dict) -> str:
    """Serializează fm ca bloc YAML delimitat de ---."""
    return '---\n' + yaml.dump(fm, default_flow_style=False, allow_unicode=True) + '---\n'


def _bullets(items: list, indent: str = "        ") -> str:
    if not items:
        return f'{indent}- Nespecificat\n'
    return ''.join(f'{indent}- {it}\n' for it in items)


def _format_kv(kv: str) -> str:
    s = str(kv).strip() if kv else "75-90 kV"
    if not s.lower().endswith("kv"):
        return f"{s} kV"
    return s


def _iris_guide_tab(iris_ref: dict) -> str:
    ir = iris_ref or {}
    chapter = ir.get("chapter", "Ghidul Național IRIS")
    dose = ir.get("radiation_dose", "Clasa 2 (Medie 1 - 5 mSv)")
    grade = ir.get("recommendation_grade", "Grad A")

    lines = [
        '    === "Ghid Național IRIS"\n',
        '\n',
        '        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"\n',
        f'            - **Capitol Ghid IRIS:** *{chapter}*\n',
        f'            - **Grad de Recomandare:** **{grade}**\n',
        f'            - **Nivel de Iradiere Estimată:** `{dose}`\n',
        '\n',
        '            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }\n',
    ]
    return ''.join(lines)


def _tech_params_section(tech: dict) -> str:
    t = tech or {}
    mode = t.get("mode", "Fluoroscopie Pulsată (7.5 - 15 fps) + LIH")
    kv = _format_kv(t.get("kv", "80-100"))
    ma = t.get("ma_range", "0.5 - 4.0 mA (AEC automat)")
    sid = t.get("sid", "100 - 115 cm (detector cât mai aproape de pacient)")
    grid = t.get("grid", "Grilă antidifuzoare prezentă (îndepărtată la nou-născuți/sugari)")
    filtration = t.get("filtration", "Totală ≥ 3.0 mm Al + 0.1 - 0.2 mm Cu (filtrare spectru moale)")
    target_time = t.get("target_fluoro_time", "< 3 - 5 minute")
    lih = t.get("lih", "Activ (Last Image Hold pentru reducerea expunerii)")

    lines = [
        '    | Parametru Tehnic Scopie & Grafie | Valoare Configurare Generator / Arc C |\n',
        '    |:---------------------------------|:---------------------------------------|\n',
        f'    | **Regim Fluoroscopie** | {mode} |\n',
        f'    | **Tensiune Tub (kV)** | {kv} |\n',
        f'    | **Curent Tub Scopie (mA)** | {ma} |\n',
        f'    | **Distanță Focar-Receptor (SID)** | {sid} |\n',
        f'    | **Grilă Antidifuzoare** | {grid} |\n',
        f'    | **Filtrare Suplimentară** | {filtration} |\n',
        f'    | **Timp Țintă Scopie** | {target_time} |\n',
        f'    | **Last Image Hold (LIH)** | {lih} |\n',
    ]
    return ''.join(lines)


def _render_images_section(images: list | None, depth: int = 2) -> str:
    """Render the clinical images & iconography gallery section.

    Returns an empty string if there are no attached images or if no image has a valid URL.
    """
    if not images or not isinstance(images, list):
        return ""

    valid_images = []
    prefix = "../" * depth
    for item in images:
        if isinstance(item, dict):
            url = str(item.get("url", "")).strip()
            caption = str(item.get("caption", "")).strip()
            desc = str(item.get("description", "")).strip()
        elif isinstance(item, str):
            url = item.strip()
            caption = ""
            desc = ""
        else:
            continue

        if not url:
            continue

        if not (url.startswith("http://") or url.startswith("https://") or url.startswith("data:") or url.startswith("/") or url.startswith(".")):
            resolved_url = f"{prefix}{url}"
        else:
            resolved_url = url

        valid_images.append({
            "url": resolved_url,
            "caption": caption,
            "description": desc,
        })

    if not valid_images:
        return ""

    cards = []
    for img in valid_images:
        cap = img["caption"]
        desc = img["description"]
        alt_text = cap if cap else "Imagine de referință protocol"
        fig_cap_parts = []
        if cap:
            fig_cap_parts.append(f"<strong>{cap}</strong>")
        if desc:
            fig_cap_parts.append(f"<span>{desc}</span>")
        figcaption = f"\n<figcaption>{' — '.join(fig_cap_parts)}</figcaption>" if fig_cap_parts else ""

        card = (
            f'<figure class="protocol-image-card" markdown>\n\n'
            f'![{alt_text}]({img["url"]})\n'
            f'{figcaption}\n\n'
            f'</figure>'
        )
        cards.append(card)

    gallery_body = "\n\n".join(cards)
    return (
        f'\n\n### 🖼️ Imagini\n\n'
        f'<div class="protocol-gallery" markdown>\n\n'
        f'{gallery_body}\n\n'
        f'</div>\n'
    )


def render_fluoro_document(fm: dict) -> str:
    """Generează documentul Markdown complet pentru protocolul de Fluoroscopie / C-Arm."""
    title = fm.get('title', 'Protocol Fluoroscopie & C-Arm')
    last_updated = fm.get('last_updated', '2026-09-13')
    author = fm.get('author', 'Departamentul de Radiologie și Imagistică Medicală')
    clinical_indications = fm.get('clinical_indications', [])
    contraindications = fm.get('contraindications', [])
    prep = fm.get('patient_prep', '')
    contrast = fm.get('contrast', {})
    positioning = fm.get('positioning_equipment', {})
    tech_params = fm.get('fluoro_params', {})
    acquisition_steps = fm.get('acquisition_steps', [])
    quality_criteria = fm.get('quality_criteria', [])
    radiation_safety = fm.get('radiation_safety', [])
    iris_ref = fm.get('iris_reference', {})
    notes = fm.get('notes', '')
    images_section = _render_images_section(fm.get('images', []))

    # Formatare pași achiziție
    steps_md = []
    if acquisition_steps:
        for idx, s in enumerate(acquisition_steps, 1):
            if isinstance(s, dict):
                phase_name = s.get("phase", f"Pasul {idx}")
                desc = s.get("description", "")
                steps_md.append(f"    - **{phase_name}:** {desc}\n")
            else:
                steps_md.append(f"    - **Pasul {idx}:** {s}\n")
    else:
        steps_md.append("    - Achiziție ghidată în timp real conform protocolului clinic.\n")

    steps_str = ''.join(steps_md)

    body = f"""
# {title}

<div class="fluoro-meta-bar">
  <span class="fluoro-modality-badge">✨ Fluoroscopie & C-Arm</span>
  <span><strong>Actualizat:</strong> {last_updated}</span>
  <span><strong>Autor:</strong> {author}</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații__

    ---

    === "Indicații Clinice"

{_bullets(clinical_indications)}
    === "Contraindicații & Atenționări"

{_bullets(contraindications)}
{_iris_guide_tab(iris_ref)}-   __2. Pregătire Pacient & Substanță de Contrast__

    ---

    - **Pregătire Prealabilă:** {prep or 'Conform indicațiilor procedurale.'}
    - **Agent de Contrast:** {contrast.get('agent', 'Sulfat de Bariu sau Substanță Iodată Hidrosolubilă Non-ionică')}
    - **Cale de Administrare:** {contrast.get('route', 'Orală / Retrogradă / Injectare pe cateter')}
    - **Volum & Diluție:** {contrast.get('volume', 'Adaptat masei corporale și indicației')}
    - **Instrucțiuni Specifice:** {contrast.get('instructions', 'Se verifică absența reacțiilor alergice și a riscului de aspirație/perforație.')}

-   __3. Poziționare & Configurare Echipament (Masă / C-Arm)__

    ---

    - **Poziție Inițială Pacient:** {positioning.get('patient_position', 'Ortostatism / Decubit conform procedurii')}
    - **Configurare Braț C / Echipament:** {positioning.get('equipment_setup', 'Tub sub masă de examinare, intensificator/detector plat deasupra')}
    - **Distanță Focar-Receptor:** {positioning.get('sid', 'Optimă ≥ 100 cm')}

-   __4. Parametri Tehnici Scopie & Expunere__

    ---

{_tech_params_section(tech_params)}
-   __5. Secvență Achiziție & Incidențe Seriate__

    ---

{steps_str}
-   __6. Criterii de Calitate & Diagnostic__

    ---

{_bullets(quality_criteria, indent="    ")}
-   __7. Radioprotecție & Dozimetrie (ALARA)__

    ---

{_bullets(radiation_safety, indent="    ")}
</div>

{f'!!! note "Observații Clinice, Capcane & Recomandări Practice"\n    {notes}\n' if notes else ''}{images_section}
=== "Ghid Rapid de Execuție & Siguranță Fluoroscopică"

    1. **Pregătire și Informare:** Verificarea identității pacientului, a indicației clinice, a excluderii sarcinii la paciente fertile și informarea privind substanța de contrast.
    2. **Configurare Echipament:** La C-Arm mobil, tubul se poziționează OBLIGATORIU sub masa operatorie, iar detectorul plat cât mai aproape de pacient pentru minimalizarea radiației difuze către operator.
    3. **Optimizare Doză (ALARA):** Se utilizează regim de fluoroscopie pulsată (4 - 7.5 - 15 fps) în locul modului continuu și colimare strânsă strict pe zona de interes.
    4. **Last Image Hold (LIH):** Utilizarea imaginii înghețate pe monitor pentru decizii operatorii sau analize anatomice, fără reactivarea inutilă a pedalei de expunere.
    5. **Protecție Personal:** Toți membrii echipei prezenți în sală poartă echipament individual de protecție din plumb (șorț echivalent 0.35-0.5 mm Pb, guler tiroidian, ochelari plumbuiți) și păstrează o distanță maximă posibilă față de tub conform legii pătratului invers al distanței.
"""

    return _yaml_block(fm) + body.strip() + '\n'
