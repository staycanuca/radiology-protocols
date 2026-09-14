---
author: Departamentul de Radiologie și Imagistică Medicală
category: san
clinical_indications:
- Screening la femei cu risc înalt genetic (mutații BRCA1, BRCA2, istoric familial
  marcat)
- Stadializare loco-regională cancer mamar nou diagnosticat (evaluare multifocalitate,
  multicentricitate, bilateralitate)
- Evaluare răspuns la chimioterapie neoadjuvantă (monitorizare reducere volum tumoral)
- Suspiciune de recidivă tumorală pe cicatrice post-operatorie
- Carcinom ocult cu metastază ganglionară axilară și mamografie/ecografie negative
- Evaluarea integrității implantelor mamare (ruptură intracapsulară / extracapsulară)
coils_hardware:
  coil: Antenă mamară dedicată multicanal (Bilateral Breast Coil 8-16 canale)
  field_strength: 1.5T sau 3.0T
  positioning: Decubit ventral (prone), ambii sâni coborâți liber în cupele antenei
    fără compresie excesivă.
contraindications:
- Contraindicații generale RM; sarcină (contraindicație relativă la Gadoliniu); eGFR
  < 30 ml/min.
contrast:
  agent: Chelat de Gadoliniu macrociclic
  dose: 0.1 mmol/kg corp
  flow_rate: 2.0 - 2.5 ml/s cu injector automat + 20-30 ml ser fiziologic
  notes: Generarea automată a imaginilor de substracție (post-contrast minus pre-contrast)
    și a curbelor cinetice (Tip I progresivă, Tip II platou, Tip III wash-out).
  timing: Achiziție dinamică rapidă pre-contrast și post-contrast în 5-6 faze consecutive
    la fiecare 60-90 secunde timp de minimum 6-7 minute
iris_reference:
  chapter: Senologie - Diagnostic și Screening Mamar
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Curba cinetică de tip III (wash-out rapid precoce) are specificitate de peste
  85-90% pentru carcinom invaziv. Leziunile se clasifică conform categoriilor BI-RADS
  MRI (1 la 6).
patient_prep: Programare optimă în zilele 7 - 14 ale ciclului menstrual (faza foliculară)
  pentru minimalizarea captării hormonale fiziologice de fond (BPE - background parenchymal
  enhancement); cateter venos 20G montat în antebraț cu prelungitor lung pentru injectare
  din exterior.
quality_criteria:
- Poziționare impecabilă a ambilor sâni fără plicaturare cutanată sau contact cu marginea
  antenei
- Supresie de grăsime perfect omogenă bilateral pe secvențele dinamice
- Calcularea obligatorie a curbelor cinetice intensitate-timp pe stația de post-procesare
  dedicată
safety_considerations:
- SAR bine tolerat pe bobină dedicată
- Pentru evaluarea rupturii de implant mamar siliconic se rulează secvențe suplimentare
  dedicate de supresie a apei și supresie a grăsimii (secvență 'Silicon Only')
sequences:
- fat_sat: Nu
  fov_matrix: FOV 340 mm / 384x320
  name: Axial T2 TSE de Înaltă Rezoluție
  notes: Chisturi, fibroadenoame (hipersemnal T2), edem cutanat, arhitectură glandulară
  plane: Axial bilateral
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4500 ms / TE 100 ms
- fat_sat: FatSat
  fov_matrix: FOV 340 mm / 192x160
  name: Axial DWI (b=0, 800-1000) + ADC Map
  notes: Restricție de difuzie corelată cu celularitatea înaltă din leziuni maligne
  plane: Axial bilateral
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4500 ms / TE 60 ms
- fat_sat: Nu
  fov_matrix: FOV 340 mm / 384x256
  name: Axial T1 Nativ Fără FatSat
  notes: Cartografiere anatomie și diferențiere sângerare/chist hemoragic
  plane: Axial
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 600 ms / TE 10 ms
- fat_sat: Dixon / FatSat
  fov_matrix: FOV 340 mm / 384x384
  name: 3D T1 GRE Dinamic multipfazic cu supresie de grăsime
  notes: 1 fază nativă + 5 faze post-contrast seriate la 60-90s; substracție automată
  plane: Axial bilateral (apnee sau respirație superficială)
  slice_gap: 1.0 - 1.5 mm izotrop
  tr_te: TR 4.5 ms / TE 1.7 ms / FA 12°
- fat_sat: FatSat
  fov_matrix: FOV 200 mm / 320x256
  name: Sagital T1 + C de Înaltă Rezoluție (pe sânul afectat)
  notes: Evaluare detaliată a extensiei ductale și a distanței față de mamelon și
    mușchiul pectoral
  plane: Sagital unilateral
  slice_gap: 2.5 mm / gap 0 mm
  tr_te: TR 550 ms / TE 10 ms
