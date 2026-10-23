"""Necessary manuscript/provenance consistency checks, not scientific approval."""
from pathlib import Path
import csv,hashlib,io,json,re,subprocess

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
BASE='b21a9ebe964b07d5c5986730c93b811fadfe1803'
BASE_DIR='review_writing/manuscripts/v3.5.3-cn'
PREFIX='review_writing/manuscripts/v3.5.4-cn/'
BRANCH='writing/constellation-review-v354-literature-synthesis-20261023'

def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()
def oldfile(name):return subprocess.check_output(['git','show',f'{BASE}:{BASE_DIR}/{name}'],cwd=ROOT)
def rows(path):return list(csv.DictReader(path.open(encoding='utf-8-sig')))
pattern=re.compile(r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]')
def citations(text):
    for m in pattern.finditer(text):
        ns=[]
        for p in m.group(1).split(','):
            q=re.split('[–—-]',p);ns.extend(range(int(q[0]),int(q[-1])+1))
        yield m,ns

text=(HERE/'REVIEW_CN_v3.5.4.md').read_text(encoding='utf-8')
body,bib=text.split('## 参考文献',1)
prior=oldfile('REVIEW_CN_v3.5.3.md').decode('utf-8');oldbody=prior.split('## 参考文献',1)[0]
old=list(csv.DictReader(io.StringIO(oldfile('references/REFERENCE_REGISTER_v3.5.3.csv').decode('utf-8-sig'))))
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.4.csv')
integration=rows(HERE/'references/SOURCE_INTEGRATION_v3.5.4.csv')
locations=rows(HERE/'references/CITATION_LOCATIONS_v3.5.4.csv')
selection=rows(HERE/'references/SOURCE_SELECTION_v3.5.4.csv')
bounds=rows(HERE/'references/SCIENTIFIC_BOUNDARIES_v3.5.4.csv')
byold={r['stable_id']:r for r in old};bynew={r['stable_id']:r for r in reg}
by_number={int(r['v354_number']):r for r in reg}
added=set(bynew)-set(byold)
checks={}
checks['same_title_five_chapters_and_3_1_to_3_6_domains']=(
 body.splitlines()[0]==oldbody.splitlines()[0] and
 re.findall(r'^## [1-5] .+$',body,re.M)==re.findall(r'^## [1-5] .+$',oldbody,re.M) and
 re.findall(r'^### 3\.[1-6] .+$',body,re.M)==re.findall(r'^### 3\.[1-6] .+$',oldbody,re.M))
checks['120_unique_sources_94_retained_26_added']=(len(reg)==len(bynew)==120 and set(byold)<=set(bynew) and len(added)==26 and added=={r['stable_id'] for r in integration})
keep_fields=['reference_text','actual_version','version_resolution','actual_source_url','version_record_path']
checks['retained_source_identities_and_versions_unchanged']=all(all(bynew[sid][k]==r[k] for k in keep_fields) for sid,r in byold.items())
checks['bibliography_matches_numbered_register']=re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v354_number'],r['reference_text']) for r in reg]
first=[];observed=[];narrative={s:[] for s in bynew};bad=[]
for lineno,line in enumerate(body.splitlines(),1):
    for _,ns in citations(line):
        for n in ns:
            if n not in by_number:bad.append(n);continue
            if n not in first:first.append(n)
            sid=by_number[n]['stable_id'];observed.append((sid,str(n),str(lineno)))
            if not line.startswith('|'):narrative[sid].append(str(lineno))
checks['all_sources_cited_in_first_appearance_order']=not bad and first==list(range(1,121))
checks['citation_location_record_matches_actual_text']=observed==[(r['stable_id'],r['v354_number'],r['line']) for r in locations]
checks['each_added_source_has_narrative_use']=all(narrative[s] for s in added) and all(r['narrative_citation_lines'].split(';')==narrative[r['stable_id']] for r in integration)
bindings=[]
for r in integration:
    paths=[ROOT/p for p in r['reading_note_paths'].split(';')]
    if not all(p.is_file() for p in paths):bindings.append((r['stable_id'],'missing note'));continue
    corpus='\n'.join(p.read_text(encoding='utf-8') for p in paths)
    for cid in r['existing_claim_ids_used'].split(';'):
        if cid not in corpus:bindings.append((r['stable_id'],cid))
