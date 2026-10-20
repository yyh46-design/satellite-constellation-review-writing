# 大型卫星星座智能运行管理中的规划与协同决策方法综述

Planning and Coordinated Decision-Making for Intelligent Operations Management of Large Satellite Constellations: A Review

**v3.2-CN · 2026-10-20 · 运行决策主线调整稿；作者审阅版**

## 摘要

大型卫星星座的智能运行管理，不仅需要生成任务与资源安排，还需要根据运行状态确定调整措施，协调多个决策主体，并确认新安排能够投入执行。本文采用问题导向的叙述性综述，将研究范围限定于智能运行管理中的规划与协同决策层，以对地观测和通信为主要场景，沿决定形成、跨星协调以及决定采用与更新组织代表研究。任务分配、活动安排和资源优化构成主要算法内容，规则推理、计划修复和执行监督用于分析状态变化如何转化为后续行动。比较表明，候选缩减、局部协调、计划复用和预计算减少不同类型的工作，其价值取决于保留的选择及完整运行成本；任务与资源共同决定的收益受业务目标、可改变量和有效计算时间限制；预测、搜索辅助、动作生成、恢复行动选择和部署批准承担不同职责，不能由局部算法性能推定完整自主运行能力。本文进一步区分计算位置、修改权限和执行确认，按模型性质、实际运行环节及验证规模组织证据，并提出有限预算下的决策组合、延迟信息下的调整范围以及恢复行动与业务接续的比较问题。所得综合为大型星座运行决策方法的选取和衔接提供有条件的依据，不以通用反馈框架或异构实验排名替代具体方法分析。

**关键词：** 大型卫星星座；智能运行管理；任务规划；协同决策；资源配置；动态重规划

## Abstract

Intelligent operations management of large satellite constellations requires not only task and resource schedules but also the selection of responses to operational changes, coordination among decision makers, and confirmation that revised plans can be executed. This problem-driven narrative review focuses on the planning and coordinated decision-making layer, using Earth observation and communications as the main application domains. Representative studies are organized around decision formation, multi-satellite coordination, and decision adoption and updating. Task allocation, activity scheduling, and resource optimization provide the principal algorithmic content; rule-based reasoning, plan repair, and execution supervision explain how changing states lead to subsequent actions. The synthesis distinguishes workloads reduced by candidate filtering, local coordination, plan reuse, and precomputation. It relates the value of joint decisions to service objectives, revisable variables, and effective computational budgets, and separates prediction, search assistance, action generation, recovery selection, and deployment approval. Computational location, revision authority, and execution confirmation are examined independently. Evidence is organized by model properties, operational functions actually evaluated, and validation scale. Research questions concern decision coupling under limited budgets, permissible adjustments with delayed information, and the connection between recovery actions and service resumption. The review supports conditional method selection without treating a generic feedback architecture or heterogeneous performance results as proof of integrated autonomy.

**Keywords:** large satellite constellations; intelligent operations management; mission planning; coordinated decision-making; resource allocation; dynamic replanning

## 1 引言

### 1.1 从任务调度到运行决策

卫星星座通过多颗卫星共同承担观测、通信等业务。面对请求，需要选择执行卫星、安排活动时间并分配能源、存储、计算和通信资源；执行过程中，还需要根据请求变化、设备可用状态和资源占用，决定保留、修改或停止哪些活动。大型分布式卫星系统的自动化运行研究已将排程、监测、资源配置和轨道管理作为相互联系的职责讨论[1]。本文关注其中将状态与业务要求转化为可执行决定的规划与协同决策层，而不是将调度算法等同于全部运行管理。

多颗卫星增加了任务分配的选择，也使不同安排产生联系。同一观测请求可能由多颗卫星完成，一颗卫星可能面对多个竞争请求；多颗卫星使用同一地面站或链路时，还需协调传输时间与容量。规模负担取决于请求数量、候选机会、共享资源和更新频度，而非只由星数决定。计划复用、几何邻域协调和网络表示复用分别减少部分重算、协商和构图工作[2–4]。这些机制是否有用，还取决于旧结果是否适用于当前状态，以及协调后的决定能否被相关节点采用。

观测和通信提供两类主要应用。观测请求需要安排成像及后续处理、下传，并按产品质量和交付期限评价；通信业务需要持续调整用户关联、无线资源和数据路径，按给定时段的需求满足、吞吐、时延和中断评价。部署、补给和维护改变可用卫星与资源条件[5]。故障或通信机会失效时，运行决策还须确定受影响的任务、可采用的调整措施及其授权范围，随后才是如何求得新的具体安排。

因此，本文将三个结果分开：算法提出了什么方案，执行系统实际采用了什么，以及业务最终得到什么。研究对象仍是大型星座智能运行管理，但技术分析聚焦规划与协同决策；状态感知和底层控制按其提供的状态、可行性条件和执行结果作为接口，不展开为独立的全面技术综述。

### 1.2 已有综述与本文的研究定位

敏捷观测综述已梳理任务模型与求解方法[6]，卫星调度应用综述进一步讨论观测、通信和集成安排[7]；分布式空间系统综述覆盖智能体、组织、通信及任务管理[8]。自动化运行研究联系规划、执行、监测及星地职责[1,9]，通信专题综述讨论网络组织和资源管控[10,11]。这些研究已涉及协同和动态调整，不能将“连接多个环节”本身作为本文的新发现。

Singla等[12]将平台资源和网络需求纳入统一任务表达，并讨论集成、协调和自适应组织；可信自主卫星运行综述[13]则从人工智能、分布式系统和人机协同等方面分析运行能力及其实现条件。本文不另提一个总体运行架构，也不全面分类所有自主系统技术，而是比较架构内部的决策方法：使用哪些状态，决定什么，由谁计算和修改，如何检查、批准并采用结果。表1说明这种切入点与已有工作的联系；它并不宣称其他综述没有讨论相同问题。

**表1 已有综述与本文运行决策比较的衔接**

| 已有主题 | 代表来源 | 提供的基础 | 本文进一步组织的比较 |
|---|---|---|---|
| 观测与卫星调度 | [6,7] | 问题、模型与求解方法 | 任务安排怎样随可用状态和可改变量改变 |
| 分布式空间系统 | [8] | 智能体、通信及任务管理 | 计算位置、信息内容与修改权限分别怎样影响协调 |
| 自动化运行 | [1,9] | 规划、执行、监测及工具 | 提出计划、采用配置和确认结果分别由谁完成 |
| 网络与资源管控 | [10,11] | 通信业务及资源优化 | 业务传输、数据交付和协调信息的不同作用 |
| 运行与网络集成 | [12] | 统一任务及交互框架 | 同一组织内哪些决定联合、固定或局部更新 |
| 可信自主运行 | [13] | AI、分布式系统及人机协同 | 按实际决策职责与批准条件比较，不以智能标签判断自治程度 |
| 空间物流 | [5] | 部署、补给与服务资源 | 能力到位怎样改变行动选择和业务接续 |

全文围绕三项相连的问题展开。第一，如何根据任务、资源和运行状态形成安排或调整措施，解释优化、搜索、学习与规则的实际作用。第二，如何在地面与多颗卫星之间分配计算和权限，协调任务归属及共享资源。第三，如何把候选方案变成被采用的安排，并依据执行结果保持、修复或扩大重规划范围。持续服务用于检验这些决定是否转化为业务结果，不作为无中断保证或跨业务统一分数。

本文的综合工作是将方法放回其决策职责与执行条件进行比较。第3章保留具体算法机制，第4章分析规模、耦合、信息和权限如何改变方法取舍；通用的“状态—决策—执行”顺序只用来组织材料，不作为新的系统架构贡献。

### 1.3 研究边界与证据使用

