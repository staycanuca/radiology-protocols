---
author: MDCT.net / Multidetector CT Practical Guide
category: vascular
clinical_indications:
- 'Evaluare CT dedicată: Peripheral Artery Disease'
- Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
- Conform ghidului practic multidetector CT (MDCT.net)
contrast:
  agent: Iohexol / Iopamidol / Iomeprol (400 mg I/mL)
  duration: 25 s
  flow_rate: 4 mL/s
  roi: Aortă / Arteră de referință
  timing: SureStart just above the aortic bifurcation at 200 HU
  trigger: 120 - 180 HU
  volume: 100 mL
iris_reference:
  chapter: Aparat cardiovascular & Sistem vascular
  radiation_dose: Clasa 4 (Ridicată > 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: ct
notes:
  additional_recons: Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR
    la stația de post-procesare.
  nursing: Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte
    de injectare. Flush salin 40-50 mL.
  rad: Examinare optimizată pentru Peripheral Artery Disease. Analiză multiplanară
    axială, coronală și sagitală.
  tech: 'Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri
    de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters;
    Acquisition Parameters; Reconstruction Parameters; Protocol Details; † Refer to
    Addendum A for detailed explanation of SUREExposure; ‡ Refer to Addendum C for
    detailed explanation of SURE IQ.'
  tips: Utilizați reconstrucția iterativă specifică producătorului pentru menținerea
    raportului semnal-zgomot la doze scăzute de radiație.
npo: Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă
position: Supine, feet first
premedication: Conform ghidului MDCT.net pentru Canon – Toshiba – AquilionOne
protocol_type: contrast-enhanced
recons:
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR)
  kernel: Standard / Țesut moale / Osos
  notes: Serie diagnostică primară
  plane: Axial
  thickness_increment: Volume 1 x 0.8 mm (Noncontrast and contrast scans)
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
  renal: Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
series:
- delay: SureStart just above the aortic bifurcation at 200 HU
  end: 'toes (Note: Noncontrast scan must be performed first with same parameters)'
  name: Achiziție CT Peripheral Artery Disease
  notes: 'Scaner: Canon – Toshiba – AquilionOne | Direcție: Cephalocaudal'
  start: Above diaphragm
  thickness: 0.5 x 64
slug: ct-mdct-peripheral-artery-disease-toshiba-aquilionone-15
tech_params:
  collimation: 0.5 x 64
  kv: 120 kV
  mas: SUREExposure †
  pitch: 0.8 - 1.2
  rotation_time: 0.5 s
  scan_mode: Elicoidal / Volumetric (Cephalocaudal)
  slice_thickness: 0.5 x 64
title: CT Peripheral Artery Disease (Canon – Toshiba – AquilionOne)
---

# CT Peripheral Artery Disease (Canon – Toshiba – AquilionOne)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT Peripheral Artery Disease | SureStart just above the aortic bifurcation at 200 HU | Above diaphragm → toes (Note: Noncontrast scan must be performed first with same parameters) |

    === "Indicații Clinice"

        - Evaluare CT dedicată: Peripheral Artery Disease
        - Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat cardiovascular & Sistem vascular*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 4 (Ridicată > 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Supine, feet first
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă
    - **Premedicație / Pregătire:**
        - Conform ghidului MDCT.net pentru Canon – Toshiba – AquilionOne

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Iohexol / Iopamidol / Iomeprol (400 mg I/mL) |
        | Volum | 100 mL |
        | Rată de Flux | 4 mL/s |
        | Durată | 25 s |
        | Metodă Temporizare | SureStart just above the aortic bifurcation at 200 HU |
        | Poziționare ROI | Aortă / Arteră de referință |
        | Declanșator (HU) | 120 - 180 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | SUREExposure † |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.5 x 64 |
    | **Colimare Detector** | 0.5 x 64 |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (Cephalocaudal) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters; Acquisition Parameters; Reconstruction Parameters; Protocol Details; † Refer to Addendum A for detailed explanation of SUREExposure; ‡ Refer to Addendum C for detailed explanation of SURE IQ.

    === "Note Asistent"

        - Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte de injectare. Flush salin 40-50 mL.

        !!! warning "Siguranță"
            - **Funcție Renală:** Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru Peripheral Artery Disease. Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT Peripheral Artery Disease | Above diaphragm | toes (Note: Noncontrast scan must be performed first with same parameters) | SureStart just above the aortic bifurcation at 200 HU | 0.5 x 64 | Scaner: Canon – Toshiba – AquilionOne | Direcție: Cephalocaudal |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | Volume 1 x 0.8 mm (Noncontrast and contrast scans) | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | 0.5 - 1.0 mm izotrop | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | Coronal / Sagital 2-3 mm, MIP 5-10 mm | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
