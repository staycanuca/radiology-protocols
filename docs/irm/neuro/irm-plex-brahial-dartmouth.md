---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: neuro
clinical_indications:
- Plexopatie brahială de etiologie neprecizată (durere radiculară, parestezii, slăbiciune
  musculară a membrului superior)
- Traumatisme de plex brahial (suspiciune de avulsie radiculară preganglionară sau
  ruptură postganglionară)
- Tumori ale tecii nervoase periferice (schwannom, neurofibrom) sau sindrom de defileu
  toracic (TOS)
- Sindrom Pancoast-Tobias (tumoră de vârf pulmonar cu invazie de plex brahial C8-T1)
- Plexită post-radică vs. recidivă tumorală la pacienți oncologici tratați
coils_hardware:
  coil: Combinație antenă Neurovasculară (Head & Neck Array) + antenă Body posterioară/anterioară
    pe claviculă și umăr
  field_strength: 1.5 Tesla sau 3.0 Tesla
  positioning: Decubit dorsal, brațele relaxate pe lângă corp (sau cu brațul afectat
    în ușoară abducție dacă se investighează TOS dinamic)
contraindications:
- Contraindicații feromagnetice clasice RM
- Imposibilitatea menținerii decubitului dorsal fără mișcare a umerilor
contrast:
  agent: Gadoliniu macrociclic 0.1 mmol/kg
  dose: 0.1 mmol/kg + flush salin 20 mL
  flow_rate: 1.5 - 2.0 mL/s
  timing: Achiziție post-contrast tardivă la 2-3 minute
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
modality: irm
notes: Protocolul Dartmouth Hitchcock subliniază importanța secvenței sagitale T1/T2
  perpendiculare pe claviculă pentru vizualizarea directă a 'triunghiului interscalenic'
  format de mușchiul scalen anterior, scalen mijlociu și prima coastă.
patient_prep: Screening feromagnetic complet. Se explică pacientului să evite înghițirea
  repetată în timpul scanărilor gâtului pentru a nu crea artefacte de mișcare pe rădăcinile
  nervoase.
quality_criteria:
- Acoperire completă a rădăcinilor emergente C5, C6, C7, C8 și T1 de la foramenul
  intervertebral până la diviziunile axilare
- Absența artefactelor de pulsație vasculară prin plasarea benzilor de presaturație
  pe artera subclavie
safety_considerations:
- Screening feromagnetic riguros
- Verificare eGFR
sequences:
- fat_sat: Da (STIR robust la interfețe osoase)
  fov_matrix: FOV 360 mm / Matrice 384×256
  name: Coronal T2 STIR / SPAIR Bilateral (Vedere de Ansamblu)
  notes: Comparație simetrică între plexul drept și cel stâng; identificare edem și
    hipersemnal radicular
  plane: Coronal
  slice_gap: 3.5 mm / 0.5 mm gap
  tr_te: TR 4500 ms / TE 65 ms / TI 160 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / Matrice 320×256
  name: Sagital T1 SE Unilateral (Plex Afectat)
  notes: Esențial pentru anatomia trunchiurilor și cordoanelor înconjurate de grăsime
    între mușchii scaleni
  plane: Sagital oblic (perpendicular pe claviculă de la coloană la axilă)
  slice_gap: 3.0 mm / 0.5 mm gap
  tr_te: TR 650 ms / TE 12 ms
- fat_sat: Da
  fov_matrix: FOV 200 mm / Matrice 320×256
  name: Sagital T2 FS Unilateral
  notes: Evidențierea inflamației, comprimării nervoase și leziunilor de continuitate
  plane: Sagital oblic
  slice_gap: 3.0 mm / 0.5 mm gap
  tr_te: TR 3800 ms / TE 85 ms
- fat_sat: Nu
  fov_matrix: FOV 240 mm / Matrice 320×256
  name: Coronal T1 SE
  notes: Detecție pseudomeningocele post-traumatice și infiltrare tumorală
  plane: Coronal
  slice_gap: 3.0 mm
  tr_te: TR 600 ms / TE 11 ms
- fat_sat: Da
  fov_matrix: FOV 260 mm
  name: 3D T2 SPACE STIR Izotrop (opțional)
  notes: Navigare MPR în orice plan de-a lungul traiectului radicular C5–T1
  plane: 3D Volumetric Coronal
  slice_gap: 1.0 mm izotrop
  tr_te: TR 2500 ms / TE 180 ms
- fat_sat: Da
  fov_matrix: FOV 240 mm / Matrice 320×256
  name: Post-Contrast Coronal & Axial 3D T1 FS
  notes: Captare patologică de contrast în neurinoame, plexită infecțioasă/inflamatorie
    sau invazie neoplazică
  plane: Coronal & Axial
  slice_gap: 1.5 mm
  tr_te: TR 4.5 ms / TE 1.8 ms