本文所称规划包括选择任务、活动及必要的后续行动；调度进一步确定由哪些卫星、在何时、以何种资源执行；协同决策处理多个主体相互影响的选择。这些概念用于界定本文范围，不要求每项原研究使用同一术语。智能运行管理涵盖利用目标、状态、模型和规则形成、检查与更新决定，因而不专指神经网络，也不预设所有决定必须在星上或无人工介入完成。

技术主体为任务规划、资源配置、多星协调和运行变化后的调整。状态监测及诊断以可提供的事实、估计和不确定性进入决策；轨迹和姿态控制以可执行条件、时间占用及终端状态进入规划；硬件研制、完整故障检测分类、底层控制器设计及认证体系不作全面综述。局部恢复行动只用于解释状态怎样触发措施，不据单星或地面原型推定星座级恢复能力。

“大型”通过成员数、请求负载、候选数量、竞争范围和更新频度说明，不设一个适用于所有任务的星数门槛。单星、GEO、深空及通用多智能体研究用于解释相关机制，并保留原有任务条件和验证规模。通信首次按三种角色区分：面向用户的通信业务、观测数据处理后的交付，以及跨节点决策所需的信息交换。

本研究采用问题导向叙述性选录，以既有主题库及参考链追溯为基础。详细机制依据实际取得并定向核读的正文，作者稿、接受稿和正式版按实际版本解释；已有综述承担定位，官方资料承担具体运行事件或接口说明。新增综合明确区分原研究结果与本文推论，不以未取得正文为由断言某研究缺少某项功能，不把不同论文的局部验证拼接为完整系统实证。

第2章定义运行决策对象、状态、可选行动和比较基础；第3章分析规划求解、规则、学习、多星协调及动态调整；第4章讨论决定形成、采用和更新的条件性取舍与验证；第5章总结可由现有证据支持的认识。来源可得性和任务选择仍限制覆盖范围，全文不进行跨论文统一性能排名。

## 2 智能运行管理中的决策问题与比较基础

### 2.1 任务与资源安排：已知条件和待作出的决定

以对地观测为例，请求通常给出目标位置、观测要求、优先级和完成期限。在轨道给定时，可以计算卫星与目标满足观测几何要求的时间段，以下称为几何可见时间段。它只说明几何条件；姿态转换、载荷限制及能源和存储是否允许执行，仍需另行检查。

假设一次成像持续时间已给定，需要选择执行卫星、使用哪个时间段，并确定开始时刻。多个请求由同一卫星承担时，还需安排先后顺序和姿态调整时间。若原模型已经枚举开始时刻和持续时间，算法只决定是否选择候选活动；若时间或持续时间可调，则须求出相应取值，不能替原模型增加不存在的变量。

观测后的处理和下传会反过来影响任务选择。图像占用存储，处理消耗计算资源和能源，下传需满足星地通信机会及接收容量。多个卫星共用地面站时，要协调时间和数据量；对要求按期交付的请求，需检查整段处理和传输能否及时完成。通信业务则给定用户需求、覆盖和可用容量，决定服务卫星、传输资源和路径，并随需求及覆盖变化更新。

在智能运行管理中，这些问题还要附带状态适用时刻、已执行活动和可撤回条件。已经执行的成像不能撤销，地面站预约依规则修改[14]，已分配传输容量限制新请求[15]，新激光链路的建立时间限制路径何时可用[16]。这里既有物理约束，也有运行规则，不能把求解器允许改变的变量直接当成系统具有的修改权限。

**表2 运行决策的输入、决定及结果交接**

| 决策职责 | 已知条件或状态输入 | 需要作出的选择 | 后续需要确认的结果 |
|---|---|---|---|
| 任务与活动规划 | 请求、候选卫星、窗口、时长及已有计划 | 接受哪些请求，由谁执行，何时开始及执行顺序 | 活动及资源约束满足，相关节点采用安排 |
| 资源配置 | 能源、存储、计算和通信状态及需求 | 为哪些活动分配多少资源 | 额度和占用更新，配置实际生效 |
| 变化后的调整 | 故障或新请求、已执行前缀、可用替代活动 | 保留、推迟、取消、转移任务或扩大重规划 | 原安排撤回条件满足，替代安排无冲突 |
| 恢复行动选择 | 经确认的异常事实、允许行动及前序行动结果 | 选择下一项恢复措施或退出动作 | 措施执行成功或失败，状态可供后续规划使用 |
| 多星协调 | 任务归属、报价、资源承诺及消息时序 | 谁拥有任务或资源，哪些冲突需重新协商 | 各参与节点的相关决定一致 |
| 决定采用 | 候选计划、当前状态、授权和生效时限 | 批准、拒绝、重新计算或维持仍有效的安排 | 执行系统已采用何版本，随后实际结果是什么 |

表2是本文的职责归纳，不表示所有原研究同时覆盖这些步骤。“恢复行动选择”与“故障诊断”不同：本文关心已获得何种事实足以触发何种措施，以及结果怎样进入下一次决定，而不全面比较产生这些事实的检测器。

图1保留观测、处理、传输和共享资源的业务联系，作为规划问题的背景图；运行措施、批准及结果确认在本章和后文单独分析。

![图1](assets/fig1_service_framework_ai_v2.png)

图1 观测与通信业务的任务及资源关系。它表示本综述中任务与资源规划所处的业务环境，不是完整的智能运行架构。观测按产品交付评价，通信按给定时段的服务指标评价；反馈箭头是功能联系示意，不表示全部环节已经在同一系统验证。

### 2.2 决策方法、计算位置与权限

优化模型用变量表示选择，用约束排除不允许的安排，用目标评价可选结果；启发式通过追加、插入、删除或交换活动构造和改进计划。学习可以预测需求、选择搜索操作，或根据状态提出活动。规则推理则根据事实和预先定义的条件选择策略或行动。它们可以组合，但需要说明每种方法的输入和输出，避免把学习建议、可行计划和可执行指令当成同一对象。

计算位置与决策权限是两个维度。地面节点可以提出候选计划并等待审批，星上节点可以只在已授权的资源范围内局部调整，分布式算法也可能运行在地面用户节点而非卫星。管理拓扑与跨星分配研究[2,3,17]提供组织实例，具体自治程度仍取决于谁可以接受任务、撤回承诺、选择恢复措施和采用新配置，而不是是否使用AI或分布式计算。

联合建模说明哪些变量相互影响，分解求解说明计算如何拆分，滚动规划说明何时根据新信息更新；三者并不互斥。可以用启发式求解联合模型，也可以在分层系统中共同选择部分变量。比较时需进一步说明一个子问题的结果是否回到其他部分，已固定的选择何时还可修改。

本文将候选方案、经检查的方案、获准采用的方案和实际采用的配置分开记录。有些系统把其中若干步骤自动完成，有些保留人工审定。没有明确授权时，不能从“生成了满足模型约束的方案”推定已经执行；同样，保留人工批准也不否定前段规划和状态处理具有自动化能力。

### 2.3 一个贯穿示例：载荷不可用后的任务接续

为说明决策链，设想一颗观测卫星的载荷暂时不可用，但存储和通信仍可工作，同时原计划已占用若干地面站时段。该例是本文构造的说明情景，不是新增实验，也不描述某一完整在轨系统。

首先要区分尚未采集的请求、已经存储的图像和仍可执行的下传，不能把载荷失效等同于卫星全部能力消失。其次，根据期限、替代卫星窗口和可撤回预约，选择保留已有图像下传、推迟未执行请求、转交其他卫星或取消不能兑现的活动。此时任务与资源调度负责形成具体安排，行动选择还须受到故障处置规则和修改权限限制。

最后要确认接替节点是否采用新任务、旧资源是否确实释放，以及是否因消息滞后而重复分配。恢复动作成功只说明相应功能得到处理，计划采用只说明新的安排进入执行，产品交付才回答受影响需求是否满足。这个例子贯穿后文的方法比较，但不同文献只能分别支持其中已实际研究的环节。

