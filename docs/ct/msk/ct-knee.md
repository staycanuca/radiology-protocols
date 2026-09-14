---
author: Departamentul de Radiologie
category: msk
clinical_indications:
- Fracturi de platou tibial (clasificare Schatzker)
- Fracturi ale condililor femurali
- Fracturi de rotulă
- Planificare chirurgicală osteosinteză sau artroplastie
- Evaluarea materialului de osteosinteză sau a protezei de genunchi
contrast:
  agent: Nativ de regulă. Contrast dacă se suspectează artrită septică/flegmon
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 75 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Clasificare Schatzker. Măsurarea gradului de înfundare a suprafeței
    articulare tibiale. Randare 3D VR.
  nursing: Fără linie venoasă de rutină.
  rad: 'Fracturi de platou tibial: înfundare articulară (măsurată în mm), dehiscență,
    separare corticală. Condili femurali, rotulă, capul fibulei. Fragmente intraarticulare
    osteocondrale.'
  tech: De la femurul distal până la nivelul tibiei și fibulei proximale. Achiziție
    submilimetrică. Câmp extins pentru aprecierea axului mecanic al membrului. Scout
    bilateral.
  tips: Scout bilateral pentru evaluarea axului mecanic (varus/valgus).
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu picioarele înainte
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Genunchi
  fov: Genunchi
  kernel: Bone
  notes: Filtru osos de înaltă rezoluție
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Genunchi
  fov: Genunchi
  kernel: Bone
  notes: Plan coronal pe platoul tibial
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Genunchi
  fov: Genunchi
  kernel: Bone
  notes: Plan sagital pentru rotulă și panta tibială
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Genunchi
  fov: Genunchi
  kernel: Bone
  notes: Randare tridimensională 3D pentru planificare chirurgicală
  plane: 3D surface
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Tibia/fibula proximală
  name: CT Genunchi
  notes: Achiziție elicoidală submilimetrică
  start: Femur distal
  thickness: 0.625 mm
slug: ct-knee
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
title: CT Genunchi
sources:
- title: ACR-SSR Practice Parameter for Musculoskeletal CT
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf
  institution: ACR / SSR
  source_region: US
  kind: Standard de practică MSK
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: c0429ea24ea0955f09249fe969fc88b0a48e70073a42bab3ba08be042e1085f4
- title: UT Southwestern Radiology — Musculoskeletal CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Genunchi

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Genunchi | 0 sec | Femur distal → Tibia/fibula proximală |

    === "Indicații Clinice"

        - Fracturi de platou tibial (clasificare Schatzker)
        - Fracturi ale condililor femurali
        - Fracturi de rotulă
        - Planificare chirurgicală osteosinteză sau artroplastie
        - Evaluarea materialului de osteosinteză sau a protezei de genunchi

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se suspectează artrită septică/flegmon |
        | Volum | Dacă este indicat: 75 mL |
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

        - De la femurul distal până la nivelul tibiei și fibulei proximale. Achiziție submilimetrică. Câmp extins pentru aprecierea axului mecanic al membrului. Scout bilateral.

    === "Note Asistent"

        - Fără linie venoasă de rutină.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Fracturi de platou tibial: înfundare articulară (măsurată în mm), dehiscență, separare corticală. Condili femurali, rotulă, capul fibulei. Fragmente intraarticulare osteocondrale.

    === "Sfaturi & Recomandări"

        - Scout bilateral pentru evaluarea axului mecanic (varus/valgus).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Genunchi | Femur distal | Tibia/fibula proximală | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Genunchi | Genunchi | 1 mm/1 mm | Bone |  | Filtru osos de înaltă rezoluție |
    | Coronal | CT Genunchi | Genunchi | 1 mm/1 mm | Bone |  | Plan coronal pe platoul tibial |
    | Sagital | CT Genunchi | Genunchi | 1 mm/1 mm | Bone |  | Plan sagital pentru rotulă și panta tibială |
    | 3D surface | CT Genunchi | Genunchi | 0.75 mm/0.75 mm | Bone |  | Randare tridimensională 3D pentru planificare chirurgicală |

## Surse și revizuire

- [ACR-SSR Practice Parameter for Musculoskeletal CT](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf) — *ACR / SSR* (US)
- [UT Southwestern Radiology — Musculoskeletal CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
