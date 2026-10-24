"""Necessary consistency checks for V3.5.6; not scientific or submission approval."""
from pathlib import Path
import csv, hashlib, io, json, re, subprocess

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
BASE='8d4cc6ee784cbf455453f5ded05ce88623332538'
OLD='review_writing/manuscripts/v3.5.5-cn'
PREFIX='review_writing/manuscripts/v3.5.6-cn/'
BRANCH='writing/constellation-review-v356-comparative-evidence-20261024'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()
def before(path):return subprocess.check_output(['git','show',f'{BASE}:{OLD}/{path}'],cwd=ROOT)
def rows(path):return list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
def sha(data):return hashlib.sha256(data).hexdigest()

manuscript=HERE/'REVIEW_CN_v3.5.6.md'
text=manuscript.read_text(encoding='utf-8');body,bib=text.split('## 参考文献',1)
oldtext=before('REVIEW_CN_v3.5.5.md').decode('utf-8');oldbody=oldtext.split('## 参考文献',1)[0]
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.6.csv');by_id={r['stable_id']:r for r in reg};by_num={int(r['v356_number']):r for r in reg}
oldreg=list(csv.DictReader(io.StringIO(before('references/REFERENCE_REGISTER_v3.5.5.csv').decode('utf-8-sig'))));old_id={r['stable_id']:r for r in oldreg}
mapping=rows(HERE/'references/NUMBER_MAP_v3.5.5_TO_v3.5.6.csv')
locations=rows(HERE/'references/CITATION_LOCATIONS_v3.5.6.csv')
claims=rows(HERE/'references/REVISION_EVIDENCE_v3.5.6.csv')
comparisons=rows(HERE/'references/WITHIN_STUDY_COMPARISONS_v3.5.6.csv')
rechecks=json.loads((HERE/'references/TARGETED_RECHECKS_v3.5.6.json').read_text(encoding='utf-8'))
boundaries=rows(HERE/'references/SCIENTIFIC_BOUNDARIES_v3.5.6.csv')
integration=rows(HERE/'references/SOURCE_INTEGRATION_v3.5.6.csv')
metrics=json.loads((HERE/'audit/REVISION_METRICS.json').read_text(encoding='utf-8'))
baseline=json.loads((HERE/'audit/BASELINE_IDENTITY.json').read_text(encoding='utf-8'))
checks={}
checks['title_five_chapters_and_3_1_to_3_6_preserved']=(body.splitlines()[0]==oldbody.splitlines()[0] and re.findall(r'^## [1-5] .+$',body,re.M)==re.findall(r'^## [1-5] .+$',oldbody,re.M) and re.findall(r'^### 3\.[1-6] .+$',body,re.M)==re.findall(r'^### 3\.[1-6] .+$',oldbody,re.M))
checks['120_stable_sources_no_additions_or_deletions']=len(reg)==len(by_id)==120 and set(by_id)==set(old_id)
identity_fields=['actual_version','version_resolution','actual_source_url','version_record_path','human_verified']
checks['actual_source_versions_and_human_status_preserved']=all(all(r[f]==old_id[sid][f] for f in identity_fields) for sid,r in by_id.items())
bib_changes=[sid for sid,r in by_id.items() if r['reference_text']!=old_id[sid]['reference_text']]
checks['only_bibliographic_process_note_removed']=bib_changes==['E-B20-L042'] and by_id['E-B20-L042']['reference_text']==old_id['E-B20-L042']['reference_text'].replace('; formal text not compared.','.')
checks['bibliography_and_register_match']=re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v356_number'],r['reference_text']) for r in reg]
checks['120_number_map_identities_preserved']=len(mapping)==120 and all(r['v356_number']==r['v355_number']==by_id[r['stable_id']]['v356_number'] for r in mapping)
pattern=re.compile(r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]')
first=[];observed=[];bad=[];sec=''
for ln,line in enumerate(body.splitlines(),1):
    h=re.match(r'^#{2,4} (\d+(?:\.\d+)*) ',line)
    if h:sec=h.group(1)
    kind='table' if line.startswith('|') else 'figure_caption' if re.match(r'^图\d',line) else 'narrative'
    for match in pattern.finditer(line):
        for part in match.group(1).split(','):
            bounds=re.split('[–—-]',part)
            for n in range(int(bounds[0]),int(bounds[-1])+1):
                if n not in by_num:bad.append(n);continue
                if n not in first:first.append(n)
                observed.append({'stable_id':by_num[n]['stable_id'],'v356_number':str(n),'v355_number':str(n),'line':str(ln),'section':sec,'context_kind':kind})
