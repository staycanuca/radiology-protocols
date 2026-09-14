---
author: null
category: msk
clinical_indications:
- Fracturi ale membrului superior (humerus diafizar, radius, ulnă)
- Fracturi complexe de antebraț (Monteggia, Galeazzi)
- Evaluarea alinierii, calusului osos sau a materialului de osteosinteză
contrast:
  agent: Nativ de regulă. Contrast dacă se suspectează complicații supurative/vasculare
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 75 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Documentați sediul exact și aliniamentul. Fereastră de părți
    moi dacă se administrează contrast. Randare 3D dacă fractura este complexă.
  nursing: Fără linie venoasă de rutină.
  rad: Traiecte de fractură, angulație, deplasare, cominuție, extensie intraarticulară.
    Raportul cu structurile osoase adiacente.
  tech: Câmpul de scanare centrat pe zona de interes. Achiziție submilimetrică. Poziționați
    brațul pentru a asigura confortul pacientului și calitatea optimă a imaginii.
  tips: Poziționare adaptată mobilității pacientului traumatizat.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal sau poziție adaptată confortului pacientului cu membrul imobilizat
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: CT Membru Superior
  fov: Segment osos
  kernel: Bone
  notes: Fereastră osoasă axială
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Membru Superior
  fov: Segment osos
  kernel: Bone
  notes: Plan coronal în axul segmentului
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Membru Superior
  fov: Segment osos
  kernel: Bone
  notes: Plan sagital
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Membru Superior
  fov: Segment osos
  kernel: Bone
  notes: Randare tridimensională 3D în caz de fracturi complexe
  plane: 3D surface
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Distal de sediul leziunii
  name: CT Membru Superior
  notes: Achiziție elicoidală submilimetrică
  start: Proximal de sediul leziunii
  thickness: 0.625 mm
slug: ct-upper-extremity
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
title: CT Membru Superior (Segmentar)
---

# CT Membru Superior (Segmentar)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Membru Superior | 0 sec | Proximal de sediul leziunii → Distal de sediul leziunii |

    === "Indicații Clinice"

        - Fracturi ale membrului superior (humerus diafizar, radius, ulnă)
        - Fracturi complexe de antebraț (Monteggia, Galeazzi)
        - Evaluarea alinierii, calusului osos sau a materialului de osteosinteză

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal sau poziție adaptată confortului pacientului cu membrul imobilizat
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se suspectează complicații supurative/vasculare |
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

        - Câmpul de scanare centrat pe zona de interes. Achiziție submilimetrică. Poziționați brațul pentru a asigura confortul pacientului și calitatea optimă a imaginii.

    === "Note Asistent"

        - Fără linie venoasă de rutină.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Traiecte de fractură, angulație, deplasare, cominuție, extensie intraarticulară. Raportul cu structurile osoase adiacente.

    === "Sfaturi & Recomandări"

        - Poziționare adaptată mobilității pacientului traumatizat.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Membru Superior | Proximal de sediul leziunii | Distal de sediul leziunii | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Membru Superior | Segment osos | 1 mm/1 mm | Bone |  | Fereastră osoasă axială |
    | Coronal | CT Membru Superior | Segment osos | 1 mm/1 mm | Bone |  | Plan coronal în axul segmentului |
    | Sagital | CT Membru Superior | Segment osos | 1 mm/1 mm | Bone |  | Plan sagital |
    | 3D surface | CT Membru Superior | Segment osos | 0.75 mm/0.75 mm | Bone |  | Randare tridimensională 3D în caz de fracturi complexe |
