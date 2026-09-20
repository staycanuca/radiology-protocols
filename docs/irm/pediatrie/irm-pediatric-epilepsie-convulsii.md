---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Crize convulsive cu debut recent sau epilepsie refractară la tratament medicamentos
- Suspiciune de displazie corticală focală (FCD) sau anomalie de migrare neuronală
- Scleroză mezială temporală / hipocampică
- Evaluare prechirurgicală a epilepsiei rezistente la copil
- Convulsii febrile atipice sau prelungite
coils_hardware:
  coil: Antenă Head/Neck de înaltă densitate (32 sau 64 canale)
  field_strength: 3.0 Tesla (preferat) sau 1.5 Tesla
  positioning: Decubit dorsal, aliniere anatomică riguroasă, fixare cap cu suporturi
    speciale
contraindications:
- Dispozitive medicale implantate non-MR Conditional
- Claustrofobie severă sau agitație extremă necontrolată
contrast:
  agent: Nativ (contrastul nu este indicat de rutină în epilepsie fără suspiciune
    tumorală)
  dose: N/A
  flow_rate: N/A
  notes: Contrastul se administrează doar dacă se identifică leziuni focale suspecte
    de natură tumorală sau infecțioasă.
  timing: N/A
iris_reference:
  chapter: Pediatrie - Sistem Nervos Central
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol optimizat conform ghidurilor WFPI și ILAE pentru detecția focarelor
  epileptogene subtile la copil.
patient_prep: Pregătire atentă a copilului; la pacienții sub 2 ani se ajustează parametrii
  de mielinizare; pentru examinări de înaltă rezoluție se recomandă tehnici 'feed-and-wrap'
  sau sedare dacă este strict necesară.
quality_criteria:
- Rezoluție sub-milimetrică pe secvența 3D T1 cu contrast optim substanță albă / substanță
  cenușie
- Orientare precisă a planului coronal perpendicular pe axul hipocampilor
- Absența artefactelor de mișcare la nivelul lobilor temporali
safety_considerations:
- La 3.0T se monitorizează atent SAR-ul din cauza secvențelor FSE/FLAIR lungi
- Protecție acustică dublă adaptată vârstei
sequences:
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 220 mm / 192x192
  name: Axial DWI (b=0, b=1000) + hartă ADC
  notes: Excludere edem citotoxic post-critic, leziuni ischemice recente (1-2 min)
  plane: Axial
  slice_gap: 3.0-4.0 mm / gap 0.4 mm
  tr_te: TR 3500 ms / TE 70 ms
- fat_sat: Nu
  fov_matrix: FOV 240 mm / 256x256
  name: 3D T1WI Izotrop Sagital (MPRAGE / BRAVO)
  notes: Grosime corticală, joncțiune substanță albă/cenușie, reformate multiplanare
    fine (5-7 min)
  plane: Sagital 3D Izotrop
  slice_gap: 1.0 mm izotrop (fără gap)
  tr_te: TR 1900-2300 ms / TE 2.5-3.0 ms / TI 900 ms
- fat_sat: Nu
  fov_matrix: FOV 220 mm / 384x288
  name: Axial T2WI TSE
  notes: Diferențiere structurală lobară, heterotopii nodulare (3-5 min)
  plane: Axial
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 4000-5000 ms / TE 100 ms
- fat_sat: Nu
  fov_matrix: FOV 180-200 mm / 320x256
  name: Coronal T2WI Oblic (perpendicular pe axul hipocampilor)
  notes: Orientat strict perpendicular pe axul lung al hipocampilor; volumetrie și
    semnal hipocampic (3-4 min)
  plane: Coronal Oblic
  slice_gap: 2.0-3.0 mm / gap 0.3 mm
  tr_te: TR 4000-5000 ms / TE 100-110 ms
- fat_sat: Nu
  fov_matrix: FOV 220 mm / 256x256
  name: Axial EPI / T2* GRE / SWI
  notes: Detecție cavernoame, calcificări (tuberoză scleroasă, Sturge-Weber) (2 min)
  plane: Axial
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 600-800 ms / TE 20 ms
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 256x256
  name: 3D FLAIR Axial (Opțional, recomandat la > 2 ani)
  notes: Hipersemnal discret în displaziile corticale focale și scleroza hipocampică
    (4-5 min)
  plane: Axial 3D
  slice_gap: 1.0-1.2 mm izotrop
  tr_te: TR 8000 ms / TE 100 ms / TI 2400 ms
