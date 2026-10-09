# 2026-10-09：书目身份与证据边界定向修订

本文件记录本轮**针对既有审计问题的修订**，不宣称148条候选文献均已全文验证。历史Excel不改动，当前可用记录以本分支Markdown和CSV为准。

| ID | 本轮性质 | 来源位置与核对结论 | 正文中的用法限制 |
| --- | --- | --- | --- |
| O09 | 原文局部核查／修订 | [Springer正式全文](https://link.springer.com/article/10.1007/s40295-025-00487-6) §2假设A.1：忽略相位成本，仅五个轨道根数转移 | 不能写成完整六维交会与连续安全已验证；数值场景为MEO–GEO附近20客户 |
| O10 | 原文局部核查／修订 | [Springer正式全文](https://link.springer.com/article/10.1007/s40295-026-00580-4) §3假设2忽略主模型相位成本，§6.5.2/Fig.14后续作解析相位成本估计 | 区分“主优化中纳入”和“解后估计”；两者不可混写 |
| O75 | 书目身份问题已解决 | [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/9373338)：IEEE Access 9 (2021), 39985–39994；2021-03-09，DOI 10.1109/ACCESS.2021.3064928 | 官方书目信息已确认，不等于详细技术试验已完成全文核查 |
| O92 | 版本对应已确认 | [arXiv v4](https://arxiv.org/abs/2601.06188v4)标题、Comments和关联DOI：原题AAMAS 2026扩展摘要，2026-08-01 v4改题并增补内容 | 会议摘要与新版长稿的技术结论不得混用；FAME不是据此确认的飞行验证 |
| O97 | 原文局部核查／边界保留 | [Springer §3.1](https://link.springer.com/article/10.1007/s12567-025-00651-6)的RaspTank rover故障导航演示 | rover验证不能写成在轨卫星FDIR验证 |
| O99 | 原文局部核查／边界保留 | [Springer §4.2–4.3](https://link.springer.com/article/10.1007/s10270-026-01426-1)明确工具链试验与专家评价的有效性范围 | 不是大型星座规模性或真实飞行效果验证 |
| O111 | 已有正确边界保留，不提升等级 | [Remote Sensing原文入口](https://www.mdpi.com/2072-4292/15/6/1577)：单颗敏捷卫星多子系统耦合；主库原已标注“单星证据” | 不可将单星调度实验证明为跨星座闭环，完整技术精读待做 |
| O112 | 正式出版身份、摘要已核／状态修订 | [Wiley正式期刊](https://onlinelibrary.wiley.com/doi/10.1002/sat.70082)：2026-08-24首次发表；摘要涉及观测/处理耦合与YOLOv8平台执行时间实验 | 不能由正式摘要推出整星座在轨验证，期刊全文与[预印本](https://arxiv.org/abs/2604.05937)差异待查 |

## 修改和保留范围

- **本轮更新**：`evidence/MAPPING_BY_SECTION.md`、`evidence/literature_evidence_mapping_148.csv`、`literature/literature_index_148.csv`、`literature/references_148.bib`（O75）、`evidence/FIRST_READING_QUEUE_40.md`、`README.md`。
- **本轮未改**：文献主键、148个DOI和主用章节映射；六份Excel历史快照及其清单SHA-256；O111已经正确标注的单星证据边界。
- **仍需开展**：实际用于正文的代表研究全文方法与实验核查、跨版本结果对照、每个比较判断所依赖的原文页码/图表、作者人工逐条复核。
- **书目核查与技术论证分离**：DOI、出版页码、作者、年份核对完成只证明身份匹配，不使技术结论自动通过。
