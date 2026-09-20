---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Suspiciune sau monitorizare de anevrism cerebral intracranian
- Stenoze sau ocluzii carotidiene, vertebrale sau ale arterelor cerebrale majore
- Suspiciune de disecție arterială cervico-cerebrală
- Malformații arterio-venoase (MAV) sau fistule durale
- Tromboză venoasă cerebrală (MRV asociat)
coils_hardware:
  coil: Antenă dedicată Head/Neck multicanal (16–32 canale)
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, cap centrat în izocentru, imobilizare cu pernuțe laterale
contraindications:
- Clipurilor anevrismale feromagnetice non-MR Conditional
- Implanturi active incompatibile (pacemaker vechi, neurostimulatoare non-compatibile)
contrast:
  agent: Gadoliniu macrociclic (Gadobutrol / Gadoterat de meglumină)
  dose: 0.1 mmol/kg (standard)
  flow_rate: 1.5 - 2.0 mL/s urmat de flush salin 20 mL
  notes: Secvența 3D TOF este nativă; achiziția 3D CE-MRA este sincronizată cu contrastul.
  timing: Bolus tracking dinamic la nivelul bifurcației carotidiene / crosei aortice
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol standard OHSU de neuroradiologie pentru caracterizarea non-invazivă
  a sistemului arterial cerebral.
patient_prep: Screening complet de securitate RM conform politicii OHSU. Căști fonoizolante.
quality_criteria:
- Reconstrucții MIP rotite în trepte de 15° pe axul stânga-dreapta și antero-posterior
- Vizualizare clară a ramurilor arteriale A1, A2, M1, M2, P1, P2 și a arterei comunicante
  anterioare/posterioare
- Absența artefactelor majore de mișcare sau turbulență la bifurcația carotidiană
safety_considerations:
- Screening riguros feromagnetic Zonele III/IV conform politicii OHSU
- Verificare implanturi (stenturi, clipuri anevrismale) — documentație MR Conditional
  obligatorie
- Limită SAR < 2.0 W/kg în modul normal de operare
sequences:
- fat_sat: Nu (TOW fat suppression opțional)
  fov_matrix: FOV 200 mm / Matrice 320×256
  name: 3D TOF MRA Arterial (Fără contrast)
  notes: Achiziție nativă de înaltă rezoluție a poligonului lui Willis; reconstrucții
    MIP rotate la 360°
  plane: Axial / 3D Volumetric
  slice_gap: 0.8 - 1.0 mm (izotrop)
  tr_te: TR 20-25 ms / TE 3.0-4.0 ms / Flip angle 18-20°
- fat_sat: Nu
  fov_matrix: FOV 240 mm / Matrice 256×256
  name: Axial 3D T1 MPRAGE Nativ
  notes: Referință anatomică cerebrală și detectare hematoame intramurale (disecție)
  plane: Sagital / Reconstrucție 3-plane
  slice_gap: 1.0 mm izotrop
  tr_te: TR 1900-2300 ms / TE 2.5-3.5 ms / TI 900 ms
- fat_sat: Nu
  fov_matrix: FOV 300-350 mm / Matrice 384×384
  name: 3D CE-MRA Dinamic Post-Contrast
  notes: Acoperire de la arcul aortic până la vertex; bolus tracking pe arterele vertebrale/carotide
  plane: Coronal / 3D Volumetric
  slice_gap: 0.9 - 1.0 mm
  tr_te: TR 3.5-4.5 ms / TE 1.2-1.6 ms
