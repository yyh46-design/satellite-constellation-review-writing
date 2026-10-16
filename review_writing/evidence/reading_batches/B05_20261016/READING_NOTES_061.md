# [61] Robust Earth Observation Satellite Scheduling With Uncertainty of Cloud Coverage

中文译名：考虑云覆盖不确定性的鲁棒对地观测卫星调度。DOI：[ 10.1109/TAES.2019.2947978 ](https://doi.org/10.1109/TAES.2019.2947978)。

版本：author_manuscript_dated_2020-03-18。入口：[实际阅读来源](https://drive.google.com/uc?export=download&id=1ZWAE-hwLsw2lb1-6BrzXHcVYRNGIDMJe)。作者公开GoogleDrive副本由Leus公开出版物页直接链接，41页，首页Preprint submitted to IEEE TAES March18,2020；未与正式12页配对。

本轮类别：followup_no_unique_increment。补读不增加不同论文数。

阅读范围：物理PDF选读页[24, 25, 26, 27, 28, 31]；实际图页复核[26, 28]的相关区域；文件SHA256 `900e6c9125732d92f2d17ca3072dd2a23130515d2bc01f399e942b989d94bacb`。

|ID|原文定位|观察|使用边界|
|---|---|---|---|
|B05-061-C01|Section4, 46/270 unfinished integer masters；页[26, 28]|300目标270例有46例在1200秒未完成整数主问题，作者仍讨论其最好解与LP上界差距。|未完成不是无可行解或物理不可行；不能把这些例删除后报告性能。|
|B05-061-C02|Section4.2.1 p25 definitions; Tables4–7；页[25, 27, 28]|p25设整数求解器1%容差；opt数限时内完成的整数主问题；gap为最好解与LP上界距离。|不能把opt列当原整数问题零间隙全局证书，LP gap也不是已知整数最优值的实测误差。|
|B05-061-C03|candidate-mission explanation；页[28]|测试候选任务不超过2000，文中据此解释DP定价快。|不能把300目标直接当几千卫星规模，且当前输入范围限制外推。|
|B05-061-C04|horizon sensitivity；页[31]|更长时域既增候选与机会，也可能因接近收益上界呈易—难—易的运行时间变化。|时域长度与难度不必单调，比较需同时报候选数及饱和程度。|

服务综述：3.2.3与4.1：主问题限时、LP界和规模难度。

仍缺：41页作者稿未配正式版；全部列生成/定价证明与实验未复现。完成/opt列不代表原整数问题全局最优。

作者归纳与原文观察分列；候选位置只供后续修订，不表示原段已整体核验。下载/HTML可见/渲染均不计为自动精读完成。`human_verified=false`；正式版配对、全部证明与独立实验未关闭。
