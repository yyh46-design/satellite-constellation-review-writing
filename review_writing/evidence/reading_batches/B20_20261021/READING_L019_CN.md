# B20-L019｜J2摄动下利用差异升力与阻力的卫星编队保持

Satellite formation keeping using differential lift and drag under J2 perturbation

- 作者：Xiaowei Shao; Mingxuan Song; Jihe Wang; Dexin Zhang; Junli Chen
- [正式文献入口](https://doi.org/10.1108/aeat-06-2015-0168)；正式卷期年：2017。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Jihe-Wang/publication/312252561_Satellite_formation_keeping_using_differential_lift_and_drag_under_J2_perturbation/links/5c3b35ada6fdccd6b5a8f795/Satellite-formation-keeping-using-differential-lift-and-drag-under-J2-perturbation.pdf)；版本：2017 publisher-layout copy publicly uploaded by coauthor; PDF p1 cover; article pp11–19。
- 来源ID：E-B20-L019；叙述正文阅读范围：PDF物理页2–9；全文10页。
- 本地文本快照SHA-256：2effccdd2a8c6ba45d181bdbdc9274778e1d8f43ad8f0e4797c9fdabadd88811。**该值不是PDF原文件哈希。**
- 正文通过公开PDF文本读取；PDF原件未成功归档，图表和公式的图像核查待完成。未独立复证明或复现实验。
- 采用状态：CANDIDATE_AFTER_HUMAN_REVIEW；human_verified=false。

## 问题与机制

如何用气动力维持受J2摄动的双星构型？

五块可转动平板产生差分升阻力；Lyapunov反馈给出期望加速度，拟合式换算攻角。

## 验证层级

双星数值仿真，包含GPS、执行器误差及构型尺度/高度扫描。

## 可追溯论点

- **C-B20-001**：研究范围为双星；三颗及以上的扩展留作后续工作。
  定位：PDF物理页9；Conclusion, L1074–1089。
- **C-B20-002**：五块气动板配置旨在分别生成三轴差分加速度。
  定位：PDF物理页4；Configurations of actuators, Fig.2–3, L285–318。
- **C-B20-003**：控制律基于CW误差系统；验证采用含J2的轨道传播。
  定位：PDF物理页5, 6；The problem formulation; Controller design, Eq.(5),(8)–(12)。
- **C-B20-004**：稳定性推导依赖实际与期望控制加速度近似相等的条件。
  定位：PDF物理页5, 6；L409–420; Lyapunov argument L681–721。
- **C-B20-005**：构型尺度或高度增大时，气动控制能力可能不足。
  定位：PDF物理页8, 9；The application analysis, Fig.10–11, L965–995。

## 采用边界与阅读者判断

- 读者判断：本研究应作为物理可执行性筛选的基础材料；未建立通信拓扑、协商权限或多星避碰协议，不能归为大星群分布式安全控制验证。
- 读者判断：建模、拟合与执行之间的近似需要显式列出；厘米级误差和高度界限仅作该仿真条件下的报告，不作为可迁移性能承诺。
- 书目信息以Crossref和所读首页为准：正式卷期为2017年89(1):11–19；保留原候选表字节，不把DOI中的2015当作出版年。

## 对综述的帮助

可给拟增的3.6.1提供“任务需求—可达控制力—维持范围”的例子；在现有4.4讨论执行验证时，强调先校核执行器裕量。不能用这一双星结果填补多星协同证据。

这是后续写作的候选证据与组织建议，本批没有修改v3.2正文。文件核验不等于科学结论的人工终核。
