# 已读文献的选择与正文整合

日期：2026-10-28。承接提交：`589138bd210c7f84777a9a90444ad90e00ca07d5`。

本次根据[上一轮增强安排](LITERATURE_AND_CONTENT_ENHANCEMENT_CN.md)，核对与当前缺口相关的旧库精读笔记，并回看所选来源的原文段落。新增进入本讨论稿的来源为6项，全部来自已有精读库；另深化2项已经引用的来源。本次不计新增完整正文精读，不改变旧库的版本、全文取得或HOLD/RESERVE状态。

## 1. 本次补出的联系

正文继续围绕“任务需求—轨道构型与动力学模型—部署、维持与安全重构—任务资源协同与执行反馈”展开。补充内容分别回答：误差怎样影响构型容差，任务容差怎样形成维持代价，控制中断和机动后轨道要求怎样改变轨迹选择，以及轨道方案怎样分层求解并随执行修正。每项研究进入其所支撑的物理关系或方法比较。

| 新进入本稿的来源 | 位置与论述作用 | 既有精读依据与本次原文回看 |
|---|---|---|
| Ben-Yaacov等，2016，Covariance analysis of differential drag-based satellite cluster flight | 2.2：连接名义几何、估计误差与任务容差；解释相对误差为何需要星间交叉协方差 | [E-B19-L015](../../evidence/reading_batches/B19_20261021/READING_L015_CN.md)，C-B19-016—020；回看正文第6–7物理页的增广误差状态、滤波更新与相对协方差。沿用已取得的正文文本快照，未新增PDF图像核读 |
| Guffanti与D’Amico，2022，Robust Passively Safe Spacecraft Swarming via Closed-form and Optimization-based Control Approaches | 3.4、5：将控制中断后的自由漂移纳入构型和转移选择，联系解析安全条件与数值优化 | [E-B13-S007](../../evidence/reading_batches/B13_20261020/READING_S007_CN.md)，C-B13-026—029；回看第2–4物理页的积分常数、非可积漂移及误差裕量。按双星实例说明机制 |
| Pavanello等，2024预印本，Long-Term Fuel-Optimal Collision Avoidance Maneuvers with Station-Keeping Constraints | 3.4、5：以维持约束引起机动方向和代价变化为例，区分全程轨道范围与软终端恢复要求 | [E-B12-L047](../../evidence/reading_batches/B12_20261020/READING_L047_CN.md)，C-B12-018—023；回看第19、29–30物理页。沿用arXiv:2307.06004v2及其GEO比较条件，不新增跨模型燃料排名 |
| Pedari等，2026预印本，A Hierarchical Control Architecture for Optimal Guidance and Navigation of Satellite Formations | 4.2：连接目标构型、成员指派、个体轨迹与执行反馈，说明层间传递终态和实际状态的作用 | [E-B13-S010](../../evidence/reading_batches/B13_20261020/READING_S010_CN.md)，C-B13-039—043；回看第7、18、21、35物理页。保留同构卫星、姿态与平移解耦，以及可靠性在终态评价的条件；未将文件名作为正式发表证明 |
| Botelho等，2026，Robust Model Predictive Control for Rendezvous with Relative Orbital Elements and System Level Synthesis | 4.3、5：区分执行中的状态反馈与重新优化，比较反馈预设计、名义轨迹更新和全方案更新 | [E-B15-S029](../../evidence/reading_batches/B15_20261020/READING_S029_CN.md)，C-B15-037—041；回看第19–20物理页及既有模型笔记。保留线性模型、准确状态反馈和有界过程扰动条件 |
| Scala等，2026，所读接受稿，Motion Planning Strategies for Safety Procedure of Multisatellite Formation-Flying Systems | 4.4：说明失推后的自然运动如何改变恢复终态，联系科学基线与安全待命几何 | [E-B18-S051](../../evidence/reading_batches/B18_20261021/READING_S051_CN.md)，C-B18-001—005；回看第29–31物理页。保留三星仿真、及时故障通报；安全转移结果与后续业务接续设想分别表述 |

