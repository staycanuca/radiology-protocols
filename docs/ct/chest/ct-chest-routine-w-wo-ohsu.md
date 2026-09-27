---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: chest
clinical_indications:
- Evaluare mase și noduli pulmonari, adenopatii mediastinale sau hilare
- Pneumonii complicate, abces pulmonar, empiem pleural
- Stadializare și reevaluare neoplazică în cancerul bronhopulmonar
- Traumatisme toracice, hemotorax, pneumotorax
- Patologie vasculară mediastinală sau aortică
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 25-30s
  flow_rate: 2.5 - 3.0 mL/s
  roi: N/A
  timing: 30-35 secunde delay (fază arterială/mediastinală timpurie)
  trigger: N/A
  volume: 80-100 mL
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 3 (Moderată 5 - 8 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: MIP și MinIP pentru decelarea nodulilor micronodulari și a bronșiilor
    dilatate.
  nursing: Verificare permeabilitate abord venos periferic.
  rad: Căutați noduli pulmonari, bronhogramă aerică, revărsate pleurale, adenopatii
    mediastinale (> 10 mm pe axul scurt) și afectare pericardică.
  tech: 'Canulă 20G antecubitală. Instrucțiuni de respirație clare: ''inspirați adânc
    și opriți respirația''. Flush salin 30 mL.'
  tips: Pentru evaluarea strictă a parenchimului fără contrast, se aplică protocolul
    Chest WO cu doză redusă.
npo: Repaus alimentar 4 ore pentru examinarea cu contrast; N/A pentru nativ
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Fără contrast oral
protocol_type: contrast-enhanced
recons:
- acquisition: CT Torace
  fov: Torace
  ir_strength: Admire 3 / AIDR 3D
  kernel: Pulmonar (I50f / Lung) + Mediastinal (I30f / Soft Tissue)
  notes: Fereastră de parenchim pulmonar (W1500 / L-600) și fereastră mediastinală
    (W350 / L40)
  plane: Axial, Coronal & Sagital
  thickness_increment: 1.5 mm / 1.5 mm
safety:
  allergy: Conform politicii OHSU dacă se administrează contrast.
  renal: Conform politicii OHSU dacă se administrează contrast.
series:
- delay: 30-35 sec (sau 0 sec dacă nativ)
  end: Sub recesurile costo-diafragmatice posterioare (baza plămânilor)
  name: CT Torace
  notes: Scanare în apnee inspiratorie profundă
  start: Deasupra vârfurilor pulmonare
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 1.0 - 1.2
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Torace Nativ & cu Contrast (Protocol OHSU)
---

# CT Torace Nativ & cu Contrast (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Torace | 30-35 sec (sau 0 sec dacă nativ) | Deasupra vârfurilor pulmonare → Sub recesurile costo-diafragmatice posterioare (baza plămânilor) |

    === "Indicații Clinice"

        - Evaluare mase și noduli pulmonari, adenopatii mediastinale sau hilare
        - Pneumonii complicate, abces pulmonar, empiem pleural
        - Stadializare și reevaluare neoplazică în cancerul bronhopulmonar
        - Traumatisme toracice, hemotorax, pneumotorax
        - Patologie vasculară mediastinală sau aortică

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 8 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore pentru examinarea cu contrast; N/A pentru nativ
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 80-100 mL |
        | Rată de Flux | 2.5 - 3.0 mL/s |
        | Durată | 25-30s |
        | Metodă Temporizare | 30-35 secunde delay (fază arterială/mediastinală timpurie) |
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
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 1.0 - 1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 20G antecubitală. Instrucțiuni de respirație clare: 'inspirați adânc și opriți respirația'. Flush salin 30 mL.

    === "Note Asistent"

        - Verificare permeabilitate abord venos periferic.

        !!! warning "Siguranță"
            - **Funcție Renală:** Conform politicii OHSU dacă se administrează contrast.
            - **Alergii:** Conform politicii OHSU dacă se administrează contrast.

    === "Note Radiolog"

        - Căutați noduli pulmonari, bronhogramă aerică, revărsate pleurale, adenopatii mediastinale (> 10 mm pe axul scurt) și afectare pericardică.

    === "Sfaturi & Recomandări"

        - Pentru evaluarea strictă a parenchimului fără contrast, se aplică protocolul Chest WO cu doză redusă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Torace | Deasupra vârfurilor pulmonare | Sub recesurile costo-diafragmatice posterioare (baza plămânilor) | 30-35 sec (sau 0 sec dacă nativ) | 0.625 mm | Scanare în apnee inspiratorie profundă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | CT Torace | Torace | 1.5 mm / 1.5 mm | Pulmonar (I50f / Lung) + Mediastinal (I30f / Soft Tissue) | Admire 3 / AIDR 3D | Fereastră de parenchim pulmonar (W1500 / L-600) și fereastră mediastinală (W350 / L40) |
