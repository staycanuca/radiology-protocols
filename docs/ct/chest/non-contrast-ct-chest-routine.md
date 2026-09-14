---
author: null
category: chest
clinical_indications:
- Evaluare pneumonie / condensare alveolară / infecție
- Tuse cronică sau hemoptizie ușoară fără suspiciune TEP
- Evaluare emfizem pulmonar și bronșiectazii
- Contraindicație la substanță de contrast iodată
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
  additional_recons: MIP și MinIP la nevoie
  nursing: Nu este necesar acces venos.
  rad: Evaluare parenchim, mediastin, perete toracic și etaj abdominal superior inclus.
  tech: Scanare în inspir profund, craniocaudal, de la apex la sinusurile costodiafragmatice.
  tips: Antrenați apneea înainte de scanare pentru a evita artefactele bazale.
npo: Nu este necesar
position: Decubit dorsal cu picioarele înainte și brațele ridicate
premedication: Nu este necesară
protocol_type: non-contrast
recons:
- acquisition: Nativ
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Fereastră pulmonară
  plane: Axial
  thickness_increment: 1.25 mm/1.0 mm
- acquisition: Nativ
  fov: Torace
  ir_strength: '3'
  kernel: Standard
  notes: Fereastră mediastinală
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Nativ
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Coronal pulmonar
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Nativ
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Sagital pulmonar
  plane: Sagital
  thickness_increment: 2.5 mm/2.5 mm
safety:
  allergy: Nu este cazul
  renal: Nu este cazul
series:
- delay: Imediat
  end: Glande suprarenale
  name: Torace Nativ Rutină
  notes: Inspir profund
  start: Vârfuri pulmonare
  thickness: 1.25 mm
slug: non-contrast-ct-chest-routine
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 1.25 mm
title: CT Torace Nativ de Rutină
---

# CT Torace Nativ de Rutină

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Torace Nativ Rutină | Imediat | Vârfuri pulmonare → Glande suprarenale |

    === "Indicații Clinice"

        - Evaluare pneumonie / condensare alveolară / infecție
        - Tuse cronică sau hemoptizie ușoară fără suspiciune TEP
        - Evaluare emfizem pulmonar și bronșiectazii
        - Contraindicație la substanță de contrast iodată

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
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.25 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare în inspir profund, craniocaudal, de la apex la sinusurile costodiafragmatice.

    === "Note Asistent"

        - Nu este necesar acces venos.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul
            - **Alergii:** Nu este cazul

    === "Note Radiolog"

        - Evaluare parenchim, mediastin, perete toracic și etaj abdominal superior inclus.

    === "Sfaturi & Recomandări"

        - Antrenați apneea înainte de scanare pentru a evita artefactele bazale.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Torace Nativ Rutină | Vârfuri pulmonare | Glande suprarenale | Imediat | 1.25 mm | Inspir profund |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Nativ | Torace | 1.25 mm/1.0 mm | Plămân | 3 | Fereastră pulmonară |
    | Axial | Nativ | Torace | 2.5 mm/2.5 mm | Standard | 3 | Fereastră mediastinală |
    | Coronal | Nativ | Torace | 2.5 mm/2.5 mm | Plămân | 3 | Coronal pulmonar |
    | Sagital | Nativ | Torace | 2.5 mm/2.5 mm | Plămân | 3 | Sagital pulmonar |
