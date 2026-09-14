---
author: Departamentul de Radiologie și Imagistică Medicală
category: abdomen-pelvis
clinical_indications:
- Valoare PSA seric crescută sau în dinamică ascendentă (suspiciune cancer de prostată)
- Ghidare pentru biopsie prostatică țintită prin fuziune RMN-Ecografie (Fusion Biopsy)
- Stadializare loco-regională a adenocarcinomului de prostată (extensie extracapsulară
  ECE, invazie vezicule seminale)
- Supraveghere activă a pacienților cu cancer de prostată cu risc scăzut
- Evaluare recidivă biochimică după prostatectomie radicală sau radioterapie
coils_hardware:
  coil: Antenă Pelvic Phased-Array multicanal de suprafață (fără necesar de antenă
    endorectală la 3.0T)
  field_strength: Preferabil 3.0 Tesla (sau 1.5 Tesla cu antenă de suprafață performantă)
  positioning: Decubit dorsal, centrare la 2 cm deasupra simfizei pubiene.
contraindications:
- Contraindicații generale RM; proteză totală de șold bilaterală din metal feromagnetic
  (artefacte majore).
contrast:
  agent: Chelat de Gadoliniu macrociclic
  dose: 0.1 mmol/kg corp
  flow_rate: 2.5 - 3.0 ml/s cu injector automat + 30 ml ser fiziologic
  notes: DCE este secvență secundară utilă în special pentru clarificarea leziunilor
    de zonă periferică clasificate PI-RADS 3.
  timing: Achiziție dinamică rapidă DCE (Dynamic Contrast-Enhanced) la fiecare 5-10
    secunde timp de minimum 2 minute
iris_reference:
  chapter: Urologie & Oncologie - Neoplasm Prostatic
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Scor PI-RADS 1-5 atribuit fiecărei leziuni suspecte. Categoriile PI-RADS 4
  și 5 indică suspiciune înaltă / foarte înaltă de malignitate clinic semnificativă
  (Gleason ≥ 3+4) și necesită biopsie țintită.
patient_prep: Evacuare rectală în dimineața examinării (microclismă opțională); abstinență
  sexuală 3-4 zile anterior (pentru repleția veziculelor seminale); administrare Buscopan
  20 mg IV pentru oprirea peristaltismului rectal; vezică urinară semi-plină (nu destinsă
  la maximum).
quality_criteria:
- Respectarea strictă a specificațiilor tehnice PI-RADS v2.1
- Absența artefactelor de distorsiune geometrică rectală pe secvența DWI (asigurată
  prin evacuare)
- Grosime de strat maximă de 3.0 mm fără spațiu între secțiuni (gap 0)
safety_considerations:
- SAR bine controlat pe pelvis
- Examinarea se programează la minimum 6-8 săptămâni după o puncție biopsie prostatică
  pentru resorbția hematoamelor ce pot mima sau masca tumori
sequences:
- fat_sat: Nu
  fov_matrix: FOV 180 mm / 384x320
  name: T2 TSE de Înaltă Rezoluție Axial (Small FOV)
  notes: 'Anatomie zonală: zona de tranziție (TZ) și zona periferică (PZ), capsulă'
  plane: Axial perpendicular pe uretra prostatică
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4500 ms / TE 110 ms
- fat_sat: Nu
  fov_matrix: FOV 180 - 200 mm / 320x256
  name: T2 TSE Sagital și Coronal
  notes: Bază, apex, vezicule seminale, col vezical
  plane: Sagital și Coronal
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4000 ms / TE 100 ms
- fat_sat: FatSat
  fov_matrix: FOV 180 mm / 128x128
  name: DWI Multi-b (b=50, 800, 1400 s/mm²) + ADC Map
  notes: Secvența dominantă pentru Zona Periferică (PZ)
  plane: Axial
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 5000 ms / TE 70 ms
- fat_sat: FatSat
  fov_matrix: FOV 180 mm / 128x128
  name: Calculated Ultra-High b-value (b=2000 s/mm²)
  notes: Supresie completă a semnalului adenomatos benign de fond
  plane: Axial
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: Calculat sintetic sau achiziționat
- fat_sat: FatSat
  fov_matrix: FOV 200 mm / 192x160
  name: 3D T1 Dinamic DCE (Perfusion)
  notes: Captare precoce focală asimetrică și wash-out rapid
  plane: Axial
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 3.5 ms / TE 1.4 ms / Rezoluție temporală < 7-10s
- fat_sat: Nu
  fov_matrix: FOV 360 mm / 320x256
  name: Axial T1 Pelvis Mare
  notes: Adenopatii pelvine obturatorii/iliace și hemoragie post-biopsie
  plane: Axial
  slice_gap: 4.0 mm / gap 0.5 mm
  tr_te: TR 600 ms / TE 10 ms
