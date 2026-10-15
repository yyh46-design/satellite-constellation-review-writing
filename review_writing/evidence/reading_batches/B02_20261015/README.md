# B02：15篇面向综述写作的定向正文核读

**本轮已为15篇建立正文核读记录、90条命题检查、37页实际页面视检，并对应v1.9的35处显式引用。累计35篇定向正文核读，另5篇局部正文接触。** 这是对写作用命题的定向精读，不声称本轮15篇已全篇逐页/逐证明完成；正式版配对关闭0，人工作者终核0。

日期：2026-10-15（Asia/Shanghai）。父提交：`cfda3fb7560e3aa2b89452593d8e59a4c7f06d5b`；中文稿冻结基准：`51be6a1326e8c615ea24f80f1887f16a2e7b02fc`。本批独立本地分支：`research/constellation-review-reading-b02-20261015`。只增加本目录，不改历史稿件、台账或编号；不创建PR/合并，不自动进入下一批。最新指令未要求本轮push，故先作可审阅的本地提交。

## 为什么选择这15篇

按冻结五章稿的实际论证选择，不为凑篇数用摘要替代正文：能力/维护/服务接口4篇[17][23][27][28]，观测分配与学习协同2篇[34][65]，安全与健康分析5篇[84][85][87][95][98]，自主工程与验证4篇[108][109][117][120]。其中[34][65][98]由历史局部接触升级，其余12篇由尚未充分确认进入定向核读。

