from pathlib import Path
import json,re,hashlib,collections,html,urllib.parse

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'review_full_draft_20261010'
old=(BASE/'REVIEW_FULL_v0.6.md').read_text(encoding='utf-8')
base_manifest=json.loads((BASE/'SOURCE_AND_CLAIM_RECORD_v0.6.json').read_text(encoding='utf-8'))
selection=json.loads((ROOT/'CANDIDATE_SELECTION_v0.7.json').read_text(encoding='utf-8'))['selected']
meta=json.loads((ROOT/'BIBLIOGRAPHY_ADDITIONS_METADATA_v0.7.json').read_text(encoding='utf-8'))
excluded={'O53','O08','O104','O85'}
selected=[x for x in selection if x['ID'] not in excluded]
byid={x['ID']:x for x in selected}
bydoi={x['DOI'].lower():x for x in selected}

def keep(doi, section):
    s=old[old.index(section):]
    if '\n## ' in s: s=s.split('\n## ',1)[0]
    ps=[p for p in s.split('\n\n') if doi in p and not p.startswith('|')]
    if not ps: raise ValueError((doi,section))
    return ps[0]

ch31='''## 3.1 长期能力配置与运维决策

长期配置决定未来可以调用哪些卫星、备用资源和服务设施。覆盖需求、随机失效与轨道转移分别影响能力的位置、数量及到位时间。空间物流综述{{R08}}将网络流、库存和任务运行纳入共同的问题范围；以下按构型、备份和服务能力比较具体模型。

构型研究可沿“目标构型—转移过程—分阶段变化”理解。Appel等{{10.1016/j.actaastro.2014.02.016}}优化多星重构机动，突出终端构型关系对转移代价的影响；Lee和Ho{{10.2514/1.A35685}}联合选择区域覆盖构型和卫星分配，权衡覆盖与机动成本；多阶段重构{{10.2514/1.A35990}}则让各阶段的构型和转移共同参与决策。这些模型分别使用给定目标、区域需求或预先已知的阶段需求，离线多阶段设计与未知需求下的在线响应具有不同的信息条件。

相近研究进一步改变需求和部署假设。复杂区域模式设计{{O57}}以访问模式和星座模式的循环卷积关系组织二元整数规划；不确定关注区域下的部署优化{{O54}}将需求情景纳入部署策略评价。Gwon和Ahn{{O58}}把有限停泊时间、J₂引起的升交点赤经（RAAN）漂移、发射容量及完成窗口纳入两阶段设计，分析成本—完成时间权衡。该文的可部署性是设计层面的RAAN可达性筛选，未完整建模发射轨迹和运行部署过程，因此不宜把这种筛选等同于全部卫星已经到位。

@@INVENTORY@@

双供应通道模型{{10.2514/1.A36281}}将经停泊轨道转移和直接注入目标轨道面两种补给过程共同纳入库存策略。Han等的马尔可夫链研究{{O35}}分别描述轨道面和停泊库存，再用不动点迭代求相互一致的稳态；其双通道扩展{{O36}}继续将直接和间接补给纳入状态演化。这一研究组从供应途径和随机状态两方面细化库存分析，比较时应同时保留失效过程、补给时间及轨道条件。稳态供应表现描述长期平均行为，某次故障后的业务恢复仍需相应的时间过程。

Iridium新增5颗备星的公开部署资料{{ENG:iridium}}说明备份是实际运营配置的一部分。数量体现冗余水平，所在位置和转移条件决定何时能够接替业务。因此，库存设计可通过备份数量、供应等待和恢复时间与运行调度连接。

@@MAINTENANCE@@

@@DEPOT@@

服务能力的配置还受未来需求和推进方式影响。服务船部署研究{{10.1155/2021/6644339}}选择预部署轨道并评价潜在客户可达性，需求不确定性框架{{10.2514/1.A34978}}则利用滚动时域更新服务与物流活动。高、低推力权衡框架{{O02}}把用户定义的轨迹模型接入混合整数线性规划，使推进技术与短期排程、长期设施决策共同比较。生命周期评估{{O33}}进一步区分随机与认知不确定性。它们扩展的是需求信息、转移模型和评价时域，不能用同一个静态“服务容量”代替这些条件。

这组研究把长期投入转化为位置、可用时刻、资源余量和成本。其与日常调度的连接，需要明确配置怎样改变未来可执行活动集合，以及失效或需求变化何时触发更新。

---

'''
ch31=ch31.replace('@@INVENTORY@@',keep('10.2514/1.A34387','## 3.1')).replace('@@MAINTENANCE@@',keep('10.2514/1.A36684','## 3.1')).replace('@@DEPOT@@',keep('10.2514/1.A35691','## 3.1'))

