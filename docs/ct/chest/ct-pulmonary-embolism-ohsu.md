---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: chest
clinical_indications:
- Suspiciune de trombembolism pulmonar acut (TEP)
- Scor Wells sau Geneva intermediar sau înalt, sau D-dimeri pozitivi
- Dispnee acută inexplicabilă, durere toracică pleuritică, hemoptizie, sincope
- Evaluare hipertensiune pulmonară cronică trombembolică (CTEPH)
contrast:
  agent: Isovue 370 / Omnipaque 350
  duration: 12-15s
  flow_rate: 4.5 - 5.0 mL/s
  roi: Trunchiul arterei pulmonare principale
  timing: Bolus tracking în trunchiul arterei pulmonare, trigger 100 HU
  trigger: 100 HU
  volume: 60-75 mL
last_updated: '2026-09-20'
notes:
  additional_recons: MIP axial și coronal cu grosime de 5-10 mm pentru analiza ramurilor
    subsegmentare periferice.
  nursing: Verificare permeabilitate canulă venoasă cu jet rapid de ser înainte de
    conectarea injectorului automat.
  rad: Căutați defecte de umplere parțiale sau ocluzive (semnul călărețului pe bifurcație).
    Evaluați semnele de suprasolicitare a ventriculului drept (raport VD/VS > 1.0,
    reflux de contrast în vena cavă inferioară și venele suprahepatice).
  tech: Achiziție caudo-cranială preferată. Canulă 18G în plica cotului. Flush salin
    40-50 mL la 4.5 mL/s imediat după contrast pentru a goli vena cavă superioară
    și a elimina artefactele de striere.
  tips: 'Respirație: pacientul trebuie instruit să inspire ușor și să mențină apneea
    fără manevră Valsalva (care ar scădea întoarcerea venoasă și ar dilua contrastul
    în atriul drept cu sânge neopacifiat).'
npo: Repaus alimentar 2-4 ore dacă starea pacientului permite; în urgență N/A
position: Decubit dorsal cu brațele ridicate complet deasupra capului
premedication: Fără contrast oral
protocol_type: contrast-enhanced
recons:
- acquisition: Angio-CT Pulmonar
  fov: Torace
  ir_strength: Admire 3 / AIDR 3D
  kernel: Mediastinal (I30f) + Pulmonar (I50f)
  notes: Detecție defecte de umplere endoluminale în arterele pulmonare
  plane: Axial
  thickness_increment: 1.0 mm / 0.7 mm
- acquisition: Angio-CT Pulmonar
  fov: Torace
  ir_strength: Admire 3 / AIDR 3D
  kernel: Mediastinal (I30f)
  notes: Urmărire ramificații arteriale în plan anatomic
  plane: Coronal & Sagital
  thickness_increment: 1.5 mm / 1.5 mm
safety:
  allergy: Conform politicii OHSU. În suspiciune acută de TEP masiv, beneficiul este
    prioritar.
  renal: eGFR > 30 mL/min; la pacienți instabili hemodinamic se asigură hidratare
    promptă.
series:
- delay: Trigger + 3-4 sec
  end: Vârfuri pulmonare
  name: Angio-CT Pulmonar
  notes: Opacifiere densă a arterelor pulmonare principale, lobare, segmentare și
    subsegmentare (> 250 HU)
  start: Baza plămânilor (direcție caudo-cranială pentru a reduce artefactele de respirație
    la baze)
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 80-100 kVp (optimizat pentru K-edge iod)
  mas: CAREDose4D / SureExposure3D
  pitch: 1.2 - 1.5 (achiziție ultra-rapidă)
  rotation_time: 0.28 - 0.33 s
  scan_mode: Elicoidal (Flash / Dual Source)
  slice_thickness: 0.625 mm
title: CT Angiografie Pulmonară / TEP (Protocol OHSU)
---

# CT Angiografie Pulmonară / TEP (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Pulmonar | Trigger + 3-4 sec | Baza plămânilor (direcție caudo-cranială pentru a reduce artefactele de respirație la baze) → Vârfuri pulmonare |

    === "Indicații Clinice"

        - Suspiciune de trombembolism pulmonar acut (TEP)
        - Scor Wells sau Geneva intermediar sau înalt, sau D-dimeri pozitivi
        - Dispnee acută inexplicabilă, durere toracică pleuritică, hemoptizie, sincope
        - Evaluare hipertensiune pulmonară cronică trombembolică (CTEPH)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate complet deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 2-4 ore dacă starea pacientului permite; în urgență N/A
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 / Omnipaque 350 |
        | Volum | 60-75 mL |
        | Rată de Flux | 4.5 - 5.0 mL/s |
        | Durată | 12-15s |
        | Metodă Temporizare | Bolus tracking în trunchiul arterei pulmonare, trigger 100 HU |
        | Poziționare ROI | Trunchiul arterei pulmonare principale |
        | Declanșator (HU) | 100 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | CAREkV 80-100 kVp (optimizat pentru K-edge iod) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.28 - 0.33 s |
    | **Pitch (Factor Pas)** | 1.2 - 1.5 (achiziție ultra-rapidă) |
    | **Mod Scanare** | Elicoidal (Flash / Dual Source) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Achiziție caudo-cranială preferată. Canulă 18G în plica cotului. Flush salin 40-50 mL la 4.5 mL/s imediat după contrast pentru a goli vena cavă superioară și a elimina artefactele de striere.

    === "Note Asistent"

        - Verificare permeabilitate canulă venoasă cu jet rapid de ser înainte de conectarea injectorului automat.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min; la pacienți instabili hemodinamic se asigură hidratare promptă.
            - **Alergii:** Conform politicii OHSU. În suspiciune acută de TEP masiv, beneficiul este prioritar.

    === "Note Radiolog"

        - Căutați defecte de umplere parțiale sau ocluzive (semnul călărețului pe bifurcație). Evaluați semnele de suprasolicitare a ventriculului drept (raport VD/VS > 1.0, reflux de contrast în vena cavă inferioară și venele suprahepatice).

    === "Sfaturi & Recomandări"

        - Respirație: pacientul trebuie instruit să inspire ușor și să mențină apneea fără manevră Valsalva (care ar scădea întoarcerea venoasă și ar dilua contrastul în atriul drept cu sânge neopacifiat).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Pulmonar | Baza plămânilor (direcție caudo-cranială pentru a reduce artefactele de respirație la baze) | Vârfuri pulmonare | Trigger + 3-4 sec | 0.625 mm | Opacifiere densă a arterelor pulmonare principale, lobare, segmentare și subsegmentare (> 250 HU) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Pulmonar | Torace | 1.0 mm / 0.7 mm | Mediastinal (I30f) + Pulmonar (I50f) | Admire 3 / AIDR 3D | Detecție defecte de umplere endoluminale în arterele pulmonare |
    | Coronal & Sagital | Angio-CT Pulmonar | Torace | 1.5 mm / 1.5 mm | Mediastinal (I30f) | Admire 3 / AIDR 3D | Urmărire ramificații arteriale în plan anatomic |
