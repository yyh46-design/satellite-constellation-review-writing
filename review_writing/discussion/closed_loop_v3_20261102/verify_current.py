from pathlib import Path
import re,json
p=Path(__file__).resolve().parent
s=(p/'REVIEW_CN_CLOSED_LOOP_V3.1.md').read_text(encoding='utf-8')
b,r=s.split('# 参考文献\n',1)
refs=re.findall(r'^\[(\d+)\] ',r,re.M)
seen=[]
for m in re.finditer(r'\[(\d+(?:[,–]\d+)*)\]',b):
    for part in m[1].split(','):
        q=part.split('–')
        for n in (range(int(q[0]),int(q[1])+1) if len(q)==2 else [int(q[0])]):
            if n not in seen:seen.append(n)
assert refs==list(map(str,range(1,106)))
assert seen==list(range(1,106))
assert len(re.findall(r'^# [1-5] ',b,re.M))==5
assert len(re.findall(r'^\*\*表[1-6] ',b,re.M))==6
assert len(re.findall(r'\$\$.*?\$\$',b,re.S))==2
assert '2026年10月6日' in b and '超过1.1万颗' in b
assert '表4至表6' in b
assert not any(t in b for t in ['控制纠偏','轨迹重算','任务重排','构型与成员调整'])
print('PASS: 105 references in first-use order; five chapters, six tables, two equations; dated operator count and consistent category names.')

