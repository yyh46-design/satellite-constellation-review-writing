# [17] Joint satellite platform and constellation sizing for instantaneous beam-hopping in 5G/6G Non-Terrestrial Networks

中文译名：面向5G/6G非地面网络瞬时跳波束的卫星平台与星座联合规模设计。DOI：[10.1016/j.comnet.2024.110942](https://doi.org/10.1016/j.comnet.2024.110942)。

版本：publisher_typeset_version_hosted_institutionally。UPM公开PDF具有Computer Networks 257 (2025) 110942、最终排版、DOI及版权/许可标记。OpenAlex的submittedVersion标签与实际文件不符；按实际页认定为出版社排版正式版副本。

[实际阅读入口](https://oa.upm.es/88332/1/10309454.pdf)；本轮类别：followup_no_unique_increment。历史已计数来源补读，不重复计篇数。

本轮范围：物理页[3, 10, 12]的相关段落；实际图页相关区域[10, 12]。PDF SHA256 `06661c9a49d0e32888481708abc1c23c95f204b6a8fda0d8356a582c0de84094`。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-017-C01|§2.2 antenna architecture；物理页[3]|更细波束/小区提高按地域需求分配的灵活性，同时增加星上天线复杂度和切换序列颗粒度。|架构灵活性与实现负担一起变化，不能只把小区细化写成无代价收益。|
|B07-017-C02|power budget; Table3; Eq16；物理页[10]|平台功率估算采用载荷占比，且假定地影与日照采用相同运行模式，不在地影额外限制业务。|这是尺寸设计前提，不是已求解含电池状态和调度限电的全年运行策略。|
|B07-017-C03|Eqs18–20; Table3；物理页[10]|太阳阵列尺寸用寿命末期功率，案例分别设VLEO三年与LEO五年寿命。|不同寿命会改变补充需求；由寿命标称值不能推出随机失效补给及时性。|
|B07-017-C04|Table6; Eq22; 15-year cost comparison；物理页[12]|15年比较中，短寿命方案需要更多轮替换；总CAPEX与单位容量成本又可能给出不同排序。|保留寿命、容量分母和排除运营费用；不把低单位容量估值当低总预算或低恢复损失。|

服务综述：3.1.1/4.2：平台功率设计与持续能力的条件。

仍缺：其余链路与波束推导、完整寿命/电池动态及成本仍未独立复现；不是2026市场报价。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
