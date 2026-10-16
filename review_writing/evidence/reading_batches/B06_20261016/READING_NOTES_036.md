# [36] Scheduling of Earth observing satellites using distributed constraint optimization

中文译名：基于分布式约束优化的对地观测卫星调度。DOI：[10.1007/s10951-024-00816-x](https://doi.org/10.1007/s10951-024-00816-x)。

版本：publisher_version_Springer。18页Springer正式排版，Journal of Scheduling 27:507–524 (2024)、DOI/在线日期匹配。

[实际阅读入口](https://link.springer.com/content/pdf/10.1007/s10951-024-00816-x.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[9, 12]的相关段落；实际图页复核[9, 12]的相关区域。PDF SHA256 `ee77d1c2433335c5d87b085489a4f466462a53627699088668237baedcbe9d38`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-036-C01|small-instance BnB；物理页[9]|完整BnB仅用于两星等小实例，其最优值支持小例中启发式质量比较。|不能把该最优证书转移到大例或全部DCOP变体。|
|B06-036-C02|four benchmark sets；物理页[9]|大例八星、最多3000观测机会且容量不紧；中/高冲突设置另测试容量约束。|八星、请求数、机会数与容量紧度是不同难度维度。|
|B06-036-C03|Gini metrics and fairness discussion；物理页[9, 12]|分别测请求数和归一化奖励的Gini；平等参与机会与最终分配公平分开讨论。|对称起点不保证更低Gini，文中亦未见集中/分布在此指标上明确差异。|
|B06-036-C04|efficiency measures；物理页[9]|效率指标分运行时间与交换消息数，30个随机实例按给定区间生成。|消息条数不是字节、带宽占用或消息新鲜度；未与真实链路丢失统一测试。|

服务综述：3.2.1及4.1/4.2：规模、基线和公平性的不同含义。

仍缺：图页相关区域本轮复核，未复现实例与算法；全部隐私/通信证明和运行动态仍未核完。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
