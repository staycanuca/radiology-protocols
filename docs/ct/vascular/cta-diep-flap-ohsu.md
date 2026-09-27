---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: vascular
clinical_indications:
- Planificare pre-operatorie pentru reconstrucție mamară autologă cu lambou DIEP (Deep
  Inferior Epigastric Perforator)
- Cartografierea arterelor perforatoare epigastrice inferioare profunde și a traiectului
  lor intramuscular prin dreptul abdominal
- Evaluarea calibrului și dominanței perforatoarelor (mediale vs laterale)
- Aprecierea sistemului venos superficial (vena epigastrică superficială) și a grosimii
  lamboului adipos subcutanat abdominal
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 25s
  flow_rate: 4.0 - 5.0 mL/s
  roi: Aorta abdominală distală
  timing: Bolus tracking în aorta abdominală distală (trigger 150 HU)
  trigger: 150 HU
  volume: 100-120 mL
iris_reference:
  chapter: Aparat cardiovascular & Sistem vascular
  radiation_dose: Clasa 4 (Ridicată > 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: Randare 3D VR cu transparență cutanată pentru harta chirurgicală
    a perforatoarelor raportate la ombilic.
  nursing: Confort pacient.
  rad: 'Pentru fiecare perforatoare dominantă (> 1 mm diametru), raportați: 1) Distanța
    X (față de linia mediană în cm); 2) Distanța Y (față de ombilic în cm); 3) Lungimea
    traiectului intramuscular; 4) Relația cu vena satelită.'
  tech: Canulă 18G în plica cotului. Flush salin 40 mL. Asigurați-vă că nu se aplică
    nicio bandă sau senzor pe abdomenul anterior care ar deforma peretele abdominal.
  tips: Localizarea precisă a celor mai bune 2-3 perforatoare scurtează semnificativ
    timpul chirurgical și reduce riscul de necroză a lamboului.
npo: Repaus alimentar 4 ore
position: Decubit dorsal, brațele ridicate deasupra capului, fără compresie pe abdomenul
  anterior
premedication: Fără contrast oral; fără bandaj compresiv pe abdomen
protocol_type: contrast-enhanced
recons:
- acquisition: CTA DIEP
  fov: Perete Abdominal Anterior
  ir_strength: Standard
  kernel: Vascular / Standard
  notes: Măsurare diametru perforatoare la emergența din fascia anterioară a dreptului
    abdominal
  plane: Axial
  thickness_increment: 1.0 mm / 0.7 mm
- acquisition: CTA DIEP
  fov: Perete Abdominal
  ir_strength: Standard
  kernel: Vascular
  notes: 'Urmărire traiect intramuscular: direct vs oblic lung prin mușchi'
  plane: Sagital & Coronal
  thickness_increment: 1.5 mm / 1.0 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m².
series:
- delay: Trigger + 5 sec
  end: Sub simfiza pubiană (nivelul bifurcației femurale)
  name: CTA DIEP
  notes: Acoperire completă a peretelui abdominal anterior de la coaste până la coapse
  start: Nivelul diafragmului (T11-T12)
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CTA Perforatoare DIEP Reconstrucție Mamară (Protocol OHSU)
---

# CTA Perforatoare DIEP Reconstrucție Mamară (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CTA DIEP | Trigger + 5 sec | Nivelul diafragmului (T11-T12) → Sub simfiza pubiană (nivelul bifurcației femurale) |

    === "Indicații Clinice"

        - Planificare pre-operatorie pentru reconstrucție mamară autologă cu lambou DIEP (Deep Inferior Epigastric Perforator)
        - Cartografierea arterelor perforatoare epigastrice inferioare profunde și a traiectului lor intramuscular prin dreptul abdominal
        - Evaluarea calibrului și dominanței perforatoarelor (mediale vs laterale)
        - Aprecierea sistemului venos superficial (vena epigastrică superficială) și a grosimii lamboului adipos subcutanat abdominal

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat cardiovascular & Sistem vascular*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 4 (Ridicată > 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, brațele ridicate deasupra capului, fără compresie pe abdomenul anterior
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral; fără bandaj compresiv pe abdomen

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 100-120 mL |
        | Rată de Flux | 4.0 - 5.0 mL/s |
        | Durată | 25s |
        | Metodă Temporizare | Bolus tracking în aorta abdominală distală (trigger 150 HU) |
        | Poziționare ROI | Aorta abdominală distală |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 18G în plica cotului. Flush salin 40 mL. Asigurați-vă că nu se aplică nicio bandă sau senzor pe abdomenul anterior care ar deforma peretele abdominal.

    === "Note Asistent"

        - Confort pacient.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m².
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Pentru fiecare perforatoare dominantă (> 1 mm diametru), raportați: 1) Distanța X (față de linia mediană în cm); 2) Distanța Y (față de ombilic în cm); 3) Lungimea traiectului intramuscular; 4) Relația cu vena satelită.

    === "Sfaturi & Recomandări"

        - Localizarea precisă a celor mai bune 2-3 perforatoare scurtează semnificativ timpul chirurgical și reduce riscul de necroză a lamboului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CTA DIEP | Nivelul diafragmului (T11-T12) | Sub simfiza pubiană (nivelul bifurcației femurale) | Trigger + 5 sec | 0.625 mm | Acoperire completă a peretelui abdominal anterior de la coaste până la coapse |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA DIEP | Perete Abdominal Anterior | 1.0 mm / 0.7 mm | Vascular / Standard | Standard | Măsurare diametru perforatoare la emergența din fascia anterioară a dreptului abdominal |
    | Sagital & Coronal | CTA DIEP | Perete Abdominal | 1.5 mm / 1.0 mm | Vascular | Standard | Urmărire traiect intramuscular: direct vs oblic lung prin mușchi |
