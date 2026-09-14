---
author: None
category: chest
clinical_indications:
- Screening cancer bronhopulmonar (fumători / foști fumători)
- Urmărire nodul pulmonar
- Evaluare leziuni parenchimatoase la pacienți asimptomatici
contrast:
  agent: N/A
  duration: ''
  flow_rate: ''
  roi: ''
  timing: ''
  trigger: ''
  volume: ''
last_updated: '2026-01-01'
notes:
  additional_recons: MIP axial 5 mm pentru detecția nodulilor
  nursing: Fără abord venos.
  rad: Clasificare noduli conform Lung-RADS.
  tech: Scanare în inspir profund. Menținerea strictă a dozei joase (CTDIvol < 3 mGy).
  tips: Centrare atentă a pacientului în izocentru pentru a optimiza modulația dozei
    de radiație.
npo: Nu este necesar
position: Decubit dorsal cu picioarele înainte și brațele ridicate
premedication: Nu este necesară
protocol_type: non-contrast
recons:
- acquisition: Nativ Doză Redusă
  fov: Torace
  ir_strength: '4'
  kernel: Plămân
  notes: Parenchim pulmonar
  plane: Axial
  thickness_increment: 1.25 mm/1.0 mm
- acquisition: Nativ Doză Redusă
  fov: Torace
  ir_strength: '4'
  kernel: Standard
  notes: Mediastin
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Nativ Doză Redusă
  fov: Torace
  ir_strength: '4'
  kernel: Plămân
  notes: Plămân coronal
  plane: Coronal
  thickness_increment: 2.0 mm/2.0 mm
safety:
  allergy: Nu este cazul
  renal: Nu este cazul
series:
- delay: Imediat
  end: Sinusuri costodiafragmatice
  name: Torace Nativ Doză Redusă
  notes: CTDIvol redus
  start: Vârfuri pulmonare
  thickness: 1.0 mm
slug: non-contrast-ct-chest-low-dose
synonyms: []
tech_params:
  aec: Activat (Protocol doză redusă / Ultra low-dose)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Doză redusă (referință 40-60 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 1.0 mm
title: CT Torace Nativ Doză Redusă
---

# CT Torace Nativ Doză Redusă

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Torace Nativ Doză Redusă | Imediat | Vârfuri pulmonare → Sinusuri costodiafragmatice |

    === "Indicații Clinice"

        - Screening cancer bronhopulmonar (fumători / foști fumători)
        - Urmărire nodul pulmonar
        - Evaluare leziuni parenchimatoase la pacienți asimptomatici

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte și brațele ridicate
    - **Repaus Alimentar (NPO):** Nu este necesar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Doză redusă (referință 40-60 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Protocol doză redusă / Ultra low-dose) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.0 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare în inspir profund. Menținerea strictă a dozei joase (CTDIvol < 3 mGy).

    === "Note Asistent"

        - Fără abord venos.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul
            - **Alergii:** Nu este cazul

    === "Note Radiolog"

        - Clasificare noduli conform Lung-RADS.

    === "Sfaturi & Recomandări"

        - Centrare atentă a pacientului în izocentru pentru a optimiza modulația dozei de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Torace Nativ Doză Redusă | Vârfuri pulmonare | Sinusuri costodiafragmatice | Imediat | 1.0 mm | CTDIvol redus |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Nativ Doză Redusă | Torace | 1.25 mm/1.0 mm | Plămân | 4 | Parenchim pulmonar |
    | Axial | Nativ Doză Redusă | Torace | 2.5 mm/2.5 mm | Standard | 4 | Mediastin |
    | Coronal | Nativ Doză Redusă | Torace | 2.0 mm/2.0 mm | Plămân | 4 | Plămân coronal |
