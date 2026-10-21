# B20-L050｜地球静止轨道长期避碰与随机轨道维持的联合处理

Combined Long-Term Collision Avoidance and Stochastic Station-Keeping in Geostationary Earth Orbit

- 作者：Andrea De Vittori; Zeno Pavanello; Pierluigi Di Lizia; Jay McMahon; Roberto Armellin
- [正式文献入口](https://doi.org/10.2514/1.g008629)；正式卷期年：2025。
- [实际读取的公开PDF](https://re.public.polimi.it/retrieve/61e91a18-bfc3-4ad3-84cd-52bef2c46d8f/DEVIA_OA_01-25.pdf)；版本：40-page repository accepted manuscript including cover; title shortens formal Geostationary Earth Orbit to GEO; paired DOI1.G008629。
- 来源ID：E-B20-L050；叙述正文阅读范围：PDF物理页2–36；全文40页。
- 本地文本快照SHA-256：2da1096829f826c5223719206b2bef00aa504ad5f8bbe55d3d2257289e6d1283。**该值不是PDF原文件哈希。**
- 正文通过公开PDF文本读取；PDF原件未成功归档，图表和公式的图像核查待完成。未独立复证明或复现实验。
- 采用状态：CANDIDATE_AFTER_HUMAN_REVIEW；human_verified=false。

## 问题与机制

长期交会中，如何联结避碰、位置不确定性和轨道保持？

SCP/SOCP联合处理IPoC约束和轨道框机会约束；比较单独/联合几何约束及风险分配。

## 验证层级

GEO构造交会仿真，比较确定性与随机保持；轨道确定更新采用合成步骤。

## 可追溯论点

- **C-B20-026**：规避指标采用瞬时碰撞概率IPoC，不能直接等同全时段碰撞概率。
  定位：PDF物理页3, 13；Introduction L85–87; SectionIII Eq.(27), L799–827。
- **C-B20-027**：单独与联合机会约束分别处理经纬度边界及其相关性。
  定位：PDF物理页6, 7, 18, 19, 20, 21；SectionII.A; III.D Eq.(46)–(60)。
- **C-B20-028**：优化约束在积分节点施加；网格密度影响节点间违约。
  定位：PDF物理页13, 28；Eq.(27); SectionIV.A L2114–2121。
- **C-B20-029**：轨道更新后缩小协方差并分段重规划，但更新过程是合成的。
  定位：PDF物理页25, 26, 35；SectionIII.E; IV.E, L1844–1917,L2483–2491。
- **C-B20-030**：该算例经纬度相关性接近零，未充分检验强相关情形。
  定位：PDF物理页32, 33, 36；Fig.18; Conclusion L2563–2567。

## 采用边界与阅读者判断

- 读者判断：空间两维的联合约束不自动等于全时段联合风险保证；IPoC、框内概率、跨时段事故概率应分别列栏。
- 读者判断：原稿将IRA代价下降的一般性质与本问题的限制分开说明（物理页9–10、14）；不据此宣称本联合问题每次迭代必然节省燃料或全局收敛。
- 读者判断：合成OD展示了更新信息如何改变可行域，但未构成真实导航链路闭环或多主动星协商实验。把“可用于闭环”与“闭环已验证”分别记录。

## 对综述的帮助

对现有4.3、4.4最有价值：新轨道信息可能改变规避必要性，采用的控制计划应随证据更新。拟增3.6.3可借它比较恢复目标、概率约束和再规划触发之间的关系。

这是后续写作的候选证据与组织建议，本批没有修改v3.2正文。文件核验不等于科学结论的人工终核。
