---
author: Departamentul de Radiologie și Imagistică Medicală
category: abdomen-pelvis
clinical_indications:
- Evaluare inițială și monitorizare activitate inflamatorie în Boala Crohn
- Detecție complicații transmurale (stenoze fibroase vs. inflamatorii, fistule entero-enterice/cutanate,
  abcese mezenterice)
- Evaluare răspuns terapeutic la medicație biologică anti-TNF
- Urmărire la tineri și copii fără expunere la radiații ionizante
coils_hardware:
  coil: Antenă Phased-Array Abdomen-Pelvis combinată (acoperire de la diafragm la
    simfiza pubiană)
  field_strength: 1.5T (preferabil pentru mai puține artefacte de susceptibilitate
    gazoasă) sau 3.0T
  positioning: Decubit ventral (prone) preferat deoarece reduce grosimea abdomenului
    și separă ansele ileale, sau decubit dorsal dacă nu este tolerat.
contraindications:
- Ocluzie intestinală completă acută; contraindicații generale RM.
contrast:
  agent: Chelat de Gadoliniu macrociclic IV
  dose: 0.1 - 0.15 mmol/kg corp
  flow_rate: 2.0 - 2.5 ml/s injectare automată + 30 ml ser fiziologic
  notes: Îngroșarea parietală > 3 mm cu hipercaptare stratificată mucoasă/submucoasă
    și edem T2 indică inflamație acută activă.
  timing: Secvențe 3D T1 cu FatSat la 45s (arterial enteric), 70s (portal) și 180s
    (tardiv)
iris_reference:
  chapter: Tub Digestiv - Boală Crohn și Boli Inflamatorii
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Permite diferențierea precisă între stenoza inflamatorie activă (edem T2, difuzie
  restricționată, captare intensă) ce răspunde la terapie medicamentoasă și stenoza
  fibroasă cicatricială ce necesită rezecție chirurgicală sau dilatare.
patient_prep: À jeun 6 ore; ingestie fracționată de 1000-1500 ml soluție hiperosmolară
  non-absorbabilă (PEG - polietilenglicol sau Manitol 2.5%) în decurs de 45-60 minute
  înainte de scanare pentru distensia uniformă a anselor de intestin subțire; administrare
  IV de antispastic (Butilscopolamină / Buscopan 20 mg sau Glucagon 1 mg) imediat
  înainte de secvențe.
quality_criteria:
- Distensie luminală adecvată a anselor jejunale și a ileonului terminal (> 2-2.5
  cm calibru)
- Absența artefactelor de peristaltică prin administrarea promptă a antispasticului
- Acoperire anatomică completă de la unghiul Treitz până la ampula rectală
safety_considerations:
- Buscopan este contraindicat la pacienți cu glaucom cu unghi îngust, hipertrofie
  de prostată cu retenție de urină sau tahiaritmii severe (se poate folosi Glucagon)
sequences:
- fat_sat: Nu
  fov_matrix: FOV 420 mm / 384x256
  name: Coronal T2 HASTE / SSFSE Free-breathing
  notes: Evaluare distensie luminală pe tot cadrul jejuno-ileal
  plane: Coronal abdomen-pelvis
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: Single-shot / TE 90 ms
- fat_sat: FatSat
  fov_matrix: FOV 420 mm / 320x256
  name: Coronal T2 cu supresie de grăsime (FatSat / SPAIR)
  notes: Edem parietal în strat submucos, lichid liber, colecții peridigestive
  plane: Coronal
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: Single-shot / TE 90 ms
- fat_sat: Nu
  fov_matrix: FOV 350 mm / 256x256
  name: Axial T2 HASTE / TrueFISP cine-motilitate
  notes: 'Apreciere peristaltică: stenozele rigide lipsite de motilitate'
  plane: Axial pe ansele afectate (ileon terminal)
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 3.5 ms / TE 1.5 ms
- fat_sat: FatSat
  fov_matrix: FOV 380 mm / 192x160
  name: Axial & Coronal DWI (b=0, 600, 900) + ADC
  notes: Restricție de difuzie corelată direct cu scorul endoscopic de inflamație
  plane: Axial și Coronal
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 4500 ms / TE 65 ms
- fat_sat: Dixon / FatSat
  fov_matrix: FOV 400 mm / 320x256
  name: 3D T1 GRE Dinamic multipfazic post-Gd
  notes: Priză de contrast parietală, semnul pieptenului (comb sign - vase vasa recta
    dilatate)
  plane: Coronal și Axial
  slice_gap: 2.5 mm interpolat la 1.2 mm
  tr_te: TR 3.8 ms / TE 1.6 ms
