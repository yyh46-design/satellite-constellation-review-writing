# 任务驱动的大型卫星星座轨道设计、构型演化与协调运行综述

## 摘要

大型卫星星座的业务能力取决于成员在何时、何地形成可用的观测与通信机会，以及这些机会能否在轨道、资源和安全约束下转化为实际服务。轨道构型决定机会的空间分布与时间结构，摄动、维持和重构则持续改变这一基础。本文围绕任务需求与轨道行动的相互作用，比较构型设计、部署与维持、需求响应重构及多星协调方法。文献分析表明，覆盖率、平均重访和最长服务间断对应不同的构型选择；利用自然漂移形成或调整构型，需要同时计入到位时间和等待期间的业务代价；差动阻力和低推力机动的价值还取决于供电、载荷可用时段及成员剩余能力。决策组织应随依赖范围和响应期限确定：当轨道选择改变后续任务机会，或资源预算连接多个阶段时，部分联合建模能够保留这些联系；分层求解则需要传递足以表达相互约束的机会、占用和控制余量。多星共同安全进一步依赖相容的控制输入与动作时序，恢复效果应结合能力到位、计划启用和实际业务满足评价。现有研究支持上述机制及若干研究内部的条件性比较，其向大型星座的推广仍需结合主动成员数量、跨组竞争和信息时效分析。未来重点是建立任务价值与可维持构型之间的联系，形成可事前判断的决策范围选择依据，并用同一处置事件中的业务结果评价恢复方法。

**关键词：** 大型卫星星座；轨道构型；轨道摄动；构型维持；需求响应重构；多星协同；业务恢复

## 1 引言

卫星星座的运行问题始于任务对空间与时间的要求。区域观测关注目标何时进入视场、两次访问间隔多长以及数据何时交付；分布式测量还要求成员间形成特定的相对几何。轨道设计为这些活动提供机会，任务规划从中选择活动并配置资源，运行监督则根据实际状态更新后续安排。大型分布式卫星系统的自动化研究已将规划、监测和轨道管理纳入相互联系的运行职责[1]。对这些职责的综合，需要进一步解释它们为何相互影响，以及哪些决定应共同处理。

轨道动力学使这种联系具有鲜明的航天特征。初始几何随摄动演化，构型维持占用推进能力和可用时间，轨道重构改变后续覆盖与接触条件。因此，任务需求既是轨道设计的输入，也是评价轨道行动是否值得实施的依据。仅以末态构型或推进剂消耗评价一种方法，容易遗漏到位之前的业务等待、机动期间的活动中断，以及各成员剩余能力的差异。

本文关注的问题是：任务需求如何转化为星座构型和轨道行动，轨道演化与机动能力又如何限制任务执行，并影响维持、重构和任务调整的选择？围绕这一问题，初始设计用于解释业务机会从何而来，构型演化用于解释机会为何改变，协调运行用于解释多个成员如何形成可执行的行动。不同阶段通过时间窗口、资源占用、控制余量和任务价值联系起来。

本文采用问题导向的叙述性综述，选择能够说明上述联系的代表研究。构型与轨迹论文用于解释物理机制和可行条件，规划论文用于比较变量选择及求解组织，任务报告用于分析实际执行约束。单星实验和小编队研究可解释局部机制，其验证规模与大型星座的运行能力分别讨论。下文依次分析任务指标到构型的转换、构型演化与机动选择，以及多星协调和业务恢复，并据此提出需要进一步研究的问题。

## 2 从任务需求到可实现的轨道构型

### 2.1 任务指标决定构型优化的目标

构型设计首先需要明确任务要求的是持续可见、较高覆盖比例、较短平均等待，还是对最长服务间断的限制。这些指标对应不同的时间结构。相同的覆盖总时长可以集中在少数时段，也可以分散为多次访问；平均重访较短的构型仍可能保留一次较长间断。因而，卫星数量和覆盖率适合描述部分能力，构型选择还需要与任务允许的间断方式对应。

Lee等将种子卫星的访问序列、成员相位分布和目标覆盖序列联系起来，通过循环卷积构造二元整数规划，在给定轨道族内选择满足时空变化覆盖要求的成员位置[2]。该方法将对称分布之外的候选纳入搜索，尤其适用于各目标、各时段要求不同的区域任务。这里的优化对象是给定种子轨道和离散表示下的星座模式；覆盖序列的满足仍需后续运行条件支撑。

