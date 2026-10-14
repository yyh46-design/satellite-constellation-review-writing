# 后续文献精读与精修优先队列

基准为v1.6冻结来源记录叠加本会话v1.7双语引用位置；排序根据**正文命题证据缺口**，不是论文质量或算法性能排名。

## P0｜五篇正文缺口

首先查可合法获取的出版方、作者及机构正式文件。仍无法取得时，不再依靠摘要推导具体实验、消融和性能数字。

|编号|文献标题|中文引用块数|核验时关注的边界|
|---|---|---:|---|
|[75]|NGSO Satellites Beam Hopping Strategy Based on Load Balancing and Interference Avoidance for Coexistence With GSO Systems|4|未获正文，具体关联、干扰和基线未知|
|[77]|Routing cost-integrated intelligent handover strategy for multi-layer LEO mega-constellation networks|3|仅摘要，单层学习与跨层抖动成本细节待核|
|[79]|Scalable routing in low-Earth orbit satellite constellations: Architecture and algorithms|4|DBR/DAR方法及稳定收益的全文依据缺失|
|[80]|Segment routing for traffic engineering and effective recovery in low-earth orbit satellite constellations|4|分段流量工程不可写成物理容量分配已证|
|[112]|Reference architecture for autonomy and adaptivity in satellites|3|MAPE-K完整接口、NIMBUS验证、性能未知|

## P0｜四篇正式版本对照

逐命题比较已读arXiv作者稿与正式期刊：参数、公式、图表、基线及结论分别登记same/changed/not_used/unverified。

|编号|文献标题|中文引用块数|核验时关注的边界|
|---|---|---:|---|
|[53]|Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing|8|先采集后星地处理；Wiley正式版仍未逐命题对照|
|[74]|Joint Beam Scheduling and Power Optimization for Beam Hopping LEO Satellite Systems|6|作者稿8束61位置；正式版与页码冲突均未关闭|
|[76]|Demand-Aware Beam Hopping and Power Allocation for Load Balancing in Digital Twin Empowered LEO Satellite Networks|7|FPA/DPA整体策略，不是纯功率因果消融；IEEE正式版待核|
|[121]|On-Demand Routing in LEO Mega-Constellations With Dynamic Laser Inter-Satellite Links|8|作者稿有PDF局部像素检查，IEEE正式版未核；不等于星载在线期限|

## P1｜出版PDF与版本细节

核正文文字提取与正式PDF图表/符号；[73]预测误差不可直接变成实际吞吐收益，[107]规则不等式尤其需要检查原页。

|编号|文献标题|中文引用块数|核验时关注的边界|
|---|---|---:|---|
|[73]|A Hybrid Forecasting Model for Self-Similar Traffic in LEO Mega-Constellation Networks|4|ON/OFF合成流量；预测误差不等于路由收益；正式PDF图表和水印待核|
|[107]|Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling|3|正式提供正文文本，规则符号和水印混排待原PDF核|

## P1｜竞争综述全文

当前只核公开摘要，不能据摘要声称现有综述全文均忽略跨业务管理。要写覆盖缺口，必须取得对应正文。

|编号|文献标题|中文引用块数|核验时关注的边界|
|---|---|---:|---|
|[7]|低轨巨型星座智能组网技术综述|2|按原稿证据范围使用，未作本轮整篇内容核验|
|[8]|低轨通信卫星星座网络资源管控与优化技术综述|2|按原稿证据范围使用，未作本轮整篇内容核验|

## P1｜第3–4章核心原始研究

优先核观测调度、资源耦合、学习辅助、安全事件和在轨运行案例的模型假设、指标分母及证据类型。

|编号|文献标题|中文引用块数|核验时关注的边界|
|---|---|---:|---|
|[33]|A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites|4|按原稿证据范围使用，未作本轮整篇内容核验|
|[34]|Decentralized Observation Allocation for a Large-Scale Constellation|4|按原稿证据范围使用，未作本轮整篇内容核验|
|[42]|Joint Observation and Transmission Scheduling in Agile Satellite Networks|4|按原稿证据范围使用，未作本轮整篇内容核验|
|[43]|Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm|2|按原稿证据范围使用，未作本轮整篇内容核验|
|[59]|Lagrangian hierarchical mixed-integer programming for ultra-large-scale satellite scheduling under dynamic task delivery|2|按原稿证据范围使用，未作本轮整篇内容核验|
|[63]|Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites|4|按原稿证据范围使用，未作本轮整篇内容核验|
|[65]|Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations|6|仅共享已完成状态不含未来计划意图，作者稿与正式版本待核|
|[84]|Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques|2|按原稿证据范围使用，未作本轮整篇内容核验|
|[89]|Starlink Collision Avoidance CONOPS|3|按原稿证据范围使用，未作本轮整篇内容核验|
|[114]|What is Starling?|5|按原稿证据范围使用，未作本轮整篇内容核验|

## P2｜旧精读重新锁定版本

部分记录只有旧版已精读结论，需补当年读到的PDF版本/页码、可重复找到的模型和实验局限。

|编号|文献标题|中文引用块数|核验时关注的边界|
|---|---|---:|---|
|[18]|Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control|4|按原稿证据范围使用，未作本轮整篇内容核验|
|[35]|Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation|4|按原稿证据范围使用，未作本轮整篇内容核验|
|[66]|A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling|2|按原稿证据范围使用，未作本轮整篇内容核验|
|[71]|Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit|3|按原稿证据范围使用，未作本轮整篇内容核验|
|[101]|Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry|1|按原稿证据范围使用，未作本轮整篇内容核验|
|[102]|Knowledge-based satellite failure detection, isolation and recovery (FDIR)|2|按原稿证据范围使用，未作本轮整篇内容核验|
|[119]|A model-driven framework for supervised reconfiguration of satellite schedulers|2|按原稿证据范围使用，未作本轮整篇内容核验|

## 每篇达到可用于逐句精修的关闭标准

一篇文献必须有实际阅读版本、可靠PDF/HTML源、具体节/图/表/页、模型变量与负载条件、对照方法与结果解释，并在v1.7中英文句子、表格和结论中作一致处理。无法打开正式版则保留not_verified；仅书目身份通过不等于方法或实验支持。

论文已有人工作者终核标志仍为false；本队列没有新读完任何第三方全文。