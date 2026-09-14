---
author: Departamentul de Radiologie și Imagistică Medicală
category: msk
clinical_indications:
- Lombalgie inflamatorie cronică la adult tânăr (< 45 ani) conform criteriilor ASAS
- Suspiciune de spondiloartrită axială / Spondilită anchilozantă în stadiu pre-radiografic
- Evaluarea activității inflamatorii (edem osos subcondral activ) înaintea inițierii
  terapiei biologice
- 'Diagnostic diferențial: osteitis condensans ilii, infecție (sacroiliită septică),
  fracturi de insuficiență'
coils_hardware:
  coil: Antenă Phased-Array Body / Pelvis 16-32 canale combinată cu antena Spine din
    masă
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, centrare pe linia medio-sagitală la 3 cm sub spinele
    iliace antero-superioare.
contraindications:
- Contraindicații generale RM.
contrast:
  agent: Nativ este suficient în 90% din cazuri conform ghidului ASAS/ESR; contrast
    IV rezervat pentru suspiciuni de sacroiliită septică (abcese pelvine).
  dose: Fără contrast de rutină
  flow_rate: Nu este cazul
  notes: Edemul osos activ subcondral se evaluează cu maximă sensibilitate pe secvența
    STIR.
  timing: Nu este cazul
iris_reference:
  chapter: Reumatologie - Spondilartropatii Seronegative
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: 'Criteriul ASAS pozitiv: prezența edemului osos subcondral (hipersemnal STIR)
  pe cel puțin două secțiuni consecutive sau în cel puțin două localizări pe aceeași
  secțiune.'
patient_prep: Chestionar RM; decubit dorsal, membre inferioare în extensie lejeră,
  bandă de compresie elastică pe abdomen inferior pentru reducerea artefactelor respiratorii.
quality_criteria:
- Angulare obligatorie a planului coronal oblic pe fața anterioară a corpului sacrat
  S1-S3
- Supresie de grăsime omogenă pe ambele aripi iliace și masiv sacrat
- Rezoluție suficientă pentru decelarea eroziunilor subcondrale milimetrice
safety_considerations:
- SAR moderat, examinare bine tolerată
sequences:
- fat_sat: STIR
  fov_matrix: FOV 200 - 220 mm / 320x256
  name: Coronal Oblic STIR / TIRM
  notes: Secvența definitorie pentru sacroiliită activă conform criteriilor ASAS
  plane: Coronal oblic paralel cu axul lung al sacrului (S1-S3)
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 4500 ms / TE 45 ms / TI 160 ms
- fat_sat: Nu
  fov_matrix: FOV 200 - 220 mm / 384x256
  name: Coronal Oblic T1 TSE
  notes: 'Modificări structurale cronice: metaplazie grasă subcondrală, eroziuni,
    punți osoase, anchiloză'
  plane: Coronal oblic paralel cu sacrul
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 550 ms / TE 10 ms
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 200 mm / 320x256
  name: Axial Oblic T2 FatSat
  notes: Confirmare edem versant iliac vs. sacrat, capsulită și entezită
  plane: Axial oblic perpendicular pe sacru
  slice_gap: 3.5 mm / gap 0.4 mm
  tr_te: TR 3500 ms / TE 65 ms
- fat_sat: Nu
  fov_matrix: FOV 380 mm / 384x256
  name: Coronal T1 TSE Bazin Întreg
  notes: Evaluare globală articulații coxo-femurale (excludere necroză cap femural)
  plane: Coronal clasic
  slice_gap: 4.0 mm / gap 0.5 mm
  tr_te: TR 550 ms / TE 12 ms
slug: irm-bazin-si-articulatii-sacroiliace
title: IRM Bazin & Articulații Sacroiliace (Protocol Spondilartrită axSpA)
---
# IRM Bazin & Articulații Sacroiliace (Protocol Spondilartrită axSpA)

<div class="irm-meta-bar">
  <span class="irm-modality-badge">🧲 Imagistică prin Rezonanță Magnetică (IRM)</span>
  <span><strong>Actualizat:</strong> 2026-09-13</span>
  <span><strong>Autor:</strong> Departamentul de Radiologie și Imagistică Medicală</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații RM__

    ---

    === "Indicații Clinice"

        - Lombalgie inflamatorie cronică la adult tânăr (< 45 ani) conform criteriilor ASAS
        - Suspiciune de spondiloartrită axială / Spondilită anchilozantă în stadiu pre-radiografic
        - Evaluarea activității inflamatorii (edem osos subcondral activ) înaintea inițierii terapiei biologice
        - Diagnostic diferențial: osteitis condensans ilii, infecție (sacroiliită septică), fracturi de insuficiență

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Reumatologie - Spondilartropatii Seronegative*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Chestionar RM; decubit dorsal, membre inferioare în extensie lejeră, bandă de compresie elastică pe abdomen inferior pentru reducerea artefactelor respiratorii.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Phased-Array Body / Pelvis 16-32 canale combinată cu antena Spine din masă
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe linia medio-sagitală la 3 cm sub spinele iliace antero-superioare.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ este suficient în 90% din cazuri conform ghidului ASAS/ESR; contrast IV rezervat pentru suspiciuni de sacroiliită septică (abcese pelvine).
    - **Doză Recomandată:** Fără contrast de rutină
    - **Rată de Injectare (Debit):** Nu este cazul
    - **Temporizare & Faze Dinamice:** Nu este cazul
    - **Filtrare Renală & Precauții:** Edemul osos activ subcondral se evaluează cu maximă sensibilitate pe secvența STIR.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal Oblic STIR / TIRM** | Coronal oblic paralel cu axul lung al sacrului (S1-S3) | TR 4500 ms / TE 45 ms / TI 160 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 - 220 mm / 320x256 | STIR | Secvența definitorie pentru sacroiliită activă conform criteriilor ASAS |
    | **Coronal Oblic T1 TSE** | Coronal oblic paralel cu sacrul | TR 550 ms / TE 10 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 - 220 mm / 384x256 | Nu | Modificări structurale cronice: metaplazie grasă subcondrală, eroziuni, punți osoase, anchiloză |
    | **Axial Oblic T2 FatSat** | Axial oblic perpendicular pe sacru | TR 3500 ms / TE 65 ms | 3.5 mm / gap 0.4 mm | FOV 200 mm / 320x256 | FatSat / SPAIR | Confirmare edem versant iliac vs. sacrat, capsulită și entezită |
    | **Coronal T1 TSE Bazin Întreg** | Coronal clasic | TR 550 ms / TE 12 ms | 4.0 mm / gap 0.5 mm | FOV 380 mm / 384x256 | Nu | Evaluare globală articulații coxo-femurale (excludere necroză cap femural) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Angulare obligatorie a planului coronal oblic pe fața anterioară a corpului sacrat S1-S3
    - Supresie de grăsime omogenă pe ambele aripi iliace și masiv sacrat
    - Rezoluție suficientă pentru decelarea eroziunilor subcondrale milimetrice

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR moderat, examinare bine tolerată

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Criteriul ASAS pozitiv: prezența edemului osos subcondral (hipersemnal STIR) pe cel puțin două secțiuni consecutive sau în cel puțin două localizări pe aceeași secțiune.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
