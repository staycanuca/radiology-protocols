---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: vascular
clinical_indications:
- Boală arterială periferică obstructivă (BAPO / PAD) cu claudicație intermitentă
  invalidantă
- Ischemie critică de membru (durere de repaus, ulcerații ischemice, gangrenă)
- Ischemie acută de membru inferior (embolie/tromboză arterială acută)
- Planificare pre-revascularizare (angioplastie percutană cu stent vs bypass chirurgical
  femuro-popliteu/femuro-distal)
- Evaluare post-operatorie de permeabilitate a bypass-ului vascular sau stenturilor
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 30s
  flow_rate: 4.0 - 5.0 mL/s
  roi: Aorta abdominală distală
  timing: Bolus tracking la nivelul aortei abdominale distale (deasupra bifurcației
    iliace, trigger 150 HU)
  trigger: 150 HU
  volume: 120-150 mL
iris_reference:
  chapter: Aparat cardiovascular & Sistem vascular
  radiation_dose: Clasa 4 (Ridicată > 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D VR cu substracție osoasă automată a scheletului
    pelvin și al membrelor inferioare.
  nursing: Verificare pulsuri periferice și temperatură cutanată distală.
  rad: Descrieți stenozele conform clasificării TASC II; evaluați permeabilitatea
    celor 3 vase gambiere (tibială anterioară, tibială posterioară, fibulară/peronieră)
    și reconstituirea arcului plantar.
  tech: Canulă 18G antecubitală. Flush salin generos (50 mL la 4.5 mL/s). Viteza mesei
    trebuie calibrată atent pentru a nu depăși bolusul de contrast la pacienții cu
    flux lent / boală arterială severă.
  tips: La pacienți cu ischemie critică sau diabet, viteza de curgere a sângelui este
    redusă; un pitch mai mic sau un delay suplimentar de 2-3 secunde previne scanarea
    înaintea contrastului.
npo: Repaus alimentar 4 ore; hidratare orală permisă
position: Decubit dorsal, picioarele poziționate primele în gantry (feet-first), picioarele
  rotite ușor intern și imobilizate cu bandă adezivă
premedication: Fără contrast oral
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Runoff
  fov: Abdomen, Bazin & Membre Inferioare
  ir_strength: Standard
  kernel: Vascular / I30f
  notes: Secțiuni axiale fine pentru evaluarea stenozelor excentrice și plăcilor calcificate
  plane: Axial
  thickness_increment: 1.0 mm / 1.0 mm
- acquisition: CTA Runoff
  fov: Bazin & Membre Inferioare
  ir_strength: Standard
  kernel: Vascular
  notes: 'MIP pe segmente: 1) Aorto-iliac; 2) Femuro-popliteu; 3) Tibio-peronier și
    arc plantar'
  plane: Coronal
  thickness_increment: 5.0 mm / 2.5 mm MIP
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m² obligatoriu (la diabetici se verifică statusul hidratării).
series:
- delay: Trigger + 4-6 sec
  end: Vârful degetelor picioarelor (inclusiv arcul plantar)
  name: CTA Runoff Membre Inferioare
  notes: Scanare continuă sincronizată cu bolusul de contrast pe tot traiectul arterial
    până la nivelul labei piciorului
  start: Nivelul diafragmului / trunchiului celiac
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0 (adaptat vitezei de propagare a contrastului)
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal continuu pe cursă lungă (aprox. 1200-1400 mm)
  slice_thickness: 0.625 mm
title: CTA Runoff Membre Inferioare & Aorto-Iliac (Protocol OHSU)
---

# CTA Runoff Membre Inferioare & Aorto-Iliac (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CTA Runoff Membre Inferioare | Trigger + 4-6 sec | Nivelul diafragmului / trunchiului celiac → Vârful degetelor picioarelor (inclusiv arcul plantar) |

    === "Indicații Clinice"

        - Boală arterială periferică obstructivă (BAPO / PAD) cu claudicație intermitentă invalidantă
        - Ischemie critică de membru (durere de repaus, ulcerații ischemice, gangrenă)
        - Ischemie acută de membru inferior (embolie/tromboză arterială acută)
        - Planificare pre-revascularizare (angioplastie percutană cu stent vs bypass chirurgical femuro-popliteu/femuro-distal)
        - Evaluare post-operatorie de permeabilitate a bypass-ului vascular sau stenturilor

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat cardiovascular & Sistem vascular*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 4 (Ridicată > 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, picioarele poziționate primele în gantry (feet-first), picioarele rotite ușor intern și imobilizate cu bandă adezivă
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore; hidratare orală permisă
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 120-150 mL |
        | Rată de Flux | 4.0 - 5.0 mL/s |
        | Durată | 30s |
        | Metodă Temporizare | Bolus tracking la nivelul aortei abdominale distale (deasupra bifurcației iliace, trigger 150 HU) |
        | Poziționare ROI | Aorta abdominală distală |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 (adaptat vitezei de propagare a contrastului) |
    | **Mod Scanare** | Elicoidal continuu pe cursă lungă (aprox. 1200-1400 mm) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 18G antecubitală. Flush salin generos (50 mL la 4.5 mL/s). Viteza mesei trebuie calibrată atent pentru a nu depăși bolusul de contrast la pacienții cu flux lent / boală arterială severă.

    === "Note Asistent"

        - Verificare pulsuri periferice și temperatură cutanată distală.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m² obligatoriu (la diabetici se verifică statusul hidratării).
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Descrieți stenozele conform clasificării TASC II; evaluați permeabilitatea celor 3 vase gambiere (tibială anterioară, tibială posterioară, fibulară/peronieră) și reconstituirea arcului plantar.

    === "Sfaturi & Recomandări"

        - La pacienți cu ischemie critică sau diabet, viteza de curgere a sângelui este redusă; un pitch mai mic sau un delay suplimentar de 2-3 secunde previne scanarea înaintea contrastului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CTA Runoff Membre Inferioare | Nivelul diafragmului / trunchiului celiac | Vârful degetelor picioarelor (inclusiv arcul plantar) | Trigger + 4-6 sec | 0.625 mm | Scanare continuă sincronizată cu bolusul de contrast pe tot traiectul arterial până la nivelul labei piciorului |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA Runoff | Abdomen, Bazin & Membre Inferioare | 1.0 mm / 1.0 mm | Vascular / I30f | Standard | Secțiuni axiale fine pentru evaluarea stenozelor excentrice și plăcilor calcificate |
    | Coronal | CTA Runoff | Bazin & Membre Inferioare | 5.0 mm / 2.5 mm MIP | Vascular | Standard | MIP pe segmente: 1) Aorto-iliac; 2) Femuro-popliteu; 3) Tibio-peronier și arc plantar |
