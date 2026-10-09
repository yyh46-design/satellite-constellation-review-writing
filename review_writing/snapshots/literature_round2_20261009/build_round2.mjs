import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir=path.dirname(fileURLToPath(import.meta.url));
const annotations=JSON.parse(await fs.readFile(path.join(dir,'round2_annotations.json'),'utf8'));
const registry=JSON.parse(await fs.readFile(path.join(dir,'crossref_metadata.json'),'utf8'));
const queries=JSON.parse(await fs.readFile(path.join(dir,'search_queries.json'),'utf8'));
const previous=JSON.parse(await fs.readFile(path.join(dir,'../literature_20261009/literature_records.json'),'utf8'));
const previousDois=new Set([...previous.reviews,...previous.originals].map(x=>x.doi.toLowerCase()));
const decode=s=>String(s??'').replaceAll('&amp;','&').replaceAll('&lt;','<').replaceAll('&gt;','>').replaceAll('&quot;','"');
const dateParts=m=>m?.['date-parts']?.[0];
const priorityOrder={'首读':0,'重点':1,'参照':2};
const names={A:'整体自主运维与运行架构',B:'服务能力配置与动态调度',C:'物理可行性与安全',D:'分布式自主与协同'};
const records=annotations.records.map(x=>{
 const entry=registry[x.doi.toLowerCase()];const m=entry?.raw??{};
 const title=x.manual_title??decode(m.title?.[0]);
 const en=x.official_en??title;
 const year=x.year??dateParts(m.published)?.[0]??dateParts(m.issued)?.[0];
 const authors=x.authors??(m.author??[]).map(a=>[a.given,a.family].filter(Boolean).join(' ')).join('; ');
 const venue=x.venue??decode(m['container-title']?.[0]);
 const check=entry?.status==='registry_match'?'Crossref题名与DOI匹配':'正式期刊PDF首页核对；Crossref未取得';
 if(!title||!en||!year||!venue||!x.zh||!x.source)throw Error('Missing required metadata '+x.id);
 if(!/^10\.\d{4,9}\/.+$/i.test(x.doi))throw Error('Invalid DOI '+x.id);
 if(year>2026)throw Error('Beyond cutoff year '+x.id);
 if(previousDois.has(x.doi.toLowerCase()))throw Error('Already in round 1 '+x.id);
 if(m.DOI&&m.DOI.toLowerCase()!==x.doi.toLowerCase())throw Error('Registry mismatch '+x.id);
 return {...x,title,en,year,authors,venue,check,registryUrl:entry?.registry_url??'',doiUrl:'https://doi.org/'+x.doi,
  pub:dateParts(m.published)?.join('-')??'',online:dateParts(m['published-online'])?.join('-')??'',print:dateParts(m['published-print'])?.join('-')??'',manualFullTextAccepted:false};
}).sort((a,b)=>a.direction.localeCompare(b.direction)||priorityOrder[a.priority]-priorityOrder[b.priority]||b.year-a.year||a.id.localeCompare(b.id));
if(new Set(records.map(x=>x.doi.toLowerCase())).size!==records.length)throw Error('Duplicate DOI');
if(new Set(records.map(x=>x.id)).size!==records.length)throw Error('Duplicate ID');
await fs.writeFile(path.join(dir,'literature_records.json'),JSON.stringify({asOf:annotations.as_of,records,pending:annotations.pending},null,2));
const counts=Object.fromEntries(Object.keys(names).map(k=>[k,records.filter(x=>x.direction===k).length]));
const wb=Workbook.create();const methods=wb.worksheets.add('新增方法研究');const search=wb.worksheets.add('检索与纳入');
const font='Arial';const letter=n=>{let s='';for(n++;n>0;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;};
function table(sheet,start,headers,rows,widths,name){
 const last=letter(headers.length-1),end=start+rows.length;
 const grid=sheet.getRange(`A${start}:${last}${end}`);
 grid.values=[headers,...rows];grid.format={font:{name:font,size:11,color:'#172B4D'},wrapText:true,verticalAlignment:'top'};
 sheet.getRange(`A${start}:${last}${start}`).format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},wrapText:true,horizontalAlignment:'center',verticalAlignment:'center',rowHeight:43};
 widths.forEach((v,i)=>sheet.getRange(`${letter(i)}${start}:${letter(i)}${end}`).format.columnWidth=v);
 rows.forEach((row,i)=>{
  const n=i+start+1;
  if(i%2)sheet.getRange(`A${n}:${last}${n}`).format.fill='#F3F6FA';
  const lines=Math.max(...row.map((v,j)=>String(v??'').split('\n').reduce((total,line)=>total+Math.max(1,Math.ceil([...line].reduce((sum,ch)=>sum+(ch.charCodeAt(0)>255?1.8:1),0)/Math.max(8,widths[j]-2))),0)));
  sheet.getRange(`A${n}:${last}${n}`).format.rowHeight=Math.max(58,lines*15+12);
 });
 const t=sheet.tables.add(`A${start}:${last}${end}`,true,name);t.showFilterButton=true;t.showBandedColumns=false;
 return {last,end};
}
methods.showGridLines=false;methods.tabColor='#233E60';
methods.getRange('A2').values=[['星座运维方法与原创研究：第二轮检索']];
methods.getRange('A2').format.font={name:font,size:15,bold:true,color:'#172B4D'};
methods.getRange('A2:H2').format.rowHeight=28;
methods.getRange('A3').values=[['截至2026-10-09，新增30篇。与第一轮按DOI去重，编号续接O22—O51。中文译名为工作译名。']];
methods.getRange('A3').format.font={name:font,size:11,color:'#526277'};
methods.getRange('A3:H3').format.rowHeight=24;
const headers=['ID','方向','阅读优先级','年份（卷期／在线）','英文原标题／中文论文英文对应题名','中文译名／中文原标题','DOI','期刊／会议','决策阶段','轨道／场景','研究问题','方法机制','约束／假设','规模与时域（已提取）','验证证据','保证与适用边界','与本项目关系（本轮判断）','建议章节','内容提取依据','题名与DOI核对','版本说明','作者','','一手来源／作者公开稿','Crossref记录'];
const rows=records.map(x=>[x.id,x.direction,x.priority,x.year,x.en,x.zh,x.doi,x.venue,x.stage,x.orbit,x.question,x.method,x.constraints,x.scale,x.evidence,x.boundary,x.use,x.chapters,x.basis,x.check,x.note,x.authors,'',[x.source,x.extra_source].filter(Boolean).join('\n'),x.registryUrl]);
const widths=[9,10,13,14,62,39,42,34,30,36,40,47,47,52,42,52,50,13,52,38,58,38,3,80,75];
const main=table(methods,5,headers,rows,widths,'Round2Methods');
methods.getRange(`D6:D${main.end}`).setNumberFormat('0');methods.getRange(`D6:D${main.end}`).format.horizontalAlignment='right';
methods.getRange(`G6:G${main.end}`).format.font={name:font,size:11,color:'#14589A'};
methods.getRange(`W5:W${main.end}`).format.fill='#FFFFFF';
methods.freezePanes.freezeRows(5);methods.freezePanes.freezeColumns(1);
search.showGridLines=false;
search.getRange('A2').values=[['第二轮检索范围与纳入记录']];search.getRange('A2').format.font={name:font,size:15,bold:true,color:'#172B4D'};
search.getRange('A2:D2').format.rowHeight=28;
const notes=[
 ['项目','记录'],
 ['日期','2026-10-09，Asia/Shanghai。'],
 ['本轮目标','沿四个方向补充方法与原创研究，优先补齐部署、库存、服务路径、在线协同和安全执行。'],
 ['纳入数量',`${records.length}篇有正式DOI的研究论文。A ${counts.A}，B ${counts.B}，C ${counts.C}，D ${counts.D}。另留2篇DOI待核候选，未计入主表。`],
 ['已有库去重','逐条对第一轮41个主表DOI进行大小写无关比较，新增无重复。第一轮21篇原创研究加本轮30篇，共51个研究型论文条目。'],
 ['DOI核对','29篇取得Crossref题名匹配，1篇中文论文以正式期刊PDF首页核对。没有用猜测补全DOI。'],
 ['内容读取范围','摘要与定向正文阅读并行。逐条列出提取依据，规模未取得时明确待提取。尚未完成作者人工全文验收。'],
 ['检索性质','公开网络定向检索，出版社、作者机构与公开论文入口交叉追溯，Crossref作编目核对。本轮不是Scopus／Web of Science全库系统筛选。'],
 ['主要纳入规则','研究问题与四方向相关，正式题名及DOI可追溯，有可提取的原始研究内容。GEO、MEO与NRHO标为方法参照。'],
 ['版本处理','预印本、机构报告与正式发表版本使用同一主表条目，列版本线索。相近团队的不同DOI仍需全文确认案例是否独立。'],
 ['年份处理','优先正式卷期年，未有卷期时用在线年。O39在线2022、卷期2023；O49卷期标2025而DOI含2026；O36登记2026年11月卷期，当前公开页面可读。'],
 ['规模的定义','分别记录服务艇／卫星数、任务／目标数、轨道面数、训练实例数及规划时域。题名中的large-scale／scalable不作为实验规模。'],
 ['A 整体自主运维','O22—O26。系统运行流程、星上平台、资源管理、观测与下传联合调度。'],
 ['B 服务配置与调度','O27—O36。部署轨道、备份库存、补网、移动服务站、多服务艇路径与不确定服务时长。'],
 ['C 物理与安全','O37—O45。接近筛查、事件精化、长期规避运行、交会轨迹与概率／连续时间安全约束。'],
 ['D 分布式自主协同','O46—O51。合同网、CBBA、异步一致性、多智能体学习及动态重规划。'],
 ['建议章节','1范围与目标，2系统架构，3能力与配置，4调度与协同，5物理安全与执行，6验证比较，7研究展望。'],
 ['全文下一步','先读O28、O29、O31、O32、O37、O41、O45、O46、O48。提取模型假设、实际规模、代价构建、保证前提、训练和求解总成本。']
];
search.getRange(`A4:B${notes.length+3}`).values=notes;search.getRange(`A4:B${notes.length+3}`).format={font:{name:font,size:11,color:'#172B4D'},wrapText:true,verticalAlignment:'top'};
search.getRange('A4:B4').format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:30};
search.getRange(`A4:A${notes.length+3}`).format.columnWidth=25;search.getRange(`B4:B${notes.length+3}`).format.columnWidth=115;
search.getRange(`A5:B${notes.length+3}`).format.autofitRows();
const pendingStart=notes.length+6;
search.getRange(`A${pendingStart}`).values=[['DOI待核候选（未计入主表）']];search.getRange(`A${pendingStart}`).format.font={name:font,size:11,bold:true,color:'#172B4D'};
const pendingRows=annotations.pending.map((x,i)=>['P'+String(i+1).padStart(2,'0'),x.title+'\n'+x.zh+'\n'+x.year+'。'+x.doi_status+'。'+x.reason+'\n'+x.source]);
table(search,pendingStart+2,['ID','候选论文信息与一手来源'],pendingRows,[25,115],'PendingCandidates');
const logStart=pendingStart+7;
const logRows=queries.map(x=>[x[0],x[1],'公开网络定向检索',new Date('2026-10-09T00:00:00Z')]);
table(search,logStart,['方向','实际检索词／域名过滤','入口','日期'],logRows,[25,115,28,18],'Round2SearchLog');
search.getRange(`D${logStart+1}:D${logStart+queries.length}`).setNumberFormat('yyyy-mm-dd');
// Restore source-note widths after table utilities share the same physical columns.
search.getRange(`A4:A${notes.length+3}`).format.columnWidth=25;search.getRange(`B4:B${notes.length+3}`).format.columnWidth=115;
search.getRange(`A5:B${notes.length+3}`).format.autofitRows();
wb.recalculate();
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:2000});
await fs.writeFile(path.join(dir,'formula_error_scan.json'),scan.ndjson);
const inspect=await wb.inspect({kind:'table',range:'新增方法研究!A5:H9',include:'values,formulas',tableMaxRows:5,tableMaxCols:8,maxChars:2500});
await fs.writeFile(path.join(dir,'workbook_inspection.json'),inspect.ndjson);
for(const [sheetName,range,file] of [['新增方法研究','A2:H9','methods_preview.png'],['新增方法研究','K11:N14','analysis_preview.png'],['检索与纳入','A2:B16','search_preview.png'],['检索与纳入',`A${pendingStart}:B${pendingStart+4}`,'pending_preview.png'],['检索与纳入',`A${logStart}:D${logStart+3}`,'queries_preview.png']]){
 const blob=await wb.render({sheetName,range,scale:1.1,format:'png'});await fs.writeFile(path.join(dir,file),new Uint8Array(await blob.arrayBuffer()));
}
const outputPath=path.join(dir,'星座运维方法研究_第二轮_20261009.xlsx');
await (await SpreadsheetFile.exportXlsx(wb)).save(outputPath);
const audit={asOf:annotations.as_of,records:records.length,counts,uniqueDOIs:new Set(records.map(x=>x.doi.toLowerCase())).size,overlapWithRound1:records.filter(x=>previousDois.has(x.doi.toLowerCase())).length,registryMatches:records.filter(x=>x.check.startsWith('Crossref')).length,publisherPDFMatches:records.filter(x=>!x.check.startsWith('Crossref')).map(x=>({id:x.id,doi:x.doi})),queries:queries.length,pendingCandidates:annotations.pending.length,manualFullTextAccepted:false,outputPath};
await fs.writeFile(path.join(dir,'delivery_audit.json'),JSON.stringify(audit,null,2));console.log(JSON.stringify(audit));
