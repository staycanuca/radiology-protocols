"""Ten source-backed RX drafts for the approved September 2026 expansion."""
from copy import deepcopy
from datetime import date
from scripts.render_rx_protocol import render_rx_document, PENDING

BATCH = 'rx-expansion-2026-09-15'
SOURCES = {
    'aapm': dict(title='AAPM PS 8-A — Patient Gonadal and Fetal Shielding',
        url='https://www.aapm.org/org/policies/details.asp?id=2552', institution='AAPM', section='Policy text',
        summary='Sinteză: AAPM recomandă renunțarea la ecranarea gonadală/fetală de rutină a pacientului. Politica locală distinge pacientul de personal și însoțitor.'),
    'nnuh': dict(title='NNUH — Justification Criteria & Technique Guide, v8, februarie 2024',
        url='https://www.nnuh.nhs.uk/publication/download/justification-criteria-technique-guide-for-plain-radiological-examinations-version-8/',
        institution='Norfolk and Norwich University Hospitals NHS', section='Secțiunile anatomice; coloană toracală p.36; Appendix 6 p.48',
        summary='Sinteză: ghid instituțional de selecție a incidențelor RX. Include proiecții pentru oase lungi, coloană și măsurători de membre inferioare. Detaliile echipamentului NNUH nu sunt presetări locale.'),
    'humerus': dict(title='RCH — Humeral shaft fractures, Emergency Department',
        url='https://www.rch.org.au/clinicalguide/guideline_index/fractures/Humeral_shaft_fractures_Emergency_Department/', institution='Royal Children’s Hospital Melbourne', section='5. Radiological investigations',
        summary='Sinteză: în evaluarea fracturii diafizare de humerus la copil se folosesc proiecții AP și laterală. Ghidul clinic nu furnizează un tabel universal de expunere.'),
    'antebrat': dict(title='RCH — Radius/ulna shaft fractures, Emergency Department',
        url='https://www.rch.org.au/clinicalguide/guideline_index/fractures/Radialulna_shaft_diaphysis_fractures_Emergency_Department/', institution='Royal Children’s Hospital Melbourne', section='5. Radiological investigations',
        summary='Sinteză: AP și profil ale antebrațului, cu cotul și pumnul incluse. Dacă articulațiile nu pot fi evaluate adecvat, sunt necesare imagini dedicate pentru leziunile asociate.'),
    'femur': dict(title='RCH — Femoral shaft fractures, Emergency Department',
        url='https://www.rch.org.au/clinicalguide/guideline_index/fractures/femoral_shaft_emergency/', institution='Royal Children’s Hospital Melbourne', section='5. Radiological investigations',
        summary='Sinteză: examinarea pediatrică a diafizei femurale folosește AP și profil, cu întreg femurul, șoldul și genunchiul incluse. Mișcările pot fi dureroase și necesită adaptare.'),
    'gamba': dict(title='RCH — Tibial shaft fractures, Emergency Department',
        url='https://www.rch.org.au/clinicalguide/guideline_index/fractures/tibial_shaft_emergency/', institution='Royal Children’s Hospital Melbourne', section='6–7. Investigations and radiographic appearances',
        summary='Sinteză: AP și profil ale tibiei/fibulei, incluzând genunchiul și glezna. Fractura copilului mic poate fi ocultă inițial; incidențele suplimentare și reevaluarea se decid clinic.'),
    'clavicula': dict(title='RCH — Clavicle fractures, Emergency Department',
        url='https://www.rch.org.au/clinicalguide/guideline_index/fractures/Clavicle_fractures_Emergency_Department/', institution='Royal Children’s Hospital Melbourne', section='5. Radiological investigations',
        summary='Sinteză: ghidul pediatric descrie AP și AP cu angulație cefalică de 15 grade. Leziunile mediale sau deplasate necesită evaluare clinică specifică; nu se forțează poziționarea.'),
    'scolioza': dict(title='RCH — Scoliosis, referral guideline',
        url='https://www.rch.org.au/ortho/for_health_professionals/Scoliosis/', institution='Royal Children’s Hospital Melbourne', section='Investigations',
        summary='Sinteză: evaluarea inițială a curburilor coloanei la copil utilizează radiografii ale întregii coloane în ortostatism, PA și profil. EOS este o opțiune unde este disponibil.'),
    'telemetrie': dict(title='RCH — Limb Reconstruction, Clinic',
        url='https://www.rch.org.au/limbrecon/the_lr_process/Clinic/', institution='Royal Children’s Hospital Melbourne', section='Imaging',
        summary='Sinteză: evaluarea reconstrucției membrelor poate utiliza EOS pentru lungimi și unghiuri. Documentul este contextual; tehnica de telemetrie se completează din ghidul tehnic și configurația locală.'),
    'bilant': dict(title='ESPR/ESR — Imaging of suspected child abuse, 2024',
        url='https://link.springer.com/article/10.1007/s00330-024-11052-4', institution='European Society of Paediatric Radiology', section='Skeletal survey; Table 4a/4b',
        summary='Sinteză: bilanțul scheletic pentru suspiciune de abuz folosește proiecții regionale standardizate și o evaluare ulterioară. Setul inițial diferă de cel de control; aplicarea depinde de vârstă și context.'),
    'corp-strain': dict(title='RCH — Foreign body ingestion',
        url='https://www.rch.org.au/clinicalguide/guideline_index/Foreign_body_ingestion/', institution='Royal Children’s Hospital Melbourne', section='Investigations',
        summary='Sinteză: radiografia este indicată selectiv pentru obiect necunoscut, baterie, magneți, obiect cu risc sau copil simptomatic. La copilul mic poate include gâtul, toracele și abdomenul. Ingestiile cu risc mic nu necesită automat imagistică.'),
    'neonatal': dict(title='East of England Neonatal ODN — NEC guideline, mai 2024',
        url='https://networks.nhs.uk/?attachment=17274&document_file=1985&document_type=document&download_document_file=1', institution='East of England Neonatal Operational Delivery Network', section='4.2.1 Investigations; Appendix 1',
        summary='Sinteză: evaluarea NEC include radiografie abdominală AP, cu decubit lateral stâng când este necesar. La copilul care nu poate fi întors se poate folosi profil cu rază orizontală în decubit dorsal. Reevaluarea este ghidată clinic.'),
}


