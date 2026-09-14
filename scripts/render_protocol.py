"""render_protocol.py — shared module for generating protocol Markdown documents.

Public API
----------
render_document(fm: dict) -> str
    Takes a YAML front matter dict and returns a complete Markdown document string
    (YAML front matter block + rendered body).
"""

from __future__ import annotations

import yaml


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _yaml_block(fm: dict) -> str:
    """Serialise *fm* to a fenced YAML front matter block."""
    return '---\n' + yaml.dump(fm, default_flow_style=False, allow_unicode=True) + '---\n'


def _is_no_contrast(agent: str) -> bool:
    """Return True when the agent value indicates no contrast."""
    return agent.strip().upper() in ('N/A', 'NONE', '', 'FARA', 'FĂRĂ')


def _contrast_section(contrast: dict) -> str:
    """Render the IV contrast card content."""
    agent = contrast.get('agent', '')
    if _is_no_contrast(agent):
        return (
            '    !!! info "Fără Contrast Intravenos"\n'
            '    Acest protocol nu necesită administrare de contrast intravenos.\n'
        )

    lines = [
        '    === "Parametri de Injectare"\n',
        '\n',
        '        | Parametru | Valoare |\n',
        '        |-----------|-------|\n',
        f'        | Agent | {agent} |\n',
        f'        | Volum | {contrast.get("volume", "")} |\n',
        f'        | Rată de Flux | {contrast.get("flow_rate", "")} |\n',
        f'        | Durată | {contrast.get("duration", "")} |\n',
        f'        | Metodă Temporizare | {contrast.get("timing", "")} |\n',
        f'        | Poziționare ROI | {contrast.get("roi", "")} |\n',
        f'        | Declanșator (HU) | {contrast.get("trigger", "")} |\n',
        '\n',
        '    === "Cerințe de Laborator"\n',
        '        Doză completă dacă eGFR > 30 mL/min\n',
        '        !!! warning "Dacă eGFR < 30 mL/min"\n',
        r'            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)' + '\n',
    ]
    return ''.join(lines)


def _premedication_bullets(premedication: str) -> str:
    """Return indented bullet lines for the premedication field."""
    if not premedication or not premedication.strip():
        return '        - Nu este necesară\n'
    items = [item.strip() for item in premedication.split('|') if item.strip()]
    if not items:
        return '        - Nu este necesară\n'
    return ''.join(f'        - {item}\n' for item in items)


def _indications_bullets(indications: list) -> str:
    if not indications:
        return '        - Niciuna\n'
    return ''.join(f'        - {ind}\n' for ind in indications)


_IRIS_CATEGORY_MAP = {
    'abdomen': ('Aparat digestiv & Abdomen', 'https://radiologie-pediatrica.ro/iris/'),
    'chest': ('Torace & Pulmon', 'https://radiologie-pediatrica.ro/iris/'),
    'cardiac': ('Aparat cardiovascular (Cord)', 'https://radiologie-pediatrica.ro/iris/'),
    'vascular': ('Aparat cardiovascular & Sistem vascular', 'https://radiologie-pediatrica.ro/iris/'),
    'neuro': ('Cap, Gât & Coloană vertebrală', 'https://radiologie-pediatrica.ro/iris/'),
    'msk': ('Aparat locomotor & Articulații', 'https://radiologie-pediatrica.ro/iris/'),
    'trauma': ('Traumatisme & Politraumă', 'https://radiologie-pediatrica.ro/iris/'),
}


def _iris_guide_tab(category: str) -> str:
    cat_info = _IRIS_CATEGORY_MAP.get(str(category).strip().lower(), ('Ghidul Național IRIS', 'https://radiologie-pediatrica.ro/iris/'))
    chapter_name = cat_info[0]
    lines = [
        '    === "Ghid Național IRIS"\n',
        '\n',
        '        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"\n',
        f'            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *{chapter_name}*).\n',
        '\n',
        '            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }\n',
    ]
    return ''.join(lines)


def _series_acquisition_summary(series: list) -> str:
    """Render the compact series summary table inside Clinical Summary card."""
    rows = ''
    for s in series:
        rows += f'        | {s.get("name","")} | {s.get("delay","")} | {s.get("start","")} → {s.get("end","")} |\n'
    return rows


def _series_full_table(series: list) -> str:
    rows = ''
    for s in series:
        rows += (
            f'    | {s.get("name","")} | {s.get("start","")} | {s.get("end","")} '
            f'| {s.get("delay","")} | {s.get("thickness","")} | {s.get("notes","")} |\n'
        )
    return rows


def _recons_table(recons: list) -> str:
    rows = ''
    for r in recons:
        rows += (
            f'    | {r.get("plane","")} | {r.get("acquisition","")} | {r.get("fov","")} '
            f'| {r.get("thickness_increment","")} | {r.get("kernel","")} '
            f'| {r.get("ir_strength","")} | {r.get("notes","")} |\n'
        )
    return rows


def _format_kv(kv: str) -> str:
    kv_str = str(kv).strip() if kv else "120"
    if not kv_str.lower().endswith("kv") and "dual" not in kv_str.lower():
        return f"{kv_str} kV"
    return kv_str


def _format_mas(mas: str) -> str:
    return str(mas).strip() if mas else "Auto (referință 200)"


def _format_rot(rot: str) -> str:
    rot_str = str(rot).strip() if rot else "0.5 s"
    if rot_str.endswith("s") and not rot_str.endswith(" s"):
        rot_str = rot_str[:-1] + " s"
    return rot_str


def _format_pitch(pitch: str) -> str:
    return str(pitch).strip() if pitch else "1.0 - 1.2"


