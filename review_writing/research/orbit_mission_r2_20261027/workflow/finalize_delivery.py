from pathlib import Path
import json,csv,re,hashlib,shutil,zipfile,collections
P=Path(__file__).resolve().parent
R1=P.parent/'constellation_orbit_mission_discussion_r1_20261027'
BASE=Path(r'D:\SKT727\worktrees\constellation_review_v3510_20261026')
DEST=Path(r'D:\SKT727\worktrees\constellation_orbit_research_r2_20261027\review_writing\research\orbit_mission_r2_20261027')
DEST.mkdir(parents=True,exist_ok=True)
def readcsv(name):return list(csv.DictReader((P/name).open(encoding='utf-8-sig')))
def write(name,s):(P/name).write_text(s.strip()+'\n',encoding='utf-8')
pool=readcsv('CANDIDATE_POOL.csv');reads=readcsv('READING_REGISTER.csv');refs=readcsv('REFERENCE_REGISTER_R2.csv')
# Recheck bounded source registries; whole rows preserve version aliases for inspection.
files=[BASE/'review_writing/literature/literature_index_148.csv',BASE/'review_writing/manuscripts/v3.5.9-cn/references/REFERENCE_REGISTER_v3.5.9.csv']
files+=list((BASE/'review_writing/evidence/reading_batches').glob('*/discovery/SCREENING_LEDGER.csv'))
hits=[]
for x in pool:
 doi=x['doi'].lower()
 for f in files:
  lines=f.read_text(encoding='utf-8-sig',errors='replace').splitlines()
  for i,l in enumerate(lines,1):
   if (doi and doi in l.lower()) or x['title'].lower() in l.lower():
    hits.append(dict(candidate=x['stable_id'],doi=doi,path=str(f.relative_to(BASE)).replace('\\','/'),line=i,row=l))