ch32='''## 3.2 动态任务与多资源联合调度

运行调度在任务窗口和可用资源下选择、分配及排序活动。研究之间的差别不仅是求解算法，还包括信息由谁掌握、哪些后续资源参与选择，以及新任务或异常如何改变已有计划。以下按搜索分解、主体协调、任务链和在线计划组织比较，代表研究的具体条件集中列于表2。

### 搜索分解与任务表示

敏捷卫星调度的早期研究{{O65}}比较贪心、动态规划、约束规划和局部搜索，说明选择与定时需要随姿态机动和任务窗口共同处理。通用马尔可夫决策过程研究{{O69}}以学习处理排序、以构造式启发式确定时刻；大规模多目标分解学习{{O105}}又结合任务分配、排序及全局修补。这些方法改变决策表示和搜索组织，学习生成的排序仍需要对应可执行时序。

@@DECOMPOSITION@@

### 主体间协调与信息条件

@@PARJAN@@

@@GND@@

分布式方法还有不同的信息与组织出发点。Krigman等{{O91}}把多主体观测请求表示为分布式约束优化问题，利用分布式随机算法和最大增益消息算法生成时刻表，减少向中央主体预先集中私有请求的需要。一致性任务包拍卖{{O93}}则组合局部竞价和一致性消冲突机制，为后续卫星任务分配提供通用方法基础。前者围绕请求所属主体及约束信息，后者围绕任务包与竞价共识；请求权限、协调消息和隐私保护机制属于不同的建模条件，比较时需分别说明。

通信受限研究把消息可达性纳入运行条件。Li等{{10.1016/j.asr.2020.02.018}}在同步和异步任务包方法中加入通信机会预测，实验中的收益与交互次数权衡随通信成本改变。延迟通信下的多星规划{{O114}}使用时延处理和协同决策模型，不确定环境下的星上调度{{O51}}结合合同网、黑板协调及滚动规划。异步市场分配{{O115}}进一步研究消息延迟、丢失和动态事件，但属于通用多智能体环境，不能直接作为真实星间网络的效果证据。它们共同补充了“需要什么消息”和“消息何时到达”两个条件。

### 观测、传输与处理任务链

观测收益逐渐向后续资源延伸。He等{{10.1109/TMC.2021.3076088}}将成像和传输窗口统一为整数线性规划，以半正定松弛与遗传算法组合求解；能源约束联合调度{{10.1016/j.actaastro.2025.02.008}}继续加入充电，利用多背包分配和局部搜索改进蚁群方法。集成敏捷观测调度{{O17}}补充成像与下传共同安排的问题表达；异构星座提示—精细观测调度{{O18}}则利用混合整数线性规划处理具有先后依赖的观测活动。各模型推进了不同深度的任务链，增加成像机会、完成下传和完成后续观测分别对应不同收益阶段。

地面资源研究进一步说明，可见窗口还需要转化为无冲突的通信安排。单星—多站优化{{O72}}讨论通信机会和可行排程，空军卫星控制网络研究{{O74}}比较受共享资源竞争影响的调度方法，下传案例{{O77}}将业务约束接入调度生成过程。深空网络的混合整数规划{{O75}}提供另一种天线排程表达；Johnston等{{O76}}的调度引擎将用户需求展开为跟踪时段，组合搜索与修复，并接入运营协商流程。它们属于不同网络和任务场景，价值在于说明共享地面设施、请求表达和计划修复怎样影响可用通信资源。

公开服务接口使完成事件和资源承诺更加具体。Planet Tasking API{{ENG:planet}}区分采集、质量满足和交付；相应灵活产品可能在订单期限内继续采集。AWS Ground Station{{ENG:aws}}在预约时保存任务配置快照，后续配置更新需取消并重约才能应用到已有预约。前者提供复采触发条件，后者提供资源承诺与更新条件，联合调度可以据此区分已采集、合格产品和已确认通信安排。

@@EDGE@@

计算卸载研究补充任务链中的处理位置和资源分配。多智能体卸载与资源优化{{O78}}、LEO边缘计算的集中训练与分散执行{{O80}}以及星地协同推理资源管理{{O81}}，分别组合卸载决策、学习与资源优化。轨道感知调度{{O125}}把轨道运动与通信可见性纳入分布式计算安排，并以离散事件仿真评价任务响应；Kodan{{O128}}通过离线生成专用模型和运行时选择，缓解星上计算与下传之间的瓶颈。它们主要评价计算任务或数据价值，接入观测系统时，还需说明处理结果如何改变任务完成状态及下一轮选择。

### 不确定性、在线更新与策略部署

新任务到达后的改进可以发生在重新搜索或协调环节。Qi等{{10.1016/j.eswa.2025.128502}}利用滚动时域形成连续静态子问题，由深度强化学习生成初解，再通过大邻域搜索的破坏—修复改善安排。滚动时域多智能体学习{{O48}}采用集中训练、分散执行的策略组织；前述通信预测{{10.1016/j.asr.2020.02.018}}和合同网协调{{O51}}则更直接处理成员间的信息和更新时机。共同评价应覆盖任务收益、更新时限和计划改动，但各方法实际减少的是搜索、训练或协调中的不同成本。

@@RL@@

### 服务任务的路径、补给与不确定性

在轨服务同样需要选择、分配和排序任务，还须处理移动客户、轨道转移与补给。可加注服务机器人的多轨路径调度{{10.1016/j.cie.2022.108852}}用时变网络统一访问与补给；GEO加注鲁棒调度{{10.1016/j.cja.2025.103774}}则采用预算不确定集描述服务时长并搜索服务分配及顺序。多服务星任务规划{{O07}}补充多目标搜索与轨道转移的联合选择，GEO加注和碎片移除混合规划{{O30}}比较随机期望与鲁棒不确定性表达。合并讨论的依据是共同的访问与执行依赖，而不同推进、服务类型和不确定性条件仍需分开。

@@LOWTHRUST@@

Apa等较早的多客户低推力研究{{O09}}在出发与到达轨道、质量和时刻上构造转移代价网格，插值后比较组合路径搜索；其摄动、地影和质量变化使路径代价随状态变化，但该模型忽略相位机动代价。与上述低轨漂移研究一起看，预计算能够减少路线搜索成本，终端交会、相位和安全条件是否进入代价模型，则决定离散最优路线能够支持何种执行结论。

这些比较组共同覆盖任务选择与资源竞争。数学分解改变搜索组织，主体协调改变信息范围，学习改变初解或策略生成，资源耦合与在线计划更新则改变候选活动和任务完成阶段。表2保留核心研究的模型和验证条件，避免用统一性能分数混合不同问题。

@@TABLE2@@

---

'''
for tag,doi in [('DECOMPOSITION','10.1016/j.cor.2025.107259'),('PARJAN','10.2514/1.I011215'),('GND','10.1613/jair.1.16997'),('EDGE','10.1002/sat.70082'),('RL','10.2514/1.A35736'),('LOWTHRUST','10.1007/s40295-026-00580-4')]:
    ch32=ch32.replace('@@'+tag+'@@',keep(doi,'## 3.2'))