Rogers等的五类模型及其公开配套实现进一步区分了覆盖成本、覆盖比例、观测奖励、最大重访和平均重访目标[3]。作者公开的西雅图单目标算例中，两个方案均配置5颗卫星：最小化最大重访的方案，最大和平均重访分别为22 min和14.95 min；最小化平均重访的方案，相应为44 min和12.43 min。该对照采用相同的候选轨道族和离散周期，数值说明两种指标会选择不同的访问时间分布。这些数值来自作者配套仓库的结果表，而非本文重新求解。

由此，面向任务的构型设计应把业务允许的最长等待、重点时段和空间差异直接表达为约束或目标。对于具有硬期限的任务，平均指标主要用于比较满足期限后的效率；对于允许迟到的业务，则可依据等待或延迟代价评价不同构型。二者对应不同的任务模型，不能以同一种“覆盖改善”概括。

### 2.2 部署时间把几何候选转化为可到达候选

任务性能较好的构型还需要在规定时间内形成。Gwon和Ahn将停泊轨道与目标轨道之间的差异节点进动纳入候选筛选，再选择注入条件、成员及运载分配[4]。在其设计级近似中，可积累的升交点赤经差由相对进动速率和可用驻留时间共同决定，可写为

\[
\Delta\Omega_{\mathrm{avail}}\approx
\left|\dot\Omega_{\mathrm{parking}}-\dot\Omega_{\mathrm{target}}\right|
T_{\mathrm{dwell}} .
\]

这一关系使任务所需的轨道面分布受到部署期限约束。它描述的是J₂差异进动提供的节点分离，具体转移持续时间和其他运行限制还需另行计入。

自然漂移的价值由此具有时间条件。允许较长等待时，部分轨道面分离可以通过漂移积累；要求较早形成能力时，可达候选随可用驻留时间缩小。对构型设计而言，部署完成时间应与覆盖指标共同进入比较。对运行规划而言，尚未到位的卫星也应按实际可用时刻进入资源集合，而非从计划开始就提供全部能力。这是从部署模型延伸到运行接口的综合判断。

### 2.3 几何机会如何转化为任务完成

轨道构型提供的访问机会还要经过资源分配才能形成业务结果。He等在给定轨道下共同安排观测和传输，并与使用相同算法、分别优化两个环节的基线比较[5]。在三颗观测星、12 h仿真及所测业务期限内，原文图示中的联合方案取得更高的任务加权完成收益。图示未附可直接引用的差值表，分开基线的变量固定次序也未充分展开，因而适合用于说明该模型中上下游选择的联系。

这一结果为轨道设计与运行评价提供了衔接：新增观测机会的业务价值取决于是否存在后续处理、存储和交付条件。当这些条件成为主要约束时，继续优化几何覆盖可能无法获得相应的完成收益。构型层因此需要接收运行层返回的容量和期限信息，运行层也需要获知轨道调整将改变哪些未来机会。

## 3 构型演化、维持与需求响应重构

### 3.1 测量几何与可维持性共同决定构型

构型维持的目标应由任务所需的相对几何确定。Leroy等研究的大气内重力波层析任务，需要利用略有倾角差的立方星展开二维掩星采样；倾角差同时造成不同的J₂节点退行速率，使成员逐渐分散[6]。其维持方法按升交点赤经偏差触发机动，最大加速度限制可维持的分离程度，总速度增量预算限制任务寿命。推进持续时间还影响精密定轨条件及掩星测量的可用时段。

这一案例把任务设计中的两种要求联系起来：测量希望获得足够的空间展开，控制系统需要承担维持这种展开的代价。较大的几何分离是否有利，需要连同维持能力、寿命和有效测量时间评价。由此可提出一种面向任务的设计思路：先确定满足测量要求的构型范围，再在其中比较长期可维持性，而非始终以最小构型误差作为唯一目标。这是基于机制的综合，不是该案例已验证的通用最优设计准则。

### 3.2 差动阻力的关键是可持续使用的姿态和时间

