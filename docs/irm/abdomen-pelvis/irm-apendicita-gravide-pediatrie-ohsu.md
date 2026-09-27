---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen-pelvis
clinical_indications:
- Suspiciune clinică de apendicită acută la paciente gravide (în orice trimestru de
  sarcină)
- Apendicită acută suspectată la copii și adolescenți când ecografia este neconcludentă
  sau tehnic dificilă
- Durere acută de fosă iliacă dreaptă la pacienți la care se dorește evitarea completă
  a iradierii prin CT
- Diagnosticul diferențial al patologiei inflamatorii acute pelvine la paciente tinere
coils_hardware:
  coil: Antenă Body phased-array multicanal (16–32 canale) centrată pe abdomenul inferior
    și pelvis
  field_strength: 1.5 Tesla (preferat în sarcină pentru SAR redus) sau 3.0 Tesla
  positioning: Decubit dorsal (sau decubit lateral stâng ușor în trimestrul III pentru
    prevenirea sindromului de compresie cavă)
contraindications:
- Implanturi feromagnetice non-MR Conditional
contrast:
  agent: Fără contrast (protocol exclusiv nativ)
  dose: N/A
  flow_rate: N/A
  notes: Contraindicație de rutină a administrării de Gadoliniu în sarcină conform
    ghidurilor OHSU și ACR.
  timing: N/A
iris_reference:
  chapter: Aparat digestiv & Abdomen
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol oficial OHSU de primă intenție la gravide cu suspiciune de apendicită
  după ecografie, cu sensibilitate și specificitate > 95%.
patient_prep: Fără contrast oral; fără substanță de contrast intravenos; vezică urinară
  parțial plină pentru reperaj anatomic.
quality_criteria:
- Identificarea apendicelui normal (diametru < 6 mm, perete fin < 2 mm, lumen colabat
  sau umplut cu gaz/lichid fără edem pericecal)
- 'Dacă apendicele nu poate fi menționat ca normal, identificarea clară a semnelor
  pozitive: diametru > 7 mm, îngroșare parietală, edem T2 FS periapendicular, restricție
  DWI'
- Durată totală la aparat menținută sub 15-20 minute
safety_considerations:
- 'La gravide: scanare exclusivă în mod SAR normal (< 2.0 W/kg)'
- Fără contrast pe bază de Gadoliniu
- Evitarea apneei prelungite; secvențele SSFSE sunt achiziționate în respirație liberă
  sau apnee scurtă
sequences:
- fat_sat: Nu
  fov_matrix: FOV 350-400 mm / Matrice 256×256
  name: Coronal SSFSE / HASTE T2 (Abdomen & Pelvis)
  notes: 'Vedere de ansamblu: poziție cec, deplasare uterină a anselor, lichid liber
    peritoneal'
  plane: Coronal
  slice_gap: 4.0 mm / gap 0 mm (sau overlap 50% dacă pacientul respiră)
  tr_te: TR 1000-1500 ms / TE 80-90 ms
- fat_sat: Nu
  fov_matrix: FOV 300-350 mm / Matrice 256×256
  name: Axial SSFSE / HASTE T2
  notes: Identificare bază apendiculară la joncțiunea cu fundul cecului
  plane: Axial
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 1000-1500 ms / TE 80-90 ms
- fat_sat: Nu
  fov_matrix: FOV 300-350 mm / Matrice 256×256
  name: Sagital SSFSE / HASTE T2
  notes: Urmărire traiect retrocecal sau pelvin al apendicelui
  plane: Sagital
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 1000-1500 ms / TE 80-90 ms
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 300-350 mm / Matrice 256×224
  name: Axial T2 FatSat (SPAIR / FS)
  notes: Evidențiere edem periapendicular, infiltrare a grăsimii fosei iliace drepte
    și colecții lichidiene
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 1500-2000 ms / TE 80 ms
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 300-350 mm / Matrice 128×128
  name: Axial DWI (b=50, b=800) + hartă ADC
  notes: Hipersemnal b=800 în peretele apendicular și restricție pe ADC = semn înalt
    specific de apendicită supurată
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3000-4000 ms / TE 60-70 ms
- fat_sat: Nu (Dual-echo)
  fov_matrix: FOV 320 mm / Matrice 256×192
  name: Axial In-Phase / Out-of-Phase T1 GRE
  notes: Detectare apendicolit / fecalit (semnal negru pe ambele ecouri) și sânge
    subacut
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 150 ms / TE 2.2 / 4.4 ms (la 1.5T)
title: RM Apendicită Acută Nativă - Gravide & Pediatrie (Protocol OHSU)
---
# RM Apendicită Acută Nativă - Gravide & Pediatrie (Protocol OHSU)

