# B20-L063｜基于相对E/I矢量的最优卫星编队避碰机动

Optimal Satellite-Formation Collision-Avoidance Maneuver Based on Relative E/I Vectors

- 作者：Xiaowei Shao; Jihe Wang; Dexin Zhang; Junli Chen
- [正式文献入口](https://doi.org/10.1061/(asce)as.1943-5525.0000642)；正式卷期年：2016。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Jihe-Wang/publication/304030214_Optimal_Satellite-Formation_Collision-Avoidance_Maneuver_Based_on_Relative_EI_Vectors/links/5a6848f44585159da0db01e6/Optimal-Satellite-Formation-Collision-Avoidance-Maneuver-Based-on-Relative-E-I-Vectors.pdf)；版本：10-page 2016 publisher-layout article publicly uploaded by coauthor; J. Aerospace Engineering29(6):04016048。
- 来源ID：E-B20-L063；叙述正文阅读范围：PDF物理页1–10；全文10页。
- 本地文本快照SHA-256：986cf2fe7167ded8cba3d39157a3245a7d0c94d1fb0fd659ca1c0a0614641c9c。**该值不是PDF原文件哈希。**
- 正文通过公开PDF文本读取；PDF原件未成功归档，图表和公式的图像核查待完成。未独立复证明或复现实验。
- 采用状态：CANDIDATE_AFTER_HUMAN_REVIEW；human_verified=false。

## 问题与机制

在突发构型异常后，怎样用有限脉冲恢复被动安全距离？

固定相对倾角向量，以两次脉冲调整相对偏心率向量；将安全距离约束转为E向量平面内的双曲线几何。

## 验证层级

给出固定安全距离与固定燃料预算的两类算例；另讨论多星几何扩展，但数值部分仍以双星情形为主。

## 可追溯论点

- **C-B20-031**：被动安全参数取相对运动径向—法向平面内的最小距离。
  定位：PDF物理页2, 3, 4；Safety parameter, Eq.(17)–(19), L70–83,L241–246,L359–393。
- **C-B20-032**：所用机动保持相对倾角向量不变，并用两次脉冲调整相对偏心率向量。
  定位：PDF物理页2, 3；Two-impulse strategy; L192–195; proof structure。
- **C-B20-033**：给定安全距离时，以双曲线上最近点求低代价解，并用Newton法迭代。
  定位：PDF物理页5, 6；Fuel-optimal collision avoidance maneuver, L471–488,L568–573。
- **C-B20-034**：给定燃料预算时，以可达圆与安全双曲线相切构造最大安全参数的启发式解。
  定位：PDF物理页6；Collision avoidance maneuver with limited fuel, L638–688。
- **C-B20-035**：正文讨论多星的目标几何扩展；后续仿真围绕两类规避设计展开。
  定位：PDF物理页7, 8, 9, 10；Figs.7–8; Simulations, L711–742。

## 采用边界与阅读者判断

- 读者判断：安全参数属于终态被动相对轨道的几何性质，不是碰撞概率，也不是对整个机动区间全部距离的硬约束；终态安全与机动途中的安全需要分别检查。
- 读者判断：保持相对倾角向量不变、两体近似和两脉冲构造限制了最优性结论的适用范围；机动时间不是这里优化的决策变量，不能直接推出紧急时限可行。
- 读者判断：多星几何可行域的说明不等于已验证多主动星协商协议；数值案例不能作为大规模分布式安全控制的证据。公式与图形尚未图像核查，未独立复现Newton迭代。

## 对综述的帮助

现有3.4可将它与L024对照：构型分配之后，还需在可达域内选取安全的终端相对轨道；拟增3.6.3可用来区分被动安全、燃料预算与全程避碰保证。

这是后续写作的候选证据与组织建议，本批没有修改v3.2正文。文件核验不等于科学结论的人工终核。
