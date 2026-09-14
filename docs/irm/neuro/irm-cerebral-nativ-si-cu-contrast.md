---
author: Departamentul de Radiologie și Imagistică Medicală
category: neuro
clinical_indications:
- Cefalee cronică persistentă cu caractere atipice sau semne de focar neurologic
- Suspiciune de proces expansiv intracranian primitiv sau diseminări secundare (metastaze)
- Boală demielinizantă (scleroză multiplă) - diagnostic și monitorizare activitate
  lezională
- Epilepsie / crize convulsive cu debut recent
- Evaluare infecții SNC (meningo-encefalită, abces cerebral)
coils_hardware:
  coil: Antenă dedicată Head/Neck 32 - 64 canale
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, cap centrat în izocentru pe nasion, imobilizare confortabilă
    cu pernuțe de spumă.
contraindications:
- Stimulatoare cardiace, defibrilatoare (ICD) sau neurostimulatoare non-MR Conditional
- Clipurilor anevrismale intracraniene feromagnetice
- Corpi străini metalici intraoculari sau fragmente de schije în vecinătatea structurilor
  vitale
- Proteze auditive implantabile / implant cohlear nesigur RM
- Claustrofobie severă refractară (necesită sedare/anestezie)
- eGFR < 30 mL/min/1.73m² (precauție la chelati de Gadoliniu; risc de NSF)
contrast:
  agent: Chelat de Gadoliniu macrociclic (Gadobutrol 1.0 mmol/ml sau Gadoterat 0.5
    mmol/ml)
  dose: 0.1 mmol/kg corp (0.1 ml/kg Gadobutrol sau 0.2 ml/kg Gadoterat)
  flow_rate: 1.5 - 2.0 ml/s injectare automată urmată de 20 ml ser fiziologic
  notes: Risc de NSF minimizat prin utilizarea exclusivă a agenților macrociclici
    stabili conform ghidului ESUR.
  timing: Achiziție secvențe post-contrast T1 la minimum 2-3 minute de la injectare
iris_reference:
  chapter: Sistem Nervos Central - Neuroimagistică
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: În suspiciunea de scleroză multiplă se adaugă secvență 3D Sagital FLAIR cu
  reconstrucție axială și coronală.
patient_prep: Completare și semnare a chestionarului de securitate RM; îndepărtarea
  tuturor accesoriilor metalice, bijuteriilor, protezelor dentare mobile; verificare
  funcție renală (creatinină/eGFR).
quality_criteria:
- Raport semnal-zgomot (SNR) optim cu vizualizare netă a joncțiunii cortico-subcorticale
- Absența artefactelor de pulsație din sinusurile venoase sau arterele carotide/bazilară
- Acoperire completă vertex - foramen magnum fără trunchiere anatomică
safety_considerations:
- SAR corp întreg menținut în mod normal de operare (< 2.0 W/kg)
- Protecție acustică obligatorie cu căști fonoizolante și dopuri de urechi
- Monitorizare continuă video și verbală prin interfon
sequences:
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 320x256
  name: Sagital T1 SE / TSE
  notes: Anatomie linia mediană, corp calos, fosa posterioară
  plane: Sagital
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 500 ms / TE 10 ms
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 384x288
  name: Axial T2 TSE
  notes: Diferențiere substanță albă/cenușie, edem vasogenic
  plane: Axial (paralel CA-CP)
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 4500 ms / TE 100 ms
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 320x224
  name: Axial FLAIR
  notes: Supresie LCR liber; leziuni periventriculare și corticale
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 9000 ms / TE 90 ms / TI 2500 ms
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 230 mm / 192x192
  name: Axial DWI (b=0, b=1000) + hartă ADC
  notes: Restricție de difuzie (hipersemnal DWI + hiposemnal ADC)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3500 ms / TE 70 ms
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 320x256
  name: Axial T2* GRE / SWI
  notes: Detecție microsângerări, hemosiderină, calcificări
  plane: Axial
  slice_gap: 3.0 - 4.0 mm / gap 0 mm
  tr_te: TR 600 ms / TE 20 ms / FA 15°
- fat_sat: Nu
  fov_matrix: FOV 256 mm / 256x256
  name: 3D T1 GRE + C (MPRAGE / BRAVO)
  notes: Captare leptomeningiană, noduli milimetrici, reconstrucții MPR
  plane: 3D Sagital Izotrop
  slice_gap: 1.0 mm izotrop
  tr_te: TR 1900 ms / TE 2.5 ms / TI 900 ms
slug: irm-cerebral-nativ-si-cu-contrast
title: IRM Cerebral Nativ și cu Substanță de Contrast
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
position: Decubit dorsal, cap centrat în izocentru pe nasion, imobilizare confortabilă
  cu pernuțe de spumă.
