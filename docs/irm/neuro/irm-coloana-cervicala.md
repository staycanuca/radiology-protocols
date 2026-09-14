---
author: Departamentul de Radiologie și Imagistică Medicală
category: neuro
clinical_indications:
- Cervicobrahialgie acută sau cronică rebelă la tratament
- Suspiciune de mielopatie cervicală (mers spastic, hiporeflexie/hiperreflexie, parestezii
  membre)
- Traumatism vertebro-medular cervical (evaluare ligamente, discuri și măduvă)
- Suspiciune de leziune demielinizantă medulară cervicală sau siringomielie
coils_hardware:
  coil: Antenă Head/Neck/Spine dedicată
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, gâtul în rectitudine anatomică, pernuță sub cap și
    genunchi flectați ușor pe suport.
contraindications:
- Contraindicații generale RM; materiale de osteosinteză feromagnetice nestabile.
contrast:
  agent: Nativ în mod obișnuit; se injectează Gd 0.1 mmol/kg în suspiciuni de tumori,
    infecții (spondilodiscită) sau plăci active demielinizante.
  dose: 0.1 mmol/kg (la indicație)
  flow_rate: 1.5 - 2.0 ml/s
  notes: Examinarea de rutină pentru discopatie degenerativă nu necesită substanță
    de contrast.
  timing: Achiziție T1 post-contrast cu FatSat în 2 planuri
iris_reference:
  chapter: Coloană Vertebrală - Segment Cervical
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Dacă se constată mielopatie cervicală compresivă, se măsoară diametrul antero-posterior
  al canalului spinal și gradul de stenoză.
patient_prep: Chestionar de securitate RM; pacientul este instruit să nu înghită în
  timpul rulării secvențelor sagitale pentru a evita artefactele de mișcare ale faringelui.
quality_criteria:
- Vizualizare clară de la joncțiunea cranio-cervicală (gaura occipitală) până la vertebra
  T2
- Banda de presaturație plasată anterior pe esofag/trahee pentru reducerea artefactelor
  de deglutiție
- Semnal LCR omogen fără artefacte majore de flux pulsatil
safety_considerations:
- 'Atenție la plăcuțele de titan cervicale anterioare: se utilizează secvențe TSE
  în loc de GRE pentru scăderea susceptibilității'
sequences:
- fat_sat: Nu
  fov_matrix: FOV 240 mm / 384x256
  name: Sagital T1 TSE
  notes: Morfologie corpi vertebrali, măduvă galbenă, aliniament
  plane: Sagital cervical (C1-T2)
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 550 ms / TE 10 ms
- fat_sat: Nu
  fov_matrix: FOV 240 mm / 384x288
  name: Sagital T2 TSE
  notes: Canal spinal, hipersemnal intramedular (mielomalacie / edem)
  plane: Sagital cervical
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 3500 ms / TE 100 ms
- fat_sat: STIR
  fov_matrix: FOV 240 mm / 320x224
  name: Sagital STIR / TIRM
  notes: Edem osos, fracturi, leziuni ligamentare posterioare
  plane: Sagital cervical
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 4000 ms / TE 50 ms / TI 160 ms
- fat_sat: Nu
  fov_matrix: FOV 180 mm / 320x256
  name: Axial T2* MEDIC / FFE / T2 TSE
  notes: Gaura de conjugare, foramen neural, uncoartroză, compresie radiculară
  plane: Axial înclinat pe spațiile discale (C3-C7)
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 700 ms / TE 15 ms / FA 25°
slug: irm-coloana-cervicala
title: IRM Coloană Cervicală
sources:
- title: OHSU Diagnostic Radiology — Brain & Spine MRI Protocols
  url: https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols
  institution: OHSU
  source_region: US
  kind: Protocol instituțional IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: f472cca210c17724389892b28b4ff21ac0d171c1731755f8540809a18a414746
