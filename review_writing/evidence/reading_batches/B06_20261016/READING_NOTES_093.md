# [93] Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation

中文译名：带扰动估计的航天器交会机会约束模型预测控制。DOI：[10.1016/j.conengprac.2011.09.006](https://doi.org/10.1016/j.conengprac.2011.09.006)。

版本：publisher_typeset_personal_copy_on_author_website。13物理页含Elsevier封面+Control Engineering Practice20(2012):111–122正式排版个人副本。

[实际阅读入口](https://aero.us.es/rvazquez/papers/CEP-2012.pdf)；本轮类别：new_targeted_from_inherited。新增定向记录，不表示全篇逐证明完成。

阅读范围：物理页[2, 3, 6, 7, 8, 9, 10, 12, 13]的相关段落；实际图页复核[6, 9, 10]的相关区域。PDF SHA256 `28fe0c42f83135e4d420b01f3bd3a4010459c39ede2937dfac7550f5406ccb2f`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-093-C01|HCW model; Section4.1/4.2；物理页[3, 7, 8]|设计采用HCW加性扰动，仿真用非线性相对动力学并另测偏心轨道；失准扰动还与控制输入相关。|是对特定失配的仿真检验，不是任意非线性扰动下理论保证。|
|B06-093-C02|Eq36–46, chance constraint reformulation；物理页[6, 7]|以高斯均值协方差和卡方椭球构造裕量，p为扰动集合的概率设计参数。|不能把单个集合的p直接写成整次任务独立认证的成功概率；联合风险尚未审完。|
|B06-093-C03|Section3.5, Eq47–52；物理页[7]|用模型残差、指数遗忘递推更新均值和协方差，不必保存全部历史。|推断分布参数与分布已知不同；非高斯性和估计误差的校准未独立验证。|
|B06-093-C04|Table1, Monte Carlo1220cases；物理页[9]|在1220个所设场景中，鲁棒控制未报告约束违反，均到达0.2m内；非鲁棒结果较差。|有限样本全成功不等于零风险证明；必须保留生成范围和控制器参数。|
|B06-093-C05|Table1; Figs7/8；物理页[9, 10]|表1的平均成本按各自成功子集统计，图8另只比较两法均成功的任务。|二者分母不同，不能直接用表中均值替代配对节省比例。|
|B06-093-C06|mission durations/arrival plots；物理页[9, 10, 12]|图中数千秒为交会飞行时间，表1成本单位为m/s控制代价。|不能当CPU求解耗时或货币成本；本轮没有取得总决策预算证明。|

服务综述：3.4.2及4.4：概率设计参数、有限仿真、成功分母与实际误差。

仍缺：13物理页含Elsevier封面+12正式刊页；全部推导和联合/全程风险、估计置信度、求解CPU和硬件未独立核验。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
