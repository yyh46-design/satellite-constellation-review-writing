# B19-L036｜利用等体积长方体计算卫星瞬时碰撞概率

Satellite Instantaneous Collision Probability Computation Using Equivalent Volume Cuboids

- 作者：Shuo Zhang; Tuo Fu; Defeng Chen; Huawei Cao
- [正式文献入口](https://doi.org/10.2514/1.g004711)；DOI：10.2514/1.g004711。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Shuo-Zhang-120/publication/342355766_Satellite_Instantaneous_Collision_Probability_Computation_Using_Equivalent_Volume_Cuboids/links/5ef0a4b2299bf1faac6cad26/Satellite-Instantaneous-Collision-Probability-Computation-Using-Equivalent-Volume-Cuboids.pdf)；版本：作者公开的19页带行号稿；接受状态未在稿内确认，正式文献2020。
- 来源ID：E-B19-L036；叙述正文阅读范围为PDF物理页1–16，所读PDF共19页。
- 本地文本快照SHA-256：a770535d235d94f5f77f49e7b479f4ad59246d290780cd1c26383f4f69b1815b。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：candidate_after_human_review；human_verified=false。

## 问题、输入与决策

怎样用较低代价近似计算非高斯相对位置的瞬时碰撞概率？

先分裂并传播高斯混合；将每项积分区域变换成椭球，再用等体积长方体近似，分解为一维积分。

## 验证层级

GEO和LEO两个数值案例，与数值积分、Monte Carlo及等体积球近似比较。

## 可追溯论点

- **C-B19-041**：本文主要风险量是固定时刻位于合成硬体内的概率。
  定位：PDF物理页1, 3；Sec.II, Eq.(1)。
- **C-B19-042**：分裂方向按线性传播的位置不确定性影响选择。
  定位：PDF物理页5, 6；Sec.III.A, Eqs.(5)–(10)。
- **C-B19-043**：等体积长方体把三维积分近似为三个一维积分的乘积。
  定位：PDF物理页9, 10, 11, 12, 13；Sec.IV, Eqs.(28)–(38)。
- **C-B19-044**：作者报告的LEO算例中，峰值概率存在约13%的低估。
  定位：PDF物理页15；Sec.V.B discussion of Fig.4。
- **C-B19-045**：论文明确指出该几何近似的误差难以解析估计。
  定位：PDF物理页16；Sec.VI final paragraph。

## 采用边界与阅读者判断

- 瞬时概率曲线不能直接求和当作累计交会概率。
- 等体积并不保留概率质量，因此不能把近似值默认作为保守上界。
- 13%来自正文报告，图像与正式版数字未终核；不纳入跨论文数值排行榜。

## 对综述的帮助

建议3.6.2明确瞬时与累计概率的区别；4.4说明近似误差可能影响阈值判断，需要校准和回退。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
