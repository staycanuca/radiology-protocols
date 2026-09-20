---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Traumatism cervical acut (criterii NEXUS sau Canadian C-Spine Rule pozitive)
- Cervicalgie severă cu deficit neurologic radicular sau medular
- Evaluare pre- și post-operatorie (artrodeză, cage-uri, șuruburi pediculare)
- Suspiciune de procese expansive osteolitice/osteoblastice sau infecții (spondilodiscită)
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
  additional_recons: Reconstrucții 3D VR pentru fracturi complexe de C1/C2 (Jefferson,
    Hangman, Odontoid).
  nursing: Mențineți gulerul cervical rigid la pacienții cu suspiciune de traumatism
    până la infirmarea imagistică.
  rad: Verificați liniile vertebrale sagitale (anterioară, posterioară, spino-laminară),
    integritatea procesului odontoid și intervalul atlantodental (< 3 mm la adult,
    < 5 mm la copil).
  tech: 'Nivel de reperaj: axilar. Asigurați includerea completă a joncțiunii cervico-toracice
    C7-T1. Dacă umerii suprapun C7, folosiți tracțiune pe membrele superioare.'
  tips: Pentru examinări cu contrast în infecții/tumori, scanarea se efectuează la
    70 secunde după injectarea a 100 mL contrast.
npo: N/A pentru examinare nativă; 4 ore dacă se solicită contrast
position: Decubit dorsal, umerii coborâți cât mai mult prin tracțiune blândă dacă
  starea permite
premedication: Fără contrast oral
protocol_type: non-contrast
recons:
- acquisition: CT C-Spine
  fov: C-Spine
  ir_strength: Standard
  kernel: Osos (Bone)
  notes: Secțiuni fine osoase pentru decelarea fracturilor liniare
  plane: Axial
  thickness_increment: 1.0 mm / 1.0 mm
- acquisition: CT C-Spine
  fov: C-Spine
  ir_strength: Standard
  kernel: Osos (Bone)
  notes: Evaluare aliniament corpuri vertebrale, spații discale și articulații atlanto-axoidiene/zigoapofizare
  plane: Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT C-Spine
  fov: C-Spine
  ir_strength: Standard
  kernel: Țesut Moale (Soft Tissue)
  notes: Evaluare spații paravertebrale și canal rahidian
  plane: Axial
  thickness_increment: 3.0 mm / 3.0 mm
safety:
  allergy: Conform politicii OHSU dacă se injectează contrast.
  renal: Conform politicii OHSU dacă se injectează contrast.
series:
- delay: 0 sec (sau 70 sec dacă cu contrast)
  end: Vârfurile pulmonare (pentru a include complet T1)
  name: CT Coloană Cervicală
  notes: DFOV 200 mm (mai mare dacă este necesar pentru a cuprinde complet anatomia
    coloanei cervicale)
  start: Baza craniului (pentru a include occiputul și C1)
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Coloană Cervicală (Protocol OHSU)
---

# CT Coloană Cervicală (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Coloană Cervicală | 0 sec (sau 70 sec dacă cu contrast) | Baza craniului (pentru a include occiputul și C1) → Vârfurile pulmonare (pentru a include complet T1) |

    === "Indicații Clinice"

        - Traumatism cervical acut (criterii NEXUS sau Canadian C-Spine Rule pozitive)
        - Cervicalgie severă cu deficit neurologic radicular sau medular
        - Evaluare pre- și post-operatorie (artrodeză, cage-uri, șuruburi pediculare)
        - Suspiciune de procese expansive osteolitice/osteoblastice sau infecții (spondilodiscită)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal, umerii coborâți cât mai mult prin tracțiune blândă dacă starea permite
    - **Repaus Alimentar (NPO):** N/A pentru examinare nativă; 4 ore dacă se solicită contrast
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

        - Nivel de reperaj: axilar. Asigurați includerea completă a joncțiunii cervico-toracice C7-T1. Dacă umerii suprapun C7, folosiți tracțiune pe membrele superioare.

    === "Note Asistent"

        - Mențineți gulerul cervical rigid la pacienții cu suspiciune de traumatism până la infirmarea imagistică.

        !!! warning "Siguranță"
            - **Funcție Renală:** Conform politicii OHSU dacă se injectează contrast.
            - **Alergii:** Conform politicii OHSU dacă se injectează contrast.

    === "Note Radiolog"

        - Verificați liniile vertebrale sagitale (anterioară, posterioară, spino-laminară), integritatea procesului odontoid și intervalul atlantodental (< 3 mm la adult, < 5 mm la copil).

    === "Sfaturi & Recomandări"

        - Pentru examinări cu contrast în infecții/tumori, scanarea se efectuează la 70 secunde după injectarea a 100 mL contrast.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Coloană Cervicală | Baza craniului (pentru a include occiputul și C1) | Vârfurile pulmonare (pentru a include complet T1) | 0 sec (sau 70 sec dacă cu contrast) | 0.625 mm | DFOV 200 mm (mai mare dacă este necesar pentru a cuprinde complet anatomia coloanei cervicale) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT C-Spine | C-Spine | 1.0 mm / 1.0 mm | Osos (Bone) | Standard | Secțiuni fine osoase pentru decelarea fracturilor liniare |
    | Coronal & Sagital | CT C-Spine | C-Spine | 2.0 mm / 2.0 mm | Osos (Bone) | Standard | Evaluare aliniament corpuri vertebrale, spații discale și articulații atlanto-axoidiene/zigoapofizare |
    | Axial | CT C-Spine | C-Spine | 3.0 mm / 3.0 mm | Țesut Moale (Soft Tissue) | Standard | Evaluare spații paravertebrale și canal rahidian |