title: IRM Plex Brahial Nativ & cu Contrast (Protocol DHMC)
---
# IRM Plex Brahial Nativ & cu Contrast (Protocol DHMC)

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

        - Plexopatie brahială de etiologie neprecizată (durere radiculară, parestezii, slăbiciune musculară a membrului superior)
        - Traumatisme de plex brahial (suspiciune de avulsie radiculară preganglionară sau ruptură postganglionară)
        - Tumori ale tecii nervoase periferice (schwannom, neurofibrom) sau sindrom de defileu toracic (TOS)
        - Sindrom Pancoast-Tobias (tumoră de vârf pulmonar cu invazie de plex brahial C8-T1)
        - Plexită post-radică vs. recidivă tumorală la pacienți oncologici tratați

    === "Contraindicații & Screening Metalic"

        - Contraindicații feromagnetice clasice RM
        - Imposibilitatea menținerii decubitului dorsal fără mișcare a umerilor

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cap, Gât & Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Screening feromagnetic complet. Se explică pacientului să evite înghițirea repetată în timpul scanărilor gâtului pentru a nu crea artefacte de mișcare pe rădăcinile nervoase.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla sau 3.0 Tesla
    - **Antenă de Recepție (Coil):** Combinație antenă Neurovasculară (Head & Neck Array) + antenă Body posterioară/anterioară pe claviculă și umăr
    - **Poziție Pacient & Centrare:** Decubit dorsal, brațele relaxate pe lângă corp (sau cu brațul afectat în ușoară abducție dacă se investighează TOS dinamic)

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic 0.1 mmol/kg
    - **Doză Recomandată:** 0.1 mmol/kg + flush salin 20 mL
    - **Rată de Injectare (Debit):** 1.5 - 2.0 mL/s
    - **Temporizare & Faze Dinamice:** Achiziție post-contrast tardivă la 2-3 minute
    - **Filtrare Renală & Precauții:** Evaluare eGFR conform ghidurilor ESUR; risc redus de Fibroză Sistemică Nefrogenă (NSF) pentru agenții macrociclici.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T2 STIR / SPAIR Bilateral (Vedere de Ansamblu)** | Coronal | TR 4500 ms / TE 65 ms / TI 160 ms | 3.5 mm / 0.5 mm gap | FOV 360 mm / Matrice 384×256 | Da (STIR robust la interfețe osoase) | Comparație simetrică între plexul drept și cel stâng; identificare edem și hipersemnal radicular |
    | **Sagital T1 SE Unilateral (Plex Afectat)** | Sagital oblic (perpendicular pe claviculă de la coloană la axilă) | TR 650 ms / TE 12 ms | 3.0 mm / 0.5 mm gap | FOV 200 mm / Matrice 320×256 | Nu | Esențial pentru anatomia trunchiurilor și cordoanelor înconjurate de grăsime între mușchii scaleni |
    | **Sagital T2 FS Unilateral** | Sagital oblic | TR 3800 ms / TE 85 ms | 3.0 mm / 0.5 mm gap | FOV 200 mm / Matrice 320×256 | Da | Evidențierea inflamației, comprimării nervoase și leziunilor de continuitate |
    | **Coronal T1 SE** | Coronal | TR 600 ms / TE 11 ms | 3.0 mm | FOV 240 mm / Matrice 320×256 | Nu | Detecție pseudomeningocele post-traumatice și infiltrare tumorală |
    | **3D T2 SPACE STIR Izotrop (opțional)** | 3D Volumetric Coronal | TR 2500 ms / TE 180 ms | 1.0 mm izotrop | FOV 260 mm | Da | Navigare MPR în orice plan de-a lungul traiectului radicular C5–T1 |
    | **Post-Contrast Coronal & Axial 3D T1 FS** | Coronal & Axial | TR 4.5 ms / TE 1.8 ms | 1.5 mm | FOV 240 mm / Matrice 320×256 | Da | Captare patologică de contrast în neurinoame, plexită infecțioasă/inflamatorie sau invazie neoplazică |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Acoperire completă a rădăcinilor emergente C5, C6, C7, C8 și T1 de la foramenul intervertebral până la diviziunile axilare
    - Absența artefactelor de pulsație vasculară prin plasarea benzilor de presaturație pe artera subclavie

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening feromagnetic riguros
    - Verificare eGFR

</div>


!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocolul Dartmouth Hitchcock subliniază importanța secvenței sagitale T1/T2 perpendiculare pe claviculă pentru vizualizarea directă a 'triunghiului interscalenic' format de mușchiul scalen anterior, scalen mijlociu și prima coastă.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
