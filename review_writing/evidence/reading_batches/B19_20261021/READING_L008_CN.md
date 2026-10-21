# B19-L008｜利用差异升力与阻力的卫星编队飞行控制研究

Study of satellite formation flying control using differential lift and drag

- 作者：D. Ivanov; M. Kushniruk; M. Ovchinnikov
- [正式文献入口](https://doi.org/10.1016/j.actaastro.2018.07.047)；DOI：10.1016/j.actaastro.2018.07.047。
- [实际读取的公开PDF](https://www.researchgate.net/profile/Danil-Ivanov-2/publication/326572095_Study_of_Satellite_Formation_Flying_Control_Using_Differential_Lift_and_Drag/links/5b56dedc45851507a7c43eb3/Study-of-Satellite-Formation-Flying-Control-Using-Differential-Lift-and-Drag.pdf)；版本：作者上传的28页稿，2018；与期刊正式排版未逐页比对。
- 来源ID：E-B19-L008；叙述正文阅读范围为PDF物理页1–26，所读PDF共28页。
- 本地文本快照SHA-256：35b465a0e3ef2666f0fe0ff0a1b33ebeb6a3cf75a5a84f35fb4620a036efce50。这是文本快照哈希，**不是PDF原文件哈希**。
- 本批通过公开PDF的文本读取完成正文精读。PDF原件未成功本地归档；图表图像核查待完成。未独立复证明或复现实验。
- 采用状态：candidate_after_human_review；human_verified=false。

## 问题、输入与决策

LQR期望控制怎样转成实际可执行的差异升阻力？

由两星相对状态求LQR力，再反解帆板姿态；不可行时按轴优先实现替代控制。

## 验证层级

线性模型与含J2、GOST大气和参数误差的数值试验。

## 可追溯论点

- **C-B19-006**：差异升阻力的可达集合取决于两星姿态与气体表面作用参数。
  定位：PDF物理页3, 4, 5, 6, 7；Sec.1, Figs.3–5。
- **C-B19-007**：姿态反解可能没有解；所需力分量各自未超界仍不保证联合可行。
  定位：PDF物理页10, 11；Sec.2.2, Eq.(14)。
- **C-B19-008**：外包圆柱只是可达集合近似，内部仍有无法实现的控制。
  定位：PDF物理页12, 13；Sec.2.3, Fig.7 discussion。
- **C-B19-009**：作者以1000个初始偏差试验检查替代控制下的收敛。
  定位：PDF物理页24；Sec.3.3, Figs.21–22 discussion。
- **C-B19-010**：大气密度设定偏差会改变收敛，文中也展示发散情形。
  定位：PDF物理页25, 26；Sec.3.3, Figs.23–24; Conclusion。

## 采用边界与阅读者判断

- 没有显式碰撞概率约束，不可把构型跟踪收敛写成避碰认证。
- 所读稿含图号复用；按章节、公式和PDF物理页联合定位。
- 状态可准确取得及姿态执行近似是假设；真实传感误差、执行时延仍需补证。

## 对综述的帮助

用于建议3.6.1及4.4说明“规划给出的动作”还要经过执行可行性检查；外包可行域带来的遗漏应作为局限写出。

以上为阅读工作记录和后续写作建议，尚未写入v3.2。出处可追溯不等于科学结论已获人工认可。