### 2.4 评价对象与证据范围

业务评价需先明确事件和分母。观测中接受请求、成像、下传与合格产品交付不同，[18]按期完成观测和传输才计请求收益，[19]则分别计算观测收益与下传体积。通信需明确用户集合和评价时段，同时记录已服务性能与未满足需求，不只报告成功子集的平均时延。

方法评价同时记录准备、训练、在线求解、协调和配置采用所需的工作。求解得到的可行解、松弛界、最优解和超时分别报告；阶段可重叠时按事件时刻核算，不机械求和，也不把未报告的协调或部署时间当成零。扩大星数、单位星任务量、候选连接和竞争范围的试验应分别解释。

运行证据按三个方面记录：模型中证明或数值检查的性质，实际评估到的运行步骤，以及验证规模与平台。静态求解、循环重规划、配置检查、地面原型和飞行事件分别回答不同问题，不组成一个无需任务条件的成熟度排名。尤其应保留未采用计划、失败恢复、取消请求和安全退出，避免只按生成的计划评价智能运行能力。

## 3 规划、求解与协同决策方法

本章保留任务和资源调度的算法深度，再说明运行状态如何选择规划策略或恢复行动。前三节解释求解机制，第四节解释多星组织，第五节连接状态、行动和后续计划；这些维度可以出现在同一方法中，不构成相互排斥的算法分类树。

### 3.1 优化建模与分解求解

优化建模通过变量表达决定，通过约束排除不允许的安排，再根据目标函数评价候选。例如，二元变量表示请求是否接受或成像是否选择，时间变量表示活动开始时刻，资源变量表示处理和传输获得的容量。哪些量需要求解由具体模型确定。

Seman等[20]将不同任务与能源状态纳入混合整数线性模型，依据光照和工作消耗描述电池变化，约束单星及多星共同参与或冗余执行的任务。其ε约束方法将部分目标转为给定水平的约束，改变水平后调用Gurobi分析权衡。1—5星实验说明能源与任务选择的联系，不能据此证明大型星座求解性能。

Lemaître等[21]的受限单轨道段模型将候选图像和离散开始时刻组织为动态规划状态。在图像顺序预定、收益线性并去除立体成像约束等条件下，可以获得相应受限问题的最优解。约束规划则对图像与时间变量赋值，传播约束并排除不允许的组合；两类方法的约束范围不同，最优性结论不能直接互换。

He等[18]使观测和传输共同完成成为请求获益的条件。所读作者稿输入观测和传输时间段、权重与期限，输出窗口关联及相应时间安排，使下传条件影响观测选择。3颗观测星、12小时规划时域的仿真支持所设条件下的联合安排收益，仍需保留无误码传输和图像质量简化等假设。

Soret等[22]则先确定本轮采集，再配置处理节点负载和处理器频率。给定负载下利用时间约束消去频率，进而求解剩余资源问题。共同选择发生在下游处理，本轮采集作为输入；固定流水线、稳定链路和平均处理时间约束限定结果，不构成逐请求按期交付保证。

云覆盖不确定性研究[23]采用列生成启发式，将一条卫星轨道段内的观测序列作为候选，主问题选择已有序列，动态规划产生可改善当前目标的新序列，最后求解已生成候选上的整数问题。这避免一开始枚举全部序列，但完整整数问题的全局最优性仍取决于候选完整性及终止状态。

单星波束与功率研究[24]按时隙先选当前服务区域，再固定选束结果优化连续功率。波束表示集中向一定区域提供无线信号，功率影响当前传输量，并通过剩余需求影响下一时隙。分阶段处理因而需要说明当轮固定了什么，以及本轮结果何时影响后续选择。

上述研究区分了扩大决定范围和改变求解组织。运行管理可以预先规定哪些任务或资源不可撤回，再在剩余变量上调用适当求解方法；模型能够给出更大范围的候选，并不自动增加系统实际拥有的修改权。

### 3.2 启发式构造、局部搜索与混合求解

启发式按规则构造安排，局部搜索则反复修改已有方案。对观测任务，可以逐项选择请求并插入成像活动，检查姿态转换、时间与资源冲突；随后通过增加、删除或交换活动改善目标值。方法解释应明确每次修改什么，而不只列算法名称。

Lemaître等[21]比较贪心构造与局部搜索。贪心沿轨道段追加能够衔接的图像并估计剩余机会价值，局部搜索通过插入或删除改变序列。它们与动态规划的差别既在搜索机制，也在所保留的收益与约束，不能将不同约束组的结果直接排名。

Rocha等[19]的机构工作论文用图表示候选活动及其衔接，同时考虑观测、下传、能源和存储。方法通过减少连接、简化整数模型和局部混合整数规划邻域控制搜索规模。局部邻域每次只开放部分活动或连接，其余暂时固定；需要分别检查是否删去可行顺序，以及是否仍排除不满足姿态转换等条件的组合。观测收益和下传体积也应保留各自定义。

He等[18]的外层遗传搜索选择观测—传输窗口关联，内层通过半定松弛、随机化和可行性调整产生具体时间安排，结果返回外层评价候选。这种分层计算仍保留上下游相互影响，不能归为先固定观测后独立下传。

Handley[4]则在无直接星间链路的地面中继网络中，利用地理分块缩小候选范围，并保留网络图、更新连接代价。其节省主要来自减少重复构图，与缩小可行域或改变搜索操作不同。在线复用需要能及时反映当前连接，否则计算节省不能直接转化为有效计划。

启发式还可作为运行决策中的候选生成器，由规则限定允许动作、由后续检查判断候选能否采用。但这种组合只有在相应信息和约束确实传递时才成立；采用局部优化求解器也不赋予整个搜索流程全局最优性。

### 3.3 学习辅助搜索与活动选择

学习分别可以预测需求、选择搜索操作或提出活动，三者接收和输出的对象不同。流量预测研究[25]在合成序列上评价估计误差，直接产物是需求预测；是否改善服务还需观察资源策略怎样使用它，不能由误差下降直接推出吞吐或恢复收益。

Song等[26]的RL-GA保留遗传搜索，以Q-learning依据适应度改善选择交叉、变异或其组合，再由窗口选择和解码得到具体安排。学习输出搜索操作，可行性仍由解码处理。两颗卫星、不同任务数量的实验扩展的是请求负载，不是星座成员规模，完整成本也应包含解码和约束处理。

Herrmann等[27]用单星环境中的蒙特卡洛树搜索提供状态—动作评价，训练神经策略，再将同一策略用于多颗卫星。上层目标分配、局部策略、动作屏蔽和完成状态共享分别负责目标归属、活动选择、允许动作及已完成任务的信息更新。共享完成状态仍可能滞后，不能完全避免同一时刻的竞争。

其4—40星实验评价了上述组合，而非仅评价神经策略。上层整数模型未联合描述下层全部资源动态，运行计算还依赖离线训练与预处理。Basilisk中的共同仿真比较[28]提供了区分策略和安全动作处理作用的条件，不能用局部推理时间代替全流程响应。

Ngo等[29]以地面覆盖小区簇为智能体，学习波束激活、频段和功率，并用奖励惩罚处理过量干扰。小区簇数不等于卫星数，惩罚项也不等于逐动作硬约束保证。对运行管理而言，还须说明策略动作处于何种授权范围，由谁检查和实际配置。

表3比较候选安排的生成机制。需求预测、学习建议、解码后计划和最终采用的动作应分别记录；不因使用学习模型就将方法归为全自主运行。

**表3 代表规划与求解方法的作用机制**

