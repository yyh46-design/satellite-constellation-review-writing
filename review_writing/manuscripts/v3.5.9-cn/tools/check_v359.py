"""Bounded manuscript consistency checks; not an author scientific review."""
from pathlib import Path
import collections, csv, difflib, hashlib, io, json, re, subprocess

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
BASE='d408fd5b657b04278dac0d6b3965d1b517cb8341'
OLD='review_writing/manuscripts/v3.5.8-cn/'
PREFIX='review_writing/manuscripts/v3.5.9-cn/'
BRANCH='writing/constellation-review-v359-cn-expression-20261026'
PAT=r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]'

def rawgit(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
def git(*args): return rawgit(*args).decode('utf-8').strip()
def oldbytes(name):return rawgit('show',BASE+':'+OLD+name)
def rows(path):return list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
def oldrows(name):return list(csv.DictReader(io.StringIO(oldbytes(name).decode('utf-8-sig'))))
def sha(b):return hashlib.sha256(b).hexdigest()
def span(s,start,end):return s[s.index(start):s.index(end,s.index(start))]
def numbers(s):
    result=[]
    for group in re.findall(PAT,s):
        for part in group.split(','):
            ends=re.split('[–—-]',part)
            result.extend(range(int(ends[0]),int(ends[-1])+1))
    return result
def table(s,n):return re.search(r'^\*\*表'+str(n)+r' .+?\*\*\n\n((?:\|.*\n)+)',s,re.M).group(0)
def han(s):return len(re.findall('[\u4e00-\u9fff]',s))

text=(HERE/'REVIEW_CN_v3.5.9.md').read_text(encoding='utf-8')
old=oldbytes('REVIEW_CN_v3.5.8.md').decode('utf-8')
body,bib=text.split('## 参考文献',1);oldbody,oldbib=old.split('## 参考文献',1)
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.9.csv')
prior=oldrows('references/REFERENCE_REGISTER_v3.5.8.csv')
byid={r['stable_id']:r for r in reg};oldid={r['stable_id']:r for r in prior};bynum={int(r['v359_number']):r for r in reg}
locations=rows(HERE/'references/CITATION_LOCATIONS_v3.5.9.csv')
boundaries=rows(HERE/'references/SCIENTIFIC_BOUNDARIES_v3.5.9.csv')
claims=rows(HERE/'references/REVISION_EVIDENCE_v3.5.9.csv')
comparisons=rows(HERE/'references/COMPARISON_LOCATIONS_v3.5.9.csv')
adoptions=rows(HERE/'references/SOURCE_INTEGRATION_v3.5.9.csv')
edits=json.loads((HERE/'audit/EDIT_LOG_v3.5.9.json').read_text(encoding='utf-8'))
metrics=json.loads((HERE/'audit/REVISION_METRICS.json').read_text(encoding='utf-8'))
protected=json.loads((HERE/'references/PROTECTED_PASSAGES_v3.5.9.json').read_text(encoding='utf-8'))
checks={}
checks['five_chapters_all_headings_title_and_3_1_to_3_6_preserved']=re.findall(r'^#{1,4} .+$',body,re.M)==re.findall(r'^#{1,4} .+$',oldbody,re.M)
checks['120_source_ids_numbers_versions_and_human_states_preserved']=len(reg)==len(byid)==120 and set(byid)==set(oldid) and all(r['v359_number']==r['v358_number']==oldid[s]['v358_number'] and all(r[k]==oldid[s][k] for k in ['reference_text','actual_version','version_resolution','actual_source_url','version_record_path','human_verified']) for s,r in byid.items())
checks['entire_bibliography_unchanged_and_register_exact']=bib==oldbib and re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v359_number'],r['reference_text']) for r in reg]
checks['full_citation_order_unchanged']=re.findall(PAT,body)==re.findall(PAT,oldbody) and set(numbers(body))==set(range(1,121))
observed=[];sec=''
for ln,line in enumerate(body.splitlines(),1):
    heading=re.match(r'^#{2,4} (\d+(?:\.\d+)*) ',line)
    if heading:sec=heading.group(1)
    kind='table' if line.startswith('|') else 'table_note' if re.match(r'^注\d+：',line) else 'figure_caption' if re.match(r'^图\d',line) else 'narrative'
    for n in numbers(line):observed.append({'stable_id':bynum[n]['stable_id'],'v359_number':str(n),'v358_number':str(n),'line':str(ln),'section':sec,'context_kind':kind})
checks['citation_locations_exact']=locations==observed
checks['source_evidence_paths_resolve']=all((ROOT/r['version_record_path']).is_file() for r in reg)
replay=old
for e in edits:
    assert replay.count(e['before'])==1,e['edit_id']
    replay=replay.replace(e['before'],e['after'],1)
checks['all_37_editorial_changes_replay_exactly']=len(edits)==37 and replay==text and all(sha(e['before'].encode())==e['baseline_text_sha256'] and sha(e['after'].encode())==e['revised_text_sha256'] and old[:old.index(e['before'])].count('\n')+1==e['baseline_start_line'] and text[:text.index(e['after'])].count('\n')+1==e['current_start_line'] for e in edits)
chapter_nums=lambda s:collections.Counter(re.findall(r'\d+(?:\.\d+)?',re.sub(PAT,'',span(s,'## 1 引言','## 5 结论'))))
checks['chapter_1_to_4_numeric_tokens_unchanged']=chapter_nums(text)==chapter_nums(old)
checks['14_key_evidence_passages_byte_identical']=len(protected)==14 and all(span(text,p['start'],p['end'])==span(old,p['start'],p['baseline_end']) and sha(span(text,p['start'],p['end']).encode())==p['sha256'] for p in protected)
checks['tables_7_8_9_and_numeric_notes_unchanged']=all(table(body,n)==table(oldbody,n) for n in [7,8,9]) and span(text,'注1：[10]','#### 4.2.3 ')==span(old,'注1：[10]','#### 4.2.3 ')
oldbounds={r['boundary_id']:r for r in oldrows('references/SCIENTIFIC_BOUNDARIES_v3.5.8.csv')}
checks['23_historical_scientific_boundaries_retained']=len(boundaries)==23 and all(all(r[k]==oldbounds[r['v358_boundary_id']][k] for k in ['baseline_boundary_id','preserved_scientific_meaning','stable_source_ids','inherited_record_paths','inherited_evidence_ids','human_verified','current_disposition']) for r in boundaries)
oldclaims={r['claim_id']:r for r in oldrows('references/REVISION_EVIDENCE_v3.5.8.csv')}
claim_errors=[]
for r in claims:
    earlier=oldclaims[r['inherited_claim_id']]
    if not all(r[k]==earlier[k] for k in ['claim_summary','claim_sha256','claim_kind','stable_source_ids','current_numbers','evidence_ids','human_verified','new_unique_reading_credit']):claim_errors.append([r['claim_id'],'inherited proposition changed'])
    if sha(r['claim_summary'].encode())!=r['claim_sha256']:claim_errors.append([r['claim_id'],'hash'])
    if r['current_lines']!=';'.join(str(i) for i,l in enumerate(body.splitlines(),1) if r['anchor'] in l):claim_errors.append([r['claim_id'],'anchor'])
    target=HERE/r['evidence_record']
    if not target.is_file() or not all(e in target.read_text(encoding='utf-8') for e in r['evidence_ids'].split(';')):claim_errors.append([r['claim_id'],'source pointer'])
checks['seven_existing_claims_and_source_locations_retained']=len(claims)==7 and not claim_errors
oldcomp={r['inherited_check_id']:r for r in oldrows('references/COMPARISON_LOCATIONS_v3.5.8.csv')}
checks['four_within_study_comparisons_and_source_values_retained']=len(comparisons)==4 and all(r['values_json']==oldcomp[r['inherited_check_id']]['values_json'] and r['source_locator']==oldcomp[r['inherited_check_id']]['source_locator'] and r['anchor'] in body.splitlines()[int(r['current_line'])-1] and (HERE/r['inherited_record']).is_file() for r in comparisons)
checks['26_historical_adoptions_and_current_lines_retained']=len(adoptions)==26 and {r['stable_id'] for r in adoptions}=={r['stable_id'] for r in oldrows('references/SOURCE_INTEGRATION_v3.5.8.csv')} and all(r['narrative_citation_lines']==';'.join(x['line'] for x in locations if x['stable_id']==r['stable_id'] and x['context_kind']=='narrative') for r in adoptions)
data=oldrows('references/E013_TABLE2_DATA_v3.5.8.csv');valid=[r for r in data if r['MCRP_reward']]
tally={method:{label:sum(fn(int(r[method+'_reward']),int(r['MCRP_reward'])) for r in valid) for label,fn in [('higher',lambda a,b:a>b),('lower',lambda a,b:a<b),('equal',lambda a,b:a==b)]} for method in ['RHP','MP']}
checks['existing_24_row_counts_failures_and_counterexample_retained']=len(data)==24 and len(valid)==23 and data[9]['MCRP_status']=='OUT_OF_MEMORY_NA' and tally=={'RHP':{'higher':7,'lower':12,'equal':4},'MP':{'higher':5,'lower':18,'equal':0}} and all(s in body for s in ['4613/4581/4589','46.03/0.14/27.38','7个较高、12个较低、4个相同','5个较高、18个较低、0个相同','实例10的MCRP因内存不足返回N/A','6个实例启发式较好、10个略差、2个相同','26.21%','1.77%','462.24'])
checks['rta_counterexample_information_and_failure_scope_retained']=all(s in body for s in ['相同2000组五星初态','分散实现通过率为90.95%','两者均取得全部成员状态','区别包括能否共同选择输入','失败含约束违反或无可行输入','不能一律解释为实体碰撞','碰撞数中位数却未变化','到达指标允许碰撞后继续累计'])
checks['new_summary_retains_conditions_not_universal_dominance']=all(s in body for s in ['在所测期限内','完整模型亦有占优实例','事前选择阈值尚待研究','完整任务—轨道—安全过程的组织建议仍属条件性综合','given orbits','only in some instances','full models also perform better in others','recommendations for the complete task–orbit–safety process remain conditional']) and '更能解释局部机制' not in body
checks['gsoc_and_recovery_event_scope_retained']=all(s in body for s in ['四类结果可以交叠','依据构型偏差推断SAR运行未受影响','未报告对应事件的直接交付或业务损失测量','缺口在于将同一在轨处置过程连接到直接业务结果','还需同条件比较才能判断不同恢复路径的净收益'])
checks['scope_selection_and_large_scale_bridge_present']=all(s in body for s in ['问题导向的叙述性综述','不主张检索穷尽性','未形成可复现的统一数据库检索式和完整排除流程','出版社与期刊页面、预印本服务器','不设单一星数门槛','小规模研究用于解释局部机制','这些结构计数不是求解时间或安全性能的增长定律'])
figs=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['nine_tables_and_four_original_figures']=re.findall(r'^\*\*表([1-9]) ',body,re.M)==list('123456789') and len(figs)==4 and all((HERE/f).read_bytes()==oldbytes(f) for f in figs)
checks['figure_captions_unchanged']=re.findall(r'^图\d .+$',body,re.M)==re.findall(r'^图\d .+$',oldbody,re.M)
checks['table_columns_consistent']=all(len({len(l.split('|')) for l in t.strip().splitlines()})==1 for t in re.findall(r'(?:^\|.*\n)+',body,re.M))
selection=rows(ROOT/'review_writing/manuscripts/v3.5.4-cn/references/SOURCE_SELECTION_v3.5.4.csv')
holds=[r for r in selection if r['reading_id'] in {'S045','L071'}]
checks['hold_and_human_states_not_upgraded']=len(holds)==2 and all('HOLD' in r['decision'] and not r['v354_number'] for r in holds) and all(r['human_verified']=='false' for r in reg+boundaries+claims+comparisons+adoptions) and metrics['human_verified'] is False and metrics['submission_ready'] is False and metrics['author_freeze_confirmation']=='PENDING'
changed=git('diff',BASE,'--name-only').splitlines()
status=rawgit('status','--porcelain','--untracked-files=all').decode('utf-8').splitlines()
checks['only_v359_directory_changed']=all(p.startswith(PREFIX) for p in changed) and all(s[3:].startswith(PREFIX) for s in status)
checks['v358_baseline_tree_bytes_preserved']=all((ROOT/p).read_bytes()==rawgit('show',BASE+':'+p) for p in git('ls-tree','-r','--name-only',BASE,'--',OLD).splitlines()) and git('branch','--show-current')==BRANCH and git('merge-base',BASE,'HEAD')==BASE
expected=''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='V3.5.8/REVIEW_CN_v3.5.8.md',tofile='V3.5.9/REVIEW_CN_v3.5.9.md'))
checks['diff_counts_and_hashes_exact']=(HERE/'audit/V3.5.8_TO_V3.5.9.diff').read_text(encoding='utf-8')==expected and metrics['manuscript_sha256']==sha(text.encode()) and metrics['baseline_manuscript_sha256']==sha(old.encode()) and metrics['body_han_before']==han(oldbody) and metrics['body_han_after']==han(body)
missing=[]
for name in ['README_CN.md','SCIENTIFIC_REVISION_CN.md','REVISION_RESPONSE_CN.md','REFERENCE_INTEGRATION_CN.md','REVIEW_CN_v3.5.9.md']:
    for link in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in link and not link.startswith('#') and link!='VALIDATION_REPORT.json' and not (HERE/link).is_file():missing.append(link)
checks['delivery_and_inherited_record_links_resolve']=not missing
report={
    'status':'PASS' if all(checks.values()) else 'FAIL','baseline_commit':BASE,'branch':BRANCH,
    'scope':'Editorial consistency, evidence preservation and file identity; not independent source verification or author scientific approval.',
    'references_before':120,'references_after':120,'references_added':0,'references_removed':0,
    'new_unique_full_text_readings':0,'new_experiments':0,'formal_pairings_newly_closed':0,
    'human_verified':False,'submission_ready':False,'author_freeze_confirmation':'PENDING',
    'manuscript_sha256':sha(text.encode()),'checks':checks,'claim_errors':claim_errors,'missing_links':missing
}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],'claim_errors':claim_errors,'missing_links':missing},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
