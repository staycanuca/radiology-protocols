---
author: null
category: msk
clinical_indications:
- Fracturi ale mâinii (metacarpiene, falange)
- Fractură de scafoid sau alte oase carpiene
- Suspiciune de corp străin radioopac
- Planificare chirurgicală a reducerii anatomice a fracturilor articulare
contrast:
  agent: Nativ de regulă. Substanță de contrast dacă se suspectează flegmon / tenosinovită
  flow_rate: 2 mL/s
  volume: 'Dacă este indicat: 50 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Reformatări specifice pe axul lung al scafoidului. Randare 3D
    dacă fractura este cominutivă articulară. Localizarea topografică a corpilor străini.
  nursing: Fără linie venoasă decât dacă este indicat contrast.
  rad: Oase carpiene, metacarpiene, falange proximale, medii și distale. Articulații
    carpo-metacarpiene (CMC), metacarpo-falangiene (MCF) și interfalangiene (IF).
    Fragmente deplasate sau rotații.
  tech: De la nivelul radiusului și ulnei distale până la vârful degetelor. Achiziție
    submilimetrică. Mâna întinsă plat, imobilizată cu burete de spumă.
  tips: Poziția Superman este optimă pentru a evita iradierea corpului și artefactele.
    Secțiuni submilimetrice esențiale pentru scafoid.
npo: Nu este necesar repaus alimentar
position: Decubit ventral cu brațul întins deasupra capului ('poziție Superman') cu
  palma așezată plan pe masă
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Mână
  fov: Mână
  kernel: Bone
  notes: Secțiuni fine axiale osoase
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Mână
  fov: Mână
  kernel: Bone
  notes: Plan coronal al mâinii
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Mână
  fov: Mână
  kernel: Bone
  notes: Plan sagital pe axul degetelor
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Mână
  fov: Carp
  kernel: Bone
  notes: Plan oblic sagital pe axul lung al scafoidului
  plane: Oblique sagittal
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Vârful degetelor
  name: CT Mână
  notes: Achiziție elicoidală submilimetrică
  start: Radius/ulnă distală
  thickness: 0.625 mm
slug: ct-hand
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 150-200 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Mână
---

# CT Mână

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Mână | 0 sec | Radius/ulnă distală → Vârful degetelor |

    === "Indicații Clinice"

        - Fracturi ale mâinii (metacarpiene, falange)
        - Fractură de scafoid sau alte oase carpiene
        - Suspiciune de corp străin radioopac
        - Planificare chirurgicală a reducerii anatomice a fracturilor articulare

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit ventral cu brațul întins deasupra capului ('poziție Superman') cu palma așezată plan pe masă
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Substanță de contrast dacă se suspectează flegmon / tenosinovită |
        | Volum | Dacă este indicat: 50 mL |
        | Rată de Flux | 2 mL/s |
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
    | **Curent Tub (mAs)** | Auto (referință 150-200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la nivelul radiusului și ulnei distale până la vârful degetelor. Achiziție submilimetrică. Mâna întinsă plat, imobilizată cu burete de spumă.

    === "Note Asistent"

        - Fără linie venoasă decât dacă este indicat contrast.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Oase carpiene, metacarpiene, falange proximale, medii și distale. Articulații carpo-metacarpiene (CMC), metacarpo-falangiene (MCF) și interfalangiene (IF). Fragmente deplasate sau rotații.

    === "Sfaturi & Recomandări"

        - Poziția Superman este optimă pentru a evita iradierea corpului și artefactele. Secțiuni submilimetrice esențiale pentru scafoid.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Mână | Radius/ulnă distală | Vârful degetelor | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Mână | Mână | 1 mm/1 mm | Bone |  | Secțiuni fine axiale osoase |
    | Coronal | CT Mână | Mână | 1 mm/1 mm | Bone |  | Plan coronal al mâinii |
    | Sagital | CT Mână | Mână | 1 mm/1 mm | Bone |  | Plan sagital pe axul degetelor |
    | Oblique sagittal | CT Mână | Carp | 0.75 mm/0.75 mm | Bone |  | Plan oblic sagital pe axul lung al scafoidului |
