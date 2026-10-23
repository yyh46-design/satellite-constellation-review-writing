"""Necessary consistency checks; this does not approve scientific claims or submission."""
from pathlib import Path
from collections import Counter
import csv, hashlib, io, json, re, subprocess

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
BASE='fc97c754d21fabc1357da0f5c97e9c2ba7249cd3'
OLD='review_writing/manuscripts/v3.5.4-cn'
PREFIX='review_writing/manuscripts/v3.5.5-cn/'
BRANCH='writing/constellation-review-v355-conditional-synthesis-20261023'

def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').rstrip('\r\n')
def oldfile(name):return subprocess.check_output(['git','show',f'{BASE}:{OLD}/{name}'],cwd=ROOT)
def rows(path):return list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
pattern=re.compile(r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]')
def numbers(group):
    result=[]
    for part in group.split(','):
        bounds=re.split('[–—-]',part);result.extend(range(int(bounds[0]),int(bounds[-1])+1))
    return result

text=(HERE/'REVIEW_CN_v3.5.5.md').read_text(encoding='utf-8')
body,bib=text.split('## 参考文献',1)
oldtext=oldfile('REVIEW_CN_v3.5.4.md').decode('utf-8');oldbody=oldtext.split('## 参考文献',1)[0]
reg=rows(HERE/'references/REFERENCE_REGISTER_v3.5.5.csv')
oldreg=list(csv.DictReader(io.StringIO(oldfile('references/REFERENCE_REGISTER_v3.5.4.csv').decode('utf-8-sig'))))
by_id={r['stable_id']:r for r in reg};by_number={int(r['v355_number']):r for r in reg};by_old={r['stable_id']:r for r in oldreg}
integration=rows(HERE/'references/SOURCE_INTEGRATION_v3.5.5.csv')
locations=rows(HERE/'references/CITATION_LOCATIONS_v3.5.5.csv')
mapping=rows(HERE/'references/NUMBER_MAP_v3.5.4_TO_v3.5.5.csv')
boundaries=rows(HERE/'references/SCIENTIFIC_BOUNDARIES_v3.5.5.csv')
evidence=rows(HERE/'references/SYNTHESIS_EVIDENCE_v3.5.5.csv')
selection=rows(HERE/'references/SOURCE_SELECTION_v3.5.4.csv')
checks={}
checks['title_five_chapters_and_3_1_to_3_6_scope_preserved']=(body.splitlines()[0]==oldbody.splitlines()[0] and re.findall(r'^## [1-5] .+$',body,re.M)==re.findall(r'^## [1-5] .+$',oldbody,re.M) and re.findall(r'^### 3\.[1-6] .+$',body,re.M)==re.findall(r'^### 3\.[1-6] .+$',oldbody,re.M))
checks['120_stable_sources_no_additions_or_removals']=len(reg)==len(by_id)==120 and set(by_id)==set(by_old)
fields=['reference_text','actual_version','version_resolution','actual_source_url','version_record_path','human_verified']
checks['source_versions_reference_text_and_human_status_unchanged']=all(all(row[field]==by_old[sid][field] for field in fields) for sid,row in by_id.items())
checks['bibliography_matches_current_register']=re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v355_number'],r['reference_text']) for r in reg]
checks['number_map_resolves_all_120_stable_ids']=len(mapping)==120 and all(row['stable_id'] in by_id and row['v354_number']==by_id[row['stable_id']]['v354_number'] and row['v355_number']==by_id[row['stable_id']]['v355_number'] for row in mapping)
first=[];observed=[];bad=[];current='';narrative={sid:[] for sid in by_id};used_sections={sid:set() for sid in by_id}
for line_number,line in enumerate(body.splitlines(),1):
    heading=re.match(r'^#{2,4} (\d+(?:\.\d+)*) ',line)
    if heading:current=heading.group(1)
    kind='table' if line.startswith('|') else 'figure_caption' if re.match(r'^图\d',line) else 'narrative'
    for match in pattern.finditer(line):
        for n in numbers(match.group(1)):
            if n not in by_number:bad.append(n);continue
            if n not in first:first.append(n)
            row=by_number[n];sid=row['stable_id'];used_sections[sid].add(current)
            observed.append((sid,str(n),row['v354_number'],str(line_number),current,kind))
            if kind=='narrative':narrative[sid].append(str(line_number))
