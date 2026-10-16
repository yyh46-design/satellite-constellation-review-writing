# [102] Knowledge-based satellite failure detection, isolation and recovery (FDIR)

中文译名：基于知识的卫星故障检测、隔离与恢复。DOI：[10.1007/s12567-025-00651-6](https://doi.org/10.1007/s12567-025-00651-6)。

版本：publisher_VOR_Springer_OA_modified_publication2026。14页CEAS18(2026):991–1004；首页Published online28July2025、modified publication2026。未据此猜测修改内容或与旧版等同。

[实际阅读入口](https://link.springer.com/content/pdf/10.1007/s12567-025-00651-6.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[4, 8, 11, 12]的相关段落；实际图页复核[4, 11, 12]的相关区域。PDF SHA256 `a5a6ab8a7c4edb752066de7fc35eec30c1fa3a5ecfb878afe7bdfa9dd71e7f03`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-102-C01|three modules and mission-specific service；物理页[4]|PERCEPTION导出故障事实，FDIR选动作并处理互斥，ACTION执行；规则文件经服务装载/重启并可保存环境。|观测、决策与执行有明确接口，更新失败需告警；不是任意学习权重在线安全更新。|
|B06-102-C02|success/failure checks；物理页[8]|漫游车清障动作后检查成功/失败，失败再避障，成功后回NAVIGATING交给GNC。|恢复包括结果确认和模式移交，不只是发出一条动作命令。|
|B06-102-C03|hardware/results；物理页[11]|RaspberryPi4、约30参数、10Hz案例分别报告事实创建<1.5ms与规则执行<2.5ms。|不同分项不能改称全任务最坏时延；代表性飞行硬件和完整配置测量仍待完成。|
|B06-102-C04|scale and observability limits；物理页[11, 12]|大数据池事实注入可能成瓶颈；跨规则依赖增多会降低可读性，内部时序事实仍需遥测表示。|可解释规则语法不自动解决大规模维护、运算和运行可观测性。|

服务综述：3.4.3及4.3/4.4：诊断—动作—确认、规则更新和验证平台。

仍缺：新取得14页正式副本首页modified publication2026，旧版内容差异未核。飞行硬件、完整FDIR规则、持续时间/最坏耗时与全部规则依赖未复现。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
