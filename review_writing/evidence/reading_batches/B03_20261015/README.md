# B03：面向大型星座管理综述的15篇定向精读与归纳

执行日期：2026-10-15（Asia/Shanghai）。本批完成15篇不同学术来源的模型、方法、实验和限制等相关段落核读，形成90条带页码的命题记录，并实际视觉复核32个PDF页面。目的在于增强现有五章综述的比较论证，保持当前写作粒度，不开展整稿改写或实验复现。

## 本批结果与计数口径

- 本批15篇均为累计定向核读集合中的新增论文；累计从35增至**50篇定向正文核读**，另有5篇局部正文接触，共55篇学术来源具有正文接触记录。
- 15个本机完整PDF均已核大小、物理页数和SHA256。其中5个为正式排版副本，10个为已识别版本的作者稿。DOI匹配不表示作者稿与正式版内容已相同。
- 90条记录分别说明观察、引用边界、原文定位和正文候选位置；16行显式引用依赖逐行绑定冻结稿哈希。
- “定向精读”不表示所有页、附录、推导或代码均已完成；本批全篇逐页/逐证明完成声明为0，正式版配对关闭为0，所有human_verified=false。
- 学术来源111篇的派生划分：50定向、5局部、5缺正文、51尚未充分确认；10项工程/标准材料沿用历史状态。总书目仍121条。

## 最值得用于写作的结论

1. [24]已有固定分配后的连续位置细化，与[25]的区别应落实到联合变量与访问线路，不能只写离散/连续。
2. Kodan[58]已把处理选择关联到高价值数据下传，可作为价值映射正例，同时保留硬件测量与仿真范围。
3. [25]部分结果只统计成功求解实例；[20][21]共享基准；[47]的启发式收益受实例结构影响。综述应同时交代统计分母、预算与基线信息。
4. DSN[50]适合说明候选、协商和承诺的区别；[49]数值优化与[50]历史部署不能拼接成同一算法的部署证明。

上述结论均为本批归纳，具体原文边界见对应笔记和命题表。正文候选尚未采用。

## 阅读清单

