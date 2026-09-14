"""render_irm_protocol.py — Generator și renderer de documente Markdown pentru Protocoalele IRM (Imagistică prin Rezonanță Magnetică).

Public API:
-----------
render_irm_document(fm: dict) -> str
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
    chapter = ir.get("chapter", "Imagistică prin Rezonanță Magnetică (IRM)")
    dose = ir.get("radiation_dose", "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)")
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


def _sequences_table(sequences: list) -> str:
    if not sequences:
        return '    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații |\n    |:---|:---|:---|:---|:---|:---|:---|\n    | *Conform protocolului specific* | - | - | - | - | - | - |\n'

    lines = [
        '    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |\n',
        '    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|\n',
    ]
    for s in sequences:
        if isinstance(s, dict):
            name = s.get("name", "Secvență")
            plane = s.get("plane", "Axial")
            tr_te = s.get("tr_te", "-")
            thick = s.get("slice_gap", "-")
            mat = s.get("fov_matrix", "-")
            fatsat = s.get("fat_sat", "Nu")
            notes = s.get("notes", "-")
            lines.append(f'    | **{name}** | {plane} | {tr_te} | {thick} | {mat} | {fatsat} | {notes} |\n')
        else:
            lines.append(f'    | **{s}** | - | - | - | - | - | - |\n')
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


def render_irm_document(fm: dict) -> str:
    """Generează documentul Markdown complet pentru protocolul IRM."""
    title = fm.get('title', 'Protocol IRM')
    last_updated = fm.get('last_updated', '2026-09-13')
    author = fm.get('author', 'Departamentul de Radiologie și Imagistică Medicală')
    clinical_indications = fm.get('clinical_indications', [])
    contraindications = fm.get('contraindications', [])
    prep = fm.get('patient_prep', '')
    hardware = fm.get('coils_hardware', {})
    contrast = fm.get('contrast', {})
    sequences = fm.get('sequences', [])
    quality_criteria = fm.get('quality_criteria', [])
    safety_considerations = fm.get('safety_considerations', [])
    iris_ref = fm.get('iris_reference', {})
    notes = fm.get('notes', '')
    images_section = _render_images_section(fm.get('images', []))

    seq_table_str = _sequences_table(sequences)

    body = f"""
# {title}

<div class="irm-meta-bar">
  <span class="irm-modality-badge">🧲 Imagistică prin Rezonanță Magnetică (IRM)</span>
  <span><strong>Actualizat:</strong> {last_updated}</span>
  <span><strong>Autor:</strong> {author}</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații RM__

    ---

    === "Indicații Clinice"

{_bullets(clinical_indications)}
    === "Contraindicații & Screening Metalic"

{_bullets(contraindications)}
{_iris_guide_tab(iris_ref)}-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** {prep or 'Completare obligatorie a chestionarului de securitate RM, îndepărtare corpuri metalice externe, bijuterii și machiaj.'}
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** {hardware.get('field_strength', '1.5 Tesla / 3.0 Tesla')}
    - **Antenă de Recepție (Coil):** {hardware.get('coil', 'Antenă dedicată regiunii de examinat')}
    - **Poziție Pacient & Centrare:** {hardware.get('positioning', 'Decubit dorsal cu capul/picioarele înainte, centrare optică în izocentru')}

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** {contrast.get('agent', 'Chelat de Gadoliniu macrociclic hidrosolubil')}
    - **Doză Recomandată:** {contrast.get('dose', '0.1 mmol/kg corp (0.1 - 0.2 ml/kg corp)')}
    - **Rată de Injectare (Debit):** {contrast.get('flow_rate', '1.5 - 2.0 ml/s urmat de bolus de 20-30 ml ser fiziologic')}
    - **Temporizare & Faze Dinamice:** {contrast.get('timing', 'Faze precoce arteriale/portale/tardive adaptate organului examinat')}
    - **Filtrare Renală & Precauții:** {contrast.get('notes', 'Evaluare eGFR conform ghidurilor ESUR; risc redus de Fibroză Sistemică Nefrogenă (NSF) pentru agenții macrociclici.')}

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

{seq_table_str}
-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

{_bullets(quality_criteria, indent="    ")}
-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

{_bullets(safety_considerations, indent="    ")}
</div>

{f'!!! note "Observații Clinice, Capcane & Recomandări Practice"\n    {notes}\n' if notes else ''}{images_section}
=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
"""

    return _yaml_block(fm) + body.strip() + '\n'