- title: ACR-ASNR-SPR Practice Parameter for the Performance of Magnetic Resonance
    Imaging (MRI) of the Brain
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Brain.pdf
  institution: ACR / ASNR
  source_region: US
  kind: Standard de practică IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 05b5d22ee8b61e427ebdd5871542c5dee1f63a2932ca9179c569964f9b430a90
position: Decubit dorsal, gâtul în rectitudine anatomică, pernuță sub cap și genunchi
  flectați ușor pe suport.
---

# IRM Coloană Cervicală

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

        - Cervicobrahialgie acută sau cronică rebelă la tratament
        - Suspiciune de mielopatie cervicală (mers spastic, hiporeflexie/hiperreflexie, parestezii membre)
        - Traumatism vertebro-medular cervical (evaluare ligamente, discuri și măduvă)
        - Suspiciune de leziune demielinizantă medulară cervicală sau siringomielie

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM; materiale de osteosinteză feromagnetice nestabile.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Coloană Vertebrală - Segment Cervical*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Chestionar de securitate RM; pacientul este instruit să nu înghită în timpul rulării secvențelor sagitale pentru a evita artefactele de mișcare ale faringelui.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Head/Neck/Spine dedicată
    - **Poziție Pacient & Centrare:** Decubit dorsal, gâtul în rectitudine anatomică, pernuță sub cap și genunchi flectați ușor pe suport.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ în mod obișnuit; se injectează Gd 0.1 mmol/kg în suspiciuni de tumori, infecții (spondilodiscită) sau plăci active demielinizante.
    - **Doză Recomandată:** 0.1 mmol/kg (la indicație)
    - **Rată de Injectare (Debit):** 1.5 - 2.0 ml/s
    - **Temporizare & Faze Dinamice:** Achiziție T1 post-contrast cu FatSat în 2 planuri
    - **Filtrare Renală & Precauții:** Examinarea de rutină pentru discopatie degenerativă nu necesită substanță de contrast.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T1 TSE** | Sagital cervical (C1-T2) | TR 550 ms / TE 10 ms | 3.0 mm / gap 0.3 mm | FOV 240 mm / 384x256 | Nu | Morfologie corpi vertebrali, măduvă galbenă, aliniament |
    | **Sagital T2 TSE** | Sagital cervical | TR 3500 ms / TE 100 ms | 3.0 mm / gap 0.3 mm | FOV 240 mm / 384x288 | Nu | Canal spinal, hipersemnal intramedular (mielomalacie / edem) |
    | **Sagital STIR / TIRM** | Sagital cervical | TR 4000 ms / TE 50 ms / TI 160 ms | 3.0 mm / gap 0.3 mm | FOV 240 mm / 320x224 | STIR | Edem osos, fracturi, leziuni ligamentare posterioare |
    | **Axial T2* MEDIC / FFE / T2 TSE** | Axial înclinat pe spațiile discale (C3-C7) | TR 700 ms / TE 15 ms / FA 25° | 3.0 mm / gap 0.3 mm | FOV 180 mm / 320x256 | Nu | Gaura de conjugare, foramen neural, uncoartroză, compresie radiculară |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Vizualizare clară de la joncțiunea cranio-cervicală (gaura occipitală) până la vertebra T2
    - Banda de presaturație plasată anterior pe esofag/trahee pentru reducerea artefactelor de deglutiție
    - Semnal LCR omogen fără artefacte majore de flux pulsatil

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Atenție la plăcuțele de titan cervicale anterioare: se utilizează secvențe TSE în loc de GRE pentru scăderea susceptibilității

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Dacă se constată mielopatie cervicală compresivă, se măsoară diametrul antero-posterior al canalului spinal și gradul de stenoză.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [OHSU Diagnostic Radiology — Brain & Spine MRI Protocols](https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols) — *OHSU* (US)
- [ACR-ASNR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Brain](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Brain.pdf) — *ACR / ASNR* (US)
