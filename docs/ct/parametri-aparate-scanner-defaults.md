---
title: Parametri Impliciti Scanere CT (Siemens, GE, Philips)
author: MCB Radiology / Clinical Engineering
category: ct
modality: ct
slug: parametri-aparate-scanner-defaults
clinical_indications:
  - Ghid tehnic de referință pentru parametri impliciți de scanare CT
  - Standardizare protocoale Siemens, GE și Philips
last_updated: '2026-09-27'
sources:
  - title: Scanner Default Protocols Manual
    url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Scanner%20Default%20Protocols.html
    relationship: authoritative_institutional_reference
---

# ⚙️ Parametri Impliciti Scanere CT (Siemens, GE, Philips)

Ghid tehnic de referință pentru parametrii impliciți de scanare, tehnologiile de modulare automată a dozei și algoritmii de reconstrucție iterativă pe platformele tomografice majore (**Siemens Healthineers**, **GE HealthCare**, **Philips Healthcare**). Fiecare secțiune detaliază kilovoltajul (kV), modularea automată a curentului (CARE Dose4D / Smart mA / DoseWise), colimarea detectorilor, timpul de rotație și kernele de reconstrucție recomandate.

---

## 1. Comparație Tehnologică Parametri Impliciti

| Parametru Tehnic | Siemens SOMATOM Drive / Force | GE Revolution Ascend Plus / Maxima | Philips Incisive 128 |
|:-----------------|:------------------------------|:-----------------------------------|:---------------------|
| **Modulare Automată Curent Tub** | **CARE Dose4D** (calibrare calitativă ref mAs) | **Smart mA / Auto mA** (zgomot țintă Noise Index - NI) | **DoseWise / Z-DOM / D-DOM** (DRI index) |
| **Selecție Automată Tensiune** | **CARE kV** (optimizat pentru substanță de contrast iodată) | **kV Assist** (adaptat la mărimea pacientului) | **Patient Specific kV** |
| **Reconstrucție Iterativă** | **ADMIRE** (Advanced Modeled Iterative Reconstruction, nivele 2-4) | **ASiR-V** (Adaptive Statistical Iterative Recon, 40-60%) / **TrueFidelity** (DLIR - Deep Learning) | **iDose4** (nivele 3-5) & **IMR** (Knowledge-based Iterative Model) |
| **Filtrare & Reducere Artefacte Metal** | **iMAR** (Iterative Metal Artifact Reduction) | **Smart MAR** | **O-MAR** (Orthopedic Metal Artifact Reduction) |
| **Viteze Rotație Gantry** | 0.28 s (Drive) / 0.25 s (Force) | 0.35 s (Ascend Plus) / 0.5 s | 0.33 s - 0.5 s |
| **Detector / Colimare Maximă** | $2 \times 64 \times 0.6$ mm / $2 \times 96 \times 0.6$ mm | $64 \times 0.625$ mm ($40$ mm lățime) | $64 \times 0.625$ mm ($40$ mm lățime) |

---

## 2. Parametri Impliciti de Scanare pe Regiuni Anatomice

### 2.1. Abdomen & Pelvis (Rutină cu Contrast)
- **Siemens Drive / Force:**
    - Mod scanare: Spirală, colimare $128 \times 0.6$ mm (Drive) / $192 \times 0.6$ mm (Force), pitch 0.8.
    - Tensiune/Curent: CARE kV (On, referință 100-120 kV), CARE Dose4D On (Quality Ref. mAs: 150-180 mAs).
    - Reconstrucție: Grosime secțiune 3.0 mm, increment 3.0 mm; Reconstrucție subțire 0.75 mm / 0.5 mm pentru reformate 3D MPR; Kernel I30f / I31f (ADMIRE 3).
