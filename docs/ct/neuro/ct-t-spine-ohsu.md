---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Traumatism toracic cu durere pe linia mediană sau mecanism de decelerare
- Fracturi de compresie osteoporotică sau traumatice de corp vertebral
- Evaluare metastaze vertebrale toracice, leziuni litice sau blastice
- Suspiciune de spondilodiscită toracică sau abces epidural (cu contrast)
contrast:
  agent: FĂRĂ (sau Omnipaque 300 100 mL @ 2.0 mL/s, delay 70s în suspiciune tumorală/infecție)
  duration: 0 - 50s
  flow_rate: 2.0 mL/s
  roi: N/A
  timing: N/A (sau 70s post-contrast)
  trigger: N/A
  volume: 0 - 100 mL
iris_reference:
  chapter: Coloană vertebrală & Traumatisme
  radiation_dose: Clasa 3 (Moderată 4 - 8 mSv)
  recommendation_grade: Grad B
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții sagitale curbate pe axul rahidian în caz de scolioză
    severă.
  nursing: Confort pacient și asistență la ridicarea brațelor.
  rad: Numărați vertebrele de sus în jos din scout (T1 la T12) pentru localizarea
    precisă a leziunilor; verificați peretele posterior al corpului vertebral (risc
    de compresie canaliculară).
  tech: 'Reper centrare: nivelul ombilicului. Brațele ridicate deasupra capului pentru
    a reduce artefactele de atenuare pe torace.'
  tips: În caz de contrast, se injectează 100 mL Omnipaque 300 @ 2.0 mL/s cu scanare
    la 70 secunde.
npo: N/A pentru nativ; 4 ore pentru contrast
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Fără contrast oral
protocol_type: non-contrast
recons:
- acquisition: CT T-Spine
  fov: T-Spine
  ir_strength: Standard
  kernel: Osos (Bone)
  notes: Secțiuni osoase axiale
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT T-Spine
  fov: T-Spine
  ir_strength: Standard
  kernel: Osos (Bone)
  notes: Apreciere cifoză, colaps vertebral și aliniament
  plane: Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT T-Spine
  fov: T-Spine
  ir_strength: Standard
  kernel: Țesut Moale (Soft Tissue)
  notes: Evaluare mase paravertebrale și hematoame epidurale
  plane: Axial
  thickness_increment: 3.0 mm / 3.0 mm
safety:
  allergy: Conform politicii OHSU dacă se injectează contrast.
  renal: Conform politicii OHSU dacă se injectează contrast.
series:
- delay: 0 sec (sau 70 sec dacă cu contrast)
  end: Nivel L1 (pentru a include complet T12 și L1)
  name: CT Coloană Toracală
  notes: DFOV 200 mm centrat pe coloana toracală
  start: Nivel C7-T1 (pentru a include complet T1)
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Coloană Toracală (Protocol OHSU)
---

# CT Coloană Toracală (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Coloană Toracală | 0 sec (sau 70 sec dacă cu contrast) | Nivel C7-T1 (pentru a include complet T1) → Nivel L1 (pentru a include complet T12 și L1) |

    === "Indicații Clinice"

        - Traumatism toracic cu durere pe linia mediană sau mecanism de decelerare
        - Fracturi de compresie osteoporotică sau traumatice de corp vertebral
        - Evaluare metastaze vertebrale toracice, leziuni litice sau blastice
        - Suspiciune de spondilodiscită toracică sau abces epidural (cu contrast)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Coloană vertebrală & Traumatisme*
            - **Grad de Recomandare:** **Grad B**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 4 - 8 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** N/A pentru nativ; 4 ore pentru contrast
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | FĂRĂ (sau Omnipaque 300 100 mL @ 2.0 mL/s, delay 70s în suspiciune tumorală/infecție) |
        | Volum | 0 - 100 mL |
        | Rată de Flux | 2.0 mL/s |
        | Durată | 0 - 50s |
        | Metodă Temporizare | N/A (sau 70s post-contrast) |
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

        - Reper centrare: nivelul ombilicului. Brațele ridicate deasupra capului pentru a reduce artefactele de atenuare pe torace.

    === "Note Asistent"

        - Confort pacient și asistență la ridicarea brațelor.

        !!! warning "Siguranță"
            - **Funcție Renală:** Conform politicii OHSU dacă se injectează contrast.
            - **Alergii:** Conform politicii OHSU dacă se injectează contrast.

    === "Note Radiolog"

        - Numărați vertebrele de sus în jos din scout (T1 la T12) pentru localizarea precisă a leziunilor; verificați peretele posterior al corpului vertebral (risc de compresie canaliculară).

    === "Sfaturi & Recomandări"

        - În caz de contrast, se injectează 100 mL Omnipaque 300 @ 2.0 mL/s cu scanare la 70 secunde.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Coloană Toracală | Nivel C7-T1 (pentru a include complet T1) | Nivel L1 (pentru a include complet T12 și L1) | 0 sec (sau 70 sec dacă cu contrast) | 0.625 mm | DFOV 200 mm centrat pe coloana toracală |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT T-Spine | T-Spine | 2.0 mm / 2.0 mm | Osos (Bone) | Standard | Secțiuni osoase axiale |
    | Coronal & Sagital | CT T-Spine | T-Spine | 2.0 mm / 2.0 mm | Osos (Bone) | Standard | Apreciere cifoză, colaps vertebral și aliniament |
    | Axial | CT T-Spine | T-Spine | 3.0 mm / 3.0 mm | Țesut Moale (Soft Tissue) | Standard | Evaluare mase paravertebrale și hematoame epidurale |
