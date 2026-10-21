# B18-S054｜Starling早期在轨协商、导航与自主机动失效边界

Starling CubeSat Swarm Technology Demonstration Flight Results

- 作者：Scott Miller; Caleb Adams; Nahum Alem; Howard Cannon; Randy Grashuis; Ted Hendriks; Soon Hwang; Michael Iatauro; Craig Pires; Justin Kruger; Simone D’Amico
- [来源入口](https://ntrs.nasa.gov/citations/20240006994)；标识：NASA:20240006994。
- 实际版本：NASA NTRS会议稿SSC24-I-06，38th Annual Small Satellite Conference，13物理页。
- [实际获取PDF](https://ntrs.nasa.gov/api/citations/20240006994/downloads/SSC24_Starling_Swarm_Flight_Results.pdf)；13页；来源ID：E-B18-S054。
- 源文件SHA-256：59d276712b31cfd8d3af07d9c182c90bc25d402b1541a168fdc3292d36c70256。
- 正文叙述范围：PDF物理页1–12；关键页视觉核查：1, 5, 8, 10。
- 附录/证明范围：No separate appendix; references skim; targeted equations, no independent proof/experiment reproduction。
- 证据角色：multi_spacecraft_flight_report；采用状态：candidate_after_human_review。
- AI正文精读完成，人工终核待完成；未逐式复证明或独立复现实验。S编号不占原80篇L编号。

## 研究问题

四颗CubeSat的网络、观测协商、视觉导航和自主机动是否都完成同一层次的在轨闭环；实际平台问题如何打断计划采用和执行。

## 输入、决策与协同机制

BATMAN跨星网络、GPS双频数据、星敏感器影像和地面精密定轨。DSA实际只有三颗加入软件网络；Starling-1上行/更新异常导致其未参加该项试验。

DSA各星用MILP求GPS信道分配；StarFOX估计绝对/相对轨道；ROMEO生成队形维持机动，仍设计由地面完成交会筛查和最终Go/No-Go。

网络提供状态/奖励交换，各星独立构造同一分配问题、取出本地部分执行。协商一致是同一计划，不保证持续一致，更不等于轨道避碰安全。机动链中导航滤波、推进剂限制和命令时序各自能阻止执行。

## 验证设置与证据层级

四星在轨技术演示；DSA三星在选定时段再一致平均2.04 s、最慢46 s，但并非全时一致。MANET演示多跳和多速率，超过50 KB文件传输不可靠。ROMEO在本报告截止阶段未完成完整机动成功条件；StarFOX部分模式用飞行数据在地面后处理验证。

## 可追溯论点

- **C-B18-016**：MANET在轨测试实现多跳传输，但超过50 KB文件的可靠接收存在持续问题。
  原文定位：PDF物理页4, 5；MANET Flight Results。
- **C-B18-017**：ROMEO计划被设计为地面筛查后发出Go/No-Go，48小时实验窗中约前半用于生成和筛查。
  原文定位：PDF物理页5；ROMEO Flight Results, 48-hour workflow。
- **C-B18-018**：该版ROMEO因导航滤波和命令时间问题，未能规划并执行满足完整成功条件的机动。
  原文定位：PDF物理页5, 6, 12；ROMEO Flight Results; Summary。
- **C-B18-019**：DSA实际为三颗星的信道协商；选定时段平均再一致2.04 s，最大离群值46 s。
  原文定位：PDF物理页7, 8；DSA Flight Results, Figs.8–10。
- **C-B18-020**：模式4在轨尝试受硬件问题阻碍，随后采用飞行影像及模拟跨星测量在地面数字孪生中验证。
  原文定位：PDF物理页10, 11；StarFOX Navigation Mode4 detailed result。

## 适用边界与待核问题

- 同一Starling任务的阶段报告，与S057/S058共享数据和平台，不能当三次独立复验。
- StarFOX p9概述四模式已演示，p10明确模式4在轨尝试受硬件阻碍后由地面数字孪生演示；采用后者的具体层级。
- 报告中的Starling 1.5跨运营者交通协调是后续计划，不能据此认定已经实现。
- p11实验日期出现2025年份与2024会议截点不协调，保留原文问题，不拿该日期建立进度结论。
- 结果为任务方报告，未取得原始全量遥测做独立核验。

## 对综述的作用

优先补“形成—协调—采用更新”的实证链：观测计划能自主协商，并不保证自主机动链已打通；失败原因也应是综述的重要证据。

以上为阅读者的采用建议，尚未写入v3.2。完成阅读和文件核验不等于科学结论已经获认可。
