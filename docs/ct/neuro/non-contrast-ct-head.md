---
author: Departamentul de Radiologie
category: neuro
clinical_indications:
- Protocol de primă intenție în suspiciunea de AVC acut
- Traumatism cranio-cerebral (TCC)
- Cefalee acută brutală severă ('cea mai intensă durere de cap din viață')
- Alterarea stării de conștiență / comă / confuzie inexplicabilă
- Suspiciune de hemoragie intracraniană sau hidrocefalie acută
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-01-03'
notes:
  additional_recons: Secțiuni fine submilimetrice sau de 1.25 mm în fereastră osoasă
    dacă se suspectează fracturi craniene fine.
  nursing: Nu este necesară linie venoasă. Explicați pacientului importanța imobilizării
    capului.
  rad: Căutați semnul arterei cerebrale medii hiperdense. Evaluați diferențierea substanță
    albă-cenușie (ștergerea conturului nucleilor bazali sau al panglicii insulare).
    Identificați hemoragia (epidurală, subdurală, subarahnoidiană, intraparenchimatoasă,
    intraventriculară). Evaluați efectul de masă, devierea liniei mediene și angajările
    cerebrale.
  tech: Minimizați mișcarea pacientului. Înclinați gantry-ul paralel cu linia orbitomeatală
    (OM) / baza craniului pentru a reduce doza de iradiere pe cristalin. Asigurați
    poziția perfect dreaptă a capului.
  tips: Îndepărtați protezele dentare și aparatele auditive. Asigurați capul cu benzi
    de fixare.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu capul fixat simetric în suportul dedicat
premedication: ''
protocol_type: neuroradiology
recons:
- acquisition: CT Cerebral Nativ
  fov: Craniu
  kernel: Brain
  notes: Serie diagnostică primară în fereastră de creier
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: CT Cerebral Nativ
  fov: Craniu
  kernel: Bone
  notes: Fereastră osoasă pentru decelarea fracturilor calotei și bazei
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Cerebral Nativ
  fov: Craniu
  kernel: Brain
  notes: Plan coronal pentru baza craniului și vertex
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: CT Cerebral Nativ
  fov: Craniu
  kernel: Brain
  notes: Plan sagital pentru structurile liniei mediene și ventriculul IV
  plane: Sagital
  thickness_increment: 2.5 mm/2.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Gaura occipitală
  name: CT Cerebral Nativ
  notes: Unghi paralel cu linia orbitomeatală / baza craniului
  start: Vertex
  thickness: 2.5 mm
slug: non-contrast-ct-head
synonyms: []
tech_params:
  aec: Activat (Modulare angulară adaptivă / mAs fix fosa posterioară)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: '120'
  mas: Auto (referință 300 mAs)
  pitch: '0.5'
  rotation_time: 1s
  scan_mode: Secvențial (Axial) sau Elicoidal fin
  slice_thickness: 2.5 mm
title: CT Cerebral Nativ
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

# CT Cerebral Nativ

**Ultima actualizare:** 2026-01-03
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Cerebral Nativ | 0 sec | Vertex → Gaura occipitală |

    === "Indicații Clinice"

        - Protocol de primă intenție în suspiciunea de AVC acut
        - Traumatism cranio-cerebral (TCC)
        - Cefalee acută brutală severă ('cea mai intensă durere de cap din viață')
        - Alterarea stării de conștiență / comă / confuzie inexplicabilă
        - Suspiciune de hemoragie intracraniană sau hidrocefalie acută

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul fixat simetric în suportul dedicat
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Fără substanță de contrast |
        | Volum |  |
        | Rată de Flux |  |
        | Durată |  |
        | Metodă Temporizare |  |
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
    | **Curent Tub (mAs)** | Auto (referință 300 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / mAs fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 2.5 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | 1 s |
    | **Pitch (Factor Pas)** | 0.5 |
    | **Mod Scanare** | Secvențial (Axial) sau Elicoidal fin |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Minimizați mișcarea pacientului. Înclinați gantry-ul paralel cu linia orbitomeatală (OM) / baza craniului pentru a reduce doza de iradiere pe cristalin. Asigurați poziția perfect dreaptă a capului.

    === "Note Asistent"

        - Nu este necesară linie venoasă. Explicați pacientului importanța imobilizării capului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Căutați semnul arterei cerebrale medii hiperdense. Evaluați diferențierea substanță albă-cenușie (ștergerea conturului nucleilor bazali sau al panglicii insulare). Identificați hemoragia (epidurală, subdurală, subarahnoidiană, intraparenchimatoasă, intraventriculară). Evaluați efectul de masă, devierea liniei mediene și angajările cerebrale.

    === "Sfaturi & Recomandări"

        - Îndepărtați protezele dentare și aparatele auditive. Asigurați capul cu benzi de fixare.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Cerebral Nativ | Vertex | Gaura occipitală | 0 sec | 2.5 mm | Unghi paralel cu linia orbitomeatală / baza craniului |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Cerebral Nativ | Craniu | 2.5 mm/2.5 mm | Brain |  | Serie diagnostică primară în fereastră de creier |
    | Axial | CT Cerebral Nativ | Craniu | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă pentru decelarea fracturilor calotei și bazei |
    | Coronal | CT Cerebral Nativ | Craniu | 2.5 mm/2.5 mm | Brain |  | Plan coronal pentru baza craniului și vertex |
    | Sagital | CT Cerebral Nativ | Craniu | 2.5 mm/2.5 mm | Brain |  | Plan sagital pentru structurile liniei mediene și ventriculul IV |

## Surse și revizuire

- [AAPM CT Protocols — Adult Routine Head CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Neuro / Head Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
