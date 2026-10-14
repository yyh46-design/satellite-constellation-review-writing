# 大型卫星星座智能管理与调度研究综述：典型业务、技术路线与运行实践

Intelligent Management and Scheduling of Large Satellite Constellations: Application Scenarios, Technical Approaches, and Operational Practice

**v1.9 · 2026-10-14 · 中文作者审阅稿；全文英文尚未同步；作者终核待完成**

## 摘要

大型卫星星座需要在可用能力、时变业务需求和执行状态之间持续协调。本文采用问题导向的叙述性综述，以对地观测和通信为核心业务，比较构型维护、任务规划、网络资源配置、安全执行与异常恢复的代表研究。比较以决策变量、可获得的信息、可修改的活动及业务完成条件为依据，区分联合选择、顺序安排和运行反馈，并追踪预处理、求解、协调和配置生效的成本。进一步的文献对照表明，即使研究均称为“观测—下传联合调度”，其目标也可能分别计量成功调度的请求加权值或观测收益与下传数据量的组合；计算简化还可能改变可搜索的解集合。由此，本文归纳判断决策范围的三个条件：后续瓶颈是否改变当前选择、相关信息能否及时获得，以及调整能否在机会到期前生效。已有实例说明局部化、计划复用与学习辅助的收益依赖任务竞争、训练或预处理成本及资源承诺；运营接口和飞行案例则界定了任务完成、状态反馈及异常处置的实际事件。本文据此提出可检验的跨业务比较问题，强调在共同业务结果与证据范围内评价方法，而非对异构算例统一排名。

**关键词：** 大型卫星星座；任务调度；通信资源管理；在轨服务；运行反馈；自主运行

## Abstract

Sustained operation of large satellite constellations requires coordinating available capabilities, evolving service demand, and execution states. This problem-driven narrative review examines Earth observation and communications alongside constellation maintenance, mission scheduling, network resource allocation, safe execution, and recovery. Representative studies are compared by their decision variables, available information, revisable activities, and service-completion criteria, with explicit attention to preprocessing, optimization, coordination, and enactment costs. A closer comparison reveals that studies labeled as integrated observation–downlink scheduling may optimize different outcomes, including the weighted value of successfully scheduled requests or a combination of observation profit and downloaded data volume. Computational simplifications may also restrict the feasible search space. The review consequently develops three qualitative considerations for choosing a decision scope: whether downstream bottlenecks change current choices, whether relevant information arrives in time, and whether revisions can take effect before opportunities expire. Findings on local coordination, plan reuse, learning assistance, operational interfaces, and flight demonstrations are interpreted within their specific task and validation conditions. This synthesis identifies testable comparisons across services without assuming common performance rankings for heterogeneous models.

## 1 引言

### 1.1 从活动安排到持续服务

大型星座将大量成员、重复出现的服务机会与持续到达的需求组织在同一运行过程中。卫星数量增加能够提供更多候选观测窗口或接入对象，也会扩大任务竞争、状态交换和计划修改的范围。已有自动化运行综述将可扩展性与运行组织列为重要问题[1]。因此，管理与调度的研究对象不能仅由“分配了多少任务”描述，还需要说明这些任务利用了哪些能力、在什么条件下完成，以及计划失效后如何恢复。

对地观测与通信体现了两种不同的服务过程。观测请求通常经由目标选择、成像、处理与交付形成离散完成事件；通信业务则依赖接入、波束、功率、频谱与路径的持续配置。两者均面对时变机会和有限资源，但观测数量、交付时延、通信吞吐与中断不能互相替代。维护和在轨服务研究进一步说明，可用能力本身也需要通过备份、补给、维修及资源转移维持[2]。本文将这些活动视为业务运行的支撑，而不将星座管理简化为某一种优化算法或单星自主软件。

### 1.2 已有综述与本文贡献

已有综述从不同问题域梳理了星座管理的技术基础。Wang等[3]按模型、约束和求解方式整理敏捷观测调度；Ferrari等[4]将成像、通信及集成调度置于对地和外层空间观测任务中，其通信活动主要服务于数据获取与交付。Jabbarpour等[5]以智能体及协调方式组织分布式空间系统研究，Ben-Larbi等[1][6]则从运行职责、自动化模式和工具分析规模增长带来的变化。两篇中文通信综述的公开摘要[7][8]覆盖智能组网及资源管控，提供面向持续用户流量的研究视角。上述文献的分类对象分别是任务、协调主体、运行组织或网络资源，因而适合解释不同层面的问题。

本文以服务过程而非算法名称为比较起点。卫星运行与网络管理的集成研究[9]已经讨论平台资源和业务需求的共同安排；本文在观测、通信和能力维护的代表模型之间进一步完成三项工作：首先，识别不同研究究竟奖励“已观测”“已下传的数据量”“按期完成的请求”还是持续服务质量，防止相似术语掩盖不同优化目标；其次，比较下游约束在何时进入上游选择，区分同次求解、顺序传递和事后反馈保留的可修改范围；最后，将候选构造、求解、信息交换与执行生效的负担放回具体任务和验证环境，解释方法可扩展性的条件。第3章逐项讨论代表研究，第4章在此基础上提出可供后续共同算例检验的条件性认识，表1概括与既有综述的衔接。

**表1 已有综述的组织视角与本文的比较重点**

| 文献 | 主要组织视角 | 本文进一步比较的内容 |
| --- | --- | --- |
| 观测调度综述[3][4] | 任务模型、资源约束、方法及集成调度 | 采集、处理、交付的完成条件及下游资源作用 |
| 智能体综述[5] | 协调主体、架构与任务管理 | 共享内容、消息时机和局部决策权限 |
| 自动化运行综述[1][6] | 运行模式、职责及工具 | 算法结果、配置生效和运行状态的对应 |
| 通信管理综述[7][8] | 公开摘要所列组网与资源管控方向 | 与观测下传业务区分，比较持续用户流量的资源需求 |
| SatOps—NetOps综述与框架[9] | 平台和网络的交互模式及实现 | 共同模型、顺序输入与反馈的决策范围及代价 |

### 1.3 研究范围与综述方法

本文采用问题导向的叙述性综述，以已有主题检索、代表论文追溯及通信管理专题补充组织文献，侧重模型、方法和适用条件的比较，不作穷尽性文献频率估计或跨论文性能元分析。对地观测和通信是主要业务，在轨服务及安全恢复按其管理功能纳入；单星、GEO、深空和通用多智能体研究提供相关方法参照，并保留原任务域。“大型”指成员、候选活动或协调规模对求解产生实质影响，不采用统一数量阈值。“智能管理”涵盖依据状态和目标进行规划优化、规则推理、协调与学习的决策方法。

文献比较提取任务对象、可选变量、资源与信息条件、更新过程、结果指标和验证环境。模型结果按实际场景和对照解释，作者稿在相关研究处注明；公开摘要仅用于研究方向概述。原研究结论、原作者解释与本文跨研究归纳分别表述，图表中的分类和条件判断不作为新增实验结果。各来源的实际阅读版本、命题定位和核查状态单独记录，本文的叙述性选录也不用于判断未覆盖领域的研究是否存在。

## 2 管理对象与比较基础

### 2.1 业务过程与支撑能力

星座管理同时具有业务属性和支撑功能属性。对地观测围绕请求、候选窗口及信息产品组织活动，通信业务围绕用户流量及持续连接分配资源。构型、备份和维护决定可用成员及能力的时间与空间分布，安全执行与恢复又依据事件更新这些条件。图1据此组织业务过程和共用管理功能；其中的箭头表示输入或状态更新，各功能在具体研究中仍可分别求解。

![图1](../figures/fig1_zh.svg)

图1 业务过程与管理职责的交叉组织。实线表示资源或任务输入，回线表示运行状态更新；两类业务的完成条件不同。此图为本文综合绘制，不代表某一已验证系统架构。

### 2.2 决策时域与资源承诺

长期配置决定资产数量、位置和未来能力，业务调度利用这些条件选择活动，执行与恢复更新已完成的动作及剩余资源。除时间尺度外，三者还由决策可以修改的范围区分：某些轨道、请求和资源安排已经固定，另一些仍可重新分配。本文以“资源承诺”概括计划确认后对后续选择的约束，但保留两类不同来源：AWS Ground Station的预约及变更属于公开业务规则[52]；接触图调度中扣减已用容量并保留早先安排属于特定算法假设[106]。二者可以用于比较计划修改的自由度，却并不代表相同的实际执行协议。

### 2.3 决策权限与信息结构

集中、分层和分布式描述信息汇集及决策权限的组织方式；主问题—子问题分解描述求解过程；集中训练与分散执行描述学习系统的两个阶段。这些分类可以同时出现在同一方法中，但不能相互替代。动态管理拓扑研究[10]关注成员组织及其演化，观测协调研究[34][35]则关注成员如何识别任务竞争。因此，可扩展性既取决于问题被如何划分，也取决于每个决策者实际获得的状态、需要交换的消息以及冲突消解所需的时间。

### 2.4 完成条件、约束与评价量

约束决定可行活动的范围，目标函数决定模型奖励什么。尤其在观测数据链中，“完成采集”“形成合格产品”“完成下传”以及“增加下传字节数”不能互换：两种联合观测—传输研究[42][44]即采用不同的奖励构造。通信星座的吞吐、时延与业务中断也有不同统计对象。表2据此将决策自由度与可观察结果并列；比较技术效果时，必须先核对目标函数、统计分母和任务完成事件，再讨论算法收益。

**表2 业务对象、决策范围及比较边界**

| 对象 | 典型可选量 | 结果与必须保留的边界 |
| --- | --- | --- |
| 观测请求 | 目标、卫星、窗口、次序 | 采集、质量满足和交付分别计量；重复观测是否有价值需由请求定义 |
| 数据处理与传输 | 处理节点、负载、频率、下传或路径 | 已给定采集负载与可反向调整采集不同；星地处理集合须明确 |
| 通信业务 | 关联、波束、功率、频谱、路径 | 吞吐、时延、抖动及中断具有不同分母；保留负载与建链前提 |
| 能力维持 | 备份、补给、服务设施及维修行动 | 库存满足、资产到位和业务恢复不是同一完成事件 |
| 安全与恢复 | 筛查、跟踪、机动、诊断、计划修复 | 风险估计不等于动作完成；安全退出不等于原任务完成 |

### 2.5 可扩展性与验证对象

模型规模由卫星、请求、候选窗口、资源类型和冲突范围共同决定。方法成本则可分为候选生成与预处理、优化求解、成员协调和配置生效等部分，学习方法还涉及训练投入。结果解释须与这些计时对象一致。本文分别考察模型仿真、软件或硬件测试、运行接口、独立测量和飞行案例；每类材料支持其实际观察或验证的对象，跨业务比较主要围绕机制和条件展开。

## 3 大型星座管理与调度的主要技术路线

本节按能力形成、业务安排和执行恢复组织代表研究。观测与通信分别展开，以比较各自的决策对象、求解方法及资源限制；在轨服务分别纳入维护能力与访问调度。第3.5节进一步比较不同研究如何将一个环节的结果送入另一环节，为第4章的跨研究归纳提供具体依据。

### 3.1 长期能力配置与持续运维

#### 3.1.1 从几何覆盖到可部署能力

