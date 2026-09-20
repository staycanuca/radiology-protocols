---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Oftalmopatie tiroidiană Basedow-Graves (evaluare edem și activitate inflamatorie
  în mușchii oculomotori)
- Nevrită optică, neuropatii optice demielinizante sau ischemice
- Mase tumorale orbitare (hemangiom cavernos, meningiom de teacă de nerv optic, gliom,
  schwannom)
- Strabism restrictiv și evaluare dinamică a motilității musculare oculare (Cine ENT)
- Exoftalmie / proptoză unilaterală sau bilaterală neelucidată
coils_hardware:
  coil: Antenă dedicată Head/Neck multicanal de înaltă rezoluție
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, privire fixată înainte pe un punct de referință cu
    ochii închiși ușor pentru secvențele statice
contraindications:
- Corpi străini intraoculari feromagnetici (contraindicație absolută)
contrast:
  agent: Gadoliniu macrociclic (Gadoteridol / Gadobutrol)
  dose: 0.1 mmol/kg
  flow_rate: 1.5 - 2.0 mL/s
  notes: Supresia de grăsime (FatSat) este obligatorie pe secvențele post-contrast
    orbitare.
  timing: Secvențe post-contrast la 2-3 minute de la injectare
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol specializat OHSU integrând evaluarea statică și dinamică a patologiei
  orbitare și a nervului optic.
patient_prep: Îndepărtarea completă a machiajului ocular (fardurile conțin oxizi de
  fier care produc artefacte severe de susceptibilitate). Instrucțiuni de fixare a
  privirii.
quality_criteria:
- Supresie de grăsime omogenă pe secvențele coronale T2 FS și T1 FS post-contrast
- Absența artefactelor de clipire sau mișcare a globilor oculari
- Rezoluție spațială înaltă cu matrice minim 256×256 pe FOV mic (14-16 cm)
safety_considerations:
- Screening pentru corpi străini metalici intraoculari (radiografie orbitară prealabilă
  dacă există istoric de polizare/sudură)
- Evitarea compresiei oculare cu pernuțele de imobilizare
sequences:
- fat_sat: Nu
  fov_matrix: FOV 140-160 mm / Matrice 256×256
  name: Coronal T1 TSE (Secțiuni Fine)
  notes: 'Anatomie de bază: apreciere calibru pântece musculare (drept inferior, medial,
    superior, lateral) și grăsime conică'
  plane: Coronal (Perpendicular pe nervii optici)
  slice_gap: 2.5 mm / gap 0.2 mm
  tr_te: TR 500-650 ms / TE 10-15 ms
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 140-160 mm / Matrice 256×224
  name: Coronal T2 FS (STIR / SPAIR)
  notes: 'Cheie diagnostică pentru oftalmopatia Graves: hipersemnal T2 în mușchii
    oculari indică inflamație activă'
  plane: Coronal
  slice_gap: 2.5 mm / gap 0.2 mm
  tr_te: TR 3500-4500 ms / TE 60-80 ms
- fat_sat: Nu
  fov_matrix: FOV 160 mm / Matrice 256×256
  name: Axial T2 TSE / FSE
  notes: Evaluare traiect intraconal și canalicular al nervului optic și apex orbitar
  plane: Axial (Paralel cu traiectul nervilor optici)
  slice_gap: 2.5 mm / gap 0.2 mm
  tr_te: TR 3000-4000 ms / TE 80-90 ms
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 180 mm / Matrice 128×128
  name: Axial DWI (b=0, b=800) + ADC
  notes: Diferențiere celulită orbitară / abces / limfom orbitar
  plane: Axial
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 3000 ms / TE 70 ms
- fat_sat: Nu
  fov_matrix: FOV 180 mm / Matrice 192×192
  name: Cine bSSFP ENT (Evaluare Dinamică Motilitate)
  notes: Pacientul privește succesiv punctele de reper (sus, jos, stânga, dreapta)
    pentru a evalua excursia musculară
  plane: Coronal / Sagital oblic
  slice_gap: 4.0 mm
  tr_te: TR 3.0 ms / TE 1.5 ms
- fat_sat: FatSat obligatoriu
  fov_matrix: FOV 140-160 mm / Matrice 256×256
  name: Coronal T1 FS + C Post-Contrast
  notes: Captare patologică în teaca nervului optic (meningiom/nevrită) sau în pântecele
    musculare
  plane: Coronal
  slice_gap: 2.5 mm / gap 0.2 mm
  tr_te: TR 550-700 ms / TE 10-15 ms
- fat_sat: FatSat obligatoriu
  fov_matrix: FOV 160 mm / Matrice 256×256
  name: Axial T1 FS + C Post-Contrast
  notes: Acoperire de la globul ocular până la chiasma optică
  plane: Axial
  slice_gap: 2.5 mm / gap 0.2 mm
  tr_te: TR 550-700 ms / TE 10-15 ms
