---
author: null
category: msk
clinical_indications:
- Fracturi de oase tarsiene (calcaneu, talus, navicular, cuboid, cuneiforme)
- Leziune sau disjuncție a articulației Lisfranc sau Chopart
- Fracturi de metatarsiene și falange
- Corpi străini radiopaci / planificare chirurgicală osteosinteză
contrast:
  agent: Nativ de regulă. Contrast dacă se suspectează flegmon / osteomielită
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 75 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții oblice în axul lung al articulației Lisfranc. Măsurarea
    unghiurilor calcaneene. Randare 3D VR.
  nursing: Fără linie venoasă de rutină.
  rad: Fracturi de calcaneu (măsurarea unghiului Böhler și Gissane, afectarea fațetei
    posterioare subtalare). Aliniamentul liniei articulare Lisfranc (baza metatarsianului
    II cu cuneiformul intermediar). Fragmente intraarticulare.
  tech: De la tuberozitatea calcaneului până la vârful degetelor. Achiziție submilimetrică.
    Examinare bilaterală utilă pentru comparația aliniamentului tarsian.
  tips: Comparația bilaterală ajută la confirmarea subluxațiilor discrete Lisfranc.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu genunchii flectați și talpa sprijinită pe masa de examinare
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Picior
  fov: Picior
  kernel: Bone
  notes: Fereastră osoasă în axul lung al piciorului
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Picior
  fov: Picior
  kernel: Bone
  notes: Plan coronal perpendicular pe metatarsiene
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Picior
  fov: Picior
  kernel: Bone
  notes: Plan sagital pentru bolta plantară și calcaneu
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Picior
  fov: Picior
  kernel: Bone
  notes: Plan oblic dedicat articulației Lisfranc
  plane: Oblique
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Degete picioare
  name: CT Picior
  notes: Achiziție elicoidală submilimetrică
  start: Calcaneu
  thickness: 0.625 mm
slug: ct-foot
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
title: CT Picior
---

# CT Picior

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Picior | 0 sec | Calcaneu → Degete picioare |

    === "Indicații Clinice"

        - Fracturi de oase tarsiene (calcaneu, talus, navicular, cuboid, cuneiforme)
        - Leziune sau disjuncție a articulației Lisfranc sau Chopart
        - Fracturi de metatarsiene și falange
        - Corpi străini radiopaci / planificare chirurgicală osteosinteză

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu genunchii flectați și talpa sprijinită pe masa de examinare
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se suspectează flegmon / osteomielită |
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

        - De la tuberozitatea calcaneului până la vârful degetelor. Achiziție submilimetrică. Examinare bilaterală utilă pentru comparația aliniamentului tarsian.

    === "Note Asistent"

        - Fără linie venoasă de rutină.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Fracturi de calcaneu (măsurarea unghiului Böhler și Gissane, afectarea fațetei posterioare subtalare). Aliniamentul liniei articulare Lisfranc (baza metatarsianului II cu cuneiformul intermediar). Fragmente intraarticulare.

    === "Sfaturi & Recomandări"

        - Comparația bilaterală ajută la confirmarea subluxațiilor discrete Lisfranc.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Picior | Calcaneu | Degete picioare | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Picior | Picior | 1 mm/1 mm | Bone |  | Fereastră osoasă în axul lung al piciorului |
    | Coronal | CT Picior | Picior | 1 mm/1 mm | Bone |  | Plan coronal perpendicular pe metatarsiene |
    | Sagital | CT Picior | Picior | 1 mm/1 mm | Bone |  | Plan sagital pentru bolta plantară și calcaneu |
    | Oblique | CT Picior | Picior | 1 mm/1 mm | Bone |  | Plan oblic dedicat articulației Lisfranc |
