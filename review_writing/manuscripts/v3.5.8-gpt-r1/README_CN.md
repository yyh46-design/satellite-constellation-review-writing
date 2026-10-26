# GPT_R1 与 V3.5.9 整合交接

日期：2026-10-26。此目录提供 GPT 独立精修稿及两稿比较结论，供 Codex 实际整合。GPT_R1 正文与上一轮交付版本逐字节相同；比较中发现的问题保留在原稿内，由本轮整合统一修正。

## 阅读入口

1. [Codex 整合任务](CODEX_INTEGRATION_PROMPT_CN.md)：执行范围、输入、必要修改及交付要求。
2. [两稿比较与合并方案](COMPARISON_AND_MERGE_PLAN_CN.md)：各小节取舍及具体句子。
3. [GPT_R1 完整正文](REVIEW_CN_v3.5.8_GPT_R1.md)：完整中英文摘要、五章、9张表及120条书目，四张原图位于 assets/。
4. [来源标识](SOURCE_MANIFEST.json)：固定基准及正文、图件身份。

## 三份输入

- 共同基准 V3.5.8：提交 `d408fd5b657b04278dac0d6b3965d1b517cb8341`，正文 `review_writing/manuscripts/v3.5.8-cn/REVIEW_CN_v3.5.8.md`。
- Codex V3.5.9：提交 `1604e8ac3932019a207d3396e8d447e871b7686c`，正文 `review_writing/manuscripts/v3.5.9-cn/REVIEW_CN_v3.5.9.md`；来源状态及未关闭事项见该版本 `SCIENTIFIC_REVISION_CN.md` 与既有登记。
- GPT_R1：本目录正文；SHA-256 为 `98e2618fa434bbe203c5ec593c3e9ce8cd516f86565c1b9c51049abcb3248c8c`。

交接分支以 V3.5.9 的固定提交为父提交，包含上述历史材料。GPT_R1 是独立语言候选，尚未整合为新的正式中文版本。两稿均不具有高于原研究及已登记证据的科学优先权。

## 当前状态

中文正文仍待作者确认冻结；来源状态、既有 HOLD 和未关闭事项不升级，`human_verified=false`、`submission_ready=false`。本目录发布的是稿件与整合要求，没有完成 Codex 合稿，也没有新增来源、全文精读或实验。

本次交接仅新增独立目录及分支，供后续从 V3.5.9 继续版本演进。
