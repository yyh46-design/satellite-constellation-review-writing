# Intelligent Management and Scheduling of Large Satellite Constellations: Application Scenarios, Technical Approaches, and Operational Practice

## Abstract

Large satellite constellations must coordinate time-varying service demand, limited resources, and changing spacecraft availability. This problem-driven narrative review treats Earth observation and communication networks as two principal service domains and examines long-term capability planning, mission and network-resource scheduling, safe execution, recovery, and integrated operations. Representative models are compared through their decision variables, information assumptions, solution and update mechanisms, performance measures, and validation environments. Incremental planning and geometric neighborhood decomposition reduce different computational and coordination burdens; their effects on task satisfaction, redundancy, and solution quality depend on workload and baselines. Observation, processing, and delivery can be connected through joint selection, staged optimization, or feedback rather than a universal end-to-end solver. Communication management must address interference, user association, handover, and time-varying routing under different network assumptions. Operational interfaces, independent measurements, and bounded flight demonstrations provide evidence complementary to algorithmic studies. The review synthesizes developments across service domains and management functions and discusses service restoration, dynamic resource coordination, plan revision, and cross-module validation as future research questions.

**Keywords:** large satellite constellations; intelligent management; mission scheduling; satellite communication networks; resource allocation; autonomous operations

# 1. Introduction

## 1.1. Expanding Services and the Requirement for Sustained Operations

