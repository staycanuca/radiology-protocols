---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Caracterizare avansată mase abdominale solide (nefroblastom / tumoare Wilms, neuroblastom,
  hepatoblastom)
- Evaluare patologie pancreatică / biliară (pancreas divisum, chist de coledoc) la
  copil
- Boli inflamatorii intestinale pediatrice (boală Crohn) - protocol de enterografie
  RM extinsă
- Bilanț oncologic abdominal complet pre- și post-chimioterapie
coils_hardware:
  coil: Antenă Phased-Array Body multicanal
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, brațele ridicate deasupra capului dacă este confortabil
contraindications:
- Implanturi feromagnetice incompatibile RM
- Alergie documentată la chelati de Gadoliniu sau insuficiență renală severă fără
  epurare
contrast:
  agent: Chelat de Gadoliniu macrociclic hidrosolubil
  dose: 0.1 mmol/kg corp (sau 0.1-0.2 ml/kg în funcție de concentrație)
  flow_rate: 1.0 - 1.5 ml/s urmat de 15 ml ser fiziologic
  notes: Secvențe dinamice 3D T1 cu supresie de grăsime.
  timing: 'Faze dinamice: arterială (15-20 s), venoasă portală (50-60 s), tardivă
    (2-3 min)'
iris_reference:
  chapter: Pediatrie - Aparat digestiv & Abdomen
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol avansat WFPI pentru caracterizarea completă a maselor abdominale și
  patologiei hepato-bilio-pancreatice pediatrice.
patient_prep: Repaus alimentar 4 ore; la copii cooperanți se exersează comenzile scurte
  de apnee; dacă nu e posibilă apneea, se utilizează secvențe cu medieri crescute
  (5 NEX) în respirație liberă.
quality_criteria:
- 'Timp total de scanare: 15–20 minute'
- Sincronizare excelentă a fazei arteriale pentru evaluarea pediculilor vasculari
  tumorali
- Rezoluție spațială adecvată pentru detectarea trombozei de venă cavă inferioară
  sau renală
safety_considerations:
- Monitorizare funcție renală (eGFR)
- Menținere SAR în limitele modului normal
sequences:
- fat_sat: Nu
  fov_matrix: FOV 300-360 mm / 256x256
  name: Coronal T2WI Single-Shot (HASTE / SSFSE)
  notes: Respirație liberă (FB), panoramă abdominală (30–45 s)
  plane: Coronal
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 1000 ms / TE 80 ms
- fat_sat: Nu
  fov_matrix: FOV 280-320 mm / 256x256
  name: Axial T2WI Single-Shot (HASTE / SSFSE)
  notes: Respirație liberă (FB), morfologie organe parenchimatoase (30–45 s)
  plane: Axial
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 1000 ms / TE 80 ms
- fat_sat: Nu
  fov_matrix: FOV 300-340 mm / 256x256
  name: Coronal bSSFP (TrueFISP / FIESTA)
  notes: Trigger respirator (RT), contrast excelent sânge/țesut, anatomie vasculară
    (2 min)
  plane: Coronal
  slice_gap: 3.5 mm / gap 0 mm
  tr_te: TR 3.5 ms / TE 1.5 ms / FA 60°