差动阻力通过改变迎风面积调整轨道衰减及相对沿轨运动，其吸引力在于减少推进剂需求。但实施动作通常需要改变姿态，因此气动力、发电和载荷运行必须同时考虑。Hull等报告的EO-1试验提供了直接的运行例子：一次低阻力姿态因供电不足进入安全模式，另一次因星敏感器过热中断[7]。这项单星试验揭示了姿态持续时间的实际限制，不能视为多星自主控制的飞行验证。

Kim和Yoon在两星调相模型中共同描述阻力面积与发电投影面积，并依据日照和电池状态切换调相、充电模式[8]。该研究说明控制目标可以从瞬时阻力差扩展到持续可用的调相能力；其中一组对照的任务姿态限制不对称，相关增益仍需按其设置解释。两项研究共同提示，控制器应选择平台能够持续保持的动作，而不是仅追求最大的瞬时控制效果。

成员数量增加后，姿态可用性还会转化为协调问题。S-NET规划把通信、值守等活动纳入运行可用率，并处理多个星对共享参考星时的切换冲突[9]。各星对独立计算的高、低阻力切换不能直接同时执行，论文通过延迟部分机动开始时刻同步共同切换。该序列属于规划和未来演示建议，其价值在于揭示共享成员如何连接原本局部的控制问题。

因此，差动阻力的任务收益应由调相时间、轨道高度损失和活动可用率共同描述。较长的等待可以换取较低推进剂需求，但等待期间是否能够继续承担业务、多个星对是否争用同一成员，决定了这一取舍在运行中是否有价值。这里需要传递到任务层的量，包括允许姿态及其持续时间、控制活动占用和预计到位时刻。

### 3.3 目标构型、成员指派和转移控制的职责

重构包含三个相互联系的选择：确定目标构型，决定成员与目标位置的对应，以及规划到位过程。Arnas和Linares利用均匀分布的对称性及槽位兼容关系研究星座扩容、缩减和重新分布[10]。这些关系可以减少目标构型的搜索，并在所设几何和槽位条件下分析最小间距。有限时长转移中的推进约束和安全要求仍应在轨迹层表达。

相对轨道要素为目标几何与控制动作提供了直接联系。Gaias和D’Amico在近圆参考轨道的相对运动模型中分析多脉冲重构[11]：相对半长轴可以通过自然漂移积累沿轨变化，机动位置则影响相对偏心率等要素的改变。将终端时刻纳入模型后，可比较不同机动组合在给定转移时间内的代价。此时，允许等待多久、何时可以机动，本身就是方案选择的一部分。

成员指派也会改变轨迹代价。Appel等利用相对终端条件联立成员转移，在其案例中，总推进剂减少仍可能伴随个别成员消耗增加[12]。对于需要持续运行的星座，这意味着总量目标之外还应保留逐星剩余能力：同一总成本可能对应不同的后续可用成员集合。

三类选择的组织可据此确定。目标位置和转移代价相对稳定时，可先生成构型，再以代价表连接指派与轨迹求解；当目标位置、到位时间或成员剩余能力会改变可行对应关系时，则需要反馈更新，或联合其中的关键变量。这种分工依赖接口信息是否足够，不能仅依据算法名称确定。

### 3.4 重构收益需要同时观察业务机会和成员代价

需求响应重构改变了卫星未来经过目标的时刻，因此可以把轨道动作与任务选择放在同一比较中。McGrath和Macdonald利用升降轨、滑行及恢复组成低推力候选，再按响应时间、控制代价和目标距离选择行动[13]。其24星案例中，Cairngorms平均覆盖时长由2.8 min增至4.5 min，最长局部重访间隔却由15.5 h增至17.7 h；引入燃料均衡还使总速度增量和完成时间增加。由此，重构的业务效果应同时保留所需覆盖、关键间断和成员消耗，不能由单个改善指标代替。

多阶段配置进一步将当前机动与后续机会联系起来。Lee等的确定性多阶段模型在阶段之间传递构型和机动预算，并比较不同前视范围的求解方法[14]。其目标路径全时域预知，适合分析预算跨阶段分配的影响；未来任务尚未揭示时，前视信息的可得性需要作为另一项条件处理。

面向任务的重构因此包含两个判断：新构型是否提供所需机会，以及获得这些机会所付出的时间和资源是否可以接受。恢复原有高度或进入新的覆盖模式，只完成了其中一部分。业务可以由其他成员提前接续，也可能在构型到位后继续等待处理、传输或授权。恢复方案应按能力到位时机、业务期限和等待代价整体评价。

