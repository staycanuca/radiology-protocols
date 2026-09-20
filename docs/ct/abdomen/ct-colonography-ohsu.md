---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Screening pentru polipi colonici și cancer colorectal la adulți cu risc mediu
- Colonoscopie optică incompletă (dolicocolon, stenoză obstructivă, aderențe post-operatorii)
- Pacienți tarați sau cu comorbidități severe care contraindică sedarea/anestezia
  colonoscopiei optice
contrast:
  agent: CO2 (insuflare colonică mecanică automată cu insuflator dedicat) sau aer
    ambiental
  duration: N/A
  flow_rate: N/A
  roi: N/A
  timing: După distensie colonică adecvată verificată pe scout
  trigger: N/A
  volume: Insuflare până la presiune de 15-20 mmHg (aprox. 1.5 - 2.5 L CO2)
last_updated: '2026-09-20'
notes:
  additional_recons: Randare 3D virtuală a suprafeței mucoasei colonice.
  nursing: Asistență la insuflare și monitorizarea confortului pacientului (spasme
    abdominale reduse prin administrare de antispastic Buscopan/Glucagon dacă nu este
    contraindicat).
  rad: Navigare 2D și 3D endoluminală; diferențiere polip sesil/pediculat (nemobil)
    de materii fecale reziduale (mobile pe prone sau marcate cu contrast - tagging).
    Raportare conform C-RADS.
  tech: Inserție sondă rectală moale, insuflare controlată de CO2 cu pompă automată.
    Scout AP și profil pentru confirmarea distensiei optime înainte de scanarea elicoidală.
  tips: Utilizarea CO2 în locul aerului ambiental este mult superioară deoarece CO2
    se absoarbe rapid prin mucoasa colică, eliminând balonarea și durerea post-procedură.
npo: Pregătire colonică completă cu o zi înainte (soluție polietilenglicol / citrat
  de magneziu)
position: 'Scanare în 2 poziții: 1) Decubit dorsal (Supine); 2) Decubit ventral (Prone)
  sau decubit lateral stâng'
premedication: Fecal tagging cu contrast iodat oral slab (Gastrografin 20-30 mL) și
  suspensie fină de bariu în seara precedentă
protocol_type: specialized
recons:
- acquisition: Supine & Prone
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Secțiuni subțiri pentru navigație endoluminală 3D 'fly-through'
  plane: Axial & Coronal
  thickness_increment: 1.25 mm / 1.0 mm
safety:
  allergy: N/A — fără contrast intravenos
  renal: N/A — fără contrast intravenos
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: CT Colonografie — Decubit Dorsal (Supine)
  notes: Apnee inspiratorie completă; verificare distensie cec, unghiuri și sigmoid
  start: Cupole diafragmatice
  thickness: 0.625 mm
- delay: 0 sec
  end: Simfiză pubiană
  name: CT Colonografie — Decubit Ventral (Prone)
  notes: Schimbarea poziției permite deplasarea lichidului rezidual și a aerului în
    segmentele colice colabate pe supine
  start: Cupole diafragmatice
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100-120 kV
  mas: 30-50 mAs (Doză ultra-joasă / Low-Dose CTDIvol < 3-5 mGy)
  pitch: 1.0 - 1.2
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Colonografie / Colonoscopie Virtuală (Protocol OHSU)
---

# CT Colonografie / Colonoscopie Virtuală (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Colonografie — Decubit Dorsal (Supine) | 0 sec | Cupole diafragmatice → Simfiză pubiană |
        | CT Colonografie — Decubit Ventral (Prone) | 0 sec | Cupole diafragmatice → Simfiză pubiană |

    === "Indicații Clinice"

        - Screening pentru polipi colonici și cancer colorectal la adulți cu risc mediu
        - Colonoscopie optică incompletă (dolicocolon, stenoză obstructivă, aderențe post-operatorii)
        - Pacienți tarați sau cu comorbidități severe care contraindică sedarea/anestezia colonoscopiei optice

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Scanare în 2 poziții: 1) Decubit dorsal (Supine); 2) Decubit ventral (Prone) sau decubit lateral stâng
    - **Repaus Alimentar (NPO):** Pregătire colonică completă cu o zi înainte (soluție polietilenglicol / citrat de magneziu)
    - **Premedicație / Pregătire:**
        - Fecal tagging cu contrast iodat oral slab (Gastrografin 20-30 mL) și suspensie fină de bariu în seara precedentă

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | CO2 (insuflare colonică mecanică automată cu insuflator dedicat) sau aer ambiental |
        | Volum | Insuflare până la presiune de 15-20 mmHg (aprox. 1.5 - 2.5 L CO2) |
        | Rată de Flux | N/A |
        | Durată | N/A |
        | Metodă Temporizare | După distensie colonică adecvată verificată pe scout |
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
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | 30-50 mAs (Doză ultra-joasă / Low-Dose CTDIvol < 3-5 mGy) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0 - 1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Inserție sondă rectală moale, insuflare controlată de CO2 cu pompă automată. Scout AP și profil pentru confirmarea distensiei optime înainte de scanarea elicoidală.

    === "Note Asistent"

        - Asistență la insuflare și monitorizarea confortului pacientului (spasme abdominale reduse prin administrare de antispastic Buscopan/Glucagon dacă nu este contraindicat).

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — fără contrast intravenos
            - **Alergii:** N/A — fără contrast intravenos

    === "Note Radiolog"

        - Navigare 2D și 3D endoluminală; diferențiere polip sesil/pediculat (nemobil) de materii fecale reziduale (mobile pe prone sau marcate cu contrast - tagging). Raportare conform C-RADS.

    === "Sfaturi & Recomandări"

        - Utilizarea CO2 în locul aerului ambiental este mult superioară deoarece CO2 se absoarbe rapid prin mucoasa colică, eliminând balonarea și durerea post-procedură.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Colonografie — Decubit Dorsal (Supine) | Cupole diafragmatice | Simfiză pubiană | 0 sec | 0.625 mm | Apnee inspiratorie completă; verificare distensie cec, unghiuri și sigmoid |
    | CT Colonografie — Decubit Ventral (Prone) | Cupole diafragmatice | Simfiză pubiană | 0 sec | 0.625 mm | Schimbarea poziției permite deplasarea lichidului rezidual și a aerului în segmentele colice colabate pe supine |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial & Coronal | Supine & Prone | Abdomen | 1.25 mm / 1.0 mm | Standard / I30f | Admire 3 / AIDR 3D | Secțiuni subțiri pentru navigație endoluminală 3D 'fly-through' |
