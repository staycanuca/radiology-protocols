"""generate_initial_eco_protocols.py — Generează protocoalele inițiale de Ecografie / Ultrasonografie (US).

Categorii:
- abdomen-pelvis: Abdomen Total, FAST Urgență, Pelvis Ginecologic & Vezical, Aparat Urinar
- parti-moi-endocrin: Tiroidă & Paratiroide (TIRADS), Ganglioni Cervicali, Părți Moi (Lipom/Colecție), Glande Salivare
- vascular-doppler: Doppler Carotidian & Vertebral, Doppler Venos Membru Inferior (TVP), Doppler Arterial Membru Inferior, Doppler Aortă Abdominală
- msk: Umăr & Coafa Rotatorilor, Genunchi & Aparat Extensor, Tendon Achilean & Gleznă
- san: Ecografie Mamară Bilaterală (BI-RADS US)
- pediatrie: Ecografie Transfontanelară (ETF), Șold Sugar (Screening Graf), Abdomen Pediatric (Apendicită/Pilor)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from render_eco_protocol import render_eco_document

ECO_PROTOCOLS = [
    # -----------------------------------------------------------------------
    # 1. ABDOMEN & PELVIS
    # -----------------------------------------------------------------------
    {
        "title": "Ecografie Abdominală Totală (Generală)",
        "slug": "eco-abdomen-total",
        "category": "abdomen-pelvis",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Sindrom dureros abdominal acut sau cronic",
            "Hepatomegalie, evaluarea steatozei hepatice și cirozei",
            "Suspiciune de litiază biliară, colică biliară, icter mecanic",
            "Evaluarea colecistului, pancreasului, splinei și rinichilor",
            "Screening abdominal de rutină și monitorizare ascită",
        ],
        "contraindications": [
            "Lipsă fereastră acustică adecvată cauzată de meteorism abdominal marcat",
            "Pansamente ocluzive abdominale întinse sau emfizem subcutanat",
        ],
        "patient_prep": "À jeun (post alimentar strict) minimum 6 ore anterior examinării pentru evacuarea stomacului și repleția colecistului; vezică urinară în semirepleție.",
        "transducers_equipment": {
            "transducer_types": "Sondă Convexă 3.5 - 5.0 MHz (screening de adâncime) + Sondă Liniară 7.5 - 12.0 MHz (suprafață hepatică, perete colecist, apendice)",
            "patient_position": "Decubit dorsal, completat obligatoriu cu decubit lateral stâng (pentru hil hepatic și splină) și ortostatism/apnee profundă la nevoie",
            "gel_acoustic_window": "Gel ecografic apos hipoalergenic; ferestre acustice subcostale și intercostale",
        },
        "technical_settings": {
            "preset": "Abdomen General",
            "modes": "Mod B (2D grayscale) + Doppler Color (CFM) + Doppler Pulsat (PW)",
            "focus_depth": "Focalizare dinamică adaptată organului examinat; adâncime 12-18 cm",
            "gain_thi": "THI (Tissue Harmonic Imaging) activat obligatoriu pentru reducerea artefactelor de reverberare și îmbunătățirea rezoluției de contrast",
            "measurements_criteria": "Diametru craniocaudal lob drept hepatic (<150 mm), diametru perete colecist (<3 mm), ax lung splină (<120 mm), ax lung renal (100-120 mm)",
        },
        "standard_views": [
            {
                "view": "Secțiune longitudinală epigastrică",
                "anatomical_target": "Lob hepatic stâng, aortă abdominală, pancreas",
                "landmarks": "Lobul stâng anterior de aorta abdominală și vena splenică / trunchiul celiac",
                "normal_aspect": "Ecostructură fină omogenă, bord ascuțit, calibru aortic normal <20 mm",
            },
            {
                "view": "Secțiune oblică subcostală dreaptă",
                "anatomical_target": "Colecist și hil hepatic",
                "landmarks": "Vena portă, artera hepatică și calea biliară principală (triada portală)",
                "normal_aspect": "Colecist alitiazic, perete subțire <3 mm, CBP cu diametru <6 mm (<8 mm la colecistectomizați)",
            },
            {
                "view": "Secțiune intercostală dreaptă",
                "anatomical_target": "Lob hepatic drept și rinichi drept",
                "landmarks": "Ecoreflexivitate comparativă parenchim hepatic vs. corticală renală (spațiul Morrison)",
                "normal_aspect": "Parenchim hepatic izoecogen sau ușor hiperecogen față de corticala renală, fără lichid liber în Morrison",
            },
            {
                "view": "Secțiune intercostală stângă",
                "anatomical_target": "Splină și rinichi stâng",
                "landmarks": "Fereastra splenică la nivelul spațiilor intercostale IX-XI stângi (spațiul Koller)",
                "normal_aspect": "Splină omogenă, lungime <12 cm, fără lichid liber perisplenic sau perirenal",
            },
        ],
        "quality_criteria": [
            "Optimizarea TGC pentru o atenuare uniformă de la suprafață la profunzime",
            "Vizualizarea integrală a cupolei diafragmatice drepte pentru excluderea leziunilor subcapsulare",
            "Compresie gradată și utilizarea manevrei Valsalva / apnee în inspir pentru coborârea ficatului și splinei",
        ],
        "safety_and_limitations": [
            "Indice mecanic (MI) < 1.0 și indice termic (TIB/TIS) < 1.0 conform principiului ALARA",
            "Pancreasul și retroperitoneul pot fi mascate de gazul gastric/colonic; se recomandă administrare de apă necarbogazoasă pentru fereastră gastrică dacă este clinic necesar",
        ],
        "iris_reference": {
            "chapter": "Aparat Digestiv & Abdomen",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "În caz de durere în hipocondrul drept, se evaluează semnul Murphy ecografic la compresia colecistului cu transductorul. Orice îngroșare parietală a colecistului se corelează cu statusul alimentar.",
    },
    {
        "title": "Protocol Ecografic FAST / E-FAST în Traumatologia de Urgență",
        "slug": "eco-fast-trauma-urgenta",
        "category": "abdomen-pelvis",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Politraumatism major / traumatism toraco-abdominal închis sau deschis",
            "Instabilitate hemodinamică inexplicabilă la pacientul traumatizat",
            "Suspiciune de hemoperitoneu, hemotorace, pneumotorace sau tamponadă cardiacă",
            "Triage rapid în camera de gardă (UPU)",
        ],
        "contraindications": [
            "Indicație chirurgicală absolută emergentă imediată (laparotomie de urgență directă)",
            "Lipsa contraindicațiilor absolute — ecografia FAST se efectuează în paralel cu resuscitarea volemică",
        ],
        "patient_prep": "Fără pregătire prealabilă (situație de urgență); decubit dorsal strict.",
        "transducers_equipment": {
            "transducer_types": "Sondă Phased-Array / Sectorială (2 - 4 MHz) sau Sondă Convexă (3.5 - 5 MHz) pentru cavitățile abdominală și pericardică; Sondă Liniară (7 - 12 MHz) pentru pneumotorace",
            "patient_position": "Decubit dorsal strict, fără mobilizarea coloanei vertebrale (stabilizare cu guler cervical)",
            "gel_acoustic_window": "Gel ecografic abundent; decontaminare rapidă a tegumentelor",
        },
        "technical_settings": {
            "preset": "Emergency / Trauma / FAST",
            "modes": "Mod B (2D) rapid + Mod M (pentru pneumotorace: semnul stratosferei vs. țărmul mării)",
            "focus_depth": "Adâncime mare inițial (15-20 cm) pentru detectarea colecțiilor declive",
            "gain_thi": "Câștig crescut pentru evidențierea spațiilor anecogene (lichidiene)",
            "measurements_criteria": "Evaluare calitativă binară (Prezent / Absent revărsat lichidian liber anecogen)",
        },
        "standard_views": [
            {
                "view": "Incidență Subxifoidiană (Pericardică)",
                "anatomical_target": "Sac pericardic și camere cardiace",
                "landmarks": "Lobul stâng hepatic ca fereastră acustică, miocardul VS/VD",
                "normal_aspect": "Absența benzii anecogene între pericard și miocard (fără hemopericard)",
            },
            {
                "view": "Incidență Hipocondru Drept (Morrison)",
                "anatomical_target": "Recesul hepatorenal și recesul pleural drept",
                "landmarks": "Interfața lob hepatic drept - pol superior rinichi drept + sinus costodiafragmatic",
                "normal_aspect": "Linie hiperecogenă continuă fără spațiu anecogen Morrison; semnul perdelei pulmonare prezent",
            },
            {
                "view": "Incidență Hipocondru Stâng (Koller)",
                "anatomical_target": "Recesul splenorenal și recesul pleural stâng",
                "landmarks": "Splină, pol superior rinichi stâng, hemidiafragm stâng",
                "normal_aspect": "Absența lamei de lichid subdiafragmatic sau în spațiul splenorenal",
            },
            {
                "view": "Incidență Suprapubiană (Pelvină / Douglas)",
                "anatomical_target": "Fundul de sac Douglas (reces rectovezical / rectouterin)",
                "landmarks": "Vezică urinară în secțiune transversală și longitudinală",
                "normal_aspect": "Absența lichidului liber retrovezical sau perivezical",
            },
            {
                "view": "Incidențe Pulmonare Anterioare (E-FAST)",
                "anatomical_target": "Pleură parietală și viscerală (spațiile intercostale II-IV)",
                "landmarks": "Coaste cu con de umbră posterior și linia pleurală hiperecogenă",
                "normal_aspect": "Prezența glisării pleurale (lung sliding) și a cozilor de cometă; în mod M: semnul țărmului mării",
            },
        ],
        "quality_criteria": [
            "Examinare completă efectuată în sub 2-3 minute",
            "Examinarea ambelor sinusuri costodiafragmatice pentru excluderea hemotoracelui",
            "Repetarea protocolului (serial FAST) la 15-30 minute dacă starea clinică a pacientului se modifică",
        ],
        "safety_and_limitations": [
            "FAST negativ nu exclude leziunile de organ parenchimatos fără hemoperitoneu liber sau leziunile retroperitoneale",
            "La pacientul stabil hemodinamic cu mecanism violent de traumatism, protocolul de elecție rămâne CT Politraumatism",
        ],
        "iris_reference": {
            "chapter": "Politraumatism & Urgențe Traumatice",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Protocolul E-FAST este exclusiv o investigație de orientare salvatoare de viață (răspuns DA/NU la întrebarea dacă există lichid liber/pneumotorace compresiv).",
    },
    {
        "title": "Ecografie Pelvină Ginecologică și a Vezicii Urinare (Transabdominală)",
        "slug": "eco-pelvis-ginecologic-si-vezical",
        "category": "abdomen-pelvis",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Durere pelvină acută sau cronică, dismenoree, metroragii",
            "Suspiciune de formațiuni ovariene chistice sau solide",
            "Fibromatoză uterină, evaluarea grosimii endometriale",
            "Evaluarea vezicii urinare (polipi, tumori vezicale, litiază)",
        ],
        "contraindications": [
            "Vezică urinară complet evacuată (impune amânarea sau abordul transvaginal la paciente compatibile)",
        ],
        "patient_prep": "Ingestie de 750 - 1000 ml apă plată necarbogazoasă cu 60-90 minute anterior examinării, fără urinare; vezica urinară trebuie să fie în repleție completă.",
        "transducers_equipment": {
            "transducer_types": "Sondă Convexă 3.5 - 5.0 MHz (screening transabdominal) / Sondă Endocavitară Transvaginală 5.0 - 9.0 MHz (la nevoie pentru rezoluție înaltă)",
            "patient_position": "Decubit dorsal relaxat",
            "gel_acoustic_window": "Gel ecografic apos; vezica urinară destinsă servește drept fereastră acustică",
        },
        "technical_settings": {
            "preset": "Pelvis Gyn / Bladder",
            "modes": "Mod B (2D) + Doppler Color (CFM) pentru vascularizația maselor anexiale",
            "focus_depth": "Focalizare posterioară (retrouterin și pe anexe); adâncime 10-16 cm",
            "gain_thi": "THI activat; atenuare redusă datorită ferestrei lichidiene vezicale",
            "measurements_criteria": "Dimensiuni uterine (longitudinal, anteroposterior, transversal), grosime endometru (dublu strat), volume ovariene (L x l x grosime x 0.52)",
        },
        "standard_views": [
            {
                "view": "Secțiune sagitală mediană pelvină",
                "anatomical_target": "Uter, col uterin, cavitate endometrială, fund de sac Douglas",
                "landmarks": "Vezica urinară anterior, vaginul inferior, canalul cervical",
                "normal_aspect": "Miometru omogen, linie endometrială regulată corespunzătoare fazei ciclului, Douglas liber",
            },
            {
                "view": "Secțiune transversală pelvină",
                "anatomical_target": "Corp uterin, coarne uterine, ovare bilateral",
                "landmarks": "Vasele iliace interne ca reper posterior pentru lojele ovariene",
                "normal_aspect": "Ovare cu foliculi periferici, stromă normală, fără mase chistice complexe",
            },
            {
                "view": "Secțiuni ortogonale vezicale",
                "anatomical_target": "Vezică urinară (pereți, lumen, joncțiuni ureterovezicale)",
                "landmarks": "Perete anterior, posterior, trigon vezical",
                "normal_aspect": "Perete subțire și suplu <3-4 mm în repleție, conținut anecogen pur, jeturi ureterale Doppler prezente",
            },
        ],
        "quality_criteria": [
            "Vezica urinară trebuie să depășească fundul uterin pentru a oferi fereastră acustică optimă",
            "Măsurarea endometrului se efectuează pe secțiune strict medio-sagitală la nivelul grosimii maxime",
        ],
        "safety_and_limitations": [
            "ALARA respectat; abordul transabdominal poate avea rezoluție suboptimală la pacientele cu obezitate",
        ],
        "iris_reference": {
            "chapter": "Obstetrică & Ginecologie",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "În caz de formațiune chistică ovariană, se consemnează criteriile IOTA (unilocular/multilocular, proiecții papilare, vascularizație Doppler).",
    },
    {
        "title": "Ecografie Renală și a Tractului Urinar",
        "slug": "eco-aparat-urinar-rinichi-vezica",
        "category": "abdomen-pelvis",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Colică renală, hematurie macroscopică sau microscopică",
            "Suspiciune de hidronefroză, litiază renală sau vezicală",
            "Infecții de tract urinar recurente, pielonefrită acută",
            "Insuficiență renală acută sau cronică, monitorizare chisturi renale",
            "Evaluarea reziduului urinar post-micțional (RPM)",
        ],
        "contraindications": [
            "Lipsa contraindicațiilor absolute",
        ],
        "patient_prep": "Hidratare per os (500 ml apă cu 45 min anterior examinării) pentru repleție vezicală optimă; nu este necesar repaus alimentar prelungit.",
        "transducers_equipment": {
            "transducer_types": "Sondă Convexă 3.5 - 5.0 MHz (screening) + Sondă Liniară 7.5 - 12.0 MHz (pentru joncțiuni ureterovezicale și calculi vezicali mici)",
            "patient_position": "Decubit dorsal, completat cu decubite laterale (stâng și drept) și decubit ventral pentru rinichi ectopici/ptotici",
            "gel_acoustic_window": "Gel ecografic apos",
        },
        "technical_settings": {
            "preset": "Renal / Urology",
            "modes": "Mod B (2D) + Doppler Color (pentru diferențierea vaselor de dilatațiile pielocaliceale și jeturile ureterale)",
            "focus_depth": "Focalizare pe sinusul renal și joncțiunea cortico-medulară; adâncime 10-15 cm",
            "gain_thi": "THI activat pentru accentuarea conului de umbră posterior al calculilor",
            "measurements_criteria": "Lungime renală (100-120 mm), indice parenchimatos / grosime corticală (15-20 mm), volum vezical premicțional și postmicțional (L x l x H x 0.52)",
        },
        "standard_views": [
            {
                "view": "Ax longitudinal renal (drept și stâng)",
                "anatomical_target": "Parenchim renal, piramide Malpighi, sinus renal hiperecogen",
                "landmarks": "Ficatul anterior (dreapta), splina anterior (stânga), psoasul posterior",
                "normal_aspect": "Contur neted, corticală omogenă, raport cortico-medular păstrat, sinus hiperecogen fără dilatație",
            },
            {
                "view": "Ax transversal la nivelul hilului renal",
                "anatomical_target": "Bazinel renal, arteră și venă renală",
                "landmarks": "Artera renală posterioară față de vena renală",
                "normal_aspect": "Bazinel nedilatat (<10 mm în ax AP), absența calculilor obstructivi",
            },
            {
                "view": "Secțiune vezicală transversală la nivelul trigonului",
                "anatomical_target": "Meate ureterale și jeturi ureterale Doppler",
                "landmarks": "Baza vezicii urinare, deasupra prostatei / colului vezical",
                "normal_aspect": "Jeturile ureterale simetrice la examen Doppler color (exclud obstrucția ureterală completă)",
            },
        ],
        "quality_criteria": [
            "Măsurarea axului lung renal maxim în plan strict coronal/sagital",
            "Diferențierea certă a chisturilor simple Bosniak I de chisturile complicate sau masele solide",
            "Măsurarea reziduului postmicțional imediat după evacuarea vezicală",
        ],
        "safety_and_limitations": [
            "Ureterul lombar mijlociu nu este vizibil ecografic din cauza gazelor intestinale; calculii ureterali mici pot fi omiși",
        ],
        "iris_reference": {
            "chapter": "Aparat Uro-Genital & Suprarenale",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "În colica renală acută, absența dilatației pielocaliceale în primele ore nu exclude litiaza obstructivă incipientă. Se recomandă reevaluare sau CT nativ (Low-Dose) la persistența simptomelor.",
    },

    # -----------------------------------------------------------------------
    # 2. PĂRȚI MOI & ENDOCRINOLOGIE
    # -----------------------------------------------------------------------
    {
        "title": "Ecografie Tiroidiană și a Glandelor Paratiroide (Clasificare EU-TIRADS)",
        "slug": "eco-tiroida-si-paratiroide-tirads",
        "category": "parti-moi-endocrin",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Nodul tiroidian palpabil sau descoperit incidental",
            "Gușă polinodulară, tiroidită cronică autoimună (Hashimoto), boala Graves",
            "Disfuncție tiroidiană (hipotiroidism / hipertiroidism)",
            "Suspiciune de adenom paratiroidian în hiperparatiroidism primar",
            "Monitorizare postoperatorie sau post-terapie cu iod radioactiv",
        ],
        "contraindications": [
            "Lipsa contraindicațiilor absolute",
        ],
        "patient_prep": "Fără pregătire specială; hiperextensia gâtului cu un suport sub umeri; îndepărtarea colierelor.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară de înaltă frecvență 7.5 - 15.0 MHz (High-Resolution Linear)",
            "patient_position": "Decubit dorsal cu capul în hiperextensie moderată pe rulou cervical",
            "gel_acoustic_window": "Gel ecografic apos din abundență",
        },
        "technical_settings": {
            "preset": "Thyroid / Small Parts",
            "modes": "Mod B (2D) + Doppler Color (CFM) + Doppler Power (PDI) + Elastografie (Strain / Shear-Wave)",
            "focus_depth": "Focalizare superficială la nivelul parenchimului tiroidian (1.5 - 3.5 cm)",
            "gain_thi": "THI activat pentru definirea microcalcificărilor și marginilor nodulare",
            "measurements_criteria": "Dimensiuni lobi (L x l x grosime), volum tiroidian total, dimensiuni istm (<4 mm); pentru noduli: compoziție, ecogenitate, formă (taller-than-wide), margini, focare ecogene (microcalcificări)",
        },
        "standard_views": [
            {
                "view": "Secțiune transversală istmică și bilobară",
                "anatomical_target": "Istm tiroidian, ambii lobi, trahee, carotide",
                "landmarks": "Inelele traheale median, arterele carotide comune lateral",
                "normal_aspect": "Parenchim hiperecogen omogen față de mușchii pretiroidieni, capsulă continuă",
            },
            {
                "view": "Secțiune longitudinală lobară (dreaptă și stângă)",
                "anatomical_target": "Lob tiroidian de la polul superior la cel inferior",
                "landmarks": "Artera carotidă comună și vena jugulară internă lateral",
                "normal_aspect": "Lungime lobară 40-60 mm, grosime 13-18 mm, ecostructură fină omogenă",
            },
            {
                "view": "Explorare lojă paratiroidiană posterioară",
                "anatomical_target": "Poli posteriori tiroidieni superior și inferior",
                "landmarks": "Fascia posterioară tiroidiană și esofagul (la stânga)",
                "normal_aspect": "Paratiroidele normale nu sunt vizualizabile ecografic; adenomul apare ca masă ovalară hipoecogenă cu pedicul vascular polar",
            },
        ],
        "quality_criteria": [
            "Încadrarea fiecărui nodul tiroidian într-o categorie de risc conform EU-TIRADS (1 până la 5)",
            "Examinarea obligatorie a compartimentelor ganglionare cervicale centrale (VI) și laterale (II-IV)",
            "Evaluarea vascularizației nodulare Doppler (tip I avascular, tip II perinodular, tip III intern)",
        ],
        "safety_and_limitations": [
            "ALARA respectat; extensia retrosternală a gușilor masive nu poate fi evaluată complet ecografic (necesită CT)",
        ],
        "iris_reference": {
            "chapter": "Gât & Părți Moi Cervicale",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Nodulii EU-TIRADS 5 >10 mm și EU-TIRADS 4 >15 mm au indicație de puncție biopsie aspirativă cu ac fin (FNAB) ghidată ecografic.",
    },
    {
        "title": "Ecografie a Ganglionilor Limfatici Cervicali",
        "slug": "eco-ganglioni-limfatici-cervicali",
        "category": "parti-moi-endocrin",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Adenopatie cervicală palpabilă unică sau multiplă",
            "Bilanț de extensie ganglionară în neoplazii ORL, tiroidiene sau limfoame",
            "Limfadenită acută sau cronică, suspiciune de tuberculoză ganglionară",
            "Monitorizare post-terapeutică oncologică",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Decubit dorsal cu hiperextensia gâtului și rotația capului contralateral ariei examinate.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară de înaltă frecvență 9.0 - 15.0 MHz",
            "patient_position": "Decubit dorsal cu gâtul deflectat și rotit succesiv stânga/dreapta",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Lymph Nodes / Neck",
            "modes": "Mod B de înaltă rezoluție + Doppler Color + Doppler Pulsat + Elastografie",
            "focus_depth": "Focalizare strictă pe adâncimea ganglionului (1.0 - 3.0 cm)",
            "gain_thi": "THI activat pentru detalii fine capsulare și corticale",
            "measurements_criteria": "Raport ax lung / ax scurt (L/S ratio: >2 benign, <2 rotund malign), grosime corticală, hil hiperecogen central",
        },
        "standard_views": [
            {
                "view": "Scanare sistematică pe nivele ganglionare (I - VI)",
                "anatomical_target": "Nivelele submentonier/submandibular (I), jugulocarotidian superior/mediu/inferior (II-IV), triunghi posterior (V)",
                "landmarks": "Mușchiul sternocleidomastoidian, pachetul vascular carotido-jugular",
                "normal_aspect": "Ganglioni ovalari cu hil grăsos hiperecogen prezent, semnal Doppler exclusiv hilar central, ax scurt <6-8 mm",
            }
        ],
        "quality_criteria": [
            "Scanare bilaterală comparativă obligatorie pe toate cele 6 compartimente ganglionare cervicale",
            "Căutarea semnelor de malignitate: formă rotundă (L/S <2), absența hilului, microcalcificări, necroză chistică, vascularizație haotică periferică",
        ],
        "safety_and_limitations": ["Tehnică complet sigură (Clasa 0)"],
        "iris_reference": {
            "chapter": "Gât & Părți Moi Cervicale",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Orice adenopatie cu caractere suspecte (pierderea hilului, corticală excentrică) impune consemnarea exactă a nivelului anatomic conform clasificării Robbins.",
    },
    {
        "title": "Ecografie de Părți Moi Subcutanate (Formațiuni, Lipom, Colecție)",
        "slug": "eco-parti-moi-lipom-colectie",
        "category": "parti-moi-endocrin",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Formațiune subcutanată palpabilă (suspiciune de lipom, chist sebaceu/epidermoid, hemangiom)",
            "Suspiciune de colecție lichidiană, abces, hematom posttraumatic sau serom postoperator",
            "Corpi străini radiotransparenți subcutanați (lemn, spini, sticlă)",
            "Hernii parietale abdominale (epigastrică, ombilicală, Spiegel, inghinală)",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Fără pregătire specială; poziționare adaptată regiunii anatomice afectate.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară de înaltă frecvență 10.0 - 18.0 MHz (cu pernuță de gel / standoff pad la leziuni exofitice)",
            "patient_position": "Adaptată zonei de interes; manevră Valsalva pentru hernii parietale",
            "gel_acoustic_window": "Strat generos de gel ecografic pentru evitarea compresiei exagerate a structurilor superficiale",
        },
        "technical_settings": {
            "preset": "Musculoskeletal / Superficial Parts",
            "modes": "Mod B + Doppler Color (CFM) cu PRF jos (pentru fluxuri sanguine lente) + Elastografie",
            "focus_depth": "Focalizare foarte superficială (0.5 - 2.5 cm)",
            "gain_thi": "THI optimizat",
            "measurements_criteria": "Trei dimensiuni ortogonale, distanța față de tegument și raportul cu fascia profundă musculară",
        },
        "standard_views": [
            {
                "view": "Secțiuni ortogonale (longitudinal și transversal) centrate pe formațiune",
                "anatomical_target": "Tegument, hipoderm (țesut celular subcutanat), fascie profundă, mușchi subiacent",
                "landmarks": "Linia hiperecogenă a fasciei musculare profunde",
                "normal_aspect": "Planuri tisulare paralele regulate; lipomul apare ovalar, izo-/hiperecogen, compresibil, paralel cu tegumentul, avascular",
            }
        ],
        "quality_criteria": [
            "Scanare fără compresie excesivă pentru a nu colaba vasele mici sau deforma leziunea",
            "Verificarea semnalului Doppler Color pentru excluderea anevrismelor sau malformațiilor arteriovenoase",
        ],
        "safety_and_limitations": ["Leziunile profunde subfasciale mari pot necesita completare prin examen IRM"],
        "iris_reference": {
            "chapter": "Aparat Locomotor & Părți Moi",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Chistul sebaceu (epidermoid) prezintă caracteristic întărire acustică posterioară și adesea un traiect punctiform ('punctum') către epiderm.",
    },
    {
        "title": "Ecografie a Glandelor Salivare (Parotidă și Submandibulară)",
        "slug": "eco-glande-salivare-parotida-submandibulara",
        "category": "parti-moi-endocrin",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Tumefacție parotidiană sau submandibulară acută sau cronică",
            "Suspiciune de litiază salivară (sialolitiază, colică salivară prandială)",
            "Formațiuni tumorale salivare (adenom pleomorf, tumoră Warthin)",
            "Sialadenită acută bacteriană / virală (oreion), sindrom Sjögren",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Fără pregătire specială; stimularea secreției salivare (suc de lămâie) poate fi utilizată pentru dilatarea ductului Stenon/Wharton.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară 7.5 - 14.0 MHz",
            "patient_position": "Decubit dorsal cu capul deflectat și ușor rotit",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Small Parts / Salivary Glands",
            "modes": "Mod B + Doppler Color (pentru diferențierea vaselor de ductele dilatate)",
            "focus_depth": "Focalizare la 1.5 - 3.5 cm",
            "gain_thi": "THI activat pentru evidențierea calculilor hiperecogeni cu con de umbră",
            "measurements_criteria": "Dimensiuni glandulare, calibru duct principal (Warton / Stenon <2 mm), dimensiuni noduli",
        },
        "standard_views": [
            {
                "view": "Secțiune longitudinală și transversală parotidiană",
                "anatomical_target": "Lobul superficial parotidian, vena retromandibulară, artera carotidă externă",
                "landmarks": "Ramul mandibulei anterior, conductul auditiv extern superior",
                "normal_aspect": "Parenchim hiperecogen omogen comparativ cu mușchiul maseter, fără ganglioni măriți patologic",
            },
            {
                "view": "Secțiune submandibulară",
                "anatomical_target": "Glanda submandibulară și ductul Wharton",
                "landmarks": "Pântecele anterior al mușchiului digastric și mușchiul milohioidian",
                "normal_aspect": "Ecostructură triunghiulară omogenă, duct Wharton colabat invizibil sau <1.5 mm",
            }
        ],
        "quality_criteria": [
            "Examinare bilaterală comparativă obligatorie",
            "Urmărirea ductului Stenon pe fața externă a mușchiului maseter până la emergența bucală",
        ],
        "safety_and_limitations": ["Lobul profund parotidian este parțial mascat de ramul osos mandibular (poate necesita IRM)"],
        "iris_reference": {
            "chapter": "Gât & Părți Moi Cervicale",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Calculii salivari apar ca focare intens hiperecogene cu con de umbră posterior net și dilatație ductală în amonte.",
    },

    # -----------------------------------------------------------------------
    # 3. VASCULAR / ECOGRAFIE DOPPLER
    # -----------------------------------------------------------------------
    {
        "title": "Ecografie Doppler a Arterelor Carotide și Vertebrale (Vase Cervico-Cerebrale)",
        "slug": "eco-doppler-carotidian-si-vertebral",
        "category": "vascular-doppler",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Accident vascular cerebral ischemic (AVC), atac ischemic tranzitor (AIT), amauroză fugace",
            "Suflu carotidian asimptomatic depistat stetacustic",
            "Screening ateromatos la pacienți cu factori de risc cardiovascular multipli",
            "Monitorizare post-endarterectomie carotidiană sau angioplastie cu stent",
            "Sindrom de furt subclavicular, vertij de cauză hemodinamică",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Fără pregătire specială; relaxarea musculaturii gâtului, fără vorbire în timpul achiziției spectrelor Doppler.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară Vasculară 5.0 - 10.0 MHz (cu opțiune de sondă convexă la bifurcații înalte sau gât scurt/obez)",
            "patient_position": "Decubit dorsal, capul ușor deflectat și rotit la 45° contralateral",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Carotid / Cerebrovascular",
            "modes": "Triplex: Mod B (2D IMT) + Doppler Color (CFM) + Doppler Spectral Pulsat (PW)",
            "focus_depth": "Focalizare la adâncimea bulbului carotidian (2.5 - 4.5 cm)",
            "gain_thi": "Ajustare unghi Doppler riguros la ≤60°; eșantion de volum plasat în centrul fluxului laminar",
            "measurements_criteria": "Grosime intimă-medie (IMT normal <0.9 mm), Viteză Sistolică Maximă (PSV), Viteză Telediastolică (EDV), Raport PSV ACI / ACC",
        },
        "standard_views": [
            {
                "view": "Secțiune longitudinală carotidiană (ACC, Bifurcație, ACI, ACE)",
                "anatomical_target": "Artera carotidă comună, sinusul carotidian, carotida internă și externă",
                "landmarks": "ACI este posterior-laterală, fără ramuri cervicale; ACE este anterior-medială cu ramuri",
                "normal_aspect": "Pereți supli cu IMT normal, flux laminar, spectru Doppler ACI cu rezistență joasă (diastolă largă)",
            },
            {
                "view": "Secțiune transversală carotidiană",
                "anatomical_target": "Estimarea ariei stenozei și morfologia plăcii de aterom",
                "landmarks": "Artera carotidă comună medial și vena jugulară internă lateral",
                "normal_aspect": "Lumen complet anecogen, fără plăci hipo/hiperecogene, umplere color omogenă",
            },
            {
                "view": "Secțiune longitudinală posterioară (Segment V2 arteră vertebrală)",
                "anatomical_target": "Artera și vena vertebrală între procesele transverse",
                "landmarks": "Conurile de umbră paralele ale apofizelor transverse cervicale (C6-C2)",
                "normal_aspect": "Flux anterograd cranial, spectru de rezistență joasă, calibru normal >2 mm",
            },
        ],
        "quality_criteria": [
            "Măsurarea obligatorie a unghiului de insonare Doppler la exact ≤60° pentru cuantificarea vitezelor",
            "Gradarea stenozei carotidiene conform criteriilor de consens NASCET / SRU (PSV <125 cm/s: <50%; PSV 125-230: 50-69%; PSV >230 cm/s: ≥70%)",
            "Descrierea compoziției plăcii (omogenă fibroasă, hipoecogenă lipidică instabilă, ulcerată sau calcificată)",
        ],
        "safety_and_limitations": ["Tehnică complet non-ionizantă, non-invazivă"],
        "iris_reference": {
            "chapter": "Aparat Cardiovascular & Vase",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "În cazul unei stenoze strânse (preocluzive), vitezele pot scădea paradoxal (string sign / trickling flow). Se impune utilizarea Doppler-ului Power și a PRF-ului scăzut.",
    },
    {
        "title": "Ecografie Doppler Venos al Membrelor Inferioare (Tromboză Venoasă Profundă & Insuficiență)",
        "slug": "eco-doppler-venos-membru-inferior",
        "category": "vascular-doppler",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Suspiciune clinică de Tromboză Venoasă Profundă (TVP) — edem unilateral, durere, căldură locală, semn Homans pozitiv",
            "Suspiciune de trombembolism pulmonar (TEP) la pacient cu focar embolic necunoscut",
            "Insuficiență venoasă cronică, boală varicoasă, ulcer venos de gambă",
            "Tromboflebită superficială (safenă mare / mică) și evaluarea extensiei către crosa safeno-femurală",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Fără pregătire specială; decubit dorsal pentru sistemul venos profund femural; ortostatism pentru cartografierea refluxului varicos.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară Vasculară 5.0 - 12.0 MHz (sondă convexă opțională la pacienți obezi pentru axul iliac)",
            "patient_position": "Decubit dorsal cu rotație externă a membrului inferior (genunchi ușor flectat) și ortostatism pentru reflux",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Venous Lower Extremity",
            "modes": "Mod B cu manevră de compresie (CUS) + Doppler Color + Doppler Spectral Pulsat (modulație respiratorie)",
            "focus_depth": "Focalizare adaptată adâncimii pachetului venos (2 - 6 cm)",
            "gain_thi": "PRF coborât (Color Velocity Scale 10-15 cm/s) pentru fluxuri venoase lente",
            "measurements_criteria": "Compresibilitate completă în plan transversal (CUS); durată reflux venos (>0.5 s pentru safene, >1.0 s pentru vene profunde)",
        },
        "standard_views": [
            {
                "view": "Secțiune transversală cu compresie mecanică (CUS la fiecare 1-2 cm)",
                "anatomical_target": "Vena femurală comună, joncțiunea safeno-femurală, vena femurală profundă și superficială",
                "landmarks": "Artera femurală lateral, vena medial; compresie completă cu transductorul până la colabarea totală a lumenului",
                "normal_aspect": "Colabare completă a pereților venoși ('semnul ochiului care clipește'); absența materialului ecogen endoluminal",
            },
            {
                "view": "Secțiune transversală și longitudinală în fosa poplitee",
                "anatomical_target": "Vena poplitee și joncțiunea safeno-poplitee",
                "landmarks": "Vena poplitee situată superficial față de artera poplitee",
                "normal_aspect": "Lumen complet compresibil, flux spontan modulat respirator, augmentare la compresie distală pe gambă",
            },
            {
                "view": "Evaluarea venelor gambiere (tibiale posterioare, peroniere, gastrocnemiene)",
                "anatomical_target": "Axele venoase profunde infrapatelare pereche",
                "landmarks": "Artera satelită între cele două vene tributare",
                "normal_aspect": "Compresibilitate completă, semnal Doppler color prezent la manevra de stoarcere musculară",
            },
        ],
        "quality_criteria": [
            "Criteriul de diagnostic cert pentru TVP este ABSENȚA compresibilității complete a lumenului venos la presiunea cu sonda",
            "Testarea manevrei Valsalva și a augmentării la compresia gambei",
            "Consemnarea caracterului trombului (recent/hipoecogen mobil vs. vechi/hiperecogen retractil aderent)",
        ],
        "safety_and_limitations": ["Nu se exercită compresie mecanică violentă pe trombi proaspeți flotanți din cauza riscului de embolizare"],
        "iris_reference": {
            "chapter": "Aparat Cardiovascular & Vase",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Protocolul CUS în 2 puncte (femural comun și popliteu) sau complet pe întreg membrul este metoda de elecție absolută conform Ghidului Național IRIS.",
    },
    {
        "title": "Ecografie Doppler Arterial al Membrelor Inferioare",
        "slug": "eco-doppler-arterial-membru-inferior",
        "category": "vascular-doppler",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Claudicație intermitentă (durere la mers la distanță fixă)",
            "Durere ischemică de repaus, extremități reci, palide sau cianotice",
            "Ulcere ischemice periferice sau gangrenă digitală",
            "Abolirea sau diminuarea pulsurilor periferice (femural, popliteu, tibial posterior, pedios)",
            "Monitorizare post-bypass arterial periferic sau angioplastie percutană",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Repaus fizic culcat 10-15 minute anterior examinării pentru stabilizarea hemodinamică.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară Vasculară 5.0 - 10.0 MHz + Sondă Convexă 3.5 MHz (pentru arterele iliace comune și externe)",
            "patient_position": "Decubit dorsal; decubit ventral sau lateral pentru artera poplitee",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Arterial Lower Extremity",
            "modes": "Mod B + Doppler Color + Doppler Spectral Pulsat (PW cu unghi ≤60°)",
            "focus_depth": "Focalizare adaptată vasului (3 - 7 cm)",
            "gain_thi": "PRF ajustat pentru viteze arteriale medii-înalte (50-100 cm/s)",
            "measurements_criteria": "Morfologie undă Doppler (trifazică normală vs. bifazică / monofazică stenotică), raport viteze PSV pre/post stenoză (Vr >2 indică stenoză >50%)",
        },
        "standard_views": [
            {
                "view": "Secțiune longitudinală ax femural (AFC, AFS, AFP)",
                "anatomical_target": "Artera femurală comună, superficială și profundă",
                "landmarks": "Bifurcația femurală sub ligamentul inghinal",
                "normal_aspect": "Pereți subțiri fără calcificări obstructive, flux trifazic cu componentă protodiastolică inversată",
            },
            {
                "view": "Secțiune longitudinală ax popliteu și trunchi tibio-peronier",
                "anatomical_target": "Artera poplitee și bifurcația gambieră",
                "landmarks": "Artera poplitee profundă față de vena poplitee în spațiul popliteu",
                "normal_aspect": "Flux trifazic cu PSV 60-90 cm/s, absența anevrismului popliteu",
            },
            {
                "view": "Secțiune longitudinală artere gambiere (tibială anterioară, posterioară, pedioasă)",
                "anatomical_target": "Artera tibială posterioară retromaleolar și artera pedioasă pe fața dorsală a piciorului",
                "landmarks": "Maleola internă (ATP) și oasele tarsiene (AP)",
                "normal_aspect": "Lumen permeabil, flux pulsatil prezent",
            }
        ],
        "quality_criteria": [
            "Înregistrarea spectrului Doppler spectral pe toate cele 3 axe majore (femural, popliteu, gambier)",
            "Identificarea tranziției de la spectru trifazic la spectru monofazic (tardus-parvus) ce semnalează stenoză hemodinamică în amonte",
        ],
        "safety_and_limitations": ["Calcificările masive de tip Mönckeberg (diabet, uremie) pot genera con de umbră ce împiedică insonarea adecvată"],
        "iris_reference": {
            "chapter": "Aparat Cardiovascular & Vase",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Ecografia Doppler arterială este metoda neinvazivă inițială esențială de stadializare a arteriopatiei obliterante conform clasificării Leriche-Fontaine.",
    },
    {
        "title": "Ecografie Doppler a Aortei Abdominale (Screening & Monitorizare Anevrism)",
        "slug": "eco-doppler-aorta-abdominala-anevrism",
        "category": "vascular-doppler",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Screening pentru Anevrismul de Aortă Abdominală (AAA) la bărbați >65 ani fumători",
            "Masă pulsatilă abdominală descoperită la examenul clinic",
            "Monitorizarea periodică a diametrului anevrismelor de aortă abdominală cunoscute (<55 mm)",
            "Evaluarea extensiei către arterele iliace și excluderea disecției de aortă abdominală",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "À jeun 6 ore pentru reducerea gazelor intestinale suprapuse peste retroperitoneu.",
        "transducers_equipment": {
            "transducer_types": "Sondă Convexă Abdominală 3.0 - 5.0 MHz",
            "patient_position": "Decubit dorsal; compresie gradată lentă pentru îndepărtarea anselor intestinale",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Abdominal Vascular / Aorta",
            "modes": "Mod B de înaltă precizie dimensională + Doppler Color + Doppler Spectral",
            "focus_depth": "Focalizare pe peretele posterior aortic (7 - 12 cm)",
            "gain_thi": "THI activat pentru delimitarea precisă a peretelui extern aortic",
            "measurements_criteria": "Diametru transversal și anteroposterior maxim măsurat strict din perete extern în perete extern (outer-to-outer)",
        },
        "standard_views": [
            {
                "view": "Secțiune transversală de la diafragm la bifurcație",
                "anatomical_target": "Aorta proximală, juxtarenală, infrarenală și arterele iliace comune",
                "landmarks": "Arterele renale emergente, bifurcația aortică la nivelul vertebrei L4",
                "normal_aspect": "Diametru transversal descendent normal <20 mm (ectazie 20-29 mm; AAA definit la ≥30 mm)",
            },
            {
                "view": "Secțiune longitudinală mediană",
                "anatomical_target": "Axa lungă a aortei abdominale",
                "landmarks": "Trunchiul celiac și artera mezenterică superioară anterior",
                "normal_aspect": "Pereți paraleli fără bombare fuziformă sau saculară, absența trombozei murale",
            }
        ],
        "quality_criteria": [
            "Măsurătoarea outer-to-outer în secțiune strict perpendiculară pe axul longitudinal al vasului",
            "Măsurarea grosimii trombului mural și a lumenului circulant rezidual prin Doppler color",
        ],
        "safety_and_limitations": ["În caz de anevrism rapid progresiv (>10 mm/an) sau >50-55 mm, se recomandă Angio-CT pentru planificare terapeutică chirurgicală/EVAR"],
        "iris_reference": {
            "chapter": "Aparat Cardiovascular & Vase",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Anevrismul este definit la un diametru transversal ≥30 mm. Pragul de intervenție chirurgicală sau endovasculară este de 55 mm la bărbați și 50 mm la femei.",
    },

    # -----------------------------------------------------------------------
    # 4. MUSCULOSCHELETIC (MSK)
    # -----------------------------------------------------------------------
    {
        "title": "Ecografie de Umăr și a Coafei Rotatorilor",
        "slug": "eco-umar-coafa-rotatorilor",
        "category": "msk",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Durere de umăr (omalgie), impotență funcțională, sindrom de impingement subacromial",
            "Suspiciune de ruptură parțială sau completă de coafă a rotatorilor",
            "Tendinopatie calcifiantă de supraspinos",
            "Tendinită sau instabilitate de tendon lung al bicepsului brahial (TLBB)",
            "Bursită subacromio-subdeltoidiană (SASD)",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Pacient așezat pe scaun rotativ, fără spătar, brațul mobil liber pentru manevre dinamice.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară MSK de înaltă frecvență 9.0 - 18.0 MHz",
            "patient_position": "Așezat pe scaun; poziții dinamice standardizate (Crass, Modified Crass, rotație internă/externă)",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Musculoskeletal Shoulder",
            "modes": "Mod B de înaltă rezoluție + Doppler Power/Color (pentru hiperemie inflamatorie)",
            "focus_depth": "Focalizare superficială (1.5 - 3.5 cm)",
            "gain_thi": "Ajustare riguroasă a unghiului de incidență la 90° pe tendon pentru eliminarea anizotropiei",
            "measurements_criteria": "Grosime tendoane, dimensiune ruptură (anteroposterior și retractare mediolaterală), distensie bursă SASD (>1.5-2 mm patologică)",
        },
        "standard_views": [
            {
                "view": "Șanțul bicipital (Transversal și Longitudinal)",
                "anatomical_target": "Tendonul capului lung al bicepsului (TLBB)",
                "landmarks": "Marea și mica tuberozitate humerală",
                "normal_aspect": "Tendon ovalar hiperecogen fibrilar bine centrat în culisă, fără revărsat peritendinos marcat",
            },
            {
                "view": "Incidență anterioară în rotație externă",
                "anatomical_target": "Tendonul subscapular",
                "landmarks": "Mica tuberozitate și procesul coracoid",
                "normal_aspect": "Tendon fibrilar continuu care se inseră ferm pe mica tuberozitate",
            },
            {
                "view": "Poziția Crass Modificată (mâna la buzunarul de la spate)",
                "anatomical_target": "Tendonul supraspinos și bursa SASD",
                "landmarks": "Capul humeral convex ('anvelopa') și marginea acromială",
                "normal_aspect": "Structură 'în cioc de papagal' hiperecogenă continuă, fără defect hipoecogen transmural sau corticală deșirată",
            },
            {
                "view": "Incidență posterioară (cu mâna pe umărul opus)",
                "anatomical_target": "Tendonul infraspinos, rotund mic și labrumul glenoidian posterior",
                "landmarks": "Interlinia articulară glenohumerală posterioară",
                "normal_aspect": "Tendoane regulate, absența chisturilor paralabrale sau a distensiei articulare posterioare",
            },
        ],
        "quality_criteria": [
            "Explorarea dinamică a impingementului subacromial în timpul abducției active a brațului",
            "Evitarea erorilor de anizotropie prin menținerea fasciculului strict perpendicular pe fibrele tendinoase",
        ],
        "safety_and_limitations": ["Tehnică sigură; rupturile masive retractate medial sub acromion pot necesita confirmare IRM"],
        "iris_reference": {
            "chapter": "Aparat Locomotor & Părți Moi",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Anizotropia (înnegrirea artificială a tendonului la angulație oblică a sondei) este principala capcană ce poate simula o ruptură tendinoasă fals-pozitivă.",
    },
    {
        "title": "Ecografie de Genunchi și a Aparatului Extensor",
        "slug": "eco-genunchi-si-aparat-extensor",
        "category": "msk",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Durere anterioară de genunchi, suspiciune de tendinopatie rotuliană (jumper's knee) sau cvadricipitală",
            "Hidartroză / revărsat articular în recesul suprapatelar",
            "Tumefacție poplitee, suspiciune de chist sinovial Baker (rupt sau intact)",
            "Leziuni ale ligamentelor colaterale (LCM / LCL)",
            "Boala Osgood-Schlatter la adolescenți",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Decubit dorsal cu genunchiul flectat la 30° pentru recesul anterior; decubit ventral pentru fosa poplitee.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară MSK 7.5 - 15.0 MHz",
            "patient_position": "Decubit dorsal (compartiment anterior/medial/lateral) și decubit ventral (fosa poplitee)",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "MSK Knee",
            "modes": "Mod B + Doppler Color/Power (pentru sinovită activă și hiperemie peritendinoasă)",
            "focus_depth": "Focalizare superficială (1.5 - 4.0 cm)",
            "gain_thi": "THI activat",
            "measurements_criteria": "Grosime tendon cvadricipital și rotulian (<4.5-5 mm), dimensiune reces suprapatelar, ax lung/lățime chist Baker",
        },
        "standard_views": [
            {
                "view": "Secțiune longitudinală suprapatelară (în flexie 30°)",
                "anatomical_target": "Tendon cvadricipital, recesul sinovial suprapatelar, grăsimea prefemurală",
                "landmarks": "Baza rotulei inferior, corticala femurului posterior",
                "normal_aspect": "Tendon fibrilar omogen, reces sinovial virtual fără lamă lichidiană >2 mm",
            },
            {
                "view": "Secțiune longitudinală infrapatelară",
                "anatomical_target": "Tendon rotulian, bursa infrapatelară profundă, tuberozitatea tibială",
                "landmarks": "Vârful rotulei și tuberozitatea anterioară a tibiei (TAT)",
                "normal_aspect": "Fibre hiperecogene paralele compacte, fără arii hipoecogene la inserții",
            },
            {
                "view": "Secțiune transversală și longitudinală în fosa poplitee",
                "anatomical_target": "Recesul gastrocnemio-semimembranos (Chistul Baker)",
                "landmarks": "Tendonul semimembranos medial și capul medial al gastrocnemianului",
                "normal_aspect": "Formațiune lichidiană anecogenă cu colet ('gât') specific de comunicare între cei doi mușchi",
            },
        ],
        "quality_criteria": [
            "Verificarea coletului de comunicare articulară a oricărui chist popliteu pentru a certifica natura de chist Baker",
            "Ligamentele încrucișate (LIA/LIP) și meniscurile profunde nu pot fi evaluate complet ecografic (necesită IRM Genunchi)",
        ],
        "safety_and_limitations": ["Leziunile intraarticulare profunde sunt apanajul IRM"],
        "iris_reference": {
            "chapter": "Aparat Locomotor & Părți Moi",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Ruperea unui chist Baker mimează clinic o tromboză venoasă profundă de gambă (pseudotromboflebită). Ecografia rezolvă rapid diagnosticul diferențial.",
    },
    {
        "title": "Ecografie de Tendon Achilean, Gleznă și Fascie Plantară",
        "slug": "eco-tendon-achilean-si-glezna",
        "category": "msk",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Durere posterioară de călcâi, suspiciune de ruptură parțială sau totală de tendon ahilean",
            "Tendinopatie ahileană inserțională sau non-inserțională, entezită",
            "Fascită plantară, durere la primii pași de dimineață în călcâi",
            "Entorse de gleznă (leziune ligament talofibular anterior - LTFA, calcaneofibular - LCF)",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Decubit ventral cu picioarele atârnând liber la marginea mesei de examinare; manevre dinamice de flexie dorsală/plantară.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară MSK 9.0 - 18.0 MHz de înaltă rezoluție",
            "patient_position": "Decubit ventral cu piciorul în afara mesei pentru tendonul achilean; decubit dorsal pentru glezna anterioară/laterală",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "MSK Ankle & Foot",
            "modes": "Mod B + Doppler Power (pentru neovascularizație în tendinopatii cronice)",
            "focus_depth": "Focalizare superficială (1.0 - 2.5 cm)",
            "gain_thi": "Fascicul perpendicular pe fibrele ahileene pentru evitarea anizotropiei",
            "measurements_criteria": "Grosime AP tendon achilean (normal 4 - 6 mm); grosime fascie plantară la inserția pe calcaneu (normal <4.0 mm)",
        },
        "standard_views": [
            {
                "view": "Secțiune longitudinală a tendonului achilean",
                "anatomical_target": "Joncțiune miotendinoasă, corp tendinos, inserție pe calcaneu, bursă retrocalcaneană",
                "landmarks": "Tendonul deasupra grăsimii Kager, inserția pe tuberozitatea posterioară a calcaneului",
                "normal_aspect": "Benzi fibrilare paralele hiperecogene continue, grosime constantă, fără diastazis sau colecție în bursa retrocalcaneană",
            },
            {
                "view": "Secțiune transversală a tendonului achilean",
                "anatomical_target": "Morfologia eliptică a tendonului",
                "landmarks": "Contur anterior plat sau ușor concav, margini convexe",
                "normal_aspect": "Arie transversală omogenă, contur neted, absența ariei hipoecogene focale",
            },
            {
                "view": "Secțiune longitudinală a fasciei plantare",
                "anatomical_target": "Inserția entezică a fasciei plantare pe tuberculul medial al calcaneului",
                "landmarks": "Tuberozitatea inferioară a calcaneului",
                "normal_aspect": "Bandă fibrilară hiperecogenă compactă cu grosime <4 mm, fără hiperemie Doppler",
            },
        ],
        "quality_criteria": [
            "Testarea dinamică a discontinuității în dorsiflexie pasivă la suspiciunea de ruptură completă (diastazisul capetelor tendinoase)",
            "Documentarea prezenței neovascularizației intratendinoase prin Doppler Power în tendinopatiile cronice",
        ],
        "safety_and_limitations": ["Procedură complet sigură"],
        "iris_reference": {
            "chapter": "Aparat Locomotor & Părți Moi",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Ruptura de tendon achilean apare cel mai frecvent la 2-6 cm proximal de inserția calcaneană (zona critică hipovascularizată).",
    },

    # -----------------------------------------------------------------------
    # 5. SENOLOGIE / SÂN
    # -----------------------------------------------------------------------
    {
        "title": "Ecografie Mamară Bilaterală și Axilară (Clasificare BI-RADS US)",
        "slug": "eco-mamara-bilaterala-birads",
        "category": "san",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Nodul mamar palpabil sau scurgere mamelonară",
            "Metodă de primă linie la femei tinere (<40 ani), gravide sau care alăptează",
            "Completare obligatorie a mamografiei la sâni denși (densitate mamară tip C și D ACR)",
            "Caracterizarea leziunilor nodulare (chist simplu vs. masă solidă)",
            "Ghidaj pentru puncție biopsie mamară percutană (Core Biopsy)",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "Decubit dorsal cu brațul de partea examinată ridicat deasupra capului pentru aplatizarea glandei pe torace.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară de înaltă frecvență 10.0 - 18.0 MHz (High-Frequency Matrix Linear)",
            "patient_position": "Decubit dorsal, completat cu poziție oblică la 30-45° cu perniță sub spate pentru cadranele externe",
            "gel_acoustic_window": "Gel ecografic abundent",
        },
        "technical_settings": {
            "preset": "Breast High Resolution",
            "modes": "Mod B + Doppler Color/Power + Elastografie (Strain Ratio / Shear-Wave)",
            "focus_depth": "Focalizare multiplă adaptată la nivelul zonei premamare, glandulare și retromamare",
            "gain_thi": "THI activat pentru diferențierea optimă a chisturilor cu conținut dens de tumorile solide",
            "measurements_criteria": "Trei dimensiuni ortogonale pentru fiecare nodul, orientare (paralelă vs. non-paralelă taller-than-wide), margini, ecogenitate, atenuare posterioară",
        },
        "standard_views": [
            {
                "view": "Scanare radială și antiradială / cadrane (cadran cu cadran)",
                "anatomical_target": "Toate cele 4 cadrane mamare, regiunea retroareolară și prelungirea axilară",
                "landmarks": "Sistemul cadranar / orar (ex: ora 2 la 3 cm de mamelon) și profunzimea (1-3)",
                "normal_aspect": "Repartiție armonioasă a țesutului fibroglandular hiperecogen și a grăsimii subcutanate, canale galactofore <2 mm",
            },
            {
                "view": "Explorarea regiunii axilare bilaterale",
                "anatomical_target": "Ganglionii limfatici axilari (nivelele Berg I-III)",
                "landmarks": "Vena axilară și mușchiul pectoral mare",
                "normal_aspect": "Ganglioni ovalari cu hil adipos hiperecogen conservat, corticală subțire și uniformă <3 mm",
            }
        ],
        "quality_criteria": [
            "Concluzionarea obligatorie a fiecărei leziuni și a examinării globale într-o categorie standardizată BI-RADS US (1 până la 6)",
            "Documentarea elastografică: leziunile maligne sunt tipic rigide (scor mare de duritate / viteză mare de propagare a undei de forfecare)",
        ],
        "safety_and_limitations": [
            "Complet non-iradiantă (Clasa 0); ecografia mamară nu înlocuiește screeningul mamografic la femeile peste 40 de ani în privința microcalcificărilor izolate",
        ],
        "iris_reference": {
            "chapter": "Senologie & Patologie Mamară",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Categoriile BI-RADS 3 impun monitorizare ecografică la 6 luni. Categoriile BI-RADS 4 și 5 impun biopsie histologică ghidată ecografic.",
    },

    # -----------------------------------------------------------------------
    # 6. PEDIATRIE
    # -----------------------------------------------------------------------
    {
        "title": "Ecografie Transfontanelară (ETF) la Nou-Născut și Sugar",
        "slug": "eco-transfontanelara-nou-nascut",
        "category": "pediatrie",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Screening la nou-născuți prematuri (<32 săptămâni) sau cu greutate mică la naștere (<1500 g)",
            "Suspiciune de hemoragie peri-intraventriculară (HPIV) sau leucomalacie periventriculară (LPV)",
            "Asfixie perinatală, encefalopatie hipoxico-ischemică",
            "Creștere rapidă a perimetrului cranian, suspiciune de hidrocefalie",
            "Screening malformații cerebrale congenitale sau infecții TORCH",
        ],
        "contraindications": [
            "Fontanelă anterioară închisă complet sau suturi sinostozate",
        ],
        "patient_prep": "Sugar calm, preferabil alimentat anterior; capul stabilizat cu blândețe de către asistent sau părinte; gel încălzit la temperatura corpului.",
        "transducers_equipment": {
            "transducer_types": "Sondă Microconvexă / Phased-Array Pediatrică 5.0 - 8.0 MHz + Sondă Liniară 8.0 - 15.0 MHz (pentru spațiul subarahnoidian și cortex)",
            "patient_position": "Decubit dorsal în incubator sau pe masa de examinare",
            "gel_acoustic_window": "Gel ecografic hipoalergenic cald aplicat pe fontanela anterioară",
        },
        "technical_settings": {
            "preset": "Neonatal Head / Neuro",
            "modes": "Mod B de înaltă rezoluție + Doppler Color și Doppler Pulsat pe artera cerebrală anterioară (ACA)",
            "focus_depth": "Focalizare de la nivelul corpului calos până la fosa posterioară (4 - 8 cm)",
            "gain_thi": "Optimizat pentru țesut cerebral pediatric",
            "measurements_criteria": "Indice ventricular Levene, lățime corn frontal, diametru talamo-occipital, indice de rezistivitate pe ACA (IR normal 0.65 - 0.75)",
        },
        "standard_views": [
            {
                "view": "Secțiuni coronale standardizate prin fontanela anterioară (6 planuri: de la lobii frontali la occipitali)",
                "anatomical_target": "Lobi frontali, coarne frontale ventriculare, orificiile Monro, corpul ventriculilor laterali, trigonul și parenchimul occipital",
                "landmarks": "Planul coronal 3 la nivelul orificiilor Monro și plexurilor coroide din ventriculul III",
                "normal_aspect": "Ventriculi simetrici, substanță albă periventriculară fin ecogenă (ecogenitate inferioară plexului coroid)",
            },
            {
                "view": "Secțiuni sagitale și parasagitale (median și prin ventriculii laterali bilateral)",
                "anatomical_target": "Corpul calos, ventriculul III, trunchiul cerebral, vermisul cerebelos, șanțul caudotalamic",
                "landmarks": "C-ul corpului calos pe secțiunea medio-sagitală; șanțul caudotalamic pe parasagital",
                "normal_aspect": "Corp calos prezent, vermis cerebelos dezvoltat, absența cheagurilor în șanțul caudotalamic (sediul predilect al HPIV grad I)",
            }
        ],
        "quality_criteria": [
            "Gradarea hemoragiei peri-intraventriculare conform clasificării Papile (Gradele I - IV)",
            "Măsurarea indicelui de rezistivitate (IR) pe artera cerebrală anterioară pentru evaluarea presiunii intracraniene",
        ],
        "safety_and_limitations": [
            "Complet inofensivă, repetabilă la patul bolnavului în terapie intensivă neonatală (TINN)",
        ],
        "iris_reference": {
            "chapter": "Pediatrie & Neonatologie",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Examinare de primă linie la toți prematurii în primele 3-7 zile de viață pentru detectarea precoce a hemoragiei de matrice germinativă.",
    },
    {
        "title": "Ecografie de Șold la Sugar (Screeningul Displaziei de Dezvoltare - Metoda Graf)",
        "slug": "eco-sold-sugar-screening-displazie",
        "category": "pediatrie",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Screening universal sau țintit pentru Displazia de Dezvoltare a Șoldului (DDH) la vârsta de 4-6 săptămâni",
            "Factori de risc prezenți: prezentație pelviană, istoric familial de luxație de șold, oligohidramnios",
            "Semne clinice de instabilitate la examenul ortopedic pediatric (semnul Ortolani, Barlow pozitiv)",
            "Asimetrie de pliuri coxo-femurale, inegalitate aparentă de membre inferioare (semn Galeazzi)",
        ],
        "contraindications": ["Vârsta >6-8 luni cu osificare avansată a nucleului capului femural (după această vârstă se indică Rx Bazin)"],
        "patient_prep": "Sugar liniștit, alimentat recent; îmbrăcăminte lejeră în jumătatea inferioară.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară Pediatrică 7.5 - 12.0 MHz",
            "patient_position": "Decubit lateral strict (drept apoi stâng) pe un suport dedicat sau susținut de părinte",
            "gel_acoustic_window": "Gel ecografic apos călduț",
        },
        "technical_settings": {
            "preset": "Pediatric Hip / Graf",
            "modes": "Mod B de înaltă rezoluție fără THI excesiv (pentru a păstra conturul neted al reperelor osoase)",
            "focus_depth": "Focalizare pe acetabul și capul femural (2.0 - 4.5 cm)",
            "gain_thi": "Gain reglat pentru definirea clară a limbusului cartilaginos și a sprâncenei osoase acetabulare",
            "measurements_criteria": "Unghiul alfa (α - acoperirea osoasă a acetabulului) și unghiul beta (β - acoperirea cartilaginoasă)",
        },
        "standard_views": [
            {
                "view": "Secțiune coronală standardizată prin mijlocul acetabulului (Planul Standard Graf)",
                "anatomical_target": "Sprânceana osoasă acetabulară, marginea inferioară a ilionului, labrumul acetabular",
                "landmarks": "Prezența obligatorie a 3 repere pe aceeași imagine: linia iliacă rectilinie, sprânceana osoasă și labrumul cartilaginos",
                "normal_aspect": "Șold de Tip Ia / Ib conform Graf: Unghi alfa ≥ 60° (acoperire osoasă adecvată) și unghi beta < 55°",
            }
        ],
        "quality_criteria": [
            "Imaginea este validă pentru măsurători cantitative doar dacă respectă cele 3 criterii anatomice de validare Graf",
            "Încadrarea șoldului în tipurile Graf: Tip I (Normal, alfa ≥60°), Tip IIa/IIb (Fiziologic imatur / Întârziat, alfa 50-59°), Tip IIc/D (Risc înalt/Decentrat), Tip III/IV (Luxat/Ecentrat)",
        ],
        "safety_and_limitations": ["Tehnică complet sigură, elimină iradierea gonadică a sugarului"],
        "iris_reference": {
            "chapter": "Pediatrie & Neonatologie",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "Ecografia Graf efectuată precoce (4-6 săptămâni) permite tratamentul conservator simplu cu ham Pavlik, evitând chirurgia complexă a luxației neglijate.",
    },
    {
        "title": "Ecografie Abdominală Pediatrică (Apendicită Acută & Stenoză Hipertrofică de Pilor)",
        "slug": "eco-abdomen-pediatric-apendicita-pilor",
        "category": "pediatrie",
        "modality": "eco",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "last_updated": "2026-09-13",
        "clinical_indications": [
            "Vărsături explozive 'în jet' la sugarul de 2-8 săptămâni (suspiciune de Stenoză Hipertrofică de Pilor - SHP)",
            "Durere în fosa iliacă dreaptă, febră, apărare musculară la copil (suspiciune de Apendicită Acută)",
            "Dureri paroxistice cu plâns inconsolabil și scaun cu aspect de 'peltea de coacăze' (suspiciune de Invaginație Intestinală)",
            "Limfadenită mezenterică la copilul mic",
        ],
        "contraindications": ["Lipsa contraindicațiilor absolute"],
        "patient_prep": "La sugarul suspect de SHP: examinare după administrare de puțină glucoză per os pentru destinderea antrului gastric.",
        "transducers_equipment": {
            "transducer_types": "Sondă Liniară de înaltă frecvență 7.5 - 15.0 MHz (esențială pentru apendice și pilor) + Sondă Convexă Pediatrică 5.0 MHz",
            "patient_position": "Decubit dorsal, completat cu decubit oblic drept la sugar pentru deplasarea conținutului gastric în pilor",
            "gel_acoustic_window": "Gel ecografic încălzit",
        },
        "technical_settings": {
            "preset": "Pediatric Abdomen / Pylorus / Appendix",
            "modes": "Mod B cu compresie gradată blândă + Doppler Color",
            "focus_depth": "Focalizare superficială pe ansele intestinale și pilor (2.0 - 5.0 cm)",
            "gain_thi": "THI activat pentru evidențierea stratificării parietale digestive",
            "measurements_criteria": "Pilor: grosime musculară (>3.0 mm) și lungime canal piloric (>15-16 mm); Apendice: diametru transversal extern (>6 mm) și incompresibilitate",
        },
        "standard_views": [
            {
                "view": "Secțiune transversală și longitudinală pe canalul piloric (la sugar)",
                "anatomical_target": "Canalul piloric între antru și bulbul duodenal",
                "landmarks": "Colecistul anterior, lobul hepatic drept superior, capul pancreasului posterior",
                "normal_aspect": "Grosimea peretelui muscular piloric <2 mm, deschidere normală a pilorului cu evacuare gastrică periodică",
            },
            {
                "view": "Secțiune oblică în fosa iliacă dreaptă cu compresie gradată (la copil)",
                "anatomical_target": "Apendice cecal și ansele ileale terminale",
                "landmarks": "Vasele iliace externe posterior, fundul cecului superior",
                "normal_aspect": "Apendice compresibil suplu cu diametru <6 mm, stratificare parietală conservată, fără coprolit hiperecogen și fără grăsime periapendiculară hiperecogenă",
            },
            {
                "view": "Secțiune transversală pe masă abdominală suspectă (invaginație)",
                "anatomical_target": "Ansa invaginată (invaginat și intussuscipiens)",
                "landmarks": "Frecvent localizată pe traiectul colonului ascendent sau transvers",
                "normal_aspect": "Absența aspectului în 'țintă' (target sign / doughnut sign) sau 'pseudorinichi'",
            },
        ],
        "quality_criteria": [
            "Efectuarea compresiei gradate blânde pentru evacuarea gazelor și reducerea distanței față de apendice",
            "Verificarea vascularizației parietale prin Doppler Color (hiperemie în apendicită incipientă, absența fluxului în faza gangrenoasă)",
        ],
        "safety_and_limitations": [
            "Evită complet iradierea CT la copil conform Ghidului IRIS (Ecografia este prima intenție absolută)",
        ],
        "iris_reference": {
            "chapter": "Pediatrie & Urgențe Abdominale",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
        },
        "notes": "La sugarul cu SHP, grosimea stratului muscular piloric ≥3.0 mm pe secțiune transversală ('semnul gogoșii') și lungimea canalului ≥15 mm confirmă diagnosticul chirurgical.",
    },
]


CATEGORIES_PAGES = {
    "abdomen-pelvis": {
        "title": "Ecografie Abdomen & Pelvis",
        "description": "Protocoale ecografice pentru examinarea organelor parenchimatoase abdominale, pelvisului ginecologic, aparatului urinar și protocolul de urgență FAST.",
    },
    "parti-moi-endocrin": {
        "title": "Ecografie Părți Moi & Endocrinologie",
        "description": "Protocoale de ultrasonografie de înaltă rezoluție pentru tiroidă (EU-TIRADS), ganglioni limfatici cervicali, glande salivare și formațiuni subcutanate.",
    },
    "vascular-doppler": {
        "title": "Ecografie Vasculară & Doppler",
        "description": "Protocoale clinice Triplex Doppler pentru vasele cervico-cerebrale, sistemul venos profund și superficial, arterele membrelor inferioare și aorta abdominală.",
    },
    "msk": {
        "title": "Ecografie Musculoscheletică (MSK)",
        "description": "Protocoale dinamice pentru articulația umărului (coafa rotatorilor), genunchiului (aparat extensor/Baker) și tendonului achilean/fasciei plantare.",
    },
    "san": {
        "title": "Ecografie Senologică (Sân)",
        "description": "Protocol standardizat de ecografie mamară bilaterală și axilară cu clasificare BI-RADS US și criterii elastografice.",
    },
    "pediatrie": {
        "title": "Ecografie Pediatrică & Neonatală",
        "description": "Protocoale non-iradiante de primă linie: ecografie transfontanelară (ETF), screeningul luxației de șold (Graf) și urgențe abdominale infantile.",
    },
}


def main():
    docs_eco = REPO_ROOT / "docs" / "eco"
    docs_eco.mkdir(parents=True, exist_ok=True)

    # 1. Creează docs/eco/index.md
    main_index = docs_eco / "index.md"
    main_index.write_text(
        """---
