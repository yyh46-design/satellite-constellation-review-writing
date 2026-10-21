# B19-L030｜卫星碰撞概率计算的改进

Satellite Collision Probability Enhancements

- 作者：Salvatore Alfano
- [正式文献入口](https://doi.org/10.2514/1.15523)；DOI：10.2514/1.15523。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Salvatore-Alfano/publication/245432708_Satellite_Collision_Probability_Enhancements/links/5473bf6b0cf29afed60f5a3f/Satellite-Collision-Probability-Enhancements.pdf)；版本：作者公开的5页正式版；JGCD 29(3), 2006, 588–592。
- 来源ID：E-B19-L030；叙述正文阅读范围为PDF物理页1–5，所读PDF共5页。
- 本地文本快照SHA-256：d585328ff9c19767fc4b0e827163b2801673c7e41b1b73d650eff213a83ab1a7。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：candidate_after_human_review；human_verified=false。

## 问题、输入与决策

缺少姿态信息或协方差尺度不可靠时，风险估计应怎样表达保守性？

构造矩形物体的保守投影，在给定协方差形状条件下搜索姿态、尺度等变量对应的最大概率。

## 验证层级

参数化数值测试与一组历史SOCRATES配对的宽度因子统计。

## 可追溯论点

- **C-B19-026**：碰撞平面计算依赖短时、近线性相对运动等假设。
  定位：PDF物理页1, 2, 5；Simplified formulation; Conclusions。
- **C-B19-027**：未知姿态时，构造覆盖可能接触区域的投影再搜索方位。
  定位：PDF物理页2, 3；Unknown orientation formulation。
- **C-B19-028**：最大概率计算保持投影协方差轴比固定。
  定位：PDF物理页3；Maximum probability formulation。
- **C-B19-029**：最大概率对应的协方差尺度可用于提示需要更准确的轨道信息。
  定位：PDF物理页2, 3, 5；Maximum probability and data sufficiency discussion。
- **C-B19-030**：数值测试覆盖物体尺度、错失距离、轴比与方位的变化。
  定位：PDF物理页3, 4；Numerical Testing。

## 采用边界与阅读者判断

- 最大概率是指定模型与固定轴比下的结果，不是所有分布不确定性的统一上界。
- 历史样本及计算条件不能作为当前运营数据。
- 纸面扫描公式的OCR较差，精确实现与数值采用均待图像复核。

## 对综述的帮助

建议3.6.2区别名义Pc、条件最大Pc和数据是否足以支撑决策；4.3讨论观测更新而非立即机动的选择。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
