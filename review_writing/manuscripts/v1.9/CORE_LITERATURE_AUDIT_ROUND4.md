# 第四轮定向原文核查（v1.9）

本轮新增原文正文定向核读两篇（[42][44]，均为公开作者/机构版），另核出版摘要/片段三篇（[23][33][63]）。没有新复现实验，没有完成五篇正式版本的全篇对照，作者终核仍待完成。

## [42] Joint Observation and Transmission Scheduling in Agile Satellite Networks

实际核读版本：2021 IEEE accepted manuscript; University of Toronto faculty-hosted PDF; 15 pages。来源：https://www.comm.utoronto.ca/~liang/publications/TMC_ObsTrans_ASN.pdf

- **R4-42-1** `author_version_only/supported`：以观测和传输时间窗联合调度、以成功安排的任务加权收益为目标；采用半正定松弛与遗传搜索
  - 原文定位：PDF pp.1–2 (§1), pp.9–12 (§4.2–5.2), p.13 (§5.4), Figs 3 and 6
  - 条件：模型依赖给定窗口、固定网络容量；不是所有任务和产品质量的通用度量
  - v1.9：p322a, p42a, t3, t6
- **R4-42-2** `author_version_only/supported`：系统模型忽略成像角度对图像质量的影响，并假设传输无误码
  - 原文定位：PDF p.4, §3.1, system assumptions; PDF image inspected for p.1 and p.12
  - 条件：不引申为真实链路可靠性及合格产品质量已经验证
  - v1.9：p322a, t3
- **R4-42-3** `author_version_only/supported`：时窗关联与窗内资源安排构成分层求解；与直接SDR对照，计算时间降低且图3任务收益接近
  - 原文定位：PDF pp.9–12, §4.2; §5.2 Fig.3
  - 条件：限于原作者STK/Matlab算例，不等于所有星座场景求解实时性
  - v1.9：p41a, p42a2

## [44] The integrated agile Earth observation satellite scheduling problem

实际核读版本：CIRRELT-2024-28 institutional working paper; 31 PDF pages; 2025 publication abstract separately inspected。来源：https://www.cirrelt.ca/documentstravail/cirrelt-2024-28.pdf

- **R4-44-1** `author_version_only/supported`：目标函数包含观测目标收益和已下传数据量两项
  - 原文定位：CIRRELT PDF pp.2–4 §1; pp.11–12 §3, objective (1) and discussion
  - 条件：下载体积与完成的目标/请求数量不可互作同一收益指标
  - v1.9：p24a, p322a2, p35b, p42a, p42c, t3, t6
- **R4-44-2** `author_version_only/supported`：改进整数模型以计算可处理性换取可能缩小的可行搜索空间，另用图结构简化和MIP邻域搜索
  - 原文定位：CIRRELT PDF pp.4–5 §1, pp.17–21 §4–5, Algorithm 1; publisher 2025 abstract
  - 条件：不同简化分别可能改变模型可行域或搜索算法；未复验解空间等价性
  - v1.9：p322a2, p41a, p42a2, t3, t6
- **R4-44-3** `author_version_only/supported`：作者机构工作论文在特定硬件/求解器上测试，示例数据由原卫星任务集划分成不同任务和卫星规模
  - 原文定位：CIRRELT PDF pp.22–23 §6.1, technical setup; formal publisher abstract
  - 条件：正式期刊全文逐命题对照未关闭；不得当作机载在线实时演示
  - v1.9：p41c, p42a2

## [23] On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation

实际核读版本：AIAA Journal of Spacecraft and Rockets formally published abstract, 3 Aug 2026; full body not newly read。来源：https://doi.org/10.2514/1.A36684

- **R4-23-1** `formal_abstract_only/supported`：正式出版摘要以卫星运营方维护成本/服务要求与在轨服务方定价/利润为两类决策目标
  - 原文定位：AIAA JSR published abstract 3 Aug 2026
  - 条件：仅出版摘要，不宣称全文条件或每个Pareto点的计算细节已经核实
  - v1.9：p31c2, p31d
- **R4-23-2** `formal_abstract_only/supported`：运营维护的经济改善发生在限定故障和服务条件下，不等同单次业务恢复时延已测定
  - 原文定位：AIAA JSR published abstract and scope
  - 条件：将单次恢复业务损失作为本文提出的进一步比较问题
  - v1.9：p31c2, p45a

## [33] A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites

实际核读版本：Elsevier Computers & Operations Research publisher abstract/highlights/Introduction excerpt, 2026; full body not newly read。来源：https://doi.org/10.1016/j.cor.2025.107259

- **R4-33-1** `formal_abstract_and_intro/supported`：结构化Dantzig–Wolfe分解、动态规划定价及能源约束构成算法主要结构
  - 原文定位：Computers & Operations Research 185 (2026) 107259, Highlights, Abstract and Introduction excerpts
  - 条件：没有取得正式技术全文，本轮不复验分支定价优化界与全部性能条件
  - v1.9：p321a, p41a, t3

## [63] Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites

实际核读版本：Elsevier Expert Systems with Applications publisher abstract/highlights and section snippets; full body not newly read。来源：https://doi.org/10.1016/j.eswa.2025.128502

- **R4-63-1** `formal_abstract_and_snippets/supported`：滚动时域将在线任务转为静态子问题；深度学习解码任务序列与资源选择，再以定制破坏—修复算子改进
  - 原文定位：Expert Systems with Applications 291 (2025) 128502, Highlights, Abstract and section snippets
  - 条件：没有取得全文；不使用摘要总收益百分比归因单独模块
  - v1.9：p323b, p43c, t3

## 综述归纳并非原论文实验结果

- **R4-SYN-1** `review_author_synthesis`，引用[42, 44, 53, 106]：同属联合观测和下传的两项研究可能采用任务加权价值与下传数据量不同的服务目标；跨模型对照必须先锁定指标与分母。；计入原文实验核验：**否**。
- **R4-SYN-2** `review_author_synthesis`，引用[33, 42, 44, 63]：为减少计算而改变求解过程、候选表示或模型可行域具有不同损失来源；应区分计算开销与解质量。；计入原文实验核验：**否**。
- **R4-SYN-3** `review_author_synthesis`，引用[18, 22, 23]：对能力恢复需要区分库存供应、资产到位、载荷可用和业务重分配，不能由经济维护收益直接推断恢复时长改善。；计入原文实验核验：**否**。
- **R4-SYN-4** `review_author_synthesis`，引用[9, 42, 44, 53, 106, 121]：资源连接方式的可用性受下游瓶颈、信息新鲜度和允许修改的时间窗共同约束。；计入原文实验核验：**否**。
