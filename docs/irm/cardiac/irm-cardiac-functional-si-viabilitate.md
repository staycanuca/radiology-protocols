---
author: Departamentul de Radiologie și Imagistică Medicală
category: cardiac
clinical_indications:
- Evaluare viabilitate miocardică post-infarct miocardic înainte de revascularizare
  (PCI/CABG)
- Diagnostic și diferențiere cardiomiopatii (dilatativă, hipertrofică, non-compactare,
  amiloidoză)
- Suspiciune de miocardită acută (criteriile Lake Louise actualizate)
- Cuantificare precisă volume ventriculare și fracție de ejecție (FEVS, FEVD - gold
  standard)
- Aritmii ventriculare de cauză neclară, displazie aritmogenă de ventricul drept (ARVD)
coils_hardware:
  coil: Antenă Phased-Array Cardiacă dedicată 32 canale cu gating ECG integrat
  field_strength: 1.5T (standard de aur pentru bSSFP fără artefacte de banding) sau
    3.0T
  positioning: Decubit dorsal, centrare pe linia mediosternală la nivelul spațiului
    IV intercostal.
contraindications:
- Stimulatoare cardiace sau ICD incompatibile RM; aritmii frecvente necontrolate (fibrilație
  atrială rapidă - afectează triggerul ECG); eGFR < 30 ml/min.
contrast:
  agent: Chelat de Gadoliniu macrociclic
  dose: 0.15 - 0.20 mmol/kg corp (împărțit în bolus de perfuzie și bolus de viabilitate)
  flow_rate: 3.5 - 4.0 ml/s cu injector automat
  notes: Timpul de inversie (TI) se calibrează precis prin secvență Look-Locker pentru
    a anula complet semnalul miocardului sănătos (miocard negru).
  timing: Secvențe LGE (Late Gadolinium Enhancement) achiziționate la 10-15 minute
    post-injectare
iris_reference:
  chapter: Cardiologie - Imagistică Cardiovasculară
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: 'Transmuralitatea LGE prezice șansa de recuperare funcțională post-revascularizare:
  dacă fibroza ocupă < 50% din grosimea peretelui, segmentul este viabil și contractilitatea
  se poate recupera.'
patient_prep: Fără cofeină, fumat sau energizante cu 12 ore înainte; electrozi ECG
  compatibili RM plasați pe torace; instruire atentă privind apneea inspiratorie repetată
  de 8-12 secunde.
quality_criteria:
- Sincronizare ECG stabilă fără erori de trigger pe unda R
- Anularea perfectă a semnalului miocardului normal (miocard 'negru') pe secvențele
  LGE
- Apnee inspiratorie stabilă și reproductibilă
safety_considerations:
- Monitorizare ritm cardiac în permanență în sala de scanare
- Defibrilator extern compatibil RM disponibil în zona de pregătire
sequences:
- fat_sat: Nu
  fov_matrix: FOV 340 mm / 256x216
  name: Cine-bSSFP Ax Scurt (Short-Axis Stack)
  notes: Cuantificare volume end-diastolice/sistolice, masă VS, fracție de ejecție
  plane: Ax scurt ventricular de la bază la apex
  slice_gap: 8.0 mm / gap 2.0 mm
  tr_te: TR 3.0 ms / TE 1.5 ms / 30 faze/ciclu
- fat_sat: Nu
  fov_matrix: FOV 340 mm / 256x216
  name: Cine-bSSFP Axe Lungi (2-Chamber, 3-Chamber, 4-Chamber)
  notes: Cinetica segmentară a pereților conform modelului AHA 17 segmente
  plane: Axe lungi cardiace
  slice_gap: 6.0 mm / gap 0 mm
  tr_te: TR 3.0 ms / TE 1.5 ms
- fat_sat: STIR
  fov_matrix: FOV 340 mm / 256x192
  name: T2-STIR Black Blood (Edem Miocardic)
  notes: Raport intensitate semnal miocard/mușchi scheletic > 1.9 indică edem acut
  plane: Ax scurt și 4 camere
  slice_gap: 8.0 mm / gap 2.0 mm
  tr_te: Dual-inversion recovery / TE 65 ms
- fat_sat: Nu
  fov_matrix: FOV 340 mm / 256x192
  name: T1 Mapping nativ și post-contrast (ECV)
  notes: Cuantificare fracție de volum extracelular (ECV) - crescut în amiloidoză
    și fibroză difuză
  plane: Ax scurt (bază, mediu, apex)
  slice_gap: 8.0 mm
  tr_te: MOLLI / SASHA
- fat_sat: Inversion Recovery
  fov_matrix: FOV 340 mm / 256x216
  name: Late Gadolinium Enhancement (LGE 2D/3D PSIR)
  notes: 'Infarct: captare subendocardică/transmurală pe teritoriu coronarian; Miocardită:
    captare subepicardică/mediomiocardică'
  plane: Ax scurt complet, 2C, 3C, 4C
  slice_gap: 8.0 mm / gap 2.0 mm
  tr_te: TR 700 ms / TE 3.0 ms / TI 250-320 ms
