---
author: MDCT.net / Multidetector CT Practical Guide
category: cardiac
clinical_indications:
- 'Evaluare CT dedicată: Aortic dissection'
- Protocol tehnic optimizat pentru scanerul Canon – Toshiba – Aquilion 64 CFX
- Conform ghidului practic multidetector CT (MDCT.net)
contrast:
  agent: Iohexol / Iopamidol / Iomeprol (400 mg I/mL)
  duration: 20 s
  flow_rate: 5 mL/s
  roi: Aortă / Arteră de referință
  timing: SureStart in the descending aorta at 180 HU
  trigger: 120 - 180 HU
  volume: 100 mL
last_updated: '2026-09-20'
modality: ct
notes:
  additional_recons: Reconstrucții multiplanare MPR, MIP și randare de volum 3D VR
    la stația de post-procesare.
  nursing: Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte
    de injectare. Flush salin 40-50 mL.
  rad: Examinare optimizată pentru Aortic dissection. Analiză multiplanară axială,
    coronală și sagitală.
  tech: 'Protocol calibrat pentru platforma Canon – Toshiba – Aquilion 64 CFX. Parametri
    de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters;
    Acquisition Parameters; Reconstruction Parameters; Protocol Details; noncontrast
    imaging can be performed at the discretion of the trauma care specialist and radiologist;
    † Refer to Addendum A for detailed explanation of SUREExpo.'
  tips: Utilizați reconstrucția iterativă specifică producătorului pentru menținerea
    raportului semnal-zgomot la doze scăzute de radiație.
npo: Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă
position: Supine, feet first
premedication: Conform ghidului MDCT.net pentru Canon – Toshiba – Aquilion 64 CFX
protocol_type: contrast-enhanced
recons:
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR)
  kernel: Standard / Țesut moale / Osos
  notes: Serie diagnostică primară
  plane: Axial
  thickness_increment: Axial 1 (3 x 3 mm) soft tissue; Axial 2 (3 x 3 mm) lung (if
    desired)
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Standard
  notes: Reconstrucții multiplanare izotrope fine
  plane: Coronal & Sagital
  thickness_increment: Volume 0.5 x 0.5 mm (or 20% overlap 0.5 x 0.3 mm if desired)
- acquisition: MDCT Volumetric
  fov: Adaptat anatomic
  ir_strength: Standard
  kernel: Vascular / 3D
  notes: Reconstrucții angiografice și de volum
  plane: MIP / 3D VR
  thickness_increment: AUTO MIP (coronal/sagittal)
safety:
  allergy: Screening alergologic conform ghidului MDCT.net și IRIS.
  renal: Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
series:
- delay: SureStart in the descending aorta at 180 HU
  end: Above the aortic arch through the bifurcation
  name: Achiziție CT Aortic dissection
  notes: 'Scaner: Canon – Toshiba – Aquilion 64 CFX | Direcție: Cephalocaudal'
  start: Above the aortic arch through the bifurcation
  thickness: 0.5 x (32/64)
slug: ct-mdct-aortic-dissection-toshiba-aquilion-64-cfx-10
tech_params:
  collimation: 0.5 x (32/64)
  kv: 120 kV
  mas: SUREExposure †
  pitch: 0.8 - 1.2
  rotation_time: 0.5 s
  scan_mode: Elicoidal / Volumetric (Cephalocaudal)
  slice_thickness: 0.5 x (32/64)
title: CT Aortic dissection (Canon – Toshiba – Aquilion 64 CFX)
---

# CT Aortic dissection (Canon – Toshiba – Aquilion 64 CFX)

**Ultima actualizare:** 2026-09-20
**Autor:** MDCT.net / Multidetector CT Practical Guide

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție CT Aortic dissection | SureStart in the descending aorta at 180 HU | Above the aortic arch through the bifurcation → Above the aortic arch through the bifurcation |

    === "Indicații Clinice"

        - Evaluare CT dedicată: Aortic dissection
        - Protocol tehnic optimizat pentru scanerul Canon – Toshiba – Aquilion 64 CFX
        - Conform ghidului practic multidetector CT (MDCT.net)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Supine, feet first
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore înainte de scanare; hidratare orală permisă
    - **Premedicație / Pregătire:**
        - Conform ghidului MDCT.net pentru Canon – Toshiba – Aquilion 64 CFX

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Iohexol / Iopamidol / Iomeprol (400 mg I/mL) |
        | Volum | 100 mL |
        | Rată de Flux | 5 mL/s |
        | Durată | 20 s |
        | Metodă Temporizare | SureStart in the descending aorta at 180 HU |
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
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.5 x (32/64) |
    | **Colimare Detector** | 0.5 x (32/64) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.2 |
    | **Mod Scanare** | Elicoidal / Volumetric (Cephalocaudal) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol calibrat pentru platforma Canon – Toshiba – Aquilion 64 CFX. Parametri de achiziție conform ghidului practic MDCT.net. Detalii producător: Contrast Parameters; Acquisition Parameters; Reconstruction Parameters; Protocol Details; noncontrast imaging can be performed at the discretion of the trauma care specialist and radiologist; † Refer to Addendum A for detailed explanation of SUREExpo.

    === "Note Asistent"

        - Canulă 18-20G antecubitală pentru debite > 3 mL/s. Verificare debit înainte de injectare. Flush salin 40-50 mL.

        !!! warning "Siguranță"
            - **Funcție Renală:** Evaluare eGFR > 30 mL/min/1.73m² pre-contrast.
            - **Alergii:** Screening alergologic conform ghidului MDCT.net și IRIS.

    === "Note Radiolog"

        - Examinare optimizată pentru Aortic dissection. Analiză multiplanară axială, coronală și sagitală.

    === "Sfaturi & Recomandări"

        - Utilizați reconstrucția iterativă specifică producătorului pentru menținerea raportului semnal-zgomot la doze scăzute de radiație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție CT Aortic dissection | Above the aortic arch through the bifurcation | Above the aortic arch through the bifurcation | SureStart in the descending aorta at 180 HU | 0.5 x (32/64) | Scaner: Canon – Toshiba – Aquilion 64 CFX | Direcție: Cephalocaudal |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | MDCT Volumetric | Adaptat anatomic | Axial 1 (3 x 3 mm) soft tissue; Axial 2 (3 x 3 mm) lung (if desired) | Standard / Țesut moale / Osos | Iterative Reconstruction activată (AIDR 3D / SAFIRE / ASiR) | Serie diagnostică primară |
    | Coronal & Sagital | MDCT Volumetric | Adaptat anatomic | Volume 0.5 x 0.5 mm (or 20% overlap 0.5 x 0.3 mm if desired) | Standard | Standard | Reconstrucții multiplanare izotrope fine |
    | MIP / 3D VR | MDCT Volumetric | Adaptat anatomic | AUTO MIP (coronal/sagittal) | Vascular / 3D | Standard | Reconstrucții angiografice și de volum |
