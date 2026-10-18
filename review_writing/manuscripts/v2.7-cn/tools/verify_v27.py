"""Read-only checks of structure, citation identity, history and optional Word; not scientific acceptance."""
from pathlib import Path
import argparse,csv,difflib,hashlib,json,re,subprocess,zipfile
import xml.etree.ElementTree as ET

BASE='4194ad110aaf64e502da00ea5474594aacaaa662'
FROZEN='51be6a1326e8c615ea24f80f1887f16a2e7b02fc'
PREFIX='review_writing/manuscripts/v2.7-cn/'
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[4])
ap.add_argument('--git',default='git');ap.add_argument('--word',type=Path)
ap.add_argument('--manifest-check',action='store_true');ap.add_argument('--output',type=Path)
a=ap.parse_args();R=a.repo;D=R/PREFIX
def git(*args,input=None):return subprocess.run([a.git,'-C',str(R),*args],input=input,capture_output=True,check=True).stdout
def sha(b):return hashlib.sha256(b).hexdigest()
def get(n):return json.loads((D/n).read_text(encoding='utf-8'))
def csvget(n):
 with (D/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def clean(s):return re.sub(r'\s*<!--.*?-->','',s).strip()
def norm(s):return re.sub(r'\s+',' ',s.replace('\u2060','').replace('\u00a0',' ')).strip()
def inline(s):return norm(re.sub(r'\[([^\]]+)\]\((https?://[^\s]+)\)',lambda m:m[1],s).replace('**',''))
checks=[]
def ck(name,truth,detail=None):
 assert truth,f'{name}: {detail}'
 checks.append({'check':name,'pass':True,**({'detail':detail} if detail is not None else {})})

md=(D/'REVIEW_CN_v2.7.md').read_text(encoding='utf-8');body,bib=md.split('\n## 参考文献\n',1)
old=git('show',BASE+':review_writing/manuscripts/v2.6-cn/REVIEW_CN_v2.6.md').decode('utf-8')
oldbody,oldbib=old.split('\n## 参考文献\n',1)
S=get('REVISION_SCOPE_AND_COUNTS.json');rows=csvget('references/REFERENCE_INDEX.csv');claims=csvget('CLAIM_EVIDENCE_MAP.csv')
ck('95_unique_source_identities',len(rows)==95 and len({x['stable_id'] for x in rows})==95)
ck('numbering_retained',all(x['v27']==x['v26'] for x in rows) and [int(x['v27']) for x in rows]==list(range(1,96)))
seen=list(dict.fromkeys(map(int,re.findall(r'\[(\d+)\]',re.sub(r'<!--.*?-->','',body)))))
entries=dict((int(n),t) for n,t in re.findall(r'^(\d+)\. (.+)$',bib,re.M))
oldentries=dict((int(n),t) for n,t in re.findall(r'^(\d+)\. (.+)$',oldbib,re.M))
ck('first_appearance_and_complete_bibliography',seen==list(range(1,96)) and list(entries)==seen)
ck('only_ref70_year_corrected',all(entries[n]==(oldentries[n].replace('Astrodynamics, 2021,','Astrodynamics, 2022,') if n==70 else oldentries[n]) for n in entries))
byref={int(x['v27']):x['stable_id'] for x in rows};ids=set(byref.values())
ck('152_unique_mapped_blocks',len(claims)==152 and len({x['claim_id'] for x in claims})==152)
for r in claims:
 t=clean(md.splitlines()[int(r['line'])-1]);refs=list(dict.fromkeys(map(int,re.findall(r'\[(\d+)\]',t))));eids=[x for x in r['evidence_ids'].split(';') if x]
 ck('claim_'+r['claim_id'],sha(t.encode())==r['text_sha256'] and ';'.join(map(str,refs))==r['reference_numbers'] and set(eids)<=ids and all(byref[n] in eids for n in refs) and r['human_verified']=='False')
ck('no_unmapped_claim_ids',set(re.findall(r'\[claim:([^\]]+)\]',body))=={x['claim_id'] for x in claims})
ck('five_chapters_seven_tables_two_figures',len(re.findall(r'^## [1-5] ',body,re.M))==5 and len(re.findall(r'^\*\*表\d',body,re.M))==7 and len(re.findall(r'^!\[',body,re.M))==2)
reg=get('REVISION_REGISTER_CN.json')
ck('60_rewrites_one_addition',reg['rewritten_blocks']==60 and reg['added_blocks']==1 and len(reg['blocks'])==61)
for r in reg['blocks']:
 line=next(s for s in md.splitlines() if '[claim:'+r['claim_id']+']' in s)
 ck('change_registry_'+r['claim_id'],clean(line)==r['after'])
expected=''.join(difflib.unified_diff(old.splitlines(keepends=True),md.splitlines(keepends=True),fromfile='v2.6-cn/REVIEW_CN_v2.6.md',tofile='v2.7-cn/REVIEW_CN_v2.7.md'))
ck('exact_saved_unified_diff',(D/'CHANGES_FROM_v2.6.diff').read_text(encoding='utf-8')==expected)
ck('visible_captions_unchanged',[clean(s) for s in body.splitlines() if re.match(r'^图[12] ',s)]==[clean(s) for s in oldbody.splitlines() if re.match(r'^图[12] ',s)])
for name in ['fig1_cn.svg','fig2_cn.svg']:
 ck('unchanged_svg_'+name,(D/'assets'/name).read_bytes()==git('show',BASE+':review_writing/manuscripts/v2.6-cn/assets/'+name))
ck('scope_counters',S['reference_count']==95 and S['academic_sources']==85 and S['engineering_sources']==10 and S['claim_blocks']==152 and S['manuscript_sha256']==sha((D/'REVIEW_CN_v2.7.md').read_bytes()))
ck('bounded_reading_and_draft_status',S['new_whole_paper_readings']==0 and S['formal_version_pairs_closed']==0 and S['human_verified'] is False and S['submission_ready'] is False and S['English_abstract_synchronized'] is True and S['English_full_manuscript_synchronized'] is False)
recheck=get('SOURCE_PASSAGE_RECHECKS_20261018.json')['records']
ck('six_targeted_sources',{x['stable_source_id'] for x in recheck}=={'E034','E042','E053','E065','E106','E121'})
ck('eight_pages_actually_viewed',sum(len(x['visual_pages']) for x in recheck)==8 and all(p['actual_visual_review'] is True and p['human_verified'] is False for x in recheck for p in x['visual_pages']))
ck('no_reading_or_pair_upgrade',all(x['new_whole_paper_reading'] is False and x['formal_version_pair_closed'] is False and x['human_verified'] is False for x in recheck))

# Compare every baseline blob. Git may expand LF to CRLF at checkout; this normalization is explicit.
tree=[]
for rec in git('ls-tree','-rz',BASE).split(b'\0'):
 if not rec:continue
 meta,path=rec.split(b'\t',1);mode,typ,oid=meta.split();assert typ==b'blob';tree.append((oid.decode(),path.decode('utf-8')))
data=git('cat-file','--batch',input=('\n'.join(oid for oid,p in tree)+'\n').encode());pos=0;hist=[];eol=[]
for oid,path in tree:
 end=data.index(b'\n',pos);size=int(data[pos:end].split()[2]);blob=data[end+1:end+1+size];pos=end+size+2
 current=(R/path).read_bytes();normalized=current!=blob and b'\0' not in current and current.replace(b'\r\n',b'\n')==blob
 ck('history_'+path,current==blob or normalized)
 if normalized:eol.append(path)
 hist.append({'path':path,'git_blob_sha256':sha(blob),'checkout_sha256':sha(current),'checkout_eol_only':normalized})
ck('batch_exact',pos==len(data))
v19='review_writing/manuscripts/v1.9/REVIEW_CN_v1.9.md';frozen=sha(git('show',FROZEN+':'+v19))
ck('frozen_v19_unchanged',sha((R/v19).read_bytes().replace(b'\r\n',b'\n'))==frozen)
changed=[x for x in git('diff','--name-only',BASE).decode('utf-8').splitlines() if x]
untracked=[x for x in git('ls-files','--others','--exclude-standard').decode('utf-8').splitlines() if x]
ck('changes_only_in_new_directory',all(p.startswith(PREFIX) for p in changed+untracked),{'changed_paths':len(changed),'untracked_paths':len(untracked)})

word_details=None
if a.word:
 W={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
 def tag(n):return '{'+W['w']+'}'+n
 expected=[];ls=[clean(x) for x in md.splitlines()];i=0
 while i<len(ls):
  s=ls[i];i+=1
  if not s or s.startswith('!['):continue
  if s.startswith('|'):
   table=[];i-=1
   while i<len(ls) and ls[i].startswith('|'):
    row=ls[i];i+=1
    if re.match(r'^\|\s*-',row):continue
    table.append([inline(x.strip()) for x in row.strip('|').split('|')])
   expected.append(['table',table]);continue
  expected.append(['p',inline(re.sub(r'^#{1,4} ','',s))])
 with zipfile.ZipFile(a.word) as z:
  root=ET.fromstring(z.read('word/document.xml'));actual=[]
  for el in root.find('w:body',W):
   if el.tag==tag('p'):
    t=norm(''.join(x.text or '' for x in el.iter(tag('t'))))
    if t:actual.append(['p',t])
   elif el.tag==tag('tbl'):
    actual.append(['table',[[norm(''.join(t.text or '' for t in cell.iter(tag('t')))) for cell in row.findall('w:tc',W)] for row in el.findall('w:tr',W)]])
  ck('complete_word_text_and_tables',actual==expected,{'expected_blocks':len(expected),'actual_blocks':len(actual)})
  pics=root.findall('.//wp:docPr',W);tabs=root.findall('.//w:tbl',W)
  ck('two_images_with_alt_text',len(pics)==2 and all(p.get('descr') and p.get('title') for p in pics))
  ck('seven_editable_tables_repeated_headers',len(tabs)==7 and all(t.find('w:tr/w:trPr/w:tblHeader',W) is not None for t in tabs))
  ck('95_reference_bookmarks',len(root.findall('.//w:bookmarkStart',W))==95)
  ck('no_tracked_changes_or_comments',not root.findall('.//w:ins',W) and not root.findall('.//w:del',W) and not any('comments.xml' in n for n in z.namelist()))
 word_details={'path':str(a.word),'sha256':sha(a.word.read_bytes()),'bytes':a.word.stat().st_size,'text_and_tables_equal':True,'blocks':len(expected),'pages':23}
 receipt=get('WORD_OUTPUT_RECEIPT.json')
 ck('word_receipt_identity',receipt['file']['sha256']==word_details['sha256'] and receipt['source_sha256']==sha((D/'REVIEW_CN_v2.7.md').read_bytes()))
 ck('all_23_pages_actually_viewed',receipt['page_count']==23 and receipt['actual_visual_review_pages']==list(range(1,24)) and receipt['visual_review_done'] is True and len(receipt['rendered_pages'])==23)
bad=[p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file() and p.suffix.lower() in {'.pdf','.docx','.png','.zip','.pyc'}]
ck('no_thirdparty_or_word_binaries_in_repo',not bad,bad)
if a.manifest_check:
 H=get('SHA256_MANIFEST.json');files={x['path']:x for x in H['files']};current={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 ck('manifest_exact_file_set',set(files)==current)
 for name,h in files.items():ck('manifest_'+name,sha((D/name).read_bytes())==h['sha256'] and (D/name).stat().st_size==h['bytes'])
result={'status':'PASS','scope':'结构、引文身份、历史内容及交付一致性；不是科学或人工验收','date_client':'2026-10-18','parent_commit':BASE,'historical_paths_checked':len(tree),'historical_content_aggregate_sha256':sha(json.dumps(hist,ensure_ascii=False,separators=(',',':')).encode()),'checkout_crlf_only_paths':eol,'frozen_v19_blob_sha256':frozen,'checks_passed':len(checks),'checks':checks,'word':word_details,'human_verified':False,'submission_ready':False,'push_performed':False}
if a.output:a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k not in {'checks','checkout_crlf_only_paths'}},ensure_ascii=True,indent=2))
