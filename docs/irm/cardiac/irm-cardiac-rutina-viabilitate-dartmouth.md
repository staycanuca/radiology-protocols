---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: cardiac
clinical_indications:
- Evaluarea viabilității miocardice și a necrozei/cicatricii fibroase post-infarct
  miocardic
- Miocardită acută sau subacută (criteriile Lake Louise actualizate)
- Cardiomiopatii neischemice (dilatativă, hipertrofică, amiloidoză, sarcoidoză cardiacă)
- Cuantificarea precisă a volumelor, masei și fracției de ejecție a ventriculului
  stâng și drept (FEVS, FEVD)
coils_hardware:
  coil: Antenă Cardiac Phased Array dedicată 16–32 canale cu gating ECG optic/vectorial
  field_strength: Preferabil 1.5 Tesla (recomandat de DHMC pentru minimizarea artefactelor
    de flux) sau 3.0 Tesla cu shim dedicat
  positioning: Decubit dorsal, capul înainte, electrozi ECG pe hemitoracele anterior
    stâng
contraindications:
- Stimulatoare cardiace / defibrilatoare non-compatibile RM sau electrozi abandonați
- Aritmii severe necontrolate (fibrilație atrială rapidă cu ritm complet neregulat
  degradează CINE-ul)
- Imposibilitatea cooperării pentru apnee scurtă de 8–10 secunde
contrast:
  agent: Gadoliniu macrociclic (Gadovist / Dotarem)
  dose: 0.15 - 0.20 mmol/kg (doză împărțită sau bolus unic pentru LGE)
  flow_rate: 2.0 - 3.0 mL/s + 30 mL flush salin
  timing: Examinare LGE (Late Gadolinium Enhancement) efectuată la 10–15 minute post-injectare
iris_reference:
  chapter: Cardiologie & Angiografie
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
modality: irm
notes: 'Ghidul DHMC recomandă 1.5T pentru minimizarea artefactelor de susceptibilitate
  pe secvențele bSSFP. Viabilitatea este definită prin extensia transmurală LGE: transmuralitate
  < 50% indică șanse mari de recuperare a funcției contractile post-revascularizare.'
patient_prep: Evitarea cafelei și a stimulentelor cu 12 ore înainte de procedură.
  Aplicare riguroasă a electrozilor ECG pentru sincronizare cardiacă de calitate (semnal
  undă R înalt).
quality_criteria:
- Nul miocardic impecabil pe LGE (miocardul sănătos apare complet negru, evidențiind
  contrastul leziunii)
- Unde CINE fluide fără artefacte de aritmie
- Acoperire completă a ventriculului stâng de la baza inelului mitral până la apexul
  veritabil
safety_considerations:
- Monitorizare puls și saturație O2 continuă pe monitorul compatibil RM
- Verificare eGFR > 30 mL/min
sequences:
- fat_sat: Nu
  fov_matrix: FOV 400 mm
  name: Localizatoare Cardiace 3-Plane (Scout)
  notes: Identificarea axului lung al cordului
  plane: Axial, Coronal, Sagital
  slice_gap: 8.0 mm
  tr_te: Ultra-rapid bSSFP
- fat_sat: Nu
  fov_matrix: FOV 340 mm / Matrice 256×208
  name: CINE bSSFP 2-Camere (2CH - Ax Lung Vertical)
  notes: 25-30 faze/ciclu cardiac în apnee; evaluare perete anterior și inferior VS
  plane: 2-Camere (plan prin apex și centrul valvei mitrale)
  slice_gap: 6.0 - 8.0 mm
  tr_te: TR 2.8 ms / TE 1.2 ms
- fat_sat: Nu
  fov_matrix: FOV 340 mm / Matrice 256×208
  name: CINE bSSFP 4-Camere (4CH - Ax Lung Orizontal)
  notes: Evaluare ventricul stâng, ventricul drept, atrii și valve atrio-ventriculare
  plane: 4-Camere (plan prin apex, septul interventricular și peretele lateral)
  slice_gap: 6.0 - 8.0 mm
  tr_te: TR 2.8 ms / TE 1.2 ms
