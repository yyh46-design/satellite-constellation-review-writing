# B19-L004｜面向内重力波层析探测的立方星星座轨道维持

Orbital Maintenance of a Constellation of CubeSats for Internal Gravity Wave Tomography

- 作者：Stephen Leroy; Riley Fitzgerald; Kerri Cahoy; James Abel; James Clark
- [正式文献入口](https://doi.org/10.1109/jstars.2019.2961084)；DOI：10.1109/jstars.2019.2961084。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Stephen-Leroy-2/publication/339220232_Orbital_Maintenance_of_a_Constellation_of_CubeSats_for_Internal_Gravity_Wave_Tomography/links/5e46c789458515072d9dab44/Orbital-Maintenance-of-a-Constellation-of-CubeSats-for-Internal-Gravity-Wave-Tomography.pdf)；版本：作者公开的IEEE正式版，2020，13:307–317，11页。
- 来源ID：E-B19-L004；叙述正文阅读范围为PDF物理页1–9，所读PDF共11页。
- 本地文本快照SHA-256：3b420a3fd4d143a145af4c0bed2bc03db4a9b63083686e3b47383adec5695040。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：candidate_after_human_review；human_verified=false。

## 问题、输入与决策

观测构型的空间分离需求怎样受推进能力和寿命约束？

输入为轨道倾角差、RAAN容差、最大加速度和总ΔV；用半长轴调整配合轨道法向机动保持构型。

## 验证层级

理论模型与STK、GMAT轨道仿真；并非在轨维持演示。

## 可追溯论点

- **C-B19-001**：不同倾角造成差异节点退行，单独匹配平均运动不足以维持构型。
  定位：PDF物理页2, 3, 4；Sec.III, Eqs.(1)–(4)。
- **C-B19-002**：维持规则由RAAN偏差阈值触发，并在最大、最小纬度附近成对机动。
  定位：PDF物理页5, 6；Sec.V station-keeping rules。
- **C-B19-003**：最大加速度与总ΔV分别限制可维持的分离程度和任务持续时间。
  定位：PDF物理页7, 8；Fig.6 discussion; Sec.VI。
- **C-B19-004**：寿命计算未计入最初部署所需推进量。
  定位：PDF物理页7；Sec.V immediately after Fig.6。
- **C-B19-005**：长时间推进会与掩星测量所需定轨精度冲突，形成任务可用时间约束。
  定位：PDF物理页9；Sec.VI, Eq.(18) discussion。

## 采用边界与阅读者判断

- BIT-3的推进器分类需另核实，暂不沿用文中所有“electrospray”标签。
- 图6没有完成图像核查，型号数值和曲线差异暂不用于定量比较。
- 阅读了附录A的构型几何说明，未逐式复核或复现轨道传播。

## 对综述的帮助

建议新增3.6.1时，用它连接观测几何、推进资源与维持调度；4.4讨论任务执行窗口与轨道修复的耦合。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
