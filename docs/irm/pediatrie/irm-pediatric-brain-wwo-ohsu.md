---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: pediatrie
clinical_indications:
- Leziuni focale cerebrale sau suspiciune de neoplazie SNC pediatrică (astrocitom,
  meduloblastom, ependimom)
- Infecții intracraniene pediatrice (meningită bacteriană/virală, encefalită, abces
  cerebral, empiem)
- Cefalee cronică progresivă sau cu semne neurologice de focar
- Evaluare post-operatorie sau monitorizare oncopediatrică neuroaxială
- Deficite neurologice acute sau subacute la copil
coils_hardware:
  coil: Antenă dedicată Head pediatrică multicanal (16–32 canale) cu pernuțe moi
  field_strength: 1.5 Tesla / 3.0 Tesla
  positioning: Decubit dorsal, cap imobilizat confortabil, măsuri active de confort
    și distragere pediatrică (Child Life)
contraindications:
- Implanturi feromagnetice incompatibile RM
contrast:
  agent: Gadoliniu macrociclic cu stabilitate înaltă (Gadoterat de meglumină / Gadobutrol)
  dose: 0.1 mmol/kg (strict conform greutății copilului)
  flow_rate: 1.0 - 1.5 mL/s + flush salin 10-15 mL
  notes: Administrare de contrast aprobată doar în indicații oncologice, infecțioase
    sau vasculare clare.
  timing: Scanare post-contrast imediat după injectare
iris_reference:
  chapter: Pediatrie - Sistem Nervos Central
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
modality: irm
notes: Protocol complet pediatric OHSU pentru diagnostic neoplazic și infecțios de
  înaltă rezoluție.
patient_prep: 'La sugari (< 6 luni): tehnică feed-and-wrap (alimentare și înfășare
  înainte de scanare). La copii cooperanți: muzică / povești audio prin căști RM.
  La copii necooperanți: sedare conform politicii OHSU Moderate Sedation.'
quality_criteria:
- Acoperire craniană completă fără trunchiere la nivelul foramen magnum
- Secvențe T1 post-contrast evaluate în comparație directă cu secvența T1 nativă
- Protecție acustică dublă certificată pentru volumul cranian pediatric
safety_considerations:
- Protecție fonică dublă obligatorie (căști adaptate + dopuri siliconice)
- Monitorizare pulsoximetrie compatibilă RM pe durata întregii examinări
- SAR strict menținut în limita normală (< 2.0 W/kg)
sequences:
- fat_sat: Nu
  fov_matrix: FOV 200-220 mm / Matrice 256×256
  name: Sagital 3D T1 MPRAGE Nativ
  notes: 'Anatomie de înaltă rezoluție: corp calos, fosă posterioară, joncțiune cervico-medulară,
    mielinizare'
  plane: Sagital / Reconstrucție 3-plane
  slice_gap: 0.9 - 1.0 mm izotrop
  tr_te: TR 2000-2400 ms / TE 2.5-3.5 ms / TI 900 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / Matrice 320×256
  name: Axial T2 TSE / FSE
  notes: Diferențiere substanță albă/cenușie și evaluare edem vasogenic
  plane: Axial
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 4000-5000 ms / TE 100-110 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / Matrice 256×224
  name: Axial FLAIR
  notes: Supresie LCR; evidențiere leziuni periventriculare și leptomeningeale
  plane: Axial
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 8000-9000 ms / TE 90-110 ms / TI 2200-2400 ms
- fat_sat: FatSat (EPI)
  fov_matrix: FOV 200 mm / Matrice 128×128
  name: Axial DWI (b=0, b=1000) + hartă ADC
  notes: Restricție de difuzie în leziuni celulare hiperdense (meduloblastom) sau
    abcese cerebrale
  plane: Axial
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 3000-4000 ms / TE 70 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / Matrice 256×192
  name: Axial T2* / SWI
  notes: Sensibilitate la hemoragii intratumorale, microhemoragii și calcificări
  plane: Axial
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 600-800 ms / TE 15-25 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / Matrice 256×256
  name: Axial T1 SE / TSE Post-Contrast
  notes: Captare patologică focală sau difuză a barierei hemato-encefalice
  plane: Axial
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 500-650 ms / TE 10-15 ms
- fat_sat: FatSat obligatoriu
  fov_matrix: FOV 200 mm / Matrice 256×224
  name: Coronal T1 FS Post-Contrast (sau 3D T1 FS)
  notes: Evaluare fosa posterioară, unghi ponto-cerebelos și diseminare leptomeningeală
  plane: Coronal
  slice_gap: 3.5 - 4.0 mm / gap 0.4 mm
  tr_te: TR 550-700 ms / TE 10-15 ms