## 4 从轨道行动到多星协调运行

### 4.1 根据依赖范围和响应期限组织求解

联合建模的作用是保留相互影响的选择。部署可达性改变目标构型集合，观测后的交付容量影响上游活动价值，跨阶段机动预算影响未来配置，这些联系在前述研究中具有不同的物理与资源来源。若事先固定其中一部分变量，就可能失去另一部分决策所需的候选。部分联合可以针对这些具体联系展开，而不必把所有状态和活动一次性纳入同一个模型。

前视范围的价值需要结合限时求解结果判断。在多阶段重构的23个数值可比实例中，单阶段前视滚动方法相对全时域模型的覆盖奖励为7个较高、12个较低、4个相同；另有1个全时域实例因内存不足失败[14]。两者采用不同含义的时间限制，目标又预先已知，因此这组结果反映该研究中的限时求解取舍，不能直接解释为在线组织方式的普遍排序。

区域重构研究则保持配置、指派和覆盖模型不变，比较拉格朗日启发式与限时混合整数线性规划[15]。紧机动预算组的18个实例中，启发式取得6个较高、10个较低和2个相同的目标值。这是同模型的求解器比较，与前述改变前视范围的比较属于不同维度。联合模型可以分解计算，分层组织也可以滚动更新。

局部处理的依据是受影响范围和既有承诺。增量观测分配研究保留未受变化影响的安排，以减少重复处理[16]。这一思路用于轨道变化时，需要进一步检查原有活动的窗口、资源占用和前后继是否仍然成立。局部方案能够维持可行，也仍需评价因此放弃的跨星机会。

据此，本文将决策组织概括为表1中的条件性选择。除列出的研究内部对照外，各方式在完整任务—轨道—安全过程中的适用条件属于文献综合，尚无统一的事前选择阈值。

**表1 任务与轨道决策的组织条件**

| 组织方式 | 适用条件与需要交换的信息 | 主要取舍 | 证据性质 |
|---|---|---|---|
| 分别求解并反馈 | 子问题可通过机会窗口、资源占用和控制余量表达关键相互约束 | 子问题较易处理，但边界信息遗漏可能使结果失效 | 基于不同机制的综合 |
| 部分联合建模 | 上游选择改变下游可行机会，或共同预算连接多个阶段 | 保留重要候选，同时增加计算负担 | 业务链及配置子问题有直接对照，整体组织为综合 |
| 滚动更新 | 保留已执行事实，按可用信息重新安排未来动作 | 前视价值与当次求解时间共同决定结果 | 多阶段重构的确定性研究内对照[14] |
| 局部复用 | 变化局部，保留活动及跨边界承诺仍有效 | 减少重复求解，可能放弃更大范围的新机会 | 增量分配机制及接口综合[16] |

### 4.2 共同安全取决于相容动作和有效信息

多星安全需要同时处理外部接近和成员之间的动作影响。Błażejczyk和Zagórski将碎片接近、编队内间距与终端条件置于序列凸轨迹规划中[17]，提供了在同一控制问题内协调外部与内部约束的例子。它说明安全要求可以改变成员共同选择的轨迹，但具体保证仍由所用动力学、约束检查和算例范围确定。

共享意图可以改善任务协调，安全效果则需要单独测量。Dolan等比较共享与隐藏其他卫星目标的学习策略，目标共享改善了到达表现，而两种情形的碰撞数中位数相同[18]。其到达指标允许在碰撞后继续累计，因此可用于评价目标协调，不能据此认定获得无碰撞完成。

控制输入的选择责任进一步影响共同可行性。Dunlap等在同一组2000个五星初态中，集中式运行时保障全部通过，分散实现通过率为90.95%；两种实现都取得全部成员状态，差别包括能否共同选择控制输入[19]。失败包含约束违反或无可行输入，并不全部等于实体碰撞。该对照支持的认识是：完整状态信息需要与相容的输入选择机制配合，才能处理成员间共同约束。

对运行组织而言，应明确共享的是当前状态、预测轨迹还是已承诺动作，并规定这些信息在何时更新、何时失效。若多个成员同时修改原先用于检查的轨迹，就需要重新协调相关约束；若按顺序更新，则要说明其他成员在这一期间保持什么承诺。共同安全因而同时涉及轨道模型、控制余量、通信时效和动作更新规则。

