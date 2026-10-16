# [48] Satellite downlink scheduling problem: A case study

中文译名：卫星下传调度问题：案例研究。DOI：[10.1016/j.omega.2015.01.001](https://doi.org/10.1016/j.omega.2015.01.001)。

版本：author_preprint_arxiv_1206.5503v3_2015-02-14_repository_copy。Essex仓储作者稿，实际首页arXiv:1206.5503v3，14 Feb 2015；23页，与Omega正式DOI尚未逐命题配对。

[实际阅读入口](https://repository.essex.ac.uk/17381/1/1206.5503v3.pdf)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[7, 8, 9, 19]的相关段落；实际图页相关区域[8, 19]。PDF SHA256 `9ff7e684cef48bcb609ed6f9ebfcbedf373316fa00de539560cc77e5f60d34ab`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-048-C01|GRASP; Algorithms1–2；物理页[7, 8]|完整交换邻域加三次复杂度解码使遍历成本高，GRASP采用随机邻域访问和时间限额。|声明的是限时启发式，不是穷尽邻域或局部最优完成；复杂度为作者分析未独立证明。|
|B07-048-C02|ejection chain; partial and full objective；物理页[8]|移除hole位置请求的部分排列用于链搜索评分，同时计算完整排列目标保存最好完整解。|内部辅助评分与最终可交付排程目标应分开，不能把部分解当完整结果。|
|B07-048-C03|tabu representation discussion；物理页[9]|不同请求排列可以映射到同一实际排程，单纯记录排列位置的禁忌表可能无法排除重复排程。|表示层多样性不等于业务安排多样性；这是文中解释，未独立复现实验。|
|B07-048-C04|§7.3; Fig2；物理页[19]|过载时alpha权重改变漏排数与迟延的折中；图2平均30秒搜索、10个种子和高密度实例。|有限加权搜索点不等于精确Pareto前沿，低密度全安排也不能代表过载表现。|

服务综述：3.2.2/4.1：解码器、邻域和评价量。

仍缺：未重跑算例、全部解码器复杂度证明及正式配对；参数外推保持开放。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