- fat_sat: FatSat
  fov_matrix: FOV 280-320 mm / 320x256
  name: Axial T2WI FSE FS (cu supresie de grăsime)
  notes: Trigger respirator (RT), detectare edem, afectare chistică sau inflamatorie
    (3–5 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3000-4500 ms / TE 85 ms
- fat_sat: Nu (Dual-Echo)
  fov_matrix: FOV 280-320 mm / 256x192
  name: Axial T1WI In/Opposed Phase
  notes: Apnee (BH) sau respirație liberă cu 5 NEX (2–6 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 140 ms / TE 2.2 ms & 4.4 ms
- fat_sat: FatSat
  fov_matrix: FOV 280-320 mm / 128x128
  name: Axial DWI (b=50, b=400, b=800) + ADC
  notes: Efectuată înainte de contrast; evaluare celularitate tumorală (3–4 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3500 ms / TE 65 ms
- fat_sat: FatSat (VIBE / LAVA)
  fov_matrix: FOV 280-320 mm / 256x224
  name: Axial 3D T1WI FS Dinamic Pre- și Post-Contrast
  notes: Faze dinamice arteriale, venoase și tardive în apnee sau respirație liberă
    cu medieri (6 min)
  plane: Axial 3D
  slice_gap: 2.0-3.0 mm reconstruit la 1.5 mm
  tr_te: TR 3.5 ms / TE 1.4 ms / FA 12°
slug: irm-pediatric-abdomen-lung-extins
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
title: RM Pediatric — Protocol Abdomen Lung / Extins (Long Abdomen)
---
# RM Pediatric — Protocol Abdomen Lung / Extins (Long Abdomen)

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

        - Caracterizare avansată mase abdominale solide (nefroblastom / tumoare Wilms, neuroblastom, hepatoblastom)
        - Evaluare patologie pancreatică / biliară (pancreas divisum, chist de coledoc) la copil
        - Boli inflamatorii intestinale pediatrice (boală Crohn) - protocol de enterografie RM extinsă
        - Bilanț oncologic abdominal complet pre- și post-chimioterapie

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice incompatibile RM
        - Alergie documentată la chelati de Gadoliniu sau insuficiență renală severă fără epurare

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Aparat digestiv & Abdomen*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Repaus alimentar 4 ore; la copii cooperanți se exersează comenzile scurte de apnee; dacă nu e posibilă apneea, se utilizează secvențe cu medieri crescute (5 NEX) în respirație liberă.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă Phased-Array Body multicanal
    - **Poziție Pacient & Centrare:** Decubit dorsal, brațele ridicate deasupra capului dacă este confortabil

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic hidrosolubil
    - **Doză Recomandată:** 0.1 mmol/kg corp (sau 0.1-0.2 ml/kg în funcție de concentrație)
    - **Rată de Injectare (Debit):** 1.0 - 1.5 ml/s urmat de 15 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Faze dinamice: arterială (15-20 s), venoasă portală (50-60 s), tardivă (2-3 min)
    - **Filtrare Renală & Precauții:** Secvențe dinamice 3D T1 cu supresie de grăsime.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T2WI Single-Shot (HASTE / SSFSE)** | Coronal | TR 1000 ms / TE 80 ms | 4.0 mm / gap 0 mm | FOV 300-360 mm / 256x256 | Nu | Respirație liberă (FB), panoramă abdominală (30–45 s) |
    | **Axial T2WI Single-Shot (HASTE / SSFSE)** | Axial | TR 1000 ms / TE 80 ms | 4.0 mm / gap 0 mm | FOV 280-320 mm / 256x256 | Nu | Respirație liberă (FB), morfologie organe parenchimatoase (30–45 s) |
    | **Coronal bSSFP (TrueFISP / FIESTA)** | Coronal | TR 3.5 ms / TE 1.5 ms / FA 60° | 3.5 mm / gap 0 mm | FOV 300-340 mm / 256x256 | Nu | Trigger respirator (RT), contrast excelent sânge/țesut, anatomie vasculară (2 min) |
    | **Axial T2WI FSE FS (cu supresie de grăsime)** | Axial | TR 3000-4500 ms / TE 85 ms | 4.0 mm / gap 0.4 mm | FOV 280-320 mm / 320x256 | FatSat | Trigger respirator (RT), detectare edem, afectare chistică sau inflamatorie (3–5 min) |
    | **Axial T1WI In/Opposed Phase** | Axial | TR 140 ms / TE 2.2 ms & 4.4 ms | 4.0 mm / gap 0.4 mm | FOV 280-320 mm / 256x192 | Nu (Dual-Echo) | Apnee (BH) sau respirație liberă cu 5 NEX (2–6 min) |
    | **Axial DWI (b=50, b=400, b=800) + ADC** | Axial | TR 3500 ms / TE 65 ms | 4.0 mm / gap 0.4 mm | FOV 280-320 mm / 128x128 | FatSat | Efectuată înainte de contrast; evaluare celularitate tumorală (3–4 min) |
    | **Axial 3D T1WI FS Dinamic Pre- și Post-Contrast** | Axial 3D | TR 3.5 ms / TE 1.4 ms / FA 12° | 2.0-3.0 mm reconstruit la 1.5 mm | FOV 280-320 mm / 256x224 | FatSat (VIBE / LAVA) | Faze dinamice arteriale, venoase și tardive în apnee sau respirație liberă cu medieri (6 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de scanare: 15–20 minute
    - Sincronizare excelentă a fazei arteriale pentru evaluarea pediculilor vasculari tumorali
    - Rezoluție spațială adecvată pentru detectarea trombozei de venă cavă inferioară sau renală

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Monitorizare funcție renală (eGFR)
    - Menținere SAR în limitele modului normal

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol avansat WFPI pentru caracterizarea completă a maselor abdominale și patologiei hepato-bilio-pancreatice pediatrice.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
