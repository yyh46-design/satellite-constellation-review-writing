# [91] Autonomous Trajectory Planning for Rendezvous and Proximity Operations by Conic Optimization

中文译名：采用锥优化的交会与近距离操作自主轨迹规划。DOI：[ 10.2514/1.58436 ](https://doi.org/10.2514/1.58436)。

版本：author_manuscript_public_HTML_26page_layout。入口：[实际阅读来源](https://www.researchgate.net/publication/268557803_Autonomous_Trajectory_Planning_for_Rendezvous_and_Proximity_Operations_by_Conic_Optimization)。HTML作者稿26页布局，正式刊页375–389；不可混用两个页码系统。

本轮类别：new_targeted_HTML。新增定向核读记录，非整篇逐证明完成。

阅读范围：公开HTML工具快照行 [[917, 984], [2817, 2905], [3161, 3340], [4681, 4907], [5300, 5412], [5612, 5676]]；没有PDF页码、文件哈希或像素核验。

|ID|原文定位|观察|使用边界|
|---|---|---|---|
|B05-091-C01|HTML L917–984, Assumption1/Lemma1；页不适用|无损结论带有指向约束、活动弧及状态约束等条件。|没有完成全部引理证明审核，不能泛化为任意RPO无损。|
|B05-091-C02|HTML L2817–2905; L3161–3189, successive procedure；页不适用|逐次更新后再解线性时变动力学的锥约束问题。|每个SOCP与原非线性问题的保证须分别说明。|
|B05-091-C03|HTML L4681–4907, discretization；页不适用|梯形离散在网格施加约束，指定中间时刻须纳入网格。|本轮未独立验证离散误差及连续时间满足性。|
|B05-091-C04|HTML L5300–5344; L5612–5645, numerics；页不适用|秒级以下计时指固定迭代的MOSEK子问题；2000–3000秒是接近段任务时长。|不能混作整个规划的总CPU或千星在线实证。|

服务综述：3.4.2及4.4：分开无损松弛、逐次解、离散化与求解器保证。

仍缺：公开HTML作者版26页布局，正式刊页375–389不能用于此副本定位。无PDF，公式像素和全部证明未核。

作者归纳与原文观察分列；候选位置只供后续修订，不表示原段已整体核验。下载/HTML可见/渲染均不计为自动精读完成。`human_verified=false`；正式版配对、全部证明与独立实验未关闭。
