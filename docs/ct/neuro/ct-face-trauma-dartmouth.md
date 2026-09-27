---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: neuro
clinical_indications:
- Traumatism cranio-facial acut (accidente rutiere, agresiuni, căderi)
- 'Suspiciune de fracturi maxilo-faciale: orbite (blow-out), oase nazale, complex
  zigomatico-maxilar (ZMC), mandibulă'
- Fracturi Le Fort tip I, II sau III
- Evaluarea corpilor străini radioopaci intraorbitali sau faciale și a hematoamelor
  retrobulbare
contrast:
  agent: N/A
  duration: N/A
  flow_rate: N/A
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: Fără contrast
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 2 (Scăzută 1 - 5 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: Atenție la menținerea căilor aeriene permeabile la pacienții politraumatizați
    cu sângerare orofaringiană masivă.
  rad: Căutați semne de herniere sau pensare a mușchiului drept inferior în fracturile
    de planșeu orbitar (urgență oftalmologică), fracturi ale plăcii cribriforme cu
    fistulă LCR (rinolicvoree) și integritatea proceselor pterigoide (fracturile de
    pterigoide definesc complexul Le Fort).
  tech: Îndepărtați protezele dentare mobile, cerceii și piercingurile faciale pentru
    a minimiza artefactele metalice de striere.
  tips: Utilizați algoritmi de reducere a artefactelor metalice (iMAR / SEMAR) dacă
    pacientul are implanturi dentare voluminoase.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal, capul centrat în tetieră, planul ocluzal perpendicular pe
  masă dacă este posibil
premedication: Fără contrast
protocol_type: non-contrast
recons:
- acquisition: CT Masiv Facial Nativ
  fov: Masiv Facial (16-18 cm)
  ir_strength: High
  kernel: Bone High-Resolution (I70f) & Soft Tissue (I30f)
  notes: Fereastră osoasă strictă pentru detectarea microfracturilor
  plane: Axial Osos & Părți Moi
  thickness_increment: 1.0 mm / 0.8 mm
- acquisition: CT Masiv Facial Nativ
  fov: Masiv Facial
  ir_strength: High
  kernel: Bone & Soft Tissue
  notes: Planul coronal este crucial pentru evaluarea planșeului orbitar și a lamelor
    pterigoidiene
  plane: Coronal & Sagital
  thickness_increment: 1.5 mm / 1.5 mm
- acquisition: CT Masiv Facial Nativ
  fov: Masiv facial
  ir_strength: High
  kernel: Bone
  notes: Reconstrucție tridimensională esențială pentru chirurgia maxilo-facială (OMFS)
  plane: 3D VR Schelet Facial
  thickness_increment: 3D VR
safety:
  allergy: Fără risc — examinare nativă.
  renal: Fără risc renal.
series:
- delay: 0 sec
  end: Sub marginea inferioară a mandibulei (simfiză mentonieră)
  name: CT Masiv Facial Nativ
  notes: Acoperire completă a tuturor structurilor scheletice faciale și cavităților
    aeriene
  start: Imediat deasupra sinusurilor frontale
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 120 kVp
  mas: CAREDose4D / SureExposure (Ref 180-220 mAs)
  pitch: 0.8 - 0.9
  rotation_time: 0.5 s
  scan_mode: Elicoidal fin izotrop
  slice_thickness: 0.625 mm
title: CT Masiv Facial Traumă (Protocol Dartmouth Hitchcock)
---

# CT Masiv Facial Traumă (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Masiv Facial Nativ | 0 sec | Imediat deasupra sinusurilor frontale → Sub marginea inferioară a mandibulei (simfiză mentonieră) |

    === "Indicații Clinice"

        - Traumatism cranio-facial acut (accidente rutiere, agresiuni, căderi)
        - Suspiciune de fracturi maxilo-faciale: orbite (blow-out), oase nazale, complex zigomatico-maxilar (ZMC), mandibulă
        - Fracturi Le Fort tip I, II sau III
        - Evaluarea corpilor străini radioopaci intraorbitali sau faciale și a hematoamelor retrobulbare

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cap, Gât & Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Scăzută 1 - 5 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, capul centrat în tetieră, planul ocluzal perpendicular pe masă dacă este posibil
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Fără contrast

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kVp kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure (Ref 180-220 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 0.9 |
    | **Mod Scanare** | Elicoidal fin izotrop |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Îndepărtați protezele dentare mobile, cerceii și piercingurile faciale pentru a minimiza artefactele metalice de striere.

    === "Note Asistent"

        - Atenție la menținerea căilor aeriene permeabile la pacienții politraumatizați cu sângerare orofaringiană masivă.

        !!! warning "Siguranță"
            - **Funcție Renală:** Fără risc renal.
            - **Alergii:** Fără risc — examinare nativă.

    === "Note Radiolog"

        - Căutați semne de herniere sau pensare a mușchiului drept inferior în fracturile de planșeu orbitar (urgență oftalmologică), fracturi ale plăcii cribriforme cu fistulă LCR (rinolicvoree) și integritatea proceselor pterigoide (fracturile de pterigoide definesc complexul Le Fort).

    === "Sfaturi & Recomandări"

        - Utilizați algoritmi de reducere a artefactelor metalice (iMAR / SEMAR) dacă pacientul are implanturi dentare voluminoase.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Masiv Facial Nativ | Imediat deasupra sinusurilor frontale | Sub marginea inferioară a mandibulei (simfiză mentonieră) | 0 sec | 0.625 mm | Acoperire completă a tuturor structurilor scheletice faciale și cavităților aeriene |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial Osos & Părți Moi | CT Masiv Facial Nativ | Masiv Facial (16-18 cm) | 1.0 mm / 0.8 mm | Bone High-Resolution (I70f) & Soft Tissue (I30f) | High | Fereastră osoasă strictă pentru detectarea microfracturilor |
    | Coronal & Sagital | CT Masiv Facial Nativ | Masiv Facial | 1.5 mm / 1.5 mm | Bone & Soft Tissue | High | Planul coronal este crucial pentru evaluarea planșeului orbitar și a lamelor pterigoidiene |
    | 3D VR Schelet Facial | CT Masiv Facial Nativ | Masiv facial | 3D VR | Bone | High | Reconstrucție tridimensională esențială pentru chirurgia maxilo-facială (OMFS) |
