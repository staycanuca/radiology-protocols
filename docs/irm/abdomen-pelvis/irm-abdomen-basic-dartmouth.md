---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: abdomen-pelvis
clinical_indications:
- Evaluare generală abdominală pentru leziuni focale sau procese inflamatorii/infecțioase
- Suspiciune de colecții intraabdominale, abcese viscerale sau periviscerale
- Dureri abdominale persistente nespecifice fără diagnostic cert la ecografie sau
  CT
- Caracterizarea formațiunilor chistice vs. solide la pacienți cu contraindicație
  de contrast iodat
coils_hardware:
  coil: Antenă de corp multicanal Phased Array (Body Coil 18–32 canale) + antenă Spine
    posterioară
  field_strength: 1.5 Tesla sau 3.0 Tesla (Siemens / GE / Philips)
  positioning: Decubit dorsal, picioarele sau capul înainte, centrare optică la nivelul
    apendicelui xifoid
contraindications:
- Stimulator cardiac / pacemaker vechi non-MR conditional sau electrozi intracardiaci
  abandonați
- Clipsuri anevrismale intracraniene feromagnetice
- Corpi străini metalici intraoculari
- Implanturi cohleare non-compatibile
contrast:
  agent: Chelat de Gadoliniu macrociclic hidrosolubil (Gadobutrol / Gadoterat de meglumină)
  dose: 0.1 mmol/kg (standard)
  flow_rate: 1.5 - 2.0 mL/s urmat de flush salin 20-30 mL
  timing: 'Fază dinamică multifazică: Arterială tardivă (18-22 sec), Venoasă portală
    (60-70 sec), Echilibru (3 min)'
iris_reference:
  chapter: Abdomen & Pelvis
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
modality: irm
notes: Protocol de bază DHMC optimizat pe platforma Siemens, transpozabil direct pe
  aparate GE și Philips. În caz de ascită masivă, se recomandă utilizarea SPAIR sau
  DIXON pentru supresie adipoasă omogenă.
patient_prep: Repaus alimentar 4-6 ore înainte de examinare pentru a reduce peristaltismul
  intestinal și a asigura repleția colecistului. Chestionar complet de securitate
  feromagnetică.
quality_criteria:
- Absența artefactelor majore de mișcare respiratorie prin instruirea corectă a pacientului
- Supresie omogenă a semnalului grăsimii pe întreg volumul abdominal la secvențele
  FatSat
- Calcul automat al hărților ADC și al seriilor de substracție digitală (Post minus
  Pre-contrast)
safety_considerations:
- Screening feromagnetic riguros Zonele III/IV
- Verificare eGFR conform recomandărilor ACR/ESUR pentru agenți macrociclici
- Supraveghere acustică și furnizare de dopuri / căști fonoizolante
sequences:
- fat_sat: Nu
  fov_matrix: FOV 440 mm / Matrice 320×256
  name: Coronal T2 HASTE / Single-Shot
  notes: Apnee inspiratorie / expiratorie scurtă; vedere de ansamblu a întregului
    abdomen și retroperitoneu
  plane: Coronal
  slice_gap: 5.0 mm / 1.0 mm gap
  tr_te: TR 1400 ms / TE 91 ms
- fat_sat: Nativ (In/Opposed phase)
  fov_matrix: FOV 380 mm / Matrice 256×192
  name: Axial T1 Dual Echo In / Out of Phase
  notes: Detecție grăsime microscopică intracelulară (steatoză hepatică, adenom suprarenalian)
  plane: Axial
  slice_gap: 5.0 mm / 1.0 mm gap
  tr_te: TR 170 ms / TE 1.2 & 2.4 ms (la 3T) sau 2.3 & 4.6 ms (la 1.5T)
- fat_sat: Da (Spectral Fat Saturation / SPAIR)
  fov_matrix: FOV 380 mm / Matrice 320×256
  name: Axial T2 FS (Fat Suppressed BLADE / TSE)
  notes: Caracterizare leziuni chistice, edem, hemangioame și procese inflamatorii
  plane: Axial
  slice_gap: 5.0 mm / 1.0 mm gap
  tr_te: TR 1600 ms / TE 95 ms
- fat_sat: Da
  fov_matrix: FOV 380 mm / Matrice 192×144
  name: Axial DWI cu coeficient ADC
  notes: 'Valori b: 50, 400, 750 s/mm² cu generare automată de hartă cantitativă ADC;
    detecție celularitate înaltă / abcese'
  plane: Axial
  slice_gap: 5.0 mm / 1.0 mm gap
  tr_te: TR 5800 ms / TE 61 ms
- fat_sat: Da
  fov_matrix: FOV 380 mm / Matrice 288×216
  name: Axial 3D T1 VIBE FS Pre-Contrast
  notes: Secvență nativă volumetrică de referință pentru scăderile digitale
  plane: Axial
  slice_gap: 3.0 mm (izotrop interpolat)
  tr_te: TR 3.5 ms / TE 1.4 ms
- fat_sat: Da
  fov_matrix: FOV 380 mm / Matrice 288×216
  name: Axial 3D T1 VIBE FS Dinamic Post-Contrast (60-70s)
  notes: Fază venoasă portală clasică cu scăderi digitale automate (Subtractions)
  plane: Axial
  slice_gap: 3.0 mm
  tr_te: TR 3.5 ms / TE 1.4 ms
