---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Suspiciune de osteomielită acută hematogenă la copil (febră, durere osoasă localizată,
  refuzul sprijinului)
- Artrită septică (evaluare revărsat articular și afectare epifizară)
- 'Miozită, flegmon sau abces de părți moi profunde (ex: mușchiul psoas, obturator
  intern)'
- Suspiciune de abces subperiostal care necesită drenaj chirurgical de urgență
coils_hardware:
  coil: Antenă dedicată extremității (genunchi, gleznă, umăr) sau antenă flexibilă
    de suprafață
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Poziționare confortabilă a segmentului anatomic de interes în izocentru
contraindications:
- Implanturi metalice feromagnetice nesigure RM
- Alergie la substanța de contrast pe bază de Gadoliniu
contrast:
  agent: Chelat de Gadoliniu macrociclic
  dose: 0.1 mmol/kg corp
  flow_rate: 1.0 - 1.5 ml/s urmat de 15 ml ser fiziologic
  notes: Contrastul este esențial pentru diferențierea flegmonului ne-necrozat de
    abcesul lichefiat cu lizereu periferic captant.
  timing: Achiziție secvențe T1 FS post-contrast imediat și la 2-3 minute
iris_reference:
  chapter: Pediatrie - Aparat locomotor & Articulații
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol standardizat WFPI pentru diagnosticul precoce și precis al infecțiilor
  musculoscheletale la copil, prevenind sechelele de creștere osoasă.
patient_prep: Imobilizare atentă a membrului afectat; atelare confortabilă pentru
  a reduce durerea provocată de mișcare.
quality_criteria:
- 'Timp total de scanare: 10–15 min nativ; 20–25 min cu contrast'
- Supresie de grăsime uniformă și eficientă pe secvențele STIR și T1 FS
- Includerea completă a focarului osos și a compartimentelor musculare adiacente
safety_considerations:
- Poziționare blândă pentru a nu agrava durerea membrului inflamat
- Doza de contrast strict adaptată greutății corporale (0.1 mmol/kg)
sequences:
- fat_sat: Nu
  fov_matrix: FOV 180-240 mm / 320x224
  name: Coronal T1WI TSE
  notes: Înlocuire grăsime medulară hematopoietică/osoasă (hiposemnal T1 patologic)
    (3 min)
  plane: Coronal
  slice_gap: 3.0-4.0 mm / gap 0.4 mm
  tr_te: TR 500-600 ms / TE 10 ms
- fat_sat: STIR
  fov_matrix: FOV 180-240 mm / 256x256
  name: Coronal STIR
  notes: Sensibilitate maximă pentru edem osos inflamator, revărsat articular și edem
    muscular (3 min)
  plane: Coronal
  slice_gap: 3.0-4.0 mm / gap 0.4 mm
  tr_te: TR 3500-4500 ms / TE 45-60 ms / TI 150 ms
- fat_sat: FatSat
  fov_matrix: FOV 160-220 mm / 256x256
  name: Axial T2WI FS
  notes: Delimitare abcese subperiostale, traiecte fistuloase, colecții intramusculare
    (4–6 min)
  plane: Axial
  slice_gap: 3.5-4.0 mm / gap 0.4 mm
  tr_te: TR 3500-4500 ms / TE 75-90 ms
- fat_sat: Nu
  fov_matrix: FOV 180-240 mm / 320x224
  name: Sagital T1WI TSE
  notes: Confirmare anatomică în plan ortogonal a extensiei lezionale (3 min)
  plane: Sagital
  slice_gap: 3.0-4.0 mm / gap 0.4 mm
  tr_te: TR 500-600 ms / TE 10 ms
- fat_sat: FatSat
  fov_matrix: FOV 180-240 mm / 320x224
  name: Sagital T1WI FS Post-Contrast
  notes: Captare măduvă osoasă, periost și sinovială (3 min)
  plane: Sagital
  slice_gap: 3.0-4.0 mm / gap 0.4 mm
  tr_te: TR 550-650 ms / TE 10 ms
- fat_sat: FatSat
  fov_matrix: FOV 180-240 mm / 320x224
  name: Coronal T1WI FS Post-Contrast
  notes: Evaluare colecții purulente (centru necrotic non-captant cu lizereu periferic)
    (3 min)
  plane: Coronal
  slice_gap: 3.0-4.0 mm / gap 0.4 mm
  tr_te: TR 550-650 ms / TE 10 ms
slug: irm-pediatric-osteomielita-infectii-msk
sources:
- institution: WFPI
  kind: Standard internațional de imagistică pediatrică
  title: WFPI Pediatric MRI Protocols — World Federation of Pediatric Imaging
  url: https://wfpiweb.org/Resources/Modalities/MRIProtocols.aspx
