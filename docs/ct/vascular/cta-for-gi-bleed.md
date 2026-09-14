---
author: None
category: vascular
clinical_indications:
- Hemoragie digestivă superioară sau inferioară activă
- Hematemeză masivă
- Melenă însoțită de instabilitate hemodinamică
- Rectoragie masivă / hematochezie
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4-5 mL/s
  roi: Aorta abdominală
  timing: 'Protocol trifazic: Nativ + Arterial + Tardiv'
  trigger: 150 HU
  volume: 1.5 mL/kg
last_updated: '2026-01-05'
notes:
  additional_recons: MIP al tuturor celor 3 faze afișate în paralel pentru comparație
    imediată. Identificarea ramului vascular sursă pentru ghidarea radiologiei intervenționale
    (embolizare).
  nursing: Linie venoasă de calibru mare 18-20G indispensabilă. Verificați refluxul
    sanguin și permeabilitatea înainte de injectare.
  rad: 'Faza nativă: decelarea hiperdensităților preexistente (cheaguri proaspete,
    material hemostatic, corpi străini). Faza arterială: identificarea jetului activ
    de extravazare (blush arterial). Faza tardivă: acumulare progresivă și redistribuire
    luminală a contrastului ce confirmă sângerarea activă.'
  tech: Debitul crescut de injectare (4-5 mL/s) este critic pentru faza arterială.
    Faza arterială la 25 secunde, apoi faza tardivă la 90-180 secunde pentru a decela
    acumularea progresivă (pooling) de contrast intraluminal.
  tips: Brațele complet ridicate. Viteză mare de deplasare a mesei pentru a acoperi
    rapid întreg abdomenul.
npo: Fără repaus alimentar - urgență medicală
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: vascular
recons:
- acquisition: Fază Nativă
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Decelarea hiperdensităților native
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Arterială
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Evidențierea extravazării arteriale / jetului activ
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Tardivă
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Aprecierea acumulării progresive de contrast în lumenul intestinal
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Arterială
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: MIP coronal pentru urmărirea originii vasculare a sângerării
  plane: Coronal
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Documentați situația de urgență dacă este cunoscută alergia
  renal: Urgență hemoragică - se efectuează cu monitorizare
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă
  notes: Detecția hiperdensităților intrinseci intraluminale
  start: Diafragm
  thickness: 1.25 mm
- delay: 25 sec
  end: Simfiză pubiană
  name: Fază Arterială
  notes: Debit ridicat (5 mL/s) pentru evidențierea extravazării active
  start: Diafragm
  thickness: 0.625 mm
- delay: 90-180 sec
  end: Simfiză pubiană
  name: Fază Tardivă
  notes: Întârziere extinsă pentru vizualizarea acumulării intraluminale de contrast
  start: Diafragm
  thickness: 1.25 mm
slug: cta-for-gi-bleed
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 300 mAs)
  pitch: '1.375'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT pentru Hemoragie Digestivă Activă
sources:
- title: ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic
    Angiography (CTA)
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf
  institution: ACR / NASCI / SIR
  source_region: US
  kind: Standard de practică angio-CT
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: bf7ff18eff996f000474c6a03d89a358f09f8af2ee90da1217121760ae1ae6f9
- title: UT Southwestern Radiology — CTA & Vascular CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# Angio-CT pentru Hemoragie Digestivă Activă

**Ultima actualizare:** 2026-01-05
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | Diafragm → Simfiză pubiană |
        | Fază Arterială | 25 sec | Diafragm → Simfiză pubiană |
        | Fază Tardivă | 90-180 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Hemoragie digestivă superioară sau inferioară activă
        - Hematemeză masivă
        - Melenă însoțită de instabilitate hemodinamică
        - Rectoragie masivă / hematochezie

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență medicală
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 20s |
        | Metodă Temporizare | Protocol trifazic: Nativ + Arterial + Tardiv |
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
    | **Curent Tub (mAs)** | Auto (referință 300 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Debitul crescut de injectare (4-5 mL/s) este critic pentru faza arterială. Faza arterială la 25 secunde, apoi faza tardivă la 90-180 secunde pentru a decela acumularea progresivă (pooling) de contrast intraluminal.

    === "Note Asistent"

        - Linie venoasă de calibru mare 18-20G indispensabilă. Verificați refluxul sanguin și permeabilitatea înainte de injectare.

        !!! warning "Siguranță"
            - **Funcție Renală:** Urgență hemoragică - se efectuează cu monitorizare
            - **Alergii:** Documentați situația de urgență dacă este cunoscută alergia

    === "Note Radiolog"

        - Faza nativă: decelarea hiperdensităților preexistente (cheaguri proaspete, material hemostatic, corpi străini). Faza arterială: identificarea jetului activ de extravazare (blush arterial). Faza tardivă: acumulare progresivă și redistribuire luminală a contrastului ce confirmă sângerarea activă.

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate. Viteză mare de deplasare a mesei pentru a acoperi rapid întreg abdomenul.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | Diafragm | Simfiză pubiană | 0 sec | 1.25 mm | Detecția hiperdensităților intrinseci intraluminale |
    | Fază Arterială | Diafragm | Simfiză pubiană | 25 sec | 0.625 mm | Debit ridicat (5 mL/s) pentru evidențierea extravazării active |
    | Fază Tardivă | Diafragm | Simfiză pubiană | 90-180 sec | 1.25 mm | Întârziere extinsă pentru vizualizarea acumulării intraluminale de contrast |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Decelarea hiperdensităților native |
    | Axial | Fază Arterială | Abdomen-Pelvis | 1.25 mm/1.25 mm | Standard |  | Evidențierea extravazării arteriale / jetului activ |
    | Axial | Fază Tardivă | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Aprecierea acumulării progresive de contrast în lumenul intestinal |
    | Coronal | Fază Arterială | Abdomen-Pelvis | 2 mm/2 mm | Standard |  | MIP coronal pentru urmărirea originii vasculare a sângerării |

## Surse și revizuire

- [ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf) — *ACR / NASCI / SIR* (US)
- [UT Southwestern Radiology — CTA & Vascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
