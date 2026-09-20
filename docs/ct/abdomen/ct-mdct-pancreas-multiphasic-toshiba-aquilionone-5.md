---
author: MDCT.net / Multidetector CT Practical Guide
category: abdomen
clinical_indications:
- 'Evaluare CT dedicată: Pancreas (Multiphasic)'
- Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
- Conform ghidului practic multidetector CT (MDCT.net)
contrast:
  agent: Iohexol / Iopamidol / Iomeprol (400 mg I/mL)
  duration: 50 s
  flow_rate: 2 mL/s
  roi: Aortă / Arteră de referință
  timing: SureStart at 180 HU in the abdominal aorta plus 10 sec for the arterial
    phase
  trigger: 120 - 180 HU
  volume: 100 mL
last_updated: '2026-09-20'
modality: ct
notes:
  additional_recons: Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR
    la stația de post-procesare.
  nursing: Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte
    de injectare. Flush salin 40-50 mL.
  rad: Examinare optimizată pentru Pancreas (Multiphasic). Analiză multiplanară axială,
    coronală și sagitală.
  tech: 'Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri
    de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast;
    Acquisition Parameters; Reconstruction Parameters; Protocol Details; † Lower kVp
    to 100 or 80 for patients with lower body mass; ‡ Refer to Addendum A for detailed
    explanation of SUREExposure; ◊ Refer to Addendum B for detailed explanation .'
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
  thickness_increment: 3 x 3 mm
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Standard
  notes: Reconstrucții multiplanare izotrope fine
  plane: Coronal & Sagital
  thickness_increment: Body standard volume
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Vascular / 3D
  notes: Reconstrucții angiografice și de volum
  plane: MIP / 3D VR
  thickness_increment: MultiView (Auto MPR selected as desired)
safety:
  allergy: Screening alergologic conform ghidului MDCT.net și IRIS.
  renal: Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
series:
- delay: SureStart at 180 HU in the abdominal aorta plus 10 sec for the arterial phase
  end: crests
  name: Achiziție CT Pancreas (Multiphasic)
  notes: 'Scaner: Canon – Toshiba – AquilionOne | Direcție: Cephalocaudal; table movement
    is “out”'
  start: Diaphragm
  thickness: 0.5 x 32/64 (1 x 16/32 for larger abdomen)
slug: ct-mdct-pancreas-multiphasic-toshiba-aquilionone-5
tech_params:
  collimation: 0.5 x 32/64 (1 x 16/32 for larger abdomen)
  kv: 120 † kV
  mas: SUREExposure ‡
  pitch: 0.8 - 1.2
  rotation_time: 0.5 (0.75 for larger abdomen) s
  scan_mode: Elicoidal / Volumetric (Cephalocaudal; table movement is “out”)
  slice_thickness: 0.5 x 32/64 (1 x 16/32 for larger abdomen)
title: CT Pancreas (Multiphasic) (Canon – Toshiba – AquilionOne)
---

# CT Pancreas (Multiphasic) (Canon – Toshiba – AquilionOne)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT Pancreas (Multiphasic) | SureStart at 180 HU in the abdominal aorta plus 10 sec for the arterial phase | Diaphragm → crests |

    === "Indicații Clinice"

        - Evaluare CT dedicată: Pancreas (Multiphasic)
        - Protocol tehnic optimizat pentru scanerul Canon – Toshiba – AquilionOne
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
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
        | Rată de Flux | 2 mL/s |
        | Durată | 50 s |
        | Metodă Temporizare | SureStart at 180 HU in the abdominal aorta plus 10 sec for the arterial phase |
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
    | **Tensiune Tub (kV)** | 120 † kV |
    | **Curent Tub (mAs)** | SUREExposure ‡ |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.5 x 32/64 (1 x 16/32 for larger abdomen) |
    | **Colimare Detector** | 0.5 x 32/64 (1 x 16/32 for larger abdomen) |
    | **Timp de Rotație** | 0.5 (0.75 for larger abdomen) s |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (Cephalocaudal; table movement is “out”) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma Canon – Toshiba – AquilionOne. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast; Acquisition Parameters; Reconstruction Parameters; Protocol Details; † Lower kVp to 100 or 80 for patients with lower body mass; ‡ Refer to Addendum A for detailed explanation of SUREExposure; ◊ Refer to Addendum B for detailed explanation .

    === "Note Asistent"

        - Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte de injectare. Flush salin 40-50 mL.

        !!! warning "Siguranță"
            - **Funcție Renală:** Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru Pancreas (Multiphasic). Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT Pancreas (Multiphasic) | Diaphragm | crests | SureStart at 180 HU in the abdominal aorta plus 10 sec for the arterial phase | 0.5 x 32/64 (1 x 16/32 for larger abdomen) | Scaner: Canon – Toshiba – AquilionOne | Direcție: Cephalocaudal; table movement is “out” |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | 3 x 3 mm | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | Body standard volume | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | MultiView (Auto MPR selected as desired) | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
