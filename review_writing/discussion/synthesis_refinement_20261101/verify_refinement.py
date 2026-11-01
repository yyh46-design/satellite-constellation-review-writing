"""Compare this refinement with the previous saved package. Reads only; changes nothing."""
from pathlib import Path
import re
import json
import hashlib
import sys

root = Path(__file__).resolve().parent
new = (root / 'REVIEW_ROUTE_A_CN.md').read_text(encoding='utf-8')
old = (root / '../cja_text_revision_20261101/REVIEW_ROUTE_A_CN.md').read_text(encoding='utf-8')

def split(t):
    body, refs = t.split('# 参考文献\n', 1)
    return body, {int(n): e for n, e in re.findall(r'^\[(\d+)\] (.+)$', refs, re.M)}

def strip_annot(e):
    # authors + title: text before the first full stop that follows the title
    return re.sub(r'\s+', '', '.'.join(e.split('. ')[:2]))

bo, ro = split(old); bn, rn = split(new)
assert list(rn) == list(range(1, 90)) and len(ro) == 89
first = list(dict.fromkeys(int(x) for x in re.findall(r'\[(\d+)\]', bn)))
assert first == list(range(1, 90)), 'first-use order'

# map old number -> new number through the reference entries' bibliographic core
core_new = {strip_annot(e): n for n, e in rn.items()}
mapping = {o: core_new[strip_annot(e)] for o, e in ro.items()}
assert sorted(mapping.values()) == list(range(1, 90))
moved = {o: n for o, n in mapping.items() if o != n}
changed = [n for o, n in mapping.items() if ro[o] != rn[n]]
assert moved == {79: 80, 80: 81, 81: 79}, moved
assert sorted(changed) == [5, 34, 36, 38, 46], changed
assert bo.split('# 1 引言', 1)[0] == bn.split('# 1 引言', 1)[0], 'abstracts and keywords'

def secs(t):
    parts = re.split(r'(?m)^(#{1,2} .*)$', t); d = {}; cur = '_pre'
    for p in parts:
        if re.match(r'^#{1,2} ', p): cur = p.strip()
        else: d[cur] = d.get(cur, '') + p
    return d
so, sn = secs(bo), secs(bn)
assert list(so) == list(sn), 'headings'
for h in so:
    co = {mapping[int(x)] for x in re.findall(r'\[(\d+)\]', so[h])}
    cn = {int(x) for x in re.findall(r'\[(\d+)\]', sn[h])}
    assert co == cn, (h, co ^ cn)

assert re.findall(r'\$\$(.*?)\$\$', bo, re.S) == re.findall(r'\$\$(.*?)\$\$', bn, re.S)
assert re.findall(r'^注[1-4]：.*$', bo, re.M) == re.findall(r'^注[1-4]：.*$', bn, re.M)
assert len(re.findall(r'(?m)^\|', bo)) == len(re.findall(r'(?m)^\|', bn))
# Row counts alone miss changed values. Compare every table cell after the one
# documented abbreviation expansion and the reference-number mapping.
old_rows = re.findall(r'(?m)^\|.*$', bo)
new_rows = re.findall(r'(?m)^\|.*$', bn)
mapped_rows = [re.sub(r'\[(\d+)\]', lambda m: '[' + str(mapping[int(m[1])]) + ']', row)
               .replace('限时MILP', '限时混合整数线性规划（MILP）') for row in old_rows]
assert mapped_rows == new_rows, 'table contents'
for phrase in ['普遍适用的事前阈值', '主要来自Rossi', '本文的综合判断', '直接业务结果',
               '增长规律', '同条件的直接对照', '90.95%', '未形成统一可复现']:
    assert phrase in bn, phrase
chapters_2_to_4 = bn.split('# 2 ',1)[1].split('# 5 结论与展望')[0]
for n in ['19.73', '2304', '6173', '2.75', '90.95', '2000组']:
    assert n in chapters_2_to_4, n
conclusion = sn['# 5 结论与展望']
for phrase in ['小天体多器', '给定轨道', '少量主动成员', '缺少与事件对应的直接业务结果',
               '普遍适用的事前阈值', '限时设置', '条件性综合判断']:
    assert phrase in conclusion, ('conclusion', phrase)
assert '二十脉冲算例' in sn['## 4.3 动态更新与学习辅助决策']
assert '不取决于策略本身' not in bn
assert '只有会改变可行性或候选排序的资源反馈' not in conclusion

identity = json.loads((root/'INPUT_IDENTITY.json').read_text(encoding='utf-8'))
text_sha = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
assert text_sha(old) == identity['base_manuscript_lf_utf8_sha256'], '3536392 baseline text'
assert text_sha((root/'REFINEMENT_NOTES_CN.md').read_text(encoding='utf-8')) == identity['input_notes_lf_utf8_sha256']
register = json.loads((root/'REFERENCE_REGISTER.json').read_text(encoding='utf-8'))
assert [r['number'] for r in register['references']] == list(range(1,90))
for record in register['references']:
    assert record['citation_as_in_manuscript'] == rn[record['number']]
    assert mapping[record['previous_revision_number']] == record['number']
    assert record['human_verified'] is False
    for field in ['reading_record','baseline_register','input_notes','metadata_check_record','targeted_check_record']:
        if record.get(field):
            assert (root/record[field]).is_file(), record[field]
status = json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert status['reference_count'] == 89 and status['sources_added_this_revision'] == 0
assert status['human_verified'] is False and status['submission_ready'] is False
for name in ['README.md', 'INTEGRATION_NOTES_CN.md']:
    for target in re.findall(r'\]\(([^)]+)\)', (root/name).read_text(encoding='utf-8')):
        if not target.startswith(('http:', 'https:', '#')):
            assert ((root/name).parent/target).exists(), (name,target)

han = lambda s: len(re.findall(r'[一-鿿]', s))
counts = {h: {'old':han(so[h]), 'new':han(sn[h])}
          for h in ['## 1.2 相关研究与本文定位', '## 4.3 动态更新与学习辅助决策', '# 5 结论与展望']}
result = {
    'result':'PASS', 'reference_count':89, 'renumbering':moved,
    'updated_bibliographic_entries':sorted(changed), 'abstracts_and_keywords_unchanged':True,
    'per_section_reference_sets_preserved':True, 'first_use_sequential':True,
    'formulas_preserved':len(re.findall(r'\$\$(.*?)\$\$', bn,re.S)),
    'numeric_table_notes_preserved':len(re.findall(r'^注[1-4]：.*$',bn,re.M)),
    'all_table_contents_preserved_except_declared_expansion':True,
    'conclusion_conditions_preserved':True, 'reference_register_matches':True,
    'han_counts':counts, 'whole_body_han':{'old':han(bo),'new':han(bn)},
    'manuscript_lf_utf8_sha256':text_sha(new), 'human_verified':False, 'submission_ready':False,
    'scope':'Structure, preservation and recorded source mapping; not complete scientific verification.'
}
if '--json' in sys.argv:
    print(json.dumps(result,ensure_ascii=False,indent=2))
else:
    print('PASS')
    print('renumbered (old->new):', moved)
    print('reference entries with updated bibliographic notes:', sorted(changed))
    for h, count in counts.items(): print(h,count['old'],'->',count['new'])
    print('whole text Chinese characters',han(bo),'->',han(bn))
    print('Abstracts, table contents, numerical notes, source mapping and conditions: PASS')