slug: irm-mamar-bilateral-cu-contrast
title: IRM Mamar Bilateral cu Substanță de Contrast - Protocol BI-RADS
---
# IRM Mamar Bilateral cu Substanță de Contrast - Protocol BI-RADS

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

        - Screening la femei cu risc înalt genetic (mutații BRCA1, BRCA2, istoric familial marcat)
        - Stadializare loco-regională cancer mamar nou diagnosticat (evaluare multifocalitate, multicentricitate, bilateralitate)
        - Evaluare răspuns la chimioterapie neoadjuvantă (monitorizare reducere volum tumoral)
        - Suspiciune de recidivă tumorală pe cicatrice post-operatorie
        - Carcinom ocult cu metastază ganglionară axilară și mamografie/ecografie negative
        - Evaluarea integrității implantelor mamare (ruptură intracapsulară / extracapsulară)

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM; sarcină (contraindicație relativă la Gadoliniu); eGFR < 30 ml/min.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Senologie - Diagnostic și Screening Mamar*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Programare optimă în zilele 7 - 14 ale ciclului menstrual (faza foliculară) pentru minimalizarea captării hormonale fiziologice de fond (BPE - background parenchymal enhancement); cateter venos 20G montat în antebraț cu prelungitor lung pentru injectare din exterior.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă mamară dedicată multicanal (Bilateral Breast Coil 8-16 canale)
    - **Poziție Pacient & Centrare:** Decubit ventral (prone), ambii sâni coborâți liber în cupele antenei fără compresie excesivă.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic
    - **Doză Recomandată:** 0.1 mmol/kg corp
    - **Rată de Injectare (Debit):** 2.0 - 2.5 ml/s cu injector automat + 20-30 ml ser fiziologic
    - **Temporizare & Faze Dinamice:** Achiziție dinamică rapidă pre-contrast și post-contrast în 5-6 faze consecutive la fiecare 60-90 secunde timp de minimum 6-7 minute
    - **Filtrare Renală & Precauții:** Generarea automată a imaginilor de substracție (post-contrast minus pre-contrast) și a curbelor cinetice (Tip I progresivă, Tip II platou, Tip III wash-out).

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Axial T2 TSE de Înaltă Rezoluție** | Axial bilateral | TR 4500 ms / TE 100 ms | 3.0 mm / gap 0 mm | FOV 340 mm / 384x320 | Nu | Chisturi, fibroadenoame (hipersemnal T2), edem cutanat, arhitectură glandulară |
    | **Axial DWI (b=0, 800-1000) + ADC Map** | Axial bilateral | TR 4500 ms / TE 60 ms | 3.0 mm / gap 0 mm | FOV 340 mm / 192x160 | FatSat | Restricție de difuzie corelată cu celularitatea înaltă din leziuni maligne |
    | **Axial T1 Nativ Fără FatSat** | Axial | TR 600 ms / TE 10 ms | 3.0 mm / gap 0 mm | FOV 340 mm / 384x256 | Nu | Cartografiere anatomie și diferențiere sângerare/chist hemoragic |
    | **3D T1 GRE Dinamic multipfazic cu supresie de grăsime** | Axial bilateral (apnee sau respirație superficială) | TR 4.5 ms / TE 1.7 ms / FA 12° | 1.0 - 1.5 mm izotrop | FOV 340 mm / 384x384 | Dixon / FatSat | 1 fază nativă + 5 faze post-contrast seriate la 60-90s; substracție automată |
    | **Sagital T1 + C de Înaltă Rezoluție (pe sânul afectat)** | Sagital unilateral | TR 550 ms / TE 10 ms | 2.5 mm / gap 0 mm | FOV 200 mm / 320x256 | FatSat | Evaluare detaliată a extensiei ductale și a distanței față de mamelon și mușchiul pectoral |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Poziționare impecabilă a ambilor sâni fără plicaturare cutanată sau contact cu marginea antenei
    - Supresie de grăsime perfect omogenă bilateral pe secvențele dinamice
    - Calcularea obligatorie a curbelor cinetice intensitate-timp pe stația de post-procesare dedicată

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR bine tolerat pe bobină dedicată
    - Pentru evaluarea rupturii de implant mamar siliconic se rulează secvențe suplimentare dedicate de supresie a apei și supresie a grăsimii (secvență 'Silicon Only')

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Curba cinetică de tip III (wash-out rapid precoce) are specificitate de peste 85-90% pentru carcinom invaziv. Leziunile se clasifică conform categoriilor BI-RADS MRI (1 la 6).

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
