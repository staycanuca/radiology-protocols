---
author: Departamentul de Radiologie și Imagistică Medicală
category: abdomen-pelvis
clinical_indications:
- Icter mecanic obstructiv (diferențiere litiază coledociană vs. stenoză tumorală)
- Suspiciune de coledocolitiază cu ecografie neconcludentă
- Stadializare colangiocarcinom (tumoare Klatskin) și neoplasm de cap de pancreas
- Colangită sclerozantă primitivă (CSP) - diagnostic și monitorizare stricturi
- Anomalii congenitale ale arborelui biliar (chist de coledoc, pancreas divisum)
coils_hardware:
  coil: Antenă Phased-Array Abdomen 16-32 canale
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, centrare pe rebordul costal drept.
contraindications:
- Contraindicații generale de securitate RM.
contrast:
  agent: Nativ (tehnică puternic hidroponderată T2 bazată pe proprietatea lichidului
    biliar staționar de a avea un timp T2 foarte lung). Substanță de contrast IV paramagnetică
    se asociază doar dacă se suspectează o masă tumorală pancreatică sau hepatică
    asociată.
  dose: 0 ml de rutină (sau 0.1 mmol/kg dacă se asociază bilanț tumoral)
  flow_rate: Nu este cazul
  notes: MRCP este o procedură complet non-invazivă, înlocuind ERCP diagnostică care
    are risc de pancreatită post-procedurală de 3-5%.
  timing: Nu este cazul
iris_reference:
  chapter: Căi Biliare & Pancreas - Icter Mecanic
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Calculii biliari apar caracteristic ca defecte de umplere cu semnal negru (hiposemnal)
  înconjurate de bila hiperintensă T2.
patient_prep: À jeun strict 6-8 ore pentru golirea stomacului și reținerea bilei în
  veziculă; administrare per os de 100-150 ml suc de ananas sau afine (bogat în mangan)
  cu 15 min înainte de examinare ca agent de contrast negativ natural pentru stingerea
  semnalului T2 din stomac și duoden.
quality_criteria:
- Semnal intens alb strălucitor al căilor biliare intra- și extrahepatice și al canalului
  pancreatic
- Supresie completă a grăsimii și a lichidului digestiv suprapus
- Absența artefactelor de respirație prin utilizarea triggerului respirator adecvat
safety_considerations:
- Complet non-invaziv, fără risc de pancreatită acută iatrogenă
sequences:
- fat_sat: Nu
  fov_matrix: FOV 360 mm / 320x256
  name: Coronal T2 HASTE / SSFSE câmp mare
  notes: Vedere de ansamblu hipocondru drept, ficat, stomac
  plane: Coronal
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: Single-shot / TE 90 ms
- fat_sat: FatSat
  fov_matrix: FOV 350 mm / 320x256
  name: Axial T2 FatSat subțire
  notes: Coledoc distal intrapancreatic, ampulă Vater, canal Wirsung
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: Gating respirator / TE 85 ms
- fat_sat: FatSat
  fov_matrix: FOV 280 mm / 384x288
  name: MRCP Gros Radiale Single-Shot (Thick-Slab)
  notes: Imagine 'colangiografică' de proiecție instantanee a întregului arbore
  plane: Radiale oblice centrate pe coledoc (la fiecare 15°)
  slice_gap: Grosime 30 - 40 mm (o singură secțiune groasă)
  tr_te: TR 4500 ms / TE 700 - 800 ms (ultra-T2)
- fat_sat: FatSat / SPAIR
  fov_matrix: FOV 300 mm / 320x320
  name: 3D MRCP Subțire de Înaltă Rezoluție (Navigated / Triggered)
  notes: Gold standard pentru calculi milimetrici și stenoze fine
  plane: Coronal oblic 3D volumetric
  slice_gap: 1.0 mm izotrop reconstruibil multiplanar
  tr_te: TR 2500 ms / TE 550 ms
slug: colangio-irm-mrcp
title: Colangio-IRM (MRCP) - Evaluare Non-invazivă a Căilor Biliare
---
# Colangio-IRM (MRCP) - Evaluare Non-invazivă a Căilor Biliare

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

        - Icter mecanic obstructiv (diferențiere litiază coledociană vs. stenoză tumorală)
        - Suspiciune de coledocolitiază cu ecografie neconcludentă
        - Stadializare colangiocarcinom (tumoare Klatskin) și neoplasm de cap de pancreas
        - Colangită sclerozantă primitivă (CSP) - diagnostic și monitorizare stricturi
        - Anomalii congenitale ale arborelui biliar (chist de coledoc, pancreas divisum)

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale de securitate RM.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Căi Biliare & Pancreas - Icter Mecanic*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** À jeun strict 6-8 ore pentru golirea stomacului și reținerea bilei în veziculă; administrare per os de 100-150 ml suc de ananas sau afine (bogat în mangan) cu 15 min înainte de examinare ca agent de contrast negativ natural pentru stingerea semnalului T2 din stomac și duoden.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Phased-Array Abdomen 16-32 canale
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe rebordul costal drept.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ (tehnică puternic hidroponderată T2 bazată pe proprietatea lichidului biliar staționar de a avea un timp T2 foarte lung). Substanță de contrast IV paramagnetică se asociază doar dacă se suspectează o masă tumorală pancreatică sau hepatică asociată.
    - **Doză Recomandată:** 0 ml de rutină (sau 0.1 mmol/kg dacă se asociază bilanț tumoral)
    - **Rată de Injectare (Debit):** Nu este cazul
    - **Temporizare & Faze Dinamice:** Nu este cazul
    - **Filtrare Renală & Precauții:** MRCP este o procedură complet non-invazivă, înlocuind ERCP diagnostică care are risc de pancreatită post-procedurală de 3-5%.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T2 HASTE / SSFSE câmp mare** | Coronal | Single-shot / TE 90 ms | 4.0 mm / gap 0.4 mm | FOV 360 mm / 320x256 | Nu | Vedere de ansamblu hipocondru drept, ficat, stomac |
    | **Axial T2 FatSat subțire** | Axial | Gating respirator / TE 85 ms | 4.0 mm / gap 0.4 mm | FOV 350 mm / 320x256 | FatSat | Coledoc distal intrapancreatic, ampulă Vater, canal Wirsung |
    | **MRCP Gros Radiale Single-Shot (Thick-Slab)** | Radiale oblice centrate pe coledoc (la fiecare 15°) | TR 4500 ms / TE 700 - 800 ms (ultra-T2) | Grosime 30 - 40 mm (o singură secțiune groasă) | FOV 280 mm / 384x288 | FatSat | Imagine 'colangiografică' de proiecție instantanee a întregului arbore |
    | **3D MRCP Subțire de Înaltă Rezoluție (Navigated / Triggered)** | Coronal oblic 3D volumetric | TR 2500 ms / TE 550 ms | 1.0 mm izotrop reconstruibil multiplanar | FOV 300 mm / 320x320 | FatSat / SPAIR | Gold standard pentru calculi milimetrici și stenoze fine |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Semnal intens alb strălucitor al căilor biliare intra- și extrahepatice și al canalului pancreatic
    - Supresie completă a grăsimii și a lichidului digestiv suprapus
    - Absența artefactelor de respirație prin utilizarea triggerului respirator adecvat

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Complet non-invaziv, fără risc de pancreatită acută iatrogenă

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Calculii biliari apar caracteristic ca defecte de umplere cu semnal negru (hiposemnal) înconjurate de bila hiperintensă T2.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
