# 大型卫星星座智能管理与调度研究综述

Intelligent Management and Scheduling of Large Satellite Constellations: Service Completion, Resource Coupling, and Operational Feedback

**v2.2-CN · 2026-10-17 · 作者审阅稿；科学内容、版本及投稿声明仍待作者终核**

## 摘要

大型卫星星座的持续运行需要协调能力配置、业务需求与执行反馈。现有研究分别优化覆盖、任务收益、网络性能或安全处置，其决策范围与完成条件不同，限制了方法之间的直接比较。本文采用问题导向的叙述性综述，以对地观测和通信为核心业务，梳理长期能力维持、任务规划、网络资源管理以及安全与恢复的技术路线，并从业务完成条件、资源耦合和信息权限三个方面开展综合分析。代表研究表明，成像收益、下传数据量和按期完成请求对应不同结果；库存供应、资产到位与业务恢复也具有不同时间含义。能量约束、学习辅助搜索、接入协议和路由更新的比较进一步说明，方法的适用性取决于可修改的决定、可及时获得的状态以及配置生效时间。联合选择、顺序安排与反馈可以在不同层次组合，其代价应覆盖预处理、训练、求解、协调和执行。公开接口、软件原型、独立测量与飞行案例为上述分析提供互补依据。本文据此归纳不同管理方式的适用条件，并提出面向共同业务结果、延迟信息和可修改资源的研究问题。 <!-- [claim:CN22C001] [evidence:] -->

**关键词：** 大型卫星星座；任务调度；通信资源管理；在轨服务；运行反馈；自主运行

## Abstract

Sustained operation of large satellite constellations requires coordination of available capabilities, service demand, and execution feedback. Existing studies optimize coverage, task rewards, network performance, or safety under different decision scopes and completion criteria, which limits direct comparison. This problem-driven narrative review examines Earth observation and communications together with capability maintenance, mission planning, network resource management, and recovery. It compares representative studies through service-completion criteria, resource coupling, and information and decision authority. Imaging rewards, downloaded data volume, and requests completed by their deadlines represent different outcomes; inventory supply, asset arrival, and service recovery likewise denote different events. Comparisons of energy constraints, learning-assisted search, handover protocols, and routing updates show that applicability depends on revisable decisions, timely state information, and configuration activation. Joint selection, sequential allocation, and feedback can be combined at different levels, with costs spanning preprocessing, training, optimization, coordination, and execution. Public interfaces, software prototypes, independent measurements, and flight cases provide complementary evidence. The synthesis identifies conditions for choosing and evaluating management methods and outlines research questions involving common service outcomes, delayed information, and revisable resources. <!-- [claim:CN22C002] [evidence:] -->

**Keywords:** large satellite constellations; mission scheduling; communication resource management; on-orbit servicing; operational feedback; autonomous operations

## 1 引言

### 1.1 从任务分配到持续运行

大型星座把重复出现的活动机会、持续到达的需求和多个决策主体置于同一运行过程中。增加卫星可以扩展候选观测窗口和接入机会，也会增加资源竞争、状态交换与计划更新的负担。自动化运行研究已将资源排程、监测、配置及轨道管理列为相互关联的扩展问题[1]。因此，评价管理与调度方法需要追踪一项安排如何利用可用能力、形成业务结果，并在状态改变后继续执行。 <!-- [claim:CN22C003] [evidence:E001] -->

对地观测与通信呈现了不同的服务过程。观测请求通常经过成像、处理和传输，以满足质量与时限的信息产品作为完成结果；通信业务围绕持续流量配置关联、波束、功率、频谱及路径。两者共享时间、能源、存储和地面设施，但完成一次成像、增加下传数据量与维持连接质量分别回答不同问题。空间物流研究进一步将部署、补给与重构纳入能力维持[2]。这些长期决定会改变后续可用的成员、位置与资源，安全干预和异常恢复则在运行中再次修改这些条件。 <!-- [claim:CN22C004] [evidence:E002] -->

### 1.2 已有综述与本文的分析重点

已有综述为各问题域提供了不同的组织方式。敏捷观测综述[3]比较任务模型、约束与求解方法，卫星调度综述[4]将成像、通信和集成调度置于观测任务背景中；其分类能够揭示活动安排的结构，跨论文结果仍需保留目标函数及模型差异。多智能体综述[5]以主体、协调架构和任务管理组织分布式空间系统；自动化运行研究[1][6]则关注运行职责、地面与星上功能及工具。通信专题综述[7][8]进一步涉及网络组织、控制及资源管理，而SatOps—NetOps研究[9]直接讨论平台运行和网络需求的连接。表1据此概括本文与既有研究的衔接，不将这些视角的差别解释为其他综述未覆盖某一领域的证明。 <!-- [claim:CN22C005] [evidence:E003,E004,E005,E001,E006,E007,E008,E009] -->

**表1 既有综述的组织对象与本文的比较问题**

| 代表文献 | 主要组织对象 | 本文衔接的比较问题 | <!-- [claim:CN22C006] [evidence:] -->
| --- | --- | --- |
| 观测与卫星调度[3][4] | 任务、资源约束与求解方法 | 采集、处理、下传与请求交付分别如何完成 | <!-- [claim:CN22C007] [evidence:E003,E004] -->
| 分布式空间系统[5] | 智能体、协调方式与任务管理 | 共享何种信息、何时共享、谁有权修改活动 | <!-- [claim:CN22C008] [evidence:E005] -->
| 自动化运行[1][6] | 运行职责、自动化模式及工具 | 计划输出如何经过执行检查而改变运行状态 | <!-- [claim:CN22C009] [evidence:E001,E006] -->
| 通信管理[7][8] | 网络组织、控制和资源配置 | 持续用户流量与观测数据下传的目标有何差别 | <!-- [claim:CN22C010] [evidence:E007,E008] -->
| SatOps—NetOps[9] | 平台运行与网络管理的交互 | 共同选择、顺序传递和反馈分别保留哪些权限 | <!-- [claim:CN22C011] [evidence:E009] -->

本文围绕大型星座持续服务，对相关研究开展三个方面的综合分析。首先，区分采集、处理、下传、按期交付以及能力恢复等完成事件，明确目标函数和评价量所对应的业务结果。其次，比较联合选择、顺序配置与执行反馈保留的可改变量，分析下游约束和资源承诺如何影响当前安排。最后，结合信息获得时刻、计算与协调成本以及配置生效过程，归纳不同连接方式的适用条件。表2建立结果比较基础，图2区分决策连接关系，表6总结其适用条件；第3章展开代表研究，第4章形成综合认识和后续研究问题。本文保留各研究的任务域与验证条件，不对异构算例构造统一性能排名。 <!-- [claim:CN22C012] [evidence:] -->

### 1.3 范围、选录方式与证据使用

本文是一篇问题导向的叙述性综述。文献来自既有主题文献库、代表研究的参考链追溯和专题补充，按管理职责及其对业务结果的作用选录。对地观测和通信是核心业务；构型、补给、在轨服务、安全与恢复按其支撑作用纳入。单星、地球同步轨道、深空及通用多智能体研究用于解释相关方法，论述中保留原任务域。“大型”表示成员、候选活动或协调规模已对求解和运行组织产生实质影响，不设置统一卫星数量阈值。“智能管理”涵盖基于状态与目标的优化、规则推理、协调和学习。 <!-- [claim:CN22C013] [evidence:] -->

本文按决策对象、可选变量、资源约束、可获得信息、更新权限、完成事件、评价量和验证环境提取比较内容。纳入方法分析的学术来源须具有可获取且已定向核读的正文，原始研究承担相应的方法和结果论述，既有综述用于界定研究范围与分类视角。出版社PDF、完整HTML、机构接受稿及作者预印本均按实际版本使用；涉及模型假设、结果条件和版本差别的限制保留在相应论述中。官方工程资料用于说明接口、软件性质或具体运行事件。本文分别表述原研究结果与跨研究归纳，不据此作穷尽性的文献频率估计或跨论文性能元分析。 <!-- [claim:CN22C014] [evidence:] -->

## 2 管理对象与比较基础

### 2.1 业务过程与可用能力

观测与通信共享平台资源，却具有不同的业务完成过程。观测管理需要把目标请求转化为可执行的采集、处理和交付活动；通信管理需要使有限资源持续响应空间分布和时间变化的流量。构型及维护决定能力在何处、何时可用，安全与恢复根据执行事件改变成员和任务状态。图1以业务过程为横向主线，以能力、资源与反馈为共同管理职责，避免将某个求解器等同于完整运行体系。 <!-- [claim:CN22C015] [evidence:] -->

![图1 业务过程与共同管理职责](assets/fig1_cn.svg)

图1 业务过程与共同管理职责。箭头表示任务、资源或状态的传递，为本文归纳；具体研究可以只优化其中一部分，不表示图中全部功能已在同一系统验证。 <!-- [claim:CN22C016] [evidence:] -->

### 2.2 决策时域、权限与资源承诺

长期配置选择资产、位置和未来能力，业务调度据此选择活动，执行与恢复再更新状态。时间尺度之外，还需要说明哪些决定可以修改。本文将已经确认的安排对后续选择的限制称为资源承诺，并区分其来源：预约服务的配置及变更规则[10]、接触图算法对已分配容量的保留[11]，以及激光链路建立的物理时间[12]分别约束不同环节。比较重规划时，应说明承诺由谁作出、是否允许撤回及修改何时生效。 <!-- [claim:CN22C017] [evidence:E052,E106,E121] -->

集中、分层和分布式描述信息汇集与决策权限；主问题—子问题分解描述求解组织；集中训练与分散执行描述学习阶段。一个方法可以同时具有这些特征。管理拓扑研究[13]关注成员组织及中心切换，观测分配研究[14][15]关注任务竞争和冲突信息。两者的消息范围、决策权限及计时对象需要分别报告。 <!-- [claim:CN22C018] [evidence:E010,E034,E035] -->

### 2.3 完成事件、评价量与比较分母

约束限定可行活动，目标函数决定模型奖励的结果。在观测链中，成像、质量满足、处理完成、数据下传和请求按期交付可以发生在不同时刻。联合观测—传输模型[16][17]即采用不同的奖励构造：按成功安排请求计权，与并列奖励观测和下传体积具有不同含义。通信吞吐、排队时延、公平性和中断也依赖各自的统计对象。表2将这些结果与决策变量并列，作为后文比较的基础。 <!-- [claim:CN22C019] [evidence:E042,E044] -->

**表2 管理对象、可选变量与结果定义**

| 管理对象 | 典型可选变量 | 需要明确的完成事件或分母 | <!-- [claim:CN22C020] [evidence:] -->
| --- | --- | --- |
| 观测请求 | 目标、成员、窗口及活动顺序 | 采集、质量满足、按期交付；重复观测的价值 | <!-- [claim:CN22C021] [evidence:] -->
| 处理与传输 | 处理节点、负载、频率及路径 | 处理结束、下传字节或完整产品；成功请求子集 | <!-- [claim:CN22C022] [evidence:] -->
| 通信业务 | 关联、波束、功率、频谱及路由 | 流量满足、排队/端到端时延、越限或实际中断 | <!-- [claim:CN22C023] [evidence:] -->
| 能力维持 | 备星、补给、设施及维修行动 | 库存供应、资产到位、任务能力恢复、业务重分配 | <!-- [claim:CN22C024] [evidence:] -->
| 安全与恢复 | 跟踪、机动、诊断及计划修复 | 风险信息、约束满足、安全退出及原任务恢复 | <!-- [claim:CN22C025] [evidence:] -->