- fat_sat: Nu
  fov_matrix: FOV 340 mm / Matrice 256×208
  name: CINE bSSFP Ax Scurt Stivă Completă (SAX Stack)
  notes: 10-12 secțiuni contigue ce acoperă întreg ventriculul; standardul de aur
    pentru FEVS, VTD, VTS și masă miocardică
  plane: Short Axis (perpendicular pe sept de la inelul mitral la apex)
  slice_gap: 8.0 mm contiguu (fără gap)
  tr_te: TR 2.8 ms / TE 1.2 ms
- fat_sat: Da (Inversion Recovery)
  fov_matrix: FOV 340 mm
  name: T2 TIRM / Black Blood Axial & SAX (Edem Miocardic)
  notes: Raport semnal miocard/mușchi scheletic > 1.9 indică edem miocardic acut (miocardită
    sau infarct acut)
  plane: Short Axis & 4CH
  slice_gap: 8.0 mm
  tr_te: TR 2 cicluri R-R / TE 60-70 ms
- fat_sat: Nu
  fov_matrix: FOV 340 mm
  name: TI Scout (Look-Locker CINE)
  notes: Identificarea timpului de inversie optim (TI de nul miocardic, uzual 280–340
    ms) înainte de LGE
  plane: Short Axis medioventricular
  slice_gap: 8.0 mm
  tr_te: Single shot inversion recovery
- fat_sat: Da
  fov_matrix: FOV 340 mm / Matrice 256×208
  name: LGE / PSIR 2D & 3D (Late Gadolinium Enhancement)
  notes: 'Faza tardivă (10-15 min post contrast): hipersemnal alb transmural/subendocardic
    în necroză ischemică vs. subepicardic/mediomiocardic în miocardită/cardiomiopatii
    neischemice'
  plane: Short Axis (stivă completă) + 2CH + 4CH
  slice_gap: 8.0 mm
  tr_te: TR 700 ms / TE 1.5 ms / TI optimizat din Look-Locker
title: IRM Cardiac Funcție & Viabilitate LGE (Protocol DHMC)
---
# IRM Cardiac Funcție & Viabilitate LGE (Protocol DHMC)