def _resolve_slice(tech_params: dict, series: list) -> str:
    if tech_params.get("slice_thickness"):
        return str(tech_params["slice_thickness"]).strip()
    if tech_params.get("slice"):
        return str(tech_params["slice"]).strip()
    if series:
        all_th = [s.get("thickness", "").strip() for s in series if s.get("thickness")]
        sub_mm = [t for t in all_th if t.startswith("0.") or "0.6" in t or "0.5" in t or "0.7" in t]
        if sub_mm:
            return sub_mm[0]
        if all_th:
            return all_th[0]
    return "0.625 mm"


def _resolve_collimation(tech_params: dict, category: str) -> str:
    if tech_params.get("collimation"):
        return str(tech_params["collimation"]).strip()
    if category == "cardiac":
        return "64 × 0.625 mm sau 128 × 0.6 mm"
    return "Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)"


def _resolve_aec(tech_params: dict, category: str) -> str:
    if tech_params.get("aec"):
        return str(tech_params["aec"]).strip()
    if category == "cardiac":
        return "Modulare ECG activată (pulsare conform ritmului cardiac)"
    elif category == "neuro":
        return "Activat (Modulare angulară adaptivă / Curent fix fosa posterioară)"
    elif category == "trauma":
        return "Activat (Modulare automată 3D pentru politraumă)"
    return "Activat (Modulare automată 3D conform topogramei / scout)"


def _resolve_scan_mode(tech_params: dict, category: str) -> str:
    if tech_params.get("scan_mode"):
        return str(tech_params["scan_mode"]).strip()
    if category == "cardiac":
        return "Elicoidal sincronizat ECG (sau Secvențial prospectiv)"
    pitch_val = str(tech_params.get("pitch", "")).lower()
    if "sequential" in pitch_val:
        return "Secvențial (Axial)"
    return "Elicoidal (Helical)"


def _tech_params_section(tech_params: dict, series: list = None, category: str = '') -> str:
    """Render the Technical Parameters card content."""
    tp = tech_params or {}
    series = series or []

    kv_val = _format_kv(tp.get('kv', ''))
    mas_val = _format_mas(tp.get('mas', ''))
    aec_val = _resolve_aec(tp, category)
    slice_val = _resolve_slice(tp, series)
    collimation_val = _resolve_collimation(tp, category)
    rot_val = _format_rot(tp.get('rotation_time', ''))
    pitch_val = _format_pitch(tp.get('pitch', ''))
    scan_mode_val = _resolve_scan_mode(tp, category)

    lines = [
        '    | Parametru Tehnic | Valoare Configurare |\n',
        '    |:-----------------|:---------------------|\n',
        f'    | **Tensiune Tub (kV)** | {kv_val} |\n',
        f'    | **Curent Tub (mAs)** | {mas_val} |\n',
        f'    | **Control Automat al Expunerii (AEC)** | {aec_val} |\n',
        f'    | **Grosime Secțiune Achiziție (Slice)** | {slice_val} |\n',
        f'    | **Colimare Detector** | {collimation_val} |\n',
        f'    | **Timp de Rotație** | {rot_val} |\n',
        f'    | **Pitch (Factor Pas)** | {pitch_val} |\n',
        f'    | **Mod Scanare** | {scan_mode_val} |\n',
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


# ---------------------------------------------------------------------------
# Public function
# ---------------------------------------------------------------------------

def render_document(fm: dict) -> str:
    """Return a complete Markdown document for *fm*.

    Parameters
    ----------
    fm : dict
        Parsed YAML front matter dict (see module docstring for expected keys).

    Returns
    -------
    str
        Full document: YAML front matter block followed by the rendered body.
    """
    title = fm.get('title', '')
    last_updated = fm.get('last_updated', '')
    author = fm.get('author', '')
    category = fm.get('category', '')
    position = fm.get('position', '')
    npo = fm.get('npo', '')
    premedication = fm.get('premedication', '')
    contrast = fm.get('contrast', {})
    series = fm.get('series', [])
    recons = fm.get('recons', [])
    notes = fm.get('notes', {})
    safety = fm.get('safety', {})
    clinical_indications = fm.get('clinical_indications', [])
    tech_params = fm.get('tech_params', {})
    images_section = _render_images_section(fm.get('images', []))

    body = f"""
# {title}

**Ultima actualizare:** {last_updated}
**Autor:** {author}

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
{_series_acquisition_summary(series)}
    === "Indicații Clinice"

{_indications_bullets(clinical_indications)}
{_iris_guide_tab(category)}-   __2. Pregătire Pacient__

    ---

    - **Poziție:** {position}
    - **Repaus Alimentar (NPO):** {npo}
    - **Premedicație / Pregătire:**
{_premedication_bullets(premedication)}
-   __3. Contrast IV & Injectare__

    ---
{_contrast_section(contrast)}
-   __4. Parametri Tehnici Achiziție__

    ---
{_tech_params_section(tech_params, series, category)}
-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - {notes.get('tech', '')}

    === "Note Asistent"

        - {notes.get('nursing', '')}

        !!! warning "Siguranță"
            - **Funcție Renală:** {safety.get('renal', '')}
            - **Alergii:** {safety.get('allergy', '')}

    === "Note Radiolog"

        - {notes.get('rad', '')}

    === "Sfaturi & Recomandări"

        - {notes.get('tips', '')}

</div>

<div class="acquisition-diagram"></div>{images_section}

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
{_series_full_table(series)}
=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
{_recons_table(recons)}"""

    return _yaml_block(fm) + body
