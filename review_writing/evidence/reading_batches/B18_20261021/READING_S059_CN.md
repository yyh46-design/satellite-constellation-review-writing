# B18-S059｜近距操作的分区准入、取消/中止与安全验证链

Close-Proximity Operations Design, Analysis, and Validation for Non-Cooperative Targets with an Application to the ClearSpace-1 Mission

- 作者：José Vasconcelos; Serena Gaggi; Tiago Amaral; Charles Bakouche; Adina Cotuna; Ana Friaças
- [来源入口](https://doi.org/10.3390/aerospace12010067)；标识：10.3390/aerospace12010067。
- 实际版本：Aerospace 12(1):67，2025-01-18出版，23物理页；以VESPA案例设计为准，不把该旧案例当作当前CS-1任务状态。
- [实际获取PDF](https://mdpi-res.com/d_attachment/aerospace/aerospace-12-00067/article_deploy/aerospace-12-00067.pdf)；23页；来源ID：E-B18-S059。
- 源文件SHA-256：ed215ff9ad3827e57cc43e16d10f4098fda20418c1af92e0fee0d80a01a6b823。
- 正文叙述范围：PDF物理页1–21；关键页视觉核查：1, 7, 8, 19, 21。
- 附录/证明范围：No separate appendix; references skim; targeted equations, no independent proof/experiment reproduction。
- 证据角色：single_spacecraft_operational_safety；采用状态：candidate_after_human_review。
- AI正文精读完成，人工终核待完成；未逐式复证明或独立复现实验。S编号不占原80篇L编号。

## 研究问题

在逼近非合作目标时，如何把区间、准入门槛、被动安全、主动撤离及恢复组合成可验证的运行逻辑，而不只优化一条标称无碰撞轨迹。

## 输入、决策与协同机制

目标/服务星几何、姿态与相对状态估计，光照与视场条件，推进/控制能力及故障模型；使用相机、雷达及分阶段导航滤波，不是纯位置几何问题。

定义AZ/KOZ、Approach/Abort走廊、不可返回点和分阶段Go/No-Go；根据导航、执行器与资源可用性选择继续、Cancel撤回可恢复点或Abort转安全轨迹。

远距离ROE轨迹通过相对偏心率/倾角向量共线构造被动安全，近距离依靠6DOF控制与FDIR。以快速模型先找困难初态，再在高保真模型中围绕其做定向Monte Carlo；导航还用合成成像及地面光学台架补充。

## 验证设置与证据层级

单服务星对单非合作目标的任务设计与MIL仿真。给AZ半径1 km、KOZ半径6 m等案例参数；推进器失效触发Abort，Cancel停止跳跃失败仍保持远离目标。未见足以独立复现全部风险统计的完整样本数和参数分布。

## 可追溯论点

- **C-B18-041**：AZ、KOZ和捕获入口各有准入条件，AZ/KOZ的Go由地面发出，捕获Go可自主。
  原文定位：PDF物理页6, 7, 8；§3.2–3.3; Fig.5。
- **C-B18-042**：Cancel用于中断不满足接近条件的操作并保留恢复机会，Abort用于安全受威胁时进入被动安全轨迹。
  原文定位：PDF物理页8, 9；§3.4; Fig.6。
- **C-B18-043**：远距离以ROE共线构造被动安全，近距则依赖控制和FDIR补充主动安全。
  原文定位：PDF物理页14, 15, 16；§4.3–4.4; Figs.13,15。
- **C-B18-044**：故障中止用快速仿真定位困难条件，再用高保真模型作定向Monte Carlo，并测试Cancel停止跳跃失效。
  原文定位：PDF物理页18, 19, 20；§5.4–5.5; Figs.21–23。
- **C-B18-045**：论文的验证为设计/分析/MIL及地面光学试验，地面仍参与监控和决策点，并期待飞行经验后减少地面控制。
  原文定位：PDF物理页18, 21；§5.3; §6 Conclusions。

## 适用边界与待核问题

- 这是设计、分析及地面验证文献，不是CS-1已在轨捕获或多星协商演示。
- Go for AZ及KOZ由地面发令，捕获Go可自主；结尾说面向全自主并未取消现有地面准入点。
- 区域与走廊尺寸依任务缩放，1 km/6 m/50%裕度不是所有任务或法规统一数值。
- 所列标准/指南为文章的2025引用背景；本批未核对其当前法规版本，不给合规认证意见。
- 抽取夹有图形嵌入的旧版页眉/重复文字，视觉页显示正式23页；均按实际PDF物理页定位，不按嵌入的24页号。

## 对综述的作用

作为3.6.3及采用更新的工程基础：安全撤离与可恢复撤回是不同决策，执行前须验证状态和执行链可用性。向多星推广时还缺其他主动成员和次生交会约束。

以上为阅读者的采用建议，尚未写入v3.2。完成阅读和文件核验不等于科学结论已经获认可。