- fat_sat: Da
  fov_matrix: FOV 420 mm / Matrice 288×216
  name: Coronal 3D T1 VIBE FS Post-Contrast
  notes: Completare multiplanară a fazei tardive de echilibru
  plane: Coronal
  slice_gap: 3.5 mm
  tr_te: TR 3.8 ms / TE 1.5 ms
title: IRM Abdomen Rutină Nativ & cu Contrast (Protocol DHMC)
---
# IRM Abdomen Rutină Nativ & cu Contrast (Protocol DHMC)

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

        - Evaluare generală abdominală pentru leziuni focale sau procese inflamatorii/infecțioase
        - Suspiciune de colecții intraabdominale, abcese viscerale sau periviscerale
        - Dureri abdominale persistente nespecifice fără diagnostic cert la ecografie sau CT
        - Caracterizarea formațiunilor chistice vs. solide la pacienți cu contraindicație de contrast iodat

    === "Contraindicații & Screening Metalic"

        - Stimulator cardiac / pacemaker vechi non-MR conditional sau electrozi intracardiaci abandonați
        - Clipsuri anevrismale intracraniene feromagnetice
        - Corpi străini metalici intraoculari
        - Implanturi cohleare non-compatibile

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Abdomen & Pelvis*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Repaus alimentar 4-6 ore înainte de examinare pentru a reduce peristaltismul intestinal și a asigura repleția colecistului. Chestionar complet de securitate feromagnetică.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla sau 3.0 Tesla (Siemens / GE / Philips)
    - **Antenă de Recepție (Coil):** Antenă de corp multicanal Phased Array (Body Coil 18–32 canale) + antenă Spine posterioară
    - **Poziție Pacient & Centrare:** Decubit dorsal, picioarele sau capul înainte, centrare optică la nivelul apendicelui xifoid

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Chelat de Gadoliniu macrociclic hidrosolubil (Gadobutrol / Gadoterat de meglumină)
    - **Doză Recomandată:** 0.1 mmol/kg (standard)
    - **Rată de Injectare (Debit):** 1.5 - 2.0 mL/s urmat de flush salin 20-30 mL
    - **Temporizare & Faze Dinamice:** Fază dinamică multifazică: Arterială tardivă (18-22 sec), Venoasă portală (60-70 sec), Echilibru (3 min)
    - **Filtrare Renală & Precauții:** Evaluare eGFR conform ghidurilor ESUR; risc redus de Fibroză Sistemică Nefrogenă (NSF) pentru agenții macrociclici.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Coronal T2 HASTE / Single-Shot** | Coronal | TR 1400 ms / TE 91 ms | 5.0 mm / 1.0 mm gap | FOV 440 mm / Matrice 320×256 | Nu | Apnee inspiratorie / expiratorie scurtă; vedere de ansamblu a întregului abdomen și retroperitoneu |
    | **Axial T1 Dual Echo In / Out of Phase** | Axial | TR 170 ms / TE 1.2 & 2.4 ms (la 3T) sau 2.3 & 4.6 ms (la 1.5T) | 5.0 mm / 1.0 mm gap | FOV 380 mm / Matrice 256×192 | Nativ (In/Opposed phase) | Detecție grăsime microscopică intracelulară (steatoză hepatică, adenom suprarenalian) |
    | **Axial T2 FS (Fat Suppressed BLADE / TSE)** | Axial | TR 1600 ms / TE 95 ms | 5.0 mm / 1.0 mm gap | FOV 380 mm / Matrice 320×256 | Da (Spectral Fat Saturation / SPAIR) | Caracterizare leziuni chistice, edem, hemangioame și procese inflamatorii |
    | **Axial DWI cu coeficient ADC** | Axial | TR 5800 ms / TE 61 ms | 5.0 mm / 1.0 mm gap | FOV 380 mm / Matrice 192×144 | Da | Valori b: 50, 400, 750 s/mm² cu generare automată de hartă cantitativă ADC; detecție celularitate înaltă / abcese |
    | **Axial 3D T1 VIBE FS Pre-Contrast** | Axial | TR 3.5 ms / TE 1.4 ms | 3.0 mm (izotrop interpolat) | FOV 380 mm / Matrice 288×216 | Da | Secvență nativă volumetrică de referință pentru scăderile digitale |
    | **Axial 3D T1 VIBE FS Dinamic Post-Contrast (60-70s)** | Axial | TR 3.5 ms / TE 1.4 ms | 3.0 mm | FOV 380 mm / Matrice 288×216 | Da | Fază venoasă portală clasică cu scăderi digitale automate (Subtractions) |
    | **Coronal 3D T1 VIBE FS Post-Contrast** | Coronal | TR 3.8 ms / TE 1.5 ms | 3.5 mm | FOV 420 mm / Matrice 288×216 | Da | Completare multiplanară a fazei tardive de echilibru |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Absența artefactelor majore de mișcare respiratorie prin instruirea corectă a pacientului
    - Supresie omogenă a semnalului grăsimii pe întreg volumul abdominal la secvențele FatSat
    - Calcul automat al hărților ADC și al seriilor de substracție digitală (Post minus Pre-contrast)

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Screening feromagnetic riguros Zonele III/IV
    - Verificare eGFR conform recomandărilor ACR/ESUR pentru agenți macrociclici
    - Supraveghere acustică și furnizare de dopuri / căști fonoizolante

</div>


!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol de bază DHMC optimizat pe platforma Siemens, transpozabil direct pe aparate GE și Philips. În caz de ascită masivă, se recomandă utilizarea SPAIR sau DIXON pentru supresie adipoasă omogenă.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
