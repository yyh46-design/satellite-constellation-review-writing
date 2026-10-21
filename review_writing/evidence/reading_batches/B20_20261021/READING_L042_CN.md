# B20-L042｜通过碰撞概率反演联合优化避碰与轨道维持机动

Combined Collision Avoidance and Station-Keeping Maneuver Optimization by Collision Probability Inversion

- 作者：Andrea De Vittori; Gabriele Dani; Alexia Cantoni; Pierluigi Di Lizia; Roberto Armellin
- [正式文献入口](https://doi.org/10.2514/1.a36075)；正式卷期年：2026。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Andrea_De_Vittori2/publication/393614728_Combined_Collision_Avoidance_and_Station-Keeping_Maneuvers_Optimization_by_Collision_Probability_Inversion/links/687149736e247f362b18b710/Combined-Collision-Avoidance-and-Station-Keeping-Maneuvers-Optimization-by-Collision-Probability-Inversion.pdf)；版本：40-page author preprint uploaded 2025-07-11; title uses Maneuvers plural; paired formal DOI1.A36075 has Maneuver singular, 2026 volume63(1):203–217; formal text not compared。
- 来源ID：E-B20-L042；叙述正文阅读范围：PDF物理页1–37；全文40页。
- 本地文本快照SHA-256：d9e770f75647f18f8fcfdaa2832e798d0aee265a4905ab1f2dbbb13bdec032ba。**该值不是PDF原文件哈希。**
- 正文通过公开PDF文本读取；PDF原件未成功归档，图表和公式的图像核查待完成。未独立复证明或复现实验。
- 采用状态：CANDIDATE_AFTER_HUMAN_REVIEW；human_verified=false。

## 问题与机制

如何把短时避碰条件和后续轨道保持目标联结？

将Chan概率阈值反演为SMD条件，用EOE线性化与三点边值问题联结TCA及终态。

## 验证层级

概率反演测试与两种GEO交会场景；正文明确展示中途纬度越界。

## 可追溯论点

- **C-B20-011**：安全条件针对短时交会，轨道保持通过终态目标接入。
  定位：PDF物理页5, 6, 17, 18；SectionII.A–B, III.B, Eq.(1),(56)–(61)。
- **C-B20-012**：Chan概率反演采用局部展开和迭代求根。
  定位：PDF物理页14, 15, 16, 17；SectionIII.A, Eq.(36)–(55)。
- **C-B20-013**：若仅轨道保持已满足安全条件，则无需启用附加避碰约束。
  定位：PDF物理页18, 20, 21；SectionIII.B, Fig.2–3, L1255–1271,L1433–1460。
- **C-B20-014**：该稿动力学演示主要保留J2,2，且可作为更细优化的初值。
  定位：PDF物理页11；SectionII.E, L563–572。
- **C-B20-015**：一个算例中途纬度越界；终态满足不等于全程在框内。
  定位：PDF物理页30, 35；SectionIV.C–D, Fig.16,24; L2130–2135,L2474–2478。

## 采用边界与阅读者判断

- 版本边界：本次读完的是2025年公开预印稿；Crossref正式卷期为2026年63(1):203–217，题名使用单数Maneuver。未逐字比较正式版，可追溯论点绑定所读稿物理页，正式引用前须核对1.A36075对应内容。
- 读者判断：稿件讨论二次方程负乘子分支（物理页20–21）；不能据此宣称对完整不等式约束获得普遍全局最优解。相关最优性表述暂缓采用。
- 读者判断：能量最优初值、推力可执行性、全程轨道框约束和多主动星协同是不同验证层级；这篇不能单独证明后面三项。

## 对综述的帮助

可在现有4.4和拟增3.6.3说明“避碰后还能否继续运行”的终端目标。特别适合作为反例：正文中的越界现象说明终端恢复与全程运行约束必须分开评述。

这是后续写作的候选证据与组织建议，本批没有修改v3.2正文。文件核验不等于科学结论的人工终核。
