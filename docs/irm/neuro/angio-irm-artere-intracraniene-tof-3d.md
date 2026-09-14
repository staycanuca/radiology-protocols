---
author: Departamentul de Radiologie și Imagistică Medicală
category: neuro
clinical_indications:
- Screening și monitorizare anevrisme arteriale intracraniene
- Evaluare malformații arterio-venoase (MAV) și fistule durale
- Diagnostic stenoză / ocluzie aterosclerotică a arterelor cerebrale mari
- Cefalee acută brusc instalată (excludere anevrism fisurat / disecție arterială)
coils_hardware:
  coil: Antenă Head 32 sau 64 canale
  field_strength: 1.5T sau 3.0T (3T oferă rezoluție și SNR net superioare pentru ramurile
    distale)
  positioning: Decubit dorsal, centrare pe conductele auditive externe.
contraindications:
- Contraindicații generale de securitate RM (implanturi feromagnetice, pacemaker non-RM)
contrast:
  agent: Fără substanță de contrast (tehnică Time-of-Flight bazată pe flux sanguin
    nativ)
  dose: 0 ml
  flow_rate: Nu este cazul
  notes: Secvența 3D TOF se bazează pe efectul de inflow al spinilor sangvini nesaturați
    care pătrund în volumul de scanare.
  timing: Nu este cazul
iris_reference:
  chapter: Vascular Cerebral - Angio-RM
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: Pentru anevrisme mici (< 3 mm) sau disecții, se examinează secțiunile native
  subțiri de 0.5 mm, nu doar reconstrucțiile MIP.
patient_prep: Chestionar de securitate RM; pacientul este rugat să stea perfect nemișcat
  și să evite deglutiția frecventă în timpul achiziției.
quality_criteria:
- Reconstrucții MIP (Maximum Intensity Projection) radiale rotative la fiecare 15-30°
- Vizualizare clară a arterelor comunicantă anterioară (ACom) și posterioare (PCom)
- Absența artefactelor de mișcare (ghosting) sau saturație pe flux lent
safety_considerations:
- SAR limitat în mod normal
- 'Atenție la clipuri de anevrism preexistente: necesară confirmarea fișei de implant
  non-feromagnetic'
sequences:
- fat_sat: Filtrare TONE / Magnetization Transfer
  fov_matrix: FOV 200 mm / Matrice 448x320
  name: 3D TOF (Time-of-Flight) MRA Poligon Willis
  notes: Bandă de saturație presaturație venoasă superioară pentru suprimarea fluxului
    din sinusul sagital
  plane: 3D Transversal cu plăci suprapuse (MOTSA)
  slice_gap: Grosime efectivă strat 0.5 - 0.6 mm
  tr_te: TR 23 ms / TE 3.4 ms / FA 18-20°
- fat_sat: Nu
  fov_matrix: FOV 230 mm / 320x256
  name: Axial T2 TSE
  notes: Confirmare semnal 'flow-void' normal în lumenul arterial
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 4500 ms / TE 95 ms
slug: angio-irm-artere-intracraniene-tof-3d
title: Angio-IRM Artere Intracraniene (3D TOF fără contrast)
---
# Angio-IRM Artere Intracraniene (3D TOF fără contrast)

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

        - Screening și monitorizare anevrisme arteriale intracraniene
        - Evaluare malformații arterio-venoase (MAV) și fistule durale
        - Diagnostic stenoză / ocluzie aterosclerotică a arterelor cerebrale mari
        - Cefalee acută brusc instalată (excludere anevrism fisurat / disecție arterială)

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale de securitate RM (implanturi feromagnetice, pacemaker non-RM)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Vascular Cerebral - Angio-RM*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Chestionar de securitate RM; pacientul este rugat să stea perfect nemișcat și să evite deglutiția frecventă în timpul achiziției.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T (3T oferă rezoluție și SNR net superioare pentru ramurile distale)
    - **Antenă de Recepție (Coil):** Antenă Head 32 sau 64 canale
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe conductele auditive externe.

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Fără substanță de contrast (tehnică Time-of-Flight bazată pe flux sanguin nativ)
    - **Doză Recomandată:** 0 ml
    - **Rată de Injectare (Debit):** Nu este cazul
    - **Temporizare & Faze Dinamice:** Nu este cazul
    - **Filtrare Renală & Precauții:** Secvența 3D TOF se bazează pe efectul de inflow al spinilor sangvini nesaturați care pătrund în volumul de scanare.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **3D TOF (Time-of-Flight) MRA Poligon Willis** | 3D Transversal cu plăci suprapuse (MOTSA) | TR 23 ms / TE 3.4 ms / FA 18-20° | Grosime efectivă strat 0.5 - 0.6 mm | FOV 200 mm / Matrice 448x320 | Filtrare TONE / Magnetization Transfer | Bandă de saturație presaturație venoasă superioară pentru suprimarea fluxului din sinusul sagital |
    | **Axial T2 TSE** | Axial | TR 4500 ms / TE 95 ms | 4.0 mm / gap 0.4 mm | FOV 230 mm / 320x256 | Nu | Confirmare semnal 'flow-void' normal în lumenul arterial |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Reconstrucții MIP (Maximum Intensity Projection) radiale rotative la fiecare 15-30°
    - Vizualizare clară a arterelor comunicantă anterioară (ACom) și posterioare (PCom)
    - Absența artefactelor de mișcare (ghosting) sau saturație pe flux lent

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR limitat în mod normal
    - Atenție la clipuri de anevrism preexistente: necesară confirmarea fișei de implant non-feromagnetic

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Pentru anevrisme mici (< 3 mm) sau disecții, se examinează secțiunile native subțiri de 0.5 mm, nu doar reconstrucțiile MIP.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
