---
author: null
category: trauma
clinical_indications:
- Suspiciune de anevrism de aortă abdominală (AAA) rupt sau fisurat
- Urgență vasculară aortică
- Instabilitate hemodinamică cu durere abdominală acută și masă pulsatilă
contrast:
  agent: Omnipaque 350
  flow_rate: 4-5 mL/s
  roi: Aorta abdominală
  timing: 'Protocol trifazic rapid: Nativ + Arterial + Venoasă Portală'
  trigger: 150 HU
  volume: 125 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Măsurători detaliate de anevrism (diametru maxim, lungime col,
    unghiuri). Identificați sediul sângerării active. Măsurători pentru endoprotezare
    aortică (EVAR).
  nursing: Linie venoasă de calibru mare 18G minimum (ideal 2 linii). Produse sanguine
    pregătite la dispoziție.
  rad: 'Nativ: hematom retroperitoneal hiperdens, sânge liber intraperitoneal. Arterial:
    extravazare activă de contrast (jet/blush), diametre anevrism, anatomia coletului
    pentru EVAR. Portal: evaluarea ischemiei viscerale/organelor parenchimatoase.'
  tech: 'Protocol RAPID trifazic STAT: 1) Nativ toraco-abdomino-pelvin (hematom proaspăt
    retroperitoneal) 2) Arterial CAP (extravazare activă de contrast, urmărire bolus
    25-30s) 3) Fază venoasă portală CAP la 70s. Alertare imediată a chirurgiei vasculare.'
  tips: Protocol de urgență maximă (STAT). Minimizați orice întârziere. Notificați
    imediat echipa de chirurgie vasculară / radiologie intervențională.
npo: Fără repaus alimentar - urgență vitală
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: trauma
recons:
- acquisition: Fază Arterială CAP
  fov: Abdomen-Pelvis
  kernel: Vascular/Standard
  notes: Comparație între fazele native și cu contrast
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Arterială CAP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Morfologie aortică și sediul extravazării
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Arterială CAP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Extensie longitudinală a anevrismului
  plane: Sagital
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Arterială CAP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Randare 3D VR de urgență pentru planificare EVAR
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Se consemnează situația de urgență majoră
  renal: Urgență vitală - se efectuează indiferent de funcția renală
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă CAP
  notes: RAPID - detecția hematoamelor și calcificărilor
  start: Diafragm
  thickness: 0.625 mm
- delay: 25-30 sec
  end: Simfiză pubiană
  name: Fază Arterială CAP
  notes: Sângerare activă și morfologia anevrismului
  start: Diafragm
  thickness: 0.625 mm
- delay: 70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală CAP
  notes: Organe parenchimatoase și sistem venos
  start: Diafragm
  thickness: 0.625 mm
slug: trauma-code-aaa
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D pentru politraumă)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Curent crescut (referință 300 mAs)
  pitch: 1.0-1.375
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Urgență / Cod Ruptură Anevrism de Aortă Abdominală (Cod AAA)
---

# CT Urgență / Cod Ruptură Anevrism de Aortă Abdominală (Cod AAA)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă CAP | 0 sec | Diafragm → Simfiză pubiană |
        | Fază Arterială CAP | 25-30 sec | Diafragm → Simfiză pubiană |
        | Fază Venoasă Portală CAP | 70 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Suspiciune de anevrism de aortă abdominală (AAA) rupt sau fisurat
        - Urgență vasculară aortică
        - Instabilitate hemodinamică cu durere abdominală acută și masă pulsatilă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență vitală
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volum | 125 mL |
        | Rată de Flux | 4-5 mL/s |
        | Durată |  |
        | Metodă Temporizare | Protocol trifazic rapid: Nativ + Arterial + Venoasă Portală |
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
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Curent crescut (referință 300 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D pentru politraumă) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol RAPID trifazic STAT: 1) Nativ toraco-abdomino-pelvin (hematom proaspăt retroperitoneal) 2) Arterial CAP (extravazare activă de contrast, urmărire bolus 25-30s) 3) Fază venoasă portală CAP la 70s. Alertare imediată a chirurgiei vasculare.

    === "Note Asistent"

        - Linie venoasă de calibru mare 18G minimum (ideal 2 linii). Produse sanguine pregătite la dispoziție.

        !!! warning "Siguranță"
            - **Funcție Renală:** Urgență vitală - se efectuează indiferent de funcția renală
            - **Alergii:** Se consemnează situația de urgență majoră

    === "Note Radiolog"

        - Nativ: hematom retroperitoneal hiperdens, sânge liber intraperitoneal. Arterial: extravazare activă de contrast (jet/blush), diametre anevrism, anatomia coletului pentru EVAR. Portal: evaluarea ischemiei viscerale/organelor parenchimatoase.

    === "Sfaturi & Recomandări"

        - Protocol de urgență maximă (STAT). Minimizați orice întârziere. Notificați imediat echipa de chirurgie vasculară / radiologie intervențională.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă CAP | Diafragm | Simfiză pubiană | 0 sec | 0.625 mm | RAPID - detecția hematoamelor și calcificărilor |
    | Fază Arterială CAP | Diafragm | Simfiză pubiană | 25-30 sec | 0.625 mm | Sângerare activă și morfologia anevrismului |
    | Fază Venoasă Portală CAP | Diafragm | Simfiză pubiană | 70 sec | 0.625 mm | Organe parenchimatoase și sistem venos |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Arterială CAP | Abdomen-Pelvis | 2.5 mm/2.5 mm | Vascular/Standard |  | Comparație între fazele native și cu contrast |
    | Coronal | Fază Arterială CAP | Abdomen-Pelvis | 2.5 mm/2.5 mm | Vascular |  | Morfologie aortică și sediul extravazării |
    | Sagital | Fază Arterială CAP | Abdomen-Pelvis | 2.5 mm/2.5 mm | Vascular |  | Extensie longitudinală a anevrismului |
    | 3D VR | Fază Arterială CAP | Abdomen-Pelvis | 1 mm/1 mm | Vascular |  | Randare 3D VR de urgență pentru planificare EVAR |
