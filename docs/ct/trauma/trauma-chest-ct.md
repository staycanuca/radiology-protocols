---
author: Departamentul de Radiologie
category: trauma
clinical_indications:
- Traumatism toracic închis (blunt chest trauma)
- Fracturi costale multiple / volet costal
- Pneumotorax / hemotorax post-traumatic
- Contuzie pulmonară / suspiciune leziune mediastinală
contrast:
  agent: N/A
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții oblice sagitale dedicate fiecărui arc costal. Cartografierea
    fracturilor costale. Randare 3D a peretelui toracic.
  nursing: Măsuri de precauție pentru traumă. Brațele ridicate dacă starea pacientului
    permite.
  rad: Căutați pneumotorax, hemotorax, fracturi costale (numărare și localizare precisă),
    contuzie pulmonară, leziune traumatică de aortă, fracturi de stern sau omoplat.
  tech: Achiziție unică de la vârfurile pulmonare până la sinusurile costodiafragmatice.
    RECONSTRUCȚII COSTALE dedicate obligatorii. Achiziție submilimetrică.
  tips: Achiziția submilimetrică este critică pentru detaliul fracturilor costale
    fine.
npo: Fără repaus alimentar - urgență
position: Decubit dorsal cu brațele ridicate dacă starea pacientului o permite
premedication: ''
protocol_type: trauma
recons:
- acquisition: CT Nativ Torace
  fov: Torace
  kernel: Standard
  notes: Fereastră de mediastin
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: CT Nativ Torace
  fov: Torace
  kernel: Lung
  notes: Fereastră de parenchim pulmonar
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Torace
  fov: Torace
  kernel: Standard
  notes: Evaluare leziune traumatică de aortă
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Nativ Torace
  fov: Torace
  kernel: Bone
  notes: Privire de ansamblu grilaj costal
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: CT Nativ Torace
  fov: Torace
  kernel: Bone
  notes: Reconstrucții oblice sagitale pe arcurile costale
  plane: Oblique sagittal
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică (examinare fără contrast)
series:
- delay: 0 sec
  end: Sinusuri costodiafragmatice
  name: CT Nativ Torace
  notes: Achiziție submilimetrică pentru grilajul costal
  start: Vârfuri pulmonare
  thickness: 0.625 mm
- delay: Urmărire bolus
  end: Sinusuri costodiafragmatice
  name: Angio-CT Torace
  notes: Evaluarea leziunilor vasculare și aortei toracice
  start: Vârfuri pulmonare
  thickness: 0.625 mm
slug: trauma-chest-ct
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D pentru politraumă)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Torace în Traumatism (Politraumatism)
sources:
- title: ACR Appropriateness Criteria — Major Blunt Trauma
  url: https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria
  institution: ACR
  source_region: US
  kind: Criterii de oportunitate clinică
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 7a9944bf40cbdca19afa54c99c357074c28dc49534ed1c21c814d9f71c93b198
- title: UT Southwestern Radiology — Trauma Whole-Body CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Torace în Traumatism (Politraumatism)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Nativ Torace | 0 sec | Vârfuri pulmonare → Sinusuri costodiafragmatice |
        | Angio-CT Torace | Urmărire bolus | Vârfuri pulmonare → Sinusuri costodiafragmatice |

    === "Indicații Clinice"

        - Traumatism toracic închis (blunt chest trauma)
        - Fracturi costale multiple / volet costal
        - Pneumotorax / hemotorax post-traumatic
        - Contuzie pulmonară / suspiciune leziune mediastinală

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate dacă starea pacientului o permite
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D pentru politraumă) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Achiziție unică de la vârfurile pulmonare până la sinusurile costodiafragmatice. RECONSTRUCȚII COSTALE dedicate obligatorii. Achiziție submilimetrică.

    === "Note Asistent"

        - Măsuri de precauție pentru traumă. Brațele ridicate dacă starea pacientului permite.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică (examinare fără contrast)
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Căutați pneumotorax, hemotorax, fracturi costale (numărare și localizare precisă), contuzie pulmonară, leziune traumatică de aortă, fracturi de stern sau omoplat.

    === "Sfaturi & Recomandări"

        - Achiziția submilimetrică este critică pentru detaliul fracturilor costale fine.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Nativ Torace | Vârfuri pulmonare | Sinusuri costodiafragmatice | 0 sec | 0.625 mm | Achiziție submilimetrică pentru grilajul costal |
    | Angio-CT Torace | Vârfuri pulmonare | Sinusuri costodiafragmatice | Urmărire bolus | 0.625 mm | Evaluarea leziunilor vasculare și aortei toracice |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Nativ Torace | Torace | 2.5 mm/2.5 mm | Standard |  | Fereastră de mediastin |
    | Axial | CT Nativ Torace | Torace | 1.5 mm/1.5 mm | Lung |  | Fereastră de parenchim pulmonar |
    | Axial | Angio-CT Torace | Torace | 1.25 mm/1.25 mm | Standard |  | Evaluare leziune traumatică de aortă |
    | Coronal | CT Nativ Torace | Torace | 2 mm/2 mm | Bone |  | Privire de ansamblu grilaj costal |
    | Oblique sagittal | CT Nativ Torace | Torace | 1.5 mm/1.5 mm | Bone |  | Reconstrucții oblice sagitale pe arcurile costale |

## Surse și revizuire

- [ACR Appropriateness Criteria — Major Blunt Trauma](https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria) — *ACR* (US)
- [UT Southwestern Radiology — Trauma Whole-Body CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
