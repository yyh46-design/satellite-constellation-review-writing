# [34] Decentralized Observation Allocation for a Large-Scale Constellation

中文译名：面向大型星座的分散式观测分配。DOI：[10.2514/1.I011215](https://doi.org/10.2514/1.I011215)。

版本：publisher_typeset_copy_hosted_at_JPL。15页JPL公开副本含最终期刊版式、JAIS 20(8):447–461、DOI与正式出版信息；不能因文件名或机构托管就自动降为预印本。

[实际阅读入口](https://ai.jpl.nasa.gov/public/documents/papers/parjan-jais2023-mas.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[7, 10, 13]的相关段落；实际图页复核[7, 10]的相关区域。PDF SHA256 `8b0af8efb6e3f61428dd1a59b24c6d914f6db52d8dd48e03c7120e7c0a7593f9`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-034-C01|BD algorithm variants；物理页[7]|请求满足版只共享满足状态，contention版还共享可用过境数与奖励，并以上一轮信息更新。|共享内容和排序规则同时改变，不能只按“多/少通信”给统一排名。|
|B06-034-C02|grid-search setup；物理页[10]|概率参数用10颗SkySat、1030请求的训练问题网格搜索后用于后续实验。|这是预先调参，单次调用速度不包括这一成本；不保证跨规模都保持最佳参数。|
|B06-034-C03|single-threaded simulation timing；物理页[10]|本文为单线程模拟分布执行，作者把除以代理数的并行用时表述为估算。|推测并行收益不能当实测星载分布执行墙钟。|
|B06-034-C04|experiments1/4 and reward discussion；物理页[10, 13]|满足版在所测案例优于contention版；作者把差异联系到易/难请求奖励与重复观测。|更多共享信息不保证更高业务收益；节点增减测试也不是任意丢包网络证明。|

服务综述：3.2.1及4.1/4.3：消息内容、概率调参和并行计时证据。

仍缺：正式副本已读新增段，原概率/能力/通信条件与全部代码/并行实现未复现；B02计数保持。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
