# [24] Orbital Facility Location Problem for Satellite Constellation Servicing Depots

中文译名：卫星星座服务仓库的轨道设施选址问题。DOI：[10.2514/1.A35691](https://doi.org/10.2514/1.A35691)。

版本：author_preprint_arxiv_2302.12191v3_2024-03-28。实际首页arXiv:2302.12191v3，28 Mar 2024；50页作者文件包含后部附录/补充表，不作正式期刊页数。作者稿Nicholas Gollins与元数据Nick Gollins姓名写法分存。

[实际阅读入口](https://arxiv.org/pdf/2302.12191)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[6, 7, 32]的相关段落；实际图页相关区域[7, 32]。PDF SHA256 `68baa4105b5210d1a407062b78cfbf3d155364deea58d9ece46fe6a5af501a6e`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-024-C01|Eq8 and perturbing-acceleration paragraph；物理页[6]|动力学接口允许推进和其他扰动加速度进入，控制方向由推进加速度决定。|接口可表达某种扰动，不证明所有案例已纳入并验证该扰动。|
|B07-024-C02|Eqs11–16；物理页[7]|Q-law用轨道要素误差、近地点罚项和权重构造目标，逐时刻选择使Q下降最快的方向。|即时下降规则不等于全程燃料、时间或含终端相位约束的全局最优证明。|
|B07-024-C03|multiclient a posteriori study; Fig13 discussion；物理页[32]|所选设施只分析每趟两或三客户的组合，将多客户任务与逐客户返库任务比较。|局部后验组合比较不能改称全星座联合选址—多趟路由最优。|
|B07-024-C04|case1 GPS/Galileo comparison；物理页[32]|组合客户的轨道分布会改变多客户服务是否省推进剂；混合GPS/Galileo访问在部分布局下可不如分次返库。|不能把访问合并普遍写成节省成本，需保留载荷携带、轨道位置和客户组合。|

服务综述：3.1.3/3.2.4：选址代价与服务路径的接口。

仍缺：未独立核全Q-law推导；作者稿终刊配对、三客户以上路由和全设施联合多客户优化保持开放。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
