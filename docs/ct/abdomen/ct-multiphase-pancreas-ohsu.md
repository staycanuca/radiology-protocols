---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Suspiciune de adenocarcinom ductal pancreatic sau masă pancreatică neelucidată
- Caracterizare leziuni chistice pancreatice (IPMN, chistadenom seros/mucinos, pseudochist)
- Tumori neuroendocrine pancreatice (insulinom, gastrinom, glucagonom)
- Stadializare pre-operatorie a rezecabilității vasculare (artera mezenterică superioară,
  trunchi celiac, venă portă/VMS)
- Icter mecanic obstructiv nedureros (semnul Courvoisier-Terrier)
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 25-30s
  flow_rate: 4.0 - 5.0 mL/s
  roi: Aorta abdominală la nivelul trunchiului celiac
  timing: Fază Parenchimatoasă Pancreatică la 40-45 secunde + Fază Venoasă Portală
    la 70 secunde
  trigger: 150 HU (+ 25 sec delay pentru faza pancreatică)
  volume: 125-150 mL
iris_reference:
  chapter: Aparat digestiv & Abdomen
  radiation_dose: Clasa 4 (Ridicată > 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D MIP și angiografice pentru ramurile trunchiului
    celiac și artera mezenterică superioară.
  nursing: Supraveghere strictă a accesului venos la debite mari.
  rad: 'Criterii de nerezecabilitate: contact tumoral > 180° cu trunchiul celiac sau
    AMS; ocluzie nereconstructibilă a venei porte sau VMS. Măsurați diametrul canalului
    Wirsung și CBP.'
  tech: Injectare cu debit înalt (4-5 mL/s) printr-o canulă 18-20G certificată high-pressure.
    Flush salin 40 mL. Pacientul bea 500 mL apă chiar înainte de a se așeza pe masă.
  tips: Tumorile neuroendocrine sunt hipervasculare și se încarcă intens în faza arterială/pancreatică
    timpurie, spre deosebire de adenocarcinom care este hipovascular.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: 'Contrast oral neutru: 500-750 mL apă simplă cu 15-20 min înainte de
  scanare pentru distensie duodenală și gastrică optimă'
protocol_type: multiphase
recons:
- acquisition: Fază Pancreatică & Portală
  fov: Pancreas / Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Analiză detaliată a parenchimului și raporturilor vasculare
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: Fază Pancreatică & Portală
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Reconstrucții coronale curbate pe ductul Wirsung și calea biliară principală
  plane: Coronal & Sagital
  thickness_increment: 1.5 mm / 1.5 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m².
series:
- delay: 0 sec
  end: Pol inferior renal
  name: Fază Nativă (Pancreas)
  notes: Detectare calcificări ductale (pancreatită cronică) sau hemoragii
  start: Cupole diafragmatice
  thickness: 1.0 mm
- delay: 40-45 sec (sau trigger + 25s)
  end: Creste iliace
  name: Fază Parenchimatoasă Pancreatică
  notes: Contrastare maximă a parenchimului pancreatic normal; adenocarcinomul apare
    hipodens/hipovascular pe acest fond
  start: Diafragm
  thickness: 0.625 mm
- delay: 70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală (Abdomen & Pelvis)
  notes: Evaluare invazie ax venos spleno-porto-mezenteric și metastaze hepatice/peritoneale
  start: Diafragm
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Pancreas Multifazic (Protocol OHSU)
---

# CT Pancreas Multifazic (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă (Pancreas) | 0 sec | Cupole diafragmatice → Pol inferior renal |
        | Fază Parenchimatoasă Pancreatică | 40-45 sec (sau trigger + 25s) | Diafragm → Creste iliace |
        | Fază Venoasă Portală (Abdomen & Pelvis) | 70 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Suspiciune de adenocarcinom ductal pancreatic sau masă pancreatică neelucidată
        - Caracterizare leziuni chistice pancreatice (IPMN, chistadenom seros/mucinos, pseudochist)
        - Tumori neuroendocrine pancreatice (insulinom, gastrinom, glucagonom)
        - Stadializare pre-operatorie a rezecabilității vasculare (artera mezenterică superioară, trunchi celiac, venă portă/VMS)
        - Icter mecanic obstructiv nedureros (semnul Courvoisier-Terrier)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat digestiv & Abdomen*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 4 (Ridicată > 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Contrast oral neutru: 500-750 mL apă simplă cu 15-20 min înainte de scanare pentru distensie duodenală și gastrică optimă

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 125-150 mL |
        | Rată de Flux | 4.0 - 5.0 mL/s |
        | Durată | 25-30s |
        | Metodă Temporizare | Fază Parenchimatoasă Pancreatică la 40-45 secunde + Fază Venoasă Portală la 70 secunde |
        | Poziționare ROI | Aorta abdominală la nivelul trunchiului celiac |
        | Declanșator (HU) | 150 HU (+ 25 sec delay pentru faza pancreatică) |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | CAREkV 100-120 kV |
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

        - Injectare cu debit înalt (4-5 mL/s) printr-o canulă 18-20G certificată high-pressure. Flush salin 40 mL. Pacientul bea 500 mL apă chiar înainte de a se așeza pe masă.

    === "Note Asistent"

        - Supraveghere strictă a accesului venos la debite mari.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m².
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Criterii de nerezecabilitate: contact tumoral > 180° cu trunchiul celiac sau AMS; ocluzie nereconstructibilă a venei porte sau VMS. Măsurați diametrul canalului Wirsung și CBP.

    === "Sfaturi & Recomandări"

        - Tumorile neuroendocrine sunt hipervasculare și se încarcă intens în faza arterială/pancreatică timpurie, spre deosebire de adenocarcinom care este hipovascular.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă (Pancreas) | Cupole diafragmatice | Pol inferior renal | 0 sec | 1.0 mm | Detectare calcificări ductale (pancreatită cronică) sau hemoragii |
    | Fază Parenchimatoasă Pancreatică | Diafragm | Creste iliace | 40-45 sec (sau trigger + 25s) | 0.625 mm | Contrastare maximă a parenchimului pancreatic normal; adenocarcinomul apare hipodens/hipovascular pe acest fond |
    | Fază Venoasă Portală (Abdomen & Pelvis) | Diafragm | Simfiză pubiană | 70 sec | 0.625 mm | Evaluare invazie ax venos spleno-porto-mezenteric și metastaze hepatice/peritoneale |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Pancreatică & Portală | Pancreas / Abdomen | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D | Analiză detaliată a parenchimului și raporturilor vasculare |
    | Coronal & Sagital | Fază Pancreatică & Portală | Abdomen | 1.5 mm / 1.5 mm | Standard / I30f | Admire 3 / AIDR 3D | Reconstrucții coronale curbate pe ductul Wirsung și calea biliară principală |
