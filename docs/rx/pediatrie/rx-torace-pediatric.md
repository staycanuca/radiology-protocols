---
author: Departamentul de Radiologie
breathing: Expunere declanșată rapid în faza de inspir maxim (la plânsul copilului
  expunerea se face la sfârșitul inspirului profund)
category: pediatrie
centering: Nivel medio-sternal (mamelonar)
clinical_indications:
- Infecție respiratorie joasă febrilă (pneumonie, bronșiolită severă)
- Stridor acut sau suspiciune de corp străin inhalat
- Tuse cronică sau wheezing neexplicat
- Evaluare cardiomegalie congenitală
iris_reference:
  chapter: Pediatrie — Torace, pulmon, cord
  radiation_dose: Clasa 1 (Minimă < 0.02 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-15'
modality: rx
notes: Timusul normal la sugari poate mări considerabil mediastinul antero-superior;
  nu trebuie confundat cu o tumoră mediastinală sau cardiomegalie!
position: 'La sugari/copii mici: decubit dorsal pe detector (sau imobilizare cu dispozitiv
  Pigg-O-Stat în ortostatism dacă este disponibil); la copii mari: ortostatism la
  Bucky'
protection:
- Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare
  automată din template.
- Însoțitorul (părintele) echipat obligatoriu cu șorț și guler de plumb pe durata
  imobilizării
- 'Principiul ALARA strict respectat: zero repetări nejustificate'
quality_criteria:
- Simetrie a hemitoracelor (absența rotației)
- Inspir corect (minim 8-9 arcuri costale posterioare)
- Absența artefactelor de mișcare
- Recunoașterea umbrei timusului la sugar (semnul pânzei de barcă / velar — aspect
  fiziologic normal)
sid_dff: 100 - 150 cm
slug: rx-torace-pediatric
tech_params:
  aec_chambers: Manual sau AEC pediatric calibrat
  collimation: Strictă pe cutia toracică (fără abdomen)
  filtration: Suplimentară 1 mm Al + 0.1-0.2 mm Cu (filtrare suplimentară pediatrică)
  focal_spot: Focar Mic (0.6 mm)
  grid: FĂRĂ GRILĂ (reducere substanțială a dozei de iradiere la copii < 20 kg)
  kv: 60 - 70 (tehnică pediatrică adaptată)
  mas: 1.0 - 2.0 (timp de expunere ultra-scurt < 5-10 ms pentru evitarea neclarității
    cinetice)
title: Rx Torace Pediatric (Sugar & Copil)
sources:
- title: Image Gently — Pediatric Digital Radiography Protocols
  url: https://www.imagegently.org/Procedures/Digital-Radiography
  institution: Image Gently Alliance
  source_region: US
  kind: Ghid pediatric de reducere a dozei
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: ac644092c369e9d44c6a3ff568ac3cec99309230b07ba31a10fdc827ebd9e8ef
- title: Comisia Europeană (EUR 16260 / EUR 16261) — Criterii de calitate în radiologia
    pediatrică
  url: https://op.europa.eu/en/publication-detail/-/publication/d3d77212-5290-414e-8e37-27fde43b5925
  institution: Comisia Europeană
  source_region: UE
  kind: Ghid european oficial
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 25c987b787786a576863154c04db86bb8710acf0f513102efbb3b90b4131563e
---

# Rx Torace Pediatric (Sugar & Copil)

