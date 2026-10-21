# B19-L034｜高斯混合轨道不确定性下的碰撞概率

Collision Probability with Gaussian Mixture Orbit Uncertainty

- 作者：Kyle J. DeMars; Yang Cheng; Moriba K. Jah
- [正式文献入口](https://doi.org/10.2514/1.62308)；DOI：10.2514/1.62308。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Yang-Cheng-25/publication/259293060_Collision_Probability_with_Gaussian_Mixture_Orbit_Uncertainty/links/02e7e52acef1ea312c000000/Collision-Probability-with-Gaussian-Mixture-Orbit-Uncertainty.pdf)；版本：作者公开的17页接受稿；正式文献为JGCD 37(3), 2014, 979–985。
- 来源ID：E-B19-L034；叙述正文阅读范围为PDF物理页1–14，所读PDF共17页。
- 本地文本快照SHA-256：386c80ee521e50ef88e38a36996e621bae193a18212464f5f6440e090aebe377。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：candidate_after_human_review；human_verified=false。

## 问题、输入与决策

稀疏观测导致非高斯状态分布时，怎样计算时间区间内风险？

把两对象状态表示成高斯混合，以进入硬体表面的概率通量计算概率率，再随时间积分。

## 验证层级

弱观测对象与良好跟踪对象的交会算例，并与Monte Carlo结果比较。

## 可追溯论点

- **C-B19-036**：累计碰撞概率与某一瞬时位于硬体内的概率通常不相等。
  定位：PDF物理页3, 4, 5；Sec.II, Eqs.(1)–(4)。
- **C-B19-037**：概率率积分的适用性包含单次穿越条件。
  定位：PDF物理页4；Sec.II, discussion after Eq.(3)。
- **C-B19-038**：两个对象的独立状态分布形成分量两两组合的相对分布。
  定位：PDF物理页5, 6；Sec.III, Eqs.(5)–(11)。
- **C-B19-039**：计算包含速度不确定性，并对球面及时间积分使用数值求积。
  定位：PDF物理页7, 8；Sec.III, Eqs.(12)–(13)。
- **C-B19-040**：验证例以2500万次Monte Carlo与高斯混合计算对照。
  定位：PDF物理页11, 12, 13；Sec.IV, Figs.2–4。

## 采用边界与阅读者判断

- “两对象独立”不等于位置与速度相互独立。
- 相对状态定义与Eq.(8)中均值符号表述需对照正式版，精确公式采用HOLD。
- 一次算例的吻合不能推出所有稀有事件都已校准，也不能把重复穿越累加当作概率。

## 对综述的帮助

建议3.6.2解释长期、低相对速度和稀疏观测为何需要额外假设检查；4.4引入估计更新和风险重算接口。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
