---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: abdomen-pelvis
clinical_indications:
- Evaluarea preoperatorie a fistulelor anale complexe sau recidivante (clasificare
  Parks și St. James University Hospital)
- Suspiciune de abcese anorectale oculte, fosa ischioanală sau spațiul intersfincterian
- Boală Crohn perianală pentru monitorizarea răspunsului la terapia biologică / seton
- Fistule rectovaginale sau rectovezicale
coils_hardware:
  coil: Antenă Phased Array multicanal Pelvis de înaltă densitate (fără antenă endorectală)
  field_strength: Preferabil 3.0 Tesla (conform protocolului dedicat DHMC) sau 1.5
    Tesla cu antenă dedicată
  positioning: Decubit dorsal, pernă sub genunchi pentru relaxarea musculaturii planșeului
    pelvin
contraindications:
- Implanturi feromagnetice active incompatibile RM
- Fragilitate critică sau incapacitate de menținere a imobilității în decubit dorsal
contrast:
  agent: Gadoliniu macrociclic 0.1 mmol/kg
  dose: 0.1 mmol/kg
  flow_rate: 1.5 - 2.0 mL/s
  timing: Achiziție tardivă post-contrast la 70-90 secunde și 3 minute
iris_reference:
  chapter: Abdomen & Pelvis
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
modality: irm
notes: Protocolul Dartmouth Hitchcock este optimizat pentru aparatele de 3 Tesla,
  oferind o delimitare superioară a complexului sfincterian. Descrierea fistulei se
  face conform cadranului orar (ora 12 = anterior / perineu, ora 6 = posterior / coccis).
patient_prep: Mică clismă evacuatorie cu 1-2 ore înainte de procedură pentru golirea
  ampulei rectale (reduce artefactele provocate de materiile fecale și gaze). Fără
  dilatare mecanică a canalului.
quality_criteria:
- Planificarea oblică impecabilă după axul canalului anal (oblicitatea incorectă distorsionează
  anatomia sfincteriană)
- Rezoluție spațială submilimetrică în plan (pixel < 0.6 mm)
- Delimitarea precisă a orificiului intern (la nivelul liniei pectinee) și extern
  perianal
safety_considerations:
- Screening 3T feromagnetic riguros
- Verificare eGFR pre-contrast
sequences:
- fat_sat: Nu
  fov_matrix: FOV 240 mm / Matrice 384×288
  name: Sagital T2 TSE (Full FOV Pelvis)
  notes: 'Secvență de planificare fundamentală: se identifică orientarea axului lung
    al canalului anal'
  plane: Sagital
  slice_gap: 3.5 mm / 0.5 mm gap
  tr_te: TR 3500-4500 ms / TE 100 ms
- fat_sat: Nu
  fov_matrix: FOV 180 mm / Matrice 320×320 (rezoluție înaltă)
  name: Axial Oblic T2 TSE (Small FOV)
  notes: Anatomie detaliată a sfincterului anal intern (hipointens), extern (izointens)
    și spațiului intersfincterian
  plane: Axial Oblic (strict perpendicular pe axul lung al canalului anal)
  slice_gap: 3.0 mm / 0.3 mm gap
  tr_te: TR 3500-4000 ms / TE 105 ms
- fat_sat: Da
  fov_matrix: FOV 180 mm / Matrice 320×256
  name: Axial Oblic T2 FS / SPAIR (Small FOV)
  notes: Hipersemnal intens al traiectelor fistuloase active, al ramificațiilor secundare
    și al abceselor
  plane: Axial Oblic
  slice_gap: 3.0 mm / 0.3 mm gap
  tr_te: TR 4000 ms / TE 85 ms
- fat_sat: Nu
  fov_matrix: FOV 180 mm / Matrice 320×320
  name: Coronal Oblic T2 TSE (Small FOV)
  notes: Vizualizarea mușchilor ridicători anali (levator ani) și clasificarea fistulelor
    transsfincteriene vs. suprasfincteriene
  plane: Coronal Oblic (strict paralel cu axul lung al canalului anal)
  slice_gap: 3.0 mm / 0.3 mm gap
  tr_te: TR 3500 ms / TE 100 ms
- fat_sat: Da
  fov_matrix: FOV 180 mm / Matrice 320×256
  name: Coronal Oblic T2 FS / SPAIR
  notes: Diferențiere clară a extensiilor supra-sfincteriene în fosa ischioanală
  plane: Coronal Oblic
  slice_gap: 3.0 mm / 0.3 mm gap
  tr_te: TR 3800 ms / TE 85 ms
- fat_sat: Nu
  fov_matrix: FOV 180 mm / Matrice 320×256
  name: Axial Oblic T1 SE Nativ
  notes: Aprecierea anatomiei sfincteriene și identificarea sângelui / methemoglobinei
  plane: Axial Oblic
  slice_gap: 3.0 mm / 0.3 mm gap
  tr_te: TR 600 ms / TE 12 ms
- fat_sat: Da
  fov_matrix: FOV 180 mm / Matrice 192×144
  name: Axial Oblic DWI Resolve
  notes: Difuzie de înaltă rezoluție (b=50, 800) pentru identificarea abceselor oculte
    colectate
  plane: Axial Oblic
  slice_gap: 3.0 mm
  tr_te: TR 4500 ms / TE 65 ms