checks['all_120_cited_in_first_occurrence_order']=not bad and first==list(range(1,121))
checks['citation_location_record_matches_current_text']=observed==[(r['stable_id'],r['v355_number'],r['v354_number'],r['line'],r['section'],r['context_kind']) for r in locations]
oldintegration=list(csv.DictReader(io.StringIO(oldfile('references/SOURCE_INTEGRATION_v3.5.4.csv').decode('utf-8-sig'))))
checks['prior_26_adoptions_remain_same_sources_and_cohorts']=(len(integration)==26 and {r['stable_id'] for r in integration}=={r['stable_id'] for r in oldintegration} and Counter(r['cohort'] for r in integration)=={'HISTORICAL_TARGETED_BODY_READING':11,'B11_B20_COMPLETED_BODY_READING':15})
checks['prior_26_have_updated_narrative_locations']=all(narrative[r['stable_id']] and r['narrative_citation_lines'].split(';')==narrative[r['stable_id']] and set(r['current_sections'].split(';'))==used_sections[r['stable_id']] for r in integration)
binding_errors=[]
for r in integration:
    paths=[ROOT/p for p in r['reading_note_paths'].split(';')]
    if not all(p.is_file() for p in paths):binding_errors.append((r['stable_id'],'missing note'));continue
    corpus='\n'.join(p.read_text(encoding='utf-8-sig') for p in paths)
    for cid in r['existing_claim_ids_used'].split(';'):
        if cid not in corpus:binding_errors.append((r['stable_id'],cid))
checks['prior_adoption_claim_ids_and_source_records_resolve']=not binding_errors and all((ROOT/r['version_record_path']).is_file() for r in reg)
evidence_errors=[]
for r in evidence:
    paths=[ROOT/p for p in r['inherited_record_paths'].split(';')]
    ids=set(r['stable_source_ids'].split(';'))
    if not ids<=set(by_id) or not paths or not all(p.is_file() for p in paths):evidence_errors.append((r['synthesis_id'],'missing binding'));continue
    corpus='\n'.join(p.read_text(encoding='utf-8-sig') for p in paths)
    if r['existing_claim_ids']:
        for cid in r['existing_claim_ids'].split(';'):
            if cid not in corpus:evidence_errors.append((r['synthesis_id'],cid))
    if not r['current_citation_lines']:evidence_errors.append((r['synthesis_id'],'missing current location'))
    if hashlib.sha256(r['claim_summary'].encode()).hexdigest()!=r['claim_sha256']:evidence_errors.append((r['synthesis_id'],'claim hash mismatch'))
checks['18_synthesis_and_recovery_record_bindings_resolve']=len(evidence)==18 and not evidence_errors
checks['23_inherited_boundaries_record_current_disposition']=len(boundaries)==23 and len({r['baseline_boundary_id'] for r in boundaries})==23 and all(set(r['stable_source_ids'].split(';'))<=set(by_id) and r['current_sections'] and r['human_verified']=='false' for r in boundaries) and next(r for r in boundaries if r['baseline_boundary_id']=='V354-P12')['current_disposition']=='NARROWED_TO_READ_MODEL_AND_WITHDREW_FIGURE_DEPENDENT_EXAMPLE'
checks['historical_records_copied_verbatim']=all((HERE/'references'/name).read_bytes()==oldfile('references/'+name) for name in ['SCIENTIFIC_BOUNDARIES_v3.5.4.csv','SOURCE_SELECTION_v3.5.4.csv','TARGETED_RECHECKS_v3.5.4.json'])
holds=[r for r in selection if r['reading_id'] in {'S045','L071'}]
checks['reserve_and_hold_states_not_upgraded']=len(selection)==195 and len(holds)==2 and all('HOLD' in r['decision'] and not r['v354_number'] for r in holds)
checks['time_window_equation_preserved']=re.findall(r'\$\$(.*?)\$\$',body,re.S)==re.findall(r'\$\$(.*?)\$\$',oldbody,re.S)
figures=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['nine_tables_four_unchanged_png_assets']=re.findall(r'^\*\*表([1-9]) ',body,re.M)==list('123456789') and len(figures)==4 and all((HERE/f).read_bytes()==oldfile(f) for f in figures) and 'AI辅助定性草图，非数值结果' in body
checks['known_validation_scales_and_denominators_retained']=all(value in body for value in ['2000','90.95%','10星','50星','24 023','100星','35星','24星'])
checks['historical_years_match_existing_bibliography']=all(year in by_old[sid]['reference_text'] for sid,year in [('E030','2002'),('E-B20-L024','2012'),('E011','2014'),('E012','2023'),('E013','2025'),('E108','1998')])
protected=json.loads((HERE/'audit/BASELINE_IDENTITY.json').read_text(encoding='utf-8'))['protected_refs']
current_refs=git('for-each-ref','--format=%(refname) %(objectname)','refs/heads/main','refs/remotes/origin/main','refs/heads/writing/constellation-review-v354-literature-synthesis-20261023','refs/heads/writing/constellation-management-review-20261009').splitlines()
checks['protected_refs_and_old_manuscripts_unchanged']=protected==current_refs and not git('diff',BASE,'--name-only','--','review_writing/manuscripts/v3.5.4-cn','review_writing/manuscripts/v3.5.3-cn','review_writing/manuscripts/v3.5.2-cn','review_writing/manuscripts/v3.5.1-cn','review_writing/manuscripts/v3.5-cn')
changes=git('diff',BASE,'--name-only').splitlines();status=git('status','--porcelain','--untracked-files=all').splitlines()
checks['only_new_v355_directory_changed']=all(p.startswith(PREFIX) for p in changes) and all(row[3:].startswith(PREFIX) for row in status)
checks['correct_independent_branch_and_fixed_base']=git('branch','--show-current')==BRANCH and git('merge-base',BASE,'HEAD')==BASE
missing_links=[]
for name in ['REVIEW_CN_v3.5.5.md','README_CN.md','REFERENCE_INTEGRATION_CN.md','SCIENTIFIC_REVISION_CN.md','REVISION_RESPONSE_CN.md']:
    for destination in re.findall(r'\]\(([^)]+)\)',(HERE/name).read_text(encoding='utf-8')):
        if '://' not in destination and not destination.startswith('#') and destination!='VALIDATION_REPORT.json' and not (HERE/destination).is_file():missing_links.append(destination)
