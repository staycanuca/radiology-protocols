---
author: World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Monitorizare ventriculomegalie și dinamică ventriculară la copilul cu hidrocefalie
- Suspiciune de disfuncție de șunt ventriculo-peritoneal (obstrucție, hiperdrenaj)
- Evaluare colecții lichidiene extra-axiale / subdurale
- Alternativă completă non-iradiantă la scanarea CT repetată a capului
- Control rapid post-operator neurochirurgical
coils_hardware:
  coil: Antenă Head standard sau antenă flexibilă de corp dacă e necesar
  field_strength: 1.5 Tesla sau 3.0 Tesla
  positioning: Decubit dorsal, poziționare rapidă
contraindications:
- 'Implanturi feromagnetice nesigure RM (atenție la valvele de șunt reglabile: necesită
  reverificarea setării de presiune după RM conform indicațiilor producătorului)'
contrast:
  agent: Fără contrast (protocol ultra-rapid)
  dose: N/A
  flow_rate: N/A
  notes: Protocol exclusiv nativ ultra-rapid (3–5 minute).
  timing: N/A
iris_reference:
  chapter: Pediatrie - Sistem Nervos Central
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocolul 'Ventricle Check' de la WFPI înlocuiește cu succes scanările CT
  repetate, scutind copiii cu hidrocefalie de doze cumulative masive de radiații ionizante.
patient_prep: Nu necesită pregătire specială, post alimentar sau sedare. Copilul poate
  rămâne îmbrăcat în haine fără capse metalice.
quality_criteria:
- 'Timp total de examinare la aparat: 3 până la 5 minute'
- Vizualizare clară a conturului ventricular în toate cele 3 planuri
- Complet imun la artefactele respiratorii sau de agitație motorie
safety_considerations:
- 'Verificare obligatorie a tipului de valvă de șunt: dacă este valvă reglabilă magnetic
  (ex. Codman, Strata, Polaris), este obligatorie verificarea și reprogramarea presiunii
  de către neurochirurg imediat după examinare!'
sequences:
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / 256x256
  name: Axial Single-shot T2WI (HASTE / SSFSE)
  notes: Achiziție ultra-rapidă (sub 1 secundă per secțiune), complet insensibilă
    la mișcarea pacientului (1 min)
  plane: Axial
  slice_gap: 3.0-4.0 mm / gap 0 mm
  tr_te: TR 1000-1500 ms / TE 90-120 ms
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / 256x256
  name: Sagital Single-shot T2WI (HASTE / SSFSE)
  notes: Evaluare apeduct Sylvius, ventricul IV, foramen magnum și traiect cateter
    ventricular (1 min)
  plane: Sagital
  slice_gap: 3.0-4.0 mm / gap 0 mm
  tr_te: TR 1000-1500 ms / TE 90-120 ms
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / 256x256
  name: Coronal Single-shot T2WI (HASTE / SSFSE)
  notes: Evaluare coarne frontale și temporale ale ventriculilor laterali, colecții
    extra-axiale (1 min)
  plane: Coronal
  slice_gap: 3.0-4.0 mm / gap 0 mm
  tr_te: TR 1000-1500 ms / TE 90-120 ms
- fat_sat: FatSat
  fov_matrix: FOV 200 mm / 128x128
  name: Axial DWI (Opțional)
  notes: Opțional, pentru excludere ventriculită sau complicații ischemice (1-2 min)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 3000 ms / TE 70 ms
slug: irm-pediatric-hidrocefalie-control-ventriculi
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
title: RM Pediatric — Protocol Hidrocefalie & Control Ventriculi / Șunt (Quick Brain)
---
# RM Pediatric — Protocol Hidrocefalie & Control Ventriculi / Șunt (Quick Brain)

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

        - Monitorizare ventriculomegalie și dinamică ventriculară la copilul cu hidrocefalie
        - Suspiciune de disfuncție de șunt ventriculo-peritoneal (obstrucție, hiperdrenaj)
        - Evaluare colecții lichidiene extra-axiale / subdurale
        - Alternativă completă non-iradiantă la scanarea CT repetată a capului
        - Control rapid post-operator neurochirurgical

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice nesigure RM (atenție la valvele de șunt reglabile: necesită reverificarea setării de presiune după RM conform indicațiilor producătorului)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Sistem Nervos Central*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Nu necesită pregătire specială, post alimentar sau sedare. Copilul poate rămâne îmbrăcat în haine fără capse metalice.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla sau 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă Head standard sau antenă flexibilă de corp dacă e necesar
    - **Poziție Pacient & Centrare:** Decubit dorsal, poziționare rapidă

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Fără contrast (protocol ultra-rapid)
    - **Doză Recomandată:** N/A
    - **Rată de Injectare (Debit):** N/A
    - **Temporizare & Faze Dinamice:** N/A
    - **Filtrare Renală & Precauții:** Protocol exclusiv nativ ultra-rapid (3–5 minute).

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Axial Single-shot T2WI (HASTE / SSFSE)** | Axial | TR 1000-1500 ms / TE 90-120 ms | 3.0-4.0 mm / gap 0 mm | FOV 200-220 mm / 256x256 | Nu | Achiziție ultra-rapidă (sub 1 secundă per secțiune), complet insensibilă la mișcarea pacientului (1 min) |
    | **Sagital Single-shot T2WI (HASTE / SSFSE)** | Sagital | TR 1000-1500 ms / TE 90-120 ms | 3.0-4.0 mm / gap 0 mm | FOV 200-220 mm / 256x256 | Nu | Evaluare apeduct Sylvius, ventricul IV, foramen magnum și traiect cateter ventricular (1 min) |
    | **Coronal Single-shot T2WI (HASTE / SSFSE)** | Coronal | TR 1000-1500 ms / TE 90-120 ms | 3.0-4.0 mm / gap 0 mm | FOV 200-220 mm / 256x256 | Nu | Evaluare coarne frontale și temporale ale ventriculilor laterali, colecții extra-axiale (1 min) |
    | **Axial DWI (Opțional)** | Axial | TR 3000 ms / TE 70 ms | 4.0 mm / gap 0.4 mm | FOV 200 mm / 128x128 | FatSat | Opțional, pentru excludere ventriculită sau complicații ischemice (1-2 min) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Timp total de examinare la aparat: 3 până la 5 minute
    - Vizualizare clară a conturului ventricular în toate cele 3 planuri
    - Complet imun la artefactele respiratorii sau de agitație motorie

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Verificare obligatorie a tipului de valvă de șunt: dacă este valvă reglabilă magnetic (ex. Codman, Strata, Polaris), este obligatorie verificarea și reprogramarea presiunii de către neurochirurg imediat după examinare!

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocolul 'Ventricle Check' de la WFPI înlocuiește cu succes scanările CT repetate, scutind copiii cu hidrocefalie de doze cumulative masive de radiații ionizante.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
