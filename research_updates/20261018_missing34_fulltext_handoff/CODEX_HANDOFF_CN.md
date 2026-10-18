# Codex：历史34篇合法获取与两批定向精读（2026-10-18）

## 任务基线与范围

仓库 `yyh46-design/satellite-constellation-review-writing`。阅读本目录 `README_CN.md`、`FULLTEXT_ACCESS_LEDGER.csv`、`READING_CARD_OLD068_CN.md`、`SCIENTIFIC_EVIDENCE_POLICY_CN.md`，以及原提交 `6b096b694cb7d9af17026cae88ca5a42c48aab18` 的 `REFERENCE_NUMBER_MAP.csv`、`SOURCE_MANIFEST_v2.3.json`、`SUBMISSION_OPEN_ITEMS_CN.md`。只处理历史34篇缺口；编号为旧[ ]，切忌与当前94条新编号混淆。

**严格边界**：正常合法访问出版社OA、机构库、作者稿、合法的用户机构订阅或文献传递；不得规避登录/付费墙/CAPTCHA；不得以请求PDF页面、搜索引擎摘要、学位论文、会议slides或代码替换目标文献；不发送作者邮件、不在公开GitHub上传受版权保护的第三方全文；每份取得的文件在本机私有资料目录保存SHA256、页数及版本证据。精读记录可提交GitHub，论文全文通常不上传。

## 第一批：优先尝试的10个编号

- **立即可读**：旧[68] 官方正式PDF：`https://iris.polito.it/retrieve/96bbb20b-93c0-4695-b08b-998f363c3a8f/1-s2.0-S1000936125003802-main.pdf`。校验期刊首页和结尾，图、表和式号；网页已有初读卡，请独立确认。
- **出版社公开但下载待验**：旧[77] SciOpen `https://www.sciopen.com/article/10.1016/j.cja.2024.09.039`；旧[80] `https://www.sciencedirect.com/science/article/pii/S2352864822001973`（另查 `https://journal.hep.com.cn/dcn/EN/10.1016/j.dcan.2022.09.022`）。
- **需版本配对**：旧[90] 2006会议同名作者文本 vs 2008期刊 DOI `10.2514/1.29590`，作者目录 `https://acl.mit.edu/publications/`；不可先验假定同版本。
- **同题作者稿/开放稿入口**：旧[33] SSRN 5202348（第一作者UFSC96页学位论文是不同工件）；旧[55] SSRN 4611047；旧[60] SSRN 2495339（不是2634920）；旧[83] 出版社View Open Manuscript；旧[94] SSRN 5561401；旧[112] SSRN 5247404。对每个先核实际完整PDF首页、末页和表图后再变更状态。

如无法用当前工具下载，可在用户已授权的Windows浏览器/学校订阅渠道获取，必须留下成功或失败记录；**不能把URL记为FULLTEXT_ACQUIRED**。

## 第二批：其余24篇及已用文献正式版配对

按优先级筛查旧[32][38][43][45][59][31][40][63][64][67][75][79][100][103][104][110][118]，其余按相近程度继续。优先找作者机构接受稿和合法学位论文辅助材料，但同题文章的正式获取状态分别记录。已读文献[16][17][47][59][60][12]六组正式版本对照另设专门队列，**不得记入34篇的获取成功数量**。

## 每篇精读记录（必须字段）

- identity：旧编号、DOI、原始标题/作者/出版物；确切文件版本、URL、下载日期、本机路径、SHA256、PDF页数、正文起止页。
- access status：`ENTRY_LOCATED`、`FULLTEXT_ACQUIRED`、`TARGETED_READ`、`VERSION_PARITY`、`HUMAN_ACCEPTED`各自单独字段。
- science：研究对象与适用轨道、决策时域、可改变量、输入/状态权限、目标及**真实业务完成定义**、物理与算法假设、约束、求解方法的真实机制、实验设计及对照、硬件与CPU/训练/预计算/在线时间口径、失败或未完成样本、复现实验限制。
- trace：逐项对应页号、公式、图、表；哪些具体综述命题获得支持、哪部分为作者推论、与现稿已有研究重复与否、哪些结果不能推广。
- verification：阅读全文及图页不等于独立复现；作者稿和正式版未经逐项一致性核对不得标记`VERSION_PARITY=true`。人工终核须由作者显式确认。

## 两批交付与科学闸门

每一批生成：`FULLTEXT_ACQUISITION_RECEIPTS.json`、`TARGETED_READING_CARDS_CN.md`、`VERSION_PARITY_NOTES.md`、`FAILED_ACCESS_LOG.csv`、`CLAIM_EVIDENCE_PROPOSALS.csv`、`BATCH_SUMMARY_CN.md`。请逐项统计：34篇中真正取得了多少份目标论文全文、同题作者稿有多少、相关但非目标版本有多少、仅入口多少、失败多少、定向核读多少、正式配对多少。禁止把学位论文算入目标期刊篇数。

不要改v2.3/v2.4正文、图、表、正式参考文献，不合并main；先发布独立研究分支、远端commit/tree与文件SHA校验并返回中文结果，供网页版GPT从科学内容判断是否恢复引用。
