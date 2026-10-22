"""Bounded structure, identity and baseline checks for the V3.5 writing revision.

This does not establish scientific approval, whole-paper reading, or readiness to submit.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
BASE = ROOT / 'review_writing/manuscripts/v3.4-cn'
BASE_SHA = 'a019b7861032468ae1a00cc9e32e70d47b276cdc'
FOLLOWUP_SHA = '6c073473cce686388af756c04c913e6502ebea2b'
BRANCH = 'writing/constellation-review-v3-5-science-refinement-20261022'
MAIN = '4cfaff732d7d68adeecf137d9a6f2a12d12cb2c0'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()

def cited_numbers(text):
    for m in re.finditer(r'\[([0-9]+(?:[–—-][0-9]+)?(?:,[0-9]+(?:[–—-][0-9]+)?)*)\]',text):
        values=[]
        for p in m.group(1).split(','):
            q=re.split('[–—-]',p)
            values.extend(range(int(q[0]),int(q[-1])+1))
        yield m,values

def stable_text(text, rows, key):
    by_num={int(r[key]):r['stable_id'] for r in rows}
    result=[];previous=0
    for m,ns in cited_numbers(text):
        result.extend((text[previous:m.start()], '['+','.join(sorted(by_num[n] for n in ns))+']'))
        previous=m.end()
    result.append(text[previous:])
    return ''.join(result)

old_rows=list(csv.DictReader((BASE/'references/REFERENCE_REGISTER_v3.4.csv').open(encoding='utf-8-sig')))
rows=list(csv.DictReader((HERE/'references/REFERENCE_REGISTER_v3.5.csv').open(encoding='utf-8-sig')))
old=(BASE/'REVIEW_CN_v3.4.md').read_text(encoding='utf-8')
text=(HERE/'REVIEW_CN_v3.5.md').read_text(encoding='utf-8')
body,bib=text.split('## 参考文献',1)
old_body=old.split('## 参考文献',1)[0]
by_id={r['stable_id']:r for r in rows}
checks={}
checks['five_chapters_exact']=re.findall(r'^## ([1-5] .+)$',body,re.M)==[
    '1 引言','2 智能运行管理中的决策问题与比较基础','3 规划、求解与协同决策方法',
    '4 运行条件下的决策取舍、采用与验证','5 结论']
checks['six_method_headings_preserved']=re.findall(r'^### 3\.[1-6] .+$',body,re.M)==re.findall(r'^### 3\.[1-6] .+$',old_body,re.M)
checks['three_orbit_subsections_preserved']=re.findall(r'^#### 3\.6\.[1-3] .+$',body,re.M)==re.findall(r'^#### 3\.6\.[1-3] .+$',old_body,re.M)
old_mechanisms=old_body[old_body.index('### 3.1 '):old_body.index('### 3.4 ')]
new_mechanisms=body[body.index('### 3.1 '):body.index('### 3.4 ')]
checks['mechanisms_3_1_to_3_3_identical_after_citation_normalization']=stable_text(old_mechanisms,old_rows,'v34_number')==stable_text(new_mechanisms,rows,'v35_number')
checks['eight_tables_preserved']=re.findall(r'^\*\*表([1-8]) ',body,re.M)==list('12345678')
figures=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['four_baseline_figure_bytes_preserved']=len(figures)==4 and all((HERE/p).read_bytes()==(BASE/p).read_bytes() for p in figures)
checks['four_initial_v35_figure_bytes_preserved']=len(figures)==4 and all(
    (HERE/p).read_bytes()==subprocess.check_output(
        ['git','show',f'{FOLLOWUP_SHA}:review_writing/manuscripts/v3.5-cn/{p}'],cwd=ROOT)
    for p in figures)
checks['p0_subsections_present']=all(f'#### {s} ' in body for s in ['4.2.1','4.2.2','4.2.3','4.4.2','4.4.3','4.4.4'])

bib_lines=re.findall(r'^(\d+)\. (.+)$',bib,re.M)
checks['bibliography_matches_current_register']=bib_lines==[(r['v35_number'],r['reference_text']) for r in rows]
seen=[]
for _,ns in cited_numbers(body):
    for n in ns:
        if n not in seen:seen.append(n)
checks['citation_coverage_and_first_appearance_order']=seen==list(range(1,len(rows)+1))
checks['stable_ids_unique_and_baseline_90_retained']=len(old_rows)==90 and len(by_id)==len(rows)==92 and set(r['stable_id'] for r in old_rows)<=set(by_id)
checks['two_scoped_reference_additions_since_v34']=set(by_id)-{r['stable_id'] for r in old_rows}=={'E-EC-SSO-2026','E-GSOC-2012'}
checks['retained_bibliographic_identity_unchanged']=all(by_id[r['stable_id']]['reference_text']==r['reference_text'] for r in old_rows)
checks['actual_versions_or_explicit_unresolved_states']=all(r['actual_version'] and r['version_resolution'] in ['IDENTIFIED_FROM_EXISTING_OR_TARGETED_RECORD','INHERITED_VERSION_UNRESOLVED'] and 'TO_EXTRACT' not in r['actual_version'] and 'to_extract' not in r['actual_version'] for r in rows)
checks['version_record_paths_resolve']=all((ROOT/r['version_record_path']).is_file() for r in rows)

source_checks=json.loads((HERE/'references/TARGETED_SOURCE_CHECKS.json').read_text(encoding='utf-8'))
followup=json.loads((HERE/'audit/FOLLOWUP_123_SOURCE_CHECKS.json').read_text(encoding='utf-8'))
issue_statuses={str(i['issue']):i['status'] for i in followup['issues']}
limited={s['stable_id']:s for s in source_checks['sources']}
checks['limited_source_access_states_retained']=(limited['E-EC-SSO-2026']['full_text_obtained'] is False and limited['E-B20-L042']['figure_visual_completed_this_revision'] is False and limited['E-B20-L042']['formal_version_pairing_closed_by_this_revision'] is False)
checks['followup_evidence_limits_and_fixed_base_explicit']=(
    followup['followup_base_commit']==FOLLOWUP_SHA and
    issue_statuses=={
        '1':'FULL_TEXT_ACCESS_UNRESOLVED',
        '2':'INTERPRETATION_CLARIFIED_FORMAL_PAIR_AND_PIXEL_REVIEW_OPEN',
        '3':'FEASIBILITY_CRITERION_AND_OPERATIONAL_EVIDENCE_ADDED_MATCHED_NET_GAIN_OPEN'} and
    followup['new_targeted_body_reading_records']==1 and followup['new_experiments']==0)
checks['figure4_replacement_status_explicit']='必须替换，不作为正式投稿数据图' in body
checks['human_and_submission_status_false']=source_checks['human_verified'] is False and source_checks['submission_ready'] is False and followup['human_verified'] is False and followup['submission_ready'] is False and all(r['human_verified']=='false' for r in rows)
checks['baseline_v34_not_modified']=not git('diff',BASE_SHA,'--','review_writing/manuscripts/v3.4-cn')
checks['correct_branch_and_base_ancestor']=git('branch','--show-current')==BRANCH and git('merge-base',BASE_SHA,'HEAD')==BASE_SHA
checks['main_tracking_ref_unchanged']=git('rev-parse','refs/remotes/origin/main')==MAIN

local_links=[]
for name in ['REVIEW_CN_v3.5.md','REVISION_NOTES_CN.md','EVIDENCE_AND_OPEN_ITEMS_CN.md','FOLLOWUP_123_CN.md']:
    for target in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in target and not target.startswith('#'):
            local_links.append((HERE/target).exists())
checks['local_manuscript_and_review_links_resolve']=all(local_links)
changed=git('diff',BASE_SHA,'--name-only').splitlines()
checks['tracked_change_scope_only_v35']=all(p.startswith('review_writing/manuscripts/v3.5-cn/') for p in changed)

report={
    'status':'PASS' if all(checks.values()) else 'FAIL',
    'scope':'Structure, citation identity/order, explicit evidence-access states, and baseline preservation only; not semantic or submission certification',
    'baseline_commit':BASE_SHA,'followup_base_commit':FOLLOWUP_SHA,'branch':BRANCH,'main_tracking_ref_before_revision':MAIN,
    'chapters':5,'tables':8,'inherited_figures':4,'references':len(rows),
    'body_han_characters':len(re.findall(r'[\u4e00-\u9fff]',body)),
    'initial_v35_new_unique_full_text_reading_credit':0,
    'followup_new_targeted_body_reading_records':followup['new_targeted_body_reading_records'],
    'new_experiments':0,'followup_issue_statuses':issue_statuses,
    'human_verified':False,'submission_ready':False,
    'checks':checks,
    'inherited_version_unresolved':[r['stable_id'] for r in rows if r['version_resolution']=='INHERITED_VERSION_UNRESOLVED'],
    'unresolved_scientific_issues':'See EVIDENCE_AND_OPEN_ITEMS_CN.md; no blanket version closure',
    'manuscript_sha256':hashlib.sha256((HERE/'REVIEW_CN_v3.5.md').read_bytes()).hexdigest()
}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],'body_han_characters':report['body_han_characters'],'references':len(rows)},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
