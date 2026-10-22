# 第四篇大纲：依据与来源边界

查询日期：2026-10-22。状态：为候选大纲作范围核查，未执行文章中的游戏示例，未实测多代理、钩子或回放。

## 仓库依据

- origin/main 在查询时为 1d40ce4；执行 git fetch origin 成功。
- series-outline-v3.md：六篇最新编号总框架。
- series-placement-v1.md：2026-10-07 补充分工，明确独立上下文、钩子与实际状态更新属于第四篇。
- part-2/article-v12.md 及 brief.md 最新补充：第二篇已负责理解问题、评估、协同模式和工作流形成；不强制一个项目贯穿全文。
- part-3/brief.md、article-v9.md：2026-10-16 用户稿为第三篇当前版本；结尾预告第四篇展示任务执行与验证。
- 上述系列框架、分工表和第三篇 v9 与 origin/main 无差异。本地其他未提交修改不纳入本轮提交。

## 当前官方资料

1. Subagents：https://learn.chatgpt.com/docs/agent-configuration/subagents
   - 从 https://developers.openai.com/codex/subagents 打开后重定向到此页，读取上下文管理相关段落。
   - 用于核对独立上下文与中间输出管理的解释；不据此承诺每种界面、账户均提供相同入口。
2. Code review：https://learn.chatgpt.com/docs/code-review?surface=app
   - 从 https://developers.openai.com/codex/app/review 打开后重定向到此页，读取变更审阅、提问和请求证据的段落。
   - 支持围绕预期行为、最新差异和实际测试核查意见；不把 AI 审阅等同于验收与合并。
3. Hooks：https://learn.chatgpt.com/docs/hooks
   - 从 https://developers.openai.com/codex/hooks 打开后重定向到此页，读取事件匹配、工具覆盖与执行边界相关段落。
   - 当前文档列出调用前后事件，并明确部分工具路径不覆盖。正式配置前需核对实际运行环境、信任与事件语义，不在大纲复制完整配置。
4. Iterating Development Workflows with Codex：https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex
   - 打开官方示例，作为后续工作流整理研究入口；未运行示例，不作为本轮效果验证。
5. Custom Code Review rules for Codex：https://developers.openai.com/blog/custom-code-review-rules-for-codex
   - 打开官方文章，作为项目审阅标准的研究入口；不沿用其中数字或宣称自定义规则保证发现问题。

## 编辑判断与事实的区分

七节顺序、候选标题、小游戏重开问题、篇幅建议与证据组织方式均为编辑建议，不是官方标准。游戏问题目前只是示例设计；录像、截图、浏览器测试和真实设备测试的区别是写作中应保留的验证边界。

本轮未核定视频生成、Record & Replay 的具体产品入口，不写可用性断言；未调用发布接口。
