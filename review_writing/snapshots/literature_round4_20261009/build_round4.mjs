import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir=path.dirname(fileURLToPath(import.meta.url));
const read=async file=>JSON.parse(await fs.readFile(path.join(dir,file),'utf8'));
const annotations=await read('round4_annotations.json');
const candidates=await read('candidates.json');
const registry=await read('crossref_metadata.json');
const queries=await read('search_queries.json');
const priorData=await read('../literature_round3_20261009/literature_records.json');
const prior=priorData.index;
const priorDois=new Set(prior.map(x=>x.doi.toLowerCase()));
const themes=['故障恢复与重调度','大星座规模与分解','多资源联合调度','通信受限与异步协同','工程验证与公开基准'];
const direction={'故障恢复与重调度':'A','大星座规模与分解':'B','多资源联合调度':'B','通信受限与异步协同':'D','工程验证与公开基准':'A'};
const names={A:'整体自主运维与运行架构',B:'服务能力配置与动态调度',C:'物理可行性与安全',D:'分布式自主与协同'};
const decode=s=>String(s??'').replaceAll('&amp;','&').replaceAll('&lt;','<').replaceAll('&gt;','>').replaceAll('&quot;','"').replaceAll('\u00a0',' ');
const dp=m=>m?.['date-parts']?.[0];
const norm=s=>decode(s).normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]/gu,'');
if(annotations.records.length!==32||prior.length!==116||priorDois.size!==116)throw Error('Input count or historical duplicate mismatch');
const records=annotations.records.map((x,i)=>{
 const c=candidates.find(c=>c.doi?.toLowerCase()===x.doi.toLowerCase());if(!c)throw Error('Candidate missing '+x.id);const entry=registry[c.doi.toLowerCase()];const m=entry?.raw??{};
 const title=x.manual_title??decode(m.title?.[0]);
 if(!x.check_override&&(entry?.status!=='registry_match'||m.DOI?.toLowerCase()!==c.doi.toLowerCase()))throw Error('Unmatched metadata '+x.id);
 const en=x.official_en??title;
 if(norm(en)!==norm(c.title))throw Error('Candidate title mismatch '+x.id);
 const year=x.year??dp(m.published)?.[0]??dp(m.issued)?.[0];
 const venue=x.venue??decode(m['container-title']?.[0]);
 const authors=x.authors??(m.author??[]).map(a=>[a.given,a.family].filter(Boolean).join(' ')).join('; ');
 if(!title||!x.zh||!year||!venue||!x.source||!authors)throw Error('Required bibliographic value missing '+x.id);
 if(year>2026||priorDois.has(c.doi.toLowerCase()))throw Error('Cutoff or duplicate '+x.id);
 if(x.id!=='O'+(97+i))throw Error('ID sequence mismatch '+x.id);
 return {...x,title,en,year,venue,authors,doi:c.doi,theme:c.theme,direction:x.direction??direction[c.theme],
  scale:x.scale??'卫星／平台数、任务／目标数、实例数与规划时域待全文提取。',
  publicationType:x.publicationType??'期刊论文',check:x.check_override??'Crossref题名与DOI匹配；来源可追溯',registryUrl:x.check_override?'':entry.registry_url??'',doiUrl:'https://doi.org/'+c.doi,
  pub:dp(m.published)?.join('-')??'',online:dp(m['published-online'])?.join('-')??'',print:dp(m['published-print'])?.join('-')??'',manualFullTextAccepted:false};
});
if(new Set(records.map(x=>x.doi.toLowerCase())).size!==32)throw Error('Round4 duplicate DOI');
const detail=[...records].sort((a,b)=>themes.indexOf(a.theme)-themes.indexOf(b.theme)||Number(a.id.slice(1))-Number(b.id.slice(1)));
const index=[...prior,...records.map(x=>({...x,round:4,kind:'研究／方法'}))];
index.sort((a,b)=>(a.kind==='综述'?0:1)-(b.kind==='综述'?0:1)||Number(a.id.slice(1))-Number(b.id.slice(1)));
if(index.length!==148||new Set(index.map(x=>x.doi.toLowerCase())).size!==148||new Set(index.map(x=>x.id)).size!==148)throw Error('Cumulative duplicate/count');
const pending=[...priorData.pending,...annotations.pending];
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
title(main,'星座智能运维综述：第四轮缺口补检','截至2026-10-09，新增32篇；英文原标题、中文译名、DOI、规模与验证边界。编号O97—O128。');
const headers=['ID','本轮补检主题','写作用途','阅读优先级','年份','英文原标题／官方对应题名','中文译名／原标题','DOI','期刊／会议','原四方向','决策阶段','轨道／场景','研究问题','方法机制','约束／假设','规模与时域（已提取）','验证证据','保证与适用边界','与综述关系（本轮判断）','建议章节','内容提取依据','出版类型','版本／日期说明','作者','题名与DOI核对','','一手来源／作者公开稿','Crossref记录'];
const mainRows=detail.map(x=>[x.id,x.theme,x.role,x.priority,x.year,x.en,x.zh,x.doi,x.venue,x.direction,x.stage,x.orbit,x.question,x.method,x.constraints,x.scale,x.evidence,x.boundary,x.use,x.chapters,x.basis,x.publicationType,x.note,x.authors,x.check,'',[x.source,x.extra_source].filter(Boolean).join('\n'),x.registryUrl]);
const mainWidths=[9,23,15,13,14,72,44,42,38,12,29,39,43,54,51,59,45,59,55,13,58,27,77,46,41,3,98,85];
const mainEnd=table(main,5,headers,mainRows,mainWidths,'Round4Studies',95);
main.getRange(`E6:E${mainEnd.end}`).setNumberFormat('0');main.getRange(`E6:E${mainEnd.end}`).format.horizontalAlignment='right';
main.getRange(`H6:H${mainEnd.end}`).format.font={name:font,size:11,color:'#14589A'};main.getRange(`Z5:Z${mainEnd.end}`).format.fill='#FFFFFF';
const roleColors={'综述核心':'#E4F2EC','相邻方法':'#E9EFF8','背景支撑':'#F6EDD9'};
detail.forEach((x,i)=>{main.getRange(`C${i+6}`).format.fill=roleColors[x.role];main.getRange(`A${i+6}`).format.font={name:font,size:11,bold:true,color:'#233E60'};});
main.freezePanes.freezeRows(5);main.freezePanes.freezeColumns(1);
title(cumulative,'四轮文献总索引','148个去重条目：20篇综述、128个研究／方法类条目。第四轮详细信息见“本轮扩展”。','#427766');
const idxHeaders=['ID','检索轮次','文献类别','年份','英文原标题／官方对应题名','中文译名／原标题','DOI','期刊／会议','主题／既有分类','原四方向','写作用途','阅读优先级','出版类型','版本／日期说明','题名与DOI核对','作者','','一手来源／作者公开稿','Crossref记录','内容提取依据'];
const idxRows=index.map(x=>[x.id,x.round,x.kind,x.year,x.en,x.zh,x.doi,x.venue,x.theme,x.direction,x.role,x.priority,x.publicationType,x.note,x.check,x.authors,'',[x.source,x.extra_source].filter(Boolean).join('\n'),x.registryUrl??'',x.basis]);
const idxWidths=[9,12,19,13,82,46,44,43,34,27,24,14,28,79,42,56,3,100,87,66];
const idxEnd=table(cumulative,5,idxHeaders,idxRows,idxWidths,'AllLiterature',85);
cumulative.getRange(`B6:B${idxEnd.end}`).setNumberFormat('0');cumulative.getRange(`D6:D${idxEnd.end}`).setNumberFormat('0');cumulative.getRange(`G6:G${idxEnd.end}`).format.font={name:font,size:11,color:'#14589A'};cumulative.getRange(`Q5:Q${idxEnd.end}`).format.fill='#FFFFFF';
cumulative.freezePanes.freezeRows(5);cumulative.freezePanes.freezeColumns(1);
title(search,'第四轮补检范围、证据与检索记录','按五类缺口定向检索；记录版本、待核项及复现资源。','#7A6547');
const notes=[
 ['项目','记录'],['截止日期','2026-10-09，Asia/Shanghai。较早公开的在线稿可纳入，未来卷期单独说明。'],
 ['本轮目标','按故障恢复与重调度、大星座规模与分解、多资源联合调度、通信受限与异步协同、工程验证与公开基准五个主题补检。'],
 ['本轮数量',`32个新增研究／方法条目：31篇Crossref题名—DOI匹配，1篇中文研究以期刊官网及正常DOI解析核对。${Object.entries(roles).map(([k,v])=>k+' '+v).join('；')}。`],
 ['累计数量','前三轮116条加本轮32条，得到148个唯一DOI：20篇综述、128个研究／方法类条目。包括会议论文、扩展摘要、技术观点与系统经验，并非128篇完整期刊论文。'],
 ['去重规则','逐条比较前三轮116个DOI，大小写无关；本轮无重复。IPEX期刊与相关早期会议稿、Wiley正式版与预印本、仿真平台与关联稿保留版本线索，不重复计数。共享案例是否重复仍待全文比对。'],
 ['DOI含义','DOI及题名核对用于编目追溯，不能证明研究结论、实验设计或规模足够。未取得DOI的候选保留官方来源，不猜测填入。'],
 ['阅读深度','出版社摘要、作者公开稿和定向正文相结合，逐条列依据。O104、O110暂为题名级；O117规模为公开正文线索待确认。尚未完成作者人工全文验收，编目核对不表示技术结论已验收。'],
 ['年份处理','O97在线2025、出版社列2026卷期；O104在线2019、卷期2020；O109在线2021、卷期2022；O122部分来源标在线2016，正式卷期2017。其余优先卷期或已公开在线年。'],
 ['DOI异常处理','P04机构页面声明10.15142/yymd-sh44，但本轮DOI解析和DataCite API返回404，移入待核区，不计入32篇。O102 Crossref未取得，但DOI解析HTTP 200且期刊官网题名、作者、卷期一致，按出版社核对纳入。'],
 ['写作用途定义','综述核心：可直接支撑管理、调度或验证主线；相邻方法：问题相邻、需要迁移假设；背景支撑：经典算法、架构和异轨道系统经验。该标签不是论文质量评分。'],
 ['原四方向','A整体自主运维与运行架构；B服务能力配置与动态调度；C物理可行性与安全；D分布式自主与协同。主表为主关联方向，可跨章节引用。'],
 ['规模提取规则','分别记录决策卫星、轨道目录对象、任务／请求、变量和时域。O101报告1000颗卫星与50—6000任务；O102实际测试30—90颗；O103的约10,700—10,860个TLE对象不能直接当作实际任务参与卫星或在役数量。'],
 ['检索范围','公开网络定向检索，追溯出版社、作者机构、会议与公开论文入口；使用Crossref逐条核对编目。未执行Web of Science／Scopus全库系统筛选，不主张穷尽。'],
 ['检索入口','公开网络检索、出版社／会议页、作者机构公开稿，Crossref按题名发现并按DOI核对；未将二手综述中的内容直接写成已核技术结论。'],
 ['全文优先提取','先读O97、O99、O101、O108、O112、O113、O116、O119、O122、O124、O126。分别提取恢复动作、资源模型、实际规模、网络条件、训练总成本、数据划分、验证配置及代码版本。'],
 ['建议写作层级','2状态感知与运行架构；3长期能力与部署配置；4任务与星地资源调度；5物理安全和感知—规避接口；6验证与比较；7持续学习与分布式运行展望。'],
 ['剩余工作','当前148条为候选库，最终引用仍需全文筛选。应先形成章节比较表，再针对缺口补检；本轮没有执行论文算法、训练或硬件实验。']
];
for(const t of themes)notes.push([t,`${counts[t]}篇。${detail.filter(x=>x.theme===t).map(x=>x.id).join('、')}。`]);
table(search,4,notes[0],notes.slice(1),[25,118],'SearchScope',55);
const pendingStart=notes.length+7;
search.getRange(`A${pendingStart}`).values=[[`待核候选（${pending.length}条；未计入148条总索引）`]];search.getRange(`A${pendingStart}`).format.font={name:font,size:11,bold:true,color:'#172B4D'};
table(search,pendingStart+2,['ID','候选文献、来源与待核原因'],pending.map(x=>[x.id,[x.title,x.zh,String(x.year),x.doi_status??'正式DOI本轮未核定',x.reason,x.role,x.source,x.extra_source].filter(Boolean).join('\n')]),[25,118],'PendingPapers',100);
const logStart=pendingStart+pending.length+7;
search.getRange(`A${logStart-2}`).values=[[`实际检索词（${queries.length}条；F1恢复，F2规模，F3资源，F4通信，F5验证）`]];
search.getRange(`A${logStart-2}`).format.font={name:font,size:11,bold:true,color:'#172B4D'};
table(search,logStart,['检索分组','实际检索词／域名过滤','入口','日期'],queries.map(x=>[x[0],x[1],'公开网络定向检索','2026-10-09']),[25,118,28,18],'SearchQueries',55);
search.getRange('A3').values=[['F1—F5为本轮检索主题；主表A—D沿用既定方向。待核项、检索词和复现入口在下方。']];
const resourceStart=logStart+queries.length+4;
table(search,resourceStart,['复现资源（不计论文数）','官方／作者入口与用途'],annotations.resources.map(x=>[x.name,[x.note,x.source,x.extra_source].filter(Boolean).join('\n')]),[25,118],'ReproductionResources',70);
search.freezePanes.freezeRows(4);
wb.recalculate();
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:2000});
await fs.writeFile(path.join(dir,'formula_error_scan.json'),scan.ndjson);
const check=await wb.inspect({kind:'table',range:'本轮扩展!A5:H9',include:'values,formulas',tableMaxRows:5,tableMaxCols:8,maxChars:4000});
await fs.writeFile(path.join(dir,'workbook_inspection.json'),check.ndjson);
const previews=[['本轮扩展','A2:G9','round4_preview.png'],['本轮扩展','N12:R13','methods_preview.png'],['文献总索引','A2:G9','index_preview.png'],['检索记录','A2:B13','search_preview.png'],['检索记录',`A${pendingStart+5}:B${pendingStart+6}`,'pending_preview.png'],['检索记录',`A${logStart}:D${logStart+3}`,'queries_preview.png'],['检索记录',`A${resourceStart}:B${resourceStart+2}`,'resources_preview.png']];
for(const [sheetName,range,file] of (process.argv.includes('--main-preview-only')?previews.slice(0,1):previews)){const blob=await wb.render({sheetName,range,scale:1.1,format:'png'});await fs.writeFile(path.join(dir,file),new Uint8Array(await blob.arrayBuffer()));}
const outputPath=path.join(dir,'星座智能运维综述文献库_第四轮补检_20261009.xlsx');
await (await SpreadsheetFile.exportXlsx(wb)).save(outputPath);
const audit={asOf:annotations.as_of,newRecords:records.length,counts,roles,previous:prior.length,cumulative:index.length,reviews:20,researchAndMethodEntries:128,uniqueDOIs:new Set(index.map(x=>x.doi.toLowerCase())).size,overlapWithPrevious:records.filter(x=>priorDois.has(x.doi.toLowerCase())).length,registryMatches:records.filter(x=>x.check.startsWith('Crossref')).length,publisherChecks:records.filter(x=>!x.check.startsWith('Crossref')).length,queries:queries.length,pendingCandidates:pending.length,manualFullTextAccepted:false,outputPath};
await fs.writeFile(path.join(dir,'delivery_audit.json'),JSON.stringify(audit,null,2));console.log(JSON.stringify(audit));
