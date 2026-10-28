# C4N02_ROSSI｜Communication-Aware Orbit Design for Small Spacecraft Swarms around Small Bodies

作者：Federico Rossi; Saptarshi Bandyopadhyay; Mark Mote; Jean-Pierre de la Croix; Amir Rahmani。年份：2022。

实际版本：31-page author-hosted JGCD22 manuscript; journal metadata 45(11):2046–2060; publisher text parity not checked。

[实际全文](https://www.federico.io/pdf/Rossi.Bandyopadhyay.Mote.delaCroix.Rahmani.JGCD22.pdf)。DOI：10.2514/1.G006515。

PDF SHA-256：`f55952381730ac0b430a04736ca84da11aefe6d9ed7b453be2269389029cda31`。

本轮正文阅读：1–29; references 29–31 checked for identity only。原页视觉核对：[25]。

采用：`ADOPT`。既有身份：No matched body-reading note in checked repository。本轮为AI正文阅读；未独立复现、未替代作者科学终核。

## 问题、模型与方法

六个带不同科学仪器的小航天器围绕433 Eros运行，另有固定轨道的载体收集数据。外层优化各科学航天器的初始状态，内层在给定轨道上安排观测和时扩网络数据流，受可观测性、链路容量及存储限制。计入奖励的数据须在规划时域内到达载体；奖励包含观测区域价值、观测质量和完成比例。

外层采用多起点与信赖域搜索，内层混合整数模型经LP松弛及指向修复生成方案；利用对偶信息和状态转移矩阵，将资源调度对轨道的敏感性传回外层。几何采用便于求导的观测窗口近似和遮挡近似。高不规则重力下的数值传播与优化中的平滑表达分工明确。

## 可追溯论点

- C4-N02-01：同一个科学回报目标可以通过轨道外层、观测/数据流内层分解计算。定位：§III–V，pp7–22；算法1。联合建模与分解计算可组合。
- C4-N02-02：低带宽算例将有限链路配置给高价值数据来源，结果并非由全网总带宽最大化解释。定位：pp25–27，表2及图8。
- C4-N02-03：把参考距离100 km的带宽参数由10 kbps提高到250 kbps后，作者报告两种轨道设计结果几乎无差别。定位：p27。该反例支持“资源瓶颈影响耦合的价值”。
- C4-N02-04：表2为595.9与354.9的加权reward，非原始字节量；基线还使用逐星贪心与采样。定位：pp24–25。不能把67.9%解释成仅增加一个联合约束后的独立因果效应。

## 适用范围

这是小天体多器设计的方法实例；未优化时域内推进动作，导航与执行不确定性未完整加入，轨道范围通过惩罚表达，有限时域中仍有轨道接近结束时逸出。已视觉检查p25表2。采用其轨道—资源反馈机制和带宽条件，不将结果改写为地球大型星座验证。作者主页摘要与本次PDF结果措辞不同，按实际PDF使用，未关闭正式版配对。
