# B14-S016｜故障场景下多小卫星巡检的鲁棒重规划

Robust Replanning for Multi-Agent SmallSat Inspection in Failure Scenarios

- 作者：Markus H. Iversflaten; Alexander Hansson; David C. Sternberg; Oliver Jia-Richards; Keenan Albee
- [书目/原文入口](https://doi.org/10.2514/6.2025-0183)；标识：`10.2514/6.2025-0183`。
- 实际版本：AIAA SciTech 2025；实际阅读DeepBlue公开位流11页作者稿。Crossref题名作者匹配；NTNU另标acceptedVersion，但未对两个仓储文件作字节比较。
- [实际下载全文](https://backend.production.deepblue-documents.lib.umich.edu/server/api/core/bitstreams/38580eb5-5623-4dfa-a7e5-3303f2f00922/content)；来源ID：`E-B14-S016`。
- 原始PDF SHA-256：`032ce829f06855d3d2b6e50aa00c659afbc8a14bfce078b3668d4c544b6b91ab`。
- 文件共11页；正文叙述精读PDF物理页1–9；关键原页视觉核查：3, 8。
- 证据角色：`multi_agent_failure_replanning`。
- 状态：AI正文精读完成，人工终核待完成；未逐式复证明、未独立复现、未作全页视觉审计。
- 本批为S011–S020专题补充，不占用原80篇池L编号。

## 研究问题

一颗巡检小卫星推进失效后，其他健康星如何更新障碍信息并快速改道，避免局部故障中断整个群体巡检？

## 输入、决策与协同机制

站体网格几何、各星路径及故障信息进入各自AD*规划器。短时近距离动力学采用Newton–Euler，并将站体坐标视为惯性系，明确忽略轨道相对运动；推力失效通过效能矩阵和偏置建模。

AD*在1 m三维位置网格上规划/修正路径，速度与姿态单独分配；PD加推力分配伪逆执行。对故障星插入外扩碰撞区，健康星重新选择通路。

复用既有搜索状态可较快得到路径，必要时重设膨胀参数换取更快的次优解。障碍膨胀和复杂站体几何影响搜索可行性；过大裕量可包围星体或迫使全量重规划。路径相交时序按名义安排假设，未形成一般调度算法。

## 验证设置与证据层级

MuJoCo SmallSatSim三服务星绕Lunar Gateway几何巡检，一星在10 s失效，另两星改道。M1 CPU初始规划约2.7/2.9 s；反应最优重规划3.3 s，重设膨胀后次优方案1.3 s。不同解质量不能视为同等最优性下的速度提升。

## 可追溯论点

- **C-B14-026**：本文采用短时近场Newton–Euler模型并明确忽略相对轨道动力学；Lunar Gateway是几何场景，不能写成地月轨道飞行验证。
  原文定位：PDF物理页3；Dynamics model及惯性坐标近似。
- **C-B14-027**：AD*接收其他星路径和故障排除区，但相交路径的名义时序按假设处理；故障可达区域的正式分析仍属未来工作。
  原文定位：PDF物理页3, 7, 8, 9；planning assumptions、exclusion zones及future work。
- **C-B14-028**：三服务星仿真中一星10 s失效，健康星重规划避开；该证据支持失效后的群体路径调整，不提供任意故障的安全认证。
  原文定位：PDF物理页7, 8, 9；MuJoCo case study及failure response。
- **C-B14-029**：反应最优重规划3.3 s，重设膨胀参数后1.3 s得到次优解；速度比较必须同时保留解质量和计算硬件条件。
  原文定位：PDF物理页8；M1 CPU planning-time比较。

## 适用边界与待核问题

- Lunar Gateway几何并不代表已仿真完整地月轨道相对动力学。
- 故障星可达区域的形式化计算列为后续工作，当前使用外扩排除区；不能称已具严格故障可达管。
- 名义路径穿越时序有假设，未处理一般异步冲突、通信延迟或同时故障。
- 平均数秒CPU用时不是硬实时上界，也没有飞行或硬件闭环验证。

## 对综述的作用

用于3.6.3补“执行失败—障碍更新—重新规划—计划采用”的链条，并在采用条件中加入重规划时延和解质量。

本节为阅读者整合建议，尚未写入v3.2。采用前由作者核对实际全文和版本；读者分析不冒充原作者定理。
