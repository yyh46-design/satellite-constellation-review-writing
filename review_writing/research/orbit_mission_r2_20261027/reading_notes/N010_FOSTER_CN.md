# N010_FOSTER｜Differential Drag Control Scheme for Large Constellation of Planet Satellites and On-Orbit Results

作者：Cyrus Foster; James Mason; Vivek Vittaldev; Lawrence Leung; Vincent Beukelaers; Leon Stepan; Rob Zimmerman。年份：2017。

实际版本：IWSCFF 17-33，arXiv:1806.01218v1；DOI对应2018正式研究线，标题不同，未逐页配对。

原文：https://arxiv.org/pdf/1806.01218v1

PDF SHA-256：`2a13ea05405d1efe59fee5c1a2d224be05339258543bdace39cea5f894f8eb4c`

阅读范围：1–18全文。状态：BODY_READ_AI_NOT_AUTHOR_VERIFIED；human_verified=false。

既有来源：N02。采用：ADOPT_HISTORICAL_VERSION_REREAD。

历史来源N02已登记正式论文Constellation Phasing with Differential Drag on Planet Labs Satellites（2018，DOI 10.2514/1.A33927）；本轮取得并正文阅读的是2017会议稿、2018公开arXiv版本。按同研究线归并，不计全项目新增独立文献。历史是否已完成同版本正文阅读尚未统一核算。

机制：控制器先估计相对相位和相位率，再分配槽位，最后对全体成员联合生成高低阻力命令。参考星的模式影响其他成员相对加速度，因此独立星对命令不能简单叠加。p10讨论槽位与命令一体嵌套优化的计算负担，采用分阶段求解；这支持有接口的分层安排，不支持所有问题分开最优。

业务反向约束：p9几何面积比约10:1，而可用弹道系数比约3:1；成像、下传可抢占阻力模式，姿态误差和气体表面作用也影响有效控制权。平台几何能力与业务期间真正可用的控制权应分开。

飞行与仿真：pp10–12、图10–12为Flock 2p十二星、约510 km的飞行相位控制，地面每日定轨与更新。运行中有效控制权一度比预测低约50%，引起超调及槽位反复调整，后续用实测状态更新估计。p13图13为Flock 3p的88星仿真，含前80天分批调试；摘要百星能力为仿真表述，不能计成88或100星完整飞行验证。

写作采用：3.2补充业务活动如何改变轨道控制能力和真实反馈；4.4保留12星飞行与88星仿真的区别。没有据此新增协同避碰保证。

## 可追溯论点

- C-N010-01：成像和下传可抢占阻力模式，控制估计需按实际轨道反馈更新。定位：p9; pp10–12。边界：沿轨相位控制，不是全星座避碰验证。

- C-N010-02：12星为飞行相位控制，88星图为仿真。定位：pp11–13, Figs.11–13。边界：同一历史N02研究线，不重复新增独立来源。
