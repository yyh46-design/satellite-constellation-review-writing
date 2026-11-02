"""Compare REVIEW_CN_CLOSED_LOOP_V3.1.md with the author's V3. Reads only; changes nothing."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
v3 = (root / 'REVIEW_CN_CLOSED_LOOP_V3.md').read_text(encoding='utf-8')
v31 = (root / 'REVIEW_CN_CLOSED_LOOP_V3.1.md').read_text(encoding='utf-8')
b0, r0 = v3.split('# 参考文献\n', 1)
b1, r1 = v31.split('# 参考文献\n', 1)
e0 = {int(n): e for n, e in re.findall(r'^\[(\d+)\] (.+)$', r0, re.M)}
e1 = {int(n): e for n, e in re.findall(r'^\[(\d+)\] (.+)$', r1, re.M)}
assert len(e0) == len(e1) == 104 and e0 == e1, 'reference list must be identical'
assert list(dict.fromkeys(int(x) for x in re.findall(r'\[(\d+)\]', b1))) == list(range(1, 105))
assert re.findall(r'\$\$(.*?)\$\$', b0, re.S) == re.findall(r'\$\$(.*?)\$\$', b1, re.S)
assert re.findall(r'(?m)^注\d：.*$', b0) == re.findall(r'(?m)^注\d：.*$', b1)

def tables(s):
    out, cur = [], None
    for line in s.split('\n'):
        m = re.match(r'^\*\*表(\d)', line)
        if m:
            cur = m.group(1); continue
        if line.startswith('|') and cur:
            out.append((cur, line))
    return out
assert [r for k, r in tables(b0) if k in '1234'] == [r for k, r in tables(b1) if k in '1234'], 'tables 1-4'
old5 = b0[b0.index('**表5 验证规模'):b0.index('注1：Jia')]
new6 = b1[b1.index('**表6 验证规模'):b1.index('注1：Jia')]
cites = lambda s: set(re.findall(r'\[(\d+)\]', s))
assert cites(old5) == cites(new6), 'old Table 5 citations must all appear in new Table 6'
nums = lambda s: set(re.findall(r'\d+(?:[.,]\d+)?', re.sub(r'\[\d+\]', '', s)))
assert not nums(b0) - nums(b1), nums(b0) - nums(b1)
for phrase in ['普遍适用的事前选择阈值', '普遍适用的事前阈值', '主要来自Rossi', '直接业务',
               '增长规律', '90.95%', '未形成统一可复现', '可以迁移的是更新对象']:
    assert phrase in b1, phrase
for phrase in ['轨迹重优化', '任务重规划']:
    assert phrase not in b1, phrase
assert b1.count('model predictive control') == 1 and b1.index('model predictive control') < b1.index('MPC')
en = b1.split('## Abstract\n\n', 1)[1].split('\n\n', 1)[0]
han = lambda s: len(re.findall(r'[一-鿿]', s))
print('PASS: 104 references identical and in first-use order; formulas, tables 1-4 and all table notes unchanged;')
print('      old Table 5 citations all kept in Table 6; no number lost; restored scope statements present')
print('English abstract words:', len(en.split()))
print('Table 6 rows:', len([1 for k, r in tables(b1) if k == '6']) - 2, '(old Table 5:', len([1 for k, r in tables(b0) if k == '5']) - 2, ')')
print('Chinese characters before references:', han(b0), '->', han(b1))
