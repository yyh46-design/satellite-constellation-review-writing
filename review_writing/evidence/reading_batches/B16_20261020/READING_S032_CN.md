# B16-S032｜卫星相对运动的高阶障碍函数安全过滤

Safety Control for Satellite Formation Flying via High-Order Control Barrier Functions

- 作者：Xu Zhang; Haiqiang Wang; Dongze Li; Zijie Ji
- [书目/原文入口](https://doi.org/10.3390/app15073751)；标识：10.3390/app15073751。
- 实际版本：Applied Sciences 15(7), 3751，2025-03-29，出版社开放全文18页；Crossref题名/DOI匹配。
- [实际读取PDF](https://mdpi-res.com/d_attachment/applsci/applsci-15-03751/article_deploy/applsci-15-03751.pdf)；来源ID：E-B16-S032；共18页。
- 源文件SHA-256：fb76bdf57230a2ea15e6ae42ba58bf316a50abdbadcae437f3432f8595592696。
- 阅读范围：PDF物理页1–17的正文叙述；关键原页视觉核查：7, 8, 9, 17。
- 附录/证明范围：No separate appendix; proof narratives read but not independently reproduced。
- 证据角色：single_controlled_spacecraft_safety_foundation。
- 专题补充编号S031–S040；不占原80篇L编号。AI精读完成，人工终核待完成；未逐式复证明或独立复现。

## 研究问题

如何让一颗伴星在接近参考星时优先满足位置安全条件，并尽量接近既有PD控制输入？

## 输入、决策与协同机制

非线性相对动力学与可精确计算的Lie导数；三个位置分量分别设下界。仿真轨道半径8000 km，位置初值从[10,100]、速度从[0,1]选取，三个位置下界均10。

针对相对阶2构造HOCBF，以偏离PD输入最小为目标求安全控制。稳定性要求可以另用带松弛CLF约束表达，但这不等于所有版本均已实现。

这是单受控伴星相对参考星的过滤器，未构造多个受控星之间的耦合责任分配。安全条件是三个有符号坐标同时大于下界，不是任意相对方向上的球形保护区。

## 验证设置与证据层级

三个选定随机初态的数值曲线，对照PD与预测时域2的MPC。MPC明确有[-5,5]输入约束，而安全过滤部分没有相同饱和约束；结论将执行器限制、不确定性和不完美通信、广泛Monte Carlo分析列为后续。

## 可追溯论点

- **C-B16-006**：实际控制对象是一颗伴星相对参考星；安全要求为x1、x3、x5分别大于给定下界，不是一般球形距离约束或多受控星两两避碰。
  原文定位：PDF物理页4, 6, 7；§2.1、aim及§3.1 coordinate constraints。
- **C-B16-007**：安全过滤未包含执行器饱和；比较MPC却规定输入[-5,5]、预测时域2，因此曲线比较不能证明在相同输入约束下安全方法普遍优越。
  原文定位：PDF物理页8, 9, 17；QP Equation10、MPC parameters及Actuator Constraints。
- **C-B16-008**：验证仅给出三个选定初态；广泛Monte Carlo、不确定性与不完美通信仍属未来工作，平滑输入曲线也不是实测实时计算证据。
  原文定位：PDF物理页9, 14, 16, 17；Simulation Results、limitations及Conclusion。
- **C-B16-009**：第7页文字要求三个坐标条件同时成立，但安全集印为C1∪C3∪C5，第8页也保留相关并集记号；当前记录为待澄清不一致，不自行改写为交集或宣称已复核证明。
  原文定位：PDF物理页7, 8；§3.1 definition of C及higher-order sets。

## 适用边界与待核问题

- 安全集并集记号与同时满足三项约束的文字不一致，原页已核查，数学解释待作者/人工终核。
- 不将单伴星过滤器描述成多星联合可行性保证。
- 没有实测逐步优化时长、最坏时长或星载硬件结果。
- 三个初态和准确动力学不能支撑未知扰动或任意通信受损条件下的安全性。

## 对综述的作用

用作3.6.3局部安全过滤的有限基础，并对比S036的采样与误差条件；不能作为多星、饱和执行及受损通信的完整证据。

以上采用建议为阅读者分析，尚未写入v3.2；不把作者主张、读者推论或文件完整性检查当作独立科学确认。
