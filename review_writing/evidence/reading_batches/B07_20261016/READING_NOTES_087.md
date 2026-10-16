# [87] Spacecraft collision avoidance challenge: Design and results of a machine learning competition

中文译名：航天器碰撞规避挑战：机器学习竞赛的设计与结果。DOI：[10.1007/s42064-021-0101-5](https://doi.org/10.1007/s42064-021-0101-5)。

版本：author_preprint_requested_arxiv_v1_with_internal_date_mismatch。请求2008.03069v1，实际页有arXiv v1 7 Aug 2020，同时正文抬头/生成日期含28 Mar 2022，时间信息不一致。题名作者匹配并以SHA锁定所读字节，不凭请求地址推断完整修订史。

[实际阅读入口](https://arxiv.org/pdf/2008.03069v1)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[11, 12, 13, 17, 18]的相关段落；实际图页相关区域[11, 13, 18]。PDF SHA256 `85fb56bdc051d54976d4dd446bef0ed4d2198ddf1a1242878b364d53bc6d49fd`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-087-C01|team sesc; Table4；物理页[11, 12]|阈值级联利用F2侧重召回和测试构成，修正边界风险并裁剪高风险值以改变不同评分分项。|比赛分数优化不等于物理风险更准或部署校准更好，不能把经验阈值直接当操作规则。|
|B07-087-C02|team Magpies; Fig12；物理页[12, 13]|相似度网络使用筛选特征、罕见低转高异常的过采样与三折模型筛选，再集成投票。|复杂模型结果依赖稀少事件、筛样和阈值过程，不是单独LSTM结构的因果增益。|
|B07-087-C03|§5.4 difficult samples；物理页[13]|顶尖团队共同误判的事件可出现接近前风险突跳，并伴随测量不确定性较高。|作者对选中难例的分析，不可归纳为所有事件必然不可预测或所有时序特征无用。|
|B07-087-C04|Figs18–20; Monte Carlo cross-validation；物理页[17, 18]|作者另用多次分层随机切分比较LightGBM与最新风险基线，并以每切分模型平均与基线配对检验。|算法/切分层级、重复训练与独立事件需分开；本轮只读统计设计，未复算显著性或验证未来任务外推。|

服务综述：3.4.1/4.3：风险预测、指标驱动与外推。

仍缺：作者稿内部日期与请求arXiv版本差异继承；未复现重采样、统计检验、阈值或终刊配对；不能标在轨风险处置验证。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
