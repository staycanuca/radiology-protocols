---
author: MDCT.net / Multidetector CT Practical Guide
category: neuro
clinical_indications:
- 'Evaluare CT dedicată: Spine-Thoracic and Lumbar'
- Protocol tehnic optimizat pentru scanerul GE – LightSpeed 16-slice
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
  chapter: Coloană vertebrală & Traumatisme
  radiation_dose: Clasa 3 (Moderată 4 - 8 mSv)
  recommendation_grade: Grad B
last_updated: '2026-09-20'
modality: ct
notes:
  additional_recons: Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR
    la stația de post-procesare.
  nursing: Nu necesită linie venoasă dedicată.
  rad: Examinare optimizată pentru Spine-Thoracic and Lumbar. Analiză multiplanară
    axială, coronală și sagitală.
  tech: 'Protocol calibrat pentru platforma GE – LightSpeed 16-slice. Parametri de
    achiziție conform ghidului practic MDCT.net. Detalii producător: Protocol Details.'
  tips: Utilizați reconstrucția iterativă specifică producătorului pentru menținerea
    raportului semnal-zgomot la doze scăzute de radiație.
npo: Nu este necesar
position: Decubit dorsal
premedication: Conform ghidului MDCT.net pentru GE – LightSpeed 16-slice
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
  end: Conform ariei clinice de interes
  name: Achiziție CT Spine-Thoracic and Lumbar
  notes: 'Scaner: GE – LightSpeed 16-slice | Direcție: Cephalocaudal'
  start: Conform ariei clinice de interes
  thickness: 0.5 - 0.625 mm
slug: ct-mdct-spine-thoracic-and-lumbar-ge-lightspeed-16-slice-6
tech_params:
  collimation: 0.5 - 0.625 mm
  kv: 100-120 kV
  mas: Modulare automată (SUREExposure / CAREDose)
  pitch: 0.8 - 1.2
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal / Volumetric (Cephalocaudal)
  slice_thickness: 0.5 - 0.625 mm
title: CT Spine-Thoracic and Lumbar (GE – LightSpeed 16-slice)
---

# CT Spine-Thoracic and Lumbar (GE – LightSpeed 16-slice)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT Spine-Thoracic and Lumbar | Bolus tracking / SureStart | Conform ariei clinice de interes → Conform ariei clinice de interes |

    === "Indicații Clinice"

        - Evaluare CT dedicată: Spine-Thoracic and Lumbar
        - Protocol tehnic optimizat pentru scanerul GE – LightSpeed 16-slice
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Coloană vertebrală & Traumatisme*
            - **Grad de Recomandare:** **Grad B**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 4 - 8 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal
    - **Repaus Alimentar (NPO):** Nu este necesar
    - **Premedicație / Pregătire:**
        - Conform ghidului MDCT.net pentru GE – LightSpeed 16-slice

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Modulare automată (SUREExposure / CAREDose) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.5 - 0.625 mm |
    | **Colimare Detector** | 0.5 - 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (Cephalocaudal) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma GE – LightSpeed 16-slice. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Protocol Details.

    === "Note Asistent"

        - Nu necesită linie venoasă dedicată.

        !!! warning "Siguranță"
            - **Funcție Renală:** Fără restricții renale.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru Spine-Thoracic and Lumbar. Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT Spine-Thoracic and Lumbar | Conform ariei clinice de interes | Conform ariei clinice de interes | Bolus tracking / SureStart | 0.5 - 0.625 mm | Scaner: GE – LightSpeed 16-slice | Direcție: Cephalocaudal |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | Axial 1-3 mm | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | 0.5 - 1.0 mm izotrop | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | Coronal / Sagital 2-3 mm, MIP 5-10 mm | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