| 代表研究 | 输入及待决定内容 | 形成候选的方法 | 主要解释边界 |
|---|---|---|---|
| 能源感知调度[20] | 任务与光照给定，选择各星任务 | 混合整数规划及多目标权衡 | 1—5星；可行解、间隙和最优性区分 |
| 观测序列优化[21] | 图像及时间条件给定，选择序列 | 动态规划或约束规划 | 受限模型和完整模型不能混用 |
| 贪心与局部搜索[21] | 构造或修改成像序列 | 追加、插入或删除 | 收益与约束范围不同 |
| 联合观测—传输[18] | 窗口、权重与期限，决定关联及时间 | 遗传搜索与内层近似优化 | 固定实例、质量及传输假设 |
| 集成观测—下传[19] | 活动图与资源，选择活动及顺序 | 图缩减与局部整数规划 | 简化可能丢失选择；双奖励分别解释 |
| 处理配置[22] | 采集已定，配置负载与频率 | 变量消元与资源优化 | 平均时间约束，不回改本轮采集 |
| 学习辅助搜索[26] | 搜索状态，选择遗传操作 | Q-learning辅助搜索 | 解码负责可行性；两星负载实验 |
| 策略复用[27] | 单星状态与目标分配，提出动作 | 策略、屏蔽及状态共享 | 上层分配与通信贡献须分开 |

### 3.4 多星协调、信息交换与修改权限

CBBA[30]由各主体计算任务边际收益、构造任务包，再交换赢家、报价和时间戳处理重复占有。任务加入顺序不同于执行顺序；失去较早加入的任务时，需要释放随后加入且报价依赖它的任务并重算。原研究的收敛和价值结论有评分及通信前提，机器人验证不直接代替轨道执行约束。

Krigman等[31]的分布式约束优化以用户为智能体、请求为变量，将观测机会或不执行作为取值，通过分布式局部搜索处理重叠和容量冲突，并按原流程处理剩余冲突。这里分散的是用户请求选择，卫星仍是执行对象，不能从多智能体标签推定计算发生在星上。

Zilberstein等[3]利用观测竞争的几何邻域限制直接协商范围。其已有高层机制可以说明协调对象的缩减，但详细分解步骤不超出已核记录。共享地面资源仍可能把几何上分离的活动联系起来；将邻域方法迁移到新的资源模型时，应作为额外协调条件检查，而非据此断言原方法遗漏了这些约束。

通信分层管理[32]由上层确定服务区域和频谱条件，局部节点选择波束、时隙及信道；多星需求感知配置[33]把全局选束与当前选束下的星内功率调整分开。局部可调整变量受上层结果限制。延迟通信规划[34]与异步任务分配[35]又分别处理所设时延和消息更新条件，不能把一般多智能体实验直接视为在轨验证。

据此，协同决策需要同时处理任务归属、共享资源和采用状态。某节点算出新分配后，相关资源拥有者是否接受、其他节点是否获知旧安排撤回，属于决定采用过程。本文不假定所有算法已经实现一致性协议，而是把原研究报告的消息内容、参与者和确认步骤作为比较项；没有报告的部署过程不由理想通信假设替代。

### 3.5 状态驱动的策略选择、计划修复与恢复行动

#### 3.5.1 从状态估计选择规划策略

状态变化不仅可以触发重算，也可以改变怎样构造计划。He等的推理式观测方法[36]先预测电量、数据和存储等状态，再用规则调整目标选择权重，在偏向观测、下传或能源的策略之间选择，随后形成活动安排。状态估计在此改变搜索偏好，而不是直接输出已执行命令。研究对象是单颗敏捷观测卫星的多子系统耦合任务，不能将其状态适应直接写成跨星任务恢复验证。

这一机制与学习选择遗传算子[26]有共同的策略选择作用，但依据不同：前者利用预设规则及预测状态，后者利用训练得到的操作选择。本文不建立两者的性能排名，而是区分“选择怎样规划”和“规划具体做什么”；两类输出都还依赖活动构造及约束检查。

#### 3.5.2 保留事实并调整尚未执行的安排

滚动时域方法[37]结合周期与事件触发，反复安排等待和新到请求；其框架不决定采用哪种求解器。Parjan和Chien[2]在100星、一周规划时域的仿真中，复用未受变化影响的安排，移除撤回请求并安排新增请求。广播状态帮助更新分配，但仍可能保留重复观测；单线程仿真中的并行用时估计不等于实测并行时延。

鲁棒观测[23]在计划阶段用区间和预算参数处理收益偏差，保护参数不是实际云概率。天气情景规划[38]的两阶段模型共享预定观测，三阶段模型则在中午获得信息后调整后半日活动。考虑多个情景与具有信息揭示后的改排权限是两回事。GEO加注排程[39]同样以预算不确定集预先处理历时偏差，所检查的时间保护不意味着执行中具备自主重排。

Lowe等[15]逐请求搜索采集与交付路径，接受后扣减已分配容量，保留已有承诺；实现将能源和存储视作无限。当预定路径不可用时，可以局部选择后续转发路径而保留采集指派。生成替代任务还涉及版本和跨节点分配，应与局部转发试验分开。动态激光链路研究[16]进一步计入建链时间，使立即换路和保留连接的选择具有不同执行代价。

#### 3.5.3 从异常事实选择行动并确认结果

Wanninger的FDIR原型[40]把参数和事件转化为故障事实，用规则选择恢复行动并处理互斥动作，再由执行规则展开操作。前一行动的成功或失败会影响是否采用后续措施。其验证是在地面移动机器人平台上的特定故障情景，并非在轨星座恢复试验；本文仅据此分析事实、行动选择和结果反馈的衔接。

Remote Agent[41]提供另一种连接：规划器处理任务与资源约束，执行层在运行中组织活动，诊断与模式信息参与故障响应。它说明局部处置与需要重新规划的任务条件应相互传递，而不是每次异常都无条件重算全部任务。本文保留其单航天器及原任务环境，不据多个独立案例拼接出已验证的星座恢复闭环。

恢复行动选择与任务重新分配因而不能互相替代。一项局部操作可能恢复设备，却不改变已经错过的观测机会；转移任务也不意味着原设备故障已排除。表4分别记录这些方法修改的对象。把它们用于同一运行流程时，应传递行动结果及最新资源条件，再由相应规划和协调方法处理后续任务；这一组合要求是本文归纳，不是所引研究共同完成的系统。

**表4 状态变化后的决定及其实际修改范围**

| 机制与来源 | 使用的信息 | 保留或固定的内容 | 输出及后续确认 |
|---|---|---|---|
| 策略推理[36] | 预测资源和子系统限制 | 给定任务与规则 | 目标偏好，再构造和检查安排 |
| 滚动安排[37] | 新请求及更新状态 | 已执行活动 | 新时域安排，需确认采用 |
| 增量规划[2] | 请求激活、撤回及共享状态 | 未受影响的计划 | 更新分配，检查重复与冲突 |
| 鲁棒安排[23,39] | 事先给定的偏差集合 | 计划阶段信息 | 满足所设保护条件的候选，不自动增加执行权限 |
| 天气信息后改排[38] | 中午的新天气信息 | 前半日活动 | 三阶段模型重排后半日 |
| 局部路径修复[15] | 原连接失效及后续机会 | 原采集指派 | 后续转发路径，检查交付 |
| 恢复规则[40] | 异常事实及前序行动结果 | 规则和允许措施 | 下一恢复行动及效果确认；地面原型 |
| 规划—执行—诊断衔接[41] | 任务、模式及执行状态 | 已完成活动和当前约束 | 局部处置或重新规划；原单航天器环境 |

## 4 运行条件下的决策取舍、采用与验证

### 4.1 规模扩大后应减少哪些工作

大型星座的负担应拆成成员、请求、候选机会、资源竞争和更新频度。图缩减[19]减少需要搜索的连接，几何邻域[3]减少直接协商对象，增量规划[2]减少重复安排；三者控制的工作不同。更快产生局部候选，还需检查跨节点协调和采用是否成为新的主要开销。