<div class="irm-meta-bar">
  <span class="irm-modality-badge">🧲 Imagistică prin Rezonanță Magnetică (IRM)</span>
  <span><strong>Actualizat:</strong> 2026-09-26</span>
  <span><strong>Autor:</strong> Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații RM__

    ---

    === "Indicații Clinice"

        - Evaluarea viabilității miocardice și a necrozei/cicatricii fibroase post-infarct miocardic
        - Miocardită acută sau subacută (criteriile Lake Louise actualizate)
        - Cardiomiopatii neischemice (dilatativă, hipertrofică, amiloidoză, sarcoidoză cardiacă)
        - Cuantificarea precisă a volumelor, masei și fracției de ejecție a ventriculului stâng și drept (FEVS, FEVD)

    === "Contraindicații & Screening Metalic"

        - Stimulatoare cardiace / defibrilatoare non-compatibile RM sau electrozi abandonați
        - Aritmii severe necontrolate (fibrilație atrială rapidă cu ritm complet neregulat degradează CINE-ul)
        - Imposibilitatea cooperării pentru apnee scurtă de 8–10 secunde

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cardiologie & Angiografie*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Evitarea cafelei și a stimulentelor cu 12 ore înainte de procedură. Aplicare riguroasă a electrozilor ECG pentru sincronizare cardiacă de calitate (semnal undă R înalt).
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** Preferabil 1.5 Tesla (recomandat de DHMC pentru minimizarea artefactelor de flux) sau 3.0 Tesla cu shim dedicat
    - **Antenă de Recepție (Coil):** Antenă Cardiac Phased Array dedicată 16–32 canale cu gating ECG optic/vectorial
    - **Poziție Pacient & Centrare:** Decubit dorsal, capul înainte, electrozi ECG pe hemitoracele anterior stâng

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic (Gadovist / Dotarem)
    - **Doză Recomandată:** 0.15 - 0.20 mmol/kg (doză împărțită sau bolus unic pentru LGE)
    - **Rată de Injectare (Debit):** 2.0 - 3.0 mL/s + 30 mL flush salin
    - **Temporizare & Faze Dinamice:** Examinare LGE (Late Gadolinium Enhancement) efectuată la 10–15 minute post-injectare
    - **Filtrare Renală & Precauții:** Evaluare eGFR conform ghidurilor ESUR; risc redus de Fibroză Sistemică Nefrogenă (NSF) pentru agenții macrociclici.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Localizatoare Cardiace 3-Plane (Scout)** | Axial, Coronal, Sagital | Ultra-rapid bSSFP | 8.0 mm | FOV 400 mm | Nu | Identificarea axului lung al cordului |
    | **CINE bSSFP 2-Camere (2CH - Ax Lung Vertical)** | 2-Camere (plan prin apex și centrul valvei mitrale) | TR 2.8 ms / TE 1.2 ms | 6.0 - 8.0 mm | FOV 340 mm / Matrice 256×208 | Nu | 25-30 faze/ciclu cardiac în apnee; evaluare perete anterior și inferior VS |
    | **CINE bSSFP 4-Camere (4CH - Ax Lung Orizontal)** | 4-Camere (plan prin apex, septul interventricular și peretele lateral) | TR 2.8 ms / TE 1.2 ms | 6.0 - 8.0 mm | FOV 340 mm / Matrice 256×208 | Nu | Evaluare ventricul stâng, ventricul drept, atrii și valve atrio-ventriculare |
    | **CINE bSSFP Ax Scurt Stivă Completă (SAX Stack)** | Short Axis (perpendicular pe sept de la inelul mitral la apex) | TR 2.8 ms / TE 1.2 ms | 8.0 mm contiguu (fără gap) | FOV 340 mm / Matrice 256×208 | Nu | 10-12 secțiuni contigue ce acoperă întreg ventriculul; standardul de aur pentru FEVS, VTD, VTS și masă miocardică |
    | **T2 TIRM / Black Blood Axial & SAX (Edem Miocardic)** | Short Axis & 4CH | TR 2 cicluri R-R / TE 60-70 ms | 8.0 mm | FOV 340 mm | Da (Inversion Recovery) | Raport semnal miocard/mușchi scheletic > 1.9 indică edem miocardic acut (miocardită sau infarct acut) |
    | **TI Scout (Look-Locker CINE)** | Short Axis medioventricular | Single shot inversion recovery | 8.0 mm | FOV 340 mm | Nu | Identificarea timpului de inversie optim (TI de nul miocardic, uzual 280–340 ms) înainte de LGE |
    | **LGE / PSIR 2D & 3D (Late Gadolinium Enhancement)** | Short Axis (stivă completă) + 2CH + 4CH | TR 700 ms / TE 1.5 ms / TI optimizat din Look-Locker | 8.0 mm | FOV 340 mm / Matrice 256×208 | Da | Faza tardivă (10-15 min post contrast): hipersemnal alb transmural/subendocardic în necroză ischemică vs. subepicardic/mediomiocardic în miocardită/cardiomiopatii neischemice |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Nul miocardic impecabil pe LGE (miocardul sănătos apare complet negru, evidențiind contrastul leziunii)
    - Unde CINE fluide fără artefacte de aritmie
    - Acoperire completă a ventriculului stâng de la baza inelului mitral până la apexul veritabil

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Monitorizare puls și saturație O2 continuă pe monitorul compatibil RM
    - Verificare eGFR > 30 mL/min

</div>


!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Ghidul DHMC recomandă 1.5T pentru minimizarea artefactelor de susceptibilitate pe secvențele bSSFP. Viabilitatea este definită prin extensia transmurală LGE: transmuralitate < 50% indică șanse mari de recuperare a funcției contractile post-revascularizare.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
