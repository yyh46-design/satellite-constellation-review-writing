# [65] Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations

中文译名：面向可扩展对地观测卫星星座运行的单智能体强化学习。DOI：[10.2514/1.A35736](https://doi.org/10.2514/1.A35736)。

版本：publisher_typeset_copy_hosted_on_faculty_site。19页公开教师主页文件具最终JSR期刊版式、61(1):114–132和DOI；在线2023、卷期2024分别保留。

[实际阅读入口](https://hanspeterschaub.info/PapersPrivate/Herrmann2024.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[7, 11, 17]的相关段落；实际图页复核[7, 11, 17]的相关区域。PDF SHA256 `84ec30992797d7ce9d0661dc53534413631561226eccad20a85dfe3fee7ff510`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-065-C01|shield and communication models；物理页[7]|安全动作可替代策略输出；通信模型从无共享到全局目标列表，多跳LOS设近乎无限交链带宽。|系统安全不能全部归给神经策略；通信理想化须随结论保留。|
|B06-065-C02|target-distribution comparison；物理页[11]|集中分配用前看1目标的网络，分散分配用前看3目标的网络，各有不同目标列表和共享条件。|不宜解释成仅改变集中/分散一个变量的同条件消融。|
|B06-065-C03|MIP timing；物理页[11]|所报MIP求解时间以访问区间已预计算为前提。|单次分配时间不包含全部轨道可见性预处理。|
|B06-065-C04|GA comparison and RL training；物理页[17]|GA比较只有四星；给出64核运行预算，RL生成网络另需约1–2天。|离线训练与后续推理应分账；“可泛化任意初态”为作者表述，不是本批独立证实。|

服务综述：3.2.3及4.1/4.3：安全屏蔽、通信假设与完整学习成本。

仍缺：本轮定位训练/GA预算与MIP计时范围，但B02全部计时/超参数/正式配对问题不自动关闭；未复现屏蔽与动力学。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
