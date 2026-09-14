import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from protocol_workbench.pediatric_ct import build_drafts, AGE_GROUPS, WEIGHT_GROUPS
from protocol_workbench.app import frontmatter


def test_group_boundaries_are_unambiguous():
    for groups in (AGE_GROUPS, WEIGHT_GROUPS):
        assert groups[0][2] == 0
        for previous, following in zip(groups, groups[1:]):
            assert previous[3] == following[2]
    assert AGE_GROUPS[-1][3] == 216
    assert WEIGHT_GROUPS[-1][3] is None


def test_fifteen_unique_drafts_with_required_review_and_no_guessed_exposure():
    drafts = build_drafts()
    assert len(drafts) == 15
    assert len({d['fm']['slug'] for d in drafts}) == 15
    for draft in drafts:
        fm, _ = frontmatter(draft['document'])
        assert fm['pediatric_selection']['basis'] == ('age_months' if draft['family'] == 'head' else 'weight_kg')
        assert fm['review_required_fields']
        assert fm['clinical_status'] == 'draft_not_for_clinical_use'
        assert fm['tech_params']['kv'] == 'DE CONFIGURAT PE APARAT'
