---
author: Medford Radiology Group (MRG) / ACR Appropriateness Criteria
category: chest
clinical_indications:
- Suspiciune de trombembolism pulmonar acut (TEP) la paciente gravide
- Dispnee brusc instalată, durere toracică pleuritică, tahicardie inexplicabilă în sarcină
- Algoritm YEARS / Geneva adaptat sarcinii pozitiv sau D-dimeri crescuți anormal
- Suspiciune de infarct pulmonar sau trombembolism cu risc hemodinamic intermediar/înalt
contrast:
  agent: Substanță de contrast iodată non-ionică (Optiray 350 / Omnipaque 350 / Isovue 370)
  duration: 12-14s
  flow_rate: 4.0 - 4.5 mL/s
  roi: Trunchiul arterei pulmonare principale
  timing: Bolus tracking automat cu ROI în trunchiul arterei pulmonare (trigger 100 HU)
  trigger: 100 HU
  volume: 60 - 70 mL + 40 mL flush salin
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 2 (Mică 1 - 5 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-27'
notes:
  additional_recons: MIP axial 5 mm și coronal 5 mm pentru analiza arterelor segmentare
    și subsegmentare. Reconstrucții subțiri 0.625 - 1.0 mm în filtru pulmonar și mediastinal.
  nursing: Canulă 18G sau 20G în plica cotului. Asigurarea bunei hidratări per os sau IV.
    Test de toleranță și verificare rezistență vasculară înainte de injectarea automată.
  rad: Prioritizarea etapelor non-iradiante! Conform ghidului MRG, o ecografie Doppler venoasă
    a membrelor inferioare pozitivă pentru TVP confirmă diagnosticul și instituie direct
    anticoagularea terapeutică cu LMWH, scutind pacienta și fătul de scanarea toracică.
    Dacă se efectuează Angio-CT, căutați defecte de umplere endoluminale și semne de cord pulmonar acut.
  tech: Tehnica Low-kV (80 - 100 kVp) optimizează semnalul iodului la K-edge (33.2 keV)
    și scade considerabil doza de radiație. Scanare în direcție caudo-cranială pentru a
    evita artefactele respiratorii bazale. Șorț plumbat extern pelvin/abdominal (reducere scatter).
  tips: 'Instrucțiuni de respirație: inspir blând superficial fără manevră Valsalva;
    Valsalva crește presiunea intratoracică, blochează afluxul din cava inferioară și aduce
    un aflux masiv de sânge neopacifiat din cava superioară, provocând diluția tranzitorie a contrastului.'
npo: Repaus alimentar 2-4 ore dacă starea pacientei permite; în urgență N/A
position: Decubit dorsal cu brațele ridicate deasupra capului; ușoară înclinare laterală
  stânga (10-15°) dacă sarcina este avansată (trimestrul III) pentru decompresia venei cave inferioare.
premedication: Fără contrast oral
protocol_type: contrast-enhanced
recons:
- acquisition: Angio-CT Pulmonar (Low-kV)
  fov: Torace (optimizat strâns pe cutia toracică)
  ir_strength: Nivel înalt (Admire 4 / ASiR-V 50-60% / iDose4)
  kernel: Mediastinal standard (contrast înalt vascular)
  notes: Detecție defecte de umplere endoluminale în arborele arterial pulmonar
  plane: Axial
  thickness_increment: 1.0 mm / 0.7 mm
- acquisition: Angio-CT Pulmonar (Low-kV)
  fov: Torace
  ir_strength: Nivel înalt
  kernel: Pulmonar de înaltă rezoluție
  notes: Evaluare condensări pulmonare, infarct pulmonar cuneiform sau atelectazii
  plane: Axial
  thickness_increment: 1.5 mm / 1.5 mm
- acquisition: Reconstrucții Multiplanare (MPR / MIP)
  fov: Torace
  ir_strength: Nivel înalt
  kernel: Mediastinal standard
  notes: MIP coronal și sagital pentru ramurile lobare și segmentare
  plane: Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Conform politicii MRG Premedication. Dacă reacția anterioară a fost ușoară/moderată
    și examinarea este urgentă, protocol IV cu Solu-Medrol 40 mg IV cu 4-6h pre-scanare.
  renal: Verificare eGFR dacă pacienta prezintă nefropatie preexistentă; contrastul iodat
    nu este teratogen și nu se reține la gravide dacă este esențial pentru diagnosticul TEP.
series:
- delay: Bolus tracking (trigger 100 HU + 3s)
  end: Vârfuri pulmonare (deasupra apicilor)
  name: Angio-CT Pulmonar Doză Redusă (Low-kV)
  notes: Opacifiere intensă a arterelor pulmonare (> 300 HU datorită K-edge la 80-100 kVp)
  start: Baza plămânilor (unghiurile costo-diafragmatice posterioare)
  thickness: 0.625 mm
sources:
- edition: '2023'
  locator: Guideline for Suspected PE in Pregnancy & ACR Appropriateness Criteria
  title: Medford Radiology Group Clinical Guidelines
  url: https://medfordradiology.com/clinical-guidelines/
- edition: '2023'
  locator: Suspected PE in Pregnancy
  title: Medford Radiology Reading Room Documents
  url: https://medfordradiology.com/wp-content/uploads/2017/06/CLIN-PE-in-Pregnancy.pdf
tech_params:
  collimation: 128 × 0.6 mm sau 64 × 0.625 mm
  kv: 80 - 100 kVp (ajustat în funcție de greutatea pacientei)
  mas: Modulare automată a curentului de tub (CAREDose4D / SmartmA / SUREExposure)
  pitch: 1.2 - 1.4
  rotation_time: 0.28 - 0.33 s
  scan_mode: Elicoidal ultra-rapid
  slice_thickness: 0.625 mm
title: Protocol Angio-CT Torace & Algoritm Suspiciune Embolie Pulmonară în Sarcină (MRG / ACR)
---

# Protocol Angio-CT Torace & Algoritm Suspiciune Embolie Pulmonară în Sarcină (MRG / ACR)

**Ultima actualizare:** 2026-09-27  
**Autori:** Medford Radiology Group (MRG) / ACR Appropriateness Criteria Guidelines Committee  

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic & Algoritm Strategic__

    ---

    === "Rezumat Achiziție CT"

        | Serie | Fază / Declanșare | Acoperire Anatomică | Volum & Debit Contrast |
        |:---|:---|:---|:---|
        | **Angio-CT Pulmonar Low-kV** | Bolus Tracking (ROI trunchi AP, trigger 100 HU + 3s) | Baza plămânilor (diafragm) → Vârfuri pulmonare (direcție caudo-cranială) | 60 - 70 mL la 4.0 - 4.5 mL/s + 40 mL ser fiziologic |

    === "Indicații Clinice"

        - Suspiciune înaltă de trombembolism pulmonar acut (TEP) la pacienta gravidă în oricare trimestru de sarcină
        - Debut brusc de dispnee, tahicardie inexplicabilă, durere toracică pleuritică sau hemoptizie
        - Scor clinic YEARS sau Geneva revizuit sugestiv, sau valori crescute ale D-dimerilor
        - Suspiciune de cord pulmonar acut sau colaps hemodinamic nespecific

    === "Ghid Național IRIS"

        !!! info "Referință Ghid Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Mică 1 - 5 mSv)` prin optimizare Low-kV (80-100 kVp)

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary }

