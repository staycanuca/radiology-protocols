---
acquisition_steps:
- description: 'Examinare în incidență laterală a gâtului: se evaluează faza orală
    pregătitoare, motilitatea bazei limbii, elevarea laringelui, deschiderea sfincterului
    esofagian superior (mușchiul cricofaringian) și excluderea oricărei penetrări
    sau aspirații în laringe.'
  phase: Faza Orofaringiană & Actul Deglutiției
- description: 'Pacientul în OAD 35-40°: se observă unda peristaltică primară declanșată
    de deglutiție care propulsează bolusul către stomac; se evaluează undele secundare
    și eventualele contracții terțiare non-propulsive (esofag în tirbușon / presbiesofag).'
  phase: Corp Esofagian & Unde Peristaltice (OAD)
- description: Analiza deschiderii sfincterului esofagian inferior (SEI) și a vestibulului
    gastro-esofagian; se verifică simetria și suplețea ampulei epifrenice și poziția
    liniei Z.
  phase: Joncțiunea Esofago-Gastrică & Cardia
- description: După trecerea bolusului principal, se fac clisee centrate cu timp scurt
    de expunere pentru vizualizarea reliefului fin mucosal (pliuri longitudinale paralele,
    regulate, sub 2-3 mm grosime).
  phase: Fază Mucosală (Dublu Contrast)
- description: Trecerea mesei în poziție orizontală și Trendelenburg ușor; pacientul
    efectuează manevra Valsalva pentru evidențierea refluxului gastro-esofagian acid
    sau a unei hernii hiatale intermitente prin alunecare.
  phase: Clinostatism & Manevra Valsalva / Efort Tuse
author: Departamentul de Radiologie și Imagistică Medicală
category: digestiv
clinical_indications:
- Disfagie orofaringiană sau esofagiană (dificultate la deglutiție solidă/lichidă)
- Suspiciune de acalazie cardiei sau tulburări de motilitate esofagiană (spasm difuz
  esofagian)
- Diverticul faringo-esofagian Zenker, diverticuli epibronșici sau epifrenici
- Reflux gastro-esofagian sever, esofagită peptică și suspiciune de esofag Barrett
- Stenoze esofagiene post-caustice, post-radice sau benigne peptice
- Suspiciune de neoplasm esofagian (evaluare lungime și localizare stenoză)
- Evaluare post-operatorie a anastomozelor esofagiene (după confirmare preliminară
  cu contrast hidrosolubil)
contraindications:
- Suspiciune certă de perforație esofagiană acută sau fistulă eso-traheală/bronșică
  (CONTRAINDICAȚIE ABSOLUTĂ pentru Sulfatul de Bariu; se folosește exclusiv contrast
  iodat hidrosolubil non-ionic izoosmolar din cauza riscului de mediastinită baritată
  fatală sau baritoză pulmonară)
- Tulburări majore de deglutiție cu risc iminent de aspirație masivă traheo-bronșică
- Stare comatoasă sau pacient necooperant fără protezare a căilor aeriene
contrast:
  agent: Sulfat de Bariu suspensie de înaltă densitate (200-250% w/v) pentru dublu
    contrast mucosal SAU suspensie 100-120% w/v pentru examinare clasică în plin contrast;
    Dacă există suspiciune de perforație se administrează contrast hidrosolubil non-ionic
    (Omnipaque 300 / Iopamiro 300)
  instructions: Pacientul ia o gură mare de bariu, o menține în cavitatea bucală și
    înghite exclusiv la comanda sonoră, sub monitorizare fluoroscopică continuă a
    bolusului
  route: Orală (per os), înghițire voluntară la comanda medicului radiolog
  volume: 100 - 200 ml suspensie baritată
fluoro_params:
  filtration: Totală ≥ 3.0 mm Al + 0.1 mm Cu
  grid: Cu grilă antidifuzoare
  kv: 90 - 105 kV (dublu contrast) / 110 - 120 kV (plin contrast baritat)
  lih: Activ permanent
  ma_range: 1.0 - 3.5 mA (AEC automat)
  mode: Fluoroscopie Pulsată Joasă (7.5 - 15 fps) cu Last Image Hold (LIH)
  target_fluoro_time: < 2.5 minute timp total scopie