t2='''**表2 动态任务与多资源调度核心研究的比较条件**

| 代表研究 | 优化对象与资源 | 信息范围与共享内容 | 求解与计划更新 | 验证场景 | 主要贡献与适用条件 |
| --- | --- | --- | --- | --- | --- |
| 分支定价{{10.1016/j.cor.2025.107259}} | 公共/专属任务、电池 | 统一任务与资源模型 | 分解、列生成；给定时域 | 纳卫星星座仿真 | 模型内优化界；取决于定价结构 |
| 分层混合整数规划{{10.1016/j.asr.2025.12.008}} | 分配、排序、动态任务 | 统一请求与冲突信息 | 拉格朗日分配、序列修复 | 最多1000星，50—6000任务 | 分层降低算时；依赖任务结构 |
| 去中心化观测分配{{10.2514/1.I011215}} | 观测请求、简化容量 | 集中/广播/高度去中心化；完成或竞争状态 | 共享规则；从头/增量规划 | 100代理、634目标；单线程模拟 | 信息与更新规则影响冗余 |
| 几何邻域分解{{10.1613/jair.1.16997}} | 观测、存储、下传 | 公共请求/构型；局部能力与邻域消息 | GND分解、NSS协调 | 200/108星、24 h模拟 | 降低算时和消息；保留满足率差距 |
| 观测—传输联合{{10.1109/TMC.2021.3076088}} | 成像与传输窗口 | 统一窗口和任务信息 | 整数规划、松弛/遗传搜索 | 敏捷卫星网络仿真 | 下传机会参与成像选择 |
| 能源约束联合调度{{10.1016/j.actaastro.2025.02.008}} | 观测、传输、充电 | 统一多星资源模型 | 多背包分配、蚁群/局部搜索 | 多敏捷卫星仿真 | 能源补充改变可行集合 |
| 观测—处理联合{{10.1002/sat.70082}} | 质量、计算、能量 | 星上/地面处理资源 | 成像选择、推理任务分配 | 船舶检测与计算平台测试 | 完成事件延伸到信息生成 |
| 通信预测任务包{{10.1016/j.asr.2020.02.018}} | 应急观测、通信 | 同步/异步；预测通信机会 | m-CBBA/m-ACBBA更新 | 分布式观测仿真 | 收益/交互权衡随通信成本变化 |
| 学习辅助大邻域搜索{{10.1016/j.eswa.2025.128502}} | 在线应急任务 | 子问题的任务与资源状态 | 学习初解、滚动破坏—修复 | 大规模动态任务仿真 | 学习与搜索共同形成最终计划 |
| 单星策略复用{{10.2514/1.A35736}} | 观测与下传 | 四种通信；仅共享已完成状态 | 单星训练、多星复用 | Walker星座仿真 | 简化训练；同时段重复仍可能发生 |
| 学习算法比较{{10.3389/frspt.2023.1263489}} | 单星任务、资源屏蔽 | 单星状态；无跨星协调 | PPO/A2C/DQN/MCTS-Train等 | Basilisk单星仿真 | 收益、训练和模拟成本随任务变化 |
| 可补给多轨服务{{10.1016/j.cie.2022.108852}} | 访问、推进剂、补给 | 服务星/客户/设施的时变网络 | 混合整数线性规划 | 多轨服务算例 | 路径和补给统一；依赖转移表达 |
| 加注鲁棒调度{{10.1016/j.cja.2025.103774}} | 访问、服务时长 | 预算不确定集 | 鲁棒模型、混合搜索 | GEO加注仿真 | 保守性与时间不确定性共同评价 |
| 低推力漂移服务{{10.1007/s40295-026-00580-4}} | 路径、质量、加注 | 出发时刻/质量相关代价 | 转移预计算、插值/遗传搜索 | LEO多客户模拟 | 相位成本在主优化之外估计 |

表中LEO与GEO分别指低地球轨道与地球同步轨道。统一模型描述信息可用范围，不直接指明求解器物理部署在地面或星上。通信和学习算法的具体定义见本节相应研究。'''
ch32=ch32.replace('@@TABLE2@@',t2)
ch32=ch32.replace('LEO边缘计算的集中训练','低地球轨道（LEO）边缘计算的集中训练',1)
ch32=ch32.replace('GEO加注鲁棒调度','地球同步轨道（GEO）加注鲁棒调度',1)
ch32=ch32.replace('表中LEO与GEO','蒙特卡洛树搜索训练方法记为MCTS-Train。表中LEO与GEO')

