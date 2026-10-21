# B18-S058｜Starling扩展任务的执行链补强及光学态势感知边界

NASA’s Starling Mission and Space Situational Awareness Implications

- 作者：Roger C. Hunter; Elwood F. Agasid; Samson Phan; Nathan A. Benz; Scott T. Miller; Caleb A. Adams; Brian C. Kempa; Jeremy D. Frank; Michael J. Iatauro; Justin Kruger; Simone D’Amico; Julianna L. Fishman; Sasha V. Weston
- [来源入口](https://justin.zone/starling_amos_2025.pdf)；标识：AMOS2025:Starling-SSA。
- 实际版本：AMOS 2025会议论文，由作者Justin Kruger网站提供18页PDF；正文以各试验截止日为准，不作2026年任务最新状态。
- [实际获取PDF](https://justin.zone/starling_amos_2025.pdf)；18页；来源ID：E-B18-S058。
- 源文件SHA-256：eaf946d16eb7e2e090eddd586e453d98efdc2525a164e93e6ae1b89bb1e7e4d3。
- 正文叙述范围：PDF物理页1–17；关键页视觉核查：1, 3, 6, 12, 14, 15。
- 附录/证明范围：No separate appendix; references skim; targeted equations, no independent proof/experiment reproduction。
- 证据角色：multi_spacecraft_flight_extension；采用状态：candidate_after_human_review。
- AI正文精读完成，人工终核待完成；未逐式复证明或独立复现实验。S编号不占原80篇L编号。

## 研究问题

Starling早期平台/执行短板在后续软件更新中改善到哪一步，分布式观测决策、网络资源控制和光学态势感知分别有哪些实际结果与未完成环节。

## 输入、决策与协同机制

三星DSA观测与奖励交换、星敏感器影像、星上TLE目标目录；目标目录由地面更新上传，跨星通信和可见性均是能力前提。

每星1 Hz构造同一MILP并抽取本地GPS信道计划；扩展试验通过本地执行代理控制跨星电台开关、网络重建及分片重传。StarFOX+则作目标识别和快速初始定轨。

计划一致、目标覆盖和重配置时延分别定义。观测奖励变化可触发重分配，网络资源执行也进入自治环节；这比只在软件内算计划更接近采用闭环，但不等于整个星群可靠自主机动。

## 验证设置与证据层级

报告2024年11月SV4完成三次点火的一次自主维持机动；DSA1.5重复传输10 MB文件并跨网络中断重传。StarFOX+报告2025年4–7月识别591个不同对象，表2综合正确匹配81.3%。快速合作定轨仍以地面运行飞行软件处理历史飞行数据验证，8次初始化中部分误差不被采样不确定度良好覆盖。

## 可追溯论点

- **C-B18-036**：2025报告记载2024年11月SV4完成三次点火的自主维持机动，同时明确可靠星群自主机动仍不足。
  原文定位：PDF物理页3；§3.2 ROMEO。
- **C-B18-037**：DSA各星以1 Hz求同一信道MILP；计划一致、覆盖和反应时延是不同指标。
  原文定位：PDF物理页5, 6, 7；§4.2–4.4。
- **C-B18-038**：DSA1.5在轨演示按环境/位置建立和拆建网络，并通过分片重传重复完成10 MB文件传输。
  原文定位：PDF物理页9；§4.6, local autonomy and LFT results。
- **C-B18-039**：StarFOX+任务方报告识别591个不同对象，表2综合正确匹配81.3%；不等于591个对象状态全部精确恢复。
  原文定位：PDF物理页12, 13, 14；§5.4.1; Table2。
- **C-B18-040**：快速合作初始定轨结果来自地面飞行软件回放，8次初始化中最大沿轨误差约18 km且不确定度包络欠佳。
  原文定位：PDF物理页15, 16；§5.4.2 Fig.15, Table3。

## 适用边界与待核问题

- 与S054/S057共享Starling任务，仅是新阶段/专题报告，不能视作独立任务验证。
- p6写16次运行中13次成功或半成功，却随后称86.7%；13/16为81.25%，分母口径未解释，本批不采用86.7%。
- p16称2024完成所有技术目标，与p3将一次自主机动定在2024年11月且承认星群可靠机动不足存在张力；以具体结果限定结论。
- p17将DSA成果概述成队形/轨迹重构强于信道及硬件调度证据，不沿用该升级表述。
- p12–13正确/错误识别阈值的印刷不等号范围重叠；表2匹配率作为任务方报告而非独立核实精度。
- 快速初始定轨在正文中仍为地面验证及计划在轨测试，不能因会议较晚便自动视作已在轨成功。

## 对综述的作用

补计划采用和资源执行：共享状态、共同求解、计划一致、执行代理、传输校验与状态更新逐层成立。保留早期失败到后续局部成功的时间线，不用总结性口号覆盖具体限制。

以上为阅读者的采用建议，尚未写入v3.2。完成阅读和文件核验不等于科学结论已经获认可。
