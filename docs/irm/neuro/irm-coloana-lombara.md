---
author: Departamentul de Radiologie și Imagistică Medicală
category: neuro
clinical_indications:
- Lombosciatică / lumbocruralgie rebelă la tratament conservator (> 4-6 săptămâni)
- Sindrom de coadă de cal (urgență neurochirurgicală - anestezie 'în șa', retenție/incontinență
  urinară)
- Suspiciune de stenoză de canal vertebral lombar sau spondilolistezis
- Suspiciune de spondilodiscită infecțioasă sau metastaze vertebrale
- Evaluare post-operatorie (diferențiere hernie recidivată vs. fibroză periradiculară
  cicatricială)
coils_hardware:
  coil: Antenă Spine integrată în masă (phased-array)
  field_strength: 1.5T sau 3.0T
  positioning: Decubit dorsal, centrare pe vertebra L3 (la 2-3 cm deasupra crestelor
    iliace).
contraindications:
- Contraindicații generale de compatibilitate RM.
contrast:
  agent: Nativ de rutină; se injectează Gd 0.1 mmol/kg la pacienții operați recent
    (< 1 an) pentru diferențierea fibrozei (captează precoce) de hernia discală recidivată
    (necaptantă precoce).
  dose: 0.1 mmol/kg (la indicație)
  flow_rate: 1.5 - 2.0 ml/s
  notes: Spondilodiscita infecțioasă necesită obligatoriu contrast paramagnetic intravenos.
  timing: T1 post-contrast axial și sagital
iris_reference:
  chapter: Coloană Vertebrală - Segment Lombar
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: irm
notes: În caz de sindrom de coadă de cal, examinarea se efectuează în regim de urgență
  maximă pentru decompresiune chirurgicală precoce.
patient_prep: Chestionar de securitate RM; decubit dorsal confortabil cu genunchii
  flectați pe un burete cilindric pentru rectitudinea lordozei lombare.
quality_criteria:
- Cuprinderea conului medular și a primelor două vertebre sacrate
- Banda de presaturație abdominală anterioară activată pentru tăierea artefactelor
  respiratorii și aortice
- Centrare corectă angulată a pachetelor axiale pe spațiile discale intervertebrale
safety_considerations:
- SAR bine tolerat pe coloană lombară
- La pacienți cu dureri severe, poziționarea unui rulou sub fosele poplitee ameliorează
  semnificativ confortul
sequences:
- fat_sat: Nu
  fov_matrix: FOV 280 mm / 384x256
  name: Sagital T1 TSE
  notes: Modificări Modic tip 1/2, aliniament corpi vertebrali
  plane: Sagital lombar (T11 - S2)
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 600 ms / TE 10 ms
- fat_sat: Nu
  fov_matrix: FOV 280 mm / 384x288
  name: Sagital T2 TSE
  notes: Deshidratare discală, hernie posterioară, con medular (T12-L1/L2)
  plane: Sagital lombar
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 4000 ms / TE 100 ms
- fat_sat: STIR
  fov_matrix: FOV 280 mm / 320x224
  name: Sagital STIR / TIRM
  notes: Edem osos vertebral (fractură recentă osteoporotică vs. veche, spondilodiscită)
  plane: Sagital lombar
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 4200 ms / TE 50 ms / TI 160 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / 320x256
  name: Axial T2 TSE disc-pe-disc
  notes: Rădăcini nervoase în recesurile laterale și foramen, ligament galben
  plane: Axial angulat paralel cu discurile L3-L4, L4-L5, L5-S1
  slice_gap: 3.5 - 4.0 mm / gap 0.3 mm
  tr_te: TR 4000 ms / TE 105 ms
- fat_sat: Nu
  fov_matrix: FOV 200 mm / 256x256
  name: Axial T1 TSE
  notes: Grăsime epidurală, delimitare hernie discală foraminală
  plane: Axial lombar inferior (L4-S1)
  slice_gap: 4.0 mm / gap 0.4 mm
  tr_te: TR 550 ms / TE 10 ms
slug: irm-coloana-lombara
title: IRM Coloană Lombară
sources:
- title: OHSU Diagnostic Radiology — Brain & Spine MRI Protocols
  url: https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols
  institution: OHSU
  source_region: US
  kind: Protocol instituțional IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: f472cca210c17724389892b28b4ff21ac0d171c1731755f8540809a18a414746
- title: ACR-ASNR-SPR Practice Parameter for the Performance of Magnetic Resonance
    Imaging (MRI) of the Brain
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Brain.pdf
  institution: ACR / ASNR
  source_region: US
  kind: Standard de practică IRM
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 05b5d22ee8b61e427ebdd5871542c5dee1f63a2932ca9179c569964f9b430a90
position: Decubit dorsal, centrare pe vertebra L3 (la 2-3 cm deasupra crestelor iliace).
---

# IRM Coloană Lombară

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

        - Lombosciatică / lumbocruralgie rebelă la tratament conservator (> 4-6 săptămâni)
        - Sindrom de coadă de cal (urgență neurochirurgicală - anestezie 'în șa', retenție/incontinență urinară)
        - Suspiciune de stenoză de canal vertebral lombar sau spondilolistezis
        - Suspiciune de spondilodiscită infecțioasă sau metastaze vertebrale
        - Evaluare post-operatorie (diferențiere hernie recidivată vs. fibroză periradiculară cicatricială)

    === "Contraindicații & Screening Metalic"

        - Contraindicații generale de compatibilitate RM.

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Coloană Vertebrală - Segment Lombar*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Securitate Feromagnetică__

    ---

    - **Pregătire Prealabilă:** Chestionar de securitate RM; decubit dorsal confortabil cu genunchii flectați pe un burete cilindric pentru rectitudinea lordozei lombare.
    - **Protecție Auditivă:** Căști fonice / dopuri auditive obligatorii pentru toți pacienții (atenuare zgomot gradient > 25-30 dB).
    - **Monitorizare & Comunicare:** Pompiță de apel de urgență în mâna pacientului, supraveghere video și interfon bidirecțional permanent.

