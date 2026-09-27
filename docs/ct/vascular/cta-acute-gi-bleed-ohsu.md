---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: vascular
clinical_indications:
- Hemoragie digestivă superioară sau inferioară activă, severă, cu instabilitate hemodinamică
- Rectoragie masivă, melenă sau hematochezie fără sursă identificată endoscopic
- Planificare pre-angiografie intervențională de embolizare transcateter sau intervenție
  chirurgicală
- Detecția extravazării active intraluminale de contrast (debit de sângerare ≥ 0.3
  - 0.5 mL/min)
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 25-30s
  flow_rate: 4.0 - 5.0 mL/s
  roi: Aorta abdominală la originea trunchiului celiac
  timing: Fază Nativă + Fază Arterială (Bolus tracking la 150 HU în aorta celiacă)
    + Fază Venoasă Portală (65-70 sec)
  trigger: 150 HU
  volume: 125-150 mL
iris_reference:
  chapter: Aparat cardiovascular & Sistem vascular
  radiation_dose: Clasa 4 (Ridicată > 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: MIP 3D vascular pentru orientarea cateterismului selectiv.
  nursing: Monitorizare semne vitale (TA, puls) și acces la fluide de resuscitare.
  rad: 'Semn cert de sângerare activă: extravazare de contrast > 90-100 HU în faza
    arterială, care își modifică forma și crește în volum în faza venoasă (contrast
    pooling). Dacă este identificată sursa, contactați imediat radiologul intervenționist.'
  tech: Canulă de calibru mare 18G în plica cotului. Flush salin 40 mL la 4-5 mL/s.
    Scanare fără întârziere.
  tips: 'Faza nativă este critică: fără ea, o pastilă radio-opacă (bismut, fier, calciu)
    sau un clip hemostatic poate fi confundat cu sângerarea activă.'
npo: Urgență acută — N/A
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: STRICT INTERZIS contrastul oral iodat sau baritat (ar masca complet
  extravazarea activă intraluminală)
protocol_type: multiphase
recons:
- acquisition: Toate cele 3 faze
  fov: Abdomen & Pelvis
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Secțiuni fine multiplanare pentru localizarea ansei digestive afectate
  plane: Axial & Coronal
  thickness_increment: 1.5 mm / 1.5 mm
- acquisition: Fază Arterială
  fov: Abdomen
  ir_strength: Standard
  kernel: Vascular
  notes: MIP pentru cartografierea originii vasculare din AMS, AMI sau trunchiul celiac
  plane: Coronal
  thickness_increment: 5.0 mm / 2.5 mm MIP
safety:
  allergy: În urgență vitală masivă, examinarea se efectuează cu măsuri de resuscitare
    pregătite.
  renal: Beneficiul diagnosticului salvator de viață depășește riscul de nefrotoxicitate.
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă (Abdomen & Pelvis)
  notes: Esențială pentru a diferenția corpii străini intraluminali, medicamentele
    radiopace sau hematoamele preexistente de extravazarea activă
  start: Cupole diafragmatice
  thickness: 1.0 mm
- delay: Trigger + 10-15 sec
  end: Simfiză pubiană
  name: Fază Arterială (CTA)
  notes: Detecție extravazare activă arterială de contrast (blush vascular) în lumenul
    digestiv
  start: Diafragm
  thickness: 0.625 mm
- delay: 65-70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală
  notes: Confirmă persistența și acumularea progresivă (pooling) a contrastului extravazat
    în lumen
  start: Diafragm
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100-120 kV (sau 100 kV pentru sporirea atenuării iodului)
  mas: CAREDose4D / SureExposure3D
  pitch: 0.9 - 1.1
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CTA Hemoragie Digestivă Acută (Protocol OHSU)
---

# CTA Hemoragie Digestivă Acută (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă (Abdomen & Pelvis) | 0 sec | Cupole diafragmatice → Simfiză pubiană |
        | Fază Arterială (CTA) | Trigger + 10-15 sec | Diafragm → Simfiză pubiană |
        | Fază Venoasă Portală | 65-70 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Hemoragie digestivă superioară sau inferioară activă, severă, cu instabilitate hemodinamică
        - Rectoragie masivă, melenă sau hematochezie fără sursă identificată endoscopic
        - Planificare pre-angiografie intervențională de embolizare transcateter sau intervenție chirurgicală
        - Detecția extravazării active intraluminale de contrast (debit de sângerare ≥ 0.3 - 0.5 mL/min)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat cardiovascular & Sistem vascular*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 4 (Ridicată > 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Urgență acută — N/A
    - **Premedicație / Pregătire:**
        - STRICT INTERZIS contrastul oral iodat sau baritat (ar masca complet extravazarea activă intraluminală)

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 125-150 mL |
        | Rată de Flux | 4.0 - 5.0 mL/s |
        | Durată | 25-30s |
        | Metodă Temporizare | Fază Nativă + Fază Arterială (Bolus tracking la 150 HU în aorta celiacă) + Fază Venoasă Portală (65-70 sec) |
        | Poziționare ROI | Aorta abdominală la originea trunchiului celiac |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV (sau 100 kV pentru sporirea atenuării iodului) kV |
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

        - Canulă de calibru mare 18G în plica cotului. Flush salin 40 mL la 4-5 mL/s. Scanare fără întârziere.

    === "Note Asistent"

        - Monitorizare semne vitale (TA, puls) și acces la fluide de resuscitare.

        !!! warning "Siguranță"
            - **Funcție Renală:** Beneficiul diagnosticului salvator de viață depășește riscul de nefrotoxicitate.
            - **Alergii:** În urgență vitală masivă, examinarea se efectuează cu măsuri de resuscitare pregătite.

    === "Note Radiolog"

        - Semn cert de sângerare activă: extravazare de contrast > 90-100 HU în faza arterială, care își modifică forma și crește în volum în faza venoasă (contrast pooling). Dacă este identificată sursa, contactați imediat radiologul intervenționist.

    === "Sfaturi & Recomandări"

        - Faza nativă este critică: fără ea, o pastilă radio-opacă (bismut, fier, calciu) sau un clip hemostatic poate fi confundat cu sângerarea activă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă (Abdomen & Pelvis) | Cupole diafragmatice | Simfiză pubiană | 0 sec | 1.0 mm | Esențială pentru a diferenția corpii străini intraluminali, medicamentele radiopace sau hematoamele preexistente de extravazarea activă |
    | Fază Arterială (CTA) | Diafragm | Simfiză pubiană | Trigger + 10-15 sec | 0.625 mm | Detecție extravazare activă arterială de contrast (blush vascular) în lumenul digestiv |
    | Fază Venoasă Portală | Diafragm | Simfiză pubiană | 65-70 sec | 0.625 mm | Confirmă persistența și acumularea progresivă (pooling) a contrastului extravazat în lumen |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial & Coronal | Toate cele 3 faze | Abdomen & Pelvis | 1.5 mm / 1.5 mm | Standard / I30f | Admire 3 / AIDR 3D | Secțiuni fine multiplanare pentru localizarea ansei digestive afectate |
    | Coronal | Fază Arterială | Abdomen | 5.0 mm / 2.5 mm MIP | Vascular | Standard | MIP pentru cartografierea originii vasculare din AMS, AMI sau trunchiul celiac |