- **GE Revolution Ascend Plus / VCT 64:**
    - Mod scanare: Helical, colimare $64 \times 0.625$ mm (40 mm beam), pitch 0.984:1, viteză rotație 0.5 s.
    - Tensiune/Curent: 120 kV (sau kV Assist), Smart mA On (interval 100-450 mA, Noise Index NI: 12.5 - 13.5).
    - Reconstrucție: 2.5 mm axiale + 2.5 mm coronale/sagitale; Reconstrucție iterativă ASiR-V 50%; Kernel Standard.
- **Philips Incisive 128:**
    - Mod scanare: Helical, colimare $64 \times 0.625$ mm, pitch 0.891, timp rotație 0.5 s.
    - Tensiune/Curent: 120 kV, DoseWise On (Dose Right Index DRI: 17).
    - Reconstrucție: 3.0 mm / 3.0 mm, Reconstrucție iterativă iDose4 nivel 3; Filter B (Smooth/Standard).

### 2.2. Torace Rutină & Angio-CT Pulmonar (PE Protocol)
- **Siemens SOMATOM:**
    - Colimare: $128 \times 0.6$ mm, pitch 1.2 (scanare ultra-rapidă sub 2 secunde pentru stop respirator optim).
    - Parametri: CARE kV On (la Angio PE selectează frecvent 80-90 kV pentru amplificarea densității iodului la k-edge de 33.2 keV).
    - Kernele de reconstrucție:
        - Țesut moale / mediastin: I30f (ADMIRE 3), grosime 3.0 mm.
        - Fereastră pulmonară de înaltă rezoluție: I70f / B70f (Sharp), grosime 1.0 - 1.5 mm.
- **GE Revolution:**
    - Helical, pitch 1.375:1, Noise Index 14.0, rotație 0.35 s.
    - Kernele: Standard pentru mediastin; Lung / Bone pentru parenchim pulmonar; ASiR-V 50%.
- **Philips Incisive:**
    - Helical, DRI 16, rotație 0.33 s, iDose4 nivel 4.
    - Kernele: Filter B pentru mediastin, Filter Y (Sharp) pentru parenchim pulmonar.

### 2.3. Neuro / Craniu Nativ (Head Non-Contrast)
- **Siemens Drive / go.Top:**
    - Mod: Secvențial (Axial) pentru eliminarea artefactelor de con/spirală în fosa posterioară, sau spirală dedicată cu pitch redus (0.55).
    - 120 kV fix, Quality Ref. mAs: 320 mAs (supra-tentorial) / 400 mAs (fosa posterioară).
    - Kernele: H31s / J30s (Creier țesut moale), H70h (Fereastră osoasă).
- **GE Ascend / VCT:**
    - Mod: Axial step-and-shoot, 120 kV, 300-350 mA fix sau Smart mA cu NI redus (8.5 - 9.5).
    - Kernele: Soft Tissue (Brain) 5.0 mm fosa posterioară + 5.0 mm vertex; Bone 1.25 mm.
- **Philips Incisive:**
    - Mod: Axial, 120 kV, 320 mAs, iDose4 nivel 4, Filter UB (Ultra Brain) + Filter HD (Bone).

---

## 3. Manualele Oficiale PDF Scanner Defaults

Documentația tehnică de fabrică a parametrilor impliciți pentru principalele platforme CT:

- [:material-file-pdf-box: Siemens SOMATOM Drive VB20 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20Drive%20Protocols%20%28VB20%29.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Siemens SOMATOM Force VA40 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20Force%20Protocols%20%28VA40%29.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE Revolution Ascend Plus Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20Revolution%20Ascend%20Plus%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Siemens SOMATOM go.Top Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20go.Top%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE LightSpeed VCT 64 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20LightSpeed%20VCT%2064%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Philips Incisive 128 CT Exam Protocol List](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/Philips%20Incisive%20128%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Siemens SOMATOM Definition AS 64 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/Definition%20AS%2064%20Protocols%20%28VB20%29.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE Revolution Maxima 64 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20Revolution%20Maxima%2064%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE LightSpeed 16 Reference Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20LightSpeed%2016%20Protocols.pdf){ target="_blank" rel="noopener" }