cloud='''任务质量不确定性又改变收益的定义。云层不确定下的主动调度{{O66}}采用机会约束和样本近似，鲁棒调度{{O67}}使用预算不确定集与列生成，星座随机规划{{O68}}则比较多阶段混合整数模型。它们分别控制概率条件、扰动集合内表现或情景下的决策，不具有相同的保守性与信息假设。与运行中收到质量结果后复采相比，这组方法主要在计划生成时表达未确定的观测结果。

'''
ch32=ch32.replace('### 不确定性、在线更新与策略部署\n\n','### 不确定性、在线更新与策略部署\n\n'+cloud)

ch33='''## 3.3 安全执行与异常恢复

执行层把活动计划对应到连续运动、控制输入和软件动作。风险筛查、轨迹安全、异常检出及计划恢复回答不同问题，其输出需要以状态变化和资源占用反馈给调度。

### 接近事件检测与风险信息

最近接近计算与前置筛查可分开改进。Chebyshev代理多项式方法{{10.1016/j.actaastro.2020.01.020}}以分段近似和距离极值求解降低搜索成本，精度受阶数、区间与误差控制影响。风险感知传感器调度{{O12}}又将信息增益和碰撞风险用于跟踪任务选择，说明风险信息本身也受观测资源安排影响。

@@CUDA@@

碰撞规避运行仿真{{10.1007/s12567-022-00471-y}}评价谁在何时采取动作，CAMmary综述{{10.1016/j.actaastro.2025.07.027}}则比较单次机动的设计模型。ESA碰撞规避机器学习竞赛{{O88}}根据接近数据报文预测最终风险，其预测任务并未直接生成和执行安全机动。CCSDS的Conjunction Data Message标准{{ENG:ccsds}}规定跨组织接近信息的交换格式；标准化信息交换仍需后续决策和责任协调。

Starlink公开运行流程{{ENG:starlink}}把星历生成、筛查、星上风险重估与机动更新组织成循环，并按机动能力设置响应条件。这一接口将风险变化转化为新增、修改或取消动作，协调后的机动还会影响原有任务和资源计划。

### 轨迹与控制约束下的安全执行

较早的被动安全轨迹{{O40}}和锥优化交会规划{{O42}}分别讨论安全轨迹条件及自主求解；航天器群的序贯凸规划MPC{{O43}}在执行中更新轨迹，通过邻居通信组织分散计算。它们为将任务安排接入轨迹求解提供不同方法基础，其安全或收敛条件仍限定于相应动力学和约束模型。

@@MPC@@

连续时间逐次凸化研究{{10.2514/6.2026-2446}}在近直线晕轨道交会中处理被动安全，强调安全约束成立的时间范围；转用于低轨任务时，需按相应动力学重新定义条件。

@@SHIELD@@

ADRAS-J的公开案例{{ENG:adras}}将名义接近与异常退出联系起来：2024年11月30日接近失效火箭级至约15 m后，相对姿态异常触发自主中止和安全后撤。该证据对应接近观测和退出，任务评价应分别记录完成的活动、未完成阶段和安全状态。

### 异常识别、故障隔离与计划修复

Hundman等{{10.1145/3219819.3219845}}利用LSTM预测误差和动态阈值检测SMAP/MSL遥测异常；贝叶斯LSTM研究{{O61}}进一步处理数据不平衡及预测不确定性，验证门控持续学习{{O63}}则研究检测模型的运行更新。评价复核{{10.1007/s12567-023-00529-5}}说明指标、后处理与简单基线能够改变比较结论。因此，异常检出、故障原因判定和可执行恢复应采用不同的输出和指标。

@@FDIR@@

@@RESILIENT@@

计划修复还可以根据故障后剩余状态重新组织活动。RPRS{{O127}}针对深空任务的计划失败，将资源诊断、局部修复和重排程结合。它与预定义应急计划处理不同更新方式：前者寻找已有计划的可用修改，后者调用预先准备的响应。是否保持可用任务、需要修改哪些承诺及恢复后能否继续交付，构成执行反馈进入调度的共同问题。

安全执行的结果应同时记录风险缓解、约束满足、任务中断和剩余资源。由此，局部控制或故障处置的成功才能对应到后续活动集合和服务恢复，而不是直接等同于整个星座任务已完成。

---

'''
for tag,doi in [('CUDA','10.3390/aerospace10060543'),('MPC','10.1016/j.conengprac.2011.09.006'),('SHIELD','10.1007/s40295-026-00631-w'),('FDIR','10.1007/s12567-025-00651-6'),('RESILIENT','10.2514/1.I011208')]:
    ch33=ch33.replace('@@'+tag+'@@',keep(doi,'## 3.3'))
