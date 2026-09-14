---
author: null
category: msk
clinical_indications:
- Artrită gutoasă / depuneri de cristale de urat monosodic
- Tofi gutoși intraarticulari sau periarticulari
- Diferențiere gută vs. condrocalcinoză (pseudogută - CPPD)
- Cuantificarea volumului total de depozite de urat și evaluarea răspunsului terapeutic
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Cuantificarea volumetrică automată a cristalelor de urat (volum
    în cm³). Suprapunere color pe randarea 3D a scheletului.
  nursing: Fără linie venoasă. Consemnați articulațiile clinic afectate.
  rad: Cristalele de urat sunt codificate convențional în verde pe harta DECT. Decelarea
    tofilor intraarticulari, a eroziunilor osoase caracteristice ('în halou' cu margine
    sclerotică) și a depozitelor pe tendoane (tendon achilean etc.).
  tech: Tehnică Dual-Energy CT (DECT) obligatorie pentru analiza spectrală a uratului
    (80/140 kV sau spectrometrie detector dublu-strat). Acoperirea articulațiilor
    simptomatice (de regulă ambele picioare/mâini).
  tips: DECT reprezintă standardul de aur pentru vizualizarea directă a cristalelor
    de urat fără puncție articulară.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu articulația de interes poziționată central în izocentru
premedication: ''
protocol_type: non-contrast
recons:
- acquisition: DECT Gută
  fov: Articulație
  kernel: Bone and Standard
  notes: Imagini standard de referință osoasă și părți moi
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: DECT Gută
  fov: Articulație
  kernel: Urate algorithm
  notes: Harta specifică de descompunere a materialului pentru cristalele de urat
  plane: DECT urate
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: DECT Gută
  fov: Articulație
  kernel: Urate
  notes: Randare tridimensională 3D volumetrică cu codificare color a tofilor gutoși
  plane: 3D volume
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: DECT Gută
  fov: Articulație
  kernel: Bone
  notes: Plan coronal pentru evaluarea eroziunilor articulare
  plane: Coronal
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Extins contralateral
  name: DECT Gută
  notes: Achiziție cu două energii simultan (Dual Energy)
  start: Regiunea articulară afectată
  thickness: 0.625 mm
slug: ct-gout-protocol
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: Dual energy 80/140Sn or equivalent
  mas: Auto (modulare automată 3D)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Protocol Gută (DECT - Dual Energy)
---

# CT Protocol Gută (DECT - Dual Energy)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | DECT Gută | 0 sec | Regiunea articulară afectată → Extins contralateral |

    === "Indicații Clinice"

        - Artrită gutoasă / depuneri de cristale de urat monosodic
        - Tofi gutoși intraarticulari sau periarticulari
        - Diferențiere gută vs. condrocalcinoză (pseudogută - CPPD)
        - Cuantificarea volumului total de depozite de urat și evaluarea răspunsului terapeutic

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu articulația de interes poziționată central în izocentru
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Fără substanță de contrast |
        | Volum |  |
        | Rată de Flux |  |
        | Durată |  |
        | Metodă Temporizare |  |
        | Poziționare ROI |  |
        | Declanșator (HU) |  |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | Dual energy 80/140Sn or equivalent |
    | **Curent Tub (mAs)** | Auto (modulare automată 3D) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Tehnică Dual-Energy CT (DECT) obligatorie pentru analiza spectrală a uratului (80/140 kV sau spectrometrie detector dublu-strat). Acoperirea articulațiilor simptomatice (de regulă ambele picioare/mâini).

    === "Note Asistent"

        - Fără linie venoasă. Consemnați articulațiile clinic afectate.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Cristalele de urat sunt codificate convențional în verde pe harta DECT. Decelarea tofilor intraarticulari, a eroziunilor osoase caracteristice ('în halou' cu margine sclerotică) și a depozitelor pe tendoane (tendon achilean etc.).

    === "Sfaturi & Recomandări"

        - DECT reprezintă standardul de aur pentru vizualizarea directă a cristalelor de urat fără puncție articulară.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | DECT Gută | Regiunea articulară afectată | Extins contralateral | 0 sec | 0.625 mm | Achiziție cu două energii simultan (Dual Energy) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | DECT Gută | Articulație | 1 mm/1 mm | Bone and Standard |  | Imagini standard de referință osoasă și părți moi |
    | DECT urate | DECT Gută | Articulație | 0.75 mm/0.75 mm | Urate algorithm |  | Harta specifică de descompunere a materialului pentru cristalele de urat |
    | 3D volume | DECT Gută | Articulație | 0.75 mm/0.75 mm | Urate |  | Randare tridimensională 3D volumetrică cu codificare color a tofilor gutoși |
    | Coronal | DECT Gută | Articulație | 1 mm/1 mm | Bone |  | Plan coronal pentru evaluarea eroziunilor articulare |