write('HISTORICAL_MATCHES.json',json.dumps(hits,ensure_ascii=False,indent=2))
write('SOURCE_MANIFEST_R2.json',json.dumps([dict(source_id=x['id'],url=x['url'],version=x['version'],sha256=x['sha256'],pages=int(x['pdf_pages']),reading_status=x['reading_status'],reading_scope=x['pages'],human_verified=False) for x in reads],ensure_ascii=False,indent=2))
write('REVISION_AND_NEXT_STEPS_CN.md','''# 研究与写作取舍

这轮完成57项定向候选、10篇原文正文阅读和一篇可连续阅读的R2讨论稿。重点把航天轨道内容写成论证的组成部分：任务指标决定构型，摄动决定构型如何演化，控制与业务共同决定何时可以机动，以及机动后是否形成有价值的服务。

## 与中间R1相比的改变

- 取得Williams Rogers等的实际作者稿，替换仅依赖配套README的证据；核对重访表格，并更正第一作者姓名。
- 部署段增加McGrath的节点漂移与FORMOSAT-3运行对照，解释等待、停推、故障和寿命的作用。
- 差动阻力段复用历史N02研究线的原始会议稿，明确业务抢占控制姿态以及十二星飞行/88星仿真的区别。
- 重构段加入REOSSP的轨道—电量—存储—下传模型，保留固定轨道、全模型、滚动方案的数值和不利结果。
- 加入2026随机多阶段重构，保留候选轨道预裁剪及约60小时计算的边界；不宣称实时全自主能力。
- 运行反馈段加入CMAS，具体说明机动计划、取消及执行偏差怎样刷新成像安排。
- N006、N008已读但暂不采用其未核清的比较与数值。没有为了增加引用而全部塞入正文。

R2有28条参考来源，使用本轮8篇正文阅读来源和20项历史记录；它是约8500中文汉字的完整讨论样稿，用于审阅主线、摘要及代表性论证，不是替代原120来源正式长稿的新版本。原题目与V3.5.10、main、历史HOLD均未修改。R1是本轮中间讨论稿，非先前发布版本。

## 阅读建议与下一步

先读摘要、2.1、2.2、3.4和4.3，判断“任务—轨道—业务”的双向联系是否比原来清楚。重点不是增加轨道术语，而是每一类轨道方法都能解释一种任务机会、时间或资源的变化。

47项候选尚未正文阅读，下一批优先顺序见SEARCH_AND_SELECTION_CN.md。继续按10篇一批处理，优先补强应急低推力联合调度、被动退出安全、指派与轨迹共同优化，以及真实部署维护接口。再依据精读结果选择是否扩展现有正式长稿的轨道章节。

仍需作者判断：初始构型设计在正式稿中承担背景还是主要研究领域；实际作者稿与正式版的差异；完整事件链的直接业务测量仍不足；小编队机制向真实大星座迁移缺少统一对照。本轮阅读没有关闭旧有正式版配对、最近邻综述全文缺口或作者终核。

状态保持：human_verified=false，submission_ready=false；正文冻结由作者决定。
''')
write('README_CN.md','''# 任务驱动星座轨道与运行研究包 R2

2026-10-27。本轮按“多找一些，再实际精读并改写”的要求执行。

| 项目 | 数量与含义 |
|---|---|
| 定向候选池 | 57项；56项在已核对旧台账中未匹配，1项历史版本复读 |
| 本批正文阅读 | 10篇：9项本轮前台账未匹配来源＋1项历史N02版本 |
| 进入R2样稿 | 本批8篇；2篇保留待核 |
| 尚未正文阅读 | 47项；不能计为完成精读 |
| R2讨论稿参考来源 | 28项：本轮阅读8项＋沿用历史20项 |

这些统计不与旧95/97/120等口径直接相加。候选发现、原文阅读、正文采用、正式版配对和作者终核是独立状态。

## 文件入口

- [完整讨论稿 MD](REVIEW_DISCUSSION_R2_CN.md) / [TXT](REVIEW_DISCUSSION_R2_CN.txt)
- [57项候选及待核问题](CANDIDATE_POOL_CN.md) / [CSV](CANDIDATE_POOL.csv)
- [10篇阅读总结](READING_BATCH_SUMMARY_CN.md) / [逐篇笔记](reading_notes/INDEX.md)
- [修改与下一步](REVISION_AND_NEXT_STEPS_CN.md)
- [检索与取舍方法](SEARCH_AND_SELECTION_CN.md)
- [本轮论点](CLAIM_REGISTER.csv)、[阅读登记](READING_REGISTER.csv)、[样稿来源登记](REFERENCE_REGISTER_R2.csv)
- [相对中间R1差异](R1_TO_R2.diff)
- [完整材料下载包](RESEARCH_R2_REVIEW_PACKAGE.zip)

R2用于讨论更具轨道动力学内容的论证组织；未替换现有V3.5.10正式长稿，也未将新拟题目视为作者已确认的改题。基线commit为7141979de09e76c6538b05073162c6610da02cf8，tree为183472ae04b98eb7b4df7697c3afc7e8a1e09969。

原始PDF、原始查询响应及14张关键页核查图在本机保存。公开包提供实际来源链接与SHA-256；discovery保留真实查询、失败及发现元数据，移除摘要正文但保留其存在标记与哈希。正文事实来源追溯至本轮笔记或基线仓库已有记录。没有新增数值仿真。

human_verified=false；submission_ready=false。AI正文阅读和一致性检查不替代作者科学终核。
''')
write('KEY_PAGE_CHECK_CN.md','''# 本轮关键页面核对

原文正文采用文本提取阅读；对影响数值和范围判断的页面另做视觉核对。共14页：N001 p25；N002 p26/30/31；N006 p14/15；N008 p5/6；N009 p20/23/30；N010 p11/12/13。页面图在本机figures/保存，公开登记通过SOURCE_MANIFEST_R2.json绑定PDF版本和哈希。

- N001表8确认22/14.95与44/12.43，以及原PDF为78.07%，不沿用README的78.08%。
- N002表3确认24例结果的失败标记与数值对照；pp30–31确认GB、min及目标函数和评价指标的区别。
- N006表3与邻接段落场景组合待核；表4的全变化量不直接当成表3单侧幅值比较。
- N008确认式(13)/(16)的倾角项差别确实出现在PDF；只记待核，不声称已证明论文错误。
- N009确认原文60 h计算叙述与附录A裁剪方法；附录预算印刷单位不采用。
- N010图11是12星飞行、图13是88星仿真，保留有效控制权偏差反馈。

没有重画论文图、数字化读取曲线或新增实验，也未完成整套论文图表投稿终核。
''')
body,book=(P/'REVIEW_DISCUSSION_R2_CN.md').read_text(encoding='utf-8').split('## 参考文献',1)
nums=[int(x) for x in re.findall(r'\[(\d+)\]',body)]
bnums=[int(x) for x in re.findall(r'(?m)^(\d+)\. ',book)]
baseline=BASE/'review_writing/manuscripts/v3.5.10-cn/REVIEW_CN_v3.5.10.md'
checks={
'candidate_count_at_least_50':len(pool)>=50,
'candidate_ids_unique':len({x['stable_id'] for x in pool})==len(pool),
'candidate_nonempty_doi_unique':len([x['doi'].lower() for x in pool if x['doi']])==len({x['doi'].lower() for x in pool if x['doi']}),
'ten_reading_records_and_notes':len(reads)==10 and all((P/'reading_notes'/f"{x['id']}_CN.md").exists() for x in reads),
'all_saved_pdf_hashes_match':all(hashlib.sha256((P/'sources'/f"{x['id']}.pdf").read_bytes()).hexdigest()==x['sha256'] for x in reads),
'citations_bibliography_register_agree':set(nums)==set(bnums)==set(int(x['r2_number']) for x in refs)==set(range(1,29)),
'first_appearance_order':list(dict.fromkeys(nums))==list(range(1,29)),
'five_chapters':re.findall(r'(?m)^## ([1-5]) ',body)==list('12345'),
'md_txt_identical':(P/'REVIEW_DISCUSSION_R2_CN.md').read_bytes()==(P/'REVIEW_DISCUSSION_R2_CN.txt').read_bytes(),
'baseline_unchanged':hashlib.sha256(baseline.read_bytes()).hexdigest()=='8efe429876962d10918f9c2a69ea4ebc9eae9d322610ece858e0fb1b5f2f31e0',
'author_verification_not_promoted':all(x['human_verified'].lower()=='false' for x in reads+refs+pool),
}
assert all(checks.values()),checks
write('DELIVERY_CHECK.json',json.dumps({'scope':'本轮材料与引用一致性；不代表作者科学终核','checks':checks,'human_verified':False,'submission_ready':False},ensure_ascii=False,indent=2))
# Stage only research artifacts; exclude original PDFs, full extracted copyrighted text and page images.
names=['README_CN.md','REVIEW_DISCUSSION_R2_CN.md','REVIEW_DISCUSSION_R2_CN.txt','CANDIDATE_POOL_CN.md','CANDIDATE_POOL.csv','READING_BATCH_SUMMARY_CN.md','READING_REGISTER.csv','CLAIM_REGISTER.csv','REFERENCE_REGISTER_R2.csv','REVISION_AND_NEXT_STEPS_CN.md','SEARCH_AND_SELECTION_CN.md','R1_TO_R2.diff','RESEARCH_COUNTS.json','SOURCE_MANIFEST_R2.json','HISTORICAL_MATCHES.json','KEY_PAGE_CHECK_CN.md','DELIVERY_CHECK.json']
for name in names:shutil.copyfile(P/name,DEST/name)
for name in ['collect_candidates.py','acquire_sources.py','acquire_more.py','read_pages.py','render_key_pages.py','build_research.py','build_draft.py','finalize_delivery.py']:
 (DEST/'workflow').mkdir(exist_ok=True);shutil.copyfile(P/name,DEST/'workflow'/name)
