# B19-L071｜考虑碰撞避免的卫星编队—包容飞行控制

Satellite Formation-Containment Flying Control with Collision Avoidance

- 作者：Liangming Chen; Yanning Guo; Chuanjiang Li; Jing Huang
- [正式文献入口](https://doi.org/10.2514/1.i010588)；DOI：10.2514/1.i010588。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Liangming-Chen-2/publication/321781469_Satellite_Formation-Containment_Flying_Control_with_Collision_Avoidance/links/5f64b15e299bf1b53ede0834/Satellite-Formation-Containment-Flying-Control-with-Collision-Avoidance.pdf)；版本：作者公开的34页接受稿，题名Spacecraft；正式题名Satellite，2018。
- 来源ID：E-B19-L071；叙述正文阅读范围为PDF物理页1–26，所读PDF共34页。
- 本地文本快照SHA-256：210450a036d1b194f993a36a5c548325f32c60a05d9cefe660e8925a98ab0bd1。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：HOLD_pending_clarification_full_text；human_verified=false。

## 问题、输入与决策

配置形成与跟随星包容能否同时进行，并独立感知碰撞危险？

领航星形成目标构型，跟随星进入其凸包；协同状态经通信图交换，斥力通过近距测距触发。

## 验证层级

六颗领航星与四颗跟随星的平面、三棱柱数值例；附有Lyapunov分析。

## 可追溯论点

- **C-B19-046**：配置通信与近距离避碰测距在架构上分开。
  定位：PDF物理页6, 8, 9, 26；Secs.II.B and V。
- **C-B19-047**：假设领航图连通，跟随星可由领航星到达，且跟随子图无向。
  定位：PDF物理页12, 15；Assumptions1–3。
- **C-B19-048**：目标构型与最终包容位置须能容纳规定的安全距离。
  定位：PDF物理页11；Remark2。
- **C-B19-049**：控制组合速度匹配、动力学补偿、吸引项和斥力项。
  定位：PDF物理页13, 16, 17；Eqs.(15),(41)。
- **C-B19-050**：验证例包含六颗领航星和四颗跟随星。
  定位：PDF物理页17, 18, 23；Sec.IV, Cases1–2。

## 采用边界与阅读者判断

- Crossref登记后续澄清10.2514/1.I010588.c1；澄清正文尚未获得，科学采用暂HOLD。
- 不把凸包内部自动等同于任意外部障碍下的安全区域。
- 有限算例中的控制力大小不构成输入饱和下的统一可行性证明。
- 附录A仅阅读证明结构与收敛说明，未独立复证明；局部极小点等强断言不采用。

## 对综述的帮助

先留作3.4协同结构与建议3.6.3的对照候选；澄清未核实前不向v3.2写入安全定理。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
