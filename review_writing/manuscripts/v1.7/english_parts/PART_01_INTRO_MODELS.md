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
