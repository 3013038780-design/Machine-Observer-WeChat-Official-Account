# 工具请求与执行：v11 补核

查询日期：2026-10-22。

来源：[OpenAI Function calling](https://developers.openai.com/api/docs/guides/function-calling)。官方文档将工具调用解释为多步交互：模型接收可用工具说明，输出调用，应用执行，返回工具结果，再取得模型后续输出。调用包含名称与参数。

与 [Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/) 对照，用于解释请求生成与实际执行的分工，以及结果怎样成为下一轮输入。它解释公开接口和运行流程，不提供完整内部因果解释，也不证明每次任务都正确选择工具。文中搜索和咖啡机场景是说明机制的假设，不是实际调研。
