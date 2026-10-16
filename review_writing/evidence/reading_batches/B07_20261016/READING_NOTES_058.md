# [58] Kodan: Addressing the Computational Bottleneck in Space

中文译名：Kodan：缓解空间计算瓶颈。DOI：[10.1145/3582016.3582043](https://doi.org/10.1145/3582016.3582043)。

版本：publisher_typeset_proceedings_copy_hosted_Microsoft_Research。Microsoft Research公开12页ACM最终排版副本，ASPLOS 2023:392–403、DOI及许可标记可见。

[实际阅读入口](https://www.microsoft.com/en-us/research/uploads/prod/2023/08/asplosc23main-p858-p-224936cdce-68637-final.pdf)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[4, 5, 9, 10]的相关段落；实际图页相关区域[5, 10]。PDF SHA256 `d020df104eebef2d0cce6013c6620a8e7d98419521747922b37c7d0755d9b5bf`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-058-C01|Fig6; frame tiling；物理页[5]|固定网络输入下，更少图块需更强降采样，更多图块增加处理时间并保留更多细节。|更高输入分辨率与更高端到端信息价值并非同一目标，需结合帧截止期。|
|B07-058-C02|elision and §3.1；物理页[5]|部分高价值上下文可绕过昂贵过滤直接下传，低价值上下文可直接丢弃；预部署生成选择逻辑，运行时按样本选择。|这是带误判和丢弃代价的处理选择，不能称所有样本都被完整推理或保证无有价值数据损失。|
|B07-058-C03|§5.2 deadline regime；物理页[9]|当处理时间降到帧截止期以内后，文中业务价值密度主要受精确率限制，进一步提速的作用改变。|收益依赖当前瓶颈，不能将推理加速比例等同于有效交付比例。|
|B07-058-C04|Figs14–15; §§5.4–5.5；物理页[9, 10]|图块和跳过处理的收益随Orin15W、i7、1070Ti平台及应用复杂度变化。|最优配置依赖硬件和任务，不形成跨应用、跨硬件的固定统一参数。|

服务综述：3.2.2/4.2：计算与下传瓶颈及信息价值。

仍缺：历史硬件与应用条件保留；未复现分类、下传或丢弃风险，未证明全年业务交付。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