def view(name, position, coverage, quality, condition='Parte a setului inițial justificat de radiolog'):
    return dict(name=name, condition=condition, position=position, centering=coverage, quality=quality)


SPECS = [
    dict(slug='rx-humerus-ap-profil', title='RX humerus — AP și profil', category='membru-superior',
        sources=['humerus', 'nnuh'], population='Adult / pediatric — tehnici validate separat',
        indications=['Suspiciune de leziune osoasă humerală după traumatism; control justificat al unei leziuni cunoscute.'],
        views=[view('AP humerus', 'Membrul sprijinit; orientare AP adaptată toleranței.', 'Humerus integral, cu articulațiile vecine.', 'Acoperire completă, detaliu cortical și absența mișcării.'),
               view('Profil humerus', 'Proiecție laterală adaptată fără rotații forțate în traumă.', 'Același segment și capetele articulare.', 'Proiecție complementară AP, cu limitele tehnice documentate.')],
        notes='Nu se mobilizează forțat brațul dureros. Dacă problema este localizată proximal sau distal, radiologul poate selecta protocolul articular adecvat.', image_query='humerus fracture radiograph'),
    dict(slug='rx-antebrat-ap-profil', title='RX antebraț — radius și ulna', category='membru-superior',
        sources=['antebrat', 'nnuh'], population='Adult / pediatric — tehnici validate separat',
        indications=['Traumatism al antebrațului sau evaluare justificată a unei fracturi cunoscute.'],
        views=[view('AP antebraț', 'Antebrațul sprijinit în orientare AP, fără forțarea extensiei.', 'Radius și ulna integral, cot și pumn.', 'Ambele oase și relațiile articulare evaluabile.'),
               view('Profil antebraț', 'Orientare laterală adaptată mobilității; sprijin radiotransparent.', 'Cotul și pumnul în limitele imaginii.', 'Proiecție laterală utilă pentru alinierea osoasă; documentarea rotației reziduale.')],
        notes='Cotul sau pumnul insuficient vizualizate se examinează țintit, după decizia radiologului. Se verifică leziunile articulare asociate.', image_query='radius ulna fracture radiograph'),
    dict(slug='rx-femur-ap-profil', title='RX femur — AP și profil', category='membru-inferior',
        sources=['femur', 'nnuh'], population='Adult / pediatric — tehnici validate separat',
        indications=['Traumatism cu suspiciune de fractură femurală; control justificat al unei leziuni femurale.'],
        views=[view('AP femur', 'Decubit dorsal; membrul susținut în poziția tolerată.', 'Femur integral, șold și genunchi; achiziții suprapuse dacă detectorul nu acoperă lungimea.', 'Continuitatea segmentului, fără zonă omisă între imagini.'),
               view('Profil femur', 'Adaptat durerii și imobilizării; rază orizontală dacă mobilizarea nu este permisă.', 'Segmentul complet, inclusiv extremitățile articulare.', 'Acoperire și orientare documentate; detaliu osos util.')],
        notes='Poziționarea se coordonează cu echipa clinică; suspiciunea de fractură nu justifică rotații sau flexii forțate.', image_query='femoral shaft fracture x ray'),
    dict(slug='rx-gamba-ap-profil', title='RX gambă — tibie și fibulă', category='membru-inferior',
        sources=['gamba', 'nnuh'], population='Adult / pediatric — tehnici validate separat',
        indications=['Suspiciune de fractură tibială/fibulară; la copil, suspiciune clinică de fractură ocultă a gambei.'],
        views=[view('AP gambă', 'Membrul sprijinit, orientare AP în limita toleranței.', 'Tibie și fibulă integral, genunchi și gleznă.', 'Ambele oase și articulațiile incluse, fără tăierea extremităților.'),
               view('Profil gambă', 'Proiecție laterală adaptată imobilizării și durerii.', 'Aceleași limite anatomice.', 'Alinierea și corticalele evaluabile în proiecție complementară.')],
        notes='Un examen inițial fără leziuni vizibile nu exclude fractura copilului mic. Reexaminarea ori incidențele suplimentare se stabilesc clinic.', image_query='tibia fibula fracture radiograph'),
    dict(slug='rx-clavicula', title='RX claviculă', category='membru-superior',
        sources=['clavicula', 'nnuh'], population='Adult / pediatric — tehnici validate separat',
        indications=['Traumatism localizat cu suspiciune de fractură claviculară; control selectiv indicat clinic.'],
        views=[view('AP claviculă', 'Ortostatism sau decubit, după stabilitatea pacientului.', 'Clavicula completă și extremitățile ei.', 'Contur osos și deplasare evaluabile.'),
               view('AP axială claviculă', 'Pacientul rămâne sprijinit; proiecția cefalică este adaptată clinic.', 'Clavicula în întregime.', 'Proiecție complementară pentru aprecierea deplasării.', 'Ghidul RCH pediatric descrie 15° cefalic; confirmare în tehnica locală.')],
        notes='Durerea sau suspiciunea de leziune sternoclaviculară/vasculară impun coordonare cu echipa clinică, fără manevre forțate.', image_query='clavicle fracture radiograph'),
    dict(slug='rx-coloana-totala-scolioza', title='RX coloană totală în ortostatism — scolioză', category='coloana',
        sources=['scolioza'], population='Copil / adolescent; extensia la adult necesită validare locală',
        indications=['Evaluarea unei deformări suspectate clinic; urmărire ortopedică justificată.'],
        views=[view('PA coloană totală în ortostatism', 'Postură erectă reproductibilă, fără corectare voluntară forțată a curburii.', 'Coloana completă și reperele necesare măsurătorilor solicitate.', 'Continuitate anatomică și repere vizibile pentru măsurători.'),
               view('Profil coloană totală', 'Ortostatism; brațele poziționate astfel încât să permită evaluarea profilului.', 'Acoperire longitudinală conform obiectivului ortopedic.', 'Profil sagital evaluabil și postură comparabilă.', 'Evaluare inițială; repetarea la control se justifică separat.')],
        notes='Înregistrarea poziției, a suporturilor și a utilizării corsetului permite comparații. Se validează tehnica de stitching/EOS înainte de utilizare.', image_query='scoliosis standing radiograph'),
    dict(slug='rx-telemetrie-membre-inferioare', title='RX telemetrie membre inferioare — axe și lungimi', category='membru-inferior',
        sources=['nnuh', 'telemetrie'], population='Pediatric / adult după indicația ortopedică',
        indications=['Măsurarea axelor mecanice sau a discrepanței de lungime pentru planificare/urmărire ortopedică.'],
        views=[view('AP membre inferioare în sprijin', 'Ortostatism stabil și reproductibil; sprijinul/compensarea diferenței se documentează.', 'Șolduri, genunchi și glezne în aceeași examinare calibrată.', 'Repere articulare vizibile; absența mișcării și a erorilor de asamblare.'),
               view('Achiziție alternativă pentru lungime', 'Tehnică separată stabilită de radiolog dacă sprijinul nu este posibil.', 'Repere și calibrare specifice metodei aprobate.', 'Metoda este declarată; nu se confundă măsurarea lungimii cu axa în sprijin.', 'Numai dacă indicată; nu se adaugă de rutină.')],
        notes='Distanța, calibrarea, metoda de asamblare și suporturile trebuie validate pe aparatul local. O imagine necalibrată nu este etalon pentru planificare.', image_query='leg length standing x ray'),
    dict(slug='rx-bilant-scheletic-suspiciune-abuz', title='RX bilanț scheletic pediatric — suspiciune de abuz fizic', category='pediatrie',
        sources=['bilant'], population='Pediatric; selecție după vârstă și evaluare specializată',
        indications=['Suspiciune de abuz fizic pentru care echipa pediatrică/radiologul solicită bilanț scheletic.'],
        views=[view('Bilanț inițial — listă regională', 'Examinare coordonată de personal cu experiență pediatrică.', 'Set regional conform tabelului 4a ESPR, cu selecție craniană în raport cu neuroimagistica.', 'Fiecare regiune și lateralitate verificate înainte de încheiere; checklistul complet se atașează.'),
               view('Bilanț de control', 'Programare și poziționare conform traseului specializat.', 'Set de control conform tabelului 4b, distinct de setul inițial.', 'Comparație cu imaginile inițiale și documentarea regiunilor examinate.', 'ESPR descrie reevaluarea la 11–14 zile; traseul trebuie aprobat local.')],
        notes='Ciorna nu înlocuiește checklistul complet ESPR/RCR. Nu se folosește o singură expunere de corp întreg. Constatările se comunică echipei; mecanismul leziunii nu se deduce numai din imagine.',
        extra_review=['Transcrierea și validarea integrală a checklistului regional ESPR 4a/4b; protocol de neuroimagistică și comunicare'], image_query='healing rib fractures child radiograph'),
    dict(slug='rx-corp-strain-ingerat', title='RX corp străin ingerat la copil', category='pediatrie',
        sources=['corp-strain'], population='Pediatric',
        indications=['Ingestie de baterie/magneți, obiect necunoscut ori cu risc; copil simptomatic, conform evaluării clinice.'],
        views=[view('Radiografie de localizare', 'Poziție adaptată vârstei și stării clinice.', 'La copilul mic, gât–torace–abdomen când localizarea este necunoscută; limitele se decid clinic.', 'Obiectul și limitele examinate sunt documentate; acoperire fără lacune.'),
               view('Proiecție complementară țintită', 'Poziționare adaptată segmentului, la decizia radiologului.', 'Regiunea unde diferențierea/localizarea rămâne neclară.', 'Clarificarea întrebării clinice fără repetarea inutilă a întregului câmp.', 'Selectiv; nu automat pentru toate ingestiile.')],
        notes='Obiectele cu risc și copilul instabil necesită comunicare imediată. Ingestiile cu risc mic pot să nu necesite imagistică. Suspiciunea de aspirație urmează un traseu separat.', image_query='esophagus coin x ray'),
    dict(slug='rx-abdomen-neonatal', title='RX abdomen neonatal — suspiciune de NEC / perforație', category='pediatrie',
        sources=['neonatal'], population='Nou-născut / prematur',
        indications=['Suspiciune clinică de enterocolită necrozantă sau perforație; reevaluare justificată de echipa neonatală.'],
        views=[view('AP abdomen în decubit dorsal', 'La incubator/pat, cu menținerea suportului și stabilității termice.', 'Abdomenul și limitele necesare evaluării solicitate.', 'Acoperire și expunere utile, fără artefacte care împiedică evaluarea.'),
               view('Decubit lateral stâng / profil cu rază orizontală', 'Dacă întoarcerea nu este sigură, tehnică laterală cu pacientul în decubit dorsal.', 'Abdomenul, cu rază orizontală când se caută aer liber.', 'Poziția și direcția fasciculului sunt înregistrate.', 'Selectiv, în suspiciunea de perforație sau la solicitarea radiologului.')],
        notes='Reevaluarea nu are un interval universal. Se coordonează cu neonatologul și se corelează cu ecografia când este indicată; suspiciunea de complicație se comunică rapid.', image_query='necrotizing enterocolitis radiograph'),
]


