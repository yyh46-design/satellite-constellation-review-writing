"""Bounded consistency checks for V3.5.7, not author scientific approval."""
from pathlib import Path
import csv, hashlib, io, json, re, subprocess

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
BASE='24f6f1bc3fd3acab7d3f4871239e8dca6360abbc'
OLD='review_writing/manuscripts/v3.5.6-cn'
PREFIX='review_writing/manuscripts/v3.5.7-cn/'
BRANCH='writing/constellation-review-v357-structural-refinement-20261026'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()
def before(path):return subprocess.check_output(['git','show',f'{BASE}:{OLD}/{path}'],cwd=ROOT)
def rows(path):return list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
def oldrows(path):return list(csv.DictReader(io.StringIO(before(path).decode('utf-8-sig'))))
def sha(data):return hashlib.sha256(data).hexdigest()
text=(HERE/'REVIEW_CN_v3.5.7.md').read_text(encoding='utf-8')
body,bib=text.split('## 参考文献',1)
oldtext=before('REVIEW_CN_v3.5.6.md').decode('utf-8')
oldbody,oldbib=oldtext.split('## 参考文献',1)
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.7.csv')
oldreg=oldrows('references/REFERENCE_REGISTER_v3.5.6.csv')
by_id={r['stable_id']:r for r in reg};old_id={r['stable_id']:r for r in oldreg}
by_num={int(r['v357_number']):r for r in reg}
locations=rows(HERE/'references/CITATION_LOCATIONS_v3.5.7.csv')
mapping=rows(HERE/'references/NUMBER_MAP_v3.5.6_TO_v3.5.7.csv')
claims=rows(HERE/'references/REVISION_EVIDENCE_v3.5.7.csv')
comparisons=rows(HERE/'references/COMPARISON_LOCATIONS_v3.5.7.csv')
boundaries=rows(HERE/'references/SCIENTIFIC_BOUNDARIES_v3.5.7.csv')
integration=rows(HERE/'references/SOURCE_INTEGRATION_v3.5.7.csv')
metrics=json.loads((HERE/'audit/REVISION_METRICS.json').read_text(encoding='utf-8'))
baseline=json.loads((HERE/'audit/BASELINE_IDENTITY.json').read_text(encoding='utf-8'))
checks={}
checks['title_five_chapters_and_3_1_to_3_6_preserved']=body.splitlines()[0]==oldbody.splitlines()[0] and re.findall(r'^## [1-5] .+$',body,re.M)==re.findall(r'^## [1-5] .+$',oldbody,re.M) and re.findall(r'^### 3\.[1-6] .+$',body,re.M)==re.findall(r'^### 3\.[1-6] .+$',oldbody,re.M)
checks['120_stable_sources_and_numbers_retained']=len(reg)==len(by_id)==120 and set(by_id)==set(old_id) and all(r['v357_number']==r['v356_number']==old_id[sid]['v356_number'] for sid,r in by_id.items())
checks['actual_versions_bibliography_and_human_states_unchanged']=all(all(r[f]==old_id[sid][f] for f in ['actual_version','version_resolution','actual_source_url','version_record_path','human_verified','reference_text']) for sid,r in by_id.items())
checks['bibliography_exact_and_register_aligned']=bib==oldbib and re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v357_number'],r['reference_text']) for r in reg]
checks['number_map_consistent']=len(mapping)==120 and all(r['v357_number']==r['v356_number']==by_id[r['stable_id']]['v357_number'] for r in mapping)
pattern=re.compile(r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]')
observed=[];first=[];bad=[];sec=''
for ln,line in enumerate(body.splitlines(),1):
    h=re.match(r'^#{2,4} (\d+(?:\.\d+)*) ',line)
    if h:sec=h.group(1)
    kind='table' if line.startswith('|') else 'table_note' if re.match(r'^注[12]：',line) else 'figure_caption' if re.match(r'^图\d',line) else 'narrative'
    for match in pattern.finditer(line):
        for part in match.group(1).split(','):
            bounds=re.split('[–—-]',part)
            for n in range(int(bounds[0]),int(bounds[-1])+1):
                if n not in by_num:bad.append(n);continue
                if n not in first:first.append(n)
                observed.append({'stable_id':by_num[n]['stable_id'],'v357_number':str(n),'v356_number':str(n),'line':str(ln),'section':sec,'context_kind':kind})