|编号|英文原标题 / 中文译名|DOI|实际所读副本|笔记|
|---|---|---|---|---|
|[12]|Regional Constellation Reconfiguration Problem: Integer Linear Programming Formulation and Lagrangian Heuristic Method<br>区域星座重构问题：整数线性规划建模与拉格朗日启发式方法|[10.2514/1.A35685](https://doi.org/10.2514/1.A35685)|[作者稿（版本已识别）](https://arxiv.org/pdf/2206.02910)|[记录](READING_NOTES_012.md)|
|[13]|Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods<br>基于整数规划与序贯决策方法的确定性多阶段星座重构|[10.2514/1.A35990](https://doi.org/10.2514/1.A35990)|[作者稿（版本已识别）](https://arxiv.org/pdf/2401.11567)|[记录](READING_NOTES_013.md)|
|[14]|Satellite Constellation Pattern Optimization for Complex Regional Coverage<br>面向复杂区域覆盖的卫星星座模式优化|[10.2514/1.A34657](https://doi.org/10.2514/1.A34657)|[作者稿（版本已识别）](https://arxiv.org/pdf/1910.00672v4)|[记录](READING_NOTES_014.md)|
|[20]|Spare Strategy Analysis and Design for Mega Satellite Constellations Using Markov Chain<br>基于马尔可夫链的巨型卫星星座备星策略分析与设计|[10.2514/1.A36599](https://doi.org/10.2514/1.A36599)|[作者稿（版本已识别）](https://arxiv.org/pdf/2509.09957)|[记录](READING_NOTES_020.md)|
|[21]|Spare strategy for large-scale satellite constellations under dual resupply channels using Markov chain<br>双补给通道下基于马尔可夫链的大规模卫星星座备星策略|[10.1016/j.actaastro.2026.06.020](https://doi.org/10.1016/j.actaastro.2026.06.020)|[作者稿（版本已识别）](https://arxiv.org/pdf/2605.20875v2)|[记录](READING_NOTES_021.md)|
|[24]|Orbital Facility Location Problem for Satellite Constellation Servicing Depots<br>卫星星座服务仓库的轨道设施选址问题|[10.2514/1.A35691](https://doi.org/10.2514/1.A35691)|[作者稿（版本已识别）](https://arxiv.org/pdf/2302.12191)|[记录](READING_NOTES_024.md)|
|[25]|Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers<br>考虑低推力转移的卫星星座服务轨道仓库选址优化|[10.2514/1.A36386](https://doi.org/10.2514/1.A36386)|[作者稿（版本已识别）](https://arxiv.org/pdf/2502.15914)|[记录](READING_NOTES_025.md)|
|[36]|Scheduling of Earth observing satellites using distributed constraint optimization<br>基于分布式约束优化的对地观测卫星调度|[10.1007/s10951-024-00816-x](https://doi.org/10.1007/s10951-024-00816-x)|[正式排版副本](https://link.springer.com/content/pdf/10.1007/s10951-024-00816-x.pdf)|[记录](READING_NOTES_036.md)|
|[41]|Asynchronous Communication Aware Multi-Agent Task Allocation<br>考虑异步通信的多智能体任务分配|[10.24963/ijcai.2023/30](https://doi.org/10.24963/ijcai.2023/30)|[正式排版副本](https://www.ijcai.org/proceedings/2023/0030.pdf)|[记录](READING_NOTES_041.md)|
|[47]|Scheduling Space–Ground Communications for the Air Force Satellite Control Network<br>空军卫星控制网络的天地通信调度|[10.1023/B:JOSH.0000013053.32600.3c](https://doi.org/10.1023/B:JOSH.0000013053.32600.3c)|[作者稿（版本已识别）](https://www.cs.colostate.edu/~howe/papers/JOS04.pdf)|[记录](READING_NOTES_047.md)|
|[48]|Satellite downlink scheduling problem: A case study<br>卫星下传调度问题：案例研究|[10.1016/j.omega.2015.01.001](https://doi.org/10.1016/j.omega.2015.01.001)|[作者稿（版本已识别）](https://repository.essex.ac.uk/17381/1/1206.5503v3.pdf)|[记录](READING_NOTES_048.md)|
|[49]|Deep Space Network Scheduling via Mixed-Integer Linear Programming<br>基于混合整数线性规划的深空网络调度|[10.1109/ACCESS.2021.3064928](https://doi.org/10.1109/ACCESS.2021.3064928)|[作者稿（版本已识别）](https://www.columbia.edu/~rm3122/paper/deep_space.pdf)|[记录](READING_NOTES_049.md)|
|[50]|Automated Scheduling for NASA's Deep Space Network<br>NASA深空网络的自动化调度|[10.1609/aimag.v35i4.2552](https://doi.org/10.1609/aimag.v35i4.2552)|[正式排版副本](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2552/2452)|[记录](READING_NOTES_050.md)|
|[58]|Kodan: Addressing the Computational Bottleneck in Space<br>Kodan：缓解空间计算瓶颈|[10.1145/3582016.3582043](https://doi.org/10.1145/3582016.3582043)|[正式排版副本](https://www.microsoft.com/en-us/research/uploads/prod/2023/08/asplosc23main-p858-p-224936cdce-68637-final.pdf)|[记录](READING_NOTES_058.md)|
|[116]|Basilisk: A Flexible, Scalable and Modular Astrodynamics Simulation Framework<br>Basilisk：灵活、可扩展的模块化航天动力学仿真框架|[10.2514/1.I010762](https://doi.org/10.2514/1.I010762)|[正式排版副本](https://www.hanspeterschaub.info/PapersPrivate/Kenneally2020a.pdf)|[记录](READING_NOTES_116.md)|

页码指实际副本物理页；[116]为12页文章加1页cited-by附页，后者不计正文。[20]为2026年9月后续作者更新稿。[21]正式元数据刷新遇429，其正式DOI与出版串沿用冻结记录；实际读到的是已识别的arXiv v2。

## 归纳与复用入口

|文件|用途|
|---|---|
|[CROSS_STUDY_SYNTHESIS.md](CROSS_STUDY_SYNTHESIS.md)|七组跨论文比较、引用边界及正文取舍|
|[V19_CHANGE_CANDIDATES.md](V19_CHANGE_CANDIDATES.md)|候选调整表及三段可审阅文字，未应用正文|
|[ENGINEERING_CASE_DSN.md](ENGINEERING_CASE_DSN.md)|DSN工程案例融入方案，分清来源事实与作者归纳|
|[COMPARISON_MATRIX.csv](COMPARISON_MATRIX.csv)|15篇的规模单位、指标和比较条件|
|[CLAIM_CHECKS_B03.json](CLAIM_CHECKS_B03.json)|90条命题及原文页码、版本、哈希、正文位置|
|[V19_DEPENDENCY_CHECK_INDEX.csv](V19_DEPENDENCY_CHECK_INDEX.csv)|冻结正文16行显式引用依赖及哈希|
|[SOURCE_MANIFEST_B03.json](SOURCE_MANIFEST_B03.json)|英文题名、中文译名、DOI、作者/出版元数据及副本信息|
|[SOURCE_ACCESS_REGISTER.csv](SOURCE_ACCESS_REGISTER.csv)|15篇访问与版本状态|
|[READING_SCOPE_B03.json](READING_SCOPE_B03.json)|段落及实际视觉复核页，避免把渲染当阅读|
|[CUMULATIVE_READING_STATUS.md](CUMULATIVE_READING_STATUS.md)|累计数量与去重口径；JSON保存编号集合|
|[OPEN_ITEMS_B03.md](OPEN_ITEMS_B03.md)|全部未关闭项说明；JSON保留前批各项|
|[ACCESS_OBSERVATIONS.json](ACCESS_OBSERVATIONS.json)|访问限制、替换候选及普通传输记录|
|[VERIFICATION_B03.json](VERIFICATION_B03.json)|结构、引用定位、历史文件与来源哈希核验|
|[SHA256_MANIFEST.json](SHA256_MANIFEST.json)|本批全部提交文件除清单自身的SHA256|

## 尚未关闭的事项

新增六组：B03-META-21正式元数据刷新；B03-PROB-41丢包概率符号；B03-MODEL-49作者稿约束与假设对应；10篇作者稿正式版对照；剩余阅读/实验范围；候选文字作者审阅。具体关闭条件见未决项文件。

历史27项、B01新增5项、B02分组7项全部保留。缺正文[75][77][79][80][112]，旧正式版、页面、作者身份/日期及指标核验等仍未自动关闭。[10]正式/机构入口403、[37]MIT下载429后停止，本批替换为原书目[14][24]，不计失败候选为已读，不绕过限制。

## 冻结与本地留痕

冻结稿基准：`51be6a1326e8c615ea24f80f1887f16a2e7b02fc`。本批父提交：`40d9796ef116c5ca067278b16f5fece672e90f42`（B02）。独立本地分支：`research/constellation-review-reading-b03-20261015`。

仅新增本目录；v1.9、历史稿件、参考编号及前批台账保持原样。第三方PDF、抽取文字和页面图均在独立资料目录`D:\SKT727\materials\constellation_review_B03_20261015`，不提交Git。外部`B03_LOCAL_COMMIT_RECEIPT.json`记录最终commit、tree及清单自身哈希，避免自指哈希。

本轮指令为继续阅读、归纳和留痕，沿用前批本地独立提交方式；未再次push、未创建PR或合并。完成B03后停止，不自动开始B04。所有结果需作者终核，不能直接视为投稿完成状态。
