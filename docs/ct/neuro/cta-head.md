---
author: Departamentul de Radiologie
category: neuro
clinical_indications:
- Screening și diagnostic anevrisme intracraniene
- Hemoragie subarahnoidiană (HSA) non-traumatică
- Malformații vasculare intracraniene (MAV, fistule durale)
- Stenoze arteriale intracraniene
contrast:
  agent: Omnipaque 350
  flow_rate: 4-5 mL/s
  roi: Crosa aortei sau artera carotidă comună
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 75-100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Randare 3D VR interactivă și proiecții MIP multiangulare. Măsurarea
    anevrismelor în planuri tridimensionale ortogonale.
  nursing: Linie venoasă minim 20G. Bolus compact de contrast esențial.
  rad: 'Poligonul Willis complet: ACI intracraniană (porțiune pietroasă, cavernosă,
    supraclinoidiană), ACA (A1, A2), ACoA, ACM (M1, M2, M3), ACP (P1, P2), ACoP, trunchiul
    bazilar și arterele cerebeloase. Măsurați diametrele și coletul oricărui anevrism
    decelat.'
  tech: Scanare de la baza craniului până la vertex. Urmărire bolus. Achiziție submilimetrică
    dedicată reconstrucțiilor tridimensionale 3D VR.
  tips: Imobilizare fermă a capului. Secțiuni fine pentru a nu omite microanevrismele
    < 3 mm.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu capul înainte
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Imagini axiale native sursă
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Angio-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Vedere de ansamblu MIP pe axele vasculare
  plane: MIP
  thickness_increment: 5 mm/2 mm
- acquisition: Angio-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Angiogramă tridimensională 3D VR
  plane: 3D VR
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Angio-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Reconstrucții curbate pe segmente vasculare specifice
  plane: Curved MPR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Gaura occipitală
  name: CT Nativ Craniu (opțional)
  notes: Referință nativă de hemoragie dacă este suspectată HSA
  start: Vertex
  thickness: 2.5 mm
- delay: Urmărire bolus
  end: Vertex
  name: Angio-CT Cerebral
  notes: Achiziție submilimetrică pentru randare 3D vasculară
  start: Baza craniului
  thickness: 0.625 mm
slug: cta-head
synonyms: []
tech_params:
  aec: Activat (Modulare angulară adaptivă / mAs fix fosa posterioară)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: 100-120
  mas: Auto (referință 250 mAs)
  pitch: Helical
  rotation_time: 0.5-0.6s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Cerebral (Poligonul Willis)
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

# Angio-CT Cerebral (Poligonul Willis)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Nativ Craniu (opțional) | 0 sec | Vertex → Gaura occipitală |
        | Angio-CT Cerebral | Urmărire bolus | Baza craniului → Vertex |

    === "Indicații Clinice"

        - Screening și diagnostic anevrisme intracraniene
        - Hemoragie subarahnoidiană (HSA) non-traumatică
        - Malformații vasculare intracraniene (MAV, fistule durale)
        - Stenoze arteriale intracraniene

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
        | Volum | 75-100 mL |
        | Rată de Flux | 4-5 mL/s |
        | Durată |  |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Crosa aortei sau artera carotidă comună |
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
    | **Curent Tub (mAs)** | Auto (referință 250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / mAs fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | 0.5-0.6 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare de la baza craniului până la vertex. Urmărire bolus. Achiziție submilimetrică dedicată reconstrucțiilor tridimensionale 3D VR.

    === "Note Asistent"

        - Linie venoasă minim 20G. Bolus compact de contrast esențial.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Poligonul Willis complet: ACI intracraniană (porțiune pietroasă, cavernosă, supraclinoidiană), ACA (A1, A2), ACoA, ACM (M1, M2, M3), ACP (P1, P2), ACoP, trunchiul bazilar și arterele cerebeloase. Măsurați diametrele și coletul oricărui anevrism decelat.

    === "Sfaturi & Recomandări"

        - Imobilizare fermă a capului. Secțiuni fine pentru a nu omite microanevrismele < 3 mm.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Nativ Craniu (opțional) | Vertex | Gaura occipitală | 0 sec | 2.5 mm | Referință nativă de hemoragie dacă este suspectată HSA |
    | Angio-CT Cerebral | Baza craniului | Vertex | Urmărire bolus | 0.625 mm | Achiziție submilimetrică pentru randare 3D vasculară |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Cerebral | Craniu | 0.625 mm/0.625 mm | Brain |  | Imagini axiale native sursă |
    | MIP | Angio-CT Cerebral | Craniu | 5 mm/2 mm | Brain |  | Vedere de ansamblu MIP pe axele vasculare |
    | 3D VR | Angio-CT Cerebral | Craniu | 0.625 mm/0.625 mm | Brain |  | Angiogramă tridimensională 3D VR |
    | Curved MPR | Angio-CT Cerebral | Craniu | 1 mm/1 mm | Brain |  | Reconstrucții curbate pe segmente vasculare specifice |

## Surse și revizuire

- [AAPM CT Protocols — Adult Routine Head CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Neuro / Head Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
