---
author: null
category: neuro
clinical_indications:
- Traumatism de coloană vertebrală lombară
- Boală degenerativă discală / hernie de disc lombară
- Lombosciatică / radiculopatie L4, L5, S1
- Stenoză de canal vertebral lombar sau foramen
- Spondiloliză și spondilolistezis
contrast:
  agent: Nativ de regulă. Substanță de contrast dacă este bilanț post-operator (recidivă
    vs. fibroză) sau suspiciune de spondilodiscită
  flow_rate: 3 mL/s
  volume: 'Dacă este indicat: 100 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Reformatări oblice sagitale pe găurile de conjugare. Măsurători
    de calibru ale canalului rahidian. Gradarea stenozei.
  nursing: Fără linie venoasă decât dacă este necesar contrast.
  rad: Aliniament (spondilolistezis, unghi Meyerding). Fracturi cominutive sau tasări
    vertebrale. Hernii discale (protruzie, extruzie, migrare). Calibrul canalului
    rahidian și recesurilor laterale. Hipertrofia fațetelor articulare și a ligamentelor
    galbene.
  tech: De la nivelul T12 până la sacru. Achiziție elicoidală submilimetrică. Reformatări
    sagitale și coronale fine. Reconstrucții oblice paralele cu spațiile intervertebrale
    L3-L4, L4-L5, L5-S1.
  tips: Flectarea ușoară a genunchilor ameliorează confortul pacientului și reduce
    lordoza lombară accentuată.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu genunchii ușor flectați pe un suport pentru atenuarea
  lordozei
premedication: ''
protocol_type: spine
recons:
- acquisition: CT Coloană Lombară Elicoidal
  fov: Coloană lombară
  kernel: Bone
  notes: Fereastră osoasă și de părți moi
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Coloană Lombară Elicoidal
  fov: Coloană lombară
  kernel: Bone
  notes: Plan mediosagital și parasagital pe recesuri
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Coloană Lombară Elicoidal
  fov: Coloană lombară
  kernel: Bone
  notes: Plan coronal de ansamblu
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Coloană Lombară Elicoidal
  fov: Coloană lombară
  kernel: Bone
  notes: Plan oblic orientat pe găurile de conjugare L4-L5 și L5-S1
  plane: Oblique sagittal
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Sacru
  name: CT Coloană Lombară Elicoidal
  notes: Achiziție elicoidală submilimetrică
  start: T12
  thickness: 0.625 mm
slug: ct-lumbar-spine
synonyms: []
tech_params:
  aec: Activat (Modulare 3D adaptată coloanei vertebrale)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 250 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Coloană Lombară
---

# CT Coloană Lombară

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Coloană Lombară Elicoidal | 0 sec | T12 → Sacru |

    === "Indicații Clinice"

        - Traumatism de coloană vertebrală lombară
        - Boală degenerativă discală / hernie de disc lombară
        - Lombosciatică / radiculopatie L4, L5, S1
        - Stenoză de canal vertebral lombar sau foramen
        - Spondiloliză și spondilolistezis

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu genunchii ușor flectați pe un suport pentru atenuarea lordozei
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Substanță de contrast dacă este bilanț post-operator (recidivă vs. fibroză) sau suspiciune de spondilodiscită |
        | Volum | Dacă este indicat: 100 mL |
        | Rată de Flux | 3 mL/s |
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
    | **Curent Tub (mAs)** | Auto (referință 250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare 3D adaptată coloanei vertebrale) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la nivelul T12 până la sacru. Achiziție elicoidală submilimetrică. Reformatări sagitale și coronale fine. Reconstrucții oblice paralele cu spațiile intervertebrale L3-L4, L4-L5, L5-S1.

    === "Note Asistent"

        - Fără linie venoasă decât dacă este necesar contrast.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Aliniament (spondilolistezis, unghi Meyerding). Fracturi cominutive sau tasări vertebrale. Hernii discale (protruzie, extruzie, migrare). Calibrul canalului rahidian și recesurilor laterale. Hipertrofia fațetelor articulare și a ligamentelor galbene.

    === "Sfaturi & Recomandări"

        - Flectarea ușoară a genunchilor ameliorează confortul pacientului și reduce lordoza lombară accentuată.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Coloană Lombară Elicoidal | T12 | Sacru | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Coloană Lombară Elicoidal | Coloană lombară | 1.5 mm/1.5 mm | Bone |  | Fereastră osoasă și de părți moi |
    | Sagital | CT Coloană Lombară Elicoidal | Coloană lombară | 1.5 mm/1.5 mm | Bone |  | Plan mediosagital și parasagital pe recesuri |
    | Coronal | CT Coloană Lombară Elicoidal | Coloană lombară | 1.5 mm/1.5 mm | Bone |  | Plan coronal de ansamblu |
    | Oblique sagittal | CT Coloană Lombară Elicoidal | Coloană lombară | 1.5 mm/1.5 mm | Bone |  | Plan oblic orientat pe găurile de conjugare L4-L5 și L5-S1 |