checks['added_claim_ids_and_version_records_resolve']=not bindings and all((ROOT/r['source_manifest_path']).is_file() for r in integration) and all(r['actual_source_url'].startswith('https://') and r['actual_version'] for r in integration)
cohorts={k:sum(r['cohort']==k for r in integration) for k in ['B11_B20_COMPLETED_BODY_READING','HISTORICAL_TARGETED_BODY_READING']}
cited_recent={s for s in bynew if re.match(r'^E-B(?:11|12|13|14|15|16|17|18|19|20)-',s)}
checks['reading_cohorts_separate_from_citation_counts']=cohorts=={'B11_B20_COMPLETED_BODY_READING':15,'HISTORICAL_TARGETED_BODY_READING':11} and len(cited_recent)==43 and all(r['new_unique_full_text_reading_credit']=='0' for r in integration)
hold={'E-B17-S045','E-B20-L071'}
held_rows=[r for r in selection if r['reading_id'] in {'S045','L071'}]
checks['reserve_ledger_and_hold_states_retained']=len(selection)==195 and len(held_rows)==2 and all('HOLD' in r['decision'] and r['v354_decision']=='PRIOR_RESERVE_OR_HOLD_UNCHANGED' and not r['v354_number'] for r in held_rows)
boundary_fail=[]
for r in bounds:
    ps=[ROOT/p for p in r['inherited_record_paths'].split(';')]
    if not all(p.is_file() for p in ps):boundary_fail.append(r['boundary_id']);continue
    corpus='\n'.join(p.read_text(encoding='utf-8-sig') for p in ps)
    for cid in r['inherited_evidence_ids'].split(';'):
        if cid!='BASELINE_MEANING' and cid not in corpus:boundary_fail.append((r['boundary_id'],cid))
checks['inherited_scientific_boundary_records_resolve']=len(bounds)==23 and not boundary_fail and all(set(r['stable_source_ids'].split(';'))<=set(bynew) for r in bounds)
checks['original_time_window_equation_preserved']=re.findall(r'\$\$(.*?)\$\$',body,re.S)==re.findall(r'\$\$(.*?)\$\$',oldbody,re.S)
figures=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['eight_tables_and_four_identical_figure_assets']=(re.findall(r'^\*\*表([1-8]) ',body,re.M)==list('12345678') and len(figures)==4 and all((HERE/f).read_bytes()==oldfile(f) for f in figures) and 'AI辅助定性草图，非数值结果' in body)
checks['abstracts_and_key_original_values_present']=('## 摘要\n\n' in body and '## Abstract\n\n' in body and all(t in body for t in ['2000','90.95%','10星','50星','24 023','100星','35星','24星']))
changed=git('diff',BASE,'--name-only').splitlines();status=git('status','--porcelain','--untracked-files=all').splitlines()
checks['changes_confined_to_new_directory']=all(p.startswith(PREFIX) for p in changed) and all(r[3:].startswith(PREFIX) for r in status)
checks['fixed_baseline_and_original_versions_preserved']=(git('branch','--show-current')==BRANCH and git('merge-base',BASE,'HEAD')==BASE and git('rev-parse','writing/constellation-review-v353-full-style-20261022')==BASE and not git('diff',BASE,'--name-only','--','review_writing/manuscripts/v3.5.3-cn','review_writing/manuscripts/v3.5.2-cn','review_writing/manuscripts/v3.5.1-cn','review_writing/manuscripts/v3.5-cn'))
destinations=[]
for filename in ['REVIEW_CN_v3.5.4.md','README_CN.md','REFERENCE_INTEGRATION_CN.md','SCIENTIFIC_REVISION_CN.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',(HERE/filename).read_text(encoding='utf-8')):
        if '://' not in dest and not dest.startswith('#'):destinations.append((HERE/dest).is_file() or dest=='VALIDATION_REPORT.json')
checks['local_delivery_links_resolve']=bool(destinations) and all(destinations)
checks['human_or_submission_approval_not_claimed']=all(r['human_verified']=='false' for r in reg+integration+bounds)
report={'status':'PASS' if all(checks.values()) else 'FAIL','baseline_commit':BASE,'branch':BRANCH,
 'scope':'Structural, citation and source-record consistency only. Locator presence, numeric presence, and source binding do not certify scientific meaning, writing quality or submission readiness.',
 'references_before':94,'references_after':len(reg),'references_added':len(added),'references_removed':len(set(byold)-set(bynew)),
 'B11_B20_body_reading_records':97,'B11_B20_sources_now_cited':len(cited_recent),'B11_B20_still_uncited':97-len(cited_recent),
 'added_source_cohorts':cohorts,'body_han_before':len(re.findall('[\u4e00-\u9fff]',oldbody)),
 'body_han_after':len(re.findall('[\u4e00-\u9fff]',body)),'new_unique_full_text_readings':0,'new_experiments':0,
 'human_verified':False,'submission_ready':False,'EC2026_full_text_obtained':False,'L042_formal_pairing_closed':False,
 'L042_figure16_24_pixel_review_completed':False,'matched_net_service_recovery_benefit_proven':False,'figures_redrawn':0,
 'checks':checks,'binding_failures':bindings,'boundary_record_failures':boundary_fail,
 'manuscript_sha256':hashlib.sha256((HERE/'REVIEW_CN_v3.5.4.md').read_bytes()).hexdigest()}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],
 'binding_failures':bindings,'boundary_record_failures':boundary_fail,'references':len(reg)},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
