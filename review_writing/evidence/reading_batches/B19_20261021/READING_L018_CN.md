# B19-L018｜考虑星间链路的星座卫星相对跟踪控制

Relative tracking control of constellation satellites considering inter-satellite link

- 作者：M. Fakoor; F. Amozegary; M. Bakhtiari; K. Daneshjou
- [正式文献入口](https://doi.org/10.1016/j.asr.2017.07.012)；DOI：10.1016/j.asr.2017.07.012。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Fatemeh-Amozegary/publication/318448926_Relative_Tracking_Control_of_Constellation_Satellites_Considering_Inter-Satellite_Link/links/644d0f7d5762c95ac3605cc2/Relative-Tracking-Control-of-Constellation-Satellites-Considering-Inter-Satellite-Link.pdf)；版本：作者公开的26页正式版；ASR 60 (2017) 2021–2046。
- 来源ID：E-B19-L018；叙述正文阅读范围为PDF物理页1–26，所读PDF共26页。
- 本地文本快照SHA-256：ba745c13aa490c33e25cf9dd593f9d9c952d55c7fef264614702d4416f4e8e89。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：candidate_after_human_review；human_verified=false。

## 问题、输入与决策

相对轨道预测如何服务星间链路指向，载荷自由度怎样改变执行代价？

先用含J2的球面几何生成相对指向及角速度参考，再设计本体或载荷跟踪的滑模控制。

## 验证层级

一颗基准星与三种目标轨道的数值比较；控制器与PID、LQR作算例比较。

## 可追溯论点

- **C-B19-021**：几何相对运动模型为链路指向提供角速度和角加速度参考。
  定位：PDF物理页4, 5, 6；Secs.2.1–2.2, Eqs.(30)–(31)。
- **C-B19-022**：论文区分本体跟踪与载荷跟踪，并比较载荷有无转动自由度。
  定位：PDF物理页6, 7, 12, 16, 17；Secs.4.1–4.3。
- **C-B19-023**：无载荷自由度的算例未实现所需参考跟踪。
  定位：PDF物理页16；Sec.4.2 discussion of Figs.13–15。
- **C-B19-024**：有载荷自由度的设计在作者算例中降低了所需控制力矩。
  定位：PDF物理页19, 20, 26；Sec.4.3 and Conclusion。
- **C-B19-025**：模糊切换增益用于改善滑模控制的抖振。
  定位：PDF物理页20, 21, 22；Sec.4.4。

## 采用边界与阅读者判断

- “large-scale”指相对运动范围，不能据此声称大规模星数验证。
- 不研究两两避碰、碰撞概率或网络任务分配；仅是链路建立的控制基础。
- 正文存在7/6秒及500/600秒等表述差异；这些数值不采用。
- 几何模型误差的极小数值说法和商用软件对照误差并列，须另查定义；本批不采用精度优越性结论。

## 对综述的帮助

可补4.4对“协同需要通信，但通信也需要姿态与载荷资源”的讨论，避免把星间链路当成零代价前提。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
