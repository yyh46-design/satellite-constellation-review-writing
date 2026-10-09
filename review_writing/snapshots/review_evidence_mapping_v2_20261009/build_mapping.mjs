import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const dir = path.dirname(fileURLToPath(import.meta.url));
const inputPath = path.join(dir, '../review_framework_v1_20261009/screening_records.json');
const inputBytes = await fs.readFile(inputPath);
const inputHash = crypto.createHash('sha256').update(inputBytes).digest('hex');
const prior = JSON.parse(inputBytes.toString('utf8'));
const original = prior.screens;
const sections = {
  '1': '1 引言',
  '2': '2 系统框架与问题建模',
  '3.1': '3.1 长期能力配置与运维决策',
  '3.2': '3.2 动态任务与多资源联合调度',
  '3.3': '3.3 安全执行与异常恢复',
  '3.4': '3.4 跨层耦合与闭环协同',
  '4': '4 综合评价与研究展望',
  '5': '5 结论',
};

// Questions are writing tasks, not findings or additional manuscript sections.
const questionSpecs = [
  ['Q01','1','本文与已有综述的范围和比较框架有哪些差异？','研究对象、决策层级、综述时段、系统接口与证据维度','对照既有综述，界定本文范围和拟议贡献。','综述范围说明、分类表、明确排除对象与检索方式','只以已有综述作定位依据，独特性需全文对照。','既有综述覆盖矩阵'],
  ['Q02','2','集中式、分布式与混合运行架构怎样连接状态、规划和执行？','决策位置、节点职责、信息流、人工监督、触发机制','建立共同系统框架，并解释后续方法在架构中的位置。','模块和节点定义、接口、信息交换、运行触发及验证对象','软件架构提案与已运行系统分别编码。','系统架构与决策层级图'],
  ['Q03','2','状态感知与遥测异常识别怎样提供可靠的决策输入？','输入信号、训练数据、标签、阈值、漂移、误报','比较状态估计和异常检测的输入与可靠性边界。','训练测试划分、异常定义、事件指标、误报和部署条件','异常检测效果不能直接替代故障恢复或调度验证。','状态感知方法比较表'],
  ['Q04','3.1','部署与重构怎样改变覆盖和可用能力？','轨道构型、分阶段决策、需求变化、机动成本、时间','比较覆盖目标与部署、重构可执行条件的关系。','配置变量、需求场景、阶段划分、机动模型和终端要求','覆盖优化与可执行重构需分别核查。','部署与重构模型比较表'],
  ['Q05','3.1','备份与补网怎样维持星座可用性？','库存层级、失效过程、补给时延、服务水平、成本','比较备份和维护策略如何形成运行能力约束。','故障分布、库存策略、补给提前期、可用性与费用定义','数值案例和实际部署分别记录。','备份补网与维护策略表'],
  ['Q06','3.1','服务船与仓库怎样配置以满足在轨服务需求？','设施位置、船队规模、客户分配、推进方式、响应性','比较空间设施选址和服务能力配置的建模选择。','配置变量、客户需求、轨道与相位、转移代价及容量','服务案例不能直接替代常规观测或通信星座结论。','服务能力与设施配置表'],
  ['Q07','3.1','需求与故障不确定性怎样影响长期运维决策？','随机与认知不确定性、情景、风险、生命周期成本','比较长期配置中的不确定性处理与性能指标。','不确定量、信息获得时点、风险参数、成本和敏感性','区分风险模型的假设与实际运行风险。','不确定性建模比较表'],
  ['Q08','3.2','多目标在轨服务怎样联合选择、分配和安排访问？','服务船、客户、任务次序、窗口、燃料、补充','比较服务任务分配和连续访问序列的联合求解。','任务选择、路线变量、转移时间、资源更新与连续性检查','访问图和完整连续轨迹的验证范围需分别记录。','服务任务与路线调度表'],
  ['Q09','3.2','观测任务如何选择与排序，并扩展到大规模场景？','时间模型、冲突、资源、规模、分解、学习作用位置','比较基础调度模型及精确、启发式和学习混合方法。','变量约束、实例生成、卫星与任务数、上下界和总成本','不同实例及资源模型下的性能不能直接统一排名。','调度模型与求解方法表'],
  ['Q10','3.2','任务和环境变化下怎样实现鲁棒或在线重调度？','云覆盖、动态到达、风险、多目标、滚动时域','比较不确定性处理、信息更新和重规划机制。','变化模型、风险或鲁棒参数、重规划触发、收益与失败率','概率保证和经验表现分别提取。','动态与不确定调度比较表'],
  ['Q11','3.2','观测、存储和下传怎样形成完整任务链？','时间窗、任务依赖、数据库存、能量、充电、交付','比较联合观测与传输模型对任务完成定义的影响。','观测和交付变量、资源动态、耦合约束和收益定义','安排观测和完成交付的统计口径需区分。','任务链与资源耦合表'],
  ['Q12','3.2','星地通信和测控资源怎样协调排班？','接触窗口、天线容量、站点、优先级、人工协商','比较通信设施排班与星上任务调度的接口。','资源共享、时窗、冲突、实际运行流程和对照基线','深空及地面站案例作为相邻场景注明。','测控与下传排班比较表'],
  ['Q13','3.2','通信与计算资源怎样支持任务卸载和星上处理？','计算、带宽、功率、延迟、可见性、语义任务收益','比较资源分配、任务处理与观测交付之间的关系。','执行时间、节点异构性、链路模型、能耗、截止期和硬件','网络或计算仿真不直接等价于完整任务在轨运行。','通信计算与处理调度表'],
  ['Q14','3.2','异构载荷和任务依赖怎样进入协同调度？','触发任务、先后顺序、载荷类型、模式、数据依赖','比较异构任务链和载荷模式对调度模型的要求。','载荷能力、触发条件、前后关系、模式切换和交付要求','先核查具体任务链，避免把所有多星研究归为异构协同。','异构任务链示意与比较表'],
  ['Q15','3.2','分布式任务分配怎样消除冲突并满足资源约束？','拍卖、约束优化、分解、共识、代理、信息需求','比较集中与分布方法的协调机制和适用条件。','代理和变量、消息协议、收敛前提、冲突处理与资源检查','一般多机器人算法需标注向卫星场景迁移的条件。','分布式协同机制表'],
  ['Q16','3.2','延迟、丢包和异步通信怎样影响协同结果？','接触图、延迟、丢失、异步、消息成本、重复分配','比较通信受限条件下的调度与协调机制。','网络生成、延迟与丢包分布、信息版本、失败和恢复统计','网络传播性能与任务分配可行性分别核查。','通信条件与协调表现表'],
  ['Q17','3.2','空间态势感知任务怎样按信息价值和风险调度？','目标目录、传感器、信息增益、风险、可见窗口','比较传感器任务评价与星座安全决策的接口。','任务收益定义、目标状态、可见性、风险输入和后续动作','传感器任务完成不直接证明碰撞风险已经消除。','态势感知任务调度表'],
  ['Q18','3.3','计划怎样满足轨道、交会和连续执行条件？','动力学、推进、摄动、终端状态、安全区、连续时间','比较转移和交会方法对任务计划可执行性的支撑。','动力学和终端条件、连续时间检查、求解残差与参考解','低轨、地球同步轨道和月球附近场景分别标注。','物理可行性与执行检查表'],
  ['Q19','3.3','接近筛查、风险估计与规避机动怎样衔接？','最近接近、传播误差、碰撞概率、筛查、机动','比较风险计算、候选筛选与规避决策的验证范围。','误差和漏检、参考解、不确定性、规避效果与代价','事件预测、风险降低和连续安全不能混为同一保证。','碰撞风险与规避方法表'],
  ['Q20','3.3','故障发生后怎样诊断、修复计划和恢复执行？','故障种类、规则、应急计划、任务再分配、控制','比较故障处理与调度、执行恢复之间的接口。','触发条件、故障覆盖、恢复动作、剩余资源和测试对象','预定义应急范围及地面验证条件应明确记录。','异常恢复机制与证据表'],
  ['Q21','3.4','配置、调度和执行之间怎样形成闭环反馈？','层间输入输出、资源状态、执行监控、触发、重配置','核查研究真正连接了哪些层级和反馈接口。','联合变量、层间接口、反馈频率、执行失败与重规划记录','候选接口不表示已有研究已实现端到端闭环。','跨层接口与证据覆盖矩阵'],
  ['Q22','4','方法比较是否公平，规模和总成本如何计量？','基准、规模分母、硬件、训练成本、重复性、失败率','统一比较口径，解释跨研究性能比较的限制。','卫星任务数、时域、实例、数据划分、基线、资源和总代价','数量多或平均指标高均需结合条件和失败结果解释。','基准与评价条件表'],
  ['Q23','4','理论、仿真、硬件和在轨证据各支持什么结论？','验证对象、模型一致性、工具、硬件、飞行范围、复现','建立验证类型与结论范围的对应关系。','证明前提、仿真设置、板级或在环测试、飞行记录与公开材料','各证据类型提供不同支持，避免简单线性质量排序。','验证证据与适用边界表'],
  ['Q24','4','哪些接口和条件需要进一步联合研究与验证？','缺失耦合、扩展条件、不确定性、恢复、总成本','从前文比较归纳可检验的研究方向。','代表研究的实际限制、对立证据及未覆盖条件','现阶段为讨论任务，不能仅据本库数量认定研究空白。','研究问题与所需验证条件表'],
  ['Q25','5','全文结论怎样与前文已核查证据一致？','问题回答、证据范围、适用条件、贡献','综合前文结果，结论不另建立独立文献池。','回溯第2至4章已确认的论点与来源','结论沿用前文证据；不为本章强行分配独立文献。','不新增图表'],
];
const questions = questionSpecs.map(([id,section,question,axes,task,extract,boundary,display])=>({id,section,question,axes,task,extract,boundary,display}));
const qMap = new Map(questions.map(q=>[q.id,q]));

