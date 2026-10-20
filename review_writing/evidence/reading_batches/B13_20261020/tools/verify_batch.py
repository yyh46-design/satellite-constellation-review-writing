"""Verify file identity, source/claim binding and publication scope only.

Not a scientific reproduction, proof audit or safety certificate.
Run with --write-report once; ordinary runs check the frozen package hashes.
"""
import json,csv,re,sys,hashlib,subprocess
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
B=Path(__file__).resolve().parent.parent;R=B.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(R),*a])
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def csvread(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
manifest=read(B/'SOURCE_MANIFEST_B13.json');data=read(B/'READING_CONTENT.json');status=read(B/'BATCH_STATUS.json')
sources=manifest['sources'];sm={s['supplement_id']:s for s in sources};claims=csvread(B/'CLAIM_EVIDENCE_B13.csv');cm={c['claim_id']:c for c in claims}
assert len(sources)==len(data)==len(sm)==10
assert len({s['identifier'].lower() for s in sources})==10
assert sum(s['pdf_pages'] for s in sources)==181
assert sum(len(s['visual_reviews']) for s in sources)==24
assert len(claims)==len(cm)==43 and 'text' not in claims[0]
assert all(not s['human_verified'] and s['verification_status']=='human_pending' for s in sources)
local_sources=local_visuals=0;missing=[]
for d in data:
 s=sm[d['supplement_id']];p=Path(s['local_source_path']);note=(B/s['notes_path']).read_text(encoding='utf-8')
 assert s['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE'
 if p.exists():
  assert sha(p)==s['source_sha256'];local_sources+=1
  try:
   from pypdf import PdfReader
   assert len(PdfReader(p).pages)==s['pdf_pages']
  except ImportError:pass
 else:missing.append(str(p))
 assert s['source_sha256'] in note and d['actual_title'] in note
 assert s['narrative_body_pages']==list(range(d['body_pages'][0],d['body_pages'][1]+1))
 assert all(1<=n<=s['pdf_pages'] for n in s['narrative_body_pages'])
 for c in d['claims']:
  reg=cm[c['claim_id']];h=hashlib.sha256(' '.join(c['text'].split()).encode()).hexdigest()
  assert c['claim_text_sha256']==reg['claim_text_sha256']==h
  assert reg['source_id']==c['source_id']==s['source_id']
  assert reg['supplement_id']==s['supplement_id']
  assert reg['note_path']==s['notes_path']
  assert c['text'] in note and c['claim_id'] in note
  assert c['locator'] and c['pages'] and all(1<=p<=s['pdf_pages'] for p in c['pages'])
  assert reg['pdf_pages']==';'.join(map(str,c['pages']))
 for v in s['visual_reviews']:
  assert v['pdf_page'] in d['visual_pages'] and v['status']=='VISUALLY_INSPECTED'
  p=Path(v['local_path'])
  if p.exists():assert sha(p)==v['sha256'];local_visuals+=1
  else:missing.append(str(p))
for p in B.glob('*.md'):
 t=p.read_text(encoding='utf-8')
 for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',t):
  if target.startswith(('http:','https:','#')):continue
  q=p.parent/target
  if target=='VALIDATION_REPORT.json' and '--write-report' in sys.argv:continue
  assert q.is_file(),(p.name,target)
  if 'C-B13-' in label:
   first=int(re.search(r'C-B13-(\d{3})',label).group(1))
   tails=[int(n) for n in re.findall(r'(?<!\d)(\d{3})(?!\d)',label)]
   nums=list(range(first,tails[-1]+1)) if '至' in label else tails
   for n in nums:
    cid=f'C-B13-{n:03d}';assert cid in cm and cid in q.read_text(encoding='utf-8'),(p.name,cid,target)
pool=csvread(B/'READING_STATUS_80_AFTER_B13.csv');prev=csvread(B.parent/'B12_20261020/READING_STATUS_80_AFTER_B12.csv')
assert len(pool)==80
assert sum(x['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for x in pool)==20
assert sum(x['reading_status']=='NOT_CLOSE_READ' for x in pool)==60
for now,old in zip(pool,prev):
 for k in old:
  if k!='note_path':assert now[k]==old[k],(now['pool_id'],k)
 if now['note_path']:assert (B/now['note_path']).is_file()
supp=csvread(B/'SUPPLEMENT_READING_REGISTER_B13.csv')
assert len(supp)==10 and {s['supplement_id'] for s in supp}==set(sm)
assert status['original_pool_close_read_this_batch']==0 and status['original_pool_close_read_cumulative']==20
assert status['topic_supplement_close_read_this_batch']==10 and status['B11_B12_B13_close_read_records']==30
assert not status['manuscript_modified'] and not status['human_verified']
assert status['newer_version_pairing_pending']==['S008']
assert sm['S008']['identifier']=='arXiv:2504.20386v1' and sm['S008']['pdf_pages']==29
assert read(B/'metadata/S008_IDENTITY.json')['newer_version_read'] is False
assert sm['S010']['version_class']=='unversioned_author_preprint'
dedup=read(B/'DEDUP_CHECK.json');assert not dedup['matches']
assert dedup['prior_B11_B12_sources_checked']==20 and dedup['prior_B11_B12_title_or_identifier_duplicates']==0
prefix='review_writing/evidence/reading_batches/B13_20261020/'
delta=git('diff','--name-only',manifest['base_commit']).decode().splitlines()
outside=[x for x in delta if not x.startswith(prefix)];assert not outside,outside
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();assert all(x.startswith(prefix) for x in untracked)
baseline='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert sha(R/baseline)=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
assert hashlib.sha256(git('show',manifest['base_commit']+':'+baseline)).hexdigest()==sha(R/baseline)
inherited=[]
for prevbatch in ['B11_20261020','B12_20261020']:
 ps=git('ls-tree','-r','--name-only',manifest['base_commit'],'--','review_writing/evidence/reading_batches/'+prevbatch).decode().splitlines()
 for rel in ps:assert hashlib.sha256(git('show',manifest['base_commit']+':'+rel)).hexdigest()==sha(R/rel)
 inherited+=ps
files=[p for p in B.rglob('*') if p.is_file()]
assert not [p for p in files if p.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.txt','.xml','.pyc']]
report=dict(status='PASS' if not missing else 'PACKAGE_PASS_LOCAL_SOURCE_RECHECK_INCOMPLETE',batch='B13_20261020',sources=10,claims=43,pdf_pages=181,local_original_source_hashes_checked=local_sources,local_visual_hashes_checked=local_visuals,missing_local_files=missing,original80_pool_after_batch={'close_read':20,'not_close_read':60},separate_topic_supplements=10,prior_B11_B12_inherited_files_unchanged=len(inherited),manuscript_sha256_unchanged=sha(R/baseline),outside_batch_tracked_changes=outside,human_verified=False,scope='File identity, evidence links, locators, counting and change scope only; no reproduction, proof or scientific correctness certificate')
if '--write-report' in sys.argv:
 (B/'VALIDATION_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 hashes={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in B.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 (B/'SHA256_MANIFEST.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
else:
 hashes=read(B/'SHA256_MANIFEST.json')
 for rel,h in hashes.items():assert sha(B/rel)==h,rel
 assert set(hashes)=={str(p.relative_to(B)).replace('\\','/') for p in B.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 report['package_hashes_checked']=len(hashes)
print(json.dumps(report,ensure_ascii=False,indent=2))