### 4.3 计划启用、执行与业务恢复

可行轨迹进入运行，还需要经过状态确认、检查和相应权限下的计划启用。Starling飞行动力学报告描述了地面生成、审查、接近筛查及运控批准之间的衔接[20]；NanoFF在轨报告记录的导航核查、地面冲突和模型修正则影响实际机动时刻[21]。这些事件说明，响应时间包括求解之外的协调和确认过程。

本文将计划启用定义为经相应授权进入实际执行安排。活动执行表示动作已经开始，活动完成表示达到该活动的结束条件，业务满足则依据任务要求评价。几个事件可以相继发生，也可以在不同成员上交叠。例如，替代成员可以在故障星完成修复前接续服务，而已完成机动的成员也可能尚未获得可用的观测或下传时段。

GSOC报告中的接近处置将机动与构型运行联系起来，但对SAR业务未受影响的判断主要依据构型偏差，未给出对应事件的直接交付损失测量[22]。因此，分析恢复效果时应区分安全条件达到、功能资源可用、计划进入执行和实际业务满足。前几项可以解释恢复过程，最后一项用于判断这一过程是否实现了任务目的。

这一区分也使不同恢复路径可以在共同业务指标下比较。具有硬期限的请求要求能力和后续活动在期限内衔接；允许迟到的请求则可将延迟代价与资源消耗共同计入。原成员修复、替代成员接续和降低服务等级由此成为具有不同到位时机与业务代价的候选。

### 4.4 大型星座需要怎样的规模描述

局部方法能否用于大型星座，取决于同时发生的耦合规模。总星数增加会扩大可选成员集合，但一次机动可能只涉及少数主动成员；反之，共享地面站、参考星或业务容量也可能把空间上分离的成员连接起来。分解观测调度研究通过划分任务和协调分配降低集中处理负担[23]，而S-NET案例揭示了共享参考星带来的动作联系[9]。两者分别对应资源竞争与控制耦合。

因此，规模评价宜同时报告总星数、主动决策成员数、请求与接近事件数，以及跨组共享的资源。若每个局部问题只依赖有限邻居，局部计算可以随事件分散；若共享资源或安全约束跨越多个分组，则需要额外协调。现有小编队试验支持相应机制分析，尚不足以确定真实大型星座中这些依赖如何增长。具有运行意义的规模结论，应进一步给出计算、通信和批准环节共同满足响应期限的条件。

## 5 综合认识与研究展望

任务驱动的星座研究需要把构型、轨道行动和业务结果连接起来。构型层解释机会的空间分布与时间结构，演化和控制层解释这些机会能够保持多久以及如何改变，协调运行层则处理活动选择、共享资源和实际执行。三者共同决定星座能否在需求变化和安全事件后继续提供服务。

已有研究形成了几项可用于组织后续工作的认识。首先，任务指标需要落实到访问序列、最长间断或交付期限，同一覆盖总量并不能概括所有业务需求。其次，自然漂移、差动阻力和推进机动提供不同的时间—资源取舍，比较时应保留到位时间、可用活动及逐星剩余能力。再次，部分联合、分层和滚动处理可以组合，选择依据是变量联系能否通过接口充分表达，以及完整响应是否赶得上任务期限。最后，共同安全需要相容动作，业务恢复需要实际任务结果，信息共享和轨道到位分别只是其中的一部分。

进一步研究可以围绕三个问题展开。其一，如何从业务要求确定可接受的构型范围，并将维持消耗和有效任务时间共同带回设计？所需证据应连接几何容差、控制能力和业务质量，而不仅比较终态误差。其二，如何在求解前判断哪些任务、资源和轨道变量必须共同处理？有价值的对照应在相同需求、信息和响应预算下，展示扩大决策范围的收益及计算代价。其三，怎样评价安全处置与任务恢复的净收益？需要在同一事件中记录轨道行动、计划变更、活动中断和业务结果，并比较可实施的替代路径。

这些问题使轨道动力学成为运行决策的物理基础，也使任务需求成为评价轨道方法的实际尺度。围绕这两者建立可追溯的比较，能够把构型设计、控制与规划研究组织为具有明确问题和条件性认识的综述。

