---
author: Departamentul de Radiologie și Imagistică Medicală
category: msk
clinical_indications:
- Leziuni traumatice meniscale (fisure, rupturi în toartă de coș)
- Ruptură de ligament încrucișat anterior (LIA) sau posterior (LIP)
- Leziuni de ligamente colaterale (LCM, LCL) și ale unghiului postero-lateral
- Leziuni osteocondrale, osteocondrită disecantă, corpi liberi intra-articulari
- Dureri anterioare de genunchi, patologie rotuliană (condromalacie, instabilitate)
coils_hardware:
  coil: Antenă dedicată de genunchi 16 sau 18 canale (Transceive/Receive)
  field_strength: 1.5T sau 3.0T (3T excelent pentru cartografierea cartilajului)
  positioning: Decubit dorsal cu picioarele înainte, genunchiul fixat rigid în antenă
    cu perne de spumă.
contraindications:
- Contraindicații generale RM; materiale de sinteză metalice necompatibile.
contrast:
  agent: Nativ în 95% din cazuri; substanță de contrast IV doar în suspiciuni de sinovită
    proliferativă (artrită reumatoidă, PVNS) sau tumori.
  dose: Fără contrast de rutină
  flow_rate: Nu este cazul
  notes: Artro-IRM cu contrast intra-articular este rezervată cazurilor de evaluare
    a meniscului operat (re-ruptură meniscală).
  timing: Nu este cazul
iris_reference:
  chapter: Sistem Musculoscheletal - Articulația Genunchiului
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Semnul 'kissing contusion' (edem pe condilul femural lateral și platoul tibial
  postero-lateral) indică cu specificitate înaltă ruptura acută de LIA.
patient_prep: Chestionar RM; genunchiul în extensie lejeră cu rotație externă de 5°
  pentru alinierea ligamentului încrucișat anterior în plan sagital.
quality_criteria:
- Supresie de grăsime uniformă și omogenă pe întregul FOV de 15 cm
- Vizualizarea continuă a traiectului LIA pe secvențele sagitale
- Absența artefactelor de mișcare (pacientul trebuie să mențină piciorul complet relaxat)
safety_considerations:
- Antena dedicată reduce substanțial puterea necesară și SAR-ul total
sequences:
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 150 mm / 320x256
  name: Sagital DP FatSat (Densitate de Protoni cu supresie de grăsime)
  notes: Evaluare primară LIA, LIP, coarne meniscale, edem osos contuzional
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2800 ms / TE 30 ms
- fat_sat: Nu
  fov_matrix: FOV 150 mm / 320x256
  name: Sagital T1 SE
  notes: Anatomie meniscală, cartilaj articular, măduvă osoasă
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 550 ms / TE 12 ms
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 150 mm / 320x256
  name: Coronal DP FatSat
  notes: Corpuri meniscale, ligamente colaterale (LCM, LCL), platou tibial
  plane: Coronal
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2800 ms / TE 30 ms
- fat_sat: Nu
  fov_matrix: FOV 150 mm / 320x256
  name: Coronal T1 SE
  notes: Anatomie ligamentară colaterală și evaluare corticală
  plane: Coronal
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 550 ms / TE 12 ms
- fat_sat: FatSat
  fov_matrix: FOV 150 mm / 320x256
  name: Axial DP FatSat
  notes: Cartilaj femuro-patelar, retinacule patelare, tendon rotulian și cvadricipital
  plane: Axial
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2800 ms / TE 30 ms
slug: irm-genunchi
title: IRM Genunchi
sources:
- title: OHSU Diagnostic Radiology — Musculoskeletal MRI Protocols
  url: https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols
  institution: OHSU
  source_region: US
  kind: Protocol instituțional IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: f472cca210c17724389892b28b4ff21ac0d171c1731755f8540809a18a414746
- title: ACR-SSR Practice Parameter for the Performance of Musculoskeletal Magnetic
    Resonance Imaging
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Musculoskeletal.pdf
  institution: ACR / SSR
  source_region: US
  kind: Standard de practică IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 4234ca9d7210e58f3bd8273bbf42d9d235105c2df0d73ff341522727f8fe9893
