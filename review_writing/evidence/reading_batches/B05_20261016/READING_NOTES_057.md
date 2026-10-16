# [57] Orbit-aware task scheduling in satellite edge computing

中文译名：卫星边缘计算中的轨道感知任务调度。DOI：[ 10.1007/s10586-025-05663-9 ](https://doi.org/10.1007/s10586-025-05663-9)。

版本：publisher_VOR_Springer_OA。入口：[实际阅读来源](https://link.springer.com/content/pdf/10.1007/s10586-025-05663-9.pdf)。Springer公开正式排版18页，Cluster Computing28:1013(2025)，DOI及作者可核。

本轮类别：followup_no_unique_increment。补读不增加不同论文数。

阅读范围：物理PDF选读页[9, 11, 12, 15]；实际图页复核[9, 15]的相关区域；文件SHA256 `f1c1bd362d23b0f70c444fc892e6527cec5afa1dbbc69504538e86c7a2aab37b`。

|ID|原文定位|观察|使用边界|
|---|---|---|---|
|B05-057-C01|Algorithms1/2, SearchNode/PropagateSearch；页[9]|筛选用预计响应与资源条件，转发扣传输开销；无可行点时实现采用随机邻居传播。|“guarantees”指模型过滤，不是有队列波动、过期状态下的实测硬截止保证。|
|B05-057-C02|Section6.1, PriorityResource；页[11]|文中以PriorityResource排队，资源空闲则执行，否则等待释放。|所读段未说明执行中抢占；动态优先级不能直接称抢占式执行。|
|B05-057-C03|Table2, simulated time and state update；页[12]|场景时长600秒、可见域评估周期30秒、统一截止30秒。|600秒为模拟任务时间，30秒刷新与截止同阶，不能假设连续瞬时态势。|
|B05-057-C04|Section7/Table5, response-time explanation；页[15]|作者指出到达间隔变化也改变成功子集中的服务需求分布。|平均响应下降不能单独归因调度更优；同需求、共同分母比较尚需补证。|

服务综述：3.2.2、4.1与4.3：准入预测、优先级和成功子集比较。

仍缺：未检查模拟代码和所有等待/超时路径；论文段落的可行性预测不是独立实测截止保证。B04成功率与标签问题保留。

作者归纳与原文观察分列；候选位置只供后续修订，不表示原段已整体核验。下载/HTML可见/渲染均不计为自动精读完成。`human_verified=false`；正式版配对、全部证明与独立实验未关闭。
