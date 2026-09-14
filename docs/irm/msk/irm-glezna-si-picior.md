---
author: Departamentul de Radiologie și Imagistică Medicală
category: msk
clinical_indications:
- Leziuni ligamentare după entorse severe (LFTA, LFC, ligament deltoid, sindesmoză
  tibio-fibulară)
- Tendinopatii și rupturi (tendon achilian, tendon tibial posterior, tendoane peroniere)
- Leziuni osteocondrale ale domului talar
- Sindrom de impingement de gleznă (anterior / posterior - os trigonum)
- Fasciită plantară, neurom Morton sau fracturi de stres metatarsiene
coils_hardware:
  coil: Antenă dedicată de picior/gleznă 16 canale (Foot/Ankle Coil)
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal cu picioarele înainte, piciorul afectat în unghi drept
    (90°).
contraindications:
- Contraindicații generale RM.
contrast:
  agent: Nativ de regulă; contrast doar în caz de suspiciune de osteomielită, sinovită
    inflamatorie sau tumori de părți moi.
  dose: Fără contrast de rutină
  flow_rate: Nu este cazul
  notes: Nu se administrează contrast de rutină.
  timing: Nu este cazul
iris_reference:
  chapter: Sistem Musculoscheletal - Gleznă și Picior
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Leziunile ligamentului talo-fibular anterior (LFTA) se analizează excelent
  pe planul axial și coronal oblic ușor înclinat la 20°.
patient_prep: Chestionar RM; piciorul fixat la 90° flexie dorsală în antenă cu pernuțe
  de spumă pentru a evita tensionarea tendoanelor și relaxarea ligamentelor.
quality_criteria:
- Menținerea strictă a unghiului de 90° fără inversie sau eversie pe durata scanării
- Absența artefactului de 'unghi magic' (magic angle artifact la 55°) pe tendoanele
  peroniere prin calibrarea TE > 30 ms
safety_considerations:
- SAR scăzut pe extremitate periferică
sequences:
- fat_sat: Nu
  fov_matrix: FOV 150 mm / 320x256
  name: Sagital T1 SE
  notes: Morfologie tendon achilian, aponevroză plantară, unghi talo-navicular
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 550 ms / TE 12 ms
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 150 mm / 320x256
  name: Sagital DP FatSat
  notes: Rupturi tendinoase, bursită retrocalcaneană, edem dom talar
  plane: Sagital
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2800 ms / TE 30 ms
- fat_sat: FatSat
  fov_matrix: FOV 140 mm / 320x256
  name: Coronal DP FatSat
  notes: Cartilaj dom talar, ligament deltoid și ligament calcaneo-fibular
  plane: Coronal (paralel cu linia bimaleolară)
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 2800 ms / TE 30 ms
- fat_sat: FatSat
  fov_matrix: FOV 140 mm / 320x256
  name: Axial T2 TSE FatSat
  notes: Tendoane retromaleolare (tibial posterior, flexor lung, peroniere în culise)
  plane: Axial (perpendicular pe tibie)
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 3500 ms / TE 65 ms
slug: irm-glezna-si-picior
title: IRM Gleznă & Picior
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
position: Decubit dorsal cu picioarele înainte, piciorul afectat în unghi drept (90°).
---

# IRM Gleznă & Picior

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

        - Leziuni ligamentare după entorse severe (LFTA, LFC, ligament deltoid, sindesmoză tibio-fibulară)
        - Tendinopatii și rupturi (tendon achilian, tendon tibial posterior, tendoane peroniere)
        - Leziuni osteocondrale ale domului talar
        - Sindrom de impingement de gleznă (anterior / posterior - os trigonum)
        - Fasciită plantară, neurom Morton sau fracturi de stres metatarsiene

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Sistem Musculoscheletal - Gleznă și Picior*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Chestionar RM; piciorul fixat la 90° flexie dorsală în antenă cu pernuțe de spumă pentru a evita tensionarea tendoanelor și relaxarea ligamentelor.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă dedicată de picior/gleznă 16 canale (Foot/Ankle Coil)
    - **Poziție Pacient & Centrare:** Decubit dorsal cu picioarele înainte, piciorul afectat în unghi drept (90°).

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ de regulă; contrast doar în caz de suspiciune de osteomielită, sinovită inflamatorie sau tumori de părți moi.
    - **Doză Recomandată:** Fără contrast de rutină
    - **Rată de Injectare (Debit):** Nu este cazul
    - **Temporizare & Faze Dinamice:** Nu este cazul
    - **Filtrare Renală & Precauții:** Nu se administrează contrast de rutină.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T1 SE** | Sagital | TR 550 ms / TE 12 ms | 3.0 mm / gap 0.3 mm | FOV 150 mm / 320x256 | Nu | Morfologie tendon achilian, aponevroză plantară, unghi talo-navicular |
    | **Sagital DP FatSat** | Sagital | TR 2800 ms / TE 30 ms | 3.0 mm / gap 0.3 mm | FOV 150 mm / 320x256 | FatSat / SPAIR | Rupturi tendinoase, bursită retrocalcaneană, edem dom talar |
    | **Coronal DP FatSat** | Coronal (paralel cu linia bimaleolară) | TR 2800 ms / TE 30 ms | 3.0 mm / gap 0.3 mm | FOV 140 mm / 320x256 | FatSat | Cartilaj dom talar, ligament deltoid și ligament calcaneo-fibular |
    | **Axial T2 TSE FatSat** | Axial (perpendicular pe tibie) | TR 3500 ms / TE 65 ms | 3.0 mm / gap 0.3 mm | FOV 140 mm / 320x256 | FatSat | Tendoane retromaleolare (tibial posterior, flexor lung, peroniere în culise) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Menținerea strictă a unghiului de 90° fără inversie sau eversie pe durata scanării
    - Absența artefactului de 'unghi magic' (magic angle artifact la 55°) pe tendoanele peroniere prin calibrarea TE > 30 ms

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR scăzut pe extremitate periferică

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Leziunile ligamentului talo-fibular anterior (LFTA) se analizează excelent pe planul axial și coronal oblic ușor înclinat la 20°.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [OHSU Diagnostic Radiology — Musculoskeletal MRI Protocols](https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols) — *OHSU* (US)
- [ACR-SSR Practice Parameter for the Performance of Musculoskeletal Magnetic Resonance Imaging](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Musculoskeletal.pdf) — *ACR / SSR* (US)
