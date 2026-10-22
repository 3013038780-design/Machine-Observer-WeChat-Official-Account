# 第四篇 v2：机制与合作建议的来源边界

查询日期：2026-10-22。仅作大纲范围核查；未进行任务对照实验或文件制作实测。

## 本轮重新打开的官方来源

1. https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
   - 官方长任务示例，执行循环段落说明计划、编辑、调用工具、观察、修复、更新状态与继续。
   - 仅作为公开执行机制的来源，不把单个长任务案例泛化成所有工作的成功保证；不使用案例时长作为本篇效率证据。
2. https://developers.openai.com/plugins/guides/optimize-metadata
   - 工具描述与元数据影响工具发现、选择和调用。
   - 不能据此断言某次遗漏唯一是元数据造成；本文 gap 分类是编辑诊断框架。
3. https://learn.chatgpt.com/docs/artifacts-viewer?surface=app
   - 当前文件工作说明涉及文档、演示文稿、电子表格、PDF 和 HTML 的创建、预览、修订及环境差别。
   - 不能把 ChatGPT Work 的入口套到每个 Codex 环境，也不能据支持格式证明质量相同。
4. https://learn.chatgpt.com/docs/agent-configuration/subagents
   - 说明独立上下文及中间输出管理的用途。
   - 不将子代理上下文与独立事实来源混同，不保证并行一定提高端到端效率。

## 本次讨论中已打开、后续拟稿可继续核查的官方来源

- https://developers.openai.com/api/docs/guides/tools-shell ：命令与输出/执行结果的工具循环；API 工具文档不等于所有桌面设置相同。
- https://learn.chatgpt.com/docs/agent-approvals-security ：权限与审批边界，不能将缺少主动判断等同于缺授权。
- https://learn.chatgpt.com/docs/code-review?surface=app ：将审阅意见与预期行为、最新变更及测试证据对照。
- https://learn.chatgpt.com/docs/hooks ：事件触发与覆盖限制，钩子不是完整的权限边界。

## 仍需研究或实作的事项

- 不对中文与英文、MD/HTML 与 Office 的总体表现作能力排名；如需性能主张，必须有可比任务与明确评价标准。
- 文本可读写、检索、比对及脚本生成，是工作路径的解释；具体文件流程需按所用工具核对。格式转换可能丢信息。
- 尚未确认用户提及的抓取产品具体名称，不写安装步骤或必要性结论。
- 模型怎样生成判断只解释到公开机制与可观察行为；不声称获得完整内部推理，也不凭模型自述诊断单次遗漏的真实原因。
- “总交付时间包含人的提醒、审阅与返工”是本文编辑评价口径，本轮未计时，不给量化收益。
- 待正式写作前选择小样本记录实际输入、工具动作、结果和文件检查；不得把构造的教学示例标成实测。
