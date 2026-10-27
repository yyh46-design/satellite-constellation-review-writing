# N003_CMAS｜A Continuous Low-Thrust Maneuver Automation System for Electric Propulsion LEO Satellite Operations

作者：Luigi Mascolo; Zayne Thawer; Alex Paul。年份：2025。

实际版本：SpaceOps 2025, ID105，官方会议PDF。

原文：https://publications.spaceops.org/2025/download_by_id.php?id=0105

PDF SHA-256：`d94931e2c511975a07c18c813705a5d4b101d1cd158550653cd8b670b38133c1`

阅读范围：1–8全文。状态：BODY_READ_AI_NOT_AUTHOR_VERIFIED；human_verified=false。

既有来源：本轮前已核对来源台账未匹配；本批首次登记。采用：ADOPT_OPERATION_FEEDBACK。

本报告解释连续低推力机动如何进入Planet地面运行流程。其独立价值是计划、审批、执行评估与成像计划更新的接口，而不是某个轨道优化算法的性能提升。

架构与机制：LCP负责单星生命周期层的任务要求，CMAS生成具体有限时长机动。Constrained Orbit Box描述高度和偏心率等容差；Maneuver Opportunity Box描述占空比、机动位置及保护时段。pp3–5将候选机动与无机动传播比较，用informed merit function利用自然摄动，再在开始时刻、持续时间和方向的候选中选取方案。

执行链：pp5–6区分预留、动作、审批和执行评估；遥测与定轨识别未执行、部分执行或完成的机动，并更新后续任务。§4.2 p6将成像任务与维持交错，在机动计划、执行或取消后刷新成像时刻和指向。这使任务机会成为随实际轨道重新计算的量，而不是一次规划后不变的输入。

证据强度：这是运营方系统设计与运行经验报告，无受控算法对照和直接业务增益统计。p7 §5.4把星座级管理器放在未来工作中，不能把约20颗有推进能力的运营星数视为该系统已验证的多星联合控制规模。接近筛查和相应审批仍属运行链的一部分。

写作采用：4.3补充机动结果如何反馈业务安排的积极机制；不把“自动化”改写成全自主授权或全星座安全保证。

## 可追溯论点

- C-N003-01：机动计划、执行、取消后更新成像时间与指向，执行后状态反馈未来任务。定位：p6, §4.2。边界：运营架构证据，无匹配业务增益试验。

- C-N003-02：星座级管理器属于未来扩展。定位：p7, §5.4。边界：不能把运营舰队星数计为联合控制验证规模。
