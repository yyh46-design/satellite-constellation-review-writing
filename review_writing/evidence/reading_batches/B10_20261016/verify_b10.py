"""Check B10 records and immutable baselines; no downloading, rewriting or science."""
from pathlib import Path
import csv,hashlib,json,shutil,subprocess

D=Path(__file__).resolve().parent
R=D.parents[3]
G=shutil.which('git') or r'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe'
BASE='2f82af74406caa0c840e1bba763bbda2c7d51fdf'
FROZEN='51be6a1326e8c615ea24f80f1887f16a2e7b02fc'
PREFIX='review_writing/evidence/reading_batches/B10_20261016/'
def git(*a): return subprocess.check_output([G,'-C',str(R),*a])
def read(n): return json.loads((D/n).read_text(encoding='utf-8'))
def sha(b): return hashlib.sha256(b).hexdigest()
def rows(n):
 with (D/n).open(encoding='utf-8-sig',newline='') as f: return list(csv.DictReader(f))

manifest=read('SHA256_MANIFEST.json')
actual=sorted(p.name for p in D.iterdir() if p.is_file())
assert actual==sorted(manifest['expected_local_commit_files']),actual
assert all(p.is_file() for p in D.iterdir()),'Unexpected directory'
assert len(manifest['files_excluding_manifest'])==len(actual)-1
for x in manifest['files_excluding_manifest']:
 b=(D/x['path']).read_bytes()
 assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path']
 assert b'\r\n' not in b,'All B10 files must retain LF'
 assert not b.startswith(b'\xef\xbb\xbf') or x['path'].endswith('.csv')
assert all(p.suffix.lower() not in {'.pdf','.png','.jpg','.docx','.xlsx'} for p in D.iterdir())

baseline=git('ls-tree','-r','--name-only',BASE).decode().splitlines()
assert len(baseline)==434,len(baseline)
changed=git('diff','--name-only',BASE).decode().splitlines()
assert all(x.startswith(PREFIX) for x in changed),changed
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(x.startswith(PREFIX) for x in untracked),untracked
for p in ['review_writing/manuscripts/v1.9/REVIEW_CN_v1.9.md','review_writing/manuscripts/v2.1-cn/REVIEW_CN_v2.1.md']:
 assert git('show',BASE+':'+p)==git('show','HEAD:'+p)
 assert not git('diff',BASE,'--',p)
v19='review_writing/manuscripts/v1.9/REVIEW_CN_v1.9.md'
assert sha(git('show',FROZEN+':'+v19))=='0b9f3f6f6b8d3c13af97f25d7baf3dac6dc18ecad8614e182633e12b6e3bbc69'
assert git('show',BASE+':'+v19)==git('show',FROZEN+':'+v19)

sources=read('SOURCE_MANIFEST_B10.json')['sources']
ids={f'ALT{i:02d}' for i in range(1,12)}
assert len(sources)==11 and {x['id'] for x in sources}==ids
assert sum(bool(x['local_pdf']) for x in sources)==10
assert sum(bool(x['matches_original_121']) for x in sources)==1
assert next(x for x in sources if x['id']=='ALT08')['matches_original_121']==[119]
assert not any(x['all_pages_all_proofs_read'] or x['human_verified'] or x['formal_version_parity_closed'] for x in sources)
viewed=[]
local_files_present=0
for x in sources:
 if x['local_pdf']:
  p=Path(x['local_pdf'])
  if p.exists():
   b=p.read_bytes();assert b.startswith(b'%PDF-') and sha(b)==x['pdf_sha256'] and len(b)==x['pdf_bytes']
   local_files_present+=1
  assert all(1<=p<=x['pdf_pages'] for p in x['read_pages']+x['visual_pages'])
 else:
  assert x['id']=='ALT10' and x['pdf_pages'] is None and x['pdf_sha256'] is None
  assert Path(x['body_capture_path']).exists()
  assert sha(Path(x['body_capture_path']).read_bytes())==x['body_capture_sha256']
 for v in x['actual_visual_checks']:
  assert v['visually_reviewed'] and not v['human_verified']
  p=Path(v['png']);assert p.exists() and sha(p.read_bytes())==v['sha256']
  viewed.append((x['id'],v['physical_page']))
assert len(set(viewed))==24
assert len(rows('SOURCE_ACCESS_REGISTER.csv'))==11
matrix=rows('REPLACEMENT_DECISION_MATRIX.csv')
assert len(matrix)==14
assert {int(x['原来源编号']) for x in matrix}=={33,59,63,75,77,79,80,112,42,44,53,74,76,121}
assert all(x['原缺口关闭']=='False' and x['正文已应用']=='False' for x in matrix)
deps=rows('CLAIM_DEPENDENCY_MAP.csv')
assert len(deps)==33 and {x['稿件版本'] for x in deps}=={'v1.9','v2.1-cn'}
for x in deps:
 lines=git('show',BASE+':'+x['稿件路径']).decode('utf-8').splitlines()
 assert lines[int(x['行号'])-1]==x['原段落或表格']
checks=read('CLAIM_CHECKS_B10.json')['claims']
assert len(checks)==44 and len({x['claim_id'] for x in checks})==44
assert {x['candidate_id'] for x in checks}==ids
assert all(x['source_sha256'] and x['locator'] and not x['human_verified'] and not x['reproduced'] for x in checks)

status=read('CUMULATIVE_READING_STATUS.json')
assert len(set(status['original_academic_targeted_refs']))==status['original_academic_targeted_count']==77
assert status['original_academic_remaining_count']==34
assert status['additional_candidate_papers_outside_original_catalog']==status['additional_candidate_targeted_body_reads']==10
assert status['existing_catalog_paper_reread_refs']==[119]
assert status['original_plus_external_targeted_body_paper_count']==87
assert status['original_gap_closures']==status['formal_version_pairs_closed']==0
assert not status['submission_ready'] and not status['manuscript_modified'] and not status['GitHub_push_performed']
assert not read('ACCESS_OBSERVATIONS.json')['access_bypass_used']

indexed=git('ls-files','--',PREFIX).decode().splitlines()
if indexed:
 assert {x.removeprefix(PREFIX) for x in indexed}==set(actual)
 for p in indexed:
  assert git('show',':'+p)==(R/p).read_bytes(),p
print(json.dumps({'result':'PASS','parent_commit':BASE,'local_commit_file_count':len(actual),'historical_tracked_files_unchanged':434,'frozen_v19_unchanged':True,'manuscripts_unchanged':True,'candidate_papers':11,'new_candidates_outside_original_catalog':10,'existing_paper_reread_refs':[119],'candidate_papers_with_pdf':10,'selected_local_PDF_hashes_currently_verified':local_files_present,'actual_visual_pages':24,'claim_checks':44,'citation_context_rows':33,'original_targeted':77,'original_remaining':34,'original_plus_external_targeted':87,'original_gap_closures':0,'staged_or_committed_blob_check':bool(indexed)},ensure_ascii=False,indent=2))
