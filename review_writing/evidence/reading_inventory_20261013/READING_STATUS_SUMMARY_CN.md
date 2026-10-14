# 星座管理综述：已精读／已核读文献的历史证据审计

更新时间：2026-10-13（美国东部时间）。冻结基准为提交 de1291575bf4e28d7c404e3c7b78c49f64079deb 下的 v1.6 主稿与来源登记，以及本会话完成但尚未推送的 v1.7 来源—主张记录。**本轮没有重新下载、通读或复现实验，审计的是已保存的阅读证据。**

## 一、统计口径

|阅读状态|篇数/项数|允许使用的结论|
|---|---:|---|
|A 正式出版正文定向核读|6|已检查支撑主稿特定命题的正式PDF、正式归档XML或出版方全文文本；不等于全篇逐页验证|
|B 公开作者稿定向核读|4|方法、实验及限制仅对已读作者稿成立；正式版一致性未关闭|
|C 历史一手原文定向精读记录|7|较早记录明确标注方法、实验和限制已核；仍有版本、页节定位待补|
|D 特定章节或局部正文核读|8|有具体局部阅读依据，但不足以升级为整篇精读|
|E 本轮核心全文未取得|5|仅摘要/出版社或机构条目，不能称具体变量、实验结果已经核实|
|F 其他学术文献，定向精读尚未被记录证明|81|继承书目与此前摘要/片段；不等于它们从未有人阅读|
|G 工程、标准和运营官方资料|10|不以论文精读口径计数，需按官方版本核验接口或事件|
|**总计**|**121**|111篇学术来源和10项工程/标准资料|

**可严格认定有定向正文核读或历史精读依据：17篇（A6+B4+C7）。另有8篇明确的部分正文核读记录，共25篇具有至少某种正文或章节定位。** 这不是把25篇宣称为“通篇精读”，也不能把v1.4、Round1与Round2对同一篇的重读重复累加。

## 二、A类：6篇正式出版正文定向核读

[73]与[107]采用出版方提供的正式正文**文本**，其PDF页面像素、水印及符号尚有开放项；[9][78][81][106]的正式出版源核读来自较早轮次，并非本轮重新逐页审查。

|编号|文献题名|版本或当前可见证据|实际核查的命题/范围|边界或待核项|
|---|---|---|---|---|
|[9]|Toward Integrated Satellite Operations and Network Management: A Review and Novel Framework|正式出版PDF；定向核读记录继承Round1|三类交互模式与四种具体架构分属不同分类层级；16星集成原型对best-effort；非三类模式同场景比较|三类交互模式不是四个具体架构；16星集成原型不支持模式统一排名|
|[73]|A Hybrid Forecasting Model for Self-Similar Traffic in LEO Mega-Constellation Networks|MDPI提供的正式全文文本；未完成PDF像素复核|使用ON/OFF合成自相似流量；未验证路由收益|ON/OFF合成流量；预测误差不等于路由收益；正式PDF图表和水印待核|
|[78]|A Multifaceted Look at Starlink Performance|正式WWW 2024排版PDF；Round1记录|15秒边界波动在单候选卫星窗口仍出现；内部调度只是作者解释|单候选卫星窗口波动不等于直接读出内部调度算法|
|[81]|Hierarchical Resource Management for Mega-LEO Satellite Constellation|正式PMC归档XML，PMC11820243；Round1记录|NCC/空间基站/终端职责与需求价格交换；分项组件及负载比较，不叠加成完整架构统一增益|正式PMC图号不同于预印本，组件增益不可相加|
|[106]|A delay-tolerant network approach to satellite pickup and delivery scheduling|正式出版PDF；13页；Round1记录|逐请求联合选择节点与交付路径，扣减接触容量；无限存储能源；交付增加改变成功样本；源/局部路由随接触失效条件变化|逐请求选择而非全局最优，模型假设存储与能源无限|
|[107]|Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling|MDPI提供的正式全文文本；28页正式页眉；含混入的预审水印提取，非逐字一致性证明|模型状态预测→规则调整策略权重→插入与约束检查；不写为神经预测；单颗敏捷观测卫星的观测与传输；三类资源情景，不是在轨遥测闭环；三个启发式与一个元启发式对照；不把定性比较扩展为实测在轨收益|正式提供正文文本，规则符号和水印混排待原PDF核|

## 三、B类：4篇公开作者稿定向核读

四篇均需正式版逐命题对照；**已关闭0/4**。书目或DOI与正式文章一致，不等于作者稿模型和结果必然相同。

