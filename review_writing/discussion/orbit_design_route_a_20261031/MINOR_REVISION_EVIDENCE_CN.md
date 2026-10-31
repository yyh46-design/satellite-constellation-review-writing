# 三项小修：定点来源依据

以下原编号指审阅基线d3fba9a，新编号指本轮正文。只记录本轮所需的来源角色与措辞判断，不构成全面文献复审。

## Mortari 2006（原[10]，新[12]）

- [ESA原始PDF](https://www.esa.int/gsp/ACT/doc/ACTAFUTURA/AF02/papers/AF02.2006.7.pdf)；沿用本地16页文件，SHA-256：`7695fe2221d2ddd895911948fe3f34f0b7769e2f71eeb33bd939e829b11270d5`。
- 复核物理页1—2的摘要与引言、既有页3—6的理论结构。摘要开头说明其用途是总结Flower构型的研究成果和进展；正文按Compatible orbits、Flower Constellation Phasing、Secondary Paths等主题展开。
- 判断：兼具理论阐述与进展总结，不能仅凭摘要一句话把它等同于横向比较多个构型家族的领域综述，也不能反过来宣称它毫无综述性质。
- 采用：表1称“构型理论代表研究”；1.2同时保留理论阐述和进展总结两种作用。未改变其理论内容和文献身份。

## Walker 1970（新[10]）

- 题名：Circular Orbit Patterns Providing Continuous Whole Earth Coverage。
- 作者：J. G. Walker；机构：Royal Aircraft Establishment；报告号：70211；地点：Farnborough；年份：1970。
- [National Aerospace Library原始报告馆藏](https://raes.soutron.net/Portal/Default/en-GB/RecordView/Index/176168)确认日期1970-11-01、报告号和作者；[英国气象局馆藏](https://library.metoffice.gov.uk/Portal/Default/en-GB/RecordView/Index/180138)独立确认题名、机构、年份与报告号。
- DTIC公开PDF返回403，Internet Archive副本入口返回503；未取得原报告全文。1971年的JBIS文章是另一书目条目，本稿没有把其卷页与1970报告合并。
- 使用范围：历史出处；不提取原报告覆盖数值，不计为新增正文精读。

## Lüders 1961（新[11]）

- 题名：Satellite Networks for Continuous Zonal Coverage。
- 作者：R. David Lüders；ARS Journal，1961年2月，31(2):179–184；[DOI](https://doi.org/10.2514/8.5422)。
- [出版商提交的Crossref记录](https://api.crossref.org/works/10.2514/8.5422)确认作者、题名、卷期、页码和日期；原始JSON保存在`minor_revision_metadata/LUDERS_1961_CROSSREF.json`。
- 出版社PDF及ADS入口返回403，未取得原始全文。
- 使用范围：覆盖带方法的历史出处；不采用原始数值或未读公式，不计为新增正文精读。

## 构型机制的实际阅读依据

[Huang、Colombo、Bernelli-Zazzera，2021](https://re.public.polimi.it/bitstream/11311/1181091/1/HUANS01-21.pdf)，原[11]、新[13]。本轮重新核对出版社排版正文第151—153页的引言与方法入口，以及第169页参考文献。该文明确区分Walker的规则布局与Street-of-Coverage的连续覆盖条带，分别追溯Walker 1970系列研究和Lüders 1961。正文中的构型解释沿用这项已精读研究；新增两项经典出处补齐历史定位，不冒充全文核对。

## 组织信号与资源瓶颈的既有证据

- He（原[47]、新[49]）和Rossi（[7]）：观测数据、容量与交付窗口进入任务模型；Rossi既有阅读记录C4-N02-03、04已明确带宽敏感性与基线搜索差异。
- Lee多阶段（原[37]、新[39]）：逐星机动预算贯穿阶段，支持考察剩余预算与后续转移代价的关系；本文未由此定义预算比例阈值。
- Dunlap（[9]）：共同状态下仍可能出现约束冲突或找不到共同可行输入，支持检查跨星控制依赖；没有从该实验推导通用安全阈值。
- Pedari与Mascolo：层间终态、机动时段和实际状态的传递，支持把接口内容与更新周期作为构造分层方案的依据。接口充分性仍需在反馈求解中评价。

以上信号由本综述综合提出，保持“可先检查”的用途；排序稳定性和普遍阈值没有被改写为原论文已经证明的结果。新增数值、独立物理仿真和求解器实验均为0。
