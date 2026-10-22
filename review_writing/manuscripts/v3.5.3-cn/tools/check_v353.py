"""Bounded consistency checks for a prose-only revision, not scientific certification."""
from pathlib import Path
import csv,hashlib,io,json,re,subprocess

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
BASE='7e0fcba00176c944f8214664747caf597de73fcd'
STYLE='eb6876f6ff7e4778002989073a4110c38dc86fdb'
BRANCH='writing/constellation-review-v353-full-style-20261022'
PREFIX='review_writing/manuscripts/v3.5.3-cn/'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()

def oldfile(name):
    return subprocess.check_output(['git','show',f'{BASE}:review_writing/manuscripts/v3.5.2-cn/{name}'],cwd=ROOT)

def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
pattern=re.compile(r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]')
def citations(text):
    for m in pattern.finditer(text):
        ns=[]
        for p in m.group(1).split(','):
            q=re.split('[–—-]',p);ns.extend(range(int(q[0]),int(q[-1])+1))
        yield m,ns

def normalize(text,reg,key):
    index={int(r[key]):r['stable_id'] for r in reg};out=[];p=0
    for m,ns in citations(text):
        out.extend((text[p:m.start()],'['+','.join(sorted(index[n] for n in ns))+']'));p=m.end()
    return ''.join(out)+text[p:]

def section_sources(text,reg,key):
    index={int(r[key]):r['stable_id'] for r in reg};result={};heading='front'
    for line in text.splitlines():
        m=re.match(r'^#{2,4} (\d+(?:\.\d+)*) ',line)
        if m:heading=m.group(1)
        result.setdefault(heading,set())
        for _,ns in citations(line):result[heading].update(index[n] for n in ns)
    return result

prior=oldfile('REVIEW_CN_v3.5.2.md').decode('utf-8')
old=list(csv.DictReader(io.StringIO(oldfile('references/REFERENCE_REGISTER_v3.5.2.csv').decode('utf-8-sig'))))
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.3.csv')
bounds=rows(HERE/'references/SCIENTIFIC_BOUNDARIES_v3.5.3.csv')
locations=rows(HERE/'references/CITATION_LOCATIONS_v3.5.3.csv')
text=(HERE/'REVIEW_CN_v3.5.3.md').read_text(encoding='utf-8')
body,bib=text.split('## 参考文献',1);oldbody,oldbib=prior.split('## 参考文献',1)
pilot=subprocess.check_output(['git','show',f'{STYLE}:review_writing/manuscripts/v3.5.2-cn-style-sample/ABSTRACT_AND_SECTION_CN.md'],cwd=ROOT).decode('utf-8')
byold={r['stable_id']:r for r in old};bynew={r['stable_id']:r for r in reg}
checks={}
checks['same_title_five_chapters_and_method_domains']= (
    body.splitlines()[0]==oldbody.splitlines()[0] and
    re.findall(r'^## [1-5] .+$',body,re.M)==re.findall(r'^## [1-5] .+$',oldbody,re.M) and
    re.findall(r'^### 3\.[1-6] .+$',body,re.M)==re.findall(r'^### 3\.[1-6] .+$',oldbody,re.M) and
    re.findall(r'^#{2,4} (\d+(?:\.\d+)*) ',body,re.M)==re.findall(r'^#{2,4} (\d+(?:\.\d+)*) ',oldbody,re.M))
checks['same_94_source_ids_numbers_bibliography_and_actual_versions']=(
    len(reg)==len(bynew)==94 and set(byold)==set(bynew) and
    all(all(r[k]==byold[sid][k] for k in ['reference_text','actual_version','version_resolution','actual_source_url','version_record_path'])
        and r['v353_number']==byold[sid]['v352_number'] for sid,r in bynew.items()))
checks['bibliography_unchanged_and_matches_register']=(bib==oldbib and re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v353_number'],r['reference_text']) for r in reg])
first=[]
for _,ns in citations(body):
    for n in ns:
        if n not in first:first.append(n)
checks['all_sources_cited_in_first_appearance_order']=first==list(range(1,95))
oldscopes=section_sources(oldbody,old,'v352_number');newscopes=section_sources(body,reg,'v353_number')
scope_changes={s:{'added':sorted(newscopes.get(s,set())-oldscopes.get(s,set())),
                  'removed':sorted(oldscopes.get(s,set())-newscopes.get(s,set()))}
               for s in set(oldscopes)|set(newscopes) if oldscopes.get(s,set())!=newscopes.get(s,set())}
checks['source_sets_preserved_in_every_numbered_section']=not scope_changes
newabs=body.split('## 摘要\n\n',1)[1].split('\n\n**关键词',1)[0]
approvedabs=pilot.split('## 摘要\n\n',1)[1].split('\n\n**关键词',1)[0]
new422=body[body.index('#### 4.2.2 '):body.index('#### 4.2.3 ')].strip()
approved422='#### 4.2.2 '+pilot.split('#### 4.2.2 ',1)[1].split('\n\n---',1)[0]
checks['approved_chinese_abstract_and_section_adopted']=newabs==approvedabs and normalize(new422,reg,'v353_number')==normalize(approved422,old,'v352_number')
checks['time_window_equation_unchanged']=re.findall(r'\$\$(.*?)\$\$',body,re.S)==re.findall(r'\$\$(.*?)\$\$',oldbody,re.S)
checks['eight_tables_and_four_unchanged_figure_assets']=(
    re.findall(r'^\*\*表([1-8]) ',body,re.M)==list('12345678') and
    len(re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body))==4 and
    all((HERE/p).read_bytes()==oldfile(p) for p in re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)))
