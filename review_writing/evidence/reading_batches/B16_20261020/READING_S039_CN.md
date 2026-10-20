# B16-S039｜分情形处理时延与拓扑切换的深空编队控制

Formation control for networked spacecraft in deep space: with or without communication delays and with switching topology

- 作者：Nan Wang; TianWu Zhang; JieQiong Xu
- [书目/原文入口](https://doi.org/10.1007/s11432-011-4191-1)；标识：10.1007/s11432-011-4191-1。
- 实际版本：Science China Information Sciences 54(3),469–481，2011，出版社13页全文；Crossref题名/DOI匹配。
- [实际读取PDF](https://www.sciengine.com/parse/pdf/1674-733X/EjdatdLC9zueADkMq.pdf?attname=EjdatdLC9zueADkMq.pdf)；来源ID：E-B16-S039；共13页。
- 源文件SHA-256：9b5a6d1ae9b4056e1d38643b2d9be887dde2333b9a7a7580251c02d5706e7020。
- 阅读范围：PDF物理页1–12的正文叙述；关键原页视觉核查：4, 7, 8, 10。
- 附录/证明范围：No separate appendix; proof narratives read but not independently reproduced。
- 证据角色：multi_spacecraft_communication_foundation。
- 专题补充编号S031–S040；不占原80篇L编号。AI精读完成，人工终核待完成；未逐式复证明或独立复现。

## 研究问题

只用邻居的位姿信息时，深空航天器如何在固定、延迟或切换通信图下协调六自由度参考？

## 输入、决策与协同机制

Euler–Lagrange六自由度模型，外扰被假设可忽略。无向连通图、位置和姿态参考、对应速度信息与模型项；没有两两禁入或推力上限约束。

分别设计无时延、固定对称时延、时变对称时延和连通切换拓扑控制器，以误差一致及趋零为目标。

不同章节的条件适用于不同控制器；时变延迟要求非增，切换章节要求每张图都连通并有驻留条件，不能拼成任意延迟、断连、丢包同时处理的结论。

## 验证设置与证据层级

四航天器姿态仿真。作者明确省略平移几何仿真；时变延迟为指数衰减函数，拓扑在5/10/15 s切换的试验另列。随机或断裂通信留待后续。

## 可追溯论点

- **C-B16-037**：第4.3节时变时延须对称，且其导数不大于d、d不大于0，即非增时延；不能称为任意有界振荡延迟保证。
  原文定位：PDF物理页7, 8；Definition4.3及Theorem4.3。
- **C-B16-038**：切换拓扑定理要求每一张无向图都连通；该控制器与时延章节分列，不能据此声称已解决同时延迟和任意断连。
  原文定位：PDF物理页6, 7, 8, 9；Theorems4.2–4.4及controller27。
- **C-B16-039**：模型假设外扰可忽略，没有输入上限或两两禁入约束；跟踪及一致性结论不等于安全集合不变性。
  原文定位：PDF物理页4, 5, 6；complete model and control objective。
- **C-B16-040**：实际只展示四航天器姿态仿真，平移部分被明确省略；指数衰减时延与5/10/15 s拓扑切换分开试验，随机/断裂通信为未来工作。
  原文定位：PDF物理页10, 11, 12；§5 Simulation及Conclusion。
- **C-B16-041**：第8页驻留条件印为t(k−1)−t(k)≥正τ，与递增切换时刻的通常定义不相容；保留为记号待澄清，未据此宣称已独立审定或推翻稳定性证明。
  原文定位：PDF物理页8, 9；§4.4 switching-time assumption。

## 适用边界与待核问题

- 六自由度理论描述不等于六自由度碰撞安全实证。
- 时延非增和对称条件较强，不覆盖任意时变链路。
- 驻留时间式印为先前时刻减后续时刻大于正数，记号方向待澄清，不自行更正文献。
- 输入饱和、未知外扰和硬避碰未共同建模。

## 对综述的作用

用于综述的通信条件对照，明确时延、切换、噪声和断连是不同问题；并在采用环节逐项核查当前情形是否满足所引定理。

以上采用建议为阅读者分析，尚未写入v3.2；不把作者主张、读者推论或文件完整性检查当作独立科学确认。