- institution: WFPI / Springer
  kind: Ghid clinic publicat
  title: International standardization of pediatric MRI protocols (Ferraciolli et
    al., Pediatr Radiol 2024)
  url: https://doi.org/10.1007/s00247-024-06041-0
- institution: Ministerul Sănătății România
  kind: Ghid național de referință
  title: Ghidul Național de Utilizare a Tehnologiilor Imagistice (Ordinul MS 1342/2012
    - Ghid IRIS)
  url: https://radiologie-pediatrica.ro/iris/
title: RM Pediatric — Protocol Osteomielită & Infecții Musculoscheletale (Osteomyelitis
  / MSK)
---
# RM Pediatric — Protocol Osteomielită & Infecții Musculoscheletale (Osteomyelitis / MSK)

<div class="irm-meta-bar">
  <span class="irm-modality-badge">🧲 Imagistică prin Rezonanță Magnetică (IRM)</span>
  <span><strong>Actualizat:</strong> 2026-09-20</span>
  <span><strong>Autor:</strong> World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații RM__

    ---

    === "Indicații Clinice"

        - Suspiciune de osteomielită acută hematogenă la copil (febră, durere osoasă localizată, refuzul sprijinului)
        - Artrită septică (evaluare revărsat articular și afectare epifizară)
        - Miozită, flegmon sau abces de părți moi profunde (ex: mușchiul psoas, obturator intern)
        - Suspiciune de abces subperiostal care necesită drenaj chirurgical de urgență

    === "Contraindicații & Screening Metalic"

        - Implanturi metalice feromagnetice nesigure RM
        - Alergie la substanța de contrast pe bază de Gadoliniu

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Aparat locomotor & Articulații*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Imobilizare atentă a membrului afectat; atelare confortabilă pentru a reduce durerea provocată de mișcare.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată extremității (genunchi, gleznă, umăr) sau antenă flexibilă de suprafață
    - **Poziție Pacient & Centrare:** Poziționare confortabilă a segmentului anatomic de interes în izocentru

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic
    - **Doză Recomandată:** 0.1 mmol/kg corp
    - **Rată de Injectare (Debit):** 1.0 - 1.5 ml/s urmat de 15 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Achiziție secvențe T1 FS post-contrast imediat și la 2-3 minute
    - **Filtrare Renală & Precauții:** Contrastul este esențial pentru diferențierea flegmonului ne-necrozat de abcesul lichefiat cu lizereu periferic captant.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T1WI TSE** | Coronal | TR 500-600 ms / TE 10 ms | 3.0-4.0 mm / gap 0.4 mm | FOV 180-240 mm / 320x224 | Nu | Înlocuire grăsime medulară hematopoietică/osoasă (hiposemnal T1 patologic) (3 min) |
    | **Coronal STIR** | Coronal | TR 3500-4500 ms / TE 45-60 ms / TI 150 ms | 3.0-4.0 mm / gap 0.4 mm | FOV 180-240 mm / 256x256 | STIR | Sensibilitate maximă pentru edem osos inflamator, revărsat articular și edem muscular (3 min) |
    | **Axial T2WI FS** | Axial | TR 3500-4500 ms / TE 75-90 ms | 3.5-4.0 mm / gap 0.4 mm | FOV 160-220 mm / 256x256 | FatSat | Delimitare abcese subperiostale, traiecte fistuloase, colecții intramusculare (4–6 min) |
    | **Sagital T1WI TSE** | Sagital | TR 500-600 ms / TE 10 ms | 3.0-4.0 mm / gap 0.4 mm | FOV 180-240 mm / 320x224 | Nu | Confirmare anatomică în plan ortogonal a extensiei lezionale (3 min) |
    | **Sagital T1WI FS Post-Contrast** | Sagital | TR 550-650 ms / TE 10 ms | 3.0-4.0 mm / gap 0.4 mm | FOV 180-240 mm / 320x224 | FatSat | Captare măduvă osoasă, periost și sinovială (3 min) |
    | **Coronal T1WI FS Post-Contrast** | Coronal | TR 550-650 ms / TE 10 ms | 3.0-4.0 mm / gap 0.4 mm | FOV 180-240 mm / 320x224 | FatSat | Evaluare colecții purulente (centru necrotic non-captant cu lizereu periferic) (3 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de scanare: 10–15 min nativ; 20–25 min cu contrast
    - Supresie de grăsime uniformă și eficientă pe secvențele STIR și T1 FS
    - Includerea completă a focarului osos și a compartimentelor musculare adiacente

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Poziționare blândă pentru a nu agrava durerea membrului inflamat
    - Doza de contrast strict adaptată greutății corporale (0.1 mmol/kg)

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol standardizat WFPI pentru diagnosticul precoce și precis al infecțiilor musculoscheletale la copil, prevenind sechelele de creștere osoasă.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
