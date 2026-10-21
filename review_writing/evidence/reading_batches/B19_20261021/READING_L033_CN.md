# B19-L033｜卫星碰撞概率计算的一般方法

General Method for Calculating Satellite Collision Probability

- 作者：Russell P. Patera
- [正式文献入口](https://doi.org/10.2514/2.4771)；DOI：10.2514/2.4771。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Russell-Patera/publication/239414978_General_Method_for_Calculating_Satellite_Collision_Probability/links/55b7715308ae092e9657161b/General-Method-for-Calculating-Satellite-Collision-Probability.pdf)；版本：作者公开的7页正式版；JGCD 24(4), 2001, 716–722。
- 来源ID：E-B19-L033；叙述正文阅读范围为PDF物理页1–7，所读PDF共7页。
- 本地文本快照SHA-256：7e29cdc7727cc8faaf0ac7b82bd0b797e8b83ac0fe43dfb5c51a7a2dc52a356a。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：candidate_after_human_review；human_verified=false。

## 问题、输入与决策

怎样把碰撞平面的概率积分转为便于重复计算的形式？

旋转和缩放概率分布，再沿硬体投影边界做闭合路径积分；另处理原点被硬体包围的情形。

## 验证层级

与既有NASA相关程序比较，并用非球形发射器算例展示几何影响。

## 可追溯论点

- **C-B19-031**：主要推导假设交会段相对速度近似不变，并使用高斯位置误差。
  定位：PDF物理页2；Methodology Overview。
- **C-B19-032**：旋转与缩放将碰撞平面面积积分转成闭合轮廓积分。
  定位：PDF物理页2, 3, 4；Eqs.(10)–(26)。
- **C-B19-033**：硬体区域包含与不包含概率分布原点时采用不同表达。
  定位：PDF物理页4；Eqs.(26a),(26b)。
- **C-B19-034**：非球形物体以投影多边形边界表示，再累计各面的贡献。
  定位：PDF物理页5, 6；Asymmetric space objects; Eq.(38)。
- **C-B19-035**：算例的速度优势取决于积分步数、比较程序和当时硬件。
  定位：PDF物理页4, 5；CPU timings and 400/27-step comparison。

## 采用边界与阅读者判断

- “general”不能理解为已处理任意非高斯、长时非线性交会。
- 形状调整改变估计概率，不等于已给出可执行、可靠的姿态避碰策略。
- 不把历史约20倍速度结果当作现代通用性能指标。

## 对综述的帮助

作为建议3.6.2的基础方法；用它与L034、L036比较不同风险量及假设，不把计算速度和安全效果混为一谈。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
