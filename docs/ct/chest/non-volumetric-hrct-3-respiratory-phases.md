---
author: null
category: chest
clinical_indications:
- Pneumonită de hipersensibilitate (pattern capcană de aer)
- Bronșiolită constrictivă / Boală a căilor aeriene mici
- Diferențierea atenuării în mozaic (vascular vs obstructiv)
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
  additional_recons: Reconstrucții de înaltă rezoluție pentru toate cele 3 faze
  nursing: Instruiți pacientul cu privire la succesiunea manevrelor respiratorii și
    schimbarea poziției.
  rad: Faza expiratorie identifică capcana aeriană (air trapping). Faza în procubitus
    exclude atelectaziile hipostatice.
  tech: 'TREI faze secvențiale: 1) Inspir în decubit dorsal; 2) Expir în decubit dorsal;
    3) Inspir în decubit ventral (procubitus).'
  tips: Verificați că expirul este complet și susținut pentru faza de expir.
npo: Nu este necesar
position: Decubit dorsal și decubit ventral
premedication: Nu este necesară
protocol_type: chest/pulmonary
recons:
- acquisition: Inspir Supin
  fov: Torace
  ir_strength: '3'
  kernel: Înaltă rezoluție
  notes: Fereastră pulmonară
  plane: Axial
  thickness_increment: 1.0 mm
- acquisition: Expir Supin
  fov: Torace
  ir_strength: '3'
  kernel: Înaltă rezoluție
  notes: Fereastră pulmonară expir
  plane: Axial
  thickness_increment: 1.0 mm
- acquisition: Inspir Procubitus
  fov: Torace
  ir_strength: '3'
  kernel: Înaltă rezoluție
  notes: Fereastră pulmonară procubitus
  plane: Axial
  thickness_increment: 1.0 mm
safety:
  allergy: Nu este cazul
  renal: Nu este cazul
series:
- delay: Inspir
  end: Baze pulmonare
  name: 'Faza 1: Inspir Supin'
  notes: Secvențial la 10-20 mm
  start: Vârfuri pulmonare
  thickness: 1.0 mm
- delay: Expir complet
  end: Baze pulmonare
  name: 'Faza 2: Expir Supin'
  notes: Evaluare capcană aerică
  start: Vârfuri pulmonare
  thickness: 1.0 mm
- delay: Inspir
  end: Baze pulmonare
  name: 'Faza 3: Inspir Procubitus'
  notes: Decubit ventral pentru atelectazii
  start: Vârfuri pulmonare
  thickness: 1.0 mm
slug: non-volumetric-hrct-3-respiratory-phases
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Doză redusă (referință 100-150 mAs)
  pitch: N/A
  rotation_time: Sequentials
  scan_mode: Elicoidal (Helical)
  slice_thickness: 1.0 mm
title: HRCT Non-Volumetric 3 Faze Respiratorii
---

# HRCT Non-Volumetric 3 Faze Respiratorii

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Faza 1: Inspir Supin | Inspir | Vârfuri pulmonare → Baze pulmonare |
        | Faza 2: Expir Supin | Expir complet | Vârfuri pulmonare → Baze pulmonare |
        | Faza 3: Inspir Procubitus | Inspir | Vârfuri pulmonare → Baze pulmonare |

    === "Indicații Clinice"

        - Pneumonită de hipersensibilitate (pattern capcană de aer)
        - Bronșiolită constrictivă / Boală a căilor aeriene mici
        - Diferențierea atenuării în mozaic (vascular vs obstructiv)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal și decubit ventral
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
    | **Curent Tub (mAs)** | Doză redusă (referință 100-150 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.0 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | Sequential s |
    | **Pitch (Factor Pas)** | N/A |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - TREI faze secvențiale: 1) Inspir în decubit dorsal; 2) Expir în decubit dorsal; 3) Inspir în decubit ventral (procubitus).

    === "Note Asistent"

        - Instruiți pacientul cu privire la succesiunea manevrelor respiratorii și schimbarea poziției.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul
            - **Alergii:** Nu este cazul

    === "Note Radiolog"

        - Faza expiratorie identifică capcana aeriană (air trapping). Faza în procubitus exclude atelectaziile hipostatice.

    === "Sfaturi & Recomandări"

        - Verificați că expirul este complet și susținut pentru faza de expir.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Faza 1: Inspir Supin | Vârfuri pulmonare | Baze pulmonare | Inspir | 1.0 mm | Secvențial la 10-20 mm |
    | Faza 2: Expir Supin | Vârfuri pulmonare | Baze pulmonare | Expir complet | 1.0 mm | Evaluare capcană aerică |
    | Faza 3: Inspir Procubitus | Vârfuri pulmonare | Baze pulmonare | Inspir | 1.0 mm | Decubit ventral pentru atelectazii |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Inspir Supin | Torace | 1.0 mm | Înaltă rezoluție | 3 | Fereastră pulmonară |
    | Axial | Expir Supin | Torace | 1.0 mm | Înaltă rezoluție | 3 | Fereastră pulmonară expir |
    | Axial | Inspir Procubitus | Torace | 1.0 mm | Înaltă rezoluție | 3 | Fereastră pulmonară procubitus |
