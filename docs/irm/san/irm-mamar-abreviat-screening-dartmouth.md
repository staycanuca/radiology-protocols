---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: san
clinical_indications:
- Screening rapid la femei asimptomatice cu sâni denși (ACR C și D) la mamografie
- Femei cu risc intermediar de cancer mamar (istoric personal de neoplazie mamară,
  atipii epiteliale la biopsie anterioară)
- Protocol economic și confortabil (< 10 minute timp în gantry) cu sensibilitate similară
  protocolului complet
coils_hardware:
  coil: Antenă dedicată Breast Coil multicanal
  field_strength: 1.5 Tesla sau 3.0 Tesla
  positioning: Decubit ventral (prone)
contraindications:
- Contraindicații generale la câmpul magnetic RM
- Insuficiență renală severă (eGFR < 30 mL/min)
- Femei cu leziuni clinice palpabile evidente sau secreții mamelonare (acestea necesită
  protocolul diagnostic complet)
contrast:
  agent: Gadoliniu macrociclic 0.1 mmol/kg
  dose: 0.1 mmol/kg + flush salin 20 mL
  flow_rate: 2.0 mL/s
  timing: O singură achiziție post-contrast precoce la 90–120 secunde
iris_reference:
  chapter: Senologie & Mamografie
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
modality: irm
notes: Protocolul Fast Breast MRI dezvoltat de DHMC sporește accesibilitatea screening-ului
  prin rezonanță magnetică la femeile cu densitate mamară crescută, dublând rata de
  detecție a neoplaziilor mamare incipiente comparativ cu mamografia digitală simplă.
patient_prep: Zilele 7–14 ale ciclului menstrual recomandate. Chestionar RM standard.
quality_criteria:
- Timp total de achiziție sub 10 minute pe masă
- Scădere digitală automată impecabilă
- Dacă se identifică o leziune suspectă pe MIP, se recomandă completare cu secvențe
  tardive sau ecografie țintită second-look
safety_considerations:
- Screening securitate RM
- Verificare eGFR
sequences:
- fat_sat: Da
  fov_matrix: FOV 340 mm
  name: Axial T2 FS (Localizare & Benignitate)
  notes: Diferențiere rapidă a chisturilor simple de mase solide
  plane: Axial bilateral
  slice_gap: 3.0 mm
  tr_te: TR 4000 ms / TE 80 ms
- fat_sat: Da
  fov_matrix: FOV 340 mm / Matrice 384×320
  name: Axial 3D T1 VIBE FS Pre-Contrast
  notes: Referință nativă (durată scanare ~1.5 minute)
  plane: Axial bilateral
  slice_gap: 1.2 mm
  tr_te: TR 4.0 ms / TE 1.5 ms
- fat_sat: Da
  fov_matrix: FOV 340 mm / Matrice 384×320
  name: Axial 3D T1 VIBE FS Precoce Post-Contrast (la 90-120s)
  notes: Achiziție unică la vârful încărcării neoplazice (durată ~1.5 minute)
  plane: Axial bilateral
  slice_gap: 1.2 mm
  tr_te: TR 4.0 ms / TE 1.5 ms
- fat_sat: Da
  fov_matrix: FOV 340 mm
  name: Reconstrucție MIP Unică (Subtracție Post minus Pre)
  notes: 'Interpretare în < 30 secunde: un MIP complet ''negru'' exclude leziunile
    hipervasculare suspecte'
  plane: Axial MIP 3D
  slice_gap: Volumetric
  tr_te: Post-procesare automată
title: IRM Mamar Abreviat Fast Screening (Protocol Dartmouth Hitchcock)
---
# IRM Mamar Abreviat Fast Screening (Protocol Dartmouth Hitchcock)

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

        - Screening rapid la femei asimptomatice cu sâni denși (ACR C și D) la mamografie
        - Femei cu risc intermediar de cancer mamar (istoric personal de neoplazie mamară, atipii epiteliale la biopsie anterioară)
        - Protocol economic și confortabil (< 10 minute timp în gantry) cu sensibilitate similară protocolului complet

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale la câmpul magnetic RM
        - Insuficiență renală severă (eGFR < 30 mL/min)
        - Femei cu leziuni clinice palpabile evidente sau secreții mamelonare (acestea necesită protocolul diagnostic complet)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Senologie & Mamografie*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Zilele 7–14 ale ciclului menstrual recomandate. Chestionar RM standard.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla sau 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată Breast Coil multicanal
    - **Poziție Pacient & Centrare:** Decubit ventral (prone)

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic 0.1 mmol/kg
    - **Doză Recomandată:** 0.1 mmol/kg + flush salin 20 mL
    - **Rată de Injectare (Debit):** 2.0 mL/s
    - **Temporizare & Faze Dinamice:** O singură achiziție post-contrast precoce la 90–120 secunde
    - **Filtrare Renală & Precauții:** Evaluare eGFR conform ghidurilor ESUR; risc redus de Fibroză Sistemică Nefrogenă (NSF) pentru agenții macrociclici.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Axial T2 FS (Localizare & Benignitate)** | Axial bilateral | TR 4000 ms / TE 80 ms | 3.0 mm | FOV 340 mm | Da | Diferențiere rapidă a chisturilor simple de mase solide |
    | **Axial 3D T1 VIBE FS Pre-Contrast** | Axial bilateral | TR 4.0 ms / TE 1.5 ms | 1.2 mm | FOV 340 mm / Matrice 384×320 | Da | Referință nativă (durată scanare ~1.5 minute) |
    | **Axial 3D T1 VIBE FS Precoce Post-Contrast (la 90-120s)** | Axial bilateral | TR 4.0 ms / TE 1.5 ms | 1.2 mm | FOV 340 mm / Matrice 384×320 | Da | Achiziție unică la vârful încărcării neoplazice (durată ~1.5 minute) |
    | **Reconstrucție MIP Unică (Subtracție Post minus Pre)** | Axial MIP 3D | Post-procesare automată | Volumetric | FOV 340 mm | Da | Interpretare în < 30 secunde: un MIP complet 'negru' exclude leziunile hipervasculare suspecte |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de achiziție sub 10 minute pe masă
    - Scădere digitală automată impecabilă
    - Dacă se identifică o leziune suspectă pe MIP, se recomandă completare cu secvențe tardive sau ecografie țintită second-look

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening securitate RM
    - Verificare eGFR

</div>


!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocolul Fast Breast MRI dezvoltat de DHMC sporește accesibilitatea screening-ului prin rezonanță magnetică la femeile cu densitate mamară crescută, dublând rata de detecție a neoplaziilor mamare incipiente comparativ cu mamografia digitală simplă.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
