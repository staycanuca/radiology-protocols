---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Bilanț inițial de stadializare oncologică completă (limfom, melanom, cancer colorectal,
  cancer pulmonar, cancer mamar)
- Monitorizarea răspunsului terapeutic la chimioterapie / imunoterapie (criterii RECIST
  1.1)
- Sindrom febril prelungit de etiologie neelucidată (FUO)
- Scădere ponderală involuntară masivă cu suspiciune de neoplazie ocultă
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 40s
  flow_rate: 3.0 mL/s
  roi: N/A
  timing: 65-70 secunde delay (fază venoasă portală combinată torace-abdomen-pelvis)
  trigger: N/A
  volume: 120-140 mL
last_updated: '2026-09-20'
notes:
  additional_recons: MIP pulmonar axial de 5 mm pentru noduli.
  nursing: Verificare permeabilitate abord venos.
  rad: 'Examinare oncologică completă: plămâni, pleură, mediastin, ficat, suprarenale,
    retroperitoneu, mezenter, tub digestiv, pelvis și structuri osoase.'
  tech: Canulă 20G în plica cotului. Brațele ridicate. Flush salin 40 mL.
  tips: Pentru a reduce doza, asigurați-vă că pacientul este centrat exact în izocentrul
    gantry-ului.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: 'Contrast oral (opțional): 500-750 mL apă sau Readi-Cat 2'
protocol_type: contrast-enhanced
recons:
- acquisition: CT CAP
  fov: Torace / Abdomen / Bazin
  ir_strength: Admire 3 / AIDR 3D
  kernel: Pulmonar (I50f) + Mediastinal (I30f) + Abdomen (I30f) + Osos (I70f)
  notes: Serii complete multiplanare pentru torace, abdomen, pelvis și os
  plane: Axial, Coronal & Sagital
  thickness_increment: 2.5 mm / 2.5 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m².
series:
- delay: 65-70 sec
  end: Simfiză pubiană / mici trohantere
  name: CT CAP cu Contrast
  notes: Scanare continuă torace, abdomen și pelvis într-o singură apnee inspiratorie
    dacă este posibil
  start: Vârfuri pulmonare
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.9 - 1.1
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Torace, Abdomen & Pelvis (CAP) cu Contrast (Protocol OHSU)
---

# CT Torace, Abdomen & Pelvis (CAP) cu Contrast (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT CAP cu Contrast | 65-70 sec | Vârfuri pulmonare → Simfiză pubiană / mici trohantere |

    === "Indicații Clinice"

        - Bilanț inițial de stadializare oncologică completă (limfom, melanom, cancer colorectal, cancer pulmonar, cancer mamar)
        - Monitorizarea răspunsului terapeutic la chimioterapie / imunoterapie (criterii RECIST 1.1)
        - Sindrom febril prelungit de etiologie neelucidată (FUO)
        - Scădere ponderală involuntară masivă cu suspiciune de neoplazie ocultă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Contrast oral (opțional): 500-750 mL apă sau Readi-Cat 2

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 120-140 mL |
        | Rată de Flux | 3.0 mL/s |
        | Durată | 40s |
        | Metodă Temporizare | 65-70 secunde delay (fază venoasă portală combinată torace-abdomen-pelvis) |
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
    | **Tensiune Tub (kV)** | CAREkV 100-120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 20G în plica cotului. Brațele ridicate. Flush salin 40 mL.

    === "Note Asistent"

        - Verificare permeabilitate abord venos.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m².
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Examinare oncologică completă: plămâni, pleură, mediastin, ficat, suprarenale, retroperitoneu, mezenter, tub digestiv, pelvis și structuri osoase.

    === "Sfaturi & Recomandări"

        - Pentru a reduce doza, asigurați-vă că pacientul este centrat exact în izocentrul gantry-ului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT CAP cu Contrast | Vârfuri pulmonare | Simfiză pubiană / mici trohantere | 65-70 sec | 0.625 mm | Scanare continuă torace, abdomen și pelvis într-o singură apnee inspiratorie dacă este posibil |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | CT CAP | Torace / Abdomen / Bazin | 2.5 mm / 2.5 mm | Pulmonar (I50f) + Mediastinal (I30f) + Abdomen (I30f) + Osos (I70f) | Admire 3 / AIDR 3D | Serii complete multiplanare pentru torace, abdomen, pelvis și os |
