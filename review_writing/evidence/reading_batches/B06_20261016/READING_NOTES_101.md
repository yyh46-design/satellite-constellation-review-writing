# [101] Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry

中文译名：揭示高估：航天器遥测深度异常检测的重新评价。DOI：[10.1007/s12567-023-00529-5](https://doi.org/10.1007/s12567-023-00529-5)。

版本：publisher_VOR_Springer_OA。13页正式CEAS16(2024):225–237，DOI与作者相符；本轮补充历史精确定位。

[实际阅读入口](https://link.springer.com/content/pdf/10.1007/s12567-023-00529-5.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[4, 5, 7, 8, 9, 11]的相关段落；实际图页复核[7, 11]的相关区域。PDF SHA256 `e02d7fd2220a4919737c263620e1c259beff884c7d85ff15656b9fad5378fb7c`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-101-C01|thresholding and concatenation discussion；物理页[4, 5, 8]|指出测试标签调阈值及拼接独立序列的风险；本研究为公平比较也统一用最大F1阈值，另报LSTM的NPT。|共同oracle阈值不变成可部署无监督标定；NPT结果需单列。|
|B06-101-C02|metrics/aggregation examples；物理页[7, 8]|比较PA、事件召回及多种指标，说明长异常与混淆矩阵汇总可能主导总分。|事件评价不等同PA；新指标仍有持续全告警难以惩罚的问题。|
|B06-101-C03|baseline comparisons and Tables5/6；物理页[8, 11]|加入原始信号、随机未训练AE、随机告警等基线；部分深模型在所测指标下不及简单基线。|不推导所有深学习无效；排名依赖数据、阈值与指标。|
|B06-101-C04|ESA case and qualitative result；物理页[9, 11]|ESA案例只有七个异常，并选择电流通道；作者明确未以时效性为本研究重点。|不能将离线检测分数扩大成故障定位、及时处置或恢复成功率。|

服务综述：3.4.3及4.4：阈值泄漏、聚合权重、指标与简单基线。

仍缺：新取得正式PDF用于补历史精确定位，不增加去重；全部代码、标签和数据版本未独立复现。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
