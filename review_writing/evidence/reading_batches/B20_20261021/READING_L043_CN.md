# B20-L043｜低推力避碰机动优化

Low-Thrust Collision Avoidance Maneuver Optimization

- 作者：Andrea De Vittori; Maria Francesca Palermo; Pierluigi Di Lizia; Roberto Armellin
- [正式文献入口](https://doi.org/10.2514/1.g006630)；正式卷期年：2022。
- [实际读取的公开PDF](https://re.public.polimi.it/bitstream/11311/1221750/11/DEVIA_OA_02-22.pdf)；版本：16-page repository postprint including cover; paired with 2-page correction DOI1.G006630.c1 read in this batch。
- 来源ID：E-B20-L043；叙述正文阅读范围：PDF物理页2–15；全文16页。
- 本地文本快照SHA-256：0f73a0d38d00847a971b5e237b51ef1f69993be0e2bd168ae72d8edbb05c634a。**该值不是PDF原文件哈希。**
- 正文通过公开PDF文本读取；PDF原件未成功归档，图表和公式的图像核查待完成。未独立复证明或复现实验。
- 采用状态：CANDIDATE_AFTER_HUMAN_REVIEW；human_verified=false。

## 问题与机制

如何快速生成低推力避碰初值，再得到有界燃料解？

比较ECI与B平面表达；解析能量解初始化数值燃料优化，并检查非线性传播。

## 验证层级

详细LEO算例、椭圆轨道测试、摄动检验及100事件计时；另读勘误。

## 可追溯论点

- **C-B20-016**：碰撞概率模型使用短时、恒定独立协方差和球形物体假设。
  定位：PDF物理页3, 15；SectionII.C; Conclusion, L1593–1597。
- **C-B20-017**：能量最优解可能超过推力能力，不能替代有界燃料优化。
  定位：PDF物理页7, 8；SectionIII.D, L899–1013。
- **C-B20-018**：ECI表达和该B平面动力学表达的适用条件并不相同。
  定位：PDF物理页2, 11, 13；SectionII.B; IV.A.3, IV.E, L178–180,L1285–1290,L1459–1469。
- **C-B20-019**：优化阶段忽略的摄动在后验传播中另作检查。
  定位：PDF物理页2, 13；SectionII.B L152–154; IV.D L1444–1457。
- **C-B20-020**：勘误涉及原式35–36、41–42、64及74，引用须配对。
  定位：PDF物理页5, 6, 7, 12；Original equations; separate correction physical pp1–2。

## 采用边界与阅读者判断

- 勘误文本已读，不计为额外一篇候选论文；原公式的图像核查与独立复现仍待完成。作者称结果有效性不受影响，不等于本次已独立验证。
- 读者判断：基于软件环境的计时是方法工程化的线索，不能写成已有星载实时运行证据；不把小推力与任意临近TCA时刻的可行性混为一谈。
- 读者判断：它解决单主动星对非合作目标的规避，缺少多主动星权限与策略协调机制。建议与多星论文对照，不能直接作为多星协同闭环案例。

## 对综述的帮助

现有3.1及4.4可用来区分“快初值形成—执行约束补入—传播复核”。与L042/L050比较，说明短时交会假设及后续运行目标如何影响优化形式。

这是后续写作的候选证据与组织建议，本批没有修改v3.2正文。文件核验不等于科学结论的人工终核。
