# [1] Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts

中文译名：大型分布式卫星系统的自动化运行：第一部分，综述与范式转变。DOI：[10.1016/j.asr.2020.08.009](https://doi.org/10.1016/j.asr.2020.08.009)。

版本：author_preprint_public_HTML_2020-12-01。作者2020-12-01公开正文，长作者稿布局；不能用正式刊页替代HTML定位。

[实际阅读入口](https://www.researchgate.net/publication/343791434_Towards_the_Automated_Operations_of_Large_Distributed_Satellite_Systems_Part_1_Review_and_Paradigm_Shifts)；本轮类别：new_targeted_upgrade_from_partial。新增定向记录，不表示全篇逐证明完成。

阅读范围：HTML工具快照行[[620, 865], [1960, 2200], [2530, 2730]]，没有本机PDF页数、文件哈希或图公式像素。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-001-C01|HTML L620–751, operational workload；物理页不适用|扩展压力包括资源排程、监测、配置和轨道管理，固定天线竞争还增加星上等待存储。|不能只以卫星数或算法速度表示运行可扩展性。|
|B06-001-C02|HTML L2065–2139, Dove anomaly handling；物理页不适用|已知异常可自动分诊，部分反应命令排队到下一可用过站执行。|告警检测、决策和实际恢复时间不同；历史案例不代证任意异常自治。|
|B06-001-C03|HTML L2143–2188, configuration control；物理页不适用|Dove案例用试运行卫星测试版本，再向其余卫星推广，并保留按星使用不同版本的能力。|这是版本与回馈组织实例，不是在线学习模型自动获准上星。|
|B06-001-C04|HTML L2612–2701, paradigm discussion；物理页不适用|作者把系统聚合指标与分层异常处置相连，提出服务化运行接口。|二次工程描述和方向建议须与当前部署证据分开。|

服务综述：1.2、3.5和4.3：工程案例中的告警、处置、上注与版本职责。

仍缺：作者公开HTML；PDF403，图表/公式像素与终刊版本配对未核。案例与星数为文中历史记录，不是2026状态。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
