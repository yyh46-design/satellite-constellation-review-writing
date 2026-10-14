# 星座管理综述 B01：已有作者原文定向精读

执行日期：2026-10-14（Asia/Shanghai）。本轮依据“现在继续帮我推进精读一下吧”推进B00已取得的六篇作者侧原文：[42][44][53][74][76][121]。冻结正文仍为`51be6a1326e8c615ea24f80f1887f16a2e7b02fc`，B00基线为`08ec6a7ccd3673461698d52aa099b6740f2bcd1f`，本地分支为`research/constellation-review-reading-b01-20261014`。

## 本轮完成到什么程度

完成6篇**与v1.9论证有关的模型—方法—实验—限制定向核读**，建立42条命题记录、42条既有引文位置索引，实际视检30个PDF页面（含[121]接受稿四页）。所读7个PDF哈希与B00相同；论文、提取文字和页面图仅存本机独立资料目录，仓库只新增本批中文笔记与元数据。

|计量|本轮结果|
|---|---:|
|完成指定范围作者版本核读|6篇|
|全篇逐页/逐证明精读完成|0篇|
|新取得正式全文|0篇|
|正式版逐命题对照关闭|0/6|
|[121]作者稿选页配对|4对规范化文字相同；全篇未完成|
|人工作者终核/实验复现|0/0|

上述“6篇”不代表读完每篇每页及全部附录，也不代表正式版本或投稿证据闭环。准确阅读范围和页面哈希见[READING_SCOPE_B01.json](READING_SCOPE_B01.json)。全部human_verified=false，full_paper_close_read_completed=false，formal_version_parity_closed=false。

## 对当前综述最有用的发现

1. **[44]图缩减也有保留可行结构的条件。** 重叠任务分组不当可能丢失可行执行顺序；v1.9已经提示模型简化风险，但L280对图变换的概括需加条件。工作稿引用的Appendix A/B没有在当前31页文件中检出正文，证明材料也未齐。
2. **[53]应按时域区分反馈。** 当前处理优化不修改已定采集，却允许质量失败目标进入下一轮；这支持“顺序输入、下游局部联合、跨轮质量反馈可以并存”。平均处理时延约束不能写成每帧硬保证。
3. **公平指标及计算成本不宜混用。** [74]采用满意度比的Jain指数，[76]采用队列年龄极差；[74]成本比较只覆盖选束，[76]的2ms是仿真步长。
4. **[121]性能与计算分析配置要分别引用。** 主性能设置裁边阈值100，成本分析段另取1；outage为时延超QoS门槛，且门槛随建链时延变化。四页作者版本匹配不等于IEEE正式版一致。

v1.9对六篇的主要目标和算法概括大体有依据。本轮建议以局部条件补充为主，不靠增加公式和逐篇摘要扩充篇幅。详见[横向比较与工程融入](CROSS_STUDY_COMPARISON.md)、[八条修改候选](V19_CHANGE_CANDIDATES.md)。候选尚未写入正文。

## 逐篇阅读

|来源|英文原标题与中文译名|主要用途|本轮笔记|
|---|---|---|---|
|[42]|Joint Observation and Transmission Scheduling in Agile Satellite Networks<br>敏捷卫星网络中的联合观测与传输调度|共同完成条件与分层求解|[精读笔记](READING_NOTES_042.md)|
|[44]|The integrated agile Earth observation satellite scheduling problem<br>集成敏捷对地观测卫星调度问题|完成指标、图/模型简化和邻域|[精读笔记](READING_NOTES_044.md)|
|[53]|Edge Intelligence for Satellite‐Based Earth Observation: Scheduling Image Acquisition and Processing<br>卫星对地观测边缘智能：图像采集与处理调度|顺序、局部联合与质量反馈|[精读笔记](READING_NOTES_053.md)|
|[74]|Joint Beam Scheduling and Power Optimization for Beam Hopping LEO Satellite Systems<br>波束跳变低轨卫星系统的联合波束调度与功率优化|选束/连续功率和比较控制|[精读笔记](READING_NOTES_074.md)|
|[76]|Demand-Aware Beam Hopping and Power Allocation for Load Balancing in Digital Twin Empowered LEO Satellite Networks<br>数字孪生赋能低轨卫星网络中面向负载均衡的需求感知波束跳变与功率分配|DT多星选束、局部功率、队列指标|[精读笔记](READING_NOTES_076.md)|
|[121]|On-Demand Routing in LEO Mega-Constellations With Dynamic Laser Inter-Satellite Links<br>具有动态激光星间链路的低轨巨型星座按需路由|更新代价、路径保持与成本口径|[精读笔记](READING_NOTES_121.md)|

## 可检查的证据文件

- [SOURCE_MANIFEST_B01.json](SOURCE_MANIFEST_B01.json)：六篇题名、作者、DOI、版本、原文URL、7份PDF哈希；出版信息继承B00，不冒充本轮重新核元数据。
- [CLAIM_CHECKS_B01.json](CLAIM_CHECKS_B01.json)：42个命题、原页/节/式/图表定位、正文块、支持及条件判断；状态统计为`{"supported_in_read_author_version": 22, "qualification_needed": 14, "unresolved_material_gap": 1, "source_internal_inconsistency": 3, "unresolved_metric_ambiguity": 1, "limited_author_pair_match": 1}`。
- [V19_DEPENDENCY_CHECK_INDEX.csv](V19_DEPENDENCY_CHECK_INDEX.csv)：42条六篇引文位置映射。只链接相关子命题，不把含其他来源/综述综合的整个段落标成已验证。
- [PAIR_121_AUTHOR_VERSIONS.json](PAIR_121_AUTHOR_VERSIONS.json)：四对作者页规范化比较与未核范围。
- [OPEN_ITEMS_B01.md](OPEN_ITEMS_B01.md)、[OPEN_ITEM_STATUS_B01.json](OPEN_ITEM_STATUS_B01.json)：正式稿、附录、指标与参数缺口，原27项不自动关闭。
- [SHA256_MANIFEST.json](SHA256_MANIFEST.json)：本批记录文件逐字节哈希与路径集合，自身列路径但不递归自哈希。

## 保存与停止

本轮只在`review_writing/evidence/reading_batches/B01_20261014/`新增记录。冻结正文、编号、v1.9历史核验、B00及其他目录保持原样。本地记录核对通过后停止；本批尚未推送GitHub，不进入B02、整稿重写、PR/合并或实验复现。