slug: irm-prostata-multiparametrica-mpmri
title: IRM Prostată Multiparametrică (mpMRI) - Protocol PI-RADS v2.1
sources:
- title: UT Southwestern Radiology — Abdomen & Pelvis MRI Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 15b64e8c0d1c83d4ed74c3e0e07b8690a60efdcc4e9083d1af807018cacc44f0
- title: ACR-SAR-SPR Practice Parameter for the Performance of Magnetic Resonance
    Imaging (MRI) of the Abdomen and Pelvis
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Abd-Pel.pdf
  institution: ACR / SAR
  source_region: US
  kind: Standard de practică IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 96d9b81fe5cc97327da7ae58176482d43b9367d0e227000b2e105e7199658f88
position: Decubit dorsal, centrare la 2 cm deasupra simfizei pubiene.
---

# IRM Prostată Multiparametrică (mpMRI) - Protocol PI-RADS v2.1

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

        - Valoare PSA seric crescută sau în dinamică ascendentă (suspiciune cancer de prostată)
        - Ghidare pentru biopsie prostatică țintită prin fuziune RMN-Ecografie (Fusion Biopsy)
        - Stadializare loco-regională a adenocarcinomului de prostată (extensie extracapsulară ECE, invazie vezicule seminale)
        - Supraveghere activă a pacienților cu cancer de prostată cu risc scăzut
        - Evaluare recidivă biochimică după prostatectomie radicală sau radioterapie

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM; proteză totală de șold bilaterală din metal feromagnetic (artefacte majore).

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Urologie & Oncologie - Neoplasm Prostatic*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Evacuare rectală în dimineața examinării (microclismă opțională); abstinență sexuală 3-4 zile anterior (pentru repleția veziculelor seminale); administrare Buscopan 20 mg IV pentru oprirea peristaltismului rectal; vezică urinară semi-plină (nu destinsă la maximum).
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** Preferabil 3.0 Tesla (sau 1.5 Tesla cu antenă de suprafață performantă)
    - **Antenă de Recepție (Coil):** Antenă Pelvic Phased-Array multicanal de suprafață (fără necesar de antenă endorectală la 3.0T)
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare la 2 cm deasupra simfizei pubiene.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic
    - **Doză Recomandată:** 0.1 mmol/kg corp
    - **Rată de Injectare (Debit):** 2.5 - 3.0 ml/s cu injector automat + 30 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Achiziție dinamică rapidă DCE (Dynamic Contrast-Enhanced) la fiecare 5-10 secunde timp de minimum 2 minute
    - **Filtrare Renală & Precauții:** DCE este secvență secundară utilă în special pentru clarificarea leziunilor de zonă periferică clasificate PI-RADS 3.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **T2 TSE de Înaltă Rezoluție Axial (Small FOV)** | Axial perpendicular pe uretra prostatică | TR 4500 ms / TE 110 ms | 3.0 mm / gap 0 mm | FOV 180 mm / 384x320 | Nu | Anatomie zonală: zona de tranziție (TZ) și zona periferică (PZ), capsulă |
    | **T2 TSE Sagital și Coronal** | Sagital și Coronal | TR 4000 ms / TE 100 ms | 3.0 mm / gap 0 mm | FOV 180 - 200 mm / 320x256 | Nu | Bază, apex, vezicule seminale, col vezical |
    | **DWI Multi-b (b=50, 800, 1400 s/mm²) + ADC Map** | Axial | TR 5000 ms / TE 70 ms | 3.0 mm / gap 0 mm | FOV 180 mm / 128x128 | FatSat | Secvența dominantă pentru Zona Periferică (PZ) |
    | **Calculated Ultra-High b-value (b=2000 s/mm²)** | Axial | Calculat sintetic sau achiziționat | 3.0 mm / gap 0 mm | FOV 180 mm / 128x128 | FatSat | Supresie completă a semnalului adenomatos benign de fond |
    | **3D T1 Dinamic DCE (Perfusion)** | Axial | TR 3.5 ms / TE 1.4 ms / Rezoluție temporală < 7-10s | 3.0 mm / gap 0 mm | FOV 200 mm / 192x160 | FatSat | Captare precoce focală asimetrică și wash-out rapid |
    | **Axial T1 Pelvis Mare** | Axial | TR 600 ms / TE 10 ms | 4.0 mm / gap 0.5 mm | FOV 360 mm / 320x256 | Nu | Adenopatii pelvine obturatorii/iliace și hemoragie post-biopsie |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Respectarea strictă a specificațiilor tehnice PI-RADS v2.1
    - Absența artefactelor de distorsiune geometrică rectală pe secvența DWI (asigurată prin evacuare)
    - Grosime de strat maximă de 3.0 mm fără spațiu între secțiuni (gap 0)

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR bine controlat pe pelvis
    - Examinarea se programează la minimum 6-8 săptămâni după o puncție biopsie prostatică pentru resorbția hematoamelor ce pot mima sau masca tumori

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Scor PI-RADS 1-5 atribuit fiecărei leziuni suspecte. Categoriile PI-RADS 4 și 5 indică suspiciune înaltă / foarte înaltă de malignitate clinic semnificativă (Gleason ≥ 3+4) și necesită biopsie țintită.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [UT Southwestern Radiology — Abdomen & Pelvis MRI Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html) — *UT Southwestern* (US)
- [ACR-SAR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Abdomen and Pelvis](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Abd-Pel.pdf) — *ACR / SAR* (US)
