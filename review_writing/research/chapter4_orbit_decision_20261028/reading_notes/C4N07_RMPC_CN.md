# C4N07_RMPC｜Reinforced Model Predictive Guidance and Control for Spacecraft Proximity Operations

作者：Lorenzo Capra; Andrea Brandonisio; Michèle Roberta Lavagna。年份：2025。

实际版本：Aerospace 12(9), 837; publisher PDF。

[实际全文](https://mdpi-res.com/d_attachment/aerospace/aerospace-12-00837/article_deploy/aerospace-12-00837.pdf)。DOI：10.3390/aerospace12090837。

PDF SHA-256：`9633ac3ea4ad693dc5ccc3cc1776316755c65ffa691d2b9288b2e350d655afb6`。

本轮正文阅读：1–14 main text; references 14–15 identification only。原页视觉核对：[4, 12]。

采用：`ADOPT_HIERARCHICAL_ROLE_ONLY`。既有身份：No matched body-reading note in checked repository。本轮为AI正文阅读；未独立复现、未替代作者科学终核。

## 问题、模型与方法

相对运动下的非合作目标表面建图：PPO策略通过六个轴向推力选项及零动作规划成像轨迹，奖励与表面可见、光照及建图增量有关；MPC跟踪这段参考轨迹，权衡跟踪误差和控制量，并施加推力与最小距离条件。于是复杂的任务收益放在学习制导层，短时域动力学与约束放在控制层。

论文比较循环网络和Transformer策略，训练18,000回合；MPC预测400 s、采样10 s、执行首10个采样间隔。训练距离下界1.5 m，测试MPC距离界5 m，刻意观察约束修正参考轨迹。图像生成及导航噪声进入测试。Raspberry Pi 4计时图展示循环网络实现，而非两个架构均实测。

## 可追溯论点

- C4-N07-01：学习层任务轨迹与MPC轨迹可以不同，后者在参考轨迹接近目标时改变轨迹。定位：pp3–7架构及pp10–11图5–6。
- C4-N07-02：Transformer在所设任务中倾向于停留并利用目标转动获取各面，成像过程慢于循环策略；两种网络形成不同的几何/时间取舍。定位：pp11–12。
- C4-N07-03：板级计时对应循环网络；结论将与经典方法的进一步比较列为后续工作。定位：pp12–14。不能写成全面超越经典控制或已飞行验证。

## 采用范围

采用任务制导与约束跟踪的分工，连接学习输出与实际轨迹。p4式(1)–(2)的相对动力学符号、角速率表达及平均运动定义有需澄清之处（已视觉检查），p8控制量单位也需核对。本章不引用这些公式、绝对精度或无条件安全结论，相关疑点不被隐藏。
