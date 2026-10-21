# B20-L024｜基于相对轨道根数的最优卫星编队重构策略

Optimal satellite formation reconfiguration strategy based on relative orbital elements

- 作者：Jihe Wang; Jinxiu Zhang; Xibin Cao; Feng Wang
- [正式文献入口](https://doi.org/10.1016/j.actaastro.2012.02.015)；正式卷期年：2012。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Jihe-Wang/publication/256935233_Optimal_satellite_formation_reconfiguration_strategy_based_on_relative_orbital_elements/links/5adfc91fa6fdcc29358fd9cb/Optimal-satellite-formation-reconfiguration-strategy-based-on-relative-orbital-elements.pdf)；版本：2012 publisher-layout article publicly uploaded by coauthor, Acta Astronautica76:99–114。
- 来源ID：E-B20-L024；叙述正文阅读范围：PDF物理页1–16；全文16页。
- 本地文本快照SHA-256：2568b8c6d453683e64e1c2acf29cddc93cd29ff9ddd5efb8911784aca6c72b9f。**该值不是PDF原文件哈希。**
- 正文通过公开PDF文本读取；PDF原件未成功归档，图表和公式的图像核查待完成。未独立复证明或复现实验。
- 采用状态：CANDIDATE_AFTER_HUMAN_REVIEW；human_verified=false。

## 问题与机制

怎样联结单星转移代价与编队位置再分配？

在相对E/I向量平面推导脉冲代价下界，再处理固定或自由终端相位。

## 验证层级

含几何推导、单星算例与四颗从星重构仿真。

## 可追溯论点

- **C-B20-006**：问题设定为圆或近圆参考轨道的开放时间脉冲重构。
  定位：PDF物理页2；Introduction, L111–125。
- **C-B20-007**：几何下界与三脉冲构造用于面内转移，另行处理面外转移。
  定位：PDF物理页4, 5, 6, 7；Section3, Theorems1–4, Lemmas1–2。
- **C-B20-008**：固定终态构型的成员再分配用N!种对应关系表述。
  定位：PDF物理页9, 15；Section5.1 Eq.(53); Section6.3, L1100–1102,L1439–1443。
- **C-B20-009**：自由终端相位情形保留成员间相位差的假设。
  定位：PDF物理页10, 11, 12, 13；Section5 free-final-phase case, Eq.(54)–(57)。
- **C-B20-010**：所示编队重构验证采用四颗从星，另有单星固定/自由终态算例。
  定位：PDF物理页13, 14, 15；Section6.1–6.4, Tables1–4。

## 采用边界与阅读者判断

- 读者判断：单星代价可供上层分配使用，但N!写法及四星算例不足以支持大星座可扩展性；下一轮写作应分别评价代价计算和组合分配。
- 读者判断：本文问题式没有建立覆盖整段转移的成对避碰约束；燃料最优、稳定终端轨道和转移全程安全必须分开陈述。
- 读者判断：开放时间、脉冲与线性相对轨道条件限制了与时限严格、推力有界任务的直接比较；不把Remark2直接当成工程低推力最优保证。

## 对综述的帮助

现有3.1可引用为解析优化基线，3.4可用它解释“谁到哪个槽位”与“如何飞过去”的耦合。与L063并置，展示加入终态安全几何后，决策变量和可行域发生什么变化。

这是后续写作的候选证据与组织建议，本批没有修改v3.2正文。文件核验不等于科学结论的人工终核。
