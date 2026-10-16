# B10 替代候选定向核读记录

本记录依据各候选实际可读正文，不依据摘要补全方法。英文原题及中文非官方译名并列；各条页码为PDF物理页，ALT03另注印刷页，ALT11含版权封面。所有记录均为AI定向核读，human_verified=false，未逐页全文精读、未独立复现实验。

每篇的完整文件哈希、逐页看页记录与版本身份见SOURCE_MANIFEST_B10.json；44条定位命题见CLAIM_CHECKS_B10.json。

## ALT01 An Energy-Aware Task Scheduling for Quality-of-Service Assurance in Constellations of Nanosatellites

面向纳卫星星座服务质量保障的能量感知任务调度

- 作者：Laio Oriel Seman; Brenda F. Ribeiro; Cezar A. Rigo; Edemar Morsch Filho; Eduardo Camponogara; Rodrigo Leonardi; Eduardo A. Bezerra
- 正式DOI：10.3390/s22103715；实际阅读标识：10.3390/s22103715
- 版本：出版社开放获取正式PDF；[全文入口](https://mdpi-res.com/d_attachment/sensors/sensors-22-03715/article_deploy/sensors-22-03715-v3.pdf?version=1653469277)
- 核读范围：§3建模与ε约束方法；§4实验；§5结论；正文页[4, 5, 6, 10, 11, 12, 13, 17]；实际看页[5, 11, 17]。
- 方法：个体任务、共享任务、可选同时冗余，轨道光照与电池SoC约束；MILP用Gurobi求解。
- 验证条件：1—5星；同轨等间隔、623 km、96 min轨道；Julia/JuMP、Gurobi GAP≤1%；Xeon E5-2630 v4 2.20 GHz，20核40线程，64 GB，Ubuntu 20.04.2。
- 综述判断（推论）：论文给出个体与集体任务QoS及冗余之间的可行权衡，适合解释能量模型如何改变任务选择。
- 证据边界：§5明确把branch-and-price列为未来工作。不能保留原[33]已实现分支定价的描述；1—5星不是巨型星座验证；求解停止间隙不等于严格全局最优。
- 未关闭项：若综述要讨论分支定价定价子问题、列生成和大星座耗时，仍需原[33]正文或另找同类已核读来源。
- 替代建议：推荐按论点改写后采用；对应原来源[33]。

## ALT02 RL-GA: A Reinforcement Learning-based Genetic Algorithm for Electromagnetic Detection Satellite Scheduling Problem

RL-GA：面向电磁探测卫星调度的强化学习遗传算法

- 作者：Yanjie Song; Luona Wei; Qing Yang; Jian Wu; Lining Xing; Yingwu Chen
- 正式DOI：10.1016/j.swevo.2023.101236；实际阅读标识：10.1016/j.swevo.2023.101236
- 版本：作者公开的出版社排版全文；[全文入口](https://yanjiesong.github.io/files/RLGA2023.pdf)
- 核读范围：§3.1.6 Q-learning；§3.2 TTWSA；§4.1设置；§4.2.3及表6耗时；正文页[4, 5, 6, 7, 8, 10, 11]；实际看页[6, 8, 11]。
- 方法：Q表按适应度是否改善选择交叉、变异及其组合；时间窗选择器承担可行解码。
- 验证条件：2星、100—1400任务；30次运行；共同5000次评价预算；MATLAB 2020a，Core i7-7700 3.6 GHz，16 GB，Windows 11；STK 11.2生成窗口。
- 综述判断（推论）：可支撑学习位于搜索算子选择层的归类。表6列出1400任务实例约4秒的CPU时间，但个别实例并非所有方法中最快。
- 证据边界：不是深度强化学习、不是大邻域搜索，也未据所核读内容验证在线应急任务到达。任务数不能换成卫星数；案例流程不能当作独立确认的在轨实测。
- 未关闭项：原[63]的DRL-LNS在线重调度机理、训练成本和请求到达实验仍待原文；若采用ALT02，应把代表性论点改为学习辅助搜索。
- 替代建议：推荐按论点改写后采用；对应原来源[63]。

## ALT03 Handover Protocol Learning for LEO Satellite Networks: Access Delay and Collision Minimization

低轨卫星网络的切换协议学习：接入时延与碰撞最小化

- 作者：Ju-Hyung Lee; Chanyoung Park; Soohyun Park; Andreas F. Molisch
- 正式DOI：10.1109/TWC.2023.3342975；实际阅读标识：10.1109/TWC.2023.3342975
- 版本：USC公开的正式排版PDF（另取得arXiv v1）；[全文入口](https://wides.usc.edu/Updated_pdf/Handover%20Protocol%20Learning%20for%20LEO%20Satellite%20Networks%3A%20Access%20Delay%20and%20Collision%20Minimization.pdf)
- 核读范围：§III协议与碰撞；§IV学习；§V及表III、V；正文页[3, 4, 5, 9, 10, 11, 12]；实际看页[9, 11]。
- 方法：DHO用学习预测接入条件，省去测量报告环节；分别处理资源块不足与随机接入前导碰撞。
- 验证条件：1服务星＋2目标星、3轨道面、550 km；1000×1000 m²用户区域；表III用户数10—200；IMPALA、部分可观测状态仿真。
- 综述判断（推论）：表V显示接入时延改善时PRACH碰撞仍可能高于随机方案，适合综述解释多指标权衡。
- 证据边界：接入协议时延不是端到端路由时延；3星场景不能表述为多层巨型星座实测。训练用户规模增加带来额外成本。
- 未关闭项：原[77]路由代价与切换联合决策仍未被替代；若要保留该专门结论，仍需原文。ALT03与其arXiv副本未逐式对照。
- 替代建议：推荐按论点改写后采用；对应原来源[77]。

## ALT04 Beam Management in Low Earth Orbit Satellite Communication With Handover Frequency Control and Satellite-Terrestrial Spectrum Sharing

兼顾切换频率控制与星地频谱共享的低轨卫星波束管理

- 作者：Yaohua Sun; Jianfeng Zhu; Mugen Peng
- 正式DOI：候选 10.1109/TCOMM.2024.3516479；实际阅读标识：10.48550/arXiv.2404.08967
- 版本：arXiv v1作者预印本；[全文入口](https://arxiv.org/pdf/2404.08967v1)
- 核读范围：§III约束与Lyapunov转换；§IV分解；§V实验；正文页[1, 5, 6, 10, 11]；实际看页[5, 10]。
- 方法：以虚拟队列处理长期切换频率；分解星间切换、跳波束与星地频谱共享。
- 验证条件：背景1200星（30×40）、20波束小区、200地面基站簇；每小区始终由2颗可见星服务的简化；理论复杂度而非已核得的硬件计时。
- 综述判断（推论）：能补充长期切换约束与短时波束决策之间的时间尺度连接，也表明全星座规模与局部优化规模应分开报告。
- 证据边界：是卫星—地面基站共存，不是GEO—LEO共存。页面复核确认式(14)显示两二元量之和等于0，不能自行改成≤1；正式发表作者顺序与v1不同，全文同一性未核。
- 未关闭项：正式DOI仅为候选匹配：ComSoc官方目录确认题名、作者Jianfeng Zhu/Yaohua Sun/Mugen Peng、2025、5247—5263，但未取得正式全文逐式对照。保留预印本身份，不复述公式证明或绝对增益。
- 替代建议：机制候选；公式和版本待核；对应原来源[75, 77]。

## ALT05 Multi-Satellite Beam Hopping and Power Allocation Using Deep Reinforcement Learning

基于深度强化学习的多卫星跳波束与功率分配

- 作者：Xia Xie; Kexin Fan; Wenfeng Deng; Nikolaos Pappas; Qinyu Zhang
- 正式DOI：候选 尚未确认；实际阅读标识：10.48550/arXiv.2501.02309
- 版本：arXiv v1作者预印本；正式发表记录未确认；[全文入口](https://arxiv.org/pdf/2501.02309v1)
- 核读范围：§II队列；§III问题；§IV混合动作PPO；§V及表II；正文页[3, 4, 5, 6, 7, 9, 11]；实际看页[9]。
- 方法：集中式NOCC利用队列、信道状态；共享底座的离散选束与连续功率双输出PPO；惩罚波束重叠和超功率。
- 验证条件：5星、161小区、每星8波束、550 km、2 ms时隙；表II为10000回合、每回合200步。
- 综述判断（推论）：适合解释混合离散—连续动作表示，以及吞吐与队列等待时延之间的权衡。
- 证据边界：第9页正文带宽500 MHz，表II为100 MHz，已实际看页确认；不采信其绝对性能数字。软惩罚不是逐动作硬可行性证明；不是各星独立智能体。
- 未关闭项：带宽口径、实现、训练及推理硬件时间、正式发表版本待核。既有[76]已具作者正文，不因形式完整性而强行替换。
- 替代建议：储备；不采用绝对性能数字；对应原来源[75, 76]。

## ALT06 Using ground relays for low-latency wide-area routing in megaconstellations

利用地面中继实现巨型星座低时延广域路由

- 作者：Mark Handley
- 正式DOI：10.1145/3365609.3365859；实际阅读标识：10.1145/3365609.3365859
- 版本：UCL机构仓储标注的接受稿；[全文入口](https://discovery.ucl.ac.uk/id/eprint/10090242/1/hotnets-ucl.pdf)
- 核读范围：§2部署及密度；§3路由计算与差分更新；§4混合网络；afterword；正文页[1, 2, 3, 4, 5, 6, 7]；实际看页[3, 5]。
- 方法：卫星—地面中继交替转发；分块索引、保留扩展可见边及差分时延预测降低重复建图开销。
- 验证条件：2019设计仿真；1584星与5000中继的单源到全目的计算，2.7 GHz Core i7；文中报告朴素1.55 s与优化61 ms。
- 综述判断（推论）：地面中继密度、路径时延、路径变化频率和建图成本应一起讨论；可支持无ISL或混合ISL网络的架构比较。
- 证据边界：历史部署假设不是当前Starlink运行事实；最短路径传播时延和路由计算耗时是不同指标。不是原[79]/[80]具体算法、DBTS+/LFA+恢复实验的复现。
- 未关闭项：接受稿与正式版差异未核；不把2019理想光纤或当时Internet对照移植为2026现网结论。
- 替代建议：推荐按论点改写后采用；对应原来源[79, 80]。

## ALT07 A Lightweight and Scalable Design of Segment Routing in Broadband LEO Constellations Using Landmark-Based Skeleton Graphs

基于地标骨架图的宽带低轨星座轻量化可扩展分段路由设计

- 作者：Menglan Hu; Chenxin Wang; Bin Cao; Benkuan Zhou; Yan Dong; Kai Peng
- 正式DOI：候选 尚未确认；实际阅读标识：10.48550/arXiv.2411.19679
- 版本：arXiv v1作者预印本；正式发表记录未确认；[全文入口](https://arxiv.org/pdf/2411.19679v1)
- 核读范围：§III四邻ISL模型；§IV骨架与概率转发；§VII实验；正文页[1, 3, 4, 5, 9, 10, 11, 12]；实际看页[10, 11, 12]。
- 方法：地面SDN抽象区域与地标骨架，区内概率多径分段转发；采用四邻ISL二维环面及静态时间片近似。
- 验证条件：NetworkX/Python；320—3920节点；隧道数2.5k—80k；Core i5-1135G7 2.4 GHz，16 GB；延迟为负载函数模型。
- 综述判断（推论）：可作为层次化路径表达的机制候选，不能拿来支撑无ISL地面转发。图9中部分情形Dijkstra的Gini更低，不能说全指标优于Dijkstra。
- 证据边界：正文把Dijkstra耗时增长解释为指数级，与其一般算法复杂度不能等同。第12页108 s为一百零八秒，非10^8秒；图11坐标已看页。不采用其普遍性能优势结论。
- 未关闭项：代码、基线实现、重复次数、延迟标定、故障恢复有效性及正式发表版本未核；本轮未完整核验§VI证明与全部§V失效路径。
- 替代建议：储备；仅用于机制归类；对应原来源[79, 80]。

## ALT08 A model-driven framework for supervised reconfiguration of satellite schedulers

面向卫星调度器受监督重配置的模型驱动框架

- 作者：Francesco Basciani; Arianna Fedeli; Daniele Masti; Ludovico Iovino; Paolo Serri; Patrizio Pelliccione
- 正式DOI：10.1007/s10270-026-01426-1；实际阅读标识：10.1007/s10270-026-01426-1
- 版本：Springer开放获取正式PDF；[全文入口](https://link.springer.com/content/pdf/10.1007/s10270-026-01426-1.pdf)
- 核读范围：§3.1—3.4模型和受监督流程；§4.1专家评价；§4.2及表5工具链；§4.3威胁；§5讨论；正文页[7, 8, 10, 12, 15, 17, 18, 20, 22]；实际看页[8, 15, 20]。
- 方法：Ecore/EMF模型、EVL校验、XMI交换与EGL生成；遥测触发候选优化，人工审定后交平台激活；Table1区分模型变化与部署配置变化。
- 验证条件：13个星上软件进程、27次ACT、16 BTS/32 ticks，约125 ms循环；6名TAS-I专家；Apple M3 Pro、32 GB；表5是解析/校验/生成开销。
- 综述判断（推论）：适合补强优化模型如何成为可检查、可追溯、受监督配置的接口论述；同页表5明确工具链计时不代表大规模运行验证。
- 证据边界：CPU/星上软件调度层，与星座任务调度不同；<1 ms是各工具链步骤，不是优化器或整星座重规划时延。不是在轨部署证明；作者明确本篇不重新验证优化核心。
- 未关闭项：若要保留原[112]参考架构职责或NIMBUS例子，仍需原文；本篇只能改写为独立的模型驱动受监督配置实例。未核读全部31页与前作优化器。
- 替代建议：推荐按论点改写后采用；对应原来源[112]。

## ALT09 Link-identified Routing Architecture in Space

面向空间网络的链路标识路由架构

- 作者：Hefan Zhang; Zhiyuan Wang; Shan Zhang; Qingkai Meng; Hongbin Luo
- 正式DOI：10.1109/TNSE.2024.3498042；实际阅读标识：10.48550/arXiv.2411.10926
- 版本：arXiv v1作者预印本；已匹配正式书目但未核对版本；[全文入口](https://arxiv.org/pdf/2411.10926v1)
- 核读范围：§III BF转发；§IV分段；§V链路失败；§VI星地切换；§VII实验；正文页[3, 5, 9, 11, 12, 13, 14]；实际看页[9, 14]。
- 方法：包内Bloom filter编码链路ID；分段再编码平衡额外转发和编码时延；本地重路由ODR与预定绕行ODD，组播缓冲应对星地切换。
- 验证条件：INET 4.2.2/OMNeT++，66星Iridium、780 km、10 Mbps ISL、1 KB包、10 μs BF替换；MATLAB数值与包级实验分开。
- 综述判断（推论）：适合补足分段表示、链路失效局部响应及切换期间传输保持。§VII-F给出重算路线与预设绕行在时延和交付率上的区别。
- 证据边界：不是无ISL地面转发，也不是原[80]同算法。66星仿真非千星实测；BF误报有额外转发成本；§VII-B说明MATLAB和OMNeT++对环路处理不同。
- 未关闭项：正式论文17页与本轮预印本16页的文字/公式/图表差异未核；无正式版同一性结论。不能把数值模型吻合扩大为所有网络条件定理已验证。
- 替代建议：推荐按论点改写后采用；标明版本；对应原来源[77, 79, 80]。

## ALT10 A Dynamic Scheduling Method of Earth-Observing Satellites by Employing Rolling Horizon Strategy

采用滚动时域策略的对地观测卫星动态调度方法

- 作者：Qiu Dishan; He Chuan; Liu Jin; Ma Manhao
- 正式DOI：10.1155/2013/304047；实际阅读标识：10.1155/2013/304047
- 版本：出版社完整HTML可由网页工具读取；本地GET与PDF均403；[全文入口](https://onlinelibrary.wiley.com/doi/10.1155/2013/304047)
- 核读范围：出版社HTML §2—4，行166—367；公式图像未实际页面核验；正文页[]；实际看页[]。
- 方法：周期＋事件触发更新等待/新到任务集，再用启发式分配；在滚动框架下修订尚未执行任务。
- 验证条件：4—6星、100—400任务随机场景；MATLAB2007，Pentium IV 3.06 GHz、2 GB、Windows XP；缺少可读公式页面。
- 综述判断（推论）：可作动态请求到达与滚动时域的基础例证，不能代替[59]分层MIP的大规模实验。
- 证据边界：HTML有公式缺项及WIS/CIS命名不一致；不采公式和百分比增益；没有PDF文件及其页数/哈希。
- 未关闭项：欲核对公式、图3/4和算法命名仍需PDF；仅依据HTML已核读的定性流程。
- 替代建议：基础方法候选；定性采用；对应原来源[59, 63]。

## ALT11 Multi-Agent DDPG-Based Joint Beam Hopping and Resource Allocation for Cognitive GEO-LEO Satellite Networks

认知GEO–LEO卫星网络中基于多智能体DDPG的联合跳波束与资源分配

- 作者：Quynh Tu Ngo; Ying He; Beeshanga Jayawickrama; Eryk Dutkiewicz
- 正式DOI：10.1109/LNET.2025.3605531；实际阅读标识：10.1109/LNET.2025.3605531
- 版本：UTS机构公开作者全文；接受稿/正式版身份未确证；[全文入口](https://opus.lib.uts.edu.au/bitstream/10453/189674/3/Multi-Agent%20DDPG-Based%20Joint%20Beam%20Hopping%20and%20Resource%20Allocation%20for%20Cognitive%20GEO-LEO%20Satellite%20Networks.pdf)
- 核读范围：正文§II—V；式7—9；图2；表I和图4—6（物理页含封面）；正文页[2, 3, 4, 5, 6]；实际看页[4, 5, 6]。
- 方法：以小区簇作为智能体，集中评论器训练、分散执行，联合选束/子带/功率；目标含吞吐与服务时延极差，超GEO聚合干扰进入奖励惩罚。
- 验证条件：1 GEO Inmarsat-4F2＋1 LEO Iridium-NEXT914覆盖；261 LEO小区分17簇=17智能体；100 ms周期；2100训练回合。
- 综述判断（推论）：最贴近[75]的GEO—LEO共存主题，可解释联合资源动作与干扰限制，但须把多星负载平衡改成该论文的小区资源决策。
- 证据边界：物理第5页50—200 kbps，第6页图4/6为Mbps，页面确认；不采用绝对流量及提升百分比。软惩罚不等于每动作满足硬限制；17智能体不是17颗星。
- 未关闭项：流量单位、正式版对应和时延极差目标与平均时延结果的口径待核；不声称取得原[75]正文。
- 替代建议：推荐机制改写；参数与版本待核；对应原来源[75]。
