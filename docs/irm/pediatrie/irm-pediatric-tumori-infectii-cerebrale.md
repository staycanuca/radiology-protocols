---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Suspiciune sau monitorizare de proces expansiv intracranian la copil (tumori de
  fosă posterioară, gliome, craniofaringiom)
- 'Infecții acute și subacute ale SNC: meningoencefalită, empiem subdural, abces cerebral'
- Boli inflamatorii și demielinizante (ADEM, scleroză multiplă pediatrică)
- Suspiciune de diseminare leptomeningiană tumorală sau infecțioasă
coils_hardware:
  coil: Antenă dedicată Head/Neck multicanal (16-32 canale)
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, imobilizare simetrică a extremității cefalice
contraindications:
- Implanturi feromagnetice incompatibile RM
- Insuficiență renală acută sau eGFR < 30 mL/min/1.73m² (precauție la chelati de Gadoliniu)
contrast:
  agent: 'Chelat de Gadoliniu macrociclic hidrosolubil (ex: Gadobutrol, Gadoterat
    de meglumină)'
  dose: 0.1 mmol/kg corp (0.1 ml/kg pentru 1.0 M sau 0.2 ml/kg pentru 0.5 M)
  flow_rate: 1.0 - 1.5 ml/s injectare manuală sau automată, urmată de spălare cu 10-15
    ml ser fiziologic
  notes: Risc de NSF minimizat prin utilizarea exclusivă a agenților macrociclici
    stabili.
  timing: Achiziție secvențe post-contrast T1 la 2-3 minute post-injectare
iris_reference:
  chapter: Pediatrie - Sistem Nervos Central
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol standardizat WFPI optimizat pentru evaluarea completă a patologiei
  oncologice și infecțioase cerebrale în 20-30 minute.
patient_prep: Abord venos periferic montat înainte de intrarea în sala RM; repaus
  alimentar 2-4 ore dacă se folosește anestezie/sedare; verificarea funcției renale.
