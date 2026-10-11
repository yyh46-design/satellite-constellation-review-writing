# 大型卫星星座智能管理与调度的跨层方法及工程实践综述

**English title:** A Review of Cross-Layer Methods and Engineering Practice for Intelligent Management and Scheduling of Large Satellite Constellations

## 摘要

大型卫星星座的持续运行依赖能力配置、任务调度和安全执行之间的协调。备份与补给决定资源何时可用，观测、传输及计算决定任务价值何时兑现，机动和异常处置则持续改变后续计划的执行条件。本文围绕这些决策依赖，综述长期能力配置与运维、动态任务及多资源联合调度、安全执行与异常恢复，以及跨层闭环协同的代表研究。以状态、决策变量、资源约束和完成事件为共同分析要素，比较求解分解、信息组织、学习辅助与计划更新的作用，并结合公开运营接口、软件实现和飞行资料分析工程证据。所讨论研究表明，扩展性改进分别作用于组合搜索、协调范围和策略训练，收益与计算、通信及预处理代价之间的权衡取决于具体模型；任务状态共享也不必然消除同一时段的资源竞争。联合资源建模使评价从局部活动推进到产品交付和服务恢复，而离散计划的可行性仍需与动力学、风险及执行条件对应。工程案例展示了不同范围的局部连接，其系统价值需要在一致的任务与事件场景中评价。最后讨论能力到位与业务恢复、资源承诺与计划修复、学习与约束检查及跨层验证等研究方向，为大型星座管理系统的设计与评价提供问题组织和方法选择依据。

**关键词：** 大型卫星星座；智能管理；任务调度；跨层协同；多资源耦合；自主运行

## Abstract

Sustained operation of large satellite constellations requires coordination between capability planning, mission scheduling, and safe execution. Spare assets and replenishment determine when resources become available; observation, transmission, and computing determine when mission value is realized; maneuvers and anomaly responses change the conditions for subsequent activities. This review organizes representative studies around these dependencies, covering long-term capability configuration and maintenance, dynamic multi-resource scheduling, safe execution and recovery, and cross-layer coordination. States, decision variables, constraints, and completion events provide a common basis for comparing decomposition, information organization, learning assistance, and plan updates. Public operational interfaces, software implementations, and flight reports are examined to characterize engineering evidence. The reviewed studies address scalability at different stages of combinatorial search, coordination, and policy training, with trade-offs in solution quality, computation, communication, and preprocessing that depend on the underlying models. Sharing completed-task states does not necessarily eliminate simultaneous resource competition. Joint resource models extend evaluation from individual activities to product delivery and service recovery, while discrete scheduling feasibility must be related to dynamics, risk, and execution conditions. Engineering cases demonstrate specific connections at different scales, motivating evaluation within consistent mission and event scenarios. Research directions include linking asset availability to service recovery, resource commitments to plan repair, learning to constraint checking, and component validation to cross-layer operation. The review provides an analytical basis for organizing management problems and selecting methods for large satellite constellations.

**Keywords:** large satellite constellations; intelligent management; mission scheduling; cross-layer coordination; multi-resource coupling; autonomous operations

---

# 第1章 引言

## 1.1 大型星座持续运行中的管理与调度问题