## 参考文献

1. Ben-Larbi MK, Flores Pozo K, Haylok T, Choi M, Grzesik B, Haas A, et al. Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts. Advances in Space Research, 2021, 67(11): 3598–3619. DOI: 10.1016/j.asr.2020.08.009. [实际来源](https://www.researchgate.net/publication/343791434_Towards_the_Automated_Operations_of_Large_Distributed_Satellite_Systems_Part_1_Review_and_Paradigm_Shifts)

2. Lee HW, Shimizu S, Yoshikawa S, Ho K. Satellite Constellation Pattern Optimization for Complex Regional Coverage. Journal of Spacecraft and Rockets, 2020, 57(6): 1309–1327. DOI: 10.2514/1.A34657. [实际来源](https://arxiv.org/pdf/1910.00672v4)

3. Rogers DW, Won D, Koh D, Hong K, Lee HW. Optimal Satellite Constellation Configuration Design: A Collection of Mixed Integer Linear Programs. Journal of Spacecraft and Rockets, 2026, 63(4): 1144–1162. DOI: 10.2514/1.A36518. 所引模型名称及数值来自作者配套仓库README的Illustrative Example结果表。 [实际来源](https://github.com/Space-Systems-Operations-Research-Lab/Constellation-Design-MILP-Collection)

4. Gwon B, Ahn J. Two-Stage Framework for Deployment-Aware Optimization of Satellite Constellation Pattern Design. International Journal of Aeronautical and Space Sciences, 2026. DOI: 10.1007/s42405-026-01298-1. [实际来源](https://link.springer.com/content/pdf/10.1007/s42405-026-01298-1.pdf)

5. He L, Liang B, Li J, Sheng M. Joint Observation and Transmission Scheduling in Agile Satellite Networks. IEEE Transactions on Mobile Computing, 2022, 21(12): 4381–4396. DOI: 10.1109/TMC.2021.3076088. [实际来源](https://www.comm.utoronto.ca/~liang/publications/TMC_ObsTrans_ASN.pdf)

6. Leroy S, Fitzgerald R, Cahoy K, Abel J, Clark J. Orbital Maintenance of a Constellation of CubeSats for Internal Gravity Wave Tomography. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2020, 13: 307–317. DOI: 10.1109/JSTARS.2019.2961084. [实际来源](https://www.researchgate.net/profile/Stephen-Leroy-2/publication/339220232_Orbital_Maintenance_of_a_Constellation_of_CubeSats_for_Internal_Gravity_Wave_Tomography/links/5e46c789458515072d9dab44/Orbital-Maintenance-of-a-Constellation-of-CubeSats-for-Internal-Gravity-Wave-Tomography.pdf)

7. Hull S, Shelton A, Richardson D. Differential Drag Demonstration: A Post-Mission Experiment with the EO-1 Spacecraft. 1st IAA Conference on Space Situational Awareness, 2017. NASA NTRS 20170010724. [实际来源](https://ntrs.nasa.gov/api/citations/20170010724/downloads/20170010724.pdf)

8. Kim S, Yoon H. A Pitch-Roll Attitude Strategy for LEO Constellation Phasing with Differential Drag Under Power Constraints. International Journal of Aeronautical and Space Sciences, 2026, 27: 2488–2504. DOI: 10.1007/s42405-025-01071-w. [实际来源](https://link.springer.com/content/pdf/10.1007/s42405-025-01071-w.pdf)

9. Ingrillini L, Traub C, Ben-Larbi MK, Turco F, Fasoulas S, Stoll E, et al. Operationalizing differential drag control: a planning routine for the S-NET satellite formation. CEAS Space Journal, 2026, 18: 685–705. DOI: 10.1007/s12567-025-00630-x. [实际来源](https://link.springer.com/content/pdf/10.1007/s12567-025-00630-x.pdf)

10. Arnas D, Linares R. On the Theory of Uniform Satellite Constellation Reconfiguration. arXiv:2110.07817v1, 2021. https://arxiv.org/abs/2110.07817v1. [实际来源](https://arxiv.org/pdf/2110.07817v1)

11. Gaias G, D’Amico S. Impulsive Maneuvers for Formation Reconfiguration Using Relative Orbital Elements. Journal of Guidance, Control, and Dynamics, 2015, 38(6): 1036–1049. DOI: 10.2514/1.G000189. [实际来源](https://slab.sites.stanford.edu/sites/g/files/sbiybj25201/files/media/file/jgcd2015_gaiasdamico.pdf)

12. Appel L, Guelman M, Mishne D. Optimization of satellite constellation reconfiguration maneuvers. Acta Astronautica, 2014, 99: 166–174. DOI: 10.1016/j.actaastro.2014.02.016. [实际来源](https://www.researchgate.net/publication/260801708_Optimization_of_satellite_constellation_reconfiguration_maneuvers)

13. McGrath CN, Macdonald M. General Perturbation Method for Satellite Constellation Reconfiguration Using Low-Thrust Maneuvers. Journal of Guidance, Control, and Dynamics, 2019, article in advance. DOI: 10.2514/1.G003739. [实际来源](https://strathprints.strath.ac.uk/69138/1/McGrath_Macdonald_JGCD_2019_General_perturbations_method_for_satellite_constellation_reconfiguration.pdf)

14. Lee HW, Williams Rogers DO, Pearl BD, Chen H, Ho K. Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods. Journal of Spacecraft and Rockets, 2025, 62(1): 206–222. DOI: 10.2514/1.A35990. [实际来源](https://arxiv.org/pdf/2401.11567)

15. Lee HW, Ho K. Regional Constellation Reconfiguration Problem: Integer Linear Programming Formulation and Lagrangian Heuristic Method. Journal of Spacecraft and Rockets, 2023, 60(6): 1828–1845. DOI: 10.2514/1.A35685. [实际来源](https://arxiv.org/pdf/2206.02910)

16. Parjan S, Chien SA. Decentralized Observation Allocation for a Large-Scale Constellation. Journal of Aerospace Information Systems, 2023, 20(8): 447–461. DOI: 10.2514/1.I011215. [实际来源](https://ai.jpl.nasa.gov/public/documents/papers/parjan-jais2023-mas.pdf)

17. Błażejczyk M, Zagórski P. Sequential Convex Trajectory Planning for Space-Debris Conjunction Mitigation in Satellite Formations. Applied Sciences, 2026, 16(8): 3707. DOI: 10.3390/app16083707. [实际来源](https://doi.org/10.3390/app16083707)

18. Dolan S, Nayak S, Balakrishnan H. Satellite Navigation and Coordination with Limited Information Sharing. Read version: arXiv:2211.03658v3, 15 May 2023. [实际来源](https://arxiv.org/pdf/2211.03658)

19. Dunlap K, van Wijk D, Hobbs KL. Run Time Assurance for Autonomous Spacecraft Inspection. Preprint AAS 23-113, arXiv:2302.02885v2, 2023. https://arxiv.org/abs/2302.02885v2. [实际来源](https://arxiv.org/abs/2302.02885v2)

20. Alem N, Hendriks TG, Alvarellos JL, Levinson-Muth PG, Dono A. Mission Design and Flight Dynamics Operations for the Starling Swarm Technology Demonstration. 2025 AAS/AIAA Astrodynamics Specialist Conference, 2025. NASA NTRS 20250007355. https://ntrs.nasa.gov/citations/20250007355. [实际来源](https://ntrs.nasa.gov/citations/20250007355)

21. Roychowdhury D, Grau S, Boyer F, Kapitola S, Legenza A, Diez JM, et al. In-orbit demonstration of propulsive and drag-based formation control using two 2U CubeSats under operational constraints. CEAS Space Journal, 2026. DOI: 10.1007/s12567-026-00702-6. [实际来源](https://doi.org/10.1007/s12567-026-00702-6)

22. Aida S, Kirschner M. Operational Results of Conjunction Assessment and Mitigation at German Space Operations Center. Transactions of the Japan Society for Aeronautical and Space Sciences, Aerospace Technology Japan, 2012, 10(ists28): Tr_23–Tr_28. DOI: 10.2322/tastj.10.Tr_23. [实际来源](https://www.jstage.jst.go.jp/article/tastj/10/ists28/10_ists28_Tr_23/_pdf/-char/en)

23. Zilberstein I, Rao A, Salis M, Chien S. Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation. Journal of Artificial Intelligence Research, 2025, 82: 169–208. DOI: 10.1613/jair.1.16997. [实际来源]()
