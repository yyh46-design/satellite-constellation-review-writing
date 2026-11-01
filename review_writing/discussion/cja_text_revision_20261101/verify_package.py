"""Check the saved discussion package without changing any files."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
checks = json.loads((root / 'CHECKS.json').read_text(encoding='utf-8'))
text = (root / 'REVIEW_ROUTE_A_CN.md').read_text(encoding='utf-8')
source = (root / 'history/REVIEW_ROUTE_A_CN_CJA文字稿.md').read_text(encoding='utf-8')
baseline = root / '../orbit_design_route_a_20261031/REVIEW_ROUTE_A_CN.md'
register = json.loads((root / 'REFERENCE_REGISTER.json').read_text(encoding='utf-8'))
status = json.loads((root / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))

def sha(path):
    # Git can normalize CRLF during add/checkout; compare the UTF-8 text with LF.
    return hashlib.sha256(path.read_text(encoding='utf-8').encode('utf-8')).hexdigest()

def refs(value):
    return {int(n): entry for n, entry in re.findall(r'^\[(\d+)\] (.+)$', value, re.M)}

def ref_key(entry):
    return re.sub(r'\s+', '', entry.split(' [来源]')[0])[:90]

assert sha(root/'REVIEW_ROUTE_A_CN.md') == checks['document_lf_utf8_sha256'] == checks['dialogue_source_lf_utf8_sha256']
assert sha(baseline) == checks['baseline_document_lf_utf8_sha256']
for name, expected in checks['preserved_input_lf_utf8_sha256'].items():
    assert sha(root/name) == expected, name

assert len(re.findall(r'^# [1-5] ', text, re.M)) == checks['chapter_count'] == 5
assert len(re.findall(r'^\*\*表[1-5] ', text, re.M)) == checks['table_count'] == 5
formulas = re.findall(r'\$\$(.*?)\$\$', text, re.S)
assert len(formulas) == checks['display_formula_count'] == 2
assert formulas == re.findall(r'\$\$(.*?)\$\$', source, re.S)
notes = re.findall(r'^注[1-4]：.*$', text, re.M)
assert len(notes) == 5
assert notes == re.findall(r'^注[1-4]：.*$', source, re.M)
assert text.split('# 参考文献\n',1)[1] == source.split('# 参考文献\n',1)[1]

new_refs = refs(text)
assert list(new_refs) == list(range(1,90))
first_use = list(dict.fromkeys(int(n) for n in re.findall(r'\[(\d+)\]', text.split('# 参考文献\n')[0])))
assert first_use == list(range(1,90))
assert len(register['references']) == register['count'] == checks['reference_count'] == status['reference_count'] == 89
old_refs = refs(baseline.read_text(encoding='utf-8'))
inherited = [r for r in register['references'] if r['origin'] == 'INHERITED_ROUTE_A']
assert len(inherited) == len(old_refs) == 76
assert sorted(r['baseline_number'] for r in inherited) == list(range(1,77))
for record in register['references']:
    assert record['citation_as_in_manuscript'] == new_refs[record['number']]
    assert record['human_verified'] is False
    if record['origin'] == 'INHERITED_ROUTE_A':
        assert ref_key(old_refs[record['baseline_number']]) == ref_key(record['citation_as_in_manuscript'])
    for field in ['baseline_register', 'reading_record', 'input_notes']:
        if record.get(field):
            assert (root / record[field]).is_file(), record[field]
added = [r['number'] for r in register['references'] if r['origin'] == 'ADDED_IN_USER_PATCH']
assert added == register['added_reference_numbers'] == checks['added_reference_numbers']
assert len(added) == status['added_reference_count'] == 13
english = text.split('## Abstract\n\n',1)[1].split('\n\n',1)[0]
assert len(english.split()) == checks['english_abstract_whitespace_words'] == 191

for name in ['README.md','history/README.md','DIALOGUE_REVISION_NOTES_CN.md','REMAINING_REFINEMENTS_CN.md']:
    for target in re.findall(r'\]\(([^)]+)\)', (root/name).read_text(encoding='utf-8')):
        if not target.startswith(('http:', 'https:', '#')):
            assert ((root/name).parent / target).exists(), (name, target)
assert status['human_verified'] is False and status['submission_ready'] is False
assert status['chinese_scientific_content_frozen'] is False
assert status['new_original_full_text_reads_this_publication'] == 0
assert not list(root.rglob('*.pdf'))

print(json.dumps({
    'result':'PASS', 'chapters':5, 'tables':5, 'references':89,
    'baseline_references_retained':76, 'added_references':13,
    'first_use_sequential':True, 'protected_formulas':2, 'protected_table_notes':5,
    'english_abstract_whitespace_words':191,
    'document_lf_utf8_sha256':checks['document_lf_utf8_sha256'],
    'human_verified':False, 'submission_ready':False,
    'scope':'File, structure and preservation checks only.'
}, ensure_ascii=False, indent=2))
