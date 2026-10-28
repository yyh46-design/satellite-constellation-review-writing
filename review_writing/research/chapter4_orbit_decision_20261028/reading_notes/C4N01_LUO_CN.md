# C4N01_LUO｜Orbital Maneuver Optimization of Earth Observation Satellites Using an Adaptive Differential Evolution Algorithm

作者：Qizhang Luo; Wuxuan Peng; Guohua Wu; Yougang Xiao。年份：2022。

实际版本：Remote Sensing 14, 1966; publisher PDF。

[实际全文](https://mdpi-res.com/d_attachment/remotesensing/remotesensing-14-01966/article_deploy/remotesensing-14-01966.pdf)。DOI：10.3390/rs14091966。

PDF SHA-256：`04883cc858720d749f03295ef702775a575b8fb633477582e6cb9b83e26586ce`。

本轮正文阅读：1–19; references 19–21 checked for identity only。原页视觉核对：[7, 9]。

采用：`ADOPT_MODEL_STRUCTURE_ONLY`。既有身份：Historical Crossref metadata hit; no matched body-reading note in checked repository。本轮为AI正文阅读；未独立复现、未替代作者科学终核。

## 问题、模型与方法

应急目标出现后，选择执行卫星、机动时刻与速度增量，使新的过境满足任务要求。正文分别设置响应时间、地面分辨率和燃料三个单目标问题，并非一次求出三目标Pareto解集。轨道传播采用含J2长期项的根数更新，观测采用简化矩形视场、日照窗口和瞬时点目标成像；算例固定面外增量为零。自适应差分进化以图搜索选择变异、交叉及参数组合。

## 可追溯论点

- C4-N01-01：任务指标可以直接进入机动时刻和速度增量的优化，由新轨道传播回算响应与成像条件。定位：§2，pp3–9。
- C4-N01-02：三种单目标设置及可选成员范围对应不同方案选择。定位：§4，pp14–18。本文采用设计取舍，不引用数值优越性。

## 比较条件与取舍

三颗候选卫星、四个目标分别构成实例，12小时响应时域，最多50,000次适应度评价、10次运行；模型没有电池、存储和下传。可与Pearl的阶段轨位—资源模型对照“直接机动参数”和“候选轨位选择”的区别，不能做同任务性能排名。

原页p7式(14)节点进动符号、p9式(31)/(33)与段落的f1/f3对应存在疑点，已看原页；表3角度单位及转移代价也须进一步澄清。采用范围停在问题组织与方法结构，不转抄公式，不使用性能百分比。这不改变其原文取得和正文阅读完成状态。
