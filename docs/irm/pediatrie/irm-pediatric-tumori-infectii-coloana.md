---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Suspiciune de diseminare tumorală secundară pe cale LCR ('drop metastasis' din meduloblastom,
  ependimom)
- Tumori primare intramedulare (astrocitom, ependimom) sau extramedulare (schwanom,
  neuroblastom)
- Spondilodiscită infantilă sau juvenilă
- Suspiciune de abces epidural spinal sau flegmon paravertebral
- Mielită transversă sau afecțiuni demielinizante ale măduvei
coils_hardware:
  coil: Antenă spinală phased-array dedicată (Spine matrix)
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, coloana aliniată pe linia mediană
contraindications:
- Dispozitive medicale implantabile nesigure RM
- Insuficiență renală acută severă
contrast:
  agent: Chelat de Gadoliniu macrociclic
  dose: 0.1 mmol/kg corp
  flow_rate: 1.0 - 1.5 ml/s urmat de ser fiziologic
  notes: Esențial pentru diferențierea flegmon vs. abces lichefiat și evidențierea
    'drop metastases'.
  timing: Achiziție secvențe T1 post-contrast la 2-3 minute
iris_reference:
  chapter: Pediatrie - Coloană vertebrală
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol standardizat WFPI pentru coloana vertebrală pediatrică (tumori și
  infecții), cu durată optimizată la 20 minute.
patient_prep: Copilul așezat confortabil în decubit dorsal; linie venoasă verificată
  prealabil.
quality_criteria:
- 'Timp total de scanare: aproximativ 20 minute'
- Acoperire completă a segmentului de coloană vizat (cervico-toracal sau toraco-lombar)
- Supresie de grăsime uniformă pe secvențele sagitale STIR și T1 FS
safety_considerations:
- Imobilizare confortabilă pentru prevenirea durerii la copiii cu patologie spinală
  acută
- Respectare limite SAR
sequences:
- fat_sat: Nu
  fov_matrix: FOV 250-300 mm / 320x224
  name: Sagital T1WI TSE
  notes: Anatomie corpi vertebrali, înlocuire grăsime medulară în infecții/infiltrare
    (3 min)
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 450-600 ms / TE 8-12 ms
- fat_sat: FatSat / STIR
  fov_matrix: FOV 250-300 mm / 320x224
  name: Sagital T2WI FS / STIR
  notes: Edem osos vertebral, afectare discală, semnal lichidian epidural (2:30 min)
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 3500 ms / TE 80-100 ms / TI 150 ms
- fat_sat: FatSat
  fov_matrix: FOV 250-300 mm / 128x128
  name: Sagital DWI (b=0, b=800)
  notes: Restricție de difuzie în abcese epidurale și metastaze celulare (1 min)
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 3000 ms / TE 65 ms
- fat_sat: FatSat
  fov_matrix: FOV 250-300 mm / 320x224
  name: Sagital T1WI FS Post-Contrast
  notes: Evaluare captare măduvă osoasă, afectare meningiană și epidurală (5 min)
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 500-650 ms / TE 10 ms
- fat_sat: Nu
  fov_matrix: FOV 180-200 mm / 256x256
  name: Axial T2WI TSE
  notes: Compresie medulară, foramene de conjugare, extensie paravertebrală (4 min)
  plane: Axial (centrat pe leziune)
  slice_gap: 3.5 mm / gap 0.3 mm
  tr_te: TR 3500-4500 ms / TE 100 ms
- fat_sat: FatSat
  fov_matrix: FOV 180-200 mm / 256x256
  name: Axial T1WI FS Post-Contrast
  notes: Evaluare măduvă spinării, spații radiculare și delimitare capsulă abces (3:30
    min)
  plane: Axial (centrat pe leziune)
  slice_gap: 3.5 mm / gap 0.3 mm
  tr_te: TR 500-600 ms / TE 10 ms
