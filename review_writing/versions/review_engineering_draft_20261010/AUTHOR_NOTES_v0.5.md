# 第2至4章审阅稿v0.5修订说明

本版落实对v0.4的结构与综合评价意见，供作者连续阅读和讨论。五章框架继续沿用，本文件及正文只处理第2至4章；第1章、摘要和第5章尚未在本轮撰写。本轮仅在本地生成新版本。

## 阅读入口与修改范围

- 正文：REVIEW_CHAPTERS_02_04_v0.5.md。
- 代表研究证据记录：COMPARISON_EVIDENCE_v0.5.json。
- 前版正文和AUTHOR_NOTES_v0.4.md保留，可对照阅读。
- 编辑基线为本地v0.4，不将旧版远端v0.3视为本轮编辑后的内容。

| 位置 | 本次修改 | 目的 |
| --- | --- | --- |
| 第2章 | 收紧为决策对象、信息组织、状态/资源/目标及反馈接口；移去重复的具体方法与实验介绍 | 建立概念基础，避免提前复述第3章 |
| 3.2开头 | 明确求解方法、信息组织、资源耦合与计划更新为交叉维度 | 避免把不同分类轴当作互斥算法类别 |
| 3.2结尾 | 增加14篇代表文献的逐行对照表（表1）及短综合 | 将实际论文的模型、信息、决策和验证对象放在相同字段中 |
| 3.4 | 压缩配置—任务与管理拓扑的重复方法介绍 | 把论述集中到输入、输出和责任接口 |
| 4.1 | 从表1归纳扩展性改进的成本位置；原通用维度表改为表2 | 从如何评价转向现有代表研究显示了什么 |
| 4.2 | 比较完成事件、资源承诺、恢复过程和物理可行性 | 解释资源耦合如何改变任务选择，而非重复算法介绍 |
| 4.3 | 综合信息交换的独立代价、学习方法的职责和感知到恢复的依赖 | 保留具体证据支持的选择条件 |
| 4.4 | 工程表改为连接环节、实际动作和范围（表3），增加跨案例归纳 | 区分业务接口、公开流程、软件测试及限定飞行能力 |
| 4.5 | 将展望连接到前述比较的四类问题 | 形成由证据推出研究问题的结尾 |

第3.1和第3.3的主体文字保持前版内容，避免本轮扩大技术改写范围。第2章不再详细罗列这些方法，但已有47条唯一DOI全部在新稿保留。

## 代表研究英文原标题、中文译名与DOI

中文题名是工作译名，英文采用当前文献库与正文中的正式题名。表1按研究逐行整理，未给出跨论文统一数值评分，也未将不同实验平台的结果汇总为算法排名。