构型研究的基本问题是将轨道几何转化为满足需求的活动机会，但目标构型是否给定决定了优化范围。Appel等[11]在终端构型确定后选择重构机动，Lee和Ho[12]把区域构型和卫星分配共同作为决策，多阶段重构[13]进一步连接预先给定的阶段需求及阶段间转移。因此，三类模型依次增加的是目标状态或时段之间的选择空间，而不是在相同问题上简单更换求解器。覆盖模式优化[14]利用访问模式和星座模式的结构，不确定关注区域下的部署[15]则以需求情景评价方案；前者细化覆盖的组合表示，后者改变方案面对的需求集合。

部署条件把覆盖目标进一步限制为能够按时形成的能力。Gwon和Ahn[16]将停泊时间、J₂引起的升交点赤经漂移、发射容量和完成窗口纳入两阶段设计，其可达性筛选服务于部署方案选择，完整发射与到位轨迹属于更细层面的描述。通信平台与星座联合设计[17]则同时考虑天线、波束和平台参数，使覆盖要求与服务容量共同影响星座规模。两者分别突出能力到位时间和单位资产的服务能力：相同覆盖几何可能对应不同部署等待，也可能对应不同地域流量下的容量瓶颈。构型比较由此需要同时说明提供什么能力、何时可用及支撑哪些业务。

#### 3.1.2 补给等待、库存保障与能力恢复

多级库存研究[18]的作者稿将地面、停泊轨道和轨道面内备星连接为补给系统，根据库存状态触发补货，并在停泊层至轨道面层的补给中计入漂移等待与转移飞行时间。与此同时，模型把轨道面内备星接替失效单元视为即时可用，省略了这一步可能存在的重新就位时间。这两个时间过程的区别决定了结果含义：该模型已描述补给等待，但库存供应得到满足仍不自动等同于故障后的业务恢复。

双供应通道研究[19]在经停泊轨道转移之外加入直接注入选择；马尔可夫链模型[20][21]则细化备星库存及补给途径在长期运行中的随机演化。这些研究分别扩展行动集合和状态表示。在轨服务集成维护[23]又将“制造并发射新星”与“服务恢复失效资产”放入维护策略，同时考虑星座运营方满足服务水平和降低维护成本的要求，以及服务提供方的定价和利润目标。其正式出版摘要报告的是给定成本、失效和可恢复比例条件下的双主体经济权衡，并不直接给出某次故障后交付请求恢复时间的实测结果。

Iridium于2023年发射5颗备星的公开资料[22]说明备用资产已用于实际能力配置，却不代表任何库存模型的最优策略得到飞行验证。综合上述研究，可以把失效后的运行过程区分为四个事件：可用备星或服务能力存在、资源到达目标轨道或服务位置、设备恢复任务能力、受影响业务重新分配。库存模型通常评价供应水平和平均成本，服务集成维护模型还纳入供应方定价；若要评价实际业务损失，就需要把这四个事件的时间与需求序列相联系。这一连接是本文提出的比较问题，并非现有文献已共同验证的结果。

#### 3.1.3 服务设施与运行需求的衔接

服务设施研究通过位置和客户分配确定维护行动的可达范围。离散轨道仓库选址[24]联合安排设施、客户及推进需求，连续轨道选址[25]增加位置自由度并与服务顺序交替求解；固定候选集合便于组合选择，连续位置则使转移代价与布局更紧密地耦合。服务船预部署[26]侧重潜在客户可达性，滚动服务与物流模型[27]侧重需求更新，高、低推力框架[28]将转移时间及推进代价带入排程，生命周期评估[29]区分随机与认知不确定性。它们细化的分别是空间布局、更新时机、行动代价与需求知识，不宜把不同场景的成本改善看成一条统一的性能进步曲线。

这些研究与日常调度的衔接点是带有地域、时间和资源属性的可用能力，而不只是备星或服务设施数量。构型描述活动机会，补给安排给出能力到位时刻，维护行动改变失效后的可用状态。将这些输出作为给定输入、滚动更新条件或共同决策变量，会形成不同的管理问题；第4章据此讨论恢复过程与业务损失如何建立可比较的联系。

### 3.2 对地观测与在轨服务任务规划调度

#### 3.2.1 任务选择、活动时序与跨星协调

敏捷观测必须把请求选择转化为满足姿态和可见时间窗的活动序列。早期研究[30]比较贪心、动态规划、约束规划和局部搜索；学习排序[31]和分解学习[32]主要改变候选生成与搜索顺序。能量感知分支定价[33]进一步处理公共任务、专属任务及电池约束，以结构化Dantzig–Wolfe分解和动态规划定价组织求解。与仅报告启发式计划值的方法相比，结构化数学规划能够在其离散模型内提供优化界，但这一界的意义受任务表示、电池模型和候选活动集合限定。不同方法的“可扩展”主要来自求解结构变化，不能据实例规模直接形成跨研究的速度排名。

分布式分配进一步受到共享信息的限制。Parjan和Chien[34]在100个代理、634个目标的一周算例中比较集中、广播和高度去中心化分配；在固定冲突间隔及简化容量条件下，增量规划减少计算时间，同时增加重复观测。Zilberstein等[35]将问题表示为分布式约束优化，利用几何邻域分解和邻域随机搜索组织局部求解，在200星与108星、24 h模拟中同时评价任务满足、时间和消息量。前者比较共享规则与计划复用，后者利用任务竞争的局部结构。计算和消息节省均需要结合保留的重复或满足率差距理解，而不能仅以代理数量证明方法可扩展。

任务所属主体及通信机会改变协调的组织方式。多主体观测的分布式约束优化[36]减少私有请求预先集中汇集的需求；一致性任务包拍卖[37]提供局部竞价与冲突消解的通用方法，但其通用性质不等于已经验证具体星座中的执行条件。通信机会预测任务包方法[38]、延迟通信协同规划[39]及不确定环境下的合同网、黑板和滚动调度[40]分别处理消息可达性与状态变化。异步市场分配[41]从通用多智能体环境补充延迟和丢失问题。不同模型中的公共请求、私有能力、竞价和完成状态具有不同含义，通信连通并不自动提供消除任务冲突所需的全部信息。

#### 3.2.2 从采集安排到处理与交付

观测与下传同时占用时间、能源和地面通信资源，但“把两类活动联合建模”并不意味着优化同一种完成事件。He等[42]将敏捷观测窗口与传输窗口共同安排，在模型中以成功安排观测和传输的任务加权值为目标；方法将时间窗关联和窗内资源配置分层处理，结合半正定松弛与遗传搜索降低计算负担。其公开作者PDF中的传输假设无误码，并为可处理性忽略成像角度对图像质量的影响。这使模型能够讨论时间窗竞争和任务调度收益，却未直接评价产品质量或受链路误码影响的交付可靠性。

Rocha等[44]研究的集成敏捷观测模型则同时奖励目标观测收益和向地面站下传的数据量，并计入姿态切换、存储与能源动态。由于这两个奖励项并列，增加下传数据量并不自动表示增加了同样数量的完整交付请求。该研究的公开机构工作论文还提出一个可能缩小可行搜索空间的简化整数模型，并结合图结构缩减与基于混合整数规划的邻域启发式求解；这是计算可处理性与搜索范围之间的具体取舍。其2025年期刊出版摘要支持上述总体方向，但本文所核方法细节来自2024年机构工作论文，正式版逐项一致性仍应继续核对。

共享地面设施使“可通信”与“通信资源已分配”产生区别。单星—多站排程[46]、空军卫星控制网络[47]及下传案例[48]均涉及站点竞争；深空网络优化[49]与运营安排[50]说明请求协商和约束搜索的作用。两种业务接口进一步将完成事件落实为操作状态：Planet任务接口[51]区分采集、质量满足和交付，AWS Ground Station[52]对已经预约的窗口采用配置快照，变更已有安排需依照对应取消与重新预约流程。它们可以帮助评估模型能否刻画任务完成及承诺变更，却不是论文算法在商业系统上已经部署的证据。

Soret等[53]的公开作者稿在采集阶段按时间、姿态、能源和图像质量选择任务，再以已确定的负载和下传时刻配置边缘卫星及地面站处理负载与频率，并计入计算、通信能耗和容量限制。该过程以固定分发—处理—汇集流水线和稳定星间链路为前提，体现“上游顺序输入与下游局部联合”可以并存。与[42]或[44]在同一次任务安排中引入传输变量的思路相比，差异在于下游条件何时具有改变上游选择的权限，而不是研究是否使用了“联合”一词。

卸载与协同推理研究[54][55][56]主要决定计算位置、资源分配或任务推理方式；轨道感知计算调度[57]将可见性和轨道运动纳入执行机会，Kodan[58]则通过离线专用模型及运行时选择应对计算与下传瓶颈。这些方法可以为观测链提供处理能力，但其原始结果往往以计算完成、能耗或响应时间计量。只有在任务价值、处理完成和后续交付之间建立明确依赖时，计算层收益才能被解释为观测业务收益；“使用边缘计算”本身没有确定这种依赖。

#### 3.2.3 动态任务、不确定性与学习辅助

动态请求要求保留或修改已有承诺。分层混合整数规划[59]以拉格朗日分配处理任务冲突，并通过回溯与递归修复活动序列，在最多1000星、50—6000项任务的算例中研究收益与计算时间。与给定时域的分支定价[33]相比，其重点是事件到达后的分配与序列修复。云量不确定性则在生成计划时改变预期价值：主动机会约束调度[60]、预算不确定集下的鲁棒调度[61]及多阶段随机规划[62]分别采用概率、扰动集合和情景描述。三者的保守性取决于不确定性表达，不宜仅以同名收益指标排序；实际质量反馈触发的复采也不同于事前风险安排。

学习辅助调度的改进来源也需要按求解阶段拆分。Qi等[63]将滚动时域内的应急任务安排转为一系列静态子问题，使用解码方式把学习动作组织为任务次序选择与资源选择，再以针对问题设计的破坏—修复算子继续改进初解。因而，其最终计划质量不能仅归因于强化学习网络：搜索算子、约束检查和滚动重算同样影响结果。滚动时域多智能体学习[64]则侧重集中训练、分散执行时的成员协同。前者改善初解与搜索过程，后者组织在线策略权限；仅比较网络推理耗时，不足以比较完整调度响应。

单星策略复用[65]先训练一个成员，再在Walker星座中复用，并比较自由通信、单跳、多跳及无通信设置。共享已成像和已下传状态有助于避免重复完成，但不提供未来计划意图，因此自由通信下仍可能出现同一决策时段的重复选择。Basilisk环境中的单星算法比较[66]进一步显示，策略、资源屏蔽和搜索训练在收益、稳定性及训练成本上具有不同表现。单星训练的简化、快速动作生成和跨星一致分配是三个不同目标，不能由其中一个的改进推断另外两个同时实现。

#### 3.2.4 在轨服务的访问、转移与补给

在轨服务也包含选择、分配和排序，但候选活动由轨道转移而非单纯可见窗口形成。可加注多轨服务[67]通过时变网络联合访问与补给；不确定服务时长下的GEO加注[68]在访问安排中纳入鲁棒性；多服务星规划[69]连接任务选择和转移，混合加注与碎片移除[70]比较随机与鲁棒表达。改变访问次序会改变时刻、质量及后续可达集合，因此固定边权的组合排程只有在代价近似适用时才能代表原任务。

低推力轨迹预计算把连续求解成本转移到代价构造阶段。Apa等[72]在出发与到达轨道、质量和时刻上建立转移网格，再以插值支持多客户搜索，模型考虑摄动、地影与质量变化，但忽略相位机动成本。后续低轨漂移服务[71]联合推力—漂移—推力转移、访问和加注，相位影响在主优化后单独估计。这类方法使组合搜索能够利用状态相关代价，同时留下预计算网格、插值误差及未纳入终端条件的适用边界。观测调度中的窗口预处理与服务任务中的轨迹预计算均减少在线搜索负担，却不能省略对候选活动生成过程的说明。

