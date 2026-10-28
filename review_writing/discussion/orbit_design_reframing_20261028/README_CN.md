# 轨道设计主线调整：完整中文讨论稿与写作记录

日期：2026-10-28。用途：作者讨论与后续续写。

本目录保存摘要、第一至第五章的完整中文讨论稿，以及从V3.5.10、R2到本次调整形成的研究定位、章节分工和写作判断。正文以轨道设计和动力学建模为基础，贯通星座部署、维持、安全重构与任务运行。

## 阅读入口

通读入口：[完整中文讨论稿](REVIEW_DISCUSSION_ORBIT_REFRAMED_CN.md)。最新补齐部分：[摘要](ABSTRACT_REFRAMED_CN.md)、[第一章](CHAPTER_1_REFRAMED_CN.md)、[第五章](CHAPTER_5_REFRAMED_CN.md)；写作判断与依据见[补齐记录](COMPLETION_NOTES_CN.md)。

最新调整：[已读文献选择与正文整合](LIBRARY_INTEGRATION_CN.md)。本轮从已有精读库选入6项来源，深化2项已有引用，补充第二至第四章并同步第五章。全稿现引用72项去重来源；本轮新增完整正文精读为0。

1. [第二、三章整体精修稿](CHAPTERS_2_3_REFINED_CN.md)：已补入误差传播、维持代价及安全轨道选择的联系。
2. [研究定位与讨论决策](RESEARCH_POSITIONING_AND_DECISIONS_CN.md)：保存调整原因、主线、表达原则及仍待决定的问题。
3. [整篇综述的章节框架](CHAPTER_FRAMEWORK_CN.md)：说明五章分工及旧稿内容的整合位置。
4. [第四章写作方案](CHAPTER_4_WRITING_PLAN_CN.md)：本次提出的组织建议、论证顺序与主要证据。
5. [材料与引用索引](PROVENANCE_CN.md)：连接旧稿、R2和本次补读材料。
6. [第二、三章引用位置清单](CHAPTERS_2_3_CITATION_INDEX.json)、[来源与稿件状态](SOURCE_STATUS.json)。
7. [第四章完整讨论稿](CHAPTER_4_DISCUSSION_CN.md)、[第四章文献重组与补读](../../research/chapter4_orbit_decision_20261028/README_CN.md)：完成31项已有来源归组，两轮新增正文阅读共10项，9项用于讨论稿；本轮新增3项及具体改写见[续读综合](../../research/chapter4_orbit_decision_20261028/FOLLOWUP_SYNTHESIS_CN.md)。
8. [完整稿引用索引](WHOLE_DRAFT_CITATION_INDEX.json)、[当前整合检查](LIBRARY_INTEGRATION_CHECK.json)、[当前文件清单](LIBRARY_INTEGRATION_MANIFEST.json)。此前补齐的检查与清单仍保存在COMPLETION文件中。

## 分支与基线

新分支：`writing/constellation-review-orbit-design-reframing-20261028`。

起点是R2提交`402de0c31cb2642821563f6f6288987664636f51`，tree为`3ebe8fd71e95dfba17b44b6f5e68404407ed68cc`。该提交继承V3.5.10提交`7141979de09e76c6538b05073162c6610da02cf8`，tree为`183472ae04b98eb7b4df7697c3afc7e8a1e09969`。

- [V3.5.10完整正文](../../manuscripts/v3.5.10-cn/REVIEW_CN_v3.5.10.md)
- [R2研究材料入口](../../research/orbit_mission_r2_20261027/README_CN.md)
- [R2完整讨论稿](../../research/orbit_mission_r2_20261027/REVIEW_DISCUSSION_R2_CN.md)

新版章节保存在本目录，第四章研究记录另存于`review_writing/research/chapter4_orbit_decision_20261028/`。旧稿正文及参考文献编号保持原状。

## 当前进度

| 内容 | 当前状态 |
|---|---|
| 研究重心 | 已在讨论中明确：轨道设计与建模贯通运行决策，初始星座构型进入核心范围 |
| 第二、三章 | 已形成整体精修讨论稿，并从旧库补入3项来源、深化构型维持分析 |
| 摘要、第一章 | 已按轨道设计与建模主线补齐讨论稿；引言保留四行定位表 |
| 第四章 | 已完成文献归组、两轮定向补读及精修；本轮从旧库补入3项来源并深化CMAS规划接口 |
| 第五章 | 已同步本轮认识，并加入前文7项来源支撑相应结论 |
| 题目、正式引文顺序、英文摘要与图件 | 后续统一处理 |

`human_verified=false`；`submission_ready=false`；中文正文尚未冻结。

## 保存检查

[初次存档清单](ARCHIVE_MANIFEST.json)记录第二、三章复制文件的原位置与SHA-256。[初次检查结果](SAVE_CHECK.json)记录当时的存档一致性；初次保存不计新增精读。后续第四章两轮共10项正文阅读、出处及检查见[补读记录](../../research/chapter4_orbit_decision_20261028/README_CN.md)，不与初次存档或R2历史计数混合。

摘要、第一章和第五章的初次补齐，以及后续已读文献整合，均复用现有阅读材料，不新增完整正文阅读计数。历史清单对应各自保存提交；当前合并稿及本轮新增、更新文件以[整合清单](LIBRARY_INTEGRATION_MANIFEST.json)为准。
