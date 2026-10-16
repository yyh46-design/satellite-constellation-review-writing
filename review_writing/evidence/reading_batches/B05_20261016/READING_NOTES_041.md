# [41] Asynchronous Communication Aware Multi-Agent Task Allocation

中文译名：考虑异步通信的多智能体任务分配。DOI：[ 10.24963/ijcai.2023/30 ](https://doi.org/10.24963/ijcai.2023/30)。

版本：publisher_proceedings_IJCAI_2023。入口：[实际阅读来源](https://www.ijcai.org/proceedings/2023/0030.pdf)。IJCAI官方9页262–270正式会议PDF，题名作者和DOI匹配。

本轮类别：followup_no_unique_increment。补读不增加不同论文数。

阅读范围：物理PDF选读页[4, 5, 6, 7]；实际图页复核[6, 7]的相关区域；文件SHA256 `ab22251d02cb03f9e5731f6d8db751c001bf4a3245e00011e421f1b859674e50`。

|ID|原文定位|观察|使用边界|
|---|---|---|---|
|B05-041-C01|Algorithms1/2; experimental design；页[4, 5]|任务代理可由主动代理承担，握手负责发现任务；task-aware变体另有中心告知。|比较既改变异步机制也改变发现信息条件，须注明是哪一变体。|
|B05-041-C02|Section4, simulator/metric；页[5]|线程模拟用NCLO描述逻辑工作与传输延迟，平面随机点匀速移动；50个实例取均值。|NCLO不是CPU秒，平面代理数不是轨道星座工程验证。|
|B05-041-C03|Section5, loss wording/Fig2；页[6, 7]|p6把常数0.1解释为仅10%到达，但p7又将距离相关符号称丢失概率。|仅记录文本表述不一致，90%丢失结论仍须代码/作者说明确认。|
|B05-041-C04|Section5, dynamic results；页[6, 7]|中心靠近时有小优势；近理想通信下异步反复交换会增加负载并变慢。|分布式优势取决于位置、时延和消息成本，不能写成普遍优于集中式。|

服务综述：3.2.1及4.3：异步消息、发现权限、通信退化与计时。

仍缺：B03概率符号/90%丢失歧义仍open；p6文字明确10%到达，p7符号称loss概率。没有检查代码，不能替作者统一符号。

作者归纳与原文观察分列；候选位置只供后续修订，不表示原段已整体核验。下载/HTML可见/渲染均不计为自动精读完成。`human_verified=false`；正式版配对、全部证明与独立实验未关闭。
