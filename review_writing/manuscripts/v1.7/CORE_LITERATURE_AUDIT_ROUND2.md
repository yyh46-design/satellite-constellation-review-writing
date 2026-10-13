# 核心文献核验第二批：v1.6→v1.7（2026-10-13）

> **核验口径**：优先检查指定11项，其中6篇原来无全文、4篇作者稿/正式版需比对、[73]需要正式PDF像素复核。**本轮未获得可以逐式核验的6篇正式全文，也未完成4篇正式版正文对照**。发现的正式摘要与出版社、作者机构书目用于收窄正文，不能冒充全文。若最终有人工作者读到付费全文，应在后续版本升级其状态。

## 逐篇结论（用于正文修订）

| 编号 | 本轮实得版本 | 核验状态 | 已确认/适用条件 | 未关闭的证据与正文处置 |
|---|---|---|---|---|
| [75](https://doi.org/10.1109/LCOMM.2022.3213912) | publisher_abstract_only | **not_verified** | 摘要确认卫星—小区分配与多星照射模式为两个子问题，优化包括负载平衡与GSO地面站干扰；联合照射以共信道干扰准则迭代求解 | **待核**：两阶段内变量、GSO/成员间干扰约束的完整公式，具体基线、规模和性能分母。**处置**：3.3及4.2的概括保留为摘要支持的两层任务，明确‘GSO共存与共信道干扰’，不写具体成员间干扰公式或独立消融 |
| [77](https://doi.org/10.1016/j.cja.2024.09.039) | publisher_open_access_abstract_only | **not_verified** | 解析端到端传播时延参与决策；单层采用Dueling Double DQN；跨层采用抖动预测和切换开销权衡；作者公布组合方案的场景内改进 | **待核**：状态动作奖励、各时延项、跨层决策变量、是否存在独立模块消融、每个对照条件。**处置**：维持整体策略设计描述，不将组合方案改善归因于D3QN/预测单模块；表5和4.2同步标明仿真基线限制 |
| [79](https://doi.org/10.1016/j.comcom.2022.02.015) | publisher_and_institutional_abstract_only | **not_verified** | 两层结构针对无直接ISL的地面辅助拓扑；DBR按流提供有界时延但表项较多；DAR按目的地进一步减少变更而不提供同样时延界 | **待核**：DBR/DAR更新触发规则、具体时延上界、控制报文/表项与测试条件。**处置**：改为‘针对降低路径变化设计稳定路由’，不把降低控制开销的目标称为已在正文验证的量化效果 |
| [80](https://doi.org/10.1016/j.dcan.2022.09.022) | institutional_abstract_and_open_access_record | **not_verified** | DBTS/DBTS+属于流量分流；LFA/LFA+属于预先备份的快速重路由；研究场景为地面站辅助的时变LEO网络 | **待核**：完整约束、哪些容量只作为给定参数、仿真统计分母、故障/重路由时序及表图。**处置**：保留‘流量工程与故障恢复’；不使用‘物理链路容量分配’；4.2以路径/流量竞争而非‘容量优化’表述 |
| [107](https://doi.org/10.3390/rs15061577) | publisher_abstract_and_public_fulltext_excerpt | **supported_with_limit** | 研究对象是单颗敏捷对地观测卫星；建模电能与下传子系统耦合，状态变量预测反映子系统约束，规则推理在几种规划策略间切换，模拟比较三种启发式和一种元启发式 | **待核**：全部状态预测方程、精确策略规则/事件顺序及各仿真表图；非实飞遥测反馈。**处置**：3.5和表7明确‘单星多子系统状态计算/规则策略选择，模拟’；不写神经预测和在轨部署 |
| [112](https://doi.org/10.1016/j.jss.2026.112802) | publisher_abstract_and_highlights_only | **not_verified** | 基于系统性文献与工业专家验证，五个MAPE-K职责组件并区分应用/运行层，在NIMBUS平台实例化 | **待核**：完整模块间连接语义、专家验证过程、实际嵌入软件程度、性能和飞行证据。**处置**：将论文称为‘参考架构提出与NIMBUS实例化’，不说‘已在轨验证’或‘已提升调度性能’；表7标为架构/工业专家评价 |
| [53](https://doi.org/10.1002/sat.70082) | author_version_only_plus_formal_abstract | **supported_with_limit** | Wiley正式摘要确认‘两个耦合优化问题’，分别为采集与处理；作者稿明确上游采集确定下游输入，星地处理器、任务分配/频率/通信能耗和稳定ISL等约束 | **待核**：Wiley正式全文公式/图表/结果逐点一致性、GPU功率字段差异。**处置**：继续使用‘分阶段安排/两个耦合问题’；不写端到端同一全局联合求解与正式版全文相同 |
| [74](https://doi.org/10.23919/JCC.ja.2022-0864) | author_version_only_plus_official_metadata | **supported_with_limit** | 作者稿支持8波束/61位置、选束博弈与固定选择后的连续功率优化；IEEE正式元数据公开显示2024,21(10):1–14 | **待核**：期刊排版PDF页首和作者稿参数/图表一一对应；另一二手资料226–239页冲突。**处置**：文末暂保留IEEE一手记录的1–14页，并在书目审计单独保留226–239冲突；不以二手记录直接覆盖 |
| [76](https://doi.org/10.1109/TWC.2025.3545745) | author_version_only_plus_bibliography_metadata | **supported_with_limit** | 12星各4波束、168小区的作者稿模型；FPA需求选束/均分功率，DPA数孪内联合照射/离散功率，8–20 Gbit/s与更高负载趋势要连同策略差异解释 | **待核**：正式出版正文约束、基线定义和图8是否逐项一致；作者稿中的FPA自比较笔误。**处置**：保留整体策略比较，明确不能当作仅改变功率模块的严格消融；不采未经核的摘要百分比 |
| [121](https://doi.org/10.1109/TAES.2024.3415571) | author_version_only_plus_formal_bibliography | **supported_with_limit** | 作者稿模拟1584星、600个1秒快照；ISASR在低建立代价下仍优于瞬时最短路；部分保持策略并非一直占优；时延/改路/断联风险受建链代价限制 | **待核**：IEEE正式图表/模型与作者稿全文对应；预计算与分发时延/拥塞等模型省略。**处置**：保留‘建链代价依赖’与复杂度条件，不以作者稿离线耗时宣称在线已满足时限 |
| [73](https://doi.org/10.3390/aerospace11030191) | publisher_provided_text_no_formal_pdf_visual | **supported_with_limit** | 使用ON/OFF模拟自相似流量估计预测误差；将路由及服务收益列为未来工作 | **待核**：MDPI正式PDF像素级校验式(24)–(25)、图8/13/14和表8。**处置**：预测精度写为模型在合成流量上的结果，不能扩展为已验证业务吞吐提升 |

## 访问与身份说明

### [75] 多卫星波束跳变与GSO共存

- 出版方或作者入口：https://ieeexplore.ieee.org/document/9916289/
- 实际核读级别：`publisher_abstract_only`；可读正文：false。版本核对：publisher article identity confirmed; full body inaccessible
- 源定位：IEEE正式摘要；2023,27(1):278–282
- 已能支持：摘要确认卫星—小区分配与多星照射模式为两个子问题，优化包括负载平衡与GSO地面站干扰；联合照射以共信道干扰准则迭代求解
- 本轮未能确认：两阶段内变量、GSO/成员间干扰约束的完整公式，具体基线、规模和性能分母
- v1.7处置：3.3及4.2的概括保留为摘要支持的两层任务，明确‘GSO共存与共信道干扰’，不写具体成员间干扰公式或独立消融

### [77] 路由代价感知的单层/跨层切换

- 出版方或作者入口：https://www.sciopen.com/article/10.1016/j.cja.2024.09.039
- 实际核读级别：`publisher_open_access_abstract_only`；可读正文：false。版本核对：publisher full-length OA designation does not mean full body read; rendered PDF not obtained
- 源定位：CJA/SciOpen开放文章摘要；2025,38(6),103263
- 已能支持：解析端到端传播时延参与决策；单层采用Dueling Double DQN；跨层采用抖动预测和切换开销权衡；作者公布组合方案的场景内改进
- 本轮未能确认：状态动作奖励、各时延项、跨层决策变量、是否存在独立模块消融、每个对照条件
- v1.7处置：维持整体策略设计描述，不将组合方案改善归因于D3QN/预测单模块；表5和4.2同步标明仿真基线限制

### [79] 地面辅助的两层稳定路由DBR/DAR

- 出版方或作者入口：https://hub.hku.hk/handle/10722/339786
- 实际核读级别：`publisher_and_institutional_abstract_only`；可读正文：false。版本核对：publisher requires institutional access or purchase; institution has no deposited file
- 源定位：HKU Scholar Hub作者机构书目与摘要；Computer Communications 188:26–38
- 已能支持：两层结构针对无直接ISL的地面辅助拓扑；DBR按流提供有界时延但表项较多；DAR按目的地进一步减少变更而不提供同样时延界
- 本轮未能确认：DBR/DAR更新触发规则、具体时延上界、控制报文/表项与测试条件
- v1.7处置：改为‘针对降低路径变化设计稳定路由’，不把降低控制开销的目标称为已在正文验证的量化效果

### [80] 分段路由/流量分流与快速恢复

- 出版方或作者入口：https://hub.hku.hk/handle/10722/339783
- 实际核读级别：`institutional_abstract_and_open_access_record`；可读正文：false。版本核对：open access label but full body inaccessible via current tool; no bypass attempted
- 源定位：HKU机构存档摘要；Digital Communications and Networks 10(3):706–715；正文ScienceDirect返回403
- 已能支持：DBTS/DBTS+属于流量分流；LFA/LFA+属于预先备份的快速重路由；研究场景为地面站辅助的时变LEO网络
- 本轮未能确认：完整约束、哪些容量只作为给定参数、仿真统计分母、故障/重路由时序及表图
- v1.7处置：保留‘流量工程与故障恢复’；不使用‘物理链路容量分配’；4.2以路径/流量竞争而非‘容量优化’表述

### [107] 单星多子系统状态推理式调度

- 出版方或作者入口：https://www.mdpi.com/2072-4292/15/6/1577
- 实际核读级别：`publisher_abstract_and_public_fulltext_excerpt`；可读正文：partial。版本核对：formal open article indexed; document body response rate-limited; no claim of full formal audit
- 源定位：Remote Sensing 15(6):1577，正式摘要；公开论文正文引言及PDF转写摘录
- 已能支持：研究对象是单颗敏捷对地观测卫星；建模电能与下传子系统耦合，状态变量预测反映子系统约束，规则推理在几种规划策略间切换，模拟比较三种启发式和一种元启发式
- 本轮未能确认：全部状态预测方程、精确策略规则/事件顺序及各仿真表图；非实飞遥测反馈
- v1.7处置：3.5和表7明确‘单星多子系统状态计算/规则策略选择，模拟’；不写神经预测和在轨部署

### [112] MAPE-K自主参考架构与NIMBUS实例化

- 出版方或作者入口：https://www.sciencedirect.com/science/article/pii/S0164121226000361
- 实际核读级别：`publisher_abstract_and_highlights_only`；可读正文：false。版本核对：publisher full text returned 403; no openly downloadable author manuscript verified
- 源定位：JSS 236:112802，正式摘要与Highlights
- 已能支持：基于系统性文献与工业专家验证，五个MAPE-K职责组件并区分应用/运行层，在NIMBUS平台实例化
- 本轮未能确认：完整模块间连接语义、专家验证过程、实际嵌入软件程度、性能和飞行证据
- v1.7处置：将论文称为‘参考架构提出与NIMBUS实例化’，不说‘已在轨验证’或‘已提升调度性能’；表7标为架构/工业专家评价

### [53] 观测—处理顺序输入/正式版对照

- 出版方或作者入口：https://onlinelibrary.wiley.com/doi/10.1002/sat.70082；作者稿：https://arxiv.org/pdf/2604.05937v1
- 实际核读级别：`author_version_only_plus_formal_abstract`；可读正文：author_pdf_25_pages。版本核对：official Wiley full abstract supports high-level architecture; article full-text not retrieved
- 源定位：arXiv v1 pp.10–15 §3.3–4.2 Eq.(18),(22), pp.18–22 Fig.8–12；Wiley Early View摘要
- 已能支持：Wiley正式摘要确认‘两个耦合优化问题’，分别为采集与处理；作者稿明确上游采集确定下游输入，星地处理器、任务分配/频率/通信能耗和稳定ISL等约束
- 本轮未能确认：Wiley正式全文公式/图表/结果逐点一致性、GPU功率字段差异
- v1.7处置：继续使用‘分阶段安排/两个耦合问题’；不写端到端同一全局联合求解与正式版全文相同

### [74] 单星波束调度和印刷页码

- 出版方或作者入口：https://ieeexplore.ieee.org/document/10495871/；作者稿：https://arxiv.org/pdf/2312.01292v1
- 实际核读级别：`author_version_only_plus_official_metadata`；可读正文：author_pdf_14_pages。版本核对：official printed pagination first-page visually unverified
- 源定位：arXiv v1 §II-B Eq.(7)–(8), §III Algorithm 1–2, Table 2, Fig.4；IEEE Xplore刊期21(10)和页码
- 已能支持：作者稿支持8波束/61位置、选束博弈与固定选择后的连续功率优化；IEEE正式元数据公开显示2024,21(10):1–14
- 本轮未能确认：期刊排版PDF页首和作者稿参数/图表一一对应；另一二手资料226–239页冲突
- v1.7处置：文末暂保留IEEE一手记录的1–14页，并在书目审计单独保留226–239冲突；不以二手记录直接覆盖

### [76] 12星波束/功率资源的正式版本

- 出版方或作者入口：https://doi.org/10.1109/TWC.2025.3545745；作者稿：https://arxiv.org/pdf/2411.08896v1
- 实际核读级别：`author_version_only_plus_bibliography_metadata`；可读正文：author_pdf_13_pages。版本核对：IEEE正式全文未取得，保留author_version_only
- 源定位：arXiv v1 §III–V、Table II、Fig.8；TWC 24(6):5084–5098
- 已能支持：12星各4波束、168小区的作者稿模型；FPA需求选束/均分功率，DPA数孪内联合照射/离散功率，8–20 Gbit/s与更高负载趋势要连同策略差异解释
- 本轮未能确认：正式出版正文约束、基线定义和图8是否逐项一致；作者稿中的FPA自比较笔误
- v1.7处置：保留整体策略比较，明确不能当作仅改变功率模块的严格消融；不采未经核的摘要百分比

### [121] 动态激光链路路由版本对照

- 出版方或作者入口：https://doi.org/10.1109/TAES.2024.3415571；作者稿：https://arxiv.org/pdf/2406.01953v1
- 实际核读级别：`author_version_only_plus_formal_bibliography`；可读正文：author_pdf_17_pages。版本核对：arXiv p.11 Fig.3 visual check; official text inaccessible
- 源定位：arXiv §III Eq.(6)–(10), §V Fig.3(视觉复核p.11), Table III, Fig.6；IEEE TAES 60(5):7089–7105
- 已能支持：作者稿模拟1584星、600个1秒快照；ISASR在低建立代价下仍优于瞬时最短路；部分保持策略并非一直占优；时延/改路/断联风险受建链代价限制
- 本轮未能确认：IEEE正式图表/模型与作者稿全文对应；预计算与分发时延/拥塞等模型省略
- v1.7处置：保留‘建链代价依赖’与复杂度条件，不以作者稿离线耗时宣称在线已满足时限

### [73] 正式版PDF版面与流量预测

- 出版方或作者入口：https://www.mdpi.com/2226-4310/11/3/191
- 实际核读级别：`publisher_provided_text_no_formal_pdf_visual`；可读正文：published_text_previously_checked。版本核对：official PDF failed via tool; watermark text not promoted to visual formal verification
- 源定位：§3.2, §4.3 Fig.8，§5.3.3 Fig.13–14/Table 8，§6
- 已能支持：使用ON/OFF模拟自相似流量估计预测误差；将路由及服务收益列为未来工作
- 本轮未能确认：MDPI正式PDF像素级校验式(24)–(25)、图8/13/14和表8
- v1.7处置：预测精度写为模型在合成流量上的结果，不能扩展为已验证业务吞吐提升

## 独立综合判断与限制

- ‘分阶段/耦合/局部’是分类与方法机制描述，不能由摘要自动提升为全域最优或部署证据。
- [75]、[79]、[80]、[112]等未取得正式正文，主要依赖出版方摘要或机构条目；[77]虽标开放获取，所见页面只返回摘要，未得可核读模型节。用户若提供合法的PDF，可据此继续关闭具体断言。
- [107]的正式期刊身份及公开正文摘录能确认单星多子系统状态与规则调度，细致变量、表图尚未全部验收。[53]、[74]、[76]、[121]仍以公开作者稿为具体模型依据。
- [73]正式出版页有全文入口但PDF下载/页面渲染失败；沿用此前出版文本证据与‘ON/OFF合成数据’边界。
- 所有11项的人工作者最终核查均为**pending**；未开展论文算法重跑；未关闭项会逐条保存在独立清单，不因为翻译成英文而改变证据等级。
