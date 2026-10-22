"""Bounded structure, citation and provenance checks; not author scientific approval."""
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import subprocess

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
BASE_SHA = 'ab767f32ac5c82213eefe0035959039eee9739ff'
BASE_DIR = 'review_writing/manuscripts/v3.5.1-cn'
PREFIX = 'review_writing/manuscripts/v3.5.2-cn/'
BRANCH = 'writing/constellation-review-v352-prose-consolidation-20261022'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8').strip()

def oldfile(name):
    return subprocess.check_output(['git','show',f'{BASE_SHA}:{BASE_DIR}/{name}'], cwd=ROOT)

def rows(path):
    return list(csv.DictReader(path.open(encoding='utf-8-sig')))

pattern = re.compile(r'\[([0-9]+(?:[–—-][0-9]+)?(?:,[0-9]+(?:[–—-][0-9]+)?)*)\]')
def citations(text):
    for m in pattern.finditer(text):
        ns = []
        for p in m.group(1).split(','):
            q = re.split('[–—-]',p); ns.extend(range(int(q[0]),int(q[-1])+1))
        yield m, ns

def normalized(text, reg, key):
    lookup = {int(r[key]):r['stable_id'] for r in reg}
    result=[]; p=0
    for m,ns in citations(text):
        result.extend((text[p:m.start()], '['+','.join(sorted(lookup[n] for n in ns))+']'));p=m.end()
    return ''.join(result)+text[p:]

prior = oldfile('REVIEW_CN_v3.5.1.md').decode('utf-8')
old = list(csv.DictReader(io.StringIO(oldfile('references/REFERENCE_REGISTER_v3.5.1.csv').decode('utf-8-sig'))))
reg = rows(HERE/'references/REFERENCE_REGISTER_v3.5.2.csv')
evidence = rows(HERE/'references/REVISION_EVIDENCE_v3.5.2.csv')
locations = rows(HERE/'references/CITATION_LOCATIONS_v3.5.2.csv')
text = (HERE/'REVIEW_CN_v3.5.2.md').read_text(encoding='utf-8')
body,bib = text.split('## 参考文献',1)
oldbody = prior.split('## 参考文献',1)[0]
byold = {r['stable_id']:r for r in old}
bynew = {r['stable_id']:r for r in reg}
checks = {}

checks['title_five_chapters_and_six_method_domains_preserved'] = (
    body.splitlines()[0] == oldbody.splitlines()[0] and
    re.findall(r'^## [1-5] .+$',body,re.M) == re.findall(r'^## [1-5] .+$',oldbody,re.M) and
    re.findall(r'^### 3\.[1-6] .+$',body,re.M) == re.findall(r'^### 3\.[1-6] .+$',oldbody,re.M) and
    re.findall(r'^\*\*表([1-8]) ',body,re.M) == list('12345678'))
def core(t): return t[t.index('### 3.1 '):t.index('### 3.4 ')]
oldcore = normalized(core(oldbody),old,'v351_number').replace(
    '所读作者稿输入观测和传输时间段、权重与期限','其作者稿以观测和传输时间段、权重与期限为输入')
checks['core_3_1_to_3_3_algorithms_preserved_except_documented_phrase'] = oldcore == normalized(core(body),reg,'v352_number')
checks['same_94_stable_ids_bibliography_and_actual_versions'] = (
    len(reg)==len(bynew)==94 and set(byold)==set(bynew) and
    all(all(r[k]==byold[sid][k] for k in ['reference_text','actual_version','version_resolution','actual_source_url','version_record_path'])
        for sid,r in bynew.items()))
checks['bibliography_matches_register'] = re.findall(r'^(\d+)\. (.+)$',bib,re.M) == [(r['v352_number'],r['reference_text']) for r in reg]
first=[]
for _, ns in citations(body):
    for n in ns:
        if n not in first:first.append(n)