评价量还应与试验总体一致。成功请求的平均时延不能替代全部请求的按期完成率，限时内找到可行解与证明最优也属于不同状态。本文据此同时考察结果、未完成情况及获取结果所需的成本。模型仿真、软件测试、硬件原型、运行接口、外部测量和飞行事件分别支持其实际观察对象。 <!-- [claim:CN22C026] [evidence:] -->

## 3 主要技术路线及代表研究比较

### 3.1 长期能力配置与持续维护

#### 3.1.1 构型选择与能力到位

构型设计的决策范围取决于目标状态是否预先给定。终端条件下的重构机动[18]、区域构型与卫星指派的共同选择[19]，以及已知阶段需求间的重构[20]，依次增加了终端位置或阶段之间的可选量。访问模式优化[21]利用覆盖的组合结构，不确定关注区域下的部署[22]则评价未来需求情景，并以增发成员补充能力。阶段数量增加说明规划范围扩大，其在线适应性仍取决于信息何时揭示和已部署成员是否允许改变。 <!-- [claim:CN22C027] [evidence:E011,E012,E013,E014,E015] -->

能力到位还受部署过程约束。Gwon和Ahn[23]将停泊、J₂引起的升交点赤经漂移、发射容量和完成窗口纳入设计；其筛选得到潜在可达对象，最终选集仍需满足覆盖要求。通信平台与星座联合设计[24]进一步把天线、波束及平台参数与地域需求相联系。两类研究分别说明形成能力需要的时间和单位资产能提供的容量。细化覆盖或波束能够增加选择，也会带来平台复杂度及运行配置负担，因而构型比较应报告目标能力、到位时刻与实现条件。 <!-- [claim:CN22C028] [evidence:E016,E017] -->

#### 3.1.2 补给状态与业务恢复

多级库存模型[25]将地面、停泊轨道和轨道面内备星连接起来，计入停泊层向轨道面补给的漂移与转移等待，同时将轨道面内备星接替视为即时可用。双通道研究[26]在间接补给之外加入直接注入，并保留面内即时替换等前提。马尔可夫链模型[27][28]进一步描述库存、接触机会及在途补给阶段。离散时间步、实际交付机会和资产到位时刻分别控制模型精度、供给条件和运行结果，不能用平均库存量替代全部时间信息。 <!-- [claim:CN22C029] [evidence:E018,E019,E020,E021] -->

集成在轨服务的维护研究[29]同时考虑运营方年维护成本与服务方利润，并用库存订货满足率约束供给水平。已核作者稿的案例允许较长维修周转与较高订货满足率并存，原因在于备件缓冲；这也说明维修历时与用户业务中断需要不同的状态描述。其经济前沿还受定价、可修复故障比例及修后如新等假设影响，不直接代表实际市场均衡。 <!-- [claim:CN22C030] [evidence:E023] -->

Iridium公开的备星部署[30]提供了备用能力投入的工程例子。将这些资料与库存模型连接时，可区分四个事件：替代资源可得、资源到位、任务能力恢复，以及受影响业务重新分配。已有模型细化了其中不同阶段。进一步评价通信中断或未满足观测请求，需要把这些事件与共同的故障和需求序列关联；这是本文提出的比较接口。 <!-- [claim:CN22C031] [evidence:E022] -->

#### 3.1.3 设施布局、访问与滚动维护

服务设施通过位置和客户分配限定维护可达范围。轨道仓库研究[31]先在离散候选中选择设施与指派，再在固定部分决定后连续细化；位置—线路模型[32]则交替更新连续位置与多客户线路。两者的差别在于哪些变量共同变化。服务船预部署[33]为给定服务对象配置初始能力，滚动物流[34]允许需求逐步揭示，高低推力服务框架[35]进一步把转移代价和质量变化纳入访问安排。这些研究连接了设施、需求与行动，但其输出分别对应部署方案、服务计划和可达转移，尚需通过一致的任务结果解释其关系。 <!-- [claim:CN22C032] [evidence:E024,E025,E026,E027,E028] -->

这些模型连接日常调度的输出是带有时间、位置和剩余资源的能力。[34]在滚动时域内只执行计划前缀，并在需求揭示后更新后续安排；[35]则使推进条件和质量影响转移的可用范围。共同的比较问题是：当前计划依据哪些已知需求，下一轮仍可修改哪些资产和活动，以及求解预算内返回的安排何时能够执行。固定客户顺序下的位置细化、后验多客户组合与全时域联合路由应分别解释。 <!-- [claim:CN22C033] [evidence:E027,E028] -->

### 3.2 对地观测与在轨服务调度

#### 3.2.1 活动选择与跨星协调

观测调度把请求选择转化为满足姿态和可见窗口的活动序列。经典研究[36]比较了特定窗口约束问题中的贪心、动态规划、约束规划和局部搜索；能量感知研究[37]进一步将轨道光照、电池状态和任务共享纳入混合整数线性模型，区分单星专属任务、星座共享任务与同时执行的冗余任务。个体收益、星座收益与冗余因此形成资源竞争，而非单纯增加成员即可同时改善的目标。该研究以通用整数规划求解器验证1—5星场景，适合解释资源模型如何改变可行活动；其规模结论仍限于所设实例。 <!-- [claim:CN22C034] [evidence:E030,E122] -->

分布式实例展示了信息与计算的具体取舍。Parjan和Chien[14]比较集中、广播及高度去中心化分配，增量规划减少重复计算，也保留了更多重复观测。Zilberstein等[15]利用几何邻域和分布式约束优化压缩协调范围，同时评价任务满足、计算及消息量。前者复用旧计划，后者利用竞争的局部结构；两者都应将节省的成本与任务结果并列，且应区分并行时间估算和实际测量。 <!-- [claim:CN22C035] [evidence:E034,E035] -->

协调方法的保证取决于信息与评分条件。多主体观测模型[38]区分请求所属主体和协调角色；一致性任务包算法（CBBA）[39]交换赢家、报价和时间戳，并在规定的评分及通信条件下消解冲突。其贪心等价和价值界具有各自前提。延迟通信协同规划[40]把消息到达条件引入联合任务安排，异步市场方法[41]则在各主体独立更新时维持任务竞争关系。迁移这些方法时，应核对任务互补价值、状态传播条件和最终执行权限，分别评价减少通信与改变任务分配带来的结果。 <!-- [claim:CN22C036] [evidence:E036,E037,E039,E041] -->

#### 3.2.2 观测、处理与交付的连接

联合安排观测与传输可以使下游机会影响目标选择，但具体收益由完成定义决定。He等[16]的作者公开稿以期限内完成观测和传输的请求加权值为目标，将窗口关联与窗内配置分层求解；其模型采用无误码传输，并忽略成像角度对图像质量的影响。因此，该结果主要说明所设窗口与资源条件下的请求安排。 <!-- [claim:CN22C037] [evidence:E042] -->

Rocha等[17]的机构工作论文同时奖励观测收益与向地面下传的数据量，并考虑姿态、存储和能源。两个奖励项需要分别解释，下载更多数据不必对应更多完整请求。其图缩减依赖重叠任务分组及必要切换约束的覆盖，简化整数模型还可能舍弃可行解。与按期成功请求计奖的模型[16]相比，目标定义和保留的活动组合均发生变化。图表示、模型简化和邻域求解因而是不同的计算处理，应分别分析对可行序列和搜索成本的作用。 <!-- [claim:CN22C038] [evidence:E044,E042] -->

地面设施使链路机会进一步受到共享容量约束。卫星控制网络[42]、下传排程[43]及深空网络（DSN）优化[44]采用不同的实例结构、人工输入和求解预算；深空网络运营[45]还包含请求解释、候选安排、协商与确认。所引Planet和AWS公开文档[46][10]分别定义质量/交付状态与预约配置。它们使模型中的完成事件和承诺变更具有具体的操作参照，算法性能仍应由相应实验评价。 <!-- [claim:CN22C039] [evidence:E047,E048,E049,E050,E051,E052] -->

Soret等[47]的作者稿采用另一种连接方式：先确定采集负载及下传安排，再联合配置星地处理负载和频率。其采集阶段省略存储约束，处理阶段约束平均时延；固定流水线及稳定星间链路支持分阶段求解。质量失败还可触发下一轮重采。因此，本次处理优化保持上游计划，与跨轮次质量反馈可以同时存在；平均处理时延也应与逐帧截止期区分。 <!-- [claim:CN22C040] [evidence:E053] -->

处理配置还可以通过返回机会或信息价值连接业务。轨道感知调度[48]把离开地面可见域作为返回结果的边界，成功计数可包含超过业务截止期、但离域前完成的请求；其成功比例和平均响应时间应保留各自分母。Kodan[49]通过专用模型、图块和处理跳过，将处理配置连接到下传中高价值比特的比例，提供了另一种价值映射。前者直接评价请求的返回，后者关注有限下传容量中保留的信息价值。地面硬件测量与轨道链路仿真仍对应特定任务，价值密度与完整产品交付需要分别评价。 <!-- [claim:CN22C041] [evidence:E057,E058] -->

#### 3.2.3 动态请求与学习作用的位置

动态调度首先需要明确何时触发重规划，以及哪些活动仍可修改。滚动时域研究[50]结合周期与事件触发，将等待和新到任务纳入当前任务集，再以启发式分配卫星与时间窗；其4—6星实验用于解释重新安排等待任务的作用。与任务到达不同，不确定性模型还决定新信息揭示后能否改排。鲁棒模型[51]以预算参数控制收益扰动的保守范围，多阶段随机模型[52]则区分评价既定计划的两阶段形式与允许天气信息揭示后修改未来活动的三阶段形式。重新规划、保守预留和信息揭示后的调整由此具有不同的可改变量。 <!-- [claim:CN22C042] [evidence:E127,E061,E062] -->

学习方法还应按其在完整流程中的位置比较。Song等[53]用Q-learning依据适应度改善选择遗传算子，再由时间窗选择器筛选窗口并调整执行时间。学习控制搜索方向，解的可行性仍依赖解码过程。其两星、100—1400任务实验不代表同等数量卫星的协同验证。单星策略复用[54]则将训练策略用于多个成员，配合动作屏蔽、任务分配及完成状态共享；共享完成状态有助于减少重复，却未直接提供同一决策时段的未来意图。Basilisk中的算法比较[55]进一步把策略、训练与安全动作处理置于共同仿真流程。搜索效率、动作可行性和跨星协调需要分别说明实现环节与成本。 <!-- [claim:CN22C043] [evidence:E123,E065,E066] -->

#### 3.2.4 在轨服务的转移与补给

在轨服务改变了候选活动的形成方式。观测常利用预先给定的目标可见窗口，服务访问则需由推进、质量和时间条件生成可达转移[56][57]。改变访问顺序会改变后续转移的起点、资源和可用时刻，因而不能仅把空间距离作为统一任务边权。高低推力服务与滚动物流研究[34][35]还表明，轨迹模型与需求更新应通过明确的起止状态交接，再由上层安排访问与补给。 <!-- [claim:CN22C044] [evidence:E071,E072,E027,E028] -->