checks['local_manuscript_and_delivery_links_resolve']=not missing_links
checks['human_approval_and_new_reading_not_claimed']=all(r['human_verified']=='false' for r in reg+integration+boundaries+evidence) and all(r['new_unique_full_text_reading_credit']=='0' for r in integration) and all(r['new_unique_reading_credit']=='0' for r in evidence)
metrics=json.loads((HERE/'audit/REVISION_METRICS.json').read_text(encoding='utf-8'))
checks['metrics_match_current_manuscript']=metrics['manuscript_sha256']==hashlib.sha256((HERE/'REVIEW_CN_v3.5.5.md').read_bytes()).hexdigest() and metrics['body_han_after']==len(re.findall('[\u4e00-\u9fff]',body))
report={
 'status':'PASS' if all(checks.values()) else 'FAIL', 'baseline_commit':BASE,'branch':BRANCH,
 'scope':'Citation, source identity, locator binding, structure and artifact consistency only. These checks do not prove scientific meaning, image correctness, original-paper validation, human approval or submission readiness.',
 'references_before':120,'references_after':len(reg),'references_added':0,'references_removed':0,
 'B11_B20_body_reading_records':97,'B11_B20_sources_now_cited':43,'B11_B20_still_uncited':54,
 'body_han_before':len(re.findall('[\u4e00-\u9fff]',oldbody)),'body_han_after':len(re.findall('[\u4e00-\u9fff]',body)),
 'tables':9,'figures_redrawn':0,'figure_internal_labels_and_pixels_revalidated':False,
 'new_unique_full_text_readings':0,'new_experiments':0,'new_training':0,'human_verified':False,'submission_ready':False,
 'EC2026_full_text_obtained':False,'L042_formal_pairing_closed':False,'L042_figure16_24_pixel_review_completed':False,'matched_net_service_recovery_benefit_proven':False,
 'checks':checks,'binding_errors':binding_errors,'synthesis_binding_errors':evidence_errors,'missing_links':missing_links,
 'manuscript_sha256':hashlib.sha256((HERE/'REVIEW_CN_v3.5.5.md').read_bytes()).hexdigest(),
 'language_counts_for_review_only':{label:{'before':len(re.findall(p,oldbody)),'after':len(re.findall(p,body))} for label,p in [('separate_word','分别'),('limitation_phrases','不能|不等于|不足以|不构成|并非')]},
}
(HERE/'VALIDATION_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[key for key,value in checks.items() if not value],'binding_errors':binding_errors,'synthesis_binding_errors':evidence_errors,'missing_links':missing_links,'body_han_after':report['body_han_after'],'language_counts':report['language_counts_for_review_only']},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
