---
author: MDCT.net / Multidetector CT Practical Guide
category: chest
clinical_indications:
- 'Evaluare CT dedicată: Pulmonary Embolism'
- Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
- Conform ghidului practic multidetector CT (MDCT.net)
contrast:
  agent: Iohexol / Iopamidol / Iomeprol (400 mg I/mL)
  duration: 16 s
  flow_rate: 5 mL/s
  roi: Aortă / Arteră de referință
  timing: SureStart in the pulmonary artery at 150 HU
  trigger: 120 - 180 HU
  volume: 80 mL
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 3 (Moderată 5 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: ct
notes:
  additional_recons: Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR
    la stația de post-procesare.
  nursing: Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte
    de injectare. Flush salin 40-50 mL.
  rad: Examinare optimizată pentru Pulmonary Embolism. Analiză multiplanară axială,
    coronală și sagitală.
  tech: 'Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri
    de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters;
    Acquisition Parameters; Reconstruction Parameters; Protocol Details; † Refer to
    Addendum C for detailed explanation of SURE IQ.'
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
  thickness_increment: Axial 1 (5 x 2.5 mm) soft tissue; Axial 2 (5 x 2.5 mm) lung
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Standard
  notes: Reconstrucții multiplanare izotrope fine
  plane: Coronal & Sagital
  thickness_increment: Volume 0.5 x 0.5 mm (or overlap 0.5 x 0.3 mm if desired)
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Vascular / 3D
  notes: Reconstrucții angiografice și de volum
  plane: MIP / 3D VR
  thickness_increment: 'MPR: (coronal/sagittal) 3 x 3 mm; MIP: 7-10 mm with a 50%
    overlap'
safety:
  allergy: Screening alergologic conform ghidului MDCT.net și IRIS.
  renal: Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
series:
- delay: SureStart in the pulmonary artery at 150 HU
  end: costophrenic recess
  name: Achiziție CT Pulmonary Embolism
  notes: 'Scaner: Canon – Toshiba – AquilionOne | Direcție: Cephalocaudal'
  start: Apex of lung
  thickness: 0.5 x 320
slug: ct-mdct-pulmonary-embolism-toshiba-aquilionone-16
tech_params:
  collimation: 0.5 x 320; 0.5 x 64
  kv: 80-120 kV
  mas: 200 to 300
  pitch: 0.8 - 1.2
  rotation_time: 0.35 s
  scan_mode: Elicoidal / Volumetric (Cephalocaudal)
  slice_thickness: 0.5 x 320
title: CT Pulmonary Embolism (Canon – Toshiba – AquilionOne)
---

# CT Pulmonary Embolism (Canon – Toshiba – AquilionOne)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT Pulmonary Embolism | SureStart in the pulmonary artery at 150 HU | Apex of lung → costophrenic recess |

    === "Indicații Clinice"

        - Evaluare CT dedicată: Pulmonary Embolism
        - Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 10 mSv)`

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
        | Volum | 80 mL |
        | Rată de Flux | 5 mL/s |
        | Durată | 16 s |
        | Metodă Temporizare | SureStart in the pulmonary artery at 150 HU |
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
    | **Tensiune Tub (kV)** | 80-120 kV |
    | **Curent Tub (mAs)** | 200 to 300 |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.5 x 320 |
    | **Colimare Detector** | 0.5 x 320; 0.5 x 64 |
    | **Timp de Rotație** | 0.35 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (Cephalocaudal) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters; Acquisition Parameters; Reconstruction Parameters; Protocol Details; † Refer to Addendum C for detailed explanation of SURE IQ.

    === "Note Asistent"

        - Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte de injectare. Flush salin 40-50 mL.

        !!! warning "Siguranță"
            - **Funcție Renală:** Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru Pulmonary Embolism. Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT Pulmonary Embolism | Apex of lung | costophrenic recess | SureStart in the pulmonary artery at 150 HU | 0.5 x 320 | Scaner: Canon – Toshiba – AquilionOne | Direcție: Cephalocaudal |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | Axial 1 (5 x 2.5 mm) soft tissue; Axial 2 (5 x 2.5 mm) lung | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | Volume 0.5 x 0.5 mm (or overlap 0.5 x 0.3 mm if desired) | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | MPR: (coronal/sagittal) 3 x 3 mm; MIP: 7-10 mm with a 50% overlap | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
