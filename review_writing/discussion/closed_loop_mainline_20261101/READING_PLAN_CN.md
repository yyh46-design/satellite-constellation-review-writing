# 补读与证据使用计划

## 本轮补回的已有来源

|文献|v10编号|本轮编号|阅读依据|采用内容|
|---|---|---|---|---|
|Morgan等2014，10.2514/1.G000218|108|64|B05 READING_NOTES_092.md；C01—C04|凸化、信赖域、时间离散及控制约束|
|Gavilan等2012，10.1016/j.conengprac.2011.09.006|109|62|B06 READING_NOTES_093.md；C01—C03；本轮重开作者PDF相关正文|模型残差更新扰动统计，机会约束裕量|
|Valicka等2019，10.1016/j.ejor.2018.11.043|71|78|v10 3.5.2；B05 READING_NOTES_062.md及继承B04记录|信息揭示后的改排；GEO测试边界|
|Wang等2020，10.1109/TAES.2019.2947978|42|77|v10 3.5.2；B05 READING_NOTES_061.md及继承B04记录|事前收益保护与信息后改排的区分|

这些是已有定向正文阅读的复用，不新增“四篇全文精读完成”的计数。全部证明、独立实验、作者终核与未完成的正式版配对继续保留原状态。本轮Gavilan为相关段落回查；Morgan与Valicka公开PDF工具访问失败，采用仓库中可追溯阅读记录，不宣称本轮重新读过其原文。

## 新候选：尚未纳入正文

1. 优先：Yuan H, Li D, He G, Wang J. Uncertainty-resilient constrained rendezvous trajectory optimization via stochastic feedback control and unscented transformation. Acta Astronautica, 2024, 219:264–277. [期刊入口](https://doi.org/10.1016/j.actaastro.2024.03.017)。需精读误差来源、反馈与名义轨迹共同设计、约束和比较基线。
2. 优先：Kim GR, Eddy D, Kochenderfer MJ. Chance-Constrained Belief-Space Maneuver Planning for Autonomous Collision Avoidance Under Uncertainty. AMOS 2026 / [arXiv:2609.13428v1](https://arxiv.org/abs/2609.13428v1)。需精读信念更新、未来测量、等待与机动选择及风险定义。
3. 基础补充：Hartley EN, Trodden PA, Richards AG, Maciejowski JM. Model predictive control system design and implementation for spacecraft rendezvous. Control Engineering Practice, 2012, 20(7):695–713. [机构记录](https://eprints.whiterose.ac.uk/id/eprint/90483/)。需确认分阶段控制、模式切换及闭环验证能否提供现有文献未覆盖的机制。
4. 条件选读：Sportelli等. AI-Augmented Model Predictive Control for Safe and Adaptive Rendezvous and Proximity Operations. [arXiv:2607.16630v1](https://arxiv.org/abs/2607.16630v1)。重点查参数调节层是否增加独立机制认识；对抗性交会场景与星座任务区别须保留。

以上只完成候选发现和摘要/元数据级检查，不进入当前93项引用，不填充数值结果。

## 后续精读问题

每篇记录状态与信息、不确定性来源、可修改变量、触发时机、反馈方式、约束处理、比较基线、响应时间和任务结果。现有[76]—[81]是基线编号，先沿候选生成—修正—执行链深入比较；新编号见CITATION_MAP.json。

尚待补足：控制纠偏何时升级为任务重排；信息质量如何改变干预时机；闭环修正对实际任务完成和长期资源的作用。He 2023多子系统推理调度的旧阅读版本未明确，列待核，不因旧版已引用便自动采用。
