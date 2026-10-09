import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';

const dir = path.dirname(fileURLToPath(import.meta.url));
const annotations = JSON.parse(await fs.readFile(path.join(dir,'annotations.json'),'utf8'));
const registry = JSON.parse(await fs.readFile(path.join(dir,'crossref_metadata.json'),'utf8'));
const logs = JSON.parse(await fs.readFile(path.join(dir,'search_queries.json'),'utf8'));
const decode = s => String(s??'').replaceAll('&amp;','&').replaceAll('&lt;','<').replaceAll('&gt;','>').replaceAll('&quot;','"');
const priorityOrder = {'首读':0,'重点':1,'补充':2};
function enrich(a) {
  const entry = registry[a.doi.toLowerCase()];
  const m = entry?.raw ?? {};
  const title = a.manual_title ?? decode(m.title?.[0]);
  if (!title) throw new Error(`Missing original title ${a.id}`);
  const year = a.year ?? m.published?.['date-parts']?.[0]?.[0];
  if (!year) throw new Error(`Missing publication year ${a.id}`);
  const authors = a.authors ?? (m.author ?? []).map(x=>[x.given,x.family].filter(Boolean).join(' ')).join('; ');
  const venue = a.venue ?? decode(m['container-title']?.[0]);
  const check = entry?.status === 'registry_match' ? 'Crossref题名与DOI匹配' : '期刊页面DOI核对；Crossref接口未获取';
  const pub = m.published?.['date-parts']?.[0]?.join('-') ?? String(year);
  const online = m['published-online']?.['date-parts']?.[0]?.join('-') ?? '注册记录未列';
  return {...a,title,year,authors,venue,check,pub,online,doiUrl:`https://doi.org/${a.doi}`,registryUrl:entry?.registry_url??'',language:a.language??'English'};
}
const reviews = annotations.reviews.map(enrich).sort((a,b)=>priorityOrder[a.priority]-priorityOrder[b.priority]||b.year-a.year||a.id.localeCompare(b.id));
const originals = annotations.originals.map(enrich).sort((a,b)=>priorityOrder[a.priority]-priorityOrder[b.priority]||b.year-a.year||a.id.localeCompare(b.id));
const all = [...reviews,...originals];
if(new Set(all.map(x=>x.doi.toLowerCase())).size!==all.length) throw new Error('Duplicate DOI in main tables');
for(const x of all) {
  if(!/^10\.\d{4,9}\/.+$/i.test(x.doi)) throw new Error(`Invalid DOI syntax ${x.id}`);
  if(!x.zh||!x.source) throw new Error(`Missing translation/source ${x.id}`);
  if(x.year>2026) throw new Error(`Beyond search cutoff ${x.id}`);
}
await fs.writeFile(path.join(dir,'literature_records.json'),JSON.stringify({asOf:annotations.as_of,reviews,originals},null,2));

