---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: chest
clinical_indications:
- Stadializare și reevaluare oncologică în cancerul bronhopulmonar (evaluare metastaze
  hepatice și suprarenaliene)
- Tumori mediastinale, timoame, mezoteliom pleural cu extensie subdiafragmatică
- Evaluare mase pulmonare cu suspiciune de invazie transdiafragmatică în ficat
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 30-35s
  flow_rate: 2.5 - 3.0 mL/s
  roi: N/A
  timing: 60-65 secunde delay (fază de contrastare hepatică și toracică optimă)
  trigger: N/A
  volume: 100 mL
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 3 (Moderată 5 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: MIP coronal toraco-abdominal.
  nursing: Pregătire abord venos și supraveghere injectare.
  rad: Evaluați parenchimul pulmonar primar, ganglionii hilari/mediastinali, leziunile
    focale hepatice (metastaze) și nodulii suprarenalieni.
  tech: Canulă 20G antecubitală. Asigurați-vă că scanarea coboară sub polul inferior
    al ficatului pentru a nu omite leziuni la nivelul lobului drept.
  tips: Delay-ul de 60-65 secunde oferă compromisul ideal între opacifierea vaselor
    mediastinale și contrastarea parenchimatoasă a ficatului.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Fără contrast oral
protocol_type: contrast-enhanced
recons:
- acquisition: CT Torace prin Ficat
  fov: Torace / Ficat
  ir_strength: Admire 3 / AIDR 3D
  kernel: Pulmonar (I50f) + Mediastinal/Parenchim (I30f)
  notes: Fereastră de parenchim pulmonar, mediastin și parenchim hepatic
  plane: Axial, Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m².
series:
- delay: 60-65 sec
  end: Polul inferior al ficatului și glandele suprarenale (nivel L2-L3)
  name: CT Torace Extins prin Ficat
  notes: Acoperire completă a întregului parenchim pulmonar, a ficatului și a ambelor
    glande suprarenale
  start: Vârfuri pulmonare
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 1.0 - 1.2
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Torace Extins prin Ficat cu Contrast (Protocol OHSU)
---

# CT Torace Extins prin Ficat cu Contrast (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Torace Extins prin Ficat | 60-65 sec | Vârfuri pulmonare → Polul inferior al ficatului și glandele suprarenale (nivel L2-L3) |

    === "Indicații Clinice"

        - Stadializare și reevaluare oncologică în cancerul bronhopulmonar (evaluare metastaze hepatice și suprarenaliene)
        - Tumori mediastinale, timoame, mezoteliom pleural cu extensie subdiafragmatică
        - Evaluare mase pulmonare cu suspiciune de invazie transdiafragmatică în ficat

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 100 mL |
        | Rată de Flux | 2.5 - 3.0 mL/s |
        | Durată | 30-35s |
        | Metodă Temporizare | 60-65 secunde delay (fază de contrastare hepatică și toracică optimă) |
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
    | **Pitch (Factor Pas)** | 1.0 - 1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 20G antecubitală. Asigurați-vă că scanarea coboară sub polul inferior al ficatului pentru a nu omite leziuni la nivelul lobului drept.

    === "Note Asistent"

        - Pregătire abord venos și supraveghere injectare.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m².
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Evaluați parenchimul pulmonar primar, ganglionii hilari/mediastinali, leziunile focale hepatice (metastaze) și nodulii suprarenalieni.

    === "Sfaturi & Recomandări"

        - Delay-ul de 60-65 secunde oferă compromisul ideal între opacifierea vaselor mediastinale și contrastarea parenchimatoasă a ficatului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Torace Extins prin Ficat | Vârfuri pulmonare | Polul inferior al ficatului și glandele suprarenale (nivel L2-L3) | 60-65 sec | 0.625 mm | Acoperire completă a întregului parenchim pulmonar, a ficatului și a ambelor glande suprarenale |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | CT Torace prin Ficat | Torace / Ficat | 2.0 mm / 2.0 mm | Pulmonar (I50f) + Mediastinal/Parenchim (I30f) | Admire 3 / AIDR 3D | Fereastră de parenchim pulmonar, mediastin și parenchim hepatic |