-   __3. Antene (Coils), Câmp Magnetic & Poziționare__

    ---

    - **Putere Câmp Magnetic:** 1.5T sau 3.0T
    - **Antenă de Recepție (Coil):** Antenă Spine integrată în masă (phased-array)
    - **Poziție Pacient & Centrare:** Decubit dorsal, centrare pe vertebra L3 (la 2-3 cm deasupra crestelor iliace).

-   __4. Substanță de Contrast Paramagnetic (Gadoliniu)__

    ---

    - **Agent de Contrast:** Nativ de rutină; se injectează Gd 0.1 mmol/kg la pacienții operați recent (< 1 an) pentru diferențierea fibrozei (captează precoce) de hernia discală recidivată (necaptantă precoce).
    - **Doză Recomandată:** 0.1 mmol/kg (la indicație)
    - **Rată de Injectare (Debit):** 1.5 - 2.0 ml/s
    - **Temporizare & Faze Dinamice:** T1 post-contrast axial și sagital
    - **Filtrare Renală & Precauții:** Spondilodiscita infecțioasă necesită obligatoriu contrast paramagnetic intravenos.

-   __5. Protocol Secvențe RM (Parametri Tehnici)__

    ---

    | Secvență Achiziție | Plan | TR / TE | Grosime / Gap | Matrice / FOV | FatSat | Observații Tehnice |
    |:-------------------|:-----|:--------|:--------------|:--------------|:-------|:-------------------|
    | **Sagital T1 TSE** | Sagital lombar (T11 - S2) | TR 600 ms / TE 10 ms | 4.0 mm / gap 0.4 mm | FOV 280 mm / 384x256 | Nu | Modificări Modic tip 1/2, aliniament corpi vertebrali |
    | **Sagital T2 TSE** | Sagital lombar | TR 4000 ms / TE 100 ms | 4.0 mm / gap 0.4 mm | FOV 280 mm / 384x288 | Nu | Deshidratare discală, hernie posterioară, con medular (T12-L1/L2) |
    | **Sagital STIR / TIRM** | Sagital lombar | TR 4200 ms / TE 50 ms / TI 160 ms | 4.0 mm / gap 0.4 mm | FOV 280 mm / 320x224 | STIR | Edem osos vertebral (fractură recentă osteoporotică vs. veche, spondilodiscită) |
    | **Axial T2 TSE disc-pe-disc** | Axial angulat paralel cu discurile L3-L4, L4-L5, L5-S1 | TR 4000 ms / TE 105 ms | 3.5 - 4.0 mm / gap 0.3 mm | FOV 200 mm / 320x256 | Nu | Rădăcini nervoase în recesurile laterale și foramen, ligament galben |
    | **Axial T1 TSE** | Axial lombar inferior (L4-S1) | TR 550 ms / TE 10 ms | 4.0 mm / gap 0.4 mm | FOV 200 mm / 256x256 | Nu | Grăsime epidurală, delimitare hernie discală foraminală |

-   __6. Criterii de Calitate a Imaginii & Diagnostic__

    ---

    - Cuprinderea conului medular și a primelor două vertebre sacrate
    - Banda de presaturație abdominală anterioară activată pentru tăierea artefactelor respiratorii și aortice
    - Centrare corectă angulată a pachetelor axiale pe spațiile discale intervertebrale

-   __7. Securitate RM, Limită SAR & Artefacte__

    ---

    - SAR bine tolerat pe coloană lombară
    - La pacienți cu dureri severe, poziționarea unui rulou sub fosele poplitee ameliorează semnificativ confortul

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    În caz de sindrom de coadă de cal, examinarea se efectuează în regim de urgență maximă pentru decompresiune chirurgicală precoce.

=== "Ghid Rapid de Siguranță RM (Zona IV - Magnet)"

    1. **Screening Feromagnetic Riguros (Zona III -> Zona IV):** Niciun obiect metalic feromagnetic (trolere, butelii oxigen nespecifice, foarfece, monede, chei, telefoane) nu intră în sala magnetului (risc de proiectil mortal).
    2. **Verificare Implanturi Medicale:** Pacienții cu stimulatoare cardiace (pacemaker/ICD), neurostimulatoare, pompe de insulină, clipuri anevrismale intracraniene sau corpi străini intraoculari metalici necesită documentare strictă "MR Conditional" la puterea de câmp utilizată (1.5T vs 3.0T).
    3. **Rată Specifică de Absorbție (SAR):** Monitorizarea depunerii de energie de radiofrecvență (RF) în țesuturi. Respectarea limitei modului normal de operare (SAR corp întreg < 2.0 W/kg) pentru prevenirea supraîncălzirii termice, în special la pacienți febrili sau obezi.
    4. **Atenuare Artefacte:** Utilizarea benzilor de saturație spațială pentru eliminarea artefactelor de pulsație vasculară/deglutiție, calibrarea supresiei de grăsime (Dixon/SPAIR) în prezența materialelor de osteosinteză titan.

## Surse și revizuire

- [OHSU Diagnostic Radiology — Brain & Spine MRI Protocols](https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols) — *OHSU* (US)
- [ACR-ASNR-SPR Practice Parameter for the Performance of Magnetic Resonance Imaging (MRI) of the Brain](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/MR-Brain.pdf) — *ACR / ASNR* (US)