slug: irm-cardiac-functional-si-viabilitate
title: IRM Cardiac - Evaluare Funcțională, Ischemie & Viabilitate (LGE)
sources:
- title: SCMR / ACR-NASCI Practice Parameter for the Performance of Cardiac Magnetic
    Resonance Imaging
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CMR.pdf
  institution: ACR / SCMR
  source_region: US
  kind: Standard de practică IRM cardiovascular
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 8fd8c2be19913bbc74eb327ac8bb44f090f555d6bc90ffb56256d14cfb31d16d
- title: UT Southwestern Radiology — Cardiac MR Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 15b64e8c0d1c83d4ed74c3e0e07b8690a60efdcc4e9083d1af807018cacc44f0
position: Decubit dorsal, centrare pe linia mediosternală la nivelul spațiului IV
  intercostal.
---

# IRM Cardiac - Evaluare Funcțională, Ischemie & Viabilitate (LGE)

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

        - Evaluare viabilitate miocardică post-infarct miocardic înainte de revascularizare (PCI/CABG)
        - Diagnostic și diferențiere cardiomiopatii (dilatativă, hipertrofică, non-compactare, amiloidoză)
        - Suspiciune de miocardită acută (criteriile Lake Louise actualizate)
        - Cuantificare precisă volume ventriculare și fracție de ejecție (FEVS, FEVD - gold standard)
        - Aritmii ventriculare de cauză neclară, displazie aritmogenă de ventricul drept (ARVD)

    === "Contraindicații & Screening Metalic"

        - Stimulatoare cardiace sau ICD incompatibile RM; aritmii frecvente necontrolate (fibrilație atrială rapidă - afectează triggerul ECG); eGFR < 30 ml/min.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cardiologie - Imagistică Cardiovasculară*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Fără cofeină, fumat sau energizante cu 12 ore înainte; electrozi ECG compatibili RM plasați pe torace; instruire atentă privind apneea inspiratorie repetată de 8-12 secunde.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T (standard de aur pentru bSSFP fără artefacte de banding) sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Phased-Array Cardiacă dedicată 32 canale cu gating ECG integrat
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe linia mediosternală la nivelul spațiului IV intercostal.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic
    - **Doză Recomandată:** 0.15 - 0.20 mmol/kg corp (împărțit în bolus de perfuzie și bolus de viabilitate)
    - **Rată de Injectare (Debit):** 3.5 - 4.0 ml/s cu injector automat
    - **Temporizare & Faze Dinamice:** Secvențe LGE (Late Gadolinium Enhancement) achiziționate la 10-15 minute post-injectare
    - **Filtrare Renală & Precauții:** Timpul de inversie (TI) se calibrează precis prin secvență Look-Locker pentru a anula complet semnalul miocardului sănătos (miocard negru).

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Cine-bSSFP Ax Scurt (Short-Axis Stack)** | Ax scurt ventricular de la bază la apex | TR 3.0 ms / TE 1.5 ms / 30 faze/ciclu | 8.0 mm / gap 2.0 mm | FOV 340 mm / 256x216 | Nu | Cuantificare volume end-diastolice/sistolice, masă VS, fracție de ejecție |
    | **Cine-bSSFP Axe Lungi (2-Chamber, 3-Chamber, 4-Chamber)** | Axe lungi cardiace | TR 3.0 ms / TE 1.5 ms | 6.0 mm / gap 0 mm | FOV 340 mm / 256x216 | Nu | Cinetica segmentară a pereților conform modelului AHA 17 segmente |
    | **T2-STIR Black Blood (Edem Miocardic)** | Ax scurt și 4 camere | Dual-inversion recovery / TE 65 ms | 8.0 mm / gap 2.0 mm | FOV 340 mm / 256x192 | STIR | Raport intensitate semnal miocard/mușchi scheletic > 1.9 indică edem acut |
    | **T1 Mapping nativ și post-contrast (ECV)** | Ax scurt (bază, mediu, apex) | MOLLI / SASHA | 8.0 mm | FOV 340 mm / 256x192 | Nu | Cuantificare fracție de volum extracelular (ECV) - crescut în amiloidoză și fibroză difuză |
    | **Late Gadolinium Enhancement (LGE 2D/3D PSIR)** | Ax scurt complet, 2C, 3C, 4C | TR 700 ms / TE 3.0 ms / TI 250-320 ms | 8.0 mm / gap 2.0 mm | FOV 340 mm / 256x216 | Inversion Recovery | Infarct: captare subendocardică/transmurală pe teritoriu coronarian; Miocardită: captare subepicardică/mediomiocardică |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Sincronizare ECG stabilă fără erori de trigger pe unda R
    - Anularea perfectă a semnalului miocardului normal (miocard 'negru') pe secvențele LGE
    - Apnee inspiratorie stabilă și reproductibilă

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Monitorizare ritm cardiac în permanență în sala de scanare
    - Defibrilator extern compatibil RM disponibil în zona de pregătire

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Transmuralitatea LGE prezice șansa de recuperare funcțională post-revascularizare: dacă fibroza ocupă < 50% din grosimea peretelui, segmentul este viabil și contractilitatea se poate recupera.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [SCMR / ACR-NASCI Practice Parameter for the Performance of Cardiac Magnetic Resonance Imaging](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CMR.pdf) — *ACR / SCMR* (US)
- [UT Southwestern Radiology — Cardiac MR Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/mr.html) — *UT Southwestern* (US)