-   __2. Pregătire Pacient & Protecție Fetală__

    ---

    - **Poziționare:** Decubit dorsal cu brațele ridicate deasupra capului. În trimestrul III de sarcină, se recomandă o ușoară înclinare pe flancul stâng (10-15°) cu o perină sub fesa dreaptă pentru a preveni compresiunea venei cave inferioare de către uterul gravid.
    - **Protecție Plumbată:** Șorț de plumb așezat peste abdomen și pelvis (pentru a reduce radiația împrăștiată secundară din gantry).
    - **Acces Venos:** Canulă intravenoasă 18G sau 20G în plica cotului (evitarea venelor fragile ale mâinii pentru debite de 4.0-4.5 mL/s).

</div>

---

## Algoritmul Diagnostic MRG / ACR pentru Suspiciunea de TEP în Sarcină

```mermaid
flowchart TD
    Start["Gravidă cu Suspiciune Clinică de TEP<br/>(Dispnee, Durere Pleuritică, Tahicardie)"] --> CXR["Etapa 1: Radiografie Toracică (CXR) cu Scut Pelvin<br/>(Scor ACR: 9 / Iradiere Fetală < 0.001 mGy)"]
    
    CXR --> CXREval{"Rezultat Radiografie Toracică (CXR)"}
    
    CXREval -->|"Anormală<br/>(Opacități, Pleurezie, Atelectazie)"| DirectCTA["Cale Directă: Angio-CT Torace (CTA Chest)<br/>Protocol Low-kV (80-100 kVp)<br/>(Scintigrafia V/Q ar fi neconcludentă din cauza leziunilor parenchimatoase)"]
    
    CXREval -->|"Normală"| USDoppler["Etapa 2: Ecografie Doppler Venos Membre Inferioare (LE US)<br/>(Scor ACR: 8 / Iradiere Fetală: ZERO)"]
    
    USDoppler --> DVTCheck{"Tromboză Venoasă Profundă (TVP) Prezentă?"}
    
    DVTCheck -->|"POZITIVĂ (Tromboză Confirmată)"| TreatDVT["DIAGNOSTIC STABILIT PRIN METODĂ NON-IRADIANTĂ!<br/>Se inițiază tratamentul anticoagulant terapeutic (LMWH).<br/>NU mai este necesară nicio scanare toracică iradiantă!"]
    
    DVTCheck -->|"NEGATIVĂ"| ChoiceThorax["Etapa 3: Explorare Pulmonară Directă"]
    
    ChoiceThorax --> ChoiceVQ["Opțiunea 1: Scintigrafie de Perfuzie Tc-99m MAA Doză Redusă<br/>(Doar Perfuzie Q, fără componentă de ventilație V)<br/>Doză fetală minimă (< 0.5 mGy), iradiere mamară neglijabilă"]
    ChoiceThorax --> ChoiceCTA["Opțiunea 2: Angio-CT Torace (CTA Chest Low-kV)<br/>Disponibilitate imediată 24/7, exclude alte patologii toracice acute"]
```

