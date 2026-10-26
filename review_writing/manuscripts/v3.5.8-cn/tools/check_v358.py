"""Necessary manuscript/data/file consistency checks; not author scientific approval."""
from pathlib import Path
import csv, difflib, hashlib, io, json, re, subprocess

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
BASE = 'c78403f03e8c1f2df802c2fb910280434bae6206'
OLD = 'review_writing/manuscripts/v3.5.7-cn/'
PREFIX = 'review_writing/manuscripts/v3.5.8-cn/'
BRANCH = 'writing/constellation-review-v358-evidence-closure-20261026'
def git(*args): return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8').strip()
def before(name): return subprocess.check_output(['git', 'show', BASE + ':' + OLD + name], cwd=ROOT)
def rows(path): return list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
def oldrows(name): return list(csv.DictReader(io.StringIO(before(name).decode('utf-8-sig'))))
def sha(data): return hashlib.sha256(data).hexdigest()
def span(s, start, end): return s[s.index(start):s.index(end,s.index(start))]
def table(s,n): return re.search(r'^\*\*表'+str(n)+r' .+?\*\*\n\n((?:\|.*\n)+)',s,re.M).group(0)

text = (HERE/'REVIEW_CN_v3.5.8.md').read_text(encoding='utf-8')
oldtext = before('REVIEW_CN_v3.5.7.md').decode('utf-8')
body,bib = text.split('## 参考文献',1)
oldbody,oldbib = oldtext.split('## 参考文献',1)
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.8.csv')
oldreg=oldrows('references/REFERENCE_REGISTER_v3.5.7.csv')
by_id={r['stable_id']:r for r in reg}; old_id={r['stable_id']:r for r in oldreg}
by_num={int(r['v358_number']):r for r in reg}
locations=rows(HERE/'references/CITATION_LOCATIONS_v3.5.8.csv')
claims=rows(HERE/'references/REVISION_EVIDENCE_v3.5.8.csv')
comparisons=rows(HERE/'references/COMPARISON_LOCATIONS_v3.5.8.csv')
boundaries=rows(HERE/'references/SCIENTIFIC_BOUNDARIES_v3.5.8.csv')
integration=rows(HERE/'references/SOURCE_INTEGRATION_v3.5.8.csv')
metrics=json.loads((HERE/'audit/REVISION_METRICS.json').read_text(encoding='utf-8'))
clarifications=json.loads((HERE/'references/TARGETED_CLARIFICATIONS_v3.5.8.json').read_text(encoding='utf-8'))
checks={}
errata=json.loads((HERE/'audit/ERRATA_20261026.json').read_text(encoding='utf-8'))
initial_bytes=subprocess.check_output(['git','show',errata['baseline_commit']+':'+PREFIX+'REVIEW_CN_v3.5.8.md'],cwd=ROOT)
expected_errata=initial_bytes.decode('utf-8')
for edit in errata['edits']:
    assert expected_errata.count(edit['before'])==1
    expected_errata=expected_errata.replace(edit['before'],edit['after'])
restored=text
for edit in reversed(errata['edits']):
    assert restored.count(edit['after'])==1
    restored=restored.replace(edit['after'],edit['before'])
