---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Contraindicație absolută la substanțele de contrast iodate (antecedente de șoc anafilactic
  sever)
- Insuficiență renală severă (eGFR < 30 mL/min fără dializă cronică)
- Suspiciune de hematom retroperitoneal sau hemoragie internă spontană/post-traumatică
- Evaluare calcificări vasculare sau pancreatită cronică calcifiantă
contrast:
  agent: FĂRĂ
  duration: 0s
  flow_rate: 0 mL/s
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: 0 mL
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții coronale oblice la nevoie.
  nursing: Confort pacient.
  rad: Apreciați densitatea spontană a parenchimelor, prezența hematoamelor hiperdense
    (> 50-60 HU), calcificările și aerul liber intraperitoneal (pneumoperitoneu).
  tech: Brațele complet ridicate deasupra capului. Evitați mișcarea respiratorie pe
    durata scanării.
  tips: Dacă indicația este exclusiv litiază renală/ureterală, utilizați protocolul
    dedicat de colică renală cu doză ultra-joasă (CT Renal Colic WO).
npo: Repaus alimentar 4 ore dacă este posibil
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Fără contrast oral iodat sau baritat; apă per os permisă
protocol_type: non-contrast
recons:
- acquisition: CT Nativ
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Serii multiplanare de ansamblu
  plane: Axial, Coronal & Sagital
  thickness_increment: 3.0 mm / 3.0 mm (Axial), 2.0 mm / 2.0 mm (Cor/Sag)
safety:
  allergy: N/A — fără contrast
  renal: N/A — fără contrast
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: CT Abdomen & Pelvis Nativ
  notes: Scanare în apnee inspiratorie completă
  start: Cupole diafragmatice
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.9 - 1.1
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Abdomen & Pelvis Nativ (Protocol OHSU)
---

# CT Abdomen & Pelvis Nativ (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Abdomen & Pelvis Nativ | 0 sec | Cupole diafragmatice → Simfiză pubiană |

    === "Indicații Clinice"

        - Contraindicație absolută la substanțele de contrast iodate (antecedente de șoc anafilactic sever)
        - Insuficiență renală severă (eGFR < 30 mL/min fără dializă cronică)
        - Suspiciune de hematom retroperitoneal sau hemoragie internă spontană/post-traumatică
        - Evaluare calcificări vasculare sau pancreatită cronică calcifiantă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore dacă este posibil
    - **Premedicație / Pregătire:**
        - Fără contrast oral iodat sau baritat; apă per os permisă

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | CAREkV 100-120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Brațele complet ridicate deasupra capului. Evitați mișcarea respiratorie pe durata scanării.

    === "Note Asistent"

        - Confort pacient.

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — fără contrast
            - **Alergii:** N/A — fără contrast

    === "Note Radiolog"

        - Apreciați densitatea spontană a parenchimelor, prezența hematoamelor hiperdense (> 50-60 HU), calcificările și aerul liber intraperitoneal (pneumoperitoneu).

    === "Sfaturi & Recomandări"

        - Dacă indicația este exclusiv litiază renală/ureterală, utilizați protocolul dedicat de colică renală cu doză ultra-joasă (CT Renal Colic WO).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Abdomen & Pelvis Nativ | Cupole diafragmatice | Simfiză pubiană | 0 sec | 0.625 mm | Scanare în apnee inspiratorie completă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | CT Nativ | Abdomen | 3.0 mm / 3.0 mm (Axial), 2.0 mm / 2.0 mm (Cor/Sag) | Standard / I30f | Admire 3 / AIDR 3D | Serii multiplanare de ansamblu |