slug: irm-pediatric-tumori-infectii-coloana
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
title: RM Pediatric — Protocol Tumori & Infecții Coloană Vertebrală (Spine Tumor &
  Infection)
---
# RM Pediatric — Protocol Tumori & Infecții Coloană Vertebrală (Spine Tumor & Infection)

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

        - Suspiciune de diseminare tumorală secundară pe cale LCR ('drop metastasis' din meduloblastom, ependimom)
        - Tumori primare intramedulare (astrocitom, ependimom) sau extramedulare (schwanom, neuroblastom)
        - Spondilodiscită infantilă sau juvenilă
        - Suspiciune de abces epidural spinal sau flegmon paravertebral
        - Mielită transversă sau afecțiuni demielinizante ale măduvei

    === "Contraindicații & Screening Metalic"

        - Dispozitive medicale implantabile nesigure RM
        - Insuficiență renală acută severă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Copilul așezat confortabil în decubit dorsal; linie venoasă verificată prealabil.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă spinală phased-array dedicată (Spine matrix)
    - **Poziție Pacient & Centrare:** Decubit dorsal, coloana aliniată pe linia mediană

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic
    - **Doză Recomandată:** 0.1 mmol/kg corp
    - **Rată de Injectare (Debit):** 1.0 - 1.5 ml/s urmat de ser fiziologic
    - **Temporizare & Faze Dinamice:** Achiziție secvențe T1 post-contrast la 2-3 minute
    - **Filtrare Renală & Precauții:** Esențial pentru diferențierea flegmon vs. abces lichefiat și evidențierea 'drop metastases'.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T1WI TSE** | Sagital | TR 450-600 ms / TE 8-12 ms | 3.0 mm / gap 0.3 mm | FOV 250-300 mm / 320x224 | Nu | Anatomie corpi vertebrali, înlocuire grăsime medulară în infecții/infiltrare (3 min) |
    | **Sagital T2WI FS / STIR** | Sagital | TR 3500 ms / TE 80-100 ms / TI 150 ms | 3.0 mm / gap 0.3 mm | FOV 250-300 mm / 320x224 | FatSat / STIR | Edem osos vertebral, afectare discală, semnal lichidian epidural (2:30 min) |
    | **Sagital DWI (b=0, b=800)** | Sagital | TR 3000 ms / TE 65 ms | 3.0 mm / gap 0.3 mm | FOV 250-300 mm / 128x128 | FatSat | Restricție de difuzie în abcese epidurale și metastaze celulare (1 min) |
    | **Sagital T1WI FS Post-Contrast** | Sagital | TR 500-650 ms / TE 10 ms | 3.0 mm / gap 0.3 mm | FOV 250-300 mm / 320x224 | FatSat | Evaluare captare măduvă osoasă, afectare meningiană și epidurală (5 min) |
    | **Axial T2WI TSE** | Axial (centrat pe leziune) | TR 3500-4500 ms / TE 100 ms | 3.5 mm / gap 0.3 mm | FOV 180-200 mm / 256x256 | Nu | Compresie medulară, foramene de conjugare, extensie paravertebrală (4 min) |
    | **Axial T1WI FS Post-Contrast** | Axial (centrat pe leziune) | TR 500-600 ms / TE 10 ms | 3.5 mm / gap 0.3 mm | FOV 180-200 mm / 256x256 | FatSat | Evaluare măduvă spinării, spații radiculare și delimitare capsulă abces (3:30 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de scanare: aproximativ 20 minute
    - Acoperire completă a segmentului de coloană vizat (cervico-toracal sau toraco-lombar)
    - Supresie de grăsime uniformă pe secvențele sagitale STIR și T1 FS

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Imobilizare confortabilă pentru prevenirea durerii la copiii cu patologie spinală acută
    - Respectare limite SAR

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol standardizat WFPI pentru coloana vertebrală pediatrică (tumori și infecții), cu durată optimizată la 20 minute.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
