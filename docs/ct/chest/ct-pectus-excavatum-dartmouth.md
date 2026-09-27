---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: chest
clinical_indications:
- Deformare congenitală a peretelui toracic anterior (Pectus excavatum)
- Calculul indicelui Haller și al indicelui de asimetrie toracică
- Evaluarea compresiei sau deplasării cardiace (ventricul drept împins spre stânga)
- Planificare chirurgicală (procedura minim invazivă Nuss sau intervenția Ravitch)
contrast:
  agent: N/A
  duration: N/A
  flow_rate: N/A
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: Fără contrast
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 2 (Scăzută 1 - 5 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: Nu necesită linie venoasă periferică.
  rad: Calculați Indicele Haller = (Distanța transversă maximă a cutiei toracice)
    / (Distanța antero-posterioară minimă între fața posterioară a sternului și fața
    anterioară a corpului vertebral). Indice Haller > 3.25 este considerat sever și
    indică intervenție chirurgicală.
  tech: Instructaj atent de respirație înainte de poziționare. Pacienții sunt de regulă
    adolescenți sau tineri; prioritizați protocoalele de doză foarte scăzută (Low
    Dose CT).
  tips: Măsurați de asemenea indicele de asimetrie (raportul între hemitoracele drept
    și stâng la punctul cel mai deprimat).
npo: Nu este necesar repaus alimentar
position: Decubit dorsal, brațele ridicate confortabil deasupra capului
premedication: Fără contrast oral sau intravenos
protocol_type: non-contrast
recons:
- acquisition: CT Torace Pectus
  fov: Cutie toracică completă
  ir_strength: Iterative Reconstruction High
  kernel: Mediastinal (I30f) & Osos (I70f)
  notes: Plan de măsurare la nivelul depresiunii sternale maxime
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT Torace Pectus
  fov: Cutie toracică
  ir_strength: High
  kernel: Mediastinal & Osos
  notes: Evaluarea lungimii și angulației sternale
  plane: Sagital & Coronal
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT Torace Pectus
  fov: Perete toracic
  ir_strength: High
  kernel: Osos
  notes: Randare volumetrică 3D pentru consiliere chirurgicală
  plane: 3D VR Schelet Toracic
  thickness_increment: VR 3D
safety:
  allergy: Fără risc — examinare nativă fără contrast.
  renal: Fără restricții renale.
series:
- delay: 0 sec
  end: Baza toracelui (la nivelul recesurilor costodiafragmatice)
  name: CT Torace în Apnee Inspiratorie
  notes: Scanare în inspir profund pentru calculul standard Haller
  start: Imediat deasupra apexurilor pulmonare
  thickness: 1.0 mm
- delay: 0 sec
  end: Sub apendicele xifoid
  name: CT Torace Focussat în Expir (Opțional)
  notes: Expirul evidențiază compresia maximă sternovertebrală și poate crește indicele
    Haller
  start: Nivelul unghiului Louis sternal
  thickness: 1.25 mm
tech_params:
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 80 - 100 kVp (Protocol pediatric / tânăr adult low-dose)
  mas: 30 - 50 mAs (Optimizat ALARA pentru reducere maximă de doză)
  pitch: 1.2 - 1.4
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal ultra-rapid
  slice_thickness: 1.0 - 1.25 mm
title: CT Torace Pectus Excavatum (Protocol Dartmouth Hitchcock)
---

# CT Torace Pectus Excavatum (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Torace în Apnee Inspiratorie | 0 sec | Imediat deasupra apexurilor pulmonare → Baza toracelui (la nivelul recesurilor costodiafragmatice) |
        | CT Torace Focussat în Expir (Opțional) | 0 sec | Nivelul unghiului Louis sternal → Sub apendicele xifoid |

    === "Indicații Clinice"

        - Deformare congenitală a peretelui toracic anterior (Pectus excavatum)
        - Calculul indicelui Haller și al indicelui de asimetrie toracică
        - Evaluarea compresiei sau deplasării cardiace (ventricul drept împins spre stânga)
        - Planificare chirurgicală (procedura minim invazivă Nuss sau intervenția Ravitch)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Scăzută 1 - 5 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, brațele ridicate confortabil deasupra capului
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Fără contrast oral sau intravenos

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 80 - 100 kVp (Protocol pediatric / tânăr adult low-dose) kV |
    | **Curent Tub (mAs)** | 30 - 50 mAs (Optimizat ALARA pentru reducere maximă de doză) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.0 - 1.25 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 1.2 - 1.4 |
    | **Mod Scanare** | Elicoidal ultra-rapid |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Instructaj atent de respirație înainte de poziționare. Pacienții sunt de regulă adolescenți sau tineri; prioritizați protocoalele de doză foarte scăzută (Low Dose CT).

    === "Note Asistent"

        - Nu necesită linie venoasă periferică.

        !!! warning "Siguranță"
            - **Funcție Renală:** Fără restricții renale.
            - **Alergii:** Fără risc — examinare nativă fără contrast.

    === "Note Radiolog"

        - Calculați Indicele Haller = (Distanța transversă maximă a cutiei toracice) / (Distanța antero-posterioară minimă între fața posterioară a sternului și fața anterioară a corpului vertebral). Indice Haller > 3.25 este considerat sever și indică intervenție chirurgicală.

    === "Sfaturi & Recomandări"

        - Măsurați de asemenea indicele de asimetrie (raportul între hemitoracele drept și stâng la punctul cel mai deprimat).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Torace în Apnee Inspiratorie | Imediat deasupra apexurilor pulmonare | Baza toracelui (la nivelul recesurilor costodiafragmatice) | 0 sec | 1.0 mm | Scanare în inspir profund pentru calculul standard Haller |
    | CT Torace Focussat în Expir (Opțional) | Nivelul unghiului Louis sternal | Sub apendicele xifoid | 0 sec | 1.25 mm | Expirul evidențiază compresia maximă sternovertebrală și poate crește indicele Haller |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Torace Pectus | Cutie toracică completă | 2.0 mm / 2.0 mm | Mediastinal (I30f) & Osos (I70f) | Iterative Reconstruction High | Plan de măsurare la nivelul depresiunii sternale maxime |
    | Sagital & Coronal | CT Torace Pectus | Cutie toracică | 2.0 mm / 2.0 mm | Mediastinal & Osos | High | Evaluarea lungimii și angulației sternale |
    | 3D VR Schelet Toracic | CT Torace Pectus | Perete toracic | VR 3D | Osos | High | Randare volumetrică 3D pentru consiliere chirurgicală |