iris_reference:
  chapter: Tub Digestiv & Esofag
  radiation_dose: Clasa 2 (Medie 1 - 5 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: fluoro
notes: Dacă la debutul examinării pacientul relatează disfagie acută bruscă cu suspiciune
  de corp străin blocat (os, bol alimentar), NU se va administra masă baritată densă;
  se începe cu o înghițitură mică de contrast hidrosolubil sau se orientează direct
  către endoscopie digestivă de urgență.
patient_prep: À jeun (pe nemâncate) cu minim 6 ore anterior procedurii (evită vărsăturile
  și refluxul alimentar în timpul deglutiției); îndepărtarea protezelor dentare mobile,
  a lănțișoarelor și a hainelor cu nasturi metalici.
positioning_equipment:
  equipment_setup: Masă basculantă telecomandată 90°/15° cu amplificator de imagine
    / detector plat digital (FPD); distanță focar-receptor ≥ 100 cm
  patient_position: Ortostatism în Oblic Anterior Drept (OAD 35-40°) pentru derularea
    optimă a esofagului între coloana vertebrală și cord; completat cu incidență profil
    și clinostatism
  sid: 100 - 115 cm
quality_criteria:
- Opacifiere completă și continuă de la hipofaringe până la fornixul gastric
- Derularea anatomică a esofagului fără suprapunere pe coloana toracală sau cord
- Demonstrarea clară a reliefului mucosal parietal fără artefacte de deglutiție dublă
- Documentarea exactă a peristalticii și a tranzitului în timp real
radiation_safety:
- Colimare dinamică strânsă pe axul vertical al esofagului (lățime fascicul < 8-10
  cm)
- Folosirea obligatorie a modului pulsat la 7.5 fps în loc de scopie continuă (reduce
  doza cu 50%)
- Timp total de fluoroscopie monitorizat strict, menținut sub 2 - 2.5 minute
- DAP (Dose Area Product) de referință < 10 Gy·cm²
- Șorț de plumb pe pelvisul pacientului pe parcursul întregii examinări
slug: tranzit-esofagian
title: Tranzit Baritat Esofagian (Esofagoscopie Radiologică)
sources:
- title: ACR-SAR-SPR Practice Parameter for the Performance of Gastrointestinal Fluoroscopy
    in Adults
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf
  institution: ACR / SAR / SPR
  source_region: US
  kind: Standard de practică fluoroscopie digestivă
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 45621b1990b6eabf74f9996a8a9c707b6d18590d018367baf4fe51409a0450b0
- title: UT Southwestern Radiology — Diagnostic Fluoroscopy Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/diagnostic.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional fluoroscopie
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 4d9de4a012f12a5d0ac28d46131bf9ab7e4668e6fae1937eaf76d68167f9290d
position: Ortostatism în Oblic Anterior Drept (OAD 35-40°) pentru derularea optimă
  a esofagului între coloana vertebrală și cord; completat cu incidență profil și
  clinostatism
---

# Tranzit Baritat Esofagian (Esofagoscopie Radiologică)

<div class="fluoro-meta-bar">
  <span class="fluoro-modality-badge">✨ Fluoroscopie & C-Arm</span>
  <span><strong>Actualizat:</strong> 2026-09-13</span>
  <span><strong>Autor:</strong> Departamentul de Radiologie și Imagistică Medicală</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații__

    ---

    === "Indicații Clinice"

        - Disfagie orofaringiană sau esofagiană (dificultate la deglutiție solidă/lichidă)
        - Suspiciune de acalazie cardiei sau tulburări de motilitate esofagiană (spasm difuz esofagian)
        - Diverticul faringo-esofagian Zenker, diverticuli epibronșici sau epifrenici
        - Reflux gastro-esofagian sever, esofagită peptică și suspiciune de esofag Barrett
        - Stenoze esofagiene post-caustice, post-radice sau benigne peptice
        - Suspiciune de neoplasm esofagian (evaluare lungime și localizare stenoză)
        - Evaluare post-operatorie a anastomozelor esofagiene (după confirmare preliminară cu contrast hidrosolubil)

    === "Contraindicații & Atenționări"

        - Suspiciune certă de perforație esofagiană acută sau fistulă eso-traheală/bronșică (CONTRAINDICAȚIE ABSOLUTĂ pentru Sulfatul de Bariu; se folosește exclusiv contrast iodat hidrosolubil non-ionic izoosmolar din cauza riscului de mediastinită baritată fatală sau baritoză pulmonară)
        - Tulburări majore de deglutiție cu risc iminent de aspirație masivă traheo-bronșică
        - Stare comatoasă sau pacient necooperant fără protezare a căilor aeriene

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Tub Digestiv & Esofag*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Medie 1 - 5 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Substanță de Contrast__

    ---

    - **Pregătire Prealabilă:** À jeun (pe nemâncate) cu minim 6 ore anterior procedurii (evită vărsăturile și refluxul alimentar în timpul deglutiției); îndepărtarea protezelor dentare mobile, a lănțișoarelor și a hainelor cu nasturi metalici.
    - **Agent de Contrast:** Sulfat de Bariu suspensie de înaltă densitate (200-250% w/v) pentru dublu contrast mucosal SAU suspensie 100-120% w/v pentru examinare clasică în plin contrast; Dacă există suspiciune de perforație se administrează contrast hidrosolubil non-ionic (Omnipaque 300 / Iopamiro 300)
    - **Cale de Administrare:** Orală (per os), înghițire voluntară la comanda medicului radiolog
    - **Volum & Diluție:** 100 - 200 ml suspensie baritată
    - **Instrucțiuni Specifice:** Pacientul ia o gură mare de bariu, o menține în cavitatea bucală și înghite exclusiv la comanda sonoră, sub monitorizare fluoroscopică continuă a bolusului

-   __3. Poziționare & Configurare Echipament (Masă / C-Arm)__

    ---

    - **Poziție Inițială Pacient:** Ortostatism în Oblic Anterior Drept (OAD 35-40°) pentru derularea optimă a esofagului între coloana vertebrală și cord; completat cu incidență profil și clinostatism
    - **Configurare Braț C / Echipament:** Masă basculantă telecomandată 90°/15° cu amplificator de imagine / detector plat digital (FPD); distanță focar-receptor ≥ 100 cm
    - **Distanță Focar-Receptor:** 100 - 115 cm

-   __4. Parametri Tehnici Scopie & Expunere__

    ---

    | Parametru Tehnic Scopie & Grafie | Valoare Configurare Generator / Arc C |
    |:---------------------------------|:---------------------------------------|
    | **Regim Fluoroscopie** | Fluoroscopie Pulsată Joasă (7.5 - 15 fps) cu Last Image Hold (LIH) |
    | **Tensiune Tub (kV)** | 90 - 105 kV (dublu contrast) / 110 - 120 kV (plin contrast baritat) kV |
    | **Curent Tub Scopie (mA)** | 1.0 - 3.5 mA (AEC automat) |
    | **Distanță Focar-Receptor (SID)** | 100 - 115 cm (detector cât mai aproape de pacient) |
    | **Grilă Antidifuzoare** | Cu grilă antidifuzoare |
    | **Filtrare Suplimentară** | Totală ≥ 3.0 mm Al + 0.1 mm Cu |
    | **Timp Țintă Scopie** | < 2.5 minute timp total scopie |
    | **Last Image Hold (LIH)** | Activ permanent |

-   __5. Secvență Achiziție & Incidențe Seriate__

    ---

    - **Faza Orofaringiană & Actul Deglutiției:** Examinare în incidență laterală a gâtului: se evaluează faza orală pregătitoare, motilitatea bazei limbii, elevarea laringelui, deschiderea sfincterului esofagian superior (mușchiul cricofaringian) și excluderea oricărei penetrări sau aspirații în laringe.
    - **Corp Esofagian & Unde Peristaltice (OAD):** Pacientul în OAD 35-40°: se observă unda peristaltică primară declanșată de deglutiție care propulsează bolusul către stomac; se evaluează undele secundare și eventualele contracții terțiare non-propulsive (esofag în tirbușon / presbiesofag).
    - **Joncțiunea Esofago-Gastrică & Cardia:** Analiza deschiderii sfincterului esofagian inferior (SEI) și a vestibulului gastro-esofagian; se verifică simetria și suplețea ampulei epifrenice și poziția liniei Z.
    - **Fază Mucosală (Dublu Contrast):** După trecerea bolusului principal, se fac clisee centrate cu timp scurt de expunere pentru vizualizarea reliefului fin mucosal (pliuri longitudinale paralele, regulate, sub 2-3 mm grosime).
    - **Clinostatism & Manevra Valsalva / Efort Tuse:** Trecerea mesei în poziție orizontală și Trendelenburg ușor; pacientul efectuează manevra Valsalva pentru evidențierea refluxului gastro-esofagian acid sau a unei hernii hiatale intermitente prin alunecare.

-   __6. Criterii de Calitate & Diagnostic__

    ---

    - Opacifiere completă și continuă de la hipofaringe până la fornixul gastric
    - Derularea anatomică a esofagului fără suprapunere pe coloana toracală sau cord
    - Demonstrarea clară a reliefului mucosal parietal fără artefacte de deglutiție dublă
    - Documentarea exactă a peristalticii și a tranzitului în timp real

-   __7. Radioprotecție & Dozimetrie (ALARA)__

    ---

    - Colimare dinamică strânsă pe axul vertical al esofagului (lățime fascicul < 8-10 cm)
    - Folosirea obligatorie a modului pulsat la 7.5 fps în loc de scopie continuă (reduce doza cu 50%)
    - Timp total de fluoroscopie monitorizat strict, menținut sub 2 - 2.5 minute
    - DAP (Dose Area Product) de referință < 10 Gy·cm²
    - Șorț de plumb pe pelvisul pacientului pe parcursul întregii examinări

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Dacă la debutul examinării pacientul relatează disfagie acută bruscă cu suspiciune de corp străin blocat (os, bol alimentar), NU se va administra masă baritată densă; se începe cu o înghițitură mică de contrast hidrosolubil sau se orientează direct către endoscopie digestivă de urgență.

=== "Ghid Rapid de Execuție & Siguranță Fluoroscopică"

    1. **Pregătire și Informare:** Verificarea identității pacientului, a indicației clinice, a excluderii sarcinii la paciente fertile și informarea privind substanța de contrast.
    2. **Configurare Echipament:** La C-Arm mobil, tubul se poziționează OBLIGATORIU sub masa operatorie, iar detectorul plat cât mai aproape de pacient pentru minimalizarea radiației difuze către operator.
    3. **Optimizare Doză (ALARA):** Se utilizează regim de fluoroscopie pulsată (4 - 7.5 - 15 fps) în locul modului continuu și colimare strânsă strict pe zona de interes.
    4. **Last Image Hold (LIH):** Utilizarea imaginii înghețate pe monitor pentru decizii operatorii sau analize anatomice, fără reactivarea inutilă a pedalei de expunere.
    5. **Protecție Personal:** Toți membrii echipei prezenți în sală poartă echipament individual de protecție din plumb (șorț echivalent 0.35-0.5 mm Pb, guler tiroidian, ochelari plumbuiți) și păstrează o distanță maximă posibilă față de tub conform legii pătratului invers al distanței.

## Surse și revizuire

- [ACR-SAR-SPR Practice Parameter for the Performance of Gastrointestinal Fluoroscopy in Adults](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf) — *ACR / SAR / SPR* (US)
- [UT Southwestern Radiology — Diagnostic Fluoroscopy Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/diagnostic.html) — *UT Southwestern* (US)