ch33=ch33.replace('利用LSTM预测误差','利用长短期记忆网络（LSTM）预测误差',1)
ch33=ch33.replace('CCSDS的Conjunction Data Message标准','空间数据系统咨询委员会（CCSDS）的接近事件数据报文（Conjunction Data Message，CDM）标准',1)

ch34='''## 3.4 跨层耦合与闭环协同

跨层连接需要让状态、决策和完成事件保持对应。自动化运行分类与工具综述{{R05}}、可信自主运行的人工智能综述{{R14}}从运行组织与可信性提供背景；具体研究则通过能力可用、数据交付、状态反馈和责任协调连接部分决策。

长期物流和维护研究{{10.2514/1.A34978}}{{O02}}{{10.2514/1.A36684}}将位置、可用时刻和资源余量传给任务选择。其共同接口是能力何时能够兑现，需求与失效再触发配置或服务活动更新。

@@CONTACT@@

管理拓扑{{10.34133/space.0248}}通过管理域划分、切换预测和局部重组处理责任关系随轨道运动变化。管理关系、通信接触和任务冲突分别规定由谁协调、何时可交换及哪些决策相互影响。跨层使用这些结构时，需要对应各自的输出对象。

@@REASONING@@

Remote Agent{{O59}}较早将模型驱动的规划、执行与模式识别/重配置组织为自主软件架构。EO-1{{10.1109/SMC-IT.2006.48}}和IPEX论文{{10.2514/1.I010386}}继续提供星上科学处理与活动规划的运行经验；JPL的IPEX说明{{ENG:ipex}}明确将图像处理产生的产品与存储、CPU、电源及下传资源接入持续规划。这里的证据是单星功能连接，不能直接推导多星协调或巨型星座运行效果。

参考架构{{10.1016/j.jss.2026.112802}}将监测、分析、规划、执行与共享知识（MAPE-K）对应软件分区，并在NIMBUS相关系统中实例化；Schedule Manager{{10.2514/1.I011208}}落实任务准入与应急计划模块。NASA cFS公开演示包{{ENG:cfs}}提供框架与常用应用连接的入口，同时明确该演示包尚未完整验证为运行系统，任务级验证由具体任务承担。架构或可编译软件支撑实现职责，实际任务证据还取决于配置、硬件和验证过程。

NASA的Starling任务资料{{ENG:starling_nasa}}报告四颗CubeSat共享观测信息并协调后续GPS观测，展示成员状态进入群体选择的飞行连接。Starling 1.5资料{{ENG:starling_story}}{{ENG:starling_nasa}}则描述轨迹提交、风险信息返回、机动责任确认及实际机动；事件本身是模拟接近测试。两类案例分别处理星座内部观测竞争和跨运营方行动责任。

@@RECONFIG@@

验证工具也构成连接条件。Basilisk{{O118}}提供模块化动力学与软件仿真框架；形式化方法经验讨论{{O123}}强调规格、资源及时间约束表达、测试和运行时检查各自的作用。工具能力支持接口和场景验证，证明某一模型性质或完成一次仿真，仍需对应实际连接的任务链、节点和扰动。

以上连接分别改变能力、活动、信息或动作权限。将状态变化传入后续决策并记录其执行反馈，是这些研究的共同分析路径；验证范围则由实际连通的环节、节点规模及事件条件决定。

---

'''
for tag,doi in [('CONTACT','10.1016/j.adhoc.2023.103289'),('REASONING','10.3390/rs15061577'),('RECONFIG','10.1007/s10270-026-01426-1')]:
    ch34=ch34.replace('@@'+tag+'@@',keep(doi,'## 3.4'))
ch34=ch34.replace('NASA cFS公开演示包','NASA的核心飞行系统（core Flight System，cFS）公开演示包',1)

(ROOT/'CHAPTER_03_01_WORKING_v0.7.md').write_text(ch31,encoding='utf-8')
(ROOT/'CHAPTER_03_02_WORKING_v0.7.md').write_text(ch32,encoding='utf-8')
(ROOT/'CHAPTER_03_03_WORKING_v0.7.md').write_text(ch33,encoding='utf-8')
(ROOT/'CHAPTER_03_04_WORKING_v0.7.md').write_text(ch34,encoding='utf-8')
print(json.dumps({k+'_cjk':len(re.findall(r'[\u4e00-\u9fff]',v)) for k,v in [('3.1',ch31),('3.2',ch32),('3.3',ch33),('3.4',ch34)]},ensure_ascii=False))

