# 官方资料记录

查询日期：2026-10-03（Asia/Shanghai）

## 已打开的官方资料

4. ASD Simplified Technical English Maintenance Group，`ASD-STE100 Simplified Technical English` 与 FAQ：
   https://www.asd-ste100.org/FAQ.html
   https://www.asd-ste100.org/about_STE.html
   - ASD-STE100 是用于技术文档的受控自然语言标准；2025 年 Issue 9 标志其从 specification 转为 international standard。
   - 它包含写作规则与受控词汇，目标是减少技术文档歧义；它不是通用 AI 提示词，也不能替代任务背景、目标、权限和验收条件。
   - 正文只把它作为“写作约束”的案例，避免声称 AI 可以凭一句提示词自动满足完整标准。

1. OpenAI Developers，`Mastering remote engineering work from your phone`：
   https://developers.openai.com/blog/mastering-codex-remote-for-engineering
   - Remote 开始任务前可选择 connected host、workspace、branch/worktree 和环境设置。
   - Queue 会等待当前响应完成，Steer 会把指导注入进行中的工作。
   - Plan mode 用于改代码前提出实施路径；Goal 用于持续追踪结果；官方给出的理解是 Plan 回答“如何接近”，Goal 回答“完成时必须成立什么”。
   - 需要在正文核实：文章引用的是开发者博客中的工作方式，具体入口和可用性可能受版本、主机和账户影响。

2. OpenAI Help Center，`ChatGPT Work and Codex`：
   https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
   - Codex 专注软件开发和技术工作；可处理代码、测试、命令、变更审阅和仓库。
   - Codex 在桌面端是独立视图；可使用本地文件夹、仓库、终端和开发工具。
   - Codex Cloud 在 OpenAI 管理的计算机上运行；Remote 访问正在用户自己电脑上运行的桌面任务，两者不同。
   - Project、Chat、Work 的关系主要由 ChatGPT Project 语境说明；需要结合 Codex 专门页面继续核查，避免把 ChatGPT Project 当作 Codex workspace。

3. OpenAI Help Center，`Using Codex with your ChatGPT plan`：
   https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
   - CLI、Cloud、worktree、权限与企业工作区控制等功能会受版本、计划、工作区和权限影响。
   - Cloud 任务可在电脑休眠时继续，但本地电脑上的 Remote 仍依赖该电脑及其访问设置。

4. OpenAI Help Center，`ChatGPT Work and Codex`：
   https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
   - Codex 桌面端支持 Voice；使用电脑上下文可能需要麦克风、屏幕与音频录制、Accessibility 权限。
   - Voice、屏幕/音频录制权限、Record & Replay、普通视频录制和生成式视频是不同能力，正文不能合并称作“录制功能”。

5. OpenAI Help Center，`Using Codex with your ChatGPT plan`（Record & Replay 段落）：
   https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
   - Record & Replay 可在 ChatGPT 桌面端使用 Codex 时，把一次可重复的电脑操作转成可复用 skill；需要 Computer Use 可用并启用。
   - 录制应避免输入密钥或敏感信息；地区、计划和版本限制必须注明查询日期。

6. OpenAI Developers，`Skills`：
   https://developers.openai.com/api/docs/guides/tools-skills
   - Skill 是包含 `SKILL.md` 和可选 references、scripts、assets 的可复用指令与资源目录；官方强调渐进披露、版本管理和使用前安全审查。
   - Skill 可以影响规划、工具使用和命令执行，网络环境下存在提示注入和数据外泄风险；正文要把 Skill 写成可审查的工作流组件，不是“魔法提示词”。

7. OpenAI Developers，`Agents API Architecture` 与 `Agents`：
   https://developers.openai.com/api/docs/guides/agents-api/architecture
   https://developers.openai.com/api/docs/guides/agents
   - Harness 是运行模型与工具循环、维护 agent session 的运行时；Environment 负责文件、命令和计算；Application server 负责连接、事件和函数工具。
   - 这是 Agents API 的架构概念，不能直接等同于桌面 Codex 的工作区或某个社区插件。

8. OpenAI Developers，`Rethinking skills and prompts for GPT-6 Astra`：
   https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
   - Skill、`AGENTS.md` 和 task prompt 都会影响代理行为；Skill 描述过长、互相冲突或数量过多会增加上下文负担，官方建议短描述和渐进披露。

9. Jev/JevHarness（社区项目，非 OpenAI 官方产品）：
   https://github.com/TianyuCodings/JevHarness
   - 目前将 JevHarness 描述为帮助 Codex/Claude Code 构建任务专用、可评估的决策流水线和 Harness 的社区 skill；其来源、依赖、凭证和评估证据必须独立核查。
   - 正文只有在确认用户所说的“jev”就是这一类 Jev/TypeSafe 决策组件后，才使用具体名称；否则写成“新兴决策层工作流”。

## 待继续核查

- Codex 桌面端当前对 workspace、project、task/chat/thread 的官方定义和中文界面称呼。
- Codex Cloud 环境的创建、发布、仓库连接、网络与凭证边界。
- Plan mode 与 Goal 的当前入口、可用版本、停止条件和用户可见状态。
- 面向零基础游戏项目的官方推荐流程是否有新的 Codex CLI/桌面指南；若没有，正文明确哪些是编辑设计的示例流程。
- “ASD-STE100 提示词”这一说法的实际来源、是否指某个社区 skill 或工作流模板；官方标准与社区提示词模板分开记录。
- “jev”是否指 Jev/TypeSafe 决策模型、JevHarness，或用户提到的其他新工具；在得到确认前不把社区项目写成 Codex 内置能力。
- Harness 是指 OpenAI Agents API 的官方运行时概念，还是社区的任务专用 Harness；两者分开写。
- 具体 App 平台与游戏技术栈：选取一个不引入不必要部署复杂度的 2D 示例，并把平台/引擎选择写成案例假设而非官方推荐。

## 事实口径

未完成上述核查前，不在正文断言具体版本号、套餐、限额、中文按钮名称或所有账户都可用。案例中的阶段划分、提示模板和验收标准属于编辑设计，须与官方产品能力分开标注。
