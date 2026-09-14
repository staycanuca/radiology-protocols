---
author: null
category: neuro
clinical_indications:
- Sinuzită cronică sau recurentă
- Polipoză nazală / rinosinusală
- Obstrucție nazală / deviație de sept nazal
- Bilanț anatomic pre-operator ORL
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Documentarea variantelor anatomice. Evaluarea detaliată a complexului
    osteomeatal.
  nursing: Fără linie venoasă. Îndepărtați cerceii și protezele dentare.
  rad: Permeabilitatea sinusurilor maxilare, etmoidale, frontale și sfenoidale. Complexul
    osteo-meatal anterior și posterior. Variante anatomice (concha bullosa, celule
    Haller, celule agger nasi, sept deviat). Îngroșări mucosale, nivele hidro-aerice,
    eroziuni osoase.
  tech: De la marginea superioară a sinusurilor frontale până sub dinții maxilari.
    Achiziție submilimetrică. Reconstrucții coronale și axiale de înaltă rezoluție
    în fereastră osoasă și de părți moi.
  tips: Planul coronal direct sau reformat este esențial pentru evaluarea căilor de
    drenaj mucociliar.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu capul în poziție neutră
premedication: ''
protocol_type: neuroradiology
recons:
- acquisition: CT Sinusuri Paranazale
  fov: Sinusuri
  kernel: Bone
  notes: Fereastră osoasă coronală - reper chirurgical de bază
  plane: Coronal
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Sinusuri Paranazale
  fov: Sinusuri
  kernel: Standard
  notes: Fereastră de părți moi pentru polipi și mucoasă
  plane: Coronal
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Sinusuri Paranazale
  fov: Sinusuri
  kernel: Bone
  notes: Fereastră osoasă axială
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Sinusuri Paranazale
  fov: Sinusuri
  kernel: Bone
  notes: Plan mediosagital și parasagital
  plane: Sagital
  thickness_increment: 1.25 mm/1.25 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Sinusuri maxilare
  name: CT Sinusuri Paranazale
  notes: Achiziție elicoidală submilimetrică
  start: Sinusuri frontale
  thickness: 0.625 mm
- delay: 0 sec
  end: Maxilar
  name: Reformatare Axială
  notes: Reformatare axială din achiziția nativă
  start: Frontal
  thickness: 1.25 mm
slug: ct-sinus
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: N/A
  rotation_time: Axial or coronals
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Sinusuri Paranazale (Nativ)
---

# CT Sinusuri Paranazale (Nativ)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Sinusuri Paranazale | 0 sec | Sinusuri frontale → Sinusuri maxilare |
        | Reformatare Axială | 0 sec | Frontal → Maxilar |

    === "Indicații Clinice"

        - Sinuzită cronică sau recurentă
        - Polipoză nazală / rinosinusală
        - Obstrucție nazală / deviație de sept nazal
        - Bilanț anatomic pre-operator ORL

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul în poziție neutră
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
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | Axial or coronal s |
    | **Pitch (Factor Pas)** | N/A |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la marginea superioară a sinusurilor frontale până sub dinții maxilari. Achiziție submilimetrică. Reconstrucții coronale și axiale de înaltă rezoluție în fereastră osoasă și de părți moi.

    === "Note Asistent"

        - Fără linie venoasă. Îndepărtați cerceii și protezele dentare.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Permeabilitatea sinusurilor maxilare, etmoidale, frontale și sfenoidale. Complexul osteo-meatal anterior și posterior. Variante anatomice (concha bullosa, celule Haller, celule agger nasi, sept deviat). Îngroșări mucosale, nivele hidro-aerice, eroziuni osoase.

    === "Sfaturi & Recomandări"

        - Planul coronal direct sau reformat este esențial pentru evaluarea căilor de drenaj mucociliar.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Sinusuri Paranazale | Sinusuri frontale | Sinusuri maxilare | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |
    | Reformatare Axială | Frontal | Maxilar | 0 sec | 1.25 mm | Reformatare axială din achiziția nativă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Coronal | CT Sinusuri Paranazale | Sinusuri | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă coronală - reper chirurgical de bază |
    | Coronal | CT Sinusuri Paranazale | Sinusuri | 1.25 mm/1.25 mm | Standard |  | Fereastră de părți moi pentru polipi și mucoasă |
    | Axial | CT Sinusuri Paranazale | Sinusuri | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă axială |
    | Sagital | CT Sinusuri Paranazale | Sinusuri | 1.25 mm/1.25 mm | Bone |  | Plan mediosagital și parasagital |