checks['english_abstract_and_figure_status_retained']= '## Abstract\n\n' in body and 'under matched conditions' in body and 'AI辅助定性草图，非数值结果' in body
checks['reported_key_scales_and_counterexample_value_retained']=all(t in body for t in ['1—5星','4—40星','两颗卫星','12小时','100星','一周','24星','35星','10星','50星','24 023','2000','90.95%'])
observed=[]
for lineno,line in enumerate(body.splitlines(),1):
    for _,ns in citations(line):observed.extend((str(n),str(lineno)) for n in ns)
checks['citation_locations_match_delivered_text']=observed==[(r['v353_number'],r['line']) for r in locations]
failures=[]
for r in bounds:
    paths=[ROOT/p for p in r['inherited_record_paths'].split(';')]
    if not all(p.is_file() for p in paths):failures.append((r['boundary_id'],'missing record'));continue
    corpus='\n'.join(p.read_text(encoding='utf-8-sig') for p in paths)
    for eid in r['inherited_evidence_ids'].split(';'):
        if eid!='BASELINE_MEANING' and eid not in corpus:failures.append((r['boundary_id'],eid))
    if not set(r['stable_source_ids'].split(';'))<=set(bynew):failures.append((r['boundary_id'],'uncited source'))
checks['key_meaning_records_and_source_versions_resolve']=len(bounds)==23 and not failures and all((ROOT/r['version_record_path']).is_file() for r in reg)
changed=git('diff',STYLE,'--name-only').splitlines();status=git('status','--porcelain','--untracked-files=all').splitlines()
checks['changes_confined_to_new_version_directory']=all(p.startswith(PREFIX) for p in changed) and all(line[3:].startswith(PREFIX) for line in status)
checks['fixed_scientific_and_style_baselines_preserved']=(
    git('branch','--show-current')==BRANCH and git('merge-base',STYLE,'HEAD')==STYLE and
    git('rev-parse','writing/constellation-review-v352-prose-consolidation-20261022')==BASE and
    git('rev-parse','writing/constellation-review-style-sample-20261022')==STYLE and
    not git('diff',BASE,'--name-only','--','review_writing/manuscripts/v3.5.2-cn') and
    not git('diff',STYLE,'--name-only','--','review_writing/manuscripts/v3.5.2-cn-style-sample') and
    git('rev-parse','refs/remotes/origin/main')=='4cfaff732d7d68adeecf137d9a6f2a12d12cb2c0')
links=[]
for name in ['REVIEW_CN_v3.5.3.md','STYLE_REVISION_CN.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in dest and not dest.startswith('#'):links.append((HERE/dest).is_file() or dest=='VALIDATION_REPORT.json')
checks['delivery_links_resolve']=bool(links) and all(links)
checks['human_approval_not_claimed']=all(r['human_verified']=='false' for r in reg+bounds)
report={'status':'PASS' if all(checks.values()) else 'FAIL','baseline_commit':BASE,'approved_style_commit':STYLE,'branch':BRANCH,
    'scope':'Structural and provenance consistency only. Section source-set equality and numeric presence do not certify scientific meaning or writing quality.',
    'references_before':94,'references_after':len(reg),'references_added':0,'references_removed':0,'references_renumbered':0,
    'body_han_before':len(re.findall('[\u4e00-\u9fff]',oldbody)),'body_han_after':len(re.findall('[\u4e00-\u9fff]',body)),
    'new_unique_full_text_readings':0,'new_experiments':0,'figures_redrawn':0,
    'human_verified':False,'submission_ready':False,'EC2026_full_text_obtained':False,'L042_formal_pairing_closed':False,
    'L042_figure16_24_pixel_review_completed':False,'matched_net_service_recovery_benefit_proven':False,
    'checks':checks,'section_source_set_differences':scope_changes,'record_failures':failures,
    'manuscript_sha256':hashlib.sha256((HERE/'REVIEW_CN_v3.5.3.md').read_bytes()).hexdigest()}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],
                  'section_source_differences':scope_changes,'record_failures':failures,'references':len(reg)},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
