# [72] Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations

中文译名：存在摄动时低推力服务卫星的最优多客户轨迹规划。DOI：[10.1007/s40295-025-00487-6](https://doi.org/10.1007/s40295-025-00487-6)。

版本：publisher_VOR_Springer_OA。The Journal of the Astronautical Sciences72:7(2025)，38页正式排版；公开服务器常规字节范围续传后PDF完整、可解析。

[实际阅读入口](https://link.springer.com/content/pdf/10.1007/s40295-025-00487-6.pdf)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[10, 11, 12, 25]的相关段落；实际图页相关区域[11, 12]。PDF SHA256 `4c33ba12334a19d142e50684472aa81ad21f9b24448c92e5fabf918aa122b160`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-072-C01|Q-law; Eqs10–13；物理页[10, 11]|Q-law逐时刻选方向，最短时构造采用最大推力；燃料模式另以效能阈值引入滑行弧。|近优反馈生成不能改写成已求解全约束全局最优轨迹。|
|B07-072-C02|effectivity paragraph；物理页[11]|效能计算中的整轨极值没有闭式表达，需数值过程，例如网格搜索。|闭式控制方向不等于完整代价构造没有数值预处理成本。|
|B07-072-C03|explicit ToF limitation；物理页[12]|原文明确不能预先指定Q-law飞行时间，ToF与耗燃由权重、终止准则和效能阈值产生。|若任务要求硬到达时刻，必须另查时间可达性；不能任意指定插值弧的时长。|
|B07-072-C04|perturbed feedback; time/fuel histories；物理页[12, 25]|控制律维持开普勒形式，但在摄动传播的瞬时要素上反馈；最小燃料案例含滑行并延长总时长。|动力学传播与控制律推导层次不同；图例不证明全部摄动域和终端相位已满足。|

服务综述：3.2.4/4.1：轨迹代价来源、时间自由度和复核条件。

仍缺：未独立证明Q-law最优性或完成全部扰动轨迹核验；相位、插值与原始代码问题继承。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