initial_body=restored.split('## 参考文献',1)[0]
checks['exactly_three_errata_and_all_other_manuscript_bytes_unchanged']=len(errata['edits'])==3 and text==expected_errata and restored.encode('utf-8')==initial_bytes and sha(initial_bytes)==errata['baseline_manuscript_sha256'] and sha(text.encode('utf-8'))==errata['current_manuscript_sha256'] and text.count('\n')==restored.count('\n')
errata_diff=''.join(difflib.unified_diff(initial_bytes.decode('utf-8').splitlines(True),text.splitlines(True),fromfile='V3.5.8-initial/REVIEW_CN_v3.5.8.md',tofile='V3.5.8-errata/REVIEW_CN_v3.5.8.md'))
checks['errata_diff_and_source_locations_exact']=(HERE/'audit/V3.5.8_TO_ERRATA_20261026.diff').read_text(encoding='utf-8')==errata_diff and all(e['after'] in body.splitlines()[e['line']-1] and by_id[e['source_id']]['v358_number']==str(e['reference_number']) for e in errata['edits'])
checks['title_headings_and_five_chapters_preserved']=re.findall(r'^#{1,4} .+$',body,re.M)==re.findall(r'^#{1,4} .+$',oldbody,re.M)
checks['120_source_identities_numbers_versions_and_human_states_preserved']=len(reg)==len(by_id)==120 and set(by_id)==set(old_id) and all(r['v358_number']==r['v357_number']==old_id[s]['v357_number'] and all(r[k]==old_id[s][k] for k in ['reference_text','actual_version','version_resolution','actual_source_url','version_record_path','human_verified']) for s,r in by_id.items())
checks['bibliography_unchanged_and_register_exact']=bib==oldbib and re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v358_number'],r['reference_text']) for r in reg]
observed=[];first=[];bad=[];sec=''
for ln,line in enumerate(body.splitlines(),1):
    heading=re.match(r'^#{2,4} (\d+(?:\.\d+)*) ',line)
    if heading:sec=heading.group(1)
    kind='table' if line.startswith('|') else 'table_note' if re.match(r'^注\d+：',line) else 'figure_caption' if re.match(r'^图\d',line) else 'narrative'
    for match in re.finditer(r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]',line):
        for part in match.group(1).split(','):
            bounds=re.split('[–—-]',part)
            for n in range(int(bounds[0]),int(bounds[-1])+1):
                if n not in by_num:bad.append(n);continue
                if n not in first:first.append(n)
                observed.append({'stable_id':by_num[n]['stable_id'],'v358_number':str(n),'v357_number':str(n),'line':str(ln),'section':sec,'context_kind':kind})
checks['citation_numbers_order_and_locations_exact']=not bad and first==list(range(1,121)) and locations==observed
mapping=rows(HERE/'references/NUMBER_MAP_v3.5.7_TO_v3.5.8.csv')
checks['number_map_and_source_record_paths_resolve']=len(mapping)==120 and all(r['v358_number']==r['v357_number']==by_id[r['stable_id']]['v358_number'] for r in mapping) and all((ROOT/r['version_record_path']).is_file() for r in reg)
claim_errors=[]
for r in claims:
    ids=r['stable_source_ids'].split(';')
    if not set(ids)<=set(by_id):claim_errors.append([r['claim_id'],'source IDs']);continue
    if r['current_numbers']!=';'.join(by_id[s]['v358_number'] for s in ids):claim_errors.append([r['claim_id'],'number mapping'])
    record=HERE/r['evidence_record']
    if not record.is_file() or not all(e in record.read_text(encoding='utf-8') for e in r['evidence_ids'].split(';')):claim_errors.append([r['claim_id'],'evidence record'])
    if sha(r['claim_summary'].encode())!=r['claim_sha256']:claim_errors.append([r['claim_id'],'hash'])
    if r['current_lines']!=';'.join(str(i) for i,l in enumerate(body.splitlines(),1) if r['anchor'] in l):claim_errors.append([r['claim_id'],'anchor'])
checks['seven_changed_claims_traceable']=len(claims)==7 and not claim_errors
oldcomp={r['inherited_check_id']:r for r in oldrows('references/COMPARISON_LOCATIONS_v3.5.7.csv')}
checks['four_inherited_comparisons_retained_with_updated_locations']=len(comparisons)==4 and all(r['values_json']==oldcomp[r['inherited_check_id']]['values_json'] and r['source_locator']==oldcomp[r['inherited_check_id']]['source_locator'] and (HERE/r['inherited_record']).is_file() and r['anchor'] in body.splitlines()[int(r['current_line'])-1] for r in comparisons)
oldbounds={r['baseline_boundary_id']:r for r in oldrows('references/SCIENTIFIC_BOUNDARIES_v3.5.7.csv')}
checks['23_inherited_scientific_boundaries_preserved']=len(boundaries)==23 and all(all(r[k]==oldbounds[r['baseline_boundary_id']][k] for k in ['preserved_scientific_meaning','stable_source_ids','inherited_record_paths','inherited_evidence_ids','human_verified','current_disposition']) for r in boundaries)
checks['26_historical_adoptions_retain_sources_and_current_locations']=len(integration)==26 and {r['stable_id'] for r in integration}=={r['stable_id'] for r in oldrows('references/SOURCE_INTEGRATION_v3.5.7.csv')} and all(r['narrative_citation_lines']==';'.join(x['line'] for x in locations if x['stable_id']==r['stable_id'] and x['context_kind']=='narrative') for r in integration)
data=rows(HERE/'references/E013_TABLE2_DATA_v3.5.8.csv')
tally=json.loads((HERE/'references/E013_TABLE2_TALLY_v3.5.8.json').read_text(encoding='utf-8'))
groups={}
for group in ['all','static','dynamic']:
    valid=[r for r in data if r['MCRP_reward'] and (group=='all' or r['target_group']==group)]
    result={'numeric_denominator':len(valid)}
    for method in ['MP','RHP']:
        result[method+'_vs_MCRP']={name:[int(r['instance']) for r in valid if fn(int(r[method+'_reward']),int(r['MCRP_reward']))] for name,fn in [('higher',lambda a,b:a>b),('lower',lambda a,b:a<b),('equal',lambda a,b:a==b)]}
    groups[group]=result
