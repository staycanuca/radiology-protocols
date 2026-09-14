---
author: Departamentul de Radiologie
category: cardiac
clinical_indications:
- Suspiciune de endocardită infecțioasă pe valvă nativă sau proteză
- Formațiune tumorală cardiacă (mixom, fibrom, sarcom, metastaze)
- Vegetații valvulare sau abces perivalvular/miocardic
- Tromb intracardiac (urechiușă atrială stângă, apex VS)
contrast:
  agent: Isovue 370
  duration: 35 sec
  flow_rate: 3-4 mL/s
  timing: Timp empiric sincronizat (30s delay)
  volume: 1.6 mL/kg
last_updated: '2026-02-02'
notes:
  additional_recons: Reconstrucții multifazice dinamice (cine-CT). Planuri 4-camere,
    2-camere și axe scurte. Vederi specifice în planul valvelor.
  nursing: Linie venoasă 18-20G. Controlul frecvenței cardiace este util, dar nu critic
    dacă ritmul este stabil.
  rad: Evaluați toate aparatele valvulare pentru vegetații mobile. Analizați miocardul
    pentru abcese, pseudoanevrisme sau fistule. Evaluați prizele de contrast ale maselor
    tumorale.
  tech: Instrucțiuni respiratorii fără Valsalva. Durată fixă de injectare 35 secunde
    cu întârziere de 30 secunde. Sincronizare retrospectivă între 30-70% din intervalul
    R-R. Reconstrucții la intervale de 5% pentru evaluarea mișcării cuspelor.
  tips: Faze cardiace multiple pentru evaluarea mobilității vegetațiilor și deschiderii
    valvulare. Secțiuni fine obligatorii.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu picioarele înainte
premedication: Controlul ritmului dacă este indicat
protocol_type: cardiac gated
recons:
- acquisition: Fază Nativă Cord
  fov: Cord
  kernel: Standard
  notes: Material dens sau calcificări valvulare
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Reconstruit la cea mai bună fază cardiacă diastolică
  plane: Axial
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Standard
  notes: Serie funcțională pentru dinamica valvulară
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Fază Tardivă
  fov: Torace
  kernel: Standard
  notes: Analiza maselor și prizelor tardive de contrast
  plane: Axial
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Sub cord
  name: Fază Nativă Cord
  notes: Achiziție nativă rapidă Flash
  start: Marginea superioară a cordului
  thickness: 2.5 mm
- delay: 30 sec
  end: Sub cord
  name: Angio-CT Sincronizat ECG
  notes: Sincronizare ECG retrospectivă multifazică
  start: Marginea superioară a cordului
  thickness: 0.625 mm
- delay: 90 sec
  end: Diafragm
  name: Fază Tardivă
  notes: Detecția abceselor, vegetațiilor și încărcării tardive a maselor
  start: Vârfuri pulmonare
  thickness: 1.25 mm
slug: endocarditiscardiac-mass
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 100-120
  mas: Auto (modulare sincronizată ECG)
  pitch: 0.2-0.24
  rotation_time: 0.28s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: CT Sincronizat ECG pentru Endocardită / Masă Intracardiacă
sources:
- title: SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf
  institution: ACR / SCCT
  source_region: US
  kind: Standard de practică cardiovasculară
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 16bdb917dce22c0f1620d70ff041aa5d8e0fb7f9d2139d1b15479b41a9f34a32
- title: UT Southwestern Radiology — Cardiovascular CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Sincronizat ECG pentru Endocardită / Masă Intracardiacă

**Ultima actualizare:** 2026-02-02
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă Cord | 0 sec | Marginea superioară a cordului → Sub cord |
        | Angio-CT Sincronizat ECG | 30 sec | Marginea superioară a cordului → Sub cord |
        | Fază Tardivă | 90 sec | Vârfuri pulmonare → Diafragm |

    === "Indicații Clinice"

        - Suspiciune de endocardită infecțioasă pe valvă nativă sau proteză
        - Formațiune tumorală cardiacă (mixom, fibrom, sarcom, metastaze)
        - Vegetații valvulare sau abces perivalvular/miocardic
        - Tromb intracardiac (urechiușă atrială stângă, apex VS)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Controlul ritmului dacă este indicat

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.6 mL/kg |
        | Rată de Flux | 3-4 mL/s |
        | Durată | 35 sec |
        | Metodă Temporizare | Timp empiric sincronizat (30s delay) |
        | Poziționare ROI |  |
        | Declanșator (HU) |  |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
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

        - Instrucțiuni respiratorii fără Valsalva. Durată fixă de injectare 35 secunde cu întârziere de 30 secunde. Sincronizare retrospectivă între 30-70% din intervalul R-R. Reconstrucții la intervale de 5% pentru evaluarea mișcării cuspelor.

    === "Note Asistent"

        - Linie venoasă 18-20G. Controlul frecvenței cardiace este util, dar nu critic dacă ritmul este stabil.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați toate aparatele valvulare pentru vegetații mobile. Analizați miocardul pentru abcese, pseudoanevrisme sau fistule. Evaluați prizele de contrast ale maselor tumorale.

    === "Sfaturi & Recomandări"

        - Faze cardiace multiple pentru evaluarea mobilității vegetațiilor și deschiderii valvulare. Secțiuni fine obligatorii.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă Cord | Marginea superioară a cordului | Sub cord | 0 sec | 2.5 mm | Achiziție nativă rapidă Flash |
    | Angio-CT Sincronizat ECG | Marginea superioară a cordului | Sub cord | 30 sec | 0.625 mm | Sincronizare ECG retrospectivă multifazică |
    | Fază Tardivă | Vârfuri pulmonare | Diafragm | 90 sec | 1.25 mm | Detecția abceselor, vegetațiilor și încărcării tardive a maselor |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă Cord | Cord | 2.5 mm/2.5 mm | Standard |  | Material dens sau calcificări valvulare |
    | Axial | Angio-CT Sincronizat ECG | Cord | 0.75 mm/0.75 mm | Cardiac |  | Reconstruit la cea mai bună fază cardiacă diastolică |
    | Axial | Angio-CT Sincronizat ECG | Cord | 1.5 mm/1.5 mm | Standard |  | Serie funcțională pentru dinamica valvulară |
    | Axial | Fază Tardivă | Torace | 2 mm/2 mm | Standard |  | Analiza maselor și prizelor tardive de contrast |

## Surse și revizuire

- [SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf) — *ACR / SCCT* (US)
- [UT Southwestern Radiology — Cardiovascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
