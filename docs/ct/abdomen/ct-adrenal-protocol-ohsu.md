---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Caracterizarea unui incidentalor suprarenalian descoperit la alte examinări imagistice
- Diferențierea adenomului suprarenalian benign de metastaza suprarenaliană sau carcinomul
  corticosuprarenalian
- Evaluarea formațiunilor suprarenaliene cu densitate nativă intermediară (10–30 HU)
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 30-35s
  flow_rate: 3.0 mL/s
  roi: N/A
  timing: Fază Portală/Venoasă la 60 secunde + Fază Tardivă la 15 minute (900 secunde)
  trigger: N/A
  volume: 100 mL
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții coronale fine pentru aprecierea raportului cu polul
    superior renal.
  nursing: Menținerea pacientului în departament pe durata celor 15 minute dintre
    injectare și faza tardivă.
  rad: 'Calcul Washout: 1) APW = [(HU_60s - HU_15min) / (HU_60s - HU_nativ)] × 100.
    APW ≥ 60% = Adenom. 2) RPW = [(HU_60s - HU_15min) / HU_60s] × 100. RPW ≥ 40% =
    Adenom.'
  tech: Tensiunea tubului TREBUIE setată la 120 kV pe toate fazele; algoritmii de
    variație a kV (CAREkV) trebuie dezactivați deoarece alterează valorile HU de referință.
  tips: Evitați plasarea ROI-ului în ariile de necroză sau calcificare; ROI-ul trebuie
    să acopere cel puțin 50-70% din aria leziunii pe secțiunea cea mai mare.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Fără contrast oral
protocol_type: multiphase
recons:
- acquisition: Toate cele 3 faze
  fov: Suprarenale
  ir_strength: Standard
  kernel: Standard / I30f
  notes: Secțiuni fine pentru plasarea precisă a ROI-ului în leziune
  plane: Axial & Coronal
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m².
series:
- delay: 0 sec
  end: Sub polul inferior renal (L3)
  name: Fază Nativă (Suprarenale)
  notes: Dacă densitatea leziunii este ≤ 10 HU pe nativ, diagnosticul de adenom bogat
    în lipide este cert și examinarea se poate opri aici!
  start: Deasupra glandelor suprarenale (T11)
  thickness: 1.0 mm
- delay: 60 sec
  end: Pol inferior renal
  name: Fază Venoasă Portală (60 sec)
  notes: Măsurare densitate maximă de încărcare a masei suprarenaliene
  start: Suprarenale
  thickness: 1.0 mm
- delay: 15 min (900 sec)
  end: Pol inferior renal
  name: Fază Tardivă (15 minute)
  notes: Calculul spălării absolute (APW) și relative (RPW) a contrastului
  start: Suprarenale
  thickness: 1.0 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV (tensiune fixă obligatorie pentru validitatea măsurării HU)
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Glande Suprarenale / Washout Protocol (Protocol OHSU)
---

# CT Glande Suprarenale / Washout Protocol (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă (Suprarenale) | 0 sec | Deasupra glandelor suprarenale (T11) → Sub polul inferior renal (L3) |
        | Fază Venoasă Portală (60 sec) | 60 sec | Suprarenale → Pol inferior renal |
        | Fază Tardivă (15 minute) | 15 min (900 sec) | Suprarenale → Pol inferior renal |

    === "Indicații Clinice"

        - Caracterizarea unui incidentalor suprarenalian descoperit la alte examinări imagistice
        - Diferențierea adenomului suprarenalian benign de metastaza suprarenaliană sau carcinomul corticosuprarenalian
        - Evaluarea formațiunilor suprarenaliene cu densitate nativă intermediară (10–30 HU)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 100 mL |
        | Rată de Flux | 3.0 mL/s |
        | Durată | 30-35s |
        | Metodă Temporizare | Fază Portală/Venoasă la 60 secunde + Fază Tardivă la 15 minute (900 secunde) |
        | Poziționare ROI | N/A |
        | Declanșator (HU) | N/A |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV (tensiune fixă obligatorie pentru validitatea măsurării HU) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm / 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Tensiunea tubului TREBUIE setată la 120 kV pe toate fazele; algoritmii de variație a kV (CAREkV) trebuie dezactivați deoarece alterează valorile HU de referință.

    === "Note Asistent"

        - Menținerea pacientului în departament pe durata celor 15 minute dintre injectare și faza tardivă.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m².
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Calcul Washout: 1) APW = [(HU_60s - HU_15min) / (HU_60s - HU_nativ)] × 100. APW ≥ 60% = Adenom. 2) RPW = [(HU_60s - HU_15min) / HU_60s] × 100. RPW ≥ 40% = Adenom.

    === "Sfaturi & Recomandări"

        - Evitați plasarea ROI-ului în ariile de necroză sau calcificare; ROI-ul trebuie să acopere cel puțin 50-70% din aria leziunii pe secțiunea cea mai mare.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă (Suprarenale) | Deasupra glandelor suprarenale (T11) | Sub polul inferior renal (L3) | 0 sec | 1.0 mm | Dacă densitatea leziunii este ≤ 10 HU pe nativ, diagnosticul de adenom bogat în lipide este cert și examinarea se poate opri aici! |
    | Fază Venoasă Portală (60 sec) | Suprarenale | Pol inferior renal | 60 sec | 1.0 mm | Măsurare densitate maximă de încărcare a masei suprarenaliene |
    | Fază Tardivă (15 minute) | Suprarenale | Pol inferior renal | 15 min (900 sec) | 1.0 mm | Calculul spălării absolute (APW) și relative (RPW) a contrastului |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial & Coronal | Toate cele 3 faze | Suprarenale | 2.0 mm / 2.0 mm | Standard / I30f | Standard | Secțiuni fine pentru plasarea precisă a ROI-ului în leziune |