- fat_sat: Nu
  fov_matrix: FOV 220 mm / Matrice 320×256
  name: Axial T2 TSE / FSE
  notes: Evaluare parenchim cerebral adiacent și absența fluxului (flow void)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 4000 ms / TE 100 ms
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 220 mm / Matrice 128×128
  name: Axial DWI (b=0, b=1000) + hartă ADC
  notes: Excludere ischemie acută / microembolii cerebrale
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3500 ms / TE 70 ms
title: RM Angiografie Cerebrală MRA 3D TOF & Contrast (Protocol OHSU)
---
# RM Angiografie Cerebrală MRA 3D TOF & Contrast (Protocol OHSU)

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

        - Suspiciune sau monitorizare de anevrism cerebral intracranian
        - Stenoze sau ocluzii carotidiene, vertebrale sau ale arterelor cerebrale majore
        - Suspiciune de disecție arterială cervico-cerebrală
        - Malformații arterio-venoase (MAV) sau fistule durale
        - Tromboză venoasă cerebrală (MRV asociat)

    === "Contraindicații & Screening Metalic"

        - Clipurilor anevrismale feromagnetice non-MR Conditional
        - Implanturi active incompatibile (pacemaker vechi, neurostimulatoare non-compatibile)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cap, Gât & Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Screening complet de securitate RM conform politicii OHSU. Căști fonoizolante.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată Head/Neck multicanal (16–32 canale)
    - **Poziție Pacient & Centrare:** Decubit dorsal, cap centrat în izocentru, imobilizare cu pernuțe laterale

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic (Gadobutrol / Gadoterat de meglumină)
    - **Doză Recomandată:** 0.1 mmol/kg (standard)
    - **Rată de Injectare (Debit):** 1.5 - 2.0 mL/s urmat de flush salin 20 mL
    - **Temporizare & Faze Dinamice:** Bolus tracking dinamic la nivelul bifurcației carotidiene / crosei aortice
    - **Filtrare Renală & Precauții:** Secvența 3D TOF este nativă; achiziția 3D CE-MRA este sincronizată cu contrastul.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **3D TOF MRA Arterial (Fără contrast)** | Axial / 3D Volumetric | TR 20-25 ms / TE 3.0-4.0 ms / Flip angle 18-20° | 0.8 - 1.0 mm (izotrop) | FOV 200 mm / Matrice 320×256 | Nu (TOW fat suppression opțional) | Achiziție nativă de înaltă rezoluție a poligonului lui Willis; reconstrucții MIP rotate la 360° |
    | **Axial 3D T1 MPRAGE Nativ** | Sagital / Reconstrucție 3-plane | TR 1900-2300 ms / TE 2.5-3.5 ms / TI 900 ms | 1.0 mm izotrop | FOV 240 mm / Matrice 256×256 | Nu | Referință anatomică cerebrală și detectare hematoame intramurale (disecție) |
    | **3D CE-MRA Dinamic Post-Contrast** | Coronal / 3D Volumetric | TR 3.5-4.5 ms / TE 1.2-1.6 ms | 0.9 - 1.0 mm | FOV 300-350 mm / Matrice 384×384 | Nu | Acoperire de la arcul aortic până la vertex; bolus tracking pe arterele vertebrale/carotide |
    | **Axial T2 TSE / FSE** | Axial | TR 4000 ms / TE 100 ms | 4.0 mm / gap 0.4 mm | FOV 220 mm / Matrice 320×256 | Nu | Evaluare parenchim cerebral adiacent și absența fluxului (flow void) |
    | **Axial DWI (b=0, b=1000) + hartă ADC** | Axial | TR 3500 ms / TE 70 ms | 4.0 mm / gap 0.4 mm | FOV 220 mm / Matrice 128×128 | FatSat (EPI) | Excludere ischemie acută / microembolii cerebrale |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Reconstrucții MIP rotite în trepte de 15° pe axul stânga-dreapta și antero-posterior
    - Vizualizare clară a ramurilor arteriale A1, A2, M1, M2, P1, P2 și a arterei comunicante anterioare/posterioare
    - Absența artefactelor majore de mișcare sau turbulență la bifurcația carotidiană

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening riguros feromagnetic Zonele III/IV conform politicii OHSU
    - Verificare implanturi (stenturi, clipuri anevrismale) — documentație MR Conditional obligatorie
    - Limită SAR < 2.0 W/kg în modul normal de operare

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol standard OHSU de neuroradiologie pentru caracterizarea non-invazivă a sistemului arterial cerebral.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
