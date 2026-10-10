# 核心工程案例：研究型技术卡片（2026-10-09截点）

> 此处是为综述第2–4章精选的**16组重点案例**，总库另外有54个工程事件/项目。每组均明确区分：实际披露事件、可支持的论文主张、不可直接推断的内部算法或性能、需要进一步查询的资料。案例ID用于研究追溯，不进入期刊正文。公司材料需标“运营方披露”；NASA/ESA/NOAA材料为官方任务或政府服务资料，仍需根据原文确定演示范围。

## A｜在用商业业务及真实调度接口

### 1. Starlink：从轨道预报到自主避碰的运营闭环（EC001—EC003）
**已确认的公开工程流程。** SpaceX发布的[Starlink Collision Avoidance CONOPS](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/)说明：卫星GNSS滤波状态形成多日轨道预报；与其他运营商星历和空间目标预报筛查形成CDM；CDM上传卫星后，星载系统实时重算碰撞概率/最近距离并选择新增、修改或取消规避动作。运营方自报通常每天实施**超过1000次**规避机动。其文档还区分健康在位卫星、转轨卫星、硬件降级卫星以及不可机动/失能卫星的阈值和人工介入方式。健康在位卫星的典型自动规避触发阈值为碰撞概率约`3×10^-7`，目标约`1×10^-7`，通常在TCA前12小时以内规划；转轨时的阈值、规划窗口有所不同。

**论文用途。** 放在3.3“检测—风险评价—机动—后续筛查”的真实运营案例，也适合2.4展示连续反馈和3.4展示运营方协调接口。其覆盖的是公开CONOPS所述实际流程，而不是需要我们凭空猜测的机载算法。

**关键边界。** 企业自报的机动次数和阈值不是独立第三方验证的漏检/失效率；文档也不提供全部传播器、控制器源代码或优化求解证明。“自动规避”不等于“绝对无碰撞”。遇到无法机动或无法充分降低风险时，CONOPS明确保留人工处理。**需核**：文档发布版本、统计时间窗、与最新FCC风险报告的数字差别。

