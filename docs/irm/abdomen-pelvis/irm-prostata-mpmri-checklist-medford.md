---
author: Medford Radiology Group (MRG) / Clinical MRI Quality Committee
category: abdomen-pelvis
clinical_indications:
- Evaluare cancer de prostată și stadializare conform scorului PI-RADS v2.1
- Supraveghere activă a pacienților diagnosticați cu neoplasm de prostată
- Evaluare PSA persistent crescut sau biopsii transrectale anterioare negative cu suspiciune clinică înaltă
- Planificare biopsie fuziune RMN-Ecografie sau planificare radioterapie/prostatectomie
coils_hardware:
  coil: Antenă pelvic phased-array multicanal de suprafață (16-32 canale)
  field_strength: Scaner 3.0 Tesla preferențial (sau 1.5 Tesla validat MRG cu tehnici MAR în caz de artroplastii)
  positioning: Decubit dorsal, centrare 2 cm deasupra simfizei pubiene
contraindications:
- Dispozitive medicale implantabile incompatibile cu RM
- Artroplastii bilaterale de șold din material feromagnetic (dacă produc artefacte care distrug semnalul pe DWI)
contrast:
  agent: Chelat de Gadoliniu macrociclic (ex. Gadobutrol 0.1 mmol/kg sau Gadoterat de meglumină)
  dose: 0.1 mmol/kg corp (0.1 mL/kg pentru formulările 1.0M)
  flow_rate: 2.5 - 3.0 mL/s cu injector automat urmat de flush salin de 30 mL
  notes: Achiziție dinamică rapidă DCE (Dynamic Contrast Enhancement) la rezoluție temporală < 10 secunde timp de minimum 2-3 minute
  timing: Declanșare sincronă cu bolusul de contrast
iris_reference:
  chapter: Urologie & Oncologie - Neoplasm Prostatic
  radiation_dose: Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)
  recommendation_grade: Grad A
last_updated: '2026-09-27'
modality: irm
notes:
  additional_recons: Seria b=1400 s/mm² este exportată separat ca serie dedicată în PACS.
    Transmitere obligatorie a seriilor DCE către platforma DynaCAD pentru curbe farmacocinetice.
  nursing: Verificare conformitate pregătire digestivă (Fleet enema). Canulă 20G în plica cotului.
    Administrare antispastic (Buscopan 20 mg IV / Glucagon 1 mg) înainte de secvențele T2/DWI pentru inhibarea peristaltismului rectosigmoidian.
  rad: Evaluare multiparametrică conform PI-RADS v2.1. Categoriile PI-RADS 4 și 5 impun biopsie
    țintită. Confirmarea absenței artefactelor hemoragice post-biopsie (respectarea intervalului >6 săptămâni).
  tech: 'Regulă de aur MRG: toate secvențele cu FOV mic (T2 axial oblic, DWI/ADC, post-gadoliniu)
    trebuie să aibă planuri, grosimi și coordonate riguros copiate, astfel încât imaginile
    să poată fi parcurse sincronizat în PACS (cross-referencing).'
  tips: 'Calitate DWI: dacă se observă distorsiuni cauzate de gaz rectal, pacientul este invitat
    să evacueze rectul, iar secvența se reia. Atenție MRG: dacă se reia DWI/ADC din cauza mișcării,
    trebuie obligatoriu repetate și secvențele T2 small FOV în toate cele 3 planuri!'
patient_prep: 'Protocol MRG Enema: Fleet Saline Enema (cu o seară înainte dacă examinarea este
  înainte de ora 12:00; în dimineața examinării dacă este după ora 13:00). Regim de lichide
  clare exclusiv cu 12 ore înainte de sosire. Repaus alimentar solid 4-6 ore.'
