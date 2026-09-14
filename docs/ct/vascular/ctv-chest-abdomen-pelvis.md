---
author: null
category: vascular
clinical_indications:
- Sindrom de venă cavă superioară (SVCS)
- Ocluzie sau tromboză a axelor venoase centrale (catetere, port-a-cath, pacemaker)
- Stadializare tumorală cu suspiciune de invazie sau tromboză venoasă tumorală cavă
contrast:
  agent: Isovue 370
  duration: 40s
  flow_rate: 3 mL/s
  timing: Timp fix de întârziere (120-180s)
  volume: 2.0 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: MIP flebografic 3D. Reconstrucții MPR curbate pe întreg traiectul
    VCS și VCI.
  nursing: Linie venoasă 18-20G; luați în considerare abord venos la ambele brațe
    dacă se investighează ocluzia VCS.
  rad: Evaluați calibrul și permeabilitatea VCS, VCI și a principalilor afluenți.
    Căutați tromboză, compresiune extrinsecă sau manșonare tumorală. Identificați
    rețeaua colaterală venoasă mediastinală sau parietală.
  tech: Scanare la 120-180 secunde. Include de la vena jugulară/subclavie până la
    venele femurale. Pentru evaluarea optimă a VCS poate fi indicată injectare bilaterală
    la nivelul ambelor brațe.
  tips: Brațele ridicate. Pentru VCS este preferabilă injectarea în ambele brațe pentru
    a evita artefactele masive unilaterale.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: vascular
recons:
- acquisition: Fază Venoasă CTV
  fov: Torace
  kernel: Standard
  notes: Vena cavă superioară și venele centrale
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Venoasă CTV
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Vena cavă inferioară și afluenții săi
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă CTV
  fov: Torace-Abdomen-Pelvis
  kernel: Standard
  notes: MIP pe întregul sistem venos cav
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă CTV
  fov: Torace-Abdomen-Pelvis
  kernel: Standard
  notes: Flebogramă sagitală
  plane: Sagital
  thickness_increment: 2.5 mm/2.5 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 120-180 sec
  end: Femur proximal
  name: Fază Venoasă CTV
  notes: Fază venoasă extinsă pentru vizualizarea ambelor vene cave
  start: Apertura toracică superioară
  thickness: 0.625 mm
slug: ctv-chest-abdomen-pelvis
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Flebo-CT (CTV) Torace-Abdomen-Pelvis (Sindrom Cav Superior / Inferior)
---

# Flebo-CT (CTV) Torace-Abdomen-Pelvis (Sindrom Cav Superior / Inferior)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Venoasă CTV | 120-180 sec | Apertura toracică superioară → Femur proximal |

    === "Indicații Clinice"

        - Sindrom de venă cavă superioară (SVCS)
        - Ocluzie sau tromboză a axelor venoase centrale (catetere, port-a-cath, pacemaker)
        - Stadializare tumorală cu suspiciune de invazie sau tromboză venoasă tumorală cavă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 2.0 mL/kg |
        | Rată de Flux | 3 mL/s |
        | Durată | 40s |
        | Metodă Temporizare | Timp fix de întârziere (120-180s) |
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
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare la 120-180 secunde. Include de la vena jugulară/subclavie până la venele femurale. Pentru evaluarea optimă a VCS poate fi indicată injectare bilaterală la nivelul ambelor brațe.

    === "Note Asistent"

        - Linie venoasă 18-20G; luați în considerare abord venos la ambele brațe dacă se investighează ocluzia VCS.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați calibrul și permeabilitatea VCS, VCI și a principalilor afluenți. Căutați tromboză, compresiune extrinsecă sau manșonare tumorală. Identificați rețeaua colaterală venoasă mediastinală sau parietală.

    === "Sfaturi & Recomandări"

        - Brațele ridicate. Pentru VCS este preferabilă injectarea în ambele brațe pentru a evita artefactele masive unilaterale.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Venoasă CTV | Apertura toracică superioară | Femur proximal | 120-180 sec | 0.625 mm | Fază venoasă extinsă pentru vizualizarea ambelor vene cave |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Venoasă CTV | Torace | 2 mm/2 mm | Standard |  | Vena cavă superioară și venele centrale |
    | Axial | Fază Venoasă CTV | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Vena cavă inferioară și afluenții săi |
    | Coronal | Fază Venoasă CTV | Torace-Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | MIP pe întregul sistem venos cav |
    | Sagital | Fază Venoasă CTV | Torace-Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Flebogramă sagitală |