title: Protocoale de Ecografie & Ultrasonografie (US)
hide:
  - navigation
  - toc
---

# 📡 Protocoale de Ecografie & Ultrasonografie (US)

Protocoale clinice și tehnice de ultrasonografie convențională, Doppler color/spectral și ecografie de urgență structurate conform **Ghidului Național IRIS (Ordinul MS 1342/2012)**.

<div class="iris-official-banner" style="margin-top: 16px; margin-bottom: 24px;">
  <div class="iris-official-badge">🏛️ NON-IONIZANT &bull; CLASA 0 DE IRADIERE &bull; METODĂ DE PRIMĂ LINIE</div>
  <p class="iris-official-desc">
    Conform principiului <strong>ALARA</strong> și Ghidului IRIS, <strong>Ecografia (Ultrasonografia)</strong> este investigația de primă intenție în majoritatea afecțiunilor abdominale, pelvine, tiroidiene, vasculare și pediatrice, oferind diagnostic rapid, sigur și fără expunere la radiații ionizante.
  </p>
  <a href="../iris/" style="font-weight: 600; color: #1565c0; text-decoration: none;">
    Consultă Recomandările Ghidului Național IRIS ➔
  </a>
</div>

---

<p class="body-parts-section-heading">Categorii Clinice de Ecografie (US)</p>

