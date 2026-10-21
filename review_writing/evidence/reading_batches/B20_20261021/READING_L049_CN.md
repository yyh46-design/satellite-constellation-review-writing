# B20-L049｜编队卫星空间碎片避碰机动优化

Optimization of Space Debris Collision Avoidance Maneuver for Formation Flying Satellites

- 作者：Jae-Dong Seong; Hae-Dong Kim
- [正式文献入口](https://doi.org/10.5140/jass.2013.30.4.291)；正式卷期年：2013。
- [实际读取的公开PDF](https://www.researchgate.net/publication/260723716_Optimization_of_Space_Debris_Collision_Avoidance_Maneuver_for_Formation_Flying_Satellites/fulltext/69a9731f940e2d5e03cd68ed/Optimization-of-Space-Debris-Collision-Avoidance-Maneuver-for-Formation-Flying-Satellites.pdf)；版本：8-page 2013 publisher-layout article, JASS30(4):291–298; public PDF extraction has duplicate text layers on pp4–5。
- 来源ID：E-B20-L049；叙述正文阅读范围：PDF物理页1–7；全文8页。
- 本地文本快照SHA-256：11ab02870ffd8588b16dbece9a28f383d7ed39e6fdf9f0bbc2bdd1d63a435b24。**该值不是PDF原文件哈希。**
- 正文通过公开PDF文本读取；PDF原件未成功归档，图表和公式的图像核查待完成。未独立复证明或复现实验。
- 采用状态：CANDIDATE_AFTER_HUMAN_REVIEW；human_verified=false。

## 问题与机制

双星规避碎片时，能否同时减少后续维护负担？

PSOGSA与MATLAB/STK联算，将速度增量和维护周期组成加权适应度。

## 验证层级

一个合成碎片交会的双星仿真；不是在轨实验。

## 可追溯论点

- **C-B20-021**：决策包含两颗星各三轴速度增量，并固定提前半轨同时单脉冲。
  定位：PDF物理页5；Section2.4, Table3, L973–1005。
- **C-B20-022**：适应度同时计入避碰惩罚、速度增量和编队维护周期。
  定位：PDF物理页5；Section2.3, Eq.(9), L854–888。
- **C-B20-023**：STK传播与风险分析回传MATLAB，供启发式优化评价。
  定位：PDF物理页5；Section2.4, Fig.5, L950–972。
- **C-B20-024**：算例报告约218米间距及维护周期32到109小时。
  定位：PDF物理页6, 7；Section3, Tables4–5; L1016–1029,L1095–1103。
- **C-B20-025**：三颗及以上编队扩展在结论中作为未来工作。
  定位：PDF物理页7；Conclusion, L1104–1110。

## 采用边界与阅读者判断

- 读者判断：该例把规避和后续维护联系起来，值得写入任务恢复讨论；三倍以上维护周期是特定算例结果，不能作为一般收益。
- 待核：正文与Table3的种群/代数设置不一致；结果处“总和4cm/s”与结论“各4cm/s”也有歧义。关键表格未做图像核对，暂不采用这些数值。
- 读者判断：有限惩罚项和一次成功仿真不构成硬安全证明；没有充分算法对照时，不据引言或结论泛称PSOGSA优于所有单算法。

## 对综述的帮助

现有3.2可用为启发式求解与仿真器联算案例，4.4可讨论“规避是否减少后续维护次数”。这是双星协同机动线索，尚不足以支持大星群调度性能。

这是后续写作的候选证据与组织建议，本批没有修改v3.2正文。文件核验不等于科学结论的人工终核。
