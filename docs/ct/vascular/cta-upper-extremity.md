---
author: null
category: vascular
clinical_indications:
- Insuficiență arterială a membrului superior / ischemie acută sau cronică
- Traumatism vascular penetrant sau închis al brațului
- Planificare acces vascular pentru hemodializă (fistulă arteriovenoasă)
- Sindrom de apertură toracică superioară (Thoracic Outlet Syndrome - TOS)
contrast:
  agent: Isovue 370
  flow_rate: 4 mL/s
  roi: Artera subclavie
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: MIP și randare 3D VR. Tehnici de substracție osoasă pentru claritatea
    axului vascular.
  nursing: Linie venoasă 20G plasată în brațul CONTROLATERAL.
  rad: Evaluați arterele subclavie, axilară, brahială, radială, ulnară și arcadele
    palmare. Căutați stenoze, tromboze, anevrisme sau compresiuni extrinseci la nivelul
    defileului costoclavicular.
  tech: Scanare de la nivelul arcului aortic până la vârful degetelor. Se poate efectua
    examinare bilaterală dacă este necesară comparația. Poziționați brațul pentru
    a evidenția patologia. Injectarea se realizează OBLIGATORIU în brațul contralateral.
  tips: Poziționarea atentă a brațului pentru a evita artefactele pe torace. În suspiciunea
    de sindrom de defileu (TOS), pot fi necesare manevre dinamice (braț în adducție
    vs. abducție-rotație externă).
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațul afectat ridicat deasupra capului sau de-a lungul
  corpului
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial
  fov: Membru superior
  kernel: Vascular
  notes: Serie diagnostică primară
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Arterial
  fov: Membru superior
  kernel: Vascular
  notes: MIP pe întregul traiect al vaselor membrului superior
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Arterial
  fov: Membru superior
  kernel: Vascular
  notes: MIP sagital pe traiectul brahial și antebraț
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Arterial
  fov: Membru superior
  kernel: Vascular
  notes: Randare tridimensională 3D a axului arterial
  plane: 3D VR
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Vârful degetelor
  name: Angio-CT Arterial
  notes: Acoperire de la arcul aortic până la mâna afectată
  start: Arc aortic
  thickness: 0.625 mm
slug: cta-upper-extremity
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200 mAs)
  pitch: '0.9'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Membru Superior
---

# Angio-CT Membru Superior

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial | Urmărire bolus | Arc aortic → Vârful degetelor |

    === "Indicații Clinice"

        - Insuficiență arterială a membrului superior / ischemie acută sau cronică
        - Traumatism vascular penetrant sau închis al brațului
        - Planificare acces vascular pentru hemodializă (fistulă arteriovenoasă)
        - Sindrom de apertură toracică superioară (Thoracic Outlet Syndrome - TOS)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațul afectat ridicat deasupra capului sau de-a lungul corpului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 100 mL |
        | Rată de Flux | 4 mL/s |
        | Durată |  |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Artera subclavie |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare de la nivelul arcului aortic până la vârful degetelor. Se poate efectua examinare bilaterală dacă este necesară comparația. Poziționați brațul pentru a evidenția patologia. Injectarea se realizează OBLIGATORIU în brațul contralateral.

    === "Note Asistent"

        - Linie venoasă 20G plasată în brațul CONTROLATERAL.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați arterele subclavie, axilară, brahială, radială, ulnară și arcadele palmare. Căutați stenoze, tromboze, anevrisme sau compresiuni extrinseci la nivelul defileului costoclavicular.

    === "Sfaturi & Recomandări"

        - Poziționarea atentă a brațului pentru a evita artefactele pe torace. În suspiciunea de sindrom de defileu (TOS), pot fi necesare manevre dinamice (braț în adducție vs. abducție-rotație externă).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial | Arc aortic | Vârful degetelor | Urmărire bolus | 0.625 mm | Acoperire de la arcul aortic până la mâna afectată |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial | Membru superior | 1 mm/1 mm | Vascular |  | Serie diagnostică primară |
    | Coronal | Angio-CT Arterial | Membru superior | 1.5 mm/1.5 mm | Vascular |  | MIP pe întregul traiect al vaselor membrului superior |
    | Sagital | Angio-CT Arterial | Membru superior | 1.5 mm/1.5 mm | Vascular |  | MIP sagital pe traiectul brahial și antebraț |
    | 3D VR | Angio-CT Arterial | Membru superior | 0.75 mm/0.75 mm | Vascular |  | Randare tridimensională 3D a axului arterial |
