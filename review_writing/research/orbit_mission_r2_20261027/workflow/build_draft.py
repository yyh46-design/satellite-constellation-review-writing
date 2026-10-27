from pathlib import Path
import re,json,csv,difflib,hashlib
P=Path(__file__).resolve().parent
R1=Path(r'D:\SKT727\outputs\constellation_orbit_mission_discussion_r1_20261027')
s=(R1/'REVIEW_DISCUSSION_R1_CN.md').read_text(encoding='utf-8')
body,refs=s.split('## 参考文献',1)
oldrefs={int(n):t.strip() for n,t in re.findall(r'(?m)^(\d+)\. (.*?)(?=\n\n\d+\. |\Z)',refs,re.S)}
def replace(old,new):
 global body
 assert old in body,old[:80]
 body=body.replace(old,new,1)
start=body.index('大型卫星星座的业务能力')
end=body.index('\n\n**关键词',start)
body=body[:start]+'''大型卫星星座的任务能力既取决于轨道构型提供的访问机会，也取决于这些机会能否在动态环境中保持并转化为实际服务。摄动改变成员的相对几何，维持与重构消耗控制资源、占用业务时间，任务需求和资源状态又影响轨道行动的选择。本文以这一双向联系为主线，综述任务指标驱动的构型设计、利用自然摄动的部署与维持、面向需求变化的轨道重构，以及多星协调和运行反馈。代表性研究表明，同一星数下，平均重访与最长间断目标可得到不同构型；利用节点漂移减少直接平面机动，需要连同部署等待和剩余寿命评价；差动阻力的有效控制能力受到成像、通信、供电和热约束共同限制。在所研究的确定性观测算例中，轨道重构与观测、充电及下传共同安排提高了模型内下传量，而滚动求解以部分收益和预算分配质量换取更短计算时间。上述结果说明，任务与轨道决策的联系应通过具体机会、资源和时限表达：关键候选会被预先固定时，可联合相关变量；采用分层或分阶段方法时，则需传递并更新足以保持可行性的边界信息。共同安全还依赖相容的控制输入和更新规则，恢复评价应延伸到实际业务结果。面向大型星座，后续研究需连接任务容差与长期可维持性，处理需求和控制能力的不确定性，并验证局部决策在跨星资源竞争及响应期限下的运行效果。'''+body[end:]
replace('Rogers等的五类模型及其公开配套实现进一步区分了覆盖成本、覆盖比例、观测奖励、最大重访和平均重访目标[3]。作者公开的西雅图单目标算例中，两个方案均配置5颗卫星：最小化最大重访的方案，最大和平均重访分别为22 min和14.95 min；最小化平均重访的方案，相应为44 min和12.43 min。该对照采用相同的候选轨道族和离散周期，数值说明两种指标会选择不同的访问时间分布。这些数值来自作者配套仓库的结果表，而非本文重新求解。',
'''Williams Rogers等在同一离散槽位框架中建立覆盖成本、覆盖比例、观测奖励、最大重访和平均重访模型[3]。其西雅图单目标算例采用给定回归轨道族和120 s时间步长，两个方案均配置5颗卫星：最小化最大重访的方案，最大和平均重访分别为22 min和14.95 min；最小化平均重访的方案，相应为44 min和12.43 min。较小的平均等待伴随较大的最长间断，说明任务对时间分布的要求会改变构型选择。这一比较来自原文表8，最优性限于所用候选轨道与离散表示。''')
anchor='这一关系使任务所需的轨道面分布受到部署期限约束。它描述的是J₂差异进动提供的节点分离，具体转移持续时间和其他运行限制还需另行计入。'
replace(anchor,anchor+'''

McGrath和Macdonald进一步把升降轨、驻留、入轨及后续阻力补偿纳入部署分析[24]。其24星、4轨道面设定中，传统四次发射约需1年形成构型，单次500 km注入并利用节点漂移约需2.75年；这一差异依赖给定发射间隔、推力与轨道条件。减少发射次数因而可能延迟完整能力的形成，不同成员的部署消耗还会改变剩余任务寿命。与FORMOSAT-3/COSMIC实际TLE的比较则显示，停推、目标节点间隔改变及硬件故障会使部署偏离名义时间。这些运行事件使部署规划需要同时表达物理可达性和实际可用时刻。''')
anchor='成员数量增加后，姿态可用性还会转化为协调问题。S-NET规划把通信、值守等活动纳入运行可用率，并处理多个星对共享参考星时的切换冲突[9]。各星对独立计算的高、低阻力切换不能直接同时执行，论文通过延迟部分机动开始时刻同步共同切换。该序列属于规划和未来演示建议，其价值在于揭示共享成员如何连接原本局部的控制问题。'
replace(anchor,anchor+'''

Planet的差动阻力运行研究提供了实际相位控制的补充[25]。控制器先分配成员槽位，再对相互耦合的成员生成阻力命令；成像和下传活动可以抢占高低阻力模式，因此几何迎风面积并不能单独确定可用控制能力。Flock 2p十二星飞行中，有效控制能力一度比预测低约50%，造成超调和槽位反复调整，运控随后根据实际轨道更新估计。该文另列的88星结果是仿真。两类证据共同说明，任务层应提供控制姿态的可用时段，控制层则需返回经实际运行更新的到位时间。''')
anchor='相对轨道要素为目标几何与控制动作提供了直接联系。Gaias和D’Amico在近圆参考轨道的相对运动模型中分析多脉冲重构[11]：相对半长轴可以通过自然漂移积累沿轨变化，机动位置则影响相对偏心率等要素的改变。将终端时刻纳入模型后，可比较不同机动组合在给定转移时间内的代价。此时，允许等待多久、何时可以机动，本身就是方案选择的一部分。'
replace(anchor,anchor+''' 同一研究还表明，两类机动组合的代价排序可以随转移时域改变；当存在等代价机动位置时，时间余量也可用于避开部分禁用窗口。由此，较宽的时间安排不仅可能降低控制代价，还可能为载荷活动留出选择空间。''')
anchor='多阶段配置进一步将当前机动与后续机会联系起来。Lee等的确定性多阶段模型在阶段之间传递构型和机动预算，并比较不同前视范围的求解方法[14]。其目标路径全时域预知，适合分析预算跨阶段分配的影响；未来任务尚未揭示时，前视信息的可得性需要作为另一项条件处理。'
replace(anchor,anchor+'''

轨道变化对业务的影响还可以沿资源链继续评价。Pearl等建立可重构地球观测调度模型，在阶段边界选择轨道槽位，同时安排观测、充电和下传，并跟踪电量、存储与逐星机动预算[26]。在四星、7.25天、八阶段的Sandy已知历史路径算例中，固定轨道、全模型重构和滚动重构的模型内下传量分别为0.80、3.20和2.40 GB，求解时间分别为0.24、54.60和6.65 min。这里的下传量是评价指标，优化目标另由观测次数与加权下传次数组成。该结果说明，在所用候选轨道和资源条件下，机动增加的访问机会能够经调度转化为更多下传；有限转移过程的业务禁用和连续安全仍需在轨迹与执行层补充。

未来目标不确定时，轨道行动还需保留对不同需求情形的响应能力。Pearl和Lee的随机多阶段模型利用场景及后续价值近似选择构型[27]，将目标位置和奖励的不确定性带入决策。不过，该模型通过预先裁剪轨道槽位保证允许序列均满足预算，没有在任意轨道候选上继续优化全任务剩余预算；下传与充电也尚未共同纳入。一组两星轨道目标算例的计算约需60 h且未完全收敛，说明策略求解与当次运行响应的时间尺度需要分开。它为不确定目标提供了明确的建模路径，也提出了怎样同时保留机动预算与业务资源状态的问题。''')
anchor='区域重构研究则保持配置、指派和覆盖模型不变，比较拉格朗日启发式与限时混合整数线性规划[15]。紧机动预算组的18个实例中，启发式取得6个较高、10个较低和2个相同的目标值。这是同模型的求解器比较，与前述改变前视范围的比较属于不同维度。联合模型可以分解计算，分层组织也可以滚动更新。'
replace(anchor,anchor+'''

可重构观测调度的结果进一步显示，求解成功率和成功后的质量应同时报告[26]。24个随机实例中，全模型在10个实例返回数值可行解，这10例目标值均高于滚动方法；其余10例限时未得可行解，4例因内存不足失败，滚动方法则在全部实例得到可行解。全模型和每个滚动子问题各设60 min上限，因此并非同一累计计算预算。Sandy算例中，滚动方法虽更快，却使用了更多四星合计速度增量。这些结果支持依据响应期限选择可采用方案，同时保留完整模型在有解实例中的收益优势。''')
anchor='可行轨迹进入运行，还需要经过状态确认、检查和相应权限下的计划启用。Starling飞行动力学报告描述了地面生成、审查、接近筛查及运控批准之间的衔接[20]；NanoFF在轨报告记录的导航核查、地面冲突和模型修正则影响实际机动时刻[21]。这些事件说明，响应时间包括求解之外的协调和确认过程。'
replace(anchor,anchor+'''

连续低推力机动自动化系统CMAS给出了轨道行动与成像安排相互更新的实现方式[28]。系统用轨道容差描述维持目标，用机动机会约束表达占空比及保护时段，并将候选机动与无机动传播比较。机动被计划、执行或取消后，成像时刻和指向随之刷新；遥测与定轨确认的未执行、部分执行或完成结果再进入后续安排。该运营方报告提供的是地面流程和接口证据，星座级管理器仍列为扩展方向，尚未给出同条件的净业务收益对照。''')
replace('若每个局部问题只依赖有限邻居，局部计算可以随事件分散；若共享资源或安全约束跨越多个分组，则需要额外协调。','若每个局部问题只依赖有限邻居，局部计算可以随事件分散；若共享资源或安全约束跨越多个分组，则需要额外协调。Planet相位控制采用先槽位、后耦合命令的分阶段方法，体现了降低搜索负担的一种安排；其十二星飞行与88星仿真分别支持不同层级的规模判断[25]。')
start=body.index('已有研究形成了几项可用于组织后续工作的认识。')
end=body.index('\n\n进一步研究可以围绕三个问题展开。',start)
body=body[:start]+'''已有研究支持几项具体认识。首先，构型设计需要选择与任务一致的时间指标：五颗卫星的同条件对照中，平均重访与最大重访的最优方案并不相同[3]。其次，利用自然漂移形成或改变构型，需要连同等待、实际姿态可用率和逐星剩余能力评价；部署与差动阻力运行中的暂停、故障和控制偏差使这些条件具有直接工程意义[24][25]。再次，部分联合建模的价值可以沿任务链观察：在所研究的四星Sandy确定性算例中，重构与观测、充电、下传共同安排提高了模型内下传量，滚动求解则保留部分收益并缩短计算时间，同时付出额外预算代价[26]。这种条件性收益支持围绕关键依赖组织模型；不同前视范围、分解算法和更新频率仍应分开比较。最后，运行中的轨道变化需要反馈到后续任务，安全处置的最终价值应由任务是否及时接续来评价。

轨道动力学由此贯穿构型设计与协调运行：它决定可达构型、机会的时间演化和动作代价；任务需求则给出维持容差、响应期限及业务评价尺度。模型与运行证据共同构成二者之间的联系，但完整任务—轨道—安全过程仍缺少同条件、直接业务结果的比较。''' +body[end:]
oldrefs[3]='Williams Rogers DO, Won D, Koh D, Hong K, Lee HW. Optimal Satellite Constellation Configuration Design: A Collection of Mixed Integer Linear Programs. Journal of Spacecraft and Rockets, 2026, 63(4):1144–1162. DOI:10.2514/1.A36518. 实际阅读版本：arXiv:2507.09855v2. [原文](https://arxiv.org/pdf/2507.09855v2)'
oldrefs[23]=oldrefs[23].replace('[实际来源]()','[来源](https://doi.org/10.1613/jair.1.16997)')
oldrefs[24]='McGrath CN, Macdonald M. General Perturbation Method for Satellite Constellation Deployment Using Nodal Precession. Journal of Guidance, Control, and Dynamics, 2020, 43(4):814–824. DOI:10.2514/1.G004443. [作者接受稿](https://strathprints.strath.ac.uk/71130/1/McGrath_Macdonald_JGCD_2020_General_perturbation_method_for_satellite_constellation_deployment.pdf)'
oldrefs[25]='Foster C, Mason J, Vittaldev V, Leung L, Beukelaers V, Stepan L, Zimmerman R. Differential Drag Control Scheme for Large Constellation of Planet Satellites and On-Orbit Results. IWSCFF 17-33, 2017. 实际阅读版本：arXiv:1806.01218v1；与历史来源N02同研究线，正式版配对另记。 [原文](https://arxiv.org/pdf/1806.01218v1)'
oldrefs[26]='Pearl BD, Miller JM, Lee HW. Reconfigurable Earth Observation Satellite Scheduling Problem. Journal of Aerospace Information Systems, 2026, 23(2):136–154. DOI:10.2514/1.I011659. 实际阅读版本：arXiv:2507.10394v3. [原文](https://arxiv.org/pdf/2507.10394v3)'
oldrefs[27]='Pearl BD, Lee HW. Stochastic Multistage Constellation Reconfiguration Problem: Stochastic Dual Dynamic Integer Programming Approach. arXiv:2608.09738v1, 2026. 预印本。 [原文](https://arxiv.org/pdf/2608.09738v1)'
oldrefs[28]='Mascolo L, Thawer Z, Paul A. A Continuous Low-Thrust Maneuver Automation System for Electric Propulsion LEO Satellite Operations. SpaceOps 2025, ID105. DOI:10.82217/spaceops2025_105. [会议原文](https://publications.spaceops.org/2025/download_by_id.php?id=0105)'
order=list(dict.fromkeys(int(n) for n in re.findall(r'\[(\d+)\]',body)))
assert set(order)==set(oldrefs),(set(oldrefs)-set(order),set(order)-set(oldrefs))
mapping={old:i for i,old in enumerate(order,1)}
body=re.sub(r'\[(\d+)\]',lambda m:f'[{mapping[int(m[1])]}]',body).replace('一部分。 同一研究','一部分。同一研究')
draft=body+'## 参考文献\n\n'+'\n\n'.join(f'{mapping[n]}. {oldrefs[n]}' for n in order)+'\n'
for suffix in ['md','txt']:(P/f'REVIEW_DISCUSSION_R2_CN.{suffix}').write_text(draft,encoding='utf-8')
prior={int(x['number']):x for x in csv.DictReader((R1/'SOURCE_AND_CLAIM_REGISTER.csv').open(encoding='utf-8-sig'))}
new={x['id']:x for x in csv.DictReader((P/'READING_REGISTER.csv').open(encoding='utf-8-sig'))}
with (P/'REFERENCE_REGISTER_R2.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['r2_number','r1_number','stable_id','new_reading_id','reference_text','actual_version','evidence_record','locator','evidence_origin','human_verified']);w.writeheader()
 ids={3:'N001_ROGERS',7:'N004_HULL',11:'N005_GAIAS',24:'N007_MCGRATH',25:'N010_FOSTER',26:'N002_PEARL',27:'N009_SDDIP',28:'N003_CMAS'}
 for n in order:
  q=new[ids[n]] if n in ids else prior[n]
  w.writerow(dict(r2_number=mapping[n],r1_number=n if n<=23 else '',stable_id=('N02 / '+ids[n] if n==25 else ids[n]) if n in ids else q['stable_id'],new_reading_id=ids.get(n,''),reference_text=oldrefs[n],actual_version=q['version'] if n in ids else q['actual_version'],evidence_record='reading_notes/'+ids[n]+'_CN.md' if n in ids else q['prior_record'],locator='CLAIM_REGISTER.csv: '+ids[n] if n in ids else q['locator_and_boundary'],evidence_origin='本轮原文正文阅读' if n in ids else '既有登记与阅读记录沿用，未重复计数',human_verified=False))
(P/'R1_TO_R2.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),draft.splitlines(True),fromfile='local-discussion-R1',tofile='research-discussion-R2')),encoding='utf-8')
print(json.dumps({'references':len(order),'chinese_chars':len(re.findall('[\u4e00-\u9fff]',body)),'first_citation_order':list(mapping.values()),'r1_to_r2_number_map':mapping},ensure_ascii=False))