候选压缩可能删除原本可行的顺序，因此须与业务收益和可行域变化一起评价。局部协调要说明竞争是否能够在所选范围内处理；把同一地面站或交付容量纳入新的应用时，可能需要扩大关联范围。复用则以旧安排继续有效为前提，较小改动也可能限制新请求，因此应同时记录节省的计算与未满足需求，而不是只报告重算比例。

图表示复用[4]和轨迹代价预计算[42]利用可重复结构，但前者要更新连接，后者受轨道、质量、时刻及终端范围限制。学习策略的上层目标分配[27]也依赖已生成的可见机会。将这些方法用于运行管理，需要说明准备结果失效的判据、重建工作和状态确认时间，不能把已前移的计算当成永远不存在。

**表5 计算减负机制与运行采用条件**

| 主要工作 | 代表机制 | 可复用或缩小的条件 | 除算法用时外需要保留的代价 |
|---|---|---|---|
| 候选与执行顺序过多 | 图缩减、局部搜索[19] | 可以识别可合并或可舍弃连接 | 候选损失、约束检查及计划质量 |
| 直接协商主体过多 | 几何邻域协调[3] | 主要竞争位于相应邻域 | 跨邻域依赖、消息及采用一致性 |
| 重复安排未变化任务 | 增量规划[2] | 旧安排在当前状态下仍有效 | 保留决定对新需求的限制 |
| 重复构建网络表示 | 图复用及边权更新[4] | 连接变化可被及时反映 | 失效检测、更新和重建 |
| 重复动力学计算 | 代价网格与插值[42] | 查询未超出模型和网格范围 | 离线计算、误差及轨迹复核 |
| 每次活动选择成本高 | 策略复用[27] | 输入及动作条件仍适用 | 训练、上层分配、屏蔽及协调 |

图2继续作为减负机制示意；它并不表示这些机制在相同实例中完成了性能比较。

![图2](assets/fig2_scale_mechanisms_ai_v2.png)

图2 计算工作及其减少机制。候选缩减[19]、局部协调[3]和计划复用[2]分别影响搜索、协商与重复求解；节点和计划条不对应实测数量。用于运行决策时，还需按表5检查结果的适用性及采用过程。

### 4.2 任务、资源与调整措施应共同决定到什么范围

He等[18]在固定实例比较联合和分开安排，使下传机会参与观测评价，并在所设3星、12小时条件下提高加权成功请求收益；Lowe等[15]则在逐请求接受时检查交付容量。它们说明跨环节条件如何改变选择，后者还保留已接受请求的容量承诺，不能等同于对全部未来请求重新全局优化。

“联合”需要连同目标解释。[19]分别奖励观测和下传体积，[18]按完整请求计奖，[22]在采集已定后配置处理，[24]在当前选束后调功率。不同研究不是同场景优劣对照；应先明确要改善哪种服务结果，再决定哪些变量仍可开放。

运行状态变化还可能改变允许的措施，而不只是变量数值。例如，第2.3节的载荷失效情景要求保留已采集数据的交付，却需重新判断尚未采集请求的归属。规则行动选择[40]与任务规划[41]从不同层面处理变化。把故障标志直接送入原调度器并不足以说明智能恢复，应交代标志怎样改变可用活动、资源或允许行动，以及哪些变化会触发进一步协调。

当目标相同、扩大后的可行域包含原可行域时，最优目标不会变差，但限时求解未必取得更好的可执行结果。对运行决策，还须区分模型中允许修改、规则允许撤回以及执行来得及采用三个条件。扩大模型不能撤销已执行事实，也不能取消必要的批准步骤。

### 4.3 信息、修改权限与决定生效

完成状态、未来任务归属和已确认资源占用具有不同作用。[27]共享已成像或下传信息，[30]交换赢家、报价与时间戳处理尚未执行任务的归属；两者不能只按是否通信比较。计算中心已更新状态，也不说明执行节点同步采用了同一安排。

局部修复与较大重规划应从相同已执行前缀、信息和承诺条件比较。原路径不可用但仍有交付机会时，可以保留采集指派而调整后续转发[15]；失去所有可用机会时，是否能够重新采集或转移任务，还需检查权限和期限。不能将“后续选路”自动解释为“恢复原业务的全部选择”。

同研究条件对照提供具体边界。[15]的16星试验在名义和通信机会失效条件下比较指定路径优先转发与局部选路，相对表现随可靠性改变；原作者将其中变化联系到预定路径和期限。动态激光链路研究[16]则权衡重复建链与传播距离，低建链代价时不同保持策略表现并不一致。它们不是集中式和分布式架构的普遍排名。

决定采用还需要独立检查。Basciani等[43]针对星上软件调度配置，将建模、校验、优化和仿真产生的候选交给人工监督者批准，再生成并部署配置；监督者可拒绝或要求重新计算。其对象是软件进程及相应时间约束，不能直接替代星座业务规划。但它清楚展示了算法输出与授权采用是两个阶段；自动生成候选并不等于无人工的自主部署。

对有期限的请求，要给剩余活动留出执行时间；对持续通信，要记录配置切换期间的中断和积压。求解超时后，旧计划只有通过当前状态检查才可继续使用。某项恢复行动失败也不等于所有任务都无法执行，应依据真实结果选择下一措施或更新计划，而不是无条件重试同一安排。

![图3](assets/fig3_decision_timing_ai_v2.png)

图3 状态变化后的修改范围与执行时序。图中检查和计划采用在不同系统中可由星上、地面或人工承担，实际授权须由所引研究说明。路径修复以[15]为例，部署批准以[43]为功能参照；下部是有期限请求的示意，不是完整自主系统或实测时延。

**表6 运行条件、决策职责与可采用的比较**

| 具体条件 | 需要作出的决定 | 代表证据 | 可以支持的认识及限制 |
|---|---|---|---|
| 有限下传竞争 | 是否让下传条件改变观测选择 | 同实例联合/分开对照[18] | 所设条件下的请求收益，不是通用联合最优规则 |
| 本轮采集固定 | 如何配置处理负载与频率 | 处理模型[22] | 下游仍可优化，跨轮反馈不回改已执行活动 |
| 原接触可能失效 | 保留指定路径或局部选路 | 可靠性条件对照[15] | 取决于接触、容量及期限，不扩大为全任务恢复 |
| 换路需要建链 | 是否支付切换成本 | 路径比较[16] | 需保留传播和建链模型，不含未测控制成本 |
| 资源限制改变 | 采用何种规划策略 | 状态预测与规则[36] | 规则选择偏好，候选仍需构造和检查；单星验证 |
| 前序恢复未成功 | 采用下一措施或调整处置 | FDIR原型[40] | 行动结果反馈；地面特定场景，不是星座级恢复证明 |
| 候选配置已生成 | 批准、拒绝或再次计算 | 受监督配置[43] | 计算与采用分开，保留人工及软件任务边界 |
| 多星共享完成状态 | 是否还需任务归属和确认信息 | 机制对照[27,30] | 完成、分配和采用各有职责，跨研究不直接排名 |

图4仅保留已有三项条件性对照，不把本版新增的恢复与批准分析画成已有共同实验。

![图4](assets/fig4_conditional_comparisons_ai_v2.png)

图4 不同研究内部的条件性比较。（a）[18]的联合与分开安排；（b）[15]的接触可靠性变化，MSR优先指定路径并允许局部回退，CGR依据后续机会选路；（c）[16]所报1 ms建链条件下，ILPR、ALPR平均时延略高于ILSR，ISASR仍较低。模型与指标不同，不构成跨研究排名。该图沿用工作草图，正式图须依据原始结果及来源重新核对绘制。

### 4.4 执行监督、能力恢复与验证范围

#### 4.4.1 运行层与控制层怎样交接