- fat_sat: Da
  fov_matrix: FOV 180 mm / Matrice 320×256
  name: Axial & Coronal Oblic 3D T1 VIBE FS Post-Contrast
  notes: Priză intensă de contrast a pereților traiectului fistulos activ și a țesutului
    de granulație; scăderi digitale (Subtractions)
  plane: Axial & Coronal Oblic
  slice_gap: 1.5 - 2.0 mm izotrop
  tr_te: TR 4.2 ms / TE 1.6 ms
title: IRM Fistulă Perianală 3T (Protocol Dedicat DHMC)
---
# IRM Fistulă Perianală 3T (Protocol Dedicat DHMC)

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

        - Evaluarea preoperatorie a fistulelor anale complexe sau recidivante (clasificare Parks și St. James University Hospital)
        - Suspiciune de abcese anorectale oculte, fosa ischioanală sau spațiul intersfincterian
        - Boală Crohn perianală pentru monitorizarea răspunsului la terapia biologică / seton
        - Fistule rectovaginale sau rectovezicale

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice active incompatibile RM
        - Fragilitate critică sau incapacitate de menținere a imobilității în decubit dorsal

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Abdomen & Pelvis*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Mică clismă evacuatorie cu 1-2 ore înainte de procedură pentru golirea ampulei rectale (reduce artefactele provocate de materiile fecale și gaze). Fără dilatare mecanică a canalului.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** Preferabil 3.0 Tesla (conform protocolului dedicat DHMC) sau 1.5 Tesla cu antenă dedicată
    - **Antenă de Recepție (Coil):** Antenă Phased Array multicanal Pelvis de înaltă densitate (fără antenă endorectală)
    - **Poziție Pacient & Centrare:** Decubit dorsal, pernă sub genunchi pentru relaxarea musculaturii planșeului pelvin

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic 0.1 mmol/kg
    - **Doză Recomandată:** 0.1 mmol/kg
    - **Rată de Injectare (Debit):** 1.5 - 2.0 mL/s
    - **Temporizare & Faze Dinamice:** Achiziție tardivă post-contrast la 70-90 secunde și 3 minute
    - **Filtrare Renală & Precauții:** Evaluare eGFR conform ghidurilor ESUR; risc redus de Fibroză Sistemică Nefrogenă (NSF) pentru agenții macrociclici.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T2 TSE (Full FOV Pelvis)** | Sagital | TR 3500-4500 ms / TE 100 ms | 3.5 mm / 0.5 mm gap | FOV 240 mm / Matrice 384×288 | Nu | Secvență de planificare fundamentală: se identifică orientarea axului lung al canalului anal |
    | **Axial Oblic T2 TSE (Small FOV)** | Axial Oblic (strict perpendicular pe axul lung al canalului anal) | TR 3500-4000 ms / TE 105 ms | 3.0 mm / 0.3 mm gap | FOV 180 mm / Matrice 320×320 (rezoluție înaltă) | Nu | Anatomie detaliată a sfincterului anal intern (hipointens), extern (izointens) și spațiului intersfincterian |
    | **Axial Oblic T2 FS / SPAIR (Small FOV)** | Axial Oblic | TR 4000 ms / TE 85 ms | 3.0 mm / 0.3 mm gap | FOV 180 mm / Matrice 320×256 | Da | Hipersemnal intens al traiectelor fistuloase active, al ramificațiilor secundare și al abceselor |
    | **Coronal Oblic T2 TSE (Small FOV)** | Coronal Oblic (strict paralel cu axul lung al canalului anal) | TR 3500 ms / TE 100 ms | 3.0 mm / 0.3 mm gap | FOV 180 mm / Matrice 320×320 | Nu | Vizualizarea mușchilor ridicători anali (levator ani) și clasificarea fistulelor transsfincteriene vs. suprasfincteriene |
    | **Coronal Oblic T2 FS / SPAIR** | Coronal Oblic | TR 3800 ms / TE 85 ms | 3.0 mm / 0.3 mm gap | FOV 180 mm / Matrice 320×256 | Da | Diferențiere clară a extensiilor supra-sfincteriene în fosa ischioanală |
    | **Axial Oblic T1 SE Nativ** | Axial Oblic | TR 600 ms / TE 12 ms | 3.0 mm / 0.3 mm gap | FOV 180 mm / Matrice 320×256 | Nu | Aprecierea anatomiei sfincteriene și identificarea sângelui / methemoglobinei |
    | **Axial Oblic DWI Resolve** | Axial Oblic | TR 4500 ms / TE 65 ms | 3.0 mm | FOV 180 mm / Matrice 192×144 | Da | Difuzie de înaltă rezoluție (b=50, 800) pentru identificarea abceselor oculte colectate |
    | **Axial & Coronal Oblic 3D T1 VIBE FS Post-Contrast** | Axial & Coronal Oblic | TR 4.2 ms / TE 1.6 ms | 1.5 - 2.0 mm izotrop | FOV 180 mm / Matrice 320×256 | Da | Priză intensă de contrast a pereților traiectului fistulos activ și a țesutului de granulație; scăderi digitale (Subtractions) |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Planificarea oblică impecabilă după axul canalului anal (oblicitatea incorectă distorsionează anatomia sfincteriană)
    - Rezoluție spațială submilimetrică în plan (pixel < 0.6 mm)
    - Delimitarea precisă a orificiului intern (la nivelul liniei pectinee) și extern perianal

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening 3T feromagnetic riguros
    - Verificare eGFR pre-contrast

</div>


!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocolul Dartmouth Hitchcock este optimizat pentru aparatele de 3 Tesla, oferind o delimitare superioară a complexului sfincterian. Descrierea fistulei se face conform cadranului orar (ora 12 = anterior / perineu, ora 6 = posterior / coccis).

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