front=old[:old.index('# 第3章')]
ch4=old[old.index('# 第4章'):old.index('# 第5章')]
ch5=old[old.index('# 第5章'):old.index('# 参考文献与工程资料')]
ch4=re.sub(r'《\[[^\]]+\]\(https://doi\.org/([^\s)]+)\)》',lambda m:'研究{{'+m.group(1)+'}}',ch4)
ch4=ch4.replace('研究研究','研究')
uncertainty='''不确定性比较还需要区分输入的含义。云覆盖的机会约束、预算鲁棒与情景规划{{O66}}{{O67}}{{O68}}，分别采用概率条件、扰动集合或情景信息；服务任务的随机与鲁棒规划{{O30}}处理的是服务与转移相关不确定性；遥测模型的不确定性{{O61}}则首先描述检测输出的可信程度。它们的风险或保守性不能仅因都称为“不确定性处理”而直接比较。接入任务链时，应说明这些信息影响哪些活动、何时可获得，以及由何种反馈纠正。

'''
ch4=ch4.replace('长期维护也存在相似的资源状态差异。',uncertainty+'长期维护也存在相似的资源状态差异。')
ch4=ch4.replace('**表4 工程案例所连接的运行环节与验证范围**','**表4 工程资料和案例所连接的运行环节与验证范围**')
ch4=ch4.replace('| 案例 | 连接的运行环节','| 资料或案例 | 连接的运行环节')
extra_rows='''| [CCSDS CDM标准](https://ccsds.org/publications/bluebooks/entry/3064/) | 跨组织接近信息交换 | 标准规定接近数据报文格式 | 互操作接口；机动选择与责任确认属于后续决策 |
| [NASA cFS演示包](https://github.com/nasa/cFS) | 框架、应用与任务级验证 | README给出演示构成和验证范围 | 演示软件入口；具体任务的完整验证由任务承担 |
'''
ch4=ch4.replace('\n跨案例比较首先得到的是不同反馈对象。','\n'+extra_rows+'\n跨案例比较首先得到的是不同反馈对象。')
ch4=ch4.replace('分别表述 |\n\n| [CCSDS','分别表述 |\n| [CCSDS')
ch4=ch4.replace('软件实现补充了飞行资料未覆盖的模块性质。','软件框架和标准资料又补充实现与互操作条件。CDM规范信息交换，cFS演示包提供组件连接入口；二者均需接入具体任务的决策和验证。软件实现补充了飞行资料未覆盖的模块性质。')

engineer={}
key_urls={
 'iridium':'https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites',
 'planet':'https://docs.planet.com/develop/apis/tasking/',
 'aws':'https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html',
 'starlink':'https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/',
 'adras':'https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris',
 'ipex':'https://ai.jpl.nasa.gov/public/projects/ipex/',
 'starling_nasa':'https://www.nasa.gov/smallspacecraft/what-is-starling/',
 'starling_story':'https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/',
 'cfs':'https://github.com/nasa/cFS',
 'ccsds':'https://ccsds.org/publications/bluebooks/entry/3064/'}
for x in base_manifest['engineering_sources']:
    engineer[x['url']]=dict(x)
engineer[key_urls['cfs']]={'organization':'NASA Goddard Space Flight Center','title':'Core Flight System - Demo Bundle','title_zh':'核心飞行系统演示包','url':key_urls['cfs'],'accessed_on':'2026-10-10','document_type':'official software README','author_verified':False,'current_targeted_check':{'date':'2026-10-10','locator':'README opening paragraphs and distributions','support':'Demo bundle contents; not a fully verified operational system; mission-specific V&V responsibility.'}}
engineer[key_urls['ccsds']]={'organization':'Consultative Committee for Space Data Systems (CCSDS)','title':'Conjunction Data Message','title_zh':'接近事件数据报文','url':key_urls['ccsds'],'accessed_on':'2026-10-10','document_type':'recommended standard','standard_number':'CCSDS 508.0-B-1','published_date':'2013-06','corrigendum':'technical corrigendum 2, October 2021','author_verified':False,'current_targeted_check':{'date':'2026-10-10','locator':'Official Blue Book entry: document number, description and current-version statement','support':'Standard message format for interorganizational conjunction-information exchange; no maneuver optimization or flight-performance claim.'}}

all_sources={s['doi'].lower():dict(s) for s in base_manifest['sources']}
for source in all_sources.values():
    override=source.get('bibliographic_override')
    if override and override.get('local_author_original','').startswith('sources/'):
        override['local_author_original']='../review_full_draft_20261010/'+override['local_author_original']
if (ROOT/'CFS_PRIMARY_SNAPSHOT_v0.7.json').exists():
    cfs_snapshot=json.loads((ROOT/'CFS_PRIMARY_SNAPSHOT_v0.7.json').read_text(encoding='utf-8'))
    engineer[key_urls['cfs']]['current_targeted_check']['github_blob_sha']=cfs_snapshot['sha']
    engineer[key_urls['cfs']]['current_targeted_check']['snapshot_path']='CFS_PRIMARY_SNAPSHOT_v0.7.json'
primary_checks={
 'O35':('author arXiv abstract and registered abstract','https://arxiv.org/abs/2509.09957'),
 'O36':('author arXiv abstract','https://arxiv.org/abs/2605.20875'),
 'O57':('author arXiv abstract, formal journal DOI linked','https://arxiv.org/abs/1910.00672'),
 'O58':('publisher abstract and section 2.4 deployment-feasibility definition','https://link.springer.com/article/10.1007/s42405-026-01298-1'),
 'O02':('author arXiv abstract, formal journal DOI linked','https://arxiv.org/abs/2103.08963'),
 'O09':('publisher abstract and section 2 assumption A.1','https://link.springer.com/article/10.1007/s40295-025-00487-6'),
 'O91':('publisher abstract and introduction','https://link.springer.com/article/10.1007/s10951-024-00816-x'),
 'O115':('official conference abstract','https://www.ijcai.org/proceedings/2023/30'),
 'O76':('publisher abstract and registered abstract','https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2552'),
 'O125':('publisher abstract and registered abstract','https://link.springer.com/article/10.1007/s10586-025-05663-9'),
 'O88':('publisher abstract and registered abstract','https://link.springer.com/article/10.1007/s42064-021-0101-5'),
 'O43':('author institutional abstract','https://authors.library.caltech.edu/records/mvhns-j8a04'),
 'O128':('author institutional abstract','https://www.microsoft.com/en-us/research/publication/kodan-addressing-the-computational-bottleneck-in-space/'),
 'O59':('author original: architecture, sections 1.4 and 2','https://people.csail.mit.edu/williams/Web%20site/papers/aij98.pdf'),
 'O123':('author original: abstract and verification-practice scope','https://ai.jpl.nasa.gov/public/documents/papers/chien-nfm-2022.pdf'),
 'O65':('original publisher PDF at university course repository; abstract and problem overview','https://www2.cs.sfu.ca/CourseCentral/827/havens/papers/topic%2312%28SatelliteScheduling%29/lemaitre-2002.pdf'),
 'O74':('author original PDF; abstract and communication-scheduling problem overview','https://www.cs.colostate.edu/~howe/papers/JOS04.pdf')}