部署与平台设计提供卫星到位时间和可用容量[44,45]，库存、补给和维修描述资源供应与周转[46–48]。规划使用这些结果决定何时可以安排替代任务；资源可得、功能确认和业务重新分配不是同一事件。安全轨迹研究[49–52]则提供机动占用、终端状态及特定失效条件下的保证，运行决策不能只接收一个不带时段和前提的“安全”标签。

底层控制负责执行所需的姿态或轨道运动，本文分析的是何时选择相应行动、哪些业务因此受限，以及结果怎样改变后续计划。ADRAS-J公开的中止与后撤[53]说明安全退出的功能；原任务恢复仍需另外跟踪，不因退出成功就判定服务完成。

#### 4.4.2 结果反馈与人机分工

EO-1的任务流程[54]由星上科学分析产生目标，规划与执行功能接续处理活动，同时保留地面职责；IPEX官方资料[55]提供星上处理和持续规划的任务参照。Starling资料[56,57]说明特定多星状态共享及协调试验，需要保留四星规模、模拟事件与原任务条件。这些材料用于识别确实进入执行的功能，不证明数百或数千颗卫星的完整自治已成熟。

FDIR[40]、Remote Agent[41]和受监督配置[43]分别展示行动结果监测、规划与诊断连接，以及人工批准后的采用。三者不是同一系统的组件验证，也不是从低到高的通用自治等级。应说明各自状态输入、选择权、执行权和反馈结果，保留人工参与并不使前段自动决策失去意义。

**表7 运行证据中的决定、采用及验证边界**

| 资料或方法 | 已体现的决定或功能 | 采用与反馈的解释 | 不能据此推定的内容 |
|---|---|---|---|
| Iridium备星[58] | 备用资产投入 | 可用能力发生变化 | 库存最优或业务恢复时间 |
| Planet、AWS、DSN[14,59,60] | 交付、预约和确认流程 | 决定及资源承诺对应具体事件 | 内部算法性能或无人工自治 |
| Starlink与独立测量[61,62] | 处置流程和服务现象 | 运营说明、测量和解释分开 | 整个内部决策系统的验证 |
| ADRAS-J[53] | 中止与安全后撤 | 特定事件的执行反馈 | 原服务任务已经恢复 |
| FDIR规则原型[40] | 故障事实、措施及效果检查 | 失败后选择后续行动 | 在轨或大型星座恢复效果 |
| Remote Agent[41] | 规划、执行和诊断连接 | 按原任务条件解释局部处置与重规划 | 通用星座规模性能 |
| EO-1、IPEX[54,55] | 星上分析与后续任务 | 保留原地面职责和事件范围 | 所有任务与权限全自主 |
| Starling系列[56,57] | 多星状态及行动协调 | 保留四星与具体试验条件 | 巨型星座整体验证 |
| 受监督配置[43] | 模型、候选、检查和部署 | 人工批准与平台采用独立于优化 | 自主星座业务部署 |
| cFS、Basilisk、形式化研究[63–66] | 组件、仿真或规格性质 | 支持不同的实现和检查对象 | 同一整系统服务保证 |

#### 4.4.3 不把局部性能替代运行能力

评价记录应分三列：模型性质、实际运行步骤和验证环境。可行性或收敛证明说明规定模型下的性质；动态仿真说明所设变化下的计划更新；原型、软件检查和飞行事件说明对应功能进入了何种环境。不能把三列合成不带条件的“成熟度分数”，也不能把几篇研究各自成功的部分拼接为整星座证据。

学习模块的比较同样遵循这一要求。[27]的部分对照同时改变目标分配、前瞻和通信，[28]提供共同仿真条件。对运行层的评价应先报告组合方案的效果，再在信息、候选、约束和权限一致时替换模块，保留训练、解码、修复和协调成本。最终同时观察能力是否可用、计划是否被采用、业务是否满足，并记录拒绝、超时、退出及未完成需求。

### 4.5 可检验的研究问题

#### 4.5.1 有限预算内怎样组合任务、资源和调整决定

联合规划[18]、固定输入后的配置[22]和逐请求交付[15]说明不同决定范围。后续可以在相同请求、轨道、资源和授权条件下逐步开放任务归属、成像时间、处理及传输；通信使用相同流量、用户和评价时段逐步开放关联、波束、功率与路径。小规模分析模型潜力，大规模限时试验分析可及时采用的结果。

异常条件下还应区分增加哪些调整措施与改进求解器。例如，允许转移任务而非仅推迟，改变了动作集合；提高搜索速度而不变动作集合，改变的是求解方法。将两者分别控制，才能识别收益来自恢复选择更多，还是相同选择被更好地求解。本文提出这种对照，不宣称已经完成相应实验。

#### 4.5.2 延迟信息与授权范围怎样影响更新

固定请求、异常序列和已执行前缀，分别改变状态误差、消息延迟、承诺可撤回条件及批准时机，比较保留、局部修复和较大重规划[2,14–16]。除计划用时外，还应记录各节点何时采用结果；观测跟踪交付，通信跟踪中断及积压，不把仅生成的候选计为实际收益。

可以进一步比较预先保留余量[23,39]与信息揭示后的修改[38]。所有对照保持相同安全与状态检查，不能用无条件继续已失效旧计划作为低成本基线。对需要人工批准的任务，批准是实际运行条件；是否自动化这一环节是另一项需要独立证据支持的设计选择。

#### 4.5.3 恢复措施怎样连接业务接续

在相同故障和需求序列下，分别记录故障事实可用、恢复措施选择、措施结果、替代能力到位、任务重新分配及实际交付。库存和维护[46–48]说明资源恢复，FDIR与规划执行[40,41]说明行动和反馈，二者之间的业务接续仍需要共同场景检查。

恢复更快却未减少业务损失时，应区分原因：功能已经恢复但窗口已错过，替代卫星没有可用下传，资源尚未释放，或者新的分配尚未被采用。各阶段可能重叠，按事件记录才能判断应优先增加备份、改进恢复措施，还是改善协调与计划采用。这是将运行管理与规划算法连接的验证问题，而不是扩大到完整硬件或诊断系统设计。

## 5 结论

本文将大型卫星星座智能运行管理的分析范围限定在规划与协同决策层，沿决定形成、跨星协调以及采用和更新组织研究。任务与资源调度提供具体算法基础，状态驱动的策略与恢复行动说明变化怎样成为新的决定，执行监督和批准条件说明候选如何进入实际运行。观测和通信分别保留交付与持续服务指标，不用同一分数替代不同任务要求。

现有证据支持三项有条件的认识。第一，候选压缩、局部协调、计划复用、预计算与学习分别改变不同工作，收益须与状态适用性和完整采用成本一起评价。第二，计算位置、决策范围与修改权限不同，更多联合变量或更快局部动作不能代替跨节点冲突处理及授权。第三，恢复行动成功、候选计划可行、配置已采用和业务满足是不同结果；反馈是否有效取决于实际修改了什么、何时生效及结果是否继续影响下一次决定。

优化、启发式、学习和规则并非相互替代的智能等级。它们可以分别承担资源权衡、搜索、策略选择、行动生成及结果处理，组合效果仍需在明确的信息、约束和权限条件下验证。单星、地面原型、软件任务和特定多星飞行案例提供不同范围的证据，不能扩展为已完成巨型星座自主运行验证。

后续应围绕有限预算下的决策组合、延迟信息与授权、恢复措施和业务接续开展受控比较。本文的贡献是把算法机制与运行职责、采用条件及证据范围相联系，而不是提出一个未经整体验证的通用闭环架构。其结论仍受所选来源及原研究验证范围限制。

## 参考文献

1. Ben-Larbi MK, Flores Pozo K, Haylok T, Choi M, Grzesik B, Haas A, et al. Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts. Advances in Space Research, 2021, 67(11): 3598–3619. DOI: 10.1016/j.asr.2020.08.009.