**表3 观测与服务调度的决策组织及适用条件**

| 代表方法 | 决策与信息组织 | 比较时需要保留的条件 |
| --- | --- | --- |
| 分支定价[33] | 公共/专属任务与电池；结构化列生成和定价 | 离散模型优化界及定价成本；原文为出版摘要/引言级核对 |
| 增量与几何邻域[34][35] | 复用计划或按任务竞争邻域交换信息 | 计算/消息减少与冗余、满足率共同评价 |
| 任务包与异步协调[37][38][41] | 局部竞价、共识、消息机会及延迟 | 通用多主体环境与实际星载网络条件不同 |
| 观测—传输联合[42] | 成功调度请求的加权收益；分层时间窗优化 | 作者公开稿；传输无误码、未建模视角造成的图像质量变化 |
| 敏捷观测—下传集成[44] | 观测目标收益与下传数据量并列；图结构/整数规划 | 机构工作稿；简化模型可能缩小可行域；正式版细节待对照 |
| 观测—处理顺序配置[53] | 采集先定，下游优化星地处理负载与频率 | 作者稿、稳定ISL和固定流水线；下游不反向修改采集 |
| 动态与学习辅助修复[59][63] | 分配/排序修复；学习解码初解再破坏—修复 | 计算总时与最终可行计划；[63]仅摘要/公开片段补核 |
| 单星策略复用[65][66] | 单星训练、不同成员共享完成状态 | 训练成本与协调信息分别评价 |
| 多客户在轨服务[67][68][71][72] | 访问、补给及质量/时刻相关轨迹代价 | 推进动力学、相位和不确定性范围需区分 |

### 3.3 通信星座网络管理与资源调度

#### 3.3.1 需求估计与波束、功率配置

通信资源管理包括需求估计和实际配置两个相邻环节。Han等[73]结合经验模态分解（EMD）、自回归积分滑动平均（ARIMA）和改进灰狼优化的反向传播神经网络（IGWO-BPNN），在ON/OFF合成自相似流量上评价预测误差；路由应用在该文中列为后续工作。波束跳变则直接决定有限波束何时照射哪些区域，功率配置进一步改变可提供的服务容量。预测结果可以成为资源配置的输入，但预测误差与实际业务吞吐对应不同输出，后续调度如何使用预测是连接二者的必要环节。

单星波束—功率研究[74]的公开作者稿先在平均功率条件下用潜在博弈选束，再固定照射选择，以罚函数内点法优化连续功率。单星、8波束及61个候选位置的算例采用供需平方差衡量匹配。G-BH与G-BHPO采用相同贪心选束规则、不同功率处理，因此可比较功率配置对供需匹配的作用，但队列演化可能改变后续照射选择，不能将其改写为全时域严格固定照射序列的消融。该文的分解方案也不意味着已经求得全部离散与连续变量的全局联合最优。

多星重叠覆盖在单星资源配置之外引入服务关联与共存问题。Lin等[75]的公开摘要将卫星—小区关联及照射模式作为两个子问题，研究负载平衡和非地球同步轨道（NGSO）系统与地球同步轨道（GSO）系统的共存。Zhao等[76]的公开作者稿则采用数字孪生与多智能体学习组织需求感知配置，其12星、每星4波束、168小区模型显式处理队列、服务关联及功率。前一研究在本文中用于说明共存场景，后一研究用于分析有模型依据的负载及策略比较；两者体现的跨星协调职责有所不同。

负载水平还决定增加资源自由度的作用。Zhao等[76]作者稿中的FPA采用需求驱动选束与均分功率，DPA在数字孪生内联合选束和离散功率；给定算例中总需求为8—20 Gbit/s时吞吐接近，超过20 Gbit/s后DPA较高。这是两种整体配置在不同负载下的比较，不是只改变功率模块的因果消融。结合[74]可见，资源配置的价值取决于哪一约束成为瓶颈，以及比较方案还改变了哪些决策。增加联合变量能够扩大可调范围，但其额外计算和信息需求也应与服务变化一并分析。

#### 3.3.2 接入切换与连接保持期间的服务变化

接入选择可从即时链路质量扩展到端到端路径。Yin等[77]的公开摘要将传播时延估计纳入单层学习切换，并结合跨层时延抖动和切换开销。其研究方向表明，切换评价可以同时考虑接入之后的网络代价。对于持续服务，当前连接质量、预期保持时间和后续路径质量代表不同取舍；本文据此讨论接入与路由的联系，而不对这些模块分别给出性能归因。

服务波动也不总由更换卫星引起。Mohan等[78]的正式WWW 2024论文通过多国测量和受控终端，观察到15秒重配置边界附近的时延与吞吐变化；在英国终端限制视场、仅有一颗候选卫星的连接窗口中，波动仍然存在。这支持“卫星切换不是这些变化的必要条件”，并不直接揭示内部资源分配算法。周期性网络调度是原作者的解释。该测量因此补充了算法模型中常被合并的两种状态：服务对象保持不变，与业务性能保持稳定并非同一事件。

#### 3.3.3 路由、流量工程与更新成本

网络的可用连接决定了路由问题的结构。Zhang和Yeung[79]的公开摘要面向无直接星间链路的低轨网络，以两层组织讨论路径时延与稳定性；Zhang等[80]进一步研究地面中继条件下的分段路由、流量工程和故障恢复。这些工作围绕地面辅助转发组织路径与更新，区别于直接利用激光星间链路的模型。稳定性、流量分配与故障恢复分别对应正常拓扑演化、容量竞争和异常事件，因而需要采用与各自目标相符的评价量。

动态激光链路的建立时间使路径修改具有显式代价。Bhattacharjee等[121]的公开作者稿在1584星、600个1秒快照中比较瞬时最短路、路径保持及活动感知策略。模型采用统一建链时延，假设控制器提前计算并分发路径，并忽略排队与初始配置时延。较高建链代价下，保持或感知已有活动链路能够减少更新损失；较低代价下，部分保持策略ILPR、ALPR的平均时延略高于瞬时最短路，而ISASR在低代价算例中仍可更优。因此，不能把某些保持策略的反例泛化为全部活动感知方法的失败。

上述路线体现了不同的更新代价：地面辅助研究从路由组织与故障恢复出发，动态激光链路模型将建立新连接的时间直接写入路径评价。后者在预先完成控制计算和分发、忽略队列的条件下，能够解释路径寿命与建链时间的取舍；加入排队、状态传递和配置时延后，还会出现其他业务代价。路径搜索的计算时间因而需要与链路实际生效时间分开计量。

#### 3.3.4 分层资源管理与控制职责

分层资源管理[81]的正式归档正文将网络控制中心、空间基站和用户终端配置为不同职责层级，以全局服务区域和频谱配置约束局部波束、时隙及信道安排，并通过需求与价格交换协调资源。其频谱管理、用户调度和波束调度实验对应不同组件及负载，不能将各自收益相加成为完整架构的统一增益。与[121]提前分发路径的假设相比较，分层不仅是计算任务的划分，还规定谁能改变资源、依据哪些信息行动，以及配置何时对局部算法有效。

**表4 通信管理研究的决策对象与模型条件**

| 研究 | 决策或观察对象 | 结果的适用条件 |
| --- | --- | --- |
| 流量预测[73] | EMD—ARIMA—IGWO-BPNN预测需求 | ON/OFF合成自相似流量；评价预测，路由应用为后续工作 |
| 波束—功率[74] | 作者稿：先选束，再配置连续功率 | 单星8束61位置；功率对照采用相同选束规则 |
| GSO共存[75] | 摘要所述关联及照射两个子问题 | 用于定位负载平衡与共存问题 |
| 需求感知配置[76] | 作者稿：多星选束、星内功率和队列 | 12星168小区；FPA/DPA为整体策略比较，趋势随负载变化 |
| 路由代价切换[77] | 摘要所述端到端代价参与接入评价 | 用于定位接入与后续路径的联系 |
| 独立测量[78] | 终端时延及吞吐变化 | 单候选卫星窗口；周期调度是原作者解释 |
| 地面辅助路由[79][80] | 摘要所述分层路由、流量工程与恢复 | 无直接星间链路；按研究目标比较，不引入量化排名 |
| 激光链路路由[121] | 作者稿：路径寿命与建链时延 | 1584星600快照；统一建链代价，无队列，提前计算及分发 |
| 分层资源管理[81] | 全局频谱配置与局部资源响应 | 需求/价格交换；各组件按对应负载和对照解释 |

### 3.4 安全执行、异常恢复与服务韧性

#### 3.4.1 风险信息与处置决策

安全管理首先将潜在接近转化为可供决策使用的信息。Chebyshev代理多项式[82]以分段近似和距离极值搜索处理候选配对的最近接近计算；筛查与CUDA研究[84]则同时考察配对压缩和并行实现，所测目录中不同筛查方法存在不同遗漏表现。前者主要减少单个候选的计算负担，后者影响进入精算的候选数量及执行时间。风险感知传感器调度[83]进一步根据碰撞风险与信息增益安排跟踪，作用于风险输入的质量。三类方法分别改变精算成本、配对集合和信息获取，合并使用时应保持这些职责的区分。

接近报文上的学习竞赛[87]评价后续风险预测，机动设计综述[86]比较可选规避动作，碰撞规避运行仿真[85]分析行动主体和时机。CCSDS接近事件报文[88]规范跨组织信息，Starlink公开流程[89]连接星历更新、持续筛查、星上重估及机动新增、修改或取消。风险信息由此不仅服务于一次动作选择，还会持续改变既有安排。对观测和通信而言，安全处置的影响需要通过实际机动时段、资源占用及恢复后的活动机会传递到业务层，而不是直接由某个风险数值替代。

#### 3.4.2 轨迹约束、安全干预与任务代价

轨迹规划将任务安排转换为受动力学约束的行动。被动安全轨迹[90]从相对运动几何约束无控制阶段的安全，锥优化交会[91]利用优化结构求解可行动作，序贯凸规划的模型预测控制[92]通过状态反馈更新轨迹。机会约束交会[93]进一步在扰动分布下处理视线等约束，非合作视觉交会[94]加入图像反馈与姿轨耦合，近直线晕轨道研究[95]则处理相应动力学中的连续时间被动安全。这些路线增加的是安全要求的表达和状态更新方式；它们的结论分别以原任务域、动力学近似、时间范围及扰动假设为条件。

Stephenson和Schaub[96]的巡检研究包含两组不同对照：一组比较同一强化学习策略启用与不启用安全屏蔽后的结果；另一组将未屏蔽策略与概率路线图（PRM）比较燃料—时间表现。后一组均值采用PRM的20个种子与学习策略的1000个种子，因而与屏蔽开关实验具有不同解释对象。屏蔽除改变动作外还引入更严格的被动安全要求，性能变化不能全部归因于求解器本身。

该研究将PRM定位为离线规划路线，但仿真执行每次机动时仍按当前真实状态重解至下一航路点的两点边值问题[96]。因此，预先固定任务级路径与执行层完全不校正并非同义。比较的有效边界包括决策更新层级、安全要求及计时范围，而不仅是笼统的“开环—闭环”标签。