primary_checks['O93']=('author institutional abstract, final published version identified','https://dspace.mit.edu/entities/publication/b0bf0a05-be3b-433b-9f4b-ce314ed5178b')
for row in selected:
    r=next(x for x in meta if x['id']==row['ID']); m=r['metadata']
    authors=[' '.join(filter(None,[a.get('given',''),a.get('family','')])).strip() or a.get('name','') for a in m.get('author',[])]
    dp=m.get('published',{}).get('date-parts',[[None]])[0]
    pub={'authors':authors,'journal':(m.get('container-title') or [''])[0],'year':dp[0],'volume':m.get('volume'),'issue':m.get('issue'),'page':m.get('page'),'article_number':m.get('article-number'),'type':m['type'],'published_online':m.get('published-online',{}).get('date-parts'),'published_print':m.get('published-print',{}).get('date-parts')}
    if m['type']=='book-chapter' and len(m.get('container-title',[]))>1:
        pub['journal']=m['container-title'][-1]
        pub['series']=m['container-title'][0]
    check=primary_checks.get(row['ID'])
    urls=[x.strip() for x in row['一手来源'].splitlines() if x.strip()]
    if check and check[1] not in urls: urls.insert(0,check[1])
    all_sources[row['DOI'].lower()]={'doi':row['DOI'],'title':html.unescape(m['title'][0]),'title_zh':row['中文译名或原文题名'],'publication':pub,'registry_url':r['registry_url'],'registry_identity_checked':True,'original_source_urls':urls,'library_id':row['ID'],'inherited_content_status':row['阅读与核查状态'],'inherited_content_basis':row['内容提取依据'],'inherited_method_summary':row['模型与方法'],'current_targeted_check':{'date':'2026-10-10','locator':check[0],'url':check[1]} if check else ({'date':'2026-10-10','locator':'Publisher-deposited registered abstract','url':r['registry_url']} if r.get('registered_abstract') else None),'registered_abstract_available':bool(r.get('registered_abstract')),'author_verified':False}

body=front+'# 第3章 多层次管理、调度与执行方法\n\n'+ch31+ch32+ch33+ch34+ch4+ch5
# Resolve internal placeholders to temporary DOI links. All numbering is assigned
# from actual first appearance after the complete five-chapter body is assembled.
def temporary(m):
    key=m.group(1)
    if key.startswith('ENG:'):
        u=key_urls[key[4:]]
        return '[SOURCE]('+u+')'
    doi=byid[key]['DOI'] if key in byid else key
    if doi.lower() not in all_sources: raise ValueError('Unknown source: '+key)
    return '[SOURCE](https://doi.org/'+urllib.parse.quote(doi,safe='/.:_-')+')'
body=re.sub(r'\{\{([^{}]+)\}\}',temporary,body)
ordered=[]
for d in re.findall(r'https://doi\.org/([^\s)]+)',body):
    d=urllib.parse.unquote(d).lower()
    if d not in ordered: ordered.append(d)
assert set(ordered)==set(all_sources),(set(all_sources)-set(ordered),set(ordered)-set(all_sources))
nums={d:i+1 for i,d in enumerate(ordered)}
ordered_eng=[]
for u in re.findall(r'\]\((https?://[^\s)]+)\)',body):
    if u in engineer and u not in ordered_eng: ordered_eng.append(u)
assert set(ordered_eng)==set(engineer)
eng_nums={u:len(ordered)+i+1 for i,u in enumerate(ordered_eng)}
body=re.sub(r'\[SOURCE\]\(https://doi\.org/([^\s)]+)\)',lambda m:'['+str(nums[urllib.parse.unquote(m.group(1)).lower()])+'](https://doi.org/'+m.group(1)+')',body)
body=re.sub(r'\[SOURCE\]\((https?://[^\s)]+)\)',lambda m:'['+str(eng_nums[m.group(1)])+']('+m.group(1)+')',body)
body=re.sub(r'(\[\d+\]\([^\s)]+\))(?=\[\d+\]\()',r'\1、',body)

