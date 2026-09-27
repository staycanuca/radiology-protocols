---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen-pelvis
clinical_indications:
- Suspiciune de supraîncărcare hepatică cu fier (hemocromatoză ereditară, hemosideroză
  secundară după transfuzii repetate)
- Monitorizarea terapiei de chelare a fierului la pacienți cu talasemie majoră sau
  sindroame mielodisplazice
- Cuantificarea precisă a steatozei hepatice (NAFLD / NASH, steatohepatită metabolică)
- Evaluare pre-donare hepatică sau pre-chimioterapie hepatotoxică
coils_hardware:
  coil: Antenă Body multicanal (16–32 canale) centrată pe etajul abdominal superior
  field_strength: 1.5 Tesla (etalonul de aur pentru cuantificarea fierului) sau 3.0
    Tesla
  positioning: Decubit dorsal, brațele pe lângă cap
contraindications:
- Implanturi feromagnetice
contrast:
  agent: Fără contrast (determinare biometrică pur nativă)
  dose: N/A
  flow_rate: N/A
  notes: Substanțele de contrast pe bază de Gadoliniu alterează măsurătorile de T2*
    și sunt strict contraindicate înaintea acestei achiziții.
  timing: N/A
iris_reference:
  chapter: Aparat digestiv & Abdomen
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol de referință OHSU pentru cuantificarea non-invazivă absolută a fierului
  și grăsimii hepatice, înlocuind biopsia hepatică.
patient_prep: Repaus alimentar 4 ore înainte de examinare. Fără contrast.
quality_criteria:
- Achiziție în apnee expiratorie stabilă pentru evitarea artefactelor de mișcare pe
  secvența multi-echo
- Amplasarea a minim 3 regiuni de interes (ROI) de 1-2 cm² în parenchimul hepatic
  omogen, evitând vasele mari și căile biliare
- Coeficient de corelație R² > 0.95 pentru curba de atenuare exponențială T2*
safety_considerations:
- Screening standard RM conform politicii OHSU
- Pacienții cu hemocromatoză pot avea asociată cardiomiopatie — se recomandă monitorizare
  puls
sequences:
- fat_sat: Nu
  fov_matrix: FOV 380 mm / Matrice 192×128
  name: Multi-Echo GRE T2* / R2* Hepatic
  notes: Calcul direct al R2* (R2* = 1000 / T2* în Hz) corelat matematic cu concentrația
    de fier hepatic (LIC în mg Fe/g țesut uscat)
  plane: Axial
  slice_gap: 8.0 - 10.0 mm (3 secțiuni reprezentative prin ficat)
  tr_te: TR 150-200 ms / 6 până la 12 ecouri (TE 1.1 - 18 ms)
- fat_sat: Dixon (Fat, Water, In-phase, Out-of-phase, Fat-fraction map)
  fov_matrix: FOV 380 mm / Matrice 192×192
  name: 3D Dixon Multi-Echo PDFF (Proton Density Fat Fraction)
  notes: 'Harta procentuală a fracției de grăsime (PDFF %: normal < 5%, steatoză ușoară
    5-15%, moderată 15-25%, severă > 25%)'
  plane: Axial
  slice_gap: 4.0 mm izotrop
  tr_te: TR 6-9 ms / 6 ecouri / Flip angle 3-4° (elimină T1 bias)
- fat_sat: Nu
  fov_matrix: FOV 350 mm / Matrice 256×256
  name: Axial T2 SSFSE / HASTE
  notes: Evaluare anatomică hepatică și splenomicroscopie
  plane: Axial
  slice_gap: 5.0 mm / gap 1.0 mm
  tr_te: TR 1200 ms / TE 80 ms
- fat_sat: Nu
  fov_matrix: FOV 380 mm / Matrice 256×256
  name: Coronal T2 SSFSE / HASTE
  notes: Raport topografic ficat-splină-pancreas (apreciere depuneri de fier splenice
    și pancreatice)
  plane: Coronal
  slice_gap: 5.0 mm / gap 1.0 mm
  tr_te: TR 1200 ms / TE 80 ms
