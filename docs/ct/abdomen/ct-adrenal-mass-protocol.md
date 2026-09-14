---
author: Departamentul de Radiologie
category: abdomen
clinical_indications:
- Caracterizarea formațiunilor suprarenaliene
- Diferențiere adenom vs. metastază
- Bilanț diagnostic incidentalom suprarenalian
contrast:
  agent: Isovue 370
  duration: 40s
  flow_rate: 3 mL/s
  timing: Timp empiric de întârziere (70s)
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: 'Calcul washout absolut: (HU fază încărcată - HU tardiv) / (HU
    fază încărcată - HU nativ) x 100. >60% sugerează adenom suprarenalian.'
  nursing: Abord venos periferic 20-22G. Pacientul trebuie informat că va aștepta
    15 minute pentru seria tardivă.
  rad: 'Nativ: adenom bogat în lipide < 10 HU. Venoasă portală: încărcare cu contrast.
    Fază tardivă 15 min: calculare washout (adenomul prezintă spălare rapidă).'
  tech: 'TREI faze: 1) Fază nativă pentru densitatea absolută în HU 2) Fază venoasă
    portală la 70s 3) Fază tardivă la 15 MINUTE pentru washout. Toate fazele trebuie
    să acopere glandele suprarenale.'
  tips: Timp de așteptare al pacientului 15 min. Măsurați valorile HU cu atenție,
    poziționând ROI identic pe toate cele trei faze.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Nativă
  fov: Abdomen
  kernel: Standard
  notes: Măsurători ROI în masa suprarenaliană
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Evaluarea încărcării vasculare
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Tardivă la 15 Minute
  fov: Abdomen
  kernel: Standard
  notes: Măsurare densitate HU pentru spălare (washout)
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Vedere anatomică de ansamblu
  plane: Coronal
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Verificați istoricul alergic. Explicați faza tardivă la 15 minute.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Sub polul inferior renal
  name: Fază Nativă
  notes: Achiziție nativă de referință pentru densitate în HU
  start: Deasupra glandelor suprarenale
  thickness: 0.625 mm
- delay: 70 sec
  end: Creste iliace
  name: Fază Venoasă Portală
  notes: Fază venoasă portală pentru evaluarea încărcării
  start: Diafragm
  thickness: 0.625 mm
- delay: 900 sec (15 min)
  end: Sub glandele suprarenale
  name: Fază Tardivă la 15 Minute
  notes: Fază tardivă de spălare (washout)
  start: Deasupra glandelor suprarenale
  thickness: 0.625 mm
slug: ct-adrenal-mass-protocol
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: '1'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Protocol Masă Suprarenaliană (Washout)
sources:
- title: AAPM CT Protocols — Adult Abdomen/Pelvis CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: f0c7c2e31da9a9ed24dbdef7bd5b38994d670ba52d21b702faac79b97ace00c3
- title: UT Southwestern Radiology — CT Abdomen & Pelvis Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Protocol Masă Suprarenaliană (Washout)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | Deasupra glandelor suprarenale → Sub polul inferior renal |
        | Fază Venoasă Portală | 70 sec | Diafragm → Creste iliace |
        | Fază Tardivă la 15 Minute | 900 sec (15 min) | Deasupra glandelor suprarenale → Sub glandele suprarenale |

    === "Indicații Clinice"

        - Caracterizarea formațiunilor suprarenaliene
        - Diferențiere adenom vs. metastază
        - Bilanț diagnostic incidentalom suprarenalian

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 3 mL/s |
        | Durată | 40s |
        | Metodă Temporizare | Timp empiric de întârziere (70s) |
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
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - TREI faze: 1) Fază nativă pentru densitatea absolută în HU 2) Fază venoasă portală la 70s 3) Fază tardivă la 15 MINUTE pentru washout. Toate fazele trebuie să acopere glandele suprarenale.

    === "Note Asistent"

        - Abord venos periferic 20-22G. Pacientul trebuie informat că va aștepta 15 minute pentru seria tardivă.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic. Explicați faza tardivă la 15 minute.

    === "Note Radiolog"

        - Nativ: adenom bogat în lipide < 10 HU. Venoasă portală: încărcare cu contrast. Fază tardivă 15 min: calculare washout (adenomul prezintă spălare rapidă).

    === "Sfaturi & Recomandări"

        - Timp de așteptare al pacientului 15 min. Măsurați valorile HU cu atenție, poziționând ROI identic pe toate cele trei faze.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | Deasupra glandelor suprarenale | Sub polul inferior renal | 0 sec | 0.625 mm | Achiziție nativă de referință pentru densitate în HU |
    | Fază Venoasă Portală | Diafragm | Creste iliace | 70 sec | 0.625 mm | Fază venoasă portală pentru evaluarea încărcării |
    | Fază Tardivă la 15 Minute | Deasupra glandelor suprarenale | Sub glandele suprarenale | 900 sec (15 min) | 0.625 mm | Fază tardivă de spălare (washout) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă | Abdomen | 2.5 mm/2.5 mm | Standard |  | Măsurători ROI în masa suprarenaliană |
    | Axial | Fază Venoasă Portală | Abdomen | 2.5 mm/2.5 mm | Standard |  | Evaluarea încărcării vasculare |
    | Axial | Fază Tardivă la 15 Minute | Abdomen | 2.5 mm/2.5 mm | Standard |  | Măsurare densitate HU pentru spălare (washout) |
    | Coronal | Fază Venoasă Portală | Abdomen | 3 mm/3 mm | Standard |  | Vedere anatomică de ansamblu |

## Surse și revizuire

- [AAPM CT Protocols — Adult Abdomen/Pelvis CT](https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Abdomen & Pelvis Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
