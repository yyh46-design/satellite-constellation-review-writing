# C4N05_RART｜Towards Robust Spacecraft Trajectory Optimization via Transformers

作者：Yuji Takubo; Tommaso Guffanti; Daniele Gammelli; Marco Pavone; Simone D’Amico。年份：2025。

实际版本：arXiv:2410.05585v2, 2025-01-25; author preprint。

[实际全文](https://arxiv.org/pdf/2410.05585v2)。DOI：本轮不登记未经配对的正式DOI。

PDF SHA-256：`034f3fe2b9118b1c15923ca640bef160ddeca1f91c57f894572ad9e24af01080`。

本轮正文阅读：1–11 main text and appendix narrative; bibliography/biography not treated as evidence。原页视觉核对：[3]。

采用：`ADOPT_STRUCTURE_AND_QUALITATIVE_COMPARISON`。既有身份：No matched body-reading note in checked repository。本轮为AI正文阅读；未独立复现、未替代作者科学终核。

## 问题、模型与方法

将Transformer热启动与含机会约束的相对轨迹SCP结合，导航误差、脉冲执行误差和过程噪声通过高斯协方差模型进入安全裕量，并检查失去控制后一轨内的漂移安全。实际优化始终采用ROE；比较RTN/ROE是训练与推理状态表示的区别。约束协方差从当前名义状态和控制恢复，模拟每步获得状态估计的效果，并非实际滤波器闭环。

两类各115,000条数据集，90/10划分，100节点、1.29轨转移时域；两个航天器。没有推力幅值约束。学习轨迹作为初值，由SCP处理终端和安全条件；后验接受规则按初值的代价、约束表现决定使用学习初值或回退凸解。

## 可追溯论点

- C4-N05-01：不确定性及失控漂移要求改变可用初值和后续优化，学习模块应与这些要求一致。定位：§2–4，pp2–6。
- C4-N05-02：学习热启动在样本中同时出现改善与退化；启发式后验筛选减少较差初值，也舍弃一些有较大收益的初值。定位：pp9–11图9–10。
- C4-N05-03：正文仍将闭环MPC及飞行级GPU计时列作后续工作。定位：p11结论。不得合并TMPC另一篇实验宣称本方法已完成这些验证。

## 采用与疑点

p3式(7)在“满足”不等式时令指标为1，与“违反预算”及p10中零值对应安全的文字冲突，已看原页。本章采用方法结构与后验筛选的定性权衡，不转抄该式，不复述精确失败率或概率保证。机会约束置信度针对给定模型和约束，不能称整个多星运行过程的成功概率。
