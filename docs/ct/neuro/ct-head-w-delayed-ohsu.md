---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Suspiciune de metastaze cerebrale sau tumori primare SNC
- Infecții intracraniene, meningite, empieme, abcese cerebrale
- Leziuni demielinizante atipice în faza activă
- Evaluare post-operatorie de rezecție tumorală cerebrală
contrast:
  agent: Omnipaque 300 / Isovue 370
  duration: 50s
  flow_rate: 2.0 mL/s (Adult) / 1.0-2.0 mL/s (Peds)
  roi: N/A
  timing: Scanare tardivă la 5 minute de la debutul injectării contrastului
  trigger: N/A
  volume: 100 mL (Adult) / 2 mL/kg (Peds, max 100 mL)
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții coronale subțiri pentru evaluarea regiunii selare
    și a fosei posterioare.
  nursing: Supraveghere pacient pe durata intervalului de așteptare de 5 minute.
  rad: Căutați priză de contrast inelară (abces vs glioblastom), noduli corticali/subcorticali
    multipli hipercaptanți (metastaze), încărcare leptomeningeală sau durală.
  tech: Canulă 22G sau mai mare în plica cotului. Respectați cu strictețe intervalul
    de 5 minute de la începutul injectării.
  tips: Dacă este disponibil, RMN-ul cerebral cu contrast este de regulă superior;
    CT-ul cu contrast este rezervat pacienților cu contraindicații RM.
npo: Repaus alimentar 4 ore
position: Decubit dorsal, centrare pe bărbia pacientului
premedication: Fără contrast oral
protocol_type: contrast-enhanced
recons:
- acquisition: CT Craniu Tardiv
  fov: Cap
  ir_strength: Standard
  kernel: Creier (H31s)
  notes: Serii multiplanare cu contrast tardiv
  plane: Axial, Coronal & Sagital (Adult)
  thickness_increment: 5.0 mm / 5.0 mm
- acquisition: CT Craniu Tardiv
  fov: Cap
  ir_strength: Standard
  kernel: Creier Pediatric (H31s)
  notes: Secțiuni de 3 mm adaptate pediatric
  plane: Axial, Coronal & Sagital (Pediatric)
  thickness_increment: 3.0 mm / 3.0 mm
- acquisition: CT Craniu Tardiv
  fov: Cap
  ir_strength: Standard
  kernel: Osos (H60s)
  notes: Evaluare leziuni litice sau blastice ale calvariei
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m².
series:
- delay: 5 min (300 sec)
  end: Deasupra vertexului
  name: CT Craniu Tardiv cu Contrast
  notes: Temporizarea de 5 minute asigură acumularea optimă a contrastului în leziunile
    cu barieră hemato-encefalică alterată
  start: Sub baza craniului
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Craniu cu Contrast Tardiv 5 min (Protocol OHSU)
---

# CT Craniu cu Contrast Tardiv 5 min (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Craniu Tardiv cu Contrast | 5 min (300 sec) | Sub baza craniului → Deasupra vertexului |

    === "Indicații Clinice"

        - Suspiciune de metastaze cerebrale sau tumori primare SNC
        - Infecții intracraniene, meningite, empieme, abcese cerebrale
        - Leziuni demielinizante atipice în faza activă
        - Evaluare post-operatorie de rezecție tumorală cerebrală

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal, centrare pe bărbia pacientului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 300 / Isovue 370 |
        | Volum | 100 mL (Adult) / 2 mL/kg (Peds, max 100 mL) |
        | Rată de Flux | 2.0 mL/s (Adult) / 1.0-2.0 mL/s (Peds) |
        | Durată | 50s |
        | Metodă Temporizare | Scanare tardivă la 5 minute de la debutul injectării contrastului |
        | Poziționare ROI | N/A |
        | Declanșator (HU) | N/A |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm / 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 22G sau mai mare în plica cotului. Respectați cu strictețe intervalul de 5 minute de la începutul injectării.

    === "Note Asistent"

        - Supraveghere pacient pe durata intervalului de așteptare de 5 minute.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m².
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Căutați priză de contrast inelară (abces vs glioblastom), noduli corticali/subcorticali multipli hipercaptanți (metastaze), încărcare leptomeningeală sau durală.

    === "Sfaturi & Recomandări"

        - Dacă este disponibil, RMN-ul cerebral cu contrast este de regulă superior; CT-ul cu contrast este rezervat pacienților cu contraindicații RM.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Craniu Tardiv cu Contrast | Sub baza craniului | Deasupra vertexului | 5 min (300 sec) | 0.625 mm | Temporizarea de 5 minute asigură acumularea optimă a contrastului în leziunile cu barieră hemato-encefalică alterată |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital (Adult) | CT Craniu Tardiv | Cap | 5.0 mm / 5.0 mm | Creier (H31s) | Standard | Serii multiplanare cu contrast tardiv |
    | Axial, Coronal & Sagital (Pediatric) | CT Craniu Tardiv | Cap | 3.0 mm / 3.0 mm | Creier Pediatric (H31s) | Standard | Secțiuni de 3 mm adaptate pediatric |
    | Axial | CT Craniu Tardiv | Cap | 2.0 mm / 2.0 mm | Osos (H60s) | Standard | Evaluare leziuni litice sau blastice ale calvariei |