Large constellations must simultaneously serve users or observation requests across many orbital planes and maintain the spacecraft resources on which those services depend. The scheduling problem is consequently not limited to assigning each current request to a satellite. Operators must also select future orbital configurations, sustain spare assets, and revise existing plans when equipment or orbital conditions change. The scaling of ground operations and autonomous functions in distributed space systems has already been discussed by Ben-Larbi et al. [1](https://doi.org/10.1016/j.asr.2020.08.009), [6](https://doi.org/10.1016/j.asr.2020.08.018).

The operational demands of Earth-observation and communication constellations differ. Observation scheduling selects discrete or periodically repeated target acquisitions within visibility windows and subject to attitude, onboard storage, processing, and downlink limits. The mission result may concern the acquisition, an acceptable image, or a delivered product. Communication systems must continuously support changing user traffic, beam and gateway assignments, satellite handovers, and routes through a dynamic network. Their outcomes involve throughput, latency, interruption, loss, fairness, and energy use. A larger constellation does not automatically solve either problem: more spacecraft can add potential task opportunities while also increasing coordination requirements, interference, or route changes.

Long-term maintenance and safe execution affect both service domains. Spare and replenishment policies change future spacecraft availability; maneuvers and failures can disrupt observations and alter communication paths or regional capacity. On-orbit servicing and logistics are treated here as maintenance and mission-planning activities that may support multiple service domains, not as a third application category with an identical service metric. The objective of this review is to explain the resulting family of models and solution methods, the conditions behind their performance, and the extent of available implementation evidence.

## 1.2. Existing Reviews and the Added Analytical Perspective

Previous reviews provide substantive classifications of several constituent topics. Wang et al. [3](https://doi.org/10.1109/JSYST.2020.2997050) summarize the formulation, constraints, variants, and algorithms of agile Earth-observation scheduling. Ferrari et al. [4](https://doi.org/10.1016/j.cor.2024.106875) cover Earth and space observation, including imaging, communications, and integrated scheduling. The communications activities in those scheduling studies are not necessarily equivalent to allocating continuous subscriber traffic in broadband constellations. Jabbarpour et al. [5](https://doi.org/10.1016/j.actaastro.2025.10.018) survey agent-based architectures and coordination; Ben-Larbi and colleagues [1](https://doi.org/10.1016/j.asr.2020.08.009), [6](https://doi.org/10.1016/j.asr.2020.08.018) investigate operational automation paradigms and tools.

Reviews devoted to communication mega-constellations address demand prediction, access, topology, routing, and multidimensional resource control. Two recent Chinese-language reviews [7](https://doi.org/10.7527/S1000-6893.2026.32935), [8](https://doi.org/10.3873/j.issn.1000-1328.2026.02.002) document these areas in their publicly accessible abstracts; their full contents were not used to infer the absence of any subject. Singla et al. [9](https://doi.org/10.3390/technologies13080312) explicitly examine relationships between satellite operations (SatOps) and network operations (NetOps). Thus, neither coupling across management layers nor integrated satellite/network control is presented as a concept introduced for the first time here.

**Table 1. Related surveys and the comparison questions addressed in this review**

| Prior survey | Principal scope and classification | Corresponding focus here |
| --- | --- | --- |
| Wang et al. [3](https://doi.org/10.1109/JSYST.2020.2997050) | Agile observation models, variants, and algorithms | Acquisition, timing, delivery, and uncertainty as different decision outcomes |
| Ferrari et al. [4](https://doi.org/10.1016/j.cor.2024.106875) | Imaging, communications, and integrated observation scheduling | Data-delivery dependencies and differences from continuous user-network service |
| Jabbarpour et al. [5](https://doi.org/10.1016/j.actaastro.2025.10.018) | Agent-based coordination and mission management | Information availability, competition, and distributed decision conditions |
| Ben-Larbi et al. [1](https://doi.org/10.1016/j.asr.2020.08.009), [6](https://doi.org/10.1016/j.asr.2020.08.018) | Distributed-system automation and tools | Models, software responsibilities, operations, and recovery events |
| LEO network surveys [7](https://doi.org/10.7527/S1000-6893.2026.32935), [8](https://doi.org/10.3873/j.issn.1000-1328.2026.02.002) | Demand, topology, access, routing, and resource control in available abstracts | Communication management as a major business problem linked to operations |
| SatOps–NetOps study [9](https://doi.org/10.3390/technologies13080312) | Operations/network coordination and architecture | Coupled variables, update events, and the domain of actual validation |

We organize prior work using a cross-classification of **service domain and management function**. The first analytical contribution is to compare decision objects, resource and information conditions, and completion measures across two core businesses. The second is to relate solution mechanisms to workload, baselines, communication conditions, and costs. The third is to connect mathematical outputs to activities actually described in operational or flight materials, while retaining the limits of that evidence. These are contributions of synthesis rather than claims that all surveyed systems implement a common architecture or that we propose a new optimal controller.

## 1.3. Scope and Review Method

This is a problem-driven **narrative technical review**, based on prior topic searches, reference tracing, and targeted additions for communication-network management. It does not claim exhaustive systematic retrieval, a reproducible full-database screening procedure, or a statistical meta-analysis. Research was selected for its relevance to capability provision, observation scheduling, network allocation, safety and fault recovery, or interactions among these functions. General waveform design and device-level communications are considered only where they impose material constraints on constellation-wide decisions.

Earth observation and communication networks remain the core service domains. On-orbit servicing, logistics, collision-risk mitigation, and recovery enter as supporting management functions. Findings from one spacecraft, geostationary missions, deep space, and general multi-agent systems are used as methodological references with their original conditions maintained. We do not use a single satellite-count threshold for "large"; candidate windows, request density, resource coupling, messaging, and planning horizons can independently affect computational and operational scale.

The extraction dimensions include decision variables, constraints, information availability, solution and updating mechanisms, evaluation metrics, and experimental settings. Comparisons across a common model emphasize quality and cost; comparisons across different models first clarify how the problems themselves differ. Industry documents and flight reports establish only the interfaces, actions, and tests actually disclosed. Sections 2 and 3 present the modelling basis and relevant technical research; Section 4 synthesizes performance conditions and opportunities for further work; Section 5 concludes.

# 2. Operational Requirements, Management Architectures, and Problem Formulation

## 2.1. Cross-Classifying Applications and Management Problems

Constellation operations have both application-specific and management-specific features. Earth observation provides information products for target requests, while communication networks provide continuing subscriber access and data transfer. Both require capability provisioning, scheduling and allocation, safe implementation, and recovery. Availability changes caused by spacecraft faults or replenishment may affect observation opportunities, product delivery, local network capacity, and continuity of coverage.

**Table 2. Cross-classification of service domains and management functions**

| Management function | Earth-observation service | Communications service | Sections |
| --- | --- | --- | --- |
| Long-term capability and maintenance | Orbits, coverage, spares, replenishment, servicing facilities | Constellation and payload capacity, beams, gateways, redundancy | 3.1 |
| Operational scheduling and allocation | Request selection, imaging, processing, downlink, delivery | Access, beam/power/spectrum, handovers, routing, congestion | 3.2–3.3 |
| Safe execution and recovery | Maneuver safety, instrument faults, repair, reacquisition | Maneuver safety, degraded nodes/links, capacity and connection restoration | 3.4 |
| Coupled decisions and feedback | Observation choice interacts with delivery and actual execution | Access and routing depend on platform and network states | 3.5 |

Distributed observation allocation and hierarchical beam management may use related coordination ideas, but their business objects and performance measures differ. Figure 1 summarizes this distinction. The figure is an analytical organization of the literature, not a proprietary implementation.

![Figure 1. Cross-classification of service domains and management decisions](figures/operations_cross_matrix_v1.7.svg)

*Figure 1. Cross-classification of service domains and operational management functions. The diagram summarizes dependencies discussed in the literature; it does not indicate that any operator deploys a unified architecture.*

## 2.2. Decision Levels and Time Scales

We distinguish capability provisioning, operational allocation, and execution/recovery according to the variable that a decision changes rather than by a universal time threshold. Capability planning defines future asset quantities, locations, and effective availability. Operational scheduling assigns current or rolling-horizon tasks, users, beams, or paths within that capacity. Execution and recovery modify physical or software actions and return actual status, resource consumption, faults, and task outcomes.

The distinction is applicable to both businesses. An observation task and beam-allocation scheme can each be updated through rolling optimization, while a maneuver may have immediate effects on coverage but lasting implications for orbit maintenance. The choice of joint, hierarchical, or independently updated models depends on the strength of dependencies and the cost of coordinating decisions.

## 2.3. Centralized, Hierarchical, and Distributed Information Structures

In a centralized architecture, a designated planner has global or nearly global resource information. Hierarchical architectures distribute responsibilities by region, orbital plane, function, or management domain. Distributed systems rely on local states and inter-agent messages. Architecture and algorithm are separate design dimensions: a decomposed mathematical program can still execute centrally, while a policy trained jointly may be deployed across independent agents.

Physical communication links determine when messages may pass. Management topology describes responsibility for collecting and updating state. Task-conflict and network-resource graphs indicate which decisions must be coordinated. Dynamic management domains [10](https://doi.org/10.34133/space.0248), for example, track changing managerial associations caused by orbital motion; they do not in themselves specify observation-task conflicts or physical packet routes. The scope and timing of information exchange must follow the relevant dependency.

## 2.4. States, Constraints, and Objectives

Earth observation and broadband communications share platforms, orbits, power, computing resources, and ground infrastructure but describe workloads differently. Observation uses target requests, visibility windows, priorities, deadlines, and quality. Network allocation uses subscriber traffic, arrival rates, queues, channel state, interference, and quality-of-service commitments.

**Table 3. Characteristics of decision models in the two principal application domains**

| Dimension | Earth-observation scheduling | Communication-network allocation |
| --- | --- | --- |
| Workload | Target requests, viewing windows, priorities, image quality, deadlines | Traffic by user or cell, arrivals, forecasts, QoS requirements |
| Decisions | Assignment, imaging time, processing, storage and delivery | Access/handover, beam pointing, power/spectrum, gateways, route |
| Constraints | Attitude, power, storage, computing, ground passes | Interference, beam/link capacity, power, queues, topology |
| Outputs | Valid requests, value, revisit, delivery deadline, solver time | Throughput, latency, interruption, packet loss, fairness, energy, control overhead |
| Uncertainty | New requests, cloud and product quality, faults | Traffic forecast error, link changes, congestion, failures |

Adding an energy, interference, or orbital constraint changes feasibility; it need not change what the objective rewards. Redefining success from an image acquisition to delivery of an acceptable product, or from nominally allocated network capacity to service meeting QoS, changes the event associated with value. This distinction also applies to inventory availability and actual service restoration.

## 2.5. Scale, Total Cost, and Verification Objects

Scale depends on more than satellite count. Increasing candidate windows, task precedence constraints, traffic density, links, or inter-domain interference can change complexity independently. Costs arise from state generation, preprocessing, central or distributed solution, communication and confirmation, learning, and the re-activation of an updated plan. Online neural-network inference may be only one item.

A predictor produces an estimate rather than a directly executed plan. An optimizer returns a solution satisfying a particular mathematical model. A coordination method attempts to reconcile agent choices under communication rules; a controller computes physical actions. Simulation, module testing, interface documentation, operator reports, and flight demonstrations verify different properties. Evaluation should identify the exact object and operating conditions tested, rather than treating them as interchangeable evidence.

---

# 3. Principal Technical Approaches to Constellation Management and Scheduling

Constellation management includes the establishment of future capabilities, the allocation of operational resources, and the handling of execution failures. These activities are connected through asset availability, task dependencies, and state feedback. The following discussion is organized by management function and service domain rather than by algorithm name alone.

## 3.1. Long-Term Capability Planning and Sustained Maintenance

Long-term planning changes what resources will be available to schedulers and when. Constellation geometry determines observation and coverage opportunities, replenishment determines the effect of spacecraft failures, and orbital servicing facilities determine which customers can be reached. Ho's space-logistics review [2](https://doi.org/10.2514/1.A35982) relates network flow, inventory, and operational activities to orbital transfer and waiting times.

### Constellation Design, Deployment, and Reconfiguration

The tradeoff between coverage and the cost of moving toward a desired arrangement is central to reconfiguration. Appel et al. [11](https://doi.org/10.1016/j.actaastro.2014.02.016) optimize coupled maneuvers for a specified terminal constellation. Lee and Ho [12](https://doi.org/10.2514/1.A35685) simultaneously choose regional coverage patterns and assign satellites to the new positions. Multistage reconfiguration [13](https://doi.org/10.2514/1.A35990) adds configuration and transfer decisions across successive periods, using future-stage demands that are known in advance. These studies differ primarily in how target configurations and time-varying requests enter the decision model.

The feasibility of the deployment process further restricts which patterns can actually be selected. Regional pattern optimization [14](https://doi.org/10.2514/1.A34657) uses convolution structure and integer programming; uncertain target areas are examined through deployment scenarios [15](https://doi.org/10.1016/j.actaastro.2018.03.054). Gwon and Ahn [16](https://doi.org/10.1007/s42405-026-01298-1) incorporate parking duration, J2-driven right-ascension drift, launcher capacity, and completion windows into a two-stage design procedure. Its reachability approximation is a screening step in configuration planning rather than a demonstration of complete launch and transfer trajectories. Accordingly, a constellation's eventual coverage and the time and cost required to establish it should be evaluated separately.

### Platform Capacity and Gateways of Communication Constellations

Geometrical coverage does not by itself establish communication capacity. At a given geometry, the satellite payload, available beams, power, gateway locations, traffic distribution, and routes can produce very different service bottlenecks. Joint satellite platform and constellation sizing [17](https://doi.org/10.1016/j.comnet.2024.110942) links beam-hopping requirements to payload design, orbital arrangement, and constellation size. Comparisons of LEO and very-low-Earth-orbit designs are conditional on the study's traffic, coverage, platform, and cost assumptions.

Long-term design defines the geographical and temporal capacity envelope; network scheduling determines how that envelope is used by actual traffic. In highly nonuniform demand conditions, adding geometrical coverage may not relieve a congested hot spot. Platform characteristics and network infrastructure thus constrain downstream beam and route decisions, even when the formal planning models are solved at different times.

### Spares, Replenishment, and Recovery of Lost Capability

Random failures create recurring demand for spare spacecraft and replenishment. Jakob et al. [18](https://doi.org/10.2514/1.A34387) represent ground inventory, parking-orbit spares, and in-plane spares as a multi-echelon system and jointly examine spare quantities and replenishment policies. Relative orbital drift affects the transfer delay between planes; the model was evaluated across 25 parameter cases and repeated long-term stochastic simulations. The in-plane replacement is approximated as immediate, an assumption that may be appropriate for spares already in position but does not include an additional local repositioning maneuver when such a maneuver is needed. Inventory demand satisfaction and operational restoration therefore measure different stages.

Subsequent models add supply-channel choices and more detailed stochastic states. A dual-supply formulation [19](https://doi.org/10.2514/1.A36281) contrasts direct injection with replenishment through a parking orbit. Han and colleagues [20](https://doi.org/10.2514/1.A36599) use coupled Markov-chain states for in-plane and parking inventories and fixed-point iteration for steady-state estimates, while a dual-channel extension [21](https://doi.org/10.1016/j.actaastro.2026.06.020) models the two replenishment routes. Steady-state supply performance is informative for long-term investment; recovery after a particular failure has a more event-specific temporal interpretation.

Iridium's documented deployment of five additional spare satellites [22](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites) provides an operational example of spare provisioning. It confirms that redundancy is an actual investment, but does not independently measure the time required for all possible subsequent replacements. Service-based maintenance adds another alternative: Kim et al. [23](https://doi.org/10.2514/1.A36684) combine new-spacecraft replacement and restoration by on-orbit servicing in a two-objective economic model. An annual maintenance-cost reduction of up to 14.5% is reported for selected cases relative to a specified no-servicing baseline. That figure is conditional on the failure model, recoverable fraction, operator and servicer prices, and chosen case; it is not a universal benefit.

### Servicing Facilities and Uncertain Demand

Orbital facility location couples depot positions with client allocation and transfers. Shimane et al. [24](https://doi.org/10.2514/1.A35691) optimize depot selection and service assignments. Choi and Ho [25](https://doi.org/10.2514/1.A36386) extend facility location into a continuous orbital design space, alternating mixed-integer and nonlinear subproblems and studying a GPS constellation service case. Fixed candidates retain discrete selection structure, while continuous locations provide more freedom and tighter coupling with transfer cost.

Deployment strategies [26](https://doi.org/10.1155/2021/6644339) use the accessibility of potential clients to place servicers. A demand-uncertainty framework [27](https://doi.org/10.2514/1.A34978) updates servicing and logistics over a rolling horizon; propulsion tradeoff models [28](https://doi.org/10.2514/1.A35094) connect transfer characteristics to short-term schedules and longer-term infrastructure. Lifecycle analysis [29](https://doi.org/10.1016/j.actaastro.2013.02.005) distinguishes aleatory from epistemic uncertainty. Collectively, these studies demonstrate that facility investment, customer access, service times, and demand information require compatible temporal assumptions.

## 3.2. Earth-Observation and On-Orbit Servicing Mission Scheduling

Both observation and servicing scheduling involve choosing, assigning, and ordering activities, but opportunities are generated differently. Visibility and attitude restrict observation candidates; orbital transfers, client motion, propellant, and replenishment affect servicing candidates. Dynamic requests and resource constraints turn static assignment into the management of a changing set of feasible activities.

### Observation Selection, Allocation, and Timing

For agile observation, the feasible acquisition time depends on visibility and attitude slewing. Lemaître et al. [30](https://doi.org/10.1016/S1270-9638%2802%2901173-2) compared constructive and search methods including greedy selection, dynamic programming, constraint programming, and local search. A Markov-decision formulation [31](https://doi.org/10.1109/TSMC.2020.3020732) employs learning for sequencing with a further timing heuristic, whereas decomposition-and-learning multi-objective scheduling [32](https://doi.org/10.1016/j.swevo.2024.101792) combines allocation, ordering, and repair. In each case, an apparent list of desirable tasks must still be transformed into a time-feasible activity plan.

An integrated mixed-integer model can express task selection, satellite assignment, and conflicting activities, although the search space grows with the available combinations. Antunes et al. [33](https://doi.org/10.1016/j.cor.2025.107259) distinguish common tasks from those tied to a specific nanosatellite and incorporate charging and discharging of batteries. Their branch-and-price method compares Dantzig–Wolfe decompositions, uses dynamic programming for pricing and adds stabilization, strong branching, and integer heuristics. Its methodological importance is the exploitation of problem structure with bounds referring to the specified discrete optimization model; it does not establish equal efficiency for arbitrary energy models.

When decisions are decentralized, performance also depends on the information available to each participant. Parjan and Chien [34](https://doi.org/10.2514/1.I011215) compare centralized, broadcast-based, and highly decentralized allocation over a one-week scenario with 100 satellite agents and 634 ground targets. Their broadcast variants differ in whether agents share competition or request-satisfaction information. Under fixed conflict intervals and simplified capacity limits, incremental planning can reduce computation while increasing redundant observations; its experiment also shows that request satisfaction and redundancy may improve and worsen simultaneously, so one metric cannot stand for all aspects of quality.

Zilberstein et al. [35](https://doi.org/10.1613/jair.1.16997) formulate a distributed constraint optimization problem (DCOP) using geometric neighborhood decomposition (GND) and neighborhood stochastic search (NSS). The agents share requests and constellation geometry but not all of one another's detailed execution capabilities. Simulation cases comprising 200 or 108 spacecraft over 24 hours account for storage and downlink restrictions and compare satisfaction, computation and messages. On a smaller request set, the geometric method can improve satisfaction as well as computation and messaging relative to the specified broadcast heuristic; in larger scenarios, the quality–cost relationship changes. Neither local decomposition nor broad broadcasting has a baseline-independent performance ranking.

Krigman et al. [36](https://doi.org/10.1007/s10951-024-00816-x) distribute observation requests among agents with DCOP algorithms that avoid centralizing private request information. Consensus-based bundle auctions [37](https://doi.org/10.1109/TRO.2009.2022423) instead use bids, bundles, and consistency updates to resolve assignment conflicts. Incomplete communications create additional difficulties: Li et al. [38](https://doi.org/10.1016/j.asr.2020.02.018) predict communication opportunities in synchronous and asynchronous bundle allocation, whereas delayed-communication planning [39](https://doi.org/10.1109/JSEE.2016.00066), onboard contract-net and blackboard coordination [40](https://doi.org/10.1016/j.asr.2021.09.003), and general asynchronous market allocation [41](https://doi.org/10.24963/ijcai.2023/30) address different message conditions. Information semantics, latency and competition jointly determine which decentralized arrangements can be reconciled.

### Joint Arrangement of Observation, Processing, Downlink, and Delivery

Data acquisition may have limited value if no suitable downstream transfer exists. He et al. [42](https://doi.org/10.1109/TMC.2021.3076088) jointly represent imaging and transmission windows using an integer programming model solved with semidefinite relaxation and genetic search. Energy-aware joint scheduling [43](https://doi.org/10.1016/j.actaastro.2025.02.008) adds charging to observation and downlink decisions through multiknapsack allocation and an improved ant-colony approach. Integrated agile scheduling [44](https://doi.org/10.1016/j.cor.2025.107212) further models acquisition and downlink, while heterogeneous tip-and-cue missions [45](https://doi.org/10.1016/j.actaastro.2026.04.059) include precedence between initial detection and follow-on observations. Thus, different problems reward completed acquisitions, transmissions, or dependent chains.

Shared ground stations impose additional constraints. Single-spacecraft/multistation optimization [46](https://doi.org/10.1016/j.cor.2014.11.004), Air Force control-network scheduling [47](https://doi.org/10.1023/B:JOSH.0000013053.32600.3c), and empirical downlink scheduling [48](https://doi.org/10.1016/j.omega.2015.01.001) model competition among station contacts. Mixed-integer formulations for the Deep Space Network [49](https://doi.org/10.1109/ACCESS.2021.3064928) and operational automated scheduling [50](https://doi.org/10.1609/aimag.v35i4.2552) likewise distinguish geometrical contact opportunities from a confirmed resource schedule. Their mission domains differ, so their numbers should not be pooled into a common satellite-network benchmark.

Commercial interfaces provide explicit completion and commitment states. The Planet Tasking API [51](https://docs.planet.com/develop/apis/tasking/) distinguishes acquisition, quality evaluation, and delivery, and some orders may require further collection attempts. AWS Ground Station [52](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html) typically requires cancelling and rebooking to change the time or mission profile of an existing contact. Its [contact versioning documentation](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.versioning.html), however, permits limited ephemeris or target updates without cancelling the window and specifies asynchronous confirmation. These operational interfaces do not reveal proprietary optimization algorithms; they do establish different states of resource commitment and plan modification.

Onboard computation introduces a further processing decision. The publicly available author version by Soret et al. [53](https://doi.org/10.1002/sat.70082) first selects acquisitions under time, attitude, and power limits and then uses the resulting workload and downstream windows to optimize processing assignments and processor frequency across satellites and ground stations. The publisher abstract describes two coupled optimization problems, while the detailed ordering and fixed processing pipeline are supported by the author manuscript, not by an established complete identity with the formal Wiley version. These results concern modelling and numerical evaluation rather than a demonstrated deployed autonomous constellation.

Related work considers multi-agent offloading [54](https://doi.org/10.1109/JIOT.2024.3482290), centralized training with decentralized processing [55](https://doi.org/10.1016/j.comcom.2024.05.008), and satellite–ground collaborative inference [56](https://doi.org/10.1109/TMC.2025.3570799). Orbit-aware computational scheduling [57](https://doi.org/10.1007/s10586-025-05663-9) incorporates contact variation; Kodan [58](https://doi.org/10.1145/3582016.3582043) changes model-processing costs through offline specialization and runtime selection. Moving computation to another node differs from altering the work required by one task. Both methods need joint consideration of inference quality, transmission, and deadlines.

### Dynamic Requests, Uncertainty, and Replanning

Changes in requests can alter existing assignments and the feasible order of activities. Qin et al. [59](https://doi.org/10.1016/j.asr.2025.12.008) solve a dynamic multiknapsack task allocation using Lagrangian methods and repair sequences through backtracking and recursion. Their reported experiments reach 1,000 spacecraft and 50–6,000 tasks. This differs from fixed-period column generation [33](https://doi.org/10.1016/j.cor.2025.107259): the former places particular emphasis on new arrivals and revision of the previous sequence.

Cloud uncertainty affects the probability that an acquisition will yield a useful product. Proactive chance-constrained scheduling [60](https://doi.org/10.1016/j.cor.2016.04.014), budget-robust methods [61](https://doi.org/10.1109/TAES.2019.2947978), and scenario-based multistage stochastic programming [62](https://doi.org/10.1016/j.ejor.2018.11.043) have different uncertainty and information assumptions. Choosing an acquisition under a probability distribution is not the same as responding to actual image-quality feedback through a new request. Both can be valuable for different operational conditions.

In online algorithms, reinforcement learning plays several distinct roles. Qi et al. [63](https://doi.org/10.1016/j.eswa.2025.128502) use a trained policy to construct an initial solution within rolling-horizon instances and then apply destroy–repair large-neighborhood search. Another rolling-horizon multi-agent method [64](https://doi.org/10.1016/j.eswa.2025.128350) organizes centralized training and decentralized execution. These differ from communication-aware negotiation [38](https://doi.org/10.1016/j.asr.2020.02.018) and contract-net updates [40](https://doi.org/10.1016/j.asr.2021.09.003), where the exchanged messages participate directly in reconciling decisions.

Herrmann et al. [65](https://doi.org/10.2514/1.A35736) train a policy in a single-spacecraft environment and reuse it across Walker constellation members under full, single-hop, multihop, and absent communication. Sharing images already acquired or delivered reduces some redundancy but does not necessarily avoid simultaneous selection because future intentions have not been confirmed. The related Basilisk comparison [66](https://doi.org/10.3389/frspt.2023.1263489) reports PPO, resource-masked PPO, A2C, DQN, MCTS-Train and genetic search. Performance and training costs depend on task complexity; simulation resets and replays contribute to the costs of search-based training. Hence training, online policy execution, and multi-satellite coordination are separate cost components.

### Servicing Routes, Replenishment, and Execution Conditions

Servicing customers move continuously, and route cost can depend on departure epoch, spacecraft mass, propulsion and refueling. A time-varying routing and scheduling model [67](https://doi.org/10.1016/j.cie.2022.108852) links service craft, clients and refueling sites. GEO refueling under uncertain duration [68](https://doi.org/10.1016/j.cja.2025.103774) uses a budget uncertainty set, while multiple-service-craft planning [69](https://doi.org/10.1016/j.asr.2017.05.037) and mixed refueling/debris-removal missions [70](https://doi.org/10.1016/j.asr.2024.05.059) incorporate different transfer and uncertainty conditions.

Low-thrust servicing is particularly dependent on state-specific transfer costs. Apa and colleagues [72](https://doi.org/10.1007/s40295-025-00487-6) precompute transfers indexed by orbits, mass and epoch for combinatorial search. A thrust–drift–thrust servicing formulation [71](https://doi.org/10.1007/s40295-026-00580-4) includes J2 effects, drag, eclipses and mass variation in transfer models and uses interpolation and a genetic algorithm for the outer customer sequence. Phasing costs are estimated after the principal optimization rather than included in its objective. Neither offline transfer tables nor a favourable discrete route proves satisfaction of all proximity-operations and terminal constraints.

**Table 4. Representative observation and servicing methods and their conditions**

| Study | Decisions and resources | Information and sharing | Solution or revision | Validation | Contribution and qualification |
| --- | --- | --- | --- | --- | --- |
| Branch-and-price [33](https://doi.org/10.1016/j.cor.2025.107259) | Common/specific tasks and battery | Common task/resource model | Decomposition and column generation | Nanosatellite simulations | Model-relative bounds depend on pricing structure |
| Hierarchical MIP [59](https://doi.org/10.1016/j.asr.2025.12.008) | Allocation, order, arrivals | Request/conflict set | Lagrangian assignment and repair | Up to 1,000 satellites, 50–6,000 tasks | Dynamic response depends on task structure |
| Decentralized allocation [34](https://doi.org/10.2514/1.I011215) | Requests and simplified capacity | Central/broadcast/local competition states | Rules and incremental planning | 100 agents, 634 targets; serial simulation | Information and update rules affect redundancy |
| Geometric decomposition [35](https://doi.org/10.1613/jair.1.16997) | Imaging, storage, downlink | Public requests, local capabilities | GND and NSS | 200/108 satellites over 24 h | Cost and satisfaction tradeoffs depend on request load |
| Joint observation/transmission [42](https://doi.org/10.1109/TMC.2021.3076088) | Imaging and contact windows | Joint mission data | Integer program and hybrid search | Agile-network simulation | Downlink opportunities constrain imaging |
| Joint charging model [43](https://doi.org/10.1016/j.actaastro.2025.02.008) | Imaging, contacts and charging | Multisatellite resources | Knapsack and ant-colony/local search | Agile constellation simulation | Energy replenishment changes feasibility |
| Staged acquisition/processing [53](https://doi.org/10.1002/sat.70082) | Quality, CPU, energy | Onboard and terrestrial processors | Acquisition followed by processor allocation/frequency | Ship detection/platform tests | Author-version-dependent model; information product focus |
| Communications-aware bundles [38](https://doi.org/10.1016/j.asr.2020.02.018) | Emergency tasks/communication | Predicted contact windows | Synchronous/asynchronous negotiation | Distributed simulation | Benefit/message balance varies with cost |
| Learning-assisted LNS [63](https://doi.org/10.1016/j.eswa.2025.128502) | Online emergency tasks | Rolling horizon data | Policy initial solution then repair | Dynamic scheduling tests | Both learning and search affect final solution |
| Reused single-agent policy [65](https://doi.org/10.2514/1.A35736) | Imaging/downlink | Completed tasks under four link modes | Single-agent training, multisatellite deployment | Walker constellation simulation | Training simplified; simultaneous redundancy possible |
| RL comparison [66](https://doi.org/10.3389/frspt.2023.1263489) | Single-satellite actions | No multisatellite coordination | PPO/A2C/DQN/MCTS-Train etc. | Basilisk | Reward and simulation/training cost vary |
| Refuellable multi-orbit servicing [67](https://doi.org/10.1016/j.cie.2022.108852) | Visits, propellant, refueling | Time-varying service network | Mixed-integer program | Servicing instances | Route/refueling dependence |
| Robust GEO refueling [68](https://doi.org/10.1016/j.cja.2025.103774) | Visits and uncertain duration | Budget uncertainty set | Robust search | GEO simulations | Risk conservatism depends on time model |
| Low-thrust servicing [71](https://doi.org/10.1007/s40295-026-00580-4) | Sequence, mass and refueling | Epoch/mass transfer costs | Grid, interpolation and GA | LEO multi-client simulation | Additional phasing cost outside core optimization |

The table preserves the domain of each experiment. Satellite count, simulated agent time and formal bounds are not directly comparable measures of method superiority.

---

## 3.3. Communication-Constellation Network Management and Resource Scheduling

LEO communication services face simultaneous variation in traffic demand and network topology. Satellite motion changes which users can be served, where gateways are accessible, and which end-to-end routes exist. Beam count, spectrum, transmit power, gateway capacity, and inter-satellite links impose competing limitations. The relevant scheduling tasks include traffic estimation, beam and power assignment, satellite handover, routing, traffic engineering, and hierarchical control. These operations differ from scheduling the downlink of already-acquired Earth-observation data.

### Demand Prediction and Beam, Power, and Spectrum Assignment

Uneven user demand challenges fixed beam illumination and equal resource allocation. Beam hopping serves several coverage regions over successive slots, while power, frequency, and satellite–cell associations constrain the resulting rates and interference. Han et al. [73](https://doi.org/10.3390/aerospace11030191) combine empirical mode decomposition, autoregressive integrated moving averages, and an optimized neural predictor for self-similar traffic generated in ON/OFF simulations. Their reported results primarily concern prediction accuracy on synthetic traffic. The paper presents routing applications as future work; an improved service rate has not been demonstrated by that prediction experiment.

The author version of beam-hopping resource optimization [74](https://doi.org/10.23919/JCC.ja.2022-0864) examines one satellite with eight beams and 61 beam positions. A potential-game formulation selects illuminated positions under average power assumptions, after which a penalty-based interior-point method optimizes continuous transmit power. The supply–demand squared deviation is evaluated against greedy beam-hopping baselines with equal or optimized power. Better allocation within the study's model does not establish a globally optimal joint integer–continuous solution; the printed pagination of the formal version also remains to be verified.

For overlapping multisatellite coverage, satellite–cell association and beam illumination must be coordinated with cochannel interference. Lin et al. [75](https://doi.org/10.1109/LCOMM.2022.3213912) divide the problem into cell association and multisatellite illumination while considering load balance and coexistence interference affecting GSO ground stations. This two-part design is supported by the published abstract; the full member-to-member interference equations and detailed ablations were not verified from the published body. A demand-aware study [76](https://doi.org/10.1109/TWC.2025.3545745) uses a digital-twin-assisted and multi-agent configuration in an author-manuscript scenario with 12 satellites, four beams each, and 168 cells.

The latter paper compares a demand-aware beam selection with uniform power (FPA) against a digitally coordinated selection and power scheme (DPA). Their throughput is similar within the stated 8–20 Gbit/s aggregate-demand range; at higher reported load, DPA performs better in the author-version experiments. Because the strategies differ in decision organization as well as power, this result is not a controlled ablation of only the power optimizer. More generally, the benefit of coupling beam selection, association and power depends on the location of the capacity bottleneck, interference and available computation and network state.

### User Access, Handover, and Continuity

Fast LEO orbital motion forces terminals to change serving satellite or beam. An elevation-angle or signal-strength rule assesses instantaneous link conditions but may ignore downstream routing delay, congestion or the cost of repeatedly switching. Conversely, preserving an attachment can reduce handovers at the expense of temporary path or radio-link efficiency. Thus, handover is a decision about both a serving node and the duration of the commitment.

Yin et al. [77](https://doi.org/10.1016/j.cja.2024.09.039) use analytical estimates of end-to-end propagation delay in their single-layer decision objective and apply Dueling Double DQN to obtain a policy. Cross-layer handover considers jitter prediction and switching cost. The currently accessible formal abstract supports the overall mechanism, not an independent causal attribution to one module; detailed state, action and reward formulations and any separate ablations require full-text confirmation.

Independent measurement offers a different type of evidence. Mohan et al. [78](https://doi.org/10.1145/3589334.3645328) report worldwide and controlled Starlink performance measurements, including throughput and delay variations around approximately 15-second network reconfiguration boundaries. In a UK terminal setting with deliberately restricted sky visibility, fluctuations were observed during windows with a single candidate serving satellite. This establishes that a serving-satellite handover is not a necessary explanation for all such variations. The authors propose an interpretation involving periodic network scheduling, but their experiments do not directly reveal the operator's proprietary scheduling rules.

### Time-Varying Topology, Routing, and Congestion Recovery

A communication route can change because of predictable orbital motion, gateway availability, congestion or a fault. Routing models must distinguish networks using a ground-assisted relay structure without direct inter-satellite forwarding from systems with dynamically established laser inter-satellite links (ISLs). In both, frequent route replacement may increase control effort; retaining an unsuitable old path can reduce service quality.

Zhang and Yeung [79](https://doi.org/10.1016/j.comcom.2022.02.015) address the ground-assisted case with two levels of routing. Publisher and institutional abstracts distinguish per-flow, bounded-delay routing (DBR), with a larger forwarding-state burden, from a destination-based alternative (DAR) designed to reduce update activity without preserving the same bound. Complete route-update rules, exact bounds and numerical control overhead remain unverified because the formal body was not obtained.

In a comparable ground-assisted dynamic topology, Zhang et al. [80](https://doi.org/10.1016/j.dcan.2022.09.022) introduce DBTS/DBTS+ as traffic-splitting/traffic-engineering methods and LFA/LFA+ as alternatives for rapid fault recovery. Those methods concern allocation of flows across available links; available institutional text does not establish an optimization of physical satellite link-capacity hardware. Their detailed capacity constraints, failures, and evaluation denominators remain a full-text gap.

Bhattacharjee et al. [121](https://doi.org/10.1109/TAES.2024.3415571) instead study the cost of creating dynamic laser ISLs. Their public author manuscript uses 1,584 satellites and 600 one-second snapshots and compares instantaneous shortest paths, route persistence and activity-aware policies when new links require establishment time. Route persistence or activity-aware handling can reduce update penalties when these are substantial; under very low link-establishment costs, some persistence methods have slightly worse mean delay than shortest-path routing, although this should not be generalized to every activity-aware algorithm. Their centralized controller is assumed to precompute and distribute routes, and the simulated model does not fully account for queueing or the initial configuration delay. Model execution time is therefore not proof of an onboard online deadline.

Together, these studies distinguish route stability, traffic engineering, restoration and laser-link activity. They should not be ranked by average propagation delay alone when their physical topology, queueing, traffic and reconfiguration assumptions differ.

### Cross-Domain Resource Allocation and Control Responsibilities

A centrally updated global state can support broad-spectrum planning but may impose excessive information and calculation costs. Locally operated beams, channels and routes can respond faster but need safeguards against interference and resource conflicts across administrative domains.

Gou et al. [81](https://doi.org/10.3390/s25030902) distinguish a network control center, space-based stations and user terminals. Global service-area and spectrum decisions bound local beam and channel selection, while demand and price exchange connect management levels. The formal archived paper separately evaluates spectral management, user scheduling, and beam scheduling components. Such results do not by themselves establish that an entire commercial constellation operates at the combined reported gain or achieves a particular coordination deadline.

SatOps–NetOps integration [9](https://doi.org/10.3390/technologies13080312) also involves information and responsibility separation. Its integrated, coordinated and adaptive categories are **three modes of interaction**; the source paper describes **four concrete architectural scenarios**. A simulated integrated prototype provides specific implementation evidence, not a head-to-head ranking of all three interaction modes. Likewise, centralized laser-route computation [121](https://doi.org/10.1109/TAES.2024.3415571) presupposes that controller-computed paths reach the forwarding nodes in time. Allocating management responsibility thus also allocates information dependencies and update authority.

**Table 5. Coordination objects, assumptions and principal tradeoffs in communications research**

| Study | Object | Model/information assumptions | Main relationship or limitation |
| --- | --- | --- | --- |
| Traffic forecasting [73](https://doi.org/10.3390/aerospace11030191) | Future traffic load | Synthetic self-similar ON/OFF demand | Prediction only; downstream routing/service benefit unverified |
| Single-satellite beam/power [74](https://doi.org/10.23919/JCC.ja.2022-0864) | Discrete illumination and continuous power | Author version: 8 beams, 61 cells | Power changes supply–demand matching; formal page conflict open |
| Multisatellite/GSO coexistence [75](https://doi.org/10.1109/LCOMM.2022.3213912) | Satellite–cell association and beam patterns | Abstract: multisatellite overlap and cochannel coexistence | Staged method; complete interference constraints unverified |
| Demand-aware resources [76](https://doi.org/10.1109/TWC.2025.3545745) | Multisatellite beams, power and queues | Author version: 12 satellites, 168 cells | Overall policy comparison depends on load, not a power-only ablation |
| Routing-aware handover [77](https://doi.org/10.1016/j.cja.2024.09.039) | Serving satellite and handover | Path delay, jitter and switching cost | Integrated policy; detailed ablation pending |
| Independent network study [78](https://doi.org/10.1145/3589334.3645328) | User-observed delay and throughput | Controlled and wider Starlink measurements | Boundary variation even with one serving candidate; internal rule unknown |
| Ground-assisted routing [79](https://doi.org/10.1016/j.comcom.2022.02.015), [80](https://doi.org/10.1016/j.dcan.2022.09.022) | Stable routes, flow splitting, recovery | No direct ISL; changing ground-assisted connections | Distinguish update design, traffic engineering and fault rerouting |
| Dynamic laser-link routing [121](https://doi.org/10.1109/TAES.2024.3415571) | Route and laser-link states | Author model: 1,584 nodes, establishment delay, no queues | Path persistence benefit depends on setup cost and policy |
| Hierarchical resources [81](https://doi.org/10.3390/s25030902) | Global spectrum and local resource control | Prices, demand, capacity and responsibilities | Performance is component- and workload-specific |

The evidence and numerical conditions refer to the accessible versions identified in the audit, not a common multisystem benchmark.

---

## 3.4. Safe Execution, Fault Recovery, and Service Resilience

A planned activity must still satisfy the dynamics, spacecraft health, and external-risk conditions encountered during execution. Conjunction screening identifies events requiring further attention, trajectory planning and control generate physically feasible actions, and fault management or plan repair updates what can be performed next. These activities support both observation and communication services, although they evaluate different kinds of safety and completion.

### Conjunction Detection and Risk Information

Computational cost arises both from identifying potentially relevant object pairs and from accurately finding the closest approach within each candidate pair. Chebyshev proxy polynomials [82](https://doi.org/10.1016/j.actaastro.2020.01.020) approximate distance over time intervals and locate stationary points, reducing dependence on dense pointwise search under specified approximation conditions. Saingyen et al. [84](https://doi.org/10.3390/aerospace10060543) compare Smart Sieve, CSieve and CAOS-D candidate filters and use CUDA to accelerate catalog screening. In the tested cases, GPU methods reduce processing time while some filtering strategies miss events. A screening-speed gain must therefore be interpreted together with event retention, missed cases and downstream accurate propagation.

Tracking-resource allocation can itself affect risk information. Risk-aware sensor scheduling [83](https://doi.org/10.1016/j.asr.2021.04.042) relates observational information and collision risk to tracking decisions. Learning-based risk estimation appears in the collision-avoidance competition [87](https://doi.org/10.1007/s42064-021-0101-5), while the CAMmary survey [86](https://doi.org/10.1016/j.actaastro.2025.07.027) classifies avoidance maneuver design and constellation-operation simulations [85](https://doi.org/10.1007/s12567-022-00471-y) analyze operational roles and maneuver timing. Event identification, final risk probability, and maneuver choice are related but distinct outputs.

The CCSDS Conjunction Data Message (CDM) standard [88](https://ccsds.org/publications/bluebooks/entry/3064/) specifies an exchange format for conjunction information. Starlink's published collision-avoidance concept of operations [89](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/) describes orbit-state generation, continuous conjunction checks, onboard risk reassessment, and possible addition, modification or cancellation of maneuvers. It is an operator account of a functioning process; without underlying model details it cannot be presented as proof of a universal guarantee that no conjunction is missed.

### Trajectory Constraints, Feedback Control, and Safe Operations

Safe rendezvous design expresses collision clearance, field-of-view or line-of-sight restrictions, terminal states, and actuator limits as trajectory constraints. Passively safe paths [90](https://doi.org/10.2514/1.29590) emphasize properties maintained after particular failures; conic optimization [91](https://doi.org/10.2514/1.58436) offers a structured trajectory solver; sequential convex-programming model-predictive control for spacecraft swarms [92](https://doi.org/10.2514/1.G000218) updates trajectories using neighbor-state information. These approaches differ in their safety properties, computational structure, and use of feedback.

Chance-constrained control addresses explicitly modelled uncertainty. Gavilan et al. [93](https://doi.org/10.1016/j.conengprac.2011.09.006) use Hill–Clohessy–Wiltshire relative dynamics, line-of-sight constraints, Gaussian disturbances and algebraic chance constraints, evaluated against nominal feedback through Monte Carlo simulation. Chance-constrained visual servoing [94](https://doi.org/10.1016/j.ast.2025.111237) adds coupled attitude–orbit and image feedback, disturbance estimation and constraint tightening for a noncooperative target. The respective guarantees or empirical success rates apply to the chosen dynamics, measurement, and disturbance representations. Continuous-time successive convexification for a near-rectilinear halo orbit [95](https://doi.org/10.2514/6.2026-2446) addresses yet another domain of passive safety, not a directly transferable guarantee for LEO constellations.

Stephenson and Schaub [96](https://doi.org/10.1007/s40295-026-00631-w) compare shielded reinforcement learning against probabilistic roadmaps and mixed-integer quadratically constrained planning in spacecraft inspection. Their simulation compares closed-loop online response with an offline open-loop trajectory and associated differences in fuel, time, and computational expenditure. An algorithm's online speed and the mission performance of its resulting trajectories must be interpreted together with the constraints enforced by shielding or optimization.

ADRAS-J provides a concrete off-nominal flight event [97](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris). After approaching a noncooperative upper stage to about 15 m in November 2024, a relative-attitude anomaly triggered an autonomous retreat. The announced inspection objectives and additional approach objectives do not have identical completion statuses. Such an event illustrates the need to distinguish safety-preserving withdrawal, activities not executed, and objectives already achieved; it does not establish that a debris capture occurred.

### Anomaly Detection, Isolation, and Plan Repair

Telemetry-anomaly algorithms often identify departures from expected behaviour without determining the root cause or implementing a recovery action. Hundman et al. [98](https://doi.org/10.1145/3219819.3219845) use LSTM prediction errors and dynamic thresholds for SMAP/MSL anomaly datasets. Bayesian LSTM work [99](https://doi.org/10.1016/j.actaastro.2020.12.012) addresses imbalance and prediction uncertainty; validation-gated continual learning [100](https://doi.org/10.1016/j.actaastro.2026.07.065) concerns model updates. Re-evaluation of detector benchmarks [101](https://doi.org/10.1007/s12567-023-00529-5) shows how postprocessing and evaluation rules alter comparisons. Detector precision or recall is consequently different from fault-isolation accuracy and recovered service.

Knowledge-based FDIR [102](https://doi.org/10.1007/s12567-025-00651-6) maps telemetry facts and rules to diagnoses and actions. Its demonstration on a ground-based RaspTank rover using a Raspberry Pi establishes the operation of a particular rule system but is not a satellite-flight validation or a complete representative avionics performance benchmark.

Plan-management software introduces another layer. Gillette and George's Schedule Manager [103](https://doi.org/10.2514/1.I011208) processes time windows, priorities, conflict categories, and resource restrictions, and can activate predefined contingency plans after a failed task. Its core Flight System integration and board or functional tests are evidence of software behaviour. A reactive plan repair approach [104](https://doi.org/10.1016/j.actaastro.2020.05.011) instead diagnoses resources and repairs or reschedules activities after failures in a deep-space task setting. Both approaches revise operational activity choices, but the original task domains and available recovery actions differ.

**Table 6. Outputs and validation objects in safe execution and recovery research**

| Study | Direct output | Connected function | Validation and limitations |
| --- | --- | --- | --- |
| Conjunction filters and CUDA [84](https://doi.org/10.3390/aerospace10060543) | Candidate events for subsequent analysis | Catalog screening to precise evaluation | Event retention and computation measured on test catalogs |
| Chance-constrained MPC [93](https://doi.org/10.1016/j.conengprac.2011.09.006) | Feedback input and predicted trajectory | Relative state to safety constraints | Linear relative dynamics, assumed disturbance law, Monte Carlo |
| Shielded RL versus roadmap [96](https://doi.org/10.1007/s40295-026-00631-w) | Inspection control or path | Task geometry to safe actions | Shared simulated mission, offline/online and fuel/time distinctions |
| Knowledge-based FDIR [102](https://doi.org/10.1007/s12567-025-00651-6) | Fault classification and recovery action | State facts to rule-triggered responses | Ground demonstrator, not flight-certified FDIR |
| Schedule Manager [103](https://doi.org/10.2514/1.I011208) | Activity plan and contingency | Task failure to preplanned response | Software and board tests; predefined coverage |
| Reactive plan repair [104](https://doi.org/10.1016/j.actaastro.2020.05.011) | Updated or repaired schedule | Resource diagnosis to revised activities | Deep-space mission model; multisatellite transfer unverified |

## 3.5. Coupled Management Problems and Integrated Operations

The preceding sections concern decisions that may be linked without being solved in one monolithic optimizer. Reviews of automation tools [6](https://doi.org/10.1016/j.asr.2020.08.018) and trusted autonomous operations [105](https://doi.org/10.1016/j.paerosci.2023.100960) also examine different organizational and assurance responsibilities; their coverage complements, rather than proves, any specific integrated system. A servicing resource is available only at particular locations and epochs; observation choice can depend on data-delivery paths; network decisions can change after a maneuver or loss of a payload. This section considers three ways in which those dependencies are represented: common selection, staged transfer between models, and operational feedback.

### Task Allocation and Data-Delivery Paths

The contact-graph scheduling framework of Lowe et al. [106](https://doi.org/10.1016/j.adhoc.2023.103289) combines data acquisition and delivery-route choice in a delay-tolerant network. The published model searches one request at a time, deducts allocated contact capacity, and assumes unlimited storage and energy. Its reported delivery rates and average latency among successfully delivered requests must be read together: changing the set of completed requests also changes the latency sample. The framework demonstrates the value of considering downstream delivery when choosing a source satellite, not a proof of global optimality over all requests.

By contrast, the acquisition/processing work [53](https://doi.org/10.1002/sat.70082) supplies a previously determined acquisition plan to a downstream computation and transmission model. The two studies connect activities at different points in the decision sequence, with different degrees of joint selection. Neither arrangement is intrinsically better: evaluating the value of a broader joint model requires a shared task load, consistent definitions of success, and the cost of using more state information.

### Asset State and Business-Resource Reconfiguration

Orbital servicing and logistics methods [23](https://doi.org/10.2514/1.A36684), [27](https://doi.org/10.2514/1.A34978), [28](https://doi.org/10.2514/1.A35094) affect what assets or services are ready at a particular time. Communication-platform sizing [17](https://doi.org/10.1016/j.comnet.2024.110942) similarly bounds network capacity before dynamic user allocation. Their shared outcome is a time- and location-dependent capability, but their optimization objectives, approximations and units remain different.

Singla et al. [9](https://doi.org/10.3390/technologies13080312) explicitly examine interaction between satellite operations and network operations. They distinguish integrated, coordinated, and adaptive **interaction modes**, and provide four concrete architectural scenarios. Their scheduler combines construction and local improvement, with plan revision triggered by telemetry and failed tasks. The integrated prototype is evaluated in a 16-satellite simulation against a particular semi-manual best-effort baseline. That evidence supports the tested implementation rather than a common performance ranking of all three modes.

Hierarchical resource management [81](https://doi.org/10.3390/s25030902) allocates service regions, spectrum and local scheduling responsibilities. Starlink's published avoidance process [89](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/) shows how risk states affect maneuvers. The link between changed orbits, locally degraded capacity and business rescheduling is therefore a meaningful integration question, but neither source alone establishes a complete unified network-and-maneuver optimizer.

### Feedback, Plan Modification, and Coordinated Execution

The reasoning-based agile observation scheduler [107](https://doi.org/10.3390/rs15061577) uses predicted or computed multi-subsystem states to select scheduling strategies through rules in a **single-spacecraft simulated environment**. Available publisher text does not establish a neural state predictor or an in-orbit multisatellite trial. Earlier Remote Agent [108](https://doi.org/10.1016/S0004-3702%2898%2900068-X), EO-1 [109](https://doi.org/10.1109/SMC-IT.2006.48), and IPEX [110](https://doi.org/10.2514/1.I010386), [111](https://ai.jpl.nasa.gov/public/projects/ipex/) provide different software or mission evidence for autonomous planning and resource feedback.

A reference architecture for autonomy and adaptivity [112](https://doi.org/10.1016/j.jss.2026.112802) organizes monitoring, analysis, planning, execution and shared knowledge under MAPE-K and presents industrial expert appraisal and NIMBUS instantiation. Publicly readable publisher metadata and abstract support the architecture and case instantiation, not flight validation or a measured constellation-wide scheduling benefit. The Schedule Manager [103](https://doi.org/10.2514/1.I011208) and NASA core Flight System [113](https://github.com/nasa/cFS) illustrate further software implementation aspects without removing the need for mission-specific validation.

NASA Starling [114](https://www.nasa.gov/smallspacecraft/what-is-starling/) reports coordinated observation among four CubeSats. The Starling 1.5 demonstration [115](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/) also involved exchanging trajectory/risk information and executing an actual autonomous maneuver in a **simulated conjunction scenario**. Coordinated observation, inter-operator responsibility assignment, and actual orbit control are distinct functions demonstrated under different event conditions; together they motivate but do not constitute full verification of an integrated commercial megaconstellation.

**Table 7. Forms of linkage and the scope of implementation evidence**

| Linking mechanism | Study or resource | Exchanged or dependent state | Observed model or validation scope |
| --- | --- | --- | --- |
| Joint selection | Contact-graph scheduling [106](https://doi.org/10.1016/j.adhoc.2023.103289) | Acquisition choice, delivery paths, contact capacities | Per-request joint search and discrete-event simulation |
| Staged downstream arrangement | Observation/processing [53](https://doi.org/10.1002/sat.70082) | Acquisition load, processors, downlink epochs | Author manuscript: upstream acquisition, downstream allocation/frequency |
| Integrated/architectural SatOps–NetOps | Singla et al. [9](https://doi.org/10.3390/technologies13080312) | Satellite tasks/resources, business demand and plan state | Three modes, four configurations; one integrated prototype tested |
| State-driven policy choice | Reasoning-based scheduler [107](https://doi.org/10.3390/rs15061577) | Predicted single-spacecraft observation/downlink/power states | Simulated rule-based selection, not multisatellite flight |
| Feedback in operations | IPEX [111](https://ai.jpl.nasa.gov/public/projects/ipex/), Starling [114](https://www.nasa.gov/smallspacecraft/what-is-starling/), [115](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/) | Resources, observations, conjunction and action responsibility | Single-spacecraft planning, four-spacecraft coordination, bounded maneuver trial |
| Architecture and components | MAPE-K [112](https://doi.org/10.1016/j.jss.2026.112802), cFS [113](https://github.com/nasa/cFS) | Modules, knowledge and control interfaces | Expert evaluation, instantiation, demonstration framework; no generic constellation performance guarantee |

Basilisk [116](https://doi.org/10.2514/1.I010762) and formal-methods discussions [117](https://doi.org/10.1007/978-3-031-06773-0_1) provide modelling and validation tools relevant to further integration. However, broader management functions cannot simply be assembled by adding isolated success metrics across unrelated tasks and testbeds.

---

# 4. Synthesis of Technical Progress and Research Directions

## 4.1. Solution Mechanisms and Scalability

The computational challenge of a large constellation comes from the combination of candidate tasks or users, resource conflicts, time-varying states, and the information required to coordinate decisions. Different solutions reduce different work. Branch-and-price scheduling [33](https://doi.org/10.1016/j.cor.2025.107259) restructures the discrete task/energy model and can provide bounds relative to that model, whereas beam/power optimization [74](https://doi.org/10.23919/JCC.ja.2022-0864) separates illumination decisions from continuous power control. These decompositions concern different variables, constraints, and algorithms; their empirical times cannot be ranked without a shared experiment.

Local coordination and the reuse of previous plans offer distinct means of controlling update cost. In the experiment reported by Parjan and Chien [34](https://doi.org/10.2514/1.I011215), incremental continual planning is faster than replanning from scratch and can improve request satisfaction while increasing duplicate observations. In the decomposition study by Zilberstein et al. [35](https://doi.org/10.1613/jair.1.16997), smaller request instances show an improvement in both satisfaction and computation/messages relative to the selected broadcast baseline; larger workloads introduce a different tradeoff. Thus, faster local or incremental computation does not imply a fixed direction of change in solution quality.

There is a related but distinct role for preserving network routes. Ground-assisted routing [79](https://doi.org/10.1016/j.comcom.2022.02.015) is designed to avoid unnecessary route changes, although the magnitude of control savings remains a full-text evidence gap here. In laser-link routing [121](https://doi.org/10.1109/TAES.2024.3415571), keeping paths is useful under non-negligible setup delays but some persistence policies lose a small mean-delay advantage when setup is cheap. The result depends on link setup, policy choice, route life and queue assumptions.

**Table 8. Mechanisms of computational and coordination scaling**

| Mechanism | Part of the problem affected | Expected direct role | Limitation or tradeoff |
| --- | --- | --- | --- |
| Mathematical programming and structured decomposition | Variable/constraint organization, master and subproblem | Exploit combinatorial structure; some models supply bounds | Pricing cost and original-model validity remain relevant |
| Hierarchical planning and repair | Allocation, order and plan revisions | Reduce scope of the next update and reuse work | Existing commitments and missed/duplicate tasks |
| Distributed coordination | Information scope, conflict resolution, decision authority | Reduce some centralized processing and support local response | Message delay, stale state, congestion and conflict density |
| Forecasting and learning-assisted search | Estimated demand, initial solution, search operator | Anticipate demand or accelerate particular search stages | Forecast error, training costs, downstream optimization |
| Learned policies with safety checks | Action proposal and constraint validation | Reuse offline training for rapid proposals | Domain shift, screening, failed checks and fallback |
| Multi-resource and cross-stage optimization | Tasks, routes, service capacities, feedback states | Expose downstream bottlenecks when choosing current actions | Increased model complexity, data needs and coordination cost |

No row establishes a universally fastest algorithm. A meaningful evaluation accounts separately for preprocessing, training, search, communications, plan confirmation and execution-related latency, with the workload and solution requirements stated. Complexity can increase even at the same satellite count if requests, windows, precedence or communication conflicts become denser.

## 4.2. Resource Dependencies from Local Activities to Service Outcomes

Resource coupling matters because the feasibility of a current choice can depend on downstream processes. Imaging/downlink optimization [42](https://doi.org/10.1109/TMC.2021.3076088) selects acquisitions with transfer opportunities in view; charging-aware schedules [43](https://doi.org/10.1016/j.actaastro.2025.02.008) track future energy state. Staged acquisition and processing [53](https://doi.org/10.1002/sat.70082) uses an upstream acquisition plan as a downstream input, whereas contact-graph scheduling [106](https://doi.org/10.1016/j.adhoc.2023.103289) jointly chooses an acquisition spacecraft and the delivery path one request at a time. Joint selection, staged decisions and operational feedback are different mathematical arrangements, each of which should be evaluated against the service event actually rewarded.

In communication services, single-satellite beam/power assignment [74](https://doi.org/10.23919/JCC.ja.2022-0864) addresses illumination and continuous resource allocation. Multisatellite/GSO coexistence [75](https://doi.org/10.1109/LCOMM.2022.3213912) adds association and cochannel interference, subject to presently unverified full-equation details. Demand-aware digital-twin policies [76](https://doi.org/10.1109/TWC.2025.3545745) are affected by the demand level, but the author-version FPA/DPA comparison changes the overall policy and is not a strict power-only ablation. Routing-aware handover [77](https://doi.org/10.1016/j.cja.2024.09.039) introduces downstream path cost, while segment-routing traffic engineering and failure recovery [80](https://doi.org/10.1016/j.dcan.2022.09.022) operate over available links and do not establish optimizable physical link-capacity hardware. Dynamic laser ISLs [121](https://doi.org/10.1109/TAES.2024.3415571) introduce route-activation delay. The common point is not a single unified optimum but the effect of different bottlenecks on local choices.

Service value must be defined before comparing models. Observation requests may be considered complete after imaging, acceptable inference or confirmed product delivery. A communication service is often better described by sustained throughput, delay, reliability or fairness during a workload. In contact-graph results, the average delay among delivered requests also changes when the set of successful requests changes. Likewise, throughput differences between beam policies can depend on load. Denominators, success conditions, and computational expense belong together in a comparison.

Maintenance and safety affect the available resource set. Spare inventories [18](https://doi.org/10.2514/1.A34387), servicing-inclusive maintenance [23](https://doi.org/10.2514/1.A36684), maneuvering, and partial payload faults can change when a satellite or link is usable. Asset possession, mission-ready capability, and actual restoration of user-facing service are related but distinct stages. A useful cross-function model needs to specify the time and resource transitions that matter to its operational objective.

## 4.3. Information Conditions for Distributed and Learned Methods

Effective coordination depends on what information agents exchange, its freshness, and the action that the information authorizes. In the policy-reuse study [65](https://doi.org/10.2514/1.A35736), participants exchange statuses of targets already acquired or downlinked. Even under unrestricted communications, this does not necessarily preclude simultaneous future selection of one target, because future intent is not part of the shared information. Connectivity gives a channel for messages, not automatically a conflict-free plan.

Communication-aware bundle allocation [38](https://doi.org/10.1016/j.asr.2020.02.018) makes the timing of opportunities part of task coordination. General asynchronous bundle experiments [118](https://doi.org/10.1109/SAM.2018.8448984) provide a reference for lossy message environments but do not reproduce every physical ISL condition. Hierarchical resource control [81](https://doi.org/10.3390/s25030902) exchanges demand and configuration/price information; centralized laser routing [121](https://doi.org/10.1109/TAES.2024.3415571) assumes path calculations reach participating nodes before execution. These mechanisms assign different meanings to state, proposed actions, confirmed resources and actually completed activities.

Learning also performs multiple roles. Traffic prediction [73](https://doi.org/10.3390/aerospace11030191) supplies estimates rather than routing gains; learning-assisted search [63](https://doi.org/10.1016/j.eswa.2025.128502) generates candidates that subsequent combinatorial optimization improves; the policy-reuse model [65](https://doi.org/10.2514/1.A35736) generates direct per-satellite choices; shielded policies [96](https://doi.org/10.1007/s40295-026-00631-w) use safety constraints to limit admissible physical actions. A gain in the first stage may not be fully transmitted to the final service objective because of conflicts, failed checks or communication delays. Fair comparisons must include training, downstream repair, coordination and appropriate fallback.

## 4.4. What Public Operational and Flight Evidence Actually Validates

Operational data expose distinctions not always explicit in mathematical objectives. Planet's Tasking API [51](https://docs.planet.com/develop/apis/tasking/) defines acquisition, quality and product states; the AWS scheduling API [52](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html) defines contact commitments and permissible changes, including the qualified version-update pathway. They are evidence of publicly defined service interfaces, not of the operator's hidden scheduling optimizer. Different implementation and mission records are summarized in Table 9.

**Table 9. Public operating documents and missions: supported functions and boundaries**

| Resource or case | Reported state or action | What it can and cannot establish |
| --- | --- | --- |
| Iridium spare deployment [22](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites) | Spare assets placed on orbit | Physical redundancy; restoration time requires further events |
| Planet Tasking API [51](https://docs.planet.com/develop/apis/tasking/) | Acquisition, quality review and delivery | Observable business-state definitions; internal algorithms unknown |
| AWS Ground Station [52](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html) and [versioning](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.versioning.html) | Contact reservations, configuration snapshots, qualified updates | Commitment and modification rules, not universal editing freedom |
| Starlink collision avoidance [89](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/) | Screening, onboard risk reassessment, maneuver revision | Disclosed workflow, not independent proof of zero misses |
| ADRAS-J [97](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris) | Approach and autonomous retreat | Safe withdrawal, not a completed capture |
| IPEX [111](https://ai.jpl.nasa.gov/public/projects/ipex/) | Single-spacecraft processing and replanning | Resource-feedback flight functions, not constellation-wide scheduling |
| Starling and Starling 1.5 [114](https://www.nasa.gov/smallspacecraft/what-is-starling/), [115](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/) | Four-spacecraft observation coordination and maneuver during a simulated conjunction | Distinct bounded demonstrations, not an integrated megaconstellation verification |
| CCSDS CDM [88](https://ccsds.org/publications/bluebooks/entry/3064/) and NASA cFS [113](https://github.com/nasa/cFS) | Information format and software integration framework | Interface and component foundation; mission-specific validation still required |
| Independent Starlink measurements [78](https://doi.org/10.1145/3589334.3645328) | User-side variations even with one candidate serving satellite | Empirical behaviour; not a direct observation of internal scheduling logic |

IPEX [111](https://ai.jpl.nasa.gov/public/projects/ipex/), Starling [114](https://www.nasa.gov/smallspacecraft/what-is-starling/) and Starling 1.5 [115](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/) exemplify increasingly varied forms of operational coordination, but not one experiment in which every function was integrated. Starlink's avoidance procedure [89](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/) and ADRAS-J [97](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris) show how risk or anomalous attitude can change a physical operation. The evidence is informative only when the specific mission objective and action achieved are kept distinct.

Software studies address still different questions. Supervised operating-system scheduler reconfiguration [119](https://doi.org/10.1007/s10270-026-01426-1) concerns onboard software process timing, not allocation of Earth-observation requests among many spacecraft. Model checking [120](https://doi.org/10.1007/s10270-025-01281-6) evaluates specifications and computational scaling under specified abstractions. Mathematical modelling, board tests, business interfaces, independent measurements and flight tests thus establish complementary rather than interchangeable results.

## 4.5. Research Challenges and Future Directions

**Linking capability restoration and business loss.** Multi-echelon spares [18](https://doi.org/10.2514/1.A34387), dual-supply strategies [19](https://doi.org/10.2514/1.A36281), and servicing-based maintenance [23](https://doi.org/10.2514/1.A36684) provide different mechanisms of capability recovery. A comparison on common failure and demand sequences could distinguish inventory satisfaction from time-to-readiness and the actual loss of observation delivery or communication service. Such an experiment would test when omitted transfer and commissioning stages materially change planning decisions.

**Choosing an appropriate degree of end-to-end coupling.** Contact-graph methods [106](https://doi.org/10.1016/j.adhoc.2023.103289) can select acquisition and delivery paths together, whereas staged processing [53](https://doi.org/10.1002/sat.70082) takes an upstream plan as fixed input. Demand-aware beams [76](https://doi.org/10.1109/TWC.2025.3545745), handover with routing cost [77](https://doi.org/10.1016/j.cja.2024.09.039), and laser route establishment [121](https://doi.org/10.1109/TAES.2024.3415571) reveal further downstream dependencies. The question is not whether all decisions should always be jointly optimized, but when a more extensive model yields measurable service benefits relative to staged or feedback-based choices at acceptable computation and communication cost.

**Planning with delayed information and confirmed commitments.** Incremental planning [34](https://doi.org/10.2514/1.I011215), communication-aware bundles [38](https://doi.org/10.1016/j.asr.2020.02.018), hierarchical resource control [81](https://doi.org/10.3390/s25030902), and dynamic ISL routing [121](https://doi.org/10.1109/TAES.2024.3415571) all depend on what state is shared and when revisions become effective. Common scenarios can compare retaining local commitments, cancelling and reallocating them, and the effects on completion, latency and temporary disruption.

**Testing the downstream value of learning.** Prediction [73](https://doi.org/10.3390/aerospace11030191), learning-assisted search [63](https://doi.org/10.1016/j.eswa.2025.128502), and shielded control [96](https://doi.org/10.1007/s40295-026-00631-w) act at different stages. Fixed downstream optimizers and consistent workload budgets would clarify how changes in predictor error, candidate quality or policy execution affect operational metrics after resource allocation, safety checks and fallback.

**Integrated validation on common event scenarios.** IPEX [111](https://ai.jpl.nasa.gov/public/projects/ipex/), Starling [114](https://www.nasa.gov/smallspacecraft/what-is-starling/), and the Starling 1.5 experiment [115](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/) each demonstrate bounded links between state, plans, participants and actions. Joint tests involving task competition, network-state changes, partial asset failures and safety maneuvers could establish which combinations preserve feasible plans and delivered service. This is a proposal for specific research and evidence, not a claim that no prior integrated studies exist.

# 5. Conclusions

Intelligent management and scheduling of large satellite constellations encompass both service-specific decision problems and cross-service operational functions. Using service domain and management function as complementary organizing dimensions, this review has examined Earth-observation task scheduling, communication-network resource management, capability planning, replenishment and on-orbit servicing, safe execution, recovery and integrated operations. Observation systems connect acquisition, processing and delivery; communication systems continuously allocate access, beam and power resources, routes and capacity. Although both encounter dynamic resource conflict, their input loads, success conditions and state variables should remain distinct in a technical comparison.

Research has developed mathematical planning and decomposition, heuristics, distributed coordination, traffic prediction, learning-assisted search and autonomous control. Incremental planning and geometric neighborhood decomposition reduce different forms of repeated computation or messaging and exhibit workload- and baseline-dependent relationships with task satisfaction and duplication. Resource coupling between acquisition and delivery can arise through joint decisions, staged downstream optimization or feedback updates. Their effects are contingent on precisely which resources and future service events are included.

Communications studies demonstrate different limits of coordination scale and control frequency. Beam and power policies produce workload-dependent performance; service association and GSO coexistence introduce interference constraints; route persistence must balance path quality against reconfiguration and laser-link setup. Independent network measurements further distinguish uninterrupted attachment to a satellite from a guarantee of constant end-user service quality. These findings support conditional technical comparisons rather than a cross-domain performance ranking.

Algorithm simulation, software demonstrations, published business interfaces, independent operational measurements, and spaceflight trials provide different evidence. They document model mechanisms, software behaviour, service state rules or specific physical actions, respectively. Linking asset readiness to restored service, matching the scope of coupled optimizations to downstream bottlenecks, and updating decisions under delayed information are consequently important subjects for further research. Reproducible scenarios incorporating shared service requests, network changes, failures and safety events can help establish when local improvements jointly support sustained constellation operation.

# References

1. Mohamed Khalil Ben-Larbi; Kattia Flores Pozo; Tom Haylok, et al. Towards the automated operations of large distributed satellite systems. Part 1: Review and paradigm shifts. *Advances in Space Research, 2021, 67(11): 3598-3619*. DOI: [10.1016/j.asr.2020.08.009](https://doi.org/10.1016/j.asr.2020.08.009).

2. Koki Ho. Space Logistics Modeling and Optimization: Review of the State of the Art. *Journal of Spacecraft and Rockets, 2024, 61(5): 1417-1427*. DOI: [10.2514/1.A35982](https://doi.org/10.2514/1.A35982).

3. Xinwei Wang; Guohua Wu; Lining Xing, et al. Agile Earth Observation Satellite Scheduling Over 20 Years: Formulations, Methods, and Future Directions. *IEEE Systems Journal, 2021, 15(3): 3881-3892*. DOI: [10.1109/JSYST.2020.2997050](https://doi.org/10.1109/JSYST.2020.2997050).

4. Benedetta Ferrari; Jean-François Cordeau; Maxence Delorme, et al. Satellite Scheduling Problems: A survey of applications in Earth and outer space observation. *Computers & Operations Research, 2025, 173: 106875*. DOI: [10.1016/j.cor.2024.106875](https://doi.org/10.1016/j.cor.2024.106875).

5. Mohammad Reza Jabbarpour; Bao Quoc Vo; Ghaith El-Dalahmeh, et al. Agent-based approaches for distributed space systems and mission management: Methodologies, current practices and challenges. *Acta Astronautica, 2026, 238: 237-257*. DOI: [10.1016/j.actaastro.2025.10.018](https://doi.org/10.1016/j.actaastro.2025.10.018).

6. Mohamed Khalil Ben-Larbi; Kattia Flores Pozo; Mirue Choi, et al. Towards the automated operations of large distributed satellite systems. Part 2: Classifications and tools. *Advances in Space Research, 2021, 67(11): 3620-3637*. DOI: [10.1016/j.asr.2020.08.018](https://doi.org/10.1016/j.asr.2020.08.018).

7. Li-Zeng Gong; Wenlong Zhang; Quan Chen, et al. Survey of intelligent networking technologies for LEO mega-constellations. *Acta Aeronautica et Astronautica Sinica, 2026*(online 23 March 2026). DOI: [10.7527/S1000-6893.2026.32935](https://doi.org/10.7527/S1000-6893.2026.32935).

8. Hang Di; Tao Dong; Zhihui Liu, et al. Survey of network resource management and optimization for LEO communication satellite constellations. *Journal of Astronautics, 2026, 47(2): 270-283*. DOI: [10.3873/j.issn.1000-1328.2026.02.002](https://doi.org/10.3873/j.issn.1000-1328.2026.02.002).

9. Arnau Singla; Franco Criscola; David Canales, et al. Toward Integrated Satellite Operations and Network Management: A Review and Novel Framework. *Technologies, 2025, 13(8): 312*. DOI: [10.3390/technologies13080312](https://doi.org/10.3390/technologies13080312).

10. Yuhe Mao; Yunhua Wu; Xiaozhe Ju, et al. Dynamic Management Topology Construction, Evolution, and Maintenance of Low Earth Orbit Mega-Constellation. *Space: Science & Technology, 2025, 5: 0248*. DOI: [10.34133/space.0248](https://doi.org/10.34133/space.0248).

11. Leonid Appel; Moshe Guelman; David Mishne. Optimization of satellite constellation reconfiguration maneuvers. *Acta Astronautica, 2014, 99: 166-174*. DOI: [10.1016/j.actaastro.2014.02.016](https://doi.org/10.1016/j.actaastro.2014.02.016).

12. Hang Woon Lee; Koki Ho. Regional Constellation Reconfiguration Problem: Integer Linear Programming Formulation and Lagrangian Heuristic Method. *Journal of Spacecraft and Rockets, 2023, 60(6): 1828-1845*. DOI: [10.2514/1.A35685](https://doi.org/10.2514/1.A35685).

13. Hang Woon Lee; David O. Williams Rogers; Brycen D. Pearl, et al. Deterministic Multistage Constellation Reconfiguration Using Integer Programming and Sequential Decision-Making Methods. *Journal of Spacecraft and Rockets, 2025, 62(1): 206-222*. DOI: [10.2514/1.A35990](https://doi.org/10.2514/1.A35990).

14. Hang Woon Lee; Seiichi Shimizu; Shoji Yoshikawa, et al. Satellite Constellation Pattern Optimization for Complex Regional Coverage. *Journal of Spacecraft and Rockets, 2020, 57(6): 1309-1327*. DOI: [10.2514/1.A34657](https://doi.org/10.2514/1.A34657).

15. Hang Woon Lee; Pauline C. Jakob; Koki Ho, et al. Optimization of satellite constellation deployment strategy considering uncertain areas of interest. *Acta Astronautica, 2018, 153: 213-228*. DOI: [10.1016/j.actaastro.2018.03.054](https://doi.org/10.1016/j.actaastro.2018.03.054).

16. Beomjin Gwon; Jaemyung Ahn. Two-Stage Framework for Deployment-Aware Optimization of Satellite Constellation Pattern Design. *International Journal of Aeronautical and Space Sciences, 2026*. DOI: [10.1007/s42405-026-01298-1](https://doi.org/10.1007/s42405-026-01298-1).

17. Samuel Martínez Zamacola; Ramón Martínez Rodríguez-Osorio; Miguel A. Salas-Natera. Joint satellite platform and constellation sizing for instantaneous beam-hopping in 5G/6G Non-Terrestrial Networks. *Computer Networks, 2025, 257: 110942*. DOI: [10.1016/j.comnet.2024.110942](https://doi.org/10.1016/j.comnet.2024.110942).

18. Pauline Jakob; Seiichi Shimizu; Shoji Yoshikawa, et al. Optimal Satellite Constellation Spare Strategy Using Multi-Echelon Inventory Control. *Journal of Spacecraft and Rockets, 2019, 56(5): 1449-1461*. DOI: [10.2514/1.A34387](https://doi.org/10.2514/1.A34387).

19. Jaewoo Kim; Jaemyung Ahn; Taehyun Sung. Replenishment Strategy for Satellite Constellation with Dual Supply Modes. *Journal of Spacecraft and Rockets, 2025, 62(5): 1567-1583*. DOI: [10.2514/1.A36281](https://doi.org/10.2514/1.A36281).

20. Seungyeop Han; Zachary Grieser; Shoji Yoshikawa, et al. Spare Strategy Analysis and Design for Mega Satellite Constellations Using Markov Chain. *Journal of Spacecraft and Rockets, 2026: 1-12*. DOI: [10.2514/1.A36599](https://doi.org/10.2514/1.A36599).

21. Seungyeop Han; Shoji Yoshikawa; Takumi Noro, et al. Spare strategy for large-scale satellite constellations under dual resupply channels using Markov chain. *Acta Astronautica, 2026, 248: 614-629*(assigned to the November 2026 issue; online date pending source confirmation). DOI: [10.1016/j.actaastro.2026.06.020](https://doi.org/10.1016/j.actaastro.2026.06.020).

22. Iridium. Iridium Adds to Constellation Resilience with Launch of Spare Satellites. [official source](https://investor.iridium.com/2023-05-20-Iridium-Adds-to-Constellation-Resilience-with-Launch-of-Spare-Satellites). Accessed 10 October 2026.

23. Jaewoo Kim; Taehyun Sung; Woonam Hwang, et al. On-Orbit Servicing-Integrated Maintenance Strategy for a Satellite Constellation. *Journal of Spacecraft and Rockets, 2026: 1-18*. DOI: [10.2514/1.A36684](https://doi.org/10.2514/1.A36684).

24. Yuri Shimane; Nicholas Gollins; Koki Ho. Orbital Facility Location Problem for Satellite Constellation Servicing Depots. *Journal of Spacecraft and Rockets, 2024, 61(3): 808-825*. DOI: [10.2514/1.A35691](https://doi.org/10.2514/1.A35691).

25. Euihyeon Choi; Koki Ho. Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers. *Journal of Spacecraft and Rockets, 2026, 63(1): 4-13*. DOI: [10.2514/1.A36386](https://doi.org/10.2514/1.A36386).

26. Yaxiong Li; Xinglong Sun; Xinxue Liu, et al. Deployment of On-Orbit Service Vehicles Using a Fuzzy Adaptive Particle Swarm Optimization Algorithm. *Modelling and Simulation in Engineering, 2021, 2021: 1-15*. DOI: [10.1155/2021/6644339](https://doi.org/10.1155/2021/6644339).

27. Tristan Sarton du Jonchay; Hao Chen; Onalli Gunasekara, et al. Framework for Modeling and Optimization of On-Orbit Servicing Operations Under Demand Uncertainties. *Journal of Spacecraft and Rockets, 2021, 58(4): 1157-1173*. DOI: [10.2514/1.A34978](https://doi.org/10.2514/1.A34978).

28. Tristan Sarton du Jonchay; Hao Chen; Masafumi Isaji, et al. On-Orbit Servicing Optimization Framework with High- and Low-Thrust Propulsion Tradeoff. *Journal of Spacecraft and Rockets, 2022, 59(1): 33-48*. DOI: [10.2514/1.A35094](https://doi.org/10.2514/1.A35094).

29. Wen Yao; Xiaoqian Chen; Yiyong Huang, et al. On-orbit servicing system assessment and optimization methods based on lifecycle simulation under mixed aleatory and epistemic uncertainties. *Acta Astronautica, 2013, 87: 107-126*. DOI: [10.1016/j.actaastro.2013.02.005](https://doi.org/10.1016/j.actaastro.2013.02.005).

30. Michel Lemaı̂tre; Gérard Verfaillie; Frank Jouhaud, et al. Selecting and scheduling observations of agile satellites. *Aerospace Science and Technology, 2002, 6(5): 367-381*. DOI: [10.1016/S1270-9638(02)01173-2](https://doi.org/10.1016/S1270-9638%2802%2901173-2).

31. Yongming He; Lining Xing; Yingwu Chen, et al. A Generic Markov Decision Process Model and Reinforcement Learning Method for Scheduling Agile Earth Observation Satellites. *IEEE Transactions on Systems, Man, and Cybernetics: Systems, 2022, 52(3): 1463-1474*. DOI: [10.1109/TSMC.2020.3020732](https://doi.org/10.1109/TSMC.2020.3020732).

32. Jing Qi; Min Hu; Lining Xing. A decompose-and-learn multi-objective algorithm for scheduling large-scale earth observation satellites. *Swarm and Evolutionary Computation, 2025, 92: 101792*. DOI: [10.1016/j.swevo.2024.101792](https://doi.org/10.1016/j.swevo.2024.101792).

33. Pedro Marcolin Antunes; Laio Oriel Seman; Eduardo Camponogara. A branch-and-price algorithm for energy aware task scheduling of constellations of nanosatellites. *Computers & Operations Research, 2026, 185: 107259*. DOI: [10.1016/j.cor.2025.107259](https://doi.org/10.1016/j.cor.2025.107259).

34. Shreya Parjan; Steve A. Chien. Decentralized Observation Allocation for a Large-Scale Constellation. *Journal of Aerospace Information Systems, 2023, 20(8): 447-461*. DOI: [10.2514/1.I011215](https://doi.org/10.2514/1.I011215).

35. Itai Zilberstein; Ananya Rao; Matthew Salis, et al. Decentralized, Decomposition-Based Observation Scheduling for a Large-Scale Satellite Constellation. *Journal of Artificial Intelligence Research, 2025, 82: 169-208*. DOI: [10.1613/jair.1.16997](https://doi.org/10.1613/jair.1.16997).

36. Shai Krigman; Tal Grinshpoun; Lihi Dery. Scheduling of Earth observing satellites using distributed constraint optimization. *Journal of Scheduling, 2024, 27(5): 507-524*. DOI: [10.1007/s10951-024-00816-x](https://doi.org/10.1007/s10951-024-00816-x).

37. Han-Lim Choi; L. Brunet; J.P. How. Consensus-Based Decentralized Auctions for Robust Task Allocation. *IEEE Transactions on Robotics, 2009, 25(4): 912-926*. DOI: [10.1109/TRO.2009.2022423](https://doi.org/10.1109/TRO.2009.2022423).

38. Guoliang Li. Online scheduling of distributed Earth observation satellite system under rigid communication constraints. *Advances in Space Research, 2020, 65(11): 2475-2496*. DOI: [10.1016/j.asr.2020.02.018](https://doi.org/10.1016/j.asr.2020.02.018).

39. Chong Wang; Jinhui Tang; Xiaohang Cheng, et al. Distributed cooperative task planning algorithm for multiple satellites in delayed communication environment. *Journal of Systems Engineering and Electronics, 2016, 27(3): 619-633*. DOI: [10.1109/JSEE.2016.00066](https://doi.org/10.1109/JSEE.2016.00066).

40. Weiyi Yang; Lei He; Xiaolu Liu, et al. Onboard coordination and scheduling of multiple autonomous satellites in an uncertain environment. *Advances in Space Research, 2021, 68(11): 4505-4524*. DOI: [10.1016/j.asr.2021.09.003](https://doi.org/10.1016/j.asr.2021.09.003).

41. Ben Rachmut; Sofia Amador Nelke; Roie Zivan. Asynchronous Communication Aware Multi-Agent Task Allocation. *Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence, 2023: 262-270*. DOI: [10.24963/ijcai.2023/30](https://doi.org/10.24963/ijcai.2023/30).

42. Lijun He; Ben Liang; Jiandong Li, et al. Joint Observation and Transmission Scheduling in Agile Satellite Networks. *IEEE Transactions on Mobile Computing, 2022, 21(12): 4381-4396*. DOI: [10.1109/TMC.2021.3076088](https://doi.org/10.1109/TMC.2021.3076088).

43. Minghao Shang; Ronggang Yuan; Bin Song, et al. Joint observation and transmission scheduling of multiple agile satellites with energy constraint using improved ACO algorithm. *Acta Astronautica, 2025, 230: 92-103*. DOI: [10.1016/j.actaastro.2025.02.008](https://doi.org/10.1016/j.actaastro.2025.02.008).

44. Yure Rocha; Guilherme O. Chagas; Leandro C. Coelho, et al. The integrated agile Earth observation satellite scheduling problem. *Computers & Operations Research, 2025, 184: 107212*. DOI: [10.1016/j.cor.2025.107212](https://doi.org/10.1016/j.cor.2025.107212).

45. Sung Jun Kim; Minchae Kim; Han-Lim Choi. Tip-and-cue mission scheduling in heterogeneous satellite constellations using mixed-integer linear programming. *Acta Astronautica, 2026, 246: 921-940*. DOI: [10.1016/j.actaastro.2026.04.059](https://doi.org/10.1016/j.actaastro.2026.04.059).

46. Sara Spangelo; James Cutler; Kyle Gilson, et al. Optimization-based scheduling for the single-satellite, multi-ground station communication problem. *Computers & Operations Research, 2015, 57: 1-16*. DOI: [10.1016/j.cor.2014.11.004](https://doi.org/10.1016/j.cor.2014.11.004).

47. Laura Barbulescu; Jean-Paul Watson; L. Darrell Whitley, et al. Scheduling Space–Ground Communications for the Air Force Satellite Control Network. *Journal of Scheduling, 2004, 7(1): 7-34*. DOI: [10.1023/B:JOSH.0000013053.32600.3c](https://doi.org/10.1023/B:JOSH.0000013053.32600.3c).

48. Daniel Karapetyan; Snezana Mitrovic Minic; Krishna T. Malladi, et al. Satellite downlink scheduling problem: A case study. *Omega, 2015, 53: 115-123*. DOI: [10.1016/j.omega.2015.01.001](https://doi.org/10.1016/j.omega.2015.01.001).

49. Alex Sabol; Ryan Alimo; Farhad Kamangar, et al. Deep Space Network Scheduling via Mixed-Integer Linear Programming. *IEEE Access, 2021, 9: 39985-39994*. DOI: [10.1109/ACCESS.2021.3064928](https://doi.org/10.1109/ACCESS.2021.3064928).

50. Mark D. Johnston; Daniel Tran; Belinda Arroyo, et al. Automated Scheduling for NASA's Deep Space Network. *AI Magazine, 2014, 35(4): 7-25*. DOI: [10.1609/aimag.v35i4.2552](https://doi.org/10.1609/aimag.v35i4.2552).

51. Planet. Tasking API. [official source](https://docs.planet.com/develop/apis/tasking/). Accessed 10 October 2026。

52. Amazon Web Services. Work with contacts. [official source](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html). Accessed 10 October 2026。

53. Beatriz Soret; Antonio M. Mercado‐Martínez; Antonio Jurado‐Navas, et al. Edge Intelligence for Satellite‐Based Earth Observation: Scheduling Image Acquisition and Processing. *International Journal of Satellite Communications and Networking, 2026: sat.70082*. DOI: [10.1002/sat.70082](https://doi.org/10.1002/sat.70082).

54. Min Jia; Liang Zhang; Jian Wu, et al. Deep Multiagent Reinforcement Learning for Task Offloading and Resource Allocation in Satellite Edge Computing. *IEEE Internet of Things Journal, 2025, 12(4): 3832-3845*. DOI: [10.1109/JIOT.2024.3482290](https://doi.org/10.1109/JIOT.2024.3482290).

55. Hai Li; Jinyang Yu; Lili Cao, et al. Multi-agent reinforcement learning based computation offloading and resource allocation for LEO Satellite edge computing networks. *Computer Communications, 2024, 222: 268-276*. DOI: [10.1016/j.comcom.2024.05.008](https://doi.org/10.1016/j.comcom.2024.05.008).

56. Wenhao Fan; Qingcheng Meng; Guan Wang, et al. Satellite Edge Intelligence: DRL-Based Resource Management for Task Inference in LEO-Based Satellite-Ground Collaborative Networks. *IEEE Transactions on Mobile Computing, 2025, 24(10): 10710-10728*. DOI: [10.1109/TMC.2025.3570799](https://doi.org/10.1109/TMC.2025.3570799).

57. Danilo Magliarisi; Emiliano Casalicchio; Vincenzo Salvatore. Orbit-aware task scheduling in satellite edge computing. *Cluster Computing, 2025, 28(16): 1013*. DOI: [10.1007/s10586-025-05663-9](https://doi.org/10.1007/s10586-025-05663-9).

58. Bradley Denby; Krishna Chintalapudi; Ranveer Chandra, et al. Kodan: Addressing the Computational Bottleneck in Space. *Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 3, 2023: 392-403*. DOI: [10.1145/3582016.3582043](https://doi.org/10.1145/3582016.3582043).

59. Jiahao Qin; Hongxia Wang; Xudong Gao, et al. Lagrangian hierarchical mixed-integer programming for ultra-large-scale satellite scheduling under dynamic task delivery. *Advances in Space Research, 2026, 77(11): 11252-11270*. DOI: [10.1016/j.asr.2025.12.008](https://doi.org/10.1016/j.asr.2025.12.008).

60. Jianjiang Wang; Erik Demeulemeester; Dishan Qiu. A pure proactive scheduling algorithm for multiple earth observation satellites under uncertainties of clouds. *Computers & Operations Research, 2016, 74: 1-13*. DOI: [10.1016/j.cor.2016.04.014](https://doi.org/10.1016/j.cor.2016.04.014).

61. Xinwei Wang; Guopeng Song; Roel Leus, et al. Robust Earth Observation Satellite Scheduling With Uncertainty of Cloud Coverage. *IEEE Transactions on Aerospace and Electronic Systems, 2020, 56(3): 2450-2461*. DOI: [10.1109/TAES.2019.2947978](https://doi.org/10.1109/TAES.2019.2947978).

62. Christopher G. Valicka; Deanna Garcia; Andrea Staid, et al. Mixed-integer programming models for optimal constellation scheduling given cloud cover uncertainty. *European Journal of Operational Research, 2019, 275(2): 431-445*. DOI: [10.1016/j.ejor.2018.11.043](https://doi.org/10.1016/j.ejor.2018.11.043).

63. Jing Qi; Min Hu; Lining Xing, et al. Deep reinforcement learning-assisted large neighborhood search for online scheduling large-scale emergency tasks to Earth-observing satellites. *Expert Systems with Applications, 2025, 291: 128502*. DOI: [10.1016/j.eswa.2025.128502](https://doi.org/10.1016/j.eswa.2025.128502).

64. Zhe Li; Xin Zhu; Changdi Liu, et al. Dynamic task scheduling optimization by rolling horizon deep reinforcement learning for distributed satellite system. *Expert Systems with Applications, 2025, 289: 128350*. DOI: [10.1016/j.eswa.2025.128350](https://doi.org/10.1016/j.eswa.2025.128350).

65. Adam Herrmann; Mark A. Stephenson; Hanspeter Schaub. Single-Agent Reinforcement Learning for Scalable Earth-Observing Satellite Constellation Operations. *Journal of Spacecraft and Rockets, 2024, 61(1): 114-132*. DOI: [10.2514/1.A35736](https://doi.org/10.2514/1.A35736).

66. Adam Herrmann; Hanspeter Schaub. A comparative analysis of reinforcement learning algorithms for earth-observing satellite scheduling. *Frontiers in Space Technologies, 2023, 4: 1263489*. DOI: [10.3389/frspt.2023.1263489](https://doi.org/10.3389/frspt.2023.1263489).

67. Susan E. Sorenson; Sarah G. Nurre Pinkley. Multi-orbit routing and scheduling of refuellable on-orbit servicing space robots. *Computers & Industrial Engineering, 2023, 176: 108852*. DOI: [10.1016/j.cie.2022.108852](https://doi.org/10.1016/j.cie.2022.108852).

68. Shuai YIN; Chuanjiang LI; Edoardo FADDA, et al. On-orbit refueling robust mission scheduling with uncertain duration for geosynchronous orbit spacecraft. *Chinese Journal of Aeronautics, 2026, 39(1): 103774*. DOI: [10.1016/j.cja.2025.103774](https://doi.org/10.1016/j.cja.2025.103774).

69. K. Daneshjou; A.A. Mohammadi-Dehabadi; M. Bakhtiari. Mission planning for on-orbit servicing through multiple servicing satellites: A new approach. *Advances in Space Research, 2017, 60(6): 1148-1162*. DOI: [10.1016/j.asr.2017.05.037](https://doi.org/10.1016/j.asr.2017.05.037).

70. Weikui Liang; Hui Zhi; Peng Han, et al. GEO satellite on-orbit refueling and debris removal hybrid mission planning under uncertainty. *Advances in Space Research, 2024, 74(5): 2376-2387*. DOI: [10.1016/j.asr.2024.05.059](https://doi.org/10.1016/j.asr.2024.05.059).

71. Riccardo Apa; Jennifer Hudson; Marcello Romano. Low-Thrust Propulsion and Drift Orbit Optimization for Multi-Client Servicing Missions in Low Earth Orbit. *The Journal of the Astronautical Sciences, 2026, 73(2): 36*. DOI: [10.1007/s40295-026-00580-4](https://doi.org/10.1007/s40295-026-00580-4).

72. Riccardo Apa; Shambo Bhattacharjee; Jennifer Hudson, et al. Optimal Multi-Client Trajectory Planning for A Low-Thrust Servicing Satellite in the Presence of Perturbations. *The Journal of the Astronautical Sciences, 2025, 72(2): 7*. DOI: [10.1007/s40295-025-00487-6](https://doi.org/10.1007/s40295-025-00487-6).

73. Chi Han; Wei Xiong; Ronghuan Yu. A Hybrid Forecasting Model for Self-Similar Traffic in LEO Mega-Constellation Networks. *Aerospace, 2024, 11(3): 191*. DOI: [10.3390/aerospace11030191](https://doi.org/10.3390/aerospace11030191).

74. Zheng Shuang; Zhang Xing; Wang Peng, et al. Joint Beam Scheduling and Power Optimization for Beam Hopping LEO Satellite Systems. *China Communications, 2024, 21(10): 1-14*. DOI: [10.23919/JCC.ja.2022-0864](https://doi.org/10.23919/JCC.ja.2022-0864).

75. Zhiyuan Lin; Zuyao Ni; Linling Kuang, et al. NGSO Satellites Beam Hopping Strategy Based on Load Balancing and Interference Avoidance for Coexistence With GSO Systems. *IEEE Communications Letters, 2023, 27(1): 278-282*. DOI: [10.1109/LCOMM.2022.3213912](https://doi.org/10.1109/LCOMM.2022.3213912).

76. Ruili Zhao; Jun Cai; Jiangtao Luo, et al. Demand-Aware Beam Hopping and Power Allocation for Load Balancing in Digital Twin Empowered LEO Satellite Networks. *IEEE Transactions on Wireless Communications, 2025, 24(6): 5084-5098*. DOI: [10.1109/TWC.2025.3545745](https://doi.org/10.1109/TWC.2025.3545745).

77. Zhenglong YIN; Quan CHEN; Lei YANG, et al. Routing cost-integrated intelligent handover strategy for multi-layer LEO mega-constellation networks. *Chinese Journal of Aeronautics, 2025, 38(6): 103263*. DOI: [10.1016/j.cja.2024.09.039](https://doi.org/10.1016/j.cja.2024.09.039).

78. Nitinder Mohan; Andrew E. Ferguson; Hendrik Cech, et al. A Multifaceted Look at Starlink Performance. *Proceedings of the ACM Web Conference 2024, 2024: 2723-2734*. DOI: [10.1145/3589334.3645328](https://doi.org/10.1145/3589334.3645328).

79. Shengyu Zhang; Kwan L. Yeung. Scalable routing in low-Earth orbit satellite constellations: Architecture and algorithms. *Computer Communications, 2022, 188: 26-38*. DOI: [10.1016/j.comcom.2022.02.015](https://doi.org/10.1016/j.comcom.2022.02.015).

80. Shengyu Zhang; Xiaoqian Li; Kwan Lawrence Yeung. Segment routing for traffic engineering and effective recovery in low-earth orbit satellite constellations. *Digital Communications and Networks, 2024, 10(3): 706-715*. DOI: [10.1016/j.dcan.2022.09.022](https://doi.org/10.1016/j.dcan.2022.09.022).

81. Liang Gou; Dongming Bian; Yulei Nie, et al. Hierarchical Resource Management for Mega-LEO Satellite Constellation. *Sensors, 2025, 25(3): 902*. DOI: [10.3390/s25030902](https://doi.org/10.3390/s25030902).

82. Elad Denenberg. Satellite closest approach calculation through Chebyshev Proxy Polynomials. *Acta Astronautica, 2020, 170: 55-65*. DOI: [10.1016/j.actaastro.2020.01.020](https://doi.org/10.1016/j.actaastro.2020.01.020).

83. Nicholas Ravago; Brandon A. Jones. Risk-aware sensor scheduling and tracking of large constellations. *Advances in Space Research, 2021, 68(6): 2530-2550*. DOI: [10.1016/j.asr.2021.04.042](https://doi.org/10.1016/j.asr.2021.04.042).

84. Phasawee Saingyen; Sittiporn Channumsin; Suwat Sreesawet, et al. Performance Investigation of the Conjunction Filter Methods and Enhancement of Computation Speed on Conjunction Assessment Analysis with CUDA Techniques. *Aerospace, 2023, 10(6): 543*. DOI: [10.3390/aerospace10060543](https://doi.org/10.3390/aerospace10060543).

85. Simon Burgis; Lukas Rohrmüller; Martin Michel, et al. Simulation of satellites and constellations for the assessment of collision avoidance operations. *CEAS Space Journal, 2023, 15(5): 655-670*. DOI: [10.1007/s12567-022-00471-y](https://doi.org/10.1007/s12567-022-00471-y).

86. Zeno Pavanello; Luigi De Maria; Andrea De Vittori, et al. CAMmary: A review of spacecraft collision avoidance manoeuvre design methods. *Acta Astronautica, 2025, 236: 770-789*. DOI: [10.1016/j.actaastro.2025.07.027](https://doi.org/10.1016/j.actaastro.2025.07.027).

87. Thomas Uriot; Dario Izzo; Luís F. Simões, et al. Spacecraft collision avoidance challenge: Design and results of a machine learning competition. *Astrodynamics, 2021, 6(2): 121-140*. DOI: [10.1007/s42064-021-0101-5](https://doi.org/10.1007/s42064-021-0101-5).

88. Consultative Committee for Space Data Systems (CCSDS). Conjunction Data Message. CCSDS 508.0-B-1, June 2013, including Technical Corrigendum 2 (October 2021). [Official source](https://ccsds.org/publications/bluebooks/entry/3064/). Accessed 10 October 2026。

89. SpaceX. Starlink Collision Avoidance CONOPS. [official source](https://space-safety.starlink.com/docs/space-safety-articles/starlink_cola_conops/). Accessed 10 October 2026。

90. Louis Breger; Jonathan P. How. Safe Trajectories for Autonomous Rendezvous of Spacecraft. *Journal of Guidance, Control, and Dynamics, 2008, 31(5): 1478-1489*. DOI: [10.2514/1.29590](https://doi.org/10.2514/1.29590).

91. Ping Lu; Xinfu Liu. Autonomous Trajectory Planning for Rendezvous and Proximity Operations by Conic Optimization. *Journal of Guidance, Control, and Dynamics, 2013, 36(2): 375-389*. DOI: [10.2514/1.58436](https://doi.org/10.2514/1.58436).

92. Daniel Morgan; Soon-Jo Chung; Fred Y. Hadaegh. Model Predictive Control of Swarms of Spacecraft Using Sequential Convex Programming. *Journal of Guidance, Control, and Dynamics, 2014, 37(6): 1725-1740*. DOI: [10.2514/1.G000218](https://doi.org/10.2514/1.G000218).

93. Francisco Gavilan; Rafael Vazquez; Eduardo F. Camacho. Chance-constrained model predictive control for spacecraft rendezvous with disturbance estimation. *Control Engineering Practice, 2012, 20(2): 111-122*. DOI: [10.1016/j.conengprac.2011.09.006](https://doi.org/10.1016/j.conengprac.2011.09.006).

94. Zhenbo Zhao; Fan Wu; Jian Chen. Chance-constrained visual servoing MPC for non-cooperative spacecraft rendezvous. *Aerospace Science and Technology, 2026, 169: 111237*. DOI: [10.1016/j.ast.2025.111237](https://doi.org/10.1016/j.ast.2025.111237).

95. Purnanand Elango; Abraham P. Vinod; Kenji Kitamura, et al. Continuous-Time Successive Convexification for Passively-Safe Spacecraft Rendezvous on a Near Rectilinear Halo Orbit. *AIAA SCITECH 2026 Forum, 2026*. DOI: [10.2514/6.2026-2446](https://doi.org/10.2514/6.2026-2446).

96. Mark Stephenson; Hanspeter Schaub. Two Approaches to Autonomous Spacecraft Inspection: Shielded Reinforcement Learning versus Probabilistic Roadmaps. *The Journal of the Astronautical Sciences, 2026, 73(5): 89*. DOI: [10.1007/s40295-026-00631-w](https://doi.org/10.1007/s40295-026-00631-w).

97. Astroscale. Astroscale’s ADRAS-J Achieves Historic 15-Meter Approach to Space Debris. [official source](https://www.astroscale.com/en/news/astroscales-adras-j-achieves-historic-15-meter-approach-to-space-debris). Accessed 10 October 2026。

98. Kyle Hundman; Valentino Constantinou; Christopher Laporte, et al. Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding. *Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2018: 387-395*. DOI: [10.1145/3219819.3219845](https://doi.org/10.1145/3219819.3219845).

99. Junfu Chen; Dechang Pi; Zhiyuan Wu, et al. Imbalanced satellite telemetry data anomaly detection model based on Bayesian LSTM. *Acta Astronautica, 2021, 180: 232-242*. DOI: [10.1016/j.actaastro.2020.12.012](https://doi.org/10.1016/j.actaastro.2020.12.012).

100. Nils Kuhn; Bruno Sánchez Gómez; Natalia Moreno Blasco, et al. Validation-gated continual learning for anomaly detection in satellite telemetry. *Acta Astronautica, 2026, 249: 971-985*(assigned to the December 2026 issue; online date pending source confirmation). DOI: [10.1016/j.actaastro.2026.07.065](https://doi.org/10.1016/j.actaastro.2026.07.065).

101. Lars Herrmann; Marie Bieber; Wim J. C. Verhagen, et al. Unmasking overestimation: a re-evaluation of deep anomaly detection in spacecraft telemetry. *CEAS Space Journal, 2024, 16(2): 225-237*. DOI: [10.1007/s12567-023-00529-5](https://doi.org/10.1007/s12567-023-00529-5).

102. Sascha Wanninger. Knowledge-based satellite failure detection, isolation and recovery (FDIR). *CEAS Space Journal, 2026, 18(5): 991-1004*. DOI: [10.1007/s12567-025-00651-6](https://doi.org/10.1007/s12567-025-00651-6).

103. Antony Gillette; Alan George. Resilient Autonomous Mission Management for Decentralized Multispacecraft Missions. *Journal of Aerospace Information Systems, 2023, 20(7): 387-397*. DOI: [10.2514/1.I011208](https://doi.org/10.2514/1.I011208).

104. Chao Chen; Rui Xu; Shengying Zhu, et al. RPRS: a reactive plan repair strategy for rapid response to plan failures of deep space missions. *Acta Astronautica, 2020, 175: 155-162*. DOI: [10.1016/j.actaastro.2020.05.011](https://doi.org/10.1016/j.actaastro.2020.05.011).

105. Kathiravan Thangavel; Roberto Sabatini; Alessandro Gardi, et al. Artificial Intelligence for Trusted Autonomous Satellite Operations. *Progress in Aerospace Sciences, 2024, 144: 100960*. DOI: [10.1016/j.paerosci.2023.100960](https://doi.org/10.1016/j.paerosci.2023.100960).

106. Christopher John Lowe; Ruaridh Alexander Clark; Ciara Norah McGrath, et al. A delay-tolerant network approach to satellite pickup and delivery scheduling. *Ad Hoc Networks, 2023, 151: 103289*. DOI: [10.1016/j.adhoc.2023.103289](https://doi.org/10.1016/j.adhoc.2023.103289).

107. Changyuan He; Yunfeng Dong; Hongjue Li, et al. Reasoning-Based Scheduling Method for Agile Earth Observation Satellite with Multi-Subsystem Coupling. *Remote Sensing, 2023, 15(6): 1577*. DOI: [10.3390/rs15061577](https://doi.org/10.3390/rs15061577).

108. Nicola Muscettola; P.Pandurang Nayak; Barney Pell, et al. Remote Agent: to boldly go where no AI system has gone before. *Artificial Intelligence, 1998, 103(1-2): 5-47*. DOI: [10.1016/S0004-3702(98)00068-X](https://doi.org/10.1016/S0004-3702%2898%2900068-X).

109. Gregg Rabideau; Daniel Tran; Steve Chien, et al. Mission Operations of Earth Observing-1 with Onboard Autonomy. *2nd IEEE International Conference on Space Mission Challenges for Information Technology (SMC-IT'06), 2006: 367-373*. DOI: [10.1109/SMC-IT.2006.48](https://doi.org/10.1109/SMC-IT.2006.48).

110. Steve Chien; Joshua Doubleday; David R. Thompson, et al. Onboard Autonomy on the Intelligent Payload Experiment CubeSat Mission. *Journal of Aerospace Information Systems, 2017, 14(6): 307-315*. DOI: [10.2514/1.I010386](https://doi.org/10.2514/1.I010386).

111. NASA Jet Propulsion Laboratory. IPEX. [official source](https://ai.jpl.nasa.gov/public/projects/ipex/). Accessed 10 October 2026。

112. Francesco Basciani; Luciana Rebelo; Patrizio Pelliccione. Reference architecture for autonomy and adaptivity in satellites. *Journal of Systems and Software, 2026, 236: 112802*. DOI: [10.1016/j.jss.2026.112802](https://doi.org/10.1016/j.jss.2026.112802).

113. NASA Goddard Space Flight Center. Core Flight System - Demo Bundle. [official source](https://github.com/nasa/cFS). Accessed 10 October 2026。

114. NASA. What is Starling?. [official source](https://www.nasa.gov/smallspacecraft/what-is-starling/). Accessed 10 October 2026。

115. NASA. NASA Starling and SpaceX Starlink Improve Space Traffic Coordination. [official source](https://www.nasa.gov/centers-and-facilities/ames/nasa-starling-and-spacex-starlink-improve-space-traffic-coordination/). Accessed 10 October 2026。

116. Patrick W. Kenneally; Scott Piggott; Hanspeter Schaub. Basilisk: A Flexible, Scalable and Modular Astrodynamics Simulation Framework. *Journal of Aerospace Information Systems, 2020, 17(9): 496-507*. DOI: [10.2514/1.I010762](https://doi.org/10.2514/1.I010762).

117. Steve A. Chien. Formal Methods for Trusted Space Autonomy: Boon or Bane?. *NASA Formal Methods (Lecture Notes in Computer Science), 2022: 3-13*. DOI: [10.1007/978-3-031-06773-0_1](https://doi.org/10.1007/978-3-031-06773-0_1).

118. Matthew Rantanen; Jalil Modares; Nicholas Mastronarde, et al. Performance of the Asynchronous Consensus Based Bundle Algorithm in Lossy Network Environments. *2018 IEEE 10th Sensor Array and Multichannel Signal Processing Workshop (SAM), 2018: 311-315*. DOI: [10.1109/SAM.2018.8448984](https://doi.org/10.1109/SAM.2018.8448984).

119. Francesco Basciani; Arianna Fedeli; Daniele Masti, et al. A model-driven framework for supervised reconfiguration of satellite schedulers. *Software and Systems Modeling, 2026*. DOI: [10.1007/s10270-026-01426-1](https://doi.org/10.1007/s10270-026-01426-1).

120. Philipp Chrszon; Paulina Maurer; George Saleip, et al. Model checking of spacecraft operational designs: a scalability analysis. *Software and Systems Modeling, 2025, 24(6): 1825-1846*. DOI: [10.1007/s10270-025-01281-6](https://doi.org/10.1007/s10270-025-01281-6).

121. Dhiraj Bhattacharjee; Pablo G. Madoery; Aizaz U. Chaudhry, et al. On-Demand Routing in LEO Mega-Constellations With Dynamic Laser Inter-Satellite Links. *IEEE Transactions on Aerospace and Electronic Systems, 2024, 60(5): 7089-7105*. DOI: [10.1109/TAES.2024.3415571](https://doi.org/10.1109/TAES.2024.3415571).