title: RM Cerebral Pediatric cu/fără Contrast (Protocol OHSU)
---
# RM Cerebral Pediatric cu/fără Contrast (Protocol OHSU)

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

        - Leziuni focale cerebrale sau suspiciune de neoplazie SNC pediatrică (astrocitom, meduloblastom, ependimom)
        - Infecții intracraniene pediatrice (meningită bacteriană/virală, encefalită, abces cerebral, empiem)
        - Cefalee cronică progresivă sau cu semne neurologice de focar
        - Evaluare post-operatorie sau monitorizare oncopediatrică neuroaxială
        - Deficite neurologice acute sau subacute la copil

    === "Contraindicații & Screening Metalic"

        - Implanturi feromagnetice incompatibile RM

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie - Sistem Nervos Central*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** La sugari (< 6 luni): tehnică feed-and-wrap (alimentare și înfășare înainte de scanare). La copii cooperanți: muzică / povești audio prin căști RM. La copii necooperanți: sedare conform politicii OHSU Moderate Sedation.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5 Tesla / 3.0 Tesla
    - **Antenă de Recepție (Coil):** Antenă dedicată Head pediatrică multicanal (16–32 canale) cu pernuțe moi
    - **Poziție Pacient & Centrare:** Decubit dorsal, cap imobilizat confortabil, măsuri active de confort și distragere pediatrică (Child Life)

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Gadoliniu macrociclic cu stabilitate înaltă (Gadoterat de meglumină / Gadobutrol)
    - **Doză Recomandată:** 0.1 mmol/kg (strict conform greutății copilului)
    - **Rată de Injectare (Debit):** 1.0 - 1.5 mL/s + flush salin 10-15 mL
    - **Temporizare & Faze Dinamice:** Scanare post-contrast imediat după injectare
    - **Filtrare Renală & Precauții:** Administrare de contrast aprobată doar în indicații oncologice, infecțioase sau vasculare clare.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital 3D T1 MPRAGE Nativ** | Sagital / Reconstrucție 3-plane | TR 2000-2400 ms / TE 2.5-3.5 ms / TI 900 ms | 0.9 - 1.0 mm izotrop | FOV 200-220 mm / Matrice 256×256 | Nu | Anatomie de înaltă rezoluție: corp calos, fosă posterioară, joncțiune cervico-medulară, mielinizare |
    | **Axial T2 TSE / FSE** | Axial | TR 4000-5000 ms / TE 100-110 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 mm / Matrice 320×256 | Nu | Diferențiere substanță albă/cenușie și evaluare edem vasogenic |
    | **Axial FLAIR** | Axial | TR 8000-9000 ms / TE 90-110 ms / TI 2200-2400 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 mm / Matrice 256×224 | Nu | Supresie LCR; evidențiere leziuni periventriculare și leptomeningeale |
    | **Axial DWI (b=0, b=1000) + hartă ADC** | Axial | TR 3000-4000 ms / TE 70 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 mm / Matrice 128×128 | FatSat (EPI) | Restricție de difuzie în leziuni celulare hiperdense (meduloblastom) sau abcese cerebrale |
    | **Axial T2* / SWI** | Axial | TR 600-800 ms / TE 15-25 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 mm / Matrice 256×192 | Nu | Sensibilitate la hemoragii intratumorale, microhemoragii și calcificări |
    | **Axial T1 SE / TSE Post-Contrast** | Axial | TR 500-650 ms / TE 10-15 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 mm / Matrice 256×256 | Nu | Captare patologică focală sau difuză a barierei hemato-encefalice |
    | **Coronal T1 FS Post-Contrast (sau 3D T1 FS)** | Coronal | TR 550-700 ms / TE 10-15 ms | 3.5 - 4.0 mm / gap 0.4 mm | FOV 200 mm / Matrice 256×224 | FatSat obligatoriu | Evaluare fosa posterioară, unghi ponto-cerebelos și diseminare leptomeningeală |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Acoperire craniană completă fără trunchiere la nivelul foramen magnum
    - Secvențe T1 post-contrast evaluate în comparație directă cu secvența T1 nativă
    - Protecție acustică dublă certificată pentru volumul cranian pediatric

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - Protecție fonică dublă obligatorie (căști adaptate + dopuri siliconice)
    - Monitorizare pulsoximetrie compatibilă RM pe durata întregii examinări
    - SAR strict menținut în limita normală (< 2.0 W/kg)

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Protocol complet pediatric OHSU pentru diagnostic neoplazic și infecțios de înaltă rezoluție.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.
