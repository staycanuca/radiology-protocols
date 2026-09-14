---
author: Departamentul de Radiologie și Imagistică Medicală
category: neuro
clinical_indications:
- Deficit neurologic acut în fereastră terapeutică de tromboliză / trombectomie (<
  4.5h - 24h)
- Wake-up stroke (accident vascular cerebral cu oră de debut necunoscută - mismatch
  DWI-FLAIR)
- Suspiciune de ocluzie de vas mare intracranian (LVO)
- Diagnostic diferențial stroke-mimic (migrenă cu aură, criză epileptică post-ictală
  Todd, hipoglicemie)
coils_hardware:
  coil: Antenă Head 32 canale
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, centrare nasion, cap fixat pentru evitarea mișcării.
contraindications:
- Instabilitate hemodinamică sau respiratorie severă incompatibilă cu sala RM
- Prezența implanturilor feromagnetice nesigure RM
contrast:
  agent: Nativ (fără contrast obligatoriu pentru mismatch) sau 0.1 mmol/kg Gd dacă
    se efectuează perfuzie PWI
  dose: 0.1 mmol/kg (opțional perfuzie)
  flow_rate: 4.0 - 5.0 ml/s pentru perfuzie dinamică DSC
  notes: Mismatch DWI/FLAIR permite selecția pacienților pentru tromboliză în wake-up
    stroke fără a necesita contrast.
  timing: DSC-PWI cu urmărire bolus
iris_reference:
  chapter: Neurologie de Urgență - AVC Ischemic
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Dacă există mismatch DWI-FLAIR (DWI pozitiv, FLAIR negativ), pacientul beneficiază
  de tromboliză chiar dacă ora debutului este necunoscută.
patient_prep: Protocol ultra-rapid 'Code Stroke' (< 10-15 minute); monitorizare TA
  și SpO2 compatibile RM; verificare rapidă a absenței protezelor cardiace non-RM.
quality_criteria:
- Timp total de scanare 'door-to-image' sub 12-15 minute
- Hărți ADC calculate automat și disponibile instantaneu pe consola PACS
- MIP 3D TOF generat automat pentru orientarea echipei de neuroradiologie intervențională
safety_considerations:
- Monitorizare electrocardiografică și pulsoximetrică continuă compatibilă RM
- Personal antrenat pentru transfer rapid la masa de angiografie intervențională în
  caz de trombectomie
sequences:
- fat_sat: FatSat
  fov_matrix: FOV 230 mm / 192x192
  name: DWI (b=0, b=1000) + ADC Map (Ultra-fast)
  notes: Core ischemic citotoxic precoce (minute de la debut)
  plane: Axial
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 3000 ms / TE 65 ms
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 256x224
  name: Axial FLAIR
  notes: 'Evaluare mismatch: leziune DWI pozitivă + FLAIR negativă = debut < 4.5 ore'
  plane: Axial
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 9000 ms / TE 90 ms / TI 2500 ms
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 256x256
  name: Axial T2* GRE / SWI
  notes: Excludere absolută a hemoragiei intracraniene și semn de trombus intraluminal
    (susceptibility sign)
  plane: Axial
  slice_gap: 4.0 mm / gap 0 mm
  tr_te: TR 600 ms / TE 20 ms
- fat_sat: TONE ramp pulse
  fov_matrix: FOV 200 mm / 384x256
  name: 3D TOF MRA Poligon Willis
  notes: Identificare ocluzie arteră cerebrală medie (M1/M2), arteră carotidă internă
    terminală sau trunchi bazilar
  plane: 3D Axial
  slice_gap: 0.6 - 0.7 mm subțire
  tr_te: TR 22 ms / TE 3.5 ms / FA 18°
slug: irm-cerebral-stroke-ischemie
title: IRM Cerebral Urgență - Protocol AVC Ischemic Acut (Stroke)
---
# IRM Cerebral Urgență - Protocol AVC Ischemic Acut (Stroke)

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

        - Deficit neurologic acut în fereastră terapeutică de tromboliză / trombectomie (< 4.5h - 24h)
        - Wake-up stroke (accident vascular cerebral cu oră de debut necunoscută - mismatch DWI-FLAIR)
        - Suspiciune de ocluzie de vas mare intracranian (LVO)
        - Diagnostic diferențial stroke-mimic (migrenă cu aură, criză epileptică post-ictală Todd, hipoglicemie)

    === "Contraindicații & Screening Metalic"

        - Instabilitate hemodinamică sau respiratorie severă incompatibilă cu sala RM
        - Prezența implanturilor feromagnetice nesigure RM

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Neurologie de Urgență - AVC Ischemic*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Protocol ultra-rapid 'Code Stroke' (< 10-15 minute); monitorizare TA și SpO2 compatibile RM; verificare rapidă a absenței protezelor cardiace non-RM.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Head 32 canale
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare nasion, cap fixat pentru evitarea mișcării.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ (fără contrast obligatoriu pentru mismatch) sau 0.1 mmol/kg Gd dacă se efectuează perfuzie PWI
    - **Doză Recomandată:** 0.1 mmol/kg (opțional perfuzie)
    - **Rată de Injectare (Debit):** 4.0 - 5.0 ml/s pentru perfuzie dinamică DSC
    - **Temporizare & Faze Dinamice:** DSC-PWI cu urmărire bolus
    - **Filtrare Renală & Precauții:** Mismatch DWI/FLAIR permite selecția pacienților pentru tromboliză în wake-up stroke fără a necesita contrast.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **DWI (b=0, b=1000) + ADC Map (Ultra-fast)** | Axial | TR 3000 ms / TE 65 ms | 4.0 mm / gap 0 mm | FOV 230 mm / 192x192 | FatSat | Core ischemic citotoxic precoce (minute de la debut) |
    | **Axial FLAIR** | Axial | TR 9000 ms / TE 90 ms / TI 2500 ms | 4.0 mm / gap 0 mm | FOV 230 mm / 256x224 | Nu | Evaluare mismatch: leziune DWI pozitivă + FLAIR negativă = debut < 4.5 ore |
    | **Axial T2* GRE / SWI** | Axial | TR 600 ms / TE 20 ms | 4.0 mm / gap 0 mm | FOV 230 mm / 256x256 | Nu | Excludere absolută a hemoragiei intracraniene și semn de trombus intraluminal (susceptibility sign) |
    | **3D TOF MRA Poligon Willis** | 3D Axial | TR 22 ms / TE 3.5 ms / FA 18° | 0.6 - 0.7 mm subțire | FOV 200 mm / 384x256 | TONE ramp pulse | Identificare ocluzie arteră cerebrală medie (M1/M2), arteră carotidă internă terminală sau trunchi bazilar |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de scanare 'door-to-image' sub 12-15 minute
    - Hărți ADC calculate automat și disponibile instantaneu pe consola PACS
    - MIP 3D TOF generat automat pentru orientarea echipei de neuroradiologie intervențională

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Monitorizare electrocardiografică și pulsoximetrică continuă compatibilă RM
    - Personal antrenat pentru transfer rapid la masa de angiografie intervențională în caz de trombectomie

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Dacă există mismatch DWI-FLAIR (DWI pozitiv, FLAIR negativ), pacientul beneficiază de tromboliză chiar dacă ora debutului este necunoscută.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
