# B04：大型星座管理综述的15篇定向精读与归纳

执行日期：2026-10-15，Asia/Shanghai。本批围绕既有五章综述的实际命题，完成15篇来源中模型、方法、对照、结果与限制的相关正文核读，保存90条定位记录，并实际复核32页相关图表/公式/文字区域。没有开展整稿重写或实验复现。

## 结果与计数

- 选定15篇：[2][5][7][8][16][19][26][30][39][57][61][62][72][86][92]。五篇综述、十篇研究论文；[86]还含其作者的受限数值比较。
- 累计定向核读从50增至**65篇**。其中[5][72]由局部接触升级，本批新增不同正文接触13篇；另3篇局部，共**68篇学术来源有正文接触记录**。不是68篇全文逐页/逐证明完成。
- 14个完整本地PDF均核页数、大小、SHA256；8正式排版副本、5作者稿、1出版社待终排PDF。[26]仅公开HTML正文可读，PDF与缺失公式/图页仍未取得。
- 90条命题、22行冻结稿显式引用依赖、15篇笔记和比较表均已记录来源身份与引用限制；10篇取得Crossref快照，另5篇按实际PDF/出版社信息记录，未填造缺失卷期。
- 全篇逐页逐证明完成声明0，正式版配对闭合0，作者人工终核0；全部human_verified=false。学术来源111篇=65定向+3局部+5缺正文+38沿用/未充分确认，另10项工程/标准保持历史状态，书目仍121条。

## 对写作最有用的归纳

1. 不确定性先区分未知对象、信息揭示时刻与调整权限：[61]收益集合保守性、[62]两阶段质量评价和三阶段改排并非同一种能力。
2. 完成指标需说明事件和分母：[57]成功不等于业务按期，[19]库存满足不等于业务即时恢复；[30]算法比较还受实际问题限制。
3. 规模、最优性和计时都需保留条件：[16]潜在覆盖代理与实际选集不同，[72]分钟级序列搜索前有小时级预计算，[92]每次平均求解与整次轨迹计时不可混用。
4. 安全结论有适用条件：[92]的通信、误差、计算期限与连续安全条件应随结论引用；[86]受限CAM比较没有覆盖非标称鲁棒性或工程全链时延。
5. 已有综述能支撑紧凑五章写法；本文贡献宜落在跨问题的决策联系和比较条件，避免只以类别覆盖多宣称新意。

详细命题边界见笔记和[跨文献归纳](CROSS_STUDY_SYNTHESIS.md)。这些是AI辅助的初步分析，不等于作者终核。

## 本批清单

中文论文[7][8]列中文原标题与出版社英文译名；其他论文列正式英文题名及中文译名，所读版本差别另记。[19]所读预印本题名含Optimal，正式题名不含。

