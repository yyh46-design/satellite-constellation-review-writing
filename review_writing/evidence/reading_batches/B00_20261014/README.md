# 星座管理综述 B00：原文获取与版本核验

执行日期：2026-10-14（Asia/Shanghai）。仓库：`yyh46-design/satellite-constellation-review-writing`。冻结提交：`51be6a1326e8c615ea24f80f1887f16a2e7b02fc`。独立分支：`research/constellation-review-reading-b00-20261014`。**只做来源准备与版本身份审计；B01/B02未启动、正文未修改、新增全文精读完成0篇。**

## 结果及统计口径

13篇全部核对了DOI书目、出版社/公开原文入口、作者机构或arXiv线索及当前工作区既有PDF。取得6个来源的7份有效PDF：[42][44][53][74][76][121]；[121]同时有arXiv v1与NRC接受稿。所有有效PDF记录实际页数、字节大小、SHA256与全页提取状态。首次三份arXiv传输不完整，解析失败，不计下载成功；后续正常完整传输已另留记录。

|严格身份/访问状态|来源数|编号|
|---|---:|---|
|已确认正式全文（VOR）|0|无|
|作者侧完整原文PDF|6|42、44、53、74、76、121|
|仅摘要/有限章节片段|5|75、77、79、80、112|
|出版社提供全文文字层，但PDF版本与原页未确认|2|73、107|
|连书目/摘要均完全无法访问|0|无|
|合计|13|按最佳实际访问状态互斥统计|

必须单列[73][107]：公开文字页注明全文由MDPI提供，全文文字展示并非仅摘要；但下载链接失败、提取存在水印/符号问题，本轮没有取得其正式PDF，不能直接计入“已确认正式全文”。因此不强迫四个粗类别之和等于13，也不把两篇降成“仅摘要”。正式PDF取得数为0；作者稿不是VOR；DOI/机构封面标签不能证明最终正式版。

|来源|当前最高可用材料|仍缺什么|
|---|---|---|
|[42]|作者稿/工作论文，15页|正式版对照未齐|
|[44]|作者稿/工作论文，31页|正式版对照未齐|
|[53]|作者稿/工作论文，25页|正式版对照未齐|
|[73]|出版社全文文字层，PDF待核|原PDF页面未齐|
|[74]|作者稿/工作论文，14页|正式版对照未齐|
|[75]|仅摘要/章节片段|完整正文未齐|
|[76]|作者稿/工作论文，13页|正式版对照未齐|
|[77]|仅摘要/章节片段|完整正文未齐|
|[79]|仅摘要/章节片段|完整正文未齐|
|[80]|仅摘要/章节片段|完整正文未齐|
|[107]|出版社全文文字层，PDF待核|原PDF页面未齐|
|[112]|仅摘要/章节片段|完整正文未齐|
|[121]|作者稿/工作论文，17页|正式版对照未齐|

## 版本审计发现

- [42]Toronto公开PDF15页，无最终刊号/分页或直接接受声明；历史Round4曾称接受稿，本轮仅确认作者稿身份。
- [44]CIRRELT-2024-28为2024年机构工作论文，31页含封面；2025正式期刊元数据可核，正式正文仍未取得。
- [53][74][76][121]arXiv提交史均仅显示v1。[53]稿面日期2026-04-08与提交日2026-04-07分别保留；[76]真实提交日为2024-10-29，不从编号2411推日期。
- [74]预印本有占位卷期/DOI。公开出版社元数据给1-14，但历史226-239冲突仍缺PDF或直接卷目录终核。[53]当前Crossref没有1-22分页，本轮不新增确认。
- [121]NRC接受稿18页含机构封面，论文17页。封面有Publisher版本标签、正式DOI；实际论文页却明确作者接受版且未完全编辑，故不计VOR。两份作者文件可在后续授权后比较，正式版差异仍不可关闭。
- [107]公开文字展示含正式页眉和旧FOR PEER REVIEW水印；继续保留页面/符号问题，不将混排直接判为论文错误。

## 正文依赖与交付

[CLAIM_DEPENDENCY_MAP.csv](CLAIM_DEPENDENCY_MAP.csv)记录57处显式引文、56个来源—正文块组合，涵盖段落、表3/4/6及图2，带冻结正文哈希与实际行定位。每条命题均为v1.9既有依赖，B00支持判定全部unverified，不是本轮新精读结果。[42]在L123/p322a2还有显式引文，旧轻量索引遗漏，本轮只在新增映射补记。

- [SOURCE_ACCESS_REGISTER.csv](SOURCE_ACCESS_REGISTER.csv)：13篇总表，英文原标题及本轮中文译名、DOI、作者、出版信息、版本、URL、主文件哈希/页数、缺口。
- [SOURCE_ACCESS_DETAILS.json](SOURCE_ACCESS_DETAILS.json)：逐篇结构化详情及继承定位，作者/正式版身份边界。
- [VERSION_COMPARISON_QUEUE.json](VERSION_COMPARISON_QUEUE.json)：六篇正式版对照队列，当前0/6对材料齐备；另记[121]作者侧双版本。
- [UNAVAILABLE_AND_BLOCKERS.md](UNAVAILABLE_AND_BLOCKERS.md)：全部失败入口、具体未取得材料与历史27项未关闭清单。
- [B01_B02_READINESS.md](B01_B02_READINESS.md)：六篇作者侧可核读子集、正式对照和全文/PDF页面HOLD范围。
- [LOCAL_PDF_INVENTORY.json](LOCAL_PDF_INVENTORY.json)：本机7份有效PDF的页数、字节、SHA256及提取/身份首页检查范围；不含论文正文。
- [ACCESS_ATTEMPTS.json](ACCESS_ATTEMPTS.json)、[WEB_ACCESS_OBSERVATIONS.json](WEB_ACCESS_OBSERVATIONS.json)：普通访问的成功、403/418/429/404、超时和不完整传输记录。
- [FROZEN_INPUTS.json](FROZEN_INPUTS.json)、[DEPENDENCY_MAP_AUDIT.json](DEPENDENCY_MAP_AUDIT.json)：冻结原始Git blob哈希与映射审计。
- [SHA256_MANIFEST.json](SHA256_MANIFEST.json)：发布路径与逐文件SHA256；自文件列入路径清单但不递归自哈希，外部发布回执另核其SHA256。

第三方PDF、提取文字及身份页面图片仅在本机独立目录 `D:\SKT727\materials\constellation_review_B00_20261014`，不上传GitHub。不默认授权后续B01/B02。所有human_verified=false；正式版一致性完成0/6，核心实际页检查未完成；冻结E/S关口仍HOLD。历史正文、编号、阅读总账和27项记录不改。

## Git发布核对方式

只提交本目录新文件，从冻结提交派生，不创建PR或合并。发布后以Git远端分支ref读取commit，再fetch该commit读取tree；与本地commit/tree逐一比较。发布文件集合必须等于SHA256_MANIFEST.publication_paths，逐blob字节核对哈希，冻结提交到新commit的所有diff路径必须限于本目录且全部为A。commit/tree及清单自身SHA256保存于本机发布回执，并在执行结束的报告给出，避免把当前commit/tree写回自身产生循环。

**停止点：完成B00来源准备与Git发布校验后停止。**