<div class="rx-meta-bar">
  <span class="rx-modality-badge">📷 Radiografie Convențională (Rx)</span>
  <span><strong>Actualizat:</strong> 2026-09-13</span>
  <span><strong>Autor:</strong> Departamentul de Radiologie</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic & Indicații__

    ---

    === "Indicații Clinice"

        - Infecție respiratorie joasă febrilă (pneumonie, bronșiolită severă)
        - Stridor acut sau suspiciune de corp străin inhalat
        - Tuse cronică sau wheezing neexplicat
        - Evaluare cardiomegalie congenitală

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie — Torace, pulmon, cord*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 1 (Minimă < 0.02 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Poziționare & Centrare Fascicul__

    ---

    - **Poziție Pacient:** La sugari/copii mici: decubit dorsal pe detector (sau imobilizare cu dispozitiv Pigg-O-Stat în ortostatism dacă este disponibil); la copii mari: ortostatism la Bucky
    - **Punct de Centrare Fascicul:** Nivel medio-sternal (mamelonar)
    - **Distanță Focar-Film (DFF / SID):** 100 - 150 cm
    - **Comandă Respiratorie:** Expunere declanșată rapid în faza de inspir maxim (la plânsul copilului expunerea se face la sfârșitul inspirului profund)

-   __3. Parametri Tehnici Expunere__

    ---

    | Parametru Tehnic | Valoare Configurare Generator / Tub |
    |:-----------------|:-------------------------------------|
    | **Tensiune Tub (kV)** | 60 - 70 (tehnică pediatrică adaptată) kV |
    | **Sarcină / Produs Curent-Timp (mAs)** | 1.0 - 2.0 (timp de expunere ultra-scurt < 5-10 ms pentru evitarea neclarității cinetice) mAs |
    | **Distanță Focar-Film (DFF / SID)** | 100 - 150 cm |
    | **Grilă Antidifuzoare (Bucky)** | FĂRĂ GRILĂ (reducere substanțială a dozei de iradiere la copii < 20 kg) |
    | **Dimensiune Focar** | Focar Mic (0.6 mm) |
    | **Camere de Ionizare AEC** | Manual sau AEC pediatric calibrat |
    | **Colimare Fascicul** | Strictă pe cutia toracică (fără abdomen) |
    | **Filtrare Tub** | Suplimentară 1 mm Al + 0.1-0.2 mm Cu (filtrare suplimentară pediatrică) |

-   __4. Criterii de Calitate & Reușită Imagine__

    ---

    - Simetrie a hemitoracelor (absența rotației)
    - Inspir corect (minim 8-9 arcuri costale posterioare)
    - Absența artefactelor de mișcare
    - Recunoașterea umbrei timusului la sugar (semnul pânzei de barcă / velar — aspect fiziologic normal)

-   __5. Protecție Radiologică (ALARA)__

    ---

    - Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.
    - Însoțitorul (părintele) echipat obligatoriu cu șorț și guler de plumb pe durata imobilizării
    - Principiul ALARA strict respectat: zero repetări nejustificate

</div>

!!! note "Observații Clinice & Tehnice"
    Timusul normal la sugari poate mări considerabil mediastinul antero-superior; nu trebuie confundat cu o tumoră mediastinală sau cardiomegalie!

=== "Ghid Rapid de Execuție"

    1. **Identificarea și verificarea pacientului:** verificare identitate, zonă de examinat, consimțământ conform procedurii și evaluarea posibilității unei sarcini, când este relevantă.
    2. **Pregătire:** îndepărtarea oricăror obiecte radiopace (bijuterii, agrafe, fermoare, proteze, pansamente dense).
    3. **Poziționare precisă:** alinierea receptorului de imagine și a tubului la distanța prescrisă (100 - 150 cm).
    4. **Colimare strictă:** adaptarea fasciculului strict la regiunea de diagnostic pentru scăderea iradierii și reducerea radiației difuze.
    5. **Radioprotecție:** verificarea [politicii RX](../radioprotectie.md), cu măsuri distincte pentru pacient, personal și însoțitor.

## Surse și revizuire

- [Image Gently — Pediatric Digital Radiography Protocols](https://www.imagegently.org/Procedures/Digital-Radiography) — *Image Gently Alliance* (US)
- [Comisia Europeană (EUR 16260 / EUR 16261) — Criterii de calitate în radiologia pediatrică](https://op.europa.eu/en/publication-detail/-/publication/d3d77212-5290-414e-8e37-27fde43b5925) — *Comisia Europeană* (UE)
