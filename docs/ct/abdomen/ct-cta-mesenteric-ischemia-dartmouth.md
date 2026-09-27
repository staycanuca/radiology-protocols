---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: abdomen
clinical_indications:
- Suspiciune de ischemie mezenterică acută (durere abdominală severă disproporționată
  cu datele obiective)
- Tromboză sau embolie acută a arterei mezenterice superioare (AMS) sau a trunchiului
  celiac
- Tromboză venoasă mezenterică (VMS, venă portă)
- Ischemie non-ocluzivă mezenterică (NOMI) la pacienți în stare critică / șoc septic
  sau cardiogen
contrast:
  agent: Omnipaque 350 / Isovue 370 (Tehnică Split-Bolus 150 mL)
  duration: Bipazic cu pauză de 25s între injectări
  flow_rate: 4.0 mL/s
  roi: Aorta abdominală deasupra trunchiului celiac
  timing: Injectare 100 mL contrast -> pauză 25s -> injectare restul de 50 mL cu Smart
    Prep pe aortă
  trigger: 150 HU
  volume: '150 mL total: 100 mL la prima fază + 50 mL la a doua fază'
iris_reference:
  chapter: Abdomen & Pelvis
  radiation_dose: Clasa 3 (Moderată 5 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: Urgență chirurgicală și imagistică majoră — transport prompt și alertare
    radiolog.
  rad: 'Căutați semne de ischemie intestinală: defect de încărcare arterial/venos,
    îngroșare parietală, pneumatoză intestinală, gaz în sistemul portomezenteric,
    lichid liber, perforație (pneumoperitoneu).'
  tech: 'Canulă 18G sau 20G cu debit verificat la ser 4 mL/s. Respectați strict schema
    split bolus: 100 mL injectat, pauză 25s, apoi 50 mL cu Smart Prep.'
  tips: Planul sagital este crucial pentru evaluarea stenozei sau ocluziei ostiale
    a AMS și a trunchiului celiac.
npo: Repaus alimentar de urgență
position: Decubit dorsal, picioarele înainte (feet first), brațele ridicate deasupra
  capului
premedication: FĂRĂ contrast oral (contrastul oral pozitiv maschează hiperemia, edemul
  sau absența încărcării parietale a anselor intestinale)
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Abdomen & Pelvis
  fov: Abdomen-Pelvis
  ir_strength: Standard
  kernel: Standard
  notes: Serie trimisă în PACS pentru evaluare inițială
  plane: Axial Standard
  thickness_increment: 2.5 mm / 2.5 mm
- acquisition: CTA Abdomen & Pelvis
  fov: Abdomen-Pelvis
  ir_strength: Standard
  kernel: Standard
  notes: Serie subțire pentru vizualizarea ramurilor jejunale și ileale ale AMS
  plane: Axial Thin Slice
  thickness_increment: 1.25 mm / 1.0 mm
- acquisition: CTA Abdomen & Pelvis
  fov: Vase mezenterice
  ir_strength: Standard
  kernel: Standard
  notes: Originea trunchiului celiac și AMS evaluate optim în plan sagital
  plane: Coronal & Sagital MIP
  thickness_increment: 2.0 mm q 2.0 mm MIP
- acquisition: CTA Abdomen & Pelvis
  fov: Vase mezenterice
  ir_strength: Standard
  kernel: Standard
  notes: Rotire 3D aortă și reconstrucție dublu oblică a originilor viscerale
  plane: 3D VR & Curbat Aorto-Mezenteric
  thickness_increment: Reformatare curbată
safety:
  allergy: Conform politicii instituționale de urgență.
  renal: În suspiciune critică de ischemie mezenterică acută, scanarea nu se amână
    pentru așteptarea creatininei.
series:
- delay: Trigger Smart Prep pe aortă
  end: Sub simfiza pubiană
  name: CTA Abdomen & Pelvis Split-Bolus
  notes: Tehnica split-bolus DHMC realizează opacifiere arterială intensă concomitent
    cu faza venoasă mezenterică și parietală
  start: Deasupra cupolelor diafragmatice
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 100 - 120 kVp (AEC activ)
  mas: Modulare automată de doză
  pitch: 0.9 - 1.1
  rotation_time: 0.5 s
  scan_mode: Elicoidal rapid
  slice_thickness: 0.625 - 1.25 mm
title: CTA Ischemie Mezenterică - Split Bolus (Protocol Dartmouth Hitchcock)
---

# CTA Ischemie Mezenterică - Split Bolus (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CTA Abdomen & Pelvis Split-Bolus | Trigger Smart Prep pe aortă | Deasupra cupolelor diafragmatice → Sub simfiza pubiană |

    === "Indicații Clinice"

        - Suspiciune de ischemie mezenterică acută (durere abdominală severă disproporționată cu datele obiective)
        - Tromboză sau embolie acută a arterei mezenterice superioare (AMS) sau a trunchiului celiac
        - Tromboză venoasă mezenterică (VMS, venă portă)
        - Ischemie non-ocluzivă mezenterică (NOMI) la pacienți în stare critică / șoc septic sau cardiogen

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Abdomen & Pelvis*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, picioarele înainte (feet first), brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar de urgență
    - **Premedicație / Pregătire:**
        - FĂRĂ contrast oral (contrastul oral pozitiv maschează hiperemia, edemul sau absența încărcării parietale a anselor intestinale)

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 (Tehnică Split-Bolus 150 mL) |
        | Volum | 150 mL total: 100 mL la prima fază + 50 mL la a doua fază |
        | Rată de Flux | 4.0 mL/s |
        | Durată | Bipazic cu pauză de 25s între injectări |
        | Metodă Temporizare | Injectare 100 mL contrast -> pauză 25s -> injectare restul de 50 mL cu Smart Prep pe aortă |
        | Poziționare ROI | Aorta abdominală deasupra trunchiului celiac |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 - 120 kVp (AEC activ) kV |
    | **Curent Tub (mAs)** | Modulare automată de doză |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 - 1.25 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.1 |
    | **Mod Scanare** | Elicoidal rapid |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 18G sau 20G cu debit verificat la ser 4 mL/s. Respectați strict schema split bolus: 100 mL injectat, pauză 25s, apoi 50 mL cu Smart Prep.

    === "Note Asistent"

        - Urgență chirurgicală și imagistică majoră — transport prompt și alertare radiolog.

        !!! warning "Siguranță"
            - **Funcție Renală:** În suspiciune critică de ischemie mezenterică acută, scanarea nu se amână pentru așteptarea creatininei.
            - **Alergii:** Conform politicii instituționale de urgență.

    === "Note Radiolog"

        - Căutați semne de ischemie intestinală: defect de încărcare arterial/venos, îngroșare parietală, pneumatoză intestinală, gaz în sistemul portomezenteric, lichid liber, perforație (pneumoperitoneu).

    === "Sfaturi & Recomandări"

        - Planul sagital este crucial pentru evaluarea stenozei sau ocluziei ostiale a AMS și a trunchiului celiac.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CTA Abdomen & Pelvis Split-Bolus | Deasupra cupolelor diafragmatice | Sub simfiza pubiană | Trigger Smart Prep pe aortă | 0.625 mm | Tehnica split-bolus DHMC realizează opacifiere arterială intensă concomitent cu faza venoasă mezenterică și parietală |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial Standard | CTA Abdomen & Pelvis | Abdomen-Pelvis | 2.5 mm / 2.5 mm | Standard | Standard | Serie trimisă în PACS pentru evaluare inițială |
    | Axial Thin Slice | CTA Abdomen & Pelvis | Abdomen-Pelvis | 1.25 mm / 1.0 mm | Standard | Standard | Serie subțire pentru vizualizarea ramurilor jejunale și ileale ale AMS |
    | Coronal & Sagital MIP | CTA Abdomen & Pelvis | Vase mezenterice | 2.0 mm q 2.0 mm MIP | Standard | Standard | Originea trunchiului celiac și AMS evaluate optim în plan sagital |
    | 3D VR & Curbat Aorto-Mezenteric | CTA Abdomen & Pelvis | Vase mezenterice | Reformatare curbată | Standard | Standard | Rotire 3D aortă și reconstrucție dublu oblică a originilor viscerale |