position: Decubit dorsal cu picioarele înainte, genunchiul fixat rigid în antenă cu
  perne de spumă.
---

# IRM Genunchi

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

        - Leziuni traumatice meniscale (fisure, rupturi în toartă de coș)
        - Ruptură de ligament încrucișat anterior (LIA) sau posterior (LIP)
        - Leziuni de ligamente colaterale (LCM, LCL) și ale unghiului postero-lateral
        - Leziuni osteocondrale, osteocondrită disecantă, corpi liberi intra-articulari
        - Dureri anterioare de genunchi, patologie rotuliană (condromalacie, instabilitate)

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM; materiale de sinteză metalice necompatibile.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Sistem Musculoscheletal - Articulația Genunchiului*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Chestionar RM; genunchiul în extensie lejeră cu rotație externă de 5° pentru alinierea ligamentului încrucișat anterior în plan sagital.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T (3T excelent pentru cartografierea cartilajului)
    - **Antenă de Recepție (Coil):** Antenă dedicată de genunchi 16 sau 18 canale (Transceive/Receive)
    - **Poziție Pacient & Centrare:** Decubit dorsal cu picioarele înainte, genunchiul fixat rigid în antenă cu perne de spumă.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ în 95% din cazuri; substanță de contrast IV doar în suspiciuni de sinovită proliferativă (artrită reumatoidă, PVNS) sau tumori.
    - **Doză Recomandată:** Fără contrast de rutină
    - **Rată de Injectare (Debit):** Nu este cazul
    - **Temporizare & Faze Dinamice:** Nu este cazul
    - **Filtrare Renală & Precauții:** Artro-IRM cu contrast intra-articular este rezervată cazurilor de evaluare a meniscului operat (re-ruptură meniscală).

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital DP FatSat (Densitate de Protoni cu supresie de grăsime)** | Sagital | TR 2800 ms / TE 30 ms | 3.0 mm / gap 0.3 mm | FOV 150 mm / 320x256 | FatSat / SPAIR | Evaluare primară LIA, LIP, coarne meniscale, edem osos contuzional |
    | **Sagital T1 SE** | Sagital | TR 550 ms / TE 12 ms | 3.0 mm / gap 0.3 mm | FOV 150 mm / 320x256 | Nu | Anatomie meniscală, cartilaj articular, măduvă osoasă |
    | **Coronal DP FatSat** | Coronal | TR 2800 ms / TE 30 ms | 3.0 mm / gap 0.3 mm | FOV 150 mm / 320x256 | FatSat / SPAIR | Corpuri meniscale, ligamente colaterale (LCM, LCL), platou tibial |
    | **Coronal T1 SE** | Coronal | TR 550 ms / TE 12 ms | 3.0 mm / gap 0.3 mm | FOV 150 mm / 320x256 | Nu | Anatomie ligamentară colaterală și evaluare corticală |
    | **Axial DP FatSat** | Axial | TR 2800 ms / TE 30 ms | 3.0 mm / gap 0.3 mm | FOV 150 mm / 320x256 | FatSat | Cartilaj femuro-patelar, retinacule patelare, tendon rotulian și cvadricipital |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Supresie de grăsime uniformă și omogenă pe întregul FOV de 15 cm
    - Vizualizarea continuă a traiectului LIA pe secvențele sagitale
    - Absența artefactelor de mișcare (pacientul trebuie să mențină piciorul complet relaxat)

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Antena dedicată reduce substanțial puterea necesară și SAR-ul total

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Semnul 'kissing contusion' (edem pe condilul femural lateral și platoul tibial postero-lateral) indică cu specificitate înaltă ruptura acută de LIA.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [OHSU Diagnostic Radiology — Musculoskeletal MRI Protocols](https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols) — *OHSU* (US)
- [ACR-SSR Practice Parameter for the Performance of Musculoskeletal Magnetic Resonance Imaging](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Musculoskeletal.pdf) — *ACR / SSR* (US)
