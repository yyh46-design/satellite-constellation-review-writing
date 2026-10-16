# [92] Model Predictive Control of Swarms of Spacecraft Using Sequential Convex Programming

中文译名：采用序列凸规划的航天器集群模型预测控制。DOI：[ 10.2514/1.G000218 ](https://doi.org/10.2514/1.G000218)。

版本：publisher_typeset_VOR_copy_author_public_repository。入口：[实际阅读来源](https://caltech.app.box.com/shared/static/xb19dc8ih9su97894omrmh8k44tfko1u.pdf)。作者Caltech研究页直接链接公开Box副本，16页正式JGCD37(6)(2014):1725–1740排版，题名/DOI吻合；不保存临时签名下载跳转。

本轮类别：followup_no_unique_increment。补读不增加不同论文数。

阅读范围：物理PDF选读页[4, 5, 6, 11, 12]；实际图页复核[5, 6, 12]的相关区域；文件SHA256 `e977867ad600a2be7ab982703c34e07d80f90000363d95daa9bfa266c06e6bb0`。

|ID|原文定位|观察|使用边界|
|---|---|---|---|
|B05-092-C01|Eq10–18; Proposition1/Figs2/3；页[4, 5]|动力学线性化并零阶保持离散；避碰用名义轨迹定义安全半空间，给出充分条件。|半空间是保守限制，不是原非凸可行域的等价替换。|
|B05-092-C02|Eq19–23, trust-region and iteration budget；页[6]|通过缩信赖域使相邻迭代变化小于阈值，并按每轮耗时与总预算选迭代数。|迭代变化小不能独立证明原非线性全局最优或闭环渐近稳定。|
|B05-092-C03|continuous safety; Remark6；页[11, 12]|离散点避碰另需速度、加速度与步长条件；缩步长改善安全界却增计算负担。|不能只展示离散轨迹就宣称连续安全，步长与求解期限须共同报告。|
|B05-092-C04|Theorem7; infeasibility discussion；页[12]|条件化可解性针对初始/避碰约束；速度推力限制仍可能导致不可行，文中建议延长末时。|该定理不是全部约束递归可行或原截止期保证。|

服务综述：3.4.2及4.4：凸化内近似、信赖域、离散步长与约束恢复。

仍缺：全部定理条件、非线性闭环稳定性、全时域安全与独立求解复现未完成；B04通信/误差/期限条件保持。

作者归纳与原文观察分列；候选位置只供后续修订，不表示原段已整体核验。下载/HTML可见/渲染均不计为自动精读完成。`human_verified=false`；正式版配对、全部证明与独立实验未关闭。
