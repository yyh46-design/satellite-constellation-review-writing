from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone
from lxml import etree as E
import csv, difflib, hashlib, html, json, re, shutil, subprocess, unicodedata, zipfile

R = Path(r'D:\SKT727\worktrees\constellation_review_cja_format_20261019')
P = Path(__file__).parent
D = R/'review_writing/manuscripts/v3.1-cn'
O = Path(r'D:\SKT727\outputs\constellation_review_v3_1_cn_20261019')
S = R/'review_writing/discussion/algorithm_refinement_v1_2_20261019'
B = R/'review_writing/manuscripts/v3.0-cn-p1'
WORD_SOURCE = Path(r'D:\SKT727\outputs\constellation_review_v3_0_p1_20261019\REVIEW_CN_v3.0-P1_第一批精修稿.docx')
WORD = D/'REVIEW_CN_v3.1.docx'
GIT = r'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w':W,'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
RX = re.compile(r'\[([0-9,，、–—\-\s]+)\]')

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
def load(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def dump(p,obj): Path(p).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def readcsv(p):
    with Path(p).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def csvwrite(p,rows):
    assert rows
    with Path(p).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def clean(s): return re.sub(r'\s*<!--.*?-->','',s).strip()
def inline(s): return re.sub(r'\*\*(.+?)\*\*',r'\1',s).replace('`','')
def expand(s):
    result=[]
    for x in re.split('[,，、]',s):
        x=x.strip();m=re.fullmatch(r'(\d+)\s*[–—\-]\s*(\d+)',x)
        result.extend(range(int(m[1]),int(m[2])+1) if m else [int(x)])
    return result
def numbers(s): return [n for m in RX.finditer(s) for n in expand(m[1])]
def compact(ns):
    ns=sorted(set(ns));out=[];i=0
    while i<len(ns):
        j=i
        while j+1<len(ns) and ns[j+1]==ns[j]+1:j+=1
        out.append(f'{ns[i]}–{ns[j]}' if j-i>=2 else ','.join(map(str,ns[i:j+1])));i=j+1
    return ','.join(out)
def normalized(s):
    return ''.join(c.lower() for c in unicodedata.normalize('NFKC',s) if c.isalnum())
def q(s):return '{'+W+'}'+s
def eltext(p):return ''.join(p.itertext()) if False else ''.join(p.xpath('.//w:t/text()',namespaces=NS))

assert not D.exists() or ((D/'WORD_OUTPUT_RECEIPT.json').is_file() and load(D/'WORD_OUTPUT_RECEIPT.json')['visual_review_done'] is False)
assert sha(WORD_SOURCE)=='309fda4917815005bac8156756e8e0ba0b19f0313b4e21ef2bfafa9d3b7d8346'
D.mkdir(parents=True,exist_ok=True);O.mkdir(parents=True,exist_ok=True);S.mkdir(parents=True,exist_ok=True)
(D/'references').mkdir(exist_ok=True);(D/'assets').mkdir(exist_ok=True);(D/'tools').mkdir(exist_ok=True)
baseline_md=(B/'REVIEW_CN_v3.0-P1.md').read_text(encoding='utf-8-sig')
source_manifest=load(R/'review_writing/manuscripts/v2.3-cn/SOURCE_MANIFEST_v2.3.json')
byid={r['evidence_id']:r for r in source_manifest['sources']}
legacy_sources=load(R/'review_writing/manuscripts/v2.0/SOURCE_MANIFEST_v2.0.json')['sources']
for source in legacy_sources:
    if source['evidence_id']=='E068' and source['evidence_id'] not in byid:
        assert source['doi']=='10.1016/j.cja.2025.103774'
        byid[source['evidence_id']]=source
index=readcsv(B/'references/REFERENCE_INDEX.csv');byold={int(r['v27']):r for r in index}
oldrefs={int(m[1]):m[2] for line in baseline_md.splitlines() if (m:=re.match(r'^(\d+)\.\s+(.+)',line))}
assert len(oldrefs)==95
preserve=[R/'review_writing/discussion/algorithm_refinement_20261019',R/'review_writing/discussion/algorithm_refinement_v1_1_20261019',B,R/'review_writing/manuscripts/v2.9-cn-figures-prose']
baseline_hashes={p.relative_to(R).as_posix():sha(p) for folder in preserve for p in folder.rglob('*') if p.is_file()}
tracked=[p for p in subprocess.check_output([GIT,'-C',str(R),'ls-tree','-rz','--name-only','HEAD']).decode().split('\0') if p]
tracked_hashes={p:sha(R/p) for p in tracked}

draft=(P/'ASSEMBLED_CONVERSATION_OLD_NUMBERS.md').read_text(encoding='utf-8')
original_draft=draft
integration=[]
draft=re.sub(r'[ \t]+(?=\[[0-9,，、–—\-\s]+\])','',draft)
integration.append({'kind':'citation_spacing_normalization','scope':'remove ordinary spaces immediately before numeric citation markers; Word uses nonbreaking citation glue'})
figures={
1:('fig1_service_framework_ai_v2.png','图1 观测与通信业务的任务及资源关系。观测以产品交付评价，通信按给定时段内的吞吐、时延和中断评价。能源、存储、计算及通信机会限制活动选择；反馈通路为关系示意，不表示所有功能已经在同一系统中完成验证。'),
2:('fig2_scale_mechanisms_ai_v2.png','图2 计算工作及相应减少机制。候选缩减[18]、局部协调[3]和计划复用[2]分别改变搜索连接、协商范围和重复求解内容。节点、连接和计划条均为机制示意，不对应实际拓扑或实验数量。'),
3:('fig3_decision_timing_ai_v2.png','图3 状态更新后的修改范围与执行时序。检查信息是否仍适用、安排是否满足约束及修改是否允许后，可以保留有效计划、局部修复或扩大重规划范围。局部路径修复以[14]为例。下部是有期限请求的时序示意，阶段可能重叠，时间长度不表示实测数据；持续通信另按服务时段评价。'),
4:('fig4_conditional_comparisons_ai_v2.png','图4 不同研究中的条件性比较。（a）[17]在固定实例中比较观测与传输的联合、分开安排；（b）[14]比较通信机会可靠性变化后的请求失败率，MSR优先采用指定路径并允许局部回退，CGR依据后续机会局部选路；（c）[15]在所报1 ms建链条件下，ILPR、ALPR的平均时延略高于即时最短路ILSR，ISASR仍较低。三项研究的模型和指标不同，图中排序不构成统一排名或通用阈值。')}
insertions=[('### 2.2 ',1,'图1概括观测、处理、传输与共享资源之间的关系。'),('### 4.2 ',2,'图2归纳不同计算工作及其减少机制。'),('**表6 ',3,'图3示意状态更新后选择修改范围及交付执行的过程。'),('### 4.4 ',4,'图4并列展示不同研究中的条件性比较。')]
for anchor,n,intro in insertions:
    pos=draft.index(anchor);fn,cap=figures[n]
    block=intro+'\n\n![图'+str(n)+'](assets/'+fn+')\n\n'+cap+'\n\n'
    draft=draft[:pos]+block+draft[pos:]
    integration.append({'kind':'retain_figure_and_add_callout','figure':n,'before':anchor,'caption_old_numbers':cap,'image_sha256':sha(B/'assets'/fn)})
    shutil.copyfile(B/'assets'/fn,D/'assets'/fn)

seen=[]
for n in numbers(draft):
    if n not in seen:seen.append(n)
assert len(seen)==64
renumber={old:i+1 for i,old in enumerate(seen)}
draft=RX.sub(lambda m:'['+compact(renumber[n] for n in expand(m[1]))+']',draft)
title=draft.splitlines()[0][2:]
english_title='Task and Resource Scheduling in Large Satellite Constellations: A Review of Solution Methods, Multi-Satellite Coordination, and Dynamic Plan Updates'
english_abstract=('Scheduling in large satellite constellations determines which satellites perform tasks, when activities occur, and how energy, storage, computation, and communication resources are allocated. Growth in satellite and request numbers, competition for shared resources, and changing operational states connect solution quality, computational cost, and plan updates. Focusing on Earth observation and communications, this review examines optimization, heuristic search, and learning methods, together with multi-satellite coordination, dynamic replanning, and validation conditions. Candidate reduction, local coordination, plan reuse, and precomputation reduce different workloads; their benefits must be assessed alongside changes in feasible choices and preparation and coordination costs. The value of joint task and resource decisions depends on service objectives, revisable variables, and available computation time. Learning supports demand prediction, search-operator selection, or action generation, while constraint handling and cross-satellite conflict resolution require explicit mechanisms. Evaluation should track when updated plans take effect and distinguish observation-product delivery from communication-service outcomes. Further research should compare decision combinations under limited computational budgets, permissible changes with delayed information, and the effects of satellite and resource recovery on service losses under common conditions.')
assert 150<=len(english_abstract.split())<=200,len(english_abstract.split())
draft=draft.replace('# '+title+'\n','# '+title+'\n\n'+english_title+'\n\n**v3.1-CN · 2026-10-19 · 本轮会话精修整合审阅稿**\n',1)
pos=draft.index('## 1 ')
draft=draft[:pos]+'## Abstract\n\n'+english_abstract+'\n\n**Keywords:** large satellite constellations; task allocation; resource allocation; multi-satellite coordination; dynamic replanning; learning-assisted scheduling\n\n'+draft[pos:]

meta=load(P/'CROSSREF_AUTHOR_METADATA_LOCAL.json');bymeta={r['old_number']:r for r in meta}
author_audit=[];bibliography={}
for old in seen:
    original=oldrefs[old];item=byid[byold[old]['stable_id']];m=bymeta.get(old,{})
    new=original;status='original_institutional_entry_retained';authors=[]
    if old in [40,51,87]:
        status={40:'original_author_names_retained_registry_family_contains_full_name',51:'original_author_names_retained_registry_name_order_ambiguous',87:'original_author_names_retained_registry_merges_multiple_authors'}[old]
    elif m.get('status')=='metadata_only' and m.get('authors'):
        nt=normalized(item['title']);mapped=[];chars=[]
        for i,c in enumerate(original):
            for x in unicodedata.normalize('NFKC',c):
                if x.isalnum():chars.append(x.lower());mapped.append(i)
        ix=''.join(chars).find(nt)
        if ix>=0 and difflib.SequenceMatcher(None,nt,normalized(' '.join(m.get('title',[])))).ratio()>.85:
            for a in m['authors']:
                family=a.get('family') or a.get('literal') or a.get('name')
                if not family:break
                given=a.get('given','');initials=''.join(part[0] for part in re.findall(r'[^\W\d_]+',given,flags=re.UNICODE))
                authors.append(family+(' '+initials if initials else ''))
            if len(authors)==len(m['authors']):
                display=authors if len(authors)<=6 else authors[:6]+['et al.']
                new=', '.join(display).rstrip('.')+'. '+original[mapped[ix]:]
                status='structured_doi_metadata_author_format_only'
            else:status='original_entry_retained_incomplete_structured_author_metadata'
        else:status='original_entry_retained_title_match_needs_review'
    elif old in bymeta:status='original_entry_retained_registry_access_unavailable'
    bibliography[old]=new
    author_audit.append({'v31_number':renumber[old],'previous_v30_number':old,'stable_id':byold[old]['stable_id'],'identity':byold[old]['doi_or_official_url'],'author_format_status':status,'metadata_access_status':m.get('status','not_applicable'),'structured_author_count':len(authors),'human_verified':False})
draft=draft.rstrip()+'\n\n## 参考文献\n\n'+'\n\n'.join(f'{renumber[n]}. {bibliography[n]}' for n in seen)+'\n'

def parse(md):
    lines=md.splitlines();out=[];i=0;inrefs=False
    while i<len(lines):
        s=clean(lines[i]);i+=1
        if not s:continue
        if s.startswith('|'):
            rows=[[v.strip() for v in s.strip('|').split('|')]]
            while i<len(lines) and lines[i].strip().startswith('|'):
                x=clean(lines[i]);i+=1
                if not re.match(r'^\|\s*[-:]+',x):rows.append([v.strip() for v in x.strip('|').split('|')])
            out.append({'kind':'table','rows':rows});continue
        m=re.match(r'^(#{1,4})\s+(.+)',s)
        if m:
            out.append({'kind':'heading','level':len(m[1]),'text':m[2]});inrefs=inrefs or m[2]=='参考文献';continue
        m=re.match(r'^!\[图(\d+)\]\(([^)]+)\)',s)
        if m:out.append({'kind':'image','number':int(m[1]),'path':m[2]});continue
        if inrefs:
            m=re.match(r'^(\d+)\.\s+(.+)',s);assert m,s
            out.append({'kind':'reference','number':int(m[1]),'text':m[2]});continue
        out.append({'kind':'paragraph','text':s})
    return out

blocks=parse(draft)
first=[]
for x in blocks:
    if x['kind']=='reference':break
    t=' '.join(' '.join(row) for row in x['rows']) if x['kind']=='table' else x.get('text','')
    for n in numbers(t):
        if n not in first:first.append(n)
assert first==list(range(1,65)),first
assert len([x for x in blocks if x['kind']=='table'])==7
assert len([x for x in blocks if x['kind']=='image'])==4
(D/'REVIEW_CN_v3.1.md').write_text(draft,encoding='utf-8')
dump(D/'MANUSCRIPT_BLOCKS.json',blocks)
dump(D/'CONVERSATION_INTEGRATION_LOG.json',{'conversation_chapter_body_sha256':digest(original_draft),'integration_edits':integration,'english_abstract_added_and_synchronized':True,'english_abstract_words':len(english_abstract.split()),'english_fulltext_created':False,'citation_numbers_regenerated':True,'scientific_results_added':False,'new_fulltext_readings':0,'formal_version_pairs_closed':0,'human_verified':False})

# Rebuild only the authorized body slots of the retained CJA manuscript package.
with zipfile.ZipFile(WORD_SOURCE) as z:infos=z.infolist();parts={n:z.read(n) for n in z.namelist()}
source_parts=dict(parts);doc=E.fromstring(parts['word/document.xml']);body=doc.find(q('body'))
source_body=deepcopy(body);ps=source_body.findall(q('p'))
def findp(prefix):return next(p for p in ps if eltext(p).startswith(prefix))
templates={'title':deepcopy(ps[0]),'en_title':deepcopy(ps[1]),'banner':deepcopy(ps[2]),'body':deepcopy(findp('大型星座需要同时')),'caption':deepcopy(findp('图1 ')),'ref':deepcopy(findp('[1] ')),'h2':deepcopy(findp('1 引言')),'h3':deepcopy(findp('1.1 ')),'h4':deepcopy(findp('4.5.1 '))}
table_templates={len(t.findall(q('tblGrid')+'/'+q('gridCol'))):deepcopy(t) for t in source_body.findall(q('tbl'))}
image_templates={int(p.xpath('.//wp:docPr/@id',namespaces=NS)[0]):deepcopy(p) for p in ps if p.xpath('.//wp:docPr/@id',namespaces=NS)}
sect=deepcopy(source_body.find(q('sectPr')))
for child in list(body):body.remove(child)

def set_text(p,value,refs=True):
    base=None
    for r in p.findall(q('r')):
        pr=r.find(q('rPr'))
        if pr is None or pr.find(q('vertAlign')) is None:base=deepcopy(pr) if pr is not None else E.Element(q('rPr'));break
    if base is None:base=E.Element(q('rPr'))
    for n in ['vertAlign','color','b','bCs']:
        for x in base.findall(q(n)):base.remove(x)
    E.SubElement(base,q('color')).set(q('val'),'000000')
    for child in list(p):
        if child.tag!=q('pPr'):p.remove(child)
    def add(t,cite=False,bold=False):
        if not t:return
        r=E.SubElement(p,q('r'));pr=deepcopy(base);r.append(pr)
        if cite:
            E.SubElement(pr,q('vertAlign')).set(q('val'),'superscript')
            t=t[1:-1].replace('–','\u2011');t='\u00a0'+'\u2060'.join(t)
        if bold:E.SubElement(pr,q('b'))
        x=E.SubElement(r,q('t'));x.set('{http://www.w3.org/XML/1998/namespace}space','preserve');x.text=t
    tokens=re.compile(r'\*\*(.+?)\*\*|\[([0-9,，、–—\-\s]+)\]')
    last=0
    for m in tokens.finditer(value):
        add(value[last:m.start()])
        if m[1] is not None:add(m[1],bold=True)
        elif refs:add(m[0],cite=True)
        else:add(m[0])
        last=m.end()
    add(value[last:])
    return p

widths={1:[1700,1000,3000,3597],2:[1700,3500,4097],3:[1950,2850,2000,2497],4:[1700,2500,2300,2797],5:[2000,2300,2500,2497],6:[1900,2300,2000,3097],7:[1800,2500,2200,2797]}
def make_table(rows,n):
    cols=len(rows[0]);assert all(len(r)==cols for r in rows)
    t=deepcopy(table_templates[cols]);trs=t.findall(q('tr'));head=deepcopy(trs[0]);row_template=deepcopy(trs[1])
    for tr in trs:t.remove(tr)
    grid=t.find(q('tblGrid'))
    for child in list(grid):grid.remove(child)
    for width in widths[n]:E.SubElement(grid,q('gridCol')).set(q('w'),str(width))
    props=t.find(q('tblPr'));tw=props.find(q('tblW'))
    if tw is None:tw=E.SubElement(props,q('tblW'))
    tw.set(q('type'),'dxa');tw.set(q('w'),str(sum(widths[n])))
    for i,row in enumerate(rows):
        tr=deepcopy(head if i==0 else row_template);trpr=tr.find(q('trPr'))
        if trpr is None:trpr=E.Element(q('trPr'));tr.insert(0,trpr)
        for x in trpr.findall(q('trHeight')):trpr.remove(x)
        if trpr.find(q('cantSplit')) is None:E.SubElement(trpr,q('cantSplit'))
        for j,(cell,value) in enumerate(zip(tr.findall(q('tc')),row)):
            cp=cell.find(q('tcPr'));cw=cp.find(q('tcW'))
            if cw is None:cw=E.SubElement(cp,q('tcW'))
            cw.set(q('type'),'dxa');cw.set(q('w'),str(widths[n][j]))
            va=cp.find(q('vAlign'))
            if va is None:va=E.SubElement(cp,q('vAlign'))
            va.set(q('val'),'center')
            # CJA reference-derived three-line table, with expandable rows.
            for cb in cp.findall(q('tcBorders')):cp.remove(cb)
            if i in [0,len(rows)-1]:
                cb=E.SubElement(cp,q('tcBorders'));edge=E.SubElement(cb,q('bottom'));edge.set(q('val'),'single');edge.set(q('sz'),'4' if i==0 else '6');edge.set(q('color'),'000000')
            pp=cell.findall(q('p'));p=pp[0]
            for extra in pp[1:]:cell.remove(extra)
            set_text(p,value)
            pr=p.find(q('pPr'))
            for x in pr.findall(q('keepNext')):pr.remove(x)
            if i==0:
                E.SubElement(pr,q('keepNext')).set(q('val'),'1')
                for run in p.findall(q('r')):
                    rp=run.find(q('rPr'))
                    if rp.find(q('b')) is None:E.SubElement(rp,q('b'))
        t.append(tr)
    return t

table_number=0;expected=[]
for x in blocks:
    k=x['kind']
    if k=='heading':
        template=templates['title'] if x['level']==1 else templates['h'+str(x['level'])]
        p=set_text(deepcopy(template),x['text'])
        if x['level']==1 and '：' in x['text']:
            run=p.find(q('r'));t=run.find(q('t'));prefix,suffix=t.text.split('：',1);t.text=prefix+'：';E.SubElement(run,q('br'));E.SubElement(run,q('t')).text=suffix
        body.append(p);expected.append(['p',x['text']])
    elif k=='image':body.append(deepcopy(image_templates[x['number']]))
    elif k=='table':table_number+=1;body.append(make_table(x['rows'],table_number));expected.append(['table',[[inline(v) for v in row] for row in x['rows']]])
    elif k=='reference':
        value=f'[{x["number"]}] '+x['text'];p=set_text(deepcopy(templates['ref']),value,False)
        mark=E.Element(q('bookmarkStart'));mark.set(q('id'),str(1000+x['number']));mark.set(q('name'),'ref_v31_'+str(x['number']));p.insert(1,mark)
        end=E.SubElement(p,q('bookmarkEnd'));end.set(q('id'),str(1000+x['number']))
        body.append(p);expected.append(['p',value])
    else:
        value=x['text'];plain=inline(value)
        template=templates['en_title'] if value==english_title else templates['banner'] if value.startswith('**v3.1-CN') else templates['caption'] if re.match(r'^(?:\*\*)?[图表]\d',value) else templates['body']
        p=set_text(deepcopy(template),value)
        if re.match(r'^\*\*表\d',value):
            pr=p.find(q('pPr'));kn=pr.find(q('keepNext'))
            if kn is None:kn=E.SubElement(pr,q('keepNext'))
            kn.set(q('val'),'1')
        body.append(p);expected.append(['p',plain])
body.append(sect)
parts['word/document.xml']=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
core=E.fromstring(parts['docProps/core.xml']);dc='http://purl.org/dc/elements/1.1/'
ct=core.find('{'+dc+'}title')
if ct is None:ct=E.SubElement(core,'{'+dc+'}title')
ct.text=title
parts['docProps/core.xml']=E.tostring(core,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(WORD,'w',zipfile.ZIP_DEFLATED) as z:
    for info in infos:z.writestr(info,parts[info.filename])

def normalized_p(p):
    result=[]
    for child in p:
        if child.tag==q('r'):
            t=eltext(child).replace('\u2060','').replace('\u2011','–')
            va=child.find(q('rPr')+'/'+q('vertAlign'))
            if va is not None and va.get(q('val'))=='superscript':t=t.removeprefix('\u00a0')
            result.append('['+t+']' if va is not None and va.get(q('val'))=='superscript' else t)
        elif child.tag!=q('pPr'):result.append(eltext(child))
    return ''.join(result)
actual=[]
for x in body:
    if x.tag==q('p'):
        t=normalized_p(x)
        if t:actual.append(['p',t])
    elif x.tag==q('tbl'):actual.append(['table',[[normalized_p(c.find(q('p'))) for c in row.findall(q('tc'))] for row in x.findall(q('tr'))]])
assert actual==expected,next(((i,a,e) for i,(a,e) in enumerate(zip(actual,expected)) if a!=e),('length',len(actual),len(expected)))
changed=[n for n in source_parts if parts[n]!=source_parts[n]]
assert set(changed)=={'word/document.xml','docProps/core.xml'},changed
def signature(node):
    return (node.tag,tuple(sorted(node.attrib.items())),(node.text or '').strip(),tuple(signature(c) for c in node))
assert signature(sect)==signature(source_body.find(q('sectPr')))
assert len(doc.findall('.//'+q('bookmarkStart')))==64
assert sha(WORD_SOURCE)=='309fda4917815005bac8156756e8e0ba0b19f0313b4e21ef2bfafa9d3b7d8346'

# Source identity, citation numbering, and evidence scope remain separate records.
reference_rows=[];disposition=[]
for old in range(1,96):
    row=byold[old];sid=row['stable_id'];src=byid[sid]
    record={'previous_v30_number':old,'v31_number':renumber.get(old,''),'stable_id':sid,'title':src['title'],'identity':row['doi_or_official_url'],'kind':src.get('kind','academic'),'status':'cited_in_v31' if old in renumber else 'retained_in_library_not_cited_in_v31','reason':'本轮会话正文保留' if old in renumber else '会话重组后未直接引用；原来源与阅读记录保留','historical_version':row['historical_version'],'historical_route':row['historical_fulltext_or_official_route'],'history_record_code':row['history_record_code'],'human_verified':False}
    disposition.append(record)
    if old in renumber:reference_rows.append(record)
reference_rows.sort(key=lambda x:x['v31_number'])
csvwrite(D/'references/REFERENCE_INDEX_v3.1.csv',reference_rows)
csvwrite(D/'references/SOURCE_LIBRARY_95_DISPOSITION.csv',disposition)
csvwrite(D/'references/AUTHOR_FORMAT_AUDIT.csv',author_audit)
dump(D/'references/AUTHOR_METADATA_AUDIT.json',meta)
shutil.copyfile(B/'references/REFERENCE_INDEX.csv',D/'references/REFERENCE_INDEX_v3.0_95.csv')

defaults={'1.1':['E001','E034','E035','E125','E002'],'1.2':['E003','E004','E005','E006','E007','E008','E009'],'2.1':['E030','E034','E042','E044','E122'],'2.2':['E030','E037','E042','E065','E122','E123'],'2.3':['E042','E044','E074','E076','E106'],'3.1':['E030','E122','E042','E053','E061','E074'],'3.2':['E030','E044','E042','E125'],'3.3':['E073','E123','E065','E066','E128'],'3.4':['E037','E036','E035','E081','E076','E039','E041'],'3.5':['E127','E034','E061','E062','E106','E121'],'4.1':['E044','E035','E034','E125','E072','E065'],'4.2':['E042','E106','E044','E053','E074'],'4.3':['E065','E037','E052','E106','E081','E121'],'4.4':['E016','E017','E018','E019','E023','E091','E092','E093','E095','E097','E102','E108','E119','E109','E111','E114','E115'],'5':['E034','E035','E042','E044','E053','E065','E106','E121','E123']}
new_to_old={v:k for k,v in renumber.items()};claims=[];section='';counter=0
for x in blocks:
    if x['kind']=='heading':section=x['text'];continue
    if x['kind'] in ['reference','image']:continue
    texts=[' | '.join(row) for row in x['rows']] if x['kind']=='table' else [x['text']]
    for text in texts:
        counter+=1;direct=numbers(text);key=(re.match(r'(\d+(?:\.\d+)?)',section) or ['',''])[1]
        ids=sorted({byold[new_to_old[n]]['stable_id'] for n in direct})
        if not ids:ids=defaults.get(key,[])
        kind='source_based_statement_or_synthesis' if direct else 'explanatory_synthesis_with_section_context' if ids else 'author_scope_definition_or_transition'
        if section.startswith('4.5'):kind='proposed_research_question_not_experiment_result'
        claims.append({'claim_id':f'CN31C{counter:03}','section':section,'text_sha256':digest(inline(text)),'reference_numbers':';'.join(map(str,sorted(set(direct)))),'evidence_ids':';'.join(ids),'interpretation':kind,'support_basis':'existing_targeted_reading_records; no new fulltext verification','human_verified':False})
csvwrite(D/'CLAIM_EVIDENCE_MAP.csv',claims)
dump(D/'BASELINE_PROVENANCE.json',{'source_word':str(WORD_SOURCE),'source_word_sha256':sha(WORD_SOURCE),'source_md_sha256':digest(baseline_md),'source_conversation_body_sha256':digest(original_draft),'tracked_baseline_sha256':tracked_hashes,'preserved_local_baseline_sha256':baseline_hashes,'modified_docx_parts':changed,'styles_and_section_preserved':True,'source_figure_bytes_preserved':True})

# Carry the latest terminology rules forward and add the agreed citation-writing rules.
previous=R/'review_writing/discussion/algorithm_refinement_v1_1_20261019'
standard=(previous/'REFINEMENT_STANDARD_CN_v1.1.md').read_text(encoding='utf-8')
standard=standard.replace('版本：v1.1。更新日期：2026-10-19，Asia/Shanghai。基于v1.0增加决策表述与术语界定要求。','版本：v1.2。更新日期：2026-10-19，Asia/Shanghai。沿用v1.1的对象、条件与决定要求，补充本轮确认的引用叙述方式。',1)
addition='''### 7.1 文献提及方式与引用位置

采用数字顺序编码引用。作者名加编号、内容陈述后标编号、方法名加编号和“文献加编号”可以配合使用，分别服务于不同叙述目的。

- 一般归纳以共同问题、方法或认识作主语，并在对应内容后标注来源。
- 代表论文的机制说明可以作者名或方法名引导，明确谁提出了什么、该方法怎样工作。
- 对照具体论文的模型、假设或实验时，可以使用“文献[编号]”；避免每段机械重复这一开头。
- 多项来源合并引用时，共同表述须由各项来源实际支持。不同分句依据不同来源时，编号分别紧跟相应分句。
- 连续介绍同一研究时，在指代清楚的条件下使用“该方法”“该模型”，不必每句重复作者姓名；来源变化或具体结果须清楚归属。
- 本文的定义、分类、综合和建议与原论文事实分开；综合判断仍应能回指其依据。
- 不规定各类句式的机械比例。减少逐篇罗列，以共同问题和实质差异组织段落。
- 中文审阅Markdown保留方括号便于追踪，CJA Word导出使用数字上标。文末按全文首次引用顺序编号，引用合并、范围及稳定E编号同步核对。

'''
standard=standard.replace('## 8 摘要、引言与语言',addition+'## 8 摘要、引言与语言',1)
standard=standard.replace('[方法说明卡模板](METHOD_CARD_TEMPLATE_CN.md)','[方法说明卡模板](METHOD_CARD_TEMPLATE_CN.md)')
standard=standard.replace('[v1.0执行计划](../algorithm_refinement_20261019/EXECUTION_PLAN_CN.md)','[v1.0执行计划](../algorithm_refinement_20261019/EXECUTION_PLAN_CN.md)')
standard=standard.replace('v1.1新增要求应用于后续各批及回查','v1.1及v1.2要求应用于后续各批及回查')
standard=standard.replace('本规范针对 v2.9 中文稿“运行过程交代较多，调度问题与算法关系呈现不足”的问题，指导下一轮内容精修。','本规范起于v2.9中文稿中调度问题与算法关系呈现不足的问题，本轮结合v3.1整合稿更新，继续指导后续内容精修。')
standard=standard.replace('题名中的“智能管理”采用优化、规则、协调与学习共同参与决策的含义。增加学习算法名称不能代替说明其实际作用。当前题名先作为工作题名，待正文范围稳定后再核对其覆盖承诺。','当前工作题名为“大型卫星星座任务与资源调度综述：求解方法、多星协调与动态更新”。优化、规则、协调与学习按它们参与决策的具体作用展开；增加学习算法名称不能代替机制说明。后续调整题名时，仍需核对其与正文范围的一致性。')
standard=standard.replace('现有第3.1节的能力形成内容主要移入第2章条件说明，代表性优化方法按作用移入第3章；第3.2和3.3节按问题与方法重新归组；第3.4节的安全、故障内容进入条件变化与运行比较；第3.5节的执行衔接主要支撑第4章。迁移保留来源、模型条件和版本身份，避免复制后重复论证。','从v2.9重组时采用以下迁移原则：能力形成内容压缩为条件说明，代表性求解方法按作用进入第3章；安全、故障和执行衔接进入第4章的条件变化与运行验证。v3.1已据此整合。后续迁移仍保留来源、模型条件和版本身份，避免复制后重复论证。')
standard=standard.replace('会话中的第二章试修尚未据此回写完整稿或Word。','本轮会话中的五章试修已整合为v3.1-CN，并按既定CJA中文工作稿样式生成Word；页面检查状态以本轮交付记录为准。')
standard=standard.replace('`BASELINE_AND_DELIVERY.json`','`BASELINE_AND_DELIVERY.json`')
(S/'REFINEMENT_STANDARD_CN_v1.2.md').write_text(standard,encoding='utf-8')
for name in ['METHOD_CARD_TEMPLATE_CN.md','DECISION_CLARITY_CHECKLIST_CN.md']:shutil.copyfile(previous/name,S/name)
(S/'CITATION_WRITING_CHECKLIST_CN.md').write_text('# 引用叙述检查表\n\n- 段落是否先明确共同问题。\n- 代表论文是否解释实际机制，而非只列作者和算法名称。\n- 内容、作者、方法和文献引导是否各有明确用途。\n- 编号是否紧跟它实际支持的内容。\n- 分组引用是否由每项来源支持共同表述。\n- 本文综合与原论文结果是否分开。\n- 全文首次引用顺序与稳定E编号映射是否一致。\n- Word是否统一数字上标，书目是否覆盖全部实际引文。\n',encoding='utf-8')
(S/'README_CN.md').write_text('# 精修规范v1.2\n\n后续采用[完整精修规范v1.2](REFINEMENT_STANDARD_CN_v1.2.md)。第8.1节保留具体对象、已知条件和待决定内容的要求，第7.1节新增本轮确认的引用叙述规则。\n\n配套文件包括[方法卡](METHOD_CARD_TEMPLATE_CN.md)、[决策表述检查表](DECISION_CLARITY_CHECKLIST_CN.md)与[引用检查表](CITATION_WRITING_CHECKLIST_CN.md)。v1.0和v1.1均保留原状。\n',encoding='utf-8')
dump(S/'BASELINE_AND_DELIVERY.json',{'version':'v1.2','date':'2026-10-19','based_on':'v1.1','original_v1_1_standard_sha256':sha(previous/'REFINEMENT_STANDARD_CN_v1.1.md'),'changed_sections':['7.1 citation narrative rules','12 current manuscript status'],'current_manuscript':'../../manuscripts/v3.1-cn/REVIEW_CN_v3.1.md','scope':'carry forward accepted clarity requirements and record citation-writing rules confirmed in the conversation','scientific_verification_unchanged':True,'submission_ready':False})

def markup(s):
    s=html.escape(s);s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    return RX.sub(lambda m:'<sup>'+m[1]+'</sup>',s)
web=['<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>星座任务与资源调度综述 v3.1</title><style>body{max-width:980px;margin:36px auto;padding:0 22px;font:17px/1.8 SimSun,serif;color:#111}h1,h2,h3,h4{color:#000;line-height:1.5}img{width:100%;max-width:900px}table{border-collapse:collapse;width:100%;font-size:14px;margin:14px 0}th,td{padding:9px;text-align:left;vertical-align:top}thead{border-top:2px solid #000;border-bottom:1px solid #000}tbody{border-bottom:2px solid #000}.reference{font:14px/1.6 "Times New Roman",serif;padding-left:32px;text-indent:-32px}sup{font-size:.72em}</style><body>']
for x in blocks:
    k=x['kind']
    if k=='heading':web.append(f'<h{x["level"]}>'+markup(x['text'])+f'</h{x["level"]}>')
    elif k=='image':web.append('<p><img src="'+x['path']+'" alt="图'+str(x['number'])+'"></p>')
    elif k=='table':web.append('<table><thead><tr>'+''.join('<th>'+markup(v)+'</th>' for v in x['rows'][0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+markup(v)+'</td>' for v in row)+'</tr>' for row in x['rows'][1:])+'</tbody></table>')
    elif k=='reference':web.append('<p class="reference">['+str(x['number'])+'] '+html.escape(x['text'])+'</p>')
    else:web.append('<p>'+markup(x['text'])+'</p>')
web.append('</body></html>');(D/'REVIEW_CN_v3.1.html').write_text(''.join(web),encoding='utf-8')
oldclean=re.sub(r'\s*<!--.*?-->','',baseline_md)
comparison=difflib.HtmlDiff(wrapcolumn=55).make_file(oldclean.splitlines(),draft.splitlines(),'v3.0-CN-P1','v3.1-CN',context=True,numlines=2)
(D/'REVISION_COMPARISON_CN.html').write_text(comparison,encoding='utf-8')

counts={'academic':sum(byid[r['stable_id']].get('kind')=='academic' for r in reference_rows),'engineering':sum(byid[r['stable_id']].get('kind')!='academic' for r in reference_rows)}
fallback=[r['v31_number'] for r in author_audit if r['author_format_status'].startswith('original_entry_retained_registry')]
summary={'version':'v3.1-CN','date':'2026-10-19','chapter_count':5,'table_count':7,'figure_count':4,'reference_count':64,'source_library_count':95,'sources_not_cited_but_retained':31,'source_counts':counts,'claim_records':len(claims),'word_markdown_blocks':len(actual),'english_abstract_words':len(english_abstract.split()),'english_fulltext_complete':False,'metadata_only_doi_responses':sum(r['status']=='metadata_only' for r in meta),'metadata_access_exceptions':fallback,'new_fulltext_readings':0,'formal_version_pairs_closed':0,'human_verified':False,'submission_ready':False,'page_count':None,'visual_review_done':False}
dump(D/'REVISION_SUMMARY.json',summary)
dump(D/'WORD_OUTPUT_RECEIPT.json',{'path':'REVIEW_CN_v3.1.docx','sha256':sha(WORD),'bytes':WORD.stat().st_size,'page_count':None,'visual_review_done':False,'actual_visual_review_pages':[],'human_verified':False,'submission_ready':False})
(D/'README_CN.md').write_text(f'''# v3.1中文精修整合稿

本版将本轮会话确定的题名、摘要、五章正文与七张表整合为一份完整审阅稿，并沿用四幅英文草图。Word采用已核验的CJA中文工作稿样式，尚不是英文正式投稿稿。

- [完整Markdown正文](REVIEW_CN_v3.1.md)
- [可编辑Word](REVIEW_CN_v3.1.docx)
- [阅读HTML](REVIEW_CN_v3.1.html)
- [与v3.0-P1的修改对照](REVISION_COMPARISON_CN.html)
- [本轮精修规范v1.2](../../discussion/algorithm_refinement_v1_2_20261019/REFINEMENT_STANDARD_CN_v1.2.md)
- [参考文献与稳定编号](references/REFERENCE_INDEX_v3.1.csv)
- [95项来源的保留和引用状态](references/SOURCE_LIBRARY_95_DISPOSITION.csv)
- [未关闭项](OPEN_ITEMS_CN.md)

本版实际引用64项来源，其中学术来源{counts['academic']}项、工程资料{counts['engineering']}项。原95项来源中的其余31项仍保留在来源库和历史稿中，本轮没有为保持数量而加入无直接用途的引文。新编号按正文和图表的首次出现顺序生成，稳定E编号保留。

结构主线为具体调度问题、求解与协调方法、运行条件下的方法比较。正文区分已知条件与待作出的决定；一般归纳以问题和方法作主语，代表研究保留必要机制说明。图注增加必要条件说明，图像本身沿用原稿并保留AI辅助制作的来源记录。

本轮没有新增全文精读或关闭正式版本差异。英文题名、摘要和关键词已同步，完整英文稿、作者科学终核和投稿终核仍待完成。页面与内容检查结果见本轮交付记录。
''',encoding='utf-8')
(D/'OPEN_ITEMS_CN.md').write_text('''# 未关闭项

- 六组正式版本差异E042、E044、E053、E074、E076、E121继续保留，按实际取得的作者稿、接受稿或预印本解释相关结果。
- E035仅保留既有高层机制；确切本地版本恢复和详细分解步骤仍待核，不据本轮重组增加已读范围。
- E127按既有完整HTML中的定性流程使用；缺少公式和图页的实际页面核验。
- E068的身份取自既有v2.0来源记录与当前95项索引；本版只保留鲁棒安排的方向性提及，不将索引中的正式全文入口视为本轮实际核读证明，原文与历史核读记录衔接仍待复核。
- 52项DOI元数据响应仅用于作者字段排版；元数据不验证正文内容或版本一致性。两项中文DOI的Crossref请求返回404，一项返回429；这些结果不证明DOI无效。相关条目沿用已有书目与来源身份，其中中文来源的完整作者名单及CJA作者格式仍待终核。
- 原编号51的滚动时域论文存在登记姓名顺序歧义，本版保留原来源中的完整作者姓名，不据登记字段机械生成可能颠倒姓与名的缩写；最终姓名格式待作者终核。
- 当前编号29的首位作者被登记为完整姓名而没有独立的名字段，当前编号51的登记记录把两名作者合并进同一个字段。这两项均沿用原书目作者记录，不据该响应删减作者；完整作者名单和最终缩写格式待核。
- 本轮来源库95项，正文引用64项；其余31项是否在后续科学修订中重新纳入，应取决于具体论证需要。
- 四图为沿用的AI辅助PNG草图；正文与图注关系已检查，正式矢量重绘、图内术语进一步精简和投稿图件终核尚未完成。
- 作者、单位、基金、贡献、利益冲突、数据与工具披露等声明需要作者据实填写，本轮未生成这些信息。
- 中文页数不代表英文满足篇幅要求。完整英文稿及其分页、期刊当期指南和投稿系统项目仍需终核。
- 自动一致性与AI页面检查不代替作者科学确认；human_verified=false，submission_ready=false。
''',encoding='utf-8')
(D/'GPT_REVIEW_BRIEF_CN.md').write_text('''# 本轮审阅说明

请结合完整正文和精修规范v1.2，评价这篇问题导向叙述性综述的科学内容与可读性。

1. 第2章能否说清具体卫星、请求和资源对象，以及已知条件和待决定内容。
2. 第3章是否解释代表方法如何得到安排，是否存在算法、组织和更新维度混淆或逐篇罗列。
3. 第4章的条件性判断是否有足够来源支持，是否混用了跨研究结构比较与同研究性能对照。
4. 题名、摘要、引言与结论是否与第2—4章一致，是否仍过度偏向通信。
5. 实际引用64项、来源库保留95项的当前组合，是否留下具体重要论证缺口；请指出缺口，不仅建议凑数量。

本轮没有新增全文精读，正式版本差异、作者科学确认、完整英文和最终图件仍未关闭。请区分正文中可依据已有证据修改的问题与需要新增原文核验的问题。
''',encoding='utf-8')
(D/'.gitattributes').write_text('*.docx binary\n*.png binary\n',encoding='utf-8')
for p,h in baseline_hashes.items():assert sha(R/p)==h,p
for p,h in tracked_hashes.items():assert sha(R/p)==h,p
shutil.copyfile(Path(__file__),D/'tools/build_v31.py')
shutil.copyfile(WORD,O/'REVIEW_CN_v3.1_CJA中文精修整合稿.docx')
print(json.dumps(summary,ensure_ascii=False,indent=2))