checks['24_table_rows_and_23_pair_denominator_recomputed']=len(data)==24 and [int(r['instance']) for r in data]==list(range(1,25)) and groups==tally['groups'] and groups['all']['numeric_denominator']==23 and data[9]['MCRP_status']=='OUT_OF_MEMORY_NA' and data[9]['MCRP_reward']=='' and tally['excluded_numeric_comparison']==[10]
checks['reported_counts_counterexample_and_failure_match_data']=all(len(groups['all']['RHP_vs_MCRP'][k])==n for k,n in [('higher',7),('lower',12),('equal',4)]) and all(len(groups['all']['MP_vs_MCRP'][k])==n for k,n in [('higher',5),('lower',18),('equal',0)]) and [data[12][k] for k in ['MCRP_reward','MP_reward','RHP_reward','MCRP_runtime_s','MP_runtime_s','RHP_runtime_s']]==['4613','4581','4589','46.03','0.14','27.38'] and all(t in body for t in ['4613/4581/4589','46.03/0.14/27.38','7个较高、12个较低、4个相同','5个较高、18个较低、0个相同','实例10的MCRP因内存不足返回N/A'])
checks['original_positive_negative_results_and_budgets_preserved']=all(t in body for t in ['2356/2335/2356','4610/4584/4656','32.53/0.03/13.62','10 800 s（限时）/0.04/5942.12','6个实例启发式较好、10个略差、2个相同','26.21%','1.77%','462.24','每个子问题限时3600 s','累积运行时间','不能当作等计算预算','奖励按覆盖计算','负值目标的符号约定'])
checks['graphical_baseline_scope_explicit_without_fabricated_order']=all(t in body for t in ['JOTSAS分别优化观测、传输资源','在这一模型和所测期限内','图6仅呈现曲线，未列数值表','不给出精确差值或百分比','未展开分开优化时的变量固定方式和求解次序'])
checks['gsoc_event_proxy_and_direct_service_distinguished']=all(t in body for t in ['GSOC个案已将同一次在轨处置中的机动实施与构型变化联系起来','未报告对应事件的直接交付或业务损失测量','而非完全缺少连贯的事件记录','将处置过程与直接业务结果连接后']) and '表内没有一行经所引证据确认' not in body
checks['conclusion_and_abstract_not_upgraded_to_general_rules']=body.count('普遍适用的事前选择阈值尚待研究')==2 and '尚无普遍适用的事前选择阈值，相关问题见4.5.1' in body and '比单一总星数更能解释' not in body and all(t in body for t in ['在三颗观测星、12小时仿真及所测业务期限内','three observation satellites over a 12-hour simulation','only in some instances','组织建议仍属于条件性综合'])
checks['unchanged_chapters_and_sections_exact']=all(span(initial_body,a,b)==span(oldbody,a,b) for a,b in [('## 1 引言','#### 4.2.2 '),('#### 4.2.3 ','#### 4.4.4 '),('### 4.5 ','## 5 结论')])
checks['table8_and_non_gsoc_table9_rows_unchanged']=table(body,8)==table(oldbody,8) and '\n'.join(l for l in table(body,9).splitlines() if 'GSOC TanDEM-X' not in l)=='\n'.join(l for l in table(oldbody,9).splitlines() if 'GSOC TanDEM-X' not in l)
figs=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['nine_tables_four_original_figures_retained']=re.findall(r'^\*\*表([1-9]) ',body,re.M)==list('123456789') and len(figs)==4 and all((HERE/f).read_bytes()==before(f) for f in figs)
checks['table_columns_consistent']=all(len({len(l.split('|')) for l in t.strip().splitlines()})==1 for t in re.findall(r'(?:^\|.*\n)+',body,re.M))
checks['clarification_source_hashes_and_identity_records_match']=len(clarifications['checks'])==3 and all(sha(Path(r['local_pdf']).read_bytes())==r['sha256'] and by_id[r['stable_id']]['v358_number']==str(r['number']) for r in clarifications['checks'])
selection=rows(ROOT/'review_writing/manuscripts/v3.5.4-cn/references/SOURCE_SELECTION_v3.5.4.csv')
holds=[r for r in selection if r['reading_id'] in {'S045','L071'}]
checks['hold_and_human_states_not_upgraded']=len(holds)==2 and all('HOLD' in r['decision'] and not r['v354_number'] for r in holds) and all(r['human_verified']=='false' for r in reg+claims+comparisons+boundaries+integration) and all(r['human_verified'] is False and r['formal_pairing_newly_closed'] is False for r in clarifications['checks'])
checks['baseline_bytes_and_branch_preserved']=(ROOT/OLD/'REVIEW_CN_v3.5.7.md').read_bytes()==before('REVIEW_CN_v3.5.7.md') and git('branch','--show-current')==BRANCH and git('merge-base',BASE,'HEAD')==BASE
changes=git('diff',BASE,'--name-only').splitlines()
# Preserve the two-column porcelain prefix, including an initial blank status column.
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=ROOT).decode('utf-8').splitlines()
checks['only_new_version_directory_changes']=all(p.startswith(PREFIX) for p in changes) and all(r[3:].startswith(PREFIX) for r in status)
expected=''.join(difflib.unified_diff(oldtext.splitlines(True),text.splitlines(True),fromfile='V3.5.7/REVIEW_CN_v3.5.7.md',tofile='V3.5.8/REVIEW_CN_v3.5.8.md'))
checks['diff_metrics_and_manuscript_hash_exact']=(HERE/'audit/V3.5.7_TO_V3.5.8.diff').read_text(encoding='utf-8')==expected and metrics['body_han_before']==len(re.findall('[\u4e00-\u9fff]',oldbody)) and metrics['body_han_after']==len(re.findall('[\u4e00-\u9fff]',body)) and metrics['manuscript_sha256']==sha(text.encode())
missing=[]
for name in ['README_CN.md','SCIENTIFIC_REVISION_CN.md','REVISION_RESPONSE_CN.md','REFERENCE_INTEGRATION_CN.md','REVIEW_CN_v3.5.8.md','ERRATA_CN.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in dest and not dest.startswith('#') and dest!='VALIDATION_REPORT.json' and not (HERE/dest).is_file():missing.append(dest)
checks['delivery_links_resolve']=not missing
report={'status':'PASS' if all(checks.values()) else 'FAIL','baseline_commit':BASE,'branch':BRANCH,
        'scope':'Necessary citation, source, tally, prose-scope and file consistency; not independent scientific review or author approval.',
        'errata_baseline_commit':errata['baseline_commit'],'errata_edit_count':3,'author_freeze_confirmation':'PENDING',
        'references_before':120,'references_after':120,'references_added':0,'references_removed':0,'new_unique_full_text_readings':0,
        'targeted_existing_source_clarifications':3,'descriptive_existing_table_tallies':1,'new_experiments':0,'human_verified':False,'submission_ready':False,
        'EC2026_full_text_obtained':False,'L042_formal_pairing_closed':False,'L042_figure16_24_pixel_review_completed':False,
        'matched_net_service_recovery_benefit_proven':False,'figures_redrawn':0,'body_han_before':metrics['body_han_before'],'body_han_after':metrics['body_han_after'],
        'manuscript_sha256':metrics['manuscript_sha256'],'checks':checks,'claim_errors':claim_errors,'missing_links':missing}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],'claim_errors':claim_errors,'missing_links':missing},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
