# [27] Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties

中文译名：需求不确定条件下在轨服务运行建模与优化框架。DOI：[10.2514/1.A34978](https://doi.org/10.2514/1.A34978)。

版本：author_manuscript_requested_arxiv_v1。读取请求地址2103.08962v1的46页作者稿；实际题名/作者与目标一致。首页未见可直接确认的arXiv版本印记，PDF内置题名/作者保留AIAA模板字段，不能据此改书目或判定正式版。

[实际阅读入口](https://arxiv.org/pdf/2103.08962v1)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[21, 22, 39]的相关段落；实际图页复核[21, 22]的相关区域。PDF SHA256 `2a8482625618b2cf4471a32505d346fb77f6d32951fc99a56f58990bf485f19a`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-027-C01|Eq14–20, objective costs；物理页[21]|利润包含服务收入及采购制造、发射、延迟罚金、仓库和服务星运行成本。|不能把目标值只称燃料最优，或忽略被计入的服务延迟代价。|
|B06-027-C02|RH planning/control horizons；物理页[22]|PH只执行其首个CH，然后传递系统状态再滚动，传统形式假设PH内预测准确。|分段最优解不自动拼成整个随机长时域的全局最优。|
|B06-027-C03|modified event-triggered RH；物理页[22]|随机服务需求出现时重规划，长期无随机需求也可定期规划；预测由已触发需求和确定性需求组成。|不是预知所有未来随机故障，也不是所有滚动模型都持续在线重训练。|
|B06-027-C04|architecture-comparison scope；物理页[39]|作者明确案例旨在展示复杂基础设施建模分析能力，而非给市场条件下最佳架构的定论。|不能将模型演示扩大成实际商业优势或普遍架构排名。|

服务综述：3.2.4及4.3：滚动时域的触发、预测和成本包含项。

仍缺：46页作者稿未配终刊；跨阶段在途承诺完整约束和全部轨迹/库存推导仍未审完，市场结论只到案例范围。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