实际事件同样需要区分名义任务和安全目标。ADRAS-J于2024年11月30日在约15 m接近后触发自主中止与安全后撤[97]，说明异常状态能够改变原定活动进程。安全退出完成了保护航天器的目标，但并不对应原定接近或服务活动的正常完成。评价恢复策略时，安全结果和保留下来的任务能力应分别计量。

#### 3.4.3 从异常识别到计划恢复

异常检测、诊断和恢复对状态信息的要求逐步变化。LSTM预测误差与动态阈值[98]识别遥测偏差，贝叶斯不平衡数据模型[99]及验证门控持续学习[100]分别处理预测不确定性与模型更新；评价复核[101]说明样本、指标和后处理影响方法比较。知识规则FDIR[102]则用状态事实触发故障判别及恢复操作，在地面原型中连接检测与响应。前一类方法的直接输出是异常线索，后一类依赖可解释规则决定行动；两者之间仍需要诊断依据及执行条件，检测指标本身没有确定恢复成功率。

任务失败还会破坏活动时序和资源分配。Schedule Manager[103]依据窗口、优先级和冲突管理任务，失败时装载预定义应急计划，其验证覆盖软件及开发板；RPRS[104]在深空任务中根据剩余资源进行局部修复与重排。预定义响应把主要决策前移，但作用范围受已准备方案限制；在线修复扩大了对当前状态的适应性，同时增加诊断、搜索及重新生效的负担。这一区别与单纯提高检测准确率不同：恢复策略需要输出可执行的新安排，并明确原任务何时可以继续、哪些活动仍须放弃。

**表5 安全与恢复方法的直接输出和验证对象**

| 研究环节 | 直接输出 | 证据的适用范围 |
| --- | --- | --- |
| 接近计算与筛查[82][84] | 候选事件与最近接近结果 | 近似、目录、误差或漏检条件；不直接输出规避动作 |
| 风险预测与跟踪[83][87] | 信息分配和风险估计 | 输入质量与预测目标；不等于机动完成 |
| 安全轨迹与控制[90][91][92][93][94][95] | 轨迹与控制动作 | 动力学、扰动、连续/离散约束和原任务域 |
| 学习安全干预与路线图[96] | 安全屏蔽开关；未屏蔽RL与PRM的两组不同对照 | 任务与安全要求、样本数量和计时范围分别解释；PRM执行有状态校正 |
| 规则FDIR[102] | 故障判断及恢复操作 | 地面原型；规则覆盖与硬件代表性 |
| 任务管理与修复[103][104] | 应急计划或修复后的活动 | 软件/开发板或深空模型；不直接证明星座服务恢复 |

### 3.5 多问题耦合与综合运行管理

综合运行研究通过任务依赖、可用资源和状态更新连接不同功能。自动化工具分类[6]与可信自主运行综述[105]提供了职责和实现背景；本节关注具体模型中信息如何传递、哪些决定共同形成以及哪些仍保持固定。联合选择、顺序安排与运行反馈可在同一系统中并存，分别处理当前决策中的依赖、已经形成的输入和执行后的变化。

#### 3.5.1 交付约束参与分配与既有资源保留

接触图采集与交付调度[106]在请求到达后共同搜索任务传递、采集和交付路径，按最早交付选择执行卫星。资源感知版本扣减已分配接触容量，并保留此前请求的资源占用，后续请求不能在该算法中任意重分配这些额度。与[42]以任务加权调度收益、[44]以观测收益及下传体积评价的模型相比，[106]着重逐请求交付数量和成功样本交付时延，且假设能源和存储无限。三者都使后续传输条件参与前期安排，但“请求是否交付”和“下载了多少数据”属于不同评价量。

其16星离散事件实验进一步区分交付数量与成功样本时延；在接触不可靠时，按当前可用连接进行局部路由具有相对优势[106]。这说明调度阶段的容量安排和传输阶段的路径选择可能面对不同状态。保留任务分配、但允许传输绕行，与重新分配所有任务是不同的反馈范围，最终业务结果受到两者共同影响。

另一种连接由已经形成的采集安排向下游传递。[53]保留上游决定，优化星地处理分配；相关卸载方法[54][55][56]围绕处理位置或推理资源形成局部决策。长期能力配置[17][23][27][28]又通过可用时刻、位置和剩余资源向任务层提供输入。这些模型分别在请求、处理和能力阶段引入依赖，其决定能否反向修改上游变量并不一致。图2并列呈现联合选择、顺序输入和运行反馈；第4.2节用共同完成条件、信息获得时间及允许修改的资源范围判断各方式的适用条件。

#### 3.5.2 统一任务模型与状态驱动调度

SatOps—NetOps框架[9]将卫星资源和网络需求写入统一任务模型，用构造启发式、局部搜索及事件触发重排形成计划。原文按交互方式区分集成、协调、自适应三类模式，并展开为四种具体架构；16星性能比较对应其中的集成原型。分层资源管理[81]采用全局配置约束局部资源响应，两者都连接不同决策职责，但统一任务模型与层间配置传递保留的局部权限不同。因而，架构分类适合描述决策组织，具体性能仍对应实际实现及其比较场景。

推理式敏捷观测研究[107]通过模型预测观测、传输、存储和能源状态，用规则调整策略权重，再执行目标插入与约束检查。其单星仿真比较资源充足、传输受限和能源受限情景。该方法把子系统状态转化为调度偏好，而不是同时搜索全部子系统动作；模型预测、规则选择与活动构造在这里具有可区分的职责。这种状态驱动策略提供了资源变化参与计划更新的另一方式，其范围仍限定于相应单星模型。

#### 3.5.3 执行反馈与协同范围

Remote Agent[108]将规划、执行、模式识别和重配置组织为自主运行架构；EO-1[109]及IPEX[110][111]提供星上处理、资源监测与持续规划的单星经验。自主与自适应参考架构[112]的公开摘要从监测、分析、规划、执行及共享知识讨论模块职责，cFS演示包[113]则提供软件组件连接基础。前两类任务经验围绕实际功能及事件，后两类材料围绕架构和组件组织；其共同作用是明确状态在哪里产生、由哪个主体使用以及如何进入下一轮决策。

Starling[114]以四颗CubeSat共享观测状态并协调后续GPS观测，Starling 1.5[115]则在模拟接近场景中交换轨迹及风险信息、明确责任并执行实际机动。群体观测和跨运营方风险处置分别扩展成员及管理主体之间的协同，其触发事件和动作权限并不相同。Basilisk[116]与形式化方法[117]为动力学仿真和规格检查提供工具；把这些功能组合起来时，需要保持状态、计划及动作之间的一致性，而业务收益仍由具体任务序列决定。

![图2](../figures/fig2_zh.svg)

图2 联合选择、顺序安排与运行反馈的决策联系。实线对应代表研究采用的输入或状态更新，虚线为本文归纳的跨业务能力联系；三种方式可组合使用。图内案例依据[9][53][106][111][114][115]，其适用条件进一步见表6。

## 4 综合认识与研究展望

### 4.1 问题结构与完整决策成本

可扩展性的收益来自问题结构被利用的具体位置。分支定价[33]通过结构化列生成减少直接处理的变量，观测—传输调度[42]在时间窗关联与窗内配置之间分层搜索，[44]通过图缩减和邻域启发式降低计算负担；轨迹预计算[71][72]把动力学求解前移，增量规划[34]复用旧安排，几何邻域[35]限制冲突协调范围。它们分别改变变量生成、搜索维度、预处理和消息范围，因此“模型求解更快”的可解释成本对象并不相同。特别是[44]中可能缩小可行集合的简化模型，说明计算改善还应检查是否改变了可达到的解质量。

可扩展性评价至少要区分三类代价：构造候选状态及模型所需的准备成本，给定一次输入的求解与协调成本，以及计划修改后真正生效的成本。前一类包括预计算轨迹或训练策略，中间一类包括列生成定价、搜索和消息交换，最后一类包括已确认资源的变更和新链路建立。计划复用[34]可以少算却保留重复观测，邻域化[35]可以减少协调却产生满足率差距；激光链路路径保持[121]则在建链成本很低时可能损失端到端时延。评价这些策略时，应报告被节省的成本与相同业务定义下损失或改善的结果，而不是仅比较算法单次运行时间。

这些成本能否摊销取决于时间跨度和变化频率。离线解库、航天动力学轨迹网格和训练策略需要在多次任务中复用；如果需求和轨道状态频繁偏离准备条件，就需要重建或校正。相同秒级求解时间对剩余数分钟的观测窗口与持续排队的通信业务具有不同意义。一个可复核的比较至少应交代准备开销、重复使用次数、每次更新的求解时间、成员消息与真实资源生效时刻；只有具备相同业务目标和相近的输入条件，跨算法的相对收益才有可解释基础。

### 4.2 资源耦合的收益条件与决策范围

资源耦合首先表现为“后续约束是否会改变当前选择”。He等[42]将观测与传输窗口纳入同一任务可行性安排，Lowe等[106]在逐请求采集节点选择时检验交付接触容量，Soret等[53]则先固定采集计划再优化下游处理。三种方法分别改变同次求解、逐请求路径选择和顺序输入的决策范围。即便两个模型均称“观测—下传联合”，其目标可能不同：[42]的加权调度请求与[44]的观测收益加下传数据量不能直接互换。因而，判断扩大联合范围是否有收益，首先应检查下游瓶颈是否真实排除或改变上游候选，以及其影响是否计入研究实际采用的服务指标。

计算可处理性构成第二个条件。[42]通过时间窗关联与窗内配置的分层求解减小搜索负担，[44]既使用可能缩小可行搜索空间的模型简化，也使用保留结构的图变换与邻域改进。在给定输入下，这些技术可降低部分计算开销，但其影响对象分别可能是求解过程、候选表示或可行域本身。综述不能据某篇论文的加速比例推断其他模型必然获益；相反，应同时列出所保留的任务完成定义、简化后的可行范围及实验计算平台。

信息时效和动作生效构成第三个条件。下游容量在当前时刻可准确获得时，共同选择可避免上游决策占用无法兑现的机会；如果状态到达滞后，扩大模型也可能只是联合使用了过期信息。反过来，若上游活动尚未确认、且后续计划可在窗口失效前修正，顺序安排加运行反馈可能提供足够的适应能力；若资源不可撤销或建链时间较长，重规划的理论最优值也未必能兑现。这里的条件判断属于本综述跨论文形成的定性分析，不是原研究已经证明的统一阈值。

表6把评价从“选择何种算法”改为“如何比较在给定任务条件下的决策连接”。联合选择与顺序安排描述变量在何时进入同次求解；反馈描述执行后可修改的范围，三者是可组合维度。比较时应同时固定任务完成的定义、当前已承诺资源、状态滞后和允许修改的窗口；对于[44]一类含多个奖励项的模型，还需分别报告观测收益和数据交付量。否则，共同求解后的目标值变化可能来自奖励定义、求解空间或接受请求集合，而非联合程度本身。

**表6 联合选择、顺序安排与运行反馈的适用条件分析**

| 连接方式与参考研究 | 更可能适用的输入与时机 | 结果与比较口径 | 计算及执行代价 |
| --- | --- | --- | --- |
| 联合选择[42][44][106] | 下游窗口或容量可在当前选择时获得，并可能改变上游节点/时序 | 请求完成和下载数据量分别计；确认是否允许部分交付 | 变量耦合及求解规模增大；[44]部分简化模型可能缩小可行域 |
| 顺序安排与下游局部优化[53][74] | 上游计划已经确定，下游仍存在可优化的处理/功率资源 | 记录固定了哪些变量、负载和下游目标 | 上游无法在本次下游求解中响应拥塞或能量瓶颈 |
| 状态反馈与计划修复[9][107][111] | 执行状态变化，未确认活动仍可在机会到期前调整 | 状态版本、修改时点、按期完成和重规划频率 | 信息延迟、冲突检查及配置生效消耗剩余窗口 |
| 多方式组合（本文综合）[9][53][106] | 不同阶段的活动具有不同承诺和更新权限 | 用共同任务、负载与扰动序列分别评估各环节 | 权限交叠和状态版本不一致，可能抵消局部算法收益 |

