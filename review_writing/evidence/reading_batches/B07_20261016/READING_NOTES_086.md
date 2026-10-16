# [86] CAMmary: A review of spacecraft collision avoidance manoeuvre design methods

中文译名：CAMmary：航天器避碰机动设计方法综述。DOI：[10.1016/j.actaastro.2025.07.027](https://doi.org/10.1016/j.actaastro.2025.07.027)。

版本：author_preprint_arxiv_2503.22555v1_2025-03-28。arXiv v1，40物理页，2025-03-28；未与Acta正式排版进行全文配对。

[实际阅读入口](https://arxiv.org/pdf/2503.22555)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[8, 9, 12, 16]的相关段落；实际图页相关区域[8, 16]。PDF SHA256 `9b2e1c032b9b99cfb88530ed54cbbfb47c4880f36740d24a1e5ddf2e91377a31`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-086-C01|§2.2.2 IPoC；物理页[8]|该综述将IPoC描述为长遭遇中的瞬时概率快照，与常见短遭遇PoC计算分开讨论。|综述性分类，不证明IPoC与全时间窗遭遇概率普遍等价。|
|B07-086-C02|constant-PDF approximation discussion；物理页[8]|综述介绍常PDF近似时保留位置不确定性尺度相对硬体半径较大的条件。|引用某近似需追到原始模型前提，不能只保留计算快的结论；本轮未核其原始证明。|
|B07-086-C03|numerical CAM overview；物理页[9, 12]|综述指出直接数值法便于加入操作/饱和约束，同时需考虑计算成本与局部收敛，相关算例结果仍各有模型条件。|这是方法分类与原文转述，不是B07对全部数值法的独立统一排名。|
|B07-086-C04|multiple encounters overview；物理页[16]|综述区分多遭遇总风险约束与逐遭遇风险限值分配，并讨论长传播下非高斯表示。|不能把若干单遭遇阈值自动当成整体风险保证；原始风险合成和近似精度尚未独立审核。|

服务综述：3.4.1/4.4：风险度量和规避方法的综述性分类。

仍缺：本来源是综述，其转述原始方法未在B07逐篇打开；不新增这些被引原始论文的精读计数。作者稿正式版配对和概率定理仍待核。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