protocol_type: contrast-enhanced
quality_criteria:
- Respectarea intervalului de cel puțin 6 săptămâni post-biopsie prostatică
- Supresie omogenă a grăsimii pe întreaga glandă prostatică pe secvențele fat-sat
- Valoare b înaltă (b=1400 s/mm²) calculată sau achiziționată direct
- Coordonate geometrice identice copiate între T2, DWI și DCE
safety_considerations:
- Protocol de verificare eGFR conform MRG Contrast Administration Guideline (valabilitate 30z ambulator, 48h spitalizați)
- Verificare atentă a compatibilității RM pentru orice implant pelvin
sequences:
- fat_sat: Nu
  fov_matrix: FOV 180 - 200 mm / matrice 320 × 256
  name: T2 TSE Axial Oblic (Small FOV)
  notes: Unghi perpendicular pe axul lung al uretrei prostatice; acoperire de la baza veziculelor seminale până la apex
  plane: Axial oblic
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4000 - 5500 ms / TE 100 - 115 ms
- fat_sat: Nu
  fov_matrix: FOV 180 - 200 mm / matrice 320 × 256
  name: T2 TSE Sagital & Coronal Oblic (Small FOV)
  notes: Sagital pe linia mediană a uretrei; Coronal oblic paralel cu axul uretrei
  plane: Sagital & Coronal oblic
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4000 - 5000 ms / TE 100 - 110 ms
- fat_sat: Da (SPAIR / FatSat)
  fov_matrix: FOV 180 - 200 mm / matrice 128 × 128 (reconstruită 256)
  name: DWI / ADC (Difuzie Axial Oblic - b50, b800, b1400)
  notes: Copiere identică a geometriei după T2 Axial Oblic. Export serie dedicată b=1400 în PACS.
  plane: Axial oblic
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4500 - 6000 ms / TE minim (60-75 ms)
- fat_sat: Da
  fov_matrix: FOV 240 - 260 mm / matrice 256 × 256
  name: T1 TSE Axial Large FOV
  notes: Evaluare ganglioni limfatici obturatori și iliaci, metastaze osoase și focare hemoragice intraprostatice (hipersemnal T1)
  plane: Axial
  slice_gap: 4.0 mm / gap 0.5 mm
  tr_te: TR 600 - 750 ms / TE 10 - 15 ms
- fat_sat: Da (3D T1 cu supresie de grăsime)
  fov_matrix: FOV 180 - 200 mm / matrice 256 × 256
  name: DCE Dinamic Post-Gadoliniu (DynaCAD)
  notes: Rezoluție temporală sub 10s pe fază; copiere identică a geometriei T2 Small FOV
  plane: Axial oblic
  slice_gap: 3.0 mm / gap 0 mm
  tr_te: TR 4 - 6 ms / TE 1.5 - 2.5 ms
sources:
- edition: '2023'
  locator: Prostate MRI Checklist & Imaging Preps
  title: Medford Radiology Group MRI Support Documents
  url: https://medfordradiology.com/mri/
- edition: '2023'
  locator: MRG Prostate MRI Checklist Facility Guideline
  title: Medford Radiology Group
  url: https://medfordradiology.com/wp-content/uploads/2017/06/MRI-Prostate-Checklist-1.2017.pdf
title: Protocol & Checklist de Calitate IRM Prostată mpMRI (Medford Radiology Group)
---

# Protocol & Checklist de Calitate IRM Prostată mpMRI (Medford Radiology Group)

**Ultima actualizare:** 2026-09-27  
**Autori:** Medford Radiology Group (MRG) / Clinical MRI Quality Committee  

---

<div class="grid cards" markdown>

-   __1. Rezumat Protocol Tehnic mpMRI__

    ---

    === "Pachete Secvențe Cheie"

        | Secvență | Plan / Geometrie | Grosime / Gap | Parametri Esențiali |
        |:---|:---|:---|:---|
        | **T2 TSE Small FOV** | Axial Oblic (perpendicular pe uretră) | 3.0 mm / gap 0 | FOV 180 mm, rezoluție spațială sub-milimetrică |
        | **T2 TSE Sagital & Coronal** | Sagital & Coronal Oblic | 3.0 mm / gap 0 | Apex, bază, invazie vezicule seminale |
        | **DWI / ADC (b=50, 800, 1400)** | Axial Oblic (geometrie copiată din T2) | 3.0 mm / gap 0 | Serie dedicată b=1400 s/mm² în PACS |
        | **T1 TSE Large FOV** | Axial Pelvis | 4.0 mm / gap 0.5 | Hemoragii post-biopsie, noduli limfatici |
        | **DCE Dinamic (DynaCAD)** | Axial Oblic (geometrie copiată din T2) | 3.0 mm / gap 0 | Rezoluție temporală < 10 secunde, 2-3 minute |

    === "Indicații Clinice"

        - Suspiciune înaltă de adenocarcinom prostatic (PSA crescut, raport PSA liber/total scăzut, tușeu rectal suspect)
        - Cartografiere lezională și ghidare pentru puncție biopsie de fuziune RMN-Ecografie (Fusion Biopsy)
        - Stadializare loco-regională a cancerului confirmat (depășire capsulară ECE, invazie vezicule seminale)
        - Monitorizare activă a tumorilor cu risc scăzut (Active Surveillance)
        - Recidivă biochimică post-prostatectomie radicală sau post-radioterapie

    === "Ghid Național IRIS"

        !!! info "Referință Ghid Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol:** *Urologie & Oncologie - Neoplasm Prostatic*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary }

