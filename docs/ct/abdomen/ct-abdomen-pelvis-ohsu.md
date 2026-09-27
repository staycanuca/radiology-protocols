---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Dureri abdominale acute sau cronice de etiologie neprecizată
- Suspiciune de infecții intraabdominale, colecții sau abcese
- Diverticulită acută, apendicită sau patologie inflamatorie pelvină
- Monitorizare oncologică și stadializare neoplazică
- Ocluzie intestinală sau suspiciune de ischemie mezenterică
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 35-40s
  flow_rate: 2.5 - 3.0 mL/s
  roi: N/A
  timing: Timp empiric de întârziere 65-70 secunde (fază venoasă portală)
  trigger: N/A
  volume: 100 mL (1.5 mL/kg, max 120 mL)
iris_reference:
  chapter: Aparat uro-genital și glande suprarenale
  radiation_dose: Clasa 4 (Ridicată > 10 mSv)
  recommendation_grade: Grad B
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții coronale și sagitale oblice la nevoie; secțiuni
    fine 1.0 mm pentru evaluare vasculară 3D MIP.
  nursing: Canulă venoasă 20G în plica cotului. Verificare extravazare cu flush salin
    20 mL înainte de injectarea contrastului.
  rad: Examinare sistematică a parenchimelor abdominale (ficat, splină, pancreas,
    rinichi, suprarenale), tractului digestiv, spațiilor peritoneale și retroperitoneale,
    ganglionilor și structurilor vasculare.
  tech: 'Verificați abordul venos periferic (20G preferat). Brațele complet ridicate
    deasupra capului pentru a preveni artefactele de beam-hardening. Ghidare respirație:
    apnee inspiratorie.'
  tips: La pacienți tineri sau cu suspiciune de litiază urinară, se recomandă evaluare
    preliminară nativă cu doză ultra-joasă (ultra-low-dose).
npo: Repaus alimentar 4 ore pentru alimente solide; hidratare orală permisă
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: 'Contrast oral (opțional conform indicației): 500-750 mL apă sau Readi-Cat
  2 fracționat cu 30-45 min înainte de scanare'
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D Standard
  kernel: Standard / I30f
  notes: Serie diagnostică primară
  plane: Axial
  thickness_increment: 3.0 mm / 3.0 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D Standard
  kernel: Standard / I30f
  notes: Evaluare anatomică cranio-caudală a viscerelor și mezenterului
  plane: Coronal
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D Standard
  kernel: Standard / I30f
  notes: Relații topografice și anse digestive
  plane: Sagital
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Screening conform politicii OHSU. Premedicație cu corticosteroizi + antihistaminice
    dacă pacientul are antecedente de reacție alergică la iod.
  renal: Evaluare eGFR conform politicii OHSU. Dacă eGFR < 30 mL/min/1.73m², discutați
    cu medicul radiolog oportunitatea examinării sau hidratării.
series:
- delay: 65-70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală
  notes: Achiziție în apnee inspiratorie completă; acoperire completă abdomen și pelvis
  start: Cupole diafragmatice
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV (Ref 120 kV)
  mas: CAREDose4D / SureExposure3D (Ref 180-220 mAs)
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Abdomen & Pelvis Rutină (Protocol OHSU)
---

# CT Abdomen & Pelvis Rutină (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Venoasă Portală | 65-70 sec | Cupole diafragmatice → Simfiză pubiană |

    === "Indicații Clinice"

        - Dureri abdominale acute sau cronice de etiologie neprecizată
        - Suspiciune de infecții intraabdominale, colecții sau abcese
        - Diverticulită acută, apendicită sau patologie inflamatorie pelvină
        - Monitorizare oncologică și stadializare neoplazică
        - Ocluzie intestinală sau suspiciune de ischemie mezenterică

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat uro-genital și glande suprarenale*
            - **Grad de Recomandare:** **Grad B**
            - **Nivel de Iradiere Estimată:** `Clasa 4 (Ridicată > 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore pentru alimente solide; hidratare orală permisă
    - **Premedicație / Pregătire:**
        - Contrast oral (opțional conform indicației): 500-750 mL apă sau Readi-Cat 2 fracționat cu 30-45 min înainte de scanare

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 100 mL (1.5 mL/kg, max 120 mL) |
        | Rată de Flux | 2.5 - 3.0 mL/s |
        | Durată | 35-40s |
        | Metodă Temporizare | Timp empiric de întârziere 65-70 secunde (fază venoasă portală) |
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
    | **Tensiune Tub (kV)** | CAREkV (Ref 120 kV) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D (Ref 180-220 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Verificați abordul venos periferic (20G preferat). Brațele complet ridicate deasupra capului pentru a preveni artefactele de beam-hardening. Ghidare respirație: apnee inspiratorie.

    === "Note Asistent"

        - Canulă venoasă 20G în plica cotului. Verificare extravazare cu flush salin 20 mL înainte de injectarea contrastului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Evaluare eGFR conform politicii OHSU. Dacă eGFR < 30 mL/min/1.73m², discutați cu medicul radiolog oportunitatea examinării sau hidratării.
            - **Alergii:** Screening conform politicii OHSU. Premedicație cu corticosteroizi + antihistaminice dacă pacientul are antecedente de reacție alergică la iod.

    === "Note Radiolog"

        - Examinare sistematică a parenchimelor abdominale (ficat, splină, pancreas, rinichi, suprarenale), tractului digestiv, spațiilor peritoneale și retroperitoneale, ganglionilor și structurilor vasculare.

    === "Sfaturi & Recomandări"

        - La pacienți tineri sau cu suspiciune de litiază urinară, se recomandă evaluare preliminară nativă cu doză ultra-joasă (ultra-low-dose).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Venoasă Portală | Cupole diafragmatice | Simfiză pubiană | 65-70 sec | 0.625 mm | Achiziție în apnee inspiratorie completă; acoperire completă abdomen și pelvis |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Venoasă Portală | Abdomen | 3.0 mm / 3.0 mm | Standard / I30f | Admire 3 / AIDR 3D Standard | Serie diagnostică primară |
    | Coronal | Fază Venoasă Portală | Abdomen | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D Standard | Evaluare anatomică cranio-caudală a viscerelor și mezenterului |
    | Sagital | Fază Venoasă Portală | Abdomen | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D Standard | Relații topografice și anse digestive |
