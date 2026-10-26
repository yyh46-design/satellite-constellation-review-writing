"""Focused editorial preservation checks, adapted from V3.5.9; not scientific approval."""
from pathlib import Path
import collections, csv, difflib, hashlib, io, json, re, subprocess, zipfile

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
PREFIX='review_writing/manuscripts/v3.5.10-cn/'
A='1604e8ac3932019a207d3396e8d447e871b7686c'
B='ba736f833a7888312bc8434acb70c4a04aba614a'
C='d408fd5b657b04278dac0d6b3965d1b517cb8341'
PAT=r'\[(\d+(?:[–—-]\d+)?(?:,\d+(?:[–—-]\d+)?)*)\]'
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
def source(commit,folder,name): return git('show',commit+':review_writing/manuscripts/'+folder+'/'+name)
def table(s,n): return re.search(r'^\*\*表'+str(n)+r' .+?\*\*\n\n(?:\|.*\n)+',s,re.M).group()
def rows(p): return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def refs(s):
 result=[]
 for group in re.findall(PAT,s):
  for part in group.split(','):
   limits=re.split('[–—-]',part)
   result.extend(range(int(limits[0]),int(limits[-1])+1))
 return result
def sha(b): return hashlib.sha256(b).hexdigest()

data=(HERE/'REVIEW_CN_v3.5.10.md').read_bytes(); text=data.decode()
prior=source(A,'v3.5.9-cn','REVIEW_CN_v3.5.9.md').decode()
basebytes=source(C,'v3.5.8-cn','REVIEW_CN_v3.5.8.md'); base=basebytes.decode()
body,bib=text.split('## 参考文献',1); oldbody,oldbib=prior.split('## 参考文献',1)
status=json.loads((HERE/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
reg=rows(HERE/status['source_register']); bynum={int(r['v359_number']):r for r in reg}
checks={}
checks['pinned_inputs']=all(sha(git('show',v['commit']+':'+v['path']))==v['sha256'] for v in status['inputs'].values()) and git('rev-parse',B+'^{tree}').decode().strip()==status['handoff_tree']
checks['five_chapters_and_all_headings']=re.findall(r'^#{1,4} .+$',text,re.M)==re.findall(r'^#{1,4} .+$',base,re.M)
checks['bibliography_bytes_and_120_source_mapping']=data.split('## 参考文献'.encode())[1]==basebytes.split('## 参考文献'.encode())[1] and bib==oldbib and len(reg)==120 and re.findall(r'^(\d+)\. (.+)$',bib,re.M)==[(r['v359_number'],r['reference_text']) for r in reg]
checks['all_340_citation_groups_and_order']=re.findall(PAT,body)==re.findall(PAT,oldbody) and len(re.findall(PAT,body))==340 and set(refs(body))==set(range(1,121))
locations=[]; sec=''
for ln,line in enumerate(body.splitlines(),1):
 heading=re.match(r'^#{2,4} (\d+(?:\.\d+)*) ',line)
 if heading: sec=heading.group(1)
 for n in refs(line): locations.append({'stable_id':bynum[n]['stable_id'],'current_number':str(n),'line':str(ln),'section':sec})
checks['current_citation_map']=rows(HERE/'audit/CITATION_LOCATIONS_v3.5.10.csv')==locations
def numeric_tokens(s):
 s=s[s.index('## 1 引言'):s.index('## 5 结论')]
 # Editorial cross-references are not research values. Their targets are checked below.
 s=re.sub(r'第\d+(?:\.\d+)*(?:[—–-]\d+(?:\.\d+)*)?节|[图表注]\d+','',s)
 return collections.Counter(re.findall(r'\d+(?:\.\d+)?',re.sub(PAT,'',s)))
checks['chapter_1_to_4_numeric_tokens_excluding_cross_references']=numeric_tokens(text)==numeric_tokens(base)
checks['all_math_expressions']=re.findall(r'\$[^$]+\$',body)==re.findall(r'\$[^$]+\$',oldbody)
checks['tables_4_6_7_8_9_and_notes_verbatim']=all(table(text,n)==table(base,n) for n in [4,6,7,8,9]) and re.findall(r'^注[123]：.*$',text,re.M)==re.findall(r'^注[123]：.*$',base,re.M)
figs=re.findall(r'!\[图[1-4]\]\(([^)]+)\)',body)
checks['original_four_images_and_captions']=len(figs)==4 and all((HERE/f).read_bytes()==source(C,'v3.5.8-cn',f) for f in figs) and re.findall(r'^图\d .+$',body,re.M)==re.findall(r'^图\d .+$',oldbody,re.M)
checks['three_errata_retained']=all(s in body for s in ['该历史飓风路径案例与表8所列3—5阶段的算法对照算例不同。','Joint Observation and Transmission Scheduling Algorithm with Agile Satellites，JOTSAS','前视范围的价值需要结合限时求解结果判断。'])
checks['key_comparison_and_recovery_qualifiers']=all(s in body for s in ['给定轨道和所测业务期限','原文图示对照','高于分开优化基线的任务加权完成收益','在各自限时设置和所测实例中','同一联合模型的求解器比较','各方法的时间上限含义不同','尚无普遍适用的事前选择阈值','任务—轨道—安全过程的组织建议仍属条件性综合','相同2000组五星初态','分散实现通过率为90.95%','两者均取得全部成员状态','失败含约束违反或无可行输入','碰撞数中位数却未变化','到达指标允许碰撞后继续累计','硬期限限制可接受的完成时刻','延迟惩罚则将迟到纳入代价','四类结果可以交叠','其他成员也可能先于原轨道恢复接续业务','尚缺对应事件的直接业务结果'])
checks['six_semantic_repairs_and_synchronized_abstracts']=all(s in body for s in ['上层分配确定目标归属，神经策略提出局部活动，动作屏蔽限定允许动作，完成状态共享提供任务执行信息','任务包中的报价依赖决定哪些任务需要释放重算','几何竞争则用于划分协调范围','计划采用，是候选经适用的检查与授权后被执行系统启用','完成状态描述已经完成的活动','一组能够同时满足各成员相关约束的控制输入','层间传递的任务机会、资源占用和可用余量足以表达关键相互约束','For given orbits and the tested service deadlines','original graphical comparison','weighted reward for completed tasks','separate-optimization baseline','Under the respective time limits and tested instances','a Lagrangian heuristic and time-limited mixed-integer linear programming','recommendations for the complete task–orbit–safety process remain conditional'])
selection=rows(HERE/status['hold_register']); holds=[r for r in selection if r['reading_id'] in {'S045','L071'}]
checks['source_versions_hold_and_author_states_inherited']=all(r['human_verified']=='false' for r in reg) and all((ROOT/r['version_record_path']).is_file() for r in reg) and len(holds)==2 and all('HOLD' in r['decision'] and not r['v354_number'] for r in holds) and status['human_verified'] is False and status['submission_ready'] is False and status['author_freeze_confirmation']=='PENDING'
expected=''.join(difflib.unified_diff(prior.splitlines(True),text.splitlines(True),fromfile='V3.5.9/REVIEW_CN_v3.5.9.md',tofile='V3.5.10/REVIEW_CN_v3.5.10.md'))
with zipfile.ZipFile(HERE/'REVIEW_CN_v3.5.10_FULL.zip') as z:
 package_ok=set(z.namelist())=={'REVIEW_CN_v3.5.10.md',*figs} and all(z.read(p)==(HERE/p).read_bytes() for p in z.namelist())
checks['txt_package_diff_and_digest']=(HERE/'REVIEW_CN_v3.5.10.txt').read_bytes()==data and package_ok and (HERE/'audit/V3.5.9_TO_V3.5.10.diff').read_bytes()==expected.encode() and status['manuscript_sha256']==sha(data)
changed=git('diff',B,'--name-only').decode().splitlines()
pending=git('status','--porcelain','--untracked-files=all').decode().splitlines()
checks['handoff_ancestor_only_new_directory']=git('merge-base',B,'HEAD').decode().strip()==B and all(p.startswith(PREFIX) for p in changed) and all(x[3:].startswith(PREFIX) for x in pending)
headings={m.group(1) for m in re.finditer(r'^#{2,4} (\d+(?:\.\d+)*) ',body,re.M)}
cross_refs=re.findall(r'第(\d+(?:\.\d+)+)节',body)
checks['cross_references_and_table_structure']=all(r in headings for r in cross_refs) and re.findall(r'^\*\*表([1-9]) ',body,re.M)==list('123456789') and all(len({len(l.split('|')) for l in t.strip().splitlines()})==1 for t in re.findall(r'(?:^\|.*\n)+',body,re.M))
report={'status':'PASS' if all(checks.values()) else 'FAIL','scope':'Editorial preservation and package consistency, not source revalidation or author scientific approval.','checks':checks,'manuscript_sha256':sha(data),'references':120,'citation_groups':len(re.findall(PAT,body)),'human_verified':False,'submission_ready':False,'author_freeze_confirmation':'PENDING'}
(HERE/'VALIDATION_REPORT.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],'numeric_difference':{'added':dict(numeric_tokens(text)-numeric_tokens(base)),'removed':dict(numeric_tokens(base)-numeric_tokens(text))}},ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