const workbook = Workbook.create();
const reviewSheet = workbook.worksheets.add('综述覆盖');
const originalSheet = workbook.worksheets.add('原创研究');
const searchSheet = workbook.worksheets.add('检索记录');
const font = 'Arial';
function letter(n) {let s='';for(n++;n>0;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;}
function buildTable(sheet,title,note,headers,rows,widths,tableName) {
  sheet.showGridLines=false;
  sheet.getRange('A2').values=[[title]];
  sheet.getRange('A2').format.font={name:font,size:15,bold:true,color:'#172B4D'};
  sheet.getRange('A3').values=[[note]];
  sheet.getRange('A3').format.font={name:font,size:10,color:'#526277'};
  sheet.getRange('A3').format.wrapText=false;
  const last=letter(headers.length-1), end=rows.length+5;
  const range=sheet.getRange(`A5:${last}${end}`);
  range.values=[headers,...rows];
  range.format.font={name:font,size:11,color:'#172B4D'};
  range.format.verticalAlignment='top';
  range.format.wrapText=true;
  sheet.getRange(`A5:${last}5`).format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',verticalAlignment:'center',wrapText:true,rowHeight:42};
  for(let c=0;c<headers.length;c++)sheet.getRange(`${letter(c)}5:${letter(c)}${end}`).format.columnWidth=widths[c]??30;
  for(let i=0;i<rows.length;i++) {
    const row=i+6;
    if(i%2===1)sheet.getRange(`A${row}:${last}${row}`).format.fill='#F3F6FA';
    const lineCount = Math.max(...rows[i].map((v,c)=>{
      const units=[...String(v??'')].reduce((sum,ch)=>sum+(ch.charCodeAt(0)>255?1.8:1),0);
      return Math.max(1,Math.ceil(units/Math.max(8,(widths[c]??30)-2)));
    }));
    sheet.getRange(`A${row}:${last}${row}`).format.rowHeight=Math.max(62,lineCount*15+12);
  }
  const table=sheet.tables.add(`A5:${last}${end}`,true,tableName);
  table.showFilterButton=true;
  table.showBandedColumns=false;
  sheet.freezePanes.freezeRows(5);
  sheet.freezePanes.freezeColumns(1);
  return {end,last};
}
const rh=['ID','阅读优先级','年份（卷期／在线）','原标题','中文译名／中文原标题','DOI','期刊／会议','A 系统运维','B 服务规划','C 物理与安全','D 自主协同','主要覆盖内容','分类组织方式','与本综述的比较点（本轮判断）','内容提取依据','题名与DOI核对','版本与适用说明','作者','官方英文对应题名（中文原文）','一手来源／作者机构链接','Crossref记录'];
const rr=reviews.map(x=>[x.id,x.priority,x.year,x.title,x.zh,x.doi,x.venue,...x.coverage,x.focus,x.structure,x.comparison,x.basis,x.check,x.note,x.authors,x.official_en??'',x.source,x.registryUrl]);
const rv=buildTable(reviewSheet,'大型星座运维综述：已有综述覆盖表',`截至2026-10-09｜${reviews.length}条｜主线／涉及为正向编码；待核不表示未覆盖。英文译名为本轮工作译名。`,rh,rr,[9,13,13,62,38,40,32,14,14,14,14,46,34,46,31,36,49,36,52,70,70],'ReviewCoverage');
reviewSheet.tabColor='#233E60';
const oh=['ID','阅读优先级','年份（卷期／在线）','英文原标题','中文译名','DOI','期刊／会议','主题','决策阶段','轨道／场景','研究问题','方法机制','物理／资源约束','规模／时域（已提取）','验证证据（本轮范围）','与本项目的关系（本轮判断）','建议章节','内容提取依据','题名与DOI核对','版本与适用说明','作者','一手来源／作者机构链接','Crossref记录'];
const or=originals.map(x=>[x.id,x.priority,x.year,x.title,x.zh,x.doi,x.venue,x.themes,x.stage,x.orbit,x.question,x.method,x.constraints,x.scale,x.evidence,x.use,x.chapters,x.basis,x.check,x.note,x.authors,x.source,x.registryUrl]);
const ov=buildTable(originalSheet,'大型星座运维综述：代表性原创研究',`截至2026-10-09｜${originals.length}条｜GEO、MEO为方法参照，不能直接外推LEO。待提取不表示作者未报告。`,oh,or,[9,13,13,62,38,40,32,13,30,32,42,43,41,40,40,48,14,32,36,54,36,70,70],'OriginalResearch');
originalSheet.tabColor='#436B91';
for(const sheet of [reviewSheet,originalSheet]) {
  const rows=sheet===reviewSheet?reviews:originals;
  sheet.getRange(`C6:C${rows.length+5}`).setNumberFormat('0');
  sheet.getRange(`C6:C${rows.length+5}`).format.horizontalAlignment='right';
  sheet.getRange(`F6:F${rows.length+5}`).format.font={name:font,size:11,color:'#14589A'};
  rows.forEach((x,i)=>sheet.getRange(`F${i+6}`).values=[[x.doi]]);
}

searchSheet.showGridLines=false;
searchSheet.getRange('A2').values=[['检索方法、范围与版本记录']];
searchSheet.getRange('A2').format.font={name:font,size:15,bold:true,color:'#172B4D'};
const notes=[
['项目','记录'],
['范围','大型低轨星座在轨运维与协同调度，包含配置、服务规划、物理可行性、安全与自主协同。'],
['截止日期','2026-10-09，Asia/Shanghai。'],
['检索性质','公开网络定向检索、出版社／作者机构入口与Crossref编目核对。未完成Scopus／Web of Science全库系统筛选。'],
['主表条目',`${all.length}条：${reviews.length}篇综述，${originals.length}篇代表性原创研究。按正式DOI编目，数量不代表独立实验证据数量。`],
['DOI核对',`${all.filter(x=>x.check.startsWith('Crossref')).length}条取得Crossref匹配记录；其余4条由期刊页面核对，接口未获取不等于DOI无效。`],
['内容深度','包含摘要级与定向全文阅读，逐条列出依据。编目核对与内容／方法核验是不同步骤。未完成作者人工全文验收。'],
['中文译名','英文原标题采用出版注册题名或出版社题名；中文为工作译名，不冒称出版方官方译名。中文原文另列期刊官方英文题名。'],
['覆盖符号','主线：摘要或正文明确作为主体。涉及：已读内容支持正向关联。待核：尚无可靠编码，不表示没有覆盖。'],
['阅读优先级','首读、重点、补充是围绕本次选题的阅读建议，不是论文质量或证据等级评分。'],
['A 系统运维','星座整体运行组织、配置维护、运行效能和反馈。'],
['B 服务规划','服务能力、部署、补网、库存、任务分配与服务序列。'],
['C 物理与安全','轨迹、动力学、资源可行性、风险分析、约束与验证。'],
['D 自主协同','星地协同、星上自主、分布式管理与协同架构。'],
['建议写作层级','系统目标→决策阶段→模型与算法→验证证据。第3章能力与配置、第4章调度、第6章验证比较为重点。'],
['相关版本处理','O06采用期刊DOI；相关会议DOI 10.2514/6.2026-2631保留在版本说明，重合程度需阅读全文。'],
['特殊年份','R03正式卷期2021而DOI含2020；R14卷期2024而DOI含2023；O04、O11期刊卷期2026；O20已在线但登记12月卷期尚未到期。'],
['未纳入候选','学习型紧急规避轨迹、ConstellAI和NASA任务报告可后续补查。本轮未将未充分核对或无正式DOI的报告混入主表。'],
['后续人工复核','打开首读论文全文，核对假设、实际规模、基线、全部成本、保证前提和具体页／节／表；记录纳入排除理由后再形成正式综述结论。'],
];
searchSheet.getRange(`A4:B${notes.length+3}`).values=notes;
searchSheet.getRange(`A4:B${notes.length+3}`).format={font:{name:font,size:11,color:'#172B4D'},wrapText:true,verticalAlignment:'top'};
searchSheet.getRange('A4:B4').format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},wrapText:true};
searchSheet.getRange('A4:A22').format.columnWidth=24;
searchSheet.getRange('B4:B22').format.columnWidth=105;
searchSheet.getRange('A4:B22').format.autofitRows();
const logStart=notes.length+6;
const logRows=logs.map(x=>[x[0],x[1],x[2],'公开网络学术检索','2026-10-09']);
searchSheet.getRange(`A${logStart}:E${logStart+logs.length}`).values=[['批次','实际检索词／题名','用途','入口','检索日期'],...logRows];
searchSheet.getRange(`A${logStart}:E${logStart+logs.length}`).format={font:{name:font,size:11,color:'#172B4D'},wrapText:true,verticalAlignment:'top',rowHeight:48};
searchSheet.getRange(`A${logStart}:E${logStart}`).format={fill:'#233E60',font:{name:font,size:11,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:30};
searchSheet.getRange(`C${logStart}:C${logStart+logs.length}`).format.columnWidth=41;
searchSheet.getRange(`D${logStart}:D${logStart+logs.length}`).format.columnWidth=28;
searchSheet.getRange(`E${logStart}:E${logStart+logs.length}`).format.columnWidth=18;
searchSheet.tables.add(`A${logStart}:E${logStart+logs.length}`,true,'SearchLog').showFilterButton=true;

workbook.recalculate();
const errors=await workbook.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:2000});
await fs.writeFile(path.join(dir,'formula_error_scan.json'),errors.ndjson);
if(/#(REF!|DIV\/0!|VALUE!|NAME\?|NUM!|NULL!|SPILL!|CALC!)/.test(errors.ndjson)) throw new Error('Unexpected formula error: '+errors.ndjson);
const inspection=await workbook.inspect({kind:'table',range:'综述覆盖!A5:G10',include:'values,formulas',tableMaxRows:6,tableMaxCols:7,maxChars:2500});
await fs.writeFile(path.join(dir,'workbook_inspection.json'),inspection.ndjson);
const previews=[['综述覆盖','A2:G9','review_preview.png'],['原创研究','A2:G9','original_preview.png'],['检索记录','A2:B14','search_preview.png']];
for(const [sheetName,range,file] of previews) {
  const blob=await workbook.render({sheetName,range,scale:1.25,format:'png'});
  await fs.writeFile(path.join(dir,file),new Uint8Array(await blob.arrayBuffer()));
}
const output=await SpreadsheetFile.exportXlsx(workbook);
const outputPath=path.join(dir,'星座运维综述文献矩阵_20261009.xlsx');
await output.save(outputPath);
const audit={records:all.length,reviews:reviews.length,originals:originals.length,uniqueDOIs:new Set(all.map(x=>x.doi.toLowerCase())).size,registryMatches:all.filter(x=>x.check.startsWith('Crossref')).length,publisherFallbacks:all.filter(x=>!x.check.startsWith('Crossref')).map(x=>({id:x.id,doi:x.doi,source:x.source})),searchQueries:logs.length,asOf:annotations.as_of,manualFullTextReviewComplete:false,outputPath};
await fs.writeFile(path.join(dir,'delivery_audit.json'),JSON.stringify(audit,null,2));
console.log(JSON.stringify(audit));
