"""Compare this refinement with the previous saved package. Reads only; changes nothing."""
from pathlib import Path
import re

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
for phrase in ['普遍适用的事前阈值', '主要来自Rossi', '本文的综合判断', '直接业务结果',
               '增长规律', '同条件的直接对照', '90.95%', '未形成统一可复现']:
    assert phrase in bn, phrase
for n in ['19.73', '2304', '6173', '2.75', '90.95', '2000组']:   # numbers removed from Ch.5 stay in Ch.2-4
    assert n in bn.split('# 5 结论与展望')[0], n

han = lambda s: len(re.findall(r'[一-鿿]', s))
print('PASS')
print('renumbered (old->new):', moved)
print('reference entries with updated bibliographic notes:', sorted(changed))
for h in ['## 1.2 相关研究与本文定位', '## 4.3 动态更新与学习辅助决策', '# 5 结论与展望']:
    print(h, han(so[h]), '->', han(sn[h]))
print('whole text Chinese characters', han(bo), '->', han(bn))