type_counts=collections.Counter(all_sources[d]['publication']['type'] for d in ordered)
counts={'academic':len(ordered),'journal_articles':type_counts['journal-article'],'conference_papers':type_counts['proceedings-article'],'book_chapters':type_counts['book-chapter'],'engineering_documents':len(ordered_eng),'total_sources':len(ordered)+len(ordered_eng)}
bib=f"# 参考文献与工程资料\n\n正文实际引用按唯一DOI和资料网址去重，共**{counts['total_sources']}项来源**：**{counts['academic']}篇学术文献**（{counts['journal_articles']}篇期刊论文、{counts['conference_papers']}篇会议论文、{counts['book_chapters']}篇学术会议文集章节）和**{counts['engineering_documents']}份工程资料**。英文原标题附中文工作译名；作者稿与正式版合并计数。\n\n## 学术文献\n\n"
for d in ordered:
    x=all_sources[d]; p=x['publication']; n=nums[d]
    x['reference_number']=n; x['evidence_id']=f'E{n:03d}'
    auth='; '.join(p['authors'][:3])+(', et al.' if len(p['authors'])>3 else '')
    author_text=auth if auth.endswith('.') else auth+'.'
    venue=p['journal']
    if p.get('series'): venue+=' ('+p['series']+')'
    publication=venue+', '+str(p['year'])
    if p.get('volume'): publication+=', '+str(p['volume'])
    if p.get('issue'): publication+='('+str(p['issue'])+')'
    location=p.get('page') or p.get('article_number')
    if location: publication+=': '+str(location)
    online_note=''
    printdate=p.get('published_print')
    if printdate and len(printdate[0])>1 and tuple(printdate[0][:2])>(2026,10):
        online_note='（登记编排期为'+str(printdate[0][0])+'年'+str(printdate[0][1])+'月）'
    doi_link=urllib.parse.quote(x['doi'],safe='/.:_-')
    bib+=f"{n}. {author_text} {x['title']}〔{x['title_zh']}〕. *{publication}*{online_note}. DOI: [{x['doi']}](https://doi.org/{doi_link}).\n\n"
bib+='## 工程资料\n\n'
for u in ordered_eng:
    x=engineer[u];n=eng_nums[u];x['reference_number']=n;x['evidence_id']=f'E{n:03d}'
    organization=x.get('organization') or x.get('publisher') or x.get('author') or 'Official source'
    title=x['title'];zh=x.get('title_zh') or x.get('chinese_title') or ''
    extra=''
    if x.get('standard_number'): extra=x['standard_number']+'，2013年6月，含2021年10月技术勘误2。'
    bib+=f"{n}. {organization}. {title}"+(f'〔{zh}〕' if zh else '')+f". {extra}[官方资料]({u}). 访问日期：2026-10-10。\n\n"
full=body+bib
(ROOT/'REVIEW_FULL_v0.7.md').write_text(full,encoding='utf-8')
(ROOT/'REFERENCES_v0.7.md').write_text(bib,encoding='utf-8')
manifest={'document_id':'satellite-constellation-review-v0.7','created_on':'2026-10-10','manuscript_type':'problem-driven narrative technical review','processing_boundary':'local unpublished draft; only public bibliographic/source metadata searched externally','submission_ready':False,'author_final_verification':'pending','baseline':{'path':str(BASE/'REVIEW_FULL_v0.6.md'),'sha256':hashlib.sha256((BASE/'REVIEW_FULL_v0.6.md').read_bytes()).hexdigest()},'counts':counts,'sources':[all_sources[d] for d in ordered],'engineering_sources':[engineer[u] for u in ordered_eng],'source_pool':{'repository':'yyh46-design/satellite-constellation-review-writing','commit':'06e7df85ffac5798dbd885f31df6fad2af3ce1c3','candidate_count':148,'selected_additions':48,'excluded_from_current_selection':sorted(excluded)},'new_claims':[],'evidence_limits':['Metadata identity checks do not verify technical propositions.','New grouped technical descriptions are bounded by prior recorded primary-source abstract/excerpt evidence and current targeted checks.','Sources not newly read retain their inherited evidence status; no claim that all 98 papers were fully read or author-verified.','Core quantitative statements retain v0.6 verification limits.'],'output':{'path':str(ROOT/'REVIEW_FULL_v0.7.md'),'sha256':hashlib.sha256((ROOT/'REVIEW_FULL_v0.7.md').read_bytes()).hexdigest()}}
for i,p in enumerate(body.split('\n\n')):
    ds=list(dict.fromkeys(urllib.parse.unquote(d).lower() for d in re.findall(r'https://doi\.org/([^\s)]+)',p)))
    eng=list(dict.fromkeys(u for u in re.findall(r'\]\((https?://[^\s)]+)\)',p) if u in engineer))
    if ds or eng:
        manifest['new_claims'].append({'claim_id':f'P{i:03d}','paragraph_sha256':hashlib.sha256(p.encode('utf-8')).hexdigest(),'source_dois':ds,'engineering_urls':eng,'author_verified':False,'record_type':'paragraph-source binding; not a semantic support certification'})
(ROOT/'SOURCE_AND_CLAIM_RECORD_v0.7.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'counts':counts,'body_chars':len(body),'body_cjk':len(re.findall(r'[\u4e00-\u9fff]',body)),'chapter3_cjk':len(re.findall(r'[\u4e00-\u9fff]',ch31+ch32+ch33+ch34)),'manuscript_sha256':manifest['output']['sha256']},ensure_ascii=False))
