---
author: None
category: chest
clinical_indications:
- Traheobronhomalacie
- Colaps expirator al căilor aeriene centrale
- EDAC (Colaps dinamic excesiv al căilor aeriene)
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
  additional_recons: Măsurare diametru AP traheal inspir vs expir. Calcul procent
    de colaps. Reconstrucție 3D de căi aeriene.
  nursing: Fără abord venos. Instruiți pacientul privind manevrele respiratorii dinamice.
    Poate fi necesar expir forțat.
  rad: Măsurați procentul de colaps traheal. Colapsul >50% sugerează traheomalacie.
    Evaluați bronșiile principale.
  tech: 'DOUĂ achiziții: 1) INSPIR de la carenă la carenă+10cm; 2) EXPIR FORȚAT la
    același nivel. Necesită reconstrucții specifice de căi aeriene.'
  tips: Antrenați pacientul pentru expir forțat. Păstrați exact același nivel în ambele
    faze.
npo: Nu este necesar
position: Decubit dorsal cu brațele ridicate
premedication: Nu este necesară
protocol_type: non-contrast
recons:
- acquisition: Ambele faze
  fov: Căi aeriene
  ir_strength: '3'
  kernel: Plămân
  notes: Axial căi aeriene
  plane: Axial
  thickness_increment: 1-2 mm/1 mm
- acquisition: Ambele faze
  fov: Căi aeriene
  ir_strength: '3'
  kernel: Plămân
  notes: Coronal căi aeriene
  plane: Coronal
  thickness_increment: 1.5 mm
- acquisition: Ambele faze
  fov: Căi aeriene
  ir_strength: '3'
  kernel: Plămân
  notes: Sagital căi aeriene
  plane: Sagital
  thickness_increment: 1.5 mm
- acquisition: Ambele faze
  fov: Căi aeriene
  ir_strength: N/A
  kernel: Plămân
  notes: Reconstrucție 3D de căi aeriene
  plane: 3D VR
  thickness_increment: 0.625-1 mm sursă
safety:
  allergy: Nu este cazul (fără contrast)
  renal: Nu este cazul (fără contrast)
series:
- delay: Inspir complet
  end: Carenă + 10 cm
  name: Achiziție în Inspir
  notes: Secțiuni fine pentru 3D
  start: Apertură toracică superioară
  thickness: 0.625-1 mm
- delay: Expir mediu forțat
  end: Carenă + 10 cm
  name: Achiziție în Expir Mediu
  notes: Același nivel ca în inspir
  start: Apertură toracică superioară
  thickness: 0.625-1 mm
slug: dynamic-airway-ct
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625-1 mm
title: CT Dinamic de Căi Aeriene
sources:
- title: AAPM CT Protocols — Routine Adult Chest CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: bec845e0b9aa0e1fbdd4cdc56ff2a4bb55e22590ee1e2f9b7329c8b90b876734
- title: UT Southwestern Radiology — CT Chest Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Dinamic de Căi Aeriene

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție în Inspir | Inspir complet | Apertură toracică superioară → Carenă + 10 cm |
        | Achiziție în Expir Mediu | Expir mediu forțat | Apertură toracică superioară → Carenă + 10 cm |

    === "Indicații Clinice"

        - Traheobronhomalacie
        - Colaps expirator al căilor aeriene centrale
        - EDAC (Colaps dinamic excesiv al căilor aeriene)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
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
    | **Grosime Secțiune Achiziție (Slice)** | 0.625-1 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ achiziții: 1) INSPIR de la carenă la carenă+10cm; 2) EXPIR FORȚAT la același nivel. Necesită reconstrucții specifice de căi aeriene.

    === "Note Asistent"

        - Fără abord venos. Instruiți pacientul privind manevrele respiratorii dinamice. Poate fi necesar expir forțat.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul (fără contrast)
            - **Alergii:** Nu este cazul (fără contrast)

    === "Note Radiolog"

        - Măsurați procentul de colaps traheal. Colapsul >50% sugerează traheomalacie. Evaluați bronșiile principale.

    === "Sfaturi & Recomandări"

        - Antrenați pacientul pentru expir forțat. Păstrați exact același nivel în ambele faze.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție în Inspir | Apertură toracică superioară | Carenă + 10 cm | Inspir complet | 0.625-1 mm | Secțiuni fine pentru 3D |
    | Achiziție în Expir Mediu | Apertură toracică superioară | Carenă + 10 cm | Expir mediu forțat | 0.625-1 mm | Același nivel ca în inspir |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Ambele faze | Căi aeriene | 1-2 mm/1 mm | Plămân | 3 | Axial căi aeriene |
    | Coronal | Ambele faze | Căi aeriene | 1.5 mm | Plămân | 3 | Coronal căi aeriene |
    | Sagital | Ambele faze | Căi aeriene | 1.5 mm | Plămân | 3 | Sagital căi aeriene |
    | 3D VR | Ambele faze | Căi aeriene | 0.625-1 mm sursă | Plămân | N/A | Reconstrucție 3D de căi aeriene |

## Surse și revizuire

- [AAPM CT Protocols — Routine Adult Chest CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Chest Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
