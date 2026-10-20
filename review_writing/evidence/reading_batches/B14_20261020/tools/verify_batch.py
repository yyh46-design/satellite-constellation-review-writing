"""Verify file identities, source/claim links, counting and change scope.

Not a proof audit, scientific reproduction or safety certificate.
--write-report freezes a report and package hashes; ordinary runs check them.
"""
import csv,hashlib,json,re,subprocess,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
B=Path(__file__).resolve().parent.parent;R=B.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def git(*args):return subprocess.check_output(['git','-C',str(R),*args])
def csvread(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
manifest=read(B/'SOURCE_MANIFEST_B14.json');data=read(B/'READING_CONTENT.json');status=read(B/'BATCH_STATUS.json')
sources=manifest['sources'];sm={s['supplement_id']:s for s in sources}
claims=csvread(B/'CLAIM_EVIDENCE_B14.csv');cm={c['claim_id']:c for c in claims}
assert len(sources)==len(data)==len(sm)==10
assert set(sm)=={f'S{n:03d}' for n in range(11,21)}
assert len({s['identifier'].lower() for s in sources})==10
assert sum(s['pdf_pages'] for s in sources)==124
assert sum(len(s['visual_reviews']) for s in sources)==29
assert len(claims)==len(cm)==47 and 'text' not in claims[0]
assert sum(len(d['claims']) for d in data)==47
assert set(cm)=={f'C-B14-{n:03d}' for n in range(1,48)}
assert all(not s['human_verified'] and s['verification_status']=='human_pending' for s in sources)
assert all(s['evidence_role'].startswith('single_') for sid,s in sm.items() if sid in ['S019','S020'])
assert sum(s['evidence_role'].startswith('multi_') for s in sources)==8
local_sources=local_visuals=0;missing=[]
for d in data:
 s=sm[d['supplement_id']];p=Path(s['local_source_path']);note=(B/s['notes_path']).read_text(encoding='utf-8')
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
  reg=cm[c['claim_id']];h=hashlib.sha256(' '.join(c['text'].split()).encode('utf-8')).hexdigest()
  assert c['claim_text_sha256']==reg['claim_text_sha256']==h
  assert reg['source_id']==c['source_id']==s['source_id']
  assert reg['supplement_id']==s['supplement_id'] and reg['note_path']==s['notes_path']
  assert c['text'] in note and c['claim_id'] in note
  assert c['locator'] and c['pages'] and all(1<=n<=s['pdf_pages'] for n in c['pages'])
  assert reg['pdf_pages']==';'.join(map(str,c['pages']))
 for v in s['visual_reviews']:
  assert v['pdf_page'] in d['visual_pages'] and v['status']=='VISUALLY_INSPECTED'
  p=Path(v['local_path'])
  if p.exists():assert sha(p)==v['sha256'];local_visuals+=1
  else:missing.append(str(p))
 identity=read(B/'metadata'/(s['supplement_id']+'_IDENTITY.json'))
 assert identity['source_sha256']==s['source_sha256'] and not identity['human_verified']
 assert not identity['formal_fulltext_compared']
for p in B.glob('*.md'):
 t=p.read_text(encoding='utf-8')
 for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',t):
  if target.startswith(('http:','https:','#')):continue
  q=p.parent/target
  if target=='VALIDATION_REPORT.json' and '--write-report' in sys.argv:continue
  assert q.is_file(),(p.name,target)
  if 'C-B14-' in label:
   first=int(re.search(r'C-B14-(\d{3})',label).group(1))
   nums=[int(n) for n in re.findall(r'(?<!\d)(\d{3})(?!\d)',label)]
   if '至' in label:nums=list(range(first,nums[-1]+1))
   for n in nums:
    cid=f'C-B14-{n:03d}';assert cid in cm and cid in q.read_text(encoding='utf-8'),(p.name,cid,target)
pool=csvread(B/'READING_STATUS_80_AFTER_B14.csv')
prev=csvread(B.parent/'B13_20261020/READING_STATUS_80_AFTER_B13.csv')
assert len(pool)==80
assert sum(x['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for x in pool)==20
assert sum(x['reading_status']=='NOT_CLOSE_READ' for x in pool)==60
for now,old in zip(pool,prev):
 for k in old:
  if k!='note_path':assert now[k]==old[k],(now['pool_id'],k)
 if now['note_path']:assert (B/now['note_path']).is_file()
supp=csvread(B/'SUPPLEMENT_READING_REGISTER_B14.csv')
assert len(supp)==20 and {s['supplement_id'] for s in supp}=={f'S{n:03d}' for n in range(1,21)}
assert sum(s['batch']=='B14_20261020' for s in supp)==10
for s in supp:assert (B/s['note_path']).is_file()
assert status['original_pool_close_read_this_batch']==0 and status['original_pool_close_read_cumulative']==20
assert status['topic_supplement_close_read_this_batch']==10 and status['topic_supplement_close_read_cumulative']==20
assert status['B11_B12_B13_B14_close_read_records']==40
assert not status['manuscript_modified'] and not status['human_verified']
assert status['single_controlled_spacecraft_foundation_papers']==2
assert sm['S014']['bibliographic_year']==2024 and sm['S014']['arxiv_actual_version']=='2412.10530v1'
assert sm['S017']['version_class']=='repository_preprint_v1'
assert len(read(B/'metadata/S019_IDENTITY.json')['unresolved_source_issues'])==3
dedup=read(B/'DEDUP_CHECK.json')
assert not dedup['matches'] and not dedup['prior_source_matches']
assert dedup['prior_B11_B12_B13_sources_checked']==30
registers_rechecked=0
for reg in dedup['registers']:
 p=Path(reg['path'])
 if p.exists():assert sha(p)==reg['sha256'];registers_rechecked+=1
prefix='review_writing/evidence/reading_batches/B14_20261020/'
delta=git('diff','--name-only',manifest['base_commit']).decode().splitlines()
outside=[x for x in delta if not x.startswith(prefix)];assert not outside,outside
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();assert all(x.startswith(prefix) for x in untracked)
baseline='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert sha(R/baseline)=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
assert hashlib.sha256(git('show',manifest['base_commit']+':'+baseline)).hexdigest()==sha(R/baseline)
inherited=[]
for prevbatch in ['B11_20261020','B12_20261020','B13_20261020']:
 paths=git('ls-tree','-r','--name-only',manifest['base_commit'],'--','review_writing/evidence/reading_batches/'+prevbatch).decode().splitlines()
 for rel in paths:assert hashlib.sha256(git('show',manifest['base_commit']+':'+rel)).hexdigest()==sha(R/rel)
 inherited+=paths
files=[p for p in B.rglob('*') if p.is_file()]
assert not [p for p in files if p.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.txt','.xml','.pyc']]
report=dict(status='PASS' if not missing else 'PACKAGE_PASS_LOCAL_SOURCE_RECHECK_INCOMPLETE',batch='B14_20261020',sources=10,claims=47,pdf_pages=124,local_original_source_hashes_checked=local_sources,local_visual_hashes_checked=local_visuals,missing_local_files=missing,original80_pool_after_batch={'close_read':20,'not_close_read':60},separate_topic_supplements_cumulative=20,B11_B12_B13_B14_close_read_records=40,prior_B11_B12_B13_inherited_files_unchanged=len(inherited),dedup_register_hashes_rechecked=registers_rechecked,manuscript_sha256_unchanged=sha(R/baseline),outside_batch_tracked_changes=outside,human_verified=False,scope='File identity, evidence links, locators, counting and change scope only; no reproduction, proof or scientific correctness certificate')
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