<div class="body-parts-grid">
  <a href="abdomen-pelvis/" class="body-part-card" style="border-top: 3px solid #65a30d;">
    <h3>Abdomen &amp; Pelvis (FAST)</h3>
  </a>
  <a href="parti-moi-endocrin/" class="body-part-card" style="border-top: 3px solid #65a30d;">
    <h3>Părți Moi &amp; Endocrin (TIRADS)</h3>
  </a>
  <a href="vascular-doppler/" class="body-part-card" style="border-top: 3px solid #65a30d;">
    <h3>Vascular &amp; Ecografie Doppler</h3>
  </a>
  <a href="msk/" class="body-part-card" style="border-top: 3px solid #65a30d;">
    <h3>Musculoscheletic (MSK)</h3>
  </a>
  <a href="san/" class="body-part-card" style="border-top: 3px solid #65a30d;">
    <h3>Senologie / Sân (BI-RADS)</h3>
  </a>
  <a href="pediatrie/" class="body-part-card" style="border-top: 3px solid #65a30d;">
    <h3>Pediatrie &amp; Neonatologie</h3>
  </a>
</div>
""",
        encoding="utf-8",
    )

    # 2. Creează docs/eco/.pages
    eco_pages = docs_eco / ".pages"
    eco_pages.write_text(
        """title: Protocoale Ecografie (US)
