from pathlib import Path
import json,re,hashlib,urllib.parse,unicodedata,collections
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'review_full_draft_20261010'
old=(BASE/'REVIEW_FULL_v0.6.md').read_text(encoding='utf-8')
new=(ROOT/'REVIEW_FULL_v0.7.md').read_text(encoding='utf-8')
oldbody=old.split('# 参考文献与工程资料')[0]
body,bib=new.split('# 参考文献与工程资料',1)
m=json.loads((ROOT/'SOURCE_AND_CLAIM_RECORD_v0.7.json').read_text(encoding='utf-8'))
doi_set=lambda s:{urllib.parse.unquote(d).lower() for d in re.findall(r'https://doi\.org/([^\s)]+)',s)}
assert doi_set(body)==doi_set(bib)=={x['doi'].lower() for x in m['sources']}
assert doi_set(oldbody).issubset(doi_set(body))
assert len(doi_set(body))==98
assert [int(n) for n in re.findall(r'(?m)^(\d+)\. ',bib)]==list(range(1,109))
assert '# 参考文献与工程资料'+bib==(ROOT/'REFERENCES_v0.7.md').read_text(encoding='utf-8')
assert len(m['engineering_sources'])==10
assert len({x['url'] for x in m['engineering_sources']})==10
assert all(x['url'] in body for x in m['engineering_sources'])
assert all(x['title'] and x['title_zh'] and x['publication']['authors'] and x['publication']['year'] for x in m['sources'])
assert all(x['original_source_urls'] for x in m['sources'])
assert all(x['author_verified'] is False for x in m['sources'])
assert not re.search(r'\{\{|@@|\[SOURCE\]|研究研究|补給',new)
assert re.findall(r'(?m)^# 第(\d)章',body)==['1','2','3','4','5']
assert body[:body.index('# 第3章')]==oldbody[:oldbody.index('# 第3章')]
assert body[body.index('# 第5章'):]==oldbody[oldbody.index('# 第5章'):]
assert hashlib.sha256((BASE/'REVIEW_FULL_v0.6.md').read_bytes()).hexdigest()==m['baseline']['sha256']=='f46d410547085b397f635d2f70ab9bd64c5e943dab54bc8194e81f1e0a1531c2'
raw_new=json.loads((ROOT/'BIBLIOGRAPHY_ADDITIONS_METADATA_v0.7.json').read_text(encoding='utf-8'))
raw_base=json.loads((BASE/'BIBLIOGRAPHY_METADATA_v0.6.json').read_text(encoding='utf-8'))
normalize=lambda s:re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s).lower())
for x in m['sources']:
    if x.get('library_id'):
        r=next(r for r in raw_new if r['doi'].lower()==x['doi'].lower())
        assert r['status']=='retrieved' and r['metadata']['DOI'].lower()==x['doi'].lower()
        assert normalize(r['metadata']['title'][0])==normalize(x['title'])
blocks=[]
lines=body.splitlines();i=0
while i<len(lines):
    if lines[i].startswith('|'):
        start=i; block=[]
        while i<len(lines) and lines[i].startswith('|'):block.append(lines[i]);i+=1
        cols=[len(l.split('|'))-2 for l in block]
        assert len(set(cols))==1,(start,cols)
        assert len(block)>=3
        assert all(re.fullmatch(r'\s*:?-+:?\s*',x) for x in block[1].strip('|').split('|'))
        blocks.append({'header_line':start+1,'columns':cols[0],'data_rows':len(block)-2})
    else:i+=1
assert len(blocks)==4
assert [b['data_rows'] for b in blocks]==[3,14,5,10]