title: RM Cuantificare Fier Fe & Steatoză Hepatică PDFF (Protocol OHSU)
---
# RM Cuantificare Fier Fe & Steatoză Hepatică PDFF (Protocol OHSU)

<div class="irm-meta-bar">
  <span class="irm-modality-badge">🧲 Imagistică prin Rezonanță Magnetică (IRM)</span>
  <span><strong>Actualizat:</strong> 2026-09-20</span>
  <span><strong>Autor:</strong> OHSU Diagnostic Radiology / Departamentul de Radiologie</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații RM__

    ---

    === "Indicații Clinice"

        - Suspiciune de supraîncărcare hepatică cu fier (hemocromatoză ereditară, hemosideroză secundară după transfuzii repetate)
        - Monitorizarea terapiei de chelare a fierului la pacienți cu talasemie majoră sau sindroame mielodisplazice
        - Cuantificarea precisă a steatozei hepatice (NAFLD / NASH, steatohepatită metabolică)
        - Evaluare pre-donare hepatică sau pre-chimioterapie hepatotoxică

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat digestiv & Abdomen*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Repaus alimentar 4 ore înainte de examinare. Fără contrast.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla (etalonul de aur pentru cuantificarea fierului) sau 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă Body multicanal (16–32 canale) centrată pe etajul abdominal superior
    - **Poziție Pacient & Centrare:** Decubit dorsal, brațele pe lângă cap

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Fără contrast (determinare biometrică pur nativă)
    - **Doză Recomandată:** N/A
    - **Rată de Injectare (Debit):** N/A
    - **Temporizare & Faze Dinamice:** N/A
    - **Filtrare Renală & Precauții:** Substanțele de contrast pe bază de Gadoliniu alterează măsurătorile de T2* și sunt strict contraindicate înaintea acestei achiziții.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Multi-Echo GRE T2* / R2* Hepatic** | Axial | TR 150-200 ms / 6 până la 12 ecouri (TE 1.1 - 18 ms) | 8.0 - 10.0 mm (3 secțiuni reprezentative prin ficat) | FOV 380 mm / Matrice 192×128 | Nu | Calcul direct al R2* (R2* = 1000 / T2* în Hz) corelat matematic cu concentrația de fier hepatic (LIC în mg Fe/g țesut uscat) |
    | **3D Dixon Multi-Echo PDFF (Proton Density Fat Fraction)** | Axial | TR 6-9 ms / 6 ecouri / Flip angle 3-4° (elimină T1 bias) | 4.0 mm izotrop | FOV 380 mm / Matrice 192×192 | Dixon (Fat, Water, In-phase, Out-of-phase, Fat-fraction map) | Harta procentuală a fracției de grăsime (PDFF %: normal < 5%, steatoză ușoară 5-15%, moderată 15-25%, severă > 25%) |
    | **Axial T2 SSFSE / HASTE** | Axial | TR 1200 ms / TE 80 ms | 5.0 mm / gap 1.0 mm | FOV 350 mm / Matrice 256×256 | Nu | Evaluare anatomică hepatică și splenomicroscopie |
    | **Coronal T2 SSFSE / HASTE** | Coronal | TR 1200 ms / TE 80 ms | 5.0 mm / gap 1.0 mm | FOV 380 mm / Matrice 256×256 | Nu | Raport topografic ficat-splină-pancreas (apreciere depuneri de fier splenice și pancreatice) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Achiziție în apnee expiratorie stabilă pentru evitarea artefactelor de mișcare pe secvența multi-echo
    - Amplasarea a minim 3 regiuni de interes (ROI) de 1-2 cm² în parenchimul hepatic omogen, evitând vasele mari și căile biliare
    - Coeficient de corelație R² > 0.95 pentru curba de atenuare exponențială T2*

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening standard RM conform politicii OHSU
    - Pacienții cu hemocromatoză pot avea asociată cardiomiopatie — se recomandă monitorizare puls

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol de referință OHSU pentru cuantificarea non-invazivă absolută a fierului și grăsimii hepatice, înlocuind biopsia hepatică.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
