# [25] Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers

中文译名：考虑低推力转移的卫星星座服务轨道仓库选址优化。DOI：[10.2514/1.A36386](https://doi.org/10.2514/1.A36386)。

版本：author_preprint_arxiv_2502.15914v2_2025-08-25。实际首页arXiv:2502.15914v2，25 Aug 2025；24页作者稿；与JSR正式DOI尚未逐命题配对。

[实际阅读入口](https://arxiv.org/pdf/2502.15914)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[12, 13, 14]的相关段落；实际图页相关区域[12, 14]。PDF SHA256 `ab590503c3a40246337670912368b358ac67a4228f2e84b2e15ff24d60f864d8`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-025-C01|Eq34; fixed-routing NLP；物理页[12]|固定客户顺序时，仓库位置变化只改变首段和返库段，内部客户间转移项保持常量。|该简化依赖已固定路由和文中转移模型，不能推广到全部时变/相位耦合转移。|
|B07-025-C02|Eq35–38；物理页[12]|连续位置子问题对固定路由的推进剂乘部署到LEO等效质量因子进行优化；在这一子问题中不同仓库的导数解耦。|等效发射质量与裸delta-v、货币成本不等价；局部导数解耦不代表总选址路由独立。|
|B07-025-C03|Eqs39–53; L-BFGS-B paragraph；物理页[13, 14]|解析一阶导数输入L-BFGS-B，作者用以避免数值差分、减少函数评价。|只核到算法说明和实际公式页，未完成全符号证明、梯度单测或全局最优核验。|
|B07-025-C04|Algorithm1 lead-in; warm-start；物理页[14]|路由MILP复用上一迭代解作warm start，理由是仓库小幅移动时路由常保持不变。|热启动提供候选解，不能据经验直接跳过路由重求或将旧路由视作仍最优的证书。|

服务综述：3.1.3/4.1：连续选址与路由交替求解的有效范围。

仍缺：解析梯度未独立推导/有限差分对验，退化几何与全局收敛、正式配对未核完。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