<div class="irm-meta-bar">
  <span class="irm-modality-badge">🧲 Imagistică prin Rezonanță Magnetică (IRM)</span>
  <span><strong>Actualizat:</strong> 2026-09-20</span>
  <span><strong>Autor:</strong> OHSU Diagnostic Radiology / Departamentul de Radiologie</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații RM__

    ---

    === "Indicații Clinice"

        - Suspiciune clinică de apendicită acută la paciente gravide (în orice trimestru de sarcină)
        - Apendicită acută suspectată la copii și adolescenți când ecografia este neconcludentă sau tehnic dificilă
        - Durere acută de fosă iliacă dreaptă la pacienți la care se dorește evitarea completă a iradierii prin CT
        - Diagnosticul diferențial al patologiei inflamatorii acute pelvine la paciente tinere

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice non-MR Conditional

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat digestiv & Abdomen*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Fără contrast oral; fără substanță de contrast intravenos; vezică urinară parțial plină pentru reperaj anatomic.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla (preferat în sarcină pentru SAR redus) sau 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă Body phased-array multicanal (16–32 canale) centrată pe abdomenul inferior și pelvis
    - **Poziție Pacient & Centrare:** Decubit dorsal (sau decubit lateral stâng ușor în trimestrul III pentru prevenirea sindromului de compresie cavă)

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Fără contrast (protocol exclusiv nativ)
    - **Doză Recomandată:** N/A
    - **Rată de Injectare (Debit):** N/A
    - **Temporizare & Faze Dinamice:** N/A
    - **Filtrare Renală & Precauții:** Contraindicație de rutină a administrării de Gadoliniu în sarcină conform ghidurilor OHSU și ACR.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal SSFSE / HASTE T2 (Abdomen & Pelvis)** | Coronal | TR 1000-1500 ms / TE 80-90 ms | 4.0 mm / gap 0 mm (sau overlap 50% dacă pacientul respiră) | FOV 350-400 mm / Matrice 256×256 | Nu | Vedere de ansamblu: poziție cec, deplasare uterină a anselor, lichid liber peritoneal |
    | **Axial SSFSE / HASTE T2** | Axial | TR 1000-1500 ms / TE 80-90 ms | 4.0 mm / gap 0 mm | FOV 300-350 mm / Matrice 256×256 | Nu | Identificare bază apendiculară la joncțiunea cu fundul cecului |
    | **Sagital SSFSE / HASTE T2** | Sagital | TR 1000-1500 ms / TE 80-90 ms | 4.0 mm / gap 0 mm | FOV 300-350 mm / Matrice 256×256 | Nu | Urmărire traiect retrocecal sau pelvin al apendicelui |
    | **Axial T2 FatSat (SPAIR / FS)** | Axial | TR 1500-2000 ms / TE 80 ms | 4.0 mm / gap 0.4 mm | FOV 300-350 mm / Matrice 256×224 | FatSat / SPAIR | Evidențiere edem periapendicular, infiltrare a grăsimii fosei iliace drepte și colecții lichidiene |
    | **Axial DWI (b=50, b=800) + hartă ADC** | Axial | TR 3000-4000 ms / TE 60-70 ms | 4.0 mm / gap 0.4 mm | FOV 300-350 mm / Matrice 128×128 | FatSat (EPI) | Hipersemnal b=800 în peretele apendicular și restricție pe ADC = semn înalt specific de apendicită supurată |
    | **Axial In-Phase / Out-of-Phase T1 GRE** | Axial | TR 150 ms / TE 2.2 / 4.4 ms (la 1.5T) | 4.0 mm / gap 0.4 mm | FOV 320 mm / Matrice 256×192 | Nu (Dual-echo) | Detectare apendicolit / fecalit (semnal negru pe ambele ecouri) și sânge subacut |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Identificarea apendicelui normal (diametru < 6 mm, perete fin < 2 mm, lumen colabat sau umplut cu gaz/lichid fără edem pericecal)
    - Dacă apendicele nu poate fi menționat ca normal, identificarea clară a semnelor pozitive: diametru > 7 mm, îngroșare parietală, edem T2 FS periapendicular, restricție DWI
    - Durată totală la aparat menținută sub 15-20 minute

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - La gravide: scanare exclusivă în mod SAR normal (< 2.0 W/kg)
    - Fără contrast pe bază de Gadoliniu
    - Evitarea apneei prelungite; secvențele SSFSE sunt achiziționate în respirație liberă sau apnee scurtă

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol oficial OHSU de primă intenție la gravide cu suspiciune de apendicită după ecografie, cu sensibilitate și specificitate > 95%.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
