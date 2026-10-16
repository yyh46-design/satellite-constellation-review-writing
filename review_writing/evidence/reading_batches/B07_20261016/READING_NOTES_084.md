# [84] Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques

中文译名：接近筛查方法性能评估及基于CUDA的接近分析计算提速。DOI：[10.3390/aerospace10060543](https://doi.org/10.3390/aerospace10060543)。

版本：publisher_version_MDPI。本地既有Aerospace 2023,10,543正式PDF，DOI/最终版式匹配；文字层混有重复旧FOR PEER REVIEW字符串，p11/p13实际像素未见该旧水印，按实际页面核表。

[实际阅读入口](https://www.mdpi.com/2226-4310/10/6/543)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[5, 6, 8, 9]的相关段落；实际图页相关区域[6, 9]。PDF SHA256 `0f359de7fc7eaf34b9e104716e0046584213ea3f0354a337ddaeb0dac66473c7`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-084-C01|Smart Sieve; CSieve; Fig5；物理页[5, 6]|阈值与时间步长关联；轴包络、RdotV等条件串联筛查，检测到区间接近仍不保证距离低于临界阈值。|候选接近、临界距离事件和概率风险需要分开；未独立核全公式与无漏筛条件。|
|B07-084-C02|SOCRATES comparison；物理页[8]|用相同TLE比较TCA与距离，所列最大差为0.011秒和0.015千米。|属于同输入算法对照，不代表相对真实轨道的测量精度。|
|B07-084-C03|§3.2 GPU memory strategy；物理页[9]|筛后数量难预知，使用按对象对的布尔结果及逐时段通过列表；将最近接近计算移入时间循环处理CSieve内存问题。|并行化包含数据组织/内存调度改变，不能只归因CUDA核心数。|
|B07-084-C04|all-vs-all setup；物理页[9]|24023对象一天、一分钟步长、5千米条件；双精度T4与同机CPU单核比较。|GPU/单核参照与前文另一目录七天one-vs-all不可直接当共同横向平台；未独立复现。|

服务综述：3.4.1/4.1：筛查链、验证参照与GPU内存。

仍缺：未独立证明全域不漏检；抽取层混入draft重复段但实际页面仅最终版；全部公式/实现和原漏检项继续开放。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