slug: entero-irm
title: Entero-IRM (Protocol Boală Inflamatorie Intestinală - Crohn)
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
position: Decubit ventral (prone) preferat deoarece reduce grosimea abdomenului și
  separă ansele ileale, sau decubit dorsal dacă nu este tolerat.
---

# Entero-IRM (Protocol Boală Inflamatorie Intestinală - Crohn)

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

        - Evaluare inițială și monitorizare activitate inflamatorie în Boala Crohn
        - Detecție complicații transmurale (stenoze fibroase vs. inflamatorii, fistule entero-enterice/cutanate, abcese mezenterice)
        - Evaluare răspuns terapeutic la medicație biologică anti-TNF
        - Urmărire la tineri și copii fără expunere la radiații ionizante

    === "Contraindicații & Screening Metalic"

        - Ocluzie intestinală completă acută; contraindicații generale RM.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Tub Digestiv - Boală Crohn și Boli Inflamatorii*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** À jeun 6 ore; ingestie fracționată de 1000-1500 ml soluție hiperosmolară non-absorbabilă (PEG - polietilenglicol sau Manitol 2.5%) în decurs de 45-60 minute înainte de scanare pentru distensia uniformă a anselor de intestin subțire; administrare IV de antispastic (Butilscopolamină / Buscopan 20 mg sau Glucagon 1 mg) imediat înainte de secvențe.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T (preferabil pentru mai puține artefacte de susceptibilitate gazoasă) sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Phased-Array Abdomen-Pelvis combinată (acoperire de la diafragm la simfiza pubiană)
    - **Poziție Pacient & Centrare:** Decubit ventral (prone) preferat deoarece reduce grosimea abdomenului și separă ansele ileale, sau decubit dorsal dacă nu este tolerat.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic IV
    - **Doză Recomandată:** 0.1 - 0.15 mmol/kg corp
    - **Rată de Injectare (Debit):** 2.0 - 2.5 ml/s injectare automată + 30 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Secvențe 3D T1 cu FatSat la 45s (arterial enteric), 70s (portal) și 180s (tardiv)
    - **Filtrare Renală & Precauții:** Îngroșarea parietală > 3 mm cu hipercaptare stratificată mucoasă/submucoasă și edem T2 indică inflamație acută activă.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T2 HASTE / SSFSE Free-breathing** | Coronal abdomen-pelvis | Single-shot / TE 90 ms | 4.0 mm / gap 0.4 mm | FOV 420 mm / 384x256 | Nu | Evaluare distensie luminală pe tot cadrul jejuno-ileal |
    | **Coronal T2 cu supresie de grăsime (FatSat / SPAIR)** | Coronal | Single-shot / TE 90 ms | 4.0 mm / gap 0.4 mm | FOV 420 mm / 320x256 | FatSat | Edem parietal în strat submucos, lichid liber, colecții peridigestive |
    | **Axial T2 HASTE / TrueFISP cine-motilitate** | Axial pe ansele afectate (ileon terminal) | TR 3.5 ms / TE 1.5 ms | 4.0 mm / gap 0 mm | FOV 350 mm / 256x256 | Nu | Apreciere peristaltică: stenozele rigide lipsite de motilitate |
    | **Axial & Coronal DWI (b=0, 600, 900) + ADC** | Axial și Coronal | TR 4500 ms / TE 65 ms | 4.0 mm / gap 0.4 mm | FOV 380 mm / 192x160 | FatSat | Restricție de difuzie corelată direct cu scorul endoscopic de inflamație |
    | **3D T1 GRE Dinamic multipfazic post-Gd** | Coronal și Axial | TR 3.8 ms / TE 1.6 ms | 2.5 mm interpolat la 1.2 mm | FOV 400 mm / 320x256 | Dixon / FatSat | Priză de contrast parietală, semnul pieptenului (comb sign - vase vasa recta dilatate) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Distensie luminală adecvată a anselor jejunale și a ileonului terminal (> 2-2.5 cm calibru)
    - Absența artefactelor de peristaltică prin administrarea promptă a antispasticului
    - Acoperire anatomică completă de la unghiul Treitz până la ampula rectală

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Buscopan este contraindicat la pacienți cu glaucom cu unghi îngust, hipertrofie de prostată cu retenție de urină sau tahiaritmii severe (se poate folosi Glucagon)

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Permite diferențierea precisă între stenoza inflamatorie activă (edem T2, difuzie restricționată, captare intensă) ce răspunde la terapie medicamentoasă și stenoza fibroasă cicatricială ce necesită rezecție chirurgicală sau dilatare.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [UT Southwestern Radiology — Abdomen & Pelvis MRI Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html) — *UT Southwestern* (US)
- [ACR-SAR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Abdomen and Pelvis](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Abd-Pel.pdf) — *ACR / SAR* (US)
