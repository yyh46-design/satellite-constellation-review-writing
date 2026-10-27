from pathlib import Path
import json,csv,re,hashlib,collections
P=Path(__file__).resolve().parent
REPO=Path(r'D:\SKT727\worktrees\constellation_review_v3510_20261026')
def write(name,s):
 f=P/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(s.strip()+'\n',encoding='utf-8')
def csvwrite(name,rows):
 with (P/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
acq=json.loads((P/'SOURCE_ACQUISITION.json').read_text())+json.loads((P/'SOURCE_ACQUISITION_MORE.json').read_text())
acq={x['id']:x for x in acq}
papers=[
dict(id='N001_ROGERS',title='Optimal Satellite Constellation Configuration Design: A Collection of Mixed Integer Linear Programs',authors='David O. Williams Rogers; Dongshik Won; Dongwook Koh; Kyungwoo Hong; Hang Woon Lee',year=2026,doi='10.2514/1.A36518',version='arXiv:2507.09855v2, 2026-03-26；与正式版逐页配对未完成',pages='1–38正文；39–42书目用于定位',adopt='ADOPT_METRIC_COMPARISON',old='',theme='任务指标与构型设计',
 note='''问题是如何在相同离散候选轨道和可见性矩阵下表达不同任务指标，而非比较多种算法谁普遍更强。决策包括选择轨道槽位和覆盖状态；五类MILP分别描述最小成本、覆盖比例、覆盖奖励、最大重访和平均重访。有限候选集合上的最优解不等于连续轨道设计的全局最优。

方法与条件：§III以传播后的可见性矩阵连接槽位选择和时间序列。§III.B（PDF p9）公共算例为西雅图单目标、716个120 s步长，7:1回归轨道，半长轴11546.32 km、倾角142.14°。应称给定轨道族示例，不能写成常见550 km低轨构型。

关键对照：PDF p25表8的三种5星方案，MCLP覆盖80.86%、最大/平均重访52/18.26 min；MMRT为78.07%、22/14.95 min；MART为80.02%、44/12.43 min。同样5颗星，平均等待与最长间断会作出不同选择。已视觉核对原表；作者配套README曾写MMRT覆盖78.08%，本轮采用原PDF的78.07%，不混用版本。

扩展范围：pp29–34将异质轨道、简化部署成本和几何连通性放入模型。连通约束及单星失效后的图结构性质不能替代链路预算、通信时延、供电和交付性能验证。p37仍把规模研究作为后续方向。

写作采用：讨论稿2.1用最大/平均重访直接对照解释任务指标如何塑造构型。它比普通“优化覆盖”背景句增加了指标冲突的原始证据。现有旧稿的区域覆盖模型可以与之互补，不需删除。''',
 claims=[('p25, Table 8','同一5星离散候选算例中，MMRT与MART最大/平均重访分别为22/14.95与44/12.43 min','给定轨道族与离散周期；不是重求解结果'),('pp31–34','几何连通和覆盖冗余可进入构型MILP','不是业务交付可靠性验证')]),
dict(id='N002_PEARL',title='Reconfigurable Earth Observation Satellite Scheduling Problem',authors='Brycen D. Pearl; Joseph M. Miller; Hang Woon Lee',year=2026,doi='10.2514/1.I011659',version='arXiv:2507.10394v3, 2025-11-07；正式刊期2026；与正式版逐页配对未完成',pages='1–38正文及附录；39–43书目定位',adopt='ADOPT_ORBIT_RESOURCE_DOWNLINK',old='',theme='轨道重构与业务资源共同决策',
 note='''研究将固定轨道的观测、下传、充电调度扩展为可在阶段边界选择轨道槽位的REOSSP。模型同时跟踪电池、存储和逐星机动预算，轨道选择改变目标、地面站和日照窗口。相比只比较覆盖奖励的重构研究，它增加了轨道变化经资源约束影响下传量的证据。

方法：§II–IV为MILP及滚动时域RHP，滚动传递当前轨道、已用预算、电量与数据。目标z为观测次数加带权下传次数（下传权重C=2），报告指标Z为模型内下传数据量GB。两者不得混写成同一“业务收益”，也没有验证图像质量或用户实际交付。

直接对照：§V.B，pp29–35为4星、7.25天、8阶段、每星135槽位的Sandy历史路径算例。固定轨道EOSSP、全模型REOSSP-Exact、滚动RHP的z为25/97/73；模型内下传量为0.80/3.20/2.40 GB；求解时间为0.24/54.60/6.65 min（pp30–31，已视觉核对）。总机动代价Exact 2.26 km/s、RHP 2.89 km/s，均为四星合计，逐星预算750 m/s。RHP早期消费预算会损失后续选择；不能从快算直接推出省燃料。

反例与预算：p26表3有24个随机实例；Exact 10个有数值可行解、10个限时无可行解、4个内存不足。10个数值可比实例中Exact目标值均高于RHP；RHP在24个实例都得到可行解。Exact与每个RHP子问题各有60 min上限，并非相同总预算，RHP实例8累计67.61 min。不能使用表末排除失败后的均值宣布公平总体优势。

轨道边界：几何窗口由SGP4生成，槽间机动代价采用解析脉冲模型。初始机动在任务时域外，阶段式配置未显式完整表达有限转移期间的观测禁用和全程碰撞安全。历史路径事先给定，也没有与优化后的敏捷姿态系统作匹配对照。用它证明模型内轨道—资源—下传联系，不宣称在轨净收益或大星座联合避碰。

写作采用：3.4补实质研究内对照；4.1与原有确定性多阶段/区域重构对照分开。''',
 claims=[('pp29–31, §V.B; Tables 4–6','4星Sandy算例固定/全模型/滚动下传量0.80/3.20/2.40 GB，时间0.24/54.60/6.65 min','已知历史路径；模型内下传；阶段式机动'),('p26, Table 3','24例Exact有10例数值可行、10例超时无解、4例内存失败；10个可比目标值均高于RHP','Exact与每个滚动子问题各60 min，不是相同累计预算'),('pp32–35','Exact与RHP四星总机动代价2.26/2.89 km/s','总量不等于逐星预算；不推导普遍燃料优势')]),
dict(id='N003_CMAS',title='A Continuous Low-Thrust Maneuver Automation System for Electric Propulsion LEO Satellite Operations',authors='Luigi Mascolo; Zayne Thawer; Alex Paul',year=2025,doi='10.82217/spaceops2025_105',version='SpaceOps 2025, ID105，官方会议PDF',pages='1–8全文',adopt='ADOPT_OPERATION_FEEDBACK',old='',theme='运行反馈与业务恢复',
 note='''本报告解释连续低推力机动如何进入Planet地面运行流程。其独立价值是计划、审批、执行评估与成像计划更新的接口，而不是某个轨道优化算法的性能提升。

架构与机制：LCP负责单星生命周期层的任务要求，CMAS生成具体有限时长机动。Constrained Orbit Box描述高度和偏心率等容差；Maneuver Opportunity Box描述占空比、机动位置及保护时段。pp3–5将候选机动与无机动传播比较，用informed merit function利用自然摄动，再在开始时刻、持续时间和方向的候选中选取方案。

执行链：pp5–6区分预留、动作、审批和执行评估；遥测与定轨识别未执行、部分执行或完成的机动，并更新后续任务。§4.2 p6将成像任务与维持交错，在机动计划、执行或取消后刷新成像时刻和指向。这使任务机会成为随实际轨道重新计算的量，而不是一次规划后不变的输入。

证据强度：这是运营方系统设计与运行经验报告，无受控算法对照和直接业务增益统计。p7 §5.4把星座级管理器放在未来工作中，不能把约20颗有推进能力的运营星数视为该系统已验证的多星联合控制规模。接近筛查和相应审批仍属运行链的一部分。

写作采用：4.3补充机动结果如何反馈业务安排的积极机制；不把“自动化”改写成全自主授权或全星座安全保证。''',
 claims=[('p6, §4.2','机动计划、执行、取消后更新成像时间与指向，执行后状态反馈未来任务','运营架构证据，无匹配业务增益试验'),('p7, §5.4','星座级管理器属于未来扩展','不能把运营舰队星数计为联合控制验证规模')]),
dict(id='N004_HULL',title='Differential Drag Demonstration: A Post-Mission Experiment with the EO-1 Spacecraft',authors='Scott Hull; Amanda Shelton; David Richardson',year=2017,doi='',version='NASA NTRS 20170010724；2017会议作者报告',pages='1–12全文',adopt='ADOPT_FLIGHT_NEGATIVE',old='',theme='构型维持与平台约束',
 note='''EO-1退役后单星试验检验不同姿态能否改变阻力，并考察平台实际运行限制。研究背景包括相位调整和避碰，但正文没有证明多星自主避碰成功。

实验条件与结果：轨道约673×686 km、倾角97.9°。p6第一次低阻力姿态维持略超1 h后因供电进入安全模式，第二次约12 h后因星敏感器过热退出；高阻力姿态约39 h保持稳定。载荷已关闭，不能把这些时段直接当成有效观测时段。

重要负证据：p7相对名义传播的154 m沿轨位移落在约±500 m跟踪容差内，未能据此确认阻力位移效果。这一数字尤其不能写成“完成154 m避碰”。迎风面积变化及轨道拟合阻力变化是不同测量层级。pp8–9讨论控制提前量、姿态能力和轨道高度的影响，不能转成通用安全阈值。

边界：p10的退役年限比较是推演而非实际完成的离轨过程；报告时点的规范不作为今天的规定引用。本文不采用这些年限数字。

写作采用：3.2以供电与热约束说明差动阻力可用控制权来自平台能持续保持的姿态。它补充真实不利结果，与模型内省推进剂结果构成互补。''',
 claims=[('p6','两次低阻力姿态分别因供电安全模式和星敏感器过热中断','EO-1单星退役后试验，载荷已关闭'),('p7','154 m沿轨差异小于约±500 m跟踪容差','不能据此确认位移效果或避碰成功')]),
dict(id='N005_GAIAS',title='Impulsive Maneuvers for Formation Reconfiguration Using Relative Orbital Elements',authors='Gabriella Gaias; Simone D’Amico',year=2015,doi='10.2514/1.G000189',version='JGCD 38(6):1036–1049，作者公开正式排版稿',pages='1–14全文',adopt='ADOPT_TIME_CONTROL_MECHANISM',old='',theme='构型重构与控制时机',
 note='''该研究把重构定义为在给定终端时刻达到完整相对轨道要素，系统比较两脉冲和三脉冲方案。它解释目标几何、机动时机和控制代价如何联系，并非大星座任务调度论文。

动力学：pp2–4用近圆线性相对轨道要素表示单次有限时域重构。径向脉冲可即时改变相对经度；切向脉冲改变相对半长轴，再利用自然漂移积累沿轨位移。机动位置也改变相对偏心率向量。主推导使用Kepler相对状态转移，p3说明更长引导方案可另加J2/阻力修正。

比较：表1–4给出不同方案对终端状态和机动间隔的适用条件；并非每个方案对所有初终态都可行。p10表7的E2例中，2.5轨道周期时方案12/13的Δv为0.0671/0.0562 m/s，7.5周期时为0.0495/0.0587 m/s，排序随可用时间改变。p12讨论有足够时间时存在等代价机动位置，可为排除窗口留出余地；不代表任意禁用窗口均无代价。

边界：例子约750 km、两航天器相对运动；终端完整ROE满足仍应与转移过程安全区分。被动安全几何可指导选择，但本文不能据此声称任意运行中断及连续时间碰撞安全。

写作采用：3.3用自然漂移和有限时域解释“允许等待多久、何时允许机动”为什么是科学变量。保留条件性机制，避免把具体小编队数值转成大型星座性能结论。''',
 claims=[('pp3–4, Eqs.2–6','相对半长轴变化可借自然漂移形成沿轨位移，终端时刻影响代价','近圆线性相对运动模型'),('pp10–12, Table7, §VII','两类重构方案的代价排序随给定转移时间改变；充分时域可提供等代价位置选择','不意味着任意排除窗口均可无代价满足')]),
dict(id='N006_MAINTENANCE',title='Station Maintenance for Low-Orbit Large-Scale Constellations Based on Absolute and Relative Control Strategies',authors='Min Hu; Feifei Li; Wen Xue; Chenhu Liu; Wen Guo; Yongjing Ruan',year=2025,doi='10.3390/app15094640',version='Applied Sciences 15:4640，出版商PDF',pages='1–18正文；19–20书目',adopt='RESERVE_COMPARABILITY_NUMERIC',old='',theme='构型维持与平台约束',
 note='''论文讨论绝对参考相位与相对参考相位维持。控制通过调整半长轴并利用阻力衰减形成相位反馈；相对策略依据成员累积漂移选择参考。研究可补充不同参考基准的机制，但目前不宜承担优劣排序的核心证据。

条件：§5.1为Walker 60/3/1、550 km、53°、约100天、相位容差±0.1°；§5.2为Walker 18/3/1、约300天、容差±5°，讨论部分成员机动。星数、时长和容差均不同，不能把两组结果当成保持条件相同的绝对/相对控制对照。

数值核查：PDF p14表3低太阳活动参数为29.4 m和13.1天，高活动为70.7 m和5.5天；邻接段落将13.1天与70.7 m合写。p15表4单次半长轴变化平均59.79 m，可能涉及双侧变化与幅值的不同口径，不应直接判为同一量的矛盾。已视觉核对表3、4和相邻段落，保留“太阳活动场景和调整幅值定义待厘清”。

取舍：保留正文阅读记录与候选登记；本轮讨论稿不采用其具体控制周期、调整幅值及普遍优劣结论。不是因为刊物或只出现一次而舍弃，而是现有Leroy和飞行运行证据已能解释维持问题，此文当前的独立增量不足以抵消比较口径不清。''',
 claims=[('pp13–18, §5.1–5.2','绝对与相对策略算例的规模、时长及容差不同','不能据异质算例宣布总体优劣'),('pp14–15, Tables3–4','场景参数和半长轴调整量表述需要进一步厘清','HOLD数值采用；不武断认定59.79与29.4为同一量')]),
dict(id='N007_MCGRATH',title='General Perturbation Method for Satellite Constellation Deployment Using Nodal Precession',authors='Ciara N. McGrath; Malcolm Macdonald',year=2020,doi='10.2514/1.G004443',version='作者接受稿；JGCD 43(4):814–824',pages='1–25全文',adopt='ADOPT_DEPLOYMENT_LIFETIME',old='',theme='部署与可达时间',
 note='''研究通过升降轨、驻留与入轨三阶段利用差异J2节点进动形成多个轨道面，并把部署时间、转移消耗、长期阻力补偿和发射安排连接起来。它补强从理想构型到实际可用成员集合的时间问题。

方法条件：近圆、固定倾角、分段恒定切向加速度；大气采用静态CIRA72近似，未完整表示太阳活动和地球大气自转变化。节点变化由J2长期率积累，轨道内相位与节点漂移具有不同时间尺度。总Δv包括部署与后续维持项，必须保留预算口径。

运行对照：§III pp11–13用FORMOSAT-3/COSMIC TLE与实际部署比较。FM4/FM1预测差约3/6天、FM6约11天；FM2差62天，与40天暂停及目标节点间隔由24°改为30°有关；FM3因太阳阵故障未达到最终高度而未进入同类比较。不能只摘录小误差样本宣称所有部署均准确。模型假设连续推力，运行暂停会延长实际到位时间。

设计比较：p22表4为24星、4轨道面、8年任务的假设。传统4次发射部署约1年，单次500 km注入约2.75年；各方案累计Δv包含8年阻力补偿，不包括轨道内调相。历史发射价格及季度发射假设不得作当前报价。剩余推进能力不均还会影响成员寿命与补网顺序。

写作采用：2.2解释自然漂移节省直接平面机动的同时延迟能力形成；通过部署中断反例把解析可达时间与实际运控到位时间分开。''',
 claims=[('pp11–13, §III','FORMOSAT-3的暂停、改变目标和硬件故障改变部署完成时间','模型与真实TLE对照；不能忽略不利成员'),('p22, Table4','24星设定中传统四次发射约1年，单次500 km注入约2.75年','固定任务和发射假设，非通用部署时间')]),
dict(id='N008_ZHAO',title='Deployment of Constellation with Different Inclinations Using the Nodal Precession and Thrust',authors='Shuailong Zhao; Qinyu Zhu; Xuefeng Tao; Yasheng Zhang',year=2024,doi='10.3390/s24020631',version='Sensors 24:631，出版商PDF',pages='1–14正文；15–16书目',adopt='RESERVE_GEOMETRY_CHECK',old='',theme='部署与可达时间',
 note='''研究比较改变半长轴、改变倾角以利用J2节点进动，与直接法向推力改变节点的部署途径。它强调不同倾角下的控制效应不同，可作为进一步核查的部署机制候选。

方法：近圆一阶推力变化关系及节点长期漂移，按脉冲或连续推力推导策略选择范围；数值例使用550 km、3轨道面、10°节点间隔、500 kg和50 mN等设定。文中倾角界限取决于这些几何和近似条件，不宜直接升级为通用工程准则。

确切疑点：PDF p5式(13)的脉冲节点变化代价写作sqrt(mu/a)|ΔΩ|，p6式(16)连续推力代价含sin(i)，式(17)据此比较并给出39.5402°等界限。两种节点变化比较的几何约定、倾角因子及原引用推导需进一步核对。已查看实际公式图像，排除纯文本漏字的可能；本轮没有独立复算或证明论文错误。

取舍：正文完整阅读计入本批10篇，科学采用保留RESERVE_GEOMETRY_CHECK；不采用上述数值阈值和“连续推力在某倾角必优”的表述。部署主线已有McGrath、Gwon支持，暂不为增加数量把未核清比较写入样稿。''',
 claims=[('pp5–6, Eqs.13/16/17','脉冲和连续节点变更代价的倾角项与比较几何需核对','仅记录具体疑点，不宣判原研究失效；不进入正文')]),
dict(id='N009_SDDIP',title='Stochastic Multistage Constellation Reconfiguration Problem: Stochastic Dual Dynamic Integer Programming Approach',authors='Brycen D. Pearl; Hang Woon Lee',year=2026,doi='',version='arXiv:2608.09738v1, 2026-08-10，预印本',pages='1–30正文及附录；31–34书目',adopt='ADOPT_UNCERTAINTY_WITH_LIMITS',old='',theme='不确定目标与重构决策',
 note='''论文把确定性多阶段构型选择扩展为含目标位置与奖励场景的随机问题，采用SDDiP前向抽样、后向割平面更新价值近似，并与不机动、随机机动、值迭代和Q学习比较。其独立价值是把未来不确定性显式带入轨道配置，而不是又一个泛泛的AI算法。

关键建模代价：pp9–11列出二元状态、阶段独立及完全连续补救等假设；原确定性问题的全任务累计机动预算约束(1d)未直接保留在SMCRP。附录A p30用裁剪候选槽位，使S乘以最大单次代价不超过总预算，从而保证任何允许序列均不超预算。它是保守候选构造，不等于在任意候选轨道上最优分配剩余燃料。p29仍把恢复一般预算与加入下传/充电列为未来工作。

实验：两颗观测星、20场景、4天任务。轨道目标例4重构阶段、每星20槽位；飓风例2阶段、30槽位。奖励是离散可见性累计，不是识别精度、实际成像完成或下传交付。无全程联合避碰保证。

对照和计算负担：p20表1轨道目标例平均奖励SDDiP 179.20、VI 93.40、QL 76.70、随机70.02、不机动67.55、完全预知确定性上界188.10。p23说明SDDiP十轮约60 h，子问题一小时上限使其未完全收敛；MDP方法少于12 h且未作超参数搜索，因此不将这组差异写成同预算算法排序。飓风例pp26–28 SDDiP与确定性上界均28.05，VI 26.20；SDDiP约2 h，VI略超1 h，QL略低于4 h。两类场景的收敛不能互相替代。

其他待核：附录A预算单位印作km，而前文机动代价语境为速度增量，本轮不引用该具体预算数值；算法伪码停止条件与文字之间也未做独立实现复核。本文只采用问题结构和计算限制，不引入全局最优或实时飞行能力宣称。

写作采用：3.4增一段随机目标，4.1明确离线策略与在线响应的区别；保留预印本状态。''',
 claims=[('pp10–11; p30 AppendixA','累计预算通过预裁剪槽位保证所有允许序列满足，非一般预算状态优化','受限候选集合；完整预算扩展仍属未来工作'),('pp17–23, Table1','两星轨道目标例SDDiP十轮约60 h且未完全收敛','对照方法预算与调参不同；不宣称实时或普遍优越'),('p29, Conclusions','下传与充电的随机联合调度仍为后续扩展','不把该模型当作随机REOSSP完整业务链')]),
dict(id='N010_FOSTER',title='Differential Drag Control Scheme for Large Constellation of Planet Satellites and On-Orbit Results',authors='Cyrus Foster; James Mason; Vivek Vittaldev; Lawrence Leung; Vincent Beukelaers; Leon Stepan; Rob Zimmerman',year=2017,doi='10.2514/1.A33927',version='IWSCFF 17-33，arXiv:1806.01218v1；DOI对应2018正式研究线，标题不同，未逐页配对',pages='1–18全文',adopt='ADOPT_HISTORICAL_VERSION_REREAD',old='N02',theme='构型维持与平台约束',
 note='''历史来源N02已登记正式论文Constellation Phasing with Differential Drag on Planet Labs Satellites（2018，DOI 10.2514/1.A33927）；本轮取得并正文阅读的是2017会议稿、2018公开arXiv版本。按同研究线归并，不计全项目新增独立文献。历史是否已完成同版本正文阅读尚未统一核算。

机制：控制器先估计相对相位和相位率，再分配槽位，最后对全体成员联合生成高低阻力命令。参考星的模式影响其他成员相对加速度，因此独立星对命令不能简单叠加。p10讨论槽位与命令一体嵌套优化的计算负担，采用分阶段求解；这支持有接口的分层安排，不支持所有问题分开最优。

业务反向约束：p9几何面积比约10:1，而可用弹道系数比约3:1；成像、下传可抢占阻力模式，姿态误差和气体表面作用也影响有效控制权。平台几何能力与业务期间真正可用的控制权应分开。

飞行与仿真：pp10–12、图10–12为Flock 2p十二星、约510 km的飞行相位控制，地面每日定轨与更新。运行中有效控制权一度比预测低约50%，引起超调及槽位反复调整，后续用实测状态更新估计。p13图13为Flock 3p的88星仿真，含前80天分批调试；摘要百星能力为仿真表述，不能计成88或100星完整飞行验证。

写作采用：3.2补充业务活动如何改变轨道控制能力和真实反馈；4.4保留12星飞行与88星仿真的区别。没有据此新增协同避碰保证。''',
 claims=[('p9; pp10–12','成像和下传可抢占阻力模式，控制估计需按实际轨道反馈更新','沿轨相位控制，不是全星座避碰验证'),('pp11–13, Figs.11–13','12星为飞行相位控制，88星图为仿真','同一历史N02研究线，不重复新增独立来源')])]
for d in papers:
 d.update(url=acq[d['id']]['url'],sha256=acq[d['id']]['sha256'],pdf_pages=acq[d['id']]['pages'])
 d['reading_status']='BODY_READ_AI_NOT_AUTHOR_VERIFIED'
 d['human_verified']=False
 write('reading_notes/'+d['id']+'_CN.md',f"# {d['id']}｜{d['title']}\n\n作者：{d['authors']}。年份：{d['year']}。\n\n实际版本：{d['version']}。\n\n原文：{d['url']}\n\nPDF SHA-256：`{d['sha256']}`\n\n阅读范围：{d['pages']}。状态：{d['reading_status']}；human_verified=false。\n\n既有来源：{d['old'] or '本轮前已核对来源台账未匹配；本批首次登记'}。采用：{d['adopt']}。\n\n{d['note']}\n\n## 可追溯论点\n\n"+'\n\n'.join(f"- C-{d['id'][:4]}-{i:02d}：{claim}。定位：{loc}。边界：{bound}。" for i,(loc,claim,bound) in enumerate(d['claims'],1)))
csvwrite('READING_REGISTER.csv',[{k:d[k] for k in ['id','title','authors','year','doi','version','url','sha256','pdf_pages','pages','old','reading_status','adopt','human_verified']} for d in papers])
claims=[dict(claim_id=f"C-{d['id'][:4]}-{i:02d}",source_id=d['id'],locator=loc,claim_cn=claim,boundary_cn=bound,adoption=d['adopt'],source_url=d['url'],human_verified=False) for d in papers for i,(loc,claim,bound) in enumerate(d['claims'],1)]
csvwrite('CLAIM_REGISTER.csv',claims)
write('READING_BATCH_SUMMARY_CN.md','''# 首批10篇正文阅读与采用说明

本批实际取得并阅读10篇原文正文，涉及10项研究线；其中9项在本轮前已核对台账中未匹配，1项为历史N02的会议/预印本版本复读。它们不与历史95、97、120等不同统计口径直接相加。新增引用、重新阅读、正式版配对、作者终核分别记录。

8篇用于R2讨论稿，2篇保留阅读记录而暂不写入正文。Rogers、Hull、Gaias在本轮中间R1曾仅作定向来源查阅，本轮完成正文阅读后升级为BODY_READ_AI_NOT_AUTHOR_VERIFIED；不是另外重复增加3篇。正文阅读包括问题、模型、方法、算例、结论及相关附录；没有独立复现算法、逐式证明或取得作者科学终核。

## 本轮带来的实质增量

1. 任务指标真正决定轨道构型：同星数、同候选条件下，平均重访与最长间断选择不同方案（N001）。
2. 部署具有业务时间和寿命代价：漂移形成轨道面需要等待，停推和任务变化会改变到位时刻（N007）。
3. 轨道重构可直接进入观测—电量—存储—下传调度，收益与计算代价、剩余预算需要同报（N002）。
4. 不确定目标改变前视问题，但保守候选集和离线计算代价限制其运行含义（N009）。
5. 成像/下传占用反过来限制差动阻力，机动实际结果又反馈成像窗口（N010、N003）。
6. 原文中的不利结果同样有用：EO-1低阻力姿态中断及位移未超测量容差，避免把模型控制量误写成飞行效果（N004）。

## 暂缓而非删除

N006的不同策略算例在容差、规模和时长上不匹配，太阳活动与调整量表述待厘清；N008的节点变更代价比较几何需核对。两篇均已正文阅读，但没有用其未核清数值填充样稿。既有S045、L071等HOLD、L042正式版配对及既有最近邻综述缺口均保持原状态。

各篇笔记给出实际版本、页码、正反结果和采用位置；READING_REGISTER.csv、CLAIM_REGISTER.csv为机器可读入口。human_verified=false，submission_ready=false。
''')

# Bounded candidate selection. Metadata-level relevance is not a finding or a quality certificate.
data=json.loads((P/'discovery/CROSSREF_DEDUP_CANDIDATES.json').read_text(encoding='utf-8'))
indices=[5,6,8,9,17,21,23,24,25,32,38,48,51,52,54,60,67,68,70,74,75,77,78,79,81,82,85,88,90,91,95,97,98,100,103,104,105,106,107,112,113,118,125,132,133,135,136,138,149,155]
questions={
5:'区域快速重访如何改变轨道与相位选择？',6:'单次重访约束与全局覆盖怎样共同表达？',8:'区域回归覆盖的维持目标如何联系相位和业务？',9:'非连续覆盖设计采用哪些可比指标和约束？',17:'定位任务的持续覆盖如何影响构型选择？',21:'最少跳数目标与轨道几何、覆盖之间有何取舍？',23:'回归轨道下非连续区域覆盖如何生成候选？',24:'密集低轨的覆盖设计规模及模型条件是什么？',25:'半解析传播如何进入构型搜索并控制计算量？',32:'轨道重构能否通过电量与存储约束改善下传？',38:'地面机动自动化如何衔接审批与执行反馈？',48:'极低轨演示如何把阻力补偿与业务运行联系起来？',51:'自然节点漂移对部署时间和寿命有什么代价？',52:'多轨道面部署如何结合自然进动和机动？',54:'不同倾角下改变半长轴或倾角的代价比较是否一致？',60:'巨型星座的部署排序受哪些动力学与资源约束？',67:'高保真部署与维持模型如何向规划层传递约束？',68:'ORBCOMM的任务需求如何落实到初始构型与部署？',70:'极地冰监测需求如何影响部署策略？',74:'成像与气象星座的任务规划能否共享运行机制？',75:'部署调度中发射、入轨与能力到位如何排序？',77:'被动安全如何限制脉冲重构的可行解？',78:'燃料目标与被动安全参数是否存在冲突？',79:'顺序优化降低计算量时牺牲哪些共同选择？',81:'序列凸方法怎样检查重构期间的碰撞约束？',82:'不同燃料优化方案是否在共同终态与时限下比较？',85:'分段伪谱与凸化怎样兼顾非线性轨迹和计算负担？',88:'随机轨迹优化如何传播重构安全的不确定性？',90:'失控后的被动退出安全怎样用机会约束表达？',91:'分布式安全控制依赖哪些通信和控制权假设？',95:'指派与轨迹共同优化在燃料和时间预算下的增益是什么？',97:'强化学习重构与重新任务分配是否使用可执行轨道模型？',98:'早期随机多阶段模型与2026 SDDiP版本有何实质区别？',100:'低推力重构如何维持多个目标的连续覆盖？',103:'遥感效能与重构控制是否使用同一评价口径？',104:'参数化强化学习动作如何保持机动可行性？',105:'真实低成本运控的人员、自动化和任务约束是什么？',106:'构型成本与业务覆盖如何形成设计取舍？',107:'紧急观测中机动与任务调度是否共同计入响应时间？',112:'自主任务分配怎样处理跨星共享约束？',113:'博弈式分配能否收敛且满足执行时限？',118:'轨道与密度联合估计如何影响维持预测和反馈？',125:'共识剪枝是否保留重要跨星任务机会？',132:'GEO多星维持有哪些可迁移的协调机制及不可迁移条件？',133:'网络可靠性怎样反馈构型成本，是否测量业务结果？',135:'南极任务的特殊地理需求如何决定轨道配置？',136:'条带宽度、轨迹与间断覆盖怎样共同影响成本？',138:'椭圆轨道设计与长期维持怎样共同约束通信构型？',149:'连续低推力重构的燃料最优性依赖哪些终态和时间条件？',155:'飞行动力学自动化怎样连接计划、检查和实际执行？'}
def theme(n):
 if n in [5,6,9,17,21,23,24,25,68,106,133,135,136,138]:return '任务指标与构型设计'
 if n in [51,52,54,60,70,75]:return '部署与可达时间'
 if n in [8,48,67,118,132]:return '构型维持与平台约束'
 if n in [38,74,105,155]:return '运行反馈与业务恢复'
 if n in [77,78,79,81,82,85,88,90,91,95,149]:return '重构与共同安全'
 return '任务资源与不确定重构'
selected=[]
for n in indices:
 x=data[n-1];m=x['metadata'];d=next((d for d in papers if d['doi'].lower()==x['doi']),None)
 selected.append(dict(stable_id=f'R2-C{n:03d}',doi=x['doi'],title=x['title'],authors='; '.join((a.get('given','')+' '+a.get('family','')).strip() for a in m.get('author',[])),year=x['year'],publication_date_parts=json.dumps(m.get('published',{}).get('date-parts',[])),venue=x['venue'],type=m.get('type',''),theme=theme(n),question_cn=questions[n],screen_level='BODY_READ' if d else ('METADATA_WITH_ABSTRACT' if m.get('abstract') else 'TITLE_METADATA_ONLY'),reading_id=d['id'] if d else '',reading_status=d['reading_status'] if d else 'NOT_BODY_READ',prior_id=d['old'] if d else '',project_relation='NOT_MATCHED_IN_CHECKED_REGISTERS',source_url=d['url'] if d else x['url'],metadata_url=x['url'],discovery_queries=';'.join(x['queries']),version_note=d['version'] if d else '仅书目候选；正式版/作者稿关系待取得正文后核对',adoption=d['adopt'] if d else 'CANDIDATE_NOT_CITED',human_verified=False))
for d in papers:
 if any(x['reading_id']==d['id'] for x in selected):continue
 selected.append(dict(stable_id='R2-'+d['id'][:4],doi=d['doi'],title=d['title'],authors=d['authors'],year=d['year'],publication_date_parts='',venue='见实际版本',type='原始研究或任务报告',theme=d['theme'],question_cn=d['claims'][0][1],screen_level='BODY_READ',reading_id=d['id'],reading_status=d['reading_status'],prior_id=d['old'],project_relation='PREVIOUS_LIBRARY_VERSION_REREAD' if d['old'] else 'NOT_MATCHED_IN_CHECKED_REGISTERS',source_url=d['url'],metadata_url=d['url'],discovery_queries='PRIMARY_SOURCE_TARGETED_SEARCH',version_note=d['version'],adoption=d['adopt'],human_verified=False))
csvwrite('CANDIDATE_POOL.csv',selected)
write('CANDIDATE_POOL_CN.md','# 定向候选池（'+str(len(selected))+'项）\n\n研究问题导向初筛，不是全部精读或质量认证。优先选择轨道设计、可达部署、维持、机动与业务共同决策、安全及运行反馈；纯网络协议或泛AI条目不扩展纳入。题名级候选只提出待核问题，不能支持正文结论。\n\n'+ '\n\n'.join('## '+t+'\n\n| ID | 年份 | 文献及原始入口 | 本轮关注的问题 | 阅读状态 |\n|---|---|---|---|---|\n'+'\n'.join(f"| {x['stable_id']} | {x['year']} | [{x['title']}]({x['source_url']}) | {x['question_cn']} | {x['reading_id'] or x['screen_level']} |" for x in selected if x['theme']==t) for t in dict.fromkeys(x['theme'] for x in selected)))
stats={'candidate_count':len(selected),'not_matched_in_checked_registers':sum(not x['prior_id'] for x in selected),'historical_version_reread_candidates':sum(bool(x['prior_id']) for x in selected),'body_read_records':len(papers),'not_body_read_candidates':sum(x['reading_status']=='NOT_BODY_READ' for x in selected),'adopted_read_sources':sum(x['adopt'].startswith('ADOPT') for x in papers),'reserve_read_sources':sum(x['adopt'].startswith('RESERVE') for x in papers),'human_verified':False,'submission_ready':False}
write('RESEARCH_COUNTS.json',json.dumps(stats,ensure_ascii=False,indent=2))
write('SEARCH_AND_SELECTION_CN.md',f'''# 检索、去重与阅读口径

本轮操作日期：2026-10-27。目标是补充“任务要求怎样决定轨道构型与机动，轨道能力又怎样影响业务”的证据；不宣称穷尽检索或PRISMA系统综述。

Crossref实际执行10个主题query.bibliographic查询，每个请求25项，8个成功、2个HTTP 429失败。原始成功请求共200条返回，按DOI和题名主题初筛后留下164条发现记录。164是原始发现池，不是164篇新精读，也不是164篇推荐引用。实际请求与失败见discovery/QUERY_LOG.json；未补造缺失查询。

进一步按具体研究问题选择50条Crossref候选，合并3条本批全文来源，再加入7条从原始出版、作者稿或任务报告定向找到的来源，共{len(selected)}项。题名级和带摘要元数据候选分别登记；没有正文就不报告其结果。候选中56项未在本轮核对的历史来源台账匹配、1项为历史N02版本复读。这个56是台账匹配结果，不能排除尚未统一的历史别名或版本。

去重以DOI为主、题名与作者版本关系为补充。REOSSP的2025会议与2026期刊线只列一项；Foster会议稿与正式N02归并。2025随机重构与2026 SDDiP作为相关但不同方法候选保留，不把它们当成两个独立任务飞行验证。作者库、论文引用表仅用于发现；实际采用论断来自已读取原文或原有可靠笔记。

10篇已取正文，完成问题—模型—方法—结果—限制的阅读并留笔记，其中8篇用于讨论稿，2篇保留待核。正式版配对和作者科学终核均独立于AI正文阅读。原始PDF及页面图保存在本机sources/和figures/，公开Git材料只发布笔记、来源入口和文件哈希，不批量重发第三方全文。

下一批优先：R2-C107（应急低推力与调度）、R2-C090（机会约束被动退出安全）、R2-C095（指派—轨迹共同优化）、R2-C079（大规模顺序重构）、R2-C070（极地任务部署）、R2-C118（密度与轨道估计）、R2-C038（地面自动化）、R2-C098（随机重构早期方法）、R2-C138（设计—维持耦合）、R2-C067（部署维护高保真接口）。优先级是取全文与判别科学增量的顺序，不预先保证采用。
''')
write('reading_notes/INDEX.md','# 阅读笔记索引\n\n'+'\n'.join(f"- [{d['id']}：{d['title']}]({d['id']}_CN.md) — {d['adopt']}" for d in papers))
print(json.dumps(stats,ensure_ascii=False))
