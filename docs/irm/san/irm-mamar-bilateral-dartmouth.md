---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: san
clinical_indications:
- Stadializarea locală a cancerului de sân recent diagnosticat (multifocalitate, multicentricitate,
  bilateralitate)
- Evaluarea răspunsului terapeutic la chimioterapia neoadjuvantă (NAC)
- Screening anual la femei cu risc înalt (mutații genetice BRCA1/BRCA2, risc pe viață
  > 20-25%)
- Cancer ocult cu adenopatie axilară metastatică și mamografie/ecografie negative
- Evaluarea leziunilor neconcludente mamografic sau ecografic
coils_hardware:
  coil: Antenă dedicată de sân multicanal (Breast Coil 8–16 canale)
  field_strength: 1.5 Tesla sau 3.0 Tesla
  positioning: Decubit ventral (prone), ambii sâni așezați simetric în cupele antenei
    fără pliuri cutanate
contraindications:
- Stimulator cardiac / implanturi feromagnetice incompatibile RM
- Sarcină în primul trimestru (examinare electivă fără contrast se reprogramează)
- Insuficiență renală severă (eGFR < 30 mL/min) — contraindicație la Gadoliniu
contrast:
  agent: Gadoliniu macrociclic 0.1 mmol/kg
  dose: 0.1 mmol/kg urmat de 20-30 mL flush salin
  flow_rate: 2.0 mL/s injectare automată
  timing: 'Achiziție dinamică rapidă: fază nativă pre-contrast urmată de minim 5 faze
    secvențiale la intervale de 60-90 secunde'
iris_reference:
  chapter: Senologie & Mamografie
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
modality: irm
notes: Protocolul Dartmouth Hitchcock include obligatoriu scăderi digitale automate
  (Subtractions) pe consola PACS. Raportarea leziunilor se efectuează conform terminologiei
  standardizate BI-RADS IRM.
patient_prep: Examinarea se programează optim între zilele 7–14 ale ciclului menstrual
  (faza foliculară) pentru a minimiza încărcarea de fond a parenchimului fibroglandular
  (BPE). Documentare dată ultimă menstruație (LMP).
quality_criteria:
- Supresie a grăsimii absolut omogenă bilaterală
- Rezoluție spațială înaltă (submilimetrică) și temporală (< 90-120 sec per achiziție
  dinamică)
- Calculul curbei intensitate-timp (Tip I progresiv = probabil benign, Tip II platou
  = suspect, Tip III wash-out = înalt sugestiv pentru malignitate)
safety_considerations:
- Verificare eGFR pre-contrast
- Documentare status mamar prealabil (biopsii recente, intervenții chirurgicale, radioterapie
  anterioară)
sequences:
- fat_sat: Da (Dixon / SPAIR omogen)
  fov_matrix: FOV 340 mm / Matrice 384×384
  name: Axial T2 FS Dixon / Water Excitation
  notes: Caracterizare chisturi, edem peritumoral, ganglioni axilari și leziuni benigne
    (fibroadenoame)
  plane: Axial bilateral
  slice_gap: 3.0 mm / 0.5 mm gap
  tr_te: TR 4500 ms / TE 80 ms
- fat_sat: Nu
  fov_matrix: FOV 340 mm / Matrice 384×288
  name: Axial T1 VIBE Non-FS Nativ
  notes: Aprecierea densității parenchimului glandular și a focarelor hemoragice sau
    proteice preexistente
  plane: Axial bilateral
  slice_gap: 2.5 mm
  tr_te: TR 4.5 ms / TE 1.8 ms
- fat_sat: Da
  fov_matrix: FOV 340 mm / Matrice 384×320
  name: Axial 3D T1 VIBE FS Pre-Contrast
  notes: 'Faza 1 nativă: bază de comparație pentru scăderile digitale și verificarea
    supresiei grăsimii'
  plane: Axial bilateral
  slice_gap: 1.2 - 1.5 mm izotrop
  tr_te: TR 4.2 ms / TE 1.6 ms
- fat_sat: Da
  fov_matrix: FOV 340 mm / Matrice 384×320
  name: Axial 3D T1 VIBE FS Dinamic Post-Contrast (Fazele 2–6)
  notes: Achiziții seriate la 60s, 120s, 180s, 240s, 360s post-contrast. Generare
    automată Subtraction și curbe cinetice
  plane: Axial bilateral
  slice_gap: 1.2 - 1.5 mm izotrop
  tr_te: TR 4.2 ms / TE 1.6 ms
- fat_sat: Da
  fov_matrix: FOV 220 mm / Matrice 320×256
  name: Sagital 3D T1 VIBE FS Post-Contrast Tardiv
  notes: Evaluare anatomică a raportului leziunii cu fascia mușchiului pectoral și
    mamelonul
  plane: Sagital (unilateral sau bilateral pe sânul cu leziune)
  slice_gap: 1.5 mm
  tr_te: TR 4.5 ms / TE 1.7 ms
- fat_sat: Da
  fov_matrix: FOV 340 mm
  name: Reconstrucție MIP Axial Dinamic 3D
  notes: Harta vasculară a sânilor pentru detecția instantanee a leziunilor hipervasculare
    și asimetriilor
  plane: Axial 3D MIP
  slice_gap: Proiecție volumetrică
  tr_te: MIP din scăderea fazei precoce (Faza 2 minus Faza 1)
