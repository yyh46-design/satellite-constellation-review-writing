"""Verify B18 identities, provenance, locators, counts and unchanged scope.

No proof/experiment reproduction or scientific-correctness certificate.
--write-report freezes the validation report and package byte hashes.
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
def ids(s):return [s['identifier']]+s.get('identifier_aliases',[])+([(s.get('arxiv_actual_version') or '').split('v')[0]] if s.get('arxiv_actual_version') else [])
def titles(s):return [s['title']]+s.get('aliases',[])
def prevname(n):return f'B{n:02d}_'+('20261021' if n==17 else '20261020')
manifest=read(B/'SOURCE_MANIFEST_B18.json');status=read(B/'BATCH_STATUS.json');data=read(B/'READING_CONTENT.json')
sources=manifest['sources'];sm={s['reading_id']:s for s in sources};claims=cr(B/'CLAIM_EVIDENCE_B18.csv');cm={c['claim_id']:c for c in claims}
assert len(sources)==len(data)==len(sm)==10 and set(sm)=={f'S{n:03d}' for n in range(51,61)}
assert len({s['identifier'].lower() for s in sources})==10
assert len(claims)==len(cm)==sum(len(d['claims']) for d in data)==50
assert set(cm)=={f'C-B18-{n:03d}' for n in range(1,51)} and 'text' not in claims[0]
assert sum(s['pdf_pages'] for s in sources)==271
assert sum(len(s['visual_reviews']) for s in sources)==46
for prefix,count in {'multi_':6,'single_':2,'general_':2}.items():assert sum(s['evidence_role'].startswith(prefix) for s in sources)==count
assert all(s['adoption_status']=='candidate_after_human_review' for s in sources)
missing=[];local_sources=local_visuals=0
for d in data:
 sid=d['reading_id'];s=sm[sid];p=Path(s['local_source_path']);note=(B/s['notes_path']).read_text(encoding='utf-8')
 assert s['source_format']=='PDF' and not s['source_committed_to_git'] and not s['human_verified']
 assert s['verification_status']=='human_pending' and s['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE'
 assert s['reading_date']=='2026-10-21' and s['source_sha256'] in note and d['actual_title'] in note
 assert s['actual_version']==d['actual_version'] and s['evidence_role']==d['evidence_role'] and s['adoption_status']==d['adoption_status']
 assert s['narrative_body_pages']==list(range(d['body_pages'][0],d['body_pages'][1]+1))
 assert all(1<=n<=s['pdf_pages'] for n in s['narrative_body_pages'])
 if p.exists():
  assert p.read_bytes().startswith(b'%PDF') and sha(p)==s['source_sha256'];local_sources+=1
  try:
   from pypdf import PdfReader
   pdf=PdfReader(p);assert len(pdf.pages)==s['pdf_pages']
   if s.get('arxiv_actual_version'):assert s['arxiv_actual_version'] in (pdf.pages[0].extract_text() or '')
  except ImportError:pass
 else:missing.append(str(p))
 for c in d['claims']:
  q=cm[c['claim_id']];h=hashlib.sha256(' '.join(c['text'].split()).encode('utf-8')).hexdigest()
  assert h==c['claim_text_sha256']==q['claim_text_sha256']
  assert q['source_id']==c['source_id']==s['source_id'] and q['reading_id']==sid
  assert c['claim_id'] in note and c['text'] in note and c['locator']
  assert q['note_path']==s['notes_path'] and q['adoption_status']==s['adoption_status'] and q['human_verified']=='False'
  assert c['pages'] and all(1<=n<=s['pdf_pages'] for n in c['pages']) and q['pdf_pages']==';'.join(map(str,c['pages']))
 assert set(d['visual_pages'])=={v['pdf_page'] for v in s['visual_reviews']}
 for v in s['visual_reviews']:
  assert v['status']=='VISUALLY_INSPECTED' and 1<=v['pdf_page']<=s['pdf_pages'];q=Path(v['local_path'])
  if q.exists():assert sha(q)==v['sha256'];local_visuals+=1
  else:missing.append(str(q))
 z=read(B/'metadata'/(sid+'_IDENTITY.json'))
 assert z['source_sha256']==s['source_sha256'] and z['adoption_status']==s['adoption_status']
 assert not z['human_verified'] and not z['formal_version_text_compared'] and z['source_issues'] and not z['source_issues_resolved']
assert len(list(B.glob('READING_S*_CN.md')))==10 and len(list((B/'metadata').glob('*_IDENTITY.json')))==10
crossrefs=list((B/'metadata').glob('*_CROSSREF.json'));assert len(crossrefs)==5
for p in crossrefs:
 z=read(p);s=sm[p.name.split('_')[0]];assert norm(z['title'][0])==norm(s['title']) and z['DOI'].lower()==s['identifier'].lower()
assert len(list((B/'metadata').glob('*_NASA.json')))==2
assert read(B/'metadata/S051_IDENTITY.json')['issue_year']==2026
assert read(B/'metadata/S060_IDENTITY.json')['actual_arxiv_version']=='2603.25835v1'
for sid in ['S054','S057','S058']:assert sm[sid]['research_line']=='Starling'
assert read(B/'metadata/S060_IDENTITY.json')['failure_rate_adoption']=='HOLD'
for p in B.glob('*.md'):
 for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if target.startswith(('http:','https:','#')):continue
  if target in ['VALIDATION_REPORT.json','SHA256_MANIFEST.json'] and '--write-report' in sys.argv:continue
  q=p.parent/target;assert q.is_file(),(p.name,target)
  if 'C-B18-' in label:
   first=int(re.search(r'C-B18-(\d{3})',label).group(1));nums=[int(x) for x in re.findall(r'(?<!\d)(\d{3})(?!\d)',label)]
   if '至' in label:nums=list(range(first,nums[-1]+1))
   for n in nums:
    cid=f'C-B18-{n:03d}';assert cid in cm and cid in q.read_text(encoding='utf-8'),(p.name,cid)
pool=cr(B/'READING_STATUS_80_AFTER_B18.csv');prev=cr(B.parent/'B17_20261021/READING_STATUS_80_AFTER_B17.csv')
assert len(pool)==80 and sum(r['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for r in pool)==20 and sum(r['reading_status']=='NOT_CLOSE_READ' for r in pool)==60
for now,old in zip(pool,prev):
 for k in old:
  if k!='note_path':assert now[k]==old[k]
 if old['note_path']:assert now['note_path']==posixpath.normpath('../B17_20261021/'+old['note_path']) and (B/now['note_path']).is_file()
supp=cr(B/'SUPPLEMENT_READING_REGISTER_B18.csv');prev=cr(B.parent/'B17_20261021/SUPPLEMENT_READING_REGISTER_B17.csv')
assert len(supp)==60 and {s['supplement_id'] for s in supp}=={f'S{n:03d}' for n in range(1,61)}
assert sum(s['batch']=='B18_20261021' for s in supp)==10
for s in supp:assert (B/s['note_path']).is_file()
for now,old in zip(supp[:50],prev):
 for k in old:
  if k!='note_path':assert now[k]==old[k]
 assert now['note_path']==posixpath.normpath('../B17_20261021/'+old['note_path'])
expected=dict(original_pool_close_read_this_batch=0,original_pool_close_read_cumulative=20,original_pool_remaining=60,topic_supplement_close_read_this_batch=10,topic_supplement_close_read_cumulative=60,B11_through_B18_close_read_records=80,pdf_files_acquired_and_read=10,pdf_total_pages=271,actual_visual_page_count=46,claim_count=50,multi_spacecraft_primary_papers=6,single_controlled_spacecraft_foundation_papers=2,general_or_cross_domain_foundation_papers=2,flight_report_papers=3,independent_flight_mission_lines_this_batch=1,candidate_after_human_review=10)
for k,v in expected.items():assert status[k]==v,(k,status[k])
assert not status['held_from_scientific_adoption'] and len(status['held_specific_statements'])==6
assert not status['manuscript_modified'] and not status['human_verified'] and not status['submission_ready']
dedup=read(B/'DEDUP_CHECK.json');assert not dedup['matches'] and not dedup['prior_source_matches'] and dedup['prior_sources_checked']==70
assert dedup['excluded_duplicate']['prior_source_id']=='E-B11-L012'
registers_rechecked=0;register_missing=[]
for reg in dedup['registers']:
 p=Path(reg['path'])
 if not p.exists():register_missing.append(str(p));continue
 assert sha(p)==reg['sha256'];registers_rechecked+=1;t=p.read_text(encoding='utf-8-sig')
 for s in sources:
  assert not any(i.lower() in t.lower() for i in ids(s))
  assert not any(norm(title) in norm(t) for title in titles(s))
prior=0
for n in range(11,18):
 for old in read(B.parent/prevname(n)/f'SOURCE_MANIFEST_B{n:02d}.json')['sources']:
  prior+=1;ot=[old.get('title',old.get('actual_title','')),old.get('related_formal_title','')]+old.get('aliases',[]);raw=json.dumps(old,ensure_ascii=False).lower()
  for s in sources:
   assert not any(i.lower() in raw for i in ids(s)) and not any(norm(t)==norm(u) for t in titles(s) for u in ot if u)
assert prior==70
acq=read(B/'ACQUISITION_LOG.json');assert set(acq['selected_source_ids'])==set(sm) and len(acq['successful_or_last_attempt_records'])==10
for a in acq['successful_or_last_attempt_records']:
 assert a['sha256']==sm[a['id']]['source_sha256'] and a['pages']==sm[a['id']]['pdf_pages'] and a['status']=='pdf_acquired'
 p=Path(a['extracted_pages_path'])
 if p.exists():assert sha(p)==a['extracted_pages_sha256']==sm[a['id']]['extracted_pages_sha256']
 else:missing.append(str(p))
assert len(acq['unselected_candidates'])==6
prefix='review_writing/evidence/reading_batches/B18_20261021/'
delta=git('diff','--name-only',manifest['base_commit']).decode().splitlines();outside=[x for x in delta if not x.startswith(prefix)];assert not outside,outside
assert all(x.startswith(prefix) for x in git('ls-files','--others','--exclude-standard').decode().splitlines())
baseline='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert sha(R/baseline)=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
assert hashlib.sha256(git('show',manifest['base_commit']+':'+baseline)).hexdigest()==sha(R/baseline)
inherited=[]
for n in range(11,18):
 paths=git('ls-tree','-r','--name-only',manifest['base_commit'],'--','review_writing/evidence/reading_batches/'+prevname(n)).decode().splitlines()
 for rel in paths:assert hashlib.sha256(git('show',manifest['base_commit']+':'+rel)).hexdigest()==sha(R/rel)
 inherited+=paths
assert len(inherited)==270
files=[p for p in B.rglob('*') if p.is_file()]
assert not [p for p in files if p.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.txt','.xml','.pyc']]
assert not [p for p in files if b'\r\n' in p.read_bytes()], 'Package must use LF'
report=dict(status='PASS' if not missing and not register_missing else 'PACKAGE_PASS_EXTERNAL_RECHECK_INCOMPLETE',batch='B18_20261021',sources=10,claims=50,pdf_pages=271,local_original_source_hashes_checked=local_sources,local_visual_hashes_checked=local_visuals,missing_local_files=missing,original80_pool_after_batch={'close_read':20,'not_close_read':60},separate_topic_supplements_cumulative=60,B11_through_B18_close_read_records=80,prior_B11_through_B17_inherited_files_unchanged=len(inherited),prior_source_records_rechecked=prior,dedup_register_hashes_rechecked=registers_rechecked,dedup_registers_not_available=register_missing,held_from_scientific_adoption=[],specific_statement_holds_preserved=True,shared_flight_research_line_preserved=True,manuscript_sha256_unchanged=sha(R/baseline),outside_batch_tracked_changes=outside,human_verified=False,scope='File identity, locators, links, counting and change scope only; no scientific correctness, formal proof or experiment reproduction certificate')
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