低推力预计算研究[57]在轨道、质量及时刻等维度生成代价，再利用插值支持序列搜索；漂移服务研究[56]则联合推力—漂移—推力转移、访问与加注。两者都需保留相位处理的边界。[57]的飞行时间由控制权重及终止准则等共同产生，代价表不自动支持任意指定到达时刻。评价此类方法时，应同时说明预计算成本、插值参照、直接动力学复核及未纳入的终端条件。 <!-- [claim:CN22C045] [evidence:E072,E071] -->

**表3 观测与服务调度的决定、目标和方法条件**

| 代表研究 | 可修改决定及主要方法 | 业务结果或目标 | 主要适用条件 | <!-- [claim:CN22C046] [evidence:] -->
| --- | --- | --- | --- |
| 分布式观测[14][15] | 复用计划或按几何邻域压缩协调范围 | 任务满足、重复观测及计算/消息成本 | 竞争结构与计时口径须对应 | <!-- [claim:CN22C047] [evidence:E034,E035] -->
| 拍卖与异步协调[39][40][41] | 竞价、延迟消息处理及冲突消解 | 原模型的任务价值及分配结果 | 评分、消息条件与执行权限分别保留 | <!-- [claim:CN22C048] [evidence:E037,E039,E041] -->
| 联合观测—传输[16] | 分层处理窗口关联与窗内时刻 | 期限内成功请求的加权收益 | 无误码传输；图像质量简化 | <!-- [claim:CN22C049] [evidence:E042] -->
| 观测—下传一体安排[17] | 图缩减、模型简化与邻域求解 | 观测收益与下传体积分别计奖 | 分组及切换条件；简化可改变可行域 | <!-- [claim:CN22C050] [evidence:E044] -->
| 顺序处理配置[47] | 固定本轮采集，再配置负载与频率 | 处理配置及平均时延约束 | 固定流水线；跨轮次质量重采 | <!-- [claim:CN22C051] [evidence:E053] -->
| 计算与信息价值[48][49] | 利用返回机会或选择处理配置 | 成功返回、响应时间或价值密度 | 统计分母、帧期限、误判及硬件条件不同 | <!-- [claim:CN22C052] [evidence:E057,E058] -->
| 策略复用[54][55] | 策略、动作检查及分配/状态共享 | 原仿真中的观测调度结果 | 训练、推理和跨星协调分别评价 | <!-- [claim:CN22C053] [evidence:E065,E066] -->
| 低推力服务[56][57] | 转移代价生成、访问及补给 | 原模型的转移与服务结果 | 质量、时间、相位及预计算/复核成本 | <!-- [claim:CN22C054] [evidence:E071,E072] -->
| 能量约束与学习辅助搜索[37][53] | 电池/光照下选任务；学习选择遗传算子 | QoS权衡或电磁探测收益 | 1—5星与两星任务扩展分别验证；学习和可行解码分开 | <!-- [claim:CN22C127] [evidence:E122,E123] -->

表中[16][47]按作者稿、[17]按机构工作论文中的方法记录比较；其正式版本对照继续保存在配套清单中。不同完成事件、奖励及计算条件不直接构成跨论文性能排名。 <!-- [claim:CN22C055] [evidence:E042,E053,E044] -->

### 3.3 通信网络管理与资源调度

#### 3.3.1 需求估计、波束与功率

流量预测为配置提供输入，配置再将资源转化为服务。预测研究[58]在合成自相似流量上组合经验模态分解、自回归模型与神经网络，评价的是需求预测误差，路由应用被列为后续工作。因而，预测对吞吐或排队的作用需要通过使用预测的具体策略说明。 <!-- [claim:CN22C056] [evidence:E073] -->

波束与功率研究[59]的作者稿先按平均功率选束，再固定当槽选择优化连续功率，并随到达和剩余需求更新。所设单星场景以供需平方差及满意度比的Jain指数评价匹配与公平性。对照采用相同选束规则而改变功率处理，但队列变化仍可能影响后续选择；该比较更适合解释分阶段配置的作用，而非整段时域中固定全部照射动作的单因素消融。 <!-- [claim:CN22C057] [evidence:E074] -->

多星覆盖重叠使成员关联和功率配置相互影响。需求感知资源分配[60]的作者稿由数字孪生侧多星选束与星内连续功率配置协作完成，并显式表示队列。其公平量使用覆盖小区队列包龄的极差，与单星模型[59]的满意度比Jain指数具有不同对象和方向。原文的固定功率与动态功率对照还同时改变功率动作与配置组织，吞吐差异随负载而变化。这说明增加决策自由度的价值需要结合实际瓶颈及共同对照条件解释。 <!-- [claim:CN22C058] [evidence:E076,E074] -->

共享频谱进一步引入需要保护的其他系统。Ngo等[61]的机构作者稿以LEO覆盖小区簇为智能体，通过集中评论器训练联合波束激活、子带和功率配置，并将超过GEO聚合干扰阈值的情形计入奖励惩罚。其目标同时考虑吞吐与小区间服务时延差异，智能体数不等于卫星数。与[59][60]比较时，应分别说明满意度、队列包龄与服务时延差异的定义；奖励惩罚的设置还需与执行时的约束满足分开评价。 <!-- [claim:CN22C124] [evidence:E128,E074,E076] -->

#### 3.3.2 接入切换与服务变化

切换控制既涉及目标卫星选择，也涉及协议过程中的信令与资源竞争。Lee等[62]通过学习接入状态调整切换请求，并省去传统流程中的测量报告环节。在一颗服务星与两颗目标星的仿真中，接入时延改善并不总伴随随机接入前导碰撞减少。该结果说明，应分别记录协议开销、资源块不足和接入竞争；接入阶段的改善还需通过后续路径和业务条件才能转化为端到端效果。 <!-- [claim:CN22C059] [evidence:E124] -->

独立测量为这些模型提供了不同性质的证据。Mohan等[63]观察到Starlink重配置边界附近的时延和吞吐变化，并在仅有单颗候选卫星的受控连接窗口中仍观察到波动。这支持服务变化在相应条件下无需以卫星切换为前提；周期性网络调度属于原作者对现象的解释。该例提示应分别记录接入对象、资源配置状态和最终业务性能。 <!-- [claim:CN22C060] [evidence:E078] -->

#### 3.3.3 路由结构与配置生效

路由比较首先需要区分转发架构。Handley[64]的机构接受稿研究无直接星间链路时如何通过地面中继连接卫星路径，将中继密度、传播时延、路径变化频率与重复建图成本结合分析。其分块索引和图复用降低了给定1584星、5000中继算例的重复计算负担，结果对应2019年的部署假设。动态激光链路研究[12]的作者稿则把建立新星间链路的时间纳入路径选择，采用预计算及路径分发，并省略排队与初始配置时延。转发资源、路由计算和链路建立由此成为不同的比较条件。 <!-- [claim:CN22C061] [evidence:E125,E121] -->

在动态激光链路研究[12]中，部分路径保持策略在低建链代价时增加平均时延，性能实验与计算成本分析还采用不同裁边设置。这些结果应分别解释，不能概括为活动感知方法的统一收益。路径搜索、控制消息传播和连接建立决定不同阶段的更新成本；适合高建链代价的策略，在队列主导或状态滞后的业务中还需重新评价。 <!-- [claim:CN22C062] [evidence:E121] -->

转发信息的表示又影响更新与恢复代价。Zhang等[65]的作者预印本以包内Bloom filter编码星间链路标识，通过分段再编码平衡额外转发和编码时延；遇到失效链路时，本地重算路线与使用预定绕行路径具有不同的路径质量和处理成本。其66星包级仿真与MATLAB数值实验采用不同的环路处理，结果需要分别解释。与地面中继[64]及动态建链[12]相比，该方法改变的是有星间链路网络的路径表示和失效响应方式，不能把三者的时延或恢复结果直接排序。 <!-- [claim:CN22C125] [evidence:E126,E125,E121] -->

#### 3.3.4 分层配置与局部权限

分层资源管理[66]将网络控制中心、空间基站和终端置于不同职责层级，以全局服务区域及频谱配置约束局部波束、时隙和信道安排，并交换需求与价格。其不同实验对应不同组件及负载，不能把组件收益相加为整体架构增益。分层的关键作用不仅是减少计算规模，还在于明确谁能修改哪些资源、使用何种状态以及上层配置何时对局部决策有效。 <!-- [claim:CN22C063] [evidence:E081] -->

**表4 通信管理代表研究的决策与结果定义**

| 研究及证据对象 | 决策或观察方式 | 主要结果定义 | 适用条件与解释范围 | <!-- [claim:CN22C064] [evidence:] -->
| --- | --- | --- | --- |
| 流量预测[58] | 需求估计模型 | 合成流量上的预测误差 | 配置收益由后续使用预测的策略决定 | <!-- [claim:CN22C065] [evidence:E073] -->
| 单星波束—功率[59] | 选束后优化连续功率并随需求更新 | 供需匹配及满意度公平性 | 单星；队列和后续选择随时间变化 | <!-- [claim:CN22C066] [evidence:E074] -->
| 多星需求感知配置[60] | 多星选束与星内功率配置协作 | 吞吐与队列包龄差异 | 整体策略对照；负载与动作表示不同 | <!-- [claim:CN22C067] [evidence:E076] -->
| GEO—LEO共存[61] | 以小区簇为智能体联合选束/子带/功率 | 吞吐与服务时延差异 | 机构作者稿；干扰奖励惩罚不等于逐动作硬保证 | <!-- [claim:CN22C128] [evidence:E128] -->
| 接入协议[62] | 学习调整请求并减少信令环节 | 接入时延与随机接入碰撞 | 三星仿真；两指标可呈相反变化 | <!-- [claim:CN22C129] [evidence:E124] -->
| 地面中继[64] | 分块建图、图复用及差分更新 | 传播时延、路由计算和路径变化 | 2019部署假设；接受稿，非当前现网测量 | <!-- [claim:CN22C130] [evidence:E125] -->
| 链路标识路由[65] | 包内路径编码、分段及本地失效响应 | 转发/编码成本、时延与交付率 | 有星间链路、66星仿真；按作者预印本解释 | <!-- [claim:CN22C131] [evidence:E126] -->
| 动态激光链路[12] | 路径选择计入新链路建立代价 | 原模型的端到端时延及路由更新 | 无队列、路径预分发；性能与成本配置分开 | <!-- [claim:CN22C068] [evidence:E121] -->
| 分层资源管理[66] | 全局配置约束局部波束等安排 | 原方案的服务和资源配置结果 | 层间权限、交换信息及组件实验范围 | <!-- [claim:CN22C069] [evidence:E081] -->
| 独立测量[63] | 观察受控连接窗口中的网络服务 | 时延与吞吐变化 | 外部现象；内部机制为原作者解释 | <!-- [claim:CN22C070] [evidence:E078] -->

表中作者稿、机构接受稿与预印本均按实际阅读版本解释。接入协议、传播路径、队列和路由更新采用不同的时延定义，异构场景中的结果不合并排名；公平量及成功样本的统计口径也分别保留。 <!-- [claim:CN22C071] [evidence:] -->

### 3.4 安全执行与异常恢复

#### 3.4.1 从风险信息到处置输入

