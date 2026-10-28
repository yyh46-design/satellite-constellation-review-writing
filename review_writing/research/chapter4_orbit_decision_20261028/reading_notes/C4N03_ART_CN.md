# C4N03_ART｜Transformers for Trajectory Optimization with Application to Spacecraft Rendezvous

作者：Tommaso Guffanti; Daniele Gammelli; Simone D’Amico; Marco Pavone。年份：2024。

实际版本：Stanford-hosted IEEE Aerospace 2024 author final; 13 pages; publisher text parity not checked。

[实际全文](https://slab.stanford.edu/sites/g/files/sbiybj25201/files/media/file/guffantigammellidamicopavone_ieeeaero24_final.pdf)。DOI：10.1109/AERO58975.2024.10521334。

PDF SHA-256：`11a1a29dca3d1a99305f410aede3dee93bd9432945037d46ada92125fad2ca61`。

本轮正文阅读：1–11 including appendix; references and biography checked for identity only。原页视觉核对：[9]。

采用：`ADOPT`。既有身份：No matched body-reading note in checked repository。本轮为AI正文阅读；未独立复现、未替代作者科学终核。

## 问题、模型与方法

航天器相对国际空间站完成交会，状态采用相对轨道要素，脉冲速度增量为控制；状态转移矩阵及RTN映射连接相对动力学、禁入区、航点和接近锥。Transformer依据历史状态、控制、剩余奖励及约束预算生成初始轨迹，随后由序列凸规划(SCP)求解原非凸问题。

论文比较直接预测未来状态与“学习控制—动力学传播状态”两种生成方式，后者保留所用模型下的动力学一致性；生成轨迹本身仍可能违反终态或路径约束。训练集400,000条，90/10划分；100节点、1–3轨时域、限定初始被动安全轨道族。控制对照固定SCP，分别用两点边值凸解、含航点/接近锥但不含禁入区的凸解和ART热启动。

## 可追溯论点

- C4-N03-01：学习负责初值，动力学传播和SCP分别承担状态演化与约束求解。定位：§3–4，pp3–6。
- C4-N03-02：较好初值的价值随凸松弛解对禁入区的违反程度变化；模型使用从初始即收缩的信赖域，突出初值影响。定位：p6、pp8–9图4–6。
- C4-N03-03：ART减少部分SCP迭代，但生成初值更慢，总时间大体相当；CVX的求解不可行率略低于ART。定位：pp9–10，图6。反例须与燃料收益一起保留。

## 采用方式

用于4.3的“学习辅助优化”段。百分比原意是相对凸下界的次优间隙改善，不等于总燃料同比降低；正文不引用这些百分比。所读为开环优化实验，鲁棒与闭环是后续问题，不能因相对运动模型包含扰动表达而声称完成不确定性闭环验证。已看p9原图。