|编号|文献题名|版本或当前可见证据|实际核查的命题/范围|边界或待核项|
|---|---|---|---|---|
|[53]|Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing|arXiv:2604.05937v1；25页；2026-04-07作者稿|处理器集合含边缘卫星和地面站；采集先确定，下游负载与频率优化；固定分发—处理—汇集流程与稳定ISL；不写成自由路由或已验证反向采集反馈|先采集后星地处理；Wiley正式版仍未逐命题对照|
|[74]|Joint Beam Scheduling and Power Optimization for Beam Hopping LEO Satellite Systems|arXiv:2312.01292v1；14页；2023-12-03作者稿|平均功率选束，再固定选择以罚函数内点法优化连续功率；单星8波束61位置；G-BH/G-BHPO相同贪心规则不等于整个照射序列严格相同|作者稿8束61位置；正式版与页码冲突均未关闭|
|[76]|Demand-Aware Beam Hopping and Power Allocation for Load Balancing in Digital Twin Empowered LEO Satellite Networks|arXiv:2411.08896v1；13页；提交史实际标为2024-10-29|12星×4波束、168小区；需求、队列、关联与功率条件；FPA/DPA为整体配置比较，8–20 Gbit/s相近、高负载DPA较高；非纯功率消融|FPA/DPA整体策略，不是纯功率因果消融；IEEE正式版待核|
|[121]|On-Demand Routing in LEO Mega-Constellations With Dynamic Laser Inter-Satellite Links|arXiv:2406.01953v1；17页；2024-06-04；PDF第10–12页已看像素|1584星、600个1秒时隙；无排队延迟；模型规模与参数；低建链代价下ILPR/ALPR略差于ILSR；ISASR在1 ms仍优于ILSR；计算时间与路径变化存在取舍；模型假设控制提前计算/分发，非已证明星载时限|作者稿有PDF局部像素检查，IEEE正式版未核；不等于星载在线期限|

## 四、C类：7篇历史一手原文精读记录

这些曾按方法、实验、限制开展定向阅读，不应因为未出现在15篇通信核心核验名单中而漏掉。凡缺精确原文页节的项目，先恢复真实阅读版本和图表定位。

|编号|文献题名|版本或当前可见证据|实际核查的命题/范围|边界或待核项|
|---|---|---|---|---|
|[18]|Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|多级库存/备星与响应；实际版本和页节仍需补|按原稿证据范围使用，未作本轮整篇内容核验|
|[35]|Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|200/108卫星与24 h；请求密度决定难度；各代理知道公共请求和星座构型但不具有其他代理详细能力；GND使复杂性依赖子问题；大算例NSS-GND比BD降低最慢代理算时/消息量，但任务满足率仍有差距；Java仿真算时的报告口径|按原稿证据范围使用，未作本轮整篇内容核验|
|[66]|A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|单星Basilisk环境；45/90指决策间隔；收益/稳定性随问题变化；MCTS-Train训练及模拟回溯成本高；wall clock报告训练总episodes与固定10000episodes两种口径；资源屏蔽限定模拟资源状态|按原稿证据范围使用，未作本轮整篇内容核验|
|[71]|Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|LEO低推力/漂移服务路径；精确图表位置待补|按原稿证据范围使用，未作本轮整篇内容核验|
|[101]|Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|异常检测评价指标、基线和后处理；精确页节待补|按原稿证据范围使用，未作本轮整篇内容核验|
|[102]|Knowledge-based satellite failure detection, isolation and recovery (FDIR)|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|基于CLIPS的规则FDIR与地面原型；星载硬件未证明|按原稿证据范围使用，未作本轮整篇内容核验|
|[119]|A model-driven framework for supervised reconfiguration of satellite schedulers|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|卫星调度器受监督重配置；软件验证不代表全星座业务收益|按原稿证据范围使用，未作本轮整篇内容核验|

## 五、D类：8篇指定章节或局部正文核读

其中[34][65]记录了具体方法与图表，但历史来源级别仍是“前轮提取”，本次保守保留为局部核读；[1]只核摘要/引言，[72]只核摘要与假设A.1，不将其扩大为方法与实验全面审阅。

