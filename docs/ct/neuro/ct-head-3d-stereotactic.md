---
author: Departamentul de Radiologie
category: neuro
clinical_indications:
- Planificare pre-operatorie stereotaxică / neuronavigație intraoperatorie
- Stimulare cerebrală profundă (DBS - Deep Brain Stimulation)
- Puncție-biopsie cerebrală stereotaxică
- Planificare radiochirurgie stereotaxică (Gamma Knife / CyberKnife)
contrast:
  agent: Nativ de regulă. Substanță de contrast opțională în caz de mase tumorale
  flow_rate: 3 mL/s
  volume: 'Dacă este indicat: 100 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Export direct DICOM către stația de neuronavigație / radiochirurgie.
    Reconstrucție 3D a calotei și reperelor.
  nursing: Poziționare strictă conform reperelor cerute de medicul neurochirurg. Protejarea
    cadrului stereotaxic sau markerilor fiduciali.
  rad: Localizarea reperelor anatomice (comisura anterioară - CA, comisura posterioară
    - CP, linia CA-CP). Coordonate stereotaxice (x, y, z) pentru ținta chirurgicală.
    Relația cu structurile vasculare și parenchimatoase critice.
  tech: Achiziție izotropă submilimetrică (< 0.6 mm) fără înclinarea gantry-ului (gantry
    tilt = 0 grade). Exportul volumului de date DICOM cu grosime și increment identice
    pentru sistemul de planificare neurochirurgicală.
  tips: Voxelii izotropi și lipsa unghiului gantry sunt obligatorii pentru acuratețea
    submilimetrică a navigației.
npo: Repaus alimentar 4 ore dacă se administrează contrast
position: Decubit dorsal cu capul fixat în cadru stereotaxic sau cu markeri fiduciali
  cutanați atașați
premedication: ''
protocol_type: neuroradiology
recons:
- acquisition: CT Stereotaxic Cerebral
  fov: Craniu
  kernel: Brain (Bone if needed)
  notes: Plan axial izotrop de referință
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Stereotaxic Cerebral
  fov: Craniu
  kernel: Brain
  notes: Plan coronal izotrop
  plane: Coronal
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Stereotaxic Cerebral
  fov: Craniu
  kernel: Brain
  notes: Plan mediosagital pe linia comisurală CA-CP
  plane: Sagital
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Stereotaxic Cerebral
  fov: Craniu
  kernel: Brain
  notes: Suprafață 3D pentru corelarea optică a neuronavigației
  plane: 3D surface
  thickness_increment: 0.625 mm/0.625 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică pentru scanarea nativă
series:
- delay: 0 sec
  end: Baza craniului
  name: CT Stereotaxic Cerebral
  notes: Achiziție izotropă submilimetrică cu gantry 0 grade
  start: Vertex
  thickness: 0.625 mm
slug: ct-head-3d-stereotactic
synonyms: []
tech_params:
  aec: Activat (Modulare angulară adaptivă / mAs fix fosa posterioară)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: '120'
  mas: Auto (referință 300 mAs)
  pitch: Pitch for isotropic
  rotation_time: Helicals
  scan_mode: Secvențial (Axial) sau Elicoidal fin
  slice_thickness: 0.625 mm
title: CT Cerebral 3D Stereotaxic (Planificare Neurochirurgicală / Neuronavigație)
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

# CT Cerebral 3D Stereotaxic (Planificare Neurochirurgicală / Neuronavigație)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Stereotaxic Cerebral | 0 sec | Vertex → Baza craniului |

    === "Indicații Clinice"

        - Planificare pre-operatorie stereotaxică / neuronavigație intraoperatorie
        - Stimulare cerebrală profundă (DBS - Deep Brain Stimulation)
        - Puncție-biopsie cerebrală stereotaxică
        - Planificare radiochirurgie stereotaxică (Gamma Knife / CyberKnife)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul fixat în cadru stereotaxic sau cu markeri fiduciali cutanați atașați
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore dacă se administrează contrast
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Substanță de contrast opțională în caz de mase tumorale |
        | Volum | Dacă este indicat: 100 mL |
        | Rată de Flux | 3 mL/s |
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
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | Helical s |
    | **Pitch (Factor Pas)** | Pitch for isotropic |
    | **Mod Scanare** | Secvențial (Axial) sau Elicoidal fin |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Achiziție izotropă submilimetrică (< 0.6 mm) fără înclinarea gantry-ului (gantry tilt = 0 grade). Exportul volumului de date DICOM cu grosime și increment identice pentru sistemul de planificare neurochirurgicală.

    === "Note Asistent"

        - Poziționare strictă conform reperelor cerute de medicul neurochirurg. Protejarea cadrului stereotaxic sau markerilor fiduciali.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică pentru scanarea nativă
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Localizarea reperelor anatomice (comisura anterioară - CA, comisura posterioară - CP, linia CA-CP). Coordonate stereotaxice (x, y, z) pentru ținta chirurgicală. Relația cu structurile vasculare și parenchimatoase critice.

    === "Sfaturi & Recomandări"

        - Voxelii izotropi și lipsa unghiului gantry sunt obligatorii pentru acuratețea submilimetrică a navigației.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Stereotaxic Cerebral | Vertex | Baza craniului | 0 sec | 0.625 mm | Achiziție izotropă submilimetrică cu gantry 0 grade |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Stereotaxic Cerebral | Craniu | 0.625 mm/0.625 mm | Brain (Bone if needed) |  | Plan axial izotrop de referință |
    | Coronal | CT Stereotaxic Cerebral | Craniu | 0.625 mm/0.625 mm | Brain |  | Plan coronal izotrop |
    | Sagital | CT Stereotaxic Cerebral | Craniu | 0.625 mm/0.625 mm | Brain |  | Plan mediosagital pe linia comisurală CA-CP |
    | 3D surface | CT Stereotaxic Cerebral | Craniu | 0.625 mm/0.625 mm | Brain |  | Suprafață 3D pentru corelarea optică a neuronavigației |

## Surse și revizuire

- [AAPM CT Protocols — Adult Routine Head CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Neuro / Head Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
