---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Caracterizarea unei formațiuni tumorale renale solide sau chistice (clasificare
  Bosniak v2019)
- Diferențierea carcinomului cu celule renale (RCC) de angiomiolipom (AML) sau oncocitom
- Stadializare pre-operatorie TNM (invazie venoasă în vena renală / VCI, extensie
  perinefretică)
- 'Planificare chirurgicală de nefrectomie parțială (nephrometry score: R.E.N.A.L.)'
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 30-35s
  flow_rate: 3.5 - 4.0 mL/s
  roi: N/A
  timing: Fază Corticomedulară la 30-40 secunde + Fază Nefrografică la 100 secunde
    + Fază Excretorie la 8-10 minute
  trigger: N/A
  volume: 120-140 mL
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D VR ale arterelor și venelor renale pentru chirurgia
    robotică parțială.
  nursing: Monitorizare debit injectare.
  rad: 'Criteriu cert de încărcare: creștere a densității cu > 15-20 HU între faza
    nativă și faza nefrografică. Aplicați clasificarea Bosniak v2019 pentru leziunile
    chistice renale.'
  tech: Canulă 20G antecubitală. Flush salin 40 mL. Asigurați-vă că pacientul este
    cooperant la apnee.
  tips: Faza nefrografică (100 sec) este cea mai sensibilă pentru detectarea și delimitarea
    tumorilor renale; faza corticomedulară singură poate omite tumori mici medulare.
npo: Repaus alimentar 4 ore; hidratare permisă
position: Decubit dorsal cu brațele ridicate
premedication: Fără contrast oral iodat sau baritat; 500 mL apă permisă
protocol_type: multiphase
recons:
- acquisition: Toate fazele
  fov: Rinichi
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Secțiuni fine pentru măsurători HU precise de wash-in și wash-out
  plane: Axial & Coronal
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m² obligatoriu.
series:
- delay: 0 sec
  end: L3 (sub polul inferior renal)
  name: Fază Nativă (Rinichi)
  notes: Măsurare densitate bazală HU; detectare calcificări și densități negative
    de grăsime macroscopică (< -20 HU specifică AML)
  start: T11 (deasupra rinichilor)
  thickness: 1.0 mm
- delay: 30-40 sec
  end: L3
  name: Fază Corticomedulară (Arterială)
  notes: Diferențiere cortex-medulară; anatomie vasculară arterială renală și încărcare
    tumorală precoce
  start: T11
  thickness: 0.625 mm
- delay: 100 sec
  end: Simfiză pubiană (sau pol inferior renal)
  name: Fază Nefrografică
  notes: 'Faza diagnostică cheie: parenchim renal omogen dens; detectare optimă a
    masei tumorale hipovasculare și a invaziei în grăsimea sinusului renal'
  start: Diafragm
  thickness: 0.625 mm
- delay: 8-10 min
  end: Simfiză pubiană
  name: Fază Excretorie Tardivă
  notes: Apreciere raport tumoră cu sistemul colector pielocaliceal (pre-nefrectomie
    parțială)
  start: T11
  thickness: 1.0 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Masă Renală / Protocol Rinichi Multifazic (Protocol OHSU)
---

# CT Masă Renală / Protocol Rinichi Multifazic (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă (Rinichi) | 0 sec | T11 (deasupra rinichilor) → L3 (sub polul inferior renal) |
        | Fază Corticomedulară (Arterială) | 30-40 sec | T11 → L3 |
        | Fază Nefrografică | 100 sec | Diafragm → Simfiză pubiană (sau pol inferior renal) |
        | Fază Excretorie Tardivă | 8-10 min | T11 → Simfiză pubiană |

    === "Indicații Clinice"

        - Caracterizarea unei formațiuni tumorale renale solide sau chistice (clasificare Bosniak v2019)
        - Diferențierea carcinomului cu celule renale (RCC) de angiomiolipom (AML) sau oncocitom
        - Stadializare pre-operatorie TNM (invazie venoasă în vena renală / VCI, extensie perinefretică)
        - Planificare chirurgicală de nefrectomie parțială (nephrometry score: R.E.N.A.L.)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore; hidratare permisă
    - **Premedicație / Pregătire:**
        - Fără contrast oral iodat sau baritat; 500 mL apă permisă

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 120-140 mL |
        | Rată de Flux | 3.5 - 4.0 mL/s |
        | Durată | 30-35s |
        | Metodă Temporizare | Fază Corticomedulară la 30-40 secunde + Fază Nefrografică la 100 secunde + Fază Excretorie la 8-10 minute |
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
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 20G antecubitală. Flush salin 40 mL. Asigurați-vă că pacientul este cooperant la apnee.

    === "Note Asistent"

        - Monitorizare debit injectare.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m² obligatoriu.
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Criteriu cert de încărcare: creștere a densității cu > 15-20 HU între faza nativă și faza nefrografică. Aplicați clasificarea Bosniak v2019 pentru leziunile chistice renale.

    === "Sfaturi & Recomandări"

        - Faza nefrografică (100 sec) este cea mai sensibilă pentru detectarea și delimitarea tumorilor renale; faza corticomedulară singură poate omite tumori mici medulare.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă (Rinichi) | T11 (deasupra rinichilor) | L3 (sub polul inferior renal) | 0 sec | 1.0 mm | Măsurare densitate bazală HU; detectare calcificări și densități negative de grăsime macroscopică (< -20 HU specifică AML) |
    | Fază Corticomedulară (Arterială) | T11 | L3 | 30-40 sec | 0.625 mm | Diferențiere cortex-medulară; anatomie vasculară arterială renală și încărcare tumorală precoce |
    | Fază Nefrografică | Diafragm | Simfiză pubiană (sau pol inferior renal) | 100 sec | 0.625 mm | Faza diagnostică cheie: parenchim renal omogen dens; detectare optimă a masei tumorale hipovasculare și a invaziei în grăsimea sinusului renal |
    | Fază Excretorie Tardivă | T11 | Simfiză pubiană | 8-10 min | 1.0 mm | Apreciere raport tumoră cu sistemul colector pielocaliceal (pre-nefrectomie parțială) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial & Coronal | Toate fazele | Rinichi | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D | Secțiuni fine pentru măsurători HU precise de wash-in și wash-out |
