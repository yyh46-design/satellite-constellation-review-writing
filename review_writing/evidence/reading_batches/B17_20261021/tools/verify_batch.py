"""Check B17 file identity, evidence links, counts and unchanged scope.

No scientific correctness certificate, proof reproduction or experiment replication.
With --write-report freeze report and checksums; otherwise verify the frozen package.
"""
import csv,hashlib,json,posixpath,re,subprocess,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
B=Path(__file__).resolve().parent.parent;R=B.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def norm(s):return re.sub('[^a-z0-9]','',str(s).lower())
def git(*args):return subprocess.check_output(['git','-C',str(R),*args])
def cr(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def ids(s):return [i for i in [s['identifier'],s.get('related_formal_doi'),(s.get('arxiv_actual_version') or '').split('v')[0]] if i]
def titles(s):return [s['title']]+s.get('aliases',[])
manifest=read(B/'SOURCE_MANIFEST_B17.json');status=read(B/'BATCH_STATUS.json');data=read(B/'READING_CONTENT.json')
sources=manifest['sources'];sm={s['reading_id']:s for s in sources}
claims=cr(B/'CLAIM_EVIDENCE_B17.csv');cm={c['claim_id']:c for c in claims}
assert len(sources)==len(data)==len(sm)==10
assert set(sm)=={f'S{n:03d}' for n in range(41,51)}
assert len({s['identifier'].lower() for s in sources})==10
assert len(claims)==len(cm)==sum(len(d['claims']) for d in data)==50
assert set(cm)=={f'C-B17-{n:03d}' for n in range(1,51)} and 'text' not in claims[0]
assert sum(s['pdf_pages'] for s in sources)==134
assert sum(len(s['visual_reviews']) for s in sources)==40
expected_roles={'multi_':5,'single_':3,'general_':2}
for prefix,count in expected_roles.items():assert sum(s['evidence_role'].startswith(prefix) for s in sources)==count
assert [s['reading_id'] for s in sources if s['adoption_status']=='HOLD_FOR_SOURCE_CLARIFICATION']==['S045']
local_sources=local_visuals=0;missing=[];register_missing=[]
for d in data:
 sid=d['reading_id'];s=sm[sid];p=Path(s['local_source_path']);note=(B/s['notes_path']).read_text(encoding='utf-8')
 assert s['source_format']=='PDF' and not s['source_committed_to_git']
 assert not s['human_verified'] and s['verification_status']=='human_pending'
 assert s['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' and s['reading_date']=='2026-10-21'
 assert s['source_sha256'] in note and d['actual_title'] in note
 assert s['actual_version']==d['actual_version'] and s['evidence_role']==d['evidence_role']
 assert s['adoption_status']==d['adoption_status']
 assert s['narrative_body_pages']==list(range(d['body_pages'][0],d['body_pages'][1]+1))
 assert all(1<=n<=s['pdf_pages'] for n in s['narrative_body_pages'])
 if p.exists():
  assert sha(p)==s['source_sha256'];local_sources+=1
  try:
   from pypdf import PdfReader
   pdf=PdfReader(p);assert len(pdf.pages)==s['pdf_pages']
   if s.get('arxiv_actual_version'):assert s['arxiv_actual_version'] in (pdf.pages[0].extract_text() or '')
  except ImportError:pass
 else:missing.append(str(p))
 for c in d['claims']:
  q=cm[c['claim_id']];h=hashlib.sha256(' '.join(c['text'].split()).encode('utf-8')).hexdigest()
  assert c['claim_text_sha256']==q['claim_text_sha256']==h
  assert q['reading_id']==sid and q['source_id']==c['source_id']==s['source_id']
  assert q['note_path']==s['notes_path'] and q['adoption_status']==s['adoption_status']
  assert q['human_verified']=='False' and c['text'] in note and c['claim_id'] in note and c['locator']
  assert c['pages'] and all(1<=n<=s['pdf_pages'] for n in c['pages'])
  assert q['pdf_pages']==';'.join(map(str,c['pages']))
 assert set(d['visual_pages'])=={v['pdf_page'] for v in s['visual_reviews']}
 for v in s['visual_reviews']:
  assert v['status']=='VISUALLY_INSPECTED' and 1<=v['pdf_page']<=s['pdf_pages']
  q=Path(v['local_path'])
  if q.exists():assert sha(q)==v['sha256'];local_visuals+=1
  else:missing.append(str(q))
 identity=read(B/'metadata'/(sid+'_IDENTITY.json'))
 assert identity['source_sha256']==s['source_sha256'] and not identity['human_verified'] and not identity['formal_version_text_compared']
 assert identity['adoption_status']==s['adoption_status']
assert len(list(B.glob('READING_S*_CN.md')))==10
assert len(list((B/'metadata').glob('*_IDENTITY.json')))==10
crossrefs=list((B/'metadata').glob('*_CROSSREF.json'));assert len(crossrefs)==5
for p in crossrefs:
 z=read(p);s=sm[p.name.split('_')[0]]
 assert norm(z['title'][0])==norm(s['title'])
 assert z['DOI'].lower()==(s.get('related_formal_doi') or s['identifier']).lower()
for sid,v in {'S041':'2211.03658v3','S042':'2311.09439v1','S043':'2403.03314v2','S044':'2510.19058v1','S045':'2605.20138v1','S049':'2204.00208v2'}.items():assert sm[sid]['arxiv_actual_version']==v
assert read(B/'metadata/S042_IDENTITY.json')['counts_as_one_record']
assert not read(B/'metadata/S042_IDENTITY.json')['title_difference_resolved']
assert read(B/'metadata/S045_IDENTITY.json')['scientific_claim_adoption_blocked']
assert not read(B/'metadata/S045_IDENTITY.json')['regulatory_claim_verified']
assert not read(B/'metadata/S048_IDENTITY.json')['activation_conflict_resolved']
assert read(B/'metadata/S046_IDENTITY.json')['repository_cover_pages']==1
for p in B.glob('*.md'):
 for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if target.startswith(('http:','https:','#')):continue
  q=p.parent/target
  if target in ['VALIDATION_REPORT.json','SHA256_MANIFEST.json'] and '--write-report' in sys.argv:continue
  assert q.is_file(),(p.name,target)
  if 'C-B17-' in label:
   first=int(re.search(r'C-B17-(\d{3})',label).group(1));nums=[int(x) for x in re.findall(r'(?<!\d)(\d{3})(?!\d)',label)]
   if '至' in label:nums=list(range(first,nums[-1]+1))
   for n in nums:
    cid=f'C-B17-{n:03d}';assert cid in cm and cid in q.read_text(encoding='utf-8'),(p.name,cid)
pool=cr(B/'READING_STATUS_80_AFTER_B17.csv');prev=cr(B.parent/'B16_20261020/READING_STATUS_80_AFTER_B16.csv')
assert len(pool)==80 and sum(r['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for r in pool)==20 and sum(r['reading_status']=='NOT_CLOSE_READ' for r in pool)==60
for now,old in zip(pool,prev):
 for k in old:
  if k!='note_path':assert now[k]==old[k]
 if old['note_path']:
  assert now['note_path']==posixpath.normpath('../B16_20261020/'+old['note_path'])
  assert (B/now['note_path']).is_file()
supp=cr(B/'SUPPLEMENT_READING_REGISTER_B17.csv');prev=cr(B.parent/'B16_20261020/SUPPLEMENT_READING_REGISTER_B16.csv')
assert len(supp)==50 and {s['supplement_id'] for s in supp}=={f'S{n:03d}' for n in range(1,51)}
assert sum(s['batch']=='B17_20261021' for s in supp)==10
for s in supp:assert (B/s['note_path']).is_file()
for now,old in zip(supp[:40],prev):
 for k in old:
  if k!='note_path':assert now[k]==old[k]
 assert now['note_path']==posixpath.normpath('../B16_20261020/'+old['note_path'])
for k,v in dict(original_pool_close_read_this_batch=0,original_pool_close_read_cumulative=20,original_pool_remaining=60,topic_supplement_close_read_this_batch=10,topic_supplement_close_read_cumulative=50,B11_through_B17_close_read_records=70,pdf_files_acquired_and_read=10,pdf_total_pages=134,actual_visual_page_count=40,claim_count=50,multi_spacecraft_primary_papers=5,single_controlled_spacecraft_foundation_papers=3,general_or_cross_domain_foundation_papers=2,candidate_after_human_review=9).items():assert status[k]==v,(k,status[k])
assert status['held_from_scientific_adoption']==['S045']
assert not status['manuscript_modified'] and not status['human_verified'] and not status['submission_ready']
dedup=read(B/'DEDUP_CHECK.json');assert not dedup['matches'] and not dedup['prior_source_matches'] and dedup['prior_sources_checked']==60
registers_rechecked=0
for reg in dedup['registers']:
 p=Path(reg['path'])
 if p.exists():
  assert sha(p)==reg['sha256'];registers_rechecked+=1;t=p.read_text(encoding='utf-8-sig')
  for s in sources:
   assert not any(i.lower() in t.lower() for i in ids(s))
   assert not any(norm(title) in norm(t) for title in titles(s))
 else:register_missing.append(str(p))
prior=0
for n in range(11,17):
 prev=f'B{n:02d}_20261020'
 for old in read(B.parent/prev/f'SOURCE_MANIFEST_B{n:02d}.json')['sources']:
  prior+=1;ot=[old.get('title',old.get('actual_title','')),old.get('related_formal_title','')]+old.get('aliases',[])
  raw=json.dumps(old,ensure_ascii=False).lower()
  for s in sources:
   assert not any(i.lower() in raw for i in ids(s))
   assert not any(norm(t)==norm(u) for t in titles(s) for u in ot if u)
assert prior==60
acq=read(B/'ACQUISITION_LOG.json');assert set(acq['selected_source_ids'])==set(sm) and len(acq['successful_or_last_attempt_records'])==10
for a in acq['successful_or_last_attempt_records']:assert a['sha256']==sm[a['id']]['source_sha256'] and a['pages']==sm[a['id']]['pdf_pages']
assert len(acq['unselected_candidates'])==2 and all(a['status']=='failed' for a in acq['unselected_candidates'])
prefix='review_writing/evidence/reading_batches/B17_20261021/'
delta=git('diff','--name-only',manifest['base_commit']).decode().splitlines();outside=[x for x in delta if not x.startswith(prefix)];assert not outside,outside
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();assert all(x.startswith(prefix) for x in untracked)
baseline='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert sha(R/baseline)=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
assert hashlib.sha256(git('show',manifest['base_commit']+':'+baseline)).hexdigest()==sha(R/baseline)
inherited=[]
for n in range(11,17):
 paths=git('ls-tree','-r','--name-only',manifest['base_commit'],'--',f'review_writing/evidence/reading_batches/B{n:02d}_20261020').decode().splitlines()
 for rel in paths:assert hashlib.sha256(git('show',manifest['base_commit']+':'+rel)).hexdigest()==sha(R/rel)
 inherited+=paths
assert len(inherited)==230
files=[p for p in B.rglob('*') if p.is_file()]
assert not [p for p in files if p.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.txt','.xml','.pyc']]
report=dict(status='PASS' if not missing and not register_missing else 'PACKAGE_PASS_EXTERNAL_RECHECK_INCOMPLETE',batch='B17_20261021',sources=10,claims=50,pdf_pages=134,local_original_source_hashes_checked=local_sources,local_visual_hashes_checked=local_visuals,missing_local_files=missing,original80_pool_after_batch={'close_read':20,'not_close_read':60},separate_topic_supplements_cumulative=50,B11_through_B17_close_read_records=70,prior_B11_through_B16_inherited_files_unchanged=len(inherited),prior_source_records_rechecked=prior,dedup_register_hashes_rechecked=registers_rechecked,dedup_registers_not_available=register_missing,held_from_scientific_adoption=['S045'],source_conflicts_preserved=True,manuscript_sha256_unchanged=sha(R/baseline),outside_batch_tracked_changes=outside,human_verified=False,scope='File identity, evidence links, locators, counting and change scope only; no proof, reproduction or scientific correctness certificate')
if '--write-report' in sys.argv:
 (B/'VALIDATION_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 hashes={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in B.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 (B/'SHA256_MANIFEST.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
else:
 hashes=read(B/'SHA256_MANIFEST.json')
 for rel,h in hashes.items():assert sha(B/rel)==h,rel
 assert set(hashes)=={str(p.relative_to(B)).replace('\\','/') for p in files if p.name!='SHA256_MANIFEST.json'}
 report['package_hashes_checked']=len(hashes)
print(json.dumps(report,ensure_ascii=False,indent=2))
