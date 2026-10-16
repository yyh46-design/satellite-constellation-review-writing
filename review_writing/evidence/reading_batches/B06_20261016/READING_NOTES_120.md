# [120] Model checking of spacecraft operational designs: a scalability analysis

中文译名：航天器运行设计的模型检验：可扩展性分析。DOI：[10.1007/s10270-025-01281-6](https://doi.org/10.1007/s10270-025-01281-6)。

版本：publisher_online_version_hosted_at_DLR。DLR公开22页Springer排版在线版，DOI、accepted 10 Mar 2025与published online 15 Apr 2025可见。文件未印最终卷期，Crossref后续编入24(6):1825–1846；区分在线文件身份和后续书目信息。

[实际阅读入口](https://elib.dlr.de/214190/1/s10270-025-01281-6.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[12, 14, 16]的相关段落；实际图页复核[14, 16]的相关区域。PDF SHA256 `957afcd0f6e95eb750d91f04d4d54666ce96122361f656a0cdc3fd6c1f05f5da`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-120-C01|deadlock finding examples；物理页[12]|发现消息发送受forbid约束阻塞形成的死锁；有些是建模错误，有些暴露设计过约束。|反例需要回溯错误层次，不能直接等同真实系统已发生故障。|
|B06-120-C02|measurement and stopping rules；物理页[14]|解析、构建、分析计入工具时间；模型语言转换另计，系列运行遇30分钟或10GB则停止。|不支持的性质省略用时不能当很快，资源终止不能记验证通过。|
|B06-120-C03|structure and communication；物理页[14, 16]|无通信最大254状态机可分析，异步通信中等实例就可能触10GB；不同性质没有统一最佳工具。|状态机数不是卫星数，不能把无通信规模当异步星座上限。|
|B06-120-C04|threats to validity；物理页[16]|对照工具状态/转移计数与小模型结构，仍承认只用一个运行设计的外部有效性限制。|语义交叉核对增强可信度但不是全部转换正确证明或所有任务普适排名。|

服务综述：4.1和4.4：资源停止、完整计时与模型语义比较。

仍缺：正式在线副本未复现工具/模型；单设计外推、异步消息规模上限和未支持性质继续保留；形式化结果不代表在轨系统整体认证。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
