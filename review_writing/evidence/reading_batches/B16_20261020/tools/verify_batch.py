"""Verify B16 file identities, locators, links, counting and unchanged scope.

This does not reproduce experiments or certify scientific correctness.
--write-report freezes a report and package hashes; plain runs check hashes.
"""
import csv,hashlib,json,posixpath,re,subprocess,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
B=Path(__file__).resolve().parent.parent
R=B.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def norm(t):return re.sub('[^a-z0-9]','',str(t).lower())
def git(*args):return subprocess.check_output(['git','-C',str(R),*args])
def csvread(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def ids(d):
 return [i for i in [d['identifier'],d.get('related_formal_doi'),(d.get('arxiv_actual_version') or '').split('v')[0]] if i]
manifest=read(B/'SOURCE_MANIFEST_B16.json')
data=read(B/'READING_CONTENT.json')
status=read(B/'BATCH_STATUS.json')
sources=manifest['sources'];sm={s['reading_id']:s for s in sources}
claims=csvread(B/'CLAIM_EVIDENCE_B16.csv');cm={c['claim_id']:c for c in claims}
assert len(sources)==len(data)==len(sm)==10
assert set(sm)=={f'S{n:03d}' for n in range(31,41)}
assert {d['reading_id'] for d in data}==set(sm)
assert len({s['identifier'].lower() for s in sources})==10
assert all(s['source_format']=='PDF' for s in sources)
assert sum(s['pdf_pages'] for s in sources)==140
assert sum(len(s['visual_reviews']) for s in sources)==41
assert len(claims)==len(cm)==45 and 'text' not in claims[0]
assert sum(len(d['claims']) for d in data)==45
assert set(cm)=={f'C-B16-{n:03d}' for n in range(1,46)}
assert sum(s['evidence_role'].startswith('multi_') for s in sources)==5
assert sum(s['evidence_role'].startswith('general_') for s in sources)==4
assert sum(s['evidence_role'].startswith('single_') for s in sources)==1
local_sources=local_visuals=0;missing=[];register_missing=[]
for d in data:
 sid=d['reading_id'];s=sm[sid];p=Path(s['local_source_path'])
 note=(B/s['notes_path']).read_text(encoding='utf-8')
 assert not s['human_verified'] and s['verification_status']=='human_pending'
 assert s['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE'
 assert s['source_sha256'] in note and d['actual_title'] in note
 assert s['actual_version']==d['actual_version'] and s['evidence_role']==d['evidence_role']
 assert s['narrative_body_pages']==list(range(d['body_pages'][0],d['body_pages'][1]+1))
 assert all(1<=n<=s['pdf_pages'] for n in s['narrative_body_pages'])
 if p.exists():
  assert sha(p)==s['source_sha256'];local_sources+=1
  try:
   from pypdf import PdfReader
   assert len(PdfReader(p).pages)==s['pdf_pages']
  except ImportError:pass
 else:missing.append(str(p))
 for c in d['claims']:
  reg=cm[c['claim_id']]
  h=hashlib.sha256(' '.join(c['text'].split()).encode('utf-8')).hexdigest()
  assert c['claim_text_sha256']==reg['claim_text_sha256']==h
  assert reg['source_id']==c['source_id']==s['source_id']
  assert reg['reading_id']==sid and reg['note_path']==s['notes_path']
  assert c['text'] in note and c['claim_id'] in note and c['locator']
  assert c['pages'] and all(1<=n<=s['pdf_pages'] for n in c['pages'])
  assert reg['pdf_pages']==';'.join(map(str,c['pages']))
  assert reg['human_verified']=='False'
 assert set(d['visual_pages'])=={v['pdf_page'] for v in s['visual_reviews']}
 for v in s['visual_reviews']:
  assert 1<=v['pdf_page']<=s['pdf_pages'] and v['status']=='VISUALLY_INSPECTED'
  p=Path(v['local_path'])
  if p.exists():assert sha(p)==v['sha256'];local_visuals+=1
  else:missing.append(str(p))
 identity=read(B/'metadata'/(sid+'_IDENTITY.json'))
 assert identity['source_sha256']==s['source_sha256'] and not identity['human_verified']
 assert not identity['formal_version_text_compared']
assert len(list(B.glob('READING_S*_CN.md')))==10
assert len(list((B/'metadata').glob('*_IDENTITY.json')))==10
crossrefs=list((B/'metadata').glob('*_CROSSREF.json'))
assert len(crossrefs)==4
for p in crossrefs:
 z=read(p);s=sm[p.name.split('_')[0]]
 title=s['related_formal_title'] if s['reading_id']=='S037' else s['title']
 identifier=s['related_formal_doi'] if s['reading_id']=='S037' else s['identifier']
 assert norm(z['title'][0])==norm(title) and z['DOI'].lower()==identifier.lower()
assert read(B/'metadata/S037_IDENTITY.json')['actual_report_year'] is None
assert not read(B/'metadata/S038_IDENTITY.json')['author_order_resolved']
assert read(B/'metadata/S035_IDENTITY.json')['formal_conference_id'] is None
for sid,v in {'S031':'2607.26570v1','S033':'2504.00225v3','S034':'2201.10399v1','S035':'1707.01185v1','S036':'2309.08050v1','S040':'2103.12614v1'}.items():
 assert sm[sid]['arxiv_actual_version']==v
for p in B.glob('*.md'):
 for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if target.startswith(('http:','https:','#')):continue
  q=p.parent/target
  if target=='VALIDATION_REPORT.json' and '--write-report' in sys.argv:continue
  assert q.is_file(),(p.name,target)
  if 'C-B16-' in label:
   first=int(re.search(r'C-B16-(\d{3})',label).group(1))
   nums=[int(n) for n in re.findall(r'(?<!\d)(\d{3})(?!\d)',label)]
   if '至' in label:nums=list(range(first,nums[-1]+1))
   for n in nums:
    cid=f'C-B16-{n:03d}';assert cid in cm and cid in q.read_text(encoding='utf-8'),(p.name,cid,target)
pool=csvread(B/'READING_STATUS_80_AFTER_B16.csv')
prev=csvread(B.parent/'B15_20261020/READING_STATUS_80_AFTER_B15.csv')
assert len(pool)==80
assert sum(r['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for r in pool)==20
assert sum(r['reading_status']=='NOT_CLOSE_READ' for r in pool)==60
for now,old in zip(pool,prev):
 for k in old:
  if k!='note_path':assert now[k]==old[k],(now['pool_id'],k)
 if old['note_path']:
  assert now['note_path']==posixpath.normpath('../B15_20261020/'+old['note_path'])
  assert (B/now['note_path']).is_file()
supp=csvread(B/'SUPPLEMENT_READING_REGISTER_B16.csv')
assert len(supp)==40 and {s['supplement_id'] for s in supp}=={f'S{n:03d}' for n in range(1,41)}
assert sum(s['batch']=='B16_20261020' for s in supp)==10
for s in supp:assert (B/s['note_path']).is_file()
prev_supp=csvread(B.parent/'B15_20261020/SUPPLEMENT_READING_REGISTER_B15.csv')
for now,old in zip(supp[:30],prev_supp):
 for k in old:
  if k!='note_path':assert now[k]==old[k]
assert status['original_pool_close_read_this_batch']==0 and status['original_pool_close_read_cumulative']==20
assert status['original_pool_remaining']==60
assert status['topic_supplement_close_read_this_batch']==10 and status['topic_supplement_close_read_cumulative']==40
assert status['B11_through_B16_close_read_records']==60
assert status['pdf_files_acquired_and_read']==10 and status['pdf_total_pages']==140
assert status['actual_visual_page_count']==41 and status['claim_count']==45
assert not status['manuscript_modified'] and not status['human_verified'] and not status['submission_ready']
assert status['multi_spacecraft_primary_papers']==5 and status['general_or_cross_domain_foundation_papers']==4
assert status['single_controlled_spacecraft_foundation_papers']==1
dedup=read(B/'DEDUP_CHECK.json')
assert not dedup['matches'] and not dedup['prior_source_matches']
assert dedup['prior_B11_through_B15_sources_checked']==50
registers_rechecked=0
for reg in dedup['registers']:
 p=Path(reg['path'])
 if p.exists():
  assert sha(p)==reg['sha256'];registers_rechecked+=1
  t=p.read_text(encoding='utf-8-sig')
  for s in sources:
   assert not any(i.lower() in t.lower() for i in ids(s))
   for title in [s['title'],s.get('related_formal_title')]:
    if title:assert norm(title) not in norm(t)
 else:register_missing.append(str(p))
prior_count=0
for prevbatch in [f'B{n:02d}_20261020' for n in range(11,16)]:
 for old in read(B.parent/prevbatch/f'SOURCE_MANIFEST_{prevbatch[:3]}.json')['sources']:
  prior_count+=1;ot=old.get('title',old.get('actual_title',''))
  oi=[str(old.get(k,'')).lower() for k in ['identifier','actual_identifier','formal_doi','related_formal_doi']]
  for s in sources:
   assert not any(i.lower() in oi for i in ids(s))
   for title in [s['title'],s.get('related_formal_title')]:
    if title:assert norm(title)!=norm(ot)
assert prior_count==50
acq=read(B/'ACQUISITION_LOG.json')
assert set(acq['selected_source_ids'])==set(sm)
assert len(acq['successful_or_last_attempt_records'])==10
for a in acq['successful_or_last_attempt_records']:
 assert a['sha256']==sm[a['id']]['source_sha256']
prefix='review_writing/evidence/reading_batches/B16_20261020/'
delta=git('diff','--name-only',manifest['base_commit']).decode().splitlines()
outside=[x for x in delta if not x.startswith(prefix)];assert not outside,outside
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(x.startswith(prefix) for x in untracked)
baseline='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert sha(R/baseline)=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
assert hashlib.sha256(git('show',manifest['base_commit']+':'+baseline)).hexdigest()==sha(R/baseline)
inherited=[]
for prevbatch in [f'B{n:02d}_20261020' for n in range(11,16)]:
 paths=git('ls-tree','-r','--name-only',manifest['base_commit'],'--','review_writing/evidence/reading_batches/'+prevbatch).decode().splitlines()
 for rel in paths:assert hashlib.sha256(git('show',manifest['base_commit']+':'+rel)).hexdigest()==sha(R/rel)
 inherited+=paths
files=[p for p in B.rglob('*') if p.is_file()]
assert not [p for p in files if p.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.txt','.xml','.pyc']]
report=dict(status='PASS' if not missing and not register_missing else 'PACKAGE_PASS_EXTERNAL_RECHECK_INCOMPLETE',batch='B16_20261020',sources=10,claims=45,pdf_pages=140,local_original_source_hashes_checked=local_sources,local_visual_hashes_checked=local_visuals,missing_local_files=missing,original80_pool_after_batch={'close_read':20,'not_close_read':60},separate_topic_supplements_cumulative=40,B11_through_B16_close_read_records=60,prior_B11_through_B15_inherited_files_unchanged=len(inherited),dedup_register_hashes_rechecked=registers_rechecked,dedup_registers_not_available=register_missing,version_and_author_conflicts_preserved=True,manuscript_sha256_unchanged=sha(R/baseline),outside_batch_tracked_changes=outside,human_verified=False,scope='File identity, evidence links, locators, counting and change scope only; no reproduction, proof or scientific correctness certificate')
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