shutil.copytree(P/'reading_notes',DEST/'reading_notes',dirs_exist_ok=True)
(DEST/'discovery').mkdir(exist_ok=True)
def metadata_only(obj):
 if isinstance(obj,list):return [metadata_only(x) for x in obj]
 if isinstance(obj,dict):
  out={k:metadata_only(v) for k,v in obj.items() if k!='abstract'}
  if 'abstract' in obj:
   out['abstract_present_in_local_response']=True
   out['abstract_sha256']=hashlib.sha256(obj['abstract'].encode('utf-8')).hexdigest()
  return out
 return obj
for f in (P/'discovery').iterdir():
 if f.suffix=='.json':
  (DEST/'discovery'/f.name).write_text(json.dumps(metadata_only(json.loads(f.read_text(encoding='utf-8'))),ensure_ascii=False,indent=2),encoding='utf-8')
 else:shutil.copyfile(f,DEST/'discovery'/f.name)
(DEST/'provenance').mkdir(exist_ok=True)
for name in ['REVIEW_DISCUSSION_R1_CN.md','SOURCE_AND_CLAIM_REGISTER.csv']:
 shutil.copyfile(R1/name,DEST/'provenance'/name)
manifest=[dict(path=str(f.relative_to(DEST)).replace('\\','/'),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in sorted(DEST.rglob('*')) if f.is_file() and f.name not in ['FILE_MANIFEST.json','RESEARCH_R2_REVIEW_PACKAGE.zip']]
(DEST/'FILE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
zipname='RESEARCH_R2_REVIEW_PACKAGE.zip'
with zipfile.ZipFile(P/zipname,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(DEST.rglob('*')):
  if f.is_file() and f.suffix!='.zip':z.write(f,f.relative_to(DEST))
shutil.copyfile(P/zipname,DEST/zipname)
with zipfile.ZipFile(P/zipname) as z:assert z.testzip() is None
print(json.dumps({'checks':checks,'historical_matches':hits,'files':len(manifest),'zip_bytes':(P/zipname).stat().st_size,'destination':str(DEST)},ensure_ascii=False))