| 英文原标题 | 中文工作译名 | DOI |
| --- | --- | --- |
| A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites | 纳卫星星座能源感知任务调度的分支定价算法 | [10.1016/j.cor.2025.107259](https://doi.org/10.1016/j.cor.2025.107259) |
| Lagrangian hierarchical mixed-integer programming for ultra-large-scale satellite scheduling under dynamic task delivery | 动态任务到达下超大规模卫星调度的拉格朗日分层混合整数规划 | [10.1016/j.asr.2025.12.008](https://doi.org/10.1016/j.asr.2025.12.008) |
| Decentralized Observation Allocation for a Large-Scale Constellation | 大规模星座的去中心化观测分配 | [10.2514/1.I011215](https://doi.org/10.2514/1.I011215) |
| Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation | 大规模卫星星座基于分解的去中心化观测调度 | [10.1613/jair.1.16997](https://doi.org/10.1613/jair.1.16997) |
| Joint Observation and Transmission Scheduling in Agile Satellite Networks | 敏捷卫星网络的观测与传输联合调度 | [10.1109/TMC.2021.3076088](https://doi.org/10.1109/TMC.2021.3076088) |
| Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm | 采用改进蚁群算法的多颗敏捷卫星能源约束观测与传输联合调度 | [10.1016/j.actaastro.2025.02.008](https://doi.org/10.1016/j.actaastro.2025.02.008) |
| Edge Intelligence for Satellite-Based Earth Observation: Scheduling Image Acquisition and Processing | 卫星对地观测边缘智能：图像采集与处理调度 | [10.1002/sat.70082](https://doi.org/10.1002/sat.70082) |
| Online scheduling of distributed Earth observation satellite system under rigid communication constraints | 严格通信约束下分布式对地观测卫星系统的在线调度 | [10.1016/j.asr.2020.02.018](https://doi.org/10.1016/j.asr.2020.02.018) |
| Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites | 深度强化学习辅助大邻域搜索：对地观测卫星大规模应急任务在线调度 | [10.1016/j.eswa.2025.128502](https://doi.org/10.1016/j.eswa.2025.128502) |
| Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations | 面向可扩展对地观测卫星星座运行的单智能体强化学习 | [10.2514/1.A35736](https://doi.org/10.2514/1.A35736) |
| A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling | 对地观测卫星调度强化学习算法的比较分析 | [10.3389/frspt.2023.1263489](https://doi.org/10.3389/frspt.2023.1263489) |
| Multi-orbit routing and scheduling of refuellable on-orbit servicing space robots | 可加注在轨服务空间机器人的多轨道路径与调度 | [10.1016/j.cie.2022.108852](https://doi.org/10.1016/j.cie.2022.108852) |
| On-orbit refueling robust mission scheduling with uncertain duration for geosynchronous orbit spacecraft | 考虑时长不确定性的地球同步轨道航天器在轨加注鲁棒任务调度 | [10.1016/j.cja.2025.103774](https://doi.org/10.1016/j.cja.2025.103774) |
| Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit | 低地球轨道多客户服务任务的低推力推进与漂移轨道优化 | [10.1007/s40295-026-00580-4](https://doi.org/10.1007/s40295-026-00580-4) |

## 证据处理与人工核查状态

14篇代表研究沿用原有原文定向核查、作者稿或正式摘要支撑。本轮重新查阅了分支定价、拉格朗日分层、能源联合调度、通信约束在线调度及学习辅助大邻域搜索的公开原文摘要、引言或方法片段，并重定位其他来源。逐篇范围保存在COMPARISON_EVIDENCE_v0.5.json中。检索结果只用于发现来源，不作为完整技术细节的验收。本轮未将摘要核查升级为全文核查，也未将助手定向检查标为作者人工通过。

表1使用已有支持的定性模型/方法信息及既有明确规模；没有加入新收益百分比、运行时间、最优性保证或飞行验证宣称。论文原有精确结果（例如第3.1的维护成本上限）保留既有待作者核查状态，不因本轮结构修改而获得新的事实认证。

工程来源及查阅记录承接AUTHOR_NOTES_v0.4.md。本轮只调整其分析角色，继续遵守以下范围：

- Planet复采规则限定于文档相应的灵活任务产品。
- AWS取消重约的说明对应已有预约的任务配置更新，不泛化为所有预约修改。
- ADRAS-J接近事件发生于2024年11月30日、报道发表于12月11日；安全后撤不写成捕获或移除完成。
- IPEX是单星规划运行证据，Starling分布式观测是四星限定任务。
- Starling 1.5为模拟接近测试中实际执行机动；不写成避免了真实碰撞。
- 公开API、运营流程与飞行演示分别支撑不同结论，不推断未披露的商业排程算法。

第4章新增的主要判断属于作者综合：不同扩展机制改变不同成本、资源耦合改变完成事件、信息成本改变协调选择、工程案例呈现互补的局部接口。其归纳对象限定为正文所讨论的代表研究，不声称已对148篇候选池完成逐篇编码或统计，也不以这些案例宣称全领域缺少某种系统。

## 五项文字检查

| 检查项 | 已做处理 | 仍需作者判断 |
| --- | --- | --- |
| 冗余 | 第2章移去重复的代表方法；3.4压缩重复；4章改写为跨研究结论 | 是否还需进一步压缩个别长段 |
| 动词与责任 | 区分论文建模、运营方公开、飞行任务实际执行和本文综合 | 最终英文表达与时态 |
| 段落与结构 | 开头明确比较结论，再用代表研究及案例解释；表号连续为1—3 | 完整引言和结论接入后的节奏 |
| 术语 | 保持能力配置、运行调度、执行与恢复、资源承诺与任务完成事件 | 与最终题名和英文关键词统一 |
| 数字与引用 | 核对47条唯一DOI保留、14表格条目对应正文、规模单位和案例范围 | 全文逐条人工核查与正式参考文献排版 |

## 本轮没有完成的工作

完整引言、摘要、结论、148篇全量系统筛选/编码、全部论文逐页人工核查和投稿格式整理不在本轮修改范围。正文仍是审阅稿，不标记为可提交版本。GitHub没有在本轮写入或推送。