slug: irm-pediatric-epilepsie-convulsii
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
title: RM Pediatric — Protocol Convulsii & Epilepsie (Seizure Brain)
---
# RM Pediatric — Protocol Convulsii & Epilepsie (Seizure Brain)

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

        - Crize convulsive cu debut recent sau epilepsie refractară la tratament medicamentos
        - Suspiciune de displazie corticală focală (FCD) sau anomalie de migrare neuronală
        - Scleroză mezială temporală / hipocampică
        - Evaluare prechirurgicală a epilepsiei rezistente la copil
        - Convulsii febrile atipice sau prelungite

    === "Contraindicații & Screening Metalic"

        - Dispozitive medicale implantate non-MR Conditional
        - Claustrofobie severă sau agitație extremă necontrolată

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Sistem Nervos Central*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Pregătire atentă a copilului; la pacienții sub 2 ani se ajustează parametrii de mielinizare; pentru examinări de înaltă rezoluție se recomandă tehnici 'feed-and-wrap' sau sedare dacă este strict necesară.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 3.0 Tesla (preferat) sau 1.5 Tesla
    - **Antenă de Recepție (Coil):** Antenă Head/Neck de înaltă densitate (32 sau 64 canale)
    - **Poziție Pacient & Centrare:** Decubit dorsal, aliniere anatomică riguroasă, fixare cap cu suporturi speciale

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ (contrastul nu este indicat de rutină în epilepsie fără suspiciune tumorală)
    - **Doză Recomandată:** N/A
    - **Rată de Injectare (Debit):** N/A
    - **Temporizare & Faze Dinamice:** N/A
    - **Filtrare Renală & Precauții:** Contrastul se administrează doar dacă se identifică leziuni focale suspecte de natură tumorală sau infecțioasă.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Axial DWI (b=0, b=1000) + hartă ADC** | Axial | TR 3500 ms / TE 70 ms | 3.0-4.0 mm / gap 0.4 mm | FOV 220 mm / 192x192 | FatSat (EPI) | Excludere edem citotoxic post-critic, leziuni ischemice recente (1-2 min) |
    | **3D T1WI Izotrop Sagital (MPRAGE / BRAVO)** | Sagital 3D Izotrop | TR 1900-2300 ms / TE 2.5-3.0 ms / TI 900 ms | 1.0 mm izotrop (fără gap) | FOV 240 mm / 256x256 | Nu | Grosime corticală, joncțiune substanță albă/cenușie, reformate multiplanare fine (5-7 min) |
    | **Axial T2WI TSE** | Axial | TR 4000-5000 ms / TE 100 ms | 3.0 mm / gap 0.3 mm | FOV 220 mm / 384x288 | Nu | Diferențiere structurală lobară, heterotopii nodulare (3-5 min) |
    | **Coronal T2WI Oblic (perpendicular pe axul hipocampilor)** | Coronal Oblic | TR 4000-5000 ms / TE 100-110 ms | 2.0-3.0 mm / gap 0.3 mm | FOV 180-200 mm / 320x256 | Nu | Orientat strict perpendicular pe axul lung al hipocampilor; volumetrie și semnal hipocampic (3-4 min) |
    | **Axial EPI / T2* GRE / SWI** | Axial | TR 600-800 ms / TE 20 ms | 3.0 mm / gap 0.3 mm | FOV 220 mm / 256x256 | Nu | Detecție cavernoame, calcificări (tuberoză scleroasă, Sturge-Weber) (2 min) |
    | **3D FLAIR Axial (Opțional, recomandat la > 2 ani)** | Axial 3D | TR 8000 ms / TE 100 ms / TI 2400 ms | 1.0-1.2 mm izotrop | FOV 230 mm / 256x256 | Nu | Hipersemnal discret în displaziile corticale focale și scleroza hipocampică (4-5 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Rezoluție sub-milimetrică pe secvența 3D T1 cu contrast optim substanță albă / substanță cenușie
    - Orientare precisă a planului coronal perpendicular pe axul hipocampilor
    - Absența artefactelor de mișcare la nivelul lobilor temporali

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - La 3.0T se monitorizează atent SAR-ul din cauza secvențelor FSE/FLAIR lungi
    - Protecție acustică dublă adaptată vârstei

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol optimizat conform ghidurilor WFPI și ILAE pentru detecția focarelor epileptogene subtile la copil.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
