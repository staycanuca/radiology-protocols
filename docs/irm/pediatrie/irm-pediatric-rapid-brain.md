---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Copii mici sau necooperanți cu toleranță scăzută la examinare (< 10-11 minute)
- Traumatism cranio-cerebral acut în urgență când se dorește evitarea iradierii prin
  CT
- Suspiciune de leziuni axonale difuze sau hemoragie intracraniană subacută
- Alterare acută a stării de conștiență / letargie de cauză neelucidată
- Screening neuro-pediatric rapid fără necesitatea anesteziei generale sau a sedării
coils_hardware:
  coil: Antenă dedicată Head/Neck multicanal (16–32 canale) cu pernuțe de imobilizare
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, cap centrat în izocentru, pernuțe moi laterale pentru
    prevenirea rotației
contraindications:
- Implanturi metalice feromagnetice sau dispozitive active non-MR Conditional
- Instabilitate hemodinamică sau respiratorie severă care necesită monitorizare invazivă
  de terapie intensivă
contrast:
  agent: Fără contrast (protocol nativ rapid)
  dose: N/A
  flow_rate: N/A
  notes: Examinare exclusiv nativă pentru reducerea timpului total la sub 10-11 minute.
  timing: N/A
iris_reference:
  chapter: Pediatrie - Sistem Nervos Central
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Standard internațional WFPI conceput pentru a oferi un diagnostic complet în
  10 minute, evitând sedarea și iradierea pediatrică.
patient_prep: Pregătire 'feed-and-wrap' pentru sugari (hrănire și înfășare înainte
  de scanare); căști audio cu muzică/povești pentru copii cooperanți; fără sedare
  medicamentoasă.
quality_criteria:
- Timp total de scanare la aparat menținut strict sub 11 minute
- Axial DWI și T2* fără artefacte severe de mișcare
- Vizualizare clară a ventriculilor și a fosei posterioare fără trunchiere anatomică
safety_considerations:
- Protecție fonică dublă obligatorie (căști fonoizolante + dopuri moi adaptate pediatric)
- Monitorizare vizuală permanentă și pulsoximetrie compatibilă RM
- SAR menținut în limite normale (< 2.0 W/kg)
sequences:
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 200-220 mm / 128x128
  name: Axial DWI (b=0, b=1000) + hartă ADC
  notes: Detectare ischemie acută, edem citotoxic, celularitate crescută (1-2 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3000-4000 ms / TE 60-80 ms
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / 256x192
  name: Axial EPI T2* / GRE
  notes: Sensibilitate înaltă la hemoragie acută/subacută, depuneri de hemosiderină
    (0.5 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 500-800 ms / TE 15-25 ms
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / 256x256
  name: Sagital T1WI TSE / SE
  notes: Anatomie linie mediană, corp calos, fosă posterioară, poziție amigdale cerebeloase
    (2-3 min)
  plane: Sagital
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 450-600 ms / TE 8-12 ms
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / 320x256
  name: Axial T2WI TSE
  notes: Diferențiere substanță albă/cenușie, edem vasogenic, mielinizare conform
    vârstei (2-3 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3500-4500 ms / TE 90-110 ms
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / 256x224
  name: Coronal FLAIR
  notes: Supresie semnal LCR, leziuni cortico-subcorticale, spații periventriculare
    (2-3 min)
  plane: Coronal
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 8000-9000 ms / TE 90-120 ms / TI 2200-2500 ms
slug: irm-pediatric-rapid-brain
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
title: RM Pediatric — Protocol Cerebral Rapid (Rapid Brain)
---
# RM Pediatric — Protocol Cerebral Rapid (Rapid Brain)

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

        - Copii mici sau necooperanți cu toleranță scăzută la examinare (< 10-11 minute)
        - Traumatism cranio-cerebral acut în urgență când se dorește evitarea iradierii prin CT
        - Suspiciune de leziuni axonale difuze sau hemoragie intracraniană subacută
        - Alterare acută a stării de conștiență / letargie de cauză neelucidată
        - Screening neuro-pediatric rapid fără necesitatea anesteziei generale sau a sedării

    === "Contraindicații & Screening Metalic"

        - Implanturi metalice feromagnetice sau dispozitive active non-MR Conditional
        - Instabilitate hemodinamică sau respiratorie severă care necesită monitorizare invazivă de terapie intensivă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Sistem Nervos Central*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Pregătire 'feed-and-wrap' pentru sugari (hrănire și înfășare înainte de scanare); căști audio cu muzică/povești pentru copii cooperanți; fără sedare medicamentoasă.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată Head/Neck multicanal (16–32 canale) cu pernuțe de imobilizare
    - **Poziție Pacient & Centrare:** Decubit dorsal, cap centrat în izocentru, pernuțe moi laterale pentru prevenirea rotației

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Fără contrast (protocol nativ rapid)
    - **Doză Recomandată:** N/A
    - **Rată de Injectare (Debit):** N/A
    - **Temporizare & Faze Dinamice:** N/A
    - **Filtrare Renală & Precauții:** Examinare exclusiv nativă pentru reducerea timpului total la sub 10-11 minute.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Axial DWI (b=0, b=1000) + hartă ADC** | Axial | TR 3000-4000 ms / TE 60-80 ms | 4.0 mm / gap 0.4 mm | FOV 200-220 mm / 128x128 | FatSat (EPI) | Detectare ischemie acută, edem citotoxic, celularitate crescută (1-2 min) |
    | **Axial EPI T2* / GRE** | Axial | TR 500-800 ms / TE 15-25 ms | 4.0 mm / gap 0.4 mm | FOV 200-220 mm / 256x192 | Nu | Sensibilitate înaltă la hemoragie acută/subacută, depuneri de hemosiderină (0.5 min) |
    | **Sagital T1WI TSE / SE** | Sagital | TR 450-600 ms / TE 8-12 ms | 4.0 mm / gap 0.4 mm | FOV 200-220 mm / 256x256 | Nu | Anatomie linie mediană, corp calos, fosă posterioară, poziție amigdale cerebeloase (2-3 min) |
    | **Axial T2WI TSE** | Axial | TR 3500-4500 ms / TE 90-110 ms | 4.0 mm / gap 0.4 mm | FOV 200-220 mm / 320x256 | Nu | Diferențiere substanță albă/cenușie, edem vasogenic, mielinizare conform vârstei (2-3 min) |
    | **Coronal FLAIR** | Coronal | TR 8000-9000 ms / TE 90-120 ms / TI 2200-2500 ms | 4.0 mm / gap 0.4 mm | FOV 200-220 mm / 256x224 | Nu | Supresie semnal LCR, leziuni cortico-subcorticale, spații periventriculare (2-3 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de scanare la aparat menținut strict sub 11 minute
    - Axial DWI și T2* fără artefacte severe de mișcare
    - Vizualizare clară a ventriculilor și a fosei posterioare fără trunchiere anatomică

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Protecție fonică dublă obligatorie (căști fonoizolante + dopuri moi adaptate pediatric)
    - Monitorizare vizuală permanentă și pulsoximetrie compatibilă RM
    - SAR menținut în limite normale (< 2.0 W/kg)

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Standard internațional WFPI conceput pentru a oferi un diagnostic complet în 10 minute, evitând sedarea și iradierea pediatrică.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
