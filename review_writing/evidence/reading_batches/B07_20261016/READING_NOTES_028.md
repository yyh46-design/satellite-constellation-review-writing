# [28] On-Orbit Servicing Optimization Framework with High- and Low-Thrust Propulsion Tradeoff

中文译名：考虑高低推力推进权衡的在轨服务优化框架。DOI：[10.2514/1.A35094](https://doi.org/10.2514/1.A35094)。

版本：author_manuscript_requested_arxiv_v1。读取请求地址2103.08963v1的45页作者稿；题名/作者匹配。首页无直接版本印记，不能仅凭索引acceptedVersion标签认定是接受稿或正式版。

[实际阅读入口](https://arxiv.org/pdf/2103.08963v1)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[17, 18, 32, 33]的相关段落；实际图页相关区域[18, 32, 33]。PDF SHA256 `0e2dba0414bbdf57cfa04bf5d8c408c61b0a0ad23150706bb382020df681ebbb`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-028-C01|Eqs7–10; commodity balance；物理页[17, 18]|客户节点按服务船分别守恒以禁止相互交换物资，停车节点跨船汇总以允许经仓库交换。|守恒约束同时编码交接权限；不能仅保留总量而删去载具身份约束。|
|B07-028-C02|Fig7; short-term example；物理页[32]|客户库共142星，当前时域只有19星显示需求并进入优化网络。|候选压缩改变实际组合规模，不能把全部142客户同时求解当作本例计时口径。|
|B07-028-C03|solver/hardware paragraph；物理页[32]|Gurobi9在i7-9700平台约45秒终止，采用1%gap停止条件。|是特定入模网络的近最优停止记录，不是严格零gap全局证书或完整星上决策预算。|
|B07-028-C04|Fig7; Figs8–9; 90-day profit paragraph；物理页[32, 33]|第32页称5客户被访问，第33页收入按4项服务列示，并说明未来随机需求会触发重规划、改变90天利润。|访问与服务的数量含义尚未完整对齐，图示显示初始位置线索但不自动关闭；不计算服务完成率或当作已实现最终利润。|

服务综述：3.1.3/4.1–4.3：物资交接权限、真实入模规模与结果分母。

仍缺：作者稿与正式版未配；5访问/4服务口径、全部质量/推进约束和完整重规划过程未独立复现。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
