# 第三篇研究来源记录

查询日期：2026-10-14。

## GitHub

- GitHub Docs，Hello World：https://docs.github.com/en/get-started/using-github/hello-world
- 用于核对仓库、分支、提交和协作入口的基本概念。正文采用解释性概括，不把 GitHub 功能写成所有项目的必选流程。

## MCP

- Model Context Protocol，What is MCP：https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- 用于核对 MCP 作为连接模型与外部数据、工具的开放协议定位。正文只说明能力边界，不把第三方服务器默认视为可信。

## TypeSafe / Jev

- TypeSafe 文档索引：https://docs.typesafe.ai/llms.txt
- TypeSafe 文档说明 Jev 是其 System One 模型，接收状态和结构化问题，返回代码可以使用的结构化判断。
- JevHarness 社区项目：https://github.com/TianyuCodings/JevHarness
- JevHarness README 用于了解任务专用 Harness、Jev 判断、执行轨迹和可选反思的组合方式。它是外部社区项目，不是 Codex 内置能力；正文不把其示例结果外推为普遍性能。

## 编辑边界

- GitHub、Skills、MCP、Harness 和 Jev 的关系按“保存、复用、连接、组织执行、局部决策”的编辑框架组织，不声称它们组成唯一技术路线。
- 手机小游戏、公众号流程和旅行网站均为编辑示例。
- 未在本轮执行 JevHarness、TypeSafe API、MCP 服务器或 GitHub Actions；正文不声称完成实际性能或兼容性验证。


## v2 补充核查（2026-10-14）

- https://learn.chatgpt.com/docs/extend/mcp?surface=cli ：读取连接配置、桌面设置、CLI 配置和工具权限相关段落。新文档将桌面入口称为 ChatGPT desktop app；正文提示客户端入口以当前界面为准，未声称检查用户设置页。
- https://developers.openai.com/learn/docs-mcp ：读取 Quickstart，核对公开服务端点、codex mcp add 与 list。未实际安装此服务。
- https://learn.chatgpt.com/docs/build-skills ：读取目录结构与调用机制；SKILL.md 需要名称与描述，其余目录可选。
- https://developers.openai.com/api/docs/guides/agents-api/architecture ：架构参考，不将 API 与 Codex 桌面环境等同。Harness 目录和循环为编辑示意，不是官方文件规范。
- 用户级 MCP 配置仅作脱敏状态检查；本会话 Node REPL 完成无副作用工具调用。详情见 review-v2.md；没有归档用户配置和认证信息。

## v4 补充来源（2026-10-14）

- https://git-scm.com/docs/git-worktree ：成功读取DESCRIPTION，复核一个仓库支持多个工作目录及不同分支同时检出；修正前轮缺失连字符的不可访问地址。
- https://docs.npmjs.com/cli/v11/commands/npm-ci/ ：读取Description，核对锁文件要求和清洁安装语义。正文命令仅作具有对应脚本的Node.js项目示例。
- https://docs.typesafe.ai/confidence ：复核概率与置信度语义、阈值按项目数据验证；分类不证明因果，行动授权须独立。
- MCP与AGENTS.md说明沿用前轮已读取官方资料，本文不增加新的配置接口。
