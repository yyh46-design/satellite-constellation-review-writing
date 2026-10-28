# C4N04_TMPC｜Transformer-Based Model Predictive Control: Trajectory Optimization via Sequence Modeling

作者：Davide Celestini; Daniele Gammelli; Tommaso Guffanti; Simone D’Amico; Elisa Capello; Marco Pavone。年份：2024。

实际版本：arXiv:2410.23916v1; accepted RA-L preprint; not page-paired with publisher。

[实际全文](https://arxiv.org/pdf/2410.23916v1)。DOI：10.1109/LRA.2024.3466069。

PDF SHA-256：`5e45a1a2ba5a9423e23f961804527421b8299e77d5eff431746cc33c46cdb2ad`。

本轮正文阅读：1–8 including conclusion; bibliography identification only。原页视觉核对：[8]。

采用：`ADOPT`。既有身份：No matched body-reading note in checked repository。本轮为AI正文阅读；未独立复现、未替代作者科学终核。

## 问题、模型与方法

在ART基础上，Transformer除生成初值，还给短时域MPC提供终端参考状态，距离该状态的代价将长期任务方向带入短期求解。离线开环轨迹预训练后，通过DAgger收集闭环访问状态与专家纠正数据，再训练模型；微调使用同一近似动力学模型，针对开环/闭环策略导致的状态分布变化。

实验包括相对轨道要素和脉冲控制下的空间交会仿真、四旋翼仿真及地面气浮平台。优化对照保持SCP，比较REL、仅目标距离终端代价、未微调TTO和微调FT-TTO。各仿真500实例，100节点，时域10–100节点。假定环境已知、状态完全估计。

## 可追溯论点

- C4-N04-01：学习生成的轨迹可同时提供初值与有限前视末端的参考，因而减少短时域求解的近视效应。定位：§IV.C，p4。
- C4-N04-02：仅开环训练的TTO在闭环中可劣于REL；微调后改进，表明更新方式和训练数据分布需要匹配。定位：§V.C，p7图5–6。
- C4-N04-03：地面气浮MPC对照中REL使用80 s到达/1.25 Hz，FT-TTO使用40 s/2.5 Hz；前者总喷气83.76 s，后者91.34 s。定位：pp7–8表I。不能概括为同期限下所有指标均优。

## 采用方式

采用长期指导、闭环微调和缩短优化时域之间的联系。7倍运行时间改善是论文特定时域与性能匹配比较，不推广为星载实时系数。地面气浮不是在轨试验；状态估计、分布外动力学和随机多任务扩展仍在结论中。已看p8表I。
