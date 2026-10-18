# Codex：归档v2.6引用全文，并复核版本身份

对象仅为本版95条引用：85篇学术来源、10项工程资料。先读 `REVIEW_CN_v2.6.md`、`references/REFERENCE_NUMBER_MAP.csv`、`references/REFERENCE_INDEX.csv` 和 `SUBMISSION_OPEN_ITEMS_CN.md`。历史编号、v2.5编号及v2.6编号用稳定E编号连接，不按数字猜来源。历史旧[68]为E068，本版[59]。

先复用用户电脑已有PDF/HTML，再用台账中历史阅读地址和DOI寻找合法全文。固定证据快照为仓库 `yyh46-design/satellite-constellation-review-writing` 的 `40173aaacd435a10357598868340a57b360f572e`，内有v2.3 SOURCE_MANIFEST及阅读批次原记录，E068在B02中。会话完整包另有95项完整JSON、历史哈希及只读URL展开脚本。

按E编号建本地目录。每份记录本版编号、标题/作者/DOI、实际版本、来源URL、取得日期、页数、首末页、正文完整性、本机路径及SHA256。所读作者稿保留；后取得正式版另存。完整HTML须保留正文和必要图式，不把摘要、验证码、付费提示或下载按钮算全文。

生成 LOCAL_SOURCE_INVENTORY.json/csv（95项均有去向）、ARCHIVE_SUCCESSES_CN.md、ARCHIVE_FAILURES_CN.md、VERSION_DIFFERENCES_TO_REVIEW.md。将“已在本地”“本次新保存”“仅HTML”“版本待核”“失败”“缺图式”分别记录。历史阅读状态和本机归档状态分开；下载不增加精读数。

本轮不继续搜索历史24篇缺口，不改本文题目/正文/引用，不合并main。使用正常开放来源或用户已有合法订阅，不规避访问控制、不发送作者邮件；第三方全文仅在本机保存，不上传无再分发许可的全文。向GitHub提交原创台账和哈希需保持独立研究分支；中文科学终核留给作者。

结构复核可运行 `python tools/verify_v26.py --root .`，它只查编号、图件和追溯标识，不宣告论文内容正确或CJA投稿合格。
