"""render_rx_protocol.py — Generator și renderer de documente Markdown pentru Protocoalele Rx (Radiologie Clasică).

Public API:
-----------
render_rx_document(fm: dict) -> str
    Preia dicționarul YAML frontmatter și generează documentul Markdown complet (front matter + body).
"""

from __future__ import annotations

import yaml

PENDING = 'DE CONFIGURAT PE APARAT'
QUICK_PROTECTION = '    5. **Radioprotecție:** verificarea [politicii RX](../radioprotectie.md), cu măsuri distincte pentru pacient, personal și însoțitor.'


def _yaml_block(fm: dict) -> str:
    """Serializează fm ca bloc YAML delimitat de ---."""
    return '---\n' + yaml.dump(fm, default_flow_style=False, allow_unicode=True) + '---\n'


def _indications_bullets(indications: list) -> str:
    if not indications:
        return '        - Nicio indicație specificată\n'
    return ''.join(f'        - {ind}\n' for ind in indications)


def _quality_bullets(criteria: list) -> str:
    if not criteria:
        return '    - Criterii standard conform bunelor practici radiologice.\n'
    return ''.join(f'    - {c}\n' for c in criteria)


def _protection_bullets(protection: list) -> str:
    if not protection:
        return '    - Măsuri standard ALARA de radioprotecție aplicate.\n'
    return ''.join(f'    - {p}\n' for p in protection)


def _format_kv(kv: str) -> str:
    s = str(kv).strip() if kv else PENDING
    if s == PENDING:
        return s
    if not s.lower().endswith("kv"):
        return f"{s} kV"
    return s


def _format_mas(mas: str) -> str:
    s = str(mas).strip() if mas else PENDING
    if s == PENDING:
        return s
    if not s.lower().endswith("mas") and not "aec" in s.lower() and not "auto" in s.lower():
        return f"{s} mAs"
    return s


def _iris_guide_tab(iris_ref: dict, category: str) -> str:
    ir = iris_ref or {}
    chapter = ir.get("chapter", "Ghidul Național IRIS")
    dose = ir.get("radiation_dose") or "De verificat pentru examinarea și populația selectate"
    grade = ir.get("recommendation_grade") or "De verificat pe indicație; fără grad atribuit automat"

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


