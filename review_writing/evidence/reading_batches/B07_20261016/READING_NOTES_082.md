# [82] Satellite closest approach calculation through Chebyshev Proxy Polynomials

中文译名：基于Chebyshev代理多项式的卫星最近接近计算。DOI：[10.1016/j.actaastro.2020.01.020](https://doi.org/10.1016/j.actaastro.2020.01.020)。

版本：author_accepted_manuscript_public_HTML_2020-06-07。公开页面明确Authors Accepted Manuscript，接受日15January2020，作者EladDenenberg于7June2020上传；本轮未取得PDF，不推定正式版内容相同。

[实际阅读入口](https://www.researchgate.net/publication/338609111_Satellite_Closest_Approach_Calculation_Through_Chebyshev_Proxy_Polynomials)；本轮类别：new_targeted_from_inherited。新增去重定向记录。

本轮范围：公开HTML工具快照行[[247, 326], [919, 1274], [1288, 1595], [1726, 2004], [2069, 2214]]，无本机PDF哈希/页数/图公式像素。

|命题ID|原文定位|观察|解释与引用边界|
|---|---|---|---|
|B07-082-C01|HTML L247–326; L2199–2214；物理页不适用|位置/速度传播在算法中作为黑箱；实际评估使用SGP4，换传播器、含机动和星上实现仍列为后续工作。|接口可替换不等于跨传播器已验证，桌面结果不能写成在轨部署。|
|B07-082-C02|HTML L919–1054 versus L1100–1175；物理页不适用|一般CPP求根介绍升阶/二分的代价折中，具体CATCH用预选阶数和周期相关固定分段减少反复调整。|不能将一般自适应求根描述自动归给本文固定参数实现；未证统一误差上界。|
|B07-082-C03|HTML L1100–1175; L1389–1400; L1895–2004；物理页不适用|N=16和半最短轨道周期的间隔来自所测算例选择；原文承认高偏心率案例精度下降。|每段极值数、可微性和固定阶数等数学前提尚未独立审核；不当作任意摄动/机动域证书。|
|B07-082-C04|HTML L1402–1419; L1574–1595；物理页不适用|性能表同时给CPU时间、传播评价数、代理构建数和误差；例中基准最小值由Matlab multistart获得。|误差相对同一传播模型下的数值基准，不是实际测轨真值误差或碰撞概率校准。|
|B07-082-C05|HTML L2111–2161; Table11；物理页不适用|one-on-all先经几何筛查剩5563对象，表11时间单位为分钟，误差比较再以SBO-ANCAS作基准。|不得把表11分钟转录成秒；不能将筛查后单星对目录结果当全部对象两两精算。|
|B07-082-C06|HTML L1056–1274; L2175–2214；物理页不适用|产物是TCA和相应距离；HTML公式/伪代码的导数、变量标记有待PDF像素复核。|数值近距离计算本身不输出规避动作或任务恢复；不据HTML记号缺损判代码错误或完成证明。|

服务综述：3.4.1/4.1：候选精算与筛查、概率风险分离。

仍缺：本轮仅作者接受稿公开HTML；本机PDF、公式图表像素、正式版配对、数学前提、端点与伪代码记号及星载实测仍缺。

这是定向命题核读，未申报全页/全证明完成或独立实验复现；human_verified=false、formal_version_parity_closed=false、submission_ready=false。正文候选未应用。
