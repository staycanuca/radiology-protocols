---
author: Departamentul de Radiologie și Imagistică Medicală
category: neuro
clinical_indications:
- Suspiciune de microadenom hipofizar secretant (prolactinom, boală Cushing, acromegalie)
- Macroadenom hipofizar (evaluare invazie sinus cavernos și compresie chiasmă optică)
- Diabet insipid central (evaluare neurohipofiză și tijă pituitară)
- Deficite hormonale hipofizare / panhipopituitarism
coils_hardware:
  coil: Antenă Head 32 sau 64 canale
  field_strength: 1.5T sau preferabil 3.0T (rezoluție spațială superioară pe câmp
    mic de 12-14 cm)
  positioning: Decubit dorsal, centrare pe nasion, plan de scanare strict perpendicular
    pe planul selar.
contraindications:
- Contraindicații generale RM; insuficiență renală severă dacă eGFR < 30 ml/min.
contrast:
  agent: Chelat de Gadoliniu macrociclic
  dose: 0.1 mmol/kg corp
  flow_rate: 2.0 - 2.5 ml/s urmat de flush de 20 ml ser fiziologic
  notes: Microadenoamele apar tipic ca arii hipocaptante tardiv-contrastate pe fondul
    captării precoce a parenchimului hipofizar normal.
  timing: Achiziție dinamică rapidă coronală T1 (la fiecare 15-20 secunde timp de
    2-3 minute)
iris_reference:
  chapter: Endocrinologie - Neuroimagistică Hipofizară
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: În caz de macroadenom voluminos, se adaugă o secvență axială T2 sau FLAIR a
  întregului creier pentru hidrocefalie obstructivă.
patient_prep: Completare chestionar securitate RM; verificare eGFR; imobilizare atentă
  a capului.
quality_criteria:
- Delimitare netă a chiasmei optice și a conturului glandei hipofize
- Rezoluție sub-milimetrică în plan (matrice mare raportată la FOV mic de 140 mm)
- Absența artefactelor de susceptibilitate provenite din sinusul sfenoid pneumatizat
safety_considerations:
- SAR redus pe câmp mic de examinare
- Monitorizare confort pacient pentru evitarea mișcărilor în faza dinamică
sequences:
- fat_sat: Nu
  fov_matrix: FOV 140 mm / 256x256
  name: Sagital T1 SE de înaltă rezoluție
  notes: Identificare hipersemnal fiziologic neurohipofiză
  plane: Sagital selar
  slice_gap: 2.0 - 2.5 mm / gap 0.2 mm
  tr_te: TR 500 ms / TE 10 ms
- fat_sat: Nu
  fov_matrix: FOV 140 mm / 320x256
  name: Coronal T2 TSE subțire
  notes: Evaluare sinusuri cavernoase și chiasmă optică
  plane: Coronal selar
  slice_gap: 2.0 - 2.5 mm / gap 0.2 mm
  tr_te: TR 3500 ms / TE 90 ms
- fat_sat: Nu
  fov_matrix: FOV 140 mm / 256x256
  name: Coronal T1 SE Nativ
  notes: Bază de comparație pentru faza dinamică
  plane: Coronal selar
  slice_gap: 2.0 - 2.5 mm / gap 0.2 mm
  tr_te: TR 500 ms / TE 10 ms
- fat_sat: Nu
  fov_matrix: FOV 140 mm / 256x192
  name: Coronal T1 Dinamic post-Gd (5-6 faze)
  notes: Secvență la 0s, 20s, 40s, 60s, 90s, 120s de la bolus
  plane: Coronal selar
  slice_gap: 2.5 mm / gap 0 mm
  tr_te: TR 250 - 300 ms / TE 8 ms
- fat_sat: Nu
  fov_matrix: FOV 140 mm / 320x256
  name: Sagital & Coronal T1 Tardiv + C
  notes: Studiu tardiv al leziunii și al extensiei supraselare
  plane: Sagital și Coronal
  slice_gap: 2.0 mm / gap 0.2 mm
  tr_te: TR 500 ms / TE 10 ms
slug: irm-hipofiza-cu-contrast-dinamic
title: IRM Hipofiză (Regiune Selară) cu Substanță de Contrast Dinamic
---
# IRM Hipofiză (Regiune Selară) cu Substanță de Contrast Dinamic

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

        - Suspiciune de microadenom hipofizar secretant (prolactinom, boală Cushing, acromegalie)
        - Macroadenom hipofizar (evaluare invazie sinus cavernos și compresie chiasmă optică)
        - Diabet insipid central (evaluare neurohipofiză și tijă pituitară)
        - Deficite hormonale hipofizare / panhipopituitarism

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM; insuficiență renală severă dacă eGFR < 30 ml/min.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Endocrinologie - Neuroimagistică Hipofizară*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Completare chestionar securitate RM; verificare eGFR; imobilizare atentă a capului.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau preferabil 3.0T (rezoluție spațială superioară pe câmp mic de 12-14 cm)
    - **Antenă de Recepție (Coil):** Antenă Head 32 sau 64 canale
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe nasion, plan de scanare strict perpendicular pe planul selar.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic
    - **Doză Recomandată:** 0.1 mmol/kg corp
    - **Rată de Injectare (Debit):** 2.0 - 2.5 ml/s urmat de flush de 20 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Achiziție dinamică rapidă coronală T1 (la fiecare 15-20 secunde timp de 2-3 minute)
    - **Filtrare Renală & Precauții:** Microadenoamele apar tipic ca arii hipocaptante tardiv-contrastate pe fondul captării precoce a parenchimului hipofizar normal.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T1 SE de înaltă rezoluție** | Sagital selar | TR 500 ms / TE 10 ms | 2.0 - 2.5 mm / gap 0.2 mm | FOV 140 mm / 256x256 | Nu | Identificare hipersemnal fiziologic neurohipofiză |
    | **Coronal T2 TSE subțire** | Coronal selar | TR 3500 ms / TE 90 ms | 2.0 - 2.5 mm / gap 0.2 mm | FOV 140 mm / 320x256 | Nu | Evaluare sinusuri cavernoase și chiasmă optică |
    | **Coronal T1 SE Nativ** | Coronal selar | TR 500 ms / TE 10 ms | 2.0 - 2.5 mm / gap 0.2 mm | FOV 140 mm / 256x256 | Nu | Bază de comparație pentru faza dinamică |
    | **Coronal T1 Dinamic post-Gd (5-6 faze)** | Coronal selar | TR 250 - 300 ms / TE 8 ms | 2.5 mm / gap 0 mm | FOV 140 mm / 256x192 | Nu | Secvență la 0s, 20s, 40s, 60s, 90s, 120s de la bolus |
    | **Sagital & Coronal T1 Tardiv + C** | Sagital și Coronal | TR 500 ms / TE 10 ms | 2.0 mm / gap 0.2 mm | FOV 140 mm / 320x256 | Nu | Studiu tardiv al leziunii și al extensiei supraselare |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Delimitare netă a chiasmei optice și a conturului glandei hipofize
    - Rezoluție sub-milimetrică în plan (matrice mare raportată la FOV mic de 140 mm)
    - Absența artefactelor de susceptibilitate provenite din sinusul sfenoid pneumatizat

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR redus pe câmp mic de examinare
    - Monitorizare confort pacient pentru evitarea mișcărilor în faza dinamică

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    În caz de macroadenom voluminos, se adaugă o secvență axială T2 sau FLAIR a întregului creier pentru hidrocefalie obstructivă.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
