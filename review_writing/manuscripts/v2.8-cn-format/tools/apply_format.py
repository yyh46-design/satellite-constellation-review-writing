"""Patch a copy of the v2.7 Word package. Never rewrite scientific prose or source files."""
from pathlib import Path
from copy import deepcopy
import argparse,csv,hashlib,json,re,shutil,zipfile
from lxml import etree as E

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--repo',type=Path,default=Path(r'D:\SKT727\worktrees\constellation_review_cja_format_20261019'))
ap.add_argument('--source',type=Path,default=Path(r'D:\SKT727\outputs\constellation_review_v2_7_20261018\REVIEW_CN_v2.7_中文精修稿.docx'))
ap.add_argument('--output-dir',type=Path,default=Path(r'D:\SKT727\outputs\constellation_review_v2_8_format_20261019'))
ap.add_argument('--records-dir',type=Path,default=Path(r'D:\SKT727\materials\constellation_review_v2_8_format_20261019'))
a=ap.parse_args();R=a.repo;P=a.records_dir;O=a.output_dir
B=R/'review_writing/manuscripts/v2.7-cn';D=R/'review_writing/manuscripts/v2.8-cn-format'
D.mkdir(parents=True,exist_ok=True);P.mkdir(parents=True,exist_ok=True);O.mkdir(parents=True,exist_ok=True)
BASE='5a832d8f9af4065f5038ef301c724b28be8b4978'
EXPECTED='481d928036496b3da1c2171ce2e1f73848bdbd207f01cdb59265e7bff43168a5'
def sha(b):return hashlib.sha256(b).hexdigest()
def put(n,x):
 p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(x if isinstance(x,str) else json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
assert sha(a.source.read_bytes())==EXPECTED,'The retained v2.7 Word is not the verified source.'
with zipfile.ZipFile(a.source) as z:parts={n:z.read(n) for n in z.namelist()};infos=z.infolist()
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
def q(n):return '{'+NS['w']+'}'+n
def node(parent,name):
 el=parent.find(q(name))
 if el is None:el=E.SubElement(parent,q(name))
 return el
def attr(parent,name,**values):
 el=node(parent,name)
 for k,v in values.items():el.set(q(k),str(v))
 return el
def font(rpr,halfpt=None,east='宋体'):
 f=attr(rpr,'rFonts',ascii='Times New Roman',hAnsi='Times New Roman',cs='Times New Roman',eastAsia=east)
 for key in list(f.attrib):
  if key.endswith('Theme'):del f.attrib[key]
 attr(rpr,'color',val='000000')
 if halfpt is not None:attr(rpr,'sz',val=halfpt);attr(rpr,'szCs',val=halfpt)
def text(p):return ''.join(p.itertext()) if False else ''.join(p.xpath('.//w:t/text()',namespaces=NS))
doc=E.fromstring(parts['word/document.xml']);styles=E.fromstring(parts['word/styles.xml']);before=deepcopy(doc)
changes=[]
def log(n,bef,aft):changes.append({'item':n,'before':bef,'after':aft})
byid={s.get(q('styleId')):s for s in styles.findall(q('style'))}
for styleid,size,bold in [('Normal',22,False),('Title',32,True),('Subtitle',22,False),('Heading1',24,True),('Heading2',23,True),('Heading3',22,True),('Caption',20,False)]:
 s=byid[styleid];rp=node(s,'rPr');font(rp,size,'黑体' if styleid in ['Title','Heading1','Heading2','Heading3'] else '宋体');attr(rp,'b',val='1' if bold else '0');attr(rp,'i',val='0')
 pp=node(s,'pPr');attr(pp,'spacing',line='276',lineRule='auto',after='80' if styleid=='Normal' else '100',before='160' if styleid.startswith('Heading') else '0')
 attr(pp,'ind',firstLine='440' if styleid=='Normal' else '0')
 for el in list(pp.findall(q('pBdr'))):pp.remove(el)
 if styleid.startswith('Heading') or styleid in ['Title','Subtitle']:attr(pp,'keepNext',val='1')
 if styleid=='Caption':attr(pp,'keepLines',val='1')
for sid,size,bold in [('CJARef',19,False),('CJATableText',19,False),('CJATableHeader',19,True),('CJARevision',18,False)]:
 s=E.SubElement(styles,q('style'));s.set(q('type'),'paragraph');s.set(q('customStyle'),'1');s.set(q('styleId'),sid)
 attr(s,'name',val=sid);attr(s,'basedOn',val='Normal');pp=node(s,'pPr');attr(pp,'ind',firstLine='0');attr(pp,'spacing',line='276',lineRule='auto',after='0');font(node(s,'rPr'),size);attr(node(s,'rPr'),'b',val='1' if bold else '0')
 if sid=='CJARef':attr(pp,'spacing',line='264',lineRule='auto',after='80');attr(pp,'ind',left='360',hanging='360');attr(pp,'keepLines',val='1')
 if sid=='CJARevision':attr(pp,'spacing',line='240',lineRule='auto',after='100')
log('页面与正文','A4单栏；中文正文11 pt、1.35倍行距','A4及页边距保持；中文11 pt、1.15倍行距；西文Times New Roman')
log('标题层级','题名17 pt；一级14 pt；二级12 pt；三级11.5 pt','题名16 pt；一级12 pt；二级11.5 pt；三级11 pt；黑色一致')

body=doc.find(q('body'));inrefs=False;refnums=[];caption_styles=[]
oldversion='v2.7-CN · 2026-10-18 · 正文证据比较精修稿；作者审阅版'
newversion='v2.8-CN · 2026-10-19 · CJA格式整理；中文作者审阅版'
for i,p in enumerate(body.findall(q('p'))):
 t=text(p);pp=node(p,'pPr');sid=pp.find(q('pStyle'));role=sid.get(q('val')) if sid is not None else 'Normal'
 if t==oldversion:
  ts=p.findall('.//'+q('t'));assert len(ts)==1;ts[0].text=newversion;attr(pp,'pStyle',val='CJARevision');attr(pp,'ind',firstLine='0');attr(pp,'spacing',line='240',lineRule='auto',before='0',after='100')
  for r in p.findall(q('r')):font(node(r,'rPr'),18);attr(node(r,'rPr'),'b',val='0')
 elif t.startswith('Intelligent Management and Scheduling of Large Satellite Constellations'):
  attr(pp,'pStyle',val='Subtitle');attr(pp,'jc',val='center');attr(pp,'ind',firstLine='0');attr(pp,'spacing',line='276',lineRule='auto',after='120')
 elif t=='参考文献':inrefs=True
 elif inrefs and re.match(r'^\d+\. ',t):
  n=int(re.match(r'^(\d+)\.',t)[1]);refnums.append(n);first=p.find('.//'+q('t'));assert first is not None and re.match(r'^\d+\. ',first.text or '')
  first.text=re.sub(r'^\d+\. ',f'[{n}] ',first.text,count=1);attr(pp,'pStyle',val='CJARef');attr(pp,'ind',left='360',hanging='360',firstLine='0');attr(pp,'spacing',line='264',lineRule='auto',after='80')
  for r in p.findall(q('r')):font(node(r,'rPr'),19)
 elif role=='Caption':
  attr(pp,'spacing',line='276',lineRule='auto',before='100',after='80');attr(pp,'keepLines',val='1');attr(pp,'ind',firstLine='0');caption_styles.append(t[:16])
  for r in p.findall(q('r')):font(node(r,'rPr'),20)
 elif role=='Normal' and t and not p.findall('.//'+q('drawing')):
  # Ordinary prose inherits the revised Normal spacing. Keep intentional abstract and keyword overrides.
  attr(pp,'spacing',line='276',lineRule='auto',after='80')
assert refnums==list(range(1,96))
log('文末参考文献显示','1. 至95.；多条作者/题名仍为历史核验文字','[1]至[95]；悬挂缩进、Times New Roman9.5 pt；条目文字不补名、不重排')

table_receipts=[]
for no,tbl in enumerate(body.findall(q('tbl')),1):
 pr=node(tbl,'tblPr');bd=node(pr,'tblBorders')
 for el in list(bd):bd.remove(el)
 for side in ['left','right','insideH','insideV']:attr(bd,side,val='nil')
 attr(bd,'top',val='single',sz='8',color='000000');attr(bd,'bottom',val='single',sz='8',color='000000')
 mar=node(pr,'tblCellMar')
 for side,w in [('top',70),('bottom',70),('left',85),('right',85)]:attr(mar,side,w=w,type='dxa')
 rows=tbl.findall(q('tr'))
 for ri,row in enumerate(rows):
  trp=node(row,'trPr');attr(trp,'cantSplit',val='1')
  if ri==0:attr(trp,'tblHeader',val='1')
  for cell in row.findall(q('tc')):
   tcpr=node(cell,'tcPr')
   for sh in list(tcpr.findall(q('shd'))):tcpr.remove(sh)
   cb=node(tcpr,'tcBorders')
   for e in list(cb):cb.remove(e)
   for side in ['left','right','top','bottom']:attr(cb,side,val='nil')
   if ri==0:
    attr(cb,'top',val='single',sz='8',color='000000')
    attr(cb,'bottom',val='single',sz='4',color='000000')
   if ri==len(rows)-1:attr(cb,'bottom',val='single',sz='8',color='000000')
   for p in cell.findall(q('p')):
    pp=node(p,'pPr');attr(pp,'pStyle',val='CJATableHeader' if ri==0 else 'CJATableText');attr(pp,'ind',firstLine='0');attr(pp,'spacing',line='276',lineRule='auto',after='0')
    for r in p.findall(q('r')):font(node(r,'rPr'),19);attr(node(r,'rPr'),'b',val='1' if ri==0 else '0')
 table_receipts.append({'number':no,'rows':len(rows),'columns':len(rows[0].findall(q('tc'))),'header_repeats':True,'no_vertical_lines':True,'no_shading':True,'editable':True})
log('七张表格','浅色整格边框、灰蓝表头底纹','黑色横线表式，无竖线及底纹，表头下横线，跨页表头重复；单行不拆分')

# Preserve all text while splitting only numeric citation runs outside the bibliography.
supcount=0;inrefs=False
for parent in body:
 if parent.tag==q('p') and text(parent)=='参考文献':inrefs=True
 if inrefs:continue
 for p in ([parent] if parent.tag==q('p') else parent.findall('.//'+q('p'))):
  for run in list(p.findall(q('r'))):
   ts=run.findall(q('t'))
   if not ts:continue
   rt=''.join(t.text or '' for t in ts);matches=list(re.finditer(r'\[(\d{1,3})\]',rt))
   if not matches:continue
   assert all(1<=int(m[1])<=95 for m in matches)
   assert all(c.tag in [q('t'),q('rPr')] for c in run),'Mixed drawing/field run cannot be safely split.'
   oldpr=run.find(q('rPr'));frags=[];pos=0
   for m in matches:
    if m.start()>pos:frags.append((rt[pos:m.start()],False))
    frags.append((m[0],True));pos=m.end()
   if pos<len(rt):frags.append((rt[pos:],False))
   idx=list(p).index(run);p.remove(run)
   for offset,(s,issup) in enumerate(frags):
    r=E.Element(q('r'))
    if oldpr is not None:r.append(deepcopy(oldpr))
    if issup:
     rp=node(r,'rPr');oldsz=rp.find(q('sz'));citation_size=int(oldsz.get(q('val'))) if oldsz is not None else 22
     attr(rp,'vertAlign',val='superscript');font(rp,citation_size);supcount+=1
    tt=E.SubElement(r,q('t'));tt.text=s
    if s.startswith(' ') or s.endswith(' '):tt.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    p.insert(idx+offset,r)
log('文内引文','正文、表格及图注中的普通基线[n]','数字引用改为上标，引用文字、位置和编号保持原样；图中文字留待英文重画')

figs=[]
for n,inline in enumerate(doc.findall('.//wp:inline',NS),1):
 ext=inline.find('wp:extent',NS);oldcx=int(ext.get('cx'));oldcy=int(ext.get('cy'));newcx=5400000;newcy=round(oldcy*newcx/oldcx)
 ext.set('cx',str(newcx));ext.set('cy',str(newcy))
 for xe in inline.findall('.//a:xfrm/a:ext',NS):xe.set('cx',str(newcx));xe.set('cy',str(newcy))
 figs.append({'number':n,'old_width_cm':oldcx/360000,'new_width_cm':15.0,'image_bytes_changed':False,'image_text_language':'Chinese inherited placeholder','next_revision_language':'English'})
log('两图的版面尺寸','12.3 cm与14 cm','均以15 cm通栏宽显示；图片像素与SVG源内容原样保留，英文精修安排在下一阶段')

# Place the large second illustration after the paragraph that introduces it in 4.2.
# This avoids a large gap before a full figure/caption block without rewriting prose.
figure_paras=[p for p in body.findall(q('p')) if p.findall('.//'+q('drawing'))]
assert len(figure_paras)==2
fig2p=figure_paras[1];fig2cap=fig2p.getnext();assert text(fig2cap).startswith('图2 ')
heading43=next(p for p in body.findall(q('p')) if text(p).startswith('4.3 反馈更新'))
body.remove(fig2p);body.remove(fig2cap);slot=list(body).index(heading43);body.insert(slot,fig2p);body.insert(slot+1,fig2cap)
log('图2分页位置','4.3末尾，导致前页较大空白','移到4.2结尾、4.3之前，紧接引用图2的分析；图内内容及图注文字不变')

def serialize(root):return E.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
parts['word/document.xml']=serialize(doc);parts['word/styles.xml']=serialize(styles)
core=E.fromstring(parts['docProps/core.xml']);core_ns={'dc':'http://purl.org/dc/elements/1.1/','cp':'http://schemas.openxmlformats.org/package/2006/metadata/core-properties'}
for tag,value in [('{'+core_ns['dc']+'}subject','大型卫星星座综述 v2.8-CN CJA格式整理'),('{'+core_ns['dc']+'}description','Chinese author-review text retained. CJA-aligned format pass. English figure refinement is the next phase.')]:
 e=core.find(tag)
 if e is None:e=E.SubElement(core,tag)
 e.text=value
parts['docProps/core.xml']=serialize(core)
output=O/'REVIEW_CN_v2.8_CJA格式中文稿.docx'
with zipfile.ZipFile(output,'w') as z:
 for info in infos:z.writestr(info,parts[info.filename])
assert sha(a.source.read_bytes())==EXPECTED
raw=(B/'REVIEW_CN_v2.7.md').read_text(encoding='utf-8');oldmdversion='**'+oldversion+'**';assert oldmdversion in raw
newmd=raw.replace(oldmdversion,'**'+newversion+'**',1)
fig2block=re.search(r'!\[图2[^\n]+\n\n图2[^\n]+\n\n',newmd)[0]
newmd=newmd.replace(fig2block,'');anchor='### 4.3 反馈更新的信息、权限与生效条件';assert anchor in newmd
newmd=newmd.replace(anchor,fig2block+anchor,1)
put('REVIEW_CN_v2.8.md',newmd)
for p in (B/'assets').iterdir():
 if p.is_file():(D/'assets').mkdir(exist_ok=True);shutil.copyfile(p,D/'assets'/p.name)
for name in ['CLAIM_EVIDENCE_MAP.csv','references/REFERENCE_INDEX.csv','references/REFERENCE_NUMBER_MAP.csv']:
 (D/name).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(B/name,D/name)
with (B/'CLAIM_EVIDENCE_MAP.csv').open(encoding='utf-8-sig',newline='') as f:claims=list(csv.DictReader(f))
for claim in claims:claim['line']=next(i for i,s in enumerate(newmd.splitlines(),1) if '[claim:'+claim['claim_id']+']' in s)
with (D/'CLAIM_EVIDENCE_MAP.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(claims[0]),lineterminator='\n');w.writeheader();w.writerows(claims)
put('FORMAT_CHANGE_REGISTER.json',{'baseline_commit':BASE,'baseline_word_sha256':EXPECTED,'source_version':'v2.7-CN','output_version':'v2.8-CN-format','changes':changes,'scientific_paragraphs_rewritten':0,'reference_set_or_numbers_changed':False,'bibliographic_identity_text_changed':False,'reference_label_punctuation_only':True,'claim_ids_preserved':'CN27 IDs retained; no science rewrite','new_whole_paper_readings':0,'formal_version_pairs_closed':0,'human_verified':False,'submission_ready':False})
receipt={'source':str(a.source),'source_sha256':EXPECTED,'source_markdown':str(B/'REVIEW_CN_v2.7.md'),'source_markdown_sha256':sha((B/'REVIEW_CN_v2.7.md').read_bytes()),'formatted_markdown_sha256':sha((D/'REVIEW_CN_v2.8.md').read_bytes()),'file':{'path':str(output),'bytes':output.stat().st_size,'sha256':sha(output.read_bytes())},'patched_package_parts':['word/document.xml','word/styles.xml','docProps/core.xml'],'numeric_citations_superscripted':supcount,'tables':table_receipts,'figures':figs,'references':95,'page_count':None,'visual_review_done':False,'human_verified':False,'English_full_body_synchronized':False,'submission_ready':False}
(P/'WORD_BUILD_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'file':receipt['file'],'superscript_citations':supcount,'tables':len(table_receipts),'figures':len(figs)},ensure_ascii=False,indent=2))
