---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Planificare pre-operatorie neuronavigație (StealthStation, Brainlab)
- Biopsie cerebrală stereotaxică ghidată
- Implantare de electrozi pentru stimulare cerebrală profundă (DBS)
- Radiochirurgie stereotaxică (Gamma Knife / CyberKnife)
contrast:
  agent: Omnipaque 300 (opțional la cererea neurochirurgului, 100 mL @ 2.0 mL/s, delay
    5 min)
  duration: 0 - 50s
  flow_rate: 2.0 mL/s
  roi: N/A
  timing: Scanare nativă sau la 5 min post-contrast
  trigger: N/A
  volume: 0 - 100 mL
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 2 (Mică 1 - 3 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D de suprafață (SSD/VR) pentru verificarea co-înregistrării
    cu RMN.
  nursing: Protecția markerilor fiduciali cutanați dacă au fost deja aplicați de echipa
    de neurochirurgie.
  rad: Verificați că întregul set de date conține grosime și increment identic (1.0
    mm x 1.0 mm) fără secțiuni lipsă și fără artefacte de mișcare.
  tech: 'REGULĂ CRITICĂ OHSU: NU ANGULAȚI GANTRY-UL. Capul trebuie poziționat cât
    mai drept posibil. Nu excludeți țesuturile moi de pe scalp unde sunt plasați markerii
    fiduciali.'
  tips: Trimiteți datele 'raw' și reconstrucția de 1 mm direct către PACS și stația
    Stealth.
npo: Repaus alimentar 4 ore dacă se solicită contrast
position: Decubit dorsal, cap poziționat strict drept, fără nicio angulare a gantry-ului
  (0 grade)
premedication: Fără contrast oral; examinarea nativă este standard dacă nu se cere
  expres contrast
protocol_type: specialized
recons:
- acquisition: Stealth Volumetric
  fov: Cap complet
  ir_strength: Standard
  kernel: Standard / Creier
  notes: Set de date volumetric izotrop nativ pentru încărcare directă în stația de
    navigație
  plane: Axial
  thickness_increment: 1.0 mm / 1.0 mm (izotrop)
safety:
  allergy: Conform politicii OHSU dacă se injectează contrast.
  renal: Conform politicii OHSU dacă se injectează contrast.
series:
- delay: 0 sec (sau 5 min dacă cu contrast)
  end: Deasupra vertexului (inclusiv toate țesuturile moi și markerii de suprafață)
  name: Achiziție Volumetrică Stealth
  notes: DFOV 220 mm; deschideți FOV pentru a include complet țesutul moale anterior
    și posterior și markerii fiduciali
  start: Sub baza nasului / palat dur
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV
  mas: 250-300 mAs (curent fix recomandat pentru precizie geometrică)
  pitch: 0.6 - 0.8 (suprapunere fină)
  rotation_time: 0.5 - 1.0 s
  scan_mode: Elicoidal strict non-angulat
  slice_thickness: 0.625 mm
title: CT Craniu Stealth / Stereotaxic Ghidat (Protocol OHSU)
---

# CT Craniu Stealth / Stereotaxic Ghidat (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Achiziție Volumetrică Stealth | 0 sec (sau 5 min dacă cu contrast) | Sub baza nasului / palat dur → Deasupra vertexului (inclusiv toate țesuturile moi și markerii de suprafață) |

    === "Indicații Clinice"

        - Planificare pre-operatorie neuronavigație (StealthStation, Brainlab)
        - Biopsie cerebrală stereotaxică ghidată
        - Implantare de electrozi pentru stimulare cerebrală profundă (DBS)
        - Radiochirurgie stereotaxică (Gamma Knife / CyberKnife)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cap, Gât & Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Mică 1 - 3 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, cap poziționat strict drept, fără nicio angulare a gantry-ului (0 grade)
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore dacă se solicită contrast
    - **Premedicație / Pregătire:**
        - Fără contrast oral; examinarea nativă este standard dacă nu se cere expres contrast

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 300 (opțional la cererea neurochirurgului, 100 mL @ 2.0 mL/s, delay 5 min) |
        | Volum | 0 - 100 mL |
        | Rată de Flux | 2.0 mL/s |
        | Durată | 0 - 50s |
        | Metodă Temporizare | Scanare nativă sau la 5 min post-contrast |
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
    | **Curent Tub (mAs)** | 250-300 mAs (curent fix recomandat pentru precizie geometrică) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm / 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 - 1.0 s |
    | **Pitch (Factor Pas)** | 0.6 - 0.8 (suprapunere fină) |
    | **Mod Scanare** | Elicoidal strict non-angulat |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - REGULĂ CRITICĂ OHSU: NU ANGULAȚI GANTRY-UL. Capul trebuie poziționat cât mai drept posibil. Nu excludeți țesuturile moi de pe scalp unde sunt plasați markerii fiduciali.

    === "Note Asistent"

        - Protecția markerilor fiduciali cutanați dacă au fost deja aplicați de echipa de neurochirurgie.

        !!! warning "Siguranță"
            - **Funcție Renală:** Conform politicii OHSU dacă se injectează contrast.
            - **Alergii:** Conform politicii OHSU dacă se injectează contrast.

    === "Note Radiolog"

        - Verificați că întregul set de date conține grosime și increment identic (1.0 mm x 1.0 mm) fără secțiuni lipsă și fără artefacte de mișcare.

    === "Sfaturi & Recomandări"

        - Trimiteți datele 'raw' și reconstrucția de 1 mm direct către PACS și stația Stealth.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Achiziție Volumetrică Stealth | Sub baza nasului / palat dur | Deasupra vertexului (inclusiv toate țesuturile moi și markerii de suprafață) | 0 sec (sau 5 min dacă cu contrast) | 0.625 mm | DFOV 220 mm; deschideți FOV pentru a include complet țesutul moale anterior și posterior și markerii fiduciali |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Stealth Volumetric | Cap complet | 1.0 mm / 1.0 mm (izotrop) | Standard / Creier | Standard | Set de date volumetric izotrop nativ pentru încărcare directă în stația de navigație |
