---
author: Departamentul de Radiologie și Imagistică Medicală
category: abdomen-pelvis
clinical_indications:
- Suspiciune sau bilanț de endometrioză pelvină profundă (ligamente utero-sacrate,
  sept recto-vaginal, vezică, rect)
- Dismenoree severă, dispareunie profundă, dischezie și infertilitate
- Stadializare cancer de col uterin (extensie parametrială) și cancer de endometru
  (invazie miometrială)
- Caracterizarea maselor ovariene complexe conform scorului O-RADS MRI
- Cartografiere fibromatoză uterină (miometrectomie vs. embolizare artere uterine)
coils_hardware:
  coil: Antenă Phased-Array Pelvis multicanal
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, centrare pe simfiza pubiană.
contraindications:
- Contraindicații generale RM.
contrast:
  agent: Chelat de Gadoliniu macrociclic
  dose: 0.1 mmol/kg corp
  flow_rate: 2.0 ml/s
  notes: În endometrioză nativul T1 cu și fără FatSat este critic pentru sângerările
    subacute; contrastul este util în adenocarcinom și diferențiere leziuni ovariene.
  timing: 3D T1 FatSat dinamic precoce și tardiv
iris_reference:
  chapter: Ginecologie & Pelvis Feminin - Endometrioză și Neoplasme
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Semnul 'kissing ovaries' (ovare alipite pe linia mediană posterior de uter)
  indică aderențe pelvine severe și obliterarea fundului de sac Douglas.
patient_prep: À jeun 4 ore; vezică urinară în semi-repleție (nu complet destinsă pentru
  a nu împinge uterul posterior); administrare Buscopan 20 mg IV pentru imobilizarea
  anselor sigmoidiene; opțional gel ultrasonografic opacifiant steril 50-100 ml vaginal
  și 100-150 ml rectal pentru distensia cavităților și evidențierea infiltrației septale.
quality_criteria:
- Delimitare netă a zonei joncționale miometriale și a faldurilor seroase peritoneale
- Oprirea motilității rectale și uterine prin administrarea antispasticului
safety_considerations:
- Nu se efectuează în timpul menstruației abundente dacă nu este urgent
sequences:
- fat_sat: Nu
  fov_matrix: FOV 200 mm / 384x288
  name: Sagital T2 TSE de Înaltă Rezoluție
  notes: Secvență de referință pentru fund de sac Douglas, sept recto-vaginal, perete
    rectal anterior
  plane: Sagital axat pe uter și canal anal
  slice_gap: 3.5 mm / gap 0.3 mm
  tr_te: TR 4500 ms / TE 105 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / 384x256
  name: Axial T2 TSE oblic (perpendicular pe cavitatea uterină)
  notes: Ligamente utero-sacrate, torul uterin, parametre, ovare
  plane: Axial oblic
  slice_gap: 3.5 mm / gap 0.3 mm
  tr_te: TR 4000 ms / TE 100 ms
- fat_sat: Nu
  fov_matrix: FOV 240 mm / 320x256
  name: Axial T1 SE / TSE Nativ
  notes: Hipersemnal în chisturi endometrizice (endometrioame) și sângerări vechi
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 600 ms / TE 10 ms
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 240 mm / 320x256
  name: Axial T1 FatSat
  notes: Diferențiere chist dermoid/teratom (semnal stins pe FatSat) de endometriom
    (semnal persistent înalt)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 600 ms / TE 10 ms
- fat_sat: FatSat
  fov_matrix: FOV 240 mm / 192x160
  name: Axial DWI (b=0, 800) + ADC
  notes: Caracterizare noduli solizi ovarieni și stadializare neoplasm col/endometru
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 4500 ms / TE 70 ms
slug: irm-pelvis-feminin-si-endometrioza
title: IRM Pelvis Feminin & Endometrioză Profundă Infiltrativă (DIE)
---
# IRM Pelvis Feminin & Endometrioză Profundă Infiltrativă (DIE)

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

        - Suspiciune sau bilanț de endometrioză pelvină profundă (ligamente utero-sacrate, sept recto-vaginal, vezică, rect)
        - Dismenoree severă, dispareunie profundă, dischezie și infertilitate
        - Stadializare cancer de col uterin (extensie parametrială) și cancer de endometru (invazie miometrială)
        - Caracterizarea maselor ovariene complexe conform scorului O-RADS MRI
        - Cartografiere fibromatoză uterină (miometrectomie vs. embolizare artere uterine)

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale RM.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Ginecologie & Pelvis Feminin - Endometrioză și Neoplasme*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** À jeun 4 ore; vezică urinară în semi-repleție (nu complet destinsă pentru a nu împinge uterul posterior); administrare Buscopan 20 mg IV pentru imobilizarea anselor sigmoidiene; opțional gel ultrasonografic opacifiant steril 50-100 ml vaginal și 100-150 ml rectal pentru distensia cavităților și evidențierea infiltrației septale.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Phased-Array Pelvis multicanal
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe simfiza pubiană.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic
    - **Doză Recomandată:** 0.1 mmol/kg corp
    - **Rată de Injectare (Debit):** 2.0 ml/s
    - **Temporizare & Faze Dinamice:** 3D T1 FatSat dinamic precoce și tardiv
    - **Filtrare Renală & Precauții:** În endometrioză nativul T1 cu și fără FatSat este critic pentru sângerările subacute; contrastul este util în adenocarcinom și diferențiere leziuni ovariene.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T2 TSE de Înaltă Rezoluție** | Sagital axat pe uter și canal anal | TR 4500 ms / TE 105 ms | 3.5 mm / gap 0.3 mm | FOV 200 mm / 384x288 | Nu | Secvență de referință pentru fund de sac Douglas, sept recto-vaginal, perete rectal anterior |
    | **Axial T2 TSE oblic (perpendicular pe cavitatea uterină)** | Axial oblic | TR 4000 ms / TE 100 ms | 3.5 mm / gap 0.3 mm | FOV 200 mm / 384x256 | Nu | Ligamente utero-sacrate, torul uterin, parametre, ovare |
    | **Axial T1 SE / TSE Nativ** | Axial | TR 600 ms / TE 10 ms | 4.0 mm / gap 0.4 mm | FOV 240 mm / 320x256 | Nu | Hipersemnal în chisturi endometrizice (endometrioame) și sângerări vechi |
    | **Axial T1 FatSat** | Axial | TR 600 ms / TE 10 ms | 4.0 mm / gap 0.4 mm | FOV 240 mm / 320x256 | FatSat / SPAIR | Diferențiere chist dermoid/teratom (semnal stins pe FatSat) de endometriom (semnal persistent înalt) |
    | **Axial DWI (b=0, 800) + ADC** | Axial | TR 4500 ms / TE 70 ms | 4.0 mm / gap 0.4 mm | FOV 240 mm / 192x160 | FatSat | Caracterizare noduli solizi ovarieni și stadializare neoplasm col/endometru |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Delimitare netă a zonei joncționale miometriale și a faldurilor seroase peritoneale
    - Oprirea motilității rectale și uterine prin administrarea antispasticului

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Nu se efectuează în timpul menstruației abundente dacă nu este urgent

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Semnul 'kissing ovaries' (ovare alipite pe linia mediană posterior de uter) indică aderențe pelvine severe și obliterarea fundului de sac Douglas.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