checks['all_120_citations_in_first_occurrence_order']=not bad and first==list(range(1,121))
checks['current_citation_locations_exact']=locations==observed
checks['all_actual_source_record_paths_resolve']=all((ROOT/r['version_record_path']).is_file() for r in reg)
claim_errors=[]
recheck_ids={r['check_id'] for r in rechecks['comparisons']}
for r in claims:
    if not set(r['stable_source_ids'].split(';'))<=set(by_id):claim_errors.append((r['claim_id'],'unknown stable id'))
    if not (HERE/r['source_record_relative_to_version']).is_file():claim_errors.append((r['claim_id'],'missing source record'))
    if sha(r['claim_summary'].encode())!=r['claim_sha256']:claim_errors.append((r['claim_id'],'hash'))
    actual=[str(i) for i,line in enumerate(body.splitlines(),1) if r['anchor'] in line]
    if not actual or ';'.join(actual)!=r['current_lines']:claim_errors.append((r['claim_id'],'location'))
    if r['targeted_check_id'] and r['targeted_check_id'] not in recheck_ids:claim_errors.append((r['claim_id'],'check id'))
checks['13_changed_claims_resolve_to_evidence_and_current_text']=len(claims)==13 and not claim_errors
checks['comparison_csv_matches_targeted_original_page_record']=len(comparisons)==4 and all(json.loads(row['values_json'])==next(r['reported_or_visually_confirmed'] for r in rechecks['comparisons'] if r['check_id']==row['check_id']) for row in comparisons)
checks['key_numeric_transcriptions_consistent']=all(token in body for token in ['2356/2335/2356','4610/4584/4656','32.53/0.03/13.62','10 800 s（限时）/0.04/5942.12','6个实例启发式较好、10个略差、2个相同','26.21%','1.77%','462.24','1491、1736和1963']) and sum([6,10,2])==18
checks['comparison_scope_and_runtime_denominators_explicit']=all(token in body for token in ['每个子问题限时3600 s','累积运行时间','不能当作等计算预算','奖励按覆盖计算','并未比较短视、滚动与完整模型的求解效果','该文表2的实例13'])
checks['recovery_proxy_and_authority_distinctions_present']=all(token in body for token in ['仿真推进本身不记作权限确认','代理：观测尝试的几何对准表现','容量代理，未直接评价服务需求满足','未与指定处置事件绑定','运行流程文件[119]与终端性能测量[120]'])
checks['scale_count_assumptions_not_claimed_as_benchmark']=all(token in body for token in [r'N_{\mathrm{cat}}',r'每轮有$A\bar d$次发送',r'A\bar dH','未含协议开销、聚合或重传','该轮包含$A$次串行更新','不是求解时间或安全性能的增长定律'])
checks['known_window_meaning_retained_without_standalone_formula']=all(token in body for token in ['完整占用窗口需要容纳活动的开始和结束','允许开始时刻窗口则直接检查开始时间']) and r'm_i^{\mathrm{win}}' not in body
checks['23_boundary_records_retained']=len(boundaries)==23 and len({r['baseline_boundary_id'] for r in boundaries})==23 and all(set(r['stable_source_ids'].split(';'))<=set(by_id) and r['current_sections'] for r in boundaries)
oldintegration=list(csv.DictReader(io.StringIO(before('references/SOURCE_INTEGRATION_v3.5.5.csv').decode('utf-8-sig'))))
checks['prior_26_adoption_identities_and_updated_locations']=len(integration)==26 and {r['stable_id'] for r in integration}=={r['stable_id'] for r in oldintegration} and all(r['narrative_citation_lines']==';'.join(loc['line'] for loc in locations if loc['stable_id']==r['stable_id'] and loc['context_kind']=='narrative') and r['narrative_citation_lines'] for r in integration)
selection=rows(ROOT/'review_writing/manuscripts/v3.5.4-cn/references/SOURCE_SELECTION_v3.5.4.csv')
holds=[r for r in selection if r['reading_id'] in {'S045','L071'}]
checks['previous_hold_states_not_upgraded']=len(holds)==2 and all('HOLD' in r['decision'] and not r['v354_number'] for r in holds)
figs=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['nine_tables_four_pngs_same_bytes']=re.findall(r'^\*\*表([1-9]) ',body,re.M)==list('123456789') and len(figs)==4 and all((HERE/f).read_bytes()==before(f) for f in figs)
tables=re.findall(r'(?:^\|.*\n)+',body,re.M)
checks['markdown_table_column_counts_consistent']=all(len({len(line.split('|')) for line in table.strip().splitlines()})==1 for table in tables)
checks['human_approval_and_new_reading_not_claimed']=all(r['human_verified']=='false' for r in reg+claims+comparisons+boundaries+integration) and rechecks['human_verified'] is False and rechecks['submission_ready'] is False and rechecks['new_unique_full_text_readings']==0 and all(r['new_unique_reading_credit']=='0' for r in claims)
checks['correct_branch_and_baseline']=git('branch','--show-current')==BRANCH and git('merge-base',BASE,'HEAD')==BASE
protected=git('for-each-ref','--format=%(refname) %(objectname)','refs/heads/main','refs/remotes/origin/main','refs/heads/writing/constellation-review-v355-conditional-synthesis-20261023').splitlines()
checks['protected_refs_unchanged']=baseline['protected_local_refs']==protected
changes=git('diff',BASE,'--name-only').splitlines();status=git('status','--porcelain','--untracked-files=all').splitlines()
checks['only_new_v356_directory_changed']=all(p.startswith(PREFIX) for p in changes) and all(r[3:].startswith(PREFIX) for r in status)
checks['baseline_manuscript_bytes_unchanged']=(ROOT/OLD/'REVIEW_CN_v3.5.5.md').read_bytes()==before('REVIEW_CN_v3.5.5.md')
missing=[]
for filename in ['REVIEW_CN_v3.5.6.md','README_CN.md','SCIENTIFIC_REVISION_CN.md','REVISION_RESPONSE_CN.md','REFERENCE_INTEGRATION_CN.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',(HERE/filename).read_text(encoding='utf-8')):
        if '://' not in dest and not dest.startswith('#') and dest!='VALIDATION_REPORT.json' and not (HERE/dest).is_file():missing.append(dest)