def build_drafts(source_records):
    from .completion import leaves
    from .app import now
    from uuid import uuid5, NAMESPACE_URL
    output = []
    for spec in SPECS:
        sources = [deepcopy(source_records[key]) for key in spec['sources'] + ['aapm']]
        primary = sources[0]
        fm = dict(title=spec['title'], slug=spec['slug'], modality='rx', category=spec['category'],
            population=spec['population'], author='Ciornă documentată — recenzor clinic de desemnat',
            last_updated=str(date.today()), clinical_status='draft_not_for_clinical_use',
            clinical_indications=spec['indications'], standard_views=deepcopy(spec['views']),
            position='Poziționare diferențiată pe incidențe; vezi lista de achiziții.',
            centering='Conform incidenței și acoperirii anatomice documentate.', sid_dff=PENDING,
            breathing='Adaptată incidenței și cooperării; de confirmat local.',
            tech_params={key: PENDING for key in ('kv', 'mas', 'grid', 'focal_spot', 'aec_chambers', 'filtration')},
            quality_criteria=['Acoperire și criterii specifice fiecărei incidențe, conform listei de mai jos.',
                              'Identificare, lateralitate, absența mișcării și verificarea expunerii conform sistemului local.'],
            protection=['Colimare la zona justificată și tehnică adaptată dimensiunilor pacientului.',
                        'Ecranarea pacientului conform politicii locale actualizate; protecția însoțitorilor se stabilește separat.'],
            notes=spec['notes'], images=[],
            review_required_fields=['Confirmarea indicațiilor și a aplicabilității surselor la populația locală',
                'Validarea fiecărei incidențe și a adaptărilor pentru traumatism/cooperare',
                'Configurarea kV, mAs, AEC/manual, SID, grilei, focarului și filtrării pe aparat',
                'Aprobarea radioprotecției și a criteriilor de calitate de către echipa locală',
                'Revizuirea imaginilor: relevanță, identificatori vizibili și drepturi de utilizare'] + spec.get('extra_review', []),
            source_mapping={key: dict(source_id=primary['id'], section=primary.get('section'), status='adaptare pentru revizuire')
                            for key in ('clinical_indications', 'standard_views')})
        document = render_rx_document(fm)
        document += '\n## Surse de documentare\n\n' + '\n'.join(
            f"- [{s['title']}]({s['url']}) — {s.get('section', '')}" for s in sources) + '\n'
        output.append(dict(id=uuid5(NAMESPACE_URL, BATCH + '/' + spec['slug']).hex,
            document=document, sources=sources, images=[], created_at=now(), updated_at=now(), status='draft',
            revision=1, batch=BATCH, manual_body=True,
            manual_fields=sorted(set(dict(leaves(fm))) | set(fm)),
            history=[dict(at=now(), revision=1, changed=['document', 'sources'], reason='Lot RX aprobat; ciornă pentru revizuire')]))
    return output
