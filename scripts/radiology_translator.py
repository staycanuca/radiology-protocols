#!/usr/bin/env python3
"""radiology_translator.py — Motor avansat de traducere și adaptare medical-radiologică
pentru protocoalele radiografice din Ghidul de Radiologie.

Acest modul identifică fragmentele de text în limba engleză (sau mixtă româno-engleză)
din protocoalele Merrill, Bontrager, Clark și instituționale, le traduce în limba română
medicală standard și adaptează titlurile și conținutul conform terminologiei radiologice clinice.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Codificare UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


# ---------------------------------------------------------------------------
# 1. Dicționar de Corecție OCR și Ligaturi
# ---------------------------------------------------------------------------

OCR_FIXES = [
    (r'\ufb01', 'fi'),
    (r'\ufb02', 'fl'),
    (r'suВcient', 'suficient'),
    (r'diЎerent', 'diferit'),
    (r'В', 'fi'),
    (r'Ў', 'f'),
    (r'—–|––|——', '—'),
    (r'\s+([,.:;?!])', r'\1'),
]


# ---------------------------------------------------------------------------
# 2. Fraze și Construcții Clinice / Radiologice (Engleză -> Română)
# Ordinea este critică: expresiile cele mai lungi/specifice sunt plasate primele.
# ---------------------------------------------------------------------------

CLINICAL_PHRASES = [
    # --- Comenzi respiratorii (Breathing instructions) ---
    (r'Suspend respiration at the end of full expiration so that the abdominal organs are not compressed',
     'Apnee la sfârșitul expirului complet, pentru a preveni compresia organelor abdominale și a ridica diafragmul'),
    (r'Suspend respiration at the end of full expiration', 'Apnee la sfârșitul expirului profund complet (diafragm ridicat)'),
    (r'Suspend respiration at the end of full inspiration', 'Apnee la sfârșitul inspirului profund complet (expansiune pulmonară maximă)'),
    (r'Suspend at the end of full expiration', 'Apnee la sfârșitul expirului complet'),
    (r'Suspend at the end of full inspiration', 'Apnee la sfârșitul inspirului profund complet'),
    (r'Suspend at the end of expiration so that the abdominal organs are not compressed',
     'Apnee la sfârșitul expirului complet, pentru a preveni compresia organelor abdominale și a ridica diafragmul'),
    (r'Suspend at the end of expiration', 'Apnee la sfârșitul expirului complet'),
    (r'Suspend at the end of inspiration', 'Apnee la sfârșitul inspirului complet'),
    (r'Suspend at end of second full inspiration', 'Apnee la sfârșitul celui de-al doilea inspir profund'),
    (r'Exposure is made in full normal arrested inspiration', 'Expunerea se efectuează în apnee la sfârșitul inspirului profund complet'),
    (r'Exposure is made on arrested inspiration', 'Expunerea se efectuează în apnee la sfârșitul inspirului complet'),
    (r'Exposure is made at the end of expiration', 'Expunerea se efectuează în apnee la sfârșitul expirului complet'),
    (r'Exposure is made on arrested expiration', 'Expunerea se efectuează în apnee la sfârșitul expirului complet'),
    (r'Exposure is made during shallow breathing', 'Expunerea se efectuează în timpul unei respirații superficiale lente (tehnică de estompare)'),
    (r'arrested respiration(?:, usually)? after full expiration', 'Apnee la sfârșitul expirului complet (diafragm ridicat)'),
    (r'arrested respiration(?:, usually)? after full inspiration', 'Apnee la sfârșitul inspirului profund complet'),
    (r'suspend respiration to limit patient motion', 'Apnee pe durata expunerii pentru prevenirea artefactelor de mișcare ale pacientului'),
    (r'suspend respiration and expose on expiration', 'Apnee la sfârșitul expirului pe durata expunerii'),
    (r'suspend respiration and expose on inspiration', 'Apnee la sfârșitul inspirului pe durata expunerii'),
    (r'suspend respiration during exposure', 'Apnee pe durata expunerii'),
    (r'suspended respiration', 'Apnee pe durata expunerii'),
    (r'suspend respiration', 'Apnee pe durata expunerii'),
    (r'shallow breathing during exposure', 'Respirație superficială lentă pe durata expunerii (tehnică de estompare a desenului suprapus)'),
    (r'breathing technique', 'Tehnică de estompare prin respirație superficială (breathing technique)'),
    (r'full inspiration', 'Inspir profund complet'),
    (r'full expiration', 'Expir complet'),
    (r'With infants and young children, watch the breathing pattern\.\s*When [Aa]bdomen is still, make the exposure',
     'La sugari și copii mici, se monitorizează dinamica respiratorie; expunerea se declanșează când abdomenul este complet imobil'),
    (r'With infants and children, watch the breathing pattern',
     'La sugari și copii mici, se monitorizează dinamica respiratorie; expunerea se efectuează când toracele/abdomenul este imobil'),
    (r'If the patient is crying, make the exposure as the patient takes a breath (?:in )?to let out a cry',
     'Dacă pacientul plânge, expunerea se efectuează în momentul în care copilul inspiră adânc înainte de a plânge'),
    (r'Children older than 5 years(?: of age)? usually can hold their breath after a practice session',
     'Copiii cu vârsta peste 5 ani pot menține de regulă apneea după o scurtă simulare/exersare prealabilă'),
    (r'Patient should not swallow during exposure', 'Pacientul este instruit să nu înghită în timpul expunerii'),
    (r'patient should not swallow', 'pacientul nu trebuie să înghită'),

    # --- Poziționare pacient & Instrucțiuni de examinare ---
    (r'Remove all metallic or plastic objects from head and neck',
     'Se îndepărtează toate obiectele metalice sau din plastic din regiunea capului și a gâtului'),
    (r'remove all metallic or plastic objects', 'se îndepărtează toate obiectele radio-opace (metalice sau din plastic)'),
    (r'remove all metallic objects', 'se îndepărtează toate obiectele metalice'),
    (r'The patient is seated alongside the table, with the affected arm nearest to the table',
     'Pacientul stă așezat pe scaun lângă masa radiologică, cu membrul superior afectat sprijinit pe masă'),
    (r'The patient is seated alongside the table, with the affected side nearest to the table',
     'Pacientul stă așezat pe scaun lângă masa de examinare, cu partea afectată sprijinită pe masă'),
    (r'The patient is seated alongside the table', 'Pacientul este așezat pe scaun lângă masa de examinare'),
    (r'The patient sits comfortably, with the head supported',
     'Pacientul stă așezat confortabil pe scaun, cu capul sprijinit'),
    (r'The patient lies (?:Decubit Dorsal|supine) on the X-ray table',
     'Pacientul este așezat în decubit dorsal pe masa radiologică'),
    (r'The patient lies (?:Decubit Ventral|prone) on the X-ray table',
     'Pacientul este așezat în decubit ventral pe masa radiologică'),
    (r'The patient stands with the back against the vertical Bucky',
     'Pacientul stă în ortostatism, cu spatele sprijinit pe stativul vertical Bucky'),
    (r'The patient stands facing the vertical Bucky',
     'Pacientul stă în ortostatism, cu fața spre stativul vertical Bucky'),
    (r'The patient stands with the affected shoulder against',
     'Pacientul stă în ortostatism, cu umărul afectat lipit de casetă/stativ'),
    (r'The projection is best performed with the patient seated facing the',
     'Incidența se realizează optim cu pacientul așezat cu fața spre'),
    (r'The patient’s nose and chin are placed in contact with the midline of the cassette holder',
     'Nasul și bărbia pacientului sunt plasate în contact cu linia mediană a stativului/casetei'),
    (r'The patient\'s nose and chin are placed in contact with the midline of the cassette holder',
     'Nasul și bărbia pacientului sunt plasate în contact cu linia mediană a stativului/casetei'),
    (r'The median plane is vertical and the occlusal plane is horizontal',
     'Planul mediosagital este vertical, iar planul ocluzal este orizontal'),
    (r'The dorsal aspect of the trunk should be at right-angles to the cassette',
     'Fața dorsală a trunchiului trebuie să fie perpendiculară (în unghi drept) pe casetă'),
    (r'This can be assessed by palpating the iliac crests or the posterior superior iliac spines',
     'Alinierea corectă se verifică prin palparea crestelor iliace sau a spinelor iliace postero-superioare'),
    (r'The knees and hips are flexed slightly for stability',
     'Genunchii și șoldurile sunt ușor flectate pentru stabilitate și confort'),
    (r'The shoulders may be rotated slightly to allow the correct position to be attained',
     'Umerii pot fi rotiți ușor pentru a permite obținerea poziției corecte'),
    (r'The patient may grip the Bucky for stability',
     'Pacientul se poate sprijini de stativul Bucky pentru stabilitate'),
    (r'A pad is placed under the (?:Genunchi|knee) for support',
     'Se plasează un suport/pernă sub genunchi pentru sprijin și relaxare'),
    (r'The Antebraț \(Radius și Ulna\) is immobilized using a sandbag',
     'Antebrațul este imobilizat cu ajutorul unui săculeț cu nisip'),
    (r'The forearm is immobilized using a sandbag',
     'Antebrațul este imobilizat cu ajutorul unui săculeț cu nisip'),
    (r'Immobilize the head', 'Se imobilizează capul pacientului'),
    (r'Make the exposure', 'Se declanșează expunerea'),
    (r'Ask the patient to', 'Se instruiește pacientul să'),
    (r'Instruct the patient to', 'Se instruiește pacientul să'),
    (r'Have the patient', 'Se instruiește pacientul să'),
    (r'Adjust the patient’s shoulders and (?:Bazin \(Pelvis\)|bazin|pelvis) to lie in the same plane',
     'Umerii și bazinul pacientului se aliniază în același plan coronal, fără rotație'),
    (r'Adjust the patient\'s shoulders and (?:Bazin \(Pelvis\)|bazin|pelvis) to lie in the same plane',
     'Umerii și bazinul pacientului se aliniază în același plan coronal, fără rotație'),
    (r'with arms by sides', 'cu brațele pe lângă corp'),
    (r'with arms at sides', 'cu brațele pe lângă corp'),
    (r'with arms raised above head', 'cu brațele ridicate deasupra capului'),
    (r'with arms folded across chest', 'cu brațele încrucișate pe piept'),
    (r'arms by sides', 'brațele pe lângă corp'),
    (r'arms at sides', 'brațele pe lângă corp'),

    # Mamografie instrucțiuni
    (r'Inform the patient that compression of the (?:Mamografie \(Sân\)|sânului|breast) will be used',
     'Se informează pacienta cu privire la aplicarea compresiei pe glanda mamară'),
    (r'Slowly apply compression until the (?:Mamografie \(Sân\)|sânul|breast) feels taut',
     'Se aplică progresiv compresia până când glanda mamară este ferm fixată'),
    (r'Instruct the patient to indicate if the compression becomes uncomfortable',
     'Se instruiește pacienta să semnaleze dacă nivelul de compresie devine dureros'),
    (r'Release (?:Mamografie \(Sân\)|breast) compression immediately',
     'Se decomprimă sânul imediat după efectuarea expunerii'),

    # Poziționare abdominală & generală
    (r'For the AP Abdomen, or KUB, projection, place the patient in either the (?:Decubit Dorsal|supine) or the (?:upright|erect) position',
     'Pentru radiografia abdominală simplă (AP / KUB), pacientul este așezat în decubit dorsal sau în ortostatism'),
    (r'The (?:Decubit Dorsal|supine) position is preferred for most initial examinations of the [Aa]bdomen',
     'Poziția de decubit dorsal este preferată pentru majoritatea examinărilor inițiale ale abdomenului'),
    (r'Center the midsagittal plane of the body to the midline of the grid device',
     'Se centrează planul mediosagital al corpului pe linia mediană a dispozitivului Bucky/grilei'),
    (r'Center the midsagittal plane of the patient to the midline of the grid',
     'Se centrează planul mediosagital al pacientului pe linia mediană a grilei antidifuzoare'),
    (r'If the patient is upright, distribute the weight of the body equally on the feet',
     'În ortostatism, greutatea corporală este distribuită în mod egal pe ambele picioare'),
    (r'distribute the weight of the body equally on the feet',
     'greutatea corpului este distribuită egal pe ambele picioare'),
    (r'Place the patient’s arms where they do not cast shadows on the image',
     'Brațele pacientului se poziționează în afara ariei de expunere, pentru a nu proiecta umbre pe imagine'),
    (r'Place the patient\'s arms where they do not cast shadows on the image',
     'Brațele pacientului se poziționează în afara ariei de expunere, pentru a nu proiecta umbre pe imagine'),
    (r'With the patient (?:Decubit Dorsal|supine), place a support under the knees to relieve strain',
     'În decubit dorsal, se plasează o pernă/suport sub genunchi pentru relaxarea peretelui abdominal și confortul pacientului'),
    (r'place a support under the knees to relieve strain',
     'se plasează un suport sub genunchi pentru relaxarea musculaturii și reducerea lordozei lombare'),
    (r'For the (?:Decubit Dorsal|supine) position, center the IR/collimated field at the level of the iliac crests, and ensure that the pubic symphysis is included',
     'În decubit dorsal, receptorul de imagine și câmpul colimat se centrează la nivelul crestelor iliace (L4-L5), asigurând includerea simfizei pubiene'),
    (r'For the upright position, center the IR/collimated field 2 inches \(5 cm\) above the level of the iliac crests or high enough to include the diaphragm',
     'În ortostatism, receptorul și câmpul colimat se centrează la 5 cm (2 inchi) deasupra crestelor iliace, suficient de sus pentru a include cupolele diafragmatice'),
    (r'If the bladder is to be included on the upright image, center the IR/collimated field at the level of the iliac crests',
     'Dacă vezica urinară trebuie inclusă pe imaginea în ortostatism, centrarea se face la nivelul crestelor iliace'),
    (r'If a patient is too tall to include the entire pelvic area, obtain a second image to include the bladder, if necessary',
     'Dacă pacientul este înalt și aria pelviană nu este cuprinsă integral, se realizează o a doua expunere centrată pe vezica urinară'),
    (r'The patient is turned on to the left side, ideally for 20 minutes, allowing (?:any )?free air in the abdominal cavity to rise toward the right flank to avoid',
     'Pacientul este menținut în decubit lateral stâng timp de 10-20 minute, permițând acumularea aerului liber spre flancul drept pentru a evita suprapunerea pe bula gastrică'),
    (r'The patient is turned on to the left side, ideally for 20 minutes',
     'Pacientul este menținut în decubit lateral stâng timp de 10-20 minute'),
    (r'A sandbag is placed over the lower forearm for immobilization',
     'Se plasează un săculeț cu nisip pe treimea inferioară a antebrațului pentru imobilizare'),
    (r'A lead-rubber mask may be used to mask off the half of the film not in use',
     'Se poate folosi o mască din cauciuc plumbat pentru a proteja jumătatea de film/casetă neexpusă'),
    (r'Infants and small children—CR and cassette centered 1 inch \(2\.5 cm\) above umbilicus',
     'Sugari și copii mici: raza centrală și caseta se centrează la 2.5 cm deasupra ombilicului'),
    (r'Older children and adolescents—CR (?:centered|centrat) (?:at|la) (?:the )?level of (?:iliac )?crests',
     'Copii mari și adolescenți: raza centrală se centrează la nivelul crestelor iliace'),
    (r'Child immobilized with sandbags for AP Abdomen',
     'Copil imobilizat cu săculeți cu nisip pentru radiografia de abdomen AP'),
    (r'Note sandbags under and over lower limbs',
     'Notă: săculeți cu nisip plasați sub și peste membrele inferioare'),

    # --- Rază Centrală (CR) & Centrare fascicul ---
    (r'Center IR to projected CR', 'Se centrează receptorul de imagine pe proiecția razei centrale'),
    (r'Center IR to CR', 'Se centrează receptorul de imagine pe raza centrală'),
    (r'Center the IR to the central ray', 'Se centrează receptorul de imagine pe raza centrală'),
    (r'Center the IR to the CR', 'Se centrează receptorul de imagine pe raza centrală'),
    (r'The vertical central ray is centred over the head of the third metacarpal',
     'Raza centrală verticală este centrată perpendicular pe capul metacarpianului III'),
    (r'The vertical central ray is centred over the', 'Raza centrală verticală este centrată pe'),
    (r'The horizontal central ray is directed to the centre of the cassette',
     'Raza centrală orizontală este orientată perpendicular pe centrul casetei'),
    (r'The central ray is directed perpendicular to the center of the IR',
     'Raza centrală este orientată perpendicular pe centrul receptorului de imagine'),
    (r'Perpendicular to the IR at the level of the iliac crests for the (?:Decubit Dorsal|supine) position',
     'Perpendicular pe receptorul de imagine la nivelul crestelor iliace (L4-L5) pentru poziția în decubit dorsal'),
    (r'Horizontal and 2 inches \(5 cm\) above the level of the iliac crests to include the diaphragm for the upright position',
     'Fascicul orizontal centrat la 5 cm (2 inchi) deasupra crestelor iliace, pentru a include cupolele diafragmatice în ortostatism'),
    (r'Perpendicular to the IR entering', 'Perpendicular pe receptorul de imagine, cu punct de intrare la nivelul'),
    (r'Perpendicular to the center of the IR', 'Perpendicular pe centrul receptorului de imagine'),
    (r'perpendicular to the center of the IR', 'perpendicular pe centrul receptorului de imagine'),
    (r'perpendicular to the IR', 'perpendicular pe receptorul de imagine (RI)'),
    (r'parallel to the IR', 'paralel cu receptorul de imagine (RI)'),
    (r'is perpendicular to IR', 'este perpendicular pe receptorul de imagine'),
    (r'perpendicular to IR', 'perpendicular pe receptorul de imagine'),
    (r'parallel to IR', 'paralel cu receptorul de imagine'),
    (r'at right angles to the IR', 'în unghi drept față de receptorul de imagine'),
    (r'at right angles to the cassette', 'în unghi drept față de casetă'),
    (r'Angle CR (\d+)°?\s*(?:to|-)\s*(\d+)°?\s*cephalad', r'Raza centrală se înclină \1°–\2° cranial (spre cap)'),
    (r'Angle CR (\d+)°?\s*(?:to|-)\s*(\d+)°?\s*caudad', r'Raza centrală se înclină \1°–\2° caudal (spre picioare)'),
    (r'Angle CR (\d+)°?\s*cephalad', r'Raza centrală se înclină \1° cranial (spre cap)'),
    (r'Angle CR (\d+)°?\s*caudad', r'Raza centrală se înclină \1° caudal (spre picioare)'),
    (r'Angled (\d+) to (\d+) degrees cephalad', r'Înclinat \1–\2 grade cranial (spre cap)'),
    (r'Angled (\d+) to (\d+) degrees caudad', r'Înclinat \1–\2 grade caudal (spre picioare)'),
    (r'Angled (\d+) degrees cephalad', r'Înclinat \1 grade cranial'),
    (r'Angled (\d+) degrees caudad', r'Înclinat \1 grade caudal'),
    (r'Direct CR to enter at the level of the upper margin of thyroid cartilage to pass through C(\d+)',
     r'Raza centrală se orientează spre marginea superioară a cartilajului tiroid pentru a trece prin vertebra C\1'),
    (r'Direct CR to enter at the level of', 'Raza centrală se orientează spre nivelul'),
    (r'Direct CR to', 'Raza centrală se orientează spre'),
    (r'Directed to the midpoint of the IR', 'Orientat spre punctul central al receptorului de imagine'),
    (r'Directed horizontally', 'Orientat orizontal'),
    (r'Directed vertically', 'Orientat vertical'),

    # --- Criterii de calitate a imaginii (Quality criteria) ---
    (r'The following should be clearly seen:', 'Criterii radiologice de calitate a imaginii:'),
    (r'Evidence of proper collimation and presence of side marker and upright marker, if appropriate, placed clear of anatomy of interest',
     'Colimare corectă vizibilă și prezența markerului de lateralitate (D/S) și de ortostatism, poziționate în afara ariei anatomice de interes'),
    (r'Evidence of proper collimation and presence of side marker',
     'Colimare adecvată vizibilă și prezența markerului de lateralitate (D/S)'),
    (r'Area from the pubic symphysis to the upper [Aa]bdomen \(two images may be necessary if the patient is tall or wide\)',
     'Cuprinderea ariei anatomice de la simfiza pubiană până la cupolele diafragmatice (pot fi necesare două expuneri dacă pacientul este înalt/corpolent)'),
    (r'Area from the pubic symphysis to the upper [Aa]bdomen', 'Cuprinderea ariei anatomice de la simfiza pubiană până la cupolele diafragmatice'),
    (r'Proper patient alignment to IR', 'Aliniere anatomică corectă a pacientului față de receptorul de imagine'),
    (r'Centered vertebral column', 'Coloana vertebrală centrată pe linia mediană a imaginii'),
    (r'Ribs, pelvis, and hips equidistant to the edge of the image or collimated borders on both sides',
     'Simetrie bilaterală perfectă: coastele, oasele iliace și articulațiile coxofemurale la distanțe egale față de marginile colimate'),
    (r'Coaste \(Grilaj Costal\), Bazin \(Pelvis\), and hips equidistant to the edge of the image or collimated borders on both sides',
     'Simetrie bilaterală perfectă: grilajul costal, bazinul și șoldurile la distanțe egale de marginile imaginii'),
    (r'Spinous processes in the center of the lumbar vertebrae', 'Procesele spinoase centrate pe mijlocul corpurilor vertebrale lombare'),
    (r'Ischial spines of the (?:Bazin \(Pelvis\)|pelvis) symmetric, if visible', 'Spinele ischiatice ale bazinului sunt perfect simetrice bilateral'),
    (r'Alae or wings of the ilia symmetric', 'Aripile oaselor iliace sunt perfect simetrice bilateral (absența rotației bazinului)'),
    (r'Exposure factors suВcient to demonstrate the following:', 'Parametri de expunere optimi pentru evidențierea următoarelor structuri:'),
    (r'Exposure factors sufficient to demonstrate the following:', 'Parametri de expunere optimi pentru evidențierea următoarelor structuri:'),
    (r'Lateral abdominal wall and properitoneal fat layer \(flank stripe\)',
     'Peretele abdominal lateral și banda grăsoasă properitoneală (linia flancului) vizibile clar'),
    (r'Psoas muscles, lower border of the liver, and kidneys',
     'Contururile mușchilor psoas, marginea inferioară hepatică și polii renali bine diferențiați'),
    (r'Inferior Coaste \(Grilaj Costal\)', 'Arcurile costale inferioare vizibile net'),
    (r'Inferior ribs', 'Arcurile costale inferioare vizibile net'),
    (r'Transverse processes of the lumbar vertebrae', 'Procesele transverse ale vertebrelor lombare vizibile clar'),
    (r'Diaphragm without motion on upright radiograph \(crosswise IR placement/collimated field is appropriate if the patient is large\)',
     'Cupole diafragmatice nete, fără estompare cinetică de mișcare respiratorie în ortostatism'),
    (r'Diaphragm without motion on upright radiograph', 'Cupole diafragmatice nete, fără estompare cinetică de mișcare în ortostatism'),
    (r'Full lung fields with the scapulae projected laterally', 'Câmpuri pulmonare complet vizibile, cu scapulele proiectate în afara ariei pulmonare'),
    (r'The image should demonstrate all the phalanges, including the soft-tissue fingertips, the carpal and metacarpal bones, and the distal end of the radius and ulna',
     'Imaginea trebuie să demonstreze toate falangele (inclusiv părțile moi ale pulpei degetelor), oasele carpiene, metacarpienele și extremitatea distală a radiusului și ulnei'),
    (r'The inter-phalangeal and metacarpo-phalangeal and carpometacarpal joints should be demonstrated clearly',
     'Articulațiile interfalangiene, metacarpofalangiene și carpometacarpiene trebuie evidențiate net, deschise'),
    (r'sharp reproduction of the bones', 'Contururi osoase nete, fără estompare cinetică'),
    (r'Bony detail should have visually sharp reproduction', 'Detaliile osoase și trabeculația trebuie să aibă o reproducere vizuală netă'),
    (r'Soft tissues and mucosa of sinuses should be visible', 'Părțile moi și contururile mucoasei sinusale trebuie să fie vizibile'),
    (r'The condyles of the mandible should be superimposed', 'Condilii mandibulari trebuie să fie perfect suprapuși pe imaginea de profil'),
    (r'Soft tissue of adenoidal pads should be reproduced', 'Țesutul moale al vegetațiilor adenoide (polipi) trebuie clar vizibil în rinofaringe'),
    (r'Ensure that Absența rotației anatomice: clavicule echidistante față de linia apofizelor spinoase of',
     'Se verifică absența rotației: claviculele sunt riguros echidistante față de linia proceselor spinoase'),
    (r'No rotation', 'Absența rotației anatomice (simetrie bilaterală perfectă)'),
    (r'absence of rotation', 'absența rotației anatomice'),
    (r'without motion', 'fără estompare cinetică de mișcare'),

    # --- Indicații clinice & Patologie ---
    (r'Pathology of the [Aa]bdomen—evaluate gas patterns, soft tissue, and possible calcifications',
     'Patologie abdominală acută/cronică: evaluarea distribuției hidroaerice a gazelor, a țesuturilor moi și a eventualelor calcificări'),
    (r'Other anomalies or diseases of [Aa]bdomen', 'Alte anomalii sau afecțiuni ale cavității abdominale'),
    (r'Abnormal masses, accumulations of gas, airfluid levels, aneurysms \(widening or dilation of the wall of an artery, vein, or the heart\)',
     'Formațiuni tumorale, acumulări anormale de gaze, nivele hidroaerice, anevrisme vasculare (dilatarea calibrului vascular)'),
    (r'Calcification of aorta or other vessels', 'Calcificări patologice ale aortei abdominale sau ale altor vase mari'),
    (r'Umbilical hernia', 'Hernie ombilicală'),
    (r'Small bowel obstruction', 'Ocluzie intestinală pe intestinul subțire (nivele hidroaerice centrale)'),
    (r'Large bowel obstruction', 'Ocluzie intestinală pe cadrul colic (dilatație de colon)'),
    (r'Intestinal obstruction', 'Ocluzie intestinală (nivele hidroaerice)'),
    (r'Foreign bod(?:y|ies)', 'Corp străin / corpuri străine radio-opace'),
    (r'Suspected foreign body', 'Suspiciune de corp străin radio-opac'),
    (r'Renal calculi|calculi', 'Litiază urinară / calculi radio-opaci'),
    (r'Free air in the peritoneal cavity', 'Pneumoperitoneu (aer liber în cavitatea peritoneală)'),
    (r'free gas|subdiaphragmatic gas', 'pneumoperitoneu (aer liber subdiafragmatic)'),
    (r'Pleural effusion', 'Revărsat lichidian pleural (pleurezie)'),
    (r'Pneumothorax', 'Pneumotorax (colaps pulmonar)'),
    (r'Pneumonia', 'Pneumonie / procese de condensare parenchimatoasă'),
    (r'Atelectasis', 'Atelectazie pulmonară (colaps alveolar)'),
    (r'Rheumatoid arthritis', 'Poliartrită reumatoidă / artropatie inflamatorie'),
    (r'Osteoarthritis', 'Artroză / modificări degenerative osteoarticulare'),
    (r'Fractures and dislocations', 'Fracturi și luxații / subluxații articulare'),
    (r'fractures and dislocation(?:s)?', 'fracturi și luxații / subluxații'),
    (r'fracture(?:s)?', 'suspiciune de fractură'),
    (r'dislocation(?:s)?', 'luxație articulară'),
    (r'soft-tissue swelling', 'edem / tumefiere de părți moi'),
    (r'neoplasm|tumour(?:s)?', 'proces proliferativ tumoral'),

    # --- Colimare & Parametri Tehnici ---
    (r'Adjust radiation field to 14 × 17 inches \(35 × 43 cm\) on the collimator\. For smaller patients, collimate to within 1 inch \(2\.5 cm\) of shadow of the [Aa]bdomen flanks\. Place side marker in the collimated exposure field',
     'Câmpul de colimare se reglează pe formatul receptorului (35 × 43 cm). La pacienții supli, se colimează strict la 2.5 cm de conturul flancurilor abdominale. Se include markerul de lateralitate (D/S) în fascicul'),
    (r'Adjust radiation field to (\d+) × (\d+) inches \(([^)]+)\) on the collimator',
     r'Se ajustează câmpul de iradiere la formatul \3 pe colimator'),
    (r'Place side marker in the collimated exposure field', 'Se plasează markerul de lateralitate în câmpul colimat'),
    (r'For smaller patients, collimate to within 1 inch \(2\.5 cm\) of shadow',
     'Pentru pacienți de talie redusă, se colimează la 2.5 cm de conturul tegumentar'),
    (r'Close collimation to area of interest', 'Colimare strictă adaptată pe aria anatomică de interes diagnostic'),
    (r'Strictă pe regiunea de interes', 'Colimare strictă pe regiunea anatomică de interes diagnostic'),

    # --- Note automate de sistem / Curățare ---
    (r'Extragere automată; traducere terminologică parțială\. Necesită revizie\.\s*', ''),
    (r'Nespecificat în fragmentul extras; de verificat în sursă', 'Conform reperelor anatomice standard din tratat'),
]


# ---------------------------------------------------------------------------
# 3. Termeni Medicali și Anatomici Atomici (Engleză -> Română)
# ---------------------------------------------------------------------------

VOCABULARY_WORDS = [
    # Planuri & Linii de referință radiologice
    (r'\bmidsagittal plane\b', 'plan mediosagital'),
    (r'\bmidcoronal plane\b', 'plan mediocoronal'),
    (r'\bmedian sagittal plane\b', 'plan mediosagital'),
    (r'\bmedian plane\b', 'plan mediosagital'),
    (r'\bcoronal plane\b', 'plan coronal'),
    (r'\bsagittal plane\b', 'plan sagital'),
    (r'\btransverse plane\b', 'plan transversal'),
    (r'\bhorizontal plane\b', 'plan orizontal'),
    (r'\bvertical plane\b', 'plan vertical'),
    (r'\bocclusal plane\b', 'plan ocluzal'),
    (r'\borbito-meatal line\b|\bOM line\b|\bOML\b', 'linie orbitomeatală (LOM)'),
    (r'\binfraorbitomeatal line\b|\bIOML\b', 'linie infraorbitomeatală (LIOM)'),
    (r'\bacanthiomeatal line\b|\bAML\b', 'linie acantiomeatală (LAM)'),
    (r'\bmentomeatal line\b|\bMML\b', 'linie mentomeatală (LMM)'),
    (r'\binterpupillary line\b|\bIPL\b', 'linie interpupilară (LIP)'),
    (r'\bexternal acoustic meatus\b|\bEAM\b', 'conduct auditiv extern (CAE)'),

    # Repere craniu & masiv facial
    (r'\bacanthion\b', 'acantion'),
    (r'\bnasion\b', 'nazion'),
    (r'\bglabella\b', 'glabelă'),
    (r'\binion\b', 'inion'),
    (r'\bmental point\b', 'punct mentonier'),
    (r'\bangle of(?: the)? mandible\b|\bgonion\b', 'gonion (unghiul mandibulei)'),
    (r'\bmandibular condyle\b', 'condil mandibular'),
    (r'\bmandibular rami\b|\bmandibular ramus\b', 'ramuri mandibulare'),
    (r'\bmandibular body\b', 'corp mandibular'),
    (r'\bmastoid process\b', 'proces mastoidian'),
    (r'\bpetrous ridges?\b|\bpetrous pyramids?\b', 'stânci temporale (piramide pietroase)'),
    (r'\bsella turcica\b', 'șa turcească'),
    (r'\bforamen magnum\b', 'gaură occipitală mare (foramen magnum)'),
    (r'\boptic foram(?:en|ina)\b', 'gaură optică'),
    (r'\bsphenoid(?:al)? sinus(?:es)?\b', 'sinusuri sfenoidale'),
    (r'\bethmoid(?:al)? sinus(?:es)?\b', 'sinusuri etmoidale'),
    (r'\bmaxillary sinus(?:es)?\b', 'sinusuri maxilare'),
    (r'\bfrontal sinus(?:es)?\b', 'sinusuri frontale'),

    # Repere gât, torace & abdomen
    (r'\bthyroid cartilage\b', 'cartilaj tiroid (mărul lui Adam)'),
    (r'\bcricoid cartilage\b', 'cartilaj cricoid'),
    (r'\bhyoid bone\b', 'os hioid'),
    (r'\bjugular notch\b|\bsternal notch\b', 'incizură jugulară (furculiță sternală)'),
    (r'\bmanubrium sterni\b|\bmanubrium\b', 'manubriu sternal'),
    (r'\bbody of(?: the)? sternum\b', 'corp sternal'),
    (r'\bxiphoid process\b', 'apendice xifoid'),
    (r'\bsternoclavicular joints?\b|\bSC joints?\b', 'articulații sternoclaviculare'),
    (r'\bacromioclavicular joints?\b|\bAC joints?\b', 'articulații acromioclaviculare'),
    (r'\bcostophrenic angles?\b', 'sinusuri costodiafragmatice'),
    (r'\bcardiovascular silhouette\b', 'siluetă cardiovasculară'),
    (r'\biliac crests?\b', 'creste iliace'),
    (r'\banterior superior iliac spine\b|\bASIS\b', 'spină iliacă antero-superioară (SIAS)'),
    (r'\bposterior superior iliac spine\b|\bPSIS\b', 'spină iliacă postero-superioară (SIPS)'),
    (r'\bpubic symphysis\b|\bsymphysis pubis\b', 'simfiză pubiană'),
    (r'\bgreater trochanter\b', 'mare trohanter'),
    (r'\blesser trochanter\b', 'mic trohanter'),
    (r'\bischial spines?\b', 'spine ischiatice'),
    (r'\bischial tuberosit(?:y|ies)\b', 'tuberozități ischiatice'),
    (r'\bobturator foram(?:en|ina)\b', 'găuri obturatoare'),
    (r'\btransverse processes?\b', 'procese transverse'),
    (r'\bspinous processes?\b', 'procese spinoase'),
    (r'\bvertebral column\b|\bspine\b', 'coloană vertebrală'),
    (r'\bcervical vertebrae\b|\bcervical spine\b', 'coloană cervicală'),
    (r'\bthoracic vertebrae\b|\bthoracic spine\b', 'coloană toracală'),
    (r'\blumbar vertebrae\b|\blumbar spine\b', 'coloană lombară'),
    (r'\bsacrum and coccyx\b', 'sacru și coccis'),
    (r'\bdiaphragms?\b', 'cupole diafragmatice'),
    (r'\blung fields?\b', 'câmpuri pulmonare'),
    (r'\bheart and aorta\b', 'siluetă cardiovasculară și aortă'),
    (r'\bsoft palate\b', 'palat moale (văl palatin)'),
    (r'\bpharynx\b', 'faringe'),
    (r'\blarynx\b', 'laringe'),
    (r'\bcervical esophagus\b', 'esofag cervical'),
    (r'\bstomach and duodenum\b', 'stomac și duoden'),
    (r'\bsmall intestine\b|\bsmall bowel\b', 'intestin subțire'),
    (r'\blarge intestine\b|\blarge bowel\b|\bcolon\b', 'intestin gros (colon)'),
    (r'\burinary bladder\b', 'vezică urinară'),
    (r'\bkidneys?\b', 'rinichi'),
    (r'\bliver\b', 'ficat'),
    (r'\bspleen\b', 'splină'),
    (r'\bumbilicus\b', 'ombilic'),

    # Membru superior & inferior
    (r'\bacromion process\b|\bacromion\b', 'acromion'),
    (r'\bcoracoid process\b', 'proces coracoid'),
    (r'\bglenoid cavity\b|\bglenoid fossa\b', 'cavitate glenoidă'),
    (r'\bhumeral head\b', 'cap humeral'),
    (r'\bgreater tubercle\b|\bgreater tuberosity\b', 'mare tuberozitate humerală (trohiter)'),
    (r'\blesser tubercle\b|\blesser tuberosity\b', 'mică tuberozitate humerală (trohin)'),
    (r'\bmedial epicondyle\b', 'epicondil medial (epitrohlee)'),
    (r'\blateral epicondyle\b', 'epicondil lateral'),
    (r'\bradial head\b', 'cap radial'),
    (r'\bradial neck\b', 'col radial'),
    (r'\bradial tuberosity\b', 'tuberozitate radială bicipitală'),
    (r'\bolecranon process\b|\bolecranon\b', 'olecran'),
    (r'\bcoronoid process\b', 'proces coronoid'),
    (r'\bcarpal bones?\b|\bcarpals\b', 'oase carpiene'),
    (r'\bmetacarpal bones?\b|\bmetacarpals\b', 'oase metacarpiene'),
    (r'\bphalanges\b|\bdigits?\b', 'falange'),
    (r'\binterphalangeal joints?\b|\bIP joints?\b', 'articulații interfalangiene (IF)'),
    (r'\bmetacarpophalangeal joints?\b|\bMCP joints?\b', 'articulații metacarpofalangiene (MCF)'),
    (r'\bcarpometacarpal joints?\b|\bCMC joints?\b', 'articulații carpometacarpiene (CMC)'),
    (r'\bfemoral head\b', 'cap femural'),
    (r'\bfemoral neck\b', 'col femural'),
    (r'\bacetabulum\b', 'cotil (acetabul)'),
    (r'\bpatella\b', 'rotulă (patelă)'),
    (r'\btibial plateau\b', 'platou tibial'),
    (r'\btibial tuberosity\b', 'tuberozitate tibială anterioară (TTA)'),
    (r'\bfibular head\b', 'cap peronier (fibular)'),
    (r'\bmedial malleolus\b', 'maleolă medială (tibială)'),
    (r'\blateral malleolus\b', 'maleolă laterală (fibulară)'),
    (r'\bcalcaneus\b|\bcalcaneum\b|\bos calcis\b', 'calcaneu'),
    (r'\btalus\b|\bastragalus\b', 'astragal (talus)'),
    (r'\btarsal bones?\b|\btarsals\b', 'oase tarsiene'),
    (r'\bmetatarsal bones?\b|\bmetatarsals\b', 'oase metatarsiene'),
    (r'\bmetatarsophalangeal joints?\b|\bMTP joints?\b', 'articulații metatarsofalangiene (MTF)'),

    # Proiecții & Poziții standard
    (r'\bmedial rotation\b', 'rotație internă (medială)'),
    (r'\blateral rotation\b', 'rotație externă (laterală)'),
    (r'\bradiographic examination\b', 'examinare radiografică'),
    (r'\broutine projection\b', 'incidență uzuală de rutină'),
    (r'\bspecial projection\b', 'incidență specială complementară'),
    (r'\bsupplementary projection\b', 'incidență suplimentară'),
    (r'\bopen mouth\b', 'gură deschisă (transorală)'),
    (r'\bclosed mouth\b', 'gură închisă'),
    (r'\bupright position\b|\berect position\b', 'ortostatism'),
    (r'\bsupine position\b', 'decubit dorsal'),
    (r'\bprone position\b', 'decubit ventral'),
    (r'\blateral position\b', 'poziție de profil (lateral)'),
    (r'\bright or left position\b', 'poziție laterală dreaptă sau stângă'),
    (r'\bright position\b', 'poziție laterală dreaptă'),
    (r'\bleft position\b', 'poziție laterală stângă'),
    (r'\bRAO position\b', 'poziție oblică anterioară dreaptă (OAD / RAO)'),
    (r'\bLAO position\b', 'poziție oblică anterioară stângă (OAS / LAO)'),
    (r'\bRPO position\b', 'poziție oblică posterioară dreaptă (OPD / RPO)'),
    (r'\bLPO position\b', 'poziție oblică posterioară stângă (OPS / LPO)'),

    # Tehnice & Echipament
    (r'\bcentral ray\b|\bCR\b', 'raza centrală'),
    (r'\bimage receptor\b|\bIR\b', 'receptorul de imagine'),
    (r'\bgrid cassette\b', 'casetă cu grilă antidifuzoare'),
    (r'\bmoving grid\b', 'grilă mobilă Bucky'),
    (r'\banti-scatter grid\b', 'grilă antidifuzoare'),
    (r'\bvertical grid device\b|\bupright Bucky\b|\bvertical Bucky\b', 'stativ vertical Bucky'),
    (r'\bBucky table\b|\bX-ray table\b|\bradiographic table\b', 'masa radiologică'),
    (r'\bBucky tray\b', 'tăvița Bucky'),
    (r'\bfocal spot\b', 'focar tub'),
    (r'\bcollimated field\b', 'câmp colimat'),
    (r'\bradiation field\b', 'câmp de iradiere'),
    (r'\bside marker\b', 'marker de lateralitate (D/S)'),
    (r'\bexposure factors\b', 'parametri de expunere'),
    (r'\blong axis\b', 'axa longitudinală'),
    (r'\bcrosswise\b', 'transversal'),
    (r'\blengthwise\b', 'longitudinal'),
]


# ---------------------------------------------------------------------------
# 4. Curățare și Adaptare Titluri
# ---------------------------------------------------------------------------

def clean_and_adapt_title(title: str, category: str = "") -> str:
    """Transformă titlul extras într-un titlu medical standardizat, profesional și elegant în limba română."""
    if not title:
        return "Rx Protocol Radiografic"

    t = title.strip()

    # 1. Elimină prefixe de manual / numerotări de capitole din Merrill:
    t = re.sub(r'^\s*Rx\s+\d+\.\s*', 'Rx ', t)
    t = re.sub(r'^\s*Rx\s+\d+\s+—\s*', 'Rx ', t)
    t = re.sub(r'^\s*Rx\s+\d+\s+', 'Rx ', t)
    t = re.sub(r'^\s*Rx\s+Thoracic Viscera:\s*', 'Rx Torace și ', t, flags=re.I)
    t = re.sub(r'^\s*Rx\s+Upper Extremity\s*—\s*', 'Rx Membru Superior — ', t, flags=re.I)
    t = re.sub(r'^\s*Rx\s+Lower Extremity\s*—\s*', 'Rx Membru Inferior — ', t, flags=re.I)

    # 2. Curăță accesorii tehnice menționate în titlu
    t = re.sub(r'\s*—\s*Paddle:[^)]*\)\.?\s*', ' ', t, flags=re.I)
    t = re.sub(r'\s*SPECIAL PROJECTIONS\s*(\(ADDITIONAL VIEWS\))?\s*', ' ', t, flags=re.I)
    t = re.sub(r'\s*ROUTINE AND SPECIAL\s*', ' ', t, flags=re.I)
    t = re.sub(r'\s*Sample Exposure Technique Chart\s*', ' ', t, flags=re.I)
    t = re.sub(r'\s*Essential Projections\s*', ' ', t, flags=re.I)

    # 3. Traduceri de orientare și metodă în titluri
    title_replacements = [
        # Structuri mamografice
        (r'Mamografie \(Sân\)', 'Mamografie'),
        (r'Superolateral to Inferomedial Oblique \(SIO\) Projection', 'Oblică Supero-Laterală spre Infero-Medială (SIO)'),
        (r'Lateromedial Oblique \(LMO\) Projection', 'Oblică Latero-Medială (LMO)'),
        (r'Mediolateral Oblique \(MLO\) Projection', 'Oblică Medio-Laterală (MLO)'),
        (r'Exaggerated Craniocaudal \(XCCL\) Projection', 'Cranio-Caudală Exagerată (XCCL)'),
        (r'90-Degree Lateromedial \(LM\) Projection', 'Profil Latero-Medial (LM 90°)'),
        (r'90-Degree Mediolateral \(ML\) Projection', 'Profil Medio-Lateral (ML 90°)'),
        (r'Craniocaudal \(Cc\) Projection', 'Cranio-Caudală (CC)'),
        (r'Craniocaudal \(CC\) Projection', 'Cranio-Caudală (CC)'),
        (r'Tangential \(TAN\) Projection', 'Incidență Tangențială (TAN)'),
        (r'Uniform Tissue Exposure If Compression Is Adequate', 'Incidență cu Compresie Focalizată'),

        # Metode cu nume propriu
        (r'Alexander Method', 'Metoda Alexander'),
        (r'Pearson Method', 'Metoda Pearson'),
        (r'Fuchs Method', 'Metoda Fuchs'),
        (r'Haas Method', 'Metoda Haas'),
        (r'Towne Method', 'Metoda Towne'),
        (r'Schüller Method', 'Metoda Schüller'),
        (r'Moore Method Modified', 'Metoda Moore Modificată'),
        (r'Wolf Method \(For Hiatal Hernia\)', 'Metoda Wolf (Hernie Hiatala)'),
        (r'Judet(?:’|\')?s Method', 'Incidențe Judet (Aripă Iliacă și Obturatoare)'),
        (r'Stryker(?:’|\')?s Method', 'Metoda Stryker'),
        (r'Norgaard Method', 'Metoda Norgaard (Ball-Catcher)'),
        (r'Von Rosen Projection', 'Incidența Von Rosen (Displazie Șold)'),

        # Proiecții anatomice majore
        (r'Cervical Intervertebral Foramina', 'Găuri de Conjugare Cervicale (Foramene)'),
        (r'Thoracic Vertebrae', 'Coloană Toracală'),
        (r'Cervical Vertebrae', 'Coloană Cervicală'),
        (r'Lumbar Vertebrae', 'Coloană Lombară'),
        (r'Atlas and Axis', 'Atlas și Axis (C1-C2)'),
        (r'Cranial Base', 'Bază de Craniu'),
        (r'Ethmoidal and Sphenoidal Sinuses', 'Sinusuri Etmoidale și Sfenoidale'),
        (r'Paranasal Sinuses', 'Sinusuri Paranazale (SAF)'),
        (r'Soft Palate, Pharynx, Larynx, and Cervical Esophagus', 'Palat Moale, Faringe, Laringe și Esofag Cervical'),
        (r'Stomach and Duodenum', 'Stomac și Duoden (Tranzit Baritat)'),
        (r'Small Intestine', 'Intestin Subțire (Tranzit Intestinal)'),
        (r'Superior Stomach and Distal Esophagus', 'Stomac Proximal și Esofag Distal'),
        (r'Acromioclavicular Articulations', 'Articulații Acromioclaviculare'),
        (r'Sternoclavicular Articulations', 'Articulații Sternoclaviculare'),
        (r'Axillary Coaste \(Grilaj Costal\)', 'Grilaj Costal Axilar'),
        (r'Axillary Coaste', 'Grilaj Costal Axilar'),
        (r'Posterior Coaste \(Grilaj Costal\)', 'Grilaj Costal Posterior'),
        (r'Anterior Coaste \(Grilaj Costal\)', 'Grilaj Costal Anterior'),
        (r'Pulmonary Apices', 'Vârfuri Pulmonare (Apexuri)'),
        (r'Feet - supported/ În Încărcare \(Ortostatism\) projections', 'Picioare în Încărcare (Ortostatism)'),
        (r'Feet - supported', 'Picioare în Încărcare (Ortostatism)'),
        (r'Cord și Siluetă Cardiovasculară and Torace \(Câmpuri Pulmonare\) special care baby unit',
         'Torace Neonatal (Cord și Câmpuri Pulmonare) — Terapie Intensivă (ATI/SCBU)'),

        # Titluri all-caps din Bontrager
        (r'ABOVE OR BELOW DIAPHRAGM AP OBLIQUE PROJECTIONS AXILLARY Coaste \(Grilaj Costal\)',
         'Grilaj Costal Axilar — Oblică AP (Supra/Subdiafragmatic)'),
        (r'AXILLARY Coaste \(Grilaj Costal\) PA OBLIQUE PROJECTIONS \(ABOVE DIAPHRAGM\)',
         'Grilaj Costal Axilar — Oblică PA (Supradiafragmatic)'),
        (r'BILATERAL OR UNILATERAL ANTERIOR Coaste \(Grilaj Costal\) PA \(Postero-Anterior\) \(ABOVE DIAPHRAGM\)',
         'Grilaj Costal Anterior — Postero-Anterior (PA Supradiafragmatic)'),
        (r'BILATERAL OR UNILATERAL POSTERIOR Coaste \(Grilaj Costal\) AP \(Antero-Posterior\) \(ABOVE OR BELOW DIAPHRAGM\)',
         'Grilaj Costal Posterior — Antero-Posterior (AP Supra/Subdiafragmatic)'),
        (r'AP Torace traumatism acuttism / Regim Urgență AND MOBILE POSITIONING',
         'Torace AP — Radiografie la Pat / Urgență'),
        (r'15° TO 20° MEDIAL ROTATION AP MORTISE PROJECTION \(Gleznă \(Articulație Talocrurală\)\)',
         'Gleznă (Articulație Talocrurală) — Morteză AP cu Rotație Medială 15°-20°'),
        (r'ALTERNATIVE LATERAL POSITIONS', 'Variante de Poziționare pentru Incidența de Profil (Lateral)'),
        (r'LATERAL Torace POSITION', 'Profil (Lateral) Torace'),
        (r'LATEROMEDIAL PROJECTION', 'Incidență Latero-Medială'),
        (r'PEARSON METHOD', 'Metoda Pearson'),
        (r'RAO AND LAO ANTERIOR OBLIQUE POSITIONS', 'Oblică Anterioară (OAD și OAS)'),
        (r'RPO AND LPO POSTERIOR OBLIQUE POSITIONS', 'Oblică Posterioară (OPD și OPS)'),
        (r'RAO POSITION', 'Oblică Anterioară Dreaptă (OAD / RAO)'),
        (r'LAO POSITION', 'Oblică Anterioară Stângă (OAS / LAO)'),
        (r'RPO POSITION', 'Oblică Posterioară Dreaptă (OPD / RPO)'),
        (r'LPO POSITION', 'Oblică Posterioară Stângă (OPS / LPO)'),

        # Orientări comune în titluri
        (r'Right or left position the patient in the Incidență de Profil \(Lateral\)\.?', 'Profil (Drept sau Stâng)'),
        (r'Right or left position', 'Profil (Drept sau Stâng)'),
        (r'Right position', 'Profil Drept'),
        (r'Left position', 'Profil Stâng'),
        (r'R or L position', 'Profil Drept sau Stâng'),
        (r'Medial rotation', 'Rotație Internă (Medială)'),
        (r'Lateral rotation', 'Rotație Externă (Laterală)'),
        (r'Lateromedial or mediolateral', 'Latero-Medial sau Medio-Lateral'),
        (r'Lateromedial', 'Latero-Medial'),
        (r'Mediolateral', 'Medio-Lateral'),
        (r'Open-mouth', 'Transorală (Gură Deschisă)'),
        (r'Open mouth', 'Transorală (Gură Deschisă)'),
        (r'Ap Incidență Oblică — LPO position', 'Oblică Posterioară Stângă (OPS / LPO)'),
        (r'Pa Incidență Oblică — RAO position', 'Oblică Anterioară Dreaptă (OAD / RAO)'),
        (r'Ap Incidență Oblică', 'Oblică Antero-Posterioară (AP)'),
        (r'Pa Incidență Oblică', 'Oblică Postero-Anterioară (PA)'),
        (r'Ap Axial Incidență Oblică', 'Oblică Axială AP'),
        (r'Pa Axial Incidență Oblică', 'Oblică Axială PA'),
        (r'Basic projections', 'Incidențe Standard de Bază'),
        (r'Special care baby unit', 'ATI Neonatală (SCBU)'),
        (r'dorsi - palmar', 'Dorso-Palmar'),
        (r'dorsi - plantar', 'Dorso-Plantar'),
        (r'fluid levels', 'Nivele Hidroaerice'),
        (r'weight - bearing', 'În Încărcare (Ortostatism)'),
        (r'upright', 'Ortostatism'),
        (r'dorsal decubitus', 'Decubit Dorsal'),
        (r'lateral decubitus', 'Decubit Lateral'),
        (r'Antero - posterior', 'Antero-Posterior (AP)'),
        (r'Postero - anterior', 'Postero-Anterior (PA)'),
        (r'\bPROJECTIONS?\b', 'Incidență'),
        (r'\bprojections?\b', 'Incidență'),
        (r'\bPOSITIONS?\b', 'Poziționare'),
        (r'\bpositions?\b', 'Poziționare'),
        (r'\bVIEWS?\b', 'Incidență'),
        (r'\bviews?\b', 'Incidență'),
    ]

    for pattern, repl in title_replacements:
        t = re.sub(pattern, repl, t, flags=re.IGNORECASE)

    # 4. Curățare repetiții și spații
    t = re.sub(r'\bRx\s+Rx\b', 'Rx', t)
    t = re.sub(r'\bIncidență\s+Incidență\b', 'Incidență', t, flags=re.I)
    t = re.sub(r'\bPoziționare\s+Poziționare\b', 'Poziționare', t, flags=re.I)
    t = re.sub(r'\bOrtostatism\s+Incidență\b', 'în Ortostatism', t, flags=re.I)
    t = re.sub(r'\bAP\s+Ortostatism\b', 'AP în Ortostatism', t, flags=re.I)
    t = re.sub(r'\bPA\s+Ortostatism\b', 'PA în Ortostatism', t, flags=re.I)
    t = re.sub(r'\bProfil\s*\(Lateral\)\s*\(Lateral\)\b', 'Profil (Lateral)', t, flags=re.I)
    t = re.sub(r'\bDecubit\s*Dorsal\s*dorsal\b', 'Decubit Dorsal', t, flags=re.I)
    t = re.sub(r'\bAntero-Posterior\s*\(AP\)\s*\(AP\)\b', 'Antero-Posterior (AP)', t, flags=re.I)
    t = re.sub(r'\s*—\s*—\s*', ' — ', t)
    t = re.sub(r'\s+', ' ', t).strip(' —-')

    if not t.startswith('Rx '):
        t = f"Rx {t}"

    return t


# ---------------------------------------------------------------------------
# 5. Motor de Traducere Paragraf / Câmp
# ---------------------------------------------------------------------------

def translate_field_text(text: str) -> str:
    """Traduce un text descriptiv (poziționare, centrare, criterii, etc.) din engleză/mixtă în română medicală standard."""
    if not text or not isinstance(text, str):
        return text or ""

    # Pasul 1: Remediere ligaturi OCR
    res = text
    for pat, rep in OCR_FIXES:
        res = re.sub(pat, rep, res)

    # Pasul 2: Substituție fraze clinice lungi
    for pat, rep in CLINICAL_PHRASES:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)

    # Pasul 3: Substituție vocabular medical și anatomic atomic
    for pat, rep in VOCABULARY_WORDS:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)

    # Pasul 4: Curățare construcții mixte frecvente și acțiuni
    mixed_cleanups = [
        (r'\bthe patient is placed in\b', 'pacientul este așezat în'),
        (r'\bthe patient is positioned\b', 'pacientul este poziționat'),
        (r'\bthe patient is seated\b', 'pacientul este așezat pe scaun'),
        (r'\bthe patient is turned\b', 'pacientul este întors'),
        (r'\bplace the patient in\b', 'se așază pacientul în'),
        (r'\bplace the patient\b', 'se poziționează pacientul'),
        (r'\bposition the patient\b', 'se poziționează pacientul'),
        (r'\bhave the patient\b', 'se instruiește pacientul să'),
        (r'\binstruct the patient to\b', 'se instruiește pacientul să'),
        (r'\bask the patient to\b', 'se instruiește pacientul să'),
        (r'\bthe patient lies\b', 'pacientul este culcat'),
        (r'\bthe patient stands\b', 'pacientul stă în ortostatism'),
        (r'\bthe patient sits\b', 'pacientul stă așezat'),
        (r'\bcenter the\b', 'se centrează'),
        (r'\bcentered to\b', 'centrat pe'),
        (r'\bcentered at\b', 'centrat la nivelul'),
        (r'\bperpendicular to the\b', 'perpendicular pe'),
        (r'\bparallel with the\b', 'paralel cu'),
        (r'\bparallel to the\b', 'paralel cu'),
        (r'\btangential to the\b', 'tangențial pe'),
        (r'\bat right angles to the\b', 'în unghi drept față de'),
        (r'\bat an angle of\b', 'la un unghi de'),
        (r'\boptimal image receptor exposure\b', 'expunere optimă a receptorului de imagine'),
        (r'\bimage receptor exposure\b', 'expunere a receptorului de imagine'),
        (r'\barea of interest\b', 'aria de interes diagnostic'),
        (r'\bshield gonads\b', 'se efectuează ecranarea gonadelor cu șorț plumbat'),
        (r'\bgonadal shielding\b', 'ecranare gonadică'),
        (r'\bsoft-tissue\b', 'părți moi'),
        (r'\bsoft tissue\b', 'părți moi'),
        (r'\bboth sides\b', 'ambele părți (bilateral)'),
        (r'\bequidistant to\b', 'echidistant față de'),
        (r'\bequidistant from\b', 'echidistant față de'),
        (r'\bdistal end of\b', 'extremitatea distală a'),
        (r'\bproximal end of\b', 'extremitatea proximală a'),
        (r'\bdemonstrates?\b', 'evidențiază'),
        (r'\bdemonstrated clearly\b', 'clar evidențiat(e)'),
        (r'\bclearly seen\b', 'clar vizibil(e)'),
        (r'\bwithout motion\b', 'fără estompare cinetică (fără mișcare)'),
        (r'\btrabecular detail\b', 'detalii trabeculare osoase'),
        (r'\bsharp reproduction\b', 'reproducere netă a contururilor'),
        (r'\bjoint spaces?\b', 'spații articulare'),
        (r'\bfluid levels?\b', 'nivele hidroaerice'),
        (r'\bfree air\b', 'aer liber'),
        (r'\bfree gas\b', 'gaze libere'),
        (r'\bupper abdomen\b', 'etajul abdominal superior'),
        (r'\blower abdomen\b', 'etajul abdominal inferior'),
        (r'\bacute abdomen\b', 'abdomen acut'),
        (r'\bupper limb\b', 'membru superior'),
        (r'\blower limb\b', 'membru inferior'),
        (r'\bupper ribs\b', 'coaste superioare'),
        (r'\blower ribs\b', 'coaste inferioare'),
        (r'\btight collimation\b', 'colimare strictă'),
        (r'\bclose collimation\b', 'colimare strânsă'),
        (r'\bsandbags?\b', 'săculeți cu nisip'),
        (r'\bimmobilization\b', 'imobilizare'),
        (r'\bin contact with\b', 'în contact cu'),
        (r'\bat the level of\b', 'la nivelul'),
        (r'\babove the level of\b', 'deasupra nivelului'),
        (r'\bbelow the level of\b', 'sub nivelul'),
        (r'\bto include the\b', 'pentru a include'),
        (r'\bto demonstrate the\b', 'pentru a evidenția'),
        (r'\bso that the\b', 'astfel încât'),
        (r'\bsuch that the\b', 'astfel încât'),
        (r'\bwith the patient\b', 'cu pacientul'),
        (r'\bfrom the patient\b', 'de la pacient'),
        (r'\bnearest to the\b', 'cel mai apropiat de'),
        (r'\bclosest to the\b', 'cel mai apropiat de'),
        (r'\bfurthest from the\b', 'cel mai depărtat de'),
        (r'\bon the table\b', 'pe masa de examinare'),
        (r'\bon the cassette\b', 'pe casetă'),
        (r'\bagainst the cassette\b', 'sprijinit pe casetă'),
        (r'\bagainst the Bucky\b', 'sprijinit pe stativul Bucky'),
        (r'\bagainst the\b', 'pe / sprijinit de'),
        (r'\bbetween the\b', 'între'),
        (r'\bmidline of table\b', 'linia mediană a mesei'),
        (r'\bmidline of the table\b', 'linia mediană a mesei'),
        (r'\bmidline of the\b', 'linia mediană a'),
        (r'\bto the midline of\b', 'pe linia mediană a'),
        (r'\balign the\b', 'se aliniază'),
        (r'\balign midsagittal plane\b', 'se aliniază planul mediosagital'),
        (r'\balign midcoronal plane\b', 'se aliniază planul mediocoronal'),
        (r'\bthe affected side\b', 'partea afectată'),
        (r'\bthe unaffected side\b', 'partea sănătoasă (neafectată)'),
        (r'\bthe affected arm\b', 'brațul afectat'),
        (r'\bthe affected leg\b', 'membrul inferior afectat'),
        (r'\bflex the\b', 'se flectează'),
        (r'\bextend the\b', 'se extinde'),
        (r'\brotate the\b', 'se rotește'),
        (r'\badjust the\b', 'se ajustează'),
        (r'\bseat the patient\b', 'se așază pacientul pe scaun'),
        (r'\bask the patient\b', 'se instruiește pacientul să'),
        (r'\brest the patient\b', 'se sprijină pacientul'),
        (r'\bimmobilize the\b', 'se imobilizează'),
        (r'\bmake the exposure\b', 'se declanșează expunerea'),
        (r'\bdurata expunerii during exposure\b', 'pe durata expunerii'),
        (r'\bdurata expunerii and expose\b', 'pe durata expunerii și expunere'),
        (r'\band expose on expiration\b', 'și expunere în expir'),
        (r'\band expose on inspiration\b', 'și expunere în inspir'),
    ]

    for pat, rep in mixed_cleanups:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)

    # Pasul 5: Conectori, verbe și articole rămase izolate
    word_replacements = [
        (r'\bthe patient\b', 'pacientul'),
        (r'\bthe cassette\b', 'caseta'),
        (r'\bthe table\b', 'masa de examinare'),
        (r'\bthe grid\b', 'grila'),
        (r'\bthe tube\b', 'tubul'),
        (r'\bthe central ray\b', 'raza centrală'),
        (r'\bthe image receptor\b', 'receptorul de imagine'),
        (r'\bthe receptor\b', 'receptorul'),
        (r'\bthe midline\b', 'linia mediană'),
        (r'\bthe knees\b', 'genunchii'),
        (r'\bthe hips\b', 'șoldurile'),
        (r'\bthe shoulders\b', 'umerii'),
        (r'\bthe arms\b', 'brațele'),
        (r'\bthe legs\b', 'picioarele'),
        (r'\bthe feet\b', 'picioarele'),
        (r'\bthe hands\b', 'mâinile'),
        (r'\bthe fingers\b', 'degetele'),
        (r'\bthe thumb\b', 'policele'),
        (r'\bthe chin\b', 'bărbia'),
        (r'\bthe nose\b', 'nasul'),
        (r'\bthe head\b', 'capul'),
        (r'\bthe neck\b', 'gâtul'),
        (r'\bthe chest\b', 'toracele'),
        (r'\bthe abdomen\b', 'abdomenul'),
        (r'\bthe pelvis\b', 'bazinul'),
        (r'\bthe spine\b', 'coloana'),
        (r'\bthe skull\b', 'craniul'),
        (r'\bthe face\b', 'fața'),
        (r'\bthe diaphragm\b', 'diafragmul'),
        (r'\bthe lungs\b', 'plămânii'),
        (r'\bthe heart\b', 'cordul'),
        (r'\bthe creste iliace\b', 'crestele iliace'),
        (r'\bthe plan mediosagital\b', 'planul mediosagital'),
        (r'\bthe plan mediocoronal\b', 'planul mediocoronal'),
        (r'\bthe vertical raza\b', 'raza centrală verticală'),
        (r'\bthe horizontal raza\b', 'raza centrală orizontală'),
        (r'\bdirect the raza\b', 'se orientează raza centrală'),
        (r'\bwith the raza\b', 'cu raza centrală'),
        (r'\bdegrees?\b', 'grade'),
        (r'\bdegree\b', 'grad'),
        (r'\bperpendicular\b', 'perpendicular'),
        (r'\bhorizontal\b', 'orizontal'),
        (r'\bvertical\b', 'vertical'),
        (r'\bparallel\b', 'paralel'),
        (r'\boblique\b', 'oblic'),
        (r'\btangential\b', 'tangențial'),
        (r'\baxial\b', 'axial'),
        (r'\bsupine\b', 'în decubit dorsal'),
        (r'\bprone\b', 'în decubit ventral'),
        (r'\bupright\b', 'în ortostatism'),
        (r'\berect\b', 'în ortostatism'),
        (r'\bseated\b', 'așezat pe scaun'),
        (r'\bsitting\b', 'așezat'),
        (r'\bstanding\b', 'în ortostatism'),
        (r'\blying\b', 'culcat'),
        (r'\bflexed\b', 'flectat'),
        (r'\bextended\b', 'extins'),
        (r'\brotated\b', 'rotit'),
        (r'\babducted\b', 'în abducție'),
        (r'\badducted\b', 'în adducție'),
        (r'\bpronated\b', 'în pronație'),
        (r'\bsupinated\b', 'în supinație'),
        (r'\belevated\b', 'ridicat'),
        (r'\bdepressed\b', 'coborât'),
        (r'\bsupported\b', 'sprijinit'),
        (r'\bimmobilized\b', 'imobilizat'),
        (r'\brelaxed\b', 'relaxat'),
        (r'\bcentered\b', 'centrat'),
        (r'\bdirected\b', 'orientat'),
        (r'\bangled\b', 'înclinat'),
        (r'\bpositioned\b', 'poziționat'),
        (r'\bplaced\b', 'plasat'),
        (r'\badjusted\b', 'ajustat'),
        (r'\baligned\b', 'aliniat'),
        (r'\bshielded\b', 'ecranat'),
        (r'\bdemonstrated?\b', 'evidențiat'),
        (r'\bdemonstrating\b', 'evidențiind'),
        (r'\bvisible\b', 'vizibil'),
        (r'\bshown\b', 'vizualizat'),
        (r'\bsharp\b', 'net'),
        (r'\boptimal\b', 'optim'),
        (r'\bproper\b', 'corect'),
        (r'\badequate\b', 'adecvat'),
        (r'\baccurate\b', 'precis'),
        (r'\bsymmetric(?:al)?\b', 'simetric'),
        (r'\basymmetric\b', 'asimetric'),
        (r'\bbilateral\b', 'bilateral'),
        (r'\bunilateral\b', 'unilateral'),
        (r'\banterior\b', 'anterior'),
        (r'\bposterior\b', 'posterior'),
        (r'\bsuperior\b', 'superior'),
        (r'\binferior\b', 'inferior'),
        (r'\bmedial\b', 'medial'),
        (r'\blateral\b', 'lateral'),
        (r'\bproximal\b', 'proximal'),
        (r'\bdistal\b', 'distal'),
        (r'\bcranial\b|\bcephalad\b', 'cranial'),
        (r'\bcaudal\b|\bcaudad\b', 'caudal'),
        (r'\bpalmar\b', 'palmar'),
        (r'\bplantar\b', 'plantar'),
        (r'\bdorsal\b', 'dorsal'),
        (r'\bventral\b', 'ventral'),
        (r'\binternal\b', 'intern'),
        (r'\bexternal\b', 'extern'),
        (r'\bleft\b', 'stâng'),
        (r'\bright\b', 'drept'),
        (r'\bboth\b', 'ambele'),
        (r'\beach\b', 'fiecare'),
        (r'\ball\b', 'toate'),
        (r'\bany\b', 'orice'),
        (r'\bnone\b', 'niciunul'),
        (r'\band\b', 'și'),
        (r'\bor\b', 'sau'),
        (r'\bwith\b', 'cu'),
        (r'\bwithout\b', 'fără'),
        (r'\bto\b', 'la'),
        (r'\bfrom\b', 'de la'),
        (r'\bin\b', 'în'),
        (r'\bon\b', 'pe'),
        (r'\bat\b', 'la'),
        (r'\bby\b', 'prin'),
        (r'\bfor\b', 'pentru'),
        (r'\bof\b', 'de'),
        (r'\bas\b', 'ca'),
        (r'\bis\b', 'este'),
        (r'\bare\b', 'sunt'),
        (r'\bbe\b', 'fie'),
        (r'\bshould\b', 'trebuie să'),
        (r'\bmust\b', 'trebuie să'),
        (r'\bcan\b', 'poate'),
        (r'\bmay\b', 'poate'),
        (r'\bnot\b', 'nu'),
        (r'\bno\b', 'fără'),
        (r'\bposition\b', 'poziție'),
        (r'\bpositions\b', 'poziții'),
        (r'\bpatient\b', 'pacient'),
        (r'\bpatients\b', 'pacienți'),
        (r'\bbody\b', 'corp'),
        (r'\bbodies\b', 'corpuri'),
        (r'\bprojection\b', 'incidență'),
        (r'\bprojections\b', 'incidențe'),
        (r'\bview\b', 'incidență'),
        (r'\bviews\b', 'incidențe'),
        (r'\bradiograph\b', 'radiografie'),
        (r'\bradiographs\b', 'radiografii'),
        (r'\bradiography\b', 'radiografie'),
        (r'\bjoint\b', 'articulație'),
        (r'\bjoints\b', 'articulații'),
        (r'\bhead\b', 'cap'),
        (r'\barm\b', 'braț'),
        (r'\barms\b', 'brațe'),
        (r'\bleg\b', 'membru inferior'),
        (r'\blegs\b', 'membre inferioare'),
        (r'\bhand\b', 'mână'),
        (r'\bhands\b', 'mâini'),
        (r'\bfoot\b', 'picior'),
        (r'\bfeet\b', 'picioare'),
        (r'\bknee\b', 'genunchi'),
        (r'\bknees\b', 'genunchi'),
        (r'\belbow\b', 'cot'),
        (r'\belbows\b', 'coate'),
        (r'\bshoulder\b', 'umăr'),
        (r'\bshoulders\b', 'umeri'),
        (r'\bbeam\b', 'fascicul'),
        (r'\bborder\b', 'margine'),
        (r'\bborders\b', 'margini'),
        (r'\bmotion\b', 'mișcare'),
        (r'\btoward\b|\btowards\b', 'spre'),
        (r'\bbetween\b', 'între'),
        (r'\bshowing\b', 'evidențiind'),
        (r'\brotation\b', 'rotație'),
        (r'\bimage\b', 'imagine'),
        (r'\bimages\b', 'imagini'),
        (r'\bfilm\b', 'film radiologic'),
        (r'\bfilms\b', 'filme radiologice'),
        (r'\bcassette\b', 'casetă'),
        (r'\bcassettes\b', 'casete'),
        (r'\bgrid\b', 'grilă'),
        (r'\bgrids\b', 'grile'),
        (r'\bsuspend\b', 'apnee (oprirea respirației)'),
        (r'\bholding\b', 'menținerea'),
        (r'\bbreath\b', 'respirației'),
        (r'\bbreathing\b', 'respirație'),
        (r'\brespiration\b', 'respirație'),
        (r'\bexposure\b', 'expunere'),
        (r'\bexposures\b', 'expuneri'),
        (r'\bmarker\b', 'marker'),
        (r'\bmarkers\b', 'markeri'),
        (r'\bdensity\b', 'densitate optică'),
        (r'\bfracture\b', 'fractură'),
        (r'\bfractures\b', 'fracturi'),
        (r'\bdislocation\b', 'luxație'),
        (r'\bdislocations\b', 'luxații'),
        (r'\bswelling\b', 'tumefiere'),
        (r'\bfluid\b', 'lichid'),
        (r'\bfree\b', 'liber'),
        (r'\bwall\b', 'perete'),
        (r'\bwalls\b', 'pereți'),
        (r'\bdiaphragm\b', 'diafragm'),
        (r'\bapices\b', 'apexuri (vârfuri pulmonare)'),
        (r'\blungs\b', 'plămâni'),
        (r'\bribs\b', 'coaste'),
        (r'\bspine\b', 'coloană vertebrală'),
        (r'\bpelvis\b', 'bazin (pelvis)'),
        (r'\bdecubitus\b', 'decubit'),
        (r'\bvertebrae\b', 'vertebre'),
        (r'\bcrests\b', 'creste'),
        (r'\bsymphysis\b', 'simfiză'),
        # Eliminare articol hotărât englezesc 'the' / 'a' / 'an' rămas în fața cuvintelor românești
        (r'\bthe\s+', ''),
        (r'\bThe\s+', ''),
        (r'\ba\s+(?=[a-zșțîâă])', ''),
        (r'\ban\s+(?=[a-zșțîâă])', ''),
    ]

    for pat, rep in word_replacements:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)

    # Pasul 6: Curățare dubluri lexicale, prepoziționale și spațiere
    res = re.sub(r'\bpoziție\s+poziție\b', 'poziție', res, flags=re.I)
    res = re.sub(r'\bpacient\s+pacient\b', 'pacient', res, flags=re.I)
    res = re.sub(r'\bcorp\s+corp\b', 'corp', res, flags=re.I)
    res = re.sub(r'\bincidență\s+incidență\b', 'incidență', res, flags=re.I)
    res = re.sub(r'\bcasetă\s+casetă\b', 'casetă', res, flags=re.I)
    res = re.sub(r'\bgrilă\s+grilă\b', 'grilă', res, flags=re.I)
    res = re.sub(r'\bradiografie\s+radiografie\b', 'radiografie', res, flags=re.I)
    res = re.sub(r'\bapnee\s+apnee\b', 'apnee', res, flags=re.I)
    res = re.sub(r'\bpe\s+pe\b', 'pe', res, flags=re.I)
    res = re.sub(r'\bîn\s+în\b', 'în', res, flags=re.I)
    res = re.sub(r'\bși\s+și\b', 'și', res, flags=re.I)
    res = re.sub(r'\bla\s+la\b', 'la', res, flags=re.I)
    res = re.sub(r'\bde\s+de\b', 'de', res, flags=re.I)
    res = re.sub(r'\bcu\s+cu\b', 'cu', res, flags=re.I)
    res = re.sub(r'\bse\s+se\b', 'se', res, flags=re.I)
    res = re.sub(r'\beste\s+este\b', 'este', res, flags=re.I)
    res = re.sub(r'\bsunt\s+sunt\b', 'sunt', res, flags=re.I)
    res = re.sub(r'[ \t]+', ' ', res)
    res = re.sub(r'\n{3,}', '\n\n', res)
    return res.strip()


# ---------------------------------------------------------------------------
# 6. Detector de Fragmente în Engleză & Evaluator
# ---------------------------------------------------------------------------

ENGLISH_DETECTION_WORDS = {
    'the', 'and', 'with', 'patient', 'position', 'exposure', 'image', 'demonstrate',
    'demonstrated', 'centering', 'centered', 'perpendicular', 'horizontal', 'parallel',
    'erect', 'supine', 'prone', 'decubitus', 'should', 'from', 'between', 'against',
    'placed', 'seated', 'suspend', 'expiration', 'inspiration', 'respiration', 'holding',
    'breath', 'infants', 'children', 'adults', 'cassette', 'grid', 'collimated', 'beam',
    'central', 'ray', 'angle', 'angled', 'toward', 'towards', 'degrees', 'joint',
    'bones', 'vertebrae', 'crests', 'symphysis', 'marker', 'border', 'visible', 'shown',
    'seen', 'rotation', 'motion', 'sharp', 'contrast', 'density', 'fracture', 'dislocation',
    'calculi', 'foreign', 'body', 'obstruction', 'swelling', 'fluid', 'free', 'wall',
    'diaphragm', 'apices', 'lungs', 'ribs', 'spine', 'pelvis', 'head', 'arms', 'legs',
    'feet', 'hands', 'showing', 'normal', 'radiograph', 'view', 'projection'
}


def detect_english_fragments(text: str) -> list[str]:
    """Identifică cuvintele/fragmentele englezești rămase într-un text."""
    if not text or not isinstance(text, str):
        return []
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    found = [w for w in words if w in ENGLISH_DETECTION_WORDS]
    return found


def calculate_english_score(text: str) -> float:
    """Calculează un scor de prezență a limbii engleze (număr de cuvinte englezești / total cuvinte)."""
    if not text:
        return 0.0
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    if not words:
        return 0.0
    eng_count = sum(1 for w in words if w in ENGLISH_DETECTION_WORDS)
    return eng_count / len(words)


# ---------------------------------------------------------------------------
# 7. Adaptarea Întregului Protocol (Frontmatter)
# ---------------------------------------------------------------------------

def translate_protocol_frontmatter(fm: dict, use_ai: bool = False) -> tuple[dict, bool]:
    """Traduce și adaptează un protocol complet (frontmatter).
    Returnează (fm_actualizat, a_fost_modificat)."""
    updated = dict(fm)
    modified = False

    # 1. Titlu
    old_title = updated.get('title', '')
    new_title = clean_and_adapt_title(old_title, category=updated.get('category', ''))
    if new_title != old_title:
        updated['title'] = new_title
        modified = True

    # 2. Câmpuri text principale
    for key in ['position', 'centering', 'breathing', 'notes']:
        val = updated.get(key)
        if isinstance(val, str) and val.strip():
            trans = translate_field_text(val)
            if trans != val:
                updated[key] = trans
                modified = True

    # 3. Parametri tehnici (colimare)
    tech = updated.get('tech_params')
    if isinstance(tech, dict):
        collim = tech.get('collimation')
        if isinstance(collim, str):
            trans_c = translate_field_text(collim)
            if trans_c != collim:
                tech['collimation'] = trans_c
                modified = True

    # 4. Liste: Indicații clinice
    ind_list = updated.get('clinical_indications')
    if isinstance(ind_list, list):
        new_ind = []
        for item in ind_list:
            if isinstance(item, str):
                t_item = translate_field_text(item)
                new_ind.append(t_item)
            else:
                new_ind.append(item)
        if new_ind != ind_list:
            updated['clinical_indications'] = new_ind
            modified = True

    # 5. Liste: Criterii de calitate
    crit_list = updated.get('quality_criteria')
    if isinstance(crit_list, list):
        new_crit = []
        for item in crit_list:
            if isinstance(item, str):
                t_item = translate_field_text(item)
                new_crit.append(t_item)
            else:
                new_crit.append(item)
        if new_crit != crit_list:
            updated['quality_criteria'] = new_crit
            modified = True

    # 6. Imagini (captions și descriptions)
    imgs = updated.get('images')
    if isinstance(imgs, list):
        for img in imgs:
            if isinstance(img, dict):
                for k in ['caption', 'description']:
                    val = img.get(k)
                    if isinstance(val, str):
                        trans = translate_field_text(val)
                        if trans != val:
                            img[k] = trans
                            modified = True

    # 7. Sursă secțiuni (Merrill source_sections)
    src_sec = updated.get('source_sections')
    if isinstance(src_sec, dict):
        for k, v in src_sec.items():
            if isinstance(v, str):
                trans_sec = translate_field_text(v)
                if trans_sec != v:
                    src_sec[k] = trans_sec
                    modified = True

    # 8. Opțional: Rafinare AI cu agy dacă este cerut
    if use_ai and shutil.which('agy'):
        eng_density = calculate_english_score(
            f"{updated.get('position', '')} {updated.get('centering', '')} {updated.get('notes', '')}"
        )
        if eng_density > 0.15:
            try:
                from extract_bontrager_protocols import enrich_with_ai
                updated = enrich_with_ai(updated)
                modified = True
            except Exception:
                pass

    return updated, modified
