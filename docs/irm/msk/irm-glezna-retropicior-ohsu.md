---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: msk
clinical_indications:
- Tendinopatie, ruptură parțială sau totală a tendonului achilian sau a tendonului
  tibial posterior
- Leziuni ligamentare acute sau instabilitate cronică de gleznă (ligament talofibular
  anterior, calcaneofibular, deltoid)
- Sindroame de impingement anterior, anterolateral sau posterior de gleznă
- Osteonecroză aseptică de talus, fracturi de stres sau leziuni osteocondrale ale
  domului talar
- Fasceită plantară proximală și durere nespecifică de retropicior
coils_hardware:
  coil: Antenă dedicată de gleznă / picior Foot/Ankle multicanal (8–16 canale)
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, picior în flexie neutră la 90° imobilizat ferm în antenă
    pentru a preveni 'magic angle effect' pe tendoane
contraindications:
- Implanturi feromagnetice incompatibile
contrast:
  agent: Fără contrast (protocol de rutină)
  dose: N/A
  flow_rate: N/A
  notes: Contrastul i.v. se administrează doar în suspiciuni specifice de artrită
    inflamatorie, sinovită proliferativă sau infecție/abces.
  timing: N/A
iris_reference:
  chapter: Aparat locomotor & Articulații
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol standardizat OHSU MSK pentru diagnosticul precis al patologiei tendinoase,
  ligamentare și cartilaginoase de gleznă și retropicior.
patient_prep: Screening standard de securitate RM. Fără pregătire medicamentoasă specială.
quality_criteria:
- Poziționare strict neutră la 90° pentru a evita creșterea artificială de semnal
  pe tendoane datorită fenomenului 'Magic Angle' (55°)
- Supresie omogenă de grăsime pe întregul volum al retropiciorului
- Rezoluție spațială înaltă adaptată structurilor ligamentare fine
safety_considerations:
- Screening feromagnetic obligatoriu
- Verificarea eventualelor materiale de osteosinteză la nivelul gleznei — utilizare
  secvențe de reducere a artefactelor metalice (WARP/MARS) dacă este necesar
sequences:
- fat_sat: Nu
  fov_matrix: FOV 140 mm / Matrice 320×256
  name: Sagital T1 SE / TSE
  notes: Morfologie tendon achilian, fascie plantară, arhitectură osoasă calcaneu
    și talus
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 500-650 ms / TE 10-15 ms
- fat_sat: FatSat
  fov_matrix: FOV 140 mm / Matrice 288×256
  name: Sagital PD FS (Proton Density FatSat)
  notes: Edem osos, bursită retrocalcaneană, bursită pre-achiliană, rupturi fibrilare
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2500-3500 ms / TE 30-40 ms
- fat_sat: FatSat
  fov_matrix: FOV 140 mm / Matrice 288×256
  name: Coronal PD FS
  notes: Ligament colateral medial (deltoid), ligament calcaneofibular, tendoane peroniere
    și tibial posterior
  plane: Coronal (Orientat pe axul lung al calcaneului / maleole)
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2500-3500 ms / TE 30-40 ms
- fat_sat: Nu
  fov_matrix: FOV 120-140 mm / Matrice 320×256
  name: Axial T1 SE / TSE
  notes: Anatomie de secțiune transversală a compartimentelor tendinoase retromaleolare
  plane: Axial (Perpendicular pe axul lung al tibiei)
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 500-650 ms / TE 10-15 ms
- fat_sat: FatSat
  fov_matrix: FOV 120-140 mm / Matrice 288×256
  name: Axial PD FS
  notes: Tenosinovită a tendoanelor peroniere, tibial posterior, flexor lung al halucelui,
    ligament talofibular anterior (LTFA)
  plane: Axial
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2500-3500 ms / TE 30-40 ms
title: RM Retropicior & Gleznă MSK (Protocol OHSU)
---
# RM Retropicior & Gleznă MSK (Protocol OHSU)

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

        - Tendinopatie, ruptură parțială sau totală a tendonului achilian sau a tendonului tibial posterior
        - Leziuni ligamentare acute sau instabilitate cronică de gleznă (ligament talofibular anterior, calcaneofibular, deltoid)
        - Sindroame de impingement anterior, anterolateral sau posterior de gleznă
        - Osteonecroză aseptică de talus, fracturi de stres sau leziuni osteocondrale ale domului talar
        - Fasceită plantară proximală și durere nespecifică de retropicior

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice incompatibile

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat locomotor & Articulații*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Screening standard de securitate RM. Fără pregătire medicamentoasă specială.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată de gleznă / picior Foot/Ankle multicanal (8–16 canale)
    - **Poziție Pacient & Centrare:** Decubit dorsal, picior în flexie neutră la 90° imobilizat ferm în antenă pentru a preveni 'magic angle effect' pe tendoane

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Fără contrast (protocol de rutină)
    - **Doză Recomandată:** N/A
    - **Rată de Injectare (Debit):** N/A
    - **Temporizare & Faze Dinamice:** N/A
    - **Filtrare Renală & Precauții:** Contrastul i.v. se administrează doar în suspiciuni specifice de artrită inflamatorie, sinovită proliferativă sau infecție/abces.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T1 SE / TSE** | Sagital | TR 500-650 ms / TE 10-15 ms | 3.0 mm / gap 0.3 mm | FOV 140 mm / Matrice 320×256 | Nu | Morfologie tendon achilian, fascie plantară, arhitectură osoasă calcaneu și talus |
    | **Sagital PD FS (Proton Density FatSat)** | Sagital | TR 2500-3500 ms / TE 30-40 ms | 3.0 mm / gap 0.3 mm | FOV 140 mm / Matrice 288×256 | FatSat | Edem osos, bursită retrocalcaneană, bursită pre-achiliană, rupturi fibrilare |
    | **Coronal PD FS** | Coronal (Orientat pe axul lung al calcaneului / maleole) | TR 2500-3500 ms / TE 30-40 ms | 3.0 mm / gap 0.3 mm | FOV 140 mm / Matrice 288×256 | FatSat | Ligament colateral medial (deltoid), ligament calcaneofibular, tendoane peroniere și tibial posterior |
    | **Axial T1 SE / TSE** | Axial (Perpendicular pe axul lung al tibiei) | TR 500-650 ms / TE 10-15 ms | 3.0 mm / gap 0.3 mm | FOV 120-140 mm / Matrice 320×256 | Nu | Anatomie de secțiune transversală a compartimentelor tendinoase retromaleolare |
    | **Axial PD FS** | Axial | TR 2500-3500 ms / TE 30-40 ms | 3.0 mm / gap 0.3 mm | FOV 120-140 mm / Matrice 288×256 | FatSat | Tenosinovită a tendoanelor peroniere, tibial posterior, flexor lung al halucelui, ligament talofibular anterior (LTFA) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Poziționare strict neutră la 90° pentru a evita creșterea artificială de semnal pe tendoane datorită fenomenului 'Magic Angle' (55°)
    - Supresie omogenă de grăsime pe întregul volum al retropiciorului
    - Rezoluție spațială înaltă adaptată structurilor ligamentare fine

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening feromagnetic obligatoriu
    - Verificarea eventualelor materiale de osteosinteză la nivelul gleznei — utilizare secvențe de reducere a artefactelor metalice (WARP/MARS) dacă este necesar

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol standardizat OHSU MSK pentru diagnosticul precis al patologiei tendinoase, ligamentare și cartilaginoase de gleznă și retropicior.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
