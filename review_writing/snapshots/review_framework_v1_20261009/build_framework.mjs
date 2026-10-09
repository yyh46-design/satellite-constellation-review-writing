import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir=path.dirname(fileURLToPath(import.meta.url));
const read=async p=>JSON.parse(await fs.readFile(path.join(dir,p),'utf8'));
const plan=await read('framework_plan.json');
const library=await read('../literature_round4_20261009/literature_records.json');
const first=new Set(plan.first_read_ids),context=new Set(plan.context_original_ids),pending=new Set(plan.pending_technical_ids);
const tiers=['首轮锚点精读','第二轮专题精读','背景或方法参照','待全文判定'];
const chapterMap=new Map(plan.chapters.map(x=>[x.id,x.name]));
const existing=new Set(library.index.map(x=>x.id));
for(const id of [...first,...context,...pending])if(!existing.has(id))throw Error('Unknown ID '+id);
if(first.size!==40||library.index.length!==148||plan.chapters_by_original.length!==128||plan.chapters_by_review.length!==20)throw Error('Input count mismatch');
for(const id of pending)if(first.has(id)||context.has(id))throw Error('Conflicting screening '+id);
const tierReasons={
 '首轮锚点精读':'用于建立综述定位、核心模型或证据标尺，优先阅读全文；尚非最终纳入。',
 '第二轮专题精读':'与主线相关，用于补齐问题变体、比较基线或章节覆盖；在锚点后阅读。',
 '背景或方法参照':'用于概念、历史、异场景方法或验证参照；不直接外推为大型LEO系统结论。',
 '待全文判定':'题名／编目已有，但关键方法或规模尚未取得；本轮不据此作技术比较结论。'
};
const comparisonQuestions={
 '1':'核对综述的实际对象、文献时段、任务类别、分类框架、安全接口与证据维度；确定我们可以新增的比较。',
 '2':'提取节点／代理定义、状态与任务数据、规划触发、执行接口、人工监督、故障检测及恢复动作。',
 '3':'提取配置变量、需求和故障模型、库存／供给、服务节点与转移代价；说明配置如何改变可服务任务集。',
 '4':'提取变量、任务链、目标、窗口、资源动态与不确定性；确认收益是否需要实际完成或交付。',
 '5':'提取分解、算法作用位置、可行性检查、信息交换、网络异常、理论前提和训练／在线总成本。',
 '6':'提取动力学、终端状态、安全约束、连续时间检查和故障恢复；核查保证对象及执行反馈。',
 '7':'提取规模分母、时域、实例生成、重复实验、硬件、数据划分、基线、总成本与验证对象。',
 '8':'将本文的限制与前文证据连接，区分已有结论、缺失条件和可检验研究任务。'
};
const targeted={
 O01:'需求情景、两阶段决策与运行网络如何连接配置和服务调度？转移代价在哪一层计算？',
 O04:'连续仓库位置与访问序列如何交替求解？低推力、相位与转移可行性怎样处理？',
 O06:'维护策略怎样组合替换、补网和在轨服务？哪些运行／故障成本决定选择？',
 O10:'LEO漂移转移怎样生成连续多客户路线？前计算与精确轨迹之间怎样核查？',
 O16:'管理拓扑与任务可行性网络是否相同？拓扑维护触发、规模和消息成本如何计量？',
 O21:'状态、规划、执行、监控和适应模块之间有什么正式接口与运行验证？',
 O23:'单智能体策略怎样用于多星？通信和任务协调依赖哪些条件，规模与训练成本是什么？',
 O27:'库存层级、随机故障、补给时延和服务水平怎样建模，哪些变量可优化？',
 O28:'部署目标中的服务能力关系如何定义？距离／相位／窗口近似与真实可执行性有什么区别？',
 O29:'加注设施、资源补充、跨轨转移和任务排序怎样共同建模并验证连续性？',
 O31:'不确定服务时长属于哪种模型？风险／鲁棒参数怎样影响连续任务的可行性？',
 O32:'多对多服务的代理、容量与转移成本如何定义？资源约束是检查、修复还是奖励惩罚？',
 O37:'最近接近事件怎样定义、筛选与精化？求根误差、漏检和参考解如何核查？',
 O41:'机会约束对应哪种误差分布？扰动估计与MPC执行怎样连接，保证前提是什么？',
 O46:'严格通信约束的时间与消息模型是什么？怎样实现在线协议和冲突消除？',
 O60:'训练／测试和异常标签怎样划分？动态阈值及事件级误报怎样评估？',
 O64:'哪些指标和数据处理产生性能高估？简单基线、事件指标与点调整怎样比较？',
 O70:'主／子问题怎样表示电池与任务约束？上下界、定价和大规模求解成本是什么？',
 O73:'哪些范围真正用于地面站运行？现场时域、输入、故障与基线证据是什么？',
 O90:'GND与NSS怎样定义邻域和消息？变量、卫星、任务数及模型可行性怎样分开？',
 O95:'集中、广播和高度去中心化架构各自需要什么信息？资源约束和通信量怎样比较？',
 O97:'哪些FDIR规则与OBSW服务集成？rover验证了哪些恢复动作，尚未验证哪些卫星工况？',
 O99:'数字孪生、规则验证与配置生成如何衔接？专家评价与工具链验证分别支持什么结论？',
 O101:'1000颗卫星案例的任务生成、资源模型、时域和硬件是什么？在线修复与拉格朗日部分成本如何计量？',
 O108:'充电功率是否随姿态／轨道变化？观察、下传与能量状态怎样共同验证？',
 O112:'图像质量、语义任务收益与推理时间怎样进入模型？哪些耗时是实测，哪些星座结果来自仿真？',
 O113:'接触图不确定性如何影响采集、指令传播和交付？是否同时模拟任务信息和数据路径？',
 O116:'什么网络与规模下出现重复分配／漏分配？结论迁移到卫星系统需要哪些条件？',
 O119:'算法是否使用同一环境和约束？训练总成本、数据／工况划分、基线和失败率怎样报告？',
 O122:'哪些操作真正由星上自主规划控制？飞行时间、资源、异常和地面监督范围是什么？',
 O124:'模式管理模型如何扩展？各工具的性能与所验证性质是什么，抽象有哪些限制？',
 O126:'应急计划怎样触发？cFS软件验证与开发板集群分别覆盖哪些任务失败和通信条件？'
};
const screens=library.index.map(x=>{
 const n=Number(x.id.slice(1)),isReview=x.id.startsWith('R');
 const proposed=(isReview?plan.chapters_by_review[n-1]:plan.chapters_by_original[n-1]).split(',');
 if(proposed.some(v=>!chapterMap.has(v)))throw Error('Unknown chapter '+x.id);
 const tier=pending.has(x.id)?tiers[3]:first.has(x.id)?tiers[0]:(isReview||context.has(x.id))?tiers[2]:tiers[1];
 const mainChapter=isReview?'1':proposed[0];
 const fields=isReview?comparisonQuestions['1']:targeted[x.id]??comparisonQuestions[mainChapter];
 const contribution=x.use??x.focus??'具体技术内容待提取';
 const cautions=x.boundary??x.comparison??x.note??'保证前提与实验范围需全文核对';
 return {...x,tier,mainChapter,proposedChapters:proposed.join('、'),chapterName:chapterMap.get(mainChapter),
  screeningReason:tierReasons[tier]+' '+contribution,readingQuestion:fields,
  writingRole:isReview?'竞争综述／分类与范围对照':tier===tiers[2]?'背景／有条件的方法参照':tier===tiers[3]?'技术内容待核候选':'问题模型／方法机制／验证证据',
  limits:cautions,fullTextStatus:'用途初筛完成；完整全文提取与作者人工核对未完成',manualFullTextAccepted:false};
});
const counts=Object.fromEntries(tiers.map(t=>[t,screens.filter(x=>x.tier===t).length]));
if(JSON.stringify(Object.values(counts))!==JSON.stringify([40,62,40,6]))throw Error('Screen counts '+JSON.stringify(counts));
const queue=plan.first_read_ids.map((id,i)=>{
 const x=screens.find(x=>x.id===id);const group=i<8?'A 先核对已有综述':i<18?'B 建立系统与服务问题':'C 方法、安全与证据';
 return {...x,queueOrder:i+1,group};
});
const chapterCoverage=plan.chapters.map(c=>({id:c.id,all:screens.filter(x=>x.proposedChapters.split('、').includes(c.id)).length,first:screens.filter(x=>first.has(x.id)&&x.proposedChapters.split('、').includes(c.id)).length}));
await fs.writeFile(path.join(dir,'screening_records.json'),JSON.stringify({asOf:plan.as_of,counts,screens,queue,chapterCoverage,pendingOutsideLibrary:library.pending},null,2));
const wb=Workbook.create();const frame=wb.worksheets.add('框架与写作');const screen=wb.worksheets.add('148条初筛');const reading=wb.worksheets.add('首轮40篇精读');
const font='Arial';const letter=n=>{let s='';for(n++;n>0;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;};
function title(sheet,heading,sub,color){
 sheet.showGridLines=false;sheet.tabColor=color;sheet.getRange('A2').values=[[heading]];sheet.getRange('A2').format.font={name:font,size:15,bold:true,color:'#172B4D'};sheet.getRange('A2:H2').format.rowHeight=30;
 sheet.getRange('A3').values=[[sub]];sheet.getRange('A3').format.font={name:font,size:11,color:'#526277'};sheet.getRange('A3:H3').format.rowHeight=26;
}
function table(sheet,start,headers,rows,widths,name,minHeight=65){
 const last=letter(headers.length-1),end=start+rows.length;const range=sheet.getRange(`A${start}:${last}${end}`);
 range.values=[headers,...rows];range.format={font:{name:font,size:11,color:'#172B4D'},wrapText:true,verticalAlignment:'top'};
 widths.forEach((w,i)=>sheet.getRange(`${letter(i)}${start}:${letter(i)}${end}`).format.columnWidth=w);
 sheet.getRange(`A${start}:${last}${start}`).format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},wrapText:true,horizontalAlignment:'center',verticalAlignment:'center',rowHeight:43};
 rows.forEach((row,i)=>{const n=start+i+1;const length=line=>[...line].reduce((sum,ch)=>sum+(ch.charCodeAt(0)>255?1.8:1),0);const lines=Math.max(...row.map((v,j)=>String(v??'').split('\n').reduce((sum,line)=>sum+Math.max(1,Math.ceil(length(line)/Math.max(8,widths[j]-3))),0)));sheet.getRange(`A${n}:${last}${n}`).format.rowHeight=Math.max(minHeight,lines*16+15);if(i%2)sheet.getRange(`A${n}:${last}${n}`).format.fill='#F3F6FA';});
 const t=sheet.tables.add(`A${start}:${last}${end}`,true,name);t.showFilterButton=true;t.showBandedColumns=false;return {last,end};
}
title(frame,'综述框架与文献用途初筛 v1','2026-10-09；框架建议＋148条初筛＋首轮40篇精读队列。尚非全文纳入或质量评估结果。','#233E60');
frame.getRange('A2:D2').merge();frame.getRange('A3:D3').merge();
const chapterRows=plan.chapters.map(x=>[x.id,x.name,x.subsections,x.question+'\n'+x.argument,x.displays+'\n证据字段：'+x.fields,x.anchors,x.weight,x.order]);
table(frame,5,['章','章节','二级目录','核心问题与论证任务','拟图表及所需证据','锚点文献ID','篇幅建议','写作次序'],chapterRows,[10,34,72,72,65,53,14,28],'ChapterOutline',110);
frame.freezePanes.freezeRows(5);
const scopeRows=[
 ['定位','中文拟题',plan.title_zh,'拟题，投稿前再定'],['定位','英文拟题',plan.title_en,'工作题名'],['定位','核心问题',plan.central_question,'用于统一各章节'],['定位','综述类型',plan.review_type,'检索与报告方法仍需补齐'],['边界','研究对象',plan.scope,'主线与参照场景分别编码'],
 ...plan.contributions.map((x,i)=>['贡献','拟议贡献'+(i+1),x,'独特性待竞争综述全文核对']),
 ...plan.research_questions.map(x=>[x[0],x[1],x[2],'全文提取后回答']),
 ['写作','段落结构',plan.writing_pattern,'每个专题沿用'],['写作','初筛状态',plan.screening_status,'未删除原库条目'],['写作','未决事项',plan.unresolved,'本轮不填造']
];
table(frame,18,['类别','项目','内容','使用状态／说明'],scopeRows,[10,34,72,72],'ScopeAndQuestions',60);
const extractionStart=18+scopeRows.length+4;
const extractionRows=plan.extraction_fields.map((x,i)=>[String(i+1).padStart(2,'0'),x,'记录原文页码、表／图编号、具体值或定义；未取得写待提取。','不同场景不可直接合并成统一性能排名。']);
table(frame,extractionStart,['序号','全文提取字段','记录方式','比较注意'],extractionRows,[10,34,72,72],'ExtractionSchema',60);
const tierStart=extractionStart+extractionRows.length+4;
table(frame,tierStart,['分组','用途','判定说明','本轮数量'],tiers.map((x,i)=>[String(i+1),x,tierReasons[x],counts[x]]),[10,34,72,72],'ScreeningRules',60);
const pendingStart=tierStart+8;
table(frame,pendingStart,['ID','候选题名／中文译名','待核原因与状态','一手入口'],library.pending.map(x=>[x.id,x.title+'\n'+x.zh,[x.doi_status??'DOI本轮未核定',x.reason,x.role].filter(Boolean).join('\n'),[x.source,x.extra_source].filter(Boolean).join('\n')]),[10,34,72,72],'OutsideDOICandidates',95);
title(screen,'148条文献：章节映射与用途初筛','初筛分组基于现有编目与提取记录；未完成全文排除。原题名、译名与DOI全部保留。','#427766');
const screeningHeaders=['ID','本轮初筛分组','文献类别','主用章节','建议引用章节','章节名称','英文原标题／官方对应题名','中文译名／原标题','DOI','年份','期刊／会议','本轮用途判断与理由','全文重点问题','既有内容提取依据','适用限制／待核事项','完整全文状态','原建议章节','作者','','一手来源／作者公开稿','编目核对记录'];
const screeningRows=screens.map(x=>[x.id,x.tier,x.kind,x.mainChapter,x.proposedChapters,x.chapterName,x.en,x.zh,x.doi,x.year,x.venue,x.screeningReason,x.readingQuestion,x.basis,x.limits,x.fullTextStatus,x.chapters??'',x.authors,'',[x.source,x.extra_source].filter(Boolean).join('\n'),x.check]);
const screenEnd=table(screen,5,screeningHeaders,screeningRows,[10,24,18,14,20,37,78,45,43,13,41,82,85,70,78,65,18,48,3,98,55],'All148Screened',95);
screen.getRange(`J6:J${screenEnd.end}`).setNumberFormat('0');screen.getRange(`I6:I${screenEnd.end}`).format.font={name:font,size:11,color:'#14589A'};screen.getRange(`S5:S${screenEnd.end}`).format.fill='#FFFFFF';screen.freezePanes.freezeRows(5);screen.freezePanes.freezeColumns(1);
const tierColors={'首轮锚点精读':'#E4F2EC','第二轮专题精读':'#E9EFF8','背景或方法参照':'#F6EDD9','待全文判定':'#F8E6E2'};
screens.forEach((x,i)=>screen.getRange(`B${i+6}`).format.fill=tierColors[x.tier]);
title(reading,'首轮40篇精读：按论证用途排序','先核对8篇竞争综述，再阅读32篇原始研究／方法论文。队列表示阅读安排，非最终纳入清单。','#7A6547');
const queueHeaders=['顺序','阅读阶段','ID','主用章节','中文译名／原标题','英文原标题／官方对应题名','DOI','必须回答的全文问题','具体选用理由','当前读取依据','适用限制与版本','提取完成状态','','一手来源／作者公开稿'];
const queueRows=queue.map(x=>[x.queueOrder,x.group,x.id,x.mainChapter,x.zh,x.en,x.doi,x.readingQuestion,x.screeningReason,x.basis,x.limits+'\n'+(x.note??''),'未完成完整全文提取','',[x.source,x.extra_source].filter(Boolean).join('\n')]);
const queueEnd=table(reading,5,queueHeaders,queueRows,[10,29,10,14,47,78,43,90,83,67,83,34,3,99],'First40ReadingQueue',95);
reading.getRange(`A6:A${queueEnd.end}`).setNumberFormat('0');reading.getRange(`G6:G${queueEnd.end}`).format.font={name:font,size:11,color:'#14589A'};reading.getRange(`M5:M${queueEnd.end}`).format.fill='#FFFFFF';reading.freezePanes.freezeRows(5);reading.freezePanes.freezeColumns(3);
frame.getRange('J2:K6').values=[['初筛分组','数量'],...tiers.map(t=>[t,null])];frame.getRange('J2:K6').format={font:{name:font,size:11,color:'#172B4D'},wrapText:true,verticalAlignment:'top'};frame.getRange('J2:J6').format.columnWidth=25;frame.getRange('K2:K6').format.columnWidth=12;frame.getRange('J2:K2').format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},rowHeight:30};
tiers.forEach((t,i)=>frame.getRange(`K${i+3}`).formulas=[[`=COUNTIFS('148条初筛'!B6:B153,J${i+3})`]]);frame.getRange('K3:K6').setNumberFormat('0');
wb.recalculate();
const countsObserved=frame.getRange('K3:K6').values.map(x=>x[0]);if(JSON.stringify(countsObserved)!==JSON.stringify([40,62,40,6]))throw Error('Formula count mismatch '+JSON.stringify(countsObserved));
const originalTier=screen.getRange('B6').values[0][0];if(originalTier!=='背景或方法参照')throw Error('Unexpected representative record');screen.getRange('B6').values=[['首轮锚点精读']];wb.recalculate();if(JSON.stringify(frame.getRange('K3:K6').values.map(x=>x[0]))!==JSON.stringify([41,62,39,6]))throw Error('Count formula did not update');screen.getRange('B6').values=[[originalTier]];wb.recalculate();if(JSON.stringify(frame.getRange('K3:K6').values.map(x=>x[0]))!==JSON.stringify([40,62,40,6]))throw Error('Count formula restore failed');
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:1000});await fs.writeFile(path.join(dir,'error_scan.ndjson'),scan.ndjson);
const inspected=await wb.inspect({kind:'table',range:'首轮40篇精读!A5:H8',include:'values,formulas',tableMaxRows:4,tableMaxCols:8,maxChars:4000});await fs.writeFile(path.join(dir,'inspection.ndjson'),inspected.ndjson);
const previews=[['框架与写作','A2:D9','framework_preview.png'],['框架与写作','J2:K6','counts_preview.png'],['框架与写作',`A${extractionStart}:D${extractionStart+4}`,'extraction_preview.png'],['148条初筛','A2:F10','screening_preview.png'],['首轮40篇精读','A2:E10','queue_preview.png'],['首轮40篇精读','H24:K25','reading_questions_preview.png']];
for(const [sheetName,range,file] of (process.argv.includes('--framework-preview-only')?previews.slice(0,1):previews)){const blob=await wb.render({sheetName,range,scale:1.1,format:'png'});await fs.writeFile(path.join(dir,file),new Uint8Array(await blob.arrayBuffer()));}
const outputPath=path.join(dir,'星座综述框架与148篇文献初筛_v1_20261009.xlsx');await (await SpreadsheetFile.exportXlsx(wb)).save(outputPath);
const audit={asOf:plan.as_of,chapters:plan.chapters.length,total:screens.length,uniqueDOIs:new Set(screens.map(x=>x.doi.toLowerCase())).size,counts,firstQueue:queue.length,firstReviews:queue.filter(x=>x.id.startsWith('R')).length,firstOriginals:queue.filter(x=>x.id.startsWith('O')).length,pendingOutsideLibrary:library.pending.length,allTitlesTranslationsDOIsPreserved:true,manualFullTextAccepted:false,outputPath};await fs.writeFile(path.join(dir,'delivery_audit.json'),JSON.stringify(audit,null,2));console.log(JSON.stringify(audit));
