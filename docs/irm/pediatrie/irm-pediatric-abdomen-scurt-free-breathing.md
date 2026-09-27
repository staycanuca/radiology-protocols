---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Sugari și copii mici incapabili de apnee voluntară
- 'Durere abdominală acută la copil când ecografia este neconcludentă (ex: apendicită
  atipică, diverticulită)'
- Suspiciune de invaginație intestinală sau masă pelvină/abdominală palpabilă
- Screening abdominal rapid fără sedare și fără expunere la radiații ionizante
coils_hardware:
  coil: Antenă Phased-Array de corp (Body/Torso array)
  field_strength: 1.5 Tesla (preferat pentru mai puține artefacte de susceptibilitate)
    sau 3.0 Tesla
  positioning: Decubit dorsal, antenă ușor fixată pe abdomen fără a jena excursiile
    respiratorii
contraindications:
- Implanturi feromagnetice incompatibile RM
contrast:
  agent: Fără contrast (examinare nativă rapidă)
  dose: N/A
  flow_rate: N/A
  notes: Protocol exclusiv nativ conceput pentru durată minimă (8-10 minute).
  timing: N/A
iris_reference:
  chapter: Pediatrie - Aparat digestiv & Abdomen
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol WFPI conceput pentru a detecta rapid patologia abdominală pediatrică
  fără sedare și în respirație liberă.
patient_prep: Post alimentar ușor (2 ore pentru lichide clare la sugari); tehnici
  de liniștire fără sedare.
quality_criteria:
- 'Timp total de scanare la aparat: 8–10 minute'
- Complet realizabil în respirație liberă (Free-Breathing) la sugari și copii mici
- Vizualizare clară a tractului digestiv, a ficatului, splinei și rinichilor
safety_considerations:
- Nu comprimă toracele/abdomenul copilului cu antena de corp (se folosesc distanțiere
  moi)
- Protecție acustică adecvată
sequences:
- fat_sat: Nu
  fov_matrix: FOV 280-350 mm / 256x256
  name: Coronal T2WI Single-Shot (HASTE / SSFSE)
  notes: Respirație liberă (Free-Breathing), imagine panoramică abdomen-pelvis (30–45
    s)
  plane: Coronal
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 1000 ms / TE 80-90 ms
- fat_sat: Nu
  fov_matrix: FOV 250-300 mm / 256x256
  name: Axial T2WI Single-Shot (HASTE / SSFSE)
  notes: Respirație liberă (FB), orientare anatomică transversală (30–45 s)
  plane: Axial
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 1000 ms / TE 80-90 ms
- fat_sat: FatSat
  fov_matrix: FOV 250-300 mm / 256x224
  name: Axial T2WI SSFSE FS (cu supresie de grăsime)
  notes: Trigger respirator (Respiratory Trigger), edem perivisceral, apendice, limfonoduli
    (3–5 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 1500 ms / TE 80 ms
- fat_sat: FatSat
  fov_matrix: FOV 250-300 mm / 128x128
  name: Axial DWI (b=50, b=400, b=800) + ADC
  notes: Respirație liberă cu medieri crescute (NEX variabil), detecție focare inflamatorii/tumori
    (3–4 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3000-4000 ms / TE 60 ms
- fat_sat: Nu (Dual-Echo)
  fov_matrix: FOV 250-300 mm / 256x192
  name: Axial T1WI In-Phase / Opposed-Phase
  notes: Trigger respirator sau respirație liberă, evaluare grăsime intraparenchimatoasă
    și hemoragie (3–4 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 120-150 ms / TE 2.2 ms & 4.4 ms
slug: irm-pediatric-abdomen-scurt-free-breathing
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
title: RM Pediatric — Protocol Abdomen Scurt / Respirație Liberă (Short Abdomen)
---
# RM Pediatric — Protocol Abdomen Scurt / Respirație Liberă (Short Abdomen)

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

        - Sugari și copii mici incapabili de apnee voluntară
        - Durere abdominală acută la copil când ecografia este neconcludentă (ex: apendicită atipică, diverticulită)
        - Suspiciune de invaginație intestinală sau masă pelvină/abdominală palpabilă
        - Screening abdominal rapid fără sedare și fără expunere la radiații ionizante

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice incompatibile RM

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Aparat digestiv & Abdomen*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Post alimentar ușor (2 ore pentru lichide clare la sugari); tehnici de liniștire fără sedare.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla (preferat pentru mai puține artefacte de susceptibilitate) sau 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă Phased-Array de corp (Body/Torso array)
    - **Poziție Pacient & Centrare:** Decubit dorsal, antenă ușor fixată pe abdomen fără a jena excursiile respiratorii

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Fără contrast (examinare nativă rapidă)
    - **Doză Recomandată:** N/A
    - **Rată de Injectare (Debit):** N/A
    - **Temporizare & Faze Dinamice:** N/A
    - **Filtrare Renală & Precauții:** Protocol exclusiv nativ conceput pentru durată minimă (8-10 minute).

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T2WI Single-Shot (HASTE / SSFSE)** | Coronal | TR 1000 ms / TE 80-90 ms | 4.0 mm / gap 0 mm | FOV 280-350 mm / 256x256 | Nu | Respirație liberă (Free-Breathing), imagine panoramică abdomen-pelvis (30–45 s) |
    | **Axial T2WI Single-Shot (HASTE / SSFSE)** | Axial | TR 1000 ms / TE 80-90 ms | 4.0 mm / gap 0 mm | FOV 250-300 mm / 256x256 | Nu | Respirație liberă (FB), orientare anatomică transversală (30–45 s) |
    | **Axial T2WI SSFSE FS (cu supresie de grăsime)** | Axial | TR 1500 ms / TE 80 ms | 4.0 mm / gap 0.4 mm | FOV 250-300 mm / 256x224 | FatSat | Trigger respirator (Respiratory Trigger), edem perivisceral, apendice, limfonoduli (3–5 min) |
    | **Axial DWI (b=50, b=400, b=800) + ADC** | Axial | TR 3000-4000 ms / TE 60 ms | 4.0 mm / gap 0.4 mm | FOV 250-300 mm / 128x128 | FatSat | Respirație liberă cu medieri crescute (NEX variabil), detecție focare inflamatorii/tumori (3–4 min) |
    | **Axial T1WI In-Phase / Opposed-Phase** | Axial | TR 120-150 ms / TE 2.2 ms & 4.4 ms | 4.0 mm / gap 0.4 mm | FOV 250-300 mm / 256x192 | Nu (Dual-Echo) | Trigger respirator sau respirație liberă, evaluare grăsime intraparenchimatoasă și hemoragie (3–4 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de scanare la aparat: 8–10 minute
    - Complet realizabil în respirație liberă (Free-Breathing) la sugari și copii mici
    - Vizualizare clară a tractului digestiv, a ficatului, splinei și rinichilor

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Nu comprimă toracele/abdomenul copilului cu antena de corp (se folosesc distanțiere moi)
    - Protecție acustică adecvată

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol WFPI conceput pentru a detecta rapid patologia abdominală pediatrică fără sedare și în respirație liberă.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
