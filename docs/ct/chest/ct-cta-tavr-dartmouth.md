---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: chest
clinical_indications:
- Stenoză aortică severă simptomatică evaluată pentru implantare transcateter de valvă
  aortică (TAVR / TAVI)
- Măsurare inel aortic (arie, perimetru, diametre min/max) pentru alegerea mărimii
  protezei
- Calculul distanței de la inelul valvular la ostiile arterelor coronare stângă și
  dreaptă
- Evaluarea calcificărilor aparatului valvular și a tractului de ejecție al ventriculului
  stâng (LVOT)
- Cartografierea accesului vascular ilio-femural și aortei toraco-abdominale
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 18-22s
  flow_rate: 4.5 - 5.0 mL/s
  roi: Aorta descendentă la nivelul carinei
  timing: Bolus tracking pe aorta descendentă / rădăcina aortică
  trigger: 120-150 HU
  volume: 80-100 mL la prima fază cardiacă + 40-50 mL la faza thoraco-abdominală
iris_reference:
  chapter: Cardiologie & Angiografie
  radiation_dose: Clasa 3 (Moderată 5 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: Canulă venoasă periferică 18G în plica cotului drept preferată (evită artefactele
    de contrast din vena brahiocefalică stângă pe rădăcina aortică).
  rad: Măsurați perimetrul și aria inelului la nivelul planului cel mai caudal al
    celor 3 cuspe. Raportați distanța de la inel la ostiul coronarei stângi (< 10
    mm indică risc de ocluzie coronariană la expansiunea valvei).
  tech: 'Asigurați conexiune stabilă ECG cu undă R clară. Injector cu seringă dublă:
    contrast 90 mL urmat de 40 mL flush salin la 4.5 mL/s.'
  tips: Faza sistolică (30-40%) oferă adesea cele mai mari dimensiuni ale inelului
    aortic și este preferată pentru dimensionare.
npo: Repaus alimentar 4 ore
position: Decubit dorsal, brațele ridicate complet, electrozi ECG conectați, brățară
  de împământare
premedication: Fără contrast oral. Verificare ritm cardiac; beta-blocante conform
  protocolului cardiologic dacă ritmul este > 65 bpm.
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Angio-Cardiac TAVR
  fov: Cord (18-20 cm)
  ir_strength: High
  kernel: Cardiac Standard
  notes: Reconstrucții la 30-40% (sistolă) și 70-75% (diastolă) pentru măsurarea inelului
  plane: Axial Cardiac Multi-phase
  thickness_increment: 0.625 mm / 0.5 mm
- acquisition: CTA CAP Access
  fov: Torace-Abdomen-Pelvis
  ir_strength: Standard
  kernel: Standard
  notes: Cartografiere acces femural vascular
  plane: Axial, Coronal & Sagital
  thickness_increment: 1.5 mm / 1.5 mm
safety:
  allergy: Screening alergie contrast.
  renal: Verificare eGFR > 30 mL/min; pacienții cu stenoză aortică severă sunt fragili
    renal, optimizați volumul de contrast.
series:
- delay: Fără întârziere
  end: Sub baza cordului / diafragm
  name: Calcium Score Cardiac (Nativ)
  notes: Gated ECG prospectiv la 70-75% din ciclul R-R; cuantificare scor calciu Agatston
    valvular
  start: Nivelul carinei traheale
  thickness: 2.5 - 3.0 mm
- delay: Trigger + 4 sec
  end: Sub cord
  name: CTA Angio-Cardiac TAVR (Gated ECG)
  notes: Achiziție sincronizată ECG multipafazică (30-80% din ciclu) pentru analiza
    dinamicii sistolo-diastolice a inelului aortic
  start: Carină
  thickness: 0.625 mm
- delay: Continuare imediată fără pauză
  end: Sub simfiza pubiană (arterele femurale comune)
  name: CTA Aortă Toraco-Abdomino-Pelvină (CAP Access)
  notes: Evaluare calibru minim, tortuozitate și calcificări circumferențiale ale
    arterelor iliace și femurale
  start: Apexuri pulmonare
  thickness: 1.0 - 1.25 mm
tech_params:
  collimation: 128 × 0.6 mm
  kv: 100 - 120 kVp
  mas: Modulare adaptivă cardiacă
  pitch: ECG gated elicoidal sau Flash spiral
  rotation_time: 0.28 - 0.33 s
  scan_mode: Cardio ECG-gated pentru rădăcina aortică + Spirală rapidă pentru acces
    vascular
  slice_thickness: 0.625 mm
title: CTA Planificare Transcateter TAVR / TAVI (Protocol Dartmouth Hitchcock)
---

# CTA Planificare Transcateter TAVR / TAVI (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Calcium Score Cardiac (Nativ) | Fără întârziere | Nivelul carinei traheale → Sub baza cordului / diafragm |
        | CTA Angio-Cardiac TAVR (Gated ECG) | Trigger + 4 sec | Carină → Sub cord |
        | CTA Aortă Toraco-Abdomino-Pelvină (CAP Access) | Continuare imediată fără pauză | Apexuri pulmonare → Sub simfiza pubiană (arterele femurale comune) |

    === "Indicații Clinice"

        - Stenoză aortică severă simptomatică evaluată pentru implantare transcateter de valvă aortică (TAVR / TAVI)
        - Măsurare inel aortic (arie, perimetru, diametre min/max) pentru alegerea mărimii protezei
        - Calculul distanței de la inelul valvular la ostiile arterelor coronare stângă și dreaptă
        - Evaluarea calcificărilor aparatului valvular și a tractului de ejecție al ventriculului stâng (LVOT)
        - Cartografierea accesului vascular ilio-femural și aortei toraco-abdominale

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cardiologie & Angiografie*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, brațele ridicate complet, electrozi ECG conectați, brățară de împământare
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral. Verificare ritm cardiac; beta-blocante conform protocolului cardiologic dacă ritmul este > 65 bpm.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 80-100 mL la prima fază cardiacă + 40-50 mL la faza thoraco-abdominală |
        | Rată de Flux | 4.5 - 5.0 mL/s |
        | Durată | 18-22s |
        | Metodă Temporizare | Bolus tracking pe aorta descendentă / rădăcina aortică |
        | Poziționare ROI | Aorta descendentă la nivelul carinei |
        | Declanșator (HU) | 120-150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 - 120 kVp kV |
    | **Curent Tub (mAs)** | Modulare adaptivă cardiacă |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28 - 0.33 s |
    | **Pitch (Factor Pas)** | ECG gated elicoidal sau Flash spiral |
    | **Mod Scanare** | Cardio ECG-gated pentru rădăcina aortică + Spirală rapidă pentru acces vascular |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Asigurați conexiune stabilă ECG cu undă R clară. Injector cu seringă dublă: contrast 90 mL urmat de 40 mL flush salin la 4.5 mL/s.

    === "Note Asistent"

        - Canulă venoasă periferică 18G în plica cotului drept preferată (evită artefactele de contrast din vena brahiocefalică stângă pe rădăcina aortică).

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificare eGFR > 30 mL/min; pacienții cu stenoză aortică severă sunt fragili renal, optimizați volumul de contrast.
            - **Alergii:** Screening alergie contrast.

    === "Note Radiolog"

        - Măsurați perimetrul și aria inelului la nivelul planului cel mai caudal al celor 3 cuspe. Raportați distanța de la inel la ostiul coronarei stângi (< 10 mm indică risc de ocluzie coronariană la expansiunea valvei).

    === "Sfaturi & Recomandări"

        - Faza sistolică (30-40%) oferă adesea cele mai mari dimensiuni ale inelului aortic și este preferată pentru dimensionare.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Calcium Score Cardiac (Nativ) | Nivelul carinei traheale | Sub baza cordului / diafragm | Fără întârziere | 2.5 - 3.0 mm | Gated ECG prospectiv la 70-75% din ciclul R-R; cuantificare scor calciu Agatston valvular |
    | CTA Angio-Cardiac TAVR (Gated ECG) | Carină | Sub cord | Trigger + 4 sec | 0.625 mm | Achiziție sincronizată ECG multipafazică (30-80% din ciclu) pentru analiza dinamicii sistolo-diastolice a inelului aortic |
    | CTA Aortă Toraco-Abdomino-Pelvină (CAP Access) | Apexuri pulmonare | Sub simfiza pubiană (arterele femurale comune) | Continuare imediată fără pauză | 1.0 - 1.25 mm | Evaluare calibru minim, tortuozitate și calcificări circumferențiale ale arterelor iliace și femurale |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial Cardiac Multi-phase | CTA Angio-Cardiac TAVR | Cord (18-20 cm) | 0.625 mm / 0.5 mm | Cardiac Standard | High | Reconstrucții la 30-40% (sistolă) și 70-75% (diastolă) pentru măsurarea inelului |
    | Axial, Coronal & Sagital | CTA CAP Access | Torace-Abdomen-Pelvis | 1.5 mm / 1.5 mm | Standard | Standard | Cartografiere acces femural vascular |
