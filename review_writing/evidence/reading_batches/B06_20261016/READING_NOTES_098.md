# [98] Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding

中文译名：基于LSTM与非参数动态阈值的航天器异常检测。DOI：[10.1145/3219819.3219845](https://doi.org/10.1145/3219819.3219845)。

版本：author_preprint_arxiv_v3。实际页标记arXiv:1802.04431v3, 6 Jun 2018，9页ACM式作者预印本；与正式KDD DOI相关联，未逐命题配对正式版。

[实际阅读入口](https://arxiv.org/pdf/1802.04431v3)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[4, 6, 7]的相关段落；实际图页复核[4, 6, 7]的相关区域。PDF SHA256 `bd5e2eb0706d2278eec1874dd32700fbd0d929e9c7208ed33c28ae5ace305836`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-098-C01|thresholding and pruning；物理页[4, 7]|用平滑预测残差调阈值，再剪枝异常序列以降低误报，代价是召回变化。|检测表现属于预测+阈值+后处理，不能全部归给LSTM。|
|B06-098-C02|event-overlap evaluation rules；物理页[6]|标记事件只要与任一预测区间重叠就记一次TP；未按检测早晚或区间距离再评分。|这是事件命中规则，不能直接代称逐点准确率、延迟指标或另一论文的PA填充规则。|
|B06-098-C03|batch evaluation；物理页[6]|实验按一分钟聚合、70分钟批次及历史误差窗评估，并扩展/合并相近预测区间。|批次与后处理影响响应时刻，不能仅由网络推理速度声称实时恢复。|
|B06-098-C04|operating precision limitation；物理页[7]|作者指出五天含一次异常且排除无异常通道，会使实验精度高于实际实现。|需要更贴近运行基率与正常数据的误报负担，不能把实验precision当全星座告警效能。|

服务综述：3.4.3及4.4：告警事件、后处理和运行分布。

仍缺：arXiv v3正式配对、全部实现和分数公式未复现；旧表格统计疑点与实时部署完整账目仍保留。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
