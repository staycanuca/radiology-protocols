"""generate_rx_protocols.py — Generează protocoalele standard de Radiologie Clasică (Rx) și structura docs/rx/.
"""

import os
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from render_rx_protocol import render_rx_document

DOCS_RX = REPO_ROOT / "docs" / "rx"

RX_PROTOCOLS = [
    # 1. Torace
    {
        "title": "Rx Torace PA (Postero-Anterior)",
        "slug": "rx-torace-pa",
        "modality": "rx",
        "category": "torace",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Suspiciune infecție respiratorie joasă (pneumonie, bronhopneumonie)",
            "Dispnee acută sau cronică neclară",
            "Bilanț inițial hemoptizie sau tuse persistentă (> 3 săptămâni)",
            "Suspiciune revărsat pleural sau pneumotorax (în ortostatism)",
            "Evaluare cardiomegalie și congestie vasculară pulmonară",
            "Traumatism toracic minor fără criterii de politraumă",
        ],
        "position": "Ortostatism cu fața anterioară a toracelui lipită de stativul Bucky vertical, mâinile pe șolduri, umerii împinși înainte pentru degajarea omoplaților",
        "sid_dff": "180 cm (reducerea magnificării siluetei cardiace)",
        "centering": "Linia mediană posterioară, la nivelul unghiului inferior al omoplaților (T7)",
        "breathing": "Apnee în inspir profund susținut (după a doua inspirație)",
        "tech_params": {
            "kv": "120 - 125",
            "mas": "1.5 - 3 (AEC)",
            "grid": "Cu grilă antidifuzoare Bucky (raport 10:1 sau 12:1)",
            "focal_spot": "Focar Mare (1.0 - 1.2 mm)",
            "aec_chambers": "Camerele laterale (dreapta și stânga) activate",
            "collimation": "Superior la nivelul cartilajului tiroidian; inferior sub arcurile costale inferioare",
            "filtration": "Totală ≥ 2.5 mm Al echivalent",
        },
        "quality_criteria": [
            "Vizualizarea completă a câmpurilor pulmonare: de la apexuri până la unghiurile costodiafragmatice",
            "Inspir adecvat: minim 9-10 arcuri costale posterioare vizibile deasupra cupolelor diafragmatice",
            "Absența rotației: capetele mediale ale claviculelor sunt echidistante față de apofizele spinoase",
            "Omoplații sunt proiectați complet în afara ariei pulmonare",
            "Penetrare optimă: conturul coloanei toracale și al vaselor retrocardiace sunt perceptibile",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare strictă conform principiului ALARA",
            "Evaluarea posibilității unei sarcini se documentează conform procedurii locale și examinării solicitate.",
        ],
        "iris_reference": {
            "chapter": "Torace & Pulmon",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.05 mSv)",
        },
        "notes": "În suspiciune de pneumotorax mic sau corp străin bronșic, se poate solicita suplimentar un clișeu în expir forțat.",
    },
    {
        "title": "Rx Torace Profil (Lateral Stâng)",
        "slug": "rx-torace-lateral",
        "modality": "rx",
        "category": "torace",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Completare la Rx Torace PA pentru localizarea leziunilor mediastinale sau retrocardiace",
            "Evaluarea spațiului retrosternal și retrocardiac",
            "Confirmarea revărsatului pleural cantitate mică în recesul posterior",
            "Suspiciune nodul sau formațiune mascată de silueta cardiacă pe PA",
        ],
        "position": "Ortostatism cu hemitracele stâng lipit de stativul Bucky (profil stâng standard), brațele ridicate deasupra capului sau încrucișate pe creștet",
        "sid_dff": "180 cm",
        "centering": "Planul medio-axilar, la nivelul T7 (la 3-4 degete sub unghiul inferior scapular)",
        "breathing": "Apnee în inspir profund complet",
        "tech_params": {
            "kv": "125 - 130",
            "mas": "4 - 8 (AEC)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mare (1.2 mm)",
            "aec_chambers": "Camera centrală de ionizare activată",
            "collimation": "Inclusiv coloana toracală posterior și peretele toracic anterior",
            "filtration": "Totală ≥ 2.5 mm Al echivalent",
        },
        "quality_criteria": [
            "Suprapunerea precisă a arcurilor costale posterioare (rotație minimă < 1 cm)",
            "Vizualizarea clară a recesurilor costodiafragmatice posterioare",
            "Brațele sunt complet ridicate, fără artefacte peste apexurile pulmonare",
            "Penetrare clară a spațiului retrosternal și retrocardiac",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template. montat conform ALARA",
            "Colimare precisă anterior și posterior",
        ],
        "iris_reference": {
            "chapter": "Torace & Pulmon",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.1 mSv)",
        },
        "notes": "Profilul stâng este preferat deoarece reduce magnificarea cardiacă și permite vizualizarea optimă a ventriculului stâng și aortei descendente.",
    },
    {
        "title": "Rx Torace la Pat / Decubit (AP)",
        "slug": "rx-torace-la-pat-ap",
        "modality": "rx",
        "category": "torace",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Pacient nedeplasabil, critic, intubat sau monitorizat în Terapie Intensivă (ATI)",
            "Control poziție cateter venos central (CVC), tub de dren toracic, sondă intubație IOT",
            "Evaluare rapidă edem pulmonar acut, pneumotorax sub tensiune sau atelectazie la pat",
            "Monitorizare postoperatorie toracică / cardiacă",
        ],
        "position": "Decubit dorsal sau semi-șezând (Fowler) la pat, caseta/detectorul digital plasat posterior în spatele toracelui",
        "sid_dff": "100 - 120 cm (adaptat la distanța aparatului mobil)",
        "centering": "Nivel medio-sternal, perpendicular pe detector (sau ușor angulat caudal 5° dacă pacientul este semi-șezând)",
        "breathing": "Apnee la sfârșitul inspirului (sincronizat cu ventilatorul mecanic la pacientul intubat)",
        "tech_params": {
            "kv": "85 - 95 (fără grilă mobilă) sau 110 (cu grilă mobilă)",
            "mas": "2.5 - 5",
            "grid": "Opțional grilă mobilă (sau procesare software anti-scatter / gridless)",
            "focal_spot": "Focar Mic sau Mare",
            "aec_chambers": "Mod manual / expunere pre-calibrată",
            "collimation": "Strictă la marginile toracelui",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Vârful sondei IOT la 3-5 cm deasupra carinei",
            "Traiectul CVC vizualizat la joncțiunea venă cavă superioară / atriu drept",
            "Includerea completă a ambelor hemidiafragme și a unghiurilor costofrenice",
            "Notarea obligatorie pe imagine a incidenței AP la pat și a poziției (șezând/decubit)",
        ],
        "protection": [
            "Distanțare de siguranță a personalului medical la minim 2 metri în timpul expunerii",
            "Șorțuri de plumb pentru personalul prezent în salonul ATI",
        ],
        "iris_reference": {
            "chapter": "Torace & Pulmon",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 1 (Minimă < 0.08 mSv)",
        },
        "notes": "Silueta cardiacă apare mărită dimensional în proiecția AP față de PA standard din cauza divergenței fasciculului; nu se măsoară indexul cardiotoracic pe AP.",
    },
    {
        "title": "Rx Grilaj Costal / Hemitorace",
        "slug": "rx-grilaj-costal",
        "modality": "rx",
        "category": "torace",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatism toracic închis cu durere localizată și suspiciune de fractură costală",
            "Suspiciune volet costal (fracturi costale etajate pe multiple arcuri)",
            "Evaluare leziuni litice sau metastaze costale",
        ],
        "position": "Ortostatism sau decubit; incidență AP/PA centrată pe hemitoracele afectat + incidență oblică la 45° pentru desfășurarea arcurilor costale laterale",
        "sid_dff": "100 - 115 cm",
        "centering": "Punctul de maximă durere / jumătatea hemitoracelui examinat",
        "breathing": "Inspir profund pentru coastele superioare (1-9); expir complet pentru coastele inferioare (10-12 subdiafragmatice)",
        "tech_params": {
            "kv": "65 - 75 (optimizat pentru contrast osos fin)",
            "mas": "10 - 20 (cu grilă Bucky)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Camera de ionizare homolaterală",
            "collimation": "Centrată strict pe hemitoracele traumatizat",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Vizualizarea clară a continuității corticalei osoase a arcurilor costale",
            "Desfășurarea fără suprapunere a porțiunilor axilare pe incidența oblică",
            "Vizibilitatea pleurei adiacente pentru excluderea unui pneumotorax sau revărsat asociat",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare strictă unilaterală (nu se expune inutil hemitoracele sănătos)",
        ],
        "iris_reference": {
            "chapter": "Traumatisme & Torace",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 1 (Minimă < 0.2 mSv)",
        },
        "notes": "Orice suspiciune de fracturi costale multiple cu detresă respiratorie sau instabilitate impune completarea cu CT Torace.",
    },

    # 2. Abdomen & Bazin
    {
        "title": "Rx Abdomen pe Gol (Abdominală Simplă)",
        "slug": "rx-abdomen-pe-gol",
        "modality": "rx",
        "category": "abdomen",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Suspiciune de ocluzie intestinală / volvulus (evidențierea nivelelor hidroaerice)",
            "Suspiciune de perforație de organ cavitar (pneumoperitoneu - aer subdiafragmatic)",
            "Suspiciune de corp străin radioopac ingerat",
            "Calculoză renală radioopacă (orientativ)",
            "Monitorizare post-procedurală stenturi ureterale (JJ) sau tuburi de dren",
        ],
        "position": "1) Ortostatism cu spatele lipit de stativul vertical Bucky; 2) Decubit dorsal (AP) dacă pacientul este nedeplasabil; 3) Decubit lateral stâng cu rază orizontală dacă ortostatismul este imposibil",
        "sid_dff": "100 - 115 cm",
        "centering": "Pe linia mediană, la 2-3 cm deasupra crestelor iliace (pentru a include cupolele diafragmatice pe clișeul de ortostatism)",
        "breathing": "Apnee la sfârșitul unui expir complet (ridică diafragmul și relaxează musculatura abdominală)",
        "tech_params": {
            "kv": "75 - 85",
            "mas": "25 - 40 (AEC)",
            "grid": "Cu grilă antidifuzoare Bucky (raport 10:1 sau 12:1)",
            "focal_spot": "Focar Mare (1.0 - 1.2 mm)",
            "aec_chambers": "Toate cele 3 camere de ionizare sau camerele laterale",
            "collimation": "De la cupolele diafragmatice până la simfiza pubiană",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Cupolele diafragmatice trebuie incluse obligatoriu în ortostatism (pentru excluderea semnelor de pneumoperitoneu)",
            "Simfiza pubiană inclusă în marginea inferioară a clișeului de decubit",
            "Liniile mușchilor psoas și contururile renale vizibile",
            "Nivelele hidroaerice clar demarcate între faza lichidiană și cea gazoasă",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Verificare obligatorie status sarcină la paciente",
        ],
        "iris_reference": {
            "chapter": "Aparat digestiv & Abdomen",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 2 (Foarte mică ~ 0.7 - 1.2 mSv)",
        },
        "notes": "Pentru identificarea aerului liber subdiafragmatic (pneumoperitoneu), pacientul trebuie menținut în ortostatism minim 5-10 minute înainte de declanșarea expunerii.",
    },
    {
        "title": "Rx Bazin Antero-Posterior (AP)",
        "slug": "rx-bazin-ap",
        "modality": "rx",
        "category": "abdomen",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatisme pelvine, suspiciune de fractură a inelului pelvin sau aripilor iliace",
            "Durere cronică de șold, evaluarea coxartrozei bilaterale",
            "Suspiciune fractură de col femural sau fractură pertrohanteriană",
            "Bilanț preoperator și postoperator artroplastie totală de șold",
            "Leziuni osoase secundare (metastaze osoase pelvine)",
        ],
        "position": "Decubit dorsal pe masa radiologică, membrele inferioare în extensie și rotație internă de 15° (alinierea colurilor femurale)",
        "sid_dff": "100 - 115 cm",
        "centering": "Pe linia mediană, la jumătatea distanței dintre spinele iliace antero-superioare (SIAS) și marginea superioară a simfizei pubiene",
        "breathing": "Apnee în expir liniștit",
        "tech_params": {
            "kv": "75 - 85",
            "mas": "20 - 35 (AEC)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mare (1.0 mm)",
            "aec_chambers": "Camerele laterale activate",
            "collimation": "Includerea crestelor iliace superior și a treimii proximale a femurului bilateral inferior",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Includerea completă a inelului pelvin, sacrului, ambelor articulații coxo-femurale și trohanterelor",
            "Simetrie a găurilor obturatoare și a aripilor iliace (absența rotației bazinului)",
            "Colurile femurale alungite fără suprapunerea marilor trohanteri (datorită rotației interne de 15°)",
            "Linia Shenton continuă și regulată pe ambele părți",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "La femei, ecranarea poate masca sacrul sau oasele pubiene; se aplică strict dacă nu obstrucționează zona de interes",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Bazin",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 2 (Foarte mică ~ 0.8 - 1.0 mSv)",
        },
        "notes": "În traumatisme severe cu suspiciune de fractură instabilă de bazin sau col femural luxat, NU se forțează rotația internă a membrelor inferioare!",
    },

    # 3. Coloană Vertebrală
    {
        "title": "Rx Coloană Cervicală (Față & Profil)",
        "slug": "rx-coloana-cervicala",
        "modality": "rx",
        "category": "coloana",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Cervicalgii acute sau cronice, nevralgie cervico-brahială",
            "Traumatism cervical minor (pacient conștient, fără deficite neurologice)",
            "Modificări degenerative (spondiloză cervicală, uncartroză, pensări discale)",
            "Evaluarea posturii și lordozei cervicale",
        ],
        "position": "1) Incidență AP (Față): ortostatism sau șezând, bărbia ușor ridicată; 2) Incidență Laterală (Profil): ortostatism, umărul lipit de stativ, umerii coborâți la maximum; 3) Incidență Transbucală (Odontoidă) cu gura larg deschisă",
        "sid_dff": "150 - 180 cm pentru Profil (reduce magnificarea și compensează distanța umăr-coloană); 100 cm pentru Față",
        "centering": "Față: C4 (cartilajul tiroidian), angulație tub 15° cranial; Profil: C4 perpendicular pe detector; Odontoidă: perpendicular prin centrul cavității bucale deschise",
        "breathing": "Apnee în expir complet (pentru profil, umerii sunt trași în jos de două greutăți mici ținute în mâini)",
        "tech_params": {
            "kv": "65 - 75 (Față / Odontoidă); 70 - 80 (Profil)",
            "mas": "10 - 20 (cu grilă Bucky)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Camera centrală de ionizare",
            "collimation": "De la baza craniului până la vertebra T1",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Pe profil: vizualizarea obligatorie a tuturor celor 7 vertebre cervicale (C1 la C7) și a joncțiunii C7-T1",
            "Alinierea corectă a liniilor vertebrale: linia corpilor anteriori, linia corpilor posteriori și linia spino-laminară",
            "Spațiul retrofaringian normal (< 7 mm la C2, < 20 mm la C6)",
            "Pe odontoidă: dintele axisului centrat între masele laterale ale atlasului, cu spații articulare atlanto-axoidiene simetrice",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare precisă pe coloana cervicală",
        ],
        "iris_reference": {
            "chapter": "Coloană vertebrală & Traumatisme",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.2 mSv)",
        },
        "notes": "Dacă C7-T1 nu se poate vizualiza pe profil din cauza umerilor masivi, se realizează incidența specială 'Swimmer' (înotător) sau se efectuează CT Cervical.",
    },
    {
        "title": "Rx Coloană Toracală (Față & Profil)",
        "slug": "rx-coloana-toracala",
        "modality": "rx",
        "category": "coloana",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Dorsalgii cronice, cifoză dorsală accentuată (boala Scheuermann)",
            "Suspiciune tasare vertebrală osteoporotică",
            "Traumatisme toracale cu durere pe linia mediană posterioară",
            "Screening scolioză toracală",
        ],
        "position": "Față (AP): decubit dorsal sau ortostatism; Profil: decubit lateral sau ortostatism cu brațele ridicate anterior",
        "sid_dff": "100 - 115 cm",
        "centering": "Nivel T7 (la 8-10 cm sub furculița sternală pe Față)",
        "breathing": "Față: apnee în expir; Profil: respirație superficială liniștită în timpul unei expuneri prelungite (estompează coastele și desenul pulmonar)",
        "tech_params": {
            "kv": "75 - 85 (Față); 80 - 90 (Profil)",
            "mas": "25 - 50 (AEC)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mare sau Mic",
            "aec_chambers": "Camera centrală activată",
            "collimation": "Longitudinală strictă pe lățimea corpilor vertebrali (aprox. 15 cm)",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Includerea tuturor celor 12 vertebre toracale (T1 la T12)",
            "Înălțimea corpilor vertebrali și spațiile discale vizibile clar fără rotație",
            "Găurile de conjugare vizualizate clar pe profil",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare laterală strânsă",
        ],
        "iris_reference": {
            "chapter": "Coloană vertebrală",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 2 (Foarte mică ~ 0.7 mSv)",
        },
        "notes": "Efectul de toc (anode heel effect) poate fi utilizat orientând catodul spre partea inferioară a toracelui pentru o densitate mai uniformă.",
    },
    {
        "title": "Rx Coloană Lombară (Față, Profil & L5-S1)",
        "slug": "rx-coloana-lombara",
        "modality": "rx",
        "category": "coloana",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Lombalgie acută sau cronică, lombosciatică",
            "Suspiciune spondilolistezis sau spondiloliză (incidențe oblice)",
            "Tasări vertebrale osteoporotice",
            "Modificări degenerative discale, osteofitoză marginală",
        ],
        "position": "1) AP (Față): decubit dorsal cu genunchii flectați (aplatizează lordoza lombară); 2) Lateral (Profil): decubit lateral cu genunchii flectați; 3) Joncțiune L5-S1: profil centrat cu tub angulat 5-8° caudal",
        "sid_dff": "100 - 115 cm",
        "centering": "Față & Profil: Nivel L3 (la 2-3 cm deasupra crestelor iliace); L5-S1: la 4 cm sub creasta iliacă și 5 cm anterior de apofiza spinoasă",
        "breathing": "Apnee în expir complet",
        "tech_params": {
            "kv": "75 - 80 (Față); 85 - 95 (Profil); 95 - 100 (L5-S1 spot)",
            "mas": "25 - 45 (Față); 40 - 70 (Profil); 60 - 90 (L5-S1)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mare (1.0 mm)",
            "aec_chambers": "Camera centrală activată",
            "collimation": "De la T12 la joncțiunea sacro-coccigiană",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Includerea vertebrelor L1 la L5 și a sacrului superior",
            "Pe profil: găurile de conjugare deschise și spațiile discale intervertebrale paralele",
            "Pediculii vertebrali și procesele spinoase aliniate simetric pe fața AP",
            "Pe clișeul L5-S1: spațiul discal lombo-sacrat bine deschis și vizibil",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Evaluarea posibilității unei sarcini se documentează conform procedurii locale și examinării solicitate.",
        ],
        "iris_reference": {
            "chapter": "Coloană vertebrală",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 2 (Foarte mică ~ 1.0 - 1.5 mSv)",
        },
        "notes": "Incidențele oblice (pentru vizualizarea 'cățelușului Lachapelle' în spondiloliză) se realizează doar dacă există suspiciune specifică de liză istmică.",
    },

    # 4. Membru Superior
    {
        "title": "Rx Umăr (AP Neutru & Incidență Y Scapular)",
        "slug": "rx-umar-ap-axial",
        "modality": "rx",
        "category": "membru-superior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatisme ale umărului, suspiciune de luxație gleno-humerală anterioară/posterioară",
            "Fracturi de col humeral anatomic/chirurgical sau trohiter",
            "Omalgie cronică, periartrită scapulo-humerală (calcificări tendinoase)",
            "Evaluare artroză gleno-humerală sau acromio-claviculară",
        ],
        "position": "1) AP: ortostatism cu spatele la stativ, umărul ușor rotit posterior 30-45° (incidență Grashey pentru deschiderea fantei articulare); 2) Incidență Y Scapular (Profil de scapulă): pacientul rotit anterior 45-60° cu umărul afectat lipit de detector",
        "sid_dff": "100 - 115 cm",
        "centering": "La 2-3 cm sub procesul coracoid pe AP; pe spina scapulei pe incidența Y",
        "breathing": "Apnee în expir liniștit",
        "tech_params": {
            "kv": "65 - 75",
            "mas": "8 - 15 (cu grilă Bucky)",
            "grid": "Cu grilă antidifuzoare",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Camera centrală",
            "collimation": "Inclusiv treimea externă a claviculei, acromionul și treimea proximală a humerusului",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Pe AP Grashey: fanta articulară gleno-humerală este liberă fără suprapunere a marginii glenei peste capul humeral",
            "Pe incidența Y: corpul scapulei, acromionul și coracoidul formează litera Y, cu capul humeral centrat perfect în intersecția Y (excluderea luxației)",
            "Detalii trabeculare clare ale trohiterului și trohinului",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template. și guler tiroidian",
            "Colimare strictă la articulația umărului",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Membru superior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.05 mSv)",
        },
        "notes": "În caz de suspiciune de luxație, NU se forțează mișcări de rotație externă sau abducție a brațului!",
    },
    {
        "title": "Rx Cot (Față & Profil)",
        "slug": "rx-cot-fata-profil",
        "modality": "rx",
        "category": "membru-superior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatisme de cot, suspiciune fractură paletă humerală, cap radial sau olecran",
            "Luxație de cot post-traumatică",
            "Semnul pernuței de grăsime (fat pad sign) — hemartroză ocultă",
            "Artroză de cot, epicondilită cronică",
        ],
        "position": "Pacient așezat la capătul mesei radiologice. 1) Față (AP): brațul și antebrațul în extensie completă și supinație, lipite de detector; 2) Profil: cot flectat strict la 90°, marginea ulnară lipită de casetă",
        "sid_dff": "100 cm",
        "centering": "Mijlocul fantei articulare a cotului (la 2 cm sub linia interepicondiliană)",
        "breathing": "Nu este necesară apneea; pacient imobilizat complet",
        "tech_params": {
            "kv": "55 - 62",
            "mas": "3 - 6 (fără grilă)",
            "grid": "Fără grilă antidifuzoare (extremitate mică)",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "Inclusiv treimea distală de humerus și treimea proximală de radius și ulnă",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Pe față: articulația cotului complet deschisă, epicondilii humerului vizibili în profil fără rotație",
            "Pe profil: flexie strictă la 90°, suprapunerea precisă a condililor humerale (trohlee și capitul)",
            "Vizualizarea pernuței adipoase anterioare și posterioare (semnul pernuței posterioare indică hemartroză chiar în absența unei fracturi evidente)",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare restrânsă strict pe cot",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Membru superior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
        },
        "notes": "La copii, prezența nucleilor de osificare secundari (CRITOE: Capitul, Radius, Intern, Trohlee, Olecran, Extern) trebuie verificată atent în funcție de vârstă.",
    },
    {
        "title": "Rx Pumn & Incidențe Scafoid",
        "slug": "rx-pumn-si-scafoid",
        "modality": "rx",
        "category": "membru-superior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Cădere pe mâna întinsă (FOOSH) cu durere în tabachera anatomică",
            "Suspiciune fractură de scafoid carpiam",
            "Fracturi ale extremității distale de radius (Pouteau-Colles, Goyrand-Smith)",
            "Instabilitate carpiană, artroză radio-carpiană",
        ],
        "position": "1) Față (PA): pumn în pronație, degete ușor flectate; 2) Profil strict: cot la 90°, pumn și antebraț pe cant; 3) Incidență Scafoid: deviație ulnară cu angulație tub 15-20° cranial; 4) Oblică la 45°",
        "sid_dff": "100 cm",
        "centering": "Mijlocul rândului proximal carpian (la nivelul scafoidului)",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "52 - 58",
            "mas": "2.5 - 4 (fără grilă)",
            "grid": "Fără grilă antidifuzoare",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "De la metafiza radială distală la baza metacarpienelor",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Pe profil: axul radiusului, semilunarului, capitatului și metacarpianului III sunt strict aliniate",
            "Pe incidența scafoid: alungirea completă a corpului și polilor scafoidului fără scurtare perspectivă",
            "Liniile carpiene ale lui Gilula sunt continue și netede",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare precisă pe aria carpiană",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Traumatisme",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
        },
        "notes": "Dacă radiografia inițială de scafoid este normală dar durerea în tabachera anatomică persistă, se imobilizează pumnul și se repetă radiografia la 10-14 zile, sau se efectuează direct RMN / CT.",
    },
    {
        "title": "Rx Mână & Degete (Față & Oblică)",
        "slug": "rx-mana-fata-oblica",
        "modality": "rx",
        "category": "membru-superior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatisme ale mâinii, fracturi de metacarpiene (ex: fractura boxerului - metacarpian V)",
            "Fracturi și luxații ale falangelor",
            "Evaluare artrită reumatoidă (eroziuni periarticulare, pensări fante)",
            "Suspiciune corp străin radioopac în părțile moi ale mâinii",
        ],
        "position": "1) PA (Față): palma complet etalată pe detector, degetele ușor depărtate; 2) Semioblică (la 45°): mâna sprijinită pe un burete unghiular de spumă pentru separarea falangelor",
        "sid_dff": "100 cm",
        "centering": "Capul metacarpianului III",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "50 - 55",
            "mas": "2 - 3 (fără grilă)",
            "grid": "Fără grilă antidifuzoare",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "De la articulația pumnului la extremitatea distală a degetelor",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Includerea completă a carpiencelor distale, metacarpienelor și tuturor falangelor",
            "Fantele articulare interfalangiene și metacarpo-falangiene clar vizibile și deschise",
            "Pe incidența oblică: metacarpienele și falangele sunt proiectate fără suprapunere excesivă",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template. aplicat în poziție șezând",
            "Colimare strictă la conturul cutanat al mâinii",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Membru superior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
        },
        "notes": "Pentru un deget izolat (police, index etc.), se recomandă incidențe dedicate de deget (Față + Profil strict) pentru o rezoluție optimă.",
    },

    # 5. Membru Inferior
    {
        "title": "Rx Șold (AP & Profil Lauenstein)",
        "slug": "rx-sold-ap-profil",
        "modality": "rx",
        "category": "membru-inferior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Cădere cu durere inghinală și impotență funcțională (suspiciune fractură col femural)",
            "Coxartroză (pensare supero-externă, osteofitoză, geode subcondrale)",
            "Necroză avasculară de cap femural (stadii inițiale / avansate)",
            "Control proteză totală de șold",
        ],
        "position": "1) AP: decubit dorsal, membrul afectat în rotație internă de 15°; 2) Profil Lauenstein (poziție broască): coapsa în abducție de 45° și flexie de 90°",
        "sid_dff": "100 - 115 cm",
        "centering": "Pe pliul inghinal, la 2-3 cm distal de punctul mijlociu dintre SIAS și simfiză",
        "breathing": "Apnee în expir",
        "tech_params": {
            "kv": "70 - 80",
            "mas": "15 - 30 (AEC)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mic sau Mare",
            "aec_chambers": "Camera centrală de ionizare",
            "collimation": "Inclusiv acetabulul, capul, colul femural și trohanterul",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Vizualizarea clară a cotilului, capului femural, liniei intertrohanteriene și marelui/micului trohanter",
            "Profilul Lauenstein evidențiază conturul sferic anterior al capului și colului femural",
            "Trabeculația colului femural (traveele Ward) este vizibilă neted",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare unilaterală riguroasă",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Membru inferior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.3 mSv)",
        },
        "notes": "În caz de traumatism acut cu durere severă, profilul Lauenstein este strict CONTRAINDICAT! Se realizează incidența profil axială cu raza orizontală (incidența Danelius-Miller).",
    },
    {
        "title": "Rx Genunchi (Față, Profil & Axială Rotulă)",
        "slug": "rx-genunchi-fata-profil",
        "modality": "rx",
        "category": "membru-inferior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatism de genunchi, suspiciune fractură de platou tibial, rotulă sau femur distal",
            "Gonartroză (evaluare pensări fante articulare pe clișee în sprijin / ortostatism)",
            "Hemartroză post-traumatică / colecție lichidiană",
            "Instabilitate patelară sau sindrom femuro-patelar (axiale rotulă la 30° și 60°)",
        ],
        "position": "1) AP (Față): decubit dorsal sau ortostatism (cu sprijin monopodal pentru artroză), picior în extensie; 2) Profil: decubit lateral pe partea afectată, genunchi flectat la 20-30°; 3) Axiale de rotulă (Merchant/Settegast): flexie genunchi 30° sau 60° cu raza tangențială pe rotulă",
        "sid_dff": "100 - 115 cm",
        "centering": "La 1-2 cm sub vârful rotulei (direct în interlinia articulară femuro-tibială)",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "60 - 68 (Față & Profil); 58 - 64 (Axială rotulă)",
            "mas": "4 - 8 (cu grilă) sau 2.5 - 5 (fără grilă)",
            "grid": "Cu grilă la adulți (sau detector DR digital fără grilă)",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Camera centrală",
            "collimation": "Inclusiv condilii femurali distali și platourile tibiale proximale",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Pe AP: interlinia articulară femuro-tibială complet deschisă, spinele tibiale vizibile în fosa intercondiliană",
            "Pe profil: suprapunerea precisă a condililor femurali posteriori; spațiul retropatelar vizibil liber",
            "Pe axiale: rotula centrată în șanțul trohlean, fanta femuro-patelară deschisă fără subluxație",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare strictă pe aria genunchiului",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Membru inferior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.05 mSv)",
        },
        "notes": "Pentru gonartroză, incidența AP cu sprijin (în încărcare) este esențială pentru măsurarea reală a pensării spațiului articular.",
    },
    {
        "title": "Rx Gleznă (Față / Morteză & Profil)",
        "slug": "rx-glezna-fata-profil",
        "modality": "rx",
        "category": "membru-inferior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Entorsă de gleznă conform criteriilor Ottawa (durere la nivelul maleolelor, imposibilitate de sprijin)",
            "Fracturi bimalleolare sau trimalleolare",
            "Suspiciune leziune a sindesmozei tibio-fibulare",
            "Artroză tibio-astragaliană",
        ],
        "position": "1) Incidență Morteză (Față AP): decubit dorsal cu membrul inferior extins și rotație internă de 15-20° (aduce linia bimaleolară paralelă cu detectorul); 2) Profil: decubit lateral pe partea afectată, genunchi flectat, piciorul la 90° în dorsiflexie",
        "sid_dff": "100 cm",
        "centering": "Punctul mijlociu dintre cele două maleole pe fața anterioară",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "55 - 63",
            "mas": "3 - 6 (fără grilă)",
            "grid": "Fără grilă antidifuzoare",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "De la treimea distală de tibie/fibulă la baza oaselor metatarsiene",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Pe incidența morteză: spațiul articular tibio-talar este egal pe toată circumferința (superior, medial și lateral fără suprapunere fibulară)",
            "Pe profil: domul talusului este aliniat fără dublu contur (condilii talari suprapuși perfect)",
            "Vizualizarea bazei celui de-al V-lea metatarsian pentru excluderea unei fracturi asociate de avulsie",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare centrată pe gleznă",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Membru inferior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
        },
        "notes": "Aplicarea corectă a Criteriilor Ottawa reduce cu peste 30% efectuarea de radiografii inutile de gleznă.",
    },
    {
        "title": "Rx Picior (Față & Oblică)",
        "slug": "rx-picior-fata-oblica",
        "modality": "rx",
        "category": "membru-inferior",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatisme ale piciorului, fracturi de metatarsiene (inclusiv fractura de marș / stres)",
            "Fractură de bază metatarsian V (fractura Jones)",
            "Suspiciune leziune a articulației Lisfranc sau Chopart",
            "Deformații ale piciorului (hallux valgus, picior plat - evaluat în sprijin)",
        ],
        "position": "1) AP (Dorso-plantar): talpa piciorului așezată plan pe casetă, tubul angulat 10° posterior către călcâi; 2) Oblică medială: piciorul rotit intern la 30-45° față de suprafața mesei",
        "sid_dff": "100 cm",
        "centering": "Baza celui de-al treilea metatarsian",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "52 - 58",
            "mas": "2.5 - 4",
            "grid": "Fără grilă antidifuzoare",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "De la tuberozitatea calcaneului la vârfurile falangelor",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Fantele metatarso-falangiene și tarso-metatarsiene clar vizibile",
            "Pe oblică: articulațiile cuboidului cu metatarsienele IV-V și navicularul sunt eliberate de suprapuneri",
            "Baza metatarsianului V clar decelabilă fără fractură",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare strictă",
        ],
        "iris_reference": {
            "chapter": "Aparat locomotor & Membru inferior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
        },
        "notes": "Pentru evaluarea piciorului plat sau scobit, radiografiile trebuie efectuate obligatoriu în sarcină (sprijin bipodal).",
    },

    # 6. Pediatrie
    {
        "title": "Rx Torace Pediatric (Sugar & Copil)",
        "slug": "rx-torace-pediatric",
        "modality": "rx",
        "category": "pediatrie",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Infecție respiratorie joasă febrilă (pneumonie, bronșiolită severă)",
            "Stridor acut sau suspiciune de corp străin inhalat",
            "Tuse cronică sau wheezing neexplicat",
            "Evaluare cardiomegalie congenitală",
        ],
        "position": "La sugari/copii mici: decubit dorsal pe detector (sau imobilizare cu dispozitiv Pigg-O-Stat în ortostatism dacă este disponibil); la copii mari: ortostatism la Bucky",
        "sid_dff": "100 - 150 cm",
        "centering": "Nivel medio-sternal (mamelonar)",
        "breathing": "Expunere declanșată rapid în faza de inspir maxim (la plânsul copilului expunerea se face la sfârșitul inspirului profund)",
        "tech_params": {
            "kv": "60 - 70 (tehnică pediatrică adaptată)",
            "mas": "1.0 - 2.0 (timp de expunere ultra-scurt < 5-10 ms pentru evitarea neclarității cinetice)",
            "grid": "FĂRĂ GRILĂ (reducere substanțială a dozei de iradiere la copii < 20 kg)",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual sau AEC pediatric calibrat",
            "collimation": "Strictă pe cutia toracică (fără abdomen)",
            "filtration": "Suplimentară 1 mm Al + 0.1-0.2 mm Cu (filtrare suplimentară pediatrică)",
        },
        "quality_criteria": [
            "Simetrie a hemitoracelor (absența rotației)",
            "Inspir corect (minim 8-9 arcuri costale posterioare)",
            "Absența artefactelor de mișcare",
            "Recunoașterea umbrei timusului la sugar (semnul pânzei de barcă / velar — aspect fiziologic normal)",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Însoțitorul (părintele) echipat obligatoriu cu șorț și guler de plumb pe durata imobilizării",
            "Principiul ALARA strict respectat: zero repetări nejustificate",
        ],
        "iris_reference": {
            "chapter": "Pediatrie — Torace, pulmon, cord",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.02 mSv)",
        },
        "notes": "Timusul normal la sugari poate mări considerabil mediastinul antero-superior; nu trebuie confundat cu o tumoră mediastinală sau cardiomegalie!",
    },
    {
        "title": "Rx Vârstă Osoasă (Mână & Pumn Stâng)",
        "slug": "rx-varsta-osoasa",
        "modality": "rx",
        "category": "pediatrie",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Evaluarea întârzierii de creștere / talie mică constituțională",
            "Pubertate precoce sau pubertate întârziată",
            "Tratamente endocrine cu hormon de creștere (GH)",
            "Boli metabolice osoase sau displazii scheletale",
        ],
        "position": "Copil așezat pe scaun, mâna și pumnul STÂNG (convenție internațională conform Atlasului Greulich & Pyle) plasate plat pe detector cu degetele ușor depărtate",
        "sid_dff": "100 cm",
        "centering": "Capul metacarpianului III",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "45 - 50",
            "mas": "1.5 - 2.5",
            "grid": "Fără grilă",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "De la treimea distală a antebrațului stâng până la vârfurile degetelor",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Vizualizarea completă a oaselor carpiene, epifizelor și metafizelor radiusului, ulnei, metacarpienelor și falangelor",
            "Degetele complet întinse, fără flexie sau suprapunere",
            "Rezoluție osoasă fină care permite identificarea fuziunii cartilajelor de creștere",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template. aplicat în poala copilului",
            "Colimare strictă pe mâna stângă",
        ],
        "iris_reference": {
            "chapter": "Pediatrie — Aparat locomotor",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.005 mSv)",
        },
        "notes": "Se compară imaginea obținută cu standardele din Atlasul Greulich & Pyle sau metoda Tanner-Whitehouse (TW3). Mâna stângă este standardul universal chiar și la copiii dreptaci.",
    },
    {
        "title": "Rx Bazin & Șolduri Sugari (Displazie de Șold)",
        "slug": "rx-bazin-solduri-sugari",
        "modality": "rx",
        "category": "pediatrie",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Depistarea și evaluarea displaziei de dezvoltare a șoldului (DDH) la sugari peste 4-6 luni (după debutul osificării capului femural)",
            "Monitorizare post-tratament cu ham Pavlik sau atelă de abducție",
            "Luxație congenitală de șold confirmată",
        ],
        "position": "Decubit dorsal, asistentul sau părintele menține bazinul perfect orizontal, membrele inferioare în adducție ușoară și extensie simetrică",
        "sid_dff": "100 cm",
        "centering": "Pe linia mediană, la nivelul simfizei pubiene",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "55 - 60",
            "mas": "3 - 5",
            "grid": "Fără grilă (sau grilă cu raport mic 6:1)",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "De la crestele iliace la treimea superioară femurală",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Simetrie perfectă a inelului pelvin (absența înclinației pelvine)",
            "Găurile obturatoare simetrice ca dimensiune",
            "Trasarea clară a reperelor geometrice: linia Hilgenreiner (orizontală prin cartilajele triradiate), linia Perkin (verticală la marginea externă acetabulară) și linia Shenton",
            "Calculul unghiului acetabular (normal < 30° la nou-născut, < 25° la 6 luni)",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Însoțitorul este protejat cu șorț și mănuși de plumb",
        ],
        "iris_reference": {
            "chapter": "Pediatrie — Aparat locomotor",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.1 mSv)",
        },
        "notes": "La sugari sub 4-6 luni, metoda de elecție este ECOGRAFIA DE ȘOLD (metoda Graf) conform ghidului IRIS, deoarece componentele sunt predominant cartilaginoase și nu iradiază!",
    },

    # 7. Craniu & Masiv Facial
    {
        "title": "Rx Sinusuri Anterioare ale Feței (SAF / Waters)",
        "slug": "rx-sinusuri-saf-waters",
        "modality": "rx",
        "category": "craniu-saf",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Suspiciune de sinuzită acută maxilară sau frontală (nivele hidroaerice)",
            "Bilanț inițial traumatism facial (fracturi ale podelei orbitei - blow-out, fracturi malare)",
            "Polipoză nazală / opacifiere sinusală",
        ],
        "position": "Incidența Mento-Placă (Waters): ortostatism, bărbia lipită de Bucky vertical, nasul la 1-1.5 cm distanță de stativ (linia meato-orbitală face un unghi de 37° cu detectorul), gura larg deschisă pentru vizualizarea sinusului sfenoidal",
        "sid_dff": "100 cm",
        "centering": "Perpendicular prin protuberanța occipitală externă, ieșind la nivelul spinei nazale anterioare",
        "breathing": "Apnee în inspir liniștit",
        "tech_params": {
            "kv": "70 - 75",
            "mas": "15 - 25",
            "grid": "Cu grilă antidifuzoare Bucky",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Camera centrală de ionizare",
            "collimation": "De la arcadele sprâncenoase la mandibulă",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Stâncile temporale sunt proiectate imediat sub podeaua sinusurilor maxilare",
            "Simetrie a orbitelor și a arcadelor zigomatice",
            "Vizualizarea clară a transparenței sinusurilor frontale, maxilare și a celulelor etmoidale anterioare",
            "Pe varianta cu gura deschisă: sinusul sfenoidal proiectat în cavitatea bucală",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare riguroasă pe masivul facial",
        ],
        "iris_reference": {
            "chapter": "Cap — ORL",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 1 (Minimă < 0.08 mSv)",
        },
        "notes": "Ortostatismul este obligatoriu pentru evidențierea nivelelor hidroaerice (puroi/lichid în sinuzita acută sau hemo-sinus în traumatisme).",
    },
    {
        "title": "Rx Oase Proprii Nazale (OPN)",
        "slug": "rx-oase-nazale-opn",
        "modality": "rx",
        "category": "craniu-saf",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie",
        "clinical_indications": [
            "Traumatism facial direct cu epistaxis, deformare nazală și suspiciune de fractură de oase proprii nazale",
            "Evaluare medico-legală a fracturilor nazale recente",
        ],
        "position": "Profil bilateral (dreapta și stânga): decubit ventral sau șezând, fața laterală a nasului paralelă cu detectorul fără rotație",
        "sid_dff": "100 cm",
        "centering": "La 1-1.5 cm sub nasion (rădăcina nasului)",
        "breathing": "Nemodificată",
        "tech_params": {
            "kv": "45 - 50 (tehnică de părți moi / os fin)",
            "mas": "3 - 5",
            "grid": "FĂRĂ GRILĂ",
            "focal_spot": "Focar Mic (0.6 mm)",
            "aec_chambers": "Manual",
            "collimation": "Colimare foarte strânsă (câmp de 6 x 6 cm)",
            "filtration": "Totală ≥ 2.5 mm Al",
        },
        "quality_criteria": [
            "Vizualizarea fină a corticalei anterioare și a suturii nazo-frontale",
            "Spina nazală anterioară și cartilajele septale vizibile",
            "Absența suprapunerii cu arcadele dentare superioare",
        ],
        "protection": [
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.",
            "Colimare ultra-restrânsă",
        ],
        "iris_reference": {
            "chapter": "Traumatisme — Față și orbite",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
        },
        "notes": "Se efectuează întotdeauna ambele profile (drept și stâng) pentru comparație anatomică și certitudine diagnostică.",
    },
]