|编号|英文题名 / 中文译名或原标题|DOI|所读版本|笔记|
|---|---|---|---|---|
|[2]|Space Logistics Modeling and Optimization: Review of the State of the Art<br>空间物流建模与优化：研究现状综述|[10.2514/1.A35982](https://doi.org/10.2514/1.A35982)|[已识别作者稿](https://arxiv.org/pdf/2306.01107)|[记录](READING_NOTES_002.md)|
|[5]|Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges<br>分布式空间系统与任务管理的基于智能体方法：方法论、实践现状与挑战|[10.1016/j.actaastro.2025.10.018](https://doi.org/10.1016/j.actaastro.2025.10.018)|[正式排版副本](https://digital.library.adelaide.edu.au/server/api/core/bitstreams/482432e4-b0a1-48de-aefb-979a0fc69ca5/content)|[记录](READING_NOTES_005.md)|
|[7]|A Survey of Intelligent Networking Technologies for LEO Mega-Constellations<br>低轨巨型星座智能组网技术综述|[10.7527/S1000-6893.2026.32935](https://doi.org/10.7527/S1000-6893.2026.32935)|[出版社待终排PDF](https://hkxb.buaa.edu.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=21249)|[记录](READING_NOTES_007.md)|
|[8]|Review on Resource Management and Optimization Technologies for LEO Communication Satellite Constellation Networks<br>低轨通信卫星星座网络资源管控与优化技术综述|[10.3873/j.issn.1000-1328.2026.02.002](https://doi.org/10.3873/j.issn.1000-1328.2026.02.002)|[正式排版副本](https://www.spacejournal.cn/yhxb/cn/article/pdf/preview/10.3873/j.issn.1000-1328.2026.02.002.pdf)|[记录](READING_NOTES_008.md)|
|[16]|Two-Stage Framework for Deployment-Aware Optimization of Satellite Constellation Pattern Design<br>面向部署的卫星星座构型优化两阶段框架|[10.1007/s42405-026-01298-1](https://doi.org/10.1007/s42405-026-01298-1)|[正式排版副本](https://link.springer.com/content/pdf/10.1007/s42405-026-01298-1.pdf)|[记录](READING_NOTES_016.md)|
|[19]|Replenishment Strategy for Satellite Constellation with Dual Supply Modes<br>具有双供应模式的卫星星座补给策略|[10.2514/1.A36281](https://doi.org/10.2514/1.A36281)|[已识别作者稿](https://arxiv.org/pdf/2408.09696)|[记录](READING_NOTES_019.md)|
|[26]|Deployment of On-Orbit Service Vehicles Using a Fuzzy Adaptive Particle Swarm Optimization Algorithm<br>采用模糊自适应粒子群算法的在轨服务飞行器部署|[10.1155/2021/6644339](https://doi.org/10.1155/2021/6644339)|[出版社HTML；PDF缺](https://onlinelibrary.wiley.com/doi/10.1155/2021/6644339)|[记录](READING_NOTES_026.md)|
|[30]|Selecting and scheduling observations of agile satellites<br>敏捷卫星观测的选择与调度|[10.1016/S1270-9638(02)01173-2](https://doi.org/10.1016/S1270-9638(02)01173-2)|[正式排版副本](https://www2.cs.sfu.ca/CourseCentral/827/havens/papers/topic%2312%28SatelliteScheduling%29/lemaitre-2002.pdf)|[记录](READING_NOTES_030.md)|
|[39]|Distributed cooperative task planning algorithm for multiple satellites in delayed communication environment<br>时延通信环境下的多卫星分布式协同任务规划算法|[10.1109/JSEE.2016.00066](https://doi.org/10.1109/JSEE.2016.00066)|[正式排版副本](https://www.jseepub.com/CN/article/downloadArticleFile.do?attachType=PDF&id=5650)|[记录](READING_NOTES_039.md)|
|[57]|Orbit-aware task scheduling in satellite edge computing<br>卫星边缘计算中的轨道感知任务调度|[10.1007/s10586-025-05663-9](https://doi.org/10.1007/s10586-025-05663-9)|[正式排版副本](https://link.springer.com/content/pdf/10.1007/s10586-025-05663-9.pdf)|[记录](READING_NOTES_057.md)|
|[61]|Robust Earth Observation Satellite Scheduling With Uncertainty of Cloud Coverage<br>考虑云覆盖不确定性的鲁棒对地观测卫星调度|[10.1109/TAES.2019.2947978](https://doi.org/10.1109/TAES.2019.2947978)|[已识别作者稿](https://drive.google.com/uc?export=download&id=1ZWAE-hwLsw2lb1-6BrzXHcVYRNGIDMJe)|[记录](READING_NOTES_061.md)|
|[62]|Mixed-integer programming models for optimal constellation scheduling given cloud cover uncertainty<br>考虑云覆盖不确定性的最优星座调度混合整数规划模型|[10.1016/j.ejor.2018.11.043](https://doi.org/10.1016/j.ejor.2018.11.043)|[已识别作者稿](https://www.osti.gov/servlets/purl/1524209)|[记录](READING_NOTES_062.md)|
|[72]|Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations<br>存在摄动时低推力服务卫星的最优多客户轨迹规划|[10.1007/s40295-025-00487-6](https://doi.org/10.1007/s40295-025-00487-6)|[正式排版副本](https://link.springer.com/content/pdf/10.1007/s40295-025-00487-6.pdf)|[记录](READING_NOTES_072.md)|
|[86]|CAMmary: A review of spacecraft collision avoidance manoeuvre design methods<br>CAMmary：航天器避碰机动设计方法综述|[10.1016/j.actaastro.2025.07.027](https://doi.org/10.1016/j.actaastro.2025.07.027)|[已识别作者稿](https://arxiv.org/pdf/2503.22555)|[记录](READING_NOTES_086.md)|
|[92]|Model Predictive Control of Swarms of Spacecraft Using Sequential Convex Programming<br>采用序列凸规划的航天器集群模型预测控制|[10.2514/1.G000218](https://doi.org/10.2514/1.G000218)|[正式排版副本](https://caltech.app.box.com/shared/static/xb19dc8ih9su97894omrmh8k44tfko1u.pdf)|[记录](READING_NOTES_092.md)|

## 建议阅读顺序与文件

先看[CROSS_STUDY_SYNTHESIS.md](CROSS_STUDY_SYNTHESIS.md)与[V19_CHANGE_CANDIDATES.md](V19_CHANGE_CANDIDATES.md)，再按需看[REVIEW_POSITIONING.md](REVIEW_POSITIONING.md)、[COMPARISON_MATRIX.csv](COMPARISON_MATRIX.csv)及逐篇笔记。

来源/版本/访问：[SOURCE_ACCESS_REGISTER.csv](SOURCE_ACCESS_REGISTER.csv)、[SOURCE_MANIFEST_B04.json](SOURCE_MANIFEST_B04.json)、[VERSION_COMPARISON_QUEUE.json](VERSION_COMPARISON_QUEUE.json)、[ACCESS_OBSERVATIONS.json](ACCESS_OBSERVATIONS.json)。

命题/实际范围：[CLAIM_CHECKS_B04.json](CLAIM_CHECKS_B04.json)、[READING_SCOPE_B04.json](READING_SCOPE_B04.json)、[V19_DEPENDENCY_CHECK_INDEX.csv](V19_DEPENDENCY_CHECK_INDEX.csv)。HTML定位与PDF物理页分别保存，不为[26]填造页码或PDF哈希。

去重统计：[CUMULATIVE_READING_STATUS.md](CUMULATIVE_READING_STATUS.md)、[CUMULATIVE_READING_STATUS.json](CUMULATIVE_READING_STATUS.json)、[CUMULATIVE_DERIVED_LEDGER_121.json](CUMULATIVE_DERIVED_LEDGER_121.json)。

未决与校验：[OPEN_ITEMS_B04.md](OPEN_ITEMS_B04.md)、[OPEN_ITEM_STATUS_B04.json](OPEN_ITEM_STATUS_B04.json)、[VERIFICATION_B04.json](VERIFICATION_B04.json)、[SHA256_MANIFEST.json](SHA256_MANIFEST.json)。历史未关闭项全部保留，没有自动关闭。

## 本批主要未关闭项

[7]终排年份/卷期：实际图页确认DOI末尾1是上标脚注，不能误报DOI冲突，但页眉和引用栏仍矛盾。[16]同构型部署时间概括与表7/8局部行不同；[26]PDF、缺失公式/图页及具体分配一致性；[57]指标分母与优先级标签需作者审阅。5篇作者稿与正式版尚未配对；其余已读范围之外的推导/代码也未独立复核。

原缺正文[75][77][79][80][112]、原图页[73][107][96]、B02[85]本机图页及前批正式版/附录/指标/代码未决继续保留。详见OPEN_ITEMS及原记录，不能用本批数量增长视为旧问题关闭。

## 留痕与停止边界

从B03本地提交`e98d3a60d917cb9f478d4bb364f9d5214cf37e17`建立独立分支`research/constellation-review-reading-b04-20261015`，本批只新增本目录。v1.9仍以`51be6a1326e8c615ea24f80f1887f16a2e7b02fc`为冻结基准。正文Git字节SHA256为`0b9f3f6f6b8d3c13af97f25d7baf3dac6dc18ecad8614e182633e12b6e3bbc69`。

PDF、正文提取、工具快照、页面图和辅助脚本在`D:\SKT727\materials\constellation_review_B04_20261015`独立资料目录，未纳入Git。仓库仅保存可分享元数据、原创阅读记录、原文URL和校验信息，临时签名URL不保存。

本轮只完成阅读、总结、候选与本地Git留痕；未push、未创建PR或合并，未修改历史稿、编号或旧台账。完成后停止，不自动开始B05。校验清单不包含自身哈希，最终commit/tree及清单自身SHA在外部提交回执保存，避免循环自引用。
