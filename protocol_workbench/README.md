# Protocol Workbench

Unealtă standalone locală pentru documentarea, verificarea și importul protocoalelor CT, RX, IRM, US (`eco`) și fluoroscopie în aplicația din acest repository. Rulează separat de admin și de MkDocs, pe portul **5180**.

## Pornire

Din rădăcina proiectului:

```powershell
python -m pip install -r protocol_workbench/requirements.txt
python -m protocol_workbench.app
```

Deschide http://127.0.0.1:5180. Pe Windows poți folosi `start-workbench.bat` sau `start-workbench.ps1` după instalarea dependențelor. Oprește serverul cu Ctrl+C.

Dacă apare o eroare de proxy, serverul poate fi pornit dintr-un mediu cu acces la rețea restricționat. Oprește acea instanță și pornește launcherul din Windows/terminalul propriu. Instrumentul respectă configurarea proxy a mediului; nu încearcă să o ocolească. În rețele instituționale, verifică proxy-ul configurat cu administratorul rețelei.

Poți indica altă bibliotecă compatibilă:

```powershell
python -m protocol_workbench.app --repo C:\cale\radiology-protocols --port 5181
```

## Flux de lucru

1. Alege modalitatea și creează un dosar cu titlul protocolului.
2. Caută în biblioteca aplicației pentru a evita duplicatele. Alege **SUA — protocoale și ghiduri** pentru documente din cataloage americane sau **Europe PMC** pentru publicații internaționale. Poți filtra după instituție; modalitatea este cea selectată în bara laterală.
3. Atașează sursele rezultate sau URL-uri HTTPS directe către ghiduri/protocoale instituționale HTML/PDF. Instrumentul înregistrează URL-ul final, data accesării, amprenta SHA-256 și un extras de text. PDF-urile scanate necesită OCR extern. Accesibilitatea sursei nu dovedește autoritatea, actualitatea ori corectitudinea ei.
4. Sursele atașate completează automat câmpurile recunoscute din schema modalității. Valorile introduse manual sunt păstrate; panoul de sub editor arată proveniența, câmpurile lipsă și conflictele. Alege explicit o valoare din surse sau păstrează valoarea curentă. Extragerea este euristică, bazată pe reguli, și poate interpreta greșit contextul; verifică toate completările în documentul original. Textul brut rămâne în surse și poate fi inserat separat, la cerere.
5. Caută imagini în Wikimedia Commons și NLM Open-i, în paralel, sau atașează imagini prin upload/URL. Openverse este disponibil separat; accesul anonim poate fi refuzat. Căutarea folosește modalitatea protocolului, echivalențe română–engleză și ordonează imaginile după termenii din legendă/descriere, modalitate, atribuire și rezoluție. Introdu legenda, autorul, licența/permisiunea și pagina sursă. Open-i nu furnizează o licență a figurii în răspunsul utilizat; aceasta trebuie verificată în articol și completată înainte de atașare. Imaginile sunt convertite în JPEG fără EXIF, însă identificatorii înscriși în pixeli nu sunt eliminați automat.
6. Salvează și rulează verificările. Acestea controlează metadatele obligatorii, categoriile, structurile specifice modalității, existența surselor și a imaginilor, integritatea imaginilor și duplicatele de slug. Titlurile identice sunt semnalate. Nu se verifică automat exactitatea valorilor clinice sau echivalența semantică a protocoalelor.
7. Un recenzor verifică versiunea finală și confirmă explicit conținutul clinic, relevanța/anonymizarea imaginilor și drepturile de utilizare. Modificările în editor ori atașamente debifează confirmările în interfață.
8. Importă: se creează un fișier nou în `docs/<modalitate>/<categorie>/<slug>.md`, se copiază imaginile și se regenerează cei trei indici ai aplicației. Protocoalele existente nu sunt suprascrise. Dacă regenerarea unui index eșuează, importul rămâne înregistrat și interfața oferă reluarea regenerării.