---

# IRM Cerebral Nativ și cu Substanță de Contrast

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

        - Cefalee cronică persistentă cu caractere atipice sau semne de focar neurologic
        - Suspiciune de proces expansiv intracranian primitiv sau diseminări secundare (metastaze)
        - Boală demielinizantă (scleroză multiplă) - diagnostic și monitorizare activitate lezională
        - Epilepsie / crize convulsive cu debut recent
        - Evaluare infecții SNC (meningo-encefalită, abces cerebral)

    === "Contraindicații & Screening Metalic"

        - Stimulatoare cardiace, defibrilatoare (ICD) sau neurostimulatoare non-MR Conditional
        - Clipurilor anevrismale intracraniene feromagnetice
        - Corpi străini metalici intraoculari sau fragmente de schije în vecinătatea structurilor vitale
        - Proteze auditive implantabile / implant cohlear nesigur RM
        - Claustrofobie severă refractară (necesită sedare/anestezie)
        - eGFR < 30 mL/min/1.73m² (precauție la chelati de Gadoliniu; risc de NSF)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Sistem Nervos Central - Neuroimagistică*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Completare și semnare a chestionarului de securitate RM; îndepărtarea tuturor accesoriilor metalice, bijuteriilor, protezelor dentare mobile; verificare funcție renală (creatinină/eGFR).
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată Head/Neck 32 - 64 canale
    - **Poziție Pacient & Centrare:** Decubit dorsal, cap centrat în izocentru pe nasion, imobilizare confortabilă cu pernuțe de spumă.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic (Gadobutrol 1.0 mmol/ml sau Gadoterat 0.5 mmol/ml)
    - **Doză Recomandată:** 0.1 mmol/kg corp (0.1 ml/kg Gadobutrol sau 0.2 ml/kg Gadoterat)
    - **Rată de Injectare (Debit):** 1.5 - 2.0 ml/s injectare automată urmată de 20 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Achiziție secvențe post-contrast T1 la minimum 2-3 minute de la injectare
    - **Filtrare Renală & Precauții:** Risc de NSF minimizat prin utilizarea exclusivă a agenților macrociclici stabili conform ghidului ESUR.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T1 SE / TSE** | Sagital | TR 500 ms / TE 10 ms | 4.0 mm / gap 0.4 mm | FOV 230 mm / 320x256 | Nu | Anatomie linia mediană, corp calos, fosa posterioară |
    | **Axial T2 TSE** | Axial (paralel CA-CP) | TR 4500 ms / TE 100 ms | 4.0 mm / gap 0.4 mm | FOV 230 mm / 384x288 | Nu | Diferențiere substanță albă/cenușie, edem vasogenic |
    | **Axial FLAIR** | Axial | TR 9000 ms / TE 90 ms / TI 2500 ms | 4.0 mm / gap 0.4 mm | FOV 230 mm / 320x224 | Nu | Supresie LCR liber; leziuni periventriculare și corticale |
    | **Axial DWI (b=0, b=1000) + hartă ADC** | Axial | TR 3500 ms / TE 70 ms | 4.0 mm / gap 0.4 mm | FOV 230 mm / 192x192 | FatSat (EPI) | Restricție de difuzie (hipersemnal DWI + hiposemnal ADC) |
    | **Axial T2* GRE / SWI** | Axial | TR 600 ms / TE 20 ms / FA 15° | 3.0 - 4.0 mm / gap 0 mm | FOV 230 mm / 320x256 | Nu | Detecție microsângerări, hemosiderină, calcificări |
    | **3D T1 GRE + C (MPRAGE / BRAVO)** | 3D Sagital Izotrop | TR 1900 ms / TE 2.5 ms / TI 900 ms | 1.0 mm izotrop | FOV 256 mm / 256x256 | Nu | Captare leptomeningiană, noduli milimetrici, reconstrucții MPR |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Raport semnal-zgomot (SNR) optim cu vizualizare netă a joncțiunii cortico-subcorticale
    - Absența artefactelor de pulsație din sinusurile venoase sau arterele carotide/bazilară
    - Acoperire completă vertex - foramen magnum fără trunchiere anatomică

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR corp întreg menținut în mod normal de operare (< 2.0 W/kg)
    - Protecție acustică obligatorie cu căști fonoizolante și dopuri de urechi
    - Monitorizare continuă video și verbală prin interfon

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    În suspiciunea de scleroză multiplă se adaugă secvență 3D Sagital FLAIR cu reconstrucție axială și coronală.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [OHSU Diagnostic Radiology — Brain & Spine MRI Protocols](https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols) — *OHSU* (US)
- [ACR-ASNR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Brain](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Brain.pdf) — *ACR / ASNR* (US)
