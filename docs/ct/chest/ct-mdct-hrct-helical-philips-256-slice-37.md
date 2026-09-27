---
author: MDCT.net / Multidetector CT Practical Guide
category: chest
clinical_indications:
- 'Evaluare CT dedicată: HRCT (Helical)'
- Protocol tehnic optimizat pentru scanerul Philips – 256-slice
- Conform ghidului practic multidetector CT (MDCT.net)
contrast:
  agent: FĂRĂ
  duration: N/A
  flow_rate: N/A
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: N/A
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 3 (Moderată 5 - 8 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: ct
notes:
  additional_recons: Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR
    la stația de post-procesare.
  nursing: Nu necesită linie venoasă dedicată.
  rad: Examinare optimizată pentru HRCT (Helical). Analiză multiplanară axială, coronală
    și sagitală.
  tech: 'Protocol calibrat pentru platforma Philips – 256-slice. Parametri de achiziție
    conform ghidului practic MDCT.net. Detalii producător: Acquisition parameters
    (scout); Acquisition parameters (inspirational scan); Acquisition parameters (additional
    scans); Reconstruction parameters, overview (for PACS); Reconstruction parameters,
    HRCT (for PACS); Reconstruction parameters (for worksta.'
  tips: Utilizați reconstrucția iterativă specifică producătorului pentru menținerea
    raportului semnal-zgomot la doze scăzute de radiație.
npo: Nu este necesar
position: Prone (insp)
premedication: Conform ghidului MDCT.net pentru Philips – 256-slice
protocol_type: native
recons:
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR)
  kernel: Standard / Țesut moale / Osos
  notes: Serie diagnostică primară
  plane: Axial
  thickness_increment: Axial 1-3 mm
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Standard
  notes: Reconstrucții multiplanare izotrope fine
  plane: Coronal & Sagital
  thickness_increment: 0.5 - 1.0 mm izotrop
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Vascular / 3D
  notes: Reconstrucții angiografice și de volum
  plane: MIP / 3D VR
  thickness_increment: Coronal / Sagital 2-3 mm, MIP 5-10 mm
safety:
  allergy: Screening alergologic conform ghidului MDCT.net și IRIS.
  renal: Fără restricții renale.
series:
- delay: Bolus tracking / SureStart
  end: bases
  name: Achiziție CT HRCT (Helical)
  notes: 'Scaner: Philips – 256-slice | Direcție: Cephalocaudal'
  start: Apices
  thickness: 0.5 - 0.625 mm
slug: ct-mdct-hrct-helical-philips-256-slice-37
tech_params:
  collimation: 0.5 - 0.625 mm
  kv: 120 kV
  mas: Modulare automată (SUREExposure / CAREDose)
  pitch: 0.8 - 1.2
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal / Volumetric (Cephalocaudal)
  slice_thickness: 0.5 - 0.625 mm
title: CT HRCT (Helical) (Philips – 256-slice)
---

# CT HRCT (Helical) (Philips – 256-slice)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT HRCT (Helical) | Bolus tracking / SureStart | Apices → bases |

    === "Indicații Clinice"

        - Evaluare CT dedicată: HRCT (Helical)
        - Protocol tehnic optimizat pentru scanerul Philips – 256-slice
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 8 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Prone (insp)
    - **Repaus Alimentar (NPO):** Nu este necesar
    - **Premedicație / Pregătire:**
        - Conform ghidului MDCT.net pentru Philips – 256-slice

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Modulare automată (SUREExposure / CAREDose) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.5 - 0.625 mm |
    | **Colimare Detector** | 0.5 - 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (Cephalocaudal) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma Philips – 256-slice. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Acquisition parameters (scout); Acquisition parameters (inspirational scan); Acquisition parameters (additional scans); Reconstruction parameters, overview (for PACS); Reconstruction parameters, HRCT (for PACS); Reconstruction parameters (for worksta.

    === "Note Asistent"

        - Nu necesită linie venoasă dedicată.

        !!! warning "Siguranță"
            - **Funcție Renală:** Fără restricții renale.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru HRCT (Helical). Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT HRCT (Helical) | Apices | bases | Bolus tracking / SureStart | 0.5 - 0.625 mm | Scaner: Philips – 256-slice | Direcție: Cephalocaudal |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | Axial 1-3 mm | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | 0.5 - 1.0 mm izotrop | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | Coronal / Sagital 2-3 mm, MIP 5-10 mm | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
