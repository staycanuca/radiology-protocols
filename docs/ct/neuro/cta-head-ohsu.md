---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Anevrism intracranian suspectat sau monitorizat post-clipping/coiling
- Suspiciune de vasospasm cerebral post-hemoragie subarahnoidiană (HSA)
- Ocluzii sau stenoze intracraniene (M1, M2, A1, P1, trunchi bazilar)
- Malformații arterio-venoase cerebrale (MAV)
contrast:
  agent: Omnipaque 300 / Isovue 370
  duration: 20-25s
  flow_rate: 4.0 - 5.0 mL/s (Adult) / 1.0-4.0 mL/s (Peds)
  roi: Artera carotidă internă la baza craniului
  timing: Scanare la 45 secunde de la debutul injectării (sau bolus tracking)
  trigger: 120 HU
  volume: 100 mL (Adult) / 2 mL/kg (Peds, max 100 mL)
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 2 (Mică 1 - 3 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: MIP rotit la 360° și randare de volum 3D.
  nursing: Monitorizare debit injectare și absența extravazării.
  rad: Căutați anevrisme saculare la bifurcații, vasospasm focal sau difuz, tromboză
    de sinus venos asociată.
  tech: Canulă 20G antecubitală. În caz de mișcare a pacientului (Toshiba), se recomandă
    repetare cu achiziție de volum (Volume Acquisition).
  tips: Capul centrat perfect fără înclinare laterală.
npo: Repaus alimentar 2-4 ore dacă este posibil
position: Decubit dorsal, centrare pe bărbia pacientului (chin), fără angulare gantry
premedication: CT Craniu Nativ înainte de CTA Head conform cerințelor OHSU
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Cerebral
  fov: Cap
  ir_strength: Standard
  kernel: Creier / Vascular
  notes: Serii MIP multiplanare pentru evaluarea geometriei anevrismale și bifurcațiilor
  plane: Axial, Coronal & Sagital
  thickness_increment: 5.0 mm / 2.5 mm MIP
- acquisition: CTA Cerebral
  fov: Cap
  ir_strength: Standard
  kernel: Creier / Vascular
  notes: Secțiuni fine de 1 mm pentru randare MPR detaliată
  plane: Axial, Coronal & Sagital
  thickness_increment: 1.0 mm / 1.0 mm Avg
safety:
  allergy: Conform politicii OHSU.
  renal: eGFR conform protocolului OHSU.
series:
- delay: 45 sec (sau trigger)
  end: Deasupra vertexului
  name: CTA Cerebral
  notes: DFOV 220 mm; acoperire a întregului parenchim și sistem vascular intracranian
  start: Sub baza craniului (gaura occipitală)
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CTA Cerebral / Cap cu Contrast (Protocol OHSU)
---

# CTA Cerebral / Cap cu Contrast (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CTA Cerebral | 45 sec (sau trigger) | Sub baza craniului (gaura occipitală) → Deasupra vertexului |

    === "Indicații Clinice"

        - Anevrism intracranian suspectat sau monitorizat post-clipping/coiling
        - Suspiciune de vasospasm cerebral post-hemoragie subarahnoidiană (HSA)
        - Ocluzii sau stenoze intracraniene (M1, M2, A1, P1, trunchi bazilar)
        - Malformații arterio-venoase cerebrale (MAV)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cap, Gât & Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Mică 1 - 3 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, centrare pe bărbia pacientului (chin), fără angulare gantry
    - **Repaus Alimentar (NPO):** Repaus alimentar 2-4 ore dacă este posibil
    - **Premedicație / Pregătire:**
        - CT Craniu Nativ înainte de CTA Head conform cerințelor OHSU

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 300 / Isovue 370 |
        | Volum | 100 mL (Adult) / 2 mL/kg (Peds, max 100 mL) |
        | Rată de Flux | 4.0 - 5.0 mL/s (Adult) / 1.0-4.0 mL/s (Peds) |
        | Durată | 20-25s |
        | Metodă Temporizare | Scanare la 45 secunde de la debutul injectării (sau bolus tracking) |
        | Poziționare ROI | Artera carotidă internă la baza craniului |
        | Declanșator (HU) | 120 HU |

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
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 20G antecubitală. În caz de mișcare a pacientului (Toshiba), se recomandă repetare cu achiziție de volum (Volume Acquisition).

    === "Note Asistent"

        - Monitorizare debit injectare și absența extravazării.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR conform protocolului OHSU.
            - **Alergii:** Conform politicii OHSU.

    === "Note Radiolog"

        - Căutați anevrisme saculare la bifurcații, vasospasm focal sau difuz, tromboză de sinus venos asociată.

    === "Sfaturi & Recomandări"

        - Capul centrat perfect fără înclinare laterală.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CTA Cerebral | Sub baza craniului (gaura occipitală) | Deasupra vertexului | 45 sec (sau trigger) | 0.625 mm | DFOV 220 mm; acoperire a întregului parenchim și sistem vascular intracranian |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | CTA Cerebral | Cap | 5.0 mm / 2.5 mm MIP | Creier / Vascular | Standard | Serii MIP multiplanare pentru evaluarea geometriei anevrismale și bifurcațiilor |
    | Axial, Coronal & Sagital | CTA Cerebral | Cap | 1.0 mm / 1.0 mm Avg | Creier / Vascular | Standard | Secțiuni fine de 1 mm pentru randare MPR detaliată |
