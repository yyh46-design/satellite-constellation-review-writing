# 第二章轨道设计与建模：本轮定向精读

日期：2026-10-27。用途：讨论稿第二章的内容补强。材料保存在输出目录，未修改论文仓库。

本轮核对了旧精读目录、V3.5.9参考文献注册表及R2固定提交402de0c31cb2642821563f6f6288987664636f51的候选池。Savitri 2017已列为R2-C025，此前标记NOT_BODY_READ；Avendaño 2013可沿已有均匀星座重构研究的参考文献追溯。本轮阅读新增覆盖以下三项原始研究的正文。Lee 2020和Rogers 2026为既有笔记复核，不计为本轮新增精读。

## 1. 构型参数化

Avendaño, M. E.; Davis, J. J.; Mortari, D. The 2-D lattice theory of Flower Constellations. Celestial Mechanics and Dynamical Astronomy, 116, 325–337, 2013. DOI: 10.1007/s10569-013-9493-8。

实际来源：[作者上传的在线全文](https://www.researchgate.net/publication/257546091_The_2-D_lattice_theory_of_Flower_Constellations)。阅读§1–9，重点§3–5与§8；未取得可本地打开的PDF，未独立复证全部整数算法。

可用认识：§4以轨道面数、每面星数、构型相位数组织整数参数；§5使轨道周期相容条件成为可选条件；§8给出圆轨道Walker-Delta与二维格点构型的参数对应。适合用于说明构型族、周期条件、搜索变量之间的关系。理论主体采用开普勒模型，长期维持成本不由本篇给出。

整合判断：2.3应先讨论如何表示与限定设计空间，再讨论求解方法；经典名称之间应交代包含或对应关系。

## 2. 连续轨道参数搜索与覆盖计算

Savitri, T.; Kim, Y.; Jo, S.; Bang, H. Satellite Constellation Orbit Design Optimization with Combined Genetic Algorithm and Semianalytical Approach. International Journal of Aerospace Engineering, 2017, 1235692. DOI: 10.1155/2017/1235692。

实际来源：[出版社在线正文](https://onlinelibrary.wiley.com/doi/10.1155/2017/1235692)。阅读§1–6、表1–9的文字与数据；重点§3、§5。在线提取未完整显示公式图像，公式细节和部分曲线尚需PDF核对；不把这一轮记作逐式复核。

可用认识：半解析模型计算经纬度访问区间，以交集确定目标可见时段，再供NSGA-II评价轨道参数。主要设计算例为韩国区域、50个有效网格点、6小时、3星及6星变化案例。适合说明物理建模怎样减少重复覆盖评价。

采用重点是建模与搜索的组合。文中近地点/远地点措辞、部分ART标注及加速误差表述需要结合公式和图表进一步核对；本轮不摘录这些数值作综述的性能结论。

整合判断：与Lee、Rogers衔接时，说明这里改变轨道参数以重新产生访问机会，后两类模型主要在给定轨道族或候选可见性上选择构型。

## 3. 初始设计与后续维持

Arnas, D.; Casanova, D.; Tresaco, E. Relative and Absolute Station-Keeping for Two-Dimensional–Lattice Flower Constellations. Journal of Guidance, Control, and Dynamics, 2016. DOI: 10.2514/1.G000358。

实际来源：[萨拉戈萨大学机构存档](https://zaguan.unizar.es/record/130403/files/texto_completo.pdf)。本地文件为sources/ARNAS_2016.pdf，共19页作者稿；阅读正文第1–18页，书目第18–19页。实际视觉检查第8、9、16页。采用此稿页码，未与正式排版逐式配对。

可用认识：§III修正初始半长轴并调整偏心率、倾角，减小J2下构型漂移；§IV进一步根据允许的对地轨迹偏差设计机动。表2和表3比较一年、五年演化，体现初始修正与持续维持各自的作用。例子采用27星中轨Galileo式构型。

整合判断：2.2解释摄动如何进入设计，2.4解释保持何种任务几何；机动时机与策略留给第三章。星间分布保持与对地轨迹保持需要分开陈述。

## 与既有材料的组合

已有Lee 2020笔记：B03_20261015/READING_NOTES_014.md，实际版本arXiv:1910.00672v4。Rogers笔记：R2/reading_notes/N001_ROGERS_CN.md，实际版本arXiv:2507.09855v2。此次仅复核笔记，不重复增加完成篇数。

推荐的论述顺序由本轮综合提出：任务需求形成几何要求；构型参数化限定搜索空间；动力学模型形成访问时序并预测其演变；连续参数优化或离散候选选择寻找方案；最后结合部署与维持评价方案能否持续提供任务能力。这里的顺序是综述组织建议，不是某一篇论文验证过的完整统一算法。

## 已发现、未纳入本轮完成数

- R2-C005：马剑等，特定区域密集观测的低轨卫星星座最优设计方法，DOI 10.1360/N092017-00026。检索到出版社PDF索引，当前全文下载入口失败；保持候选状态。
- Huang, Colombo, Bernelli-Zazzera，Multi-criteria design of continuous global coverage Walker and Street-of-Coverage constellations through property assessment，DOI 10.1016/j.actaastro.2021.07.002。检索到机构存档及作者上传稿，尚未完成正文阅读，可用于下一轮综合设计取舍。此次不据其摘要概括性能结果。

论文仓库和原有来源状态均未修改。
