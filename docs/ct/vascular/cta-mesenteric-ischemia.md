---
author: null
category: vascular
clinical_indications:
- Ischemie mezenterică acută (durere abdominală severă necorelată cu examenul clinic)
- Ischemie mezenterică cronică (angină abdominală postprandială, scădere ponderală)
- Suspiciune de infarct intestinal / necroză de ansă
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 5 mL/s
  roi: Aorta abdominală la originea trunchiului celiac
  timing: 'Fază dublă: Arterială + Venoasă Portală'
  trigger: 150 HU
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: MIP și randare 3D VR a trunchiului celiac și AMS. Reconstrucții
    MPR curbate pe întreg traiectul arterei mezenterice superioare din profil sagital.
  nursing: Linie venoasă 18-20G obligatorie pentru debitul de 5 mL/s.
  rad: 'Arterial: analizați ostiul și traiectul trunchiului celiac, arterei mezenterice
    superioare (AMS) și inferioare (AMI) (tromboză, embolie, disecție). Portal: evaluați
    grosimea peretelui anselor, prezența pneumatozei intestinale, a gazului în vena
    portă sau a trombozei VMS.'
  tech: Fază arterială la 25 secunde pentru evaluarea trunchiurilor vasculare. Fază
    venoasă portală la 70 secunde pentru perfuzia peretelui intestinal și a venei
    mezenterice superioare (VMS). Debit de injectare rapid (5 mL/s).
  tips: Scanare rapidă. Viteza ridicată de injectare este determinantă pentru vizualizarea
    ramurilor distale mezenterice.
npo: Repaus alimentar 4 ore (sau fără repaus în urgență)
position: Decubit dorsal cu brațele ridicate
premedication: None - emergent study
protocol_type: vascular
recons:
- acquisition: Fază Arterială
  fov: Abdomen
  kernel: Vascular
  notes: Originea și calibrul vaselor mezenterice
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Evaluarea prizelor de contrast ale pereților digestivi
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Arterială
  fov: Abdomen
  kernel: Vascular
  notes: MIP coronal al vaselor mezenterice
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Arterială
  fov: Abdomen
  kernel: Vascular
  notes: MPR curbat din profil sagital pe originile AMS și trunchiului celiac
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Documentați situația clinică de urgență
  renal: Verificați eGFR; în suspiciunea de ischemie acută nu se temporizează
series:
- delay: 25 sec
  end: Creste iliace
  name: Fază Arterială
  notes: Focus pe trunchiul celiac, AMS și AMI
  start: Diafragm
  thickness: 0.625 mm
- delay: 70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală
  notes: Evaluarea perfuziei peretelui intestinal și a venelor mezenterice
  start: Diafragm
  thickness: 0.625 mm
slug: cta-mesenteric-ischemia
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 300 mAs)
  pitch: '1.375'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Ischemie Mezenterică (Acută / Cronică)
---

# Angio-CT Ischemie Mezenterică (Acută / Cronică)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Arterială | 25 sec | Diafragm → Creste iliace |
        | Fază Venoasă Portală | 70 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Ischemie mezenterică acută (durere abdominală severă necorelată cu examenul clinic)
        - Ischemie mezenterică cronică (angină abdominală postprandială, scădere ponderală)
        - Suspiciune de infarct intestinal / necroză de ansă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore (sau fără repaus în urgență)
    - **Premedicație / Pregătire:**
        - None - emergent study

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 5 mL/s |
        | Durată | 20s |
        | Metodă Temporizare | Fază dublă: Arterială + Venoasă Portală |
        | Poziționare ROI | Aorta abdominală la originea trunchiului celiac |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto (referință 300 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Fază arterială la 25 secunde pentru evaluarea trunchiurilor vasculare. Fază venoasă portală la 70 secunde pentru perfuzia peretelui intestinal și a venei mezenterice superioare (VMS). Debit de injectare rapid (5 mL/s).

    === "Note Asistent"

        - Linie venoasă 18-20G obligatorie pentru debitul de 5 mL/s.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR; în suspiciunea de ischemie acută nu se temporizează
            - **Alergii:** Documentați situația clinică de urgență

    === "Note Radiolog"

        - Arterial: analizați ostiul și traiectul trunchiului celiac, arterei mezenterice superioare (AMS) și inferioare (AMI) (tromboză, embolie, disecție). Portal: evaluați grosimea peretelui anselor, prezența pneumatozei intestinale, a gazului în vena portă sau a trombozei VMS.

    === "Sfaturi & Recomandări"

        - Scanare rapidă. Viteza ridicată de injectare este determinantă pentru vizualizarea ramurilor distale mezenterice.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Arterială | Diafragm | Creste iliace | 25 sec | 0.625 mm | Focus pe trunchiul celiac, AMS și AMI |
    | Fază Venoasă Portală | Diafragm | Simfiză pubiană | 70 sec | 0.625 mm | Evaluarea perfuziei peretelui intestinal și a venelor mezenterice |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Arterială | Abdomen | 1.25 mm/1.25 mm | Vascular |  | Originea și calibrul vaselor mezenterice |
    | Axial | Fază Venoasă Portală | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Evaluarea prizelor de contrast ale pereților digestivi |
    | Coronal | Fază Arterială | Abdomen | 2 mm/2 mm | Vascular |  | MIP coronal al vaselor mezenterice |
    | Sagital | Fază Arterială | Abdomen | 1.5 mm/1.5 mm | Vascular |  | MPR curbat din profil sagital pe originile AMS și trunchiului celiac |