Pentru lotul pediatric pregătit în această sesiune există 15 dosare în Workbench: cinci pentru CT craniu (`0–<12 luni`, `1–<5 ani`, `5–<10 ani`, `10–<15 ani`, `15–<18 ani`) și câte cinci pentru CT torace și CT abdomen-pelvis (`<5`, `5–<15`, `15–<30`, `30–<50`, `≥50 kg la copil/adolescent`). Sunt ciorne, nu protocoale importate. Fiecare are surse AAPM și Image Gently și o imagine candidată cu atribuire. Parametrii tehnici sunt marcați `DE CONFIGURAT PE APARAT`; validarea automată blochează importul până când sunt completați și revizuiți.

## Integrare și limite

### Completare și urmărirea modificărilor

- Completarea se execută la atașarea/reverificarea/eliminarea surselor și la salvarea ciornei. **Reanalizează toate sursele** folosește extrasele deja atașate; **Reverifică sursa online** descarcă din nou sursa respectivă. Nu există monitorizare periodică a internetului.
- Fiecare câmp preluat păstrează sursa, amprenta documentului, amprenta extrasului și valoarea aplicată. O valoare completată automat poate fi actualizată dacă nu a fost editată manual și sursele sunt de acord. Editările și ștergerile manuale sunt protejate.
- Diferențele dintre surse nu sunt combinate arbitrar. Alegerea utilizatorului este memorată și reevaluată când candidații se schimbă. Eliminarea sursei sau schimbarea titlului/modalității semnalează proveniența de reverificat.
- Ciornele noi includ un tabel al parametrilor, sincronizat cu YAML. Editarea manuală a tabelului oprește sincronizarea lui automată; textul clinic redactat manual este păstrat. Pentru documentele existente, verifică și coerența dintre YAML și text după completare.
- Sunt păstrate ultimele 100 de modificări, cu valori înainte/după și diferențe de document (maximum 16.000 caractere per diferență). Revizia transmisă de interfață previne salvarea sau importul peste o versiune modificată în altă filă. Un protocol încărcat pentru revizuire păstrează și amprenta fișierului original; schimbarea acestuia blochează suprascrierea.
- Biblioteca detectează modificările fișierelor existente. Istoricul și proveniența rămân în dosar; proveniența câmpurilor este inclusă și la import în `workbench_provenance`.
- Căutările de imagini reușite sunt păstrate în memorie cinci minute (maximum 32 de căutări); erorile parțiale sunt afișate și nu sunt memorate. Rezultatele duplicate după URL sunt eliminate. Scorul exprimă potrivirea textului, nu adecvarea clinică a imaginii.

