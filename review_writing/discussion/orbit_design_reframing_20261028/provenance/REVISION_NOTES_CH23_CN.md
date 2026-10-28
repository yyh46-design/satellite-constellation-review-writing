# 第二、三章整体精修记录

日期：2026-10-28。用途：作者讨论。本文档与精修稿位于论文仓库之外，既有两章讨论稿保留。

## 章节分工

第二章组织任务需求、构型自由度、演化条件、方法选择与设计评价，形成目标构型、任务容差、到位时间及控制预算要求。第三章从实际轨道状态出发，解释部署、维持、重构与安全机动如何实现这些要求。两章均包含随时间演化的设计问题，不用“静态/动态”替代职责区分。

摄动速率匹配与初始构型自由度集中在2.2，3.2仅展开偏差控制、机动时序和实际控制能力。部署在2.4承担构型评价条件，在3.1展开高度、进动、时间与发射指派。终态允许范围及任务模式恢复合并到3.3，3.4讨论安全机动及其执行状态如何进入任务接续。

## 论述与证据对应

| 精修位置 | 主要关系及取舍 | 沿用证据记录 |
|---|---|---|
| 2.1 | 任务指标影响访问总量或时间分布，轨道参数形成相应几何 | 第二章READING_SYNTHESIS_CN.md中Arnas 2021、Ko 2026；CHAPTER_CITATION_INDEX.json中的Huang、Williams Rogers、Leroy |
| 2.2 | 地固访问表示、摄动速率匹配与几何自由度，平均构型到传播评价 | 同上Schaub 2001、Arnas 2016/2021；既有Arnas与Casanova 2020和Sullivan 2017。保留模型层次，不新增普遍误差界 |
| 2.3 | 规则与子集参数化；轨道参数搜索与离散成员选择；分层目标及候选分辨率 | 同上Casanova、Ko、Jia；此前READING_MEMO_CN.md的Avendaño和Savitri；既有Lee 2020、R2 N001。Savitri采用半解析访问计算与搜索的组合关系，不另作摄动实现或数值性能主张 |
| 2.4 | 部署和维持代价、布局与转移安全、轨道机会与资源交付 | B04/B05的READING_NOTES_016.md；Huang；Jia；B12 L038 Polli；R2 N002 Pearl |
| 3.1 | 差分节点进动、到达相位与发射部署选择 | R2 N007 McGrath；B04-016-C01至03、B05-016-C01至04。跨方法连接和到达状态传递属于本文综合，不宣称文献已实现统一部署与调相求解 |
| 3.2 | 相位与漂移共同控制；推进/气动作用；姿态能源与共同参考星切换 | Arnas 2016；R2 N005、N010、N004；B19 L004 Leroy；B11 L005 Kim/Yoon、L012 S-NET。S-NET写为规划，Planet使用12星在轨结果，EO-1写为任务后单星试验 |
| 3.3 | 兼容候选、完整相对终态、脉冲与低推力参数化、指派联系、逐星预算和跨阶段状态 | B11 L017；R2 N005；B12 L022；B05-011-C01至04；B03-013-C01至06。多阶段仍为未来目标预知；没有作等计算预算性能排名 |
| 3.4 | 终态被动几何与转移安全；解析映射与序列凸化；低推力调整；共同安全 | B20 L063；B12 L062；B11 L048、L046；B17 S047。三星案例用于解释共同轨迹约束，不扩为大型星座运行验证 |

以上简写的章节材料来自：

- D:/SKT727/outputs/constellation_ch2_design_synthesis_20261027/notes/READING_SYNTHESIS_CN.md
- D:/SKT727/outputs/constellation_ch2_design_synthesis_20261027/notes/CHAPTER_CITATION_INDEX.json
- D:/SKT727/outputs/constellation_orbit_design_reading_20261027/notes/READING_MEMO_CN.md
- D:/SKT727/outputs/constellation_ch3_orbital_actions_20261028/notes/CHAPTER_EVIDENCE_MAP_CN.md
- D:/SKT727/outputs/constellation_orbit_mission_research_r2_20261027/reading_notes/
- D:/SKT727/worktrees/constellation_review_v3510_20261026/review_writing/evidence/reading_batches/

具体来源ID、论点ID、原文页码与版本条件沿用上述阅读记录。本轮是两章内容精修与组织调整，没有计为新增文献精读。

## 数值与适用条件

Ko的6星对照保留济州岛单目标、给定圆轨道重复地面轨迹及相同可见性条件：覆盖率19.73%，最长重访2304 s与6173 s。未引申为所有星数或所有参考轨道的普遍优势。

McGrath的对照保留24星、仅计J2长期项的7天覆盖比较：Cairngorms区域平均覆盖2.8→4.5 min，最长局部重访15.5→17.7 h。燃料均衡与总控制消耗、完成时间之间的取舍继续保留。覆盖指标没有改写为任务加权完成收益或端到端交付。

终态、路径和共同安全的区别继续保留；低推力恢复仍表述为相关策略中的软终端要求。R2的N006/N008保持RESERVE，既有HOLD、来源全文与图像缺口、正式版配对状态未改变。human_verified=false；submission_ready=false。

## 本轮检查

两章沿用此前32项不同来源，链接均可在前两章讨论稿中找到；没有新增引用条目或重排V3.5.10编号。文内公式维持原有近似条件，关键对照数值及单位与既有阅读记录一致。文件保存在独立输出目录。
