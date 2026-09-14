"""render_eco_protocol.py — Generator și renderer de documente Markdown pentru Protocoalele de Ecografie / Ultrasonografie (US).

Public API:
-----------
render_eco_document(fm: dict) -> str
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


def _iris_guide_tab(iris_ref: dict) -> str:
    ir = iris_ref or {}
    chapter = ir.get("chapter", "Ecografie & Ultrasonografie")
    dose = ir.get("radiation_dose", "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)")
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


def _standard_views_table(views: list) -> str:
    if not views:
        return (
            '    | Incidență / Plan Ecografic | Structură Anatomică Țintă | Repere & Tehnica de Scanare | Aspect Ecografic Normal & Măsurători |\n'
            '    |:---|:---|:---|:---|\n'
            '    | *Conform tehnicii de scanare standard* | - | - | - |\n'
        )

    lines = [
        '    | Incidență / Plan Ecografic | Structură Anatomică Țintă | Repere & Tehnica de Scanare | Aspect Ecografic Normal & Măsurători |\n',
        '    |:---------------------------|:--------------------------|:----------------------------|:-------------------------------------|\n',
    ]
    for v in views:
        if isinstance(v, dict):
            view_name = v.get("view", "Incidență standard")
            target = v.get("anatomical_target", "-")
            landmarks = v.get("landmarks", "-")
            normal = v.get("normal_aspect", "-")
            lines.append(f'    | **{view_name}** | {target} | {landmarks} | {normal} |\n')
        else:
            lines.append(f'    | **{v}** | - | - | - |\n')
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


def render_eco_document(fm: dict) -> str:
    """Generează documentul Markdown complet pentru protocolul de Ecografie."""
    title = fm.get('title', 'Protocol Ecografie')
    last_updated = fm.get('last_updated', '2026-09-13')
    author = fm.get('author', 'Departamentul de Radiologie și Imagistică Medicală')
    clinical_indications = fm.get('clinical_indications', [])
    contraindications = fm.get('contraindications', [])
    prep = fm.get('patient_prep', '')
    equip = fm.get('transducers_equipment', {})
    tech = fm.get('technical_settings', {})
    views = fm.get('standard_views', [])
    quality_criteria = fm.get('quality_criteria', [])
    safety_and_limitations = fm.get('safety_and_limitations', [])
    iris_ref = fm.get('iris_reference', {})
    notes = fm.get('notes', '')
    images_section = _render_images_section(fm.get('images', []))

    views_table_str = _standard_views_table(views)

    body = f"""
# {title}

<div class="eco-meta-bar">
  <span class="eco-modality-badge">📡 Ecografie &amp; Ultrasonografie (US)</span>
  <span><strong>Actualizat:</strong> {last_updated}</span>
  <span><strong>Autor:</strong> {author}</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații &amp; Limite Diagnostice__

    ---

    === "Indicații Clinice"

{_bullets(clinical_indications)}
    === "Contraindicații &amp; Limite Tehnice"

{_bullets(contraindications)}
{_iris_guide_tab(iris_ref)}-   __2. Pregătire Pacient &amp; Echipament (Transductori)__

    ---

    - **Pregătire Prealabilă:** {prep or 'Fără pregătire specială, cu excepția protocoalelor abdominale (repaus alimentar) sau pelvine (vezică urinară în repleție).'}
    - **Sonde / Transductori Utilizați:** {equip.get('transducer_types', 'Sondă Convexă 3.5 - 5.0 MHz / Sondă Liniară 7.5 - 14.0 MHz')}
    - **Poziționare Pacient:** {equip.get('patient_position', 'Decubit dorsal relaxat, capul pe pernă joasă; decubite laterale sau ortostatism la nevoie.')}
    - **Mediu de Cuplare & Fereastră Acustică:** {equip.get('gel_acoustic_window', 'Gel ecografic hipoalergenic în cantitate suficientă pentru eliminarea interfeței de aer.')}

-   __3. Reglaje Tehnice Ecograf &amp; Optimizare Imagine__

    ---

    - **Preset / Aplicație Clinică:** {tech.get('preset', 'Abdomen General / Părți Moi / Vascular')}
    - **Moduri de Lucru Active:** {tech.get('modes', 'Mod B (2D grayscale) + Doppler Color (CFM) + Doppler Pulsat (PW)')}
    - **Focalizare & Adâncime (Depth):** {tech.get('focus_depth', 'Focar poziționat la nivelul zonei de interes; adâncime ajustată pentru încadrarea completă a organului.')}
    - **Câștig (Gain) & Armonice Tisulare (THI):** {tech.get('gain_thi', 'THI activat pentru reducerea zgomotului de fond și artefactelor; TGC reglat uniform.')}
    - **Criterii & Măsurători Standard:** {tech.get('measurements_criteria', 'Măsurători biometrice în două axe perpendiculare; indici Doppler (IR/IP/Vmax) unde este aplicabil.')}

-   __4. Protocol de Scanare &amp; Incidențe Standard__

    ---

{views_table_str}
-   __5. Criterii de Calitate &amp; Securitate Acustică ALARA__

    ---

    === "Criterii de Calitate a Imaginii"

{_bullets(quality_criteria)}
    === "Securitate Acustică &amp; Capcane (Artefacte)"

{_bullets(safety_and_limitations)}
</div>
{images_section}
---

### Recomandări Practice &amp; Observații Tehnice
{notes or 'Documentarea iconografică obligatorie în cel puțin două planuri perpendiculare (longitudinal și transversal) pentru orice leziune decelată, cu măsurători biometrice complete și semnal Doppler asociat.'}
"""

    return _yaml_block(fm) + body