安全信息链包含不同计算任务。最近接近方法[67]利用分段近似及距离极值搜索细化候选事件；筛查与CUDA研究[68]则压缩配对并组织并行计算，其速度和遗漏表现依赖目录、步长及实现。前者改善单个候选的精算过程，后者改变需要处理的候选集合及计算组织。组合使用时，应以同一传播与事件判定条件检查精度、遗漏和总耗时。 <!-- [claim:CN22C072] [evidence:E082,E084] -->

风险预测竞赛[69]估计后续报文中的风险，机动综述[70]整理可选处置方法，运行仿真[71]生成用于规则评估的场景与接近事件。竞赛综合分数、事件生成一致性与机动安全对应不同验证对象。CCSDS报文[72]和所引Starlink流程[73]进一步说明跨组织信息、风险重估及动作更新的接口。将风险处置接入业务调度，还需记录机动占用及其后可用活动，而不是以风险估计值直接替代任务结果。 <!-- [claim:CN22C073] [evidence:E087,E086,E085,E088,E089] -->

#### 3.4.2 轨迹安全与上层任务条件

轨迹研究将上层安排转化为受动力学约束的动作。锥优化[74]、反馈模型预测控制（MPC）[75]、机会约束交会[76]及特定轨道下的连续安全约束[77]采用不同的可行域和保证条件。它们向上层提供可执行轨迹、占用时间或安全退出条件；比较时需要保留误差模型、轨道环境及终端要求，避免把一种任务中的安全结论迁移为所有星座活动的通用保证。 <!-- [claim:CN22C074] [evidence:E091,E092,E093,E095] -->

已核方法进一步揭示保证的层次。[74]的凸子问题、逐次更新过程与原非线性问题具有不同的最优性和计时范围；[75]的避碰半空间、通信范围、误差界、离散步长及求解期限共同限制安全结论。通过延长终止时刻恢复可行性还可能改变上层活动的时间承诺。[76]的设计概率和有限样本检验、[77]的连续约束表达和数值容差也需分开解释；完全失推保护的结论应保留对部分推力不足的排除范围。 <!-- [claim:CN22C075] [evidence:E091,E092,E093,E095] -->

安全屏蔽研究[78]说明对照设置同样重要。同一学习策略的屏蔽开关实验，与未屏蔽策略对概率路线图的燃料—时间比较属于两组不同试验；后者还使用不同样本数量。屏蔽会改变允许动作和安全要求，路线图在执行机动时也进行状态校正。因此，比较应报告被改变的机制、安全标准和执行更新，而非仅使用“开环”或“闭环”标签。 <!-- [claim:CN22C076] [evidence:E096] -->

ADRAS-J公开记录的自主中止与安全后撤[79]提供了实际事件参照。安全退出保护了航天器，但原定接近或服务活动的后续完成仍需另行判断。业务层评价由此需要同时记录安全结果、被放弃或推迟的活动以及恢复后的能力。 <!-- [claim:CN22C077] [evidence:E097] -->

#### 3.4.3 告警、诊断与计划恢复

遥测异常检测为恢复提供线索。[80]将预测残差、平滑、阈值及告警区间处理结合，主要对照中的收益应归于实际变化的后处理。评价复核[81]进一步显示，测试标签、阈值选择及事件匹配规则会改变离线分数。两类研究共同说明，检测模型与评估过程都参与形成最终指标。告警命中、及时发现、准确诊断与恢复成功仍需要各自的结果定义，离线分数不能直接替代恢复后的业务状态。 <!-- [claim:CN22C078] [evidence:E098,E101] -->

故障检测、隔离与恢复（FDIR）规则原型[82]将故障事实、动作选择、执行及结果确认连接起来，并在恢复后向导航模式交接。Remote Agent[83]则在规划、执行与诊断之间处理局部失败活动和全局约束的关系。二者分别展示规则原型与任务执行系统中的恢复组织。评价其与业务调度的连接时，应说明诊断依据何时可用、谁授权动作、怎样确认效果，以及剩余任务如何继续；动作被触发与任务恢复完成属于不同事件。 <!-- [claim:CN22C079] [evidence:E102,E108] -->

**表5 安全与恢复的输出及验证对象**

| 环节及代表来源 | 直接输出 | 需要核对的保证范围 | <!-- [claim:CN22C080] [evidence:] -->
| --- | --- | --- |
| 接近计算与筛查[67][68] | 候选事件及最近接近结果 | 传播/数值参照、目录、步长与遗漏 | <!-- [claim:CN22C081] [evidence:E082,E084] -->
| 风险预测与场景[71][69] | 后续风险估计或事件列表 | 各自数据、评分与场景；处置效果另评 | <!-- [claim:CN22C082] [evidence:E085,E087] -->
| 安全轨迹[74][75][76][77] | 轨迹、控制及条件化约束保证 | 原任务域、误差/分布、连续性与求解期限 | <!-- [claim:CN22C083] [evidence:E091,E092,E093,E095] -->
| 学习屏蔽[78] | 经检查的动作及安全干预 | 两组对照、安全标准和执行校正 | <!-- [claim:CN22C084] [evidence:E096] -->
| 异常检测与评价[80][81] | 预测残差、告警区间及评价分数 | 阈值、标签、事件匹配与部署条件 | <!-- [claim:CN22C085] [evidence:E098,E101] -->
| 故障与执行恢复[82][83] | 恢复动作、效果确认及后续活动 | 原型/任务系统、诊断依据与执行交接 | <!-- [claim:CN22C086] [evidence:E102,E108] -->

### 3.5 多问题连接与综合运行

#### 3.5.1 联合选择、顺序输入与反馈

自动化工具[6]和可信自主运行综述[84]提供了功能组织背景，具体连接仍需回到决策变量。[11]的接触图调度为请求选择采集节点并检验交付路径，扣减已分配容量；逐请求交付及成功样本时延是其主要评价量，模型还假设能源与存储无限。[16]在观测—传输请求层共同安排，[17]采用观测与下传体积奖励，[47]保留当轮采集后优化处理。它们都连接相邻活动，但保留的上游修改权限及完成语义不同。 <!-- [claim:CN22C087] [evidence:E006,E105,E106,E042,E044,E053] -->

接触不可靠时，[11]还允许传输阶段依据当前连接局部选择路径。保留任务分配并允许绕行，与重新选择采集节点具有不同反馈范围。图2据此区分同次选择、先后输入和执行反馈；它们可在不同层次组合，而非互斥的架构等级。 <!-- [claim:CN22C088] [evidence:E106] -->

![图2 决策连接的三种方式](assets/fig2_cn.svg)

图2 联合选择、顺序安排与运行反馈。图中代表研究按实际阅读版本解释：共同选择[16][17][11]、顺序配置[47]及状态更新[9][85][86]。虚线表示反馈只作用于仍允许修改的活动；图示为本文归纳。 <!-- [claim:CN22C089] [evidence:E042,E044,E106,E053,E009,E107,E111] -->

#### 3.5.2 统一模型与状态驱动配置

SatOps—NetOps框架[9]把平台资源与网络需求写入任务模型，通过构造、局部搜索和事件触发重排形成安排；其架构分类与具体集成原型的性能实验应分别理解。分层管理[66]则用上层配置约束局部响应。两者都连接职责，区别在于是否共同选择变量，以及配置传递后局部仍保留哪些权限。 <!-- [claim:CN22C090] [evidence:E009,E081] -->

推理式观测调度[85]根据预测的观测、传输、存储和能源状态调整策略权重，再插入任务并检查约束。这使资源状态参与活动选择，其模型预测、规则和活动构造仍有不同职责。该方法的单星仿真与多星统一任务模型提供互补例子，均需保留各自的状态表达和验证范围。 <!-- [claim:CN22C091] [evidence:E107] -->

#### 3.5.3 从计划到执行的功能交接

计划进入执行系统需要可检查的功能交接。Remote Agent[83]将规划、执行及诊断连接起来，并处理局部失败与全局约束的关系；EO-1[87]展示科学分析产生目标、CASPER调整活动和SCL检查执行的流程，同时保留地面规划与星历更新。IPEX官方资料[86]提供单星星上处理和持续规划的工程例子，cFS演示包[88]则提供软件组件连接依据。飞行事件与软件组件承担不同的证据职责，均需对应到具体输入、动作及结果。 <!-- [claim:CN22C092] [evidence:E108,E109,E111,E113] -->

配置的一致性可以在软件接口层进一步检查。Basciani等[89]用统一模型表达星上软件任务及其时序约束，将结构校验、领域规则、候选优化、仿真检查与配置生成连接起来，再由人工审定并交平台机制切换生效。模型信息变化与实际部署配置变化被分别处理，避免将所有模型更新都转成部署操作。该研究用于说明从计划到配置的交接，其对象是星上软件进程；与星座业务调度连接时，还需建立任务、资源和状态的对应关系。 <!-- [claim:CN22C126] [evidence:E119] -->

Starling[90]以四星共享观测状态并协调后续观测；Starling 1.5[91]在模拟接近场景中进行责任协调和实际机动。这些案例扩大了共享信息和动作权限的范围，但观测选择与跨运营方处置具有不同触发事件。Basilisk[92]及形式化研究[93]为模型仿真和规格检查提供工具。综合运行的评价需要进一步确认状态、计划及动作是否按同一语义交接，以及最终业务结果如何产生。 <!-- [claim:CN22C093] [evidence:E114,E115,E116,E117] -->

## 4 综合认识与研究问题

### 4.1 以共同结果和完整成本解释可扩展性

技术收益首先来自被利用的问题结构。窗口分层[16]、图缩减及邻域求解[17]、轨迹预计算[56][57]、计划复用[14]和几何邻域[15]分别改变搜索维度、候选表示、准备成本和协调范围。较少的变量或消息能够降低部分负担，也可能保留更多冗余或舍弃候选。对图变换、保守约束和候选筛选，应同时检查解质量和可行活动集合的变化。 <!-- [claim:CN22C094] [evidence:E042,E044,E071,E072,E034,E035] -->

规模比较应区分系统成员、实际需求和候选变量。[35]可按时域内需求压缩服务对象，[43]的不同排列可映射到同一排程，情景展开[52]会使少量物理成员形成大量变量；学习辅助搜索[53]则在两颗卫星上增加任务数量。名义卫星数或任务数都不能单独代表搜索难度。限时可行率、求解器间隙及未完成原因应与质量指标共同报告；[32]成功实例上的平均改善还需保留成功率，未在预算内找到安排也不能直接解释为物理不可行。 <!-- [claim:CN22C095] [evidence:E028,E048,E062,E123,E025] -->

完整决策成本包括候选与模型准备、在线求解及协调、修改后的资源生效。轨迹网格[57]和学习策略[54]把部分计算前移，DSN求解[44]包含特定准备及撤收约束，地面中继路由[64]需要更新拓扑与边时延，动态链路[12]还对新连接显式计时代价。预处理能否摊销取决于复用次数和环境变化。比较时宜同时报告准备成本、在线预算、消息开销和资源生效时刻，再判断计算能否在剩余活动窗口内完成。 <!-- [claim:CN22C096] [evidence:E072,E065,E049,E125,E121] -->

### 4.2 资源耦合何时值得共同求解

扩大决策范围的价值取决于下游约束能否改变当前候选。[16]让传输窗口参与观测安排，[11]在采集节点选择时检查交付容量，[47]则在采集固定后配置计算资源。若下游瓶颈会淘汰某些上游选择，将其提前纳入模型可以避免占用无法兑现的机会；若上游已经执行，适用问题便转为剩余资源配置或下一轮反馈。该区别由变量和承诺决定，而非“联合”这一名称。 <!-- [claim:CN22C097] [evidence:E042,E106,E053] -->

