---
author: Departamentul de Radiologie și Imagistică Medicală
category: msk
clinical_indications:
- Ruptură de coafă a rotatorilor (tendon supraspinos, infraspinos, subscapular)
- Sindrom de impingement / conflict subacromial
- Instabilitate gleno-humerală anterioară/posterioară (leziuni Bankart, Hill-Sachs)
- Leziuni de labrum superior (SLAP lesion) și tendon lung al bicepsului
- Capsulită retractilă ('umăr înghețat') sau osteonecroză aseptică cap humeral
coils_hardware:
  coil: Antenă dedicată de umăr 16 canale (Shoulder Coil mulată pe relief)
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, pacientul decalat ușor spre partea opusă pentru a aduce
    umărul cât mai aproape de izocentrul magnetului.
contraindications:
- Contraindicații generale de securitate RM.
contrast:
  agent: Nativ de regulă; Artro-IRM cu Gd diluat intra-articular (1:200 în ser) la
    sportivi tineri pentru leziuni de labrum și instabilitate glenohumerală.
  dose: Nativ sau 12-15 ml soluție diluată intra-articular
  flow_rate: Nu este cazul
  notes: Pentru patologia degenerativă a coafei la vârstnici, examinarea nativă este
    pe deplin suficientă.
  timing: Scanare în maxim 30-45 minute de la puncția intra-articulară
iris_reference:
  chapter: Sistem Musculoscheletal - Articulația Umărului
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Retracția tendonului supraspinos (stadiile Patte I-III) și degenerarea grasă
  musculară orientează decizia de reparare artroscopică.
patient_prep: Chestionar RM; brațul în rotație neutră lejeră de-a lungul corpului
  cu palma în sus (supinație ușoară); se evită rotația internă forțată care suprapune
  structurile coafei.
quality_criteria:
- Angulare precisă a planurilor coronale paralele cu corpul scapulei și fosa supraspinoasă
- Izocentrare optimă a articulației pentru eliminarea artefactelor de câmp la periferie
- Supresie spectrală excelentă a grăsimii pe întreaga arie periarticulară
safety_considerations:
- Verificare prezență ancore de sutură sau șuruburi de interferență post-operatorii
  (de regulă titan sau PEEK bioresorbabil - compatibile)
sequences:
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 160 mm / 320x256
  name: Coronal Oblic DP FatSat
  notes: Secvența cheie pentru tendonul supraspinos și joncțiunea miotendinoasă
  plane: Coronal paralel cu tendonul supraspinos
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2600 ms / TE 32 ms
- fat_sat: Nu
  fov_matrix: FOV 160 mm / 320x256
  name: Coronal Oblic T1 SE
  notes: Atrofie musculară (clasificare Goutallier), bursă subacromială
  plane: Coronal oblic
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 550 ms / TE 12 ms
- fat_sat: FatSat
  fov_matrix: FOV 160 mm / 320x256
  name: Sagital Oblic T2 FatSat
  notes: Forma acromionului (clasificare Bigliani), intervalul rotatorilor
  plane: Sagital perpendicular pe fosa glenoidă
  slice_gap: 3.5 mm / gap 0.3 mm
  tr_te: TR 3000 ms / TE 45 ms
- fat_sat: FatSat
  fov_matrix: FOV 160 mm / 320x256
  name: Axial DP FatSat
  notes: Tendon subscapular, tendonul capului lung al bicepsului, labrum anterior/posterior
  plane: Axial
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2800 ms / TE 30 ms
slug: irm-umar
title: IRM Umăr
---
# IRM Umăr

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

        - Ruptură de coafă a rotatorilor (tendon supraspinos, infraspinos, subscapular)
        - Sindrom de impingement / conflict subacromial
        - Instabilitate gleno-humerală anterioară/posterioară (leziuni Bankart, Hill-Sachs)
        - Leziuni de labrum superior (SLAP lesion) și tendon lung al bicepsului
        - Capsulită retractilă ('umăr înghețat') sau osteonecroză aseptică cap humeral

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale de securitate RM.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Sistem Musculoscheletal - Articulația Umărului*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Chestionar RM; brațul în rotație neutră lejeră de-a lungul corpului cu palma în sus (supinație ușoară); se evită rotația internă forțată care suprapune structurile coafei.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă dedicată de umăr 16 canale (Shoulder Coil mulată pe relief)
    - **Poziție Pacient & Centrare:** Decubit dorsal, pacientul decalat ușor spre partea opusă pentru a aduce umărul cât mai aproape de izocentrul magnetului.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ de regulă; Artro-IRM cu Gd diluat intra-articular (1:200 în ser) la sportivi tineri pentru leziuni de labrum și instabilitate glenohumerală.
    - **Doză Recomandată:** Nativ sau 12-15 ml soluție diluată intra-articular
    - **Rată de Injectare (Debit):** Nu este cazul
    - **Temporizare & Faze Dinamice:** Scanare în maxim 30-45 minute de la puncția intra-articulară
    - **Filtrare Renală & Precauții:** Pentru patologia degenerativă a coafei la vârstnici, examinarea nativă este pe deplin suficientă.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal Oblic DP FatSat** | Coronal paralel cu tendonul supraspinos | TR 2600 ms / TE 32 ms | 3.0 mm / gap 0.3 mm | FOV 160 mm / 320x256 | FatSat / SPAIR | Secvența cheie pentru tendonul supraspinos și joncțiunea miotendinoasă |
    | **Coronal Oblic T1 SE** | Coronal oblic | TR 550 ms / TE 12 ms | 3.0 mm / gap 0.3 mm | FOV 160 mm / 320x256 | Nu | Atrofie musculară (clasificare Goutallier), bursă subacromială |
    | **Sagital Oblic T2 FatSat** | Sagital perpendicular pe fosa glenoidă | TR 3000 ms / TE 45 ms | 3.5 mm / gap 0.3 mm | FOV 160 mm / 320x256 | FatSat | Forma acromionului (clasificare Bigliani), intervalul rotatorilor |
    | **Axial DP FatSat** | Axial | TR 2800 ms / TE 30 ms | 3.0 mm / gap 0.3 mm | FOV 160 mm / 320x256 | FatSat | Tendon subscapular, tendonul capului lung al bicepsului, labrum anterior/posterior |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Angulare precisă a planurilor coronale paralele cu corpul scapulei și fosa supraspinoasă
    - Izocentrare optimă a articulației pentru eliminarea artefactelor de câmp la periferie
    - Supresie spectrală excelentă a grăsimii pe întreaga arie periarticulară

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Verificare prezență ancore de sutură sau șuruburi de interferență post-operatorii (de regulă titan sau PEEK bioresorbabil - compatibile)

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Retracția tendonului supraspinos (stadiile Patte I-III) și degenerarea grasă musculară orientează decizia de reparare artroscopică.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
