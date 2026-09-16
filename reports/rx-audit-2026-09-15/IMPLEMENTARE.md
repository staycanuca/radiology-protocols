# Implementarea lotului RX — 15 septembrie 2026

## Actualizare: transfer în aplicația principală

La solicitarea utilizatorului, toate cele zece fișe au fost mutate în `docs/rx/`, în categoriile anatomice corespunzătoare, pentru revizuire directă. Biblioteca conține acum 32 de protocoale RX, dintre care aceste zece păstrează statutul de ciornă nevalidată clinic. Linkurile de categorie, indexul formularelor și site-ul construit au fost actualizate.

Editorul RX păstrează la salvare sursele, incidențele detaliate și metadatele de revizuire care nu au câmpuri dedicate în formular. Transferul nu atribuie aprobare clinică. Originalele Workbench sunt păstrate în `.protocol-workbench/backups/rx-library-transfer/`.

Verificare: 12 teste pentru transfer, editor, renderer și index au trecut; construcția MkDocs s-a încheiat cu succes. Secțiunile de mai jos descriu etapa inițială, înaintea transferului.

## Disponibil în aplicație

- Zece ciorne noi în Workbench, cu indicații, incidențe distincte, criterii de calitate, surse și câmpuri de revizuire. [Lista și documentele](proposals/README.md).
- Cele 22 de protocoale publicate au formulările comune de radioprotecție actualizate. Poziționarea toracală nu mai conține titlul extras eronat „Terminology”. Copiile anterioare sunt în `.protocol-workbench/backups/rx-expansion-2026-09-15/docs/rx/`.
- Template-ul nu atribuie automat kV, mAs, SID, grad de recomandare sau clasă de doză când lipsesc datele.
- Extragerea RX respinge titlurile generice identificate în locul poziției pacientului.
- Scriptul `scripts/prepare_rx_rollout.py` poate fi reluat fără suprascrierea ciornelor existente. Exporturile din acest raport reflectă ciornele la ultima rulare.

## De completat înainte de utilizarea clinică

Parametrii aparatului și adaptările locale necesită validare de către echipa clinică. Ciornele sunt marcate `draft_not_for_clinical_use`; validatorul împiedică publicarea în această stare.

Imaginile noilor fișe nu sunt încă selectate și validate. Cele două imagini din biblioteca existentă semnalate în audit păstrează necesitatea verificării drepturilor și metadatelor; acestea nu au fost inventate sau certificate prin această actualizare.

Pentru bilanțul scheletic, fișa este un cadru de lucru cu trimitere la seturile ESPR inițial/de control. Checklistul regional integral și traseul de neuroimagistică/comunicare rămân explicit obligatorii pentru revizuire. Fișa nu este încă un protocol tehnic complet.

Variantele suplimentare ale protocoalelor existente din audit rămân etapa următoare. Cele zece ciorne nu au fost adăugate la numărul protocoalelor publicate.

## Proveniență și verificare

Sursele sunt consemnate prin URL, instituție, secțiune și sinteză editorială. Consultarea web nu este prezentată ca descărcare de fișier și nu produce un hash fictiv. Schimbările ulterioare pot fi reanalizate în Workbench; câmpurile redactate sunt protejate de suprascriere automată.

Testele acoperă lipsa valorilor clinice implicite, respingerea titlurilor la extragere, generarea celor zece fișe, păstrarea editărilor la reluare și blocarea publicării ciornelor. Au fost regenerate indexurile aplicației.
