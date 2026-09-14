---
author: null
category: cardiac
clinical_indications:
- Evaluarea permeabilității grefoanelor de bypass aorto-coronarian (arteriale și venoase)
- Recurența durerilor toracice anginoase sau a echivalentelor post-bypass
- Planificare chirurgicală iterativă sau intervențională
contrast:
  agent: Isovue 370
  duration: 18s
  flow_rate: 4-5 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 200 HU
  volume: 1.1 mL/kg
last_updated: '2026-02-02'
notes:
  additional_recons: Reconstrucții MPR curbate dedicate pentru fiecare grefon. Etichetare
    explicită a grefonului (LIMA, RIMA, SVG-DA, SVG-OM, SVG-CD).
  nursing: Linie venoasă minim 20G (recomandat 18G). Verificați contraindicațiile
    pentru metoprolol sau nitroglicerină. Nitroglicerina are prioritate dacă tensiunea
    arterială este la limită.
  rad: 'Evaluați toate grefoanele: LIMA, RIMA, SVG (grefoane venoase safene). Analizați
    amănunțit anastomozele proximale și distale. Evaluați severitatea bolii vaselor
    native.'
  tech: Tehnică respiratorie non-Valsalva, instruire cardiacă riguroasă. Dacă există
    variabilitate a ritmului cardiac, pulsare milisecundă (200-450 ms). Țintă telediastolă
    dacă FC < 65 bpm; telesistolă dacă FC > 86 bpm; telediastolă spre telesistolă
    la FC 66-75 bpm.
  tips: Acoperire toracică extinsă obligatorie de la nivel supraclavicular până la
    diafragm pentru originea LIMA/RIMA. Pitch redus pentru sincronizare retrospectivă.
npo: Repaus alimentar 4 ore; fără cafeină/fumat
position: Decubit dorsal cu picioarele înainte
premedication: Beta-blocant (metoprolol) per os/IV conform protocolului cardiac; nitroglicerină
  sublingual cu 2-3 min înainte de scanare dacă nu există contraindicații
protocol_type: vascular
recons:
- acquisition: Scor de Calciu
  fov: Cord
  kernel: Standard
  notes: Calcul scor Agatston
  plane: Axial
  thickness_increment: 3 mm/3 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Torace
  kernel: Cardiac
  notes: Secțiuni fine pentru grefoane și vase native
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Torace
  kernel: Standard
  notes: Evaluare extracardiacă și mediastinală
  plane: Sagital
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Reconstrucții MPR 3D și VR ale grefoanelor
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul de alergie la contrast iodat
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Diafragm
  name: Scor de Calciu
  notes: Scor de calciu pe câmp extins
  start: Vârfuri pulmonare
  thickness: 3 mm
- delay: Urmărire bolus
  end: Diafragm
  name: Angio-CT Sincronizat ECG
  notes: Sincronizare retrospectivă ECG - câmp toracic complet
  start: Vârfuri pulmonare
  thickness: 0.625 mm
slug: coronary-cta-post-cabg
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
title: Angio-CT Coronarian Post-By-pass Aorto-Coronarian (Post-CABG)
---

# Angio-CT Coronarian Post-By-pass Aorto-Coronarian (Post-CABG)

**Ultima actualizare:** 2026-02-02
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Scor de Calciu | 0 sec | Vârfuri pulmonare → Diafragm |
        | Angio-CT Sincronizat ECG | Urmărire bolus | Vârfuri pulmonare → Diafragm |

    === "Indicații Clinice"

        - Evaluarea permeabilității grefoanelor de bypass aorto-coronarian (arteriale și venoase)
        - Recurența durerilor toracice anginoase sau a echivalentelor post-bypass
        - Planificare chirurgicală iterativă sau intervențională

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore; fără cafeină/fumat
    - **Premedicație / Pregătire:**
        - Beta-blocant (metoprolol) per os/IV conform protocolului cardiac; nitroglicerină sublingual cu 2-3 min înainte de scanare dacă nu există contraindicații

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.1 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 18s |
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

        - Tehnică respiratorie non-Valsalva, instruire cardiacă riguroasă. Dacă există variabilitate a ritmului cardiac, pulsare milisecundă (200-450 ms). Țintă telediastolă dacă FC < 65 bpm; telesistolă dacă FC > 86 bpm; telediastolă spre telesistolă la FC 66-75 bpm.

    === "Note Asistent"

        - Linie venoasă minim 20G (recomandat 18G). Verificați contraindicațiile pentru metoprolol sau nitroglicerină. Nitroglicerina are prioritate dacă tensiunea arterială este la limită.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul de alergie la contrast iodat

    === "Note Radiolog"

        - Evaluați toate grefoanele: LIMA, RIMA, SVG (grefoane venoase safene). Analizați amănunțit anastomozele proximale și distale. Evaluați severitatea bolii vaselor native.

    === "Sfaturi & Recomandări"

        - Acoperire toracică extinsă obligatorie de la nivel supraclavicular până la diafragm pentru originea LIMA/RIMA. Pitch redus pentru sincronizare retrospectivă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scor de Calciu | Vârfuri pulmonare | Diafragm | 0 sec | 3 mm | Scor de calciu pe câmp extins |
    | Angio-CT Sincronizat ECG | Vârfuri pulmonare | Diafragm | Urmărire bolus | 0.625 mm | Sincronizare retrospectivă ECG - câmp toracic complet |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Scor de Calciu | Cord | 3 mm/3 mm | Standard |  | Calcul scor Agatston |
    | Axial | Angio-CT Sincronizat ECG | Torace | 0.625 mm/0.625 mm | Cardiac |  | Secțiuni fine pentru grefoane și vase native |
    | Sagital | Angio-CT Sincronizat ECG | Torace | 2 mm/2 mm | Standard |  | Evaluare extracardiacă și mediastinală |
    | 3D VR | Angio-CT Sincronizat ECG | Cord | 1 mm/1 mm | Cardiac |  | Reconstrucții MPR 3D și VR ale grefoanelor |
