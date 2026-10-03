# 版本说明

## 2026-10-03

- 建立专题目录 `articles/2026-10-codex-guide/`。
- 完成 `brief.md`：记录文章目标、范围、标题候选、术语待核对项与来源原则。
- 完成 `outline.md`：提交候选写作逻辑与章节大纲，主线为“从一句游戏想法到可运行、可测试、可打包的 App 项目”。
- 完成 `research/official-sources.md`：归档已打开的 OpenAI 官方资料、查询日期和待核查问题。
- 当前状态：候选标题、候选大纲，等待用户审核；未开始纯文字稿、HTML、配图或发表。

## 2026-10-03（系列拆分）

- 根据用户反馈，将单篇策划扩展为四篇系列。
- 新增 `series-outline-v1.md`，按“产品地图 → 提示词与协同 → 身份化工作流 → 端到端项目”拆分。
- 更新 `brief.md`，补充系列主题、适用身份、模型/工具边界和“HiGen”待核查项。
- 新增 `research/coverage-matrix.md`，记录四篇共同的事实核查范围。

## 2026-10-03（能力缺口审计）

- 根据用户反馈重新检查四篇系列，补充 Voice、屏幕/电脑上下文、Record & Replay、Browser/Computer Use、Skills/Plugins、Memory、Scheduled Tasks、Git/review/rollback、多代理、数据隐私、用量与失败恢复。
- 将“录制”拆分为 Record & Replay、普通录屏、会议录音、视频素材采集和工作日志，避免混用。
- 更新 `series-outline-v1.md`、`research/coverage-matrix.md` 和 `research/official-sources.md`。

## 2026-10-03（Skills、Harness 与 Jev 补充）

- 将 Skills、MCP、Harness、Jev/决策层工作流加入系列能力模型。
- 区分一次性提示词、可复用 Skill、工具/MCP、Harness 运行时和外部/社区决策组件。
- 补充官方 Skills 安全与渐进披露要求，并记录 JevHarness 为社区项目，避免将其写成 Codex 内置功能。

## 2026-10-03（四篇扩展为六篇）

- 将系列从四篇扩展为六篇，新增独立的工作流组件篇，以及 GitHub、腾讯云/阿里云、网站、域名、DNS、HTTPS 和 URL 上线篇。
- 新增 `series-outline-v2.md` 和 `research/current-audit-v2.md`。
- 第六篇保留完整游戏/App 贯穿案例，用于串联前五篇，不再让云服务、网站发布和 Codex 基础地图互相挤占篇幅。

## 2026-10-03（第五篇重构）

- 根据用户反馈，取消按“GitHub、云服务、网站和网址”并列罗列的结构。
- 第五篇改按“构建 → 发布 → 运行 → 数据 → 网络 → 用户 → 观测 → 安全 → 成本 → 持续运营”的生命周期组织。
- GitHub、腾讯云、阿里云、网站、域名、DNS、HTTPS、URL 和 API 地址改为各层的实例与服务提供者。
- 更新 `series-outline-v2.md`、`brief.md`、`research/coverage-matrix.md` 和 `research/current-audit-v2.md`。

## 2026-10-03（六篇顺序重排）

- 根据用户反馈，重排六篇的主线，不再把“基础设施篇”和“完整案例篇”并列成重复教程。
- 新顺序改为：认识系统 → 提出任务 → 建立项目 → 推进项目 → 交付产品 → 长期运营。
- GitHub、网站、云服务和提示词各自只在首次成为当前问题的篇目中完整解释，其他篇目只复用。
- 新增 `series-outline-v3.md` 和 `research/sequence-audit-v3.md`；v2 保留为历史方案。

## 2026-10-03（第一篇纯文字拟稿）

- 按六篇 v3 顺序建立 `part-1/outline.md`、`part-1/article-v1.md` 和 `part-1/research/official-sources.md`。
- 完成第一篇框架与纯文字 Markdown 拟稿，主线为“一个小白第一次开始长期工作时，先判断工作在哪里、谁能操作什么、怎样让任务继续”。
- 当前状态：纯文字拟稿 v1，待用户审核；未制作 HTML、配图或发布稿。

## 2026-10-03（第一篇全文重写）

- 用户指出 v1 过于像产品说明书，阅读不顺，要求参照 Chat 版本的叙事推进。
- 新增 `part-1/article-v2.md`，从“第一次打开 Codex 的误解”开篇，改用连续问题、具体例子和工作现场主线重写全文。
- v1 保留作历史稿；v2 为当前待审纯文字稿，未制作 HTML、配图或发布稿。