|编号|文献题名|版本或当前可见证据|实际核查的命题/范围|边界或待核项|
|---|---|---|---|---|
|[1]|Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts|沿用前轮提取；待完整全文核查|常规星座运行、自动化与扩展性需求；不把2021年的工程状态叙述当作2026年现状|按原稿证据范围使用，未作本轮整篇内容核验|
|[3]|Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions|v1.6记录为原文局部已核，完整精读待完成|敏捷观测任务表示、运行约束、收益/多目标/自主变体；精确、启发式、元启发式、机器学习四种求解组织；未引用作者稿历史工程数量|按原稿证据范围使用，未作本轮整篇内容核验|
|[4]|Satellite Scheduling Problems: A survey of applications in Earth and outer space observation|沿用前轮提取；待完整全文核查|以应用/问题变体组织地球及外层空间成像、通信调度综述；正式卷期2025，DOI含2024不等于卷期年|按原稿证据范围使用，未作本轮整篇内容核验|
|[5]|Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges|沿用前轮提取；待完整全文核查|智能体类型、架构、通信、任务管理与应用分类；已经讨论健康状态和任务目标结合、能耗与通信代价；不将健康+任务本身当作本稿新颖性声明|按原稿证据范围使用，未作本轮整篇内容核验|
|[34]|Decentralized Observation Allocation for a Large-Scale Constellation|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|100代理/634目标批量案例；从头和增量持续规划；增量在该实验中更快但更多重复观测；试验是单线程分布式执行模拟；请求满足与竞争消息的效果还依赖更新/奖励策略|按原稿证据范围使用，未作本轮整篇内容核验|
|[65]|Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|四种通信设置：无通信、单跳LOS、多跳LOS、自由通信；星间只共享已经成像/下传状态，不共享计划意图；因而自由通信也保留同一决策间隔的重复观测；LOS效果依赖构型连通性；单星训练后跨星复用；MIP可用于目标预分配|仅共享已完成状态不含未来计划意图，作者稿与正式版本待核|
|[72]|Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|旧记录仅保留精读标记或局部来源信息|按原稿证据范围使用，未作本轮整篇内容核验|
|[98]|Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding|完整历史核读状态保留于冻结父记录；本轮未重新核定，不能视为未曾读过或已全文核验|arXiv方法局部核读；尚未完整实验对照|按原稿证据范围使用，未作本轮整篇内容核验|

## 六、E类：5篇尚无可读全文的核心来源

缺全文不代表原论文有错；主稿只能保留摘要直接支持的方向性论断。没有读到具体实验段落，就不要凭猜测填数据、百分比、变量或性能排名。

|编号|文献题名|版本或当前可见证据|实际核查的命题/范围|边界或待核项|
|---|---|---|---|---|
|[75]|NGSO Satellites Beam Hopping Strategy Based on Load Balancing and Interference Avoidance for Coexistence With GSO Systems|出版身份与公开摘要；全文未取得|旧记录仅保留精读标记或局部来源信息|未获正文，具体关联、干扰和基线未知|
|[77]|Routing cost-integrated intelligent handover strategy for multi-layer LEO mega-constellation networks|SCIopen/出版方摘要及元数据；全文未取得|旧记录仅保留精读标记或局部来源信息|仅摘要，单层学习与跨层抖动成本细节待核|
|[79]|Scalable routing in low-Earth orbit satellite constellations: Architecture and algorithms|出版方摘要与HKU条目；全文未取得|旧记录仅保留精读标记或局部来源信息|DBR/DAR方法及稳定收益的全文依据缺失|
|[80]|Segment routing for traffic engineering and effective recovery in low-earth orbit satellite constellations|出版方摘要；HKU条目无附件；全文未取得|旧记录仅保留精读标记或局部来源信息|分段流量工程不可写成物理容量分配已证|
|[112]|Reference architecture for autonomy and adaptivity in satellites|出版方摘要与作者/会议条目；全文未取得|旧记录仅保留精读标记或局部来源信息|MAPE-K完整接口、NIMBUS验证、性能未知|

## 七、未开展定向全文核实的其他81篇与工程资料

其余81篇学术来源目前只有继承记录，可能有早期摘要或部分提取，但本总账未见可授予定向精读等级的充分依据。来源身份和旧引文不删除，后续按正文论断重要程度逐项补齐。

单列的10项工程/标准资料为：[22] Iridium Adds to Constellation Resilience with Launch of Spare Satellites；[51] Tasking API；[52] Work with contacts；[88] Conjunction Data Message；[89] Starlink Collision Avoidance CONOPS；[97] Astroscale’s ADRAS-J Achieves Historic 15-Meter Approach to Space Debris；[111] IPEX；[113] Core Flight System – Demo Bundle；[114] What is Starling?；[115] NASA Starling and SpaceX Starlink Improve Space Traffic Coordination。工程资料说明接口、公开流程与飞行事件，不能被写成未公开的系统内部算法性能验证。

## 八、下一轮精修的使用规则

从121项CSV按编号找到具体来源 → 查看阅读等级、真实阅读版本、正文定位和限制 → 在v1.7中文/英文引用位置找原句 → 依照原文的任务场景、资源约束和基线修改句子与表格 → 同步摘要、结论并填写补核记录。**CSV中的表格块属于查找入口，不保证该表每行的全部数字均已逐项核查。**

特别保留：[53][74][76][121]正式版差异；[73][107]正式PDF校正；[74]出版页码冲突；竞争综述[7][8]仅公开摘要，不做“对方全文未覆盖”的断言。全稿121项仍需作者逐条终核，human_verified=false，submission_ready=false。旧148篇检索候选库和主稿121项引用是不同分母，不能混用。

此分支只添加阅读审计文件，不覆盖v1.6，也不声称v1.7已经推送至GitHub。