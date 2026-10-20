# B16-S038｜伪谱与粒子群重构中节点间安全的实际边界

Optimal Spacecraft Formation Reconfiguration with Collision Avoidance Using Particle Swarm Optimization

- 作者：Haibin Huang; Yufei Zhuang; Guangfu Ma; Yueyong Lv (actual PDF order)
- [书目/原文入口](https://doi.org/10.5755/j01.itc.41.2.854)；标识：10.5755/j01.itc.41.2.854。
- 实际版本：Information Technology and Control 41(2),143–150，2012，出版社8页全文；PDF与Crossref/网页作者顺序不一致，留待人工终核。
- [实际读取PDF](https://itc.ktu.lt/index.php/ITC/article/view/854/1501)；来源ID：E-B16-S038；共8页。
- 源文件SHA-256：57b7605ab6a07385e93aba84baf5b4c16c44a8b603578c3fa5a447b076bbd131。
- 阅读范围：PDF物理页1–7的正文叙述；关键原页视觉核查：5, 6, 7。
- 附录/证明范围：No separate appendix; proof narratives read but not independently reproduced。
- 证据角色：multi_spacecraft_trajectory_optimization。
- 专题补充编号S031–S040；不占原80篇L编号。AI精读完成，人工终核待完成；未逐式复证明或独立复现。

## 研究问题

如何在深空短时重构中，较快生成考虑两两避碰与推力限制的多星轨迹，并改善仅在伪谱节点避碰的不足？

## 输入、决策与协同机制

同步三航天器、定质量点质点双积分器；忽略相对引力，连续低推力有上下界，初末速度固定。例子使用归一化时间、质量、推力与安全距离。

先用LGL伪谱离散，再用KNITRO生成可行初始粒子与粒子群搜索优化平方控制能量；在最近节点附近插入四等分检查点，拒绝违反这些点约束的候选。

粒子是优化候选，不是实际卫星控制主体；Theorem1保持离散线性动力学等式，不证明全局最优或连续避碰。约束节点之间的检查仍有限。

## 验证设置与证据层级

三颗星、10个LGL点、安全距离2；200次随机优化初值比较。Table1给每次最小间距的平均值PSO为1.9138，低于要求2；原文明确承认偶发节点间违反并称可接受。本文记录违反，不自行接受其标准。

## 可追溯论点

- **C-B16-032**：算法为集中同步三航天器的双积分器轨迹优化；粒子群搜索的粒子是候选解，不是分散卫星，目标为平方推力积分而非实际推进剂质量。
  原文定位：PDF物理页2, 3, 4, 5；problem statement、objective及PSO formulation。
- **C-B16-033**：Theorem1保持线性配点动力学等式；增加最近节点附近四等分检查点仍未形成连续安全证明，作者仅称全程可能可行。
  原文定位：PDF物理页4, 5；Theorem1及§5.2 test points。
- **C-B16-034**：Table1的200次试验中，每次最小间距平均值PSO为1.9138，小于设定安全距离2；正文承认偶发节点间安全距离违反，不能登记全样本硬安全成功。
  原文定位：PDF物理页5, 6, 7；safe distance setting、§6及Table1。
- **C-B16-035**：200次Monte Carlo随机化的是优化初值；平均总用时PSO19.9936 s、LPM17.8736 s，约18 s为初始化，不能推成在星载硬件上普遍更快或抗扰安全。
  原文定位：PDF物理页6, 7；random initial values、runtime discussion及Table1。
- **C-B16-036**：PDF作者顺序为Huang/Zhuang/Ma/Lv，出版社网页和Crossref为Huang/Ma/Zhuang/Lv；题名、DOI相同，当前保留顺序冲突，不自行选定正式作者排序。
  原文定位：PDF物理页1, 2；PDF title/running head plus metadata/S038_CROSSREF.json。

## 适用边界与待核问题

- PSO的“swarm”不代表分布式或星间通信算法。
- 200次随机初值测试不等于真实动力学噪声鲁棒Monte Carlo。
- 题名optimal不构成全局最优证明，作者也称near optimal。
- 有时更小的数值违反仍是原安全约束违反，不能记为全部成功。
- 出版社PDF与Crossref作者顺序不同，采用引用前须人工确认。

## 对综述的作用

适合用作3.6.1/3.6.3的反例：节点或附加测试点通过仍不足以证明整条实际执行轨迹安全，并区分数值效率、可行性和最优性。

以上采用建议为阅读者分析，尚未写入v3.2；不把作者主张、读者推论或文件完整性检查当作独立科学确认。
