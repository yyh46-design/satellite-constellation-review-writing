"""Verify the B09 evidence package without downloading or re-reading sources."""
from pathlib import Path
import csv,hashlib,json,subprocess,shutil

D=Path(__file__).resolve().parent
R=D.parents[3]
G=shutil.which('git') or r'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe'
BASE='33b31ca40685f7c81bc579995cdccc2ce403f088'
FROZEN='51be6a1326e8c615ea24f80f1887f16a2e7b02fc'
PREFIX='review_writing/evidence/reading_batches/B09_20261016/'
def git(*args):return subprocess.check_output([G,'-C',str(R),*args])
def read(name):return json.loads((D/name).read_text(encoding='utf-8'))
def sha(b):return hashlib.sha256(b).hexdigest()

manifest=read('SHA256_MANIFEST.json')
actual=sorted(p.name for p in D.iterdir() if p.is_file())
expected=sorted(manifest['expected_published_files'])
assert actual==expected,(actual,expected)
assert all(p.is_file() for p in D.iterdir()),'Unexpected subdirectory'
for item in manifest['published_files_excluding_manifest']:
 p=D/item['path'];b=p.read_bytes()
 assert len(b)==item['bytes'] and sha(b)==item['sha256'],item['path']
assert len(manifest['published_files_excluding_manifest'])==len(actual)-1
baseline=git('ls-tree','-r','--name-only',BASE).decode().splitlines()
assert len(baseline)==420,len(baseline)
changed=git('diff','--name-only',BASE).decode().splitlines()
assert all(x.startswith(PREFIX) for x in changed),changed
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(x.startswith(PREFIX) for x in untracked),untracked
v19='review_writing/manuscripts/v1.9/REVIEW_CN_v1.9.md'
frozen=git('show',FROZEN+':'+v19)
assert sha(frozen)=='0b9f3f6f6b8d3c13af97f25d7baf3dac6dc18ecad8614e182633e12b6e3bbc69'
assert git('show',BASE+':'+v19)==frozen
sources=read('SOURCE_ACCESS_DETAILS.json')['sources']
refs={42,44,53,74,76,121,75,77,79,80,112,33,59,63}
assert {x['reference_number'] for x in sources}==refs and len(sources)==14
assert all(x['publication_metadata']['DOI'].lower()==x['doi'].lower() for x in sources)
assert all(not x['formal_version_parity_closed'] and not x['new_paper_body_reading'] for x in sources)
assert all(not x['new_complete_target_paper_PDFs'] for x in sources)
existing=[a for x in sources for a in x['existing_local_PDFs_rehashed']]
assert len(existing)==7 and all(x['recorded_hash_matches_current'] for x in existing)
with (D/'SOURCE_ACCESS_REGISTER.csv').open(encoding='utf-8-sig',newline='') as f:
 access=list(csv.DictReader(f))
assert len(access)==14 and {int(x['编号']) for x in access}==refs
with (D/'CLAIM_DEPENDENCY_MAP.csv').open(encoding='utf-8-sig',newline='') as f:
 deps=list(csv.DictReader(f))
assert {x['版本'] for x in deps}=={'v1.9','v2.1-cn'}
assert {int(x['来源编号']) for x in deps}==refs
for x in deps:
 lines=git('show',BASE+':'+x['稿件路径']).decode('utf-8').splitlines()
 assert 1<=int(x['行号'])<=len(lines)
status=read('CUMULATIVE_READING_STATUS.json')
assert status['after_B09_targeted_count']==len(set(status['after_B09_targeted_refs']))==77
assert status['remaining_academic_count']==34 and status['academic_total']==111
assert status['after_B09_targeted_count']+status['remaining_academic_count']==111
assert set(status['full_text_unavailable_refs'])=={75,77,79,80,112}
assert status['B09_new_target_paper_PDF_count']==status['B09_new_target_paper_body_read_count']==0
pairs=read('VERSION_COMPARISON_QUEUE.json')['pairs']
assert len(pairs)==6 and not any(x['pair_closed'] for x in pairs)
sup=read('SUPPLEMENTARY_MATERIALS_REGISTER.json')
assert sup['local_recovered_pdf_count']==4 and sup['local_recovered_workbook_count']==1
assert len(sup['materials'])==5 and all(x['repository_md5_matches_actual'] and x['repository_size_matches_actual'] for x in sup['materials'])
assert len(sup['actual_visual_checks'])==7 and all(x['actually_visually_inspected'] for x in sup['actual_visual_checks'])
assert not sup['paper_PDF_in_package'] and not sup['third_party_files_uploaded']
assert not any(p.suffix.lower() in {'.pdf','.docx','.xlsx','.png','.jpg'} for p in D.iterdir())
assert all(not x['human_verified'] for x in sources) and not status['submission_ready']
print(json.dumps({'result':'PASS','base_commit':BASE,'published_file_count':len(actual),'historical_tracked_paths_unchanged':420,'frozen_v19_unchanged':True,'priority_source_count':14,'new_target_paper_PDF_count':0,'new_paper_body_read_count':0,'supplementary_PDF_count':4,'actual_supplementary_page_count':7,'citation_context_rows':len(deps),'targeted_body_total':77,'remaining_academic_total':34,'closed_formal_pairs':0,'historical_changes':[]},ensure_ascii=False,indent=2))
