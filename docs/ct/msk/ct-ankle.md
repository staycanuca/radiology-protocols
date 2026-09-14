---
author: null
category: msk
clinical_indications:
- Fracturi de gleznă (maleolă internă, externă, posterioară)
- Fractură de pilon tibial
- Leziuni ale sindesmozei tibio-fibulare și ligamentare
- Planificare chirurgicală pre-operatorie / evaluare osteosinteză
contrast:
  agent: Nativ de regulă. Substanță de contrast doar în suspiciune de infecție/tumoră
  flow_rate: 2-3 mL/s
  volume: 'Dacă se administrează contrast: 75 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Randare tridimensională 3D VR a gleznei pentru planificarea osteosintezei
    chirurgicale. Maparea fragmentelor cominutive.
  nursing: Fără linie venoasă decât dacă este indicată substanță de contrast.
  rad: Fracturi maleolare (clasificare Weber). Pilon tibial. Fracturi de talus și
    calcaneu. Lărgirea spațiului sindesmozei tibio-fibulare. Fragmente osteocondrale
    intraarticulare.
  tech: Câmp de scanare de la nivelul tibiei/fibulei distale până la nivelul retropiciorului
    (inclusiv calcaneu). Achiziție submilimetrică dedicată pentru reconstrucții 3D.
    Scout bilateral pentru simetrie.
  tips: Scout bilateral pentru aprecierea rotației. Secțiuni fine submilimetrice obligatorii.
npo: Nu este necesar repaus alimentar (dacă nu se administrează contrast)
position: Decubit dorsal cu picioarele înainte; glezna în poziție neutră la 90 de
  grade
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Gleznă
  fov: Gleznă
  kernel: Bone
  notes: Filtru osos de înaltă rezoluție
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Gleznă
  fov: Gleznă
  kernel: Bone
  notes: Plan coronal articulat pe pensa tibiotalară
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Gleznă
  fov: Gleznă
  kernel: Bone
  notes: Plan sagital pentru pilonul tibial și articulația subtalară
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Gleznă
  fov: Gleznă
  kernel: Bone
  notes: Randare 3D de suprafață pentru fracturi complexe
  plane: 3D surface
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică pentru scanarea nativă
  renal: Nu se aplică pentru scanarea nativă
series:
- delay: 0 sec
  end: Retropicior (calcaneu)
  name: CT Gleznă
  notes: Achiziție elicoidală submilimetrică
  start: Tibia/fibula distală
  thickness: 0.625 mm
slug: ct-ankle
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Gleznă
---

# CT Gleznă

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Gleznă | 0 sec | Tibia/fibula distală → Retropicior (calcaneu) |

    === "Indicații Clinice"

        - Fracturi de gleznă (maleolă internă, externă, posterioară)
        - Fractură de pilon tibial
        - Leziuni ale sindesmozei tibio-fibulare și ligamentare
        - Planificare chirurgicală pre-operatorie / evaluare osteosinteză

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte; glezna în poziție neutră la 90 de grade
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar (dacă nu se administrează contrast)
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Substanță de contrast doar în suspiciune de infecție/tumoră |
        | Volum | Dacă se administrează contrast: 75 mL |
        | Rată de Flux | 2-3 mL/s |
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
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Câmp de scanare de la nivelul tibiei/fibulei distale până la nivelul retropiciorului (inclusiv calcaneu). Achiziție submilimetrică dedicată pentru reconstrucții 3D. Scout bilateral pentru simetrie.

    === "Note Asistent"

        - Fără linie venoasă decât dacă este indicată substanță de contrast.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică pentru scanarea nativă
            - **Alergii:** Nu se aplică pentru scanarea nativă

    === "Note Radiolog"

        - Fracturi maleolare (clasificare Weber). Pilon tibial. Fracturi de talus și calcaneu. Lărgirea spațiului sindesmozei tibio-fibulare. Fragmente osteocondrale intraarticulare.

    === "Sfaturi & Recomandări"

        - Scout bilateral pentru aprecierea rotației. Secțiuni fine submilimetrice obligatorii.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Gleznă | Tibia/fibula distală | Retropicior (calcaneu) | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Gleznă | Gleznă | 1 mm/1 mm | Bone |  | Filtru osos de înaltă rezoluție |
    | Coronal | CT Gleznă | Gleznă | 1 mm/1 mm | Bone |  | Plan coronal articulat pe pensa tibiotalară |
    | Sagital | CT Gleznă | Gleznă | 1 mm/1 mm | Bone |  | Plan sagital pentru pilonul tibial și articulația subtalară |
    | 3D surface | CT Gleznă | Gleznă | 0.75 mm/0.75 mm | Bone |  | Randare 3D de suprafață pentru fracturi complexe |
