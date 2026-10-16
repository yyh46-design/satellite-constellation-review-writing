# [108] Remote Agent: to boldly go where no AI system has gone before

中文译名：Remote Agent：迈向人工智能系统尚未涉足之境。DOI：[10.1016/S0004-3702(98)00068-X](https://doi.org/10.1016/S0004-3702(98)00068-X)。

版本：author_manuscript_hosted_at_MIT。MIT作者公开46页稿，标题/作者/正文对应Artificial Intelligence 103 (1998):5–47，实际文件非最终43页期刊分页；未比较正式版。pypdf文字有字形转义，PDFium更可读。

[实际阅读入口](https://people.csail.mit.edu/williams/Web%20site/papers/aij98.pdf)；本轮类别：followup_no_unique_increment。补读不增加去重数。

阅读范围：物理页[28, 29, 38, 39]的相关段落；实际图页复核[28, 38]的相关区域。PDF SHA256 `f9f4b623e6735ac1346c4fd08cf4dd3202b5bf139bc4c0c73f667f7b38c68600`。

|命题ID|原文定位|观察|解释与使用边界|
|---|---|---|---|
|B06-108-C01|EXEC/MIR integration；物理页[28]|真实飞控开发促使恢复从逐活动转为暂停失败活动，并携全局约束保护正常子系统。|恢复局部可行不能自动代表其他任务承诺仍满足。|
|B06-108-C02|execution language redesign；物理页[28, 29]|需表示持续属性、嵌套恢复上下文与外部中断暂停，推动执行语言重设计。|仅接入规划器和诊断器不足，跨模块同步语义也是实现条件。|
|B06-108-C03|human-centered operations；物理页[38]|保留地面多层监控指令、异步任务轮廓及模型/参数更新能力。|自主能力与人类监督并存，不宜以有人接管否定全部自治或反向推全无人。|
|B06-108-C04|validation/modeling separation；物理页[38, 39]|区分可审模型与求解启发式，并强调先覆盖关键功能再细化组件。|模型可检查支持验证工作，但不是全部功能与任意模型更新均获证明。|

服务综述：3.5及4.3/4.4：跨活动恢复约束和人机权限。

仍缺：46页作者版存在抽取字形问题，相关区域视觉核读；1998论文不是对后续1999全部在轨结果的完成证明；全部状态模型未复现。

原文观察与作者综合分析分开；正文候选尚未应用。human_verified=false，formal_version_parity_closed=false，submission_ready=false；无完整证明审核和独立实验复现。
