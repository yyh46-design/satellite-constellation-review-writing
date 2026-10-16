# [100] 关联作者代码静态核查

目标论文：Validation-gated continual learning for anomaly detection in satellite telemetry（面向卫星遥测异常检测的验证门控持续学习）。DOI：[10.1016/j.actaastro.2026.07.065](https://doi.org/10.1016/j.actaastro.2026.07.065)。

本轮未取得这篇论文的完整方法/结果正文。作者公开仓库README引用了该DOI，固定提交为 `636ac05995f52d3a12b6c7186646757a28c900eb`。取得10个文本文件，只实际检查下表列出的路径与片段；没有安装环境、执行代码、下载数据或复现实验。此记录不计论文精读增量。

## B08-100-A01 更新触发与数据顺序

所核循环先对当前批预测，再保存输入/异常标志，并在预设批索引处调用重训练。

证据：[src/Main_loop.py:128–144](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/Main_loop.py#L128-L144)；[src/CL_methods/continual_learning_manager.py:66–87](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/CL_methods/continual_learning_manager.py#L66-L87)。

边界：这是固定提交的调用路径观察；未测真实延迟，未证明全部方法、配置和论文实验都采用同一协议。

## B08-100-A02 更新样本与标签条件

扩展数据函数按传入异常标志排除样本，将保留片段加入临时训练集与验证集。

证据：[src/dataset_manager.py:146–214](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/dataset_manager.py#L146-L214)。

边界：异常标志的生成、确认时延和部署可得性尚未完整追踪；不能据此宣称无标注在线学习，也不能直接判定数据泄漏。

## B08-100-A03 验证门控的指标与恢复点

在ER且fixed_epochs=false路径中，先保存旧权重并测基线验证损失；只有损失下降超过配置delta才更新检查点，结束时加载该检查点。

证据：[src/CL_methods/er.py:88–129](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/CL_methods/er.py#L88-L129)；[src/CL_methods/utils.py:7–31](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/CL_methods/utils.py#L7-L31)；[src/base_model.py:53–66](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/base_model.py#L53-L66)；[src/experiment_config.py:68–88](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/experiment_config.py#L68-L88)。

边界：所核为预测损失上的经验门控，不是碰撞概率、任务安全、恢复成功或闭环性能保证；没有执行训练或测量结果。

## B08-100-A04 配置改变门控语义

ER的fixed_epochs分支按固定轮次保存权重，保存条件不要求验证损失改善；配置文件默认fixed_epochs=false。

证据：[src/CL_methods/er.py:111–129](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/CL_methods/er.py#L111-L129)；[src/experiment_config.py:80–88](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/experiment_config.py#L80-L88)。

边界：论文实际实验配置未核，不能将该分支称为论文默认行为或据此否定论文；正式写作应说明核对的配置。

## B08-100-A05 计时口径

管理器total_time在该轮训练结束、后续缓冲加入之前累加；主循环把它作为total_cl_time输出。

证据：[src/CL_methods/continual_learning_manager.py:78–89](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/CL_methods/continual_learning_manager.py#L78-L89)；[src/CL_methods/continual_learning_manager.py:234–243](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/CL_methods/continual_learning_manager.py#L234-L243)；[src/Main_loop.py:164–178](https://github.com/DerKuhno/validation-gated-continual-learning/blob/636ac05995f52d3a12b6c7186646757a28c900eb/src/Main_loop.py#L164-L178)。

边界：这个计时字段不覆盖全部推理、后处理和后续缓冲操作；不可直接当作端到端调度响应时间，未实测各部分成本。

## 对综述的用途

可在取得正文后，作为第3章模型更新与第4章反馈分析的核验线索：触发更新、确认训练数据、评价候选、保留旧权重和使更新生效是不同环节。当前只能根据所核ER路径说明这种区分，不能据此断言所有配置或论文实验均如此。验证损失与最终任务结果也需要分别评价。

仍缺论文全文、作者实际实验配置、其他策略路径、异常标志来源/确认时延、完整数据协议，以及与期刊结果的逐项对应。
