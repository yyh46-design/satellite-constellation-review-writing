# 第4章 综合评价与研究展望

## 4.1 大型星座管理方法的比较维度

现有星座管理研究已经形成了覆盖轨道构型、备份维护、观测调度、在轨服务、安全执行和自主运行的多种方法，但这些研究的目标与问题规模差异较大，不能简单按照优化收益或计算时间排列优劣。长期备份策略的主要输出可能是库存位置与补给量，观测调度需要决定卫星和成像窗口，在轨服务还要决定客户访问及轨道转移，执行层则关注风险估计、控制约束和故障后的动作。因此，评价方法的首要条件是明确论文实际优化了哪些变量、受到哪些约束，以及所报告的结果属于任务安排、物理执行还是运营成本。

以规模评价为例，《[Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation](https://doi.org/10.1613/jair.1.16997)》在200颗和108颗模拟卫星的24 h任务场景中分析分解优化的计算与通信表现，其中决策变量数与实际卫星数不是同一个规模指标。与此不同，《[Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods](https://doi.org/10.2514/1.A35990)》围绕若干阶段的覆盖收益和轨道调整安排构建优化模型，其计算复杂性既取决于卫星数量，也受到阶段数量和备选构型组合的影响。长期维护研究《[Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control](https://doi.org/10.2514/1.A34387)》则使用多年随机失效及补给仿真评价库存策略，所面对的是随机需求过程而非单次密集任务分配。这些实例表明，“大规模”应当被分解为卫星数量、任务请求数、可选决策数、规划时域及不确定事件数，而不是一个可以跨问题类型直接比较的单值。

计算效率的口径同样受到模型和求解流程影响。《[A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites](https://doi.org/10.1016/j.cor.2025.107259)》通过Dantzig–Wolfe分解和定价子问题求解具有能量约束的离散任务调度，其计算结果需要结合数学规划界和实例难度理解；《[A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling](https://doi.org/10.3389/frspt.2023.1263489)》则在单星仿真任务上比较不同学习和搜索策略，显示求解收益与训练、仿真调用和在线执行代价存在权衡。对于低推力服务，《[Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit](https://doi.org/10.1007/s40295-026-00580-4)》把轨道转移代价的网格预计算与在线路线优化分开。因此，只报告单次求解时间可能遗漏离线转移表生成、策略训练、轨道传播或重复优化的成本。跨方法比较需要同时交代优化对象、计算硬件、预处理开销、实际搜索时间以及未得到可行解的情况。

## 4.2 资源耦合与物理可执行性

从已有研究看，长期能力配置与短期任务执行都在逐步纳入更多资源和物理条件，但不同模型的耦合程度并不相同。《[Replenishment Strategy for Satellite Constellation with Dual Supply Modes](https://doi.org/10.2514/1.A36281)》通过直接注入与停泊轨道中转两种途径连接补给策略和响应时间；《[On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation](https://doi.org/10.2514/1.A36684)》又将新星补充、失效卫星恢复及运营方与服务商的经济目标放入统一维护决策。这些研究扩展了“星座可用性”的管理含义，使服务能力不仅受到备份数量影响，还依赖实际供应方式、服务回收比例和相关经济条件。另一方面，轨道重构与服务轨迹优化需要考虑机动、出发时刻和转移状态，相关成本不能简单用固定任务容量表示。

在观测任务链中，资源耦合体现为从获取数据到生成和交付信息的逐步扩展。《[Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm](https://doi.org/10.1016/j.actaastro.2025.02.008)》将成像、下传和能量补充共同纳入任务决策，而《[Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing](https://doi.org/10.1002/sat.70082)》进一步考虑图像质量与异构计算平台上的推理耗时。《[A delay-tolerant network approach to satellite pickup and delivery scheduling](https://doi.org/10.1016/j.adhoc.2023.103289)》则把任务分配与数据经过时变链路的实际送达路径联系起来。三类工作分别补充能源、计算和网络传输环节，表明单纯增加已安排的观测任务数不一定相应提高按时交付的数据产品数量。然而，其联合模型所涵盖的物理过程仍不相同，不能将分别验证的环节直接解释为同一完整业务链已得到统一验证。

轨道安全研究同样需要区分离散计划和连续过程。最近接近检测方法可以确定潜在危险事件及其时间位置，规避设计方法根据风险或动力学约束生成动作，而执行后的安全性还受到传播误差、实际控制和后续任务变化影响。《[CAMmary: A review of spacecraft collision avoidance manoeuvre design methods](https://doi.org/10.1016/j.actaastro.2025.07.027)》比较不同规避设计方法的求解原理与数值性能；《[Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation](https://doi.org/10.1016/j.conengprac.2011.09.006)》在特定相对运动模型中处理随机扰动下的概率约束；《[Two Approaches to Autonomous Spacecraft Inspection: Shielded Reinforcement Learning versus Probabilistic Roadmaps](https://doi.org/10.1007/s40295-026-00631-w)》则展示带安全屏蔽的闭环策略与更高计算成本的离线开环规划之间的差异。这些成果表明，任务执行的安全约束可以采取解析、数值和学习—优化结合的多种方式，比较时需要明确安全条件究竟适用于轨迹节点、控制动作、连续时间还是特定扰动概率模型。

## 4.3 分布式协同和智能方法的适用条件

分布式架构通常被用于减轻集中运行的协调负担，但不同研究对分布式的定义有所差异。《[Decentralized Observation Allocation for a Large-Scale Constellation](https://doi.org/10.2514/1.I011215)》通过改变观测请求的共享方式比较集中与去中心化协调；《[Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation](https://doi.org/10.34133/space.0248)》更关注管理域及其拓扑随轨道运动的变化；而《[A delay-tolerant network approach to satellite pickup and delivery scheduling](https://doi.org/10.1016/j.adhoc.2023.103289)》把数据交付路径作为任务选择的一部分。前者主要处理任务竞争，第二类研究处理信息管理的组织结构，第三类研究处理任务活动和数据路由的共同优化。因此，星座分布式调度的评价不应只记录算法是否存在中央协调节点，还应说明决策主体掌握的信息、消息到达条件以及冲突和资源状态如何保持一致。

通信受限环境使这一问题更加突出。《[Online scheduling of distributed Earth observation satellite system under rigid communication constraints](https://doi.org/10.1016/j.asr.2020.02.018)》利用通信机会预测改进任务包一致性协商，比较同步和异步协调方案；其性能随信息交换代价变化，说明较高的局部求解能力并不能直接代替网络条件分析。通用多代理领域的《[Performance of the Asynchronous Consensus Based Bundle Algorithm in Lossy Network Environments](https://doi.org/10.1109/SAM.2018.8448984)》还报告了有损网络下的重复分配或任务未分配现象，但其测试网络并非真实星间链路。两类研究提示，分布式算法的收敛条件和实际运行表现需要结合消息延迟、丢失、代理失效及任务动态性共同分析；来自不同网络模型的结论不宜无条件合并。

智能算法能够在局部优化、候选策略生成和状态识别中提高决策灵活性，但其作用位置比是否采用强化学习更值得关注。《[Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites](https://doi.org/10.1016/j.eswa.2025.128502)》把学习策略用于快速生成动态任务安排，再采用大邻域搜索修复和改善解；《[Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations](https://doi.org/10.2514/1.A35736)》则通过跨星复用单星训练策略处理多卫星任务，重点关注通信方式与资源限制。与此同时，《[Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry](https://doi.org/10.1007/s12567-023-00529-5)》指出异常检测结果会受到数据处理和评价指标影响。这些成果并不支持“学习算法普遍优于传统优化”的简单判断；更适合总结为：当学习模型承担不同功能时，应分别验证训练数据分布、约束检查方式、在线计算需求与系统对错误动作的处理机制。

## 4.4 工程验证与研究结论的适用范围

当前星座管理研究中的证据主要来自数学模型、合成或历史任务仿真、软件实现、板级试验和少量在轨自主运行案例。不同证据形式可以相互补充，但它们针对的问题并不相同。例如，长期库存和任务调度仿真能够评估特定随机需求与资源假设下的运行收益，却不能直接测量真实执行中的故障响应；软件验证可以检查计划管理模块的时序、冲突处理和配置规则，但难以单独证明轨道或姿态动作在飞行条件下的安全性。因此，对一个研究成果的成熟度判断需要说明被验证的功能、使用的数据或平台及未被纳入的边界，而不是简单将仿真、软件测试和飞行证据赋予固定等级。

飞行自主运行研究已经提供了重要的系统案例。《[Mission Operations of Earth Observing-1 with Onboard Autonomy](https://doi.org/10.1109/SMC-IT.2006.48)》介绍EO-1通过自主科学处理和规划改变原有运行流程的经验；《[Onboard Autonomy on the Intelligent Payload Experiment CubeSat Mission](https://doi.org/10.2514/1.I010386)》则报告IPEX在单星飞行任务中开展机载处理及资源驱动的重规划。它们证明了自主模块在实际航天器运行中的可用性，但不意味着已有同等证据证明数百至数千颗卫星能够同时执行分布式优化和冲突恢复。另一方面，《[Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions](https://doi.org/10.2514/1.I011208)》展示了任务管理器与飞行软件平台的集成及测试，《[A model-driven framework for supervised reconfiguration of satellite schedulers](https://doi.org/10.1007/s10270-026-01426-1)》则验证了单星机载软件配置的模型检查和受监督更新流程。后两项研究强化了软件实施与故障回退方面的证据，却分别属于特定软件任务管理和进程调度问题，不能和星座级轨道任务分配混为一个验证结果。

形式化方法还提供了一种不同于数值仿真的证据。《[Model checking of spacecraft operational designs: a scalability analysis](https://doi.org/10.1007/s10270-025-01281-6)》构建可调节复杂度的卫星模式管理模型，将其转换为不同模型检测工具的输入，比较组件交互与通信方式对状态空间和验证计算成本的影响。该研究说明形式检查能够在明确状态模型和规格条件下系统性寻找违规行为，但也暴露了状态空间随组件增加而膨胀的计算困难。对于未来星座自主运行系统，形式化约束检查、任务/资源仿真与物理在环测试应当验证不同层面的性质；只有明确各层模型如何对应，才能把局部正确性转化为对整套运行流程更可信的判断。

## 4.5 值得进一步推进的研究方向

**首先，应加强长期能力配置与具体任务可执行性之间的联系。** 当前库存、补网和服务设施研究已经能够联合处理多种供应途径、设施配置与成本目标，但库存可用性、转移到位时间及任务真正恢复服务的时刻仍可能采用不同定义。一个可检验的方向是在共同的卫星失效与任务需求场景下，将长期备份决策产生的可用资产状态传递到短期调度与轨道转移模型，比较静态可用性近似和显式考虑补位时延时的任务损失、恢复时间与总成本。该问题不应被表述为目前所有研究均未涉及，而应通过与现有联合维护和轨道服务模型进一步比较，确定仍缺少哪些约束或验证。

**其次，应在明确通信和故障条件的前提下评价分布式调度。** 现有研究已经利用几何分解、消息广播、通信机会预测及接触图联合路由改善大规模任务协调。后续更具说服力的比较应在一致的轨道与任务实例下控制链路延迟、丢包、暂时失联和节点失效等条件，同时报告任务收益、重复分配、消息数量、计算时延及故障后的恢复时间。这样才能区分不同算法真正来自局部优化结构的优势，以及依赖理想化信息共享条件获得的表现。

**再次，智能算法需要与物理约束及完整计算成本共同评价。** 在训练阶段使用大量仿真、在在线阶段只执行一次神经网络推理，与直接采用混合整数规划或局部搜索的计算路径不同。对于智能任务分配或轨迹规划，应同时记录离线训练、模型部署、在线响应、约束违规及回退修复的成本，并在不确定扰动和任务分布变化时测试性能。学习策略与安全屏蔽、形式化检查或优化修复相结合是一种值得继续研究的路径，但其可靠性必须明确落实到可检查的约束、失败条件和验证平台。

**最后，需要建立由模块到系统的逐级验证链条。** 星座运行管理不必要求每种算法都在完整在轨系统中单独演示，但应当尽可能提供可复现的模型和实验条件，并明确计划、执行、状态更新和回退机制之间的接口。面向系统集成，可先以真实任务请求或遥测数据测试感知和调度，再通过软件在环与硬件在环验证运行时序和故障恢复，最后在限定飞行任务中逐步扩大自主功能。对大型星座而言，扩展目标应包含协同的节点数量、任务持续时间和实际通信条件，而不是仅增加离散优化模型中的变量个数。

总体而言，大型星座智能管理研究的进展既表现为更复杂的联合优化模型和更高效的求解方法，也表现为状态反馈、机载软件及安全检查与任务决策逐步结合。未来工作的关键不只是追求更大的仿真规模或更高的单项收益，而是使长期配置、运行调度和执行反馈所采用的状态与约束能够相互对应，并在可追溯的试验条件下验证它们的实际作用。这一认识与第2章的系统问题定义和第3章的代表方法比较共同构成本文的分析主线。
