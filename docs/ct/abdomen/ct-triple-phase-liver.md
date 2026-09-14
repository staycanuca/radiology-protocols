---
author: Departamentul de Radiologie
category: abdomen
clinical_indications:
- Caracterizarea leziunilor focale hepatice
- Supraveghere și diagnostic carcinom hepatocelular (HCC)
- Stadializarea tumorilor hepatice primare sau secundare (metastaze hipervasculare)
contrast:
  agent: Isovue 370
  duration: 25s
  flow_rate: 4-5 mL/s
  roi: Aorta abdominală
  timing: 'Protocol trifazic: Nativ + Arterial Tardiv + Venoasă Portală + Tardivă'
  trigger: 150 HU
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții coronale și sagitale. Reconstrucții MIP pentru
    anatomia vasculară a trunchiului celiac și arterei hepatice.
  nursing: Abord venos 18-20G. Debitul ridicat de injectare (4-5 mL/s) este esențial.
  rad: 'Nativ: calcificări, hemoragii, grăsime. Arterial tardiv: hipervascularizație
    (apoptoză arterială precoce specifică HCC). Portal: leziuni hipovasculare și raport
    vascular. Tardiv: fenomen de spălare (washout) și capsulă peritumorală.'
  tech: 'PATRU achiziții: 1) Fază nativă ficat 2) Fază arterială tardivă (bolus tracking
    sau 30-35s) 3) Fază venoasă portală la 70s 4) Fază tardivă la 3-5 min. FOV: Ficat
    pentru Nativ/Arterial/Tardiv; Abdomen complet pentru Venoasă Portală. Durata injectării
    este fixă de 25 secunde.'
  tips: Debit mare de injectare. Așteptare completă pentru faza tardivă. Antrenați
    pacientul pentru apnee respiratorie reproductibilă.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: Fără contrast oral pozitiv. Apă oral opțională.
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Arterială Tardivă
  fov: Ficat
  kernel: Standard
  notes: Comparație multifazică a leziunilor
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Examinare abdomen complet în fază portală
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Comparație în plan coronal
  plane: Coronal
  thickness_increment: 3 mm/3 mm
- acquisition: Fază Arterială Tardivă
  fov: Ficat
  kernel: Standard
  notes: Substracție pentru creșterea conspicuității leziunilor
  plane: Subtraction
  thickness_increment: 2.5 mm/2.5 mm
safety:
  allergy: Verificați istoricul de reacții alergice la contrast.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Polul inferior hepatic
  name: Fază Nativă
  notes: Evaluare densitate bazală hepatică
  start: Cupola hepatică
  thickness: 0.625 mm
- delay: 30-35 sec
  end: Polul inferior hepatic
  name: Fază Arterială Tardivă
  notes: Evidențierea leziunilor hepatice hipervasculare
  start: Cupola hepatică
  thickness: 0.625 mm
- delay: 70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală
  notes: Evaluare completă parenchim hepatic și abdomen
  start: Diafragm
  thickness: 0.625 mm
- delay: 180-300 sec (3-5 min)
  end: Polul inferior hepatic
  name: Fază Tardivă
  notes: Aprecierea fenomenului de spălare (washout)
  start: Cupola hepatică
  thickness: 0.625 mm
slug: ct-triple-phase-liver
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200-250 mAs)
  pitch: 0.9-1.0
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Ficat Trifazic (Protocol Carcinom Hepatocelular / Masă Hepatică)
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

# CT Ficat Trifazic (Protocol Carcinom Hepatocelular / Masă Hepatică)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | Cupola hepatică → Polul inferior hepatic |
        | Fază Arterială Tardivă | 30-35 sec | Cupola hepatică → Polul inferior hepatic |
        | Fază Venoasă Portală | 70 sec | Diafragm → Simfiză pubiană |
        | Fază Tardivă | 180-300 sec (3-5 min) | Cupola hepatică → Polul inferior hepatic |

    === "Indicații Clinice"

        - Caracterizarea leziunilor focale hepatice
        - Supraveghere și diagnostic carcinom hepatocelular (HCC)
        - Stadializarea tumorilor hepatice primare sau secundare (metastaze hipervasculare)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral pozitiv. Apă oral opțională.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 25s |
        | Metodă Temporizare | Protocol trifazic: Nativ + Arterial Tardiv + Venoasă Portală + Tardivă |
        | Poziționare ROI | Aorta abdominală |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto (referință 200-250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9-1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - PATRU achiziții: 1) Fază nativă ficat 2) Fază arterială tardivă (bolus tracking sau 30-35s) 3) Fază venoasă portală la 70s 4) Fază tardivă la 3-5 min. FOV: Ficat pentru Nativ/Arterial/Tardiv; Abdomen complet pentru Venoasă Portală. Durata injectării este fixă de 25 secunde.

    === "Note Asistent"

        - Abord venos 18-20G. Debitul ridicat de injectare (4-5 mL/s) este esențial.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul de reacții alergice la contrast.

    === "Note Radiolog"

        - Nativ: calcificări, hemoragii, grăsime. Arterial tardiv: hipervascularizație (apoptoză arterială precoce specifică HCC). Portal: leziuni hipovasculare și raport vascular. Tardiv: fenomen de spălare (washout) și capsulă peritumorală.

    === "Sfaturi & Recomandări"

        - Debit mare de injectare. Așteptare completă pentru faza tardivă. Antrenați pacientul pentru apnee respiratorie reproductibilă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | Cupola hepatică | Polul inferior hepatic | 0 sec | 0.625 mm | Evaluare densitate bazală hepatică |
    | Fază Arterială Tardivă | Cupola hepatică | Polul inferior hepatic | 30-35 sec | 0.625 mm | Evidențierea leziunilor hepatice hipervasculare |
    | Fază Venoasă Portală | Diafragm | Simfiză pubiană | 70 sec | 0.625 mm | Evaluare completă parenchim hepatic și abdomen |
    | Fază Tardivă | Cupola hepatică | Polul inferior hepatic | 180-300 sec (3-5 min) | 0.625 mm | Aprecierea fenomenului de spălare (washout) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Arterială Tardivă | Ficat | 2.5 mm/2.5 mm | Standard |  | Comparație multifazică a leziunilor |
    | Axial | Fază Venoasă Portală | Abdomen | 2.5 mm/2.5 mm | Standard |  | Examinare abdomen complet în fază portală |
    | Coronal | Fază Venoasă Portală | Abdomen | 3 mm/3 mm | Standard |  | Comparație în plan coronal |
    | Subtraction | Fază Arterială Tardivă | Ficat | 2.5 mm/2.5 mm | Standard |  | Substracție pentru creșterea conspicuității leziunilor |

## Surse și revizuire

- [AAPM CT Protocols — Adult Abdomen/Pelvis CT](https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Abdomen & Pelvis Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