2. Parjan S, Chien SA. Decentralized Observation Allocation for a Large-Scale Constellation. Journal of Aerospace Information Systems, 2023, 20(8): 447–461. DOI: 10.2514/1.I011215.

3. Zilberstein I, Rao A, Salis M, Chien S. Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation. Journal of Artificial Intelligence Research, 2025, 82: 169–208. DOI: 10.1613/jair.1.16997.

4. Handley M. Using ground relays for low-latency wide-area routing in megaconstellations. Proceedings of the 18th ACM Workshop on Hot Topics in Networks, 2019: 125-132. DOI: 10.1145/3365609.3365859.

5. Ho K. Space Logistics Modeling and Optimization: Review of the State of the Art. Journal of Spacecraft and Rockets, 2024, 61(5): 1417–1427. DOI: 10.2514/1.A35982.

6. Wang X, Wu G, Xing L, Pedrycz W. Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions. IEEE Systems Journal, 2021, 15(3): 3881–3892. DOI: 10.1109/JSYST.2020.2997050.

7. Ferrari B, Cordeau JF, Delorme M, Iori M, Orosei R. Satellite Scheduling Problems: A survey of applications in Earth and outer space observation. Computers & Operations Research, 2025, 173: 106875. DOI: 10.1016/j.cor.2024.106875.

8. Jabbarpour MR, Vo BQ, El-Dalahmeh G, Tahir H, Kowalczyk R, Bessell T, et al. Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges. Acta Astronautica, 2026, 238: 237–257. DOI: 10.1016/j.actaastro.2025.10.018.

9. Ben-Larbi MK, Flores Pozo K, Choi M, Haylok T, Grzesik B, Haas A, et al. Towards the automated operations of large distributed satellite systems. Part 2: Classifications and tools. Advances in Space Research, 2021, 67(11): 3620–3637. DOI: 10.1016/j.asr.2020.08.018.

10. GONG L, ZHANG W, CHEN Q, et al. A Survey of Intelligent Networking Technologies for LEO Mega-Constellations. Acta Aeronautica et Astronautica Sinica, 2026, online first. DOI: 10.7527/S1000-6893.2026.32935. (in Chinese)

11. DI H, DONG T, LIU Z, et al. Review on Resource Management and Optimization Technologies for LEO Communication Satellite Constellation Networks. Journal of Astronautics, 2026, 47(2): 270–283. DOI: 10.3873/j.issn.1000-1328.2026.02.002. (in Chinese)

12. Singla A, Criscola F, Canales D, Fraire JA, Calveras A, Ruiz-de-Azua JA. Toward Integrated Satellite Operations and Network Management: A Review and Novel Framework. Technologies, 2025, 13(8): 312. DOI: 10.3390/technologies13080312.

13. Thangavel K, Sabatini R, Gardi A, Ranasinghe K, Hilton S, Servidia P, Spiller D. Artificial Intelligence for Trusted Autonomous Satellite Operations. Progress in Aerospace Sciences, 2024, 144: 100960. DOI: 10.1016/j.paerosci.2023.100960.

14. Amazon Web Services. Work with contacts. Official documentation; accessed 10 October 2026. https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html.

15. Lowe CJ, Clark RA, McGrath CN, Macdonald M. A delay-tolerant network approach to satellite pickup and delivery scheduling. Ad Hoc Networks, 2023, 151: 103289. DOI: 10.1016/j.adhoc.2023.103289.

16. Bhattacharjee D, Madoery PG, Chaudhry AU, Yanikomeroglu H, Kurt GK, Hu P, et al. On-Demand Routing in LEO Mega-Constellations With Dynamic Laser Inter-Satellite Links. IEEE Transactions on Aerospace and Electronic Systems, 2024, 60(5): 7089–7105. DOI: 10.1109/TAES.2024.3415571.

17. Mao Y, Wu Y, Ju X, Xie H, Yue C. Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation. Space: Science & Technology, 2025, 5: 0248. DOI: 10.34133/space.0248.

18. He L, Liang B, Li J, Sheng M. Joint Observation and Transmission Scheduling in Agile Satellite Networks. IEEE Transactions on Mobile Computing, 2022, 21(12): 4381–4396. DOI: 10.1109/TMC.2021.3076088.

19. Rocha Y, Chagas GO, Coelho LC, Subramanian A. The integrated agile Earth observation satellite scheduling problem. Computers & Operations Research, 2025, 184: 107212. DOI: 10.1016/j.cor.2025.107212.

20. Seman LO, Ribeiro BF, Rigo CA, Filho EM, Camponogara E, Leonardi R, et al. An Energy-Aware Task Scheduling for Quality-of-Service Assurance in Constellations of Nanosatellites. Sensors, 2022, 22(10): 3715. DOI: 10.3390/s22103715.

21. Lemaı̂tre M, Verfaillie G, Jouhaud F, Lachiver JM, Bataille N. Selecting and scheduling observations of agile satellites. Aerospace Science and Technology, 2002, 6(5): 367–381. DOI: 10.1016/S1270-9638(02)01173-2.

22. Soret B, Mercado‐Martínez AM, Jurado‐Navas A, Lyholm ND, Moretti M, Popovski P, et al. Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing. International Journal of Satellite Communications and Networking, 2026: 1–22; advance online publication, 24 August 2026. DOI: 10.1002/sat.70082.

23. Wang X, Song G, Leus R, Han C. Robust Earth Observation Satellite Scheduling With Uncertainty of Cloud Coverage. IEEE Transactions on Aerospace and Electronic Systems, 2020, 56(3): 2450–2461. DOI: 10.1109/TAES.2019.2947978.

24. Shuang Zheng; Xing Zhang; Peng Wang; Wenbo Wang. Joint Beam Scheduling and Power Optimization for Beam Hopping LEO Satellite Systems. China Communications, 2024, 21(10): 1–14. DOI: 10.23919/JCC.ja.2022-0864.

25. Han C, Xiong W, Yu R. A Hybrid Forecasting Model for Self-Similar Traffic in LEO Mega-Constellation Networks. Aerospace, 2024, 11(3): 191. DOI: 10.3390/aerospace11030191.

26. Song Y, Wei L, Yang Q, Wu J, Xing L, Chen Y. RL-GA: A Reinforcement Learning-based Genetic Algorithm for Electromagnetic Detection Satellite Scheduling Problem. Swarm and Evolutionary Computation, 2023, 77: 101236. DOI: 10.1016/j.swevo.2023.101236.

27. Herrmann A, Stephenson MA, Schaub H. Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations. Journal of Spacecraft and Rockets, 2024, 61(1): 114–132. DOI: 10.2514/1.A35736.

28. Herrmann A, Schaub H. A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling. Frontiers in Space Technologies, 2023, 4: 1263489. DOI: 10.3389/frspt.2023.1263489.

29. Ngo QT, He Y, Jayawickrama B, Dutkiewicz E. Multi-Agent DDPG-Based Joint Beam Hopping and Resource Allocation for Cognitive GEO-LEO Satellite Networks. IEEE Networking Letters, 2025, 7(4): 303-307. DOI: 10.1109/LNET.2025.3605531.

30. Han-Lim Choi; L. Brunet; J. P. How. Consensus-Based Decentralized Auctions for Robust Task Allocation. IEEE Transactions on Robotics, 2009, 25(4): 912–926. DOI: 10.1109/TRO.2009.2022423.

31. Krigman S, Grinshpoun T, Dery L. Scheduling of Earth observing satellites using distributed constraint optimization. Journal of Scheduling, 2024, 27(5): 507–524. DOI: 10.1007/s10951-024-00816-x.

