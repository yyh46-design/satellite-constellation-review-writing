# B17-S048｜NanoFF双2U卫星推进与差分阻力分阶段在轨运行

In-orbit demonstration of propulsive and drag-based formation control using two 2U CubeSats under operational constraints

- 作者：Debdeep Roychowdhury; Sebastian Grau; Fynn Boyer; Sascha Kapitola; Alan Legenza; José Manuel Diez; Benjamin Palmer; Enrico Stoll
- [来源入口](https://doi.org/10.1007/s12567-026-00702-6)；标识：10.1007/s12567-026-00702-6。
- 实际版本：CEAS Space Journal出版社开放PDF，共33页，2026年；2026-01-19接受；多项实验状态以2025-06-01为截止，不能视为2026-10现况。
- [实际获取PDF](https://link.springer.com/content/pdf/10.1007/s12567-026-00702-6.pdf)；33页；来源ID：E-B17-S048。
- 源文件SHA-256：062b392010e7a5d6ce9fc592929f8a223687c950c085dc1fa8a8c2c86b114087。
- 正文叙述范围：PDF物理页1–30；关键页视觉核查：13, 19, 22, 26, 28, 29。
- 附录/证明范围：No separate appendix; proof formulas read selectively, glossary pp31–32 and references pp32–33 skim; data statement p32 read。
- 证据角色：multi_spacecraft_flight_operations；采用状态：candidate_after_human_review。
- AI正文精读完成；人工终核待完成；未逐式复证明或独立复现实验。专题编号不占原80篇L编号。

## 研究问题

资源受限的双2U卫星如何在GNSS间歇、下传有限、食区姿态不可用和推进性能偏差下，以阶段性策略完成安全接近与构型维护。

## 输入、决策与协同机制

两颗NanoFF于2024-01部署，使用本星/地面GNSS与公开TLE估计ROE，部分阶段通过地面上传双方TLE。UHF星间链路在任务中存在，但文中更高精度状态自主交换和完整自主编队功能仍有后续计划。

先小推力脉冲抑制约45 km/d漂移，再采用差分阻力降低相对沿轨距离；通过安全E/I几何安排近距交叉。法向脉冲依据日照、传感器可用性与推进剂均衡选择哪颗星何时动作。

这是空间/地面共同维护的运行闭环：动作后等待导航更新，比较目标与实际ROE，人工修正阻力/推进参数再规划。已在轨ADM根据ROE、内外阈值和电压调节姿态，核心逻辑约30 min执行；安全近距交叉自动化及预测控制仍属计划能力，不能与已演示ADM混为一谈。

## 验证设置与证据层级

七次沿轨漂移抑制机动总Δv约0.211 m/s；与GNSS可比较的仅3次，其TLE估计Δv差异小于3 mm/s。首个受控交叉约1.8 km径法向最小分离，TLE沿轨误差可到1.5 km，而径/法向小于0.25 km。ADM示例运行在约80 km沿轨间隔；2025-04-11因PCU相关问题停止。上述为作者公开飞行分析，并非本批获取原遥测独立复算。

## 可追溯论点

- **C-B17-036**：七次沿轨机动总Δv约0.211 m/s；仅3次可作GNSS/TLE对照，Δv估计差异小于3 mm/s。
  原文定位：PDF物理页11, 13, 14；§4.1 Tables4–5。
- **C-B17-037**：机动间隔数天包含等待导航验证、地面站冲突和运行安排；参数修正仍由团队离线分析完成。
  原文定位：PDF物理页14, 16；§4.1 spacing; §5.1 monitoring and refinement。
- **C-B17-038**：首个受控交叉的径法向最小分离约1.8 km；TLE沿轨位置误差可到1.5 km，径/法向误差小于0.25 km，安全结论依赖几何裕度。
  原文定位：PDF物理页19, 22, 24；§5.2.1; Figs.24,27–28。
- **C-B17-039**：ADM核心逻辑通常30 min执行，导航传播可500 ms更新，但TLE实际新信息仅每日4–5次，频率不能混为一谈。
  原文定位：PDF物理页26；§6 timing and navigation paragraphs。
- **C-B17-040**：ADM沿轨约80 km实验含0.8/1.6 km滞环、电压15.5/15.9 V阈值；图37说明PCU事件导致实验停止。
  原文定位：PDF物理页28, 29；Table10; Fig.37; activation label conflict retained。
- **C-B17-041**：现有ADM调节阻力与计划的自主安全近距交叉不同，后者需进一步验证；图36明确是计划逻辑。
  原文定位：PDF物理页26, 27, 28；§6; Fig.36 caption。

## 适用边界与待核问题

- 双星具体构型、误差方向性和安全裕度决定TLE可用性；不能写成TLE普遍替代GNSS，尤其米级交会。
- 所述近距交叉主要由地面组织；图20/36标注planned，完整推进/阻力联合AFF尚未在该文验证。
- 正文§6说明相对经度激活，而表10激活项为Drift，表文差异保留；采用时只引用可确认的阈值和实验区间。
- 法向收缩只达预期400 m的约72%，执行误差成因尚未完全分离。
- 数据声明“未产生/分析数据”与遥测分析叙述口径待作者澄清；未提供可复算遥测，不构造独立验证主张。

## 对综述的作用

可重点用于3.6.1维护、3.6.3避碰恢复和工程约束段，说明采用更新需要等待信息、复核执行效果、满足姿态电量窗口。适合作为仿真方法的现实约束对照，不当作千星自主协同已实现的证据。

以上采用建议为阅读者分析，尚未写入v3.2。完成阅读、文件核查与科学正确性确认是不同事项。