API-uri consultate: [MediaWiki Imageinfo](https://www.mediawiki.org/wiki/API:Imageinfo), [NLM Open-i](https://catalog.data.gov/dataset/open-i), [Openverse API client și autentificare](https://docs.openverse.org/packages/js/api_client/index.html).

### Stocare și import

- Ciornele, extrasele surselor și imaginile de lucru sunt păstrate în `.protocol-workbench/`, exclus din Git. Acest folder trebuie inclus în backup dacă vrei să păstrezi dosarele.
- Importul include sursele, imaginile și declarația de revizuire în front matter. Corpul Markdown este redactat explicit, fără a injecta textele clinice implicite din rendererele existente. Imaginile și sursele sunt vizibile și în corpul documentului.
- Bibliotecile/modalitățile existente sunt citite direct din `docs/`. Panoul admin le vede la următoarea încărcare. MkDocs serve reconstruiește documentația; pentru un site static trebuie rulat build-ul și mecanismul de publicare obișnuit. Nu se efectuează deploy automat.
- Dacă ulterior salvezi protocolul prin editorul admin existent, acesta poate regenera corpul și elimina metadate necunoscute; păstrează dosarul Workbench ca evidență de proveniență și revizuire. Editorul admin nu a fost modificat.
- Recenzorul este declarat local; nu există autentificare, semnătură electronică, audit imuabil sau validare clinică automată. Nu este un PACS/DICOM viewer.
- Conexiunea la internet este necesară pentru căutări, extragerea surselor și descărcarea imaginilor. Erorile serviciilor externe sunt afișate, fără a fabrica rezultate. Sursele implicite de imagini nu necesită o cheie API; Openverse poate refuza accesul anonim.
- Serviciul ascultă numai pe `127.0.0.1`, verifică Host și folosește un token pentru operațiile de modificare. Descărcările cer HTTPS public, verifică redirecționările și limitează fișierele la 100 MB (configurabil prin `--max-upload-mb`). Este destinat unui singur utilizator local, nu expunerii pe internet.

Documentația furnizorilor: [Europe PMC REST](https://europepmc.org/RestfulWebService), [Wikimedia metadata](https://commons.wikimedia.org/wiki/Commons:Machine-readable_data/en).

## Surse americane

| Instituție | Acoperire în unealtă | Acces |
| --- | --- | --- |
| [UT Southwestern](https://www.utsouthwestern.edu/departments/radiology/protocols/) | CT, IRM, US, catalog comun diagnostic/fluoroscopie pentru RX și fluoro | Căutare în titlurile și numele PDF-urilor din catalog |
| [OHSU](https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/mri-protocols) | IRM | Căutare în titlurile protocoalelor HTML/PDF |
| [AAPM](https://www.aapm.org/pubs/ctprotocols/) | CT, protocoale și resurse tehnice | Căutare în titlurile și numele PDF-urilor |
| [AIUM](https://www.aium.org/resources/practice-parameters) | Ecografie, parametri de practică | Căutare în titlurile documentelor PDF/DOI; unele destinații pot restricționa accesul |
| [ACR Appropriateness Criteria](https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria) | Alegerea investigației după situația clinică | Link de consultare pe portalul ACR, separat de rezultate |
| [ACR Practice Parameters and Technical Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards) | Practică și standarde tehnice | Link de consultare pe portalul ACR, separat de rezultate |

Căutarea americană citește numai paginile de catalog configurate, fără explorare recursivă. Rezultatele sunt filtrate după titlu și numele fișierului, nu după textul integral al protocolului. Cataloagele sunt păstrate în memorie o oră, iar data accesării este afișată. Aceasta nu reprezintă data actualizării clinice. Maximum 100 de rezultate sunt afișate; restrânge termenii dacă sunt mai multe.

Folosește termeni scurți, precum `knee`, `head`, `thyroid`, `esophagram`. Sunt recunoscute și câteva echivalențe anatomice românești, de exemplu `genunchi`, `craniu`, `tiroidă`, `umăr`. Nu există traducere automată completă. Toți termenii semnificativi trebuie să fie prezenți, inclusiv prin echivalențele configurate.

Fiecare catalog raportează distinct numărul de documente, potrivirile și eventualele erori de acces/structură. ACR nu este prezentat ca rezultat al unei căutări automate. Catalogul comun RX/fluoro de la UT Southwestern are acoperire limitată pentru radiografia convențională. O pagină accesibilă nu garantează actualitatea documentului sau permisiunea de republicare a textului/imaginilor.

Sursele atașate de pe domeniile instituțiilor sunt etichetate automat cu instituția și regiunea SUA. Pentru legături DOI sau Wiley nu se deduce instituția numai din domeniul editorului. Revizuirea și importul folosesc același flux explicit ca înainte.

## Teste

```powershell
python -m pytest tests/test_protocol_workbench.py -q
python -m pytest tests/test_american_sources.py -q
python -m pytest tests/test_workbench_completion.py tests/test_smart_extractor.py -q
```

Testele folosesc surse și imagini sintetice și o bibliotecă temporară. Acoperă importul pentru toate modalitățile, revizuirea obligatorie, duplicatele, traversarea directoarelor, integritatea imaginilor, protecția solicitărilor și recuperarea după erori de indexare. Nu validează recomandări medicale.