title: IRM Mamar Bilateral Nativ & Dinamic (Protocol DHMC)
---
# IRM Mamar Bilateral Nativ & Dinamic (Protocol DHMC)

<div class="irm-meta-bar">
  <span class="irm-modality-badge">🧲 Imagistică prin Rezonanță Magnetică (IRM)</span>
  <span><strong>Actualizat:</strong> 2026-09-26</span>
  <span><strong>Autor:</strong> Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații RM__

    ---

    === "Indicații Clinice"

        - Stadializarea locală a cancerului de sân recent diagnosticat (multifocalitate, multicentricitate, bilateralitate)
        - Evaluarea răspunsului terapeutic la chimioterapia neoadjuvantă (NAC)
        - Screening anual la femei cu risc înalt (mutații genetice BRCA1/BRCA2, risc pe viață > 20-25%)
        - Cancer ocult cu adenopatie axilară metastatică și mamografie/ecografie negative
        - Evaluarea leziunilor neconcludente mamografic sau ecografic

    === "Contraindicații & Screening Metalic"

        - Stimulator cardiac / implanturi feromagnetice incompatibile RM
        - Sarcină în primul trimestru (examinare electivă fără contrast se reprogramează)
        - Insuficiență renală severă (eGFR < 30 mL/min) — contraindicație la Gadoliniu

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Senologie & Mamografie*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Examinarea se programează optim între zilele 7–14 ale ciclului menstrual (faza foliculară) pentru a minimiza încărcarea de fond a parenchimului fibroglandular (BPE). Documentare dată ultimă menstruație (LMP).
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla sau 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată de sân multicanal (Breast Coil 8–16 canale)
    - **Poziție Pacient & Centrare:** Decubit ventral (prone), ambii sâni așezați simetric în cupele antenei fără pliuri cutanate

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic 0.1 mmol/kg
    - **Doză Recomandată:** 0.1 mmol/kg urmat de 20-30 mL flush salin
    - **Rată de Injectare (Debit):** 2.0 mL/s injectare automată
    - **Temporizare & Faze Dinamice:** Achiziție dinamică rapidă: fază nativă pre-contrast urmată de minim 5 faze secvențiale la intervale de 60-90 secunde
    - **Filtrare Renală & Precauții:** Evaluare eGFR conform ghidurilor ESUR; risc redus de Fibroză Sistemică Nefrogenă (NSF) pentru agenții macrociclici.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Axial T2 FS Dixon / Water Excitation** | Axial bilateral | TR 4500 ms / TE 80 ms | 3.0 mm / 0.5 mm gap | FOV 340 mm / Matrice 384×384 | Da (Dixon / SPAIR omogen) | Caracterizare chisturi, edem peritumoral, ganglioni axilari și leziuni benigne (fibroadenoame) |
    | **Axial T1 VIBE Non-FS Nativ** | Axial bilateral | TR 4.5 ms / TE 1.8 ms | 2.5 mm | FOV 340 mm / Matrice 384×288 | Nu | Aprecierea densității parenchimului glandular și a focarelor hemoragice sau proteice preexistente |
    | **Axial 3D T1 VIBE FS Pre-Contrast** | Axial bilateral | TR 4.2 ms / TE 1.6 ms | 1.2 - 1.5 mm izotrop | FOV 340 mm / Matrice 384×320 | Da | Faza 1 nativă: bază de comparație pentru scăderile digitale și verificarea supresiei grăsimii |
    | **Axial 3D T1 VIBE FS Dinamic Post-Contrast (Fazele 2–6)** | Axial bilateral | TR 4.2 ms / TE 1.6 ms | 1.2 - 1.5 mm izotrop | FOV 340 mm / Matrice 384×320 | Da | Achiziții seriate la 60s, 120s, 180s, 240s, 360s post-contrast. Generare automată Subtraction și curbe cinetice |
    | **Sagital 3D T1 VIBE FS Post-Contrast Tardiv** | Sagital (unilateral sau bilateral pe sânul cu leziune) | TR 4.5 ms / TE 1.7 ms | 1.5 mm | FOV 220 mm / Matrice 320×256 | Da | Evaluare anatomică a raportului leziunii cu fascia mușchiului pectoral și mamelonul |
    | **Reconstrucție MIP Axial Dinamic 3D** | Axial 3D MIP | MIP din scăderea fazei precoce (Faza 2 minus Faza 1) | Proiecție volumetrică | FOV 340 mm | Da | Harta vasculară a sânilor pentru detecția instantanee a leziunilor hipervasculare și asimetriilor |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Supresie a grăsimii absolut omogenă bilaterală
    - Rezoluție spațială înaltă (submilimetrică) și temporală (< 90-120 sec per achiziție dinamică)
    - Calculul curbei intensitate-timp (Tip I progresiv = probabil benign, Tip II platou = suspect, Tip III wash-out = înalt sugestiv pentru malignitate)

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Verificare eGFR pre-contrast
    - Documentare status mamar prealabil (biopsii recente, intervenții chirurgicale, radioterapie anterioară)

</div>


!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocolul Dartmouth Hitchcock include obligatoriu scăderi digitale automate (Subtractions) pe consola PACS. Raportarea leziunilor se efectuează conform terminologiei standardizate BI-RADS IRM.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
