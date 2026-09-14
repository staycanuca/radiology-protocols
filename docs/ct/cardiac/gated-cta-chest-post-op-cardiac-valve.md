---
author: null
category: cardiac
clinical_indications:
- Evaluarea funcțională a protezelor valvulare (mecanice sau biologice)
- Suspiciune de dehiscență protetică sau leak paravalvular
- 'Complicații post-operatorii valvulare: tromboză de proteză, formațiuni de tip pannus,
  endocardită'
contrast:
  agent: Isovue 370
  duration: 15 sec
  flow_rate: 4-5 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 200 HU
  volume: 1.3 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții multifazice dinamice (cine-CT). Planuri specifice
    'en face' pe inelul valvular. Evaluare circumferențială paravalvulară.
  nursing: Linie venoasă minim 20G.
  rad: Evaluați mobilitatea discurilor/cuspelor protezei. Căutați defecte paravalvulare
    sau extravazare perivalvulară. Reducerea artefactelor metalice prin kV crescut
    și secțiuni fine permite vizualizarea trombilor hipodenși sau a pannusului.
  tech: Sincronizare retrospectivă. CREȘTEREA tensiunii kV la 130-140 kV pentru reducerea
    artefactelor metalice. Volum crescut de contrast (1.3 mL/kg). Reconstrucții extinse
    pe toate fazele ciclului cardiac.
  tips: kV ridicat (130-140) critic pentru străpungerea artefactelor metalice de la
    inelul protezei.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu picioarele înainte
premedication: HR < 65 preferred. Metoprolol if needed
protocol_type: cardiac gated
recons:
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Evaluarea morfologiei protezei valvulare
  plane: Axial
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Faze cardiace multiple pentru aprecierea mobilității
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Plan de ax scurt 'en face' pe orificiul valvular
  plane: Short axis
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Plan de ax lung pentru deschiderea cuspelor/discurilor
  plane: Long axis
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Sub cord
  name: Angio-CT Sincronizat ECG
  notes: Sincronizare retrospectivă cu kV RIDICAT (130-140 kV)
  start: Polul superior al cordului
  thickness: 0.625 mm
slug: gated-cta-chest-post-op-cardiac-valve
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 130-140
  mas: Auto (modulare sincronizată ECG)
  pitch: 0.2-0.24
  rotation_time: 0.28s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Torace Sincronizat ECG Post-Protezare Valvulară Cardiacă
---

# Angio-CT Torace Sincronizat ECG Post-Protezare Valvulară Cardiacă

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Sincronizat ECG | Urmărire bolus | Polul superior al cordului → Sub cord |

    === "Indicații Clinice"

        - Evaluarea funcțională a protezelor valvulare (mecanice sau biologice)
        - Suspiciune de dehiscență protetică sau leak paravalvular
        - Complicații post-operatorii valvulare: tromboză de proteză, formațiuni de tip pannus, endocardită

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - HR < 65 preferred. Metoprolol if needed

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.3 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 15 sec |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta ascendentă |
        | Declanșator (HU) | 200 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 130-140 kV |
    | **Curent Tub (mAs)** | Auto (modulare sincronizată ECG) |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28 s |
    | **Pitch (Factor Pas)** | 0.2-0.24 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Sincronizare retrospectivă. CREȘTEREA tensiunii kV la 130-140 kV pentru reducerea artefactelor metalice. Volum crescut de contrast (1.3 mL/kg). Reconstrucții extinse pe toate fazele ciclului cardiac.

    === "Note Asistent"

        - Linie venoasă minim 20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați mobilitatea discurilor/cuspelor protezei. Căutați defecte paravalvulare sau extravazare perivalvulară. Reducerea artefactelor metalice prin kV crescut și secțiuni fine permite vizualizarea trombilor hipodenși sau a pannusului.

    === "Sfaturi & Recomandări"

        - kV ridicat (130-140) critic pentru străpungerea artefactelor metalice de la inelul protezei.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Sincronizat ECG | Polul superior al cordului | Sub cord | Urmărire bolus | 0.625 mm | Sincronizare retrospectivă cu kV RIDICAT (130-140 kV) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Sincronizat ECG | Cord | 0.75 mm/0.75 mm | Cardiac |  | Evaluarea morfologiei protezei valvulare |
    | Axial | Angio-CT Sincronizat ECG | Cord | 1 mm/1 mm | Cardiac |  | Faze cardiace multiple pentru aprecierea mobilității |
    | Short axis | Angio-CT Sincronizat ECG | Cord | 1 mm/1 mm | Cardiac |  | Plan de ax scurt 'en face' pe orificiul valvular |
    | Long axis | Angio-CT Sincronizat ECG | Cord | 1 mm/1 mm | Cardiac |  | Plan de ax lung pentru deschiderea cuspelor/discurilor |