// Each line is an explicit ID-level classification. First question sets primary section.
const mappingLines = `
R01 Q02 Q15 Q01
R02 Q02 Q20 Q21 Q01
R03 Q09 Q10 Q11 Q01 Q22
R04 Q01 Q02 Q21 Q24
R05 Q02 Q01 Q23
R06 Q01 Q19
R07 Q09 Q15 Q01
R08 Q06 Q07 Q08 Q01 Q24
R09 Q09 Q11 Q12 Q01
R10 Q09 Q15 Q22 Q01
R11 Q15 Q02 Q16 Q01
R12 Q01 Q02 Q04
R13 Q09 Q22 Q01
R14 Q01 Q23 Q02 Q24
R15 Q19 Q18 Q01 Q24
R16 Q06 Q05 Q18 Q01
R17 Q06 Q08 Q18 Q01
R18 Q04 Q09 Q01
R19 Q13 Q21 Q01
R20 Q02 Q13 Q16 Q01
O01 Q07 Q06 Q08 Q21
O02 Q06 Q08 Q18 Q21
O03 Q06 Q08
O04 Q06 Q08 Q18 Q21
O05 Q05 Q07
O06 Q05 Q07 Q21 Q24
O07 Q08 Q06 Q18 Q21
O08 Q18 Q08
O09 Q18 Q08 Q21
O10 Q18 Q08 Q21
O11 Q08 Q18 Q21
O12 Q17 Q19
O13 Q18 Q08
O14 Q12
O15 Q13 Q02 Q21
O16 Q02 Q21
O17 Q11 Q09
O18 Q14 Q11 Q21
O19 Q08 Q18 Q21
O20 Q08 Q06
O21 Q02 Q21 Q23
O22 Q02 Q21 Q23
O23 Q09 Q15 Q22
O24 Q02 Q13 Q23
O25 Q09 Q10 Q22
O26 Q11 Q13
O27 Q05 Q07 Q22
O28 Q06 Q08
O29 Q08 Q06 Q18 Q21
O30 Q08 Q07
O31 Q08 Q07
O32 Q08 Q15
O33 Q07 Q05 Q22
O34 Q08 Q06 Q22
O35 Q05 Q07
O36 Q05 Q07
O37 Q19 Q22 Q24
O38 Q19 Q22
O39 Q19 Q23
O40 Q18 Q23
O41 Q18 Q23
O42 Q18 Q23
O43 Q18
O44 Q18 Q23
O45 Q18 Q23
O46 Q15 Q16 Q24
O47 Q15 Q09
O48 Q15 Q10
O49 Q15 Q09
O50 Q15 Q09
O51 Q15 Q10 Q02 Q21
O52 Q04 Q18
O53 Q04 Q18
O54 Q04 Q07
O55 Q04 Q22
O56 Q04 Q22
O57 Q04
O58 Q04
O59 Q02 Q20 Q21 Q23
O60 Q03 Q22
O61 Q03 Q22
O62 Q03
O63 Q03 Q22
O64 Q22 Q03 Q24
O65 Q09
O66 Q10 Q09
O67 Q10 Q09
O68 Q10 Q09
O69 Q09 Q10
O70 Q09 Q22
O71 Q10 Q15
O72 Q12 Q11
O73 Q12 Q23
O74 Q12 Q09
O75 Q12 Q09
O76 Q02 Q12 Q21 Q23
O77 Q12 Q11
O78 Q13 Q15
O79 Q13
O80 Q13 Q15
O81 Q13 Q11
O82 Q13
O83 Q13
O84 Q17 Q19
O85 Q17
O86 Q17
O87 Q17 Q09
O88 Q22 Q19
O89 Q17 Q09
O90 Q15 Q09 Q22
O91 Q15 Q09
O92 Q15 Q21 Q22
O93 Q15 Q16
O94 Q15
O95 Q02 Q15 Q22
O96 Q17 Q12
O97 Q20 Q03 Q23
O98 Q20 Q15 Q21
O99 Q21 Q20 Q23
O100 Q20
O101 Q09 Q22 Q24
O102 Q14 Q09 Q22
O103 Q09 Q22
O104 Q09 Q22
O105 Q09 Q22
O106 Q09 Q22
O107 Q11
O108 Q11
O109 Q11
O110 Q11 Q15
O111 Q21 Q11 Q02
O112 Q13 Q11 Q21 Q24
O113 Q16 Q11
O114 Q16 Q15
O115 Q16 Q15
O116 Q16 Q15 Q22
O117 Q02
O118 Q23 Q22
O119 Q22 Q09
O120 Q18 Q23
O121 Q09 Q14 Q22
O122 Q21 Q23 Q13
O123 Q23
O124 Q23 Q22 Q24
O125 Q13
O126 Q20 Q21 Q23 Q24
O127 Q20 Q10
O128 Q13 Q11 Q23
`;
const mappings = new Map(mappingLines.trim().split('\n').map(line=>{const [id,...qids]=line.trim().split(/\s+/);return [id,qids];}));
const currentChecks = {
  R03: {
    status: '本轮已核原文局部；完整精读待完成',
    locator: '作者公开稿v1：§2.1–2.2模型与约束；§3方法分类；§4.2集成调度。目录与基本假设已定位。',
    basis: '2026-10-09核查作者2020年公开稿目录、问题假设与分类；正式期刊版差异待核。',
    sources: ['https://arxiv.org/html/2003.06169'],
    constraints: '时间窗、任务转换、星上能量与存储；基本模型假设下传资源充足。',
    evidence: '综述文献归纳，非新增系统运行实验。',
    limit: '该稿主要讨论敏捷观测调度；下传集成作为展望，不能据此证明完整任务链已实现。',
  },
  O27: {
    status: '本轮已核原文局部；完整精读待完成',
    locator: '作者公开稿v4：§4.2模型假设；§4.3–4.4库存层级目录；§5模型精度评价开头；§6–7优化与案例目录。',
    basis: '2026-10-09核查作者公开稿摘要、§4.2假设及§5验证方式。',
    sources: ['https://arxiv.org/html/1807.02685v4'],
    constraints: '多级(s,Q)库存、随机补给时延；轨道面内备份视为立即可用，替换延迟未计入。',
    evidence: '解析库存模型，以拉丁超立方抽样仿真评价精度；数值案例。',
    limit: '解析模型采用简化库存和供给假设；面内即时替换假设需在实际星座中检验。',
  },
  O60: {
    status: '本轮已核原文局部；完整精读待完成',
    locator: '作者公开稿v3：摘要；§3方法目录；§4.1数据设置；§4.2阈值对照；§4.3表2阈值结果。',
    basis: '2026-10-09核查作者公开稿摘要、实验设置及阈值比较片段。',
    sources: ['https://arxiv.org/html/1802.04431v3'],
    evidence: 'SMAP卫星和MSL火星车的专家标记遥测；阈值与误报抑制对照。',
    limit: '真实遥测检测证据不直接证明自动恢复或星座级闭环；训练窗口和评价口径需保留。',
  },
  O64: {
    status: '本轮已核原文局部；完整精读待完成',
    locator: '出版社HTML：§3.2指标；§3.3比较评价；§4.1.1–4.1.3数据及设置。',
    basis: '2026-10-09核查出版社摘要及方法、评价和数据设置片段。',
    sources: ['https://link.springer.com/article/10.1007/s12567-023-00529-5'],
    evidence: '真实卫星遥测与公开数据集的重评，比较指标、阈值和简单基线。',
    limit: '阈值选择和指标处理影响结果；结论需保留数据与评价条件，不能外推所有深度方法。',
  },
  O112: {
    status: '本轮已核作者摘要；全文与期刊版待核',
    locator: 'arXiv:2604.05937v1摘要及Comments；该作者版本声明投稿，正式期刊版需另核。',
    basis: '2026-10-09核查作者预印本摘要；原期刊DOI沿用前轮编目。',
    sources: ['https://arxiv.org/abs/2604.05937'],
    evidence: '作者摘要报告观测与处理策略评估及不同计算平台的推理执行时间实验。',
    limit: '作者预印本与期刊版本差异待核；计算平台测量不能替代全星座在轨证据。',
  },
};
const pending = new Set(original.filter(r=>r.tier==='待全文判定').map(r=>r.id));
const sectionOrder = ['1','2','3.1','3.2','3.3','3.4','4','5'];
const tierOrder = ['首轮锚点精读','第二轮专题精读','背景或方法参照','待全文判定'];
const records = original.map(r=>{
  const qids = mappings.get(r.id);
  if(!qids || qids.some(id=>!qMap.has(id))) throw new Error('Invalid question map '+r.id);
  const primary = qMap.get(qids[0]);
  const auxiliary = [...new Set(qids.slice(1).map(id=>qMap.get(id).section))].filter(s=>s!==primary.section);
  const c = currentChecks[r.id];
  const isReview = r.id.startsWith('R');
  const isPending = pending.has(r.id);
  const status = c?.status ?? (isPending?'题名或片段定位；技术内容待核':'沿用前轮提取；待完整全文核查');
  return {
    ...r, qids, primarySection: primary.section, auxiliarySections: auxiliary,
    researchQuestion: r.question || r.focus || '具体研究问题待全文提取。',
    modelMethod: isPending ? '当前仅作主题定位；具体模型与算法待一手全文提取。' : r.method || r.focus || '模型与方法待全文提取。',
    modelConstraints: c?.constraints || (isPending?'关键假设与约束待全文提取。':r.constraints || '该综述的范围、模型假设和约束分类待逐项全文提取。'),
    evidenceScope: isPending?'验证类型、设置和结果待全文提取。':c?.evidence || r.evidence || (isReview?'综述归纳材料；具体技术结论需回溯原始研究。':'验证类型与结果待全文提取。'),
    extractionBasis: c?.basis || r.basis || '现有编目与初筛记录。',
    readingStatus: status,
    locator: c?.locator || '尚无经全文核查的精确页码、章节或图表位置。',
    plannedUse: isReview ? primary.task+' 作为既有综述或分类参照。' : (r.use || primary.task),
    evidenceLimit: [c?.limit || r.boundary || r.limits || primary.boundary, r.note].filter(Boolean).join('\n'),
    sources: [...new Set([...(c?.sources || []),r.source,r.extra_source,r.doiUrl || 'https://doi.org/'+r.doi].filter(Boolean))],
    currentCheckDate: c?new Date('2026-10-09T00:00:00Z'):null,
    humanVerified: false,
  };
}).sort((a,b)=>sectionOrder.indexOf(a.primarySection)-sectionOrder.indexOf(b.primarySection) || tierOrder.indexOf(a.tier)-tierOrder.indexOf(b.tier) || a.id[0].localeCompare(b.id[0]) || Number(a.id.slice(1))-Number(b.id.slice(1)));