表6为本文依据代表研究形成的条件化归纳，并非原论文对三类方式开展的共同实验或普遍性能排序。具体方案可同时具有联合、顺序和反馈特征。

### 4.3 信息与承诺约束下的更新及学习作用

信息共享的价值由待协调的决定决定。已完成状态[65]有助于避免再次安排已满足目标，但同时段竞争需要额外的分配或意图信息；消息机会预测和异步协调[38][118]改善信息到达条件，却不自动增加共享内容。分层资源管理[81]又限定不同主体可调整的资源。由此，信息内容、到达时机和决策权限必须共同解释：一个节点知道资源发生变化，并不意味着它有权修改已经分配给其他节点的活动。

资源承诺进一步收缩更新的选择空间。预约配置[52]有明确的变更过程，接触图调度[106]保留先前分配资源，动态链路[121]则为新配置计入建链代价。它们分别对应组织规则、算法假设和物理动作，但都说明旧计划不能被视为可无代价覆盖的文本。重规划需要同时判断信息是否更新、安排是否仍可改变及改变何时生效；局部修复与全局重算的差异也只有在这些条件一致时才可解释。

学习方法对整个运行链的作用，需要对应明确的模块职责和对照条件。流量预测[73]产生需求估计，学习辅助大邻域搜索[63]生成初解并交由破坏—修复改进，单星策略复用[65]直接作活动选择，屏蔽动作[96]则通过安全检查限制执行。后一类研究甚至会同时改变允许的安全动作集和在线计算，因此不能仅从最后的燃料—时间结果推断学习或屏蔽单独带来的收益。比较学习模块时，应保持下游资源、约束和任务样本一致，分别观察预测误差、计划质量、约束违反、训练/推理/修复成本及最终业务结果。

### 4.4 运行实践与验证对象的对应

公开运行资料帮助确定模型结果与实际事件如何对应，但证据职责不同。Planet与AWS接口[51][52]分别说明任务质量、交付状态和预约配置的操作语义；Iridium备星[22]公开能力投入，ADRAS-J[97]记录异常接近后的安全退出；Starlink独立测量[78]说明连接对象未切换时服务仍可波动。IPEX及Starling系列[111][114][115]展示限定规模和事件的星上或多星反馈。表7据观察对象组织这些材料，不将商业接口、外部测量或一次飞行事件等同于统一调度算法的性能验证。

**表7 公开运行资料与试验的观察对象**

| 资料或案例 | 已公开的状态或动作 | 对综述的用途与限制 |
| --- | --- | --- |
| Iridium[22] | 5颗备星部署 | 说明备用能力投入；不证明最优库存或即时恢复 |
| Planet / AWS[51][52] | 质量与交付状态；预约配置快照及变更 | 定义任务完成和资源承诺；非内部调度性能实验 |
| Starlink流程[89] | 风险重估与机动增改撤 | 组织数据和行动职责；不是独立性能测量 |
| Starlink独立测量[78] | 受控条件下的时延与吞吐波动 | 支持观察条件下的现象；不直接揭示内部调度 |
| ADRAS-J[97] | 接近异常后中止与安全后撤 | 安全退出已发生；原任务完成需分开判断 |
| EO-1 / IPEX[109][110][111] | 星上处理与持续规划 | 单星功能连接；不据此推断大规模协同 |
| Starling / Starling 1.5[114][115] | 四星观测选择；模拟接近中的实际机动协调 | 不同试验目标、规模和管理主体，分别解释 |
| CCSDS / cFS / 形式化研究[88][113][119][120] | 报文、组件或规格下的性质 | 提供互操作和软件依据；不是业务收益的直接验证 |

软件与业务验证也需围绕共同事件分别定指标。受监督重配置[119]和模型检查[120]评价软件配置及规格性质，形式化研究[117]讨论可证明的运行属性；业务模型则观察按期交付、服务中断、成本或任务满足。对于同一故障序列，可以依次核查故障信息是否产生、计划是否一致、动作是否按约束执行，以及服务需求何时恢复。这样的验证链能够揭示局部算法效果如何经过接口和执行传递，而不把某一项软件测试通过直接视为端到端服务改进。

### 4.5 面向持续服务的研究问题

能力恢复研究可进一步连接维护决策与受影响的业务需求。库存、补给通道和服务恢复[18][19][23]分别给出不同的能力补充方式，下一步可在共同故障和需求序列下区分资产供应、重新就位、载荷恢复与业务重分配，考察不同阶段延迟造成的未满足请求或通信中断。这一问题允许采用分层或事件驱动模型，不要求把全部库存、轨迹和任务变量一次性联立。

决定联合范围是否值得，可以建立同一任务样本下的受控比较。针对[42][44][53][106]，分别设置只安排采集、顺序考虑处理与下传、共同选择采集与下游资源，以及允许事件触发修复的方案；每组保持可见窗口、存储、容量与业务截止期一致，并事先锁定“任务完成”或“下传数据量”的统计定义。报告最终服务和计算/消息负担，而不是只比较各自原论文目标值。这样的实验可以检验表6的条件判断，但本文并没有实施此项跨论文复现。

在线更新研究可把消息传播与资源承诺放在同一时间轴上。任务完成状态、未来意图、预约配置和局部权限[38][52][65][81]影响计划能否一致生效。可比较不同更新触发方式和局部修复范围，分析状态到达、求解、冲突检查及配置生效各阶段形成的业务损失，并考察信息缺失时保留旧计划或采取保守响应的后果。观测和通信可使用相近的分析结构，但需分别定义可撤销活动和损失。

学习研究可从模块输出延伸至最终可执行业务结果。对需求预测、搜索辅助和策略生成[63][65][73][96]分别设置适当的替代方法，保持资源、安全要求及下游处理一致，并计入训练、推理和修复成本。特别需要区分因模型准确性改善而获得的收益，与因更换约束或接受不同请求集合而产生的差异。对不能保持单因素的系统比较，应明确其整体评估性质。

上述问题可由一套最小但可复核的共同事件描述串联：记录任务到达和有效期、候选观测与连接窗口、可用计算及存储、成员信息延迟、已确认资源、异常发生和恢复时刻，并冻结评价指标与计时范围。能力恢复、任务重排、路径更新与安全干预可以在相同事件序列内分别验证接口正确性、计划可行性和最终服务结果。共同输入提高比较的可解释性，并不消除原论文在轨道模型、部署权限和实验保真度上的差异。

## 5 结论

本文以对地观测与通信为核心业务，围绕能力形成、资源安排和执行恢复比较大型卫星星座管理研究。各技术路线首先在决策对象上不同：构型维护决定能力及其可用时刻，观测与通信调度分别安排离散请求和持续流量，风险、故障及软件执行改变后续状态。对同一技术名称下的模型，还需明确实际奖励的是观测收益、下载数据量、按期完成的请求还是网络服务质量，这些结果不能依同一尺度排名。

跨研究归纳得到三点条件性认识。其一，可扩展性依赖任务结构与计算被缩减、前移或复用的环节；减小搜索空间可能节约时间，也可能带来候选损失。其二，是否扩大联合范围取决于下游约束对当前选择的影响，信息可得性与允许修改的时间共同限定联合、顺序和反馈的价值。其三，已完成状态、资源承诺与配置生效具有不同语义，预测或快速生成计划还需经过搜索、冲突消解和执行约束才可能形成最终业务收益。代表研究为这些判断提供机制与条件证据，但尚不构成跨业务通用性能定律。

运营接口、独立测量、软件测试与飞行事件分别揭示完成状态、服务现象、系统性质和实际动作。后续研究可在共同任务及扰动条件下检验能力恢复对业务损失的作用、资源联合程度与计算代价的取舍，以及延迟信息下的在线调整；同时保持各研究原有的模型、样本和验证边界。本文的目的在于为技术比较提供可追踪的决策与结果定义，而非提出已经部署的统一星座运行系统。

## 参考文献

