"""Compare REVIEW_CN_CLOSED_LOOP_V2.md with V1. Reads only; changes nothing."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
v1 = (root / 'REVIEW_CN_CLOSED_LOOP_V1.md').read_text(encoding='utf-8')
v2 = (root / 'REVIEW_CN_CLOSED_LOOP_V2.md').read_text(encoding='utf-8')
b1, r1 = v1.split('# 参考文献\n', 1)
b2, r2 = v2.split('# 参考文献\n', 1)
e1 = {int(n): e for n, e in re.findall(r'^\[(\d+)\] (.+)$', r1, re.M)}
e2 = {int(n): e for n, e in re.findall(r'^\[(\d+)\] (.+)$', r2, re.M)}
assert len(e1) == len(e2) == 93
assert sorted(e1.values()) == sorted(e2.values()), 'reference entries must be identical'
inv = {n2: next(n1 for n1, x in e1.items() if x == e) for n2, e in e2.items()}
assert list(dict.fromkeys(int(x) for x in re.findall(r'\[(\d+)\]', b2))) == list(range(1, 94))
back = lambda s: re.sub(r'\[(\d+)\]', lambda m: '[%d]' % inv[int(m.group(1))], s)
assert re.findall(r'\$\$(.*?)\$\$', b1, re.S) == re.findall(r'\$\$(.*?)\$\$', b2, re.S)
assert re.findall(r'(?m)^注\d：.*$', b1) == re.findall(r'(?m)^注\d：.*$', b2)
assert re.findall(r'(?m)^\|.*$', b1) == [back(r) for r in re.findall(r'(?m)^\|.*$', b2)]
nums = lambda s: set(re.findall(r'\d+(?:\.\d+)?', re.sub(r'\[\d+\]', '', s)))
assert not nums(b1) - nums(b2), nums(b1) - nums(b2)
for phrase in ['普遍适用的事前选择阈值', '普遍适用的事前阈值', '主要来自Rossi', '直接业务',
               '增长规律', '同条件的直接对照', '90.95%', '未形成统一可复现']:
    assert phrase in b2, phrase
assert b2.count('model predictive control') == 1
en = b2.split('## Abstract\n\n', 1)[1].split('\n\n', 1)[0]
han = lambda s: len(re.findall(r'[一-鿿]', s))
moved = {inv[n]: n for n in e2 if inv[n] != n}
print('PASS: 93 references identical, first-use order sequential, formulas, table rows and notes unchanged, no number lost')
print('renumbered (V1 -> V2):', moved)
print('English abstract words:', len(en.split()))
print('Chinese characters before references:', han(b1), '->', han(b2))