if(records.length!==148 || mappings.size!==148) throw new Error('Expected 148 records');
if(new Set(records.map(r=>r.doi.toLowerCase())).size!==148) throw new Error('DOI uniqueness failed');
for(const r of original){
  const out=records.find(x=>x.id===r.id);
  if(!out || out.en!==r.en || out.zh!==r.zh || out.doi!==r.doi) throw new Error('Source identity changed '+r.id);
}

const wb=Workbook.create();
const guide=wb.worksheets.add('章节与研究问题');
const matrix=wb.worksheets.add('148篇文献证据对应');
const font='Arial';
const colors={dark:'#243A59',secondary:'#47665B',body:'#25334A',line:'#D9E1EA',amber:'#FFF3D3'};
function colName(n){let s='';for(let i=n+1;i>0;i=Math.floor((i-1)/26))s=String.fromCharCode(65+(i-1)%26)+s;return s;}
function weightedLen(s){return [...String(s??'')].reduce((n,c)=>n+(/[^\x00-\xff]/.test(c)?1.8:1),0);}
function table(sheet,start,headers,rows,widths,name,maxHeight=160){
  const end=start+rows.length,last=colName(headers.length-1);
  const area=sheet.getRange(`A${start}:${last}${end}`);
  area.values=[headers,...rows];
  area.format={font:{name:font,size:11,color:colors.body},verticalAlignment:'top',wrapText:true};
  widths.forEach((w,i)=>sheet.getRange(`${colName(i)}${start}:${colName(i)}${end}`).format.columnWidth=w);
  const t=sheet.tables.add(`A${start}:${last}${end}`,true,name);t.showFilterButton=true;t.style='TableStyleMedium2';
  sheet.getRange(`A${start}:${last}${start}`).format={fill:colors.dark,font:{name:font,size:11,bold:true,color:'#FFFFFF'},rowHeight:34,verticalAlignment:'center',horizontalAlignment:'center',wrapText:true};
  for(let i=0;i<rows.length;i++){
    const lines=Math.max(...rows[i].map((v,j)=>Math.max(1,...String(v??'').split('\n').map(line=>Math.ceil(weightedLen(line)/Math.max(widths[j]-3,4))))));
    sheet.getRange(`A${start+i+1}:${last}${start+i+1}`).format.rowHeight=Math.min(maxHeight,Math.max(38,lines*14+12));
  }
  return {start,end,last};
}
function opening(sheet,title,note,color){
  sheet.showGridLines=false;sheet.tabColor=color;
  sheet.getRange('A2').values=[[title]];sheet.getRange('A2').format={font:{name:font,size:16,bold:true,color:colors.dark},rowHeight:26,wrapText:false};
  sheet.getRange('A3').values=[[note]];sheet.getRange('A3').format={font:{name:font,size:11,color:'#56647A',italic:true},rowHeight:22,wrapText:false};
}
opening(guide,'五章综述：研究问题与文献对应','问题ID用于归类，不增加目录层级。文献ID清单为本轮映射，包含跨小节辅助用途。',colors.dark);
opening(matrix,'148篇文献：章节、研究问题与证据','方法与证据沿用前轮提取，局部原文核查单独标记。U列为空隔列，X列可补作者复核记录。',colors.secondary);
const headers=['ID','主用章节或小节','辅助章节或小节','研究问题ID','论文研究问题或综述范围','英文原标题或官方对应题名','中文译名或原文题名','DOI','年份','期刊或会议','模型与方法','关键假设与约束','证据类型及范围','内容提取依据','阅读与核查状态','已核或待核原文位置','拟写作用途','适用限制与待核事项','精读安排','全文核查重点问题','','一手来源与作者公开稿','本轮局部核查日期','作者复核记录（可填）','文献类别'];
const widths=[9,32,42,25,60,76,46,43,11,46,70,66,72,68,45,83,72,83,25,85,3,102,22,64,17];
const rows=records.map(r=>[
  r.id,sections[r.primarySection],r.auxiliarySections.map(s=>sections[s]).join('\n') || '无额外章节',r.qids.join('、'),r.researchQuestion,
  r.en,r.zh,r.doi,r.year,r.venue,r.modelMethod,r.modelConstraints,r.evidenceScope,r.extractionBasis,r.readingStatus,r.locator,
  r.plannedUse,r.evidenceLimit,r.tier,r.readingQuestion,'',r.sources.join('\n'),r.currentCheckDate,'',r.kind,
]);
const mr=table(matrix,5,headers,rows,widths,'LiteratureEvidence148',175);
matrix.getRange(`I6:I${mr.end}`).setNumberFormat('0');
matrix.getRange(`W6:W${mr.end}`).setNumberFormat('yyyy-mm-dd');
matrix.getRange(`H6:H${mr.end}`).format.font={name:font,size:11,color:'#14589A'};
matrix.getRange(`U5:U${mr.end}`).format.fill='#FFFFFF';
matrix.getRange(`X6:X${mr.end}`).format.fill='#FFF5DA';
matrix.getRange(`O6:O${mr.end}`).conditionalFormats.add('containsText',{text:'技术内容待核',format:{fill:'#FFF0CF',font:{color:'#795214'}}});
matrix.getRange(`O6:O${mr.end}`).conditionalFormats.add('containsText',{text:'已核原文局部',format:{fill:'#E7F0E9',font:{color:'#335847'}}});
matrix.getRange(`S6:S${mr.end}`).dataValidation={rule:{type:'list',values:tierOrder}};
matrix.freezePanes.freezeRows(5);matrix.freezePanes.freezeColumns(2);

