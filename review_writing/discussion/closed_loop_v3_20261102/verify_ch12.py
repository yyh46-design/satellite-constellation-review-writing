from pathlib import Path
import re

p=Path(__file__).resolve().parent
old=(p/'REVIEW_CN_CLOSED_LOOP_V3.1.md').read_text(encoding='utf-8')
new=(p/'REVIEW_CN_CLOSED_LOOP_V3.2.md').read_text(encoding='utf-8')
assert old.split('# 1 引言')[0]==new.split('# 1 引言')[0]
assert old.split('# 3 ',1)[1]==new.split('# 3 ',1)[1]
assert re.findall(r'\$\$.*?\$\$',old,re.S)==re.findall(r'\$\$.*?\$\$',new,re.S)
b,r=new.split('# 参考文献\n',1)
assert re.findall(r'^\[(\d+)\] ',r,re.M)==list(map(str,range(1,106)))
def cites(s):
    out=[]
    for m in re.finditer(r'\[(\d+(?:[,–]\d+)*)\]',s):
        for v in m[1].split(','):
            z=v.split('–')
            out.extend(range(int(z[0]),int(z[1])+1) if len(z)==2 else [int(z[0])])
    return out
assert list(dict.fromkeys(cites(b)))==list(range(1,106))
for n in [1,2]:
    a=old.split(f'# {n} ',1)[1].split(f'# {n+1} ',1)[0]
    c=new.split(f'# {n} ',1)[1].split(f'# {n+1} ',1)[0]
    assert set(cites(a))==set(cites(c))
assert len(re.findall(r'^# [1-5] ',b,re.M))==5
assert len(re.findall(r'^\*\*表[1-6] ',b,re.M))==6
c2=new.split('# 2 ',1)[1].split('# 3 ',1)[0]
assert all(x in c2 for x in ['80.86%','78.07%','80.02%','52/18.26','22/14.95','44/12.43'])
assert '法向修正引起的沿轨变化又可能需要后续的面内调整' in c2
c3=new.split('# 3 ',1)[1].split('# 4 ',1)[0]
assert '约1年' in c3 and '2.75年' in c3
assert any('650—850 km' in line for line in new.splitlines() if line.startswith('| 千星级构型几何'))
print('PASS: scope, citation identity/order, 105 references, 5 chapters, 6 tables, unchanged equations, quantitative comparisons and retained numerical contexts.')