checks['all_120_citations_preserve_first_occurrence_order']=not bad and first==list(range(1,121))
checks['current_citation_locations_exact']=locations==observed
checks['all_actual_source_record_paths_resolve']=all((ROOT/r['version_record_path']).is_file() for r in reg)
claim_errors=[]
for r in claims:
    if not set(r['stable_source_ids'].split(';'))<=set(by_id):claim_errors.append([r['claim_id'],'source ID'])
    record=HERE/r['inherited_record']
    if not record.is_file():claim_errors.append([r['claim_id'],'record'])
    elif not all(cid in record.read_text(encoding='utf-8') for cid in r['inherited_claim_or_check_ids'].split(';')):claim_errors.append([r['claim_id'],'inherited ID'])
    if sha(r['claim_summary'].encode())!=r['claim_sha256']:claim_errors.append([r['claim_id'],'hash'])
    actual=[str(i) for i,line in enumerate(body.splitlines(),1) if r['anchor'] in line]
    if not actual or ';'.join(actual)!=r['current_lines']:claim_errors.append([r['claim_id'],'location'])
checks['nine_changed_arguments_resolve_to_inherited_evidence_and_current_text']=len(claims)==9 and not claim_errors
oldcomp={r['check_id']:r for r in oldrows('references/WITHIN_STUDY_COMPARISONS_v3.5.6.csv')}
checks['four_original_comparisons_preserved_with_current_locations']=len(comparisons)==4 and all(json.loads(r['values_json'])==json.loads(oldcomp[r['inherited_check_id']]['values_json']) and r['source_locator']==oldcomp[r['inherited_check_id']]['source_locator'] and (HERE/r['inherited_record']).is_file() and r['anchor'] in body.splitlines()[int(r['current_line'])-1] for r in comparisons)
checks['numeric_results_and_unfavorable_examples_retained']=all(t in body for t in ['2356/2335/2356','4610/4584/4656','32.53/0.03/13.62','10 800 s（限时）/0.04/5942.12','6个实例启发式较好、10个略差、2个相同','26.21%','1.77%','462.24','1491、1736和1963','该文表2的实例13由完整模型取得更高奖励'])
checks['solver_budget_reward_and_RP_scopes_retained']=all(t in body for t in ['每个子问题限时3600 s','累积运行时间','不能当作等计算预算','奖励按覆盖计算','并未比较短视、滚动与完整模型的求解效果','负值目标的符号约定'])
oldbounds={r['baseline_boundary_id']:r for r in oldrows('references/SCIENTIFIC_BOUNDARIES_v3.5.6.csv')}
checks['23_scientific_boundaries_retain_meaning_and_source_ids']=len(boundaries)==23 and all(all(r[f]==oldbounds[r['baseline_boundary_id']][f] for f in ['preserved_scientific_meaning','stable_source_ids','inherited_record_paths','inherited_evidence_ids','human_verified','current_disposition']) for r in boundaries)
oldintegration=oldrows('references/SOURCE_INTEGRATION_v3.5.6.csv')
checks['26_historical_adoptions_retain_ids_and_update_locations']=len(integration)==26 and {r['stable_id'] for r in integration}=={r['stable_id'] for r in oldintegration} and all(r['narrative_citation_lines']==';'.join(x['line'] for x in locations if x['stable_id']==r['stable_id'] and x['context_kind']=='narrative') and r['narrative_citation_lines'] for r in integration)
def extract_table(s,num):return re.search(r'^\*\*表'+str(num)+r' .+?\*\*\n\n((?:\|.*\n)+)',s,re.M).group(0)
checks['tables_8_and_9_preserved_exactly']=all(extract_table(body,n)==extract_table(oldbody,n) for n in [8,9])
def span(s,start,end):return s[s.index(start):s.index(end,s.index(start))]
checks['chapters_1_2_methods_3_1_to_3_5_and_coordination_4_3_unchanged']=span(body,'## 1 引言','### 3.6 ')==span(oldbody,'## 1 引言','### 3.6 ') and span(body,'### 4.3 ','### 4.4 ')==span(oldbody,'### 4.3 ','### 4.4 ')
checks['scale_count_assumptions_and_recovery_boundaries_retained']=all(t in body for t in [r'每轮有$A\bar d$次发送',r'A\bar dH','未含协议开销、聚合或重传','该轮包含$A$次串行更新','不是求解时间或安全性能的增长定律','仿真推进本身不记作权限确认','未与指定处置事件绑定','表内没有一行经所引证据确认'])
checks['safety_window_and_version_limits_retained']=all(t in body for t in ['完整占用窗口需要容纳活动的开始和结束','允许开始时刻窗口则直接检查开始时间','在线相交检查只覆盖所查步','控制二次规划','QP）无解则表示没有可行输入','2025年作者稿','零切换时延','无误码传输'])
checks['synthesis_and_future_questions_not_promoted_to_proven_results']=all(t in body for t in ['组织建议仍属于条件性综合','尚未确认其相对其他方式的同条件净业务优势','这是待检验的组织思路','尚待解决的是','未建立同时覆盖这些环节及实际采用成本'])
selection=rows(ROOT/'review_writing/manuscripts/v3.5.4-cn/references/SOURCE_SELECTION_v3.5.4.csv')
holds=[r for r in selection if r['reading_id'] in {'S045','L071'}]
checks['previous_hold_states_not_upgraded']=len(holds)==2 and all('HOLD' in r['decision'] and not r['v354_number'] for r in holds)
figs=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['nine_tables_four_existing_figures_same_bytes']=re.findall(r'^\*\*表([1-9]) ',body,re.M)==list('123456789') and len(figs)==4 and all((HERE/f).read_bytes()==before(f) for f in figs)
tables=re.findall(r'(?:^\|.*\n)+',body,re.M)
checks['table_column_counts_consistent']=all(len({len(line.split('|')) for line in table.strip().splitlines()})==1 for table in tables)
checks['correct_branch_and_baseline']=git('branch','--show-current')==BRANCH and git('merge-base',BASE,'HEAD')==BASE
protected=git('for-each-ref','--format=%(refname) %(objectname)','refs/heads/main','refs/remotes/origin/main','refs/heads/writing/constellation-review-v356-comparative-evidence-20261024').splitlines()
checks['protected_local_refs_and_baseline_bytes_unchanged']=protected==baseline['protected_local_refs'] and (ROOT/OLD/'REVIEW_CN_v3.5.6.md').read_bytes()==before('REVIEW_CN_v3.5.6.md')
changed=git('diff',BASE,'--name-only').splitlines();status=git('status','--porcelain','--untracked-files=all').splitlines()
checks['only_new_version_directory_changed']=all(p.startswith(PREFIX) for p in changed) and all(r[3:].startswith(PREFIX) for r in status)
missing=[]
for name in ['README_CN.md','SCIENTIFIC_REVISION_CN.md','REVISION_RESPONSE_CN.md','REFERENCE_INTEGRATION_CN.md','REVIEW_CN_v3.5.7.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in dest and not dest.startswith('#') and dest!='VALIDATION_REPORT.json' and not (HERE/dest).is_file():missing.append(dest)
checks['delivery_links_resolve']=not missing
checks['human_status_and_reading_credit_not_upgraded']=all(r['human_verified']=='false' for r in reg+claims+comparisons+boundaries+integration) and all(r['new_unique_reading_credit']=='0' for r in claims+comparisons)
checks['current_metrics_and_hash_match']=metrics['body_han_before']==len(re.findall('[\u4e00-\u9fff]',oldbody)) and metrics['body_han_after']==len(re.findall('[\u4e00-\u9fff]',body)) and metrics['manuscript_sha256']==sha((HERE/'REVIEW_CN_v3.5.7.md').read_bytes())
report={'status':'PASS' if all(checks.values()) else 'FAIL','baseline_commit':BASE,'branch':BRANCH,'scope':'Citation, source-identity, inherited comparison, scientific-boundary, structure and file consistency only. Not independent peer review, author scientific verification or submission approval.','references_before':120,'references_after':120,'references_added':0,'references_removed':0,'new_unique_full_text_readings':0,'targeted_source_rechecks_this_revision':0,'new_experiments':0,'new_training':0,'human_verified':False,'submission_ready':False,'EC2026_full_text_obtained':False,'L042_formal_pairing_closed':False,'L042_figure16_24_pixel_review_completed':False,'matched_net_service_recovery_benefit_proven':False,'figures_redrawn':0,'figure_internal_labels_and_pixels_revalidated':False,'body_han_before':metrics['body_han_before'],'body_han_after':metrics['body_han_after'],'manuscript_sha256':metrics['manuscript_sha256'],'checks':checks,'claim_errors':claim_errors,'missing_links':missing}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],'claim_errors':claim_errors,'missing_links':missing},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