const chapterRows=[
  ['1','引言','选题范围、既有综述与拟议贡献',null,'综述覆盖矩阵','检索方法与范围需在写作时补齐。'],
  ['2','系统框架与问题建模','状态、对象、层级、接口、共性目标与约束',null,'系统框架图','第3章再展开具体方法。'],
  ['3','多层次管理、调度与执行方法','长期配置、动态调度、安全执行、跨层协同',null,'专题方法与接口表','沿用3.1至3.4四个小节。'],
  ['4','综合评价与研究展望','比较条件、验证范围、可复现性与研究问题',null,'评价及证据矩阵','多数文献也可辅助本章，主用数量不代表全部引用。'],
  ['5','结论','回答核心问题，保留证据适用范围',null,'不新增图表','承接前文已核证据，不单设独立文献池。'],
];
table(guide,5,['章','一级标题','论证任务','主用文献数','计划图表','写作说明'],chapterRows,[9,35,62,16,45,76],'FiveChapterPlan',100);
chapterRows.forEach((r,i)=>{
  const categorySections=sectionOrder.filter(s=>s.split('.')[0]===r[0]);
  const parts=categorySections.map(s=>`COUNTIFS('148篇文献证据对应'!$B$6:$B$153,"${sections[s]}")`);
  guide.getRange(`D${6+i}`).formulas=[['='+parts.join('+')]];
});
guide.getRange('D6:D10').setNumberFormat('0');
guide.getRange('D6:D10').format.horizontalAlignment='center';
guide.getRange('A12').values=[['原文位置未取得时保留待核，不依据题名或摘要填入精确页码及性能结论。']];
guide.getRange('A12').format={font:{name:font,size:11,color:'#56647A'},wrapText:false,rowHeight:22};
const qRows=questions.map(q=>{
  const linked=records.filter(r=>r.qids.includes(q.id));
  const first=linked.filter(r=>r.tier==='首轮锚点精读').slice(0,5);
  const anchors=first.length?first:linked.filter(r=>r.tier!=='待全文判定').slice(0,4);
  return [q.id,sections[q.section],q.question,q.axes,q.task,linked.map(r=>r.id).join('、') || '承接前文已核证据',anchors.map(r=>r.id).join('、') || '承接前文证据',q.extract,q.boundary,q.display];
});
const qr=table(guide,15,['问题ID','主用章节或小节','本节拟回答的问题','比较维度','拟写作任务','关联文献ID（本轮）','优先候选ID（本轮）','需从原文提取的证据','比较与证据边界','计划图表'],qRows,[9,35,62,62,64,65,37,85,85,48],'ResearchQuestionMap25',150);
guide.freezePanes.freezeRows(15);guide.freezePanes.freezeColumns(2);