### 2. Planet：商业任务请求并不等于成功交付（EC017—EC019）
**已确认的接口。** [Planet Tasking API](https://docs.planet.com/develop/apis/tasking/)公开从客户任务请求、排程、成像、质量判定、重新尝试到产品交付的生命周期；[Pelican/SkySat任务接口](https://docs.planet.com/develop/apis/tasking/constellations/)体现同一客户服务可调用不同载荷与卫星。Planet在[Pelican 2025任务总结](https://www.planet.com/pulse/pelican-2025-in-review/)中披露Pelican进入任务业务，后续又公布低时延通信技术试验。

**论文用途。** 3.2利用真实接口解释数学模型里“任务被接受”“卫星完成观测”“质量合格”和“产品送达”不是同一指标；3.4讨论调度与通信、处理、客户交付的数据接口。

**关键边界。** 外部Tasking API只披露客户可见状态，不代表Planet内部算法采用整数规划或强化学习。客户采购界面和在轨数据链路内部运行的时效性不可混写。**需核**：质量未达标自动复采的具体产品政策和API版本。

### 3. Capella与Umbra：商业SAR任务的优先级与接受状态（EC022—EC023）
[Capella tasking文档](https://docs.capellaspace.com/constellation-tasking/tasking-requests/)公开任务目标、时窗、成像模式及不同优先级；[Umbra Canopy](https://docs.canopy.umbra.space/docs/tasking)公开客户任务输入、排程和产品状态。

**论文用途。** 与Planet形成横向对照，说明商业遥感业务对“任务窗口、优先级、客户交付约束”的实际需求；可作为设计调度目标函数的**应用需求证据**。

**关键边界。** 无法由API推算星座最大可接受任务量、内部排程机制、失约率或优化解质量。应优先比较接口语义，不进行企业算法排名。

### 4. 商业光学中继：Kepler、OroraTech及EDRS（EC015、EC028、EC069）
[Kepler 2026年8月24日公告](https://kepler.space/kepler-delivers-optical-infrastructure-for-real-time-space-operations/)称首批光学中继网络已完成调试并开始向商业客户交付服务，具备跨轨道面、星间及星地光链路操作；其在轨计算模块说明另列EC016。OroraTech则在2026年1月公布热红外载荷与Kepler通信基础设施的合作。更成熟的[Airbus SpaceDataHighway](https://www.airbus.com/en/products-services/defence/military-space/space-data-highway)和[ESA Sentinel-2数据流说明](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2/Data_flow)确认LEO-GEO中继能够将观测数据经GEO转送地面，提高不直接处于地面站可视区时的数据下传机会。

**论文用途。** 3.2和3.4讨论“观测任务调度”为什么必须同时考虑时变通信网络、星上计算、延迟与交付；空间中继的存在使数据交付不再仅依赖卫星下一次过境地面站。

**关键边界。** EDRS的名义激光链路速率与实际端到端时延并非一回事；Kepler商业服务状态依据公司披露，具体用户链路日志待核。OroraTech发射载荷不证明计划中的全球热红外直播已经全面投入服务。

### 5. 商业地面站API：AWS、KSAT与Leaf（EC055—EC058）
[AWS Ground Station contacts](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html)支持通过SDK/CLI排程联系、取消或重排；其[Contact versioning](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.versioning.html)说明当轨道数据或任务发生变化时如何更新已有联系人状态。KSATlite通过[REST/M2M调度](https://www.ksat.no/ground-network-services/ksatlite/operations-and-scheduling/)接受过境预约与确认；[Leaf Space智能排程](https://leaf.space/inside-the-scheduler/)公开96小时滚动、任务约束请求、按需与专属访问等容量模式。

**论文用途。** 3.2把“地面天线时间窗”解释为具有实时预约、容量抢占、状态反馈、取消与版本一致性条件的工程资源；比较商业运行中可接受的任务状态定义和服务等级。

**关键边界。** APIs可以说明**实际使用的接口与约束**，无法证明各家内部优化器的算法及全局最优性。Leaf的滚动无冲突以其产品规则为条件，不能代表全世界天线资源不存在冲突。

## B｜实际运维与故障、在轨服务

### 6. Axelspace：同一星座同时有恢复与失败案例（EC030—EC031）
2026年1月，[Axelspace披露GRUS-1E恢复商业采集](https://www.axelspace.com/news/grus-1e_commercial_operations/)；在2026年7月GRUS-3七星批次发射后，[9月29日公司报告](https://www.axelspace.com/news/grus3_20260929/)4星高速下传系统异常；[10月6日后续说明](https://www.axelspace.com/ja/news/grus3_20261006/)进一步认定四颗卫星的**高速下传部分为永久故障**；公司推测原因与射频功率放大器散热不足有关，并建立外部专家评估机制。四星其他设备及低速遥测仍可工作，未立即安排离轨；其余三颗计划降低通信功率并缩短下传时长，商业运行目标推迟至**2027年2月**。

**论文用途。** 3.1、3.3和3.4讨论：发射/入轨成功不等于产生可售服务能力；故障会使星座可用任务容量下降，甚至同一批卫星出现共同子系统风险；运维系统需要记录局部功能恢复与最终业务恢复的区别。

**关键边界。** 不能将高速下传故障说成整个卫星“已失去所有通信”；也不能猜测故障根因超出公司披露的电力放大器电路调查结果。GRUS-1E的恢复与后续终止应当按时间分开。

### 7. Iridium：备星部署与slot-swap的真实运营（EC007—EC008）
[Iridium 2019年完成NEXT部署](https://investor.iridium.com/2019-01-11-Iridium-Completes-Historic-Satellite-Launch-Campaign)，公布6轨道面共66颗主要运营卫星，并在新旧星交接中采用在轨slot-swap流程。[2023年补备星公告](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites)披露新增5颗备星、当时共有14颗在轨备星。

**论文用途。** 给3.1长期库存和重构方法提供现实操作案例：备用资产的几何位置、替换动作和任务恢复能力不能简化为“一个库存单元”。

**关键边界。** 2019/2023的卫星数是事件年份口径，非2026实时状态；Iridium的方法不等同于所有LEO星座的标准替换流程。

### 8. Northrop SpaceLogistics：MEV服务船复用已有飞行事实（EC036—EC037）
[Northrop官方技术记录](https://www.northropgrumman.com/what-we-do/space/space-logistics-services)确认，MEV-1于2020年2月25日对接Intelsat IS-901提供五年GEO延寿服务，2025年完成后又对接新客户；MEV-2于2021年4月12日对接IS-10-02。

**论文用途。** 3.1说明服务船配置、部署和后续任务排序确实具有商业应用；可以为“单服务船服务多个客户”提供实际基础，也为比较在轨服务与购买新星成本提供应用动机。

**关键边界。** GEO稳定目标的喷嘴对接与LEO密集星座中的非合作捕获差异显著，不将现有成功直接推导为低轨自主批量清除的经济最优性。

### 9. Astroscale ELSA-d：合作目标、推力异常与捕获中止（EC039—EC040）
[ELSA-d任务](https://www.astroscale.com/en/missions/elsa-d)在2021年8月完成与自带合作客户的重复磁性捕获演示；2022年自动保持相对距离约30m超过7小时后，团队因异常中止进一步自主捕获，后续在推进器能力受限时重新规划，并于2024年进入服务星的离轨操作。[详细事件记录](https://www.astroscale.com/en/news/astroscales-elsa-d-mission-successfully-completes-complex-rendezvous-operation)。

**论文用途。** 第3.3节可以同时描述成功技术演示和受限状态下的**安全退出与恢复规划**；第4章讨论在轨执行证据为什么必须按动作划分。

**关键边界。** 不能把ELSA-d合作目标的磁性捕获等同于捕获真实未知碎片，亦不能把中止的自主捕获写为已经成功。

### 10. Astroscale ADRAS-J：非合作目标15米接近与自主中止（EC041—EC042）
[2024年12月原始公告](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris)报告ADRAS-J在轨对真实失效火箭级接近至约15m并进行近距离观测。星载系统在检测异常相对姿态后自主中止，退回安全距离；[2026年3月任务更新](https://www.astroscale.com/en/news/astroscales-adras-j-mission-completes-operations-begins-deorbit)说明其自身开始离轨。后续ADRAS-J2才计划尝试目标移除。

**论文用途。** 3.3讨论接近窗口、非合作目标观测、FDIR、主动安全退出；第4章用来说明科学论文中的“满足轨迹约束”和在轨执行中“遇异常时安全退出”需要不同验证。

**关键边界。** **15m接近不等于完成捕获或碎片移除。** 这类成功中止不应被归入“服务任务完成率”。

### 11. Starfish / Impulse：自主视觉接近与故障后的任务降级（EC044、EC047）
Starfish与Impulse在[2025年12月Remora试验](https://www.starfishspace.com/press-release/starfish-space-completes-autonomous-rendezvous-and-proximity-mission-in-leo-with-impulse-space/)中使用单摄像头与闭环软件，引导一艘Mira向另一航天器接近约1.25km（未对接）。另据[Impulse LEO Express 3任务日志](https://www.impulsespace.com/updates/leo-express-3-mission-updates)，星敏感器测量噪声造成姿控推进剂消耗过大，运营团队改用太阳敏感器，最终主推力机动无法执行；之后软件与姿态控制获得部分恢复、若干客户载荷完成部署。

**论文用途。** 3.3的控制策略选择、物理资源消耗与故障后计划降级；3.4的运营反馈与可完成任务集之间的联系。

**关键边界。** 相对接近1.25km不表示最终6维交会成功；恢复姿态控制不代表推进剂损失和原计划机动也得到恢复。

## C｜跨运营方空间交通与公共验证

### 12. NASA Starling × Starlink：模拟风险、真实机动（EC049、EC059）
[NASA 2025年3月正式报告](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/)披露Starling和Starlink通过风险协调系统建立运营方间责任划分与星历交换，在**模拟接近事件**中由Starling自治规划并实施真实在轨机动。NASA[Starling完整任务说明](https://www.nasa.gov/smallspacecraft/what-is-starling/)另记载4颗CubeSat完成分布式状态共享、计划与协作行动试验。

**论文用途。** 将第3.4节学术上的“多代理协同”与实际跨运营方轨道数据和机动责任分配连接起来，另可用于3.3安全执行。

**关键边界。** 不可将模拟危险接近的演习叙述为成功避免了一次现实撞击；四颗星的实飞演示不能直接推导百星规模的收益和稳定性。

### 13. NOAA TraCSS：民用大星座筛查和公开验证基准（EC052、EC070）
[NOAA官方项目页](https://space.commerce.gov/traffic-coordination-system-for-space-tracss/)截至2026年8月披露82家试点组织、其账户合计关联11,370余颗在轨卫星以及10个政府账户；[2025年5月Increment 1.2说明](https://space.commerce.gov/tracss-implements-program-increment-1-2-on-demand-ephemerides-screening-and-bulk-submissions-now-live/)介绍按需星历筛查与批量提交（一次可提交数千条）。另外，[政府公开TCA算法测试数据集](https://space.commerce.gov/dataset-for-conjunction-assessment-verification/)提供星历、两个筛查体积配置下的CDM结果以及操作说明，供提供方自测。

**论文用途。** 对第3.3节说明TCA在大型星座中需要规模化运营接口；第4章则可展示有原始数据、答案表和可说明局限的公共基准，比泛谈“应加强算法验证”更具体。

**关键边界。** 11,370余颗指已纳入项目的相关卫星口径，不等于完全由TraCSS自动执行规避；政府明确声明测试集**不是完整真实工况覆盖，也不能用于正式认证或实际运行**。

## D｜在轨自主计算与软件验证

### 14. NASA EO-1 / IPEX：单星自主的工程演化（EC060—EC061）
[NASA EO-1任务记录](https://ntrs.nasa.gov/citations/20060050174)展示星上自主科学处理与运行规划；[JPL IPEX资料](https://ai.jpl.nasa.gov/public/projects/ipex/)说明使用CASPER持续任务规划/重规划，在CPU、存储、电能和带宽约束下决定图像分析与产品下传，JPL报告产生31,000余份星上图像产品。

**论文用途。** 在第3.4节形成真正的历史技术链：自主科学处理—资源状态感知—连续计划更新—产品下传，而不把所有能力一概解释为深度强化学习。

**关键边界。** 两者都是单星技术；JPL自报的100%可靠性是特定任务及其定义，不能代表全星座故障条件下的通用可靠度。

### 15. ESA OPS-SAT / Φsat-2：软件在轨试验与实际数据产品（EC062、EC065）
[ESA OPS-SAT](https://www.esa.int/Enabling_Support/Operations/Mission_complete_for_ESA_s_OPS-SAT_flying_laboratory)是允许高校与企业上传软件开展真实在轨操作实验的开放实验平台，任务于2024年5月结束。[Φsat-2正式任务报告](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Phsat-2/Phsat-2_begins_science_phase_for_AI_Earth_images)确认2025年完成约九个月调试进入科学阶段，利用星上AI开展云区筛除、船舶和灾害等图像处理。

**论文用途。** 第4章可以从“提出算法”走向“在某一计算、载荷和操作体系下经飞行验证”的判断；第3.2节可以展示星上智能处理与任务交付的联系。

**关键边界。** 上传运行某软件不意味着算法已被充分性能验证；单星图像处理也不自动包含多星任务重分配。

### 16. 数据中继与科学运行：Φsat和EDRS共同说明的系统接口（EC065、EC069）
[ESA Sentinel-2数据流](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2/Data_flow)明确观测数据可以通过X波段直接下传，也可以通过EDRS激光链路经GEO转送地面；而Φsat-2展示了星上推理产出部分信息产品的情况。它们提供了同一任务链条的不同真实组成部分：**载荷采集、星上处理、链路选择、地面交付**。

**论文用途。** 将3.2节的多资源联合调度从“优化任务数”推进到“优化按时交付有用信息”的实际工程逻辑。

**关键边界。** 它们来自不同任务系统，不能拼接成“某星座已经同时实现星上AI和GEO激光中继的完整自治优化”；论文应明确只是通过对照展示系统接口需求。

---

## 如何将工程案例用在最终正文

推荐每个技术专题**少量、高价值、与学术论文紧密对应**的案例，而非连续列公司名。写作时先介绍对应论文的数学模型、方法和实验，再用一段实际运行案例说明应用场景或验证范围，最后进行同条件或有边界的比较。

**来源优先顺序**：独立同行评议的真实飞行论文或机构官方任务报告 > 企业工程操作文档/API/运行日志 > 公司正式状态公告 > 商业推广/规划。来源等级不代表真实性的绝对排序；每项具体性能还需知道测量条件、独立验证与时间点。

**反向证据**：工程故障及安全中止并非“不成功就不可引用”。对星座系统而言，失败发生时是否保护卫星、是否报告真实剩余能力、是否修复计划，是单纯正向演示通常无法回答的研究问题。
