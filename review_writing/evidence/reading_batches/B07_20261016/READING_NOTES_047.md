# [47] Scheduling Space–Ground Communications for the Air Force Satellite Control Network

中文译名：空军卫星控制网络的天地通信调度。DOI：[10.1023/B:JOSH.0000013053.32600.3c](https://doi.org/10.1023/B:JOSH.0000013053.32600.3c)。

版本：author_manuscript_faculty_public_copy。40页作者主页公开稿，题名/作者对应正式DOI，抽取有少量连字控制字符；不是按正式期刊分页配对的版本。

[实际阅读入口](https://www.cs.colostate.edu/~howe/papers/JOS04.pdf)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[9, 10, 17, 18]的相关段落；实际图页相关区域[9, 18]。PDF SHA256 `3c5e10d7fa07fb5ca9ea689a98d50906ea40f0bb2ed3ead28ad4e2420b9f86be`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-047-C01|Theorem2; exchange argument；物理页[9, 10]|GreedyIS最优性定理限于相同资源且无松弛的低轨请求多资源排程，证明用交换构造保持任务数。|不能把该特例最优性扩写到异构站、可变时窗或加权/延迟目标。|
|B07-047-C02|§4; benchmark discussion；物理页[17]|作者同时指出少量真实实例可能导致过拟合，而随机实例可能更难且不具真实结构。|真实与随机标签本身不能决定证据强弱；需报告实例结构和任务生成条件。|
|B07-047-C03|§4.1 problem generator；物理页[17, 18]|单资源试验按任务数与最大松弛组合生成36组、每组100实例，明确包含不现实的极端设置。|算例覆盖用于包围性能，不是对生产任务分布的概率抽样保证。|
|B07-047-C04|§4.2 CPU ceiling；物理页[18]|分支定界以每例1小时CPU为上限，部分实例即使加至10小时仍未求完。|求解未完成不能标成最优、无解或物理不可行；历史硬件秒数也不能当当前星载预算。|

服务综述：3.2.2/4.1：结构条件与精确求解的边界。

仍缺：定理只阅读相关证明段，未作独立全篇证明检查；作者稿终刊差异和全部求解结果未复现。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
