---
author: Departamentul de Radiologie
category: msk
clinical_indications:
- Fracturi ale cotului (paletă humerală, capitul, trohlee)
- Fractură de cap sau col radial
- Fractură de olecranon sau apofiză coronoidă
- Luxație de cot / Triadă teribilă (luxație + fractură coronoidă + cap radial)
contrast:
  agent: Nativ de regulă. Contrast doar în suspiciune de infecție/flegmon
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 75 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Documentați leziunile din 'triada teribilă' a cotului. Aliniamentul
    liniei radio-capitelare. Reconstrucție 3D VR.
  nursing: Fără linie venoasă decât dacă este necesar contrast.
  rad: Fracturi de humerus distal, cap radial, olecranon, coronoidă. Evaluați congruența
    articulației humero-ulnare și humero-radiale. Căutați fragmente intraarticulare
    libere.
  tech: De la humerusul distal până la nivelul radiusului și ulnei proximale. Achiziție
    submilimetrică. Poziționare cu cotul în extensie dacă este tolerată de pacient.
  tips: Poziționare în extensie dacă durerea permite. Achiziție submilimetrică pentru
    decelarea fragmentelor mici.
npo: Nu este necesar repaus alimentar
position: Decubit ventral cu brațul întins deasupra capului ('poziție Superman') sau
  decubit dorsal cu cotul poziționat confortabil pe abdomen
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Cot
  fov: Cot
  kernel: Bone
  notes: Fereastră osoasă axială
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Cot
  fov: Cot
  kernel: Bone
  notes: Plan coronal al cotului
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Cot
  fov: Cot
  kernel: Bone
  notes: Plan sagital pentru trohlee și olecranon
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Cot
  fov: Cot
  kernel: Bone
  notes: Randare 3D pentru fracturi articulare complexe
  plane: 3D surface
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Radius/ulnă proximală
  name: CT Cot
  notes: Achiziție elicoidală fină submilimetrică
  start: Humerus distal
  thickness: 0.625 mm
slug: ct-elbow
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
title: CT Cot
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

# CT Cot

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Cot | 0 sec | Humerus distal → Radius/ulnă proximală |

    === "Indicații Clinice"

        - Fracturi ale cotului (paletă humerală, capitul, trohlee)
        - Fractură de cap sau col radial
        - Fractură de olecranon sau apofiză coronoidă
        - Luxație de cot / Triadă teribilă (luxație + fractură coronoidă + cap radial)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit ventral cu brațul întins deasupra capului ('poziție Superman') sau decubit dorsal cu cotul poziționat confortabil pe abdomen
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast doar în suspiciune de infecție/flegmon |
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

        - De la humerusul distal până la nivelul radiusului și ulnei proximale. Achiziție submilimetrică. Poziționare cu cotul în extensie dacă este tolerată de pacient.

    === "Note Asistent"

        - Fără linie venoasă decât dacă este necesar contrast.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Fracturi de humerus distal, cap radial, olecranon, coronoidă. Evaluați congruența articulației humero-ulnare și humero-radiale. Căutați fragmente intraarticulare libere.

    === "Sfaturi & Recomandări"

        - Poziționare în extensie dacă durerea permite. Achiziție submilimetrică pentru decelarea fragmentelor mici.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Cot | Humerus distal | Radius/ulnă proximală | 0 sec | 0.625 mm | Achiziție elicoidală fină submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Cot | Cot | 1 mm/1 mm | Bone |  | Fereastră osoasă axială |
    | Coronal | CT Cot | Cot | 1 mm/1 mm | Bone |  | Plan coronal al cotului |
    | Sagital | CT Cot | Cot | 1 mm/1 mm | Bone |  | Plan sagital pentru trohlee și olecranon |
    | 3D surface | CT Cot | Cot | 0.75 mm/0.75 mm | Bone |  | Randare 3D pentru fracturi articulare complexe |

## Surse și revizuire

- [ACR-SSR Practice Parameter for Musculoskeletal CT](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf) — *ACR / SSR* (US)
- [UT Southwestern Radiology — Musculoskeletal CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
