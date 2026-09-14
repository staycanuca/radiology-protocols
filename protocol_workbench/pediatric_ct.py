"""Build pediatric CT review drafts. No scanner-specific exposure settings are inferred."""
from datetime import date
import copy
import yaml

# Proposed editorial intervals, not universal AAPM technique-chart thresholds.
AGE_GROUPS = [('0-12-luni', '0–<12 luni', 0, 12), ('1-5-ani', '1–<5 ani', 12, 60),
              ('5-10-ani', '5–<10 ani', 60, 120), ('10-15-ani', '10–<15 ani', 120, 180),
              ('15-18-ani', '15–<18 ani', 180, 216)]
WEIGHT_GROUPS = [('sub-5-kg', '<5 kg', 0, 5), ('5-15-kg', '5–<15 kg', 5, 15),
                 ('15-30-kg', '15–<30 kg', 15, 30), ('30-50-kg', '30–<50 kg', 30, 50),
                 ('peste-50-kg', '≥50 kg, vârstă <18 ani', 50, None)]
SOURCES = {
    'head': ('AAPM — Pediatric Routine Head CT, v1.1, 2015', 'https://www.aapm.org/pubs/CTProtocols/documents/PediatricRoutineHeadCT.pdf'),
    'chest': ('AAPM — Pediatric Routine Chest CT, 2017', 'https://www.aapm.org/pubs/CTProtocols/documents/PediatricRoutineChestCT.pdf'),
    'abdomen': ('AAPM — Pediatric Routine Abdomen and Pelvis CT, 2017', 'https://www.aapm.org/pubs/CTProtocols/documents/PediatricRoutineAbdomenPelvisCT.pdf'),
}
COMMON_SOURCES = [
    ('Image Gently — CT', 'https://www.imagegently.org/Procedures/Computed-Tomography'),
    ('Image Gently — dezvoltarea protocoalelor pediatrice', 'https://imagegently.org/Procedures/Interventional-Radiology/Protocols'),
]
PENDING = 'DE CONFIGURAT PE APARAT'
FAMILIES = {
    'head': {'name': 'CT craniu pediatric nativ', 'category': 'neuro', 'slug': 'ct-craniu-pediatric-nativ',
             'position': 'Decubit dorsal, capul centrat și stabilizat; protejarea alinierii cervicale după context.',
             'start': 'Foramen magnum', 'end': 'Vertex', 'phase': 'Nativ',
             'indications': ['Întrebare clinică intracraniană pentru care radiologul confirmă CT nativ.'],
             'task': 'Verifică hemoragia, ventriculii, efectul de masă și calota, potrivit întrebării clinice.'},
    'chest': {'name': 'CT torace pediatric de rutină', 'category': 'chest', 'slug': 'ct-torace-pediatric',
              'position': 'Decubit dorsal, centrat; brațele ridicate dacă este posibil.',
              'start': 'Apexuri pulmonare', 'end': 'Baze pulmonare', 'phase': 'Unică; nativ SAU postcontrast, după indicație',
              'indications': ['Întrebare clinică toracică pentru care radiologul confirmă CT de rutină.'],
              'task': 'Verifică plămânii, mediastinul și pleura. Alegerea contrastului se stabilește înainte de achiziție.'},
    'abdomen': {'name': 'CT abdomen-pelvis pediatric de rutină', 'category': 'abdomen', 'slug': 'ct-abdomen-pelvis-pediatric',
                'position': 'Decubit dorsal, centrat; stabilizare adaptată cooperării.',
                'start': 'Dom hepatic', 'end': 'Simfiză pubiană; limite ajustate indicației',
                'phase': 'Unică; faza și contrastul aprobate înainte de scanare',
                'indications': ['Întrebare clinică abdomino-pelvină pentru care radiologul confirmă CT.'],
                'task': 'Verifică organele și structurile relevante indicației. Contrastul intravenos și enteric se decid separat.'},
}


def build_drafts():
    drafts = []
    for family, config in FAMILIES.items():
        for suffix, label, lower, upper in (AGE_GROUPS if family == 'head' else WEIGHT_GROUPS):
            selection = {'basis': 'age_months' if family == 'head' else 'weight_kg',
                         'lower_inclusive': lower, 'upper_exclusive': upper, 'age_upper_exclusive_months': 216,
                         'grouping_status': 'proposed_for_local_review'}
            fm = {'title': config['name'] + ' — ' + label, 'slug': config['slug'] + '-' + suffix,
                  'modality': 'ct', 'category': config['category'], 'population': 'pediatric',
                  'pediatric_selection': selection, 'clinical_status': 'draft_not_for_clinical_use',
                  'author': 'Ciornă pregătită cu asistență AI — autorul clinic urmează să fie desemnat',
                  'last_updated': str(date.today()), 'clinical_indications': config['indications'],
                  'position': config['position'], 'protocol_type': 'non-contrast' if family == 'head' else 'conditional-contrast',
                  'contrast': {'agent': 'N/A' if family == 'head' else 'De selectat conform indicației și politicii pediatrice locale'},
                  'tech_params': {key: PENDING for key in ('kv', 'mas', 'aec', 'pitch', 'rotation_time', 'collimation', 'slice_thickness', 'scan_mode')},
                  'series': [{'name': config['phase'], 'start': config['start'], 'end': config['end'],
                              'delay': '0 sec' if family == 'head' else PENDING, 'thickness': PENDING}],
                  'recons': [{'acquisition': config['phase'], 'plane': 'Axial; MPR după indicație',
                              'kernel': PENDING, 'thickness_increment': PENDING, 'ir_strength': PENDING}],
                  'images': [], 'review_required_fields': [
                      'Confirmarea pragurilor de grupare pentru populația locală',
                      'Model CT, versiune software și preset pediatric validat',
                      'Completarea tech_params și reconstrucțiilor pentru grupă',
                      'Ținte locale de doză și criterii de acceptare a calității',
                  ]}
            if family != 'head':
                fm['review_required_fields'].append('Contrast: selecție, doză, concentrație, debit și întârziere aprobate local')
            body = f'''# {fm['title']}

!!! warning "Ciornă pentru revizuire — nu se utilizează clinic"
    Pragurile sunt propuneri de organizare. Presetările nu sunt validate pentru un aparat.

## Selectarea grupei

**{label}.** Limita inferioară este inclusă, cea superioară exclusă. Pentru grupele de greutate se verifică și vârsta sub 18 ani. Greutatea nu înlocuiește evaluarea dimensiunilor pacientului la alegerea tehnicii.

## Planul examinării

{config['task']}

## Înaintea utilizării

Recenzorul completează câmpurile marcate **{PENDING}**, stabilește pregătirea și măsurile de siguranță locale și rezolvă lista `review_required_fields`. Câmpul `clinical_status` se actualizează numai după revizuire. Nu există valori implicite de adult sau doze de contrast calculate de această ciornă.

## Ilustrație

Imaginea atașată este un exemplu de anatomie/patologie, nu etalon de expunere, normalitate sau potrivire cu grupa. Vârsta/greutatea cazului ilustrat nu trebuie dedusă din grupa acestui dosar.
'''
            drafts.append({'family': family, 'group': label, 'fm': copy.deepcopy(fm),
                           'document': '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + body})
    return drafts
