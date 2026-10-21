"""Audit B19 provenance, locators, counting, byte hashes and frozen scope.

This verifies local PDF TEXT CAPTURES, never original PDF binary identity.
No image review, proof reproduction or scientific acceptance is certified.
"""
import csv,hashlib,json,posixpath,re,subprocess,sys
from pathlib import Path
B=Path(__file__).resolve().parent.parent;R=B.parents[3]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub('[^a-z0-9]','',str(s).lower())
def git(*a):return subprocess.check_output(['git','-C',str(R),*a])
def cr(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def bn(n):return f'B{n:02d}_'+('20261021' if n>=17 else '20261020')
manifest=read(B/'SOURCE_MANIFEST_B19.json');status=read(B/'BATCH_STATUS.json');data=read(B/'READING_CONTENT.json')
sources=manifest['sources'];S={s['reading_id']:s for s in sources};claims=cr(B/'CLAIM_EVIDENCE_B19.csv');C={c['claim_id']:c for c in claims}
expected={'L004','L008','L014','L015','L018','L030','L033','L034','L036','L071'}
assert set(S)==expected and len(sources)==len(data)==10 and len({s['identifier'].lower() for s in sources})==10
assert len(C)==len(claims)==50 and set(C)=={f'C-B19-{n:03d}' for n in range(1,51)}
assert 'text' not in claims[0] and sum(s['pdf_pages'] for s in sources)==172
missing=[];capture_count=0;captures_complete=0
for d in data:
 sid=d['reading_id'];s=S[sid];note=(B/s['notes_path']).read_text(encoding='utf-8')
 assert s['source_format']=='REMOTE_PUBLIC_PDF_TEXT_CAPTURE'
 assert s['source_pdf_sha256'] is None and not s['source_pdf_byte_identity_verified'] and not s['source_pdf_archived']
 assert not s['source_fulltext_committed_to_git'] and s['visual_review_status']=='PENDING_TOOL_IMAGES_UNAVAILABLE'
 assert not s['human_verified'] and s['verification_status']=='human_pending'
 assert s['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' and s['pool_id']==sid and s['supplement_id'] is None
 assert s['title']==d['title'] and s['identifier']==d['identifier'] and s['actual_version']==d['actual_version']
 assert s['local_text_capture_sha256'] in note and '不是PDF原文件哈希' in note and '图表图像核查待完成' in note
 assert s['narrative_body_pages']==list(range(d['body_pages'][0],d['body_pages'][1]+1))
 f=Path(s['local_text_capture_path']);lines=[];seen=set()
 if f.exists():
  assert sha(f)==s['local_text_capture_sha256'];lines=read(f)
  assert {x['line'] for x in lines}==set(range(s['web_total_extracted_lines']));captures_complete+=1
 else:missing.append(str(f))
 for cap in s['capture_files']:
  f=Path(cap['local_path'])
  if not f.exists():missing.append(str(f));continue
  assert sha(f)==cap['sha256'];t=f.read_text(encoding='utf-8')
  assert s['acquisition_url'] in t and 'Content type: application/pdf' in t
  assert 'Number of pages: '+str(s['pdf_pages']) in t
  seen.update(map(int,re.findall(r'^L(\d+)@P',t,re.M)));capture_count+=1
 if not missing:assert seen==set(range(s['web_total_extracted_lines']))
 meta=read(B/'metadata'/(sid+'_CROSSREF.json'));identity=read(B/'metadata'/(sid+'_IDENTITY.json'))
 assert meta['DOI'].lower()==s['identifier'].lower() and norm(meta['title'][0])==norm(s['title'])
 assert identity['local_text_capture_sha256']==s['local_text_capture_sha256'] and identity['source_pdf_sha256'] is None
 assert identity['source_limitations']==d['limitations'] and not identity['formal_version_text_compared']
 for c in d['claims']:
  q=C[c['claim_id']];h=hashlib.sha256(' '.join(c['text'].split()).encode('utf-8')).hexdigest()
  assert q['claim_text_sha256']==c['claim_text_sha256']==h
  assert c['source_id']==q['source_id']==s['source_id'] and q['pool_id']==sid
  assert c['claim_id'] in note and c['text'] in note and q['note_path']==s['notes_path']
  assert q['locator']==c['locator'] and q['pdf_physical_pages']==';'.join(map(str,c['pages']))
  assert q['human_verified']=='False' and q['adoption_status']==s['adoption_status']
  assert c['pages'] and all(1<=n<=s['pdf_pages'] for n in c['pages'])
  if lines:assert all(any(x['pdf_page']==n for x in lines) for n in c['pages'])
assert len(list(B.glob('READING_L*_CN.md')))==10 and len(list((B/'metadata').glob('*_IDENTITY.json')))==10
assert len(list((B/'metadata').glob('*_CROSSREF.json')))==11
clar=read(B/'metadata/L071_CLARIFICATION_CROSSREF.json')
assert clar['DOI'].lower()=='10.2514/1.i010588.c1' and clar['update-to'][0]['DOI'].lower()==S['L071']['identifier'].lower()
assert S['L071']['adoption_status']=='HOLD_pending_clarification_full_text'
assert S['L014']['adoption_status']=='context_only_outside_core_LEO_scope'
assert sum(s['adoption_status']=='candidate_after_human_review' for s in sources)==8
pool=cr(B/'READING_STATUS_80_AFTER_B19.csv');prev=cr(B.parent/'B18_20261021/READING_STATUS_80_AFTER_B18.csv')
assert len(pool)==80 and len({x['pool_id'] for x in pool})==80
assert sum(x['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for x in pool)==30
assert sum(x['reading_status']=='NOT_CLOSE_READ' for x in pool)==49
assert sum(x['reading_status']=='PARTIAL_TEXT_READ_NOT_COUNTED' for x in pool)==1
for now,old in zip(pool,prev):
 assert now['pool_id']==old['pool_id'] and now['title_en']==old['title_en'] and now['doi']==old['doi']
 if now['pool_id'] in expected:
  assert old['reading_status']=='NOT_CLOSE_READ' and now['batch']=='B19_20261021' and now['note_path']==S[now['pool_id']]['notes_path']
 elif now['pool_id']=='L003':assert now['reading_status']=='PARTIAL_TEXT_READ_NOT_COUNTED'
 else:
  for k in old:
   if k!='note_path':assert now[k]==old[k]
  if old['note_path']:assert now['note_path']==posixpath.normpath('../B18_20261021/'+old['note_path'])
 if now['note_path']:assert (B/now['note_path']).is_file()
supp=cr(B/'SUPPLEMENT_READING_REGISTER_B19.csv');old_supp=cr(B.parent/'B18_20261021/SUPPLEMENT_READING_REGISTER_B18.csv')
assert len(supp)==len(old_supp)==60
for now,old in zip(supp,old_supp):
 for k in old:
  if k!='note_path':assert now[k]==old[k]
 assert now['note_path']==posixpath.normpath('../B18_20261021/'+old['note_path']) and (B/now['note_path']).is_file()
partial=read(B/'PARTIAL_READS.json');assert len(partial)==1 and partial[0]['pool_id']=='L003' and not partial[0]['counted_as_completed']
pf=Path(partial[0]['local_text_capture_path'])
if pf.exists():assert sha(pf)==partial[0]['local_text_capture_sha256']
else:missing.append(str(pf))
assert dict(original_pool_close_read_this_batch=10,original_pool_close_read_cumulative=30,original_pool_remaining=50,topic_supplement_close_read_this_batch=0,topic_supplement_close_read_cumulative=60,B11_through_B19_close_read_records=90,claim_count=50,B11_through_B19_claim_records=415,remote_public_pdf_text_read_count=10,remote_pdf_total_pages=172,pdf_binary_archived_count=0,pdf_binary_identity_verified_count=0,actual_visual_page_count=0).items()<=status.items()
assert not status['human_verified'] and not status['submission_ready'] and not status['manuscript_modified']
assert status['held_from_scientific_adoption']==['L071'] and status['partial_read_not_counted']==['L003']
dedup=read(B/'DEDUP_CHECK.json');prior=0
assert not dedup['prior_body_read_matches'] and dedup['prior_B11_through_B18_source_records_checked']==80
for n in range(11,19):
 for old in read(B.parent/bn(n)/f'SOURCE_MANIFEST_B{n:02d}.json')['sources']:
  prior+=1;ot=[old.get('title',old.get('actual_title',''))]+old.get('aliases',[]);t=json.dumps(old,ensure_ascii=False).lower()
  for s in sources:assert s['identifier'].lower() not in t and norm(s['title']) not in map(norm,ot)
assert prior==80
registers_checked=0
for reg in dedup['registers']:
 f=Path(reg['path'])
 if f.exists():assert sha(f)==reg['sha256'];registers_checked+=1
 else:missing.append(str(f))
assert {x['pool_id'] for x in dedup['register_matches'] if x['register'].endswith('LITERATURE_POOL.json')}==expected
acq=read(B/'ACQUISITION_LOG.json');assert set(acq['selected_ids'])==expected and acq['selected_source_binary_download_success_count']==acq['selected_pdf_binary_sha256_available_count']==acq['selected_visual_pages_success_count']==0
base=manifest['base_commit'];prefix='review_writing/evidence/reading_batches/B19_20261021/'
outside=[x for x in git('diff','--name-only',base).decode().splitlines() if not x.startswith(prefix)]
assert not outside
assert all(x.startswith(prefix) for x in git('ls-files','--others','--exclude-standard').decode().splitlines())
baseline='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert sha(R/baseline)=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
assert hashlib.sha256(git('show',base+':'+baseline)).hexdigest()==sha(R/baseline)
inherited=git('ls-tree','-r','--name-only',base,'--','review_writing/evidence/reading_batches').decode().splitlines()
for rel in inherited:assert hashlib.sha256(git('show',base+':'+rel)).hexdigest()==sha(R/rel)
inherited_recent=[x for x in inherited if any('/'+bn(n)+'/' in x for n in range(11,19))]
assert len(inherited_recent)==312 and len(inherited)==614
for p in B.glob('*.md'):
 for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if target.startswith(('http:','https:','#')):continue
  if target in ['VALIDATION_REPORT.json','SHA256_MANIFEST.json'] and '--write-report' in sys.argv:continue
  assert (p.parent/target).is_file(),(p.name,target)
files=[p for p in B.rglob('*') if p.is_file()]
assert not [p for p in files if b'\r\n' in p.read_bytes()]
assert not [p for p in files if p.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.txt','.xml','.pyc']]
report=dict(status='PASS_WITH_EXPLICIT_SOURCE_LIMITATIONS' if not missing else 'PACKAGE_ONLY_EXTERNAL_RECHECK_INCOMPLETE',sources=10,claims=50,original_pool_completed=30,original_pool_remaining=50,remaining_unread=49,remaining_partial=1,supplements=60,B11_through_B19_records=90,B11_through_B19_claims=415,remote_pdf_pages=172,complete_local_text_captures_checked=captures_complete,individual_capture_hashes_checked=capture_count,original_PDF_binary_hashes_checked=0,visual_pages_checked=0,source_binary_and_visual_checks_pending=True,register_hashes_checked=registers_checked,prior_body_records_rechecked=prior,inherited_B11_through_B18_files_unchanged=len(inherited_recent),all_inherited_batch_files_unchanged=len(inherited),manuscript_sha256_unchanged=sha(R/baseline),outside_batch_changes=outside,missing_local_files=missing,human_verified=False,submission_ready=False,scope='Text capture identity, extracted-line coverage, claim hashes/locators, counts, links and frozen scope only; no original PDF identity, image review, scientific correctness or proof/experiment reproduction certificate')
if '--write-report' in sys.argv:
 (B/'VALIDATION_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 hashes={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in B.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 (B/'SHA256_MANIFEST.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
else:
 hashes=read(B/'SHA256_MANIFEST.json')
 assert set(hashes)=={str(p.relative_to(B)).replace('\\','/') for p in files if p.name!='SHA256_MANIFEST.json'}
 for rel,h in hashes.items():assert sha(B/rel)==h,rel
 report['package_hashes_checked']=len(hashes)
print(json.dumps(report,ensure_ascii=False,indent=2))