quality_criteria:
- Comparație riguroasă 3D T1 nativ vs. post-contrast în aceeași geometrie
- FLAIR post-contrast fără hipersemnal fals pozitiv de la debit LCR
- Acoperire completă de la vertex până la joncțiunea cranio-cervicală (C2-C3)
safety_considerations:
- Monitorizare atentă la injectarea de contrast
- SAR corp întreg menținut în limite normale
sequences:
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 220 mm / 192x192
  name: Axial DWI (b=0, b=1000) + hartă ADC
  notes: Restricție de difuzie în abcese, tumori hipercelulare (ex. meduloblastom)
    (1-2 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3500 ms / TE 70 ms
- fat_sat: Nu
  fov_matrix: FOV 240 mm / 256x256
  name: 3D T1WI Izotrop Sagital Nativ (MPRAGE / BRAVO)
  notes: Morfologie nativă de referință pre-contrast (5-7 min)
  plane: Sagital 3D Izotrop
  slice_gap: 1.0 mm izotrop
  tr_te: TR 1900 ms / TE 2.5 ms / TI 900 ms
- fat_sat: Nu
  fov_matrix: FOV 220 mm / 384x288
  name: Axial T2WI TSE
  notes: Edem peritumoral, componență chistică/necrotică (3 min)
  plane: Axial
  slice_gap: 3.5 mm / gap 0.3 mm
  tr_te: TR 4000 ms / TE 100 ms
- fat_sat: Nu
  fov_matrix: FOV 220 mm / 256x256
  name: Axial SWI / T2* GRE
  notes: Hemoragie intratumorală, calcificări, neovascularizație (3-5 min)
  plane: Axial
  slice_gap: 3.0 mm / gap 0.3 mm
  tr_te: TR 600 ms / TE 20 ms
- fat_sat: Nu
  fov_matrix: FOV 240 mm / 256x256
  name: 3D T1WI Izotrop Sagital Post-Contrast (MPRAGE / BRAVO)
  notes: Captare tumorală, noduli milimetrici, reformate MPR coronale și axiale (5-7
    min)
  plane: Sagital 3D Izotrop
  slice_gap: 1.0 mm izotrop
  tr_te: TR 1900 ms / TE 2.5 ms / TI 900 ms
- fat_sat: Nu
  fov_matrix: FOV 220 mm / 256x224
  name: Coronal FLAIR Post-Contrast
  notes: Sensibilitate extrem de ridicată pentru captare leptomeningiană tumorală
    sau meningită (3 min)
  plane: Coronal
  slice_gap: 3.5 mm / gap 0.3 mm
  tr_te: TR 8500 ms / TE 100 ms / TI 2400 ms
slug: irm-pediatric-tumori-infectii-cerebrale
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
title: RM Pediatric — Protocol Tumori & Infecții Cerebrale (Brain Tumor & Infection)
---
# RM Pediatric — Protocol Tumori & Infecții Cerebrale (Brain Tumor & Infection)

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

        - Suspiciune sau monitorizare de proces expansiv intracranian la copil (tumori de fosă posterioară, gliome, craniofaringiom)
        - Infecții acute și subacute ale SNC: meningoencefalită, empiem subdural, abces cerebral
        - Boli inflamatorii și demielinizante (ADEM, scleroză multiplă pediatrică)
        - Suspiciune de diseminare leptomeningiană tumorală sau infecțioasă

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice incompatibile RM
        - Insuficiență renală acută sau eGFR < 30 mL/min/1.73m² (precauție la chelati de Gadoliniu)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Sistem Nervos Central*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Abord venos periferic montat înainte de intrarea în sala RM; repaus alimentar 2-4 ore dacă se folosește anestezie/sedare; verificarea funcției renale.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată Head/Neck multicanal (16-32 canale)
    - **Poziție Pacient & Centrare:** Decubit dorsal, imobilizare simetrică a extremității cefalice

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic hidrosolubil (ex: Gadobutrol, Gadoterat de meglumină)
    - **Doză Recomandată:** 0.1 mmol/kg corp (0.1 ml/kg pentru 1.0 M sau 0.2 ml/kg pentru 0.5 M)
    - **Rată de Injectare (Debit):** 1.0 - 1.5 ml/s injectare manuală sau automată, urmată de spălare cu 10-15 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Achiziție secvențe post-contrast T1 la 2-3 minute post-injectare
    - **Filtrare Renală & Precauții:** Risc de NSF minimizat prin utilizarea exclusivă a agenților macrociclici stabili.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Axial DWI (b=0, b=1000) + hartă ADC** | Axial | TR 3500 ms / TE 70 ms | 4.0 mm / gap 0.4 mm | FOV 220 mm / 192x192 | FatSat (EPI) | Restricție de difuzie în abcese, tumori hipercelulare (ex. meduloblastom) (1-2 min) |
    | **3D T1WI Izotrop Sagital Nativ (MPRAGE / BRAVO)** | Sagital 3D Izotrop | TR 1900 ms / TE 2.5 ms / TI 900 ms | 1.0 mm izotrop | FOV 240 mm / 256x256 | Nu | Morfologie nativă de referință pre-contrast (5-7 min) |
    | **Axial T2WI TSE** | Axial | TR 4000 ms / TE 100 ms | 3.5 mm / gap 0.3 mm | FOV 220 mm / 384x288 | Nu | Edem peritumoral, componență chistică/necrotică (3 min) |
    | **Axial SWI / T2* GRE** | Axial | TR 600 ms / TE 20 ms | 3.0 mm / gap 0.3 mm | FOV 220 mm / 256x256 | Nu | Hemoragie intratumorală, calcificări, neovascularizație (3-5 min) |
    | **3D T1WI Izotrop Sagital Post-Contrast (MPRAGE / BRAVO)** | Sagital 3D Izotrop | TR 1900 ms / TE 2.5 ms / TI 900 ms | 1.0 mm izotrop | FOV 240 mm / 256x256 | Nu | Captare tumorală, noduli milimetrici, reformate MPR coronale și axiale (5-7 min) |
    | **Coronal FLAIR Post-Contrast** | Coronal | TR 8500 ms / TE 100 ms / TI 2400 ms | 3.5 mm / gap 0.3 mm | FOV 220 mm / 256x224 | Nu | Sensibilitate extrem de ridicată pentru captare leptomeningiană tumorală sau meningită (3 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Comparație riguroasă 3D T1 nativ vs. post-contrast în aceeași geometrie
    - FLAIR post-contrast fără hipersemnal fals pozitiv de la debit LCR
    - Acoperire completă de la vertex până la joncțiunea cranio-cervicală (C2-C3)

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Monitorizare atentă la injectarea de contrast
    - SAR corp întreg menținut în limite normale

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol standardizat WFPI optimizat pentru evaluarea completă a patologiei oncologice și infecțioase cerebrale în 20-30 minute.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