上述本次回看均为定向复核，不记为重新完成六篇全文精读。源文件仍位于既有本地材料目录，本目录未复制第三方全文。

## 2. 已有来源的进一步利用

**Arnas等，2021：从构型参数化推进到维持代价。** 2.4利用原文第6节及[第二章精读记录](provenance/chapter2/READING_SYNTHESIS_CN.md)，补入任务容差、气动特性、地方时、太阳活动和机动可用时段的联系。这使初始轨道设计的比较能够延伸到持续运行条件。模型中的载荷与平台参照、太阳活动情景和地影机动安排均按设计研究使用，不作为新星座在轨结果。

**Mascolo等，2025：从执行反馈推进到规划接口。** 4.1利用[CMAS精读记录](../../research/orbit_mission_r2_20261027/reading_notes/N003_CMAS_CN.md)，补出轨道范围、机动机会、占空比和受保护时段怎样参与候选机动选择；4.4继续讨论计划、执行或取消后怎样更新成像。这两处分别说明动作形成与执行后的修正，不将其写成完整轨道—能源—存储联合优化验证。

第五章同步加入与结论直接对应的7项引用，全部已在前文使用。摘要与第一章保持原文；本次补充细化既有主线，不另设新主题。

## 3. 本次暂不加入的材料

| 材料 | 取舍原因 |
|---|---|
| Henry等，2023，安全事件筛选 | 主要解释接近事件分类，不能直接回答轨道动作的协调范围；当前不以事件数量替代轨迹耦合问题 |
| Karim等，2024，GEO开关推力MILP-MPC | 既有笔记保留公式与实现口径问题；当前有限控制讨论已有直接来源，不以其补成未经核实的联合模型 |
| Pavanello等，多接近避碰，arXiv:2406.03654v1 | 多事件机动有后续使用价值，本次先补维持、被动安全和反馈三条联系；风险表达仍按原笔记保留，未纳入本次原文复核及新增引用 |
| R2的N006、N008 | 沿用RESERVE，不因正文需要而改变采用状态 |
| Fang IAC 2025、FAST-CoOpt、Xu 2024、Guo等线索 | 尚未取得或完成所需正文精读；不计入本次可用证据或新增引用 |

## 4. 仍值得优先补读的问题

1. **初始构型与长期运行代价（2.4）**：在可比较的任务要求下，部署时长、摄动漂移、维持容差和平台能力怎样改变构型选择。已有Arnas分析可以深化这一联系，仍需要更直接的多方案取舍研究。
2. **部署顺序与阶段任务能力（3.1）**：同一目标构型采用不同注入、展开或调相顺序时，首批能力与完整能力分别何时形成。现有两项部署来源尚不足以充分比较这一问题。
3. **有限时长机动与任务资源共同安排（4.1）**：机动期间姿态、能源和载荷占用怎样影响观测及数据交付，并反过来改变轨迹或机动时机。McGrath、Pearl、Rossi和CMAS提供互补联系，新增材料应补它们之间的具体接口。

后续再按论点需要补充大型星座的轨道协调范围，以及从同一处置后状态比较多条业务接续路径的研究。当前不优先扩大通用学习算法或工程项目清单。

## 5. 保存与计数

当前正文按来源链接去重为72项，较本轮前增加6项；这些是进入本稿的新增引用，完整正文精读新增数为0。第一至第五章分别引用14、18、20、35、7项，章节之间有重复，不能直接相加；第二至第四章合计68项。

按此前“正文中作为运行案例展开的实际任务或系统”口径，仍为7组工程案例、9项支撑来源。本次新增的方法仿真不另计工程案例；上述9项来源包含在72项中。

当前文件与引用一致性见[整合检查](LIBRARY_INTEGRATION_CHECK.json)和[文件清单](LIBRARY_INTEGRATION_MANIFEST.json)。此前的COMPLETION、ARCHIVE及SAVE记录继续对应各自历史提交。原V3.5.10、R2及精读记录保持原状；`human_verified=false`，`submission_ready=false`，中文正文未冻结。
