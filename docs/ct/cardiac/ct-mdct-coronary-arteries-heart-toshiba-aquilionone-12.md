---
author: MDCT.net / Multidetector CT Practical Guide
category: cardiac
clinical_indications:
- 'Evaluare CT dedicată: Coronary Arteries, Heart'
- Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
- Conform ghidului practic multidetector CT (MDCT.net)
contrast:
  agent: Iohexol / Iopamidol / Iomeprol (400 mg I/mL)
  duration: 10.9 s
  flow_rate: 5.5 mL/s
  roi: Aortă / Arteră de referință
  timing: SureStart in the ascending aorta at 180 HU
  trigger: 120 - 180 HU
  volume: 60 mL
iris_reference:
  chapter: Aparat cardiovascular (Cord)
  radiation_dose: Clasa 3 (Moderată 4 - 8 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: ct
notes:
  additional_recons: Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR
    la stația de post-procesare.
  nursing: Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte
    de injectare. Flush salin 40-50 mL.
  rad: Examinare optimizată pentru Coronary Arteries, Heart. Analiză multiplanară
    axială, coronală și sagitală.
  tech: 'Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri
    de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters;
    Acquisition Parameters; Reconstruction Parameters; Protocol Details; *See page
    3 of Toshiba Cardiac 10 Step Guide for more detail; † Refer to Addendum C for
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
  thickness_increment: 'CTA: Volume 0.5 x 0.5 mm (or 50% overlap 0.5 x 0.25 mm if
    desired); Full FOV: 3 x 3 mm axial'
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
  thickness_increment: 3D/MPR as requested
safety:
  allergy: Screening alergologic conform ghidului MDCT.net și IRIS.
  renal: Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
series:
- delay: SureStart in the ascending aorta at 180 HU
  end: the cardiac apex
  name: Achiziție CT Coronary Arteries, Heart
  notes: 'Scaner: Canon – Toshiba – AquilionOne | Direcție: None'
  start: Carina
  thickness: 0.5 x 320
slug: ct-mdct-coronary-arteries-heart-toshiba-aquilionone-12
tech_params:
  collimation: 0.5 x 320
  kv: 100, 120 kV
  mas: 350-580
  pitch: 0.8 - 1.2
  rotation_time: Toshiba-automated optimization (SureCardio), heart rate dependent
  scan_mode: Elicoidal / Volumetric (None)
  slice_thickness: 0.5 x 320
title: CT Coronary Arteries, Heart (Canon – Toshiba – AquilionOne)
---

# CT Coronary Arteries, Heart (Canon – Toshiba – AquilionOne)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT Coronary Arteries, Heart | SureStart in the ascending aorta at 180 HU | Carina → the cardiac apex |

    === "Indicații Clinice"

        - Evaluare CT dedicată: Coronary Arteries, Heart
        - Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat cardiovascular (Cord)*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 4 - 8 mSv)`

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
        | Volum | 60 mL |
        | Rată de Flux | 5.5 mL/s |
        | Durată | 10.9 s |
        | Metodă Temporizare | SureStart in the ascending aorta at 180 HU |
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
    | **Tensiune Tub (kV)** | 100, 120 kV |
    | **Curent Tub (mAs)** | 350-580 |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.5 x 320 |
    | **Colimare Detector** | 0.5 x 320 |
    | **Timp de Rotație** | Toshiba-automated optimization (SureCardio), heart rate dependent |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (None) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters; Acquisition Parameters; Reconstruction Parameters; Protocol Details; *See page 3 of Toshiba Cardiac 10 Step Guide for more detail; † Refer to Addendum C for detailed explanation of SURE IQ.

    === "Note Asistent"

        - Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte de injectare. Flush salin 40-50 mL.

        !!! warning "Siguranță"
            - **Funcție Renală:** Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru Coronary Arteries, Heart. Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT Coronary Arteries, Heart | Carina | the cardiac apex | SureStart in the ascending aorta at 180 HU | 0.5 x 320 | Scaner: Canon – Toshiba – AquilionOne | Direcție: None |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | CTA: Volume 0.5 x 0.5 mm (or 50% overlap 0.5 x 0.25 mm if desired); Full FOV: 3 x 3 mm axial | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | 0.5 - 1.0 mm izotrop | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | 3D/MPR as requested | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
