---
author: null
category: cardiac
clinical_indications:
- Disecție acută de aortă toracică
- Durere toracică anterioară severă cu iradiere posterioară
- Urmărirea anevrismelor de aortă toracică sau a dilatațiilor rădăcinii aortice
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4-5 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 200 HU
  volume: 1.1 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MPR curbate pentru aorta toracică. Evaluare plan
    valvular aortic.
  nursing: Linie venoasă minim 20G. Controlul frecvenței cardiace optimizează calitatea.
    Administrare nitroglicerină dacă tensiunea permite.
  rad: Evaluați lumenul aortic, poarta de intrare, flapul intimal, lumenul adevărat
    vs. fals, originea coronarelor din rădăcina aortică și extensia distală.
  tech: 'Sincronizare retrospectivă ECG pe întreg toracele. Urmărire bolus în aorta
    ascendentă. Opțional: protocol de stent/endoproteză cu serie tardivă la 40 secunde.'
  tips: Controlul ritmului este important. Monitorizați stabilitatea semnalului ECG.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu picioarele înainte
premedication: HR < 60 target. Premedication not required.
protocol_type: cardiac gated
recons:
- acquisition: Angio-CT Sincronizat ECG
  fov: Torace
  kernel: Cardiac
  notes: Evaluare primară a rădăcinii și aortei ascendente
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Torace
  kernel: Cardiac
  notes: Reconstrucții curbate de-a lungul aortei toracice
  plane: Curved MPR
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Fază Nativă
  fov: Torace
  kernel: Standard
  notes: Evaluare calciu și modificări parietale
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Planuri specifice valvulare și cardiace
  plane: Short/long axis
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Diafragm
  name: Fază Nativă
  notes: Detecția calcificărilor și hematoamelor murale
  start: Vârfuri pulmonare
  thickness: 2.5 mm
- delay: Urmărire bolus
  end: Diafragm
  name: Angio-CT Sincronizat ECG
  notes: Sincronizare retrospectivă ECG pe aorta toracică
  start: Vârfuri pulmonare
  thickness: 0.625 mm
- delay: 40 sec
  end: Margine inferioară stent
  name: Tardiv Stent (opțional)
  notes: Opțional pentru decelarea endoleak-urilor tardive
  start: Margine superioară stent
  thickness: 1 mm
slug: gated-cta-chest
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: '100'
  mas: Auto (modulare sincronizată ECG)
  pitch: 0.2-0.24
  rotation_time: 0.28s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Torace Sincronizat ECG (Aortă Toracică)
---

# Angio-CT Torace Sincronizat ECG (Aortă Toracică)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | Vârfuri pulmonare → Diafragm |
        | Angio-CT Sincronizat ECG | Urmărire bolus | Vârfuri pulmonare → Diafragm |
        | Tardiv Stent (opțional) | 40 sec | Margine superioară stent → Margine inferioară stent |

    === "Indicații Clinice"

        - Disecție acută de aortă toracică
        - Durere toracică anterioară severă cu iradiere posterioară
        - Urmărirea anevrismelor de aortă toracică sau a dilatațiilor rădăcinii aortice

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - HR < 60 target. Premedication not required.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.1 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 20s |
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
    | **Tensiune Tub (kV)** | 100 kV |
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

        - Sincronizare retrospectivă ECG pe întreg toracele. Urmărire bolus în aorta ascendentă. Opțional: protocol de stent/endoproteză cu serie tardivă la 40 secunde.

    === "Note Asistent"

        - Linie venoasă minim 20G. Controlul frecvenței cardiace optimizează calitatea. Administrare nitroglicerină dacă tensiunea permite.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați lumenul aortic, poarta de intrare, flapul intimal, lumenul adevărat vs. fals, originea coronarelor din rădăcina aortică și extensia distală.

    === "Sfaturi & Recomandări"

        - Controlul ritmului este important. Monitorizați stabilitatea semnalului ECG.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | Vârfuri pulmonare | Diafragm | 0 sec | 2.5 mm | Detecția calcificărilor și hematoamelor murale |
    | Angio-CT Sincronizat ECG | Vârfuri pulmonare | Diafragm | Urmărire bolus | 0.625 mm | Sincronizare retrospectivă ECG pe aorta toracică |
    | Tardiv Stent (opțional) | Margine superioară stent | Margine inferioară stent | 40 sec | 1 mm | Opțional pentru decelarea endoleak-urilor tardive |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Sincronizat ECG | Torace | 1.25 mm/1.25 mm | Cardiac |  | Evaluare primară a rădăcinii și aortei ascendente |
    | Curved MPR | Angio-CT Sincronizat ECG | Torace | 1.5 mm/1.5 mm | Cardiac |  | Reconstrucții curbate de-a lungul aortei toracice |
    | Axial | Fază Nativă | Torace | 2.5 mm/2.5 mm | Standard |  | Evaluare calciu și modificări parietale |
    | Short/long axis | Angio-CT Sincronizat ECG | Cord | 1.5 mm/1.5 mm | Cardiac |  | Planuri specifice valvulare și cardiace |
