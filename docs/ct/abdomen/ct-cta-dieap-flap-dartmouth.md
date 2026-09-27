---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: abdomen
clinical_indications:
- Planificare preoperatorie pentru reconstrucție mamară autologă cu lambou liber perforant
  din artera epigastrică inferioară profundă (DIEP flap)
- Cartografierea vaselor perforante (calibru, traiect intramuscular vs. fascial, punct
  de emergență)
- Alegerea celui mai bun pedicul vascular (drept vs. stâng, medial vs. lateral) pentru
  reducerea timpului operator
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 30s
  flow_rate: 5.0 mL/s
  roi: Lumenul arterei femurale comune (zoom pe imaginea de monitorizare pentru plasare
    precisă a ROI)
  timing: Smart Prep pe artera femurală comună la nivelul simfizei pubiene
  trigger: 150 HU
  volume: 150 mL contrast + 50 mL flush salin
iris_reference:
  chapter: Abdomen & Pelvis
  radiation_dose: Clasa 3 (Moderată 5 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: Verificare funcție renală și antecedente alergice.
  rad: Localizați coordonatele X/Y/Z ale perforantelor dominante (distanță față de
    ombilic și linia mediană), calibrul la emergența fascială (> 1.0-1.5 mm) și traiectul
    intramuscular (scurt este preferat).
  tech: Canulă 18G în plica cotului. Asigurați debit constant de 5 mL/s. Încălziți
    abdomenul pacientei cu pătură caldă înainte de achiziție.
  tips: Verificați și calibrul venelor comitante profunde și al venei epigastrice
    superficiale (SIEV) pentru drenaj venos de rezervă.
npo: Repaus alimentar 4 ore
position: Decubit dorsal, picioarele înainte (feet first), brațele ridicate confortabil
premedication: FĂRĂ contrast oral. PĂTURĂ CALDĂ aplicată pe abdomen înainte de scanare
  pentru a preveni vasoconstricția reflexă a vaselor perforante cutanate. Îndepărtarea
  completă a îmbrăcămintei și a lenjeriei intime din zona abdominală/pelvină pentru
  a evita compresia cutanată.
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Arterial DIEAP
  fov: Abdomen-Pelvis
  ir_strength: Standard
  kernel: Standard
  notes: Evaluare de ansamblu
  plane: Axial Diagnostic
  thickness_increment: 2.5 mm / 2.5 mm
- acquisition: CTA Arterial DIEAP
  fov: Perete abdominal anterior
  ir_strength: High
  kernel: Standard
  notes: Esențial pentru urmărirea traiectului perforantelor milimetrice prin mușchiul
    drept abdominal
  plane: Axial Ultra-Subțire
  thickness_increment: 0.625 mm / 0.5 mm
- acquisition: CTA Arterial DIEAP
  fov: Perete abdominal
  ir_strength: High
  kernel: Standard
  notes: Proiecții de intensitate maximă pentru cartografierea arborizației perforantelor
  plane: MIP Axial, Coronal & Sagital
  thickness_increment: 3.0 mm q 1.5 mm MIP
- acquisition: CTA Arterial DIEAP
  fov: Tegument & perete abdominal
  ir_strength: High
  kernel: Standard
  notes: Hartă de navigație chirurgicală de suprafață cu poziționarea perforantelor
    față de ombilic
  plane: 3D Reconstrucție Volumetrică (VR)
  thickness_increment: 3D VR
safety:
  allergy: Screening alergie.
  renal: eGFR > 30 mL/min.
series:
- delay: Trigger Smart Prep femural
  end: Imediat deasupra diafragmului (direcție CAUDO-CRANIALĂ)
  name: CTA Arterial DIEAP Abdomen & Pelvis
  notes: Direcția caudo-cranială optimizează sincronizarea cu bolusul arterial în
    peretele abdominal inferior
  start: Sub simfiza pubiană (nivel inghinal)
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm sau 64 × 0.625 mm
  kv: 100 - 120 kVp
  mas: AEC CAREDose4D / SureExposure
  pitch: 0.8 - 0.9
  rotation_time: 0.5 s
  scan_mode: Elicoidal fin
  slice_thickness: 0.625 mm
title: CTA Abdomen & Pelvis DIEP Flap (Protocol Dartmouth Hitchcock)
---

# CTA Abdomen & Pelvis DIEP Flap (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CTA Arterial DIEAP Abdomen & Pelvis | Trigger Smart Prep femural | Sub simfiza pubiană (nivel inghinal) → Imediat deasupra diafragmului (direcție CAUDO-CRANIALĂ) |

    === "Indicații Clinice"

        - Planificare preoperatorie pentru reconstrucție mamară autologă cu lambou liber perforant din artera epigastrică inferioară profundă (DIEP flap)
        - Cartografierea vaselor perforante (calibru, traiect intramuscular vs. fascial, punct de emergență)
        - Alegerea celui mai bun pedicul vascular (drept vs. stâng, medial vs. lateral) pentru reducerea timpului operator

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Abdomen & Pelvis*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, picioarele înainte (feet first), brațele ridicate confortabil
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - FĂRĂ contrast oral. PĂTURĂ CALDĂ aplicată pe abdomen înainte de scanare pentru a preveni vasoconstricția reflexă a vaselor perforante cutanate. Îndepărtarea completă a îmbrăcămintei și a lenjeriei intime din zona abdominală/pelvină pentru a evita compresia cutanată.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 150 mL contrast + 50 mL flush salin |
        | Rată de Flux | 5.0 mL/s |
        | Durată | 30s |
        | Metodă Temporizare | Smart Prep pe artera femurală comună la nivelul simfizei pubiene |
        | Poziționare ROI | Lumenul arterei femurale comune (zoom pe imaginea de monitorizare pentru plasare precisă a ROI) |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 - 120 kVp kV |
    | **Curent Tub (mAs)** | AEC CAREDose4D / SureExposure |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm sau 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 0.9 |
    | **Mod Scanare** | Elicoidal fin |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 18G în plica cotului. Asigurați debit constant de 5 mL/s. Încălziți abdomenul pacientei cu pătură caldă înainte de achiziție.

    === "Note Asistent"

        - Verificare funcție renală și antecedente alergice.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min.
            - **Alergii:** Screening alergie.

    === "Note Radiolog"

        - Localizați coordonatele X/Y/Z ale perforantelor dominante (distanță față de ombilic și linia mediană), calibrul la emergența fascială (> 1.0-1.5 mm) și traiectul intramuscular (scurt este preferat).

    === "Sfaturi & Recomandări"

        - Verificați și calibrul venelor comitante profunde și al venei epigastrice superficiale (SIEV) pentru drenaj venos de rezervă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CTA Arterial DIEAP Abdomen & Pelvis | Sub simfiza pubiană (nivel inghinal) | Imediat deasupra diafragmului (direcție CAUDO-CRANIALĂ) | Trigger Smart Prep femural | 0.625 mm | Direcția caudo-cranială optimizează sincronizarea cu bolusul arterial în peretele abdominal inferior |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial Diagnostic | CTA Arterial DIEAP | Abdomen-Pelvis | 2.5 mm / 2.5 mm | Standard | Standard | Evaluare de ansamblu |
    | Axial Ultra-Subțire | CTA Arterial DIEAP | Perete abdominal anterior | 0.625 mm / 0.5 mm | Standard | High | Esențial pentru urmărirea traiectului perforantelor milimetrice prin mușchiul drept abdominal |
    | MIP Axial, Coronal & Sagital | CTA Arterial DIEAP | Perete abdominal | 3.0 mm q 1.5 mm MIP | Standard | High | Proiecții de intensitate maximă pentru cartografierea arborizației perforantelor |
    | 3D Reconstrucție Volumetrică (VR) | CTA Arterial DIEAP | Tegument & perete abdominal | 3D VR | Standard | High | Hartă de navigație chirurgicală de suprafață cu poziționarea perforantelor față de ombilic |
