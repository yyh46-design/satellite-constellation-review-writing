"""Read-only format and preservation checks. Not a scientific or submission acceptance test."""
from pathlib import Path
from collections import Counter
import argparse,csv,hashlib,json,re,subprocess,zipfile
import xml.etree.ElementTree as E

BASE='5a832d8f9af4065f5038ef301c724b28be8b4978'
PREFIX='review_writing/manuscripts/v2.8-cn-format/'
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[4]);p.add_argument('--git',default='git')
p.add_argument('--word',type=Path,required=True);p.add_argument('--source-word',type=Path,required=True);p.add_argument('--manifest-check',action='store_true');p.add_argument('--require-visual',action='store_true');p.add_argument('--output',type=Path)
a=p.parse_args();R=a.repo;D=R/PREFIX;B=R/'review_writing/manuscripts/v2.7-cn';checks=[]
W={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
def q(n):return '{'+W['w']+'}'+n
def sha(b):return hashlib.sha256(b).hexdigest()
def txt(el):return ''.join(t.text or '' for t in el.iter(q('t')))
def ck(n,t,detail=None):
 assert t,f'{n}: {detail}'
 checks.append({'check':n,'pass':True,**({'detail':detail} if detail is not None else {})})
def get(n):return json.loads((D/n).read_text(encoding='utf-8'))
def git(*args,input=None):return subprocess.run([a.git,'-C',str(R),*args],input=input,capture_output=True,check=True).stdout
def norm(s):return re.sub(r'\s+',' ',s.replace('\u2060','').replace('\u00a0',' ')).strip()
def clean(s):return re.sub(r'\s*<!--.*?-->','',s).strip()
def inline(s):return norm(re.sub(r'\[([^\]]+)\]\((https?://[^\s]+)\)',lambda m:m[1],s).replace('**',''))

md=(D/'REVIEW_CN_v2.8.md').read_text(encoding='utf-8');oldmd=(B/'REVIEW_CN_v2.7.md').read_text(encoding='utf-8')
expectedmd=oldmd.replace('**v2.7-CN · 2026-10-18 · 正文证据比较精修稿；作者审阅版**','**v2.8-CN · 2026-10-19 · CJA格式整理；中文作者审阅版**',1)
block=re.search(r'!\[图2[^\n]+\n\n图2[^\n]+\n\n',expectedmd)[0];expectedmd=expectedmd.replace(block,'');expectedmd=expectedmd.replace('### 4.3 反馈更新的信息、权限与生效条件',block+'### 4.3 反馈更新的信息、权限与生效条件',1)
ck('only_descriptor_and_figure2_relocation_in_markdown',md==expectedmd)
ck('five_chapters_seven_tables_two_figures',len(re.findall(r'^## [1-5] ',md,re.M))==5 and len(re.findall(r'^\*\*表\d',md,re.M))==7 and len(re.findall(r'^!\[',md,re.M))==2)
ck('95_reference_entries_unchanged',md.split('## 参考文献\n',1)[1]==oldmd.split('## 参考文献\n',1)[1] and len(re.findall(r'^\d+\. ',md.split('## 参考文献\n',1)[1],re.M))==95)
for name in ['fig1_cn.svg','fig2_cn.svg']:ck('svg_bytes_'+name,(D/'assets'/name).read_bytes()==(B/'assets'/name).read_bytes())
for name in ['REFERENCE_INDEX.csv','REFERENCE_NUMBER_MAP.csv']:ck('source_index_'+name,(D/'references'/name).read_bytes()==(B/'references'/name).read_bytes())
with (D/'CLAIM_EVIDENCE_MAP.csv').open(encoding='utf-8-sig',newline='') as f:claims=list(csv.DictReader(f))
with (B/'CLAIM_EVIDENCE_MAP.csv').open(encoding='utf-8-sig',newline='') as f:oldclaims=list(csv.DictReader(f))
ck('152_claims_same_identity_and_hash',len(claims)==152 and [{k:v for k,v in x.items() if k!='line'} for x in claims]==[{k:v for k,v in x.items() if k!='line'} for x in oldclaims])
for c in claims:ck('claim_line_'+c['claim_id'],'[claim:'+c['claim_id']+']' in md.splitlines()[int(c['line'])-1] and sha(clean(md.splitlines()[int(c['line'])-1]).encode())==c['text_sha256'])
ck('retained_word_source_hash',sha(a.source_word.read_bytes())=='481d928036496b3da1c2171ce2e1f73848bdbd207f01cdb59265e7bff43168a5')
with zipfile.ZipFile(a.source_word) as z:before={n:z.read(n) for n in z.namelist()}
with zipfile.ZipFile(a.word) as z:after={n:z.read(n) for n in z.namelist()}
ck('package_part_set_preserved',set(before)==set(after))
changed=[n for n in before if before[n]!=after[n]]
ck('only_three_intended_package_parts_changed',set(changed)=={'word/document.xml','word/styles.xml','docProps/core.xml'},changed)
ck('all_media_relationships_fields_and_other_parts_preserved',all(after[n]==before[n] for n in before if n not in changed))
root=E.fromstring(after['word/document.xml']);oldroot=E.fromstring(before['word/document.xml']);body=root.find(q('body'))
ck('section_geometry_identical',E.tostring(root.find('.//'+q('sectPr')))==E.tostring(oldroot.find('.//'+q('sectPr'))))
ck('reference_bookmarks_retained',[(x.get(q('id')),x.get(q('name'))) for x in root.findall('.//'+q('bookmarkStart'))]==[(x.get(q('id')),x.get(q('name'))) for x in oldroot.findall('.//'+q('bookmarkStart'))] and len(root.findall('.//'+q('bookmarkStart')))==95)
expected=[];ls=[clean(x) for x in md.splitlines()];i=0
while i<len(ls):
 s=ls[i];i+=1
 if not s or s.startswith('!['):continue
 if s.startswith('|'):
  rows=[];i-=1
  while i<len(ls) and ls[i].startswith('|'):
   line=ls[i];i+=1
   if re.match(r'^\|\s*-',line):continue
   rows.append([inline(x.strip()) for x in line.strip('|').split('|')])
  expected.append(['table',rows]);continue
 expected.append(['p',inline(re.sub(r'^#{1,4} ','',s))])
actual=[];bib=False;actualrefs=[]
for el in body:
 if el.tag==q('p'):
  t=norm(txt(el))
  if t=='参考文献':bib=True
  elif bib and re.match(r'^\[\d+\] ',t):
   n=int(re.match(r'^\[(\d+)\]',t)[1]);actualrefs.append(n);t=re.sub(r'^\[\d+\] ',f'{n}. ',t,count=1)
  if t:actual.append(['p',t])
 elif el.tag==q('tbl'):actual.append(['table',[[norm(txt(c)) for c in row.findall(q('tc'))] for row in el.findall(q('tr'))]])
ck('complete_ordered_word_text_and_tables_equal_markdown',actual==expected,{'expected':len(expected),'actual':len(actual)})
ck('reference_labels_1_to_95',actualrefs==list(range(1,96)))
refs=[];bib=False
for el in body:
 if el.tag==q('p') and txt(el)=='参考文献':bib=True
 if bib:continue
 for run in el.iter(q('r')):
  found=re.findall(r'\[(\d{1,3})\]',txt(run))
  if found:
   va=run.find('w:rPr/w:vertAlign',W);ck('superscript_run_'+str(len(refs)),va is not None and va.get(q('val'))=='superscript');refs.extend(map(int,found))
oldbody=oldmd.split('## 参考文献\n',1)[0];oldrefnums=list(map(int,re.findall(r'\[(\d+)\]',re.sub(r'<!--.*?-->','',oldbody))))
newbody=md.split('## 参考文献\n',1)[0];newrefnums=list(map(int,re.findall(r'\[(\d+)\]',re.sub(r'<!--.*?-->','',newbody))))
ck('285_citations_all_retained_and_superscript',len(refs)==285 and refs==newrefnums and Counter(refs)==Counter(oldrefnums))
ck('first_citation_order_retained',list(dict.fromkeys(refs))==list(range(1,96)))
tables=body.findall(q('tbl'));ck('seven_editable_tables',len(tables)==7)
for no,tbl in enumerate(tables,1):
 rows=tbl.findall(q('tr'));ck('header_repeat_'+str(no),rows[0].find('w:trPr/w:tblHeader',W) is not None)
 ck('no_cell_fill_'+str(no),not tbl.findall('.//w:shd',W))
 for side in ['left','right','insideV']:ck('table_no_vertical_'+str(no)+'_'+side,tbl.find('w:tblPr/w:tblBorders/w:'+side,W).get(q('val'))=='nil')
 ck('three_horizontal_rules_'+str(no),all(c.find('w:tcPr/w:tcBorders/w:top',W).get(q('val'))=='single' and c.find('w:tcPr/w:tcBorders/w:bottom',W).get(q('val'))=='single' for c in rows[0].findall(q('tc'))) and all(c.find('w:tcPr/w:tcBorders/w:bottom',W).get(q('val'))=='single' for c in rows[-1].findall(q('tc'))))
ck('two_15cm_figures',len(root.findall('.//wp:inline/wp:extent',W))==2 and all(int(e.get('cx'))==5400000 for e in root.findall('.//wp:inline/wp:extent',W)))
ck('image_alt_text_preserved',[(x.get('descr'),x.get('title')) for x in root.findall('.//wp:docPr',W)]==[(x.get('descr'),x.get('title')) for x in oldroot.findall('.//wp:docPr',W)])
ck('no_tracked_edits_comments_added',not root.findall('.//'+q('ins')) and not root.findall('.//'+q('del')) and not any('comments.xml' in n for n in after))
styles=E.fromstring(after['word/styles.xml']);normal=next(s for s in styles.findall(q('style')) if s.get(q('styleId'))=='Normal')
ck('11pt_body_and_115_spacing',normal.find('w:rPr/w:sz',W).get(q('val'))=='22' and normal.find('w:pPr/w:spacing',W).get(q('line'))=='276')
receipt=None
if (D/'WORD_OUTPUT_RECEIPT.json').is_file():
 receipt=get('WORD_OUTPUT_RECEIPT.json');ck('word_receipt_hash',receipt['file']['sha256']==sha(a.word.read_bytes()))
if a.require_visual:
 ck('all_final_pages_actually_viewed',receipt is not None and receipt['page_count']==21 and receipt['actual_visual_review_pages']==list(range(1,22)) and receipt['visual_review_done'] is True)

tree=[]
for rec in git('ls-tree','-rz',BASE).split(b'\0'):
 if not rec:continue
 meta,path=rec.split(b'\t',1);mode,typ,oid=meta.split();assert typ==b'blob';tree.append((oid.decode(),path.decode('utf-8')))
data=git('cat-file','--batch',input=('\n'.join(oid for oid,path in tree)+'\n').encode());pos=0
for oid,path in tree:
 end=data.index(b'\n',pos);size=int(data[pos:end].split()[2]);blob=data[end+1:end+1+size];pos=end+size+2;current=(R/path).read_bytes()
 ck('history_'+path,current==blob or (b'\0' not in current and current.replace(b'\r\n',b'\n')==blob))
ck('history_batch_exact',pos==len(data))
paths=git('diff','--name-only',BASE).decode('utf-8').splitlines()+git('ls-files','--others','--exclude-standard').decode('utf-8').splitlines();ck('new_directory_only',all(n.startswith(PREFIX) for n in paths))
ck('no_docx_or_thirdparty_binary_in_repo',not any(p.suffix.lower() in {'.pdf','.doc','.docx','.png','.zip','.pyc'} for p in D.rglob('*') if p.is_file()))
if a.manifest_check:
 manifest=get('SHA256_MANIFEST.json');names={x['path']:x for x in manifest['files']};current={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 ck('manifest_file_set',set(names)==current)
 for n,h in names.items():ck('manifest_'+n,sha((D/n).read_bytes())==h['sha256'] and (D/n).stat().st_size==h['bytes'])
result={'status':'PASS','scope':'格式、全文及来源身份保持、DOCX包保持和历史不变性；不代表投稿或科学终核','date_client':'2026-10-19','baseline_commit':BASE,'baseline_files_checked':len(tree),'checks_passed':len(checks),'checks':checks,'word_sha256':sha(a.word.read_bytes()),'source_word_sha256':sha(a.source_word.read_bytes()),'superscript_citations':len(refs),'word_blocks':len(actual),'references':95,'tables':7,'figures':2,'scientific_text_changed':False,'human_verified':False,'submission_ready':False}
if a.output:a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=True,indent=2))