checks['delivery_links_resolve']=not missing
checks['metrics_match_current_text']=metrics['manuscript_sha256']==sha(manuscript.read_bytes()) and metrics['body_han_after']==len(re.findall('[\u4e00-\u9fff]',body)) and metrics['body_han_before']==len(re.findall('[\u4e00-\u9fff]',oldbody))
report={'status':'PASS' if all(checks.values()) else 'FAIL','baseline_commit':BASE,'branch':BRANCH,'scope':'Source identity, citation and bibliography consistency, transcription and locator checks, document structure, protected baseline and file consistency only. Not human scientific verification or submission approval.','references_before':120,'references_after':len(reg),'references_added':0,'references_removed':0,'targeted_existing_sources_rechecked':3,'new_unique_full_text_readings':0,'new_experiments':0,'human_verified':False,'submission_ready':False,'EC2026_full_text_obtained':False,'L042_formal_pairing_closed':False,'L042_figure16_24_pixel_review_completed':False,'matched_net_service_recovery_benefit_proven':False,'figures_redrawn':0,'figure_internal_labels_and_pixels_revalidated':False,'body_han_before':metrics['body_han_before'],'body_han_after':metrics['body_han_after'],'manuscript_sha256':sha(manuscript.read_bytes()),'checks':checks,'claim_errors':claim_errors,'missing_links':missing}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],'claim_errors':claim_errors,'missing_links':missing},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