checks['all_sources_cited_and_numbered_in_first_appearance_order'] = first == list(range(1,95))
observed=[]
for lineno,line in enumerate(body.splitlines(),1):
    for _,ns in citations(line):
        observed.extend((str(n),str(lineno)) for n in ns)
checks['citation_locations_match_delivered_manuscript'] = observed == [(r['v352_number'],r['line']) for r in locations]
failures=[]
for r in evidence:
    ps=[ROOT/p for p in r['record_paths'].split(';')]
    if not all(p.is_file() for p in ps): failures.append((r['revision_id'],'missing record'));continue
    corpus='\n'.join(p.read_text(encoding='utf-8-sig') for p in ps)
    for eid in r['evidence_ids'].split(';'):
        if eid!='AUTHOR_SYNTHESIS' and eid not in corpus:failures.append((r['revision_id'],eid))
    if not set(r['stable_source_ids'].split(';'))<=set(bynew):failures.append((r['revision_id'],'source not cited'))
checks['revised_syntheses_trace_to_existing_claims_and_version_records'] = len(evidence)==6 and not failures and all((ROOT/r['version_record_path']).is_file() for r in reg)
figs=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['four_inherited_figures_are_byte_identical'] = len(figs)==4 and all((HERE/p).read_bytes()==oldfile(p) for p in figs)
checks['workflow_phrases_moved_out_of_manuscript_without_claiming_closed_issues'] = (
    not any(p in body for p in ['见本版科学精修记录','正式版配对继续待核','重绘须逐面板','待按最新主线重绘']) and
    'AI辅助定性草图，非数值结果' in body and '2025年作者稿' in body and
    '不据此判断其正文对联合优化的讨论深度' in body)
changes=git('diff',BASE_SHA,'--name-only').splitlines()
status=git('status','--porcelain','--untracked-files=all').splitlines()
checks['only_new_version_directory_changed'] = all(p.startswith(PREFIX) for p in changes) and all(line[3:].startswith(PREFIX) for line in status)
checks['fixed_parent_and_baseline_refs_preserved'] = (
    git('branch','--show-current')==BRANCH and git('merge-base',BASE_SHA,'HEAD')==BASE_SHA and
    git('rev-parse','writing/constellation-review-v351-evidence-curation-20261022')==BASE_SHA and
    git('rev-parse','refs/remotes/origin/main')=='4cfaff732d7d68adeecf137d9a6f2a12d12cb2c0')
links=[]
for name in ['REVIEW_CN_v3.5.2.md','REVISION_AND_READING_GUIDE_CN.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in dest and not dest.startswith('#'):links.append((HERE/dest).exists() or dest=='VALIDATION_REPORT.json')
checks['local_reading_and_provenance_links_resolve'] = bool(links) and all(links)
checks['human_approval_not_claimed_in_machine_records'] = all(r['human_verified']=='false' for r in reg+evidence)
han=lambda t:len(re.findall('[\u4e00-\u9fff]',t))
report = {'status':'PASS' if all(checks.values()) else 'FAIL','baseline_commit':BASE_SHA,'branch':BRANCH,
    'scope':'Structure, citations, version identity, record links and baseline preservation only. Scientific synthesis reviewed as prose, not machine certified.',
    'references_before':94,'references_after':len(reg),'references_added':0,'references_removed':0,
    'body_han_before':han(oldbody),'body_han_after':han(body),'body_han_reduction':han(oldbody)-han(body),
    'new_unique_full_text_readings':0,'new_experiments':0,'figures_redrawn':0,
    'L042_formal_pairing_closed':False,'L042_figure16_24_pixel_review_completed':False,
    'EC2026_full_text_obtained':False,'matched_net_service_recovery_benefit_proven':False,
    'human_verified':False,'submission_ready':False,'checks':checks,'evidence_link_failures':failures,
    'manuscript_sha256':hashlib.sha256((HERE/'REVIEW_CN_v3.5.2.md').read_bytes()).hexdigest()}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],
                  'references':len(reg),'body_han':han(body),'record_failures':failures},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
