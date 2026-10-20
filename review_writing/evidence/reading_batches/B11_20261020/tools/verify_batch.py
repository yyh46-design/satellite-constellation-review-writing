"""Read-only evidence integrity audit; --write-report writes only audit/hash records."""
import sys,json,csv,hashlib,re,subprocess
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
BATCH=Path(__file__).resolve().parent.parent
REPO=BATCH.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normalized_sha(t):return hashlib.sha256(' '.join(t.split()).encode('utf-8')).hexdigest()
content=json.loads((BATCH/'READING_CONTENT.json').read_text(encoding='utf-8'))
manifest=json.loads((BATCH/'SOURCE_MANIFEST_B11.json').read_text(encoding='utf-8'))
status=json.loads((BATCH/'BATCH_STATUS.json').read_text(encoding='utf-8'))
sources=manifest['sources']; byid={x['pool_id']:x for x in sources}
assert len(sources)==len(content)==10
assert len({x['formal_doi'].lower() for x in sources})==10
assert all(not x['human_verified'] for x in sources)
assert sum(x['pdf_pages'] for x in sources)==228
assert sum(len(x['visual_reviews']) for x in sources)==23
with (BATCH/'CLAIM_EVIDENCE_B11.csv').open(encoding='utf-8-sig',newline='') as f:claims=list(csv.DictReader(f))
lookup={x['claim_id']:x for x in claims}
assert len(claims)==len(lookup)==42
pdfs_checked=0;visuals_checked=0
for r in content:
 s=byid[r['pool_id']];pdf=Path(s['local_pdf_path'])
 if pdf.is_file():assert sha(pdf)==s['pdf_sha256'];pdfs_checked+=1
 assert s['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE'
 assert s['narrative_body_pages']==list(range(r['body_pages'][0],r['body_pages'][1]+1))
 assert all(1<=n<=s['pdf_pages'] for n in s['narrative_body_pages'])
 notes=(BATCH/s['notes_path']).read_text(encoding='utf-8')
 assert r['actual_title'] in notes and s['pdf_sha256'] in notes
 for c in r['claims']:
  registered=lookup[c['claim_id']]
  assert c['claim_text_sha256']==registered['claim_text_sha256']==normalized_sha(c['text'])
  assert c['text'] in notes and c['claim_id'] in notes
  assert all(1<=n<=s['pdf_pages'] for n in c['pages'])
  assert c['source_id']==registered['source_id']==s['source_id']
 for v in s['visual_reviews']:
  image=Path(v['local_path'])
  if image.is_file():assert sha(image)==v['sha256'];visuals_checked+=1
  assert v['pdf_page'] in r['visual_pages']
with (BATCH/'READING_STATUS_80_AFTER_B11.csv').open(encoding='utf-8-sig',newline='') as f:pool=list(csv.DictReader(f))
assert len(pool)==80
assert sum(x['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE' for x in pool)==10
assert sum(x['reading_status']=='NOT_CLOSE_READ' for x in pool)==70
assert {x['pool_id'] for x in pool if x['reading_status']=='AI_BODY_CLOSE_READ_COMPLETE'}==set(byid)
allfiles=[x for x in BATCH.rglob('*') if x.is_file()]
assert not [x for x in allfiles if x.suffix.lower() in ['.pdf','.png','.jpg','.txt']]
for p in BATCH.glob('*.md'):
 for path in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if not path.startswith(('https:','http:','#')):
   if path=='VALIDATION_REPORT.json' and '--write-report' in sys.argv:continue
   assert (p.parent/path).is_file(),(p.name,path)
git=Path(r'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe')
tracked_delta=subprocess.check_output([str(git),'-C',str(REPO),'diff','--name-only',manifest['base_commit']],text=True,encoding='utf-8').splitlines()
outside=[x for x in tracked_delta if not x.startswith('review_writing/evidence/reading_batches/B11_20261020/')]
assert not outside,outside
baseline_manuscript='review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
basebytes=subprocess.check_output([str(git),'-C',str(REPO),'show',manifest['base_commit']+':'+baseline_manuscript])
assert hashlib.sha256(basebytes).hexdigest()==sha(REPO/baseline_manuscript)
report={'status':'PASS','batch':'B11_20261020','sources':10,'claims':42,'local_pdf_hashes_checked':pdfs_checked,'local_visual_hashes_checked':visuals_checked,'selected_preprint_versions':3,'pool_after_batch':{'close_read':10,'not_close_read':70},'manuscript_sha256_unchanged':sha(REPO/baseline_manuscript),'outside_batch_tracked_changes':outside,'human_verified':False,'scope':'file identity, evidence linkage, locators and scope consistency; no reproduction or scientific correctness certificate'}
if '--write-report' in sys.argv:
 (BATCH/'VALIDATION_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 hashes={str(x.relative_to(BATCH)).replace('\\','/'):sha(x) for x in BATCH.rglob('*') if x.is_file() and x.name!='SHA256_MANIFEST.json'}
 (BATCH/'SHA256_MANIFEST.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2),encoding='utf-8')
else:
 hashes=json.loads((BATCH/'SHA256_MANIFEST.json').read_text(encoding='utf-8'))
 for rel,digest in hashes.items():assert sha(BATCH/rel)==digest,rel
 assert set(hashes)=={str(x.relative_to(BATCH)).replace('\\','/') for x in BATCH.rglob('*') if x.is_file() and x.name!='SHA256_MANIFEST.json'}
 report['package_hashes_checked']=len(hashes)
print(json.dumps(report,ensure_ascii=False,indent=2))
