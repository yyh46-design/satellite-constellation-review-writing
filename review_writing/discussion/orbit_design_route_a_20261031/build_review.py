"""Assemble the numbered discussion manuscript from the five editable sections.

Uses only Python's standard library. Does not access the network or alter source
evidence. Reference identity and versions are stored in REFERENCE_REGISTER.json.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PARTS=['ABSTRACT_REFRAMED_CN.md','CHAPTER_1_REFRAMED_CN.md',
       'CHAPTERS_2_3_REFINED_CN.md','CHAPTER_4_DISCUSSION_CN.md',
       'CHAPTER_5_REFRAMED_CN.md']
LINK=re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
register=json.loads((ROOT/'REFERENCE_REGISTER.json').read_text(encoding='utf-8'))
refs={r['url']:r for r in register['references']}
used=set()
chapter_sets={str(i):set() for i in range(1,6)}
occurrences=[]
texts=[]
for fn in PARTS:
    text=(ROOT/fn).read_text(encoding='utf-8-sig').strip()
    chapter=None
    for line_num,line in enumerate(text.splitlines(),1):
        head=re.match(r'# ([1-5]) ',line)
        if head:chapter=head[1]
        for label,url in LINK.findall(line):
            r=refs[url];used.add(r['number'])
            if chapter:chapter_sets[chapter].add(r['number'])
            occurrences.append({'file':fn,'line':line_num,'chapter':chapter,'number':r['number'],'url':url})
    def replace(m):
        label,url=m.groups();n=refs[url]['number']
        # Author names are useful in table source cells, but unnecessary in
        # sentence-ending citation groups. Both use the same numeric identity.
        return f'[{n}]'
    text=LINK.sub(replace,text)
    texts.append(text)
assert used==set(range(1,len(refs)+1)),(used,len(refs))
body='\n\n'.join(texts)+'\n'
assert not any(s in body for s in ['所读','所阅读','\\(','\\['])
references='\n\n'.join(f"[{r['number']}] {r['reference']} {r.get('version_citation','')} [来源](<{r['url']}>)".replace('  ',' ') for r in register['references'])
title='# 面向任务需求的大型卫星星座轨道设计与运行决策综述\n\n'
english=(ROOT/'ABSTRACT_EN.md').read_text(encoding='utf-8').strip()
full=title+texts[0]+'\n\n'+english+'\n\n'+'\n\n'.join(texts[1:])+'\n\n# 参考文献\n\n'+references+'\n'
target=ROOT/'REVIEW_ROUTE_A_CN.md'
target.write_text(full,encoding='utf-8')
(ROOT/'REFERENCES_CN.md').write_text('# 参考文献\n\n'+references+'\n',encoding='utf-8')
tables=re.findall(r'^\*\*表(\d+) ',body,re.M)
assert tables==['1','2','3','4','5'],tables
numbers={int(n) for n in re.findall(r'\[(\d+)\]',body)}
assert numbers==used
index={'unique_references':len(used),'citation_occurrences':len(occurrences),
       'per_chapter_unique':{k:len(v) for k,v in chapter_sets.items()},
       'chapters_2_to_4_unique':len(set.union(*(chapter_sets[k] for k in ['2','3','4']))),
       'occurrences':occurrences}
(ROOT/'CITATION_INDEX.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
checks={'date':'2026-10-31','scope':'assembly, numeric citation identity, five tables, selected source-bound facts; not scientific certification',
        'references':len(used),'tables':tables,'dangling_numbered_citations':[],
        'uncited_references':[],'process_language_in_body':False,
        'body_cjk_characters':len(re.findall(r'[\u4e00-\u9fff]',body)),
        'manuscript_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
        'human_verified':False,'submission_ready':False}
(ROOT/'CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in index.items() if k!='occurrences'},ensure_ascii=False))
print(json.dumps(checks,ensure_ascii=False))