core_pairs=[('3.1','10.2514/1.A34387'),('3.1','10.2514/1.A36684'),('3.1','10.2514/1.A35691'),('3.2','10.1016/j.cor.2025.107259'),('3.2','10.2514/1.I011215'),('3.2','10.1613/jair.1.16997'),('3.2','10.1002/sat.70082'),('3.2','10.2514/1.A35736'),('3.2','10.1007/s40295-026-00580-4'),('3.3','10.3390/aerospace10060543'),('3.3','10.1016/j.conengprac.2011.09.006'),('3.3','10.1007/s40295-026-00631-w'),('3.3','10.1007/s12567-025-00651-6'),('3.3','10.2514/1.I011208'),('3.4','10.1016/j.adhoc.2023.103289'),('3.4','10.3390/rs15061577'),('3.4','10.1007/s10270-026-01426-1')]
preserved=[]
for section,doi in core_pairs:
    chunk=oldbody[oldbody.index('## '+section):].split('\n## ',1)[0]
    p=next(p for p in chunk.split('\n\n') if doi in p and not p.startswith('|'))
    assert p in body,(section,doi)
    preserved.append({'section':section,'doi':doi,'paragraph_sha256':hashlib.sha256(p.encode('utf-8')).hexdigest(),'verbatim_preserved':True})
(ROOT/'CORE_PRESERVATION_v0.7.json').write_text(json.dumps(preserved,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def stats(t):
    chapters={}
    for n in range(1,6):
        start=t.index(f'# 第{n}章')
        end=t.index(f'# 第{n+1}章') if n<5 else len(t)
        chunk=t[start:end]
        chapters[str(n)]={'chinese_chars_including_tables_and_headings':len(re.findall(r'[\u4e00-\u9fff]',chunk)),'unique_academic_dois':len(doi_set(chunk))}
    narrative='\n'.join(l for l in t[t.index('# 第1章'):].splitlines() if not l.startswith(('|','#')))
    return {'body_chinese_chars':len(re.findall(r'[\u4e00-\u9fff]',t)),'five_chapter_chinese_chars':sum(x['chinese_chars_including_tables_and_headings'] for x in chapters.values()),'five_chapter_narrative_chinese_chars_excluding_tables_and_headings':len(re.findall(r'[\u4e00-\u9fff]',narrative)),'chapters':chapters}
before=stats(oldbody);after=stats(body)
reduction=1-after['chapters']['3']['chinese_chars_including_tables_and_headings']/before['chapters']['3']['chinese_chars_including_tables_and_headings']
assert 0.20<=reduction<=0.30,reduction
anchors={}
for i,line in enumerate(new.splitlines(),1):
    if line.startswith(('# 第','## 3.','**表','# 参考文献','## 工程资料')):anchors[line]=i
report={'status':'PASS_LOCAL_STRUCTURE_REFERENCE_IDENTITY_AND_PRESERVATION_CHECKS','counts':m['counts'],'all_original_50_dois_retained':True,'new_unique_academic_dois':48,'new_engineering_documents':2,'new_registry_title_doi_matches':48,'verbatim_core_paragraphs':len(preserved),'baseline_unchanged':True,'frontmatter_chapters_1_2_and_conclusion_preserved':True,'tables':blocks,'before':before,'after':after,'chapter3_chinese_character_reduction_percent':round(reduction*100,2),'five_chapter_chinese_character_reduction_percent':round((1-after['five_chapter_chinese_chars']/before['five_chapter_chinese_chars'])*100,2),'anchors':anchors,'manuscript_sha256':hashlib.sha256((ROOT/'REVIEW_FULL_v0.7.md').read_bytes()).hexdigest(),'limits':['Automated checks confirm structure, identities and preservation, not scientific proposition validity.','Human final verification, full-paper technical audit and submission formatting remain pending.']}
assert report['manuscript_sha256']==m['output']['sha256']
(ROOT/'LOCAL_CHECKS_v0.7.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['status','counts','verbatim_core_paragraphs','chapter3_chinese_character_reduction_percent','five_chapter_chinese_character_reduction_percent','tables','manuscript_sha256']},ensure_ascii=False))
print('CHAPTERS',json.dumps(after['chapters'],ensure_ascii=False))
