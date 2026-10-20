# B16-S037｜用周期更新近似集中控制的少通信架构

Spacecraft Formation Control in Deep Space with Reduced Communication Requirement

- 作者：Javad Lavaei; Ahmadreza Momeni; Amir G. Aghdam
- [书目/原文入口](https://users.encs.concordia.ca/~aghdam/TechnicalReports/TCST.pdf)；标识：author-report:TCST.pdf。
- 实际版本：实际读取大学作者站16页未标年报告；相关正式记录为2008年TCST 16(2),268–278、不同题名，DOI 10.1109/TCST.2007.903389。正式11页PDF未取得或逐字配对。
- [实际读取PDF](https://users.encs.concordia.ca/~aghdam/TechnicalReports/TCST.pdf)；来源ID：E-B16-S037；共16页。
- 源文件SHA-256：9b8061fa6a486beb40e5e6cecc3c8983f201de21526ed718bb42c1919a0afaa1。
- 阅读范围：PDF物理页1–15的正文叙述；关键原页视觉核查：5, 8, 9, 11, 15。
- 附录/证明范围：No separate appendix; proof narratives read but not independently reproduced。
- 证据角色：general_communication_architecture_with_UAV_validation。
- 专题补充编号S031–S040；不占原80篇L编号。AI精读完成，人工终核待完成；未逐式复证明或独立复现。

## 研究问题

已有集中控制器满足性能要求时，怎样让每个局部控制器通过模型副本和较少的信息交换接近原性能？

## 输入、决策与协同机制

层级LTI编队模型和已有集中动态控制器；各体估计其他体状态，模型、初始状态及可测信息决定能否保持内部稳定及性能。

将集中控制器分解为局部动态控制器，检查修改系统的稳定性；在周期更新版本中重置其他体状态估计，区间内预测整体运动。

理想等价需要完全准确的模型和初值。周期更新减少长期模型漂移，但作者只提出若预测危险则调用应急控制器的接口，严格避碰分析和重置稳定性条件仍未闭合。

## 验证设置与证据层级

实际数值对象是3架平面UAV，以英尺和英尺/秒计量；包括LQR性能与10%模型偏差例，并非轨道编队或在轨试验。相关正式书目与作者/摘要相符，但本文论点只绑定实际16页报告。

## 可追溯论点

- **C-B16-028**：与集中控制完全等价需要各体准确知道他体模型和初态；作者承认此条件不现实，实际分散控制另需检查内部稳定性。
  原文定位：PDF物理页5, 6；Theorems1–2及initial-state discussion。
- **C-B16-029**：周期刷新模型状态能减小信息陈旧，但预测危险后的应急控制器及严格避碰/重置稳定性仍待研究；更短周期并非无条件改善安全。
  原文定位：PDF物理页8, 9, 15；§II-D及Conclusion。
- **C-B16-030**：数值例实际为3架平面UAV和相对GPS信息，性能差1.08%来自选定模型/初值条件；不能写成深空三星在轨结果或普遍性能界。
  原文定位：PDF物理页10, 11, 12；§IV及performance comparison。
- **C-B16-031**：实际16页作者稿与相关正式题名不同，正式记录作者/摘要对应且DOI为10.1109/TCST.2007.903389；未取得正式全文逐字配对，只计一条研究记录。
  原文定位：PDF物理页1, 15；actual PDF title plus Crossref/Caltech bibliographic identity record。

## 适用边界与待核问题

- 题名含spacecraft不能把三UAV数值验证升级为航天器验证。
- 2008为相关正式论文的书目年，实际报告未标年。
- 周期状态更新与真实链路时延不同，后者仍列为后续。
- 应急切换只是架构建议，不能作已认证的安全备份。

## 对综述的作用

用作3.6.3采用接口的历史背景：本地模型副本、信息刷新、预测检查与接管责任需要分别说明；避免把“建议接管”写成已完成安全认证。

以上采用建议为阅读者分析，尚未写入v3.2；不把作者主张、读者推论或文件完整性检查当作独立科学确认。