1. Mohamed Khalil Ben-Larbi; Kattia Flores Pozo; Tom Haylok; et al. Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts. Advances in Space Research, 2021, 67(11): 3598–3619. DOI: 10.1016/j.asr.2020.08.009. [来源](https://doi.org/10.1016/j.asr.2020.08.009)

2. Koki Ho. Space Logistics Modeling and Optimization: Review of the State of the Art. Journal of Spacecraft and Rockets, 2024, 61(5): 1417–1427. DOI: 10.2514/1.A35982. [来源](https://doi.org/10.2514/1.A35982)

3. Xinwei Wang; Guohua Wu; Lining Xing; et al. Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions. IEEE Systems Journal, 2021, 15(3): 3881–3892. DOI: 10.1109/JSYST.2020.2997050. [来源](https://doi.org/10.1109/JSYST.2020.2997050)

4. Benedetta Ferrari; Jean-François Cordeau; Maxence Delorme; et al. Satellite Scheduling Problems: A survey of applications in Earth and outer space observation. Computers & Operations Research, 2025, 173: 106875. DOI: 10.1016/j.cor.2024.106875. [来源](https://doi.org/10.1016/j.cor.2024.106875)

5. Mohammad Reza Jabbarpour; Bao Quoc Vo; Ghaith El-Dalahmeh; et al. Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges. Acta Astronautica, 2026, 238: 237–257. DOI: 10.1016/j.actaastro.2025.10.018. [来源](https://doi.org/10.1016/j.actaastro.2025.10.018)

6. Mohamed Khalil Ben-Larbi; Kattia Flores Pozo; Mirue Choi; et al. Towards the automated operations of large distributed satellite systems. Part 2: Classifications and tools. Advances in Space Research, 2021, 67(11): 3620–3637. DOI: 10.1016/j.asr.2020.08.018. [来源](https://doi.org/10.1016/j.asr.2020.08.018)

7. 龚李赠; 张文龙; 陈全; 等. 低轨巨型星座智能组网技术综述. 航空学报, 2026; online 23 March 2026. DOI: 10.7527/S1000-6893.2026.32935. [来源](https://doi.org/10.7527/S1000-6893.2026.32935)

8. 邸航; 董涛; 刘志慧; 等. 低轨通信卫星星座网络资源管控与优化技术综述. 宇航学报, 2026, 47(2): 270–283. DOI: 10.3873/j.issn.1000-1328.2026.02.002. [来源](https://doi.org/10.3873/j.issn.1000-1328.2026.02.002)

9. Arnau Singla; Franco Criscola; David Canales; et al. Toward Integrated Satellite Operations and Network Management: A Review and Novel Framework. Technologies, 2025, 13(8): 312. DOI: 10.3390/technologies13080312. [来源](https://doi.org/10.3390/technologies13080312)

10. Yuhe Mao; Yunhua Wu; Xiaozhe Ju; et al. Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation. Space: Science & Technology, 2025, 5: 0248. DOI: 10.34133/space.0248. [来源](https://doi.org/10.34133/space.0248)

11. Leonid Appel; Moshe Guelman; David Mishne. Optimization of satellite constellation reconfiguration maneuvers. Acta Astronautica, 2014, 99: 166–174. DOI: 10.1016/j.actaastro.2014.02.016. [来源](https://doi.org/10.1016/j.actaastro.2014.02.016)

12. Hang Woon Lee; Koki Ho. Regional Constellation Reconfiguration Problem: Integer Linear Programming Formulation and Lagrangian Heuristic Method. Journal of Spacecraft and Rockets, 2023, 60(6): 1828–1845. DOI: 10.2514/1.A35685. [来源](https://doi.org/10.2514/1.A35685)

13. Hang Woon Lee; David O. Williams Rogers; Brycen D. Pearl; et al. Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods. Journal of Spacecraft and Rockets, 2025, 62(1): 206–222. DOI: 10.2514/1.A35990. [来源](https://doi.org/10.2514/1.A35990)

14. Hang Woon Lee; Seiichi Shimizu; Shoji Yoshikawa; et al. Satellite Constellation Pattern Optimization for Complex Regional Coverage. Journal of Spacecraft and Rockets, 2020, 57(6): 1309–1327. DOI: 10.2514/1.A34657. [来源](https://doi.org/10.2514/1.A34657)

15. Hang Woon Lee; Pauline C. Jakob; Koki Ho; et al. Optimization of satellite constellation deployment strategy considering uncertain areas of interest. Acta Astronautica, 2018, 153: 213–228. DOI: 10.1016/j.actaastro.2018.03.054. [来源](https://doi.org/10.1016/j.actaastro.2018.03.054)

16. Beomjin Gwon; Jaemyung Ahn. Two-Stage Framework for Deployment-Aware Optimization of Satellite Constellation Pattern Design. International Journal of Aeronautical and Space Sciences, 2026. DOI: 10.1007/s42405-026-01298-1. [来源](https://doi.org/10.1007/s42405-026-01298-1)

17. Samuel Martínez Zamacola; Ramón Martínez Rodríguez-Osorio; Miguel A. Salas-Natera. Joint satellite platform and constellation sizing for instantaneous beam-hopping in 5G/6G Non-Terrestrial Networks. Computer Networks, 2025, 257: 110942. DOI: 10.1016/j.comnet.2024.110942. [来源](https://doi.org/10.1016/j.comnet.2024.110942)

18. Pauline Jakob; Seiichi Shimizu; Shoji Yoshikawa; et al. Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control. Journal of Spacecraft and Rockets, 2019, 56(5): 1449–1461. DOI: 10.2514/1.A34387. [来源](https://doi.org/10.2514/1.A34387)

19. Jaewoo Kim; Jaemyung Ahn; Taehyun Sung. Replenishment Strategy for Satellite Constellation with Dual Supply Modes. Journal of Spacecraft and Rockets, 2025, 62(5): 1567–1583. DOI: 10.2514/1.A36281. [来源](https://doi.org/10.2514/1.A36281)

20. Seungyeop Han; Zachary Grieser; Shoji Yoshikawa; et al. Spare Strategy Analysis and Design for Mega Satellite Constellations Using Markov Chain. Journal of Spacecraft and Rockets, 2026: 1–12. DOI: 10.2514/1.A36599. [来源](https://doi.org/10.2514/1.A36599)

21. Seungyeop Han; Shoji Yoshikawa; Takumi Noro; et al. Spare strategy for large-scale satellite constellations under dual resupply channels using Markov chain. Acta Astronautica, 2026, 248: 614–629; assigned issue: November 2026. DOI: 10.1016/j.actaastro.2026.06.020. [来源](https://doi.org/10.1016/j.actaastro.2026.06.020)

22. Iridium. Iridium Adds to Constellation Resilience with Launch of Spare Satellites. Official operational release; accessed 10 October 2026 (inherited access date). https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites. [来源](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites)

23. Jaewoo Kim; Taehyun Sung; Woonam Hwang; et al. On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation. Journal of Spacecraft and Rockets, 2026: 1–18. DOI: 10.2514/1.A36684. [来源](https://doi.org/10.2514/1.A36684)

24. Yuri Shimane; Nicholas Gollins; Koki Ho. Orbital Facility Location Problem for Satellite Constellation Servicing Depots. Journal of Spacecraft and Rockets, 2024, 61(3): 808–825. DOI: 10.2514/1.A35691. [来源](https://doi.org/10.2514/1.A35691)

25. Euihyeon Choi; Koki Ho. Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers. Journal of Spacecraft and Rockets, 2026, 63(1): 4–13. DOI: 10.2514/1.A36386. [来源](https://doi.org/10.2514/1.A36386)

26. Yaxiong Li; Xinglong Sun; Xinxue Liu; et al. Deployment of On-Orbit Service Vehicles Using a Fuzzy Adaptive Particle Swarm Optimization Algorithm. Modelling and Simulation in Engineering, 2021, 2021: 1–15. DOI: 10.1155/2021/6644339. [来源](https://doi.org/10.1155/2021/6644339)

27. Tristan Sarton du Jonchay; Hao Chen; Onalli Gunasekara; et al. Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties. Journal of Spacecraft and Rockets, 2021, 58(4): 1157–1173. DOI: 10.2514/1.A34978. [来源](https://doi.org/10.2514/1.A34978)

28. Tristan Sarton du Jonchay; Hao Chen; Masafumi Isaji; et al. On-Orbit Servicing Optimization Framework with High- and Low-Thrust Propulsion Tradeoff. Journal of Spacecraft and Rockets, 2022, 59(1): 33–48. DOI: 10.2514/1.A35094. [来源](https://doi.org/10.2514/1.A35094)

29. Wen Yao; Xiaoqian Chen; Yiyong Huang; et al. On-orbit servicing system assessment and optimization methods based on lifecycle simulation under mixed aleatory and epistemic uncertainties. Acta Astronautica, 2013, 87: 107–126. DOI: 10.1016/j.actaastro.2013.02.005. [来源](https://doi.org/10.1016/j.actaastro.2013.02.005)

30. Michel Lemaître; Gérard Verfaillie; Frank Jouhaud; et al. Selecting and scheduling observations of agile satellites. Aerospace Science and Technology, 2002, 6(5): 367–381. DOI: 10.1016/S1270-9638(02)01173-2. [来源](https://doi.org/10.1016/S1270-9638(02)01173-2)

31. Yongming He; Lining Xing; Yingwu Chen; et al. A Generic Markov Decision Process Model and Reinforcement Learning Method for Scheduling Agile Earth Observation Satellites. IEEE Transactions on Systems, Man, and Cybernetics: Systems, 2022, 52(3): 1463–1474. DOI: 10.1109/TSMC.2020.3020732. [来源](https://doi.org/10.1109/TSMC.2020.3020732)

32. Jing Qi; Min Hu; Lining Xing. A decompose-and-learn multi-objective algorithm for scheduling large-scale earth observation satellites. Swarm and Evolutionary Computation, 2025, 92: 101792. DOI: 10.1016/j.swevo.2024.101792. [来源](https://doi.org/10.1016/j.swevo.2024.101792)

33. Pedro Marcolin Antunes; Laio Oriel Seman; Eduardo Camponogara. A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites. Computers & Operations Research, 2026, 185: 107259. DOI: 10.1016/j.cor.2025.107259. [来源](https://doi.org/10.1016/j.cor.2025.107259)

34. Shreya Parjan; Steve A. Chien. Decentralized Observation Allocation for a Large-Scale Constellation. Journal of Aerospace Information Systems, 2023, 20(8): 447–461. DOI: 10.2514/1.I011215. [来源](https://doi.org/10.2514/1.I011215)

35. Itai Zilberstein; Ananya Rao; Matthew Salis; et al. Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation. Journal of Artificial Intelligence Research, 2025, 82: 169–208. DOI: 10.1613/jair.1.16997. [来源](https://doi.org/10.1613/jair.1.16997)

36. Shai Krigman; Tal Grinshpoun; Lihi Dery. Scheduling of Earth observing satellites using distributed constraint optimization. Journal of Scheduling, 2024, 27(5): 507–524. DOI: 10.1007/s10951-024-00816-x. [来源](https://doi.org/10.1007/s10951-024-00816-x)

37. Han-Lim Choi; L. Brunet; J. P. How. Consensus-Based Decentralized Auctions for Robust Task Allocation. IEEE Transactions on Robotics, 2009, 25(4): 912–926. DOI: 10.1109/TRO.2009.2022423. [来源](https://doi.org/10.1109/TRO.2009.2022423)

38. Guoliang Li. Online scheduling of distributed Earth observation satellite system under rigid communication constraints. Advances in Space Research, 2020, 65(11): 2475–2496. DOI: 10.1016/j.asr.2020.02.018. [来源](https://doi.org/10.1016/j.asr.2020.02.018)

39. Chong Wang; Jinhui Tang; Xiaohang Cheng; et al. Distributed cooperative task planning algorithm for multiple satellites in delayed communication environment. Journal of Systems Engineering and Electronics, 2016, 27(3): 619–633. DOI: 10.1109/JSEE.2016.00066. [来源](https://doi.org/10.1109/JSEE.2016.00066)

40. Weiyi Yang; Lei He; Xiaolu Liu; et al. Onboard coordination and scheduling of multiple autonomous satellites in an uncertain environment. Advances in Space Research, 2021, 68(11): 4505–4524. DOI: 10.1016/j.asr.2021.09.003. [来源](https://doi.org/10.1016/j.asr.2021.09.003)

41. Ben Rachmut; Sofia Amador Nelke; Roie Zivan. Asynchronous Communication Aware Multi-Agent Task Allocation. Proceedings of IJCAI, 2023: 262–270. DOI: 10.24963/ijcai.2023/30. [来源](https://doi.org/10.24963/ijcai.2023/30)

42. Lijun He; Ben Liang; Jiandong Li; et al. Joint Observation and Transmission Scheduling in Agile Satellite Networks. IEEE Transactions on Mobile Computing, 2022, 21(12): 4381–4396. DOI: 10.1109/TMC.2021.3076088. [来源](https://doi.org/10.1109/TMC.2021.3076088)

43. Minghao Shang; Ronggang Yuan; Bin Song; et al. Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm. Acta Astronautica, 2025, 230: 92–103. DOI: 10.1016/j.actaastro.2025.02.008. [来源](https://doi.org/10.1016/j.actaastro.2025.02.008)

44. Yure Rocha; Guilherme O. Chagas; Leandro C. Coelho; et al. The integrated agile Earth observation satellite scheduling problem. Computers & Operations Research, 2025, 184: 107212. DOI: 10.1016/j.cor.2025.107212. [来源](https://doi.org/10.1016/j.cor.2025.107212)

45. Sung Jun Kim; Minchae Kim; Han-Lim Choi. Tip-and-cue mission scheduling in heterogeneous satellite constellations using mixed-integer linear programming. Acta Astronautica, 2026, 246: 921–940. DOI: 10.1016/j.actaastro.2026.04.059. [来源](https://doi.org/10.1016/j.actaastro.2026.04.059)

46. Sara Spangelo; James Cutler; Kyle Gilson; et al. Optimization-based scheduling for the single-satellite, multi-ground station communication problem. Computers & Operations Research, 2015, 57: 1–16. DOI: 10.1016/j.cor.2014.11.004. [来源](https://doi.org/10.1016/j.cor.2014.11.004)

47. Laura Barbulescu; Jean-Paul Watson; L. Darrell Whitley; et al. Scheduling Space–Ground Communications for the Air Force Satellite Control Network. Journal of Scheduling, 2004, 7(1): 7–34. DOI: 10.1023/B:JOSH.0000013053.32600.3c. [来源](https://doi.org/10.1023/B:JOSH.0000013053.32600.3c)

48. Daniel Karapetyan; Snezana Mitrovic Minic; Krishna T. Malladi; et al. Satellite downlink scheduling problem: A case study. Omega, 2015, 53: 115–123. DOI: 10.1016/j.omega.2015.01.001. [来源](https://doi.org/10.1016/j.omega.2015.01.001)

49. Alex Sabol; Ryan Alimo; Farhad Kamangar; et al. Deep Space Network Scheduling via Mixed-Integer Linear Programming. IEEE Access, 2021, 9: 39985–39994. DOI: 10.1109/ACCESS.2021.3064928. [来源](https://doi.org/10.1109/ACCESS.2021.3064928)

50. Mark D. Johnston; Daniel Tran; Belinda Arroyo; et al. Automated Scheduling for NASA's Deep Space Network. AI Magazine, 2014, 35(4): 7–25. DOI: 10.1609/aimag.v35i4.2552. [来源](https://doi.org/10.1609/aimag.v35i4.2552)

51. Planet. Tasking API. Official documentation; accessed 10 October 2026 (inherited access date). https://docs.planet.com/develop/apis/tasking/. [来源](https://docs.planet.com/develop/apis/tasking/)

52. Amazon Web Services. Work with contacts. Official documentation; accessed 10 October 2026 (inherited access date). https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html. [来源](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html)

53. Beatriz Soret; Antonio M. Mercado-Martínez; Antonio Jurado-Navas; et al. Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing. International Journal of Satellite Communications and Networking, 2026: 1–22; advance online publication, 24 August 2026. DOI: 10.1002/sat.70082. [来源](https://doi.org/10.1002/sat.70082)

54. Min Jia; Liang Zhang; Jian Wu; et al. Deep Multiagent Reinforcement Learning for Task Offloading and Resource Allocation in Satellite Edge Computing. IEEE Internet of Things Journal, 2025, 12(4): 3832–3845. DOI: 10.1109/JIOT.2024.3482290. [来源](https://doi.org/10.1109/JIOT.2024.3482290)

55. Hai Li; Jinyang Yu; Lili Cao; et al. Multi-agent reinforcement learning based computation offloading and resource allocation for LEO Satellite edge computing networks. Computer Communications, 2024, 222: 268–276. DOI: 10.1016/j.comcom.2024.05.008. [来源](https://doi.org/10.1016/j.comcom.2024.05.008)

56. Wenhao Fan; Qingcheng Meng; Guan Wang; et al. Satellite Edge Intelligence: DRL-Based Resource Management for Task Inference in LEO-Based Satellite-Ground Collaborative Networks. IEEE Transactions on Mobile Computing, 2025, 24(10): 10710–10728. DOI: 10.1109/TMC.2025.3570799. [来源](https://doi.org/10.1109/TMC.2025.3570799)

57. Danilo Magliarisi; Emiliano Casalicchio; Vincenzo Salvatore. Orbit-aware task scheduling in satellite edge computing. Cluster Computing, 2025, 28(16): 1013. DOI: 10.1007/s10586-025-05663-9. [来源](https://doi.org/10.1007/s10586-025-05663-9)

58. Bradley Denby; Krishna Chintalapudi; Ranveer Chandra; et al. Kodan: Addressing the Computational Bottleneck in Space. Proceedings of ASPLOS, Volume 3, 2023: 392–403. DOI: 10.1145/3582016.3582043. [来源](https://doi.org/10.1145/3582016.3582043)

59. Jiahao Qin; Hongxia Wang; Xudong Gao; et al. Lagrangian hierarchical mixed-integer programming for ultra-large-scale satellite scheduling under dynamic task delivery. Advances in Space Research, 2026, 77(11): 11252–11270. DOI: 10.1016/j.asr.2025.12.008. [来源](https://doi.org/10.1016/j.asr.2025.12.008)

60. Jianjiang Wang; Erik Demeulemeester; Dishan Qiu. A pure proactive scheduling algorithm for multiple earth observation satellites under uncertainties of clouds. Computers & Operations Research, 2016, 74: 1–13. DOI: 10.1016/j.cor.2016.04.014. [来源](https://doi.org/10.1016/j.cor.2016.04.014)

61. Xinwei Wang; Guopeng Song; Roel Leus; et al. Robust Earth Observation Satellite Scheduling With Uncertainty of Cloud Coverage. IEEE Transactions on Aerospace and Electronic Systems, 2020, 56(3): 2450–2461. DOI: 10.1109/TAES.2019.2947978. [来源](https://doi.org/10.1109/TAES.2019.2947978)

62. Christopher G. Valicka; Deanna Garcia; Andrea Staid; et al. Mixed-integer programming models for optimal constellation scheduling given cloud cover uncertainty. European Journal of Operational Research, 2019, 275(2): 431–445. DOI: 10.1016/j.ejor.2018.11.043. [来源](https://doi.org/10.1016/j.ejor.2018.11.043)

63. Jing Qi; Min Hu; Lining Xing; et al. Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites. Expert Systems with Applications, 2025, 291: 128502. DOI: 10.1016/j.eswa.2025.128502. [来源](https://doi.org/10.1016/j.eswa.2025.128502)

64. Zhe Li; Xin Zhu; Changdi Liu; et al. Dynamic task scheduling optimization by rolling horizon deep reinforcement learning for distributed satellite system. Expert Systems with Applications, 2025, 289: 128350. DOI: 10.1016/j.eswa.2025.128350. [来源](https://doi.org/10.1016/j.eswa.2025.128350)

65. Adam Herrmann; Mark A. Stephenson; Hanspeter Schaub. Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations. Journal of Spacecraft and Rockets, 2024, 61(1): 114–132. DOI: 10.2514/1.A35736. [来源](https://doi.org/10.2514/1.A35736)

66. Adam Herrmann; Hanspeter Schaub. A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling. Frontiers in Space Technologies, 2023, 4: 1263489. DOI: 10.3389/frspt.2023.1263489. [来源](https://doi.org/10.3389/frspt.2023.1263489)

67. Susan E. Sorenson; Sarah G. Nurre Pinkley. Multi-orbit routing and scheduling of refuellable on-orbit servicing space robots. Computers & Industrial Engineering, 2023, 176: 108852. DOI: 10.1016/j.cie.2022.108852. [来源](https://doi.org/10.1016/j.cie.2022.108852)

68. Shuai Yin; Chuanjiang Li; Edoardo Fadda; et al. On-orbit refueling robust mission scheduling with uncertain duration for geosynchronous orbit spacecraft. Chinese Journal of Aeronautics, 2026, 39(1): 103774. DOI: 10.1016/j.cja.2025.103774. [来源](https://doi.org/10.1016/j.cja.2025.103774)

69. K. Daneshjou; A. A. Mohammadi-Dehabadi; M. Bakhtiari. Mission planning for on-orbit servicing through multiple servicing satellites: A new approach. Advances in Space Research, 2017, 60(6): 1148–1162. DOI: 10.1016/j.asr.2017.05.037. [来源](https://doi.org/10.1016/j.asr.2017.05.037)

70. Weikui Liang; Hui Zhi; Peng Han; et al. GEO satellite on-orbit refueling and debris removal hybrid mission planning under uncertainty. Advances in Space Research, 2024, 74(5): 2376–2387. DOI: 10.1016/j.asr.2024.05.059. [来源](https://doi.org/10.1016/j.asr.2024.05.059)

71. Riccardo Apa; Jennifer Hudson; Marcello Romano. Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit. The Journal of the Astronautical Sciences, 2026, 73(2): 36. DOI: 10.1007/s40295-026-00580-4. [来源](https://doi.org/10.1007/s40295-026-00580-4)

72. Riccardo Apa; Shambo Bhattacharjee; Jennifer Hudson; et al. Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations. The Journal of the Astronautical Sciences, 2025, 72(2): 7. DOI: 10.1007/s40295-025-00487-6. [来源](https://doi.org/10.1007/s40295-025-00487-6)

73. Chi Han; Wei Xiong; Ronghuan Yu. A Hybrid Forecasting Model for Self-Similar Traffic in LEO Mega-Constellation Networks. Aerospace, 2024, 11(3): 191. DOI: 10.3390/aerospace11030191. [来源](https://doi.org/10.3390/aerospace11030191)

74. Shuang Zheng; Xing Zhang; Peng Wang; Wenbo Wang. Joint Beam Scheduling and Power Optimization for Beam Hopping LEO Satellite Systems. China Communications, 2024, 21(10): 1–14. DOI: 10.23919/JCC.ja.2022-0864. [来源](https://doi.org/10.23919/JCC.ja.2022-0864)

75. Zhiyuan Lin; Zuyao Ni; Linling Kuang; et al. NGSO Satellites Beam Hopping Strategy Based on Load Balancing and Interference Avoidance for Coexistence With GSO Systems. IEEE Communications Letters, 2023, 27(1): 278–282. DOI: 10.1109/LCOMM.2022.3213912. [来源](https://doi.org/10.1109/LCOMM.2022.3213912)

76. Ruili Zhao; Jun Cai; Jiangtao Luo; et al. Demand-Aware Beam Hopping and Power Allocation for Load Balancing in Digital Twin Empowered LEO Satellite Networks. IEEE Transactions on Wireless Communications, 2025, 24(6): 5084–5098. DOI: 10.1109/TWC.2025.3545745. [来源](https://doi.org/10.1109/TWC.2025.3545745)

77. Zhenglong Yin; Quan Chen; Lei Yang; et al. Routing cost-integrated intelligent handover strategy for multi-layer LEO mega-constellation networks. Chinese Journal of Aeronautics, 2025, 38(6): 103263. DOI: 10.1016/j.cja.2024.09.039. [来源](https://doi.org/10.1016/j.cja.2024.09.039)

78. Nitinder Mohan; Andrew E. Ferguson; Hendrik Cech; et al. A Multifaceted Look at Starlink Performance. Proceedings of the ACM Web Conference 2024: 2723–2734. DOI: 10.1145/3589334.3645328. [来源](https://doi.org/10.1145/3589334.3645328)

79. Shengyu Zhang; Kwan L. Yeung. Scalable routing in low-Earth orbit satellite constellations: Architecture and algorithms. Computer Communications, 2022, 188: 26–38. DOI: 10.1016/j.comcom.2022.02.015. [来源](https://doi.org/10.1016/j.comcom.2022.02.015)

80. Shengyu Zhang; Xiaoqian Li; Kwan Lawrence Yeung. Segment routing for traffic engineering and effective recovery in low-earth orbit satellite constellations. Digital Communications and Networks, 2024, 10(3): 706–715. DOI: 10.1016/j.dcan.2022.09.022. [来源](https://doi.org/10.1016/j.dcan.2022.09.022)

81. Liang Gou; Dongming Bian; Yulei Nie; et al. Hierarchical Resource Management for Mega-LEO Satellite Constellation. Sensors, 2025, 25(3): 902. DOI: 10.3390/s25030902. [来源](https://doi.org/10.3390/s25030902)

82. Elad Denenberg. Satellite closest approach calculation through Chebyshev Proxy Polynomials. Acta Astronautica, 2020, 170: 55–65. DOI: 10.1016/j.actaastro.2020.01.020. [来源](https://doi.org/10.1016/j.actaastro.2020.01.020)

83. Nicholas Ravago; Brandon A. Jones. Risk-aware sensor scheduling and tracking of large constellations. Advances in Space Research, 2021, 68(6): 2530–2550. DOI: 10.1016/j.asr.2021.04.042. [来源](https://doi.org/10.1016/j.asr.2021.04.042)

84. Phasawee Saingyen; Sittiporn Channumsin; Suwat Sreesawet; et al. Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques. Aerospace, 2023, 10(6): 543. DOI: 10.3390/aerospace10060543. [来源](https://doi.org/10.3390/aerospace10060543)

85. Simon Burgis; Lukas Rohrmüller; Martin Michel; et al. Simulation of satellites and constellations for the assessment of collision avoidance operations. CEAS Space Journal, 2023, 15(5): 655–670. DOI: 10.1007/s12567-022-00471-y. [来源](https://doi.org/10.1007/s12567-022-00471-y)

86. Zeno Pavanello; Luigi De Maria; Andrea De Vittori; et al. CAMmary: A review of spacecraft collision avoidance manoeuvre design methods. Acta Astronautica, 2025, 236: 770–789. DOI: 10.1016/j.actaastro.2025.07.027. [来源](https://doi.org/10.1016/j.actaastro.2025.07.027)

87. Thomas Uriot; Dario Izzo; Luís F. Simões; et al. Spacecraft collision avoidance challenge: Design and results of a machine learning competition. Astrodynamics, 2021, 6(2): 121–140. DOI: 10.1007/s42064-021-0101-5. [来源](https://doi.org/10.1007/s42064-021-0101-5)

88. Consultative Committee for Space Data Systems. Conjunction Data Message. CCSDS 508.0-B-1, June 2013; Technical Corrigendum 2, October 2021; accessed 10 October 2026 (inherited access date). https://ccsds.org/publications/bluebooks/entry/3064/. [来源](https://ccsds.org/publications/bluebooks/entry/3064/)

89. SpaceX. Starlink Collision Avoidance CONOPS. Official operational documentation; accessed 10 October 2026 (inherited access date). https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/. [来源](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/)

90. Louis Breger; Jonathan P. How. Safe Trajectories for Autonomous Rendezvous of Spacecraft. Journal of Guidance, Control, and Dynamics, 2008, 31(5): 1478–1489. DOI: 10.2514/1.29590. [来源](https://doi.org/10.2514/1.29590)

91. Ping Lu; Xinfu Liu. Autonomous Trajectory Planning for Rendezvous and Proximity Operations by Conic Optimization. Journal of Guidance, Control, and Dynamics, 2013, 36(2): 375–389. DOI: 10.2514/1.58436. [来源](https://doi.org/10.2514/1.58436)

92. Daniel Morgan; Soon-Jo Chung; Fred Y. Hadaegh. Model Predictive Control of Swarms of Spacecraft Using Sequential Convex Programming. Journal of Guidance, Control, and Dynamics, 2014, 37(6): 1725–1740. DOI: 10.2514/1.G000218. [来源](https://doi.org/10.2514/1.G000218)

93. Francisco Gavilan; Rafael Vazquez; Eduardo F. Camacho. Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation. Control Engineering Practice, 2012, 20(2): 111–122. DOI: 10.1016/j.conengprac.2011.09.006. [来源](https://doi.org/10.1016/j.conengprac.2011.09.006)

94. Zhenbo Zhao; Fan Wu; Jian Chen. Chance-constrained visual servoing MPC for non-cooperative spacecraft rendezvous. Aerospace Science and Technology, 2026, 169: 111237. DOI: 10.1016/j.ast.2025.111237. [来源](https://doi.org/10.1016/j.ast.2025.111237)

95. Purnanand Elango; Abraham P. Vinod; Kenji Kitamura; et al. Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit. AIAA SCITECH 2026 Forum, 2026. DOI: 10.2514/6.2026-2446. [来源](https://doi.org/10.2514/6.2026-2446)

96. Mark Stephenson; Hanspeter Schaub. Two Approaches to Autonomous Spacecraft Inspection: Shielded Reinforcement Learning versus Probabilistic Roadmaps. The Journal of the Astronautical Sciences, 2026, 73: 89. DOI: 10.1007/s40295-026-00631-w. [来源](https://doi.org/10.1007/s40295-026-00631-w)

97. Astroscale. Astroscale’s ADRAS-J Achieves Historic 15-Meter Approach to Space Debris. Official mission release; accessed 10 October 2026 (inherited access date). https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris. [来源](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris)

98. Kyle Hundman; Valentino Constantinou; Christopher Laporte; et al. Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding. Proceedings of ACM SIGKDD, 2018: 387–395. DOI: 10.1145/3219819.3219845. [来源](https://doi.org/10.1145/3219819.3219845)

99. Junfu Chen; Dechang Pi; Zhiyuan Wu; et al. Imbalanced satellite telemetry data anomaly detection model based on Bayesian LSTM. Acta Astronautica, 2021, 180: 232–242. DOI: 10.1016/j.actaastro.2020.12.012. [来源](https://doi.org/10.1016/j.actaastro.2020.12.012)

100. Nils Kuhn; Bruno Sánchez Gómez; Natalia Moreno Blasco; et al. Validation-gated continual learning for anomaly detection in satellite telemetry. Acta Astronautica, 2026, 249: 971–985; assigned issue: December 2026. DOI: 10.1016/j.actaastro.2026.07.065. [来源](https://doi.org/10.1016/j.actaastro.2026.07.065)

101. Lars Herrmann; Marie Bieber; Wim J. C. Verhagen; et al. Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry. CEAS Space Journal, 2024, 16(2): 225–237. DOI: 10.1007/s12567-023-00529-5. [来源](https://doi.org/10.1007/s12567-023-00529-5)

102. Sascha Wanninger. Knowledge-based satellite failure detection, isolation and recovery (FDIR). CEAS Space Journal, 2026, 18(5): 991–1004. DOI: 10.1007/s12567-025-00651-6. [来源](https://doi.org/10.1007/s12567-025-00651-6)

103. Antony Gillette; Alan George. Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions. Journal of Aerospace Information Systems, 2023, 20(7): 387–397. DOI: 10.2514/1.I011208. [来源](https://doi.org/10.2514/1.I011208)

104. Chao Chen; Rui Xu; Shengying Zhu; et al. RPRS: a reactive plan repair strategy for rapid response to plan failures of deep space missions. Acta Astronautica, 2020, 175: 155–162. DOI: 10.1016/j.actaastro.2020.05.011. [来源](https://doi.org/10.1016/j.actaastro.2020.05.011)

105. Kathiravan Thangavel; Roberto Sabatini; Alessandro Gardi; et al. Artificial Intelligence for Trusted Autonomous Satellite Operations. Progress in Aerospace Sciences, 2024, 144: 100960. DOI: 10.1016/j.paerosci.2023.100960. [来源](https://doi.org/10.1016/j.paerosci.2023.100960)

106. Christopher John Lowe; Ruaridh Alexander Clark; Ciara Norah McGrath; et al. A delay-tolerant network approach to satellite pickup and delivery scheduling. Ad Hoc Networks, 2023, 151: 103289. DOI: 10.1016/j.adhoc.2023.103289. [来源](https://doi.org/10.1016/j.adhoc.2023.103289)

107. Changyuan He; Yunfeng Dong; Hongjue Li; et al. Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling. Remote Sensing, 2023, 15(6): 1577. DOI: 10.3390/rs15061577. [来源](https://doi.org/10.3390/rs15061577)

108. Nicola Muscettola; P. Pandurang Nayak; Barney Pell; et al. Remote Agent: to boldly go where no AI system has gone before. Artificial Intelligence, 1998, 103(1–2): 5–47. DOI: 10.1016/S0004-3702(98)00068-X. [来源](https://doi.org/10.1016/S0004-3702(98)00068-X)

109. Gregg Rabideau; Daniel Tran; Steve Chien; et al. Mission Operations of Earth Observing-1 with Onboard Autonomy. SMC-IT, 2006: 367–373. DOI: 10.1109/SMC-IT.2006.48. [来源](https://doi.org/10.1109/SMC-IT.2006.48)

110. Steve Chien; Joshua Doubleday; David R. Thompson; et al. Onboard Autonomy on the Intelligent Payload Experiment CubeSat Mission. Journal of Aerospace Information Systems, 2017, 14(6): 307–315. DOI: 10.2514/1.I010386. [来源](https://doi.org/10.2514/1.I010386)

111. NASA Jet Propulsion Laboratory. IPEX. Official project documentation; accessed 10 October 2026 (inherited access date). https://ai.jpl.nasa.gov/public/projects/ipex/. [来源](https://ai.jpl.nasa.gov/public/projects/ipex/)

112. Francesco Basciani; Luciana Rebelo; Patrizio Pelliccione. Reference architecture for autonomy and adaptivity in satellites. Journal of Systems and Software, 2026, 236: 112802. DOI: 10.1016/j.jss.2026.112802. [来源](https://doi.org/10.1016/j.jss.2026.112802)

113. NASA Goddard Space Flight Center. Core Flight System – Demo Bundle. Official software repository; accessed 10 October 2026 (inherited access date). https://github.com/nasa/cFS. [来源](https://github.com/nasa/cFS)

114. NASA. What is Starling?. Official mission documentation; accessed 10 October 2026 (inherited access date). https://www.nasa.gov/smallspacecraft/what-is-starling/. [来源](https://www.nasa.gov/smallspacecraft/what-is-starling/)

115. NASA. NASA Starling and SpaceX Starlink Improve Space Traffic Coordination. Official mission release; accessed 10 October 2026 (inherited access date). https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/. [来源](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/)

116. Patrick W. Kenneally; Scott Piggott; Hanspeter Schaub. Basilisk: A Flexible, Scalable and Modular Astrodynamics Simulation Framework. Journal of Aerospace Information Systems, 2020, 17(9): 496–507. DOI: 10.2514/1.I010762. [来源](https://doi.org/10.2514/1.I010762)

117. Steve A. Chien. Formal Methods for Trusted Space Autonomy: Boon or Bane?. NASA Formal Methods, Lecture Notes in Computer Science, 2022: 3–13. DOI: 10.1007/978-3-031-06773-0_1. [来源](https://doi.org/10.1007/978-3-031-06773-0_1)

118. Matthew Rantanen; Jalil Modares; Nicholas Mastronarde; et al. Performance of the Asynchronous Consensus Based Bundle Algorithm in Lossy Network Environments. IEEE SAM, 2018: 311–315. DOI: 10.1109/SAM.2018.8448984. [来源](https://doi.org/10.1109/SAM.2018.8448984)

119. Francesco Basciani; Arianna Fedeli; Daniele Masti; et al. A model-driven framework for supervised reconfiguration of satellite schedulers. Software and Systems Modeling, 2026. DOI: 10.1007/s10270-026-01426-1. [来源](https://doi.org/10.1007/s10270-026-01426-1)

120. Philipp Chrszon; Paulina Maurer; George Saleip; et al. Model checking of spacecraft operational designs: a scalability analysis. Software and Systems Modeling, 2025, 24(6): 1825–1846. DOI: 10.1007/s10270-025-01281-6. [来源](https://doi.org/10.1007/s10270-025-01281-6)

121. Dhiraj Bhattacharjee; Pablo G. Madoery; Aizaz U. Chaudhry; et al. On-Demand Routing in LEO Mega-Constellations With Dynamic Laser Inter-Satellite Links. IEEE Transactions on Aerospace and Electronic Systems, 2024, 60(5): 7089–7105. DOI: 10.1109/TAES.2024.3415571. [来源](https://doi.org/10.1109/TAES.2024.3415571)
