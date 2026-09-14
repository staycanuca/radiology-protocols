---
author: None
category: cardiac
clinical_indications:
- Planificare pre-procedurală TAVR (implantare transcateter a valvei aortice)
- Stenoză aortică severă simptomatică la pacienți cu indicație de TAVR
contrast:
  agent: Isovue 370
  duration: 22s
  flow_rate: 4 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 180 HU
  volume: 1.6 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții dedicate pe inelul aortic (plan dublu oblic 'en
    face'). Măsurători ale vaselor de abord iliofemurale. Raport complet TAVR.
  nursing: Linie venoasă 20G în plica cotului.
  rad: 'Măsurători TAVR complete: aria și perimetrul inelului aortic, diametre minim/maxim,
    distanța de la inel la ostiile coronariene stâng și drept, diametrul sinusurilor
    Valsalva și al joncțiunii sinotubulare, scorul de calciu al cuspelor, calibrul
    și tortuozitatea arterelor ilio-femurale.'
  tech: 'Protocol COMBINAT: Angio-CT Torace sincronizat retrospectiv ECG + Angio-CT
    Flash rapid elicoidal Abdomen/Pelvis. Sincronizarea toracică servește măsurătorilor
    valvei, iar achiziția abdomino-pelvină planifică accesul ilio-femural.'
  tips: Protocol dedicat măsurătorilor TAVR. Secțiuni fine la nivelul rădăcinii aortice
    obligatorii.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: HR < 65 target. Premedication not required.
protocol_type: cardiac gated
recons:
- acquisition: Fază Nativă CAP
  fov: Torace-Abdomen-Pelvis
  kernel: Standard
  notes: Serie nativă de ansamblu
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angio-CT Torace Sincronizat
  fov: Cord
  kernel: Cardiac
  notes: Măsurători valvulare și rădăcină aortică
  plane: Axial
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Angio-CT Flash AP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Evaluarea calibrului vaselor de acces iliofemurale
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Torace Sincronizat
  fov: Cord
  kernel: Cardiac
  notes: Plan dublu oblic 'en face' pe inelul aortic pentru dimensionare
  plane: Double oblique
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Angio-CT Flash AP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Randare 3D a traiectului vascular de abord
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m² (frecvent pacienți vârstnici)
series:
- delay: 0 sec
  end: Capete femurale
  name: Fază Nativă CAP
  notes: Detecția calcificărilor parietale și a inelului
  start: Apertura toracică superioară
  thickness: 2.5 mm
- delay: Urmărire bolus
  end: Diafragm
  name: Angio-CT Torace Sincronizat
  notes: Sincronizare retrospectivă pentru măsurătorile inelului și rădăcinii
  start: Apertura toracică superioară
  thickness: 0.625 mm
- delay: Continuare
  end: Capete femurale
  name: Angio-CT Flash AP
  notes: Planificarea accesului vascular ilio-femural
  start: Diafragm
  thickness: 1 mm
slug: gated-cta-tavr
synonyms:
- TAVR, Transcatheter aortic valve replacement
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: '100'
  mas: Auto modulare ECG torace / Curent crescut AP
  pitch: 0.2-0.24 / 1.2-1.5
  rotation_time: 0.28 / 0.5s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Sincronizat ECG Planificare TAVR (Implantare Valvulară Aortică Transcateter)
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

# Angio-CT Sincronizat ECG Planificare TAVR (Implantare Valvulară Aortică Transcateter)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă CAP | 0 sec | Apertura toracică superioară → Capete femurale |
        | Angio-CT Torace Sincronizat | Urmărire bolus | Apertura toracică superioară → Diafragm |
        | Angio-CT Flash AP | Continuare | Diafragm → Capete femurale |

    === "Indicații Clinice"

        - Planificare pre-procedurală TAVR (implantare transcateter a valvei aortice)
        - Stenoză aortică severă simptomatică la pacienți cu indicație de TAVR

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - HR < 65 target. Premedication not required.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.6 mL/kg |
        | Rată de Flux | 4 mL/s |
        | Durată | 22s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta ascendentă |
        | Declanșator (HU) | 180 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto modulare ECG torace / Curent crescut AP |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28 / 0.5 s |
    | **Pitch (Factor Pas)** | 0.2-0.24 / 1.2-1.5 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol COMBINAT: Angio-CT Torace sincronizat retrospectiv ECG + Angio-CT Flash rapid elicoidal Abdomen/Pelvis. Sincronizarea toracică servește măsurătorilor valvei, iar achiziția abdomino-pelvină planifică accesul ilio-femural.

    === "Note Asistent"

        - Linie venoasă 20G în plica cotului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m² (frecvent pacienți vârstnici)
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Măsurători TAVR complete: aria și perimetrul inelului aortic, diametre minim/maxim, distanța de la inel la ostiile coronariene stâng și drept, diametrul sinusurilor Valsalva și al joncțiunii sinotubulare, scorul de calciu al cuspelor, calibrul și tortuozitatea arterelor ilio-femurale.

    === "Sfaturi & Recomandări"

        - Protocol dedicat măsurătorilor TAVR. Secțiuni fine la nivelul rădăcinii aortice obligatorii.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă CAP | Apertura toracică superioară | Capete femurale | 0 sec | 2.5 mm | Detecția calcificărilor parietale și a inelului |
    | Angio-CT Torace Sincronizat | Apertura toracică superioară | Diafragm | Urmărire bolus | 0.625 mm | Sincronizare retrospectivă pentru măsurătorile inelului și rădăcinii |
    | Angio-CT Flash AP | Diafragm | Capete femurale | Continuare | 1 mm | Planificarea accesului vascular ilio-femural |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă CAP | Torace-Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Serie nativă de ansamblu |
    | Axial | Angio-CT Torace Sincronizat | Cord | 0.75 mm/0.75 mm | Cardiac |  | Măsurători valvulare și rădăcină aortică |
    | Axial | Angio-CT Flash AP | Abdomen-Pelvis | 1.5 mm/1.5 mm | Vascular |  | Evaluarea calibrului vaselor de acces iliofemurale |
    | Double oblique | Angio-CT Torace Sincronizat | Cord | 0.75 mm/0.75 mm | Cardiac |  | Plan dublu oblic 'en face' pe inelul aortic pentru dimensionare |
    | 3D VR | Angio-CT Flash AP | Abdomen-Pelvis | 1 mm/1 mm | Vascular |  | Randare 3D a traiectului vascular de abord |

## Surse și revizuire

- [SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf) — *ACR / SCCT* (US)
- [UT Southwestern Radiology — Cardiovascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
