---
author: MDCT.net / Multidetector CT Practical Guide
category: cardiac
clinical_indications:
- 'Evaluare CT dedicată: Neuro CTA-Carotid Vascular Trauma'
- Protocol tehnic optimizat pentru scanerul Canon – Toshiba – Aquilion 16 CFX
- Conform ghidului practic multidetector CT (MDCT.net)
contrast:
  agent: Iohexol / Iopamidol / Iomeprol (400 mg I/mL)
  duration: 22.2 s
  flow_rate: 4.5 mL/s
  roi: Aortă / Arteră de referință
  timing: SureStart, manually start on aortic arch when blushing of arch occurs with
    contrast
  trigger: 120 - 180 HU
  volume: 100 mL
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
  rad: Examinare optimizată pentru Neuro CTA-Carotid Vascular Trauma. Analiză multiplanară
    axială, coronală și sagitală.
  tech: 'Protocol calibrat pentru platforma Canon – Toshiba – Aquilion 16 CFX. Parametri
    de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast;
    Acquisition Parameters; Recon Detail; Protocol Details; None.'
  tips: Utilizați reconstrucția iterativă specifică producătorului pentru menținerea
    raportului semnal-zgomot la doze scăzute de radiație.
npo: Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă
position: Decubit dorsal
premedication: Conform ghidului MDCT.net pentru Canon – Toshiba – Aquilion 16 CFX
protocol_type: contrast-enhanced
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
  renal: Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
series:
- delay: SureStart, manually start on aortic arch when blushing of arch occurs with
    contrast
  end: Circle of Willis
  name: Achiziție CT Neuro CTA-Carotid Vascular Trauma
  notes: 'Scaner: Canon – Toshiba – Aquilion 16 CFX | Direcție: Caudocephalad'
  start: Aortic arch
  thickness: '1'
slug: ct-mdct-neuro-cta-carotid-vascular-trauma-toshiba-aquilion-16-cfx-2
tech_params:
  collimation: '1'
  kv: 120 to 135 kV
  mas: '300'
  pitch: 0.8 - 1.2
  rotation_time: 0.4 to 0.5 s
  scan_mode: Elicoidal / Volumetric (Caudocephalad)
  slice_thickness: '1'
title: CT Neuro CTA-Carotid Vascular Trauma (Canon – Toshiba – Aquilion 16 CFX)
---

# CT Neuro CTA-Carotid Vascular Trauma (Canon – Toshiba – Aquilion 16 CFX)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT Neuro CTA-Carotid Vascular Trauma | SureStart, manually start on aortic arch when blushing of arch occurs with contrast | Aortic arch → Circle of Willis |

    === "Indicații Clinice"

        - Evaluare CT dedicată: Neuro CTA-Carotid Vascular Trauma
        - Protocol tehnic optimizat pentru scanerul Canon – Toshiba – Aquilion 16 CFX
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat cardiovascular (Cord)*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 4 - 8 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă
    - **Premedicație / Pregătire:**
        - Conform ghidului MDCT.net pentru Canon – Toshiba – Aquilion 16 CFX

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Iohexol / Iopamidol / Iomeprol (400 mg I/mL) |
        | Volum | 100 mL |
        | Rată de Flux | 4.5 mL/s |
        | Durată | 22.2 s |
        | Metodă Temporizare | SureStart, manually start on aortic arch when blushing of arch occurs with contrast |
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
    | **Tensiune Tub (kV)** | 120 to 135 kV |
    | **Curent Tub (mAs)** | 300 |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 1 |
    | **Colimare Detector** | 1 |
    | **Timp de Rotație** | 0.4 to 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (Caudocephalad) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma Canon – Toshiba – Aquilion 16 CFX. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast; Acquisition Parameters; Recon Detail; Protocol Details; None.

    === "Note Asistent"

        - Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte de injectare. Flush salin 40-50 mL.

        !!! warning "Siguranță"
            - **Funcție Renală:** Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru Neuro CTA-Carotid Vascular Trauma. Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT Neuro CTA-Carotid Vascular Trauma | Aortic arch | Circle of Willis | SureStart, manually start on aortic arch when blushing of arch occurs with contrast | 1 | Scaner: Canon – Toshiba – Aquilion 16 CFX | Direcție: Caudocephalad |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | Axial 1-3 mm | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | 0.5 - 1.0 mm izotrop | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | Coronal / Sagital 2-3 mm, MIP 5-10 mm | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