title: RM Orbite & Nervi Optici / Graves & Cine ENT (Protocol OHSU)
---
# RM Orbite & Nervi Optici / Graves & Cine ENT (Protocol OHSU)

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

        - Oftalmopatie tiroidiană Basedow-Graves (evaluare edem și activitate inflamatorie în mușchii oculomotori)
        - Nevrită optică, neuropatii optice demielinizante sau ischemice
        - Mase tumorale orbitare (hemangiom cavernos, meningiom de teacă de nerv optic, gliom, schwannom)
        - Strabism restrictiv și evaluare dinamică a motilității musculare oculare (Cine ENT)
        - Exoftalmie / proptoză unilaterală sau bilaterală neelucidată

    === "Contraindicații & Screening Metalic"

        - Corpi străini intraoculari feromagnetici (contraindicație absolută)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cap, Gât & Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Îndepărtarea completă a machiajului ocular (fardurile conțin oxizi de fier care produc artefacte severe de susceptibilitate). Instrucțiuni de fixare a privirii.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată Head/Neck multicanal de înaltă rezoluție
    - **Poziție Pacient & Centrare:** Decubit dorsal, privire fixată înainte pe un punct de referință cu ochii închiși ușor pentru secvențele statice

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic (Gadoteridol / Gadobutrol)
    - **Doză Recomandată:** 0.1 mmol/kg
    - **Rată de Injectare (Debit):** 1.5 - 2.0 mL/s
    - **Temporizare & Faze Dinamice:** Secvențe post-contrast la 2-3 minute de la injectare
    - **Filtrare Renală & Precauții:** Supresia de grăsime (FatSat) este obligatorie pe secvențele post-contrast orbitare.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T1 TSE (Secțiuni Fine)** | Coronal (Perpendicular pe nervii optici) | TR 500-650 ms / TE 10-15 ms | 2.5 mm / gap 0.2 mm | FOV 140-160 mm / Matrice 256×256 | Nu | Anatomie de bază: apreciere calibru pântece musculare (drept inferior, medial, superior, lateral) și grăsime conică |
    | **Coronal T2 FS (STIR / SPAIR)** | Coronal | TR 3500-4500 ms / TE 60-80 ms | 2.5 mm / gap 0.2 mm | FOV 140-160 mm / Matrice 256×224 | FatSat / SPAIR | Cheie diagnostică pentru oftalmopatia Graves: hipersemnal T2 în mușchii oculari indică inflamație activă |
    | **Axial T2 TSE / FSE** | Axial (Paralel cu traiectul nervilor optici) | TR 3000-4000 ms / TE 80-90 ms | 2.5 mm / gap 0.2 mm | FOV 160 mm / Matrice 256×256 | Nu | Evaluare traiect intraconal și canalicular al nervului optic și apex orbitar |
    | **Axial DWI (b=0, b=800) + ADC** | Axial | TR 3000 ms / TE 70 ms | 3.0 mm / gap 0.3 mm | FOV 180 mm / Matrice 128×128 | FatSat (EPI) | Diferențiere celulită orbitară / abces / limfom orbitar |
    | **Cine bSSFP ENT (Evaluare Dinamică Motilitate)** | Coronal / Sagital oblic | TR 3.0 ms / TE 1.5 ms | 4.0 mm | FOV 180 mm / Matrice 192×192 | Nu | Pacientul privește succesiv punctele de reper (sus, jos, stânga, dreapta) pentru a evalua excursia musculară |
    | **Coronal T1 FS + C Post-Contrast** | Coronal | TR 550-700 ms / TE 10-15 ms | 2.5 mm / gap 0.2 mm | FOV 140-160 mm / Matrice 256×256 | FatSat obligatoriu | Captare patologică în teaca nervului optic (meningiom/nevrită) sau în pântecele musculare |
    | **Axial T1 FS + C Post-Contrast** | Axial | TR 550-700 ms / TE 10-15 ms | 2.5 mm / gap 0.2 mm | FOV 160 mm / Matrice 256×256 | FatSat obligatoriu | Acoperire de la globul ocular până la chiasma optică |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Supresie de grăsime omogenă pe secvențele coronale T2 FS și T1 FS post-contrast
    - Absența artefactelor de clipire sau mișcare a globilor oculari
    - Rezoluție spațială înaltă cu matrice minim 256×256 pe FOV mic (14-16 cm)

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening pentru corpi străini metalici intraoculari (radiografie orbitară prealabilă dacă există istoric de polizare/sudură)
    - Evitarea compresiei oculare cu pernuțele de imobilizare

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol specializat OHSU integrând evaluarea statică și dinamică a patologiei orbitare și a nervului optic.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
