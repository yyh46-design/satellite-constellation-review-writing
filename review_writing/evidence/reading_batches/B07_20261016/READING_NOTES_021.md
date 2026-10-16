# [21] Spare strategy for large-scale satellite constellations under dual resupply channels using Markov chain

中文译名：双补给通道下基于马尔可夫链的大规模卫星星座备星策略。DOI：[10.1016/j.actaastro.2026.06.020](https://doi.org/10.1016/j.actaastro.2026.06.020)。

版本：author_preprint_arxiv_2605.20875v2_2026-06-21。实际首页arXiv:2605.20875v2，21 Jun 2026；57页。正式DOI沿用冻结编号；本轮Crossref请求429，正式出版元数据未独立刷新，不能据作者稿推正式出版分页。

[实际阅读入口](https://arxiv.org/pdf/2605.20875v2)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[16, 19, 23]的相关段落；实际图页相关区域[16, 19]。PDF SHA256 `a87cc30e1dbc9953f36823d44c85a38ae8d28d2fc62e9af16fdd56e04c1e004d`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-021-C01|Fig3; §3.2；物理页[16]|面内层IO/LT阶段以直接小运载器订货定义，间接通道作为周期输入；停车层阶段由间接大运载器定义。|两层同名阶段不代表同一时刻或相同业务含义。|
|B07-021-C02|Nsat_c bound below Fig3；物理页[16]|状态库存上界考虑间接补给后直接批次紧接到达的情形。|该建模上界不是每条轨道实际常驻星数，也不是优化得出的最小规模。|
|B07-021-C03|Fig4; Eq21 explanation；物理页[19]|RAAN对齐时，转移先应用间接补充，再按直接策略条件过滤。|同一步多事件的处理顺序是模型的一部分；不能在复现或比较中任意交换。|
|B07-021-C04|Eqs30–36；物理页[23]|完整状态包括订货间期和多个在途子阶段；通过边缘化与周期平均才得到库存分布。|推论：用平均库存直接充当在线控制状态会丢失阶段信息，是否足够需另证。|

服务综述：3.1.2/4.3：双通道在途状态及更新顺序。

仍缺：作者v2未配正式版；矩阵、马尔可夫性/独立性条件和代码未完整审核。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
