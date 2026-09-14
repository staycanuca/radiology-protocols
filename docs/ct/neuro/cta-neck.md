---
author: Departamentul de Radiologie
category: neuro
clinical_indications:
- Stenoză carotidiană aterosclerotică
- Disecție de arteră carotidă internă sau arteră vertebrală
- Bilanț pre-endarterectomie carotidiană (CEA) sau stentare (CAS)
- Suflu carotidian asimptomatic
contrast:
  agent: Omnipaque 350
  flow_rate: 4-5 mL/s
  roi: Crosa aortei
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 90-100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MPR curbate pentru ambele bifurcații carotidiene.
    Măsurarea precisă a stenozei NASCET. Randare 3D VR și proiecții MIP.
  nursing: Linie venoasă minim 20G în plica cotului.
  rad: Bifurcațiile carotidiene. Gradarea stenozei carotidiene conform criteriilor
    NASCET. Morfologia plăcii aterosclerotice (placă vulnerabilă, ulcerată, hipodensă/lipidică
    vs. calcificată). Arterele vertebrale pe cele 4 segmente (V1-V4). Căutați semne
    de disecție (fals lumen, hematom intramural).
  tech: De la crosa aortei până la baza craniului. Urmărire bolus în crosa aortei.
    Achiziție submilimetrică. Fără deglutiție pe parcursul scanării.
  tips: Pacientul nu trebuie să înghită în timpul scanării.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu capul înainte
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Gât
  fov: Gât
  kernel: Vascular
  notes: Imagini sursă de înaltă rezoluție
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Gât
  fov: Gât
  kernel: Vascular
  notes: Vedere coronală de ansamblu
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Gât
  fov: Gât
  kernel: Vascular
  notes: Traiectul arterelor vertebrale
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Gât
  fov: Carotidă
  kernel: Vascular
  notes: Reconstrucții curbate pentru măsurători de stenoză NASCET
  plane: Curved MPR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Baza craniului
  name: Angio-CT Gât
  notes: Achiziție caudo-cranială
  start: Arc aortic
  thickness: 0.625 mm
slug: cta-neck
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 200 mAs)
  pitch: '0.9'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Artere Cervicale / Carotide și Vertebrale
sources:
- title: AAPM CT Protocols — Adult Routine Head CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 503972f1004a69ab87fba33be79f28ad3647b389370870386d9af7967ea1691b
- title: UT Southwestern Radiology — CT Neuro / Head Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# Angio-CT Artere Cervicale / Carotide și Vertebrale

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Gât | Urmărire bolus | Arc aortic → Baza craniului |

    === "Indicații Clinice"

        - Stenoză carotidiană aterosclerotică
        - Disecție de arteră carotidă internă sau arteră vertebrală
        - Bilanț pre-endarterectomie carotidiană (CEA) sau stentare (CAS)
        - Suflu carotidian asimptomatic

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volum | 90-100 mL |
        | Rată de Flux | 4-5 mL/s |
        | Durată |  |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Crosa aortei |
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
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la crosa aortei până la baza craniului. Urmărire bolus în crosa aortei. Achiziție submilimetrică. Fără deglutiție pe parcursul scanării.

    === "Note Asistent"

        - Linie venoasă minim 20G în plica cotului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Bifurcațiile carotidiene. Gradarea stenozei carotidiene conform criteriilor NASCET. Morfologia plăcii aterosclerotice (placă vulnerabilă, ulcerată, hipodensă/lipidică vs. calcificată). Arterele vertebrale pe cele 4 segmente (V1-V4). Căutați semne de disecție (fals lumen, hematom intramural).

    === "Sfaturi & Recomandări"

        - Pacientul nu trebuie să înghită în timpul scanării.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Gât | Arc aortic | Baza craniului | Urmărire bolus | 0.625 mm | Achiziție caudo-cranială |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Gât | Gât | 1 mm/1 mm | Vascular |  | Imagini sursă de înaltă rezoluție |
    | Coronal | Angio-CT Gât | Gât | 1.5 mm/1.5 mm | Vascular |  | Vedere coronală de ansamblu |
    | Sagital | Angio-CT Gât | Gât | 1.5 mm/1.5 mm | Vascular |  | Traiectul arterelor vertebrale |
    | Curved MPR | Angio-CT Gât | Carotidă | 1 mm/1 mm | Vascular |  | Reconstrucții curbate pentru măsurători de stenoză NASCET |

## Surse și revizuire

- [AAPM CT Protocols — Adult Routine Head CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Neuro / Head Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