-   __2. Pregătire Pacient (MRG Bowel Prep Protocol)__

    ---

    - **Fleet Saline Enema (Clismă Evacuatorie Salină):**
        - *Programare Dimineața (înainte de ora 12:00):* Autoadministrare clismă Fleet în seara precedentă examinării.
        - *Programare După-amiaza (ora 13:00 sau mai târziu):* Autoadministrare clismă Fleet în dimineața examinării.
    - **Regim Alimentar:** Exclusiv lichide clare timp de **12 ore** înainte de sosirea în serviciul de imagistică.
    - **Prevenirea Artefactelor:** Administrare Buscopan 20 mg IV sau Glucagon 1 mg SC/IV imediat înainte de așezarea pacientului pe masa de scanare pentru a suprima peristaltismul rectosigmoidian.

</div>

---

## Checklist Instituțional de Calitate MRG (Prostate MRI Quality Checklist)

Medford Radiology Group impune tehnicienilor și medicilor radiologi verificarea obligatorie a următorilor 12 parametri înainte de finalizarea și validarea examinării:

```mermaid
flowchart TD
    Q1["1. S-au scurs > 6 săptămâni de la orice biopsie prostatică anterioară?"] --> Q2["2. S-a efectuat pregătirea rectală (Fleet Enema + 12h lichide clare)?"]
    Q2 --> Q3["3. Sunt atașate în PACS ultimele note clinice urologice și buletinele histopatologice anterioare?"]
    Q3 --> Q4["4. Scanarea este efectuată pe aparat 3.0 Tesla?<br/>(Dacă 1.5T: există aprobare MRG și secvențe MAR active?)"]
    Q4 --> Q5["5. Supresia de grăsime pe prostată este complet omogenă pe secvențele FatSat și DCE?"]
    Q5 --> Q6["6. Toate secvențele Small FOV (T2, DWI/ADC, DCE) au planul, grosimea și unghiul identic copiate?"]
    Q6 --> Q7["7. Imaginile DWI cu b=1400 s/mm² sunt transmise ca serie separată în PACS?"]
    Q7 --> Q8["8. Seria DCE dinamică a fost transmisă către DynaCAD pentru calculul curbelor kinetice?"]
```

### Detalierea Punctelor din Checklist-ul MRG

1. **Intervalul Post-Biopsie (> 6 Săptămâni):**
    - Puncția biopsie prostatică produce micro-hematoame intraglandulare și periprostatice. Methemoglobina produce hipersemnal T1 și hiposemnal marcat pe T2/DWI/ADC prin artefact de susceptibilitate magnetică, simulând sau mascând adenocarcinoamele semnificative clinic.
    - Dacă pacientul a suferit o biopsie recentă (< 6 săptămâni), examinarea se reprogramează, cu excepția cazurilor oncologice urgente agreate direct de medicul radiolog.
2. **Sincronizarea Geometrică a Imaginilor (Exact Parameter Copying):**
    - Pentru a permite citirea sincronă ("cross-referencing") în PACS, toate secvențele small-FOV (T2 axial oblic, DWI b50/800/1400, harta ADC și dinamica DCE) **trebuie să aibă parametri identici de poziție, unghi, grosime de secțiune (3.0 mm) și interval (gap 0)**.
3. **Verificarea Calității Secvențelor DWI & Conduita în caz de Artefacte:**
    - Se examinează imediat calitatea imaginilor de difuzie la consola aparatului înainte de injectarea contrastului.
    - *Artefact de aer rectal / distorsiune EPI:* Dacă gazul rectal deformează conturul posterior al prostatei, pacientul este dat jos de pe masă și invitat să elimine gazele/materiile la toaletă, după care se rescanază. Se poate schimba de asemenea direcția de codare a fazei (Phase Encoding).
    - **Regulă Majoră MRG:** Dacă secvența DWI/ADC trebuie repetată din cauza mișcării pacientului sau a gazelor rectale, **se vor repeta OBLIGATORIU și toate secvențele T2 Small FOV în cele 3 planuri**, pentru a menține alinierea spațială perfectă între anatomie și difuzie!
4. **Exportul Separat al Seriei b = 1400 s/mm²:**
    - Seria cu valoare b mare (b=1400) evidențiază hipersemnalul nodulilor tumorali maligni denși celulari cu restricție netă de difuzie în zona periferică (PZ). Ea trebuie trimisă ca serie de sine stătătoare în PACS, independent de b50 și b800.
5. **Integrarea DynaCAD:**
    - Datele DCE de perfuzie sunt încărcate în software-ul dedicat DynaCAD pentru trasarea curbelor de captare și spălare rapidă a contrastului (Tip III Washout = suspiciune crescută de malignitate).
