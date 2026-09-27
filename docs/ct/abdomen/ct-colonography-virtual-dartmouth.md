---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: abdomen
clinical_indications:
- Screening cancer colorectal la adulți cu risc mediu care refuză sau au contraindicație
  la colonoscopie optică
- Colonoscopie optică incompletă (stenoză ocluzivă, dolicocolon, aderențe postoperatorii,
  intoleranță)
- Pacienți vârstnici, fragili sau aflați sub tratament anticoagulant/antiagregant
  ce nu poate fi întrerupt
contrast:
  agent: N/A (Fără contrast intravenos standard)
  duration: N/A
  flow_rate: N/A
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: Fără contrast IV
iris_reference:
  chapter: Abdomen & Pelvis
  radiation_dose: Clasa 2 (Scăzută 1 - 5 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: Explicați pacientului senzația de plenitudine abdominală cauzată de insuflație.
    CO2 se absoarbe mult mai rapid decât aerul ambiant, reducând disconfortul post-procedural.
  rad: 'Evaluați leziunile polipoide: mărime (dimensiune ≥ 6 mm este semnificativă),
    mobilitate între decubit dorsal și ventral, prezența marcajului baritat/iodat
    (fecaloamele captează bariu). Raportați conform clasificării C-RADS.'
  tech: Verificați topograma înainte de scanare pentru a vă asigura că toate segmentele
    (rect, sigmoid, colon descendent, transvers, ascendent, cec) sunt bine destinse.
    Reinsuflați dacă un segment este colabat.
  tips: Evaluarea combinată 2D (secțiuni axiale și coronale cu ferestre largi) și
    3D endoluminal maximizează sensibilitatea pentru polipi sesili.
npo: Dietă cu conținut scăzut de reziduuri 2-3 zile înainte; lichide clare în ziua
  precedentă
position: 'Dublă poziționare: decubit dorsal (supine) urmat de decubit ventral (prone)
  — sau decubit lateral stâng dacă pacienta nu poate sta pe burtă'
premedication: 'Protocol DHMC GoLytely cu Stool Tagging: Tagitol V (suspensie de bariu)
  administrat fracționat cu mesele în ziua pre-scanare + Gastrografin 20-30 mL seara
  înainte pentru marcarea lichidului rezidual. Administrare antispastic (Buscopan
  / Glucagon) i.v./i.m. la insuflație dacă nu există contraindicații.'
protocol_type: non-contrast
recons:
- acquisition: Supine & Prone
  fov: Abdomen-Pelvis
  ir_strength: High
  kernel: Standard Abdominal & Fereastră Plămân/Colon (-1000/200 HU)
  notes: Analiză 2D detaliată a peretelui colic și a organelor extracolice
  plane: Axial Primar
  thickness_increment: 1.25 mm / 1.0 mm
- acquisition: Supine & Prone
  fov: Lumen colic
  ir_strength: High
  kernel: Standard
  notes: Vizualizare tridimensională endoluminală bidirecțională (retrogradă și anterogradă)
  plane: Endoluminal 3D (Navigație Virtuală)
  thickness_increment: Endoscopic 3D Fly-through
safety:
  allergy: Fără risc de reacție la contrast IV.
  renal: Nu afectează funcția renală.
series:
- delay: După confirmarea distensiei colice optime pe topogramă
  end: Simfiză pubiană / canal anal
  name: 'Scanare 1: Decubit Dorsal (Supine)'
  notes: Insuficare automată cu CO2 sau pompă manuală cu aer până la toleranță și
    distensie completă a celor 6 segmente colice
  start: Cupole diafragmatice
  thickness: 1.0 mm
- delay: Imediat după rotirea pacientului
  end: Simfiză pubiană
  name: 'Scanare 2: Decubit Ventral (Prone)'
  notes: Mobilizarea polipilor vs. resturi fecale și redistribuirea aerului în segmentele
    dependente (rect, cecum)
  start: Cupole diafragmatice
  thickness: 1.0 mm
tech_params:
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 100 - 120 kVp
  mas: 30 - 50 mAs (Supine) / 25 - 40 mAs (Prone) — Protocol ultra low-dose
  pitch: 1.2 - 1.4
  rotation_time: 0.5 s
  scan_mode: Elicoidal ultra-rapid
  slice_thickness: 1.0 - 1.25 mm
title: CT Colonografie Virtuală - Pregătire & Scanare (Protocol Dartmouth Hitchcock)
---

# CT Colonografie Virtuală - Pregătire & Scanare (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Scanare 1: Decubit Dorsal (Supine) | După confirmarea distensiei colice optime pe topogramă | Cupole diafragmatice → Simfiză pubiană / canal anal |
        | Scanare 2: Decubit Ventral (Prone) | Imediat după rotirea pacientului | Cupole diafragmatice → Simfiză pubiană |

    === "Indicații Clinice"

        - Screening cancer colorectal la adulți cu risc mediu care refuză sau au contraindicație la colonoscopie optică
        - Colonoscopie optică incompletă (stenoză ocluzivă, dolicocolon, aderențe postoperatorii, intoleranță)
        - Pacienți vârstnici, fragili sau aflați sub tratament anticoagulant/antiagregant ce nu poate fi întrerupt

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Abdomen & Pelvis*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Scăzută 1 - 5 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Dublă poziționare: decubit dorsal (supine) urmat de decubit ventral (prone) — sau decubit lateral stâng dacă pacienta nu poate sta pe burtă
    - **Repaus Alimentar (NPO):** Dietă cu conținut scăzut de reziduuri 2-3 zile înainte; lichide clare în ziua precedentă
    - **Premedicație / Pregătire:**
        - Protocol DHMC GoLytely cu Stool Tagging: Tagitol V (suspensie de bariu) administrat fracționat cu mesele în ziua pre-scanare + Gastrografin 20-30 mL seara înainte pentru marcarea lichidului rezidual. Administrare antispastic (Buscopan / Glucagon) i.v./i.m. la insuflație dacă nu există contraindicații.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | N/A (Fără contrast intravenos standard) |
        | Volum | Fără contrast IV |
        | Rată de Flux | N/A |
        | Durată | N/A |
        | Metodă Temporizare | N/A |
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
    | **Tensiune Tub (kV)** | 100 - 120 kVp kV |
    | **Curent Tub (mAs)** | 30 - 50 mAs (Supine) / 25 - 40 mAs (Prone) — Protocol ultra low-dose |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.0 - 1.25 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.2 - 1.4 |
    | **Mod Scanare** | Elicoidal ultra-rapid |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Verificați topograma înainte de scanare pentru a vă asigura că toate segmentele (rect, sigmoid, colon descendent, transvers, ascendent, cec) sunt bine destinse. Reinsuflați dacă un segment este colabat.

    === "Note Asistent"

        - Explicați pacientului senzația de plenitudine abdominală cauzată de insuflație. CO2 se absoarbe mult mai rapid decât aerul ambiant, reducând disconfortul post-procedural.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu afectează funcția renală.
            - **Alergii:** Fără risc de reacție la contrast IV.

    === "Note Radiolog"

        - Evaluați leziunile polipoide: mărime (dimensiune ≥ 6 mm este semnificativă), mobilitate între decubit dorsal și ventral, prezența marcajului baritat/iodat (fecaloamele captează bariu). Raportați conform clasificării C-RADS.

    === "Sfaturi & Recomandări"

        - Evaluarea combinată 2D (secțiuni axiale și coronale cu ferestre largi) și 3D endoluminal maximizează sensibilitatea pentru polipi sesili.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scanare 1: Decubit Dorsal (Supine) | Cupole diafragmatice | Simfiză pubiană / canal anal | După confirmarea distensiei colice optime pe topogramă | 1.0 mm | Insuficare automată cu CO2 sau pompă manuală cu aer până la toleranță și distensie completă a celor 6 segmente colice |
    | Scanare 2: Decubit Ventral (Prone) | Cupole diafragmatice | Simfiză pubiană | Imediat după rotirea pacientului | 1.0 mm | Mobilizarea polipilor vs. resturi fecale și redistribuirea aerului în segmentele dependente (rect, cecum) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial Primar | Supine & Prone | Abdomen-Pelvis | 1.25 mm / 1.0 mm | Standard Abdominal & Fereastră Plămân/Colon (-1000/200 HU) | High | Analiză 2D detaliată a peretelui colic și a organelor extracolice |
    | Endoluminal 3D (Navigație Virtuală) | Supine & Prone | Lumen colic | Endoscopic 3D Fly-through | Standard | High | Vizualizare tridimensională endoluminală bidirecțională (retrogradă și anterogradă) |
