# [109] Mission Operations of Earth Observing-1 with Onboard Autonomy

中文译名：具备星上自主能力的Earth Observing-1任务运行  
DOI：[10.1109/SMC-IT.2006.48](https://doi.org/10.1109/SMC-IT.2006.48)

本记录为B02面向v1.9写作的定向正文核读。AI辅助整理，human_verified=false；全篇逐页/逐证明完成=false；正式版配对闭合=false。

## 来源、版本与实际范围

- 正文/来源入口：https://ntrs.nasa.gov/citations/20060050174
- 版本：`author_conference_manuscript_local_existing`。既有7页作者会议稿，题名和正文身份与NTRS/目标DOI匹配；定制字体使两种文字提取均乱码，因此通过实际页面逐页视觉阅读。Crossref作者合并字段不完整；按实际首页另记11位作者，不覆盖历史书目。
- 正式元数据作者快照：Daniel Tran Gregg Rabideau。
- 期刊/会议：2nd IEEE International Conference on Space Mission Challenges for Information Technology (SMC-IT'06)；卷 未编定/未给出，期 未给出，页/文章号 367-373。精确日期见[SOURCE_MANIFEST_B02.json](SOURCE_MANIFEST_B02.json)。
- 所读副本：7个物理页；本地文件字节数 382021；SHA256 `0295832b32c21c80eede34b4f878e6df809410fcd6cc4e94a7fcdaa3a5e5fe43`。
- 正文相关段落页：文字抽取不可用，使用全部实际页面视觉阅读；实际视检页：1, 2, 3, 4, 5, 6, 7。
- 文字质量：`unusable_custom_font_encoding_visual_reading_used`。

7个实际物理页全部视觉阅读，包括架构图、运行前后流程表与结果/限制；没有做OCR或逐命令实现验证，不能等同人工终核/正式版本配对。

页码均为所读副本的物理页，从1开始；[95]有两页封面，论文页=物理页−2。列出一页不表示整页所有段落、公式或图表均已核完。

## 问题、方法、对照及可引用边界

实际首页可见作者（用于后续书目核对，未覆盖历史条目）：Gregg Rabideau; Daniel Tran; Steve Chien; Benjamin Cichy; Rob Sherwood; Dan Mandl; Stuart Frye; Seth Shulman; Joseph Szwaczkowski; Darrell Boyer; Jim Van Gaasbeck。

### B02-109-C01｜物理页1,2,3；science/CASPER/SCL architecture

星上科学分析可产生新目标，CASPER作约束规划/修复，SCL执行并做命令约束与启动/完成检查，再由科学处理反馈。

引用边界：这是有角色分工与检查的工程闭环，不是一个学习器直接输出全部控制命令。

对应v1.9候选位置：行258,318。跨论文迁移位置是拟议用途，不表示该行整段已经由此一篇证实。

### B02-109-C02｜物理页3,4,5；Figs.2–3; Table 1

改进流程仍使用地面ASPEN规划优先级、通信与星历，星上CASPER/SCL负责目标到执行；Table 1以14步对比旧/新流程。

引用边界：“自主”不表示地面规划、上行、人员与飞行动力学职责被取消。

对应v1.9候选位置：行258,318。跨论文迁移位置是拟议用途，不表示该行整段已经由此一篇证实。

### B02-109-C03｜物理页5,6；ephemeris and flight dynamics updates

文中星历及相关飞行动力学参数仍每日由地面更新；一周尺度的进一步自治是后续依赖资源条件的扩展。

引用边界：不能将周级完全脱离地面的自主运行当作此文已实现事实。

对应v1.9候选位置：行258,318。跨论文迁移位置是拟议用途，不表示该行整段已经由此一篇证实。

### B02-109-C04｜物理页6；resource assumptions

每次成像后回到nadir、轮偏置/卸载活动等简化有助预计算与参数复用，但可能增加非最优活动。

引用边界：复用的工程收益依赖运行规程；不能直接当作精细资源优化的最优解。

对应v1.9候选位置：行258,318。跨论文迁移位置是拟议用途，不表示该行整段已经由此一篇证实。

### B02-109-C05｜物理页6；last-minute observation requests

文中最后时刻请求仍要求距过境至少约120分钟，以容纳上行、重规划和准备。

引用边界：不能改写成任意紧急任务秒级自主响应。

对应v1.9候选位置：行258,318。跨论文迁移位置是拟议用途，不表示该行整段已经由此一篇证实。

### B02-109-C06｜物理页6；operational experience and cost

论文报告地面站异常/接触变更下的恢复经验以及任务总年度成本由约3.6M降至1.6M美元，并将其中超过1M美元归于ASE自动化。

引用边界：这是地面与星上整体流程的作者报告前后比较，无受控单模块因果识别；综述优先采用机制说明，不直接套给星座收益。

对应v1.9候选位置：行258,318。跨论文迁移位置是拟议用途，不表示该行整段已经由此一篇证实。

## 对本综述的作用

3.5.3与4.4表7的具体工程说明：科学事件触发目标变化、地面ASPEN与星上CASPER分工、SCL检查及反馈；用运行流程解释闭环而非罗列AI模块。

## 未关闭项

需正式出版副本与NTRS附件版本配对，11位作者与正式书目核对；地面/星上整体改变的成本归因没有受控消融，不能归功单个算法。

第三方原文、提取全文和页面图保留在本机独立资料目录；仓库只记录元数据、原创阅读笔记、来源链接与校验信息。
