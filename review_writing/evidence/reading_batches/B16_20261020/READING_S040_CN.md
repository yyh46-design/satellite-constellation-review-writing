# B16-S040｜实机通信延迟下的连通性CBF补偿启发式

Decentralized Connectivity Maintenance with Time Delays using Control Barrier Functions

- 作者：Beatrice Capelli; Hassan Fouad; Giovanni Beltrame; Lorenzo Sabattini
- [书目/原文入口](https://arxiv.org/abs/2103.12614v1)；标识：arXiv:2103.12614v1。
- 实际版本：arXiv v1，2021-03-23，共7页；正式发表版本配对未完成。原文为地面机器人研究。
- [实际读取PDF](https://arxiv.org/pdf/2103.12614v1)；来源ID：E-B16-S040；共7页。
- 源文件SHA-256：73836663b972f7fe9d3c06985b46e69b69ff6b801f3efc06ee83922dc2abe707。
- 阅读范围：PDF物理页1–6的正文叙述；关键原页视觉核查：3, 5, 6。
- 附录/证明范围：No separate appendix; proof narratives read but not independently reproduced。
- 证据角色：general_robot_connectivity_delay_foundation。
- 专题补充编号S031–S040；不占原80篇L编号。AI精读完成，人工终核待完成；未逐式复证明或独立复现。

## 研究问题

把连通性CBF从理想仿真部署到分散计算的真实机器人后，如何减轻陈旧信息对连通裕量的影响？

## 输入、决策与协同机制

R-disk通信图和一阶运动近似，图代数连通度λ2、给定阈值ε、速度上限与估计时延。各机器人通过多跳聚合全体相对位置，仍要形成全图Laplacian。

本地求解最小修改任务输入的QP，连通性CBF外另有避碰约束；将距离改为d+2vmax(τ+κ)，以经验参数κ补偿其他误差。

这是基于最坏相对运动直觉的启发式，并非通用时延安全域的显式求解。计算分散不意味着只有一跳信息，也不意味着不需要全网状态汇集。

## 验证设置与证据层级

5/10机器人仿真每配置20次，部分随机延迟配置低于期望连通阈值。实机3个Khepera IV，ARM 800 MHz、机器人本地QP，外部OptiTrack精确定位，测得延迟约0.3 s；无丢包和链路故障。

## 可追溯论点

- **C-B16-042**：各体虽独立求控制，却通过多跳传播全体相对位置以重建全图；“分散计算”不能简写成仅依一跳局部信息。
  原文定位：PDF物理页3, 4；§III-B、§IV及Buzz implementation。
- **C-B16-043**：延迟补偿使用d+2vmax(τ+κ)且κ经验调节；TableII部分随机延迟试验仍低于λ2阈值，不能声称所有试验均保持给定连通裕量。
  原文定位：PDF物理页3, 5；Equation11及TableII。
- **C-B16-044**：实体实验为3个Khepera IV本地QP、外部OptiTrack、约0.3 s延迟；位置噪声、丢包与链路故障未纳入，均留待后续。
  原文定位：PDF物理页3, 4, 5, 6；hardware setup、real experiments及Conclusion。
- **C-B16-045**：另10次覆盖试验相对给定最大可覆盖面积平均损失12.71%、标准差3.03%；这是任务覆盖代价，不能作为带宽节省或星座风险降低比例。
  原文定位：PDF物理页6；§V-E Performance analysis及Fig8。

## 适用边界与待核问题

- λ2仍大于0只说明图保持连接，与满足λ2≥ε的裕量要求不同。
- 经验调整κ并没有变成对任意网络/动力学的形式化鲁棒保证。
- 实机控制与定位条件应成对报告，不能只写“分散星载验证”。
- 覆盖损失指标与通信字节节省、任务完整成功率不同。

## 对综述的作用

用作通信模型与实际部署之间差异的通用实验基础，支撑3.6.3“采用前核查真实信息时效”的论述；不作多星验证。

以上采用建议为阅读者分析，尚未写入v3.2；不把作者主张、读者推论或文件完整性检查当作独立科学确认。
