# v3.2-CN：运行决策主线调整版

**完整正文：[REVIEW_CN_v3.2.md](REVIEW_CN_v3.2.md)**

题名：《大型卫星星座智能运行管理中的规划与协同决策方法综述》。

本轮直接修改完整稿件，不只提供重写提纲。主线由“怎样求出调度安排”调整为“怎样形成决定—协调决定—采用并更新决定”，保留任务与资源调度的算法主体，并将状态驱动策略、恢复行动及执行监督纳入具体比较。

## 优先阅读

- [最终主线及范围规范v1.3](../../discussion/operations_decision_mainline_20261020/MAINLINE_SCOPE_v1.3_CN.md)
- [分章修改说明及对照片段](REVISION_GUIDE_CN.md)
- [新增和提升论证的证据矩阵](audit/DECISION_ROLE_EVIDENCE.csv)
- [66项新旧引用与稳定编号](references/REFERENCE_NUMBER_MAP_v3.1_to_v3.2.csv)
- [来源变化及历史证据接续](references/SOURCE_CHANGES_CN.md)
- [待关闭事项](OPEN_ITEMS_CN.md)
- [Codex本地核对和Word导出任务](CODEX_VERIFY_AND_EXPORT_CN.md)

## 实际完成与边界

五章完整正文、七表、四幅继承的英文PNG草图、66项引用（57篇学术、9项工程）。v3.1的64项来源全部保留，恢复库内E105和E107，95项库中其余29项保留不引。引文按当前正文顺序重排，图注同步；图片二进制保持不变，图内旧文字/引文仍需最终逐像素核对。

主要变化集中于摘要和1.1—1.3、2.2—2.4、3.5、4.2—4.5及结论。第2.3节是明确标注的说明情景，不是新实验。FDIR地面原型不升级为星座飞行证据，受监督软件配置不升级为自主业务部署，人工批准不被默认删除。

本轮完成的是**GitHub完整Markdown主稿与研究记录发布**，没有生成或验收v3.2 Word/HTML，不把v3.1的23页或旧页面检查继承为新版成绩。正文可直接在GitHub连续阅读；本地导出请按接手说明使用原Word样式。

工具`tools/verify_v32.py`用于在克隆仓库内校验编号、来源身份及图片哈希，并生成引用索引、95项处置表和逐行对照。它在本轮发布时尚未针对远端完整克隆执行；不附虚假的PASS报告。远端发布核对与科学/排版验收分开。

本轮没有新增完整精读篇数、没有关闭正式版配对、没有新增性能实验。新增分析的原页或历史依据见证据矩阵与复核记录；`human_verified=false`、`submission_ready=false`。

## 基线与发布方式

基线提交：`06bbd4bbfd0dc67662dd19a9fe237927ca5e16b0`；基线tree：`a5aef8889da814376505b10ff7d960dd197e55b9`。

独立分支：`writing/constellation-review-v3-2-operations-decisions-20261020`。仅新增v3.2目录及主线补充规范，不修改v3.1、历史精修规范或main。原v3.1完整字节、Word及来源记录仍可在固定基线读取。