共同选择还要满足信息与生效条件。下游状态可获得、上游活动尚可修改时，联合选择能够把相邻活动的约束提前纳入同一决定；上游活动已经执行时，处理和传输配置则围绕剩余资源展开；新状态在计划执行期间出现时，反馈的作用范围取决于尚可撤销的安排及其生效窗口。图缩减和模型简化还可能改变可行范围[17]。表6据此给出定性的适用条件，供解释代表研究及设计共同场景比较，不构成三类方式的统一性能排序。 <!-- [claim:CN22C098] [evidence:E044] -->

**表6 决策连接的适用条件与评价要求**

| 连接方式及参考研究 | 主要适用条件 | 应固定的比较口径 | 主要代价 | <!-- [claim:CN22C099] [evidence:] -->
| --- | --- | --- | --- |
| 联合选择[16][17][11] | 下游状态可得且影响当前节点、窗口或次序 | 完成定义、奖励分项、候选与部分交付规则 | 耦合规模、近似及可行集合变化 | <!-- [claim:CN22C100] [evidence:E042,E044,E106] -->
| 顺序配置[47][59] | 上游已定，下游仍有可调资源 | 固定变量、输入负载及局部目标 | 上游在本次求解中保留的限制 | <!-- [claim:CN22C101] [evidence:E053,E074] -->
| 状态反馈[9][85][86] | 新状态已确认，后续活动尚可修改 | 状态版本、更新窗口和已承诺资源 | 信息传播、重排、冲突检查及生效 | <!-- [claim:CN22C102] [evidence:E009,E107,E111] -->
| 分层组合（本文归纳） | 各阶段具有不同信息、时域及权限 | 共同任务/扰动、层间输入及交接事件 | 权限交叠、重复调整及状态不一致 | <!-- [claim:CN22C103] [evidence:] -->

业务瓶颈还会改变单个模块的价值。Kodan[49]中，处理时间是否达到帧期限，会改变提速与分类精度对有效下传的作用；波束和功率研究[59][60]中，负载及队列决定配置自由度的作用。评价联合程度时，宜先保持完成定义、负载和资源条件一致，再分别改变允许修改的变量。这样才能区分来自信息利用、资源自由度和奖励构造的差异。 <!-- [claim:CN22C104] [evidence:E058,E074,E076] -->

### 4.3 信息、权限与学习模块的接口

信息共享的作用取决于待协调的决定。完成状态[54]帮助识别已满足目标，同一时段的任务竞争还需要分配或意图信息。延迟通信规划[40]与异步分配[41]在不同的信息时序下组织协调，标准CBBA[39]的评分和传播条件、分层管理[66]的权限分配也会限制结论。因此，应同时描述共享内容、获得时刻和修改权限；对于过时信息，还需保留旧决定可能继续占用资源的影响。 <!-- [claim:CN22C105] [evidence:E065,E039,E041,E037,E081] -->

资源承诺进一步确定更新范围。预约规则[10]、既有容量分配[11]及新链路建立[12]分别约束组织、算法和物理执行。局部修复与全局重算的比较，应使用相同状态、承诺和生效条件，评价保留旧计划、修改后续活动或采取保守响应造成的业务差异。 <!-- [claim:CN22C106] [evidence:E052,E106,E121] -->

学习的贡献应对应明确模块。需求预测[58]输出状态估计，Q-learning辅助遗传搜索[53]选择搜索算子，策略复用[54]生成调度动作，安全屏蔽[78]检查允许执行的动作，协议学习[62]则改变切换请求过程。它们的输入、输出和约束职责不同。具体比较需要保持任务、状态和安全要求一致，分别记录训练、推理、解码、修复及协调成本。整体方案同时改变多个组件时，可报告整体效果，单模块归因则需要保持其他条件相同的对照。 <!-- [claim:CN22C107] [evidence:E073,E123,E065,E096,E124] -->

### 4.4 运行实践及验证范围

工程资料的价值在于明确模型中的事件如何落到实际职责。表7将公开接口、测量、原型与飞行案例按观察对象组织。Planet与AWS文档[46][10]解释完成状态及预约，DSN运营[45]补充候选、协商与确认，独立测量[63]观察服务现象，EO-1和Starling系列[87][90][91]展示限定任务中的状态反馈与执行。它们为综述提供互补依据，各自的验证对象仍须保留。 <!-- [claim:CN22C108] [evidence:E051,E052,E050,E078,E109,E114,E115] -->

**表7 运行资料与工具能够支持的认识**

| 资料或案例 | 公开的状态、动作或性质 | 对综述的用途与边界 | <!-- [claim:CN22C109] [evidence:] -->
| --- | --- | --- |
| Iridium[30] | 备用资产投入 | 能力配置例子；库存最优性及恢复时间另评 | <!-- [claim:CN22C110] [evidence:E022] -->
| Planet、AWS与DSN[45][46][10] | 质量、交付、预约及安排确认 | 完成事件和承诺过程；内部优化性能另评 | <!-- [claim:CN22C111] [evidence:E050,E051,E052] -->
| Starlink流程及独立测量[63][73] | 风险行动流程；时延与吞吐现象 | 运营方说明与外部测量分开解释 | <!-- [claim:CN22C112] [evidence:E078,E089] -->
| ADRAS-J[79] | 异常后的自主中止及后撤 | 安全处置事件；原任务后续完成另评 | <!-- [claim:CN22C113] [evidence:E097] -->
| EO-1与IPEX[87][86] | 星上处理、重规划与执行检查 | 单星功能交接与地面职责 | <!-- [claim:CN22C114] [evidence:E109,E111] -->
| Starling系列[90][91] | 共享观测与实际机动协调 | 试验目标、成员规模及模拟事件条件 | <!-- [claim:CN22C115] [evidence:E114,E115] -->
| 受监督配置[89] | 模型校验、仿真检查、配置生成与审定 | 13进程工具链及专家反馈；不是大规模在轨验证 | <!-- [claim:CN22C132] [evidence:E119] -->
| CCSDS、cFS与形式化研究[72][88][93][94] | 报文、组件与规格性质 | 互操作及软件依据；业务结果另评 | <!-- [claim:CN22C116] [evidence:E088,E113,E117,E120] -->

验证链应将工件、性质与环境对应起来。受监督重配置[89]的13进程实例和6名专家评价说明模型、校验与配置生成的衔接，其工具链步骤计时不代表优化器或整星座重规划时延。模型检查[94]讨论规格性质，规则原型[82]测量特定软硬件过程，Basilisk[92]支持可配置动力学仿真。规格满足、模型可行、有限样本无违反与飞行事件分别具有不同含义。资源限制导致的未完成分析也应保留，避免将软件验证通过直接解释为持续服务改善。 <!-- [claim:CN22C117] [evidence:E119,E120,E102,E116] -->

### 4.5 面向持续服务的研究问题

首先，可在共同故障与需求序列下连接能力恢复和业务损失。库存、双通道补给与维修[25][26][29]提供不同恢复途径，比较应分别记录资源可得、到位、载荷恢复和业务重分配时间，再评价未满足请求或通信中断。这允许使用分层及事件驱动模型，不要求把全部库存、轨迹与活动一次联立。 <!-- [claim:CN22C118] [evidence:E018,E019,E023] -->

其次，可在同一任务样本下检验决策连接范围。围绕[16][17][47][11]所示机制，设置采集优先、顺序处理与下传、共同选择以及允许事件修复的方案，保持窗口、存储、容量和截止期一致，并预先确定请求完成与数据量的分项指标。比较最终业务结果、限时可行率和准备/在线/执行成本，可以检验表6的条件分析。上述共同场景评价可作为后续检验表6定性判断的方案。 <!-- [claim:CN22C119] [evidence:E042,E044,E053,E106] -->

最后，在线调整与学习评价可使用共同的事件时间轴。记录任务到达、状态确认、求解结束、冲突消解和配置生效，区分已完成、未来意图及已承诺资源[10][54][66][11][12]；为预测、搜索辅助和动作生成设置对应替代方法，并保留训练、推理与修复成本。共同输入能够增强比较的解释力，轨道模型、权限和验证保真度的差异仍需单列。 <!-- [claim:CN22C120] [evidence:E052,E065,E081,E106,E121] -->

## 5 结论

本文以对地观测与通信为核心，梳理大型星座能力维持、任务安排、网络配置及安全恢复的代表研究，并以业务完成、可改变量和运行反馈连接不同技术路线。构型与补给确定资源可用的时间和位置，业务调度将其转化为活动或持续服务，执行状态再改变后续安排。因此，模型中的决定与完成事件是解释方法联系的基础。 <!-- [claim:CN22C121] [evidence:] -->

本文形成三点综合认识。首先，成像收益、下传数据量、按期请求完成及资产恢复表示不同结果，评价应保留完成定义、统计分母和未完成情况。其次，联合选择、顺序配置与运行反馈的取舍取决于下游约束是否影响当前候选、上游是否仍可修改，以及状态和配置能否及时生效；这些方式可以在不同层次组合。最后，方法的可扩展性需要同时说明系统成员、任务、候选变量及协调主体，并将准备、训练、求解、冲突检查和配置生效纳入成本解释。局部模块的改善只有经过实际权限与功能交接，才能影响最终业务结果。 <!-- [claim:CN22C122] [evidence:] -->

公开接口、独立测量、软件验证与飞行案例使上述比较进一步对应到预约、质量确认、告警、动作及恢复等事件，各类证据支持其实际观察对象。后续研究可在共同任务和扰动序列下检验能力恢复、决策耦合与延迟更新的取舍，并追踪最终服务结果。本综述提供的是解释现有方法及组织后续评价的条件性认识，尚不能替代共同场景试验或完整运行系统验证。 <!-- [claim:CN22C123] [evidence:] -->

## 参考文献

