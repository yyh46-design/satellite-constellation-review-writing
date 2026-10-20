"""Evidence/file integrity only; no scientific experiment or proof validation.

Use --write-report to create the audit and hash manifest. Source PDFs/XML/images
are kept outside Git. When sources are absent, report that limitation explicitly.
"""
import sys,json,csv,hashlib,re,subprocess
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
BATCH=Path(__file__).resolve().parent.parent
REPO=BATCH.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normalized_sha(t):return hashlib.sha256(' '.join(t.split()).encode('utf-8')).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args])
content=json.loads((BATCH/'READING_CONTENT.json').read_text(encoding='utf-8'))
manifest=json.loads((BATCH/'SOURCE_MANIFEST_B12.json').read_text(encoding='utf-8'))
status=json.loads((BATCH/'BATCH_STATUS.json').read_text(encoding='utf-8'))
sources=manifest['sources'];byid={x['pool_id']:x for x in sources}
assert len(sources)==len(content)==len(byid)==10
assert len({x['formal_doi'].lower() for x in sources})==10
assert all(not x['human_verified'] for x in sources)
assert sum(x['pdf_pages'] for x in sources)==167
assert sum(x['source_format']=='PDF' for x in sources)==9
assert sum(x['source_format']=='JATS_XML' for x in sources)==1
assert sum(len(x['visual_reviews']) for x in sources)==18
with (BATCH/'CLAIM_EVIDENCE_B12.csv').open(encoding='utf-8-sig',newline='') as f:claims=list(csv.DictReader(f))
lookup={x['claim_id']:x for x in claims};assert len(claims)==len(lookup)==43
originals_checked=0;visuals_checked=0;missing=[]
for r in content:
 s=byid[r['pool_id']];p=Path(s['local_source_path'])
 if p.is_file():assert sha(p)==s['source_sha256'];originals_checked+=1
 else:missing.append(str(p))
 assert s['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE'
 notes=(BATCH/s['notes_path']).read_text(encoding='utf-8')
 assert r['actual_title'] in notes and s['source_sha256'] in notes
 if s['source_format']=='PDF':
  assert s['narrative_body_pages']==list(range(r['body_pages'][0],r['body_pages'][1]+1))
  assert all(1<=n<=s['pdf_pages'] for n in s['narrative_body_pages'])
 else:
  assert s['pdf_pages']==0 and r['body_pages']==r['visual_pages']==[]
  assert s['xml_body_sections']==5 and s['xml_appendix_read']
 for c in r['claims']:
  reg=lookup[c['claim_id']]
  assert c['claim_text_sha256']==reg['claim_text_sha256']==normalized_sha(c['text'])
  assert c['text'] in notes and c['claim_id'] in notes
  assert all(1<=n<=s['pdf_pages'] for n in c['pages'])
  if s['source_format']=='JATS_XML':assert not c['pages'] and c['locator'].startswith('XML ')
  assert c['source_id']==reg['source_id']==s['source_id']
 for v in s['visual_reviews']:
  p=Path(v['local_path'])
  if p.is_file():assert sha(p)==v['sha256'];visuals_checked+=1
  else:missing.append(str(p))
  assert v['pdf_page'] in r['visual_pages']
with (BATCH/'READING_STATUS_80_AFTER_B12.csv').open(encoding='utf-8-sig',newline='') as f:pool=list(csv.DictReader(f))
assert len(pool)==80
assert sum(x['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for x in pool)==20
assert sum(x['reading_status']=='NOT_CLOSE_READ' for x in pool)==60
assert {x['pool_id'] for x in pool if x['batch']=='B12_20261020'}==set(byid)
with (BATCH.parent/'B11_20261020/READING_STATUS_80_AFTER_B11.csv').open(encoding='utf-8-sig',newline='') as f:prev=list(csv.DictReader(f))
previous_ids={x['pool_id'] for x in prev if x['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE'}
assert len(previous_ids)==10 and not previous_ids.intersection(byid)
assert {x['pool_id'] for x in pool if x['batch']=='B11_20261020'}==previous_ids
for x in pool:
 if x['note_path']:assert (BATCH/x['note_path']).is_file()
files=[x for x in BATCH.rglob('*') if x.is_file()]
assert not [x for x in files if x.suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.txt','.xml']]
for p in BATCH.glob('*.md'):
 t=p.read_text(encoding='utf-8')
 for path in re.findall(r'\]\(([^)]+)\)',t):
  if not path.startswith(('https:','http:','#')):
   if path=='VALIDATION_REPORT.json' and '--write-report' in sys.argv:continue
   assert (p.parent/path).is_file(),(p.name,path)
 for cid in re.findall(r'C-B12-\d{3}',t):assert cid in lookup,(p.name,cid)
delta=git('diff','--name-only',manifest['base_commit']).decode('utf-8').splitlines()
outside=[x for x in delta if not x.startswith('review_writing/evidence/reading_batches/B12_20261020/')]
assert not outside,outside
untracked=git('ls-files','--others','--exclude-standard').decode('utf-8').splitlines()
assert all(x.startswith('review_writing/evidence/reading_batches/B12_20261020/') for x in untracked)
baseline='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert hashlib.sha256(git('show',manifest['base_commit']+':'+baseline)).hexdigest()==sha(REPO/baseline)
assert sha(REPO/baseline)=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
# Compare every inherited B11 file against its frozen parent blob.
prior=git('ls-tree','-r','--name-only',manifest['base_commit'],'--','review_writing/evidence/reading_batches/B11_20261020').decode('utf-8').splitlines()
for path in prior:assert hashlib.sha256(git('show',manifest['base_commit']+':'+path)).hexdigest()==sha(REPO/path)
report=dict(status='PASS' if not missing else 'PACKAGE_PASS_LOCAL_SOURCE_RECHECK_INCOMPLETE',batch='B12_20261020',sources=10,claims=43,local_original_source_hashes_checked=originals_checked,local_visual_hashes_checked=visuals_checked,missing_local_files=missing,source_formats={'PDF':9,'JATS_XML':1},selected_preprint_versions=3,pool_after_batch={'close_read':20,'not_close_read':60},B11_inherited_files_unchanged=len(prior),manuscript_sha256_unchanged=sha(REPO/baseline),outside_batch_tracked_changes=outside,human_verified=False,scope='File identity, evidence links, native locators and change scope only; no reproduction, proof or scientific correctness certificate')
if '--write-report' in sys.argv:
 (BATCH/'VALIDATION_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 hashes={str(x.relative_to(BATCH)).replace('\\','/'):sha(x) for x in BATCH.rglob('*') if x.is_file() and x.name!='SHA256_MANIFEST.json'}
 (BATCH/'SHA256_MANIFEST.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
else:
 hashes=json.loads((BATCH/'SHA256_MANIFEST.json').read_text(encoding='utf-8'))
 for rel,h in hashes.items():assert sha(BATCH/rel)==h,rel
 assert set(hashes)=={str(x.relative_to(BATCH)).replace('\\','/') for x in BATCH.rglob('*') if x.is_file() and x.name!='SHA256_MANIFEST.json'}
 report['package_hashes_checked']=len(hashes)
print(json.dumps(report,ensure_ascii=False,indent=2))
