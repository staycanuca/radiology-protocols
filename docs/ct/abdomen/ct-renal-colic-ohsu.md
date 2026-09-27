---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Colică nefretică acută, durere lombară acută cu iradiere inghino-genitală
- Hematurie microscopică sau macroscopică suspectă de etiologie litiazică
- Evaluare dimensiune, densitate (HU) și localizare a calculilor renali și ureterali
  înainte de ESWL sau ureteroscopie
- Urmărire post-tratament litiazic (CT Renal Colic Follow-up WO)
contrast:
  agent: FĂRĂ
  duration: 0s
  flow_rate: 0 mL/s
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: 0 mL
iris_reference:
  chapter: Aparat uro-genital și glande suprarenale
  radiation_dose: Clasa 3 (Moderată 4 - 7 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: MIP coronal pentru traiectul ureteral.
  nursing: Confort pacient; managementul durerii dacă este în colică activă.
  rad: 'Specificați: 1) Dimensiunea calculului (axul maxim); 2) Localizarea exactă
    (caliceal, bazinetal, ureter lombar, iliac sau joncțiune uretero-vezicală UVJ);
    3) Densitatea calculului în HU (acid uric < 500 HU vs oxalat/fosfat de calciu
    > 1000 HU); 4) Semne secundare de obstrucție (ureterohidronefroză, edem perirenal/periureteral).'
  tech: Protocol cu doză redusă de iradiere conform standardelor OHSU / ACR. Asigurați-vă
    că scanarea cuprinde întreaga vezică urinară până la simfiză.
  tips: Pentru pacienții subțiri (< 70 kg), scanarea la 100 kV sporește contrastul
    calculilor pe fondul țesuturilor moi, reducând simultan doza.
npo: N/A — protocol nativ
position: Decubit dorsal (sau decubit ventral/prone dacă este necesară diferențierea
  unui calcul la joncțiunea uretero-vezicală de un calcul liber în vezică)
premedication: Fără contrast oral sau i.v.
protocol_type: non-contrast
recons:
- acquisition: CT Renal Colic
  fov: Aparat Urinar
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f + Bone / I70f
  notes: Secțiuni de 2 mm pentru detecția microlitiazei (> 1-2 mm)
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: CT Renal Colic
  fov: Tract Urinar
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Vizualizare longitudinală a ureterelor și a gradului de hidronefroză
  plane: Coronal
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: N/A — fără contrast
  renal: N/A — fără contrast
series:
- delay: 0 sec
  end: Baza vezicii urinare și simfiza pubiană
  name: CT Colică Renală Nativ
  notes: Apnee inspiratorie; scanare rapidă continuă
  start: Polul superior al ambilor rinichi (T11-T12)
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100-120 kV (sau Sn100 kV)
  mas: CAREDose4D setat pe profil Low-Dose (CTDIvol < 3-4 mGy; doză efectivă < 2-3
    mSv)
  pitch: 1.0 - 1.2
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Colică Renală / Litiază Nativ Low-Dose (Protocol OHSU)
---

# CT Colică Renală / Litiază Nativ Low-Dose (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Colică Renală Nativ | 0 sec | Polul superior al ambilor rinichi (T11-T12) → Baza vezicii urinare și simfiza pubiană |

    === "Indicații Clinice"

        - Colică nefretică acută, durere lombară acută cu iradiere inghino-genitală
        - Hematurie microscopică sau macroscopică suspectă de etiologie litiazică
        - Evaluare dimensiune, densitate (HU) și localizare a calculilor renali și ureterali înainte de ESWL sau ureteroscopie
        - Urmărire post-tratament litiazic (CT Renal Colic Follow-up WO)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat uro-genital și glande suprarenale*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 4 - 7 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal (sau decubit ventral/prone dacă este necesară diferențierea unui calcul la joncțiunea uretero-vezicală de un calcul liber în vezică)
    - **Repaus Alimentar (NPO):** N/A — protocol nativ
    - **Premedicație / Pregătire:**
        - Fără contrast oral sau i.v.

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV (sau Sn100 kV) kV |
    | **Curent Tub (mAs)** | CAREDose4D setat pe profil Low-Dose (CTDIvol < 3-4 mGy; doză efectivă < 2-3 mSv) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0 - 1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol cu doză redusă de iradiere conform standardelor OHSU / ACR. Asigurați-vă că scanarea cuprinde întreaga vezică urinară până la simfiză.

    === "Note Asistent"

        - Confort pacient; managementul durerii dacă este în colică activă.

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — fără contrast
            - **Alergii:** N/A — fără contrast

    === "Note Radiolog"

        - Specificați: 1) Dimensiunea calculului (axul maxim); 2) Localizarea exactă (caliceal, bazinetal, ureter lombar, iliac sau joncțiune uretero-vezicală UVJ); 3) Densitatea calculului în HU (acid uric < 500 HU vs oxalat/fosfat de calciu > 1000 HU); 4) Semne secundare de obstrucție (ureterohidronefroză, edem perirenal/periureteral).

    === "Sfaturi & Recomandări"

        - Pentru pacienții subțiri (< 70 kg), scanarea la 100 kV sporește contrastul calculilor pe fondul țesuturilor moi, reducând simultan doza.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Colică Renală Nativ | Polul superior al ambilor rinichi (T11-T12) | Baza vezicii urinare și simfiza pubiană | 0 sec | 0.625 mm | Apnee inspiratorie; scanare rapidă continuă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Renal Colic | Aparat Urinar | 2.0 mm / 2.0 mm | Standard / I30f + Bone / I70f | Admire 3 / AIDR 3D | Secțiuni de 2 mm pentru detecția microlitiazei (> 1-2 mm) |
    | Coronal | CT Renal Colic | Tract Urinar | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D | Vizualizare longitudinală a ureterelor și a gradului de hidronefroză |
