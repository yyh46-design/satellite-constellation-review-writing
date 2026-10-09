import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir=path.dirname(fileURLToPath(import.meta.url));
const read=async file=>JSON.parse(await fs.readFile(path.join(dir,file),'utf8'));
const annotations=await read('round3_annotations.json');
const candidates=await read('candidates.json');
const registry=await read('crossref_metadata.json');
const queries=await read('search_queries.json');
const prior1=await read('../literature_20261009/literature_records.json');
const prior2=await read('../literature_round2_20261009/literature_records.json');
const prior=[...prior1.reviews,...prior1.originals,...prior2.records];
const priorDois=new Set(prior.map(x=>x.doi.toLowerCase()));
const themes=['部署与重构','健康监测与运行架构','观测任务与不确定调度','星地通信与测控排班','通信与计算资源协同','态势感知与风险决策','分布式约束与协商'];
const direction={'部署与重构':'B','健康监测与运行架构':'A','观测任务与不确定调度':'B','星地通信与测控排班':'B','通信与计算资源协同':'D','态势感知与风险决策':'C','分布式约束与协商':'D'};
const names={A:'整体自主运维与运行架构',B:'服务能力配置与动态调度',C:'物理可行性与安全',D:'分布式自主与协同'};
const decode=s=>String(s??'').replaceAll('&amp;','&').replaceAll('&lt;','<').replaceAll('&gt;','>').replaceAll('&quot;','"');
const dp=m=>m?.['date-parts']?.[0];
const norm=s=>decode(s).normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]/gu,'');
if(candidates.length!==45||annotations.records.length!==45||prior.length!==71||priorDois.size!==71)throw Error('Input count or historical duplicate mismatch');
const records=annotations.records.map((x,i)=>{
 const c=candidates[i];const entry=registry[c.doi.toLowerCase()];const m=entry?.raw??{};
 const title=x.manual_title??decode(m.title?.[0]);
 if(entry?.status!=='registry_match'||m.DOI?.toLowerCase()!==c.doi.toLowerCase())throw Error('Unmatched metadata '+x.id);
 if(norm(title)!==norm(c.title))throw Error('Candidate title mismatch '+x.id);
 const year=x.year??dp(m.published)?.[0]??dp(m.issued)?.[0];
 const venue=x.venue??decode(m['container-title']?.[0]);
 const authors=(m.author??[]).map(a=>[a.given,a.family].filter(Boolean).join(' ')).join('; ');
 if(!title||!x.zh||!year||!venue||!x.source||!authors)throw Error('Required bibliographic value missing '+x.id);
 if(year>2026||priorDois.has(c.doi.toLowerCase()))throw Error('Cutoff or duplicate '+x.id);
 if(x.id!=='O'+(52+i))throw Error('ID sequence mismatch '+x.id);
 return {...x,title,en:title,year,venue,authors,doi:c.doi,theme:c.theme,direction:direction[c.theme],
  scale:x.scale??'卫星／平台数、任务／目标数、实例数与规划时域待全文提取。',
  publicationType:x.publicationType??'期刊论文',check:'Crossref题名与DOI匹配；来源可追溯',registryUrl:entry.registry_url??'',doiUrl:'https://doi.org/'+c.doi,
  pub:dp(m.published)?.join('-')??'',online:dp(m['published-online'])?.join('-')??'',print:dp(m['published-print'])?.join('-')??'',manualFullTextAccepted:false};
});
if(new Set(records.map(x=>x.doi.toLowerCase())).size!==45)throw Error('Round3 duplicate DOI');
const detail=[...records].sort((a,b)=>themes.indexOf(a.theme)-themes.indexOf(b.theme)||Number(a.id.slice(1))-Number(b.id.slice(1)));
const index=[];
for(const [round,kind,list] of [[1,'综述',prior1.reviews],[1,'研究／方法',prior1.originals],[2,'研究／方法',prior2.records],[3,'研究／方法',records]])for(const x of list){
 index.push({...x,round,kind,en:x.en??x.official_en??x.title,theme:x.theme??(kind==='综述'?'前轮综述分类':x.themes??names[x.direction]??'前轮研究分类'),
  direction:x.direction??x.themes??'见前轮覆盖矩阵',
  role:x.role??'按前轮相关性分类',publicationType:x.publicationType??'见来源／前轮矩阵'});
}
index.sort((a,b)=>(a.kind==='综述'?0:1)-(b.kind==='综述'?0:1)||Number(a.id.slice(1))-Number(b.id.slice(1)));
if(index.length!==116||new Set(index.map(x=>x.doi.toLowerCase())).size!==116||new Set(index.map(x=>x.id)).size!==116)throw Error('Cumulative duplicate/count');
const pending=[...prior2.pending.map((x,i)=>({...x,id:'P'+String(i+1).padStart(2,'0'),role:'前轮候选，未计入总索引'})),...annotations.pending];
const counts=Object.fromEntries(themes.map(t=>[t,records.filter(x=>x.theme===t).length]));
const roles=Object.fromEntries(['综述核心','相邻方法','背景支撑'].map(t=>[t,records.filter(x=>x.role===t).length]));
await fs.writeFile(path.join(dir,'literature_records.json'),JSON.stringify({asOf:annotations.as_of,records:detail,index,pending},null,2));
const wb=Workbook.create();const main=wb.worksheets.add('本轮扩展');const cumulative=wb.worksheets.add('文献总索引');const search=wb.worksheets.add('检索记录');
const font='Arial';const letter=n=>{let s='';for(n++;n>0;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;};
function table(sheet,start,headers,rows,widths,name,minHeight=65){
 const last=letter(headers.length-1),end=start+rows.length;const grid=sheet.getRange(`A${start}:${last}${end}`);
 grid.values=[headers,...rows];grid.format={font:{name:font,size:11,color:'#172B4D'},wrapText:true,verticalAlignment:'top'};
 widths.forEach((w,i)=>sheet.getRange(`${letter(i)}${start}:${letter(i)}${end}`).format.columnWidth=w);
 sheet.getRange(`A${start}:${last}${start}`).format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},wrapText:true,horizontalAlignment:'center',verticalAlignment:'center',rowHeight:43};
 rows.forEach((row,i)=>{
  const n=start+i+1;const weightedLength=line=>[...line].reduce((sum,ch)=>sum+(ch.charCodeAt(0)>255?1.8:1),0);
  const lines=Math.max(...row.map((v,j)=>String(v??'').split('\n').reduce((sum,line)=>sum+Math.max(1,Math.ceil(weightedLength(line)/Math.max(8,widths[j]-3))),0)));
  sheet.getRange(`A${n}:${last}${n}`).format.rowHeight=Math.max(minHeight,lines*16+15);
  if(i%2)sheet.getRange(`A${n}:${last}${n}`).format.fill='#F3F6FA';
 });
 const t=sheet.tables.add(`A${start}:${last}${end}`,true,name);t.showFilterButton=true;t.showBandedColumns=false;
 return {last,end};
}
function title(sheet,heading,sub,color='#233E60'){
 sheet.showGridLines=false;sheet.tabColor=color;
 sheet.getRange('A2').values=[[heading]];sheet.getRange('A2').format.font={name:font,size:15,bold:true,color:'#172B4D'};sheet.getRange('A2:H2').format.rowHeight=30;
 sheet.getRange('A3').values=[[sub]];sheet.getRange('A3').format.font={name:font,size:11,color:'#526277'};sheet.getRange('A3:H3').format.rowHeight=24;
}
title(main,'星座智能运维综述：第三轮扩展研究','截至2026-10-09，新增45篇；英文原标题、中文工作译名、DOI及方法边界。编号O52—O96。');
const headers=['ID','扩展主题','写作用途','阅读优先级','年份','英文原标题','中文工作译名','DOI','期刊／会议','原四方向','决策阶段','轨道／场景','研究问题','方法机制','约束／假设','规模与时域（已提取）','验证证据','保证与适用边界','与综述关系（本轮判断）','建议章节','内容提取依据','出版类型','版本／日期说明','作者','题名与DOI核对','','一手来源／作者公开稿','Crossref记录'];
const mainRows=detail.map(x=>[x.id,x.theme,x.role,x.priority,x.year,x.en,x.zh,x.doi,x.venue,x.direction,x.stage,x.orbit,x.question,x.method,x.constraints,x.scale,x.evidence,x.boundary,x.use,x.chapters,x.basis,x.publicationType,x.note,x.authors,x.check,'',[x.source,x.extra_source].filter(Boolean).join('\n'),x.registryUrl]);
const mainWidths=[9,23,15,13,14,72,44,42,38,12,29,39,43,54,51,59,45,59,55,13,58,27,77,46,41,3,98,85];
const mainEnd=table(main,5,headers,mainRows,mainWidths,'Round3Studies',95);
main.getRange(`E6:E${mainEnd.end}`).setNumberFormat('0');main.getRange(`E6:E${mainEnd.end}`).format.horizontalAlignment='right';
main.getRange(`H6:H${mainEnd.end}`).format.font={name:font,size:11,color:'#14589A'};main.getRange(`Z5:Z${mainEnd.end}`).format.fill='#FFFFFF';
const roleColors={'综述核心':'#E4F2EC','相邻方法':'#E9EFF8','背景支撑':'#F6EDD9'};
detail.forEach((x,i)=>{main.getRange(`C${i+6}`).format.fill=roleColors[x.role];main.getRange(`A${i+6}`).format.font={name:font,size:11,bold:true,color:'#233E60'};});
main.freezePanes.freezeRows(5);main.freezePanes.freezeColumns(1);
title(cumulative,'三轮文献总索引','116个去重条目：20篇综述、96个研究／方法类条目。第三轮详细方法信息见“本轮扩展”。','#427766');
const idxHeaders=['ID','检索轮次','文献类别','年份','英文原标题／官方对应题名','中文译名／原标题','DOI','期刊／会议','主题／既有分类','原四方向','写作用途','阅读优先级','出版类型','版本／日期说明','题名与DOI核对','作者','','一手来源／作者公开稿','Crossref记录','内容提取依据'];
const idxRows=index.map(x=>[x.id,x.round,x.kind,x.year,x.en,x.zh,x.doi,x.venue,x.theme,x.direction,x.role,x.priority,x.publicationType,x.note,x.check,x.authors,'',[x.source,x.extra_source].filter(Boolean).join('\n'),x.registryUrl??'',x.basis]);
const idxWidths=[9,12,19,13,82,46,44,43,34,27,24,14,28,79,42,56,3,100,87,66];
const idxEnd=table(cumulative,5,idxHeaders,idxRows,idxWidths,'AllLiterature',85);
cumulative.getRange(`B6:B${idxEnd.end}`).setNumberFormat('0');cumulative.getRange(`D6:D${idxEnd.end}`).setNumberFormat('0');cumulative.getRange(`G6:G${idxEnd.end}`).format.font={name:font,size:11,color:'#14589A'};cumulative.getRange(`Q5:Q${idxEnd.end}`).format.fill='#FFFFFF';
cumulative.freezePanes.freezeRows(5);cumulative.freezePanes.freezeColumns(1);
title(search,'第三轮检索范围、版本与纳入记录','公开网络定向扩展；记录检索词与证据边界，便于后续数据库复检。','#7A6547');
const notes=[
 ['项目','记录'],['截止日期','2026-10-09，Asia/Shanghai。较早公开的在线稿可纳入，未来卷期单独说明。'],
 ['本轮目标','扩展至长期部署、健康监测、云遮不确定调度、地面站、通信与计算资源、空间态势感知和分布式约束协商。'],
 ['本轮数量',`45个新增研究／方法条目，均取得Crossref题名—DOI匹配。${Object.entries(roles).map(([k,v])=>k+' '+v).join('；')}。`],
 ['累计数量','前两轮71条加本轮45条，得到116个唯一DOI：20篇综述、96个研究／方法类条目。含会议论文、会议扩展摘要和系统经验研究，不等同于96篇完整期刊论文。'],
 ['去重规则','逐条比较前两轮71个DOI，大小写无关；本轮无重复。对已确认同题会议／期刊扩展版本及改名预印本进行合并，保留版本线索。不同研究的共享案例仍待全文比对。'],
 ['DOI含义','DOI及题名核对用于编目追溯，不能证明研究结论、实验设计或规模足够。未取得DOI的候选保留官方来源，不猜测填入。'],
 ['阅读深度','以出版社摘要、作者公开稿与定向正文为依据，逐条列读取范围。O85暂为题名级；未获得的规模与条件标待提取。尚未完成作者人工全文验收。'],
 ['年份例外','O56预印本2024、卷期2025；O69在线2020、卷期2022；O88在线2021、卷期2022；O71在线2026-09-25、拟卷期2027-01，按已公开在线年2026列出。'],
 ['版本合并','O90采用JAIR 2025扩展版，同题ICAPS 2024 DOI不重复计数；O92正式AAMAS 2026为扩展摘要，关联arXiv新版改题不另计条目，也不混用其结论。'],
 ['写作用途定义','综述核心：可直接支撑管理、调度或验证主线；相邻方法：问题相邻、需要迁移假设；背景支撑：经典算法、架构和异轨道系统经验。该标签不是论文质量评分。'],
 ['原四方向','A整体自主运维与运行架构；B服务能力配置与动态调度；C物理可行性与安全；D分布式自主与协同。主表为主关联方向，可跨章节引用。'],
 ['规模提取规则','分别记录卫星／观测平台、被观测目标、任务请求、变量、地面天线、情景与时域。20,000个空间目标不是20,000颗决策卫星；百万变量也不是百万颗卫星。'],
 ['检索范围','公开网络定向检索，追溯出版社、作者机构、会议与公开论文入口；使用Crossref逐条核对编目。未执行Web of Science／Scopus全库系统筛选，不主张穷尽。'],
 ['下一轮检索建议','用卫星／星座对象词与健康管理、鲁棒优化、测控资源、信息增益、DCOP等任务词组合；按题名引用与被引追溯，再以正式出版社页面核对版本。'],
 ['全文优先提取','先读O63、O64、O67、O68、O70、O73、O87、O89、O90、O96。提取实际规模、时间与资源模型、数据划分、上下界／保证前提、总计算成本、公开代码及部署证据。'],
 ['建议写作层级','2状态感知与运行架构；3长期能力与部署配置；4任务与星地资源调度；5物理安全和感知—规避接口；6验证与比较；7持续学习与分布式运行展望。'],
 ['数量与范围','文献数量用于判断覆盖缺口，不能替代问题分类和证据比较。最终引用应由综述边界与章节论证决定，不预设通用最低篇数。']
];
for(const t of themes)notes.push([t,`${counts[t]}篇。${detail.filter(x=>x.theme===t).map(x=>x.id).join('、')}。`]);
table(search,4,notes[0],notes.slice(1),[25,118],'SearchScope',55);
const pendingStart=notes.length+7;
search.getRange(`A${pendingStart}`).values=[['DOI待核候选（3条；未计入116条总索引）']];search.getRange(`A${pendingStart}`).format.font={name:font,size:11,bold:true,color:'#172B4D'};
table(search,pendingStart+2,['ID','候选文献、来源与待核原因'],pending.map(x=>[x.id,[x.title,x.zh,String(x.year),x.doi_status??'正式DOI本轮未核定',x.reason,x.role,x.source,x.extra_source].filter(Boolean).join('\n')]),[25,118],'PendingPapers',100);
const logStart=pendingStart+pending.length+7;
search.getRange(`A${logStart-2}`).values=[[`实际检索词（${queries.length}条；保留原分组标记A—D）`]];
search.getRange(`A${logStart-2}`).format.font={name:font,size:11,bold:true,color:'#172B4D'};
table(search,logStart,['检索分组','实际检索词／域名过滤','入口','日期'],queries.map(x=>[x[0],x[1],'公开网络定向检索','2026-10-09']),[25,118,28,18],'SearchQueries',55);
search.getRange('A3').values=[['检索分组标记仅用于记录，不等同于主表A—D方向；候选与原始检索词在下方。']];
search.freezePanes.freezeRows(4);
wb.recalculate();
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:2000});
await fs.writeFile(path.join(dir,'formula_error_scan.json'),scan.ndjson);
const check=await wb.inspect({kind:'table',range:'本轮扩展!A5:H9',include:'values,formulas',tableMaxRows:5,tableMaxCols:8,maxChars:4000});
await fs.writeFile(path.join(dir,'workbook_inspection.json'),check.ndjson);
const previews=[['本轮扩展','A2:G9','round3_preview.png'],['本轮扩展','M40:R42','methods_preview.png'],['文献总索引','A2:G9','index_preview.png'],['检索记录','A2:B13','search_preview.png'],['检索记录',`A${pendingStart}:B${pendingStart+5}`,'pending_preview.png'],['检索记录',`A${logStart}:D${logStart+3}`,'queries_preview.png']];
for(const [sheetName,range,file] of (process.argv.includes('--main-preview-only')?previews.slice(0,1):previews)){const blob=await wb.render({sheetName,range,scale:1.1,format:'png'});await fs.writeFile(path.join(dir,file),new Uint8Array(await blob.arrayBuffer()));}
const outputPath=path.join(dir,'星座智能运维综述文献库_第三轮扩展_20261009.xlsx');
await (await SpreadsheetFile.exportXlsx(wb)).save(outputPath);
const audit={asOf:annotations.as_of,newRecords:records.length,counts,roles,previous:prior.length,cumulative:index.length,reviews:20,researchAndMethodEntries:96,uniqueDOIs:new Set(index.map(x=>x.doi.toLowerCase())).size,overlapWithPrevious:records.filter(x=>priorDois.has(x.doi.toLowerCase())).length,registryMatches:records.filter(x=>x.check.startsWith('Crossref')).length,queries:queries.length,pendingCandidates:pending.length,manualFullTextAccepted:false,outputPath};
await fs.writeFile(path.join(dir,'delivery_audit.json'),JSON.stringify(audit,null,2));console.log(JSON.stringify(audit));