def generate_all_rx():
    count = 0
    categories = set()

    for p in RX_PROTOCOLS:
        cat = p["category"]
        categories.add(cat)
        cat_dir = DOCS_RX / cat
        cat_dir.mkdir(parents=True, exist_ok=True)

        md_content = render_rx_document(p)
        file_path = cat_dir / f"{p['slug']}.md"
        file_path.write_text(md_content, encoding="utf-8")
        count += 1

    # Creare .pages pentru fiecare subdirector
    cat_names = {
        "torace": "Torace & Cutie Toracică",
        "abdomen": "Abdomen & Bazin",
        "coloana": "Coloană Vertebrală",
        "membru-superior": "Membru Superior",
        "membru-inferior": "Membru Inferior",
        "pediatrie": "Pediatrie Rx",
        "craniu-saf": "Craniu & Masiv Facial",
    }

    for cat in categories:
        cat_dir = DOCS_RX / cat
        pages_file = cat_dir / ".pages"
        c_title = cat_names.get(cat, cat.title())
        pages_file.write_text(f"title: {c_title}\n", encoding="utf-8")

        # index.md pentru categorie
        cat_index = cat_dir / "index.md"
        protos_in_cat = [p for p in RX_PROTOCOLS if p["category"] == cat]
        links_list = "\n".join([f"- [{p['title']}]({p['slug']}.md)" for p in protos_in_cat])
        cat_index.write_text(f"# Protocoale Rx — {c_title}\n\n{links_list}\n", encoding="utf-8")

    # Creare docs/rx/.pages
    rx_pages = DOCS_RX / ".pages"
    rx_pages_content = """title: Protocoale Radiologie Clasică (Rx)
nav:
  - index.md
  - Radioprotecție: radioprotectie.md
  - Torace: torace
  - Abdomen & Bazin: abdomen
  - Coloană Vertebrală: coloana
  - Membru Superior: membru-superior
  - Membru Inferior: membru-inferior
  - Pediatrie: pediatrie
  - Craniu & Masiv Facial: craniu-saf
"""
    rx_pages.write_text(rx_pages_content, encoding="utf-8")

    # Creare docs/rx/index.md (Landing page)
    rx_index = DOCS_RX / "index.md"
    rx_index_content = """---
title: Ghidul Protocoalelor de Radiologie Clasică (Rx)
hide:
  - navigation
  - toc
---

# Ghidul Protocoalelor de Radiologie Clasică (Rx)

Protocoale tehnice complete de radiografie convențională și digitală pentru toate regiunile anatomice majore, adaptate cerințelor de calitate și principiilor de radioprotecție **ALARA**.

<div class="iris-official-banner" style="margin-bottom: 24px;">
  <div class="iris-official-badge">🏛️ CORELARE CU GHIDUL NAȚIONAL IRIS (ORDINUL MS 1342/2012)</div>
  <p class="iris-official-desc" style="margin-bottom: 8px !important;">
    Fiecare protocol de radiografie conține gradul de recomandare clinică (Grad A/B/C), clasa de iradiere estimată și indicațiile de primă intenție.
  </p>
  <a href="../iris/" style="font-weight: 600; color: #1565c0; text-decoration: none;">
    Verifică justificarea clinică pe Ghidul IRIS ➔
  </a>
</div>

<p class="body-parts-section-heading">Navigare după Regiunea Anatomică</p>

<div class="body-parts-grid">
  <a href="torace/" class="body-part-card">
    <h3>Torace & Cutie Toracică</h3>
  </a>
  <a href="abdomen/" class="body-part-card">
    <h3>Abdomen & Bazin</h3>
  </a>
  <a href="coloana/" class="body-part-card">
    <h3>Coloană Vertebrală</h3>
  </a>
  <a href="membru-superior/" class="body-part-card">
    <h3>Membru Superior</h3>
  </a>
  <a href="membru-inferior/" class="body-part-card">
    <h3>Membru Inferior</h3>
  </a>
  <a href="pediatrie/" class="body-part-card">
    <h3>Pediatrie Rx</h3>
  </a>
  <a href="craniu-saf/" class="body-part-card">
    <h3>Craniu & Masiv Facial</h3>
  </a>
</div>
"""
    rx_index.write_text(rx_index_content, encoding="utf-8")

    print(f"Generat cu succes {count} protocoale Rx în {len(categories)} categorii!")


if __name__ == "__main__":
    generate_all_rx()