---

## Comparație Dozimetrică Maternă & Fetală (CTA Torace vs. Scintigrafie V/Q)

| Parametru de Iradiere | Angio-CT Torace (CTA Chest Low-kV) | Scintigrafie Perfuzie Tc-99m MAA (Doză Redusă) | Concluzie Clinică & Decizie |
|:---|:---|:---|:---|
| **Doza la Glanda Mamară Maternă** | 10 – 30 mGy (țesut glandular radiosensibil proliferat în sarcină) | 0.2 – 0.5 mGy (semnificativ mai mică) | Scintigrafia de perfuzie protejează parenchimul mamar matern; CTA impune colimare strânsă și reconstrucții iterative |
| **Doza Fetală Absorbită** | 0.05 – 0.2 mGy (infimă, mult sub pragul teratogen de 50-100 mGy) | 0.1 – 0.5 mGy (excreție urinară a trasorului lângă uter) | Ambele metode sunt sigure pentru făt, doza fiind de mii de ori sub pragul de risc teratogen |
| **Disponibilitate & Viteză** | Imediată 24/7 (achiziție în 2-3 secunde) | Variabilă (necesită radiofarmaceutic disponibil și cameră gamma) | CTA este investigația de elecție în gardă și la paciente instabile |
| **Acuratețe în caz de CXR anormală** | Diagnostic cert de TEP + patologie alternativă (pneumonie, disecție, revărsat) | Risc ridicat de examinare neconcludentă / nedeterminată | Dacă radiografia toracică este anormală, **CTA este obligatorie** |

---

## Protocol Tehnic de Scanare CT Low-kV la Gravide

1. **Optimizarea Tensiunii de Tub (80 - 100 kVp):**
    - Scăderea tensiunii de la 120 kVp la 80 sau 100 kVp apropie energia fotonilor X de vârful de absorbție fotoelectrică a iodului (K-edge = 33.2 keV).
    - Permite o intensitate de semnal endoluminal mult mai mare (> 350-400 HU) cu un volum redus de contrast (60 mL) și o reducere a dozei totale de radiație cu până la 40-50%.
2. **Direcție de Scanare Caudo-Cranială:**
    - Scanarea începe de la diafragm spre apexurile pulmonare.
    - La pacientele gravide, presiunea intraabdominală crescută și efortul respirator duc la degradarea calității imagistice la bazele plămânilor la finalul apneei; direcția caudo-cranială surprinde bazele în prima secundă de achiziție, la concentrația maximă a bolusului de contrast.
3. **Prevenirea Diluției Tranzitorii a Contrastului (Transient Interruption of Contrast):**
    - Fenomenul apare frecvent la pacientele tinere și gravide când inspiră adânc imediat înainte de scanare (manevra Valsalva urmată de inspir profund).
    - Presiunea negativă intratoracică atrage un volum masiv de sânge neopacifiat din vena cavă inferioară direct în atriul drept și ventriculul drept, diluând bolusul de contrast din arterele pulmonare.
    - **Soluție practică:** Pacienta este instruită să respire liniștit și să țină o apnee blândă, fără inspir forțat.

---

## Recomandări Post-Procedură & Alăptare

- **Hidratare:** Se recomandă hidratare suplimentară (500-1000 mL apă plată sau fluide IV) pentru accelerarea excreției renale a substanței de contrast.
- **Funcția Tiroidiană Fetală / Neonatală:** Iodul administrat transplacentar se metabolizează rapid; se notează în dosarul obstetrical administrarea substanței de contrast pentru screeningul neonatal de rutină al TSH la naștere.
- **Alăptare:** Conform ACR și ghidului MRG, substanțele de contrast iodate non-ionice sunt sigure; cantitatea excretată în lapte este sub 0.04%, iar absorbția intestinală a nou-născutului este neglijabilă. Alăptarea poate continua normal.