const expectedChapters=['1','2','3','4','5'].map(c=>records.filter(r=>r.primarySection.split('.')[0]===c).length);
wb.recalculate();
const observed=guide.getRange('D6:D10').values.map(r=>r[0]);
if(JSON.stringify(expectedChapters)!==JSON.stringify(observed)) throw new Error('Chapter counts mismatch '+JSON.stringify(observed));
const expectedCounts=questions.map(q=>records.filter(r=>r.qids.includes(q.id)).length);
for(let i=0;i<questions.length;i++) if(guide.getRange(`F${16+i}`).values[0][0]!==qRows[i][5]) throw new Error('Question ID list mismatch');
// Verify dynamic counts, restoring source input before delivery.
const savedMain=matrix.getRange('B6').values[0][0];
matrix.getRange('B6').values=[[sections['2']]];wb.recalculate();
const changed=guide.getRange('D6:D10').values.map(r=>r[0]);
if(changed[0]!==expectedChapters[0]-1 || changed[1]!==expectedChapters[1]+1) throw new Error('Chapter count did not respond to input edit');
matrix.getRange('B6').values=[[savedMain]];
wb.recalculate();
if(JSON.stringify(guide.getRange('D6:D10').values.map(r=>r[0]))!==JSON.stringify(expectedChapters)) throw new Error('Chapter restore mismatch');
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:1500});
await fs.writeFile(path.join(dir,'formula_scan.ndjson'),scan.ndjson);
const inspected=await wb.inspect({kind:'table',range:'章节与研究问题!A5:F10',include:'values,formulas',tableMaxRows:6,tableMaxCols:6,maxChars:4500});
await fs.writeFile(path.join(dir,'inspection.ndjson'),inspected.ndjson);
const rowOf=id=>6+records.findIndex(r=>r.id===id);
const previews=[
  ['章节与研究问题','A2:F10','chapters_preview.png'],
  ['章节与研究问题','A15:G20','questions_preview.png'],
  ['148篇文献证据对应','A2:E9','mapping_preview.png'],
  ['148篇文献证据对应',`F5:J8`,'titles_preview.png'],
  ['148篇文献证据对应',`K${rowOf('O27')}:M${rowOf('O27')}`,'evidence_preview.png'],
  ['148篇文献证据对应',`N${rowOf('O27')}:P${rowOf('O27')}`,'locator_preview.png'],
  ['148篇文献证据对应',`Q${rowOf('O27')}:R${rowOf('O27')}`,'limits_preview.png'],
];
for(const [sheetName,range,name] of (process.argv.includes('--final-preview')?previews.filter(p=>p[2]==='chapters_preview.png'||p[2]==='evidence_preview.png'||p[2]==='locator_preview.png'||p[2]==='limits_preview.png'):previews)){
  const blob=await wb.render({sheetName,range,scale:1,format:'png'});
  await fs.writeFile(path.join(dir,name),new Uint8Array(await blob.arrayBuffer()));
}
const outputPath=path.join(dir,'五章综述_章节研究问题文献证据对应表_148篇_v2_20261009.xlsx');
await (await SpreadsheetFile.exportXlsx(wb)).save(outputPath);
const afterHash=crypto.createHash('sha256').update(await fs.readFile(inputPath)).digest('hex');
if(afterHash!==inputHash) throw new Error('Prior source was changed');
const audit={asOf:'2026-10-09',outputPath,sourceHash:inputHash,sourceUnchanged:true,total:records.length,uniqueDOIs:148,reviews:records.filter(r=>r.id.startsWith('R')).length,originals:records.filter(r=>r.id.startsWith('O')).length,allTitlesTranslationsDOIsPreserved:true,questions:questions.length,chapterCounts:Object.fromEntries(['1','2','3','4','5'].map((x,i)=>[x,expectedChapters[i]])),subsectionCounts:Object.fromEntries(sectionOrder.map(s=>[s,records.filter(r=>r.primarySection===s).length])),localOriginalPassageChecks:['R03','O27','O60','O64'],localAbstractCheck:['O112'],technicalPending:[...pending],fullTextHumanVerificationCompleted:0,priorityCounts:Object.fromEntries(tierOrder.map(t=>[t,records.filter(r=>r.tier===t).length])),questionCounts:Object.fromEntries(questions.map((q,i)=>[q.id,expectedCounts[i]])),formulaInputUpdateAndRestoreChecked:true};
await fs.writeFile(path.join(dir,'mapping_records.json'),JSON.stringify({asOf:audit.asOf,questions,records},null,2));
await fs.writeFile(path.join(dir,'delivery_audit.json'),JSON.stringify(audit,null,2));
console.log(JSON.stringify(audit));
