# B19-L014｜用于星座部署的电帆调相机动

Electric sail phasing maneuvers for constellation deployment

- 作者：Lorenzo Niccolai; Andrea Caruso; Alessandro A. Quarta; Giovanni Mengali
- [正式文献入口](https://doi.org/10.1016/j.actaastro.2019.12.003)；DOI：10.1016/j.actaastro.2019.12.003。
- [实际读取的公开PDF](https://arpi.unipi.it/retrieve/e0d6c930-940a-fcf8-e053-d805fe0aa794/%5B2020%5D%20Electric%20sail%20phasing%20maneuvers%20for%20constellation%20deployment.pdf)；版本：比萨大学公开的15页作者稿；页脚标明正式DOI与2020卷页。
- 来源ID：E-B19-L014；叙述正文阅读范围为PDF物理页1–14，所读PDF共15页。
- 本地文本快照SHA-256：d002650dd9ebce15c9f30cbd217a54874270373c5ba38ecc3e6a0620eb52846a。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：context_only_outside_core_LEO_scope；human_verified=false。

## 问题、输入与决策

题名中的星座部署是否属于本文的近地大型星座问题？

电太阳风帆在日心圆轨道上调相；部署器逐次释放卫星，以帆姿态和通断状态最小化时间。

## 验证层级

间接最优控制和数值积分；不含实际部署验证。

## 可追溯论点

- **C-B19-011**：研究对象为日心圆形工作轨道，而非地球低轨星座。
  定位：PDF物理页3, 7, 8；Sec.2; Sec.3。
- **C-B19-012**：推力模型对帆姿态施加方向限制，并近似忽略太阳风变化。
  定位：PDF物理页7；Sec.3, Eq.(1) discussion。
- **C-B19-013**：优化同时选择帆俯仰角与电子枪通断，允许开普勒滑行弧。
  定位：PDF物理页7, 8, 9, 10；Eqs.(1)–(19)。
- **C-B19-014**：释放卫星后的质量变化使后续轨道弧的特征加速度改变。
  定位：PDF物理页11, 12；Sec.4.2, Eqs.(22)–(24)。
- **C-B19-015**：部署总时间由逐段调相累加，结果高度依赖帆的性能假设。
  定位：PDF物理页12, 13, 14；Tables1–2; Conclusion。

## 采用边界与阅读者判断

- 与近地星座维持、碎片避碰和地面任务重调度的适用环境差别很大。
- 无显式两两避碰、导航误差或多运营方协同约束。
- 仅作为原候选池范围筛选记录；不把日心算例直接迁入主体结论。

## 对综述的帮助

保留为边界案例，提醒按轨道环境和控制资源筛文献；本轮不建议作为综述主干补强证据。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
