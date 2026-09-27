---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: chest
clinical_indications:
- Suspiciune de disecție acută de aortă toracică (Stanford tip A sau B)
- 'Sindrom aortic acut: hematom intramural (IMH), ulcer penetrant aterosclerotic (PAU)'
- Durere toracică posterioară sfâșietoare sau migratoare, asimetrie de puls/tensiune
  arterială
- Evaluare pre și post-operatorie de anevrism aortic toracic / proteză vasculară (TEVAR)
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 20-25s
  flow_rate: 4.0 - 5.0 mL/s
  roi: Lumenul aortei descendente la nivelul bifurcației traheale
  timing: Bolus tracking pe aorta descendentă / crosa aortică; trigger la 120-150
    HU
  trigger: 120-150 HU
  volume: 100-120 mL (adaptat la greutate)
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 3 (Moderată 5 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: Verificare eGFR, tensiune arterială la ambele brațe. Nu se întârzie examinarea
    în suspiciune clinică de disecție de tip A.
  rad: Verificați implicarea ostiilor coronariene, a trunchiului brahiocefalic, arterei
    carotide comune stângi și subclaviei stângi. Evaluați hemopericardul și hemotoracele.
  tech: Scanare caudo-cranială sau cranio-caudală rapidă. Canulă 18G în plica cotului.
    Flush salin 50 mL la 4.5 mL/s imediat post-contrast.
  tips: Apnee inspiratorie completă; asigurați-vă că scanarea se extinde suficient
    distal dacă există suspiciune de ischemie mezenterică sau renală secundară.
npo: Repaus alimentar 2-4 ore dacă starea clinică permite; în urgență N/A
position: Decubit dorsal, brațele ridicate deasupra capului
premedication: Fără contrast oral. Monitorizare continuă a tensiunii arteriale și
  a ritmului cardiac.
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Aortă Toracică
  fov: Torace
  ir_strength: Standard
  kernel: Mediastinal Standard
  notes: Serie diagnostică primară de înaltă rezoluție
  plane: Axial
  thickness_increment: 1.25 mm / 1.0 mm
- acquisition: CTA Aortă Toracică
  fov: Torace
  ir_strength: Standard
  kernel: Mediastinal Standard
  notes: Vizualizare completă a crosei și aortei descendente
  plane: Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CTA Aortă Toracică
  fov: Aortă Toracică
  ir_strength: Standard
  kernel: Standard
  notes: MIP de-a lungul curburii aortice (candy cane view) și reconstrucții 3D VR
  plane: MIP Oblic & 3D VR
  thickness_increment: 3.0 mm MIP
safety:
  allergy: Conform politicii instituționale de urgență. Beneficiul salvării vieții
    primează.
  renal: eGFR de referință; la pacienți instabili cu suspiciune acută se administrează
    hidratare post-procedurală.
series:
- delay: 0 sec
  end: Sub diafragm / glande suprarenale
  name: CT Torace Nativ (Pre-contrast)
  notes: Esențial pentru evidențierea hematomului intramural hiperdens și a deplasării
    calcificărilor intimale
  start: Deasupra apexurilor pulmonare
  thickness: 2.5 mm
- delay: Trigger + 3-5 sec
  end: Sub diafragm (sau extins pelvin până la arterele femurale comune dacă disecția
    este extinsă)
  name: CTA Aortă Toracică Angiografică
  notes: Opacifiere densă a lumenului adevărat și fals (> 300 HU); identificare fald
    intimal și orificiu de intrare
  start: Deasupra apexurilor pulmonare
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100 - 120 kVp (AEC activ)
  mas: CAREDose4D / SmartmA modulare automată
  pitch: 0.8 - 1.0
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal sincronizat ECG (ECG-gated opțional la rădăcina aortică)
  slice_thickness: 0.625 - 1.25 mm
title: CTA Disecție Aortă Toracică (Protocol Dartmouth Hitchcock)
---

# CTA Disecție Aortă Toracică (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Torace Nativ (Pre-contrast) | 0 sec | Deasupra apexurilor pulmonare → Sub diafragm / glande suprarenale |
        | CTA Aortă Toracică Angiografică | Trigger + 3-5 sec | Deasupra apexurilor pulmonare → Sub diafragm (sau extins pelvin până la arterele femurale comune dacă disecția este extinsă) |

    === "Indicații Clinice"

        - Suspiciune de disecție acută de aortă toracică (Stanford tip A sau B)
        - Sindrom aortic acut: hematom intramural (IMH), ulcer penetrant aterosclerotic (PAU)
        - Durere toracică posterioară sfâșietoare sau migratoare, asimetrie de puls/tensiune arterială
        - Evaluare pre și post-operatorie de anevrism aortic toracic / proteză vasculară (TEVAR)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 2-4 ore dacă starea clinică permite; în urgență N/A
    - **Premedicație / Pregătire:**
        - Fără contrast oral. Monitorizare continuă a tensiunii arteriale și a ritmului cardiac.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 100-120 mL (adaptat la greutate) |
        | Rată de Flux | 4.0 - 5.0 mL/s |
        | Durată | 20-25s |
        | Metodă Temporizare | Bolus tracking pe aorta descendentă / crosa aortică; trigger la 120-150 HU |
        | Poziționare ROI | Lumenul aortei descendente la nivelul bifurcației traheale |
        | Declanșator (HU) | 120-150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 - 120 kVp (AEC activ) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SmartmA modulare automată |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 - 1.25 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (ECG-gated opțional la rădăcina aortică) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare caudo-cranială sau cranio-caudală rapidă. Canulă 18G în plica cotului. Flush salin 50 mL la 4.5 mL/s imediat post-contrast.

    === "Note Asistent"

        - Verificare eGFR, tensiune arterială la ambele brațe. Nu se întârzie examinarea în suspiciune clinică de disecție de tip A.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR de referință; la pacienți instabili cu suspiciune acută se administrează hidratare post-procedurală.
            - **Alergii:** Conform politicii instituționale de urgență. Beneficiul salvării vieții primează.

    === "Note Radiolog"

        - Verificați implicarea ostiilor coronariene, a trunchiului brahiocefalic, arterei carotide comune stângi și subclaviei stângi. Evaluați hemopericardul și hemotoracele.

    === "Sfaturi & Recomandări"

        - Apnee inspiratorie completă; asigurați-vă că scanarea se extinde suficient distal dacă există suspiciune de ischemie mezenterică sau renală secundară.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Torace Nativ (Pre-contrast) | Deasupra apexurilor pulmonare | Sub diafragm / glande suprarenale | 0 sec | 2.5 mm | Esențial pentru evidențierea hematomului intramural hiperdens și a deplasării calcificărilor intimale |
    | CTA Aortă Toracică Angiografică | Deasupra apexurilor pulmonare | Sub diafragm (sau extins pelvin până la arterele femurale comune dacă disecția este extinsă) | Trigger + 3-5 sec | 0.625 mm | Opacifiere densă a lumenului adevărat și fals (> 300 HU); identificare fald intimal și orificiu de intrare |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA Aortă Toracică | Torace | 1.25 mm / 1.0 mm | Mediastinal Standard | Standard | Serie diagnostică primară de înaltă rezoluție |
    | Coronal & Sagital | CTA Aortă Toracică | Torace | 2.0 mm / 2.0 mm | Mediastinal Standard | Standard | Vizualizare completă a crosei și aortei descendente |
    | MIP Oblic & 3D VR | CTA Aortă Toracică | Aortă Toracică | 3.0 mm MIP | Standard | Standard | MIP de-a lungul curburii aortice (candy cane view) și reconstrucții 3D VR |
