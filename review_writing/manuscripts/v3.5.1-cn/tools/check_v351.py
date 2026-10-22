"""Necessary local consistency checks; not author approval or safety certification."""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
BASE=ROOT/'review_writing/manuscripts/v3.5-cn'
BASE_SHA='d61971a49b48941256f9db3612f65e34cfea388d'
MAIN_SHA='4cfaff732d7d68adeecf137d9a6f2a12d12cb2c0'
BRANCH='writing/constellation-review-v351-evidence-curation-20261022'
PREFIX='review_writing/manuscripts/v3.5.1-cn/'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()

def rows(path):
    return list(csv.DictReader(path.open(encoding='utf-8-sig')))

def citations(text):
    for m in re.finditer(r'\[([0-9]+(?:[–—-][0-9]+)?(?:,[0-9]+(?:[–—-][0-9]+)?)*)\]',text):
        values=[]
        for p in m.group(1).split(','):
            q=re.split('[–—-]',p);values.extend(range(int(q[0]),int(q[-1])+1))
        yield m,values

def normalized(text,reg,key):
    index={int(r[key]):r['stable_id'] for r in reg}
    parts=[];prev=0
    for m,ns in citations(text):
        parts.extend((text[prev:m.start()],'['+','.join(sorted(index[n] for n in ns))+']'))
        prev=m.end()
    parts.append(text[prev:]);return ''.join(parts)

old=rows(BASE/'references/REFERENCE_REGISTER_v3.5.csv')
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.1.csv')
selection=rows(HERE/'references/SOURCE_SELECTION_v3.5.1.csv')
claims=rows(HERE/'references/KEY_CLAIM_UPDATES_v3.5.1.csv')
passages=json.loads((HERE/'references/TARGETED_PASSAGE_RECHECKS.json').read_text(encoding='utf-8'))
text=(HERE/'REVIEW_CN_v3.5.1.md').read_text(encoding='utf-8')
body,bib=text.split('## 参考文献',1)
prior=(BASE/'REVIEW_CN_v3.5.md').read_text(encoding='utf-8').split('## 参考文献',1)[0]
old_ids={r['stable_id'] for r in old};new_ids={r['stable_id'] for r in reg}
curated={r['stable_id']:r for r in selection}
checks={}

checks['title_five_chapters_and_research_scope_preserved']=(
    body.splitlines()[0]==prior.splitlines()[0] and
    re.findall(r'^## [1-5] .+$',body,re.M)==re.findall(r'^## [1-5] .+$',prior,re.M) and
    re.findall(r'^### 3\.[1-6] .+$',body,re.M)==re.findall(r'^### 3\.[1-6] .+$',prior,re.M) and
    re.findall(r'^#### 3\.6\.[1-3] .+$',body,re.M)==re.findall(r'^#### 3\.6\.[1-3] .+$',prior,re.M))
a=prior[prior.index('### 3.1 '):prior.index('### 3.4 ')]
b=body[body.index('### 3.1 '):body.index('### 3.4 ')]
checks['mechanisms_3_1_to_3_3_preserved_after_renumbering']=normalized(a,old,'v35_number')==normalized(b,reg,'v351_number')
checks['eight_tables_retained']=re.findall(r'^\*\*表([1-8]) ',body,re.M)==list('12345678')
figs=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['four_figure_assets_identical_to_fixed_baseline']=len(figs)==4 and all(
    (HERE/p).read_bytes()==subprocess.check_output(['git','show',f'{BASE_SHA}:review_writing/manuscripts/v3.5-cn/{p}'],cwd=ROOT)
    for p in figs)
checks['bibliography_matches_register']=re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v351_number'],r['reference_text']) for r in reg]
first=[]
for _,ns in citations(body):
    for n in ns:
        if n not in first:first.append(n)
checks['all_94_cited_in_first_appearance_order']=len(reg)==94 and first==list(range(1,95))
checks['exact_evidence_curation_delta']=(
    len(new_ids)==len(reg) and new_ids-old_ids=={'E-B19-L004','E-B17-S041','E-B17-S043'} and
    old_ids-new_ids=={'E114'} and curated['E114']['decision']=='REMOVE_REDUNDANT_INTRO')
old_by={r['stable_id']:r for r in old}
checks['retained_versions_and_bibliography_not_silently_upgraded']=all(
    (r['reference_text']==old_by[r['stable_id']]['reference_text'] and r['actual_version']==old_by[r['stable_id']]['actual_version'])
    for r in reg if r['stable_id'] in old_by and r['stable_id'] not in {'E051','E089','E115'})