|编号|英文原标题及中文译名（点击进入逐篇笔记）|DOI|所读版本|
|---|---|---|---|
|[17]|[Joint satellite platform and constellation sizing for instantaneous beam-hopping in 5G/6G Non-Terrestrial Networks](READING_NOTES_017.md)<br>面向5G/6G非地面网络瞬时跳波束的卫星平台与星座联合规模设计|[10.1016/j.comnet.2024.110942](https://doi.org/10.1016/j.comnet.2024.110942)|正式排版副本|
|[23]|[On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation](READING_NOTES_023.md)<br>融合在轨服务的卫星星座维护策略|[10.2514/1.A36684](https://doi.org/10.2514/1.A36684)|作者稿/技术报告|
|[27]|[Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties](READING_NOTES_027.md)<br>需求不确定条件下在轨服务运行建模与优化框架|[10.2514/1.A34978](https://doi.org/10.2514/1.A34978)|作者稿/技术报告|
|[28]|[On-Orbit Servicing Optimization Framework with High- and Low-Thrust Propulsion Tradeoff](READING_NOTES_028.md)<br>考虑高低推力推进权衡的在轨服务优化框架|[10.2514/1.A35094](https://doi.org/10.2514/1.A35094)|作者稿/技术报告|
|[34]|[Decentralized Observation Allocation for a Large-Scale Constellation](READING_NOTES_034.md)<br>面向大型星座的分散式观测分配|[10.2514/1.I011215](https://doi.org/10.2514/1.I011215)|正式排版副本|
|[65]|[Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations](READING_NOTES_065.md)<br>面向可扩展对地观测卫星星座运行的单智能体强化学习|[10.2514/1.A35736](https://doi.org/10.2514/1.A35736)|正式排版副本|
|[84]|[Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques](READING_NOTES_084.md)<br>接近筛查方法性能评估及基于CUDA的接近分析计算提速|[10.3390/aerospace10060543](https://doi.org/10.3390/aerospace10060543)|正式排版副本|
|[85]|[Simulation of satellites and constellations for the assessment of collision avoidance operations](READING_NOTES_085.md)<br>用于碰撞规避运行评估的卫星与星座仿真|[10.1007/s12567-022-00471-y](https://doi.org/10.1007/s12567-022-00471-y)|正式PDF远端文字；本地/像素缺|
|[87]|[Spacecraft collision avoidance challenge: Design and results of a machine learning competition](READING_NOTES_087.md)<br>航天器碰撞规避挑战：机器学习竞赛的设计与结果|[10.1007/s42064-021-0101-5](https://doi.org/10.1007/s42064-021-0101-5)|作者稿/技术报告|
|[95]|[Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit](READING_NOTES_095.md)<br>近直线晕轨道被动安全交会的连续时间逐次凸化|[10.2514/6.2026-2446](https://doi.org/10.2514/6.2026-2446)|作者稿/技术报告|
|[98]|[Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding](READING_NOTES_098.md)<br>基于LSTM与非参数动态阈值的航天器异常检测|[10.1145/3219819.3219845](https://doi.org/10.1145/3219819.3219845)|作者稿/技术报告|
|[108]|[Remote Agent: to boldly go where no AI system has gone before](READING_NOTES_108.md)<br>Remote Agent：迈向人工智能系统尚未涉足之境|[10.1016/S0004-3702(98)00068-X](https://doi.org/10.1016/S0004-3702(98)00068-X)|作者稿/技术报告|
|[109]|[Mission Operations of Earth Observing-1 with Onboard Autonomy](READING_NOTES_109.md)<br>具备星上自主能力的Earth Observing-1任务运行|[10.1109/SMC-IT.2006.48](https://doi.org/10.1109/SMC-IT.2006.48)|作者稿/技术报告|
|[117]|[Formal Methods for Trusted Space Autonomy: Boon or Bane?](READING_NOTES_117.md)<br>可信空间自主的形式化方法：福音还是负担？|[10.1007/978-3-031-06773-0_1](https://doi.org/10.1007/978-3-031-06773-0_1)|作者稿/技术报告|
|[120]|[Model checking of spacecraft operational designs: a scalability analysis](READING_NOTES_120.md)<br>航天器运行设计的模型检验：可扩展性分析|[10.1007/s10270-025-01281-6](https://doi.org/10.1007/s10270-025-01281-6)|正式排版副本|

中文均为工作译名；正式元数据与所读副本身份分别保存，不以DOI匹配代替正式全文核验。[23]预印本题名与正式题名有冠词差异，[109]元数据作者字段不完整等例外见笔记。

## 对当前写作最有用的发现

1. [85]应放在“接近事件/评估场景生成”，原文不足以支撑L209中已分析避让主体与时机的说法。
2. [23]补到了作者v2方法正文，库存订货满足率不等于用户中断时长；[27][28]需保留需求揭示、轨迹可行域与求解预算。
3. [34][65]可按已完成状态、意图、更新时间和重复活动共同分析，而非只比较通信多少或求解速度。
4. [84][87][98]的收益必须归到实际变化的环节：筛查/硬件、风险回归/分类、固定预测器下的阈值/剪枝。
5. [108][109]适合说明闭环职责；[117][120]适合说明验证对象及边界，不能用单器案例或软件性质代替星座交付验证。

上述均为证据记录或候选写法，未自动应用到正文。跨文综合是综述分析，不冒充原论文已验证的联合系统。

## 先看哪些文件

- [跨文综合与写作取舍](CROSS_STUDY_SYNTHESIS.md)：按接口、信息、分析对象和验证对象组织。
- [工程案例如何融入](ENGINEERING_CASE_INTEGRATION.md)：EO-1实际分工表及可用候选段落。
- [v1.9局部修改候选](V19_CHANGE_CANDIDATES.md)：12组候选、优先级和三段效果示例。
- [累计计数说明](CUMULATIVE_READING_STATUS.md)：20→35；去重后40篇有正文接触。
- [未关闭项](OPEN_ITEMS_B02.md)：旧27项及B01发现全部保留，新增问题逐项列明。
- [来源访问表](SOURCE_ACCESS_REGISTER.csv)、[来源哈希/版本](SOURCE_MANIFEST_B02.json)、[实际阅读范围](READING_SCOPE_B02.json)、[90条命题](CLAIM_CHECKS_B02.json)、[正文引用定位](V19_DEPENDENCY_CHECK_INDEX.csv)。

## 材料与证据边界

14篇有本地完整有效PDF及SHA，另[85]是远端正式PDF文字可读，本地TLS/连接失败且实际图页像素未见，大小/SHA留空。[109]文字抽取不可用，已逐页视觉阅读7页；[108]改用PDFium较可读文字；[84]所用表页实际像素已核，避免混合文字层误读。渲染成功、下载成功和索引存在均不直接计为核读。

正式排版/正式远端正文6篇，作者稿/技术报告9篇。后者全部保留正式版本对照缺口。37页实际视检只是本批已检页，不是全体图表已完成。没有进行实验复现、全证明独立核验或人工作者终核。

第三方PDF、全文提取和图页均保留本机 `D:\SKT727\materials\constellation_review_B02_20261015`，仓库只存原创笔记、元数据、来源URL和哈希。访问过程见[ACCESS_OBSERVATIONS.json](ACCESS_OBSERVATIONS.json)；错误的[117]索引候选已排除。未绕过付费墙、403、验证码或TLS验证。

所有本批文件及SHA见[SHA256_MANIFEST.json](SHA256_MANIFEST.json)。清单不包含自身，避免自指哈希；清单自身哈希与最终commit/tree保存在本机外部发布回执。历史Git对象与工作区换行的核对见[VERIFICATION_B02.json](VERIFICATION_B02.json)。
