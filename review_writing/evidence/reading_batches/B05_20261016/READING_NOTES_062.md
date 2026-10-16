# [62] Mixed-integer programming models for optimal constellation scheduling given cloud cover uncertainty

中文译名：考虑云覆盖不确定性的最优星座调度混合整数规划模型。DOI：[ 10.1016/j.ejor.2018.11.043 ](https://doi.org/10.1016/j.ejor.2018.11.043)。

版本：author_accepted_manuscript_OSTI。入口：[实际阅读来源](https://www.osti.gov/servlets/purl/1524209)。OSTI公开39页作者/接受稿，非正式排版；DOI和作者题名吻合，正式版配对未关闭。

本轮类别：followup_no_unique_increment。补读不增加不同论文数。

阅读范围：物理PDF选读页[21, 22, 24, 25, 27]；实际图页复核[22, 25]的相关区域；文件SHA256 `136c28f5121ece9e892961ccaf2487e886713e4f495140dfe45c5eff76bd085c`。

|ID|原文定位|观察|使用边界|
|---|---|---|---|
|B05-062-C01|benchmark design；页[21, 22]|六个合成基准用GEO长观测窗，1440个一分钟时点，并人为生成校准窗、优先级和超额需求。|不是实飞日志；GEO近固定可见域与LEO窗口结构不能直接互换。|
|B05-062-C02|Table2; Section2.6；页[21, 24]|表2把系数C(k,t)生成时间与1%间隙求解时间分别列出，硬件为64核512GB工作站。|预处理与求解需分别保留，不能当星载CPU或端到端决策总时长。|
|B05-062-C03|two/three-stage model solvability；页[25]|100情景两传感器展开为约1900–2400万变量；三阶段9情景案例报告0.23%间隙和2400秒。|传感器数、情景数和变量数不能混称星座规模，非零间隙不应写成精确最优。|
|B05-062-C04|benchmark and schedules；页[22, 25, 27]|文中生成配置但当前模型不使用；图5比较两阶段固定安排在天气情景下的表现。|不能据“configuration”或多张天气图宣称在轨重构；信息后改排仍须引用三阶段模型原文。|

服务综述：3.2.3与4.1：GEO场景、时间网格、系数预处理和限时界。

仍缺：B04三阶段/样本外反例记录保留；正式版配对、天气分布校准与全部数学/实验复现未完成。

作者归纳与原文观察分列；候选位置只供后续修订，不表示原段已整体核验。下载/HTML可见/渲染均不计为自动精读完成。`human_verified=false`；正式版配对、全部证明与独立实验未关闭。
