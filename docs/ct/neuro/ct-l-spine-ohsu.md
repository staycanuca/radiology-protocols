---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Traumatism lombo-sacrat acut sau cădere de la înălțime
- Lombalgie acută/cronică severă cu suspiciune de fractură pe os patologic sau osteoporotic
- Evaluare montaj chirurgical (șuruburi pediculare, artrodeză intersomatică L1-S1)
- Suspiciune de spondiloliză, spondilolistezis sau stenoză de canal lombar
contrast:
  agent: FĂRĂ (sau Omnipaque 300 100 mL @ 2.0 mL/s, delay 70s în suspiciune tumorală/infecțioasă)
  duration: 0 - 50s
  flow_rate: 2.0 mL/s
  roi: N/A
  timing: N/A (sau 70s post-contrast)
  trigger: N/A
  volume: 0 - 100 mL
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D VR pentru aprecierea poziționării șuruburilor
    transpediculare.
  nursing: Asigurați poziționarea confortabilă cu suport sub genunchi pentru relaxarea
    coloanei lombare.
  rad: Verificați integritatea istmului vertebral (pars interarticularis la L5), prezența
    fragmentelor osoase retropulsate în canal și stabilitatea coloanei conform clasificării
    AO Spine / Denis.
  tech: 'Reper de centrare: nivelul șoldurilor/crestelor iliace. Dacă se solicită
    evaluarea sacrului, extindeți scanarea până la coccis.'
  tips: Pentru examinări post-operatorii cu material de osteosinteză, activați algoritmii
    de reducere a artefactelor metalice (iMAR / SEMAR).
npo: N/A pentru nativ; 4 ore pentru contrast
position: Decubit dorsal, pernuță sub genunchi pentru aplatizarea lordozei lombare
premedication: Fără contrast oral
protocol_type: non-contrast
recons:
- acquisition: CT L-Spine
  fov: L-Spine
  ir_strength: Standard
  kernel: Osos (Bone)
  notes: Secțiuni axiale osoase
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT L-Spine
  fov: L-Spine
  ir_strength: Standard
  kernel: Osos (Bone)
  notes: Evaluare înălțime spații discale, pediculi, pars interarticularis
  plane: Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT L-Spine
  fov: L-Spine
  ir_strength: Standard
  kernel: Țesut Moale (Soft Tissue)
  notes: Evaluare hernie de disc calcificată, mușchi psoas și canal rahidian
  plane: Axial
  thickness_increment: 3.0 mm / 3.0 mm
safety:
  allergy: Conform politicii OHSU dacă se injectează contrast.
  renal: Conform politicii OHSU dacă se injectează contrast.
series:
- delay: 0 sec (sau 70 sec dacă cu contrast)
  end: Nivel S1 (pentru a include complet S1; întregul sacru dacă este cerut expres)
  name: CT Coloană Lombară
  notes: DFOV 200 mm (mai mare dacă este necesar pentru anatomia lombară completă)
  start: Nivel T12 (pentru a include complet T12)
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Coloană Lombară (Protocol OHSU)
---

# CT Coloană Lombară (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Coloană Lombară | 0 sec (sau 70 sec dacă cu contrast) | Nivel T12 (pentru a include complet T12) → Nivel S1 (pentru a include complet S1; întregul sacru dacă este cerut expres) |

    === "Indicații Clinice"

        - Traumatism lombo-sacrat acut sau cădere de la înălțime
        - Lombalgie acută/cronică severă cu suspiciune de fractură pe os patologic sau osteoporotic
        - Evaluare montaj chirurgical (șuruburi pediculare, artrodeză intersomatică L1-S1)
        - Suspiciune de spondiloliză, spondilolistezis sau stenoză de canal lombar

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal, pernuță sub genunchi pentru aplatizarea lordozei lombare
    - **Repaus Alimentar (NPO):** N/A pentru nativ; 4 ore pentru contrast
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | FĂRĂ (sau Omnipaque 300 100 mL @ 2.0 mL/s, delay 70s în suspiciune tumorală/infecțioasă) |
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

        - Reper de centrare: nivelul șoldurilor/crestelor iliace. Dacă se solicită evaluarea sacrului, extindeți scanarea până la coccis.

    === "Note Asistent"

        - Asigurați poziționarea confortabilă cu suport sub genunchi pentru relaxarea coloanei lombare.

        !!! warning "Siguranță"
            - **Funcție Renală:** Conform politicii OHSU dacă se injectează contrast.
            - **Alergii:** Conform politicii OHSU dacă se injectează contrast.

    === "Note Radiolog"

        - Verificați integritatea istmului vertebral (pars interarticularis la L5), prezența fragmentelor osoase retropulsate în canal și stabilitatea coloanei conform clasificării AO Spine / Denis.

    === "Sfaturi & Recomandări"

        - Pentru examinări post-operatorii cu material de osteosinteză, activați algoritmii de reducere a artefactelor metalice (iMAR / SEMAR).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Coloană Lombară | Nivel T12 (pentru a include complet T12) | Nivel S1 (pentru a include complet S1; întregul sacru dacă este cerut expres) | 0 sec (sau 70 sec dacă cu contrast) | 0.625 mm | DFOV 200 mm (mai mare dacă este necesar pentru anatomia lombară completă) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT L-Spine | L-Spine | 2.0 mm / 2.0 mm | Osos (Bone) | Standard | Secțiuni axiale osoase |
    | Coronal & Sagital | CT L-Spine | L-Spine | 2.0 mm / 2.0 mm | Osos (Bone) | Standard | Evaluare înălțime spații discale, pediculi, pars interarticularis |
    | Axial | CT L-Spine | L-Spine | 3.0 mm / 3.0 mm | Țesut Moale (Soft Tissue) | Standard | Evaluare hernie de disc calcificată, mușchi psoas și canal rahidian |