def _tech_params_section(tech: dict, sid: str) -> str:
    t = tech or {}
    kv_val = _format_kv(t.get("kv", ""))
    mas_val = _format_mas(t.get("mas", ""))
    grid_val = t.get("grid") or PENDING
    focal_val = t.get("focal_spot") or PENDING
    aec_val = t.get("aec_chambers") or PENDING
    collimation_val = t.get("collimation", "Strictă pe regiunea de interes")
    filtration_val = t.get("filtration") or PENDING

    lines = [
        '    | Parametru Tehnic | Valoare Configurare Generator / Tub |\n',
        '    |:-----------------|:-------------------------------------|\n',
        f'    | **Tensiune Tub (kV)** | {kv_val} |\n',
        f'    | **Sarcină / Produs Curent-Timp (mAs)** | {mas_val} |\n',
        f'    | **Distanță Focar-Film (DFF / SID)** | {sid} |\n',
        f'    | **Grilă Antidifuzoare (Bucky)** | {grid_val} |\n',
        f'    | **Dimensiune Focar** | {focal_val} |\n',
        f'    | **Camere de Ionizare AEC** | {aec_val} |\n',
        f'    | **Colimare Fascicul** | {collimation_val} |\n',
        f'    | **Filtrare Tub** | {filtration_val} |\n',
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


def _views_section(views):
    if not views:
        return ''
    lines = ['\n## Incidențe și criterii de acceptare\n']
    for view in views:
        lines.append(f"\n### {view.get('name', 'Incidență')}\n")
        for key, label in [('condition', 'Selecție'), ('position', 'Poziționare'),
                           ('centering', 'Centrare / acoperire'), ('quality', 'Criterii de acceptare')]:
            if view.get(key):
                lines.append(f"\n**{label}:** {view[key]}\n")
    return ''.join(lines)


def render_rx_document(fm: dict) -> str:
    """Generează documentul Markdown complet pentru protocolul Rx."""
    title = fm.get('title', 'Protocol Radiografie')
    last_updated = fm.get('last_updated', '2026-09-13')
    author = fm.get('author', 'Departamentul de Radiologie')
    category = fm.get('category', 'diverse')
    position = fm.get('position', 'Conform incidenței standard')
    sid = fm.get('sid_dff') or PENDING
    breathing = fm.get('breathing') or 'De precizat pentru incidență și cooperarea pacientului'
    centering = fm.get('centering', 'Pe centrul ariei de interes anatomic')
    clinical_indications = fm.get('clinical_indications', [])
    tech_params = fm.get('tech_params', {})
    quality_criteria = fm.get('quality_criteria', [])
    protection = fm.get('protection', [])
    iris_ref = fm.get('iris_reference', {})
    notes = fm.get('notes', '')
    images_section = _render_images_section(fm.get('images', []))
    draft_notice = ''
    if fm.get('clinical_status') == 'draft_not_for_clinical_use':
        draft_notice = '\n!!! warning "Ciornă pentru revizuire — nu se utilizează clinic"\n    Parametrii aparatului și adaptarea locală trebuie verificate înainte de utilizarea clinică.\n'
    review_section = ''
    if fm.get('review_required_fields'):
        review_section = '\n## De finalizat la revizuire\n\n' + '\n'.join('- ' + str(v) for v in fm['review_required_fields']) + '\n'

    body = f"""
# {title}
{draft_notice}

<div class="rx-meta-bar">
  <span class="rx-modality-badge">📷 Radiografie Convențională (Rx)</span>
  <span><strong>Actualizat:</strong> {last_updated}</span>
  <span><strong>Autor:</strong> {author}</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic & Indicații__

    ---

    === "Indicații Clinice"

{_indications_bullets(clinical_indications)}
{_iris_guide_tab(iris_ref, category)}-   __2. Poziționare & Centrare Fascicul__

    ---

    - **Poziție Pacient:** {position}
    - **Punct de Centrare Fascicul:** {centering}
    - **Distanță Focar-Film (DFF / SID):** {sid}
    - **Comandă Respiratorie:** {breathing}

-   __3. Parametri Tehnici Expunere__

    ---

{_tech_params_section(tech_params, sid)}
-   __4. Criterii de Calitate & Reușită Imagine__

    ---

{_quality_bullets(quality_criteria)}
-   __5. Protecție Radiologică (ALARA)__

    ---

{_protection_bullets(protection)}
</div>

{f'!!! note "Observații Clinice & Tehnice"\n    {notes}\n' if notes else ''}{_views_section(fm.get('standard_views'))}{images_section}{review_section}
=== "Ghid Rapid de Execuție"

    1. **Identificarea și verificarea pacientului:** verificare identitate, zonă de examinat, consimțământ conform procedurii și evaluarea posibilității unei sarcini, când este relevantă.
    2. **Pregătire:** îndepărtarea oricăror obiecte radiopace (bijuterii, agrafe, fermoare, proteze, pansamente dense).
    3. **Poziționare precisă:** alinierea receptorului de imagine și a tubului la distanța prescrisă ({sid}).
    4. **Colimare strictă:** adaptarea fasciculului strict la regiunea de diagnostic pentru scăderea iradierii și reducerea radiației difuze.
{QUICK_PROTECTION}
"""

    if fm.get('sources'):
        body += '\n\n## Surse de documentare\n\n' + '\n'.join(
            f"- [{source.get('title', 'Sursă')}]({source['url']})"
            for source in fm['sources'] if isinstance(source, dict) and source.get('url')) + '\n'
    return _yaml_block(fm) + body.strip() + '\n'