32. Gou L, Bian D, Nie Y, Zhang G, Zhou H, Shi Y, et al. Hierarchical Resource Management for Mega-LEO Satellite Constellation. Sensors, 2025, 25(3): 902. DOI: 10.3390/s25030902.

33. Zhao R, Cai J, Luo J, Gao J, Ran Y. Demand-Aware Beam Hopping and Power Allocation for Load Balancing in Digital Twin Empowered LEO Satellite Networks. IEEE Transactions on Wireless Communications, 2025, 24(6): 5084–5098. DOI: 10.1109/TWC.2025.3545745.

34. Wang C, Tang J, Cheng X, Liu Y, Wang C. Distributed cooperative task planning algorithm for multiple satellites in delayed communication environment. Journal of Systems Engineering and Electronics, 2016, 27(3): 619–633. DOI: 10.1109/JSEE.2016.00066.

35. Rachmut B, Amador Nelke S, Zivan R. Asynchronous Communication Aware Multi-Agent Task Allocation. Proceedings of IJCAI, 2023: 262–270. DOI: 10.24963/ijcai.2023/30.

36. He C, Dong Y, Li H, Liew Y. Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling. Remote Sensing, 2023, 15(6): 1577. DOI: 10.3390/rs15061577.

37. Qiu Dishan; He Chuan; Liu Jin; Ma Manhao. A Dynamic Scheduling Method of Earth-Observing Satellites by Employing Rolling Horizon Strategy. The Scientific World Journal, 2013, 2013(1): 304047. DOI: 10.1155/2013/304047.

38. Valicka CG, Garcia D, Staid A, Watson JP, Hackebeil G, Rathinam S, et al. Mixed-integer programming models for optimal constellation scheduling given cloud cover uncertainty. European Journal of Operational Research, 2019, 275(2): 431–445. DOI: 10.1016/j.ejor.2018.11.043.

39. YIN S, LI C, FADDA E, GUO Y, RAN G, BRANDIMARTE P. On-orbit refueling robust mission scheduling with uncertain duration for geosynchronous orbit spacecraft. Chinese Journal of Aeronautics, 2026, 39(1): 103774. DOI: 10.1016/j.cja.2025.103774.

40. Wanninger S. Knowledge-based satellite failure detection, isolation and recovery (FDIR). CEAS Space Journal, 2026, 18(5): 991–1004. DOI: 10.1007/s12567-025-00651-6.

41. Muscettola N, Nayak PP, Pell B, Williams BC. Remote Agent: to boldly go where no AI system has gone before. Artificial Intelligence, 1998, 103(1–2): 5–47. DOI: 10.1016/S0004-3702(98)00068-X.

42. Apa R, Bhattacharjee S, Hudson J, Romano M. Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations. The Journal of the Astronautical Sciences, 2025, 72(2): 7. DOI: 10.1007/s40295-025-00487-6.

43. Basciani F, Fedeli A, Masti D, Iovino L, Serri P, Pelliccione P. A model-driven framework for supervised reconfiguration of satellite schedulers. Software and Systems Modeling, 2026. DOI: 10.1007/s10270-026-01426-1.

44. Gwon B, Ahn J. Two-Stage Framework for Deployment-Aware Optimization of Satellite Constellation Pattern Design. International Journal of Aeronautical and Space Sciences, 2026. DOI: 10.1007/s42405-026-01298-1.

45. Zamacola SM, Rodríguez-Osorio RM, Salas-Natera MA. Joint satellite platform and constellation sizing for instantaneous beam-hopping in 5G/6G Non-Terrestrial Networks. Computer Networks, 2025, 257: 110942. DOI: 10.1016/j.comnet.2024.110942.

46. Jakob P, Shimizu S, Yoshikawa S, Ho K. Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control. Journal of Spacecraft and Rockets, 2019, 56(5): 1449–1461. DOI: 10.2514/1.A34387.

47. Kim J, Ahn J, Sung T. Replenishment Strategy for Satellite Constellation with Dual Supply Modes. Journal of Spacecraft and Rockets, 2025, 62(5): 1567–1583. DOI: 10.2514/1.A36281.

48. Kim J, Sung T, Hwang W, Ahn J. On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation. Journal of Spacecraft and Rockets, 2026: 1–18. DOI: 10.2514/1.A36684.

49. Lu P, Liu X. Autonomous Trajectory Planning for Rendezvous and Proximity Operations by Conic Optimization. Journal of Guidance, Control, and Dynamics, 2013, 36(2): 375–389. DOI: 10.2514/1.58436.

50. Morgan D, Chung SJ, Hadaegh FY. Model Predictive Control of Swarms of Spacecraft Using Sequential Convex Programming. Journal of Guidance, Control, and Dynamics, 2014, 37(6): 1725–1740. DOI: 10.2514/1.G000218.

51. Gavilan F, Vazquez R, Camacho EF. Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation. Control Engineering Practice, 2012, 20(2): 111–122. DOI: 10.1016/j.conengprac.2011.09.006.

52. Elango P, Vinod AP, Kitamura K, Acikmese B, Di Cairano S, Weiss A. Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit. AIAA SCITECH 2026 Forum, 2026. DOI: 10.2514/6.2026-2446.

53. Astroscale. Astroscale’s ADRAS-J Achieves Historic 15-Meter Approach to Space Debris. Official mission release; accessed 10 October 2026. https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris.

54. Gregg Rabideau; Daniel Tran; Steve Chien; et al. Mission Operations of Earth Observing-1 with Onboard Autonomy. SMC-IT, 2006: 367–373. DOI: 10.1109/SMC-IT.2006.48.

55. NASA Jet Propulsion Laboratory. IPEX. Official project documentation; accessed 10 October 2026. https://ai.jpl.nasa.gov/public/projects/ipex/.

56. NASA. What is Starling?. Official mission documentation; accessed 10 October 2026. https://www.nasa.gov/smallspacecraft/what-is-starling/.

57. NASA. NASA Starling and SpaceX Starlink Improve Space Traffic Coordination. Official mission release; accessed 10 October 2026. https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/.

58. Iridium. Iridium Adds to Constellation Resilience with Launch of Spare Satellites. Official operational release; accessed 10 October 2026. https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites.

59. Johnston MD, Tran D, Arroyo B, Sorensen S, Tay P, Carruth B, et al. Automated Scheduling for NASA's Deep Space Network. AI Magazine, 2014, 35(4): 7–25. DOI: 10.1609/aimag.v35i4.2552.

60. Planet. Tasking API. Official documentation; accessed 10 October 2026. https://docs.planet.com/develop/apis/tasking/.

61. Mohan N, Ferguson AE, Cech H, Bose R, Renatin PR, Marina MK, et al. A Multifaceted Look at Starlink Performance. Proceedings of the ACM Web Conference 2024: 2723–2734. DOI: 10.1145/3589334.3645328.

62. SpaceX. Starlink Collision Avoidance CONOPS. Official operational documentation; accessed 10 October 2026. https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/.

63. NASA Goddard Space Flight Center. Core Flight System – Demo Bundle. Official software repository; accessed 10 October 2026. https://github.com/nasa/cFS.

64. Kenneally PW, Piggott S, Schaub H. Basilisk: A Flexible, Scalable and Modular Astrodynamics Simulation Framework. Journal of Aerospace Information Systems, 2020, 17(9): 496–507. DOI: 10.2514/1.I010762.

65. Chien SA. Formal Methods for Trusted Space Autonomy: Boon or Bane?. NASA Formal Methods, Lecture Notes in Computer Science, 2022: 3–13. DOI: 10.1007/978-3-031-06773-0_1.

66. Chrszon P, Maurer P, Saleip G, Müller S, Fischer PM, Gerndt A, et al. Model checking of spacecraft operational designs: a scalability analysis. Software and Systems Modeling, 2025, 24(6): 1825–1846. DOI: 10.1007/s10270-025-01281-6.
