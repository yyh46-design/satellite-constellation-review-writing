"""Compare the author's chapter 4 with the revised version.

Per section: cited reference set, numbers (citations removed), inline formulas.
Whole chapter: headings, Table 4 and Table 6 rows (must be identical),
Table 5 row labels and citations (columns were redesigned on purpose),
citation first-appearance order, word frequencies.
Usage: python3 -I verify_ch4.py ch4_author.md CH4_REVISED.md
"""
import re
import sys

A = open(sys.argv[1], encoding='utf-8').read()
B = open(sys.argv[2], encoding='utf-8').read()

HEAD = re.compile(r'(?m)^(4(?:\.\d)? .*)$')
CITE = re.compile(r'\[([\d,–\-]+)\]')
han = lambda s: len(re.findall(r'[一-鿿]', s))


def sections(t):
    parts = HEAD.split(t)
    out = {}
    for i in range(1, len(parts), 2):
        out[parts[i].split()[0]] = parts[i + 1]
    return out


def cites(s, ordered=False):
    seq = []
    for g in CITE.findall(s):
        for p in g.split(','):
            if re.search('[–-]', p):
                x, y = re.split('[–-]', p)
                seq += list(range(int(x), int(y) + 1))
            else:
                seq.append(int(p))
    return list(dict.fromkeys(seq)) if ordered else set(seq)


def nums(s):
    s = CITE.sub('', s)
    s = re.sub(r'\$[^$]*\$', '', s)
    return set(re.findall(r'\d+(?:[.,]\d+)?', s))


def table(t, title):
    i = t.index(title)
    rows = []
    for line in t[i:].split('\n')[1:]:
        if line.count('\t') >= 3:
            rows.append(line)
        elif rows:
            break
    return rows


ok = True
sa, sb = sections(A), sections(B)
assert list(sa) == list(sb)
print(f"{'节':<6}{'原稿':>6}{'修订':>6}  引用  数值")
for k in sa:
    ca, cb = cites(sa[k]), cites(sb[k])
    lost, new = nums(sa[k]) - nums(sb[k]), nums(sb[k]) - nums(sa[k])
    c_ok = ca == cb
    ok &= c_ok
    print(f"{k:<6}{han(sa[k]):>6}{han(sb[k]):>6}  {'同' if c_ok else '变'}  "
          f"{'丢失' + str(sorted(lost)) if lost else '无丢失'}"
          f"{'  新增' + str(sorted(new)) if new else ''}")
    if not c_ok:
        print('   only author', sorted(ca - cb), 'only revised', sorted(cb - ca))
    fa, fb = re.findall(r'\$[^$]*\$', sa[k]), re.findall(r'\$[^$]*\$', sb[k])
    if fa != fb:
        ok = False
        print('   formulas differ', fa, fb)

heads_ok = HEAD.findall(A) == HEAD.findall(B)
ok &= heads_ok
print('标题一致:', heads_ok)
for title in ['表4 ', '表5 ', '表6 ']:
    ra, rb = table(A, title), table(B, title)
    same_text = ra == rb
    same_cites = cites('\n'.join(ra)) == cites('\n'.join(rb))
    same_nums = nums('\n'.join(ra)) <= nums('\n'.join(rb))
    ok &= same_cites and same_nums
    print(f"{title}逐字一致: {same_text} | 引用集合一致: {same_cites} | 数值无丢失: {same_nums} | 行数 {len(ra)}->{len(rb)}")
print('总汉字:', han(A), '->', han(B))
oa, ob = cites(A, True), cites(B, True)
print('首次出现顺序一致:', oa == ob)
if oa != ob:
    print('   author ', oa)
    print('   revised', ob)
words = ['联系', '共同', '分别', '说明', '由此', '体现', '表明', '评价', '收益',
         '生效时间', '承诺', '任务归属', '不表示']
print('高频词（原稿→修订）:', '；'.join(f'{w} {A.count(w)}→{B.count(w)}' for w in words))
print('PASS' if ok else 'FAIL')
