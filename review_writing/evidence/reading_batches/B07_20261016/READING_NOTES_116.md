# [116] Basilisk: A Flexible, Scalable and Modular Astrodynamics Simulation Framework

中文译名：Basilisk：灵活、可扩展的模块化航天动力学仿真框架。DOI：[10.2514/1.I010762](https://doi.org/10.2514/1.I010762)。

版本：publisher_typeset_copy_plus_cited_by_appendage。教师主页13物理页文件中p1–12为正式JAIS 17(9):496–507论文，p13是附加cited-by列表，不能当论文多一页。

[实际阅读入口](https://www.hanspeterschaub.info/PapersPrivate/Kenneally2020a.pdf)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[6, 8, 9]的相关段落；实际图页相关区域[6, 8, 9]。PDF SHA256 `be2b914e7e438dadfb05b1f5d38bc584c191bce9da0f8fcb9ddb6236bc157c56`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-116-C01|state and dynamic effectors；物理页[6]|带内部积分状态的StateEffector与产生外力/力矩的DynamicEffector接口分开，由动力学管理器聚合。|模块可组合不自动证明动力学耦合和数值积分已正确验证。|
|B07-116-C02|execution control; data logging；物理页[6]|执行遵循任务组/任务/模块优先级并允许不同更新率；日志频率受生产数据任务限制，不为更高记录频率插值。|仿真调度和观测采样是独立配置，日志更密不能补回未生成的状态信息。|
|B07-116-C03|prose versus Listing6 and Fig7；物理页[8, 9]|第8页文字给动力学0.1秒、传感器0.5秒；Listing6用0.01/0.1秒，Fig7对应100/10Hz，另有FSW2Hz。|实际页确认不一致，尚未确定作者意图；后续复现必须明确选用配置，不能在综述给唯一确定周期。|
|B07-116-C04|SimpleNav paragraph；物理页[8]|示例导航输出由真实状态加Gauss–Markov误差生成，用于替代更复杂导航系统。|这种输入不等于已跑完整测定轨链或实际星载导航输入。|
|B07-116-C05|FSW modules and events；物理页[9]|C实现的飞软模块支持仿真到SWIL/未来HWIL复用，事件回调可改Python接口暴露的状态。|复用和注入能力不是某个整星座故障场景已完成验证，更不保证所有故障都被现实地建模。|

服务综述：3.5.3/4.4：仿真接口、采样周期和状态可观测性。

仍缺：原文示例文字、代码、图的采样周期不一致未关闭；13页副本最后为cited-by附页非正文；本轮未运行软件/硬件在环。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
