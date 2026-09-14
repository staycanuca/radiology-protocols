---
author: Departamentul de Radiologie și Imagistică Medicală
category: abdomen-pelvis
clinical_indications:
- Caracterizarea nodulilor hepatici descoperiți incidental la ecografie sau CT
- Screening și diagnostic hepatocarcinom (HCC) la pacienți cirotici conform criteriilor
  LI-RADS
- Diferențiere leziuni benigne (hemangiom, hiperplazie nodulară focală FNH, adenom
  hepatic) de leziuni maligne
- Bilanț pre-operator / transplant hepatic și stadializare metastaze hepatice
coils_hardware:
  coil: Antenă Phased-Array Toraco-Abdominală 16-32 canale + antenă Spine
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, centrare pe rebordul costal inferior (apendice xifoid),
    curea de monitorizare respiratorie montată pe abdomen.
contraindications:
- Contraindicații generale RM; eGFR < 30 ml/min (risc NSF la agenți non-recomandați).
contrast:
  agent: Chelat de Gadoliniu macrociclic extracelular sau agent hepato-specific (Acid
    Gadoxetic / Primovist)
  dose: 0.1 mmol/kg (sau 0.025 mmol/kg pentru Primovist)
  flow_rate: 2.0 ml/s urmat de bolus de spălare de 30 ml ser fiziologic
  notes: Injectarea automată cu seringă cu două corpuri și temporizare precisă a fazei
    arteriale este critică pentru detecția hipercaptării arteriale HCC.
  timing: Arterial tardiv (fluorotrigger pe aorta celiacă sau 18-22s), Portal (60-70s),
    Venos de tranziție (120s), Tardiv / Hepatobiliar (20 min la Primovist)
iris_reference:
  chapter: Ficat și Căi Biliare - Hepatocarcinom și Leziuni Focale
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: 'Criteriile LI-RADS 5 (certitudine absolută de HCC): nodul > 10 mm pe ficat
  cirotic cu hipercaptare arterială non-încapsulată și wash-out tardiv cu pseudocapsulă.'
patient_prep: À jeun minim 6 ore (repaus alimentar); exerciții de apnee ghidată explicate
  pacientului înainte de scanare; abord venos periferic de calibru mare (18-20G) în
  plica cotului.
quality_criteria:
- Apnee inspiratorie reproductibilă fără artefacte de 'ghosting' pe faza arterială
- Capacitatea de a surprinde wash-in arterial și wash-out venos tipice pentru LI-RADS
  5
- Supresie omogenă a semnalului grăsimii pe întregul parenchim hepatic
safety_considerations:
- Monitorizare respiratorie strictă; pacienții decompensați ascitici necesită secvențe
  'free-breathing' cu navigare
sequences:
- fat_sat: Nu
  fov_matrix: FOV 380 mm / 320x256
  name: Coronal T2 HASTE / SSFSE
  notes: Anatomie generală abdominală și repere vasculare
  plane: Coronal
  slice_gap: 5.0 mm / gap 0.5 mm
  tr_te: Single-shot / TE 90 ms
- fat_sat: Nu
  fov_matrix: FOV 380 mm / 320x224
  name: Axial T1 Dual Echo (In-Phase / Out-of-Phase)
  notes: Steatoză hepatică, încărcare lipidică intracelulară în adenoame
  plane: Axial
  slice_gap: 5.0 mm / gap 1.0 mm
  tr_te: TR 140 ms / TE 2.2 ms (OP) și 4.4 ms (IP)
- fat_sat: FatSat
  fov_matrix: FOV 380 mm / 320x256
  name: Axial T2 TSE cu supresie de grăsime (FatSat / SPAIR)
  notes: Diferențiere hemangiom/chist (foarte strălucitor) de tumori solide
  plane: Axial
  slice_gap: 5.0 mm / gap 1.0 mm
  tr_te: Gating respirator / TE 85 ms
- fat_sat: FatSat
  fov_matrix: FOV 380 mm / 192x160
  name: Axial DWI (b=50, 400, 800) + ADC Map
  notes: Restricție de difuzie în leziuni maligne celulare (HCC, metastaze)
  plane: Axial
  slice_gap: 5.0 mm / gap 1.0 mm
  tr_te: Gating respirator / TE 60 ms
- fat_sat: Dixon / FatSat
  fov_matrix: FOV 380 mm / 320x224
  name: 3D T1 GRE Dinamic multipfazic (VIBE / LAVA / THRIVE)
  notes: 'Faze: Nativ, Arterial tardiv, Portal venos, Echilibru (3 min) și Tardiv'
  plane: Axial (apnee de 15 secunde per fază)
  slice_gap: 3.0 mm interpolat la 1.5 mm
  tr_te: TR 3.5 ms / TE 1.4 ms / FA 10°
