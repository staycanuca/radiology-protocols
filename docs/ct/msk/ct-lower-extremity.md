---
author: Departamentul de Radiologie
category: msk
clinical_indications:
- Fracturi diafizare sau metafizo-epifizare complexe ale membrului inferior
- Fracturi de femur, tibie sau fibulă
- Evaluarea calusului osos, a pseudartrozei sau a materialelor de osteosinteză
- Suspiciune de osteomielită sau colecție a părților moi
contrast:
  agent: Nativ de regulă. Contrast dacă se suspectează abces / infecție
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 100 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Măsurători ale axului și rotației. Evaluarea poziției materialului
    de osteosinteză. Randare 3D VR.
  nursing: Linie venoasă necesară doar pentru cazurile cu contrast.
  rad: Tipul fracturii, deplasarea, angulația, scurtarea, cominuția și interesarea
    articulară. Poziția și stabilitatea șuruburilor/plăcilor/tijelor centromedulare.
  tech: Câmpul de scanare se adaptează strict la segmentul interesat. Achiziție submilimetrică
    pentru detaliul traiectului de fractură. Acoperire suficientă pentru determinarea
    rotației și axului mecanic.
  tips: Acoperire suficientă pentru măsurarea rotației segmentului.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu membrul inferior aliniat drept
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: CT Membru Inferior
  fov: Segment osos
  kernel: Bone
  notes: Fereastră osoasă axială
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Membru Inferior
  fov: Segment osos
  kernel: Bone
  notes: Plan coronal pe axul osului
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Membru Inferior
  fov: Segment osos
  kernel: Bone
  notes: Plan sagital
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Membru Inferior
  fov: Segment osos
  kernel: Bone
  notes: Randare tridimensională 3D pentru planificare ortopedică
  plane: 3D surface
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Distal de sediul leziunii
  name: CT Membru Inferior
  notes: Achiziție elicoidală submilimetrică
  start: Proximal de sediul leziunii
  thickness: 0.625 mm
slug: ct-lower-extremity
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200-250 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Membru Inferior (Segmentar)
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

# CT Membru Inferior (Segmentar)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Membru Inferior | 0 sec | Proximal de sediul leziunii → Distal de sediul leziunii |

    === "Indicații Clinice"

        - Fracturi diafizare sau metafizo-epifizare complexe ale membrului inferior
        - Fracturi de femur, tibie sau fibulă
        - Evaluarea calusului osos, a pseudartrozei sau a materialelor de osteosinteză
        - Suspiciune de osteomielită sau colecție a părților moi

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu membrul inferior aliniat drept
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se suspectează abces / infecție |
        | Volum | Dacă este indicat: 100 mL |
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
    | **Curent Tub (mAs)** | Auto (referință 200-250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Câmpul de scanare se adaptează strict la segmentul interesat. Achiziție submilimetrică pentru detaliul traiectului de fractură. Acoperire suficientă pentru determinarea rotației și axului mecanic.

    === "Note Asistent"

        - Linie venoasă necesară doar pentru cazurile cu contrast.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Tipul fracturii, deplasarea, angulația, scurtarea, cominuția și interesarea articulară. Poziția și stabilitatea șuruburilor/plăcilor/tijelor centromedulare.

    === "Sfaturi & Recomandări"

        - Acoperire suficientă pentru măsurarea rotației segmentului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Membru Inferior | Proximal de sediul leziunii | Distal de sediul leziunii | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Membru Inferior | Segment osos | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă axială |
    | Coronal | CT Membru Inferior | Segment osos | 1.5 mm/1.5 mm | Bone |  | Plan coronal pe axul osului |
    | Sagital | CT Membru Inferior | Segment osos | 1.5 mm/1.5 mm | Bone |  | Plan sagital |
    | 3D surface | CT Membru Inferior | Segment osos | 1 mm/1 mm | Bone |  | Randare tridimensională 3D pentru planificare ortopedică |

## Surse și revizuire

- [ACR-SSR Practice Parameter for Musculoskeletal CT](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf) — *ACR / SSR* (US)
- [UT Southwestern Radiology — Musculoskeletal CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
