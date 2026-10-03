# 第一篇官方资料与事实台账

查询日期：2026-10-03（Asia/Shanghai）

## 已核查资料

1. OpenAI Help Center，`ChatGPT Work and Codex`：
   https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
   - Codex 专注软件开发和技术工作，可处理代码、测试、命令、变更审阅和仓库。
   - 桌面端 Codex 是独立视图，可使用本地文件夹、仓库、终端和开发工具。
   - Codex Cloud 在 OpenAI 管理的计算机上运行；Remote 访问用户自己电脑上运行的桌面任务，两者不同。
   - Voice 在桌面端 Work/Codex 可用时，可能需要麦克风、屏幕与音频录制和 Accessibility 权限。

2. OpenAI Help Center，`Using Codex with your ChatGPT plan`：
   https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
   - Codex CLI、Cloud、worktree 和工作区控制会受版本、计划和权限影响。
   - Cloud 任务可在电脑休眠时继续；本地电脑上的 Remote 仍依赖该电脑和访问设置。
   - Record & Replay 可把一次可重复的电脑操作转成可复用 skill；需要 Computer Use 可用并启用，录制时不能输入密钥或敏感资料。

3. OpenAI Developers，`Mastering remote engineering work from your phone`：
   https://developers.openai.com/blog/mastering-codex-remote-for-engineering
   - Remote 开始任务前可以选择连接的主机、工作区、分支/worktree 和环境设置。
   - Queue 等待当前响应完成，Steer 向正在进行的工作注入指导。
   - Plan 用于提出实施路径，Goal 用于持续追踪结果；具体入口和可用性可能受主机、版本和账户影响。

4. OpenAI Developers，`Using Goals in Codex`：
   https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
   - Goal 是线程范围内的持续目标，不是全局记忆或项目级规则。
   - 合适的 Goal 应包含结果、验证面、约束、边界、迭代策略和受阻停止条件。

## 正文口径

- 本文解释产品关系和工作方法，不写死会快速变化的具体模型、套餐、限额和中文按钮名称。
- “工作区、项目、任务、对话”在不同产品表面可能有不同界面呈现；正文使用功能关系解释，并在最终核查时补充当前 UI 术语。
- “Record & Replay”只说明其功能定位和安全边界，不把普通录屏、会议录音和生成式视频合并成同一能力。
- Skills、MCP、Plugins、Harness 只在本篇建立层级地图，具体配置移到第三篇。