卫星星座把多个航天器的观测、通信与处理能力组织为持续提供的服务。随着任务请求、参与节点和资源依赖增加，运行管理需要同时回答三个问题：未来具备哪些可用能力，当前任务怎样分配和排序，以及计划受到扰动后怎样安全执行或恢复。《[Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts](https://doi.org/10.1016/j.asr.2020.08.009)》从传统运行流程和星座案例分析自动化与扩展性需求，说明星座规模变化会改变状态获取、协调和任务组织的成本。这一变化使管理对象从单星指令执行延伸到多个主体之间的任务和资源关系。

大型星座的管理困难并不只来自某一次优化问题的变量数量。卫星失效后，备用资产需要经过补给或转移才能形成可调用能力；观测任务选择后，还需要存储、处理及通信机会才能兑现产品价值；风险机动和异常退出又会占用资源或改变任务进度。配置、调度和执行因此具有双向依赖：上游决策限定下游的候选活动，下游消耗与异常则改变上游后续可用的状态。《[Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control](https://doi.org/10.2514/1.A34387)》、《[Joint Observation and Transmission Scheduling in Agile Satellite Networks](https://doi.org/10.1109/TMC.2021.3076088)》及《[Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions](https://doi.org/10.2514/1.I011208)》分别从库存、任务链和执行管理描述了这些依赖的一部分。

本文中的智能管理指利用状态监测、规划推理、优化、学习及主体间协调，对任务与资源变化形成可执行响应的管理能力。学习可以承担状态识别、候选生成或策略决策，优化和规则机制则可以处理资源竞争、动作条件及计划修复。它们承担的职责决定了系统如何响应变化，算法名称本身不足以说明形成了何种自主能力。因此，本综述以决策问题及其连接关系组织方法，重点分析收益、计算和通信成本、物理约束与验证证据之间的对应。

## 1.2 已有综述与本文的分析重点

观测调度综述已经形成较完整的问题表示和求解分类。《[Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions](https://doi.org/10.1109/JSYST.2020.2997050)》围绕敏捷观测任务的运行约束、收益定义及自主调度等变体，整理精确方法、启发式、元启发式和机器学习。《[Satellite Scheduling Problems: A survey of applications in Earth and outer space observation](https://doi.org/10.1016/j.cor.2024.106875)》进一步按应用与问题变体组织对地及外层空间成像、通信任务。这些综述为任务建模和算法比较提供了基础。本文在此基础上关注任务决策与能力供给、产品交付及执行恢复之间的依赖，使调度结果能够对应具体的运行完成事件。

运行自动化和巨型星座管理综述则连接了规模、架构与物理环境。前述自动化运行综述讨论地面操作方式与自动化范式；《[Managing Mega-Constellations: A Starlink-Informed Review](https://doi.org/10.3390/sym18071141)》从Starlink的轨道架构和动力学出发，分析分层管理、动态拓扑与构型保持。这类工作已经强调系统组织与单星控制的联系。本文进一步把备用与服务资源的到位条件、任务链中的资源承诺以及异常后的计划更新放入共同的比较结构，分析不同层级之间传递的状态如何改变可执行任务集合。

自主协同与安全执行也已有专门综述。《[Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges](https://doi.org/10.1016/j.actaastro.2025.10.018)》按照智能体类型、架构、通信、任务管理和应用组织研究，并讨论健康状态与任务要求的结合。《[CAMmary: A review of spacecraft collision avoidance manoeuvre design methods](https://doi.org/10.1016/j.actaastro.2025.07.027)》比较规避机动的模型与设计方法。本文采用与这些分类互补的角度：把健康与风险信息对应到可用能力、活动准入条件及恢复动作，再分析这些变化怎样进入任务调度。这里的分析重点是跨层状态、决策及证据之间的关系，而不是将某种智能体架构、健康管理主题或机动算法视为唯一主线。

## 1.3 综述范围与组织方式

本文采用问题驱动的叙述性技术综述。资料检索围绕星座运行、任务规划与调度、在轨服务、自主协同、异常恢复及碰撞规避等主题，并结合已有综述和代表研究追踪相关来源。学术论文用于分析变量、约束、求解过程及原文实验；运营接口和任务资料用于分析实际状态转换、资源承诺和已经执行的功能。文献身份通过正式题名与DOI对应，重复出现的论文及资料按唯一来源统计。

综述以大型星座持续运行的决策关系为范围，覆盖长期能力配置与运维、观测及服务任务调度、安全执行与异常恢复，以及这些问题之间的接口。通信与计算研究主要在其影响任务选择、资源分配或产品交付时进入分析。单星和小规模协同试验用于解释状态反馈、软件职责与执行条件，其规模和实际动作范围在相应论述中标明。卫星数、请求密度、候选机会、规划时域及协调范围共同构成规模条件。

本文的分析围绕三项工作展开。首先，按能力配置、运行任务调度、执行与恢复建立层级结构，并以状态、变量、约束和反馈对应代表模型。其次，沿求解方法、信息组织、资源耦合和计划更新比较技术路线，解释改进发生在哪个成本环节及何种任务完成阶段。最后，把数学与任务仿真、软件测试、运营资料和飞行证据对应到实际验证对象，从比较结果归纳跨层连接的研究问题。

全文共五章。第2章建立系统框架与建模要素；第3章介绍各层代表方法及跨层协同；第4章综合比较扩展性、资源耦合、信息条件和工程证据，并讨论研究方向；第5章总结主要认识。

---

# 第2章 系统框架与问题建模

## 2.1 大型星座运行管理的对象与决策层级

星座运行管理的对象包括航天器及服务设施、任务请求、运行资源和安全条件。不同问题改变这些对象的方式有所差异：构型和备用策略改变未来可提供的能力，任务分配安排既有资源，控制与恢复动作则改变当前执行状态。本文依据决策所改变的对象及其影响范围，组织三个相互联系的层级。

**长期能力配置**选择轨道构型、备用资产、补给途径和服务设施，决定未来能够提供的任务能力；**运行任务调度**在给定资产和状态下选择任务、执行主体及活动时序，并响应需求与资源变化；**执行与恢复**将计划转化为轨道、姿态、载荷和通信动作，处理执行误差与异常。配置层向调度层传递资产位置、可用时刻和能力，调度层向执行层传递活动及资源需求，执行结果再更新任务进度、资源余量和健康状态。这一划分是本文用于归纳文献的分析结构。

层级边界取决于决策变量。分阶段构型重构改变后续覆盖机会，观测排序分配既有机会，控制输入改变活动执行过程。《[Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods](https://doi.org/10.2514/1.A35990)》与《[Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation](https://doi.org/10.1613/jair.1.16997)》分别对应前两类问题。两者都涉及时间和资源，但其输出状态不同。滚动时域、集中求解或分布式协调是可以跨层采用的组织方式。

## 2.2 运行架构与信息组织方式

运行架构规定决策在哪里形成、使用哪些信息以及怎样协调。**集中式架构**由具有全局或近全局信息的节点统一安排任务与资源；**分层式架构**按照职责或协调范围分配计算；**分布式架构**由多个主体根据局部状态和交换的消息共同形成决策。智能体综述《[Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges](https://doi.org/10.1016/j.actaastro.2025.10.018)》将架构、智能体推理方式和通信作为不同分类要素，说明学习或规则推理并不单独决定系统的集中程度。全局协调范围、局部响应时间和通信需求需要分别描述。

信息条件还包括任务是否预先给定、其他主体的能力是否可见、共享内容是否包含计划意图，以及状态更新何时到达。去中心化观测分配研究《[Decentralized Observation Allocation for a Large-Scale Constellation](https://doi.org/10.2514/1.I011215)》比较了请求满足与竞争信息的共享；单星策略复用研究《[Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations](https://doi.org/10.2514/1.A35736)》则通过共享已成像及下传状态减少重复活动。前者用于分配协商，后者主要更新已经完成的任务记录。共享历史状态与确认未来资源使用具有不同的协调含义。

通信接触图、管理拓扑和任务冲突图也承担不同职责。接触图表示信息或数据在何时能够传递，管理拓扑表示节点的管理责任，任务冲突图表示哪些活动竞争同一资源。《[A delay-tolerant network approach to satellite pickup and delivery scheduling](https://doi.org/10.1016/j.adhoc.2023.103289)》与《[Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation](https://doi.org/10.34133/space.0248)》分别处理前两类结构。管理域可以决定由谁汇集信息，可执行通信机会和需要共同求解的任务集合仍由相应物理与冲突关系确定。

软件架构进一步规定计划怎样进入执行过程。《[Reference architecture for autonomy and adaptivity in satellites](https://doi.org/10.1016/j.jss.2026.112802)》采用监测、分析、规划、执行与共享知识（MAPE-K）反馈结构组织自主功能。它描述功能职责与状态更新，集中或分布式任务分配则描述决策信息及协调范围。模型比较因此需要同时记录决策的形成位置和进入执行软件的接口。

## 2.3 运行状态、目标函数与资源约束

本文把模型输入归纳为四类状态：卫星及设施的轨道、姿态、健康和载荷能力；任务的目标、优先级、时间窗口及完成条件；能源、推进剂、存储、计算和通信资源；需求变化、失效、轨道预测误差及观测环境等不确定因素。与之对应，决策变量可以是构型位置、补给量、任务指派、活动时刻、数据路径或控制输入。敏捷观测综述《[Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions](https://doi.org/10.1109/JSYST.2020.2997050)》中对时间表示、运行约束和收益变体的整理，为对应任务变量及约束提供了具体基础。

表1按本文的层级结构整理模型要素。其最后一列用于分析模型之间需要传递的状态，各论文实际实现的连接范围在第3章和第4章分别讨论。

**表1 星座管理各层的状态、决策、约束与反馈**

| 决策层级 | 主要状态与输入 | 典型决策变量 | 主要约束 | 向其他层传递的结果与反馈 |
| --- | --- | --- | --- | --- |
| 长期能力配置 | 构型、失效过程、库存、设施和未来需求 | 轨道位置、备份数量、补给通道和设施部署 | 覆盖需求、供应提前期、转移资源及维护预算 | 可用资产、到位时刻、可提供能力和成本；接收实际需求及失效记录 |
| 运行任务调度 | 任务窗口、可用能力、资源余量、接触机会和已有承诺 | 任务选择与指派、活动时刻、处理位置、传输路径和服务顺序 | 姿态或转移时序、能源/存储/计算/链路容量、完成期限 | 活动序列、资源需求、执行条件与任务分工；接收实际进度和资源变化 |
| 执行与恢复 | 轨道与相对状态、预测误差、健康状态及控制能力 | 机动或控制输入、执行模式、退出和恢复动作 | 动力学、终端状态、风险水平、控制边界及动作权限 | 实际消耗、完成或中止事件、剩余能力和恢复结果；触发计划或能力更新 |

资源可以表现为静态容量，也可以表现为活动引起的状态变化。《[Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control](https://doi.org/10.2514/1.A34387)》在库存状态中采用面内备星即时替换的近似；联合观测、传输与充电研究《[Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm](https://doi.org/10.1016/j.actaastro.2025.02.008)》则跟踪活动消耗与能源补充。这些表示分别服务于供给分析和运行活动安排。“已有备用资产”“资产已到位”和“资产具备执行能力”对应不同状态，可行任务集合取决于模型采用的可用性定义。

收益需要绑定明确的任务完成事件。成功排程、完成采集、生成合格信息产品和按时交付构成观测业务的不同阶段；到达服务目标、满足交会条件和完成维修或加注构成服务任务的不同阶段。相应目标可以评价阶段性收益、最终交付、等待时间或运行成本。转移路线研究《[Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit](https://doi.org/10.1007/s40295-026-00580-4)》还说明，访问排序中的代价需要对应出发状态、航天器质量和动力学过程。离散时序、资源动态、连续轨迹及风险约束各自决定模型中的不同可行性条件。

## 2.4 状态监测、规划执行与反馈机制

闭环管理把状态变化转化为后续决策的输入。监测模块形成状态估计或异常告警，计划管理模块识别受影响的活动与资源，执行模块实施调整，反馈再更新任务进度和可用能力。《[Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions](https://doi.org/10.2514/1.I011208)》以任务管理软件连接活动准入、资源与时间约束及失败后的应急计划。异常检出、故障隔离、动作完成与业务恢复分别对应不同事件，可以由不同模块处理。

任务记录需要同时保留计划状态和实际结果。对于观测，采集完成后还存在质量确认与交付；对于近距离服务，接近动作完成后还需确认终端状态和服务结果。Planet的《[Tasking API](https://docs.planet.com/develop/apis/tasking/)》将采集、质量评估和交付分开，并为相应灵活产品规定继续采集的条件。由此，执行成功是否使任务满足，需要按照原请求的完成要求判断，复采或恢复活动也要继承相应期限与资源限制。

反馈还可能改变活动集合和协调责任。载荷降级缩小后续可执行任务，机动消耗改变推进剂余量，安全退出使原任务停留在未完成阶段，通信预约的调整则改变已确认的资源使用条件。跨层协同的比较对象因此包括状态何时更新、哪些计划受影响以及新动作执行后怎样确认结果。第3章据此介绍模型和方法，第4章进一步比较它们的成本、条件与验证证据。

---

# 第3章 多层次管理、调度与执行方法

## 3.1 长期能力配置与运维决策

大型卫星星座在投入运行后，需要持续调整其轨道构型、备用资源和维护安排，以适应任务需求变化及卫星失效。与运行层面对既有卫星和任务进行分配不同，长期运维决策首先要确定哪些能力可以被持续提供：包括不同区域和时段的覆盖能力、故障后的补位能力，以及在轨服务航天器能够及时到达目标的能力。这类问题通常涉及不同时间尺度的耦合决策。构型重构直接改变卫星轨道与覆盖特性；备份与补网需要考虑随机失效和供应提前期；在轨服务设施配置则进一步受仓库位置、服务船数量及轨道转移成本影响。因此，相关研究的共同点并不是采用同一种优化算法，而是将未来运行需求转化为当前的部署、维护或资源投入决策。

在轨道构型方面，研究首先从既有星座向目标构型的转移过程入手。Appel等在《[Optimization of satellite constellation reconfiguration maneuvers](https://doi.org/10.1016/j.actaastro.2014.02.016)》中将多卫星轨道转移作为耦合优化问题，比较联合确定终端条件与分别优化单星转移的策略。其代表性算例显示，考虑卫星之间的终端构型关系可以带来推进剂节省。这类研究强调的是由当前构型实现给定目标构型所付出的机动代价，而不是直接优化长期任务收益。针对区域观测需求，Lee和Ho在《[Regional Constellation Reconfiguration Problem: Integer Linear Programming Formulation and Lagrangian Heuristic Method](https://doi.org/10.2514/1.A35685)》中将新构型设计与卫星向目标轨道位置的分配共同表示为双目标整数线性规划，在区域覆盖收益和轨道转移成本之间寻找折中。由于直接求解在问题规模增大时计算负担较高，作者进一步利用分配问题的结构构建拉格朗日松弛启发式方法。两项研究分别突出轨道转移的耦合优化和覆盖—机动成本的联合权衡，说明构型调整的评价不能只看重构后的几何覆盖，还需要考虑完成这一构型所需的机动资源。

当观测需求随任务阶段发生变化时，一次性重构又可能不足以描述全寿命运行过程。Lee等在《[Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods](https://doi.org/10.2514/1.A35990)》中将星座构型作为分阶段变化的决策对象，建立能够同时选择各阶段构型和转移安排的整数规划模型，并通过短视决策与滚动时域策略降低直接求解的复杂度。其研究在预先已知目标区域的确定性场景中比较多阶段、单阶段和不重构策略，并利用飓风Harvey相关数据构造观测案例。与单次重构不同，多阶段方法使不同时刻的覆盖收益和卫星位置变化共同进入决策，但也引入了阶段划分、未来需求信息和跨阶段机动成本等新的建模条件。这类研究可用于说明长期部署并非一次性静态设计；不过，确定性多阶段优化与运行中未知需求的在线响应仍是不同问题。

除了主动重构，卫星随机失效后的备份和补网构成长期能力维护的另一条研究路线。研究《[Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control](https://doi.org/10.2514/1.A34387)》将地面库存、停泊轨道库存与轨道面内备份组织成多级库存网络，利用库存控制策略描述备份数量和补货触发条件，并将轨道面间相对漂移引起的补给等待时间引入分析。作者通过25组参数案例及重复的多年随机仿真评价解析库存模型，为备份规模与长期成本的联合设计提供了依据。需要注意的是，其模型把轨道面内备份视为能够立即接替失效卫星，未显式计入某些构型下实际补位机动的时间。因此，库存层面的供应满足率与星座业务中断后的真实恢复时间不是完全相同的指标。

围绕备星如何进入目标轨道面，Kim等在《[Replenishment Strategy for Satellite Constellation with Dual Supply Modes](https://doi.org/10.2514/1.A36281)》中进一步区分两种供应途径：主通道先将备星送入停泊轨道，再利用星上推进实现轨道面转移；辅助通道则直接将备星注入目标轨道面。作者建立具有补给时间窗口的参数化库存策略，并分别从星座运营方和发射服务方的角度优化供应链配置。与多级库存研究主要刻画备份位置、需求和补给时间不同，双供应通道模型将发射与轨道转移方式纳入运营决策，使快速直接补网和可能具有成本优势的间接补网之间的权衡成为核心问题。两类模型均可用于维护策略评价，但其响应时间计算依赖不同的补给过程，不能直接将库存数量相同的方案视为恢复能力相同。

备用资源的部署已经进入实际星座运维。Iridium在《[Iridium Adds to Constellation Resilience with Launch of Spare Satellites](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites)》中报告于2023年5月新增部署5颗备星。该实践为备份配置提供了工程背景，也使库存模型的评价需要与恢复过程相联系：备用资产的数量描述冗余水平，所在位置及转移条件影响补位时间，投入可用状态后才能承担原有业务。因而，比较维护策略时可以同时报告备份规模、补给等待和服务恢复，解释配置成本怎样转化为连续运行能力。

仅依赖新卫星补网还可能忽略既有失效卫星的可恢复价值。《[On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation](https://doi.org/10.2514/1.A36684)》同时考虑部署新星和通过在轨服务恢复失效卫星两种维护行动，将运营方维持星座服务水平、控制维护成本的目标与在轨服务方确定服务价格及能力的目标组织为双目标优化问题。在作者设置的现实规模数值案例中，相对于不使用在轨服务的基准策略，部分联合方案的年度维护成本降低最高约14.5%，而方案选择还受到可通过服务恢复的故障比例和服务定价影响。该结果表明，维护策略不仅由物理可达性决定，还涉及运营商、发射服务和在轨服务提供方之间的经济协调。这里的成本变化属于特定失效、价格和服务模型下的数值结果，不能直接视为所有低轨星座应用在轨服务后的普遍收益。

当维护行动需要服务航天器和轨道仓库支持时，设施布局本身也成为需要提前确定的能力配置变量。《[Orbital Facility Location Problem for Satellite Constellation Servicing Depots](https://doi.org/10.2514/1.A35691)》研究仓库位置、客户分配和相关推进需求的选择，将轨道转移代价与设施配置决策联系起来。在此基础上，Choi和Ho的《[Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers](https://doi.org/10.2514/1.A36386)》进一步允许仓库轨道位置在连续空间中调整，将仓库配置和客户服务顺序构造成混合整数非线性问题，再交替求解整数规划子问题与连续非线性优化子问题。作者以GPS星座服务案例分析该方法，表明离散设施选址与连续轨道位置优化可以采用不同的分解策略。两项研究的区别在于设施候选空间及服务路径的表达方式：固定候选仓库便于利用网络或离散优化结构，而连续位置设计增加了可调整自由度，也使转移代价与轨道位置之间的耦合更加显著。

服务设施部署后的实际运行仍受到需求出现时间和目标可达性的影响。《[Deployment of On-Orbit Service Vehicles Using a Fuzzy Adaptive Particle Swarm Optimization Algorithm](https://doi.org/10.1155/2021/6644339)》通过多层优化分别处理服务航天器部署轨道、任务分配、起始时刻和简化交会成本，使用模糊自适应粒子群等方法搜索服务船配置。另一项《[Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties](https://doi.org/10.2514/1.A34978)》则针对需求随时间逐步显现的在轨服务运行，利用混合整数规划与滚动时域安排服务航天器、仓库以及补给和任务活动。前者重视预部署方案是否能够在给定轨道条件下覆盖一组潜在客户，后者强调不确定需求到达后如何调整设施与物流操作。相比传统地面库存，轨道服务能力还取决于服务船所在轨道、推进方式、可用推进剂和客户在具体历元的状态，因而更难以用单一静态容量指标描述。

长期能力配置研究分别从轨道重构、备份库存、补网方式和在轨服务设施等方面描述未来可提供的能力，其目标涉及覆盖收益、推进剂、补给及时性及维护成本。比较这些模型时，可以分析配置决策怎样改变未来可执行的任务集合，以及能力投入需要付出哪些资源和经济代价。动态调度进一步在具体任务窗口与运行状态下安排这些资源，使长期配置与日常运行通过可用资产、响应时间和任务需求相互连接。

---

## 3.2 动态任务与多资源联合调度

运行期调度选择任务、执行主体和活动时序，并处理观测、传输、计算或轨道服务之间的依赖。相关研究可以沿四个交叉维度组织：**求解方法**说明怎样处理组合搜索，**信息组织**说明谁掌握哪些状态并承担协调，**资源耦合**说明哪些活动共同竞争资源，**计划更新**说明新任务或状态变化怎样进入已有方案。同一研究可能同时采用分解优化、分布式信息交换和在线更新，因而下文按具体问题连接代表方法，并在表2中对应其模型与验证条件。

对于给定任务集合和资源约束，混合整数规划能够统一表示任务是否执行、卫星分配和时间冲突，但卫星与候选任务增加后，直接求解的计算负担迅速增大。研究《[A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites](https://doi.org/10.1016/j.cor.2025.107259)》针对纳卫星星座中可由任意卫星执行的公共任务和必须由指定卫星执行的专属任务，建立考虑电池充放电约束的混合整数规划模型，并比较两种Dantzig–Wolfe分解形式。其结构化分解利用动态规划求解定价子问题，结合对偶稳定化、强分支和整数规划启发式改进求解过程。该研究体现了精确优化方法处理星座级任务耦合的一种途径：通过重新组织主问题与子问题，减少直接处理全部候选决策的负担，并保留离散模型内的优化界信息。面向更大规模的动态任务，Qin等在《[Lagrangian hierarchical mixed-integer programming for ultra-large-scale satellite scheduling under dynamic task delivery](https://doi.org/10.1016/j.asr.2025.12.008)》中将求解划分为任务分配和任务排序两个阶段：前者采用考虑任务冲突的动态多背包模型与拉格朗日松弛，后者在新增任务到达后利用回溯和递归策略修复已有序列。其数值实验涉及最多1000颗卫星及50—6000项任务，重点考察大规模条件下的收益与收敛时间。两项研究都利用问题分解提高求解效率，但前者侧重给定混合整数模型的列生成与优化界，后者更重视大规模任务分配及动态更新时的计算效率，二者的性能结论应结合各自的任务结构理解。

除优化规模外，调度决策由谁作出、需要共享多少信息，也是星座协同的重要区别。Parjan和Chien在《[Decentralized Observation Allocation for a Large-Scale Constellation](https://doi.org/10.2514/1.I011215)》中比较了集中式、广播式去中心化和高度去中心化的观测请求分配方法。其中，广播式方法又根据共享冲突信息或请求满足状态的不同形成多种协调策略，以有限的节点间信息交换减少重复观测和请求遗漏。作者在包含100个卫星代理、634个地面目标的一周调度算例中研究了相关方法的任务分配效果。这种比较表明，去中心化并不意味着完全取消通信；不同的信息共享程度会影响局部决策能否识别其他卫星已承担的任务。该文以固定的观测冲突间隔和简化的容量约束描述部分运行限制，还比较从头生成与增量修改持续计划。增量更新在所设实验中减少运行时间，同时增加重复观测，体现了保留既有安排与重新消解竞争之间的权衡。

针对更复杂的分布式优化，Zilberstein等在《[Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation](https://doi.org/10.1613/jair.1.16997)》中将星座观测调度建模为分布式约束优化问题（DCOP），并利用几何邻域分解（GND）识别彼此影响较强的任务和卫星，将大问题转化为多个局部子问题，再通过邻域随机搜索（NSS）协调局部决策。该研究在由200颗和108颗模拟卫星构成的两类星座中开展24 h调度实验，并在存储与下传约束下比较任务满足、计算时间及消息开销。成员知道公共请求和星座构型，但不掌握其他成员的完整任务执行能力，邻域分解据此估计相关任务供给。与Parjan和Chien主要比较信息共享架构不同，Zilberstein等侧重利用观测机会和任务冲突的几何结构降低分布式优化的求解难度。二者共同表明，分布式调度的效果同时取决于任务冲突的结构、局部求解方式和节点间的信息交换，而不能仅根据卫星数量判断算法的扩展能力。

当观测结果需要在限定时限内下传时，仅安排成像任务不能完整反映任务收益。He等在《[Joint Observation and Transmission Scheduling in Agile Satellite Networks](https://doi.org/10.1109/TMC.2021.3076088)》中联合考虑敏捷卫星的成像时间窗口和较短的传输时间窗口，将观测与传输资源分配建立为整数线性规划问题，并利用半正定松弛与遗传算法的组合寻找高收益调度方案。该研究关注成像起始时刻与数据传输机会之间的时序依赖，说明增加可用观测窗口并不必然意味着相应数据能够及时传回。进一步地，《[Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm](https://doi.org/10.1016/j.actaastro.2025.02.008)》将观测、传输和充电过程纳入同一规划模型，提出结合多背包任务分配与局部搜索的改进蚁群算法（LSE-ACO-MKTA），通过先分配候选任务、再改进时序方案来降低联合搜索的复杂度。与前一研究侧重成像和传输窗口耦合相比，后一研究进一步明确了能源消耗与补充对较长时域调度的作用，因而也改变了任务选择与资源竞争的判断依据。

商业观测服务将任务完成划分为更具体的业务状态。Planet的《[Tasking API](https://docs.planet.com/develop/apis/tasking/)》区分订单提交、排程、采集和交付时间，并根据目标覆盖、云量及其他产品要求评估影像质量。对于灵活任务产品，采集可以持续进行，直到获得符合要求的影像或订单期限结束。这使同一订单可能对应多次采集尝试，质量评估结果也成为后续任务安排的输入。由此，观测调度中的任务收益可以进一步区分为已采集数据、合格产品和按时交付产品；在联合调度模型中，复采需求还可以作为受原订单期限约束的后续活动安排。

地面通信资源还具有预约和配置更新条件。AWS Ground Station的《[Work with contacts](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html)》提供通信窗口的预约、取消和重新排程功能，并在预约时保存任务配置快照；随后对任务配置的修改不自动反映到已有预约，应用这类配置更新时需要取消并重新建立预约。Planet与AWS的文档分别描述观测服务和地面通信服务，其接口体现了两类不同的运行约束：前者以采集和质量评估推进订单状态，后者将可见窗口转化为已预约的天线资源。联合调度因此还需要处理资源承诺与计划更新之间的关系。

随着星上处理能力增强，调度目标还开始从“获取并传输多少图像”延伸到“何时生成有用的信息产品”。Soret等在《[Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing](https://doi.org/10.1002/sat.70082)》中研究异构计算资源条件下的观测与处理联合安排，分别建立考虑大气湍流引起的图像质量变化和能量预算的成像机会选择问题，以及在星上和地面处理器之间分配语义推理任务的问题。论文以船舶检测与定位为应用场景，并测试了YOLOv8在不同计算平台上的推理时间。与传统观测—下传联合调度相比，这类研究把图像质量、计算耗时和任务信息价值引入决策，使“已成像”“已下传”与“已完成目标识别”成为不同的运行结果。由此，多资源调度的研究对象不再局限于卫星执行某项活动，而逐渐涉及从数据获取到信息生成的任务链。

上述方法主要围绕给定时域内的资源分配展开，而在运行过程中，应急任务到达、卫星状态改变及通信机会受限还会使已有计划需要更新。Li等在《[Online scheduling of distributed Earth observation satellite system under rigid communication constraints](https://doi.org/10.1016/j.asr.2020.02.018)》中针对随机到达的紧急观测任务，提出改进的同步一致性任务包算法（m-CBBA）和异步算法（m-ACBBA），在传统任务协商中加入通信机会预测，并与两类合同网协议方法比较。其结果显示，两种改进方法在所设实验中的任务收益和应急任务安排方面优于对照方法，但同步与异步算法的选择还与通信成本有关：通信代价较高时，同步方法在收益和交互次数之间提供了较好的折中；通信成本较低时，异步方法能够获得更高的任务收益。这说明在线协同调度不仅要决定如何插入新任务，还必须考虑计划更新所依赖的信息何时能够传递到其他卫星。

另一类在线求解方法侧重减少新任务到达后的重新搜索成本。Qi等在《[Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites](https://doi.org/10.1016/j.eswa.2025.128502)》中采用滚动时域将动态应急调度转化为连续求解的静态子问题；利用深度强化学习生成任务序列和资源选择，再通过针对卫星调度设计的破坏—修复算子进行大邻域搜索。学习方法负责快速生成初始决策，组合优化则继续修复和改进方案，两者共同参与在线计划更新。与前述通过通信预测维持多星协商一致性的工作相比，该研究主要解决动态任务到达时的搜索效率和解更新问题，反映了在线调度中“协调信息”和“重新求解”两个相互关联但不同的计算环节。

对于星上自主决策，学习策略的部署方式同样影响系统规模与协调成本。Herrmann等在《[Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations](https://doi.org/10.2514/1.A35736)》中先在单星环境训练任务决策策略，再将同一策略应用到Walker星座中的不同卫星，以避免直接训练多智能体联合策略带来的复杂度。该研究比较自由通信、单跳视线通信、多跳视线通信和无通信四种设置，成员共享已经成像或下传的目标状态。视线通信的效果与构型连通性有关；即使采用自由通信，未共享未来计划意图也使同一决策时段保留重复选择目标的可能。该方法的扩展性来自单星策略复用和相对简单的协同机制，训练对象与多智能体联合策略有所区别。另一方面，Herrmann和Schaub在《[A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling](https://doi.org/10.3389/frspt.2023.1263489)》中基于Basilisk单星任务环境比较近端策略优化（PPO）、带资源屏蔽的PPO、优势Actor–Critic（A2C）、深度Q网络（DQN）、基于蒙特卡洛树搜索的训练方法及遗传算法。不同任务复杂度下，各方法在收益、稳定性与训练时间上的表现并不一致；其中搜索式训练在较复杂的敏捷观测任务中能够获得较好的解，但计算开销也更高。结合这两类工作可以看出，学习算法的比较既需要考察策略训练与在线执行的成本，也需要明确策略在多星之间如何共享任务状态和处理资源冲突。

在轨服务调度与观测调度共享任务选择、分配和排序等离散决策，但服务对象本身沿轨道运动，执行不同客户任务之间还需考虑轨道转移、服务持续时间和推进剂补充。《[Multi-orbit routing and scheduling of refuellable on-orbit servicing space robots](https://doi.org/10.1016/j.cie.2022.108852)》将多个服务航天器、运动中的客户和补给设施表示为时变任务网络，建立以加权完成任务数为目标的混合整数线性规划模型，使访问顺序与补给安排能够统一选择。Yin等在《[On-orbit refueling robust mission scheduling with uncertain duration for geosynchronous orbit spacecraft](https://doi.org/10.1016/j.cja.2025.103774)》中进一步考虑加注任务时长的不确定性，采用预算不确定集构造鲁棒调度模型，并使用混合哈里斯鹰优化算法搜索服务分配和访问序列。前者强调移动客户、补给设施与路径决策的联合表示，后者重点处理服务时间变化对既定计划的影响，说明在轨服务调度不仅存在空间路径约束，还受到任务执行时间不确定性的影响。

在服务顺序与轨道转移成本的衔接上，Apa等在《[Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit](https://doi.org/10.1007/s40295-026-00580-4)》中针对低轨多客户服务，将推力—漂移—推力转移与客户访问路径相结合，预先在出发时刻和服务航天器质量网格上计算转移代价，再采用插值与遗传算法优化访问顺序和加注方案。该研究考虑了J₂摄动、阻力、地影及质量变化，使组合路径优化能够使用与轨道状态相关的转移成本；同时，主优化中未直接纳入相位机动代价，作者在后续分析中单独估计了相关影响。因此，该类研究与以任务时间窗和通信容量为主要约束的观测调度存在本质差异：离散顺序优化所使用的轨道转移代价需要与动力学和终端条件明确对应，具体的交会安全性仍属于执行层需要进一步讨论的问题。

上述研究共同处理任务选择与资源竞争，但降低计算负担的位置有所不同：数学分解改变搜索问题的组织，局部信息交换改变协调范围，学习策略复用改变训练与部署方式。资源联合建模和在线更新还会改变任务完成事件与候选活动集合。表2据此整理代表研究，使这些交叉维度能够逐项比较。

**表2 动态任务与多资源调度代表研究的模型、信息及更新机制**

| 代表研究 | 优化对象与资源 | 信息范围与共享内容 | 求解与计划更新机制 | 验证场景 | 主要贡献与适用条件 |
| --- | --- | --- | --- | --- | --- |
| [A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites](https://doi.org/10.1016/j.cor.2025.107259) | 公共/专属任务；执行窗口与电池约束 | 统一数学模型中的公共/专属任务与电池状态 | 离线分支定价与动态规划定价；优化给定任务集合 | 纳卫星运行调度数值实例 | 结构化列生成保留优化界；优势取决于定价与模型结构 |
| [Lagrangian hierarchical mixed-integer programming for ultra-large-scale satellite scheduling under dynamic task delivery](https://doi.org/10.1016/j.asr.2025.12.008) | 观测任务分配与排序；任务冲突 | 统一分配模型中的候选机会、任务冲突和新增任务 | 拉格朗日分配后排序；新增任务以回溯和递归更新 | 最多1000颗卫星、50—6000项任务的数值算例 | 分配与排序分解面向规模和动态更新；并非通信协议比较 |
| [Decentralized Observation Allocation for a Large-Scale Constellation](https://doi.org/10.2514/1.I011215) | 观测请求分配；简化姿态间隔和请求容量 | 初始共享请求；迭代广播请求满足状态或竞争信息 | 广播协调；比较批量、从头持续规划与增量持续规划 | 100个代理、634个目标；批量及持续规划的单线程模拟 | 增量更新在所设实验中更快，但增加重复观测；消息内容与更新规则共同作用 |
| [Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation](https://doi.org/10.1613/jair.1.16997) | 观测请求、过境机会、存储与下传约束 | 公共请求与星座构型；本地资源；邻域共享满足状态 | 几何邻域分解与随机搜索；迭代调整局部任务安排 | 200颗与108颗模拟卫星、24 h调度 | 以邻域规模控制求解与消息代价；大算例保留任务满足率权衡 |
| [Joint Observation and Transmission Scheduling in Agile Satellite Networks](https://doi.org/10.1109/TMC.2021.3076088) | 敏捷成像与数据传输；窗口和时序耦合 | 统一整数模型中的观测和传输窗口及其时序 | 半正定松弛与遗传搜索；联合确定成像和传输方案 | 敏捷卫星网络调度仿真 | 下传可行性进入观测选择；收益含义取决于联合任务模型 |
| [Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm](https://doi.org/10.1016/j.actaastro.2025.02.008) | 观测、传输和充电；存储与能源动态 | 统一规划模型中的多星任务、存储和能量状态 | 多背包分配与局部搜索增强蚁群；联动活动及充电 | 联合调度与分配、局部搜索对照实验 | 能源补充改变长期任务竞争；搜索分解和资源耦合同时存在 |
| [Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing](https://doi.org/10.1002/sat.70082) | 成像质量、能量预算与异构处理器耗时 | 成像质量、能量预算及星上/地面处理平台耗时 | 分别选择成像机会和分配语义推理活动 | 船舶检测应用与处理器推理耗时测试 | 完成事件延伸至信息生成；处理平台成本影响资源选择 |
| [Online scheduling of distributed Earth observation satellite system under rigid communication constraints](https://doi.org/10.1016/j.asr.2020.02.018) | 动态紧急观测任务；可见窗口与通信机会 | 成员本地任务包；可通信机会预测及协商消息 | 同步/异步任务包协商；通信预测支持紧急任务更新 | 随机紧急任务与不同通信成本的计算实验 | 同步与异步的收益取舍随通信成本变化 |
| [Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites](https://doi.org/10.1016/j.eswa.2025.128502) | 大规模应急观测；任务序列与资源选择 | 滚动时域内已到达请求及候选资源 | 滚动时域；学习生成初解后大邻域破坏—修复 | 基于实际轨道与应用数据构造的调度实验 | 学习用于初解生成，组合搜索继续改进；成本由两环节共同构成 |
| [Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations](https://doi.org/10.2514/1.A35736) | 星座观测与下传；单星运行资源 | 成员本地状态；四种通信设置下共享已成像/下传记录 | 单星策略跨星复用；共享完成记录后更新目标集 | Walker星座任务仿真 | 复用训练策略；仅共享完成记录时仍有同一时段重复选择 |
| [A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling](https://doi.org/10.3389/frspt.2023.1263489) | 单星对地观测；不同复杂度的任务与资源约束 | 单星任务与资源观测；不涉及星间协调 | 学习、资源屏蔽或搜索式决策；比较训练与运行代价 | 单星仿真中的收益、稳定性与计算成本比较 | 提供同一环境的算法权衡；不是星座级联合策略验证 |
| [Multi-orbit routing and scheduling of refuellable on-orbit servicing space robots](https://doi.org/10.1016/j.cie.2022.108852) | 多服务船访问移动客户；推进剂与补给 | 统一网络模型中的运动客户、补给设施及转移参数 | 混合整数线性规划；联合选择访问路径和补给 | 基于在轨运行卫星构造的三个数值案例 | 将移动目标和补给纳入访问排序；物理可达性依赖网络代价表示 |
| [On-orbit refueling robust mission scheduling with uncertain duration for geosynchronous orbit spacecraft](https://doi.org/10.1016/j.cja.2025.103774) | GEO加注分配与访问顺序；服务时长不确定性 | 任务与客户信息；预算不确定集表示加注时长扰动 | 鲁棒模型与混合哈里斯鹰搜索；应对服务时长扰动 | 典型加注场景的算法与时长扰动实验 | 处理服务时长变化；鲁棒性与收益取决于不确定集设置 |
| [Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit](https://doi.org/10.1007/s40295-026-00580-4) | LEO多客户访问与加注；低推力转移及质量变化 | 客户轨道及预测转移代价；出发时刻与质量网格 | 插值代价与遗传算法；优化访问顺序和加注方案 | 低推力轨道与多客户路线数值研究 | 连接路线与动力学代价；主优化未直接计入相位机动成本 |

表中，LEO为低地球轨道，GEO为地球同步轨道。统一模型输入说明哪些状态共同进入数学模型；它与优化器的物理部署位置分别描述。求解分解说明计算如何组织，分布式协调说明哪些主体交换哪些信息，批量或在线更新说明计划何时改变。这些属性可以同时存在于同一研究中。数值算例、单星仿真和星座仿真的结果分别对应其模型与场景。

观测调度从请求分配扩展到传输与信息生成，服务调度则把移动客户、补给和转移代价带入访问排序。Planet与AWS的接口进一步表明，复采和预约更新会改变任务及资源状态。由此，调度收益需要对应明确的完成阶段，计划更新也需要处理已执行活动和已承诺资源。下一节讨论轨道与控制条件怎样约束这些计划的实际执行。

---

## 3.3 安全执行与异常恢复

任务调度规定卫星应执行的活动及其时间顺序，执行层还需持续满足轨道、姿态和运行资源条件。对地观测涉及指向、姿态转换与能源约束，在轨服务包含转移、接近和交会，密集星座运行则需要评估与其他空间目标的接近风险。执行中的姿态异常、载荷故障或通信中断又可能改变可用能力，使原计划需要修复。相关研究可沿风险预测、安全动作生成和异常恢复三个环节组织，并进一步比较环节之间传递的风险信息、动作条件与运行状态。

### 接近事件检测与风险筛查

对于需要长期运行的密集星座，接近事件评估首先面临计算规模问题。判断两颗目标是否在预测时域内发生危险接近，需要计算其相对距离随时间变化的极值；如果对每一对空间目标都采用足够小的固定时间步长传播与检查，计算代价会随目录规模迅速增加。《[Satellite closest approach calculation through Chebyshev Proxy Polynomials](https://doi.org/10.1016/j.actaastro.2020.01.020)》提出CATCH方法，通过切比雪夫代理多项式近似轨道相对距离函数，并利用多项式求根寻找最近接近时刻。作者在低轨、地球同步轨道、不同轨道类型配对及单目标对整个空间目录的场景中，将方法与传统近似算法和代理优化方法比较，重点讨论传播次数、计算时间及最近接近时刻误差。该研究表明，合理构造代理函数并对距离极值求解，可以降低逐点搜索的负担；代理多项式的阶数、时间区间长度和误差控制共同决定检测精度，也是比较计算效率与事件覆盖时需要明确的条件。

除了精确计算候选事件，还可以通过前置筛查减少需要精算的目标组合。Saingyen等在《[Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques](https://doi.org/10.3390/aerospace10060543)》中比较Smart Sieve、CSieve及组合式CAOS-D筛查方法，并将筛查过程与CUDA并行计算结合，分别测试单星对全目录和全目录两两配对的接近评估。与不使用筛选器的计算过程相比，GPU执行能够显著减少筛查时间，但不同筛选器的漏检表现和并行资源需求存在差异：其试验发现Smart Sieve遗漏了部分事件，而另外两类方法在对应数据集上维持了筛查结果。由此可见，候选目标过滤和最近接近时刻求精关注不同指标，筛查阶段还必须报告被排除事件的核查结果。对于高密度星座，速度收益只有与候选覆盖率、漏检控制和后续精化成本一同报告才具有实际意义。

接近检测之后，还需要根据轨道预测误差和风险阈值确定是否采取规避措施。《[Simulation of satellites and constellations for the assessment of collision avoidance operations](https://doi.org/10.1007/s12567-022-00471-y)》以日益密集的低轨运行环境为背景，构建模拟卫星与星座的整体评估流程，以比较不同碰撞规避运行规则对系统的影响。其研究关注不仅由单个危险事件触发机动，还涉及由谁执行规避、何时执行及星座运行规则的选择。Pavanello等在《[CAMmary: A review of spacecraft collision avoidance manoeuvre design methods](https://doi.org/10.1016/j.actaastro.2025.07.027)》中进一步按照解析或数值求解、脉冲或连续推力、确定性或随机方法、机动时间和方向是否固定等维度分类现有规避设计方法，并对部分方法开展数值比较。两类研究分别从系统运行规则和单次机动设计出发，说明“检测到风险”“计算降低风险的机动”“将机动协调到其他任务中”是相互连接但不能互相替代的步骤。

实际避碰运行将这些环节组织为持续更新的流程。SpaceX在《[Starlink Collision Avoidance CONOPS](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/)》中公开了星历生成、接近筛查和机动规划的循环：筛查产生接近事件数据报文（Conjunction Data Message，CDM）后，星载系统依据最新的全球导航卫星系统（GNSS）状态预测重新计算碰撞概率与最近距离，并新增、修改或取消规避机动。文档还按照卫星的机动能力和运行状态设置不同的响应条件，对无法充分缓解的风险保留人工处置。该流程使风险估计、机动权限与计划更新相互关联，说明执行层需要持续处理新的状态信息及其对既定动作的影响。

### 轨迹与控制约束下的安全执行

对于交会与近距离操作，安全性不仅来自任务分配层的时间窗口，还需要在连续运动和控制输入下检查终端条件、视线限制、避碰距离等要求。《[Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation](https://doi.org/10.1016/j.conengprac.2011.09.006)》采用Hill–Clohessy–Wiltshire相对运动模型，在模型预测控制（Model Predictive Control，MPC）中引入视线约束与加性扰动，并将高斯扰动条件下的概率约束转化为可求解的代数条件；作者通过蒙特卡洛仿真比较标称控制与机会约束控制方法。与仅在名义轨迹上检查约束的策略相比，这类方法明确了扰动概率模型对允许风险水平的影响，但其约束满足声明需要与选用的线性相对动力学和扰动分布同时理解。针对非合作航天器的视觉交会，《[Chance-constrained visual servoing MPC for non-cooperative spacecraft rendezvous](https://doi.org/10.1016/j.ast.2025.111237)》将姿轨耦合与图像空间反馈结合，通过递推扰动估计和概率约束收紧处理目标翻滚、模型误差及测量噪声，并在数值与蒙特卡洛实验中评价跟踪性能。两项研究的共同点是通过显式不确定性模型改进约束处理，差别在于前者主要围绕相对运动和视线约束，后者进一步将视觉观测与姿轨耦合反馈纳入控制过程。

对于安全性要求更高的持续近距离操作，安全约束还需要说明在什么时间集合内成立。《[Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit](https://doi.org/10.2514/6.2026-2446)》面向近直线晕轨道的安全交会，研究通过连续时间逐次凸化处理机动与被动安全要求。这类研究关注推进中断等情形下的轨迹安全，与普通任务调度中只检查离散节点是否可达存在明显区别。该研究对应近直线晕轨道的动力学环境，可作为连续安全约束建模的相邻方法参照；应用到低轨星座时，需要按相应轨道环境重新定义和验证安全条件。

近年来，学习策略与基于优化的安全约束也开始结合。Stephenson和Schaub在《[Two Approaches to Autonomous Spacecraft Inspection: Shielded Reinforcement Learning versus Probabilistic Roadmaps](https://doi.org/10.1007/s40295-026-00631-w)》中研究低轨目标近距离巡检，在相同任务下比较带安全屏蔽的闭环强化学习与基于概率路线图和混合整数二次约束规划的开环轨迹。其安全屏蔽利用相对运动动力学限制可能导致碰撞的动作，路线图方法则搜索满足巡检与几何约束的航迹。高保真模拟比较显示，路线图方案在燃料和时间的权衡上具有优势，但求解代价更高且采用离线开环规划；学习策略则能够以较低的在线计算开销形成闭环控制。这一结果说明安全执行不存在脱离任务条件的统一优胜算法：优化轨迹的质量、在线反应能力和安全证明的假设范围，需要共同参与比较。

异常情况下的安全退出为近距离执行提供了另一种评价对象。据Astroscale于2024年12月11日发布的《[Astroscale’s ADRAS-J Achieves Historic 15-Meter Approach to Space Debris](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris)》，ADRAS-J在当年11月30日接近失效火箭级至约15 m，随后因相对姿态异常触发自主中止，并在到达预定捕获起始点之前安全后撤。该次操作的验证对象是接近观测和异常退出。该案例将名义接近轨迹与异常响应联系起来：当状态信息偏离预期时，执行系统需要改变动作并进入安全状态，任务评价则分别记录已完成的观测、未完成的接近阶段和退出结果。

### 异常识别、故障隔离与计划恢复

航天器运行中的异常处理通常始于遥测状态变化的识别，但异常告警并不直接给出故障原因或可执行恢复动作。Hundman等在《[Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding](https://doi.org/10.1145/3219819.3219845)》中利用长短期记忆网络预测遥测时间序列，再根据预测误差构造自适应阈值并抑制误报，使用SMAP与MSL相关遥测数据验证异常检测策略。后续研究《[Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry](https://doi.org/10.1007/s12567-023-00529-5)》对航天器异常检测的评价过程进行了重新检查，将真实Sentinel-1遥测与公开数据集结合，分析指标选择、事件后处理与简单基线对方法比较的影响。这两项研究评价遥测异常的识别效果，故障原因判定、恢复动作和跨星任务转移属于后续决策。相应指标需要区分异常检出、误报与漏报、故障隔离正确性及恢复结果，才能描述异常处置的不同阶段。

为了将诊断结果转化为执行动作，Wanninger在《[Knowledge-based satellite failure detection, isolation and recovery (FDIR)](https://doi.org/10.1007/s12567-025-00651-6)》中使用CLIPS规则系统，将状态感知、故障判别和恢复动作分成可以与既有星上软件接口交互的规则模块，并通过地面RaspTank rover导航障碍场景演示了从检测障碍到执行恢复动作的流程。在其Raspberry Pi原型设置中，约30个状态参数的事实生成和规则处理分别报告了毫秒级执行时间，但作者也明确指出完整FDIR配置在代表性飞行硬件上的性能尚待测定。与数据驱动检测器不同，规则式恢复的主要贡献是让特定故障条件与操作序列形成可检查的对应关系；其有效性则依赖规则覆盖、状态信息准确性以及实际执行平台的能力。

当异常导致原计划无法继续执行时，仅重新启动局部控制器可能不足以保持任务连续性。Gillette和George在《[Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions](https://doi.org/10.2514/1.I011208)》中提出基于任务时间窗、优先级、冲突类别及资源需求的Schedule Manager，并在任务失败时加载预先定义的应急计划，同时支持与core Flight System软件平台集成。论文报告了单元测试、功能测试和代码分析等验证，并在代表性开发板环境中开展实验。与规则式FDIR主要处理已识别故障后的局部动作相比，任务管理器进一步关注故障对计划时序和可用资源的影响，但预定义应急计划仍有适用范围，板级或软件测试也不能代替星座在轨多节点恢复的完整证据。

风险筛查、轨迹控制和故障恢复分别产生候选事件、安全动作与更新后的运行状态，星座管理需要将这些结果传递给任务决策。规避机动需要占用执行时间，并可能增加推进剂消耗，异常退出会改变服务任务的进度，部件降级则可能缩小后续可执行活动的范围。因此，安全性与任务完成应采用相互关联的评价指标：既考察风险缓解和约束满足，也记录被中断的活动、剩余资源以及重新安排任务所需的时间。这样才能把执行层的局部结果与星座持续提供服务的能力联系起来。

---

## 3.4 跨层耦合与闭环协同

长期配置、运行调度和安全执行处理不同时间尺度的决策，跨层协同需要使各层使用的状态与约束相互对应。配置层向调度层提供可用资产、服务位置和补给条件；调度层向执行层传递活动时序、资源需求与动作条件；执行产生的资源消耗、任务进度和异常状态又进入下一轮计划及维护决策。这里可沿资源可用性、任务与通信耦合、状态反馈和协调责任等接口分析已有研究，比较每项连接实际改变了哪些决策，以及通过何种实现或试验得到验证。

配置与任务调度之间的接口首先表现为资产何时可用。《[Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties](https://doi.org/10.2514/1.A34978)》通过设施与服务船的状态连接任务选择、补给和滚动决策；《[On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation](https://doi.org/10.2514/1.A36684)》则将新星补充和在轨服务恢复共同纳入维护安排。两者的连接变量分别侧重特定时段的可执行服务和长期能力维持。配置结果通过位置、可用时刻、资源余量及服务成本进入调度，需求与失效再触发相应更新。

在多星观测任务中，调度与信息传递也可能形成紧密耦合。Lowe等在《[A delay-tolerant network approach to satellite pickup and delivery scheduling](https://doi.org/10.1016/j.adhoc.2023.103289)》中提出接触图调度（Contact Graph Scheduling），利用包含时间变化通信机会的网络描述任务请求从产生到完成数据交付的过程。该方法将接触图路由与动态采集—交付问题结合，在决定由哪颗卫星采集数据时，同时考虑数据能够通过哪些星间及星地接触路径送达用户。与先独立生成观测计划、再把数据交给传输系统的串行处理不同，接触图调度使数据交付路径参与任务分配决策，目标直接关联请求到达与数据送达之间的时延。其模拟结果说明，这种联合考虑在一定接触可靠性条件下可能提高请求完成量，但性能也受时变链路预测和局部路由机制影响。这为跨层研究提供了一项明确的接口：任务效益不仅取决于卫星能否观测，还取决于观测数据是否可以在资源有限的时间网络中完成交付。

管理责任的更新又形成独立接口。《[Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation](https://doi.org/10.34133/space.0248)》通过动态管理域划分、切换时刻预测及局部重组处理管理关系随轨道运动的变化，评价对象是管理传输时延与拓扑维护。管理域规定信息由谁汇集和协调，接触图规定信息何时可传递，任务冲突图规定哪些决策需要共同处理。三类结构可以关联使用，但各自输出的管理关系、接触机会与冲突依赖需要保持对应。

当运行状态改变时，调度器还需要决定是否切换策略或者更新计划。《[Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling](https://doi.org/10.3390/rs15061577)》针对单颗敏捷对地观测卫星中观测、数据传输和能源子系统的相互影响，先预测反映不同资源瓶颈的状态变量，再建立知识规则，在观测优先、数据下传优先和能源优先等调度策略之间选择。该方法将资源状态预测直接用于后续任务安排，不再把电量、存储和下传能力只作为求解时的固定上限。论文通过与若干启发式和元启发式方法的模拟比较评价调度效果，为状态监控与计划选择之间的接口提供了具体例证。与多星管理拓扑研究相比，其反馈发生在单星子系统与单星任务计划之间，其比较重点是子系统状态如何影响策略选择；跨星任务转移还需要增加成员间的能力与任务状态交换。

单星飞行任务展示了资源反馈怎样进入实际运行。《[Mission Operations of Earth Observing-1 with Onboard Autonomy](https://doi.org/10.1109/SMC-IT.2006.48)》介绍EO-1通过Autonomous Sciencecraft Experiment将星上科学处理、规划与地面操作连接起来的经验。《[Onboard Autonomy on the Intelligent Payload Experiment CubeSat Mission](https://doi.org/10.2514/1.I010386)》则报告IPEX CubeSat利用持续活动规划与重规划安排数据处理和信息产品。JPL的《[IPEX](https://ai.jpl.nasa.gov/public/projects/ipex/)》项目说明进一步明确，星上图像分类与显著区域提取产生待下传产品，CASPER持续规划软件根据文件存储、CPU、电源和下传带宽更新活动。这些实践把数据内容分析、资源使用和在线计划联系起来，为比较星上处理与调度耦合提供了单星运行证据。

为了使自主决策能够长期运行，软件模块之间的职责与重配置方式也需要明确定义。《[Reference architecture for autonomy and adaptivity in satellites](https://doi.org/10.1016/j.jss.2026.112802)》基于系统性文献整理和专家验证提出航天器自主与适应性参考架构，将监测、分析、规划、执行与共享知识（MAPE-K）反馈思想同空间软件工程分区结合，并在NIMBUS卫星相关系统中实例化。其主要价值是将自主运行功能转化为可讨论、可复用的软件职责和交互结构，而不是单独提出某种任务分配算法。另一方面，Gillette和George在《[Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions](https://doi.org/10.2514/1.I011208)》中通过Schedule Manager在任务时间窗、资源与冲突约束下管理运行活动，并提供任务失败时加载预定义应急计划的机制。该软件与core Flight System集成，并开展单元和功能测试，显示计划执行与故障应对可以由明确的软件接口组织。前一研究侧重通用架构与分区，后一研究强调任务准入、执行顺序和计划回退的具体模块设计。

在多星协同层面，NASA的《[What is Starling?](https://www.nasa.gov/smallspacecraft/what-is-starling/)》介绍了四颗CubeSat开展的分布式航天器自主运行试验。该试验利用GPS观测电离层，成员星通过星间链路共享信息以维持一致状态，再协调选择后续优先观测和共享的GPS信号。与单星资源反馈相比，这一接口把成员星的局部测量结果传递给群体观测决策，使信息交换直接参与观测选择。其飞行证据对应四星试验中的状态共享与分布式决策，可与大规模观测分配研究共同用于分析信息范围、协调过程和验证规模。

跨运营方协调还需要交换轨迹意图并确认机动责任。NASA在《[NASA Starling and SpaceX Starlink Improve Space Traffic Coordination](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/)》中介绍，Starling 1.5通过与SpaceX共同设计的筛查服务提交轨迹、获取接近信息并接受机动责任，随后自主规划和执行机动。NASA的[任务说明](https://www.nasa.gov/smallspacecraft/what-is-starling/)明确将该事件描述为模拟接近测试。这个案例展示的连接包括轨迹提交、风险信息返回、责任确认及机动执行。它与星座内部的观测协商具有不同的协调对象：前者需要明确不同运营方的行动责任，后者主要协调成员之间的任务竞争和状态共享。

模型驱动的运行配置更新则提供了另一类较为严格的工程连接方式。《[A model-driven framework for supervised reconfiguration of satellite schedulers](https://doi.org/10.1007/s10270-026-01426-1)》将遥测监控、数字孪生模型、约束检查与配置生成联系起来，研究在人工监督下更新卫星机载实时软件进程调度器。作者使用13个进程和32个时隙等软件配置案例，开展专家评价和工具链测试，并明确指出尚未在真实卫星执行该配置更新。这里的scheduler是操作系统任务调度配置，而不是多颗卫星之间的观测请求分配；该研究展示了安全关键软件配置的约束检查与人工监督机制，其验证对象是机载进程调度配置。

跨层协同研究可以按接口的输入、决策和反馈进行比较。资源可用性连接配置与任务选择，时变链路连接观测安排与数据交付，子系统状态触发策略切换，成员间的信息共享支持协同观测，轨迹意图和责任确认支持跨运营方机动协调。上述连接分别作用于单星、星座内部及外部协作，具有不同的信息需求和验证对象。将健康状态表示为可用能力与动作条件，再传递到调度和执行，是连接这些研究的一项具体分析路径；相应评价需要记录状态变化怎样传播、哪些计划随之更新，以及执行结果如何再次进入管理决策。

---

# 第4章 综合评价与研究展望

## 4.1 扩展性来源与比较口径

表2所列研究表明，扩展性改进分别作用于组合搜索、协调范围和策略训练。分支定价与拉格朗日分解重新组织任务分配及排序问题，几何邻域分解利用观测机会和任务冲突的局部结构，单星学习策略复用减少直接训练多星联合策略的负担。这些机制可以组合使用，但它们改变的成本环节不同：数学求解效率、消息交换需求和训练复杂度分别构成相应方法的比较对象。

其中，《[A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites](https://doi.org/10.1016/j.cor.2025.107259)》在离散任务与电池模型中保留优化界，拉格朗日分层方法则把任务分配和动态序列更新分开，侧重大规模条件下的搜索与修复效率。相比之下，《[Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation](https://doi.org/10.1613/jair.1.16997)》同时讨论局部优化和通信开销，而《[Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations](https://doi.org/10.2514/1.A35736)》把规模适应性建立在策略复用及通信条件的比较上。由此，较多卫星参与实验说明该模型在相应场景中经过测试；扩展性的解释还取决于任务冲突、信息需求和更新过程怎样随规模变化。

在几何邻域分解研究的实验中，这一权衡具有明确的比较对象。《[Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation](https://doi.org/10.1613/jair.1.16997)》在小算例中比较最优解差距，在大算例中比较请求满足、最慢代理运行时间及总消息量。NSS-GND相对于广播式去中心化方法降低了运行和消息代价，大算例的任务满足率仍保留差距。这说明局部范围缩小可以同时减少求解与协调成本，但也改变可参与联合决策的候选集合。其结果支持模型内的质量—成本权衡，不等同于所有场景中质量和速度同步提高。

“大规模”的具体含义也随问题改变。千星观测分配、200星24 h分布式调度和多年随机失效库存模型分别增加了任务组合、协调节点和事件时域的复杂性。《[Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods](https://doi.org/10.2514/1.A35990)》还引入阶段及备选构型，《[Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control](https://doi.org/10.2514/1.A34387)》则依赖失效与补给过程。卫星数、请求数、候选机会、阶段数和仿真时域因而是不同的规模维度，当前这些异构实验支持解释方法各自解决的负担，尚不能组成统一的性能排序。

计算成本同样需要对应完整的求解流程。低推力服务研究将转移代价预计算与路线搜索分开，学习调度研究将训练与运行决策分开，而在线协商还消耗消息交换和冲突处理时间。单星算法比较《[A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling](https://doi.org/10.3389/frspt.2023.1263489)》显示，不同任务复杂度下的收益与计算成本并不保持同一排序。其中MCTS-Train的训练成本还包含搜索生成数据和Basilisk仿真回溯；去中心化观测分配研究的运行时间则来自单线程的分布式执行模拟。模拟器调用、训练开销和真实并行部署时延因此需要采用各自的口径。这些证据支持将预处理、训练、在线求解和协调成本分别解释，再按实际运行频率分析其总负担。表3把这一比较口径扩展到本文的各类管理问题。

**表3 不同管理问题的决策、结果与比较条件**

| 问题 | 主要决策 | 完成或有效性事件 | 主要成本 | 影响结论的条件 |
| --- | --- | --- | --- | --- |
| 长期能力配置与运维 | 构型、备份、补网和服务设施 | 覆盖能力形成、资产补位及业务恢复 | 机动、供应、设施与维护成本 | 失效过程、供应提前期及补位假设 |
| 观测及多资源调度 | 任务、窗口、处理与传输 | 采集、信息生成或按时交付 | 计算、存储、能源及通信 | 收益绑定的任务阶段、资源动态与任务到达过程 |
| 在轨服务调度 | 客户分配、访问、转移与补给 | 到达、交会或完成服务 | 时间、推进剂及转移代价生成 | 相位、终端条件与服务时长不确定性 |
| 安全执行与异常恢复 | 筛查、机动、控制与恢复动作 | 风险缓解、约束满足或安全退出 | 预测、求解、执行与任务中断 | 扰动模型、检查时间集合与机动能力 |
| 跨层协同 | 状态传播、计划更新与责任协调 | 资源记录一致、更新落实或任务恢复 | 消息、重规划及人工处置 | 实际连接的模块、节点范围及触发事件 |

## 4.2 资源耦合与物理可执行性

资源耦合的实质是改变任务可行集合和收益兑现阶段。表2中的请求分配模型主要选择观测机会；《[Joint Observation and Transmission Scheduling in Agile Satellite Networks](https://doi.org/10.1109/TMC.2021.3076088)》使下传机会参与成像选择；《[Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm](https://doi.org/10.1016/j.actaastro.2025.02.008)》进一步联合安排充电；《[Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing](https://doi.org/10.1002/sat.70082)》把质量和处理耗时纳入信息生成过程。这些扩展增加了活动间的依赖，也使原来可选的观测可能因后续资源不足而失去价值。它们建立了不同深度的任务链，收益需要按各自实际建模的完成阶段理解。

第3.2节的Planet与AWS案例又给出两类状态转换：产品质量决定订单是否满足以及是否继续采集，通信预约把可见机会转化为已承诺资源。接触图调度研究《[A delay-tolerant network approach to satellite pickup and delivery scheduling](https://doi.org/10.1016/j.adhoc.2023.103289)》则直接将数据送达路径纳入任务选择。综合来看，活动之间既存在物理依赖，也存在完成确认和资源承诺的依赖。重新安排某次采集或传输时，原订单的完成状态和已经确认的资源使用条件共同影响后续方案。以最终交付为目标的系统，因而需要把局部活动成功与整个任务链完成相联系。

长期维护也存在相似的资源状态差异。多级库存、双供应通道和服务集成维护分别描述备用资产、补给过程及失效资产恢复；Iridium备星部署说明备用资源确实可以作为运营配置的一部分。比较这些研究得到的共同认识是，冗余数量只是能力投入，位置、转移等待和恢复方式决定其何时能够承担业务。同等库存可以对应不同响应过程，维护成本降低与业务恢复加快也需要通过具体状态转换才能建立联系。

在轨服务将这一问题推进到连续动力学。《[Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit](https://doi.org/10.1007/s40295-026-00580-4)》将出发时刻、质量及低推力过程纳入路线代价，但相位机动在主优化之外另行估计；加注鲁棒调度则重点处理服务时长扰动。前者细化了转移成本，后者细化了时间不确定性，二者处理的是不同的执行条件。离散路线的优选可以支持任务排序，而其交会可行性还取决于终端状态和接近约束是否被相应模型覆盖。

安全执行研究进一步区分约束成立的范围。机会约束MPC的结论依赖相对动力学与扰动分布，安全屏蔽约束所允许的控制动作，连续时间交会方法则在所设轨道环境中处理持续安全要求。第3.3节中《[Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation](https://doi.org/10.1016/j.conengprac.2011.09.006)》与《[Two Approaches to Autonomous Spacecraft Inspection: Shielded Reinforcement Learning versus Probabilistic Roadmaps](https://doi.org/10.1007/s40295-026-00631-w)》分别展示了这些条件下的控制和规划权衡。资源条件、终端条件与安全条件对应不同可行性命题，跨层连接的关键是将它们转化为相互兼容的活动准入条件与执行反馈。

## 4.3 分布式协同和智能方法的适用条件

本文讨论的分布式观测分配方法，通过局部求解与必要的信息交换组织协调，其效果依赖共享信息与任务竞争之间的对应。表2中的去中心化观测分配比较共享请求满足状态和竞争信息，几何邻域分解则根据哪些决策彼此影响来组织局部优化。两者都将全局任务竞争转化为局部求解及信息交换，却采用不同的局部范围和消息内容。管理拓扑研究进一步处理管理责任的变化，接触图调度处理数据送达路径。这些方法分别解决任务竞争、管理组织和数据流动，不能仅按是否存在中央节点归为同一种协同机制。

通信条件会改变分布式方法之间的选择。《[Online scheduling of distributed Earth observation satellite system under rigid communication constraints](https://doi.org/10.1016/j.asr.2020.02.018)》的计算实验显示，较高通信成本下同步方法在收益与交互次数之间提供较好折中，较低通信成本下异步方法取得较高任务收益。单星策略复用的星座仿真则显示，视线通信的表现随构型连通性变化；成员仅共享已完成任务状态时，自由通信也不能消除同一时段的重复观测。两项研究分别说明通信机会和共享内容的作用，信息能够到达与未来行动已经协调是不同条件。通用多代理研究《[Performance of the Asynchronous Consensus Based Bundle Algorithm in Lossy Network Environments](https://doi.org/10.1109/SAM.2018.8448984)》中的重复分配与未分配现象补充了有损网络的风险参照，其网络实验不直接代表真实星间链路。由此，局部求解更快能否带来更及时的一致计划，取决于消息何时到达及冲突何时完成处理。

更新机制又会改变已共享信息的使用方式。《[Decentralized Observation Allocation for a Large-Scale Constellation](https://doi.org/10.2514/1.I011215)》的增量持续规划相对从头生成计划减少运行时间，同时增加重复观测；其不同广播策略的差异也与请求重新指派规则有关。结合仅共享已完成目标的学习部署研究可以看出，任务历史、当前分配和未来行动意图是不同信息。局部计划更新需要决定保留哪些承诺、撤销哪些活动，并通过相应消息让其他主体重新判断任务竞争。

学习方法在现有研究中承担的职责也有明显差异。学习辅助大邻域搜索先生成初解，再以组合搜索改善任务安排；单星策略复用把已训练策略部署到不同成员；单星算法比较则在共同环境中研究策略收益与训练代价。前两种方法分别以学习初解接入后续搜索、以单星训练接入多星部署，改进发生在不同环节；实际收益还取决于搜索改善和成员协调。对于执行控制，安全屏蔽又把可接受动作范围纳入策略运行。因而，学习与优化的结合应按候选生成、计划改善和动作约束等职责理解，其贡献不能仅由使用了哪一种学习算法概括。

感知模型还具有不同的输出责任。《[Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry](https://doi.org/10.1007/s12567-023-00529-5)》表明，数据处理和评价指标可以改变异常检测方法的比较结果。异常检出提供状态变化证据，恢复决策还需要故障含义、受影响能力和可用动作。综合任务学习与遥测研究可以看出，智能管理的系统收益来自模型输出被哪个后续模块采用，以及由此改变了哪些任务或动作；检测分数、调度收益和恢复结果需要沿这一依赖分别解释。

## 4.4 工程验证与研究结论的适用范围

第3章的工程案例表明，状态到决策、决策到动作的连接已在不同范围内得到实现或公开描述，但验证对象并不相同。Planet与AWS定义业务状态和资源承诺，Starlink公开风险信息与机动更新流程，IPEX和Starling则分别提供单星及限定多星任务中的运行证据。表4将每项资料对应到具体环节，区分接口规定、运营方报告和飞行任务中执行的动作。

**表4 工程案例所连接的运行环节与验证范围**

| 案例 | 连接的运行环节 | 公开证据中的实现或动作 | 验证范围 |
| --- | --- | --- | --- |
| [Iridium备星部署](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites) | 备份投入与在轨资产 | 运营方报告了备星部署 | 资产部署证据；补位过程和业务恢复仍是独立评价对象 |
| [Planet任务接口](https://docs.planet.com/develop/apis/tasking/) | 采集、质量确认、复采与交付 | 开发者文档定义订单及产品状态 | 业务流程与接口证据；内部排程算法及其性能需要技术资料 |
| [AWS Ground Station](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html) | 通信机会、资源预约与配置更新 | 服务文档给出预约操作和配置快照规则 | 已有预约的任务配置更新条件；不涵盖所有类型的预约修改 |
| [Starlink避碰CONOPS](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/) | 风险信息、机动更新及异常响应 | 运营方公开持续筛查与机动规划流程 | 运行职责与数据流；公开流程不构成统一基准中的算法比较 |
| [ADRAS-J近距离操作](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris) | 状态异常、自主中止与安全后撤 | 运营方报告实际接近和自主退出事件 | 特定近距离操作；报告中的捕获起始点尚未到达 |
| [IPEX](https://ai.jpl.nasa.gov/public/projects/ipex/) | 数据处理、资源状态与持续规划 | 飞行论文及JPL资料描述星上运行 | 单星数据处理与规划反馈；跨星调度需另行验证 |
| [Starling分布式自主运行试验](https://www.nasa.gov/smallspacecraft/what-is-starling/) | 局部测量、状态共享与观测选择 | NASA描述四颗CubeSat的协同观测试验 | 四星限定任务中的分布式决策；规模与任务范围明确 |
| [Starling 1.5协调试验](https://www.nasa.gov/smallspacecraft/what-is-starling/) | 轨迹交换、责任确认与机动执行 | NASA描述模拟接近测试中实际执行的自主机动 | 跨运营方协调试验；模拟风险事件与真实执行动作分别表述 |

跨案例比较首先得到的是不同反馈对象。Planet把质量确认连接到订单满足与后续采集，AWS把预约配置连接到通信资源使用，IPEX把数据处理及资源状态连接到活动重规划。三者分别反馈产品状态、资源承诺和机载活动状态。它们支持构造更明确的任务链，但目前这些案例没有共同的收益、时域及资源场景，无法据此判断哪一种调度算法性能更好。

飞行案例进一步展示了两种多主体协调。Starling分布式自主运行试验共享局部测量并选择后续观测，Starling 1.5则交换轨迹、确认机动责任并在模拟接近测试中执行机动。前者协调成员间的信息和观测选择，后者协调不同运营方的行动责任。二者分别落实了观测和安全机动中的局部连接，不能合并为同一次大型星座综合闭环验证。单星IPEX、四星Starling与跨运营方试验也不构成可以仅按节点数量排序的成熟度序列。

执行结果的解释同样需要与任务阶段对应。ADRAS-J的自主中止和安全后撤说明异常状态能够改变接近动作，但此次报告中的预定捕获起始点尚未到达。该案例中原任务推进与安全处置具有不同结果，安全退出的成功不应使未完成任务在评价中消失。Iridium备星部署则确认资产配置的实施，其转化为故障补位和业务恢复的过程仍需对应独立的时间与服务记录。两者共同提示，已实施管理动作和已恢复任务能力是不同的验证事件。

软件实现补充了飞行资料未覆盖的模块性质。《[Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions](https://doi.org/10.2514/1.I011208)》通过任务管理器与core Flight System的集成和测试检查活动管理及预定义应急计划；《[A model-driven framework for supervised reconfiguration of satellite schedulers](https://doi.org/10.1007/s10270-026-01426-1)》研究机载进程调度配置的受监督更新。它们分别连接任务活动管理和操作系统配置，测试结论对应各自软件对象。《[Model checking of spacecraft operational designs: a scalability analysis](https://doi.org/10.1007/s10270-025-01281-6)》进一步检查状态模型在给定规格下的性质及验证成本。这些证据能够支持模块与接口分析，完整任务收益和物理执行仍由相应任务实验回答。

现有代表方法和工程案例的证据由此呈现互补关系：调度仿真比较模型内的任务与资源权衡，软件测试检查模块交互及配置，飞行试验确认限定条件下的实际动作。本文所讨论的连接主要分布在不同任务与平台中，系统级结论还需要把这些接口放入一致的状态、任务和事件场景。评价重点因此是哪些输入实际改变了哪些计划、哪些动作已经执行，以及执行结果是否继续进入后续决策。

## 4.5 值得进一步推进的研究方向

前述比较指向四类连接问题。首先，长期能力配置需要更细致地表达业务恢复过程。库存模型中的即时替换近似、不同补给通道和服务恢复行动，对应不同的能力到位条件。将备用资产、转移到位、载荷可用与业务恢复表示为连续的状态转换，可以研究同等备份投入在不同位置和失效条件下恢复多少服务。关键比较是静态容量近似与显式恢复过程在共同需求场景中产生的任务损失、恢复时间和维护成本差异。

其次，动态调度需要连接任务确认、资源承诺与计划修改。观测质量不合格、已有通信预约的配置变化和安全退出分别改变任务集合、资源使用条件及执行状态。在相同请求与事件序列下比较重新求解、局部修复和分布式协商，可以分析更新速度、计划变动与最终交付之间的权衡。跨运营方活动还增加了责任确认：轨迹或机动意图改变后，各方已确认的行动怎样保持一致，是星座内部任务分配之外的协调问题。

第三，学习与优化的联合研究需要沿模块职责检验收益。对于初解生成，关键是其对后续搜索成本和最终方案的影响；对于异常识别，关键是误报与漏报怎样改变恢复活动和服务损失；对于控制策略，关键是安全检查在状态偏离训练条件时能否维持规定的动作边界。需求分布变化、通信受限和资源降级可以作为共同扰动，结合训练代价、在线时限与回退结果，判断改进来自哪个环节。

最后，工程验证需要逐步连接已经分别展示的功能。单星资源反馈、四星观测协同、跨运营方机动协调及任务管理软件提供了不同范围的实现证据。下一步可以在共同任务链中传递配置状态、活动序列和执行结果，检查资源记录、责任及任务完成事件能否保持对应。软件在环、硬件在环与限定飞行试验分别验证计划更新、执行时序和实际动作，再扩大节点与事件范围。这一方向的核心问题是：能力降级、任务竞争和安全动作同时发生时，已有局部连接能否支持及时且一致的系统响应。

---

# 第5章 结论

大型卫星星座的智能管理与调度涉及能力配置、任务组织和安全执行之间的连续决策。本文按照长期能力配置与运维、动态任务及多资源联合调度、执行与异常恢复三个层级整理代表研究，并通过状态和约束接口分析跨层协同。该结构把构型、库存、任务链、信息组织与执行反馈对应到可用能力、资源使用和任务完成事件，为理解不同技术路线的职责提供了共同基础。

所讨论的方法表明，扩展性具有不同的成本来源。数学分解减少直接处理全部组合决策的负担，几何邻域与分布式协商改变协调范围，策略复用改变训练和部署方式。它们分别依赖任务结构、信息条件和运行更新机制，任务收益、求解时间、消息开销与离线成本需要在相应场景中共同理解。局部求解更快或共享更多历史状态，都不必然产生更高质量的全局计划；分解造成的决策范围变化和同一时段的任务竞争仍参与这一权衡。

资源耦合进一步改变收益兑现和可行性的含义。备用资产只有在到位并具备能力后才能支持任务，观测只有在满足相应处理与交付条件后才能形成所要求的产品，服务访问和风险机动还需要对应连续动力学与执行约束。因此，能力投入、活动完成和业务恢复是不同事件。健康或风险变化进入调度时，需要明确其影响哪些活动、资源及动作权限，使任务安排与执行结果保持对应。

公开工程资料展示了这一连接在不同范围内的实现。运营接口定义任务状态和资源承诺，单星及限定多星飞行试验展示数据处理、协同观测或机动协调，软件测试与形式检查则回答模块及模型性质。各类证据能够相互补充，其适用范围由实际连接的环节、节点和事件条件决定。未来研究可围绕能力到位与服务恢复、资源承诺与计划修复、学习输出与约束检查，以及一致任务链中的跨层验证继续推进。评价这些连接对持续服务的作用，将有助于把已有局部方法组织为具有明确运行职责和可检查证据的星座管理系统。

---

# 参考文献与工程资料

本稿正文按唯一DOI与唯一工程资料网址去重后，共引用**58项来源**：**50篇学术文献**（46篇期刊论文、4篇会议论文）与**8份工程资料**。同一论文的作者稿与正式版合并计数；同一份NASA任务资料用于不同试验时只计一次。英文题名附中文工作译名。

## 学术文献

1. Mohamed Khalil Ben-Larbi; Kattia Flores Pozo; Tom Haylok, et al. Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts〔迈向大型分布式卫星系统自动化运行，第一部分：综述与范式转变〕. *Advances in Space Research, 2021, 67(11): 3598-3619*. DOI: [10.1016/j.asr.2020.08.009](https://doi.org/10.1016/j.asr.2020.08.009).

2. Pauline Jakob; Seiichi Shimizu; Shoji Yoshikawa, et al. Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control〔采用多级库存控制的最优卫星星座备份策略〕. *Journal of Spacecraft and Rockets, 2019, 56(5): 1449-1461*. DOI: [10.2514/1.A34387](https://doi.org/10.2514/1.A34387).

3. Lijun He; Ben Liang; Jiandong Li, et al. Joint Observation and Transmission Scheduling in Agile Satellite Networks〔敏捷卫星网络中的观测与传输联合调度〕. *IEEE Transactions on Mobile Computing, 2022, 21(12): 4381-4396*. DOI: [10.1109/TMC.2021.3076088](https://doi.org/10.1109/TMC.2021.3076088).

4. Antony Gillette; Alan George. Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions〔去中心化多航天器任务的韧性自主任务管理〕. *Journal of Aerospace Information Systems, 2023, 20(7): 387-397*. DOI: [10.2514/1.I011208](https://doi.org/10.2514/1.I011208).

5. Xinwei Wang; Guohua Wu; Lining Xing, et al. Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions〔敏捷对地观测卫星调度二十年：建模、方法与未来方向〕. *IEEE Systems Journal, 2021, 15(3): 3881-3892*. DOI: [10.1109/JSYST.2020.2997050](https://doi.org/10.1109/JSYST.2020.2997050).

6. Benedetta Ferrari; Jean-François Cordeau; Maxence Delorme, et al. Satellite Scheduling Problems: A survey of applications in Earth and outer space observation〔卫星调度问题：对地与外层空间观测应用综述〕. *Computers & Operations Research, 2025, 173: 106875*. DOI: [10.1016/j.cor.2024.106875](https://doi.org/10.1016/j.cor.2024.106875).

7. Tianle Yin; Zhijian He; Quan Li, et al. Managing Mega-Constellations: A Starlink-Informed Review〔巨型星座管理：以Starlink为参照的综述〕. *Symmetry, 2026, 18(7): 1141*. DOI: [10.3390/sym18071141](https://doi.org/10.3390/sym18071141).

8. Mohammad Reza Jabbarpour; Bao Quoc Vo; Ghaith El-Dalahmeh, et al. Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges〔分布式航天系统与任务管理的智能体方法：方法体系、实践现状与挑战〕. *Acta Astronautica, 2026, 238: 237-257*. DOI: [10.1016/j.actaastro.2025.10.018](https://doi.org/10.1016/j.actaastro.2025.10.018).

9. Zeno Pavanello; Luigi De Maria; Andrea De Vittori, et al. CAMmary: A review of spacecraft collision avoidance manoeuvre design methods〔CAMmary：航天器碰撞规避机动设计方法综述〕. *Acta Astronautica, 2025, 236: 770-789*. DOI: [10.1016/j.actaastro.2025.07.027](https://doi.org/10.1016/j.actaastro.2025.07.027).

10. Hang Woon Lee; David O. Williams Rogers; Brycen D. Pearl, et al. Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods〔采用整数规划与序贯决策方法的确定性多阶段星座重构〕. *Journal of Spacecraft and Rockets, 2025, 62(1): 206-222*. DOI: [10.2514/1.A35990](https://doi.org/10.2514/1.A35990).

11. Itai Zilberstein; Ananya Rao; Matthew Salis, et al. Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation〔面向大型卫星星座的去中心化分解式观测调度〕. *Journal of Artificial Intelligence Research, 2025, 82: 169-208*. DOI: [10.1613/jair.1.16997](https://doi.org/10.1613/jair.1.16997).

12. Shreya Parjan; Steve A. Chien. Decentralized Observation Allocation for a Large-Scale Constellation〔大型星座的去中心化观测分配〕. *Journal of Aerospace Information Systems, 2023, 20(8): 447-461*. DOI: [10.2514/1.I011215](https://doi.org/10.2514/1.I011215).

13. Adam Herrmann; Mark A. Stephenson; Hanspeter Schaub. Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations〔面向可扩展对地观测卫星星座运行的单智能体强化学习〕. *Journal of Spacecraft and Rockets, 2024, 61(1): 114-132*. DOI: [10.2514/1.A35736](https://doi.org/10.2514/1.A35736).

14. Christopher John Lowe; Ruaridh Alexander Clark; Ciara Norah McGrath, et al. A delay-tolerant network approach to satellite pickup and delivery scheduling〔卫星采集与交付调度的延迟容忍网络方法〕. *Ad Hoc Networks, 2023, 151: 103289*. DOI: [10.1016/j.adhoc.2023.103289](https://doi.org/10.1016/j.adhoc.2023.103289).

15. Yuhe Mao; Yunhua Wu; Xiaozhe Ju, et al. Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation〔低轨巨型星座动态管理拓扑的构建、演化与维护〕. *Space: Science & Technology, 2025, 5: 0248*. DOI: [10.34133/space.0248](https://doi.org/10.34133/space.0248).

16. Francesco Basciani; Luciana Rebelo; Patrizio Pelliccione. Reference architecture for autonomy and adaptivity in satellites〔卫星自主性与自适应能力的参考架构〕. *Journal of Systems and Software, 2026, 236: 112802*. DOI: [10.1016/j.jss.2026.112802](https://doi.org/10.1016/j.jss.2026.112802).

17. Minghao Shang; Ronggang Yuan; Bin Song, et al. Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm〔采用改进蚁群算法的能量约束多敏捷卫星观测与传输联合调度〕. *Acta Astronautica, 2025, 230: 92-103*. DOI: [10.1016/j.actaastro.2025.02.008](https://doi.org/10.1016/j.actaastro.2025.02.008).

18. Riccardo Apa; Jennifer Hudson; Marcello Romano. Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit〔低轨多客户服务任务的低推力推进与漂移轨道优化〕. *The Journal of the Astronautical Sciences, 2026, 73(2): 36*. DOI: [10.1007/s40295-026-00580-4](https://doi.org/10.1007/s40295-026-00580-4).

19. Leonid Appel; Moshe Guelman; David Mishne. Optimization of satellite constellation reconfiguration maneuvers〔卫星星座重构机动优化〕. *Acta Astronautica, 2014, 99: 166-174*. DOI: [10.1016/j.actaastro.2014.02.016](https://doi.org/10.1016/j.actaastro.2014.02.016).

20. Hang Woon Lee; Koki Ho. Regional Constellation Reconfiguration Problem: Integer Linear Programming Formulation and Lagrangian Heuristic Method〔区域星座重构问题：整数线性规划模型与拉格朗日启发式方法〕. *Journal of Spacecraft and Rockets, 2023, 60(6): 1828-1845*. DOI: [10.2514/1.A35685](https://doi.org/10.2514/1.A35685).

21. Jaewoo Kim; Jaemyung Ahn; Taehyun Sung. Replenishment Strategy for Satellite Constellation with Dual Supply Modes〔双供给模式下的卫星星座补网策略〕. *Journal of Spacecraft and Rockets, 2025, 62(5): 1567-1583*. DOI: [10.2514/1.A36281](https://doi.org/10.2514/1.A36281).

22. Jaewoo Kim; Taehyun Sung; Woonam Hwang, et al. On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation〔融合在轨服务的卫星星座维护策略〕. *Journal of Spacecraft and Rockets, 2026: 1-18*. DOI: [10.2514/1.A36684](https://doi.org/10.2514/1.A36684).

23. Yuri Shimane; Nicholas Gollins; Koki Ho. Orbital Facility Location Problem for Satellite Constellation Servicing Depots〔卫星星座服务仓库的轨道设施选址问题〕. *Journal of Spacecraft and Rockets, 2024, 61(3): 808-825*. DOI: [10.2514/1.A35691](https://doi.org/10.2514/1.A35691).

24. Euihyeon Choi; Koki Ho. Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers〔低推力转移下卫星星座服务轨道仓库位置优化〕. *Journal of Spacecraft and Rockets, 2026, 63(1): 4-13*. DOI: [10.2514/1.A36386](https://doi.org/10.2514/1.A36386).

25. Yaxiong Li; Xinglong Sun; Xinxue Liu, et al. Deployment of On-Orbit Service Vehicles Using a Fuzzy Adaptive Particle Swarm Optimization Algorithm〔采用模糊自适应粒子群算法的在轨服务航天器部署〕. *Modelling and Simulation in Engineering, 2021, 2021: 1-15*. DOI: [10.1155/2021/6644339](https://doi.org/10.1155/2021/6644339).

26. Tristan Sarton du Jonchay; Hao Chen; Onalli Gunasekara, et al. Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties〔需求不确定性下在轨服务运行的建模与优化框架〕. *Journal of Spacecraft and Rockets, 2021, 58(4): 1157-1173*. DOI: [10.2514/1.A34978](https://doi.org/10.2514/1.A34978).

27. Pedro Marcolin Antunes; Laio Oriel Seman; Eduardo Camponogara. A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites〔面向纳卫星星座能量感知任务调度的分支定价算法〕. *Computers & Operations Research, 2026, 185: 107259*. DOI: [10.1016/j.cor.2025.107259](https://doi.org/10.1016/j.cor.2025.107259).

28. Jiahao Qin; Hongxia Wang; Xudong Gao, et al. Lagrangian hierarchical mixed-integer programming for ultra-large-scale satellite scheduling under dynamic task delivery〔动态任务下发条件下超大规模卫星调度的拉格朗日分层混合整数规划〕. *Advances in Space Research, 2026, 77(11): 11252-11270*. DOI: [10.1016/j.asr.2025.12.008](https://doi.org/10.1016/j.asr.2025.12.008).

29. Beatriz Soret; Antonio M. Mercado‐Martínez; Antonio Jurado‐Navas, et al. Edge Intelligence for Satellite‐Based Earth Observation: Scheduling Image Acquisition and Processing〔卫星对地观测边缘智能：图像采集与处理调度〕. *International Journal of Satellite Communications and Networking, 2026: sat.70082*. DOI: [10.1002/sat.70082](https://doi.org/10.1002/sat.70082).

30. Guoliang Li. Online scheduling of distributed Earth observation satellite system under rigid communication constraints〔严格通信约束下分布式对地观测卫星系统的在线调度〕. *Advances in Space Research, 2020, 65(11): 2475-2496*. DOI: [10.1016/j.asr.2020.02.018](https://doi.org/10.1016/j.asr.2020.02.018).

31. Jing Qi; Min Hu; Lining Xing, et al. Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites〔面向大规模应急对地观测任务在线调度的深度强化学习辅助大邻域搜索〕. *Expert Systems with Applications, 2025, 291: 128502*. DOI: [10.1016/j.eswa.2025.128502](https://doi.org/10.1016/j.eswa.2025.128502).

32. Adam Herrmann; Hanspeter Schaub. A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling〔对地观测卫星调度强化学习算法的比较分析〕. *Frontiers in Space Technologies, 2023, 4: 1263489*. DOI: [10.3389/frspt.2023.1263489](https://doi.org/10.3389/frspt.2023.1263489).

33. Susan E. Sorenson; Sarah G. Nurre Pinkley. Multi-orbit routing and scheduling of refuellable on-orbit servicing space robots〔可加注在轨服务机器人跨轨道路径规划与调度〕. *Computers & Industrial Engineering, 2023, 176: 108852*. DOI: [10.1016/j.cie.2022.108852](https://doi.org/10.1016/j.cie.2022.108852).

34. Shuai YIN; Chuanjiang LI; Edoardo FADDA, et al. On-orbit refueling robust mission scheduling with uncertain duration for geosynchronous orbit spacecraft〔GEO 航天器加注时长不确定条件下的在轨加注鲁棒任务调度〕. *Chinese Journal of Aeronautics, 2026, 39(1): 103774*. DOI: [10.1016/j.cja.2025.103774](https://doi.org/10.1016/j.cja.2025.103774).

35. Elad Denenberg. Satellite closest approach calculation through Chebyshev Proxy Polynomials〔采用切比雪夫代理多项式计算卫星最近接近事件〕. *Acta Astronautica, 2020, 170: 55-65*. DOI: [10.1016/j.actaastro.2020.01.020](https://doi.org/10.1016/j.actaastro.2020.01.020).

36. Phasawee Saingyen; Sittiporn Channumsin; Suwat Sreesawet, et al. Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques〔接近筛选方法性能研究及基于 CUDA 的接近评估计算加速〕. *Aerospace, 2023, 10(6): 543*. DOI: [10.3390/aerospace10060543](https://doi.org/10.3390/aerospace10060543).

37. Simon Burgis; Lukas Rohrmüller; Martin Michel, et al. Simulation of satellites and constellations for the assessment of collision avoidance operations〔用于评估碰撞规避运行的卫星与星座仿真〕. *CEAS Space Journal, 2023, 15(5): 655-670*. DOI: [10.1007/s12567-022-00471-y](https://doi.org/10.1007/s12567-022-00471-y).

38. Francisco Gavilan; Rafael Vazquez; Eduardo F. Camacho. Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation〔结合扰动估计的航天器交会机会约束模型预测控制〕. *Control Engineering Practice, 2012, 20(2): 111-122*. DOI: [10.1016/j.conengprac.2011.09.006](https://doi.org/10.1016/j.conengprac.2011.09.006).

39. Zhenbo Zhao; Fan Wu; Jian Chen. Chance-constrained visual servoing MPC for non-cooperative spacecraft rendezvous〔非合作航天器交会的机会约束视觉伺服模型预测控制〕. *Aerospace Science and Technology, 2026, 169: 111237*. DOI: [10.1016/j.ast.2025.111237](https://doi.org/10.1016/j.ast.2025.111237).

40. Purnanand Elango; Abraham P. Vinod; Kenji Kitamura, et al. Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit〔近直线晕轨道被动安全交会的连续时间逐次凸化〕. *AIAA SCITECH 2026 Forum, 2026*. DOI: [10.2514/6.2026-2446](https://doi.org/10.2514/6.2026-2446).

41. Mark Stephenson; Hanspeter Schaub. Two Approaches to Autonomous Spacecraft Inspection: Shielded Reinforcement Learning versus Probabilistic Roadmaps〔自主航天器巡检的两种方法：带安全屏蔽的强化学习与概率路线图〕. *The Journal of the Astronautical Sciences, 2026, 73(5): 89*. DOI: [10.1007/s40295-026-00631-w](https://doi.org/10.1007/s40295-026-00631-w).

42. Kyle Hundman; Valentino Constantinou; Christopher Laporte, et al. Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding〔利用LSTM与非参数动态阈值检测航天器异常〕. *Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2018: 387-395*. DOI: [10.1145/3219819.3219845](https://doi.org/10.1145/3219819.3219845).

43. Lars Herrmann; Marie Bieber; Wim J. C. Verhagen, et al. Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry〔揭示性能高估：航天器遥测深度异常检测的重新评估〕. *CEAS Space Journal, 2024, 16(2): 225-237*. DOI: [10.1007/s12567-023-00529-5](https://doi.org/10.1007/s12567-023-00529-5).

44. Sascha Wanninger. Knowledge-based satellite failure detection, isolation and recovery (FDIR)〔基于知识的卫星故障检测、隔离与恢复（FDIR）〕. *CEAS Space Journal, 2026, 18(5): 991-1004*. DOI: [10.1007/s12567-025-00651-6](https://doi.org/10.1007/s12567-025-00651-6).

45. Changyuan He; Yunfeng Dong; Hongjue Li, et al. Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling〔考虑多子系统耦合的敏捷对地观测卫星推理式调度方法〕. *Remote Sensing, 2023, 15(6): 1577*. DOI: [10.3390/rs15061577](https://doi.org/10.3390/rs15061577).

46. Gregg Rabideau; Daniel Tran; Steve Chien, et al. Mission Operations of Earth Observing-1 with Onboard Autonomy〔具有星上自主能力的 Earth Observing-1 任务运行〕. *2nd IEEE International Conference on Space Mission Challenges for Information Technology (SMC-IT'06), 2006: 367-373*. DOI: [10.1109/SMC-IT.2006.48](https://doi.org/10.1109/SMC-IT.2006.48).

47. Steve Chien; Joshua Doubleday; David R. Thompson, et al. Onboard Autonomy on the Intelligent Payload Experiment CubeSat Mission〔智能载荷实验（IPEX）CubeSat任务的星上自主运行〕. *Journal of Aerospace Information Systems, 2017, 14(6): 307-315*. DOI: [10.2514/1.I010386](https://doi.org/10.2514/1.I010386).

48. Francesco Basciani; Arianna Fedeli; Daniele Masti, et al. A model-driven framework for supervised reconfiguration of satellite schedulers〔卫星调度器受监督重配置的模型驱动框架〕. *Software and Systems Modeling, 2026*. DOI: [10.1007/s10270-026-01426-1](https://doi.org/10.1007/s10270-026-01426-1).

49. Matthew Rantanen; Jalil Modares; Nicholas Mastronarde, et al. Performance of the Asynchronous Consensus Based Bundle Algorithm in Lossy Network Environments〔有损网络环境下异步一致性任务包算法的性能〕. *2018 IEEE 10th Sensor Array and Multichannel Signal Processing Workshop (SAM), 2018: 311-315*. DOI: [10.1109/SAM.2018.8448984](https://doi.org/10.1109/SAM.2018.8448984).

50. Philipp Chrszon; Paulina Maurer; George Saleip, et al. Model checking of spacecraft operational designs: a scalability analysis〔航天器运行设计的模型检测：可扩展性分析〕. *Software and Systems Modeling, 2025, 24(6): 1825-1846*. DOI: [10.1007/s10270-025-01281-6](https://doi.org/10.1007/s10270-025-01281-6).

## 工程资料

51. Planet. [Tasking API](https://docs.planet.com/develop/apis/tasking/)〔任务请求API〕. 开发者文档；访问日期：2026-10-10。

52. Iridium. [Iridium Adds to Constellation Resilience with Launch of Spare Satellites](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites)〔Iridium通过发射备星增强星座韧性〕. 运营方部署公告，2023-05-20；访问日期：2026-10-10。

53. Amazon Web Services. [Work with contacts](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html)〔通信窗口预约管理〕. 服务文档；访问日期：2026-10-10。

54. SpaceX. [Starlink Collision Avoidance CONOPS](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/)〔Starlink碰撞规避运行概念〕. 运营方运行流程；访问日期：2026-10-10。

55. Astroscale. [Astroscale’s ADRAS-J Achieves Historic 15-Meter Approach to Space Debris](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris)〔ADRAS-J实现距空间碎片约15米的接近〕. 运营方在轨事件报告，2024-12-11；访问日期：2026-10-10。

56. NASA Jet Propulsion Laboratory. [IPEX](https://ai.jpl.nasa.gov/public/projects/ipex/)〔智能载荷试验项目〕. 任务项目说明；访问日期：2026-10-10。

57. NASA. [What is Starling?](https://www.nasa.gov/smallspacecraft/what-is-starling/)〔Starling任务介绍〕. 飞行任务说明；访问日期：2026-10-10。

58. NASA. [NASA Starling and SpaceX Starlink Improve Space Traffic Coordination](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/)〔NASA Starling与SpaceX Starlink改进空间交通协调〕. 任务协调试验报道，2025-03-26；访问日期：2026-10-10。
