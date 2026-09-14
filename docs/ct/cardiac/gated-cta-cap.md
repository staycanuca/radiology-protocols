---
author: Departamentul de Radiologie
category: cardiac
clinical_indications:
- Disecție acută de aortă toraco-abdominală (tip Stanford A sau B)
- Anevrism extins de aortă cu interesarea rădăcinii aortice sau a valvelor
- Patologie combinată valvulară/coronariană și aortică
contrast:
  agent: Isovue 370
  duration: 20-24s
  flow_rate: 4 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 180 HU
  volume: 1.6 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MPR curbate pe toată lungimea aortei. Reformatări
    în planul inelului aortic. Randare tridimensională 3D VR.
  nursing: Linie venoasă minim 20G.
  rad: 'Torace sincronizat: evaluați cu precizie rădăcina aortică, valva aortică,
    originea coronarelor și poarta de intrare a disecției. Flash AP: ramurile viscerale
    ale aortei abdominale, malperfuzia renală sau mezenterică.'
  tech: 'DOUĂ componente sincronizate: 1) Torace sincronizat retrospectiv ECG (elimină
    pulsațiile rădăcinii aortice) 2) Achiziție elicoidală rapidă de la diafragm la
    simfiza pubiană.'
  tips: Brațele ridicate. Sincronizarea riguroasă între cele două componente elimină
    artefactele de mișcare ale rădăcinii.
npo: Repaus alimentar 4 ore (sau urgență)
position: Decubit dorsal cu brațele ridicate
premedication: HR < 65 target. Premedication not required.
protocol_type: cardiac gated
recons:
- acquisition: Angio-CT Torace Sincronizat
  fov: Torace
  kernel: Cardiac
  notes: Rădăcină aortică și valvă aortică fără artefacte de pulsație
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Flash AP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Aorta abdominală și arterele viscerale
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Torace Sincronizat
  fov: Torace-Abdomen-Pelvis
  kernel: Vascular
  notes: Reconstrucție MIP completă a aortei
  plane: Coronal
  thickness_increment: 3 mm/3 mm
- acquisition: Angio-CT Torace Sincronizat
  fov: Torace-Abdomen-Pelvis
  kernel: Vascular
  notes: Reconstrucție MPR curbată pe întreaga lungime aortică
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Documentați statutul de urgență vasculară
  renal: Verificați funcția renală dacă situația clinică o permite
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă Flash
  notes: Detecția hematoamelor intramurale native
  start: Apertura toracică superioară
  thickness: 2.5 mm
- delay: Urmărire bolus
  end: Diafragm
  name: Angio-CT Torace Sincronizat
  notes: Sincronizare retrospectivă toracică dedicată aortei ascendente
  start: Apertura toracică superioară
  thickness: 0.625 mm
- delay: Continuare
  end: Simfiză pubiană
  name: Angio-CT Flash AP
  notes: Achiziție elicoidală rapidă pitch mare fără gating
  start: Diafragm
  thickness: 1 mm
- delay: 40 sec
  end: Margine inferioară stent
  name: Tardiv Stent (opțional)
  notes: Acoperire zonă endoproteză pentru evaluarea endoleak-urilor
  start: Margine superioară stent
  thickness: 1 mm
slug: gated-cta-cap
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: '100'
  mas: Auto modulare ECG torace / Curent crescut AP
  pitch: 0.2-0.24 chest / 1.2-1.5 AP
  rotation_time: 0.28 chest / 0.5 APs
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Sincronizat ECG Torace-Abdomen-Pelvis (Aortă & Cord)
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

# Angio-CT Sincronizat ECG Torace-Abdomen-Pelvis (Aortă & Cord)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă Flash | 0 sec | Apertura toracică superioară → Simfiză pubiană |
        | Angio-CT Torace Sincronizat | Urmărire bolus | Apertura toracică superioară → Diafragm |
        | Angio-CT Flash AP | Continuare | Diafragm → Simfiză pubiană |
        | Tardiv Stent (opțional) | 40 sec | Margine superioară stent → Margine inferioară stent |

    === "Indicații Clinice"

        - Disecție acută de aortă toraco-abdominală (tip Stanford A sau B)
        - Anevrism extins de aortă cu interesarea rădăcinii aortice sau a valvelor
        - Patologie combinată valvulară/coronariană și aortică

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore (sau urgență)
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
        | Durată | 20-24s |
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
    | **Timp de Rotație** | 0.28 chest / 0.5 AP s |
    | **Pitch (Factor Pas)** | 0.2-0.24 chest / 1.2-1.5 AP |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ componente sincronizate: 1) Torace sincronizat retrospectiv ECG (elimină pulsațiile rădăcinii aortice) 2) Achiziție elicoidală rapidă de la diafragm la simfiza pubiană.

    === "Note Asistent"

        - Linie venoasă minim 20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați funcția renală dacă situația clinică o permite
            - **Alergii:** Documentați statutul de urgență vasculară

    === "Note Radiolog"

        - Torace sincronizat: evaluați cu precizie rădăcina aortică, valva aortică, originea coronarelor și poarta de intrare a disecției. Flash AP: ramurile viscerale ale aortei abdominale, malperfuzia renală sau mezenterică.

    === "Sfaturi & Recomandări"

        - Brațele ridicate. Sincronizarea riguroasă între cele două componente elimină artefactele de mișcare ale rădăcinii.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă Flash | Apertura toracică superioară | Simfiză pubiană | 0 sec | 2.5 mm | Detecția hematoamelor intramurale native |
    | Angio-CT Torace Sincronizat | Apertura toracică superioară | Diafragm | Urmărire bolus | 0.625 mm | Sincronizare retrospectivă toracică dedicată aortei ascendente |
    | Angio-CT Flash AP | Diafragm | Simfiză pubiană | Continuare | 1 mm | Achiziție elicoidală rapidă pitch mare fără gating |
    | Tardiv Stent (opțional) | Margine superioară stent | Margine inferioară stent | 40 sec | 1 mm | Acoperire zonă endoproteză pentru evaluarea endoleak-urilor |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Torace Sincronizat | Torace | 1.25 mm/1.25 mm | Cardiac |  | Rădăcină aortică și valvă aortică fără artefacte de pulsație |
    | Axial | Angio-CT Flash AP | Abdomen-Pelvis | 2 mm/2 mm | Vascular |  | Aorta abdominală și arterele viscerale |
    | Coronal | Angio-CT Torace Sincronizat | Torace-Abdomen-Pelvis | 3 mm/3 mm | Vascular |  | Reconstrucție MIP completă a aortei |
    | Sagital | Angio-CT Torace Sincronizat | Torace-Abdomen-Pelvis | 2 mm/2 mm | Vascular |  | Reconstrucție MPR curbată pe întreaga lungime aortică |

## Surse și revizuire

- [SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf) — *ACR / SCCT* (US)
- [UT Southwestern Radiology — Cardiovascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
