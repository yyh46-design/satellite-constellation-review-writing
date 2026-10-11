# v0.7新增学术引用的正文位置与依据

本表仅列本轮实际补入的48条学术引用。正式文末清单见REFERENCES_v0.7.md。位置按当前正文实际出现计算；同一来源跨节使用仍只计一次。书目身份已核对，来源查阅不等于作者完成全文技术验收。

| 编号 | 英文原标题及中文工作译名 | 正文位置 | 比较中使用的模型或机制 | 查阅依据 |
| --- | --- | --- | --- | --- |
| 19 | Space Logistics Modeling and Optimization: Review of the State of the Art / 空间物流建模与优化：研究现状综述 | 3.1 | 按应用问题与物流方法分类，覆盖ISAM、星座、网络流、排队和库存。 | 沿用一手记录：出版社正文片段与作者公开稿 |
| 22 | Satellite Constellation Pattern Optimization for Complex Regional Coverage / 面向复杂区域覆盖的卫星星座模式优化 | 3.1 | APC模式模型，以循环卷积关联访问模式和星座模式；二元整数线性规划。 | 本轮定向查阅：author arXiv abstract, formal journal DOI linked |
| 23 | Optimization of satellite constellation deployment strategy considering uncertain areas of interest / 考虑不确定关注区域的卫星星座部署策略优化 | 3.1 | 基于需求情景的部署策略优化，以期望生命周期成本为评价。 | 沿用一手记录：出版社摘要与模型概述 |
| 24 | Two-Stage Framework for Deployment-Aware Optimization of Satellite Constellation Pattern Design / 考虑部署过程的卫星星座模式设计两阶段优化框架 | 3.1 | 两阶段部署感知优化，协调注入／停泊轨道选取与最终星座模式。 | 本轮定向查阅：publisher abstract and section 2.4 deployment-feasibility definition |
| 26 | Spare Strategy Analysis and Design for Mega Satellite Constellations Using Markov Chain / 采用马尔可夫链的巨型卫星星座备份策略分析与设计 | 3.1 | 轨道面和停泊库存分别建马尔可夫链，用不动点迭代求联合一致稳态，再以 GA 优化策略。 | 本轮定向查阅：author arXiv abstract and registered abstract |
| 27 | Spare strategy for large-scale satellite constellations under dual resupply channels using Markov chain / 采用马尔可夫链的双补给通道大型卫星星座备份策略 | 3.1 | 耦合马尔可夫链与 RAAN 周期稳态。用不动点迭代和保留延迟统计的近似分析，再以 GA 最小化成本。 | 本轮定向查阅：author arXiv abstract |
| 33 | On-Orbit Servicing Optimization Framework with High- and Low-Thrust Propulsion Tradeoff / 兼顾高推力与低推力权衡的在轨服务优化框架 | 3.1、3.4 | MILP、用户定义轨迹模型与滚动时域。 | 本轮定向查阅：author arXiv abstract, formal journal DOI linked |
| 34 | On-orbit servicing system assessment and optimization methods based on lifecycle simulation under mixed aleatory and epistemic uncertainties / 混合随机与认知不确定性下基于全寿命仿真的在轨服务系统评估与优化 | 3.1 | 动态规划处理事件决策。概率与证据理论结合的 Monte Carlo 生命周期评估，再用 SOMUA-MCS 顺序优化。 | 沿用一手记录：出版社摘要与公开引言。 |
| 35 | Selecting and scheduling observations of agile satellites / 敏捷卫星观测任务的选择与调度 | 3.2 | 比较贪心、动态规划、约束规划和局部搜索等方法。 | 本轮定向查阅：original publisher PDF at university course repository; abstract and problem overview |
| 36 | A Generic Markov Decision Process Model and Reinforcement Learning Method for Scheduling Agile Earth Observation Satellites / 用于敏捷对地观测卫星调度的通用马尔可夫决策过程模型与强化学习方法 | 3.2 | 连续状态、离散动作的有限MDP；Q-learning训练Q网络处理排序，构造式启发式处理定时。 | 沿用一手记录：IEEE出版社摘要 |
| 37 | A decompose-and-learn multi-objective algorithm for scheduling large-scale earth observation satellites / 用于大规模对地观测卫星调度的分解学习多目标算法 | 3.2 | LS2MO-SS：动态学习任务分配演化算子，双向排序与全局修补。 | 沿用一手记录：出版社摘要与模型介绍 |
| 40 | Scheduling of Earth observing satellites using distributed constraint optimization / 采用分布式约束优化的对地观测卫星调度 | 3.2 | DCOP模型；DSTS中的DSA／MGM局部搜索，与集中调度方法比较。 | 本轮定向查阅：publisher abstract and introduction |
| 41 | Consensus-Based Decentralized Auctions for Robust Task Allocation / 用于鲁棒任务分配的基于一致性的去中心化拍卖 | 3.2 | CBAA与CBBA，将局部竞价、任务包构造与一致性机制结合。 | 本轮定向查阅：author institutional abstract, final published version identified |
| 43 | Distributed cooperative task planning algorithm for multiple satellites in delayed communication environment / 延迟通信环境下多卫星分布式协同任务规划算法 | 3.2 | DAG环境信息、DEC-POMDP协同框架；统一时延处理与模拟退火近似求解。 | 沿用一手记录：期刊公开摘要 |
| 44 | Onboard coordination and scheduling of multiple autonomous satellites in an uncertain environment / 不确定环境下多自主卫星的星上协调与调度 | 3.2 | 动态分布式组织。改进合同网 ICNP 与黑板模型 BM 协商，混合触发滚动规划配合自适应规则。 | 沿用一手记录：出版社论文摘要与公开引用中的方法片段，模型及实验全文待读。 |
| 45 | Asynchronous Communication Aware Multi-Agent Task Allocation / 异步通信感知的多智能体任务分配 | 3.2 | FMC_ATA，将Fisher市场清算式分配改为异步版本，并响应动态事件。 | 本轮定向查阅：official conference abstract |
| 46 | The integrated agile Earth observation satellite scheduling problem / 敏捷对地观测卫星成像与下传联合调度问题 | 3.2 | 联合调度优化；完整求解细节待全文提取。 | 沿用一手记录：出版社公开摘要 |
| 47 | Tip-and-cue mission scheduling in heterogeneous satellite constellations using mixed-integer linear programming / 采用混合整数线性规划的异构卫星星座提示—精细观测任务调度 | 3.2 | MILP＋时间窗聚类。 | 沿用一手记录：出版社公开引言与章节片段 |
| 48 | Optimization-based scheduling for the single-satellite, multi-ground station communication problem / 单卫星—多地面站通信问题的优化调度 | 3.2 | 优化调度与欠约束MIP，再通过后处理构造可行方案。 | 沿用一手记录：出版社摘要与建模说明 |
| 49 | Scheduling Space–Ground Communications for the Air Force Satellite Control Network / 美国空军卫星控制网络的星地通信调度 | 3.2 | 调度复杂度分析、遗传算法及其他启发式比较；单资源与多资源情形分开。 | 本轮定向查阅：author original PDF; abstract and communication-scheduling problem overview |
| 50 | Satellite downlink scheduling problem: A case study / 卫星下传调度问题：一个案例研究 | 3.2 | 调度生成过程将复杂约束封装为启发式接口，并比较元启发式。 | 沿用一手记录：作者机构公开稿 |
| 51 | Deep Space Network Scheduling via Mixed-Integer Linear Programming / 基于混合整数线性规划的深空网络调度 | 3.2 | 序贯MILP调度，与启发式方法比较。 | 沿用一手记录：IEEE Xplore正式出版记录核定题名、作者、卷页与日期；作者稿用于方法背景，正式全文尚待精读。 |
| 52 | Automated Scheduling for NASA's Deep Space Network / NASA深空网络的自动调度 | 3.2 | DSE调度引擎，将需求展开为跟踪时段，再搜索修复；支持网络协商流程。 | 本轮定向查阅：publisher abstract and registered abstract |
| 54 | Deep Multiagent Reinforcement Learning for Task Offloading and Resource Allocation in Satellite Edge Computing / 卫星边缘计算任务卸载与资源分配的深度多智能体强化学习 | 3.2 | MATORA将混合整数非线性问题分解为多智能体卸载决策与凸资源优化，最小化加权时延。 | 沿用一手记录：IEEE出版社摘要 |
| 55 | Multi-agent reinforcement learning based computation offloading and resource allocation for LEO Satellite edge computing networks / LEO卫星边缘计算网络中基于多智能体强化学习的计算卸载与资源分配 | 3.2 | MADDPG，集中训练、分散执行；全局奖励协调多个资源变量。 | 沿用一手记录：出版社摘要与方法介绍 |
| 56 | Satellite Edge Intelligence: DRL-Based Resource Management for Task Inference in LEO-Based Satellite-Ground Collaborative Networks / 卫星边缘智能：LEO星地协同网络任务推理的深度强化学习资源管理 | 3.2 | SD3深度强化学习结合数值优化，决定推理卸载与相关资源。 | 沿用一手记录：IEEE出版社摘要 |
| 57 | Orbit-aware task scheduling in satellite edge computing / 卫星边缘计算中的轨道感知任务调度 | 3.2 | 轨道运动与网络模型、分布式资源分配和离散事件仿真。 | 本轮定向查阅：publisher abstract and registered abstract |
| 58 | Kodan: Addressing the Computational Bottleneck in Space / Kodan：应对空间计算瓶颈 | 3.2 | 离线生成专用ML模型，运行时按样本地理上下文动态选择模型与处理精度。 | 本轮定向查阅：author institutional abstract |
| 59 | A pure proactive scheduling algorithm for multiple earth observation satellites under uncertainties of clouds / 云层不确定条件下多颗对地观测卫星的纯主动式调度算法 | 3.2、4.2 | 禁止序列分配建模、机会约束与样本近似；ILP分支切割及惰性约束。 | 沿用一手记录：出版社摘要与模型概述 |
| 60 | Robust Earth Observation Satellite Scheduling With Uncertainty of Cloud Coverage / 云覆盖不确定性下的鲁棒对地观测卫星调度 | 3.2、4.2 | 预算不确定集的线性鲁棒建模与列生成启发式，以轨道相关调度方案构造列。 | 沿用一手记录：IEEE出版社摘要 |
| 61 | Mixed-integer programming models for optimal constellation scheduling given cloud cover uncertainty / 考虑云覆盖不确定性的最优星座调度混合整数规划模型 | 3.2、4.2 | 确定性MIP及两阶段、三阶段随机MIP；预计算轨道和传感器机会。 | 沿用一手记录：出版社摘要与实验规模说明 |
| 63 | Dynamic task scheduling optimization by rolling horizon deep reinforcement learning for distributed satellite system / 采用滚动时域深度强化学习的分布式卫星系统动态任务调度优化 | 3.2 | MAMDP 建模。RH-MAPPO 用滚动时域，集中训练、各星独立执行，双损失改善训练。 | 沿用一手记录：出版社摘要及公开引言。 |
| 67 | Mission planning for on-orbit servicing through multiple servicing satellites: A new approach / 通过多个服务卫星开展在轨服务的任务规划：一种新方法 | 3.2 | 多目标粒子群＋Lambert转移；Taguchi参数设计。 | 沿用一手记录：出版社摘要与公开章节片段 |
| 68 | GEO satellite on-orbit refueling and debris removal hybrid mission planning under uncertainty / 不确定性下 GEO 卫星在轨加注与碎片移除混合任务规划 | 3.2、4.2 | 两阶段转移建立目标轨道间有向图。分别构造随机期望模型与盒不确定集鲁棒模型。 | 沿用一手记录：出版社摘要、公开引言和章节说明。 |
| 69 | Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations / 摄动条件下低推力服务卫星的最优多客户轨迹规划 | 3.2 | 转移代价预计算／插值与组合路径优化。 | 本轮定向查阅：publisher abstract and section 2 assumption A.1 |
| 71 | Risk-aware sensor scheduling and tracking of large constellations / 大型星座的风险感知传感器调度与跟踪 | 3.3 | 信息增益＋碰撞风险奖励，LMB多目标滤波与循环任务分配。 | 沿用一手记录：出版社摘要与公开章节片段 |
| 74 | Spacecraft collision avoidance challenge: Design and results of a machine learning competition / 航天器碰撞规避挑战赛：机器学习竞赛的设计与结果 | 3.3 | 机器学习竞赛设计、数据集、评价指标与参赛方法结果分析。 | 本轮定向查阅：publisher abstract and registered abstract |
| 75 | Safe Trajectories for Autonomous Rendezvous of Spacecraft / 航天器自主交会的安全轨迹 | 3.3 | 把被动碰撞规避要求作为轨迹约束，分析安全与燃料的权衡；具体构造需正式全文复核。 | 沿用一手记录：出版记录、MIT 作者发表目录及作者上传期刊稿摘要。尚未逐项核对定理。 |
| 76 | Autonomous Trajectory Planning for Rendezvous and Proximity Operations by Conic Optimization / 采用锥优化的交会与近距离操作自主轨迹规划 | 3.3 | 非线性最优控制经无损松弛与逐次求解转为 SOCP 子问题。 | 沿用一手记录：作者上传的期刊论文摘要与公开正文片段（ResearchGate），DOI 另由 Crossref 核对。 |
| 77 | Model Predictive Control of Swarms of Spacecraft Using Sequential Convex Programming / 采用序贯凸规划的航天器群模型预测控制 | 3.3 | 邻居通信的分散式 MPC，使用 SCP 迭代近似路径问题，并在执行期间更新。 | 本轮定向查阅：author institutional abstract |
| 83 | Imbalanced satellite telemetry data anomaly detection model based on Bayesian LSTM / 基于贝叶斯LSTM的不平衡卫星遥测数据异常检测模型 | 3.3、4.2 | MC dropout双向LSTM，用方差、熵和互信息刻画不确定性；VAE复评高不确定样本。 | 沿用一手记录：出版社摘要与方法说明 |
| 84 | Validation-gated continual learning for anomaly detection in satellite telemetry / 用于卫星遥测异常检测的验证门控持续学习 | 3.3 | 验证门控的持续再训练、记忆回放与LSTM预测，围绕Telemanom流程更新。 | 沿用一手记录：出版社摘要与实验设置概述 |
| 87 | RPRS: a reactive plan repair strategy for rapid response to plan failures of deep space missions / RPRS：快速响应深空任务计划失败的反应式计划修复策略 | 3.3 | forwarding dock state时间状态表示，GRDR资源诊断修复与TDPR小偏差搜索，合并重调度。 | 沿用一手记录：出版社摘要与机制概述 |
| 88 | Towards the automated operations of large distributed satellite systems. Part 2: Classifications and tools / 迈向大型分布式卫星系统自动化运行，第二部分：分类与工具 | 3.4 | 分布式卫星系统分类及自动化运行工具。 | 沿用一手记录：出版社公开内容与Crossref题名 |
| 89 | Artificial Intelligence for Trusted Autonomous Satellite Operations / 面向可信自主卫星运行的人工智能 | 3.4 | AI与信息物理系统支撑的分布式卫星运行，关注安全、可信、自主及应用挑战。 | 沿用一手记录：出版社公开摘要和正文片段 |
| 91 | Remote Agent: to boldly go where no AI system has gone before / Remote Agent：大胆迈向此前AI系统未曾涉足的领域 | 3.4 | 模型驱动的时序规划、多线程执行，以及模式识别与重配置。 | 本轮定向查阅：author original: architecture, sections 1.4 and 2 |
| 95 | Basilisk: A Flexible, Scalable and Modular Astrodynamics Simulation Framework / Basilisk：灵活、可扩展且模块化的航天动力学仿真框架 | 3.4 | 模型与运行循环解耦、消息传递模块结构、C／C++计算与Python接口。 | 沿用一手记录：作者公开正式期刊全文 |
| 96 | Formal Methods for Trusted Space Autonomy: Boon or Bane? / 可信空间自主系统的形式化方法：助力还是阻碍？ | 3.4 | 结合已部署任务经验，分析形式化验证、运行时验证和常规测试的适用范围。 | 本轮定向查阅：author original: abstract and verification-practice scope |

新增工程资料：CCSDS Conjunction Data Message标准（编号102）及NASA Core Flight System - Demo Bundle（编号106）。两者的具体来源与范围见文末清单及来源记录。