1. Mohamed Khalil Ben-Larbi; Kattia Flores Pozo; Tom Haylok; et al. Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts〔迈向大型分布式卫星系统自动化运行，第一部分：综述与范式转变〕. Advances in Space Research, 2021, 67(11): 3598–3619. DOI: 10.1016/j.asr.2020.08.009. [来源](https://doi.org/10.1016/j.asr.2020.08.009)

2. Koki Ho. Space Logistics Modeling and Optimization: Review of the State of the Art〔空间物流建模与优化：研究现状综述〕. Journal of Spacecraft and Rockets, 2024, 61(5): 1417–1427. DOI: 10.2514/1.A35982. [来源](https://doi.org/10.2514/1.A35982)

3. Xinwei Wang; Guohua Wu; Lining Xing; et al. Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions〔敏捷对地观测卫星调度二十年：建模、方法与未来方向〕. IEEE Systems Journal, 2021, 15(3): 3881–3892. DOI: 10.1109/JSYST.2020.2997050. [来源](https://doi.org/10.1109/JSYST.2020.2997050)

4. Benedetta Ferrari; Jean-François Cordeau; Maxence Delorme; et al. Satellite Scheduling Problems: A survey of applications in Earth and outer space observation〔卫星调度问题：对地与外层空间观测应用综述〕. Computers & Operations Research, 2025, 173: 106875. DOI: 10.1016/j.cor.2024.106875. [来源](https://doi.org/10.1016/j.cor.2024.106875)

5. Mohammad Reza Jabbarpour; Bao Quoc Vo; Ghaith El-Dalahmeh; et al. Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges〔分布式航天系统与任务管理的智能体方法：方法体系、实践现状与挑战〕. Acta Astronautica, 2026, 238: 237–257. DOI: 10.1016/j.actaastro.2025.10.018. [来源](https://doi.org/10.1016/j.actaastro.2025.10.018)

6. Mohamed Khalil Ben-Larbi; Kattia Flores Pozo; Mirue Choi; et al. Towards the automated operations of large distributed satellite systems. Part 2: Classifications and tools〔迈向大型分布式卫星系统自动化运行，第二部分：分类与工具〕. Advances in Space Research, 2021, 67(11): 3620–3637. DOI: 10.1016/j.asr.2020.08.018. [来源](https://doi.org/10.1016/j.asr.2020.08.018)

7. 龚李赠; 张文龙; 陈全; 等. 低轨巨型星座智能组网技术综述. 航空学报, 2026，网络首发版本；终排信息待核. DOI: 10.7527/S1000-6893.2026.32935. [来源](https://doi.org/10.7527/S1000-6893.2026.32935)

8. 邸航; 董涛; 刘志慧; 等. 低轨通信卫星星座网络资源管控与优化技术综述. 宇航学报, 2026, 47(2): 270–283. DOI: 10.3873/j.issn.1000-1328.2026.02.002. [来源](https://doi.org/10.3873/j.issn.1000-1328.2026.02.002)

9. Arnau Singla; Franco Criscola; David Canales; et al. Toward Integrated Satellite Operations and Network Management: A Review and Novel Framework〔迈向卫星运行与网络管理的一体化：综述与新框架〕. Technologies, 2025, 13(8): 312. DOI: 10.3390/technologies13080312. [来源](https://doi.org/10.3390/technologies13080312)

10. Amazon Web Services. Work with contacts〔使用卫星过站联系〕. Official documentation; accessed 10 October 2026 (inherited access date). https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html. [来源](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html)

11. Christopher John Lowe; Ruaridh Alexander Clark; Ciara Norah McGrath; et al. A delay-tolerant network approach to satellite pickup and delivery scheduling〔卫星采集与交付调度的延迟容忍网络方法〕. Ad Hoc Networks, 2023, 151: 103289. DOI: 10.1016/j.adhoc.2023.103289. [来源](https://doi.org/10.1016/j.adhoc.2023.103289)

12. Dhiraj Bhattacharjee; Pablo G. Madoery; Aizaz U. Chaudhry; et al. On-Demand Routing in LEO Mega-Constellations With Dynamic Laser Inter-Satellite Links〔具有动态激光星间链路的低轨巨型星座按需路由〕. IEEE Transactions on Aerospace and Electronic Systems, 2024, 60(5): 7089–7105. DOI: 10.1109/TAES.2024.3415571. [来源](https://doi.org/10.1109/TAES.2024.3415571)

13. Yuhe Mao; Yunhua Wu; Xiaozhe Ju; et al. Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation〔低轨巨型星座动态管理拓扑的构建、演化与维护〕. Space: Science & Technology, 2025, 5: 0248. DOI: 10.34133/space.0248. [来源](https://doi.org/10.34133/space.0248)

14. Shreya Parjan; Steve A. Chien. Decentralized Observation Allocation for a Large-Scale Constellation〔大型星座的去中心化观测分配〕. Journal of Aerospace Information Systems, 2023, 20(8): 447–461. DOI: 10.2514/1.I011215. [来源](https://doi.org/10.2514/1.I011215)

15. Itai Zilberstein; Ananya Rao; Matthew Salis; et al. Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation〔面向大型卫星星座的去中心化分解式观测调度〕. Journal of Artificial Intelligence Research, 2025, 82: 169–208. DOI: 10.1613/jair.1.16997. [来源](https://doi.org/10.1613/jair.1.16997)

16. Lijun He; Ben Liang; Jiandong Li; et al. Joint Observation and Transmission Scheduling in Agile Satellite Networks〔敏捷卫星网络中的观测与传输联合调度〕. IEEE Transactions on Mobile Computing, 2022, 21(12): 4381–4396. DOI: 10.1109/TMC.2021.3076088. [来源](https://doi.org/10.1109/TMC.2021.3076088)

17. Yure Rocha; Guilherme O. Chagas; Leandro C. Coelho; et al. The integrated agile Earth observation satellite scheduling problem〔敏捷对地观测卫星成像与下传联合调度问题〕. Computers & Operations Research, 2025, 184: 107212. DOI: 10.1016/j.cor.2025.107212. [来源](https://doi.org/10.1016/j.cor.2025.107212)

18. Leonid Appel; Moshe Guelman; David Mishne. Optimization of satellite constellation reconfiguration maneuvers〔卫星星座重构机动优化〕. Acta Astronautica, 2014, 99: 166–174. DOI: 10.1016/j.actaastro.2014.02.016. [来源](https://doi.org/10.1016/j.actaastro.2014.02.016)

19. Hang Woon Lee; Koki Ho. Regional Constellation Reconfiguration Problem: Integer Linear Programming Formulation and Lagrangian Heuristic Method〔区域星座重构问题：整数线性规划模型与拉格朗日启发式方法〕. Journal of Spacecraft and Rockets, 2023, 60(6): 1828–1845. DOI: 10.2514/1.A35685. [来源](https://doi.org/10.2514/1.A35685)

20. Hang Woon Lee; David O. Williams Rogers; Brycen D. Pearl; et al. Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods〔采用整数规划与序贯决策方法的确定性多阶段星座重构〕. Journal of Spacecraft and Rockets, 2025, 62(1): 206–222. DOI: 10.2514/1.A35990. [来源](https://doi.org/10.2514/1.A35990)

21. Hang Woon Lee; Seiichi Shimizu; Shoji Yoshikawa; et al. Satellite Constellation Pattern Optimization for Complex Regional Coverage〔面向复杂区域覆盖的卫星星座模式优化〕. Journal of Spacecraft and Rockets, 2020, 57(6): 1309–1327. DOI: 10.2514/1.A34657. [来源](https://doi.org/10.2514/1.A34657)

22. Hang Woon Lee; Pauline C. Jakob; Koki Ho; et al. Optimization of satellite constellation deployment strategy considering uncertain areas of interest〔考虑不确定关注区域的卫星星座部署策略优化〕. Acta Astronautica, 2018, 153: 213–228. DOI: 10.1016/j.actaastro.2018.03.054. [来源](https://doi.org/10.1016/j.actaastro.2018.03.054)

23. Beomjin Gwon; Jaemyung Ahn. Two-Stage Framework for Deployment-Aware Optimization of Satellite Constellation Pattern Design〔考虑部署过程的卫星星座模式设计两阶段优化框架〕. International Journal of Aeronautical and Space Sciences, 2026. DOI: 10.1007/s42405-026-01298-1. [来源](https://doi.org/10.1007/s42405-026-01298-1)

24. Samuel Martínez Zamacola; Ramón Martínez Rodríguez-Osorio; Miguel A. Salas-Natera. Joint satellite platform and constellation sizing for instantaneous beam-hopping in 5G/6G Non-Terrestrial Networks〔面向5G/6G非地面网络瞬时跳波束的卫星平台与星座联合规模设计〕. Computer Networks, 2025, 257: 110942. DOI: 10.1016/j.comnet.2024.110942. [来源](https://doi.org/10.1016/j.comnet.2024.110942)

25. Pauline Jakob; Seiichi Shimizu; Shoji Yoshikawa; et al. Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control〔采用多级库存控制的最优卫星星座备份策略〕. Journal of Spacecraft and Rockets, 2019, 56(5): 1449–1461. DOI: 10.2514/1.A34387. [来源](https://doi.org/10.2514/1.A34387)

26. Jaewoo Kim; Jaemyung Ahn; Taehyun Sung. Replenishment Strategy for Satellite Constellation with Dual Supply Modes〔双供给模式下的卫星星座补网策略〕. Journal of Spacecraft and Rockets, 2025, 62(5): 1567–1583. DOI: 10.2514/1.A36281. [来源](https://doi.org/10.2514/1.A36281)

27. Seungyeop Han; Zachary Grieser; Shoji Yoshikawa; et al. Spare Strategy Analysis and Design for Mega Satellite Constellations Using Markov Chain〔采用马尔可夫链的巨型卫星星座备份策略分析与设计〕. Journal of Spacecraft and Rockets, 2026: 1–12. DOI: 10.2514/1.A36599. [来源](https://doi.org/10.2514/1.A36599)

28. Seungyeop Han; Shoji Yoshikawa; Takumi Noro; et al. Spare strategy for large-scale satellite constellations under dual resupply channels using Markov chain〔采用马尔可夫链的双补给通道大型卫星星座备份策略〕. Acta Astronautica, 2026, 248: 614–629; assigned issue: November 2026. DOI: 10.1016/j.actaastro.2026.06.020. [来源](https://doi.org/10.1016/j.actaastro.2026.06.020)

29. Jaewoo Kim; Taehyun Sung; Woonam Hwang; et al. On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation〔融合在轨服务的卫星星座维护策略〕. Journal of Spacecraft and Rockets, 2026: 1–18. DOI: 10.2514/1.A36684. [来源](https://doi.org/10.2514/1.A36684)

30. Iridium. Iridium Adds to Constellation Resilience with Launch of Spare Satellites〔铱星通过发射备份卫星增强星座韧性〕. Official operational release; accessed 10 October 2026 (inherited access date). https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites. [来源](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites)

31. Yuri Shimane; Nicholas Gollins; Koki Ho. Orbital Facility Location Problem for Satellite Constellation Servicing Depots〔卫星星座服务仓库的轨道设施选址问题〕. Journal of Spacecraft and Rockets, 2024, 61(3): 808–825. DOI: 10.2514/1.A35691. [来源](https://doi.org/10.2514/1.A35691)

32. Euihyeon Choi; Koki Ho. Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers〔低推力转移下卫星星座服务轨道仓库位置优化〕. Journal of Spacecraft and Rockets, 2026, 63(1): 4–13. DOI: 10.2514/1.A36386. [来源](https://doi.org/10.2514/1.A36386)

33. Yaxiong Li; Xinglong Sun; Xinxue Liu; et al. Deployment of On-Orbit Service Vehicles Using a Fuzzy Adaptive Particle Swarm Optimization Algorithm〔采用模糊自适应粒子群算法的在轨服务航天器部署〕. Modelling and Simulation in Engineering, 2021, 2021: 1–15. DOI: 10.1155/2021/6644339. [来源](https://doi.org/10.1155/2021/6644339)

34. Tristan Sarton du Jonchay; Hao Chen; Onalli Gunasekara; et al. Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties〔需求不确定性下在轨服务运行的建模与优化框架〕. Journal of Spacecraft and Rockets, 2021, 58(4): 1157–1173. DOI: 10.2514/1.A34978. [来源](https://doi.org/10.2514/1.A34978)

35. Tristan Sarton du Jonchay; Hao Chen; Masafumi Isaji; et al. On-Orbit Servicing Optimization Framework with High- and Low-Thrust Propulsion Tradeoff〔兼顾高推力与低推力权衡的在轨服务优化框架〕. Journal of Spacecraft and Rockets, 2022, 59(1): 33–48. DOI: 10.2514/1.A35094. [来源](https://doi.org/10.2514/1.A35094)

36. Michel Lemaître; Gérard Verfaillie; Frank Jouhaud; et al. Selecting and scheduling observations of agile satellites〔敏捷卫星观测任务的选择与调度〕. Aerospace Science and Technology, 2002, 6(5): 367–381. DOI: 10.1016/S1270-9638(02)01173-2. [来源](https://doi.org/10.1016/S1270-9638(02)01173-2)

37. Laio Oriel Seman; Brenda F. Ribeiro; Cezar A. Rigo; Edemar Morsch Filho; Eduardo Camponogara; Rodrigo Leonardi; Eduardo A. Bezerra. An Energy-Aware Task Scheduling for Quality-of-Service Assurance in Constellations of Nanosatellites〔面向纳卫星星座服务质量保障的能量感知任务调度〕. Sensors, 2022, 22(10): 3715. DOI: 10.3390/s22103715. [来源](https://doi.org/10.3390/s22103715)

38. Shai Krigman; Tal Grinshpoun; Lihi Dery. Scheduling of Earth observing satellites using distributed constraint optimization〔采用分布式约束优化的对地观测卫星调度〕. Journal of Scheduling, 2024, 27(5): 507–524. DOI: 10.1007/s10951-024-00816-x. [来源](https://doi.org/10.1007/s10951-024-00816-x)

39. Han-Lim Choi; L. Brunet; J. P. How. Consensus-Based Decentralized Auctions for Robust Task Allocation〔用于鲁棒任务分配的基于一致性的去中心化拍卖〕. IEEE Transactions on Robotics, 2009, 25(4): 912–926. DOI: 10.1109/TRO.2009.2022423. [来源](https://doi.org/10.1109/TRO.2009.2022423)

40. Chong Wang; Jinhui Tang; Xiaohang Cheng; et al. Distributed cooperative task planning algorithm for multiple satellites in delayed communication environment〔延迟通信环境下多卫星分布式协同任务规划算法〕. Journal of Systems Engineering and Electronics, 2016, 27(3): 619–633. DOI: 10.1109/JSEE.2016.00066. [来源](https://doi.org/10.1109/JSEE.2016.00066)

41. Ben Rachmut; Sofia Amador Nelke; Roie Zivan. Asynchronous Communication Aware Multi-Agent Task Allocation〔异步通信感知的多智能体任务分配〕. Proceedings of IJCAI, 2023: 262–270. DOI: 10.24963/ijcai.2023/30. [来源](https://doi.org/10.24963/ijcai.2023/30)

42. Laura Barbulescu; Jean-Paul Watson; L. Darrell Whitley; et al. Scheduling Space–Ground Communications for the Air Force Satellite Control Network〔美国空军卫星控制网络的星地通信调度〕. Journal of Scheduling, 2004, 7(1): 7–34. DOI: 10.1023/B:JOSH.0000013053.32600.3c. [来源](https://doi.org/10.1023/B:JOSH.0000013053.32600.3c)

43. Daniel Karapetyan; Snezana Mitrovic Minic; Krishna T. Malladi; et al. Satellite downlink scheduling problem: A case study〔卫星下传调度问题：一个案例研究〕. Omega, 2015, 53: 115–123. DOI: 10.1016/j.omega.2015.01.001. [来源](https://doi.org/10.1016/j.omega.2015.01.001)

44. Alex Sabol; Ryan Alimo; Farhad Kamangar; et al. Deep Space Network Scheduling via Mixed-Integer Linear Programming〔基于混合整数线性规划的深空网络调度〕. IEEE Access, 2021, 9: 39985–39994. DOI: 10.1109/ACCESS.2021.3064928. [来源](https://doi.org/10.1109/ACCESS.2021.3064928)

45. Mark D. Johnston; Daniel Tran; Belinda Arroyo; et al. Automated Scheduling for NASA's Deep Space Network〔NASA深空网络的自动调度〕. AI Magazine, 2014, 35(4): 7–25. DOI: 10.1609/aimag.v35i4.2552. [来源](https://doi.org/10.1609/aimag.v35i4.2552)

46. Planet. Tasking API〔任务规划API〕. Official documentation; accessed 10 October 2026 (inherited access date). https://docs.planet.com/develop/apis/tasking/. [来源](https://docs.planet.com/develop/apis/tasking/)

47. Beatriz Soret; Antonio M. Mercado-Martínez; Antonio Jurado-Navas; et al. Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing〔卫星对地观测边缘智能：图像采集与处理调度〕. International Journal of Satellite Communications and Networking, 2026: 1–22; advance online publication, 24 August 2026. DOI: 10.1002/sat.70082. [来源](https://doi.org/10.1002/sat.70082)

48. Danilo Magliarisi; Emiliano Casalicchio; Vincenzo Salvatore. Orbit-aware task scheduling in satellite edge computing〔卫星边缘计算中的轨道感知任务调度〕. Cluster Computing, 2025, 28(16): 1013. DOI: 10.1007/s10586-025-05663-9. [来源](https://doi.org/10.1007/s10586-025-05663-9)

49. Bradley Denby; Krishna Chintalapudi; Ranveer Chandra; et al. Kodan: Addressing the Computational Bottleneck in Space〔Kodan：应对空间计算瓶颈〕. Proceedings of ASPLOS, Volume 3, 2023: 392–403. DOI: 10.1145/3582016.3582043. [来源](https://doi.org/10.1145/3582016.3582043)

50. Qiu Dishan; He Chuan; Liu Jin; Ma Manhao. A Dynamic Scheduling Method of Earth-Observing Satellites by Employing Rolling Horizon Strategy〔采用滚动时域策略的对地观测卫星动态调度方法〕. The Scientific World Journal, 2013, 2013(1): 304047. DOI: 10.1155/2013/304047. [来源](https://doi.org/10.1155/2013/304047) 本文依据出版社完整HTML正文。

51. Xinwei Wang; Guopeng Song; Roel Leus; et al. Robust Earth Observation Satellite Scheduling With Uncertainty of Cloud Coverage〔云覆盖不确定性下的鲁棒对地观测卫星调度〕. IEEE Transactions on Aerospace and Electronic Systems, 2020, 56(3): 2450–2461. DOI: 10.1109/TAES.2019.2947978. [来源](https://doi.org/10.1109/TAES.2019.2947978)

52. Christopher G. Valicka; Deanna Garcia; Andrea Staid; et al. Mixed-integer programming models for optimal constellation scheduling given cloud cover uncertainty〔考虑云覆盖不确定性的最优星座调度混合整数规划模型〕. European Journal of Operational Research, 2019, 275(2): 431–445. DOI: 10.1016/j.ejor.2018.11.043. [来源](https://doi.org/10.1016/j.ejor.2018.11.043)

53. Yanjie Song; Luona Wei; Qing Yang; Jian Wu; Lining Xing; Yingwu Chen. RL-GA: A Reinforcement Learning-based Genetic Algorithm for Electromagnetic Detection Satellite Scheduling Problem〔RL-GA：面向电磁探测卫星调度的强化学习遗传算法〕. Swarm and Evolutionary Computation, 2023, 77: 101236. DOI: 10.1016/j.swevo.2023.101236. [来源](https://doi.org/10.1016/j.swevo.2023.101236)

54. Adam Herrmann; Mark A. Stephenson; Hanspeter Schaub. Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations〔面向可扩展对地观测卫星星座运行的单智能体强化学习〕. Journal of Spacecraft and Rockets, 2024, 61(1): 114–132. DOI: 10.2514/1.A35736. [来源](https://doi.org/10.2514/1.A35736)

55. Adam Herrmann; Hanspeter Schaub. A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling〔对地观测卫星调度强化学习算法的比较分析〕. Frontiers in Space Technologies, 2023, 4: 1263489. DOI: 10.3389/frspt.2023.1263489. [来源](https://doi.org/10.3389/frspt.2023.1263489)

56. Riccardo Apa; Jennifer Hudson; Marcello Romano. Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit〔低轨多客户服务任务的低推力推进与漂移轨道优化〕. The Journal of the Astronautical Sciences, 2026, 73(2): 36. DOI: 10.1007/s40295-026-00580-4. [来源](https://doi.org/10.1007/s40295-026-00580-4)

57. Riccardo Apa; Shambo Bhattacharjee; Jennifer Hudson; et al. Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations〔摄动条件下低推力服务卫星的最优多客户轨迹规划〕. The Journal of the Astronautical Sciences, 2025, 72(2): 7. DOI: 10.1007/s40295-025-00487-6. [来源](https://doi.org/10.1007/s40295-025-00487-6)

58. Chi Han; Wei Xiong; Ronghuan Yu. A Hybrid Forecasting Model for Self-Similar Traffic in LEO Mega-Constellation Networks〔低轨巨型星座网络自相似流量的混合预测模型〕. Aerospace, 2024, 11(3): 191. DOI: 10.3390/aerospace11030191. [来源](https://doi.org/10.3390/aerospace11030191)

59. Shuang Zheng; Xing Zhang; Peng Wang; Wenbo Wang. Joint Beam Scheduling and Power Optimization for Beam Hopping LEO Satellite Systems〔跳波束低轨卫星系统的联合波束调度与功率优化〕. China Communications, 2024, 21(10): 1–14. DOI: 10.23919/JCC.ja.2022-0864. [来源](https://doi.org/10.23919/JCC.ja.2022-0864)

60. Ruili Zhao; Jun Cai; Jiangtao Luo; et al. Demand-Aware Beam Hopping and Power Allocation for Load Balancing in Digital Twin Empowered LEO Satellite Networks〔数字孪生赋能低轨卫星网络中面向负载平衡的需求感知跳波束与功率分配〕. IEEE Transactions on Wireless Communications, 2025, 24(6): 5084–5098. DOI: 10.1109/TWC.2025.3545745. [来源](https://doi.org/10.1109/TWC.2025.3545745)

61. Quynh Tu Ngo; Ying He; Beeshanga Jayawickrama; Eryk Dutkiewicz. Multi-Agent DDPG-Based Joint Beam Hopping and Resource Allocation for Cognitive GEO-LEO Satellite Networks〔认知GEO–LEO卫星网络中基于多智能体DDPG的联合跳波束与资源分配〕. IEEE Networking Letters, 2025, 7(4): 303-307. DOI: 10.1109/LNET.2025.3605531. [来源](https://doi.org/10.1109/LNET.2025.3605531) 本文所据UTS机构作者全文：[正文](https://opus.lib.uts.edu.au/bitstream/10453/189674/3/Multi-Agent%20DDPG-Based%20Joint%20Beam%20Hopping%20and%20Resource%20Allocation%20for%20Cognitive%20GEO-LEO%20Satellite%20Networks.pdf)。

62. Ju-Hyung Lee; Chanyoung Park; Soohyun Park; Andreas F. Molisch. Handover Protocol Learning for LEO Satellite Networks: Access Delay and Collision Minimization〔低轨卫星网络的切换协议学习：接入时延与碰撞最小化〕. IEEE Transactions on Wireless Communications, 2024, 23(7): 7624-7637. DOI: 10.1109/TWC.2023.3342975. [来源](https://doi.org/10.1109/TWC.2023.3342975)

63. Nitinder Mohan; Andrew E. Ferguson; Hendrik Cech; et al. A Multifaceted Look at Starlink Performance〔Starlink性能的多维观察〕. Proceedings of the ACM Web Conference 2024: 2723–2734. DOI: 10.1145/3589334.3645328. [来源](https://doi.org/10.1145/3589334.3645328)

64. Mark Handley. Using ground relays for low-latency wide-area routing in megaconstellations〔利用地面中继实现巨型星座低时延广域路由〕. Proceedings of the 18th ACM Workshop on Hot Topics in Networks, 2019: 125-132. DOI: 10.1145/3365609.3365859. [来源](https://doi.org/10.1145/3365609.3365859) 本文所据UCL接受稿：[正文](https://discovery.ucl.ac.uk/id/eprint/10090242/1/hotnets-ucl.pdf)。

65. Hefan Zhang; Zhiyuan Wang; Shan Zhang; Qingkai Meng; Hongbin Luo. Link-identified Routing Architecture in Space〔面向空间网络的链路标识路由架构〕. IEEE Transactions on Network Science and Engineering, 2025, 12(1): 392-408. DOI: 10.1109/TNSE.2024.3498042. [来源](https://doi.org/10.1109/TNSE.2024.3498042) 本文所据作者预印本：arXiv:2411.10926v1；DOI: 10.48550/arXiv.2411.10926。[正文](https://arxiv.org/pdf/2411.10926v1)。

66. Liang Gou; Dongming Bian; Yulei Nie; et al. Hierarchical Resource Management for Mega-LEO Satellite Constellation〔低轨巨型卫星星座的分层资源管理〕. Sensors, 2025, 25(3): 902. DOI: 10.3390/s25030902. [来源](https://doi.org/10.3390/s25030902)

67. Elad Denenberg. Satellite closest approach calculation through Chebyshev Proxy Polynomials〔采用切比雪夫代理多项式计算卫星最近接近事件〕. Acta Astronautica, 2020, 170: 55–65. DOI: 10.1016/j.actaastro.2020.01.020. [来源](https://doi.org/10.1016/j.actaastro.2020.01.020)

68. Phasawee Saingyen; Sittiporn Channumsin; Suwat Sreesawet; et al. Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques〔接近筛选方法性能研究及基于 CUDA 的接近评估计算加速〕. Aerospace, 2023, 10(6): 543. DOI: 10.3390/aerospace10060543. [来源](https://doi.org/10.3390/aerospace10060543)

69. Thomas Uriot; Dario Izzo; Luís F. Simões; et al. Spacecraft collision avoidance challenge: Design and results of a machine learning competition〔航天器碰撞规避挑战赛：机器学习竞赛的设计与结果〕. Astrodynamics, 2021, 6(2): 121–140. DOI: 10.1007/s42064-021-0101-5. [来源](https://doi.org/10.1007/s42064-021-0101-5)

70. Zeno Pavanello; Luigi De Maria; Andrea De Vittori; et al. CAMmary: A review of spacecraft collision avoidance manoeuvre design methods〔CAMmary：航天器碰撞规避机动设计方法综述〕. Acta Astronautica, 2025, 236: 770–789. DOI: 10.1016/j.actaastro.2025.07.027. [来源](https://doi.org/10.1016/j.actaastro.2025.07.027)

71. Simon Burgis; Lukas Rohrmüller; Martin Michel; et al. Simulation of satellites and constellations for the assessment of collision avoidance operations〔用于评估碰撞规避运行的卫星与星座仿真〕. CEAS Space Journal, 2023, 15(5): 655–670. DOI: 10.1007/s12567-022-00471-y. [来源](https://doi.org/10.1007/s12567-022-00471-y)

72. Consultative Committee for Space Data Systems. Conjunction Data Message〔交会数据消息〕. CCSDS 508.0-B-1, June 2013; Technical Corrigendum 2, October 2021; accessed 10 October 2026 (inherited access date). https://ccsds.org/publications/bluebooks/entry/3064/. [来源](https://ccsds.org/publications/bluebooks/entry/3064/)

73. SpaceX. Starlink Collision Avoidance CONOPS〔Starlink碰撞规避运行概念〕. Official operational documentation; accessed 10 October 2026 (inherited access date). https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/. [来源](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/)

74. Ping Lu; Xinfu Liu. Autonomous Trajectory Planning for Rendezvous and Proximity Operations by Conic Optimization〔采用锥优化的交会与近距离操作自主轨迹规划〕. Journal of Guidance, Control, and Dynamics, 2013, 36(2): 375–389. DOI: 10.2514/1.58436. [来源](https://doi.org/10.2514/1.58436)

75. Daniel Morgan; Soon-Jo Chung; Fred Y. Hadaegh. Model Predictive Control of Swarms of Spacecraft Using Sequential Convex Programming〔采用序贯凸规划的航天器群模型预测控制〕. Journal of Guidance, Control, and Dynamics, 2014, 37(6): 1725–1740. DOI: 10.2514/1.G000218. [来源](https://doi.org/10.2514/1.G000218)

76. Francisco Gavilan; Rafael Vazquez; Eduardo F. Camacho. Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation〔结合扰动估计的航天器交会机会约束模型预测控制〕. Control Engineering Practice, 2012, 20(2): 111–122. DOI: 10.1016/j.conengprac.2011.09.006. [来源](https://doi.org/10.1016/j.conengprac.2011.09.006)

77. Purnanand Elango; Abraham P. Vinod; Kenji Kitamura; et al. Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit〔近直线晕轨道被动安全交会的连续时间逐次凸化〕. AIAA SCITECH 2026 Forum, 2026. DOI: 10.2514/6.2026-2446. [来源](https://doi.org/10.2514/6.2026-2446)

78. Mark Stephenson; Hanspeter Schaub. Two Approaches to Autonomous Spacecraft Inspection: Shielded Reinforcement Learning versus Probabilistic Roadmaps〔自主航天器巡检的两种方法：带安全屏蔽的强化学习与概率路线图〕. The Journal of the Astronautical Sciences, 2026, 73: 89. DOI: 10.1007/s40295-026-00631-w. [来源](https://doi.org/10.1007/s40295-026-00631-w)

79. Astroscale. Astroscale’s ADRAS-J Achieves Historic 15-Meter Approach to Space Debris〔Astroscale的ADRAS-J完成距空间碎片15米的接近〕. Official mission release; accessed 10 October 2026 (inherited access date). https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris. [来源](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris)

80. Kyle Hundman; Valentino Constantinou; Christopher Laporte; et al. Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding〔利用LSTM与非参数动态阈值检测航天器异常〕. Proceedings of ACM SIGKDD, 2018: 387–395. DOI: 10.1145/3219819.3219845. [来源](https://doi.org/10.1145/3219819.3219845)

81. Lars Herrmann; Marie Bieber; Wim J. C. Verhagen; et al. Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry〔揭示性能高估：航天器遥测深度异常检测的重新评估〕. CEAS Space Journal, 2024, 16(2): 225–237. DOI: 10.1007/s12567-023-00529-5. [来源](https://doi.org/10.1007/s12567-023-00529-5)

82. Sascha Wanninger. Knowledge-based satellite failure detection, isolation and recovery (FDIR)〔基于知识的卫星故障检测、隔离与恢复（FDIR）〕. CEAS Space Journal, 2026, 18(5): 991–1004. DOI: 10.1007/s12567-025-00651-6. [来源](https://doi.org/10.1007/s12567-025-00651-6)

83. Nicola Muscettola; P. Pandurang Nayak; Barney Pell; et al. Remote Agent: to boldly go where no AI system has gone before〔Remote Agent：大胆迈向此前AI系统未曾涉足的领域〕. Artificial Intelligence, 1998, 103(1–2): 5–47. DOI: 10.1016/S0004-3702(98)00068-X. [来源](https://doi.org/10.1016/S0004-3702(98)00068-X)

84. Kathiravan Thangavel; Roberto Sabatini; Alessandro Gardi; et al. Artificial Intelligence for Trusted Autonomous Satellite Operations〔面向可信自主卫星运行的人工智能〕. Progress in Aerospace Sciences, 2024, 144: 100960. DOI: 10.1016/j.paerosci.2023.100960. [来源](https://doi.org/10.1016/j.paerosci.2023.100960)

85. Changyuan He; Yunfeng Dong; Hongjue Li; et al. Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling〔考虑多子系统耦合的敏捷对地观测卫星推理式调度方法〕. Remote Sensing, 2023, 15(6): 1577. DOI: 10.3390/rs15061577. [来源](https://doi.org/10.3390/rs15061577)

86. NASA Jet Propulsion Laboratory. IPEX〔智能载荷实验任务〕. Official project documentation; accessed 10 October 2026 (inherited access date). https://ai.jpl.nasa.gov/public/projects/ipex/. [来源](https://ai.jpl.nasa.gov/public/projects/ipex/)

87. Gregg Rabideau; Daniel Tran; Steve Chien; et al. Mission Operations of Earth Observing-1 with Onboard Autonomy〔具有星上自主能力的 Earth Observing-1 任务运行〕. SMC-IT, 2006: 367–373. DOI: 10.1109/SMC-IT.2006.48. [来源](https://doi.org/10.1109/SMC-IT.2006.48)

88. NASA Goddard Space Flight Center. Core Flight System – Demo Bundle〔核心飞行系统演示包〕. Official software repository; accessed 10 October 2026 (inherited access date). https://github.com/nasa/cFS. [来源](https://github.com/nasa/cFS)

89. Francesco Basciani; Arianna Fedeli; Daniele Masti; et al. A model-driven framework for supervised reconfiguration of satellite schedulers〔卫星调度器受监督重配置的模型驱动框架〕. Software and Systems Modeling, 2026. DOI: 10.1007/s10270-026-01426-1. [来源](https://doi.org/10.1007/s10270-026-01426-1)

90. NASA. What is Starling?〔Starling任务介绍〕. Official mission documentation; accessed 10 October 2026 (inherited access date). https://www.nasa.gov/smallspacecraft/what-is-starling/. [来源](https://www.nasa.gov/smallspacecraft/what-is-starling/)

91. NASA. NASA Starling and SpaceX Starlink Improve Space Traffic Coordination〔NASA Starling与SpaceX Starlink改进空间交通协调〕. Official mission release; accessed 10 October 2026 (inherited access date). https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/. [来源](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/)

92. Patrick W. Kenneally; Scott Piggott; Hanspeter Schaub. Basilisk: A Flexible, Scalable and Modular Astrodynamics Simulation Framework〔Basilisk：灵活、可扩展且模块化的航天动力学仿真框架〕. Journal of Aerospace Information Systems, 2020, 17(9): 496–507. DOI: 10.2514/1.I010762. [来源](https://doi.org/10.2514/1.I010762)

93. Steve A. Chien. Formal Methods for Trusted Space Autonomy: Boon or Bane?〔可信空间自主系统的形式化方法：助力还是阻碍？〕. NASA Formal Methods, Lecture Notes in Computer Science, 2022: 3–13. DOI: 10.1007/978-3-031-06773-0_1. [来源](https://doi.org/10.1007/978-3-031-06773-0_1)

94. Philipp Chrszon; Paulina Maurer; George Saleip; et al. Model checking of spacecraft operational designs: a scalability analysis〔航天器运行设计的模型检测：可扩展性分析〕. Software and Systems Modeling, 2025, 24(6): 1825–1846. DOI: 10.1007/s10270-025-01281-6. [来源](https://doi.org/10.1007/s10270-025-01281-6)
