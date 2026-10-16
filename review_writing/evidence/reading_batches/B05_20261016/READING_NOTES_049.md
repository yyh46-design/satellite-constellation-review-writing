# [49] Deep Space Network Scheduling via Mixed-Integer Linear Programming

中文译名：基于混合整数线性规划的深空网络调度。DOI：[ 10.1109/ACCESS.2021.3064928 ](https://doi.org/10.1109/ACCESS.2021.3064928)。

版本：author_draft_with_template_metadata。入口：[实际阅读来源](https://www.columbia.edu/~rm3122/paper/deep_space.pdf)。作者Columbia公开11页稿，仍有xxxx日期、占位DOI、VOLUME 4,2016和Table ??等模板内容；真实题名作者匹配目标DOI，但不能把模板字段当正式元数据。Δ-MILP是后续不同论文，不用于冒充此篇。

本轮类别：followup_no_unique_increment。补读不增加不同论文数。

阅读范围：物理PDF选读页[3, 4, 5, 6]；实际图页复核[4, 5]的相关区域；文件SHA256 `82227db029fb21d38852e96ffa6354d4586a2a9a2fa2ed33fc43faafc2b9242a`。

|ID|原文定位|观察|使用边界|
|---|---|---|---|
|B05-049-C01|assumptions; Eq7b/7h；页[3, 4, 5]|跟踪落在可见窗，准备/撤收可在窗外但占资源；分段各有准备撤收和最小片段/间隔。|不能把全部活动时间强行放进可见窗，也不能把拆分视为无成本。|
|B05-049-C02|Algorithm1, randomized MILP；页[5, 6]|按随机权重从解池挑初值并限时重解，最后恢复原活动数目标再限时求解。|输出是限时最好可行解，不能因底层MILP而统称全局最优。|
|B05-049-C03|numerical setup, week44/2016；页[6]|案例为2016年第44周、14资源、286活动、30任务方；单次求解器比较给54000秒。|资源、活动与任务方是不同规模单位；离线长预算不是在线秒级调度实证。|
|B05-049-C04|time discretization discussion；页[6]|缩短网格增加排程灵活性也增加变量；粗网格可能浪费15分钟撤收的余量。|不能脱离时间分辨率比较容量或求解速度。|

服务综述：3.2.2及4.1：跟踪与资源占用范围、限时随机化和离散化。

仍缺：作者模板稿的正式版配对与实现约束映射仍open；模型中活动跨资源唯一性不能仅按自然语言假设宣告完成独立验证。

作者归纳与原文观察分列；候选位置只供后续修订，不表示原段已整体核验。下载/HTML可见/渲染均不计为自动精读完成。`human_verified=false`；正式版配对、全部证明与独立实验未关闭。
