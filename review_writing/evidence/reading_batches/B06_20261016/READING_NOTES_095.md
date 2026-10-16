# [95] Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit

中文译名：近直线晕轨道被动安全交会的连续时间逐次凸化。DOI：[10.2514/6.2026-2446](https://doi.org/10.2514/6.2026-2446)。

版本：MERL_technical_report_author_conference_version。MERL TR2026-016，21个物理页含两页封面，论文页=物理页−2；官方MERL条目关联AIAA DOI。不是已配对确认的AIAA正式出版副本。

[实际阅读入口](https://www.merl.com/publications/docs/TR2026-016.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[8, 10, 14, 15, 16, 17, 18]的相关段落；实际图页复核[8, 14]的相关区域。PDF SHA256 `f681f504b8c59f20d81988246e4c55cd97c5f12414600d4fe369b53ba9553625`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-095-C01|Eq15–17, integral constraints；物理页[8]|连续路径约束转为积分等式，但为处理LICQ问题，求解时用正容差不等式。|理想连续等式、数值积分和最终容差须分层，不能称严格零误差证书。|
|B06-095-C02|linearized Gaussian moments and feedback；物理页[10]|高斯初始/执行误差经线性化传播均值协方差，再用反馈限制离散状态离散度。|分布近似和反馈前提不能省略，不是任意误差下同一风险界。|
|B06-095-C03|Table1/2,1000-sample MC；物理页[14, 15]|1000样本中被动安全违反0%，接近锥违反0.5%；beta设0.8且原文解释其保守性。|0次观测不等于零风险；设计概率不等于经验成功率，两个约束也不能合并。|
|B06-095-C04|underburn and comparison limits；物理页[14, 18]|原文明确不保证、也未评价underburn安全；不同研究初态差异妨碍直接燃耗比较。|“passively-safe”不能代称全部执行器失效安全；不做跨文献燃耗排名。|

服务综述：3.4.2及4.4：连续约束、数值容差与被动安全的具体故障情形。

仍缺：MERL报告非已配对AIAA终刊；全部附录、概率界、数值积分/独立轨迹验证未完成；underburn安全未获验证。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
