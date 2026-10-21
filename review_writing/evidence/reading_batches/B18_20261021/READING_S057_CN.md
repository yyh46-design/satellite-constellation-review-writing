# B18-S057｜Starling地面飞行动力学、避碰后恢复与故障重调度

Mission Design and Flight Dynamics Operations for the Starling Swarm Technology Demonstration

- 作者：Nahum Alem; Theodore G. Hendriks; Jose L. Alvarellos; Paul G. Levinson-Muth; Andres Dono
- [来源入口](https://ntrs.nasa.gov/citations/20250007355)；标识：NASA:20250007355。
- 实际版本：NASA NTRS会议稿，2025 AAS/AIAA Astrodynamics Specialist Conference，15物理页。
- [实际获取PDF](https://ntrs.nasa.gov/api/citations/20250007355/downloads/MissionDesign_FlightDynamicsOps_Starling_AS_2025.pdf)；15页；来源ID：E-B18-S057。
- 源文件SHA-256：bd1ffd361905395bb15c1aeac40fda51f1e177b0116d182533cdeb79386ff7a2。
- 正文叙述范围：PDF物理页1–15；关键页视觉核查：1, 10, 12, 13。
- 附录/证明范围：No separate appendix; references skim; targeted equations, no independent proof/experiment reproduction。
- 证据角色：multi_spacecraft_flight_operations；采用状态：candidate_after_human_review。
- AI正文精读完成，人工终核待完成；未逐式复证明或独立复现实验。S编号不占原80篇L编号。

## 研究问题

在实际推进故障、测量缺口、进入安全模式和外部高风险交会下，群体队形的维持与任务恢复如何被组织进日常运控闭环。

## 输入、决策与协同机制

四颗星GPS导航解、地面ODTK联合滤波和平滑、空间天气及地球定向数据；输出轨道与协方差用于队形监测、机动设计和外部交会筛查。

地面FD团队按需在每周节奏内分配维持与队形调整机动；推进泄漏后让其他成员补偿Starling-1漂移。外部碰撞规避打破原有间距时，随后安排队形恢复。

先更新状态与协方差，再生成/审查机动、CARA筛查、运控批准和执行，后续重建机动表现。平台安全模式会丢失既有活动且改变阻力，形成状态更新、资源变化与重新采用计划的耦合。

## 验证设置与证据层级

基于实际四星任务的运行报告。CARA每日多次返回未来七天交会；GPS中断对应沿轨位置3σ不确定度接近70 m。安全模式恢复多数24小时内，少数到一周；高阻姿态改变后续漂移。另有推进异常期间的数天至数周差分阻力操作。

## 可追溯论点

- **C-B18-031**：地面联合处理四星GPS进行定轨，再把轨道与协方差送CARA，接收未来七天的交会分析。
  原文定位：PDF物理页7, 8；Orbit Determination section。
- **C-B18-032**：主要机动规划由地面飞行动力学团队实施，包含审查、CARA筛查和运控批准，通常以周为节奏。
  原文定位：PDF物理页11, 12；Maneuver Planning; Table2。
- **C-B18-033**：安全模式会丢失后续已排活动，恢复后重规划；该模式阻力面积约为名义六倍。
  原文定位：PDF物理页12, 13；Off-Nominal Operations。
- **C-B18-034**：外部碰撞规避虽降低交会风险，却引入群内漂移，需要后续队形维持机动纠正。
  原文定位：PDF物理页13；Off-Nominal Operations, COLA paragraph。
- **C-B18-035**：GPS数据缺口对应Fig.4c沿轨位置3σ不确定度接近70 m；该图为May，July示例另在Fig.5。
  原文定位：PDF物理页8, 10, 11；OD discussion; Figs.4c and5。

## 适用边界与待核问题

- 主要机动规划明确在地面执行，不能因摘要使用autonomous概述就认定这套FDS是全星载自主系统。
- p4通常将差分阻力视为扰动，p13异常运行又使用差分阻力控制，两者按工况区分。
- p10将Fig.4c误称July曲线，而图注和日期为May，July对应Fig.5；ODTK版本段落也不完全一致。保留来源冲突。
- 所述恢复时间和SEU频率是该任务报告，不外推所有CubeSat的失效率。
- 与S054/S058同一任务线，未取得原始GPS/控制日志独立验证。

## 对综述的作用

优先补3.6.3避碰—恢复—任务再采用：安全动作的次生队形偏差、推进状态和地面接触机会会决定何时能恢复原计划；提供实际运行链而非只列控制算法。

以上为阅读者的采用建议，尚未写入v3.2。完成阅读和文件核验不等于科学结论已经获认可。
