# 本次原文复核的两项澄清

这两项记录补充V3.3的采用依据，不改写冻结的旧精读笔记，也不增加独立论文阅读数。机器可读版本见[PRIMARY_SOURCE_CLARIFICATIONS.json](PRIMARY_SOURCE_CLARIFICATIONS.json)。

**R33-OBS-001：S011，Run Time Assurance for Autonomous Spacecraft Inspection。** 实际版本为arXiv:2302.02885v2。PDF物理p5式(13)给出几何星间分离；p6式(17)是成员互相观测时的传感器太阳视线禁入约束。p11对分散方案失败的讨论联系后者的控制冲突。因此不能将所有失败都归结为实体碰撞，也不能解释为分散方案仅有局部状态；原文两种实现均使用全部成员状态。本版3.6.2使用C-B14-001、C-B14-002及本项澄清，不采用旧C-B14-003中过宽的“星间避碰约束”概括。原批次文件保留原字节，修正关系在此留痕。

**R33-OBS-002：S051，Motion Planning Strategies for Safety Procedure of Multisatellite Formation-Flying Systems。** 实际阅读的是DLR保存的36页作者接收稿。故障场景在PDF物理p29—30假定故障从星能够通过全向RF发送告警，使主星和健康从星立即响应。本版3.6.3明确保留这一信息条件；该例不提供任意通信中断条件下仍能接管的证据。

两项均为针对原文相关段落的AI复核，人工终核仍待完成。