nav:
  - index.md
  - Abdomen & Pelvis: abdomen-pelvis
  - Părți Moi & Endocrin: parti-moi-endocrin
  - Vascular & Doppler: vascular-doppler
  - Musculoscheletic: msk
  - Senologie (Sân): san
  - Pediatrie: pediatrie
""",
        encoding="utf-8",
    )

    # 3. Creează directoarele de categorii, .pages și index.md
    for cat_slug, cat_info in CATEGORIES_PAGES.items():
        cat_dir = docs_eco / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        cat_pages = cat_dir / ".pages"
        cat_pages.write_text(f"title: {cat_info['title']}\n", encoding="utf-8")

        cat_index = cat_dir / "index.md"
        cat_index.write_text(
            f"""# {cat_info['title']}

{cat_info['description']}

---

### Protocoale Disponibile în această Categorie

""",
            encoding="utf-8",
        )

    # 4. Generează fișierele fiecărui protocol
    generated_count = 0
    for p in ECO_PROTOCOLS:
        cat = p["category"]
        slug = p["slug"]
        file_path = docs_eco / cat / f"{slug}.md"
        md_text = render_eco_document(p)
        file_path.write_text(md_text, encoding="utf-8")
        generated_count += 1
        print(f"Generated: {file_path.relative_to(REPO_ROOT)}")

    print(f"\nSucces: {generated_count} protocoale de Ecografie (US) generate în {docs_eco.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