checks['all_92_and_72_have_individual_dispositions']=(
    len(curated)==len(selection)==195 and
    {r['stable_id'] for r in selection if r['cohort']=='V35_CITED_92'}==old_ids and
    sum(r['cohort']=='B11_B20_UNCITED_72' for r in selection)==72 and
    all(r['scientific_reason'] and r['roles'] and r['decision'] for r in selection))
checks['holds_not_adopted']=(
    curated['E-B17-S045']['decision']=='HOLD_FOR_SOURCE_CLARIFICATION' and
    curated['E-B19-L071']['decision']=='HOLD_PENDING_CLARIFICATION' and
    all(not r['v351_number'] for r in selection if r['decision'].startswith('HOLD')))
checks['version_and_reading_record_paths_resolve']=all(
    (ROOT/r['version_record_path']).is_file() and
    (not r['reading_note_path'] or (ROOT/r['reading_note_path']).is_file()) for r in selection)
checks['register_paths_resolve']=all((ROOT/r['version_record_path']).is_file() for r in reg)

claim_ids={r['revision_claim_id'] for r in claims}
claim_failures=[]
for r in claims:
    paths=r['record_paths'].split(';')
    if not all((ROOT/p).is_file() for p in paths):
        claim_failures.append((r['revision_claim_id'],'missing path'));continue
    corpus='\n'.join((ROOT/p).read_text(encoding='utf-8-sig') for p in paths)
    for cid in r['evidence_ids'].split(';'):
        if cid=='AUTHOR_SYNTHESIS':continue
        if cid in claim_ids:continue
        if cid not in corpus:claim_failures.append((r['revision_claim_id'],cid))
    if not set(r['stable_source_ids'].split(';'))<=new_ids:
        claim_failures.append((r['revision_claim_id'],'uncited source'))
checks['17_key_claim_bindings_resolve_to_existing_ids']=len(claims)==17 and not claim_failures
checks['new_adoption_not_claimed_as_new_reading_or_experiment']=(
    passages['new_unique_full_text_reading_credit']==0 and passages['new_experiments']==0 and
    passages['all_b11_b20_note_files_loaded']==97 and passages['all_b11_b20_claim_records_loaded']==450 and
    passages['b11_b20_unused_after']==69)
open_items=passages['inherited_open_items']
checks['inherited_access_and_scientific_gaps_remain_open']=(
    open_items['EC2026_full_text_obtained'] is False and
    open_items['L042_formal_pairing_closed'] is False and
    open_items['L042_figure16_24_pixel_review_completed'] is False and
    open_items['matched_net_service_recovery_benefit_proven'] is False)
checks['human_and_submission_approval_not_claimed']=(
    passages['human_verified'] is False and passages['submission_ready'] is False and
    all(r['human_verified']=='false' for r in reg+selection+claims))
changed=git('diff',BASE_SHA,'--name-only').splitlines()
status=git('status','--porcelain').splitlines()
checks['v35_history_and_main_preserved_scope_only_v351']=(
    all(p.startswith(PREFIX) for p in changed) and
    all(line[3:].startswith(PREFIX) for line in status) and
    git('rev-parse','refs/remotes/origin/main')==MAIN_SHA and
    git('branch','--show-current')==BRANCH and git('merge-base',BASE_SHA,'HEAD')==BASE_SHA)
links=[]
for name in ['REVIEW_CN_v3.5.1.md','REFERENCE_SELECTION_REVIEW_CN.md','SCIENTIFIC_REVISION_CN.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in dest and not dest.startswith('#'):
            links.append((HERE/dest).exists() or dest=='VALIDATION_REPORT.json')
checks['local_delivery_links_resolve']=all(links)
report={
    'status':'PASS' if all(checks.values()) else 'FAIL',
    'baseline_commit':BASE_SHA,'branch':BRANCH,'main_tracking_ref':MAIN_SHA,
    'scope':'Necessary structure,citation,record identity and baseline preservation checks only; scientific semantics reviewed through bounded claim records, not automatically certified',
    'references_before':92,'retained':91,'added_from_existing_readings':3,'removed_redundant_intro':1,'references_after':len(reg),
    'body_han_characters':len(re.findall('[\u4e00-\u9fff]',body)),
    'new_unique_full_text_reading_credit':0,'new_experiments':0,
    'human_verified':False,'submission_ready':False,
    'checks':checks,'claim_binding_failures':claim_failures,
    'manuscript_sha256':hashlib.sha256((HERE/'REVIEW_CN_v3.5.1.md').read_bytes()).hexdigest(),
    'open_items':'See SCIENTIFIC_REVISION_CN.md; source and figure gaps not closed'}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],
                  'claim_binding_failures':claim_failures,'references':len(reg)},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