slug: irm-ficat-multipfazic-cu-contrast
title: IRM Ficat Multipfazic cu Substanță de Contrast Paramagnetic
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
position: Decubit dorsal, centrare pe rebordul costal inferior (apendice xifoid),
  curea de monitorizare respiratorie montată pe abdomen.
---

# IRM Ficat Multipfazic cu Substanță de Contrast Paramagnetic

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

        - Caracterizarea nodulilor hepatici descoperiți incidental la ecografie sau CT
        - Screening și diagnostic hepatocarcinom (HCC) la pacienți cirotici conform criteriilor LI-RADS
        - Diferențiere leziuni benigne (hemangiom, hiperplazie nodulară focală FNH, adenom hepatic) de leziuni maligne
        - Bilanț pre-operator / transplant hepatic și stadializare metastaze hepatice

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM; eGFR < 30 ml/min (risc NSF la agenți non-recomandați).

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Ficat și Căi Biliare - Hepatocarcinom și Leziuni Focale*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** À jeun minim 6 ore (repaus alimentar); exerciții de apnee ghidată explicate pacientului înainte de scanare; abord venos periferic de calibru mare (18-20G) în plica cotului.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Phased-Array Toraco-Abdominală 16-32 canale + antenă Spine
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe rebordul costal inferior (apendice xifoid), curea de monitorizare respiratorie montată pe abdomen.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic extracelular sau agent hepato-specific (Acid Gadoxetic / Primovist)
    - **Doză Recomandată:** 0.1 mmol/kg (sau 0.025 mmol/kg pentru Primovist)
    - **Rată de Injectare (Debit):** 2.0 ml/s urmat de bolus de spălare de 30 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Arterial tardiv (fluorotrigger pe aorta celiacă sau 18-22s), Portal (60-70s), Venos de tranziție (120s), Tardiv / Hepatobiliar (20 min la Primovist)
    - **Filtrare Renală & Precauții:** Injectarea automată cu seringă cu două corpuri și temporizare precisă a fazei arteriale este critică pentru detecția hipercaptării arteriale HCC.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T2 HASTE / SSFSE** | Coronal | Single-shot / TE 90 ms | 5.0 mm / gap 0.5 mm | FOV 380 mm / 320x256 | Nu | Anatomie generală abdominală și repere vasculare |
    | **Axial T1 Dual Echo (In-Phase / Out-of-Phase)** | Axial | TR 140 ms / TE 2.2 ms (OP) și 4.4 ms (IP) | 5.0 mm / gap 1.0 mm | FOV 380 mm / 320x224 | Nu | Steatoză hepatică, încărcare lipidică intracelulară în adenoame |
    | **Axial T2 TSE cu supresie de grăsime (FatSat / SPAIR)** | Axial | Gating respirator / TE 85 ms | 5.0 mm / gap 1.0 mm | FOV 380 mm / 320x256 | FatSat | Diferențiere hemangiom/chist (foarte strălucitor) de tumori solide |
    | **Axial DWI (b=50, 400, 800) + ADC Map** | Axial | Gating respirator / TE 60 ms | 5.0 mm / gap 1.0 mm | FOV 380 mm / 192x160 | FatSat | Restricție de difuzie în leziuni maligne celulare (HCC, metastaze) |
    | **3D T1 GRE Dinamic multipfazic (VIBE / LAVA / THRIVE)** | Axial (apnee de 15 secunde per fază) | TR 3.5 ms / TE 1.4 ms / FA 10° | 3.0 mm interpolat la 1.5 mm | FOV 380 mm / 320x224 | Dixon / FatSat | Faze: Nativ, Arterial tardiv, Portal venos, Echilibru (3 min) și Tardiv |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Apnee inspiratorie reproductibilă fără artefacte de 'ghosting' pe faza arterială
    - Capacitatea de a surprinde wash-in arterial și wash-out venos tipice pentru LI-RADS 5
    - Supresie omogenă a semnalului grăsimii pe întregul parenchim hepatic

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Monitorizare respiratorie strictă; pacienții decompensați ascitici necesită secvențe 'free-breathing' cu navigare

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Criteriile LI-RADS 5 (certitudine absolută de HCC): nodul > 10 mm pe ficat cirotic cu hipercaptare arterială non-încapsulată și wash-out tardiv cu pseudocapsulă.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [UT Southwestern Radiology — Abdomen & Pelvis MRI Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html) — *UT Southwestern* (US)
- [ACR-SAR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Abdomen and Pelvis](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Abd-Pel.pdf) — *ACR / SAR* (US)
