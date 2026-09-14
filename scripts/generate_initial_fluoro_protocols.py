"""generate_initial_fluoro_protocols.py — Populează fișierele Markdown de protocoale de fluoroscopie și C-Arm."""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from render_fluoro_protocol import render_fluoro_document

PROTOCOLS = [
    # -------------------------------------------------------------
    # DIGESTIV
    # -------------------------------------------------------------
    {
        "title": "Tranzit Baritat Esofagian (Esofagoscopie Radiologică)",
        "slug": "tranzit-esofagian",
        "category": "digestiv",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Disfagie orofaringiană sau esofagiană (dificultate la deglutiție solidă/lichidă)",
            "Suspiciune de acalazie cardiei sau tulburări de motilitate esofagiană (spasm difuz esofagian)",
            "Diverticul faringo-esofagian Zenker, diverticuli epibronșici sau epifrenici",
            "Reflux gastro-esofagian sever, esofagită peptică și suspiciune de esofag Barrett",
            "Stenoze esofagiene post-caustice, post-radice sau benigne peptice",
            "Suspiciune de neoplasm esofagian (evaluare lungime și localizare stenoză)",
            "Evaluare post-operatorie a anastomozelor esofagiene (după confirmare preliminară cu contrast hidrosolubil)",
        ],
        "contraindications": [
            "Suspiciune certă de perforație esofagiană acută sau fistulă eso-traheală/bronșică (CONTRAINDICAȚIE ABSOLUTĂ pentru Sulfatul de Bariu; se folosește exclusiv contrast iodat hidrosolubil non-ionic izoosmolar din cauza riscului de mediastinită baritată fatală sau baritoză pulmonară)",
            "Tulburări majore de deglutiție cu risc iminent de aspirație masivă traheo-bronșică",
            "Stare comatoasă sau pacient necooperant fără protezare a căilor aeriene",
        ],
        "patient_prep": "À jeun (pe nemâncate) cu minim 6 ore anterior procedurii (evită vărsăturile și refluxul alimentar în timpul deglutiției); îndepărtarea protezelor dentare mobile, a lănțișoarelor și a hainelor cu nasturi metalici.",
        "contrast": {
            "agent": "Sulfat de Bariu suspensie de înaltă densitate (200-250% w/v) pentru dublu contrast mucosal SAU suspensie 100-120% w/v pentru examinare clasică în plin contrast; Dacă există suspiciune de perforație se administrează contrast hidrosolubil non-ionic (Omnipaque 300 / Iopamiro 300)",
            "route": "Orală (per os), înghițire voluntară la comanda medicului radiolog",
            "volume": "100 - 200 ml suspensie baritată",
            "instructions": "Pacientul ia o gură mare de bariu, o menține în cavitatea bucală și înghite exclusiv la comanda sonoră, sub monitorizare fluoroscopică continuă a bolusului",
        },
        "positioning_equipment": {
            "patient_position": "Ortostatism în Oblic Anterior Drept (OAD 35-40°) pentru derularea optimă a esofagului între coloana vertebrală și cord; completat cu incidență profil și clinostatism",
            "equipment_setup": "Masă basculantă telecomandată 90°/15° cu amplificator de imagine / detector plat digital (FPD); distanță focar-receptor ≥ 100 cm",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Joasă (7.5 - 15 fps) cu Last Image Hold (LIH)",
            "kv": "90 - 105 kV (dublu contrast) / 110 - 120 kV (plin contrast baritat)",
            "ma_range": "1.0 - 3.5 mA (AEC automat)",
            "grid": "Cu grilă antidifuzoare",
            "filtration": "Totală ≥ 3.0 mm Al + 0.1 mm Cu",
            "target_fluoro_time": "< 2.5 minute timp total scopie",
            "lih": "Activ permanent",
        },
        "acquisition_steps": [
            {
                "phase": "Faza Orofaringiană & Actul Deglutiției",
                "description": "Examinare în incidență laterală a gâtului: se evaluează faza orală pregătitoare, motilitatea bazei limbii, elevarea laringelui, deschiderea sfincterului esofagian superior (mușchiul cricofaringian) și excluderea oricărei penetrări sau aspirații în laringe.",
            },
            {
                "phase": "Corp Esofagian & Unde Peristaltice (OAD)",
                "description": "Pacientul în OAD 35-40°: se observă unda peristaltică primară declanșată de deglutiție care propulsează bolusul către stomac; se evaluează undele secundare și eventualele contracții terțiare non-propulsive (esofag în tirbușon / presbiesofag).",
            },
            {
                "phase": "Joncțiunea Esofago-Gastrică & Cardia",
                "description": "Analiza deschiderii sfincterului esofagian inferior (SEI) și a vestibulului gastro-esofagian; se verifică simetria și suplețea ampulei epifrenice și poziția liniei Z.",
            },
            {
                "phase": "Fază Mucosală (Dublu Contrast)",
                "description": "După trecerea bolusului principal, se fac clisee centrate cu timp scurt de expunere pentru vizualizarea reliefului fin mucosal (pliuri longitudinale paralele, regulate, sub 2-3 mm grosime).",
            },
            {
                "phase": "Clinostatism & Manevra Valsalva / Efort Tuse",
                "description": "Trecerea mesei în poziție orizontală și Trendelenburg ușor; pacientul efectuează manevra Valsalva pentru evidențierea refluxului gastro-esofagian acid sau a unei hernii hiatale intermitente prin alunecare.",
            },
        ],
        "quality_criteria": [
            "Opacifiere completă și continuă de la hipofaringe până la fornixul gastric",
            "Derularea anatomică a esofagului fără suprapunere pe coloana toracală sau cord",
            "Demonstrarea clară a reliefului mucosal parietal fără artefacte de deglutiție dublă",
            "Documentarea exactă a peristalticii și a tranzitului în timp real",
        ],
        "radiation_safety": [
            "Colimare dinamică strânsă pe axul vertical al esofagului (lățime fascicul < 8-10 cm)",
            "Folosirea obligatorie a modului pulsat la 7.5 fps în loc de scopie continuă (reduce doza cu 50%)",
            "Timp total de fluoroscopie monitorizat strict, menținut sub 2 - 2.5 minute",
            "DAP (Dose Area Product) de referință < 10 Gy·cm²",
            "Șorț de plumb pe pelvisul pacientului pe parcursul întregii examinări",
        ],
        "iris_reference": {
            "chapter": "Tub Digestiv & Esofag",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "notes": "Dacă la debutul examinării pacientul relatează disfagie acută bruscă cu suspiciune de corp străin blocat (os, bol alimentar), NU se va administra masă baritată densă; se începe cu o înghițitură mică de contrast hidrosolubil sau se orientează direct către endoscopie digestivă de urgență.",
    },
    {
        "title": "Tranzit Esofago-Gastro-Duodenal (TEGD) - Dublu Contrast",
        "slug": "tranzit-esofago-gastro-duodenal-tegd",
        "category": "digestiv",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Reflux gastro-esofagian cronic (BRGE) refractar și suspiciune de hernie hiatală (prin alunecare sau paraesofagiană)",
            "Sindrom dispeptic persistent, dureri epigastrice, suspiciune de ulcer gastric sau bulbar duodenal",
            "Suspiciune de gastrită atrofică sau hipertrofică (boala Menetrier), polipi sau leziuni infiltrative gastrice (linită plastică)",
            "Evaluarea modificărilor anatomice post-chirurgicale (gastrectomie parțială/totală, bypass gastric, sleeve gastrectomy)",
            "Diverticuloză duodenală și tulburări de evacuare gastrică (atonie, gastropareză diabetică)",
            "Compresiuni extrinseci gastrice de la nivelul pancreasului sau ficatului",
        ],
        "contraindications": [
            "Suspiciune clinică sau radiologică de abdomen acut chirurgical prin perforație de organ cavitar (bariul în cavitatea peritoneală provoacă peritonită chimică gravă); se recurge exclusiv la contrast iodat hidrosolubil",
            "Ocluzie intestinală completă mecanică",
            "Hemoragie digestivă superioară activă masivă (se temporizează pentru hemostază endoscopică)",
        ],
        "patient_prep": "À jeun strict cu cel puțin 8 ore înainte de examinare (fără alimente solide sau lichide de la miezul nopții); FĂRĂ fumat sau gumă de mestecat în dimineața examinării (nicotina și mestecatul stimulează puternic hipersecreția gastrică acidă care spală pelicula de bariu de pe mucoasă).",
        "contrast": {
            "agent": "Tehnică Dublu Contrast: Granule efervescente (bicarbonat de sodiu + acid citric / fosfat acid) cu 15 ml apă, urmate de 150 - 200 ml suspensie de Sulfat de Bariu de mare densitate (200 - 250% w/v) cu agent antispumant (simeticonă)",
            "route": "Orală (per os)",
            "volume": "150 - 250 ml bariu dens + 3 - 4 g granule efervescente",
            "instructions": "Pacientul înghite rapid granulele cu puțină apă și are instrucțiunea strictă de a NU eructa (a reține gazul pentru distensia optimă a stomacului), urmate de ingestia suspensiei baritate",
        },
        "positioning_equipment": {
            "patient_position": "Examinare dinamică multifazică: Debut în ortostatism (OAD, OAS, PA), urmat de decubit dorsal, decubit ventral, decubit oblic și Trendelenburg 15°",
            "equipment_setup": "Masă basculantă telecomandată cu fluoroscopie digitală directă FPD; telecomandă din camera de comandă",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată (7.5 - 15 fps) + Achiziție Radiografică Digitală (Digital Spot Filming)",
            "kv": "90 - 105 kV (dublu contrast) / 115 - 125 kV (plin contrast/compresie)",
            "ma_range": "1.5 - 4.0 mA (AEC)",
            "grid": "Cu grilă antidifuzoare Bucky",
            "filtration": "Filtru compozit Al + Cu",
            "target_fluoro_time": "< 3.5 - 4 minute",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {
                "phase": "Esofag & Joncțiune Eso-Gastrică",
                "description": "Pasajul inițial al bariului prin esofag în ortostatism OAD; analiza pliurilor de tranziție la nivelul cardiei.",
            },
            {
                "phase": "Distensie & Tapetare Mucoasă Gastrică (Dublu Contrast)",
                "description": "Bascularea mesei în decubit orizontal; pacientul este rotit 360° în jurul axului longitudinal pentru a tapeta întreaga mucoasă gastrică cu bariu pe fondul gazului eliberat; clisee în decubit dorsal oblic stâng (pentru antru și unghi gastric) și decubit oblic drept (pentru fornix).",
            },
            {
                "phase": "Morfologie Gastrică & Pliuri",
                "description": "Clisee centrate pe curbura mică și mare; evaluarea pliurilor mucoasei în compresie dozată moderată; aprecierea peristaltismului antral către pilor.",
            },
            {
                "phase": "Bulb & Cadru Duodenal",
                "description": "Pacientul este așezat în OAD și decubit ventral: bulbul duodenal se proiectează fără suprapunere antrală; se analizează cele trei fețe ale bulbului, baza, vârful, recesurile laterale și arcul duodenal (D1, D2, D3, D4 până la Treitz).",
            },
            {
                "phase": "Manevre de Provocare a Refluxului & Herniei Hiatale",
                "description": "Înclinare Trendelenburg 15-20°, tuse sau efort mecanic de compresiune abdominală pentru evidențierea refluxului gastro-esofagian acid patologic sau a unei hernii hiatale intermitente.",
            },
        ],
        "quality_criteria": [
            "Distensie gazoasă gastrică excelentă fără colabare sau pliuri comprimate artificial",
            "Strat uniform, fin și continuu de bariu pe faldurile gastrice fără agregare sau flocoane",
            "Bulb duodenal demonstrat în plină umplere și în dublu contrast fără suprapunere antrală",
            "Demonstrarea clară a continuității contururilor curburii mici și mari gastrice",
        ],
        "radiation_safety": [
            "Utilizarea fluoroscopiei doar pentru ghidarea poziției și orientarea cliseului, oprind pedala în timpul rotirii pacientului",
            "Utilizarea Last Image Hold (LIH) pentru validarea centrării înainte de declanșarea cliseului radiografic de înaltă rezoluție",
            "Colimare strictă pe aria stomacului și bulbului duodenal",
            "Timp de scopie strict < 3.5 minute; DAP mediu < 15 Gy·cm²",
            "Ecran plumbat de protecție gonadală poziționat sub pelvis",
        ],
        "iris_reference": {
            "chapter": "Stomac & Duoden",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "notes": "În caz de stomac operat (ex. gastro-jejuno-anastomoză Billroth II sau Roux-en-Y), se va acorda atenție deosebită verificării permeabilității ansei aferente și eferente și excluderii ulcerului peptic stomal sau a fistulelor anastomotice.",
    },
    {
        "title": "Tranzit Intestin Subțire (Enterocliză / Small Bowel Follow-Through - SBFT)",
        "slug": "tranzit-intestin-subtire-sbft",
        "category": "digestiv",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Boala Crohn cu afectare a intestinului subțire (aprecierea localizării, a numărului și lungimii stenozelor, a fistulelor entero-enterice sau entero-cutanate și a leziunilor de tip 'skip')",
            "Sindrom cronic de malabsorbție (boală celiacă refractară, sindrom de ansă oarbă, amiloidoză)",
            "Dureri abdominale recidivante de etiologie neelucidată endoscopic",
            "Sângerare digestivă ocultă fără cauză evidențiată la endoscopia superioară și colonoscopie",
            "Suspiciune de neoplazie sau limfom al intestinului subțire, diverticul Meckel complicat",
            "Episoade repetate de subocluzie mecanică prin bride peritoneale postoperatorii",
        ],
        "contraindications": [
            "Ocluzie intestinală completă mecanică instalată cu distensie masivă de anse (contraindicație pentru administrare orală de contrast dens)",
            "Suspiciune de perforație enterală cu peritonită acută",
            "Megacolon toxic sau colită fulminantă asociată",
        ],
        "patient_prep": "Regim alimentar fără reziduuri cu 2 zile anterior; à jeun cu 8-12 ore înainte de procedură; eventual administrarea unui laxativ osmotic ușor în ajun conform protocoalelor secției pentru un colon neîncărcat fecaloid.",
        "contrast": {
            "agent": "Sulfat de Bariu suspensie enterală de densitate medie (40-50% w/v) pentru tranzit per os (SBFT); La Enterocliză: administrare prin sondă nazo-jejunală a 250 ml suspensie de bariu urmată de infuzie de 1000-1500 ml soluție de metilceluloză 0.5% pentru realizarea dublului contrast enteral",
            "route": "Orală (SBFT) SAU pe sondă nazo-jejunală avansată fluoroscopic dincolo de ligamentul Treitz (Enterocliză)",
            "volume": "300 - 600 ml suspensie baritată",
            "instructions": "Pacientul bea suspensia treptat în ritm susținut; se menține în decubit lateral drept pentru stimularea evacuării rapide gastrice a bariului în duoden",
        },
        "positioning_equipment": {
            "patient_position": "Decubit ventral (poziție esențială: compresiunea naturală exercitată de greutatea pacientului pe planul mesei etalează ansele jejuno-ileale prevenind aglomerarea lor în pelvis); decubit dorsal la compresia manuală țintită",
            "equipment_setup": "Masă fluoroscopică digitală cu paletă sau con mecanic de compresiune dozată; distanță focar-film 100-115 cm",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Radiografii seriate discrete la intervale regulate + Fluoroscopie Pulsată scurtă DOAR la compresia ileală",
            "kv": "100 - 120 kV (contrast baritat enteral)",
            "ma_range": "1.0 - 3.0 mA în scopie",
            "grid": "Cu grilă antidifuzoare",
            "filtration": "≥ 3.0 mm Al",
            "target_fluoro_time": "< 2.0 minute cumulat pe toată durata tranzitului",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {
                "phase": "Cliseu de Debut (15 minute)",
                "description": "Radiografie abdominală în decubit ventral: se evaluează jejunul proximal, pliurile kerckringiene feathery (valvulele connivente) și viteza inițială de golire gastrică.",
            },
            {
                "phase": "Seriere Temporizată (30 - 60 - 90 minute)",
                "description": "Radiografii seriate la intervale de 30 minute în decubit ventral; se urmărește progresia coloanei opace prin jejunul distal și ansele ileale, monitorizând calibrul luminal și motilitatea.",
            },
            {
                "phase": "Examen Țintit Fluoroscopic pe Ileonul Terminal",
                "description": "În momentul în care bariul atinge fosa iliacă dreaptă: se trece în regim de fluoroscopie scurtă; se aplică compresiune dozată cu paleta/conul pentru a derula ultima ansă ileală și valva ileo-cecală fără suprapunerea anselor pelvine.",
            },
            {
                "phase": "Confirmarea Pasajului în Cec (Final de Examen)",
                "description": "Opacifierea cecului și a colonului ascendent confirmă tranzitul complet prin întregul intestin subțire; se face un cliseu panoramic final.",
            },
        ],
        "quality_criteria": [
            "Demonstrarea completă a tuturor segmentelor intestinului subțire până la nivelul cecului",
            "Etalarea fără suprapunere a ileonului terminal (sediul predilect al bolii Crohn)",
            "Distincție clară între desenul feathery jejunal și mucoasa mai netedă ileală",
            "Identificarea oricărei rigidități parietale, fistule, stenoze sau imagini lacunare",
        ],
        "radiation_safety": [
            "REGULĂ DE AUR: Fluoroscopia NU se lasă deschisă în așteptarea pasajului! Tranzitul se monitorizează prin radiografii punctuale (spot films) la intervale stabilite",
            "Timpul total cumulat de fluoroscopie trebuie să fie strict < 1.5 - 2 minute",
            "Colimare strictă la compresia ileonului terminal pe fosa iliacă dreaptă",
            "DAP < 12 Gy·cm²",
            "Protecție gonadală poziționată atunci când nu maschează ansele din micul bazin",
        ],
        "iris_reference": {
            "chapter": "Intestin Subțire",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "notes": "Utilizarea unui agent prokinetic (ex. metoclopramid 10 mg oral cu 15 min înainte) poate fi indicată la pacienții cu tranzit lent pentru a scurta timpul de așteptare de la 3-4 ore la sub 60-90 de minute, reducând numărul de expuneri necesare.",
    },
    {
        "title": "Clismă Baritată (Irigoscopie / Irigografie Dublu Contrast)",
        "slug": "clisma-baritata-irigoscopie",
        "category": "digestiv",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Boală diverticulară colonică (evaluarea numărului, dimensiunilor diverticulilor și decelarea stenozelor diverticulare)",
            "Polipi colonici și neoplazii colorectale (atunci când colonoscopia este incompletă din cauza dolicocolonului, a aderențelor sau a unei stenoze impassabile)",
            "Anomalii de poziție, rotație sau calibru colonic (dolicocolon, megacolon congenital Hirschsprung la adult, volvulus)",
            "Boli inflamatorii intestinale cronice (rectocolită ulcero-hemoragică, boală Crohn colonică - stadii de remisiune sau evaluare extensie)",
            "Fistule colo-vezicale, colo-vaginale sau colo-cutanate",
            "Control post-operator după intervenții colorectale (Hartmann, rezecții anterioare joase)",
        ],
        "contraindications": [
            "Megacolon toxic acut sau puseu acut fulminant de colită ulceroasă (risc crescut de perforație colonică fatală)",
            "Suspiciune de perforație colonică recentă (se folosește exclusiv contrast iodat hidrosolubil)",
            "Biopsie colonică endoscopică profundă sau polipectomie efectuată în ultimele 7 - 10 zile",
            "Apendicită acută flegmonoasă / peritonită acută",
        ],
        "patient_prep": "Pregătire mecanică riguroasă a colonului (esențială pentru un examen de diagnostic valid): dietă fără fibre/reziduuri cu 48h înainte; soluție de lavaj intestinal (polietilenglicol - Fortrans / Picoprep) administrată în ajun; clismă evacuatorie matinală; colonul trebuie să fie complet curat de materii fecale.",
        "contrast": {
            "agent": "Sulfat de Bariu suspensie colonică de înaltă densitate (85 - 100% w/v) special formulat pentru aderență mucosală + Aer atmosferic insuflat controlat prin pompă manuală Miller cu bulb de cauciuc",
            "route": "Retrogradă, prin canulă rectală atraumatică cu tub de insuflare de aer",
            "volume": "400 - 700 ml suspensie baritată + 1000 - 1500 ml aer",
            "instructions": "Se poate administra intravenos un antispastic (Buscopan / Butilscopolamină 20 mg sau Glucagon 1 mg) pentru relaxarea musculaturii colonice și reducerea disconfortului/crampelor",
        },
        "positioning_equipment": {
            "patient_position": "Examinare dinamică: Decubit lateral stâng (Sims) pentru inserția canulei, rotire în decubit ventral, decubit lateral drept, decubit dorsal și poziții oblice (OAD, OAS, oblic axial Chassard-Lapiné pentru rect și sigmoid)",
            "equipment_setup": "Masă fluoroscopică digitală telecomandată cu dispozitiv de clismă fixat la stativ la 80 cm deasupra mesei; pompă de aer cu valvă de securitate",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Joasă (7.5 fps) + Radiografii Digitale Țintite",
            "kv": "90 - 105 kV (dublu contrast) / 115 - 125 kV (plin contrast)",
            "ma_range": "1.5 - 4.0 mA",
            "grid": "Cu grilă antidifuzoare",
            "filtration": "Totală ≥ 3.0 mm Al",
            "target_fluoro_time": "< 3.5 - 4 minute",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {
                "phase": "Cliseu Abdominal Preliminar Nativ",
                "description": "Verificarea calității pregătirii colonice (absența fecalelor reziduale care pot simula polipi) și excluderea pneumoperitoneului sau a calcificărilor pelvine.",
            },
            {
                "phase": "Introducere Bariu & Umplere Retrogradă Sigmoidiană",
                "description": "Pacientul în decubit lateral stâng: bariul este instilat până la nivelul flexurii splenice; se începe insuflarea controlată de aer pentru a împinge coloana de bariu către colonul transvers și cec.",
            },
            {
                "phase": "Clisee Țintite pe Rect & Sigmoid",
                "description": "Incidență profil strict pentru rect (evaluarea spațiului retro-rectal) și incidență oblică angulată axială (30-35° caudo-cranial) pentru derularea buclei sigmoidiene fără suprapunere.",
            },
            {
                "phase": "Flexuri Colonice & Colon Transvers",
                "description": "OAS pentru flexura splenică (deschiderea unghiului splenic); OAD pentru flexura hepatică (deschiderea unghiului hepatic sub marginea inferioară a ficatului).",
            },
            {
                "phase": "Cec & Reflux Ileo-Cecal",
                "description": "Decubit dorsal oblic; vizualizarea reliefului cecal, a orificiului apendicular și a valvei ileo-cecale Bauhin.",
            },
            {
                "phase": "Clisee Panoramice Globale & Evacuare",
                "description": "Radiografii panoramice abdominale în decubit ventral și dorsal în dublu contrast complet; cliseu final post-evacuare la toaletă.",
            },
        ],
        "quality_criteria": [
            "Distensie uniformă a tuturor segmentelor colonice de la rect la cec",
            "Tapetare fină, netedă și continuă cu bariu a suprafeței mucoasei fără bule mari de aer artificiale",
            "Derularea completă a rectului, sigmoidului și flexurilor fără zone de suprapunere anatomică",
            "Excluderea artefactelor fecaloide prin mobilitatea lor sau absența bazei de implantare",
        ],
        "radiation_safety": [
            "Insuflarea de aer se efectuează lent și progresiv pentru a evita barotrauma sau durerea colicativă acută",
            "Colimare strictă pe fiecare cadran colonic examinat",
            "Timpul de scopie monitorizat strict < 3.5 minute; DAP mediu < 18 Gy·cm²",
            "Echipă protejată cu șorțuri de plumb dacă asistă pacientul la masă",
        ],
        "iris_reference": {
            "chapter": "Colon & Rect",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "notes": "La pacienții vârstnici sau fragili, canula rectală se introduce cu extremă blândețe, iar balonașul se umflă exclusiv sub control fluoroscopic direct pentru a preveni riscul de ruptură a ampulei rectale.",
    },

    # -------------------------------------------------------------
    # URINAR & PELVIS
    # -------------------------------------------------------------
    {
        "title": "Cistouretrografie Micțională (UCR / CUM / Voiding Cystourethrography)",
        "slug": "cistouretrografie-mictionala-ucr",
        "category": "urinar",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Reflux vezico-ureteral (RVU) — diagnostic de certitudine și gradare internațională (gradele I - V)",
            "Infecții de tract urinar (ITU) recurente sau înalte febrile (pielonefrită acută)",
            "Suspiciune de valve de uretră posterioară (VUP) la băieți sau bărbați tineri",
            "Stenoze uretrale post-traumatice, post-infecțioase sau iatrogene (post-cateterism / post-TURP)",
            "Diverticuli uretrali sau diverticuli vezicali mari cu retenție urinară",
            "Traumatisme pelvine cu suspiciune de ruptură vezicală (intraperitoneală vs extraperitoneală) sau ruptură de uretră",
            "Incontinență urinară complexă și evaluarea dissinergiei vezico-sfincteriene neurogene",
            "Control postoperator după reimplantare uretero-vezicală (Cohen, Politano-Leadbetter) sau plastie de uretră",
        ],
        "contraindications": [
            "Infecție urinară acută activă netratată (risc major de urosepsis bacterian ascendent secundar presiunii de umplere vezicală)",
            "Hemoragie uretrală activă (uretroragie proaspătă) după traumatism perineal recent fără explorare retrogradă prealabilă",
            "Stenoză uretrală completă ce împiedică sondajul atraumatic (se recurge la cistostomie suprapubiană)",
        ],
        "patient_prep": "Urinare completă înainte de procedură; toaletă locală riguroasă a meatului urinar cu soluție antiseptică; instilare intrauretrală de gel steril anestezic cu lidocaină (pentru lubrifiere și anestezie locală); cateterism vezical delicat cu sondă Foley sau Nelaton de calibru adecvat (12-16 Fr la adult) în condiții de asepsie chirurgicală strictă.",
        "contrast": {
            "agent": "Substanță de contrast iodată hidrosolubilă non-ionică (Omnipaque 300 / Iopamiro 300) DILUATĂ la 15 - 20% concentrație cu ser fiziologic steril călduț (37°C)",
            "route": "Retrogradă, prin cateterul vezical instalat",
            "volume": "250 - 450 ml la adult (umplere până la atingerea capacității fiziologice sau a senzației iminente de micțiune)",
            "instructions": "Instilare strict prin forță hidrostatică gravitațională (flaconul suspendat la 60-80 cm deasupra mesei); se interzice injectarea forțată cu seringa din cauza riscului de barotraumă și reflux forțat iatrogen",
        },
        "positioning_equipment": {
            "patient_position": "Decubit dorsal pentru sondare și faza de umplere; În faza micțională: la bărbați poziție Oblică Anterioară Dreaptă sau Stângă (35-45°) cu coapsa inferioară flectată și cea superioară extinsă (etalarea uretrei fără suprapunere pe oasele bazinului); la femei incidență AP",
            "equipment_setup": "Masă fluoroscopică digitală cu amplificator de imagine / FPD; bazinet/pisoar radiotransparent steril pregătit",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Joasă (4 - 7.5 fps) + Clisee Digitale Țintite",
            "kv": "70 - 85 kV",
            "ma_range": "1.0 - 2.5 mA",
            "grid": "Cu grilă la adulți",
            "filtration": "≥ 3.0 mm Al echivalent",
            "target_fluoro_time": "< 1.5 - 2 minute timp total scopie",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {
                "phase": "Cliseu Radiologic Preliminar Nativ",
                "description": "Radiografie nativă a pelvisului și a ariei renale: excluderea calculilor radioopaci vezicali sau renali și a calcificărilor pelvine.",
            },
            {
                "phase": "Faza de Umplere Progresivă (Reflux Pasiv)",
                "description": "Deschiderea perfuzorului cu contrast diluat; monitorizare fluoroscopică intermitentă (la 50, 100, 200 ml) pentru decelarea precoce a refluxului vezico-ureteral pasiv de joasă presiune înainte ca vezica să fie plină.",
            },
            {
                "phase": "Capacitate Vezicală Maximă",
                "description": "Cliseu AP pelvin la umplere completă: contururi vezicale, identificarea eventualilor diverticuli, amprentelor sau trabeculației detrusorului (vezică de luptă).",
            },
            {
                "phase": "Faza Micțională Activă (Reflux Activ & Uretră)",
                "description": "Extragerea sondei vezicale; pacientul urinează în recipient în poziție oblică 45°; declanșarea achiziției fluoroscopice în jet plin: vizualizarea uretrei prostatice, membranoase, bulbare și peniene, colului vezical și excluderea oricărui reflux ureteral activ declanșat de presiunea micțională.",
            },
            {
                "phase": "Cliseu Post-Micțional Imediat",
                "description": "Cliseu centrat pe pelvis și pe lojele renale: evaluarea reziduului vezical post-micțional și verificarea drenajului / stazei contrastului în căile urinare superioare la pacienții cu RVU.",
            },
        ],
        "quality_criteria": [
            "Vizualizarea întregii uretre masculine în jet continuu de la colul vezical până la meatul extern",
            "Includerea ambelor loje renale pe cliseele de micțiune și post-micționale pentru a nu omite refluxul înalt",
            "Delimitarea netă a colului vezical și a calibrului uretral fără artefacte de suprapunere femurală",
            "Aprecierea clară a golirii vezicale complete",
        ],
        "radiation_safety": [
            "Colimare strictă pe aria vezico-pelvină în timpul umplerii; deschiderea fasciculului către lojele renale doar dacă se decelează ascensiunea contrastului pe ureter",
            "Scopie strict pulsatilă la 4-7.5 fps; pedala se apasă doar în momentele critice ale jetului micțional",
            "Timpul total de scopie < 1.5 - 2 minute; DAP mediu < 6 Gy·cm²",
            "La sexul masculin, testiculele sunt protejate de iradierea directă prin colimarea corectă a fasciculului deasupra scrotului",
        ],
        "iris_reference": {
            "chapter": "Aparat Urinar & Nefrologie",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 1 mSv) - Clasa 2",
        },
        "notes": "Gradarea Refluxului Vezico-Ureteral (Clasificarea Internațională): Grad I (doar ureter, fără dilatație), Grad II (ureter, bazinet și calice fără dilatație), Grad III (dilatație ușoară/moderată a ureterului și bazinetului cu bontire ușoară a unghiurilor caliceale), Grad IV (dilatație moderată cu tortuozitate moderată a ureterului și calice aplatizate), Grad V (dilatație masivă și tortuozitate severă a ureterului cu amprente caliceale inversate).",
    },
    {
        "title": "Pielografie Retrogradă și Anterogradă Fluoroscopică",
        "slug": "pielografie-retrograda-si-anterograda",
        "category": "urinar",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Localizarea și cartografierea detaliată a obstrucțiilor ureterale atunci când urografia CT este neconcludentă, insuficientă sau contraindicată (insuficiență renală severă cu RFG < 30 ml/min, alergie severă la substanțele de contrast iodate administrate intravenos)",
            "Evaluarea stenozei de joncțiune pielo-ureterală (JPU) sau joncțiune uretero-vezicală (JUV)",
            "Suspiciune de leziune traumatică sau iatrogenă ureterală cu fistulă urinară (urinom pelvin/retroperitoneal)",
            "Evaluarea defectelor de umplere ureterale (calculi radiotransparenți de acid uric, cheaguri, tumori uroteliale)",
            "Ghidaj fluoroscopic pentru montarea stenturilor ureterale autostatice Double J sau cateterelor de nefrostomie",
        ],
        "contraindications": [
            "Infecție urinară acută nesterilizată (pielonefrită acută netratată)",
            "Hemoragie intra-tract urinar masivă activă",
        ],
        "patient_prep": "Procedură efectuată în sala de cistoscopie urologică sau radiologie intervențională; poziție ginecologică/litotomie; toaletă antiseptică chirurgicală riguroasă; profilaxie antibiotică conform ghidului urologic de secție.",
        "contrast": {
            "agent": "Contrast iodat hidrosolubil non-ionic (Omnipaque 300 / Iopamiro 300) diluat 1:1 cu ser fiziologic steril (concentrație finală ~150 mg I/ml)",
            "route": "Pe cateter ureteral 4-6 Fr introdus retrograd prin cistoscopie SAU pe cateterul de nefrostomie percutanată (anterograd)",
            "volume": "5 - 15 ml contrast diluat",
            "instructions": "Injectare foarte lentă, manuală, strict sub control fluoroscopic direct; se oprește injectarea imediat ce sistemul caliceal este vizibil sau la orice plângere de durere în flanc din partea pacientului",
        },
        "positioning_equipment": {
            "patient_position": "Decubit dorsal pe masa urologică radiotransparentă cu telecomandă sau sistem C-Arm mobil",
            "equipment_setup": "Arc C mobil sau masă basculantă cu detector plat; distanță focar-receptor 100 cm",
            "sid": "100 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Scurtă la cerere + Last Image Hold",
            "kv": "75 - 85 kV",
            "ma_range": "1.0 - 2.5 mA",
            "grid": "Cu grilă",
            "filtration": "≥ 3.0 mm Al",
            "target_fluoro_time": "< 1.5 minute",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {
                "phase": "Plasarea Cateterului & Cliseu Nativ",
                "description": "Medicul urolog cateterizează meatul ureteral sub ghidaj cistoscopic; radiografie nativă a tractului urinar pentru verificarea poziției vârfului cateterului la nivelul L5-S1 sau bazinet.",
            },
            {
                "phase": "Injectare Lentă de Contrast sub Scopie",
                "description": "Se injectează lent 3-5 ml contrast; se observă umplerea progresivă a lumenului ureteral de jos în sus (retrograd) sau din bazinet spre vezică (anterograd).",
            },
            {
                "phase": "Incidențe AP & Oblice (OAD, OAS)",
                "description": "Clisee în incidențe oblice pentru derularea curburilor anatomice ale ureterului și delimitarea precisă a stenozei sau a defectului de umplere.",
            },
            {
                "phase": "Opacifierea Pielo-Caliceală & Retragere",
                "description": "Opacifierea calicelor fără a forța fornixul (prevenirea refluxului pielo-venos/pielo-tubular); cliseu final în timp ce cateterul este retras pentru vizualizarea ureterului distal.",
            },
        ],
        "quality_criteria": [
            "Opacifiere uniformă a întregului ax uretero-pielo-caliceal",
            "Fornixuri caliceale ascuțite, bine definite, fără extravazare perirenală sau reflux forțat",
            "Localizarea certă a nivelului anatomic de stop al coloanei de contrast",
        ],
        "radiation_safety": [
            "Colimare longitudinală strictă pe traiectul ureterului de examinat",
            "Impulsuri de scopie de 1-2 secunde strict în timpul injectării",
            "Timp total de scopie < 1.5 minute; DAP < 5 Gy·cm²",
            "Personalul din sala de cistoscopie poartă obligatoriu șorț de plumb și guler tiroidian",
        ],
        "iris_reference": {
            "chapter": "Aparat Urinar",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "notes": "Injectarea cu presiune excesivă poate provoca reflux pielo-interstițial sau pielo-venos cu bacteriemie și durere lombară severă; la pacienții cu rinichi unic chirurgical procedura se efectuează cu precauție extremă.",
    },
    {
        "title": "Histerosalpingografie (HSG) sub Control Fluoroscopic",
        "slug": "histerosalpingografie-hsg",
        "category": "urinar",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Bilanțul complet al infertilității feminine primare sau secundare (evaluarea permeabilității trompelor uterine)",
            "Anomalii congenitale uterine mulerioase (uter septat, uter bicorn, uter didelf, uter unicorn, uter arcuat)",
            "Decelarea aderențelor / sinechiilor intrauterine (sindromul Asherman)",
            "Identificarea polipilor endometriali mari sau a fibroamelor uterine submucoase cavitare",
            "Evaluarea stenozei tubare proximale sau a hidrosalpinxului distal",
            "Verificarea permeabilității post-microchirurgie tubară sau controlul ocluziei după sterilizare tubară (Essure)",
        ],
        "contraindications": [
            "SARCINĂ certă sau suspectată (CONTRAINDICAȚIE FORMALĂ; examinarea se efectuează obligatoriu în zilele 7 - 11 ale ciclului menstrual, după oprirea sângerării menstruale și înaintea ovulației)",
            "Boală inflamatorie pelvină acută (BIP), cervicită purulentă sau endometrită acută activă",
            "Sângerare uterină activă abundentă neelucidată",
            "Alergie documentată severă la substanțele de contrast iodate",
        ],
        "patient_prep": "Examinare planificată în faza foliculară precoce (zilele 7-11 de la prima zi a ultimei menstruații); test de sarcină urinar negativ în dimineața procedurii; abstinență sexuală de la debutul menstruației; premedicație antispastică orală (No-Spa 80 mg / Drotaverină sau AINS) cu 30-45 minute înainte pentru prevenirea spasmului sfincterian al ostiului tubar; toaletă antiseptică vaginală cu soluție de betadină/clorhexidină.",
        "contrast": {
            "agent": "Contrast iodat hidrosolubil non-ionic izoosmolar/hipoosmolar (Omnipaque 300 / Iopamiro 300) ÎNCĂLZIT la temperatura corpului (37°C) — contrastul rece provoacă durere pelvină și spasm tubar reflex fals!",
            "route": "Injectare transcervicală prin canulă metalică Schultze cu con de cauciuc SAU cateter flexibil steril cu balonaș pediatric (HysteroCath / Foley 6-8 Fr)",
            "volume": "10 - 20 ml contrast iodat",
            "instructions": "Injectare foarte lină și lentă (1-2 ml pe minut), evitând injectarea bruscă care determină crampe uterine dureroase și extravazare venoasă miometrială",
        },
        "positioning_equipment": {
            "patient_position": "Poziție ginecologică (decubit dorsal cu genunchii flectați și coapsele în abducție) pe masa radiologică; centrare pe pelvisul osos inferior",
            "equipment_setup": "Masă fluoroscopică digitală cu telecomandă; specul ginecologic steril; pensă Pozzi de col uterin (dacă se folosește canulă Schultze) sau cateter atraumatic cu balonaș",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Joasă (4 - 7.5 fps) cu Last Image Hold (LIH)",
            "kv": "70 - 80 kV",
            "ma_range": "1.0 - 2.5 mA",
            "grid": "Cu grilă la paciente cu grosime pelvină normală",
            "filtration": "Totală ≥ 3.0 mm Al",
            "target_fluoro_time": "< 1 minut timp total scopie",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {
                "phase": "Cliseu Pelvin Nativ",
                "description": "Radiografie pelvină preliminară: excluderea calcificărilor pelvine, fleboliților voluminoși sau corpilor străini.",
            },
            {
                "phase": "Faza de Umplere Precoce a Cavității Uterine (1-3 ml)",
                "description": "Injectare inițială a 1-3 ml contrast: se observă conturul fin al endometrului; este momentul ideal pentru depistarea defectelor de umplere intracavitare mici (polipi endometriali, sinechii subțiri) care ar putea fi mascate la repleție completă.",
            },
            {
                "phase": "Faza de Repleție Uterină Completă (4-6 ml)",
                "description": "Opacifierea completă a cavității triunghiulare uterine; aprecierea formei, simetriei coarnelor și a marginilor uterine.",
            },
            {
                "phase": "Faza Tubară (Opacifierea Trompelor Uterine)",
                "description": "Progresia contrastului prin porțiunea interstițială, istmică și ampulară a ambelor trompe uterine; evaluarea calibrului și supleții tubare.",
            },
            {
                "phase": "Proba Cotte (Dispersia Peritoneală)",
                "description": "Momentul esențial al examinării: substanța de contrast se revarsă liber prin fimbriile tubare în cavitatea peritoneală liberă, dispersându-se între ansele intestinale; confirmă fără dubiu PERMEABILITATEA TUBARĂ bilaterală.",
            },
            {
                "phase": "Cliseu Tardiv Post-Evacuare",
                "description": "Cliseu efectuat la 10-15 minute după extragerea canulei: confirmă golirea cavității uterine și dispersia peritoneală omogenă a contrastului hidrosolubil.",
            },
        ],
        "quality_criteria": [
            "Cavitate uterină opacifiată omogen, fără bule de aer introduse accidental prin cateter",
            "Urmărirea fără întrerupere a traiectului ambelor trompe până la extremitatea fimbrială",
            "Proba Cotte net pozitivă cu dispersie peritoneală vizibilă bilateral (sau documentarea sediului precis de obstrucție tubară)",
            "Absența extravazării vasculare masive în plexurile venoase pelvine",
        ],
        "radiation_safety": [
            "Timpul de fluoroscopie trebuie să fie extrem de scurt (< 45 - 60 secunde cumulat)",
            "Colimare pelvină strictă centrată pe uter și anexe",
            "DAP < 3 - 5 Gy·cm²",
            "Dacă o trompă nu se opacifiază la început, se așteaptă 1-2 minute pentru relaxarea spasmului cornual, FĂRĂ a ține pedala de scopie apăsată",
        ],
        "iris_reference": {
            "chapter": "Ginecologie & Pelvis",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 1 mSv) - Clasa 2",
        },
        "notes": "Dacă la injectare contrastul intră imediat în venele miometriale și plexul hipogastric (extravazare venoasă), injectarea se OPREȘTE IMEDIAT; fenomenul apare în caz de presiune de injectare prea mare, endometru recent traumatizat sau efectuare prea aproape de menstruație.",
    },

    # -------------------------------------------------------------
    # INTERVENȚIONAL & C-ARM MOBIL
    # -------------------------------------------------------------
    {
        "title": "C-Arm în Ortopedie & Traumatologie: Reducere și Osteosinteză Fracturi",
        "slug": "c-arm-osteosinteza-trauma-ortopedie",
        "category": "c-arm",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Reducerea ortopedică și osteosinteza internă a fracturilor diafizare și metafizare de oase lungi (tije centromedulare blocate femur/tibie/humerus)",
            "Fixarea fracturilor de col femural și trohanteriene (șuruburi canulate, cui gamma, lamă-placă DHS)",
            "Osteosinteză minim invazivă cu plăci blocate (MIPO) la radius distal, tibie distală, humerus proximal",
            "Verificarea intraoperatorie a lungimii șuruburilor și a non-penetrării spațiului articular",
            "Controlul alinierii axiale și a lungimii membrelor în timpul manevrelor de tracțiune pe masa ortopedică",
            "Verificarea orientării componentelor protetice în artroplastiile complexe de șold sau genunchi",
        ],
        "contraindications": [
            "Absența echipamentului individual de radioprotecție (șorțuri de plumb, gulere) pentru personalul din sala de operație",
            "Lipsa drapajului steril impermeabil dedicat pentru arcul C mobil",
            "Aparat C-arm fără verificare dozimetrică CNCAN valabilă",
        ],
        "patient_prep": "Masă chirurgicală ortopedică radiotransparentă de tracțiune sau masă standard cu extensii de fibră de carbon; drapaj steril complet al arcului C (huse sterile transparente); pacient anesteziat și monitorizat.",
        "contrast": {
            "agent": "Procedură standard fără contrast; La artrografie intraoperatorie de control se folosește contrast iodat non-ionic diluat 50%",
            "route": "N/A",
            "volume": "N/A",
            "instructions": "N/A",
        },
        "positioning_equipment": {
            "patient_position": "Decubit dorsal (sau lateral) pe masa ortopedică radiotransparentă conform segmentului osos operat",
            "equipment_setup": "POZIȚIONARE MANDATORIE C-ARM: Tubul generator de raze X se plasează OBLIGATORIU SUB masa de operație, iar detectorul plat/amplificatorul de imagine DEASUPRA pacientului; această geometrie reduce radiația difuză către ochii și trunchiul chirurgului cu 70-75% comparativ cu inversul ei; detectorul se apropie cât mai mult de pielea pacientului",
            "sid": "Distanță focar-receptor standard 90 - 100 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Joasă (Low-Dose Pulse 4 - 7.5 fps) + Last Image Hold (LIH) obligatoriu",
            "kv": "60 - 75 kV (extremități distale) / 80 - 100 kV (șold, pelvis, femur)",
            "ma_range": "0.8 - 2.5 mA",
            "grid": "Cu grilă la segmente groase (șold/bazin); fără grilă la mână/antebraț",
            "filtration": "≥ 3.0 mm Al echivalent",
            "target_fluoro_time": "< 2.0 - 3.0 minute timp total scopie pe intervenție",
            "lih": "Activ obligatoriu",
        },
        "acquisition_steps": [
            {
                "phase": "Test Preliminar de Geometrie & Centrare",
                "description": "Înainte de incizia chirurgicală: arcul C este poziționat și se verifică obținerea facilă atât a incidenței AP, cât și a incidenței Profil strict la 90°, fără coliziune cu masa sau câmpurile sterile.",
            },
            {
                "phase": "Ghidaj Reducere Focar de Fractură",
                "description": "Impulsuri scurte de scopie (1 secundă) pentru verificarea alinierii fragmentelor osoase în timpul tracțiunii și manevrelor ortopedice de reducere.",
            },
            {
                "phase": "Ghidaj Broșe & Foraj",
                "description": "Controlul avansării broșelor de ghidaj Kirschner în spongioasa osoasă sau canalul medular; verificare în două planuri ortogonale (AP și profil).",
            },
            {
                "phase": "Zăvorârea Tijei (Tehnica 'Perfect Circles')",
                "description": "Arcul C este angulat oblic până când orificiile transversale ale tijei centromedulare apar ca cercuri perfect rotunde pe monitor (nu ovale); introducerea șuruburilor de zăvorâre prin centrul cercului fără deviație.",
            },
            {
                "phase": "Verificare Finală Multiax & Arhivare Documentară",
                "description": "Clisee radiografice finale salvate în AP și profil strict: documentarea lungimii tuturor șuruburilor, excluderea efracturii articulare și alinierea axelor mecanice.",
            },
        ],
        "quality_criteria": [
            "Vizualizarea netă a corticalelor osoase și a focarului de fractură în două planuri perfect ortogonale (la 90°)",
            "Excluderea oricărei pătrunderi a materialului de osteosinteză în cavitatea articulară",
            "Confirmarea zăvorârii bi-corticale corecte a șuruburilor",
            "Imagini finale salvate și transmise în sistemul PACS al spitalului",
        ],
        "radiation_safety": [
            "CHIRURGUL ȘI ASISTENȚII: Echipament de protecție obligatoriu — șorț plumbat (minim 0.35 mm Pb, preferat 0.5 mm Pb), guler tiroidian și ochelari de protecție cu sticlă plumbată pentru prevenirea opacifierii cristalinului",
            "REGULA INVERSULUI PĂTRATULUI DISTANȚEI: Personalul care nu asistă direct la masă face 2 pași înapoi (la > 2 metri, nivelul radiației difuze scade cu peste 90%)",
            "MÂINILE CHIRURGULUI: Nu se introduc niciodată mâinile în fasciculul primar direct de raze X! Se folosesc instrumente cu mâner lung de ghidaj",
            "COLIMARE: Colimatoarele lamelare ale arcului C se închid strâns strict pe focarul de osteosinteză",
            "UTILIZAREA LAST IMAGE HOLD (LIH): Chirurgul analizează imaginea oprită pe monitor, fără a menține piciorul pe pedala de expunere",
        ],
        "iris_reference": {
            "chapter": "Traumatologie & Ortopedie",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 1 mSv) - Clasa 2",
        },
        "notes": "Rotirea arcului C mobil se face întotdeauna pe axul circular al brațului; NU se mobilizează membrul operat al pacientului pentru a obține profilul, evitând deplasarea fragmentelor reduse și compromiterea sterilului.",
    },
    {
        "title": "C-Arm în Chirurgie: Colangiografie Intraoperatorie (CIO)",
        "slug": "c-arm-colangiografie-intraoperatorie",
        "category": "c-arm",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Colecistectomie laparoscopică sau clasică dificilă (anatomie neclară a triunghiului hepatocistic Calot)",
            "Suspiciune de litiază coledociană (calculi restanți în calea biliară principală decelați clinic, biologic sau ecografic)",
            "Prevenirea și decelarea precoce a leziunilor iatrogene de cale biliară principală sau canal hepatic drept aberant",
            "Dilatație inexplicabilă a căii biliare principale observată intraoperator",
            "Verificarea permeabilității joncțiunii bilio-duodenale și a funcției sfincterului Oddi",
        ],
        "contraindications": [
            "Alergie severă cunoscută (șoc anafilactic anterior) la substanțe de contrast iodate",
            "Instabilitate hemodinamică severă intraoperatorie care impune finalizarea de urgență a actului chirurgical",
        ],
        "patient_prep": "Masă chirurgicală radiotransparentă; înclinare în poziție anti-Trendelenburg (15°) și ușoară rotație a mesei pe partea dreaptă a pacientului (degajează calea biliară de suprapunerea pe coloana vertebrală lombară); drapaj steril al arcului C.",
        "contrast": {
            "agent": "Contrast iodat hidrosolubil non-ionic (Omnipaque 300 / Iopamiro 300) DILUAT OBLIGATORIU 1:1 cu ser fiziologic steril (concentrație finală ~150 mg I/ml; contrastul pur 100% este prea dens și maschează microcalculii biliari radiotransparenți!)",
            "route": "Injectare pe cateterul colangiografic (cateter ureteral 4-5 Fr sau cateter dedicat Olsen) introdus prin canalul cistic canulat",
            "volume": "10 - 20 ml contrast diluat",
            "instructions": "EXTREM DE IMPORTANT: seringa și cateterul trebuie să fie purjate perfect de orice bulă de aer; o bulă de aer injectată accidental în coledoc mimează perfect un calcul biliar!",
        },
        "positioning_equipment": {
            "patient_position": "Decubit dorsal pe masa de operație cu brațul stâng la 90° și dreptul la trunchi",
            "equipment_setup": "Arc în C mobil centrat pe hipocondrul drept; tubul sub masă, detectorul plat coborât cât mai aproape de abdomenul pacientului",
            "sid": "90 - 100 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată + Radiografie Digitală (Digital Snap)",
            "kv": "75 - 85 kV",
            "ma_range": "1.0 - 2.5 mA",
            "grid": "Cu grilă",
            "filtration": "≥ 3.0 mm Al",
            "target_fluoro_time": "< 1 minut timp total scopie",
            "lih": "Activ",
        },
        "acquisition_steps": [
            {
                "phase": "Plasare Cateter & Apnee Anestezică",
                "description": "Medicul anestezist oprește temporar ventilația mecanică a pacientului la cererea chirurgului (apnee voluntară de 5-10 secunde pentru a elimina artefactele respiratorii diafragmatice).",
            },
            {
                "phase": "Injectare Inițială Mică (3 - 5 ml)",
                "description": "Injectare lentă sub control fluoroscopic: se opacifiază canalul cistic și porțiunea distală a căii biliare principale; se evaluează ampula hepatopancreatică Vater și se caută microcalculi inclavați distal.",
            },
            {
                "phase": "Injectare Completă Arbore Biliar (5 - 8 ml)",
                "description": "Opacifierea canalului hepatic comun, a joncțiunii hepatice și a ramurilor biliare intrahepatice dreaptă și stângă; excluderea defectelor de umplere sau a canalelor biliare aberante ligaturate eronat.",
            },
            {
                "phase": "Pasaj Duodenal",
                "description": "Verificarea scurgerii libere și nestânjenite a substanței de contrast în lumenul duodenal (C duodenal) prin deschiderea sfincterului Oddi.",
            },
        ],
        "quality_criteria": [
            "Vizualizarea integrală a arborelui biliar intrahepatic și extrahepatic",
            "Demonstrarea pasajului liber al contrastului în duoden",
            "Contururi biliare regulate, fără extravazare de contrast în cavitatea peritoneală",
            "Diferențierea certă a calculilor de bulele de aer (calculul este fixat parietal sau decliv, bula de aer se mișcă spre hil)",
        ],
        "radiation_safety": [
            "Timp extrem de scurt de expunere (de obicei sub 20-30 secunde de scopie cumulată)",
            "Avertizare sonoră cu 5 secunde înainte ('Atenție, raze!') pentru ca personalul neesențial să se îndepărteze la > 2 metri",
            "Echipa operatorie poartă șorțuri de plumb și gulere tiroidiene",
            "DAP < 3 Gy·cm²",
        ],
        "iris_reference": {
            "chapter": "Chirurgie Digestivă & Căi Biliare",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 1 mSv)",
        },
        "notes": "Dacă sfincterul Oddi este în spasm și contrastul nu trece în duoden, administrarea intravenoasă de 1 mg Glucagon de către anestezist relaxează sfincterul în 60 de secunde, confirmând absența unui obstacol mecanic litiazic.",
    },
    {
        "title": "C-Arm în Terapia Durerii: Infiltrații Peridurale, Fațetare & Sacroiliace",
        "slug": "c-arm-infiltratii-rahidiene-si-durere",
        "category": "c-arm",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Radiculopatie lombară sau cervicală rebelă secundară unei hernii discale sau stenoze foraminale (infiltrație transforaminală peridurală)",
            "Sindrom fațetar lombar sau cervical (bloc de ramură medială / infiltrație intra-articulară fațetară)",
            "Sacroileită cronică, disfuncție articulară sacroiliacă dureroasă refractară la medicație conservatoare",
            "Stenoză degenerativă de canal vertebral cu claudicație neurogenă (infiltrație interlaminară sau transforaminală)",
            "Sindrom dureros post-laminectomie (failed back surgery syndrome)",
        ],
        "contraindications": [
            "Coagulopatie activă severă sau tratament anticoagulant/antiagregant neîntrerupt conform intervalelor ghidului ASRA (risc de hematom peridural compresiv)",
            "Infecție locală cutanată la locul puncției sau infecție sistemică (bacteriemie / discită / abces peridural)",
            "Alergie cunoscută severă la anestezice locale, corticosteroizi sau contrast iodat",
            "Sarcină documentată",
        ],
        "patient_prep": "Decubit ventral pe masa radiotransparentă cu pernă sub abdomen (atenuează lordoza lombară și deschide spațiile interlaminare și foramenele); monitorizare puls-oximetrie și tensiune arterială; asepsie chirurgicală cu betadină; câmp steril fenestrat.",
        "contrast": {
            "agent": "Contrast iodat hidrosolubil non-ionic izoosmolar (Omnipaque 240/300) pur",
            "route": "Injectare pe acul spinal (Tuohy 20-22G sau Quincke 22-25G) sub vizualizare fluoroscopică continuă în timp real",
            "volume": "0.5 - 2.0 ml contrast",
            "instructions": "MOMENT CRITIC: Testul cu contrast iodat este OBLIGATORIU înainte de injectarea oricărui corticosteroid; dacă se decelează difuzie vasculară intravasculară, acul se repoziționează IMEDIAT (injectarea intra-arterială a corticoidului particulat provoacă infarct medular paraplegic!)",
        },
        "positioning_equipment": {
            "patient_position": "Decubit ventral relaxat cu brațele deasupra capului",
            "equipment_setup": "Arc C mobil manevrat milimetric în 3 incidențe cheie: AP (aliniere platouri vertebrale), Oblic 20-30° (vizualizarea foramenului intervertebral și a aspectului de 'Scotty Dog' / cățel scoțian), Profil strict (verificarea adâncimii pătrunderii acului)",
            "sid": "90 - 100 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată (4 - 7.5 fps) cu colimare strânsă + Last Image Hold",
            "kv": "75 - 90 kV",
            "ma_range": "1.0 - 2.5 mA",
            "grid": "Cu grilă",
            "filtration": "≥ 3.0 mm Al",
            "target_fluoro_time": "< 45 - 60 secunde timp total scopie",
            "lih": "Activ obligatoriu",
        },
        "acquisition_steps": [
            {
                "phase": "Alinierea Nivelului Vertebral Țintă (AP)",
                "description": "Înclinarea craniocaudală a arcului C până când platourile vertebrale superioare și inferioare ale discului țintă sunt aliniate perfect paralel (linie unică pe monitor).",
            },
            {
                "phase": "Vizualizare Oblică ('Scotty Dog')",
                "description": "Rotirea arcului C oblic ipsilateral 20-25°: foramenul intervertebral și 'ochiul cățelului' (pediculul vertebral) devin vizibile; reperarea zonei de siguranță subpediculare.",
            },
            {
                "phase": "Avansarea Acului (Tehnica 'Gun-Barrel')",
                "description": "Acul spinal este orientat coaxial, perfect paralel cu traiectul razelor X (apare ca un singur punct pe ecran); avansare progresivă către treimea postero-superioară a foramenului.",
            },
            {
                "phase": "Verificare Profil Strict",
                "description": "Comutarea arcului C la 90° în profil: vârful acului se oprește în treimea postero-superioară a foramenului intervertebral, fără a depăși peretele posterior al corpului vertebral în canalul medular.",
            },
            {
                "phase": "Epidurograma cu Contrast & Excluderea Intravasculară",
                "description": "Injectarea a 1 ml de contrast non-ionic sub fluoroscopie: se evidențiază delimitarea tecii radiculare (epidurogramă) și se exclude diseminarea intravasculară (contrastul vascular se spală instantaneu) sau subarahnoidiană (mielogramă).",
            },
            {
                "phase": "Injectarea Terapeutică",
                "description": "După validarea contrastografică certă: injectarea lentă a amestecului de anestezic local (Ropivacaină/Bupivacaină) și corticosteroid (Dexametazonă / Triamcinolon).",
            },
        ],
        "quality_criteria": [
            "Poziționarea vârfului acului în ținta anatomică precisă confirmată în două planuri perpendiculare",
            "Diseminare contrastografică peridurală sau periradiculară tipică fără semne de efracție durală",
            "Excluderea absolută a difuziei intravasculare pe secvența fluoroscopică dinamică",
            "Cliseu radiologic martor salvat în sistemul PACS cu acul și contrastul pe poziție",
        ],
        "radiation_safety": [
            "Colimare milimetrică pe spațiul foraminal/articular (câmp de expunere sub 8x8 cm)",
            "Fiecare verificare se face printr-un scurt impuls de pedală de 0.5 secunde",
            "Timpul cumulat de scopie este extrem de redus (< 45 secunde)",
            "DAP < 2.5 Gy·cm²",
            "Mâinile medicului operator sunt ținute la distanță de fascicul prin utilizarea penselor de ghidaj sau a extensiilor de injectare",
        ],
        "iris_reference": {
            "chapter": "Coloană & Terapia Durerii",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 1 mSv)",
        },
        "notes": "Se recomandă cu prioritate utilizarea corticosteroizilor non-particulați (Dexametazonă fosfat sodic) pentru infiltrațiile transforaminale cervicale și lombare, deoarece particulele de depozit (ex. dipropionat de betametazonă) pot cauza tromboză microvasculară fatală în cazul unei pătrunderi neintenționate într-o arteră radiculară (artera Adamkiewicz).",
    },
    {
        "title": "C-Arm în Urologie Intervențională: Nefrostomie Percutanată & Montare Stent JJ",
        "slug": "c-arm-nefrostomie-si-stent-jj",
        "category": "c-arm",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Hidronefroză obstructivă acută febrilă cu risc iminent de urosepsis (uropionefroză litiazică)",
            "Obstrucții ureterale neoplazice pelvine compresive (cancer de col uterin avansat, vezică, prostată, colon)",
            "Stenoze ureterale iatrogene post-chirurgicale sau post-radioterapie pelvină",
            "Fistulă urinară ureterală sau vezicală postoperatorie cu urinoperitoneu sau urinoflegmon",
            "Pregătirea accesului caliceal percutanat pentru nefrolitotomie percutanată (NLP)",
            "Eșecul montării retrograde pe cale cistoscopică a stentului ureteral Double J",
        ],
        "contraindications": [
            "Coagulopatie severă necorectată (INR > 1.5, trombocite < 50.000/mmc)",
            "Hipertensiune arterială malignă necontrolată (risc major de hematom retroperitoneal prin puncție renală)",
            "Interpoziția colonului sau a splinei/ficatului pe traiectul de puncție (se evaluează ecografic/CT prealabil)",
        ],
        "patient_prep": "Decubit ventral sau decubit oblic contralateral la 30° cu sul sub flanc; monitorizare funcții vitale și linie venoasă sigură; sedare conștientă + anestezie locală infiltrativă cu Xilină 1-2% în planurile musculare lombare până la capsula renală; antibioterapie intravenoasă instituită prealabil.",
        "contrast": {
            "agent": "Contrast iodat hidrosolubil non-ionic diluat 1:1 cu ser fiziologic steril (concentrație ~150 mg I/ml)",
            "route": "Injectare pe acul de puncție Chiba (inițial) și pe cateterul de nefrostomie (la control)",
            "volume": "10 - 25 ml",
            "instructions": "Injectare lentă după aspirarea a 5-10 ml de urină (decompresie prealabilă), pentru a nu crește presiunea intrapielică în rinichiul infectat",
        },
        "positioning_equipment": {
            "patient_position": "Decubit ventral sau oblic 30° pe masa chirurgicală radiotransparentă",
            "equipment_setup": "Ghidaj combinat: Ecograf portabil pentru ghidajul puncției calicelui renal inferior + Arc în C mobil pentru ghidajul sârmei ghid, dilatării și plasării stentului/cateterului",
            "sid": "95 - 100 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Joasă (4 - 7.5 fps) + Last Image Hold",
            "kv": "75 - 85 kV",
            "ma_range": "1.0 - 2.5 mA",
            "grid": "Cu grilă",
            "filtration": "≥ 3.0 mm Al",
            "target_fluoro_time": "< 3 - 4 minute timp total scopie",
            "lih": "Activ obligatoriu",
        },
        "acquisition_steps": [
            {
                "phase": "Puncție Caliceală Ghidată",
                "description": "Sub ghidaj ecografic sau fluoroscopic se puncționează calicele renal inferior posterior (linia avasculară Brodel) cu ac Chiba 18-21G; extragerea stiletului și obținerea urinei tulburi/clare.",
            },
            {
                "phase": "Pielografie Percutanată Anterogradă",
                "description": "Injectarea a 5-10 ml de contrast iodat diluat: vizualizarea bazinetului, a calicelor și a joncțiunii pielo-ureterale blocate.",
            },
            {
                "phase": "Avansarea Sârmei Ghid Hidrofile",
                "description": "Introducerea unei sârme ghid hidrofile rigide de 0.035\" prin ac; sub control fluoroscopic continuu sârma este manipulată în bazinet și avansată în ureter dincolo de obstacol până în vezica urinară.",
            },
            {
                "phase": "Dilatare Fascială & Plasare Cateter",
                "description": "Dilatare percutanată fascială secvențială (dilatatoare 6, 8, 10 Fr) pe sârma ghid; avansarea cateterului de nefrostomie tip Pigtail (8-10 Fr) sau a stentului autostatic Double J (6-7 Fr) pe sârmă.",
            },
            {
                "phase": "Formarea Buclei Pigtail & Verificare Finală",
                "description": "Blocarea firului de retenție al buclei pigtail în bazinet; la stentul JJ se confirmă deschiderea completă a buclei superioare în bazinet și a buclei inferioare în vezica urinară; cliseu fluoroscopic final de control.",
            },
        ],
        "quality_criteria": [
            "Poziționarea sigură intra-bazinetală a buclei cateterului de nefrostomie fără cudare",
            "La stentul Double J: ambele extremități spiralate sunt perfect desfășurate în cavitățile țintă",
            "Drenaj urinar spontan imediat confirmat pe cateter",
            "Absența extravazării uro-hematice perirenale sau subcapsulare",
        ],
        "radiation_safety": [
            "Puncția inițială se face ecoghidat pentru a economisi timp de fluoroscopie și a evita iradierea",
            "Scopia C-Arm se folosește doar în momentul manevrării sârmei și verificării dilatării",
            "Colimare strictă lombară",
            "Timp de scopie menținut sub 3-4 minute; DAP < 12 Gy·cm²",
            "Tot personalul poartă echipament complet de radioprotecție din plumb",
        ],
        "iris_reference": {
            "chapter": "Urologie & Intervențional",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
        },
        "notes": "Puncția trebuie să vizeze întotdeauna un calice posterior inferior și NICIODATĂ direct bazinetul renal extrarenal; puncția directă a bazinetului prezintă risc ridicat de sângerare masivă din vasele segmentare retropielice și de fistulă urinară persistentă.",
    },

    # -------------------------------------------------------------
    # PEDIATRIE
    # -------------------------------------------------------------
    {
        "title": "Cistouretrografie Micțională Pediatrică (CUM / VCUG Pediatric)",
        "slug": "cistouretrografie-mictionala-pediatrica",
        "category": "pediatrie",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Evaluarea infecțiilor urinare febrile recurente (pielonefrită acută) la sugar și copil mic",
            "Depistarea și gradarea refluxului vezico-ureteral (RVU - clasificarea internațională a RVU, gradele I - V)",
            "Suspiciune de valve de uretră posterioară (VUP) la băieți (urgență urologică pediatrică cu risc de insuficiență renală)",
            "Bilanțul hidronefrozei antenatale persistente postnatal",
            "Tulburări micționale severe, disurie inexplicabilă, jet urinar întrerupt sau filiform",
            "Anomalii de duplicitate pielo-ureterală cu ureterocel ectopic",
            "Sindroame dismorfice congenitale asociate cu afectare urinară (Prune Belly, sindrom VACTERL)",
        ],
        "contraindications": [
            "Infecție urinară acută netratată documentată (se temporizează examinarea până la obținerea unei uroculturi sterile sub antibioterapie)",
            "Hemoragie urinară activă masivă",
        ],
        "patient_prep": "Atmosferă calmă, încăpere încălzită (prevenirea hipotermiei la nou-născuți); prezența părintelui purtând șorț de plumb pentru confortul psihic al copilului; toaletă antiseptică a meatului; cateterism vezical extrem de blând cu cateter subțire atraumatic fără balonaș (Feeding tube / sondă Nelaton 6-8 Fr) lubrifiat din abundență.",
        "contrast": {
            "agent": "Contrast iodat hidrosolubil non-ionic izoosmolar/hipoosmolar (Omnipaque 300 / Iopamiro 300) DILUAT la 12 - 15% cu ser fiziologic steril CĂLDUȚ (37°C)",
            "route": "Retrogradă pe cateterul vezical",
            "volume": "Volum adaptat capacității vezicale teoretice: Formula la copil > 1 an: Capacitate (ml) = [Vârsta în ani + 2] x 30 ml; La sugar (< 1 an): Capacitate (ml) = Greutate (kg) x 7 ml",
            "instructions": "Contrastul călduț este ESENȚIAL: contrastul rece provoacă contracții bruște spastice ale detrusorului și micțiune prematură în jurul sondei; instilare strict gravitațională (flaconul la max 40-50 cm deasupra mesei)",
        },
        "positioning_equipment": {
            "patient_position": "Decubit dorsal pe masa radiologică; în timpul micțiunii la băieți poziție oblică 35-45° cu coapsa inferioară flectată; la fetițe decubit dorsal AP",
            "equipment_setup": "MASĂ FLUOROSCOPICĂ DIGITALĂ SAU C-ARM: ÎNDEPĂRTAREA OBLIGATORIE A GRILEI ANTIDIFUZOARE (GRID REMOVAL) la nou-născuți și copii mici cu grosime pelvină < 12 cm; această măsură ALARA scade doza de radiații absorbită de copil cu 60-75% fără pierdere semnificativă de contrast; activarea filtrării de Cu (0.1 - 0.2 mm Cu)",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Foarte Joasă (3 - 7.5 fps) + Last Image Hold (LIH)",
            "kv": "60 - 70 kV (adaptat masei corporale a copilului)",
            "ma_range": "0.3 - 1.2 mA",
            "grid": "FĂRĂ GRILĂ ANTIDIFUZOARE (Grid out)",
            "filtration": "Totală ≥ 3.0 mm Al + 0.1 - 0.2 mm Cu",
            "target_fluoro_time": "< 45 - 60 secunde timp total scopie",
            "lih": "Activ obligatoriu",
        },
        "acquisition_steps": [
            {
                "phase": "Imagine Nativă Preliminară Rapidă",
                "description": "Cliseu nativ ultra-scurt sau captură LIH din scopie de 0.5s: excluderea anomaliilor osoase sacrate (agenezie sacrată, spina bifida) asociate cu vezica neurogenă.",
            },
            {
                "phase": "Umplere Gravitațională Lentă (Reflux Pasiv)",
                "description": "Instilare lentă a contrastului; monitorizare prin impulsuri extrem de scurte de scopie (la 25%, 50% și 100% din volumul estimat) pentru depistarea refluxului pasiv pe uretere.",
            },
            {
                "phase": "Capacitate Vezicală Plină",
                "description": "Vezica plină este semnalată de oprirea curgerii lichidului sau de neliniștea copilului (îndoirea genunchilor, debutul micțiunii); cliseu AP centrat.",
            },
            {
                "phase": "Faza Micțională în Jet Activ",
                "description": "Retragerea sondei vezicale; copilul urinează în jet plin; se înregistrează scurt secvența micțională (la băieți în oblic pentru a demonstra întreaga lungime a uretrei posterioare și a exclude valvele congenitale VUP).",
            },
            {
                "phase": "Cliseu Post-Micțional",
                "description": "Captură pe pelvis și pe ambele loje renale: verificarea golirii complete a vezicii și decelarea stazei contrastului în caz de reflux vezico-ureteral.",
            },
        ],
        "quality_criteria": [
            "Demonstrarea clară a anatomiei uretrei masculine de la col până la meat în jet continuu",
            "Includerea ambilor rinichi pe cliseul micțional pentru stadializarea exactă a oricărui reflux",
            "Imagine de calitate diagnostică obținută cu doza minimă absolută de iradiere",
        ],
        "radiation_safety": [
            "PRINCIPIUL ALARA APLICAT LA MAXIMUM: fără grilă antidifuzoare, filtrare suplimentară cu cupru, impulsuri scurte de scopie la 3-7.5 fps",
            "Colimare milimetrică strictă pe aria vezicii",
            "Timpul cumulat de scopie menținut strict sub 45-60 secunde",
            "DAP pediatric de referință < 0.5 - 1.5 Gy·cm² (doză de 10 ori mai mică decât la adult)",
            "Părintele însoțitor poartă șorț de plumb și guler tiroidian pe tot parcursul procedurii",
        ],
        "iris_reference": {
            "chapter": "Pediatrie & Nefrologie Pediatrică",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 1 mSv)",
        },
        "notes": "Dacă băiețelul nu urinează spontan după umplere completă, reflexul micțional poate fi stimulat prin aplicarea unei comprese reci pe abdomenul inferior sau prin poziționarea în ortostatism susținut de părinte; se evită compresiunea mecanică manuală bruscă pe vezică.",
    },
    {
        "title": "Dezinvaginare Intestinală sub Control Fluoroscopic (Reducere Pneumatică / Hidrostatică)",
        "slug": "dezinvaginare-intestinala-fluoro",
        "category": "pediatrie",
        "modality": "fluoro",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Invaginație intestinală ileo-colică acută idiopatică la sugar și copil mic (vârstă tipică 3 luni - 3 ani) diagnosticată ecografic (aspect în cocardă / pseudorinichi)",
            "Copil stabil hemodinamic, fără semne clinice de peritonită, fără șoc toxico-septic și fără pneumoperitoneu",
            "Debut al simptomatologiei de preferință sub 24 - 48 ore de la debutul primelor colici abdominale",
        ],
        "contraindications": [
            "Semne clinice de peritonită acută generalizată sau abdomen acut chirurgical",
            "Pneumoperitoneu decelat pe radiografia abdominală simplă (dovadă de perforație enterală prealabilă)",
            "Stare de șoc hipovolemic / septic sau instabilitate hemodinamică severă",
            "Invaginație ileo-ileală izolată (nu poate fi redusă pe cale retrogradă colonică; necesită chirurgie)",
            "Suspiciune certă de punct de plecare anatomic secundar patologic (diverticul Meckel, polip voluminos, limfom intestinal)",
        ],
        "patient_prep": "Linie venoasă periferică funcțională montată obligatoriu și reechilibrare volemică hidro-electrolitică inițiată; sondă nazo-gastrică deschisă la pungă pentru decomprimarea stomacului; **CHIRURGUL PEDIATRU ȘI SALA DE OPERAȚIE ALERTATE ÎN STANDBY OBLIGATORIU** înainte de a începe procedura; consimțământ informat semnat de părinți.",
        "contrast": {
            "agent": "Reducere Pneumatică (AER insuflat controlat printr-un sistem dedicat cu manometru de presiune și valvă de suprapresiune) — METODA DE ELECȚIE MODERNA; SAU Reducere Hidrostatică cu substanță de contrast iodată hidrosolubilă izoosmolară călduță / ser fiziologic călduț; CONTRAINDICAȚIE FORMALĂ pentru Sulfatul de Bariu din cauza riscului de peritonită chimică gravă în cazul unei perforații",
            "route": "Retrogradă, pe cateter rectal moale (Foley 18-22 Fr) introdus în rect",
            "volume": "Aer insuflat sub presiune strict monitorizată",
            "instructions": "Balonașul sondei Foley se umflă cu 15-20 ml aer sau ser, se trage ușor pe perineu și se etanșează fesele ferm cu benzi adezive elastice late pentru a împiedica scăpările de presiune",
        },
        "positioning_equipment": {
            "patient_position": "Decubit dorsal pe masa radiologică",
            "equipment_setup": "Masă fluoroscopică digitală sau sistem C-Arm; dispozitiv de insuflare de aer conectat la manometru mecanic de presiune calibrat",
            "sid": "100 - 115 cm",
        },
        "fluoro_params": {
            "mode": "Fluoroscopie Pulsată Scurtă la 3 - 7.5 fps; FĂRĂ GRILĂ ANTIDIFUZOARE",
            "kv": "65 - 75 kV",
            "ma_range": "0.5 - 1.5 mA",
            "grid": "Fără grilă (Grid removal)",
            "filtration": "Totală ≥ 3.0 mm Al + 0.1 mm Cu",
            "target_fluoro_time": "< 2.0 minute cumulat pe procedură",
            "lih": "Activ obligatoriu",
        },
        "acquisition_steps": [
            {
                "phase": "Radiografie Abdominală Nativă Preliminară",
                "description": "PAS OBLIGATORIU: radiografie abdominală în decubit pentru a exclude categoric pneumoperitoneul (prezența aerului liber subdiafragmatic contraindică manevra).",
            },
            {
                "phase": "Insuflare Controlată de Aer & Monitorizare Presiune",
                "description": "Se începe insuflarea de aer menținând presiunea la 80 mmHg; la nevoie se poate crește progresiv până la maxim 110 - 120 mmHg; NU SE DEPĂȘEȘTE NICIODATĂ PRESIUNEA DE 120 mmHg din cauza riscului de barotraumă și perforație colonică!",
            },
            {
                "phase": "Urmărirea Progresiei Capului de Invaginație",
                "description": "Prin impulsuri scurte de fluoroscopie de 1-2 secunde se urmărește retragerea masei de invaginație (semnul meniscului convex) din colonul stâng, prin transvers și ascendent către cec.",
            },
            {
                "phase": "Reducerea Ileo-Cecală & Refularea Masivă de Aer",
                "description": "CRITERIUL DE AUR AL SUCCESULUI: La nivelul cecului, capul de invaginație cedează brusc, iar aerul / contrastul refulează MASIV și liber în ansele ileonului terminal pe o distanță de minim 25-30 cm, concomitent cu dispariția masei tumorale palpabile.",
            },
            {
                "phase": "Cliseu Final & Decompresie",
                "description": "Cliseu radiologic documentar al reducerii complete cu aer în ileonul terminal; deschiderea sondei rectale pentru evacuarea aerului din colon; ameliorare clinică spectaculoasă a copilului.",
            },
        ],
        "quality_criteria": [
            "Evidențierea certă a refulării masive de aer sau contrast în ansele intestinului subțire (ileon)",
            "Dispariția completă a defectului de umplere rotund-ovalar din cec/colon",
            "Oprirea colicilor abdominale și adormirea liniștită a copilului după procedură",
            "Confirmare ecografică post-reducere a dispariției imaginii în cocardă",
        ],
        "radiation_safety": [
            "Regulă strictă de timp: scopia se acționează doar 1-2 secunde per verificare a poziției masei",
            "Fără grilă antidifuzoare pentru a proteja țesuturile pediatrice hipersensibile la radiații",
            "DAP mediu < 1.0 - 2.0 Gy·cm²",
            "Regula celor 3 încercări: dacă după 3 tentative de câte 3 minute de insuflare masa nu avansează deloc dincolo de cec, procedura se întrerupe și se trece la cura chirurgicală",
        ],
        "iris_reference": {
            "chapter": "Pediatrie & Urgențe Digestive",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 1 mSv)",
        },
        "notes": "Rata de succes a dezinvaginării pneumatice este de 80-90% în centrele specializate. Rata de recidivă în primele 24-48 ore este de aproximativ 5-10%; copilul rămâne internat sub supraveghere medicală 24 de ore post-procedură.",
    },
]

def generate_all():
    docs_dir = REPO_ROOT / "docs" / "fluoro"
    for proto in PROTOCOLS:
        category = proto["category"]
        slug = proto["slug"]
        cat_dir = docs_dir / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        target_path = cat_dir / f"{slug}.md"

        content = render_fluoro_document(proto)
        target_path.write_text(content, encoding="utf-8")
        print(f"Generat protocol: {target_path.relative_to(REPO_ROOT)}")

if __name__ == "__main__":
    generate_all()
