# 第四篇更新研究：GPT-6 Astra 与 2026 年实验

查询日期：2026-10-22。用户要求核对 Astra 六及更新证据，再据此完整重写。采用官方模型页、开发团队文章、研究实验与系统卡，分别限定可支持的结论。未切换用户模型、运行评测或修改项目规则。

## 型号核对

官方模型页 https://developers.openai.com/api/docs/models/gpt-6-astra 确认 GPT-6 Astra / gpt-6-astra。当前产品目录另有 GPT-6.1 Sol，不以“更新型号”替换用户指定的 Astra；本篇不讨论价格和模型排名。

## 2026-10-06：业务工作如何成为训练任务

来源：[Advancing computer use with Ironclad](https://openai.com/index/advancing-computer-use-with-ironclad/)。署名 OpenAI。

实际阅读：Turning contracting workflows into training tasks、How Astra performed、Footnotes。研究与 Ironclad 专家选取 11 项任务，为不同任务制定 8—50 项判据，并提供可练习的软件环境，基于代表性流程构建合成任务，通过强化学习训练。

可用结论：模型能力来自训练与反馈，也需要业务专家定义真实要求；不是开发者替每个用户工作逐条预写全部步骤。采购金额门槛触发审批的例子来自该文。

限制：11 项研究任务不是全部真实业务；不同模型采用各自最优的不同推理设置；时间是模拟估计，不是客户实测节省。正文不引用相对速度或百分比作普遍承诺，不称研究提供完整的 Astra 训练配方。

## 2026-09-11：旧指令可能不再适合新模型

来源：[Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)，Eric Provencher。另核对 [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra) 的 GPT-6 Astra behavior、Instruction following、Initiative and follow-through。

实际阅读：技能说明、按需读取、决策边界和持续推进相关正文。开发团队认为过长或矛盾的技能描述会影响选择，旧版详细步骤与停止条件可能过度约束 Astra；模型会更谨慎，可能比用户预期更早回来询问。

可用结论：实际行为受模型能力和当前有效指令共同影响。旧协作规则应按用途和模型核查，但不是删除所有规则或放宽所有限制。应用中的具体遗漏仍需调查，不能仅凭这篇文章断言本会话失败原因。

## GPT-6 Astra 系统卡：能力与可监测性并不同步

来源：[GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)；[GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra)，第 9 节 Monitorability，尤其 9.1 非对抗条件与 9.2 对抗条件。

实际阅读：发布说明中的监测结论，系统卡第 9 节定义、三种观察范围、非对抗汇总结论与局限。部分评测中 Astra 的文字推理可监测性较 GPT-5.6 Sol 下降；较短或信息较少的推理、较强的文字推理控制能力等是团队讨论的因素。不能把下降统一写成只在对抗条件发生；发布说明强调很多主要发现来自要求规避监测的对抗评测。

限制：可监测性是特定观察者从线索推断目标行为的能力，不等于解释全部内部计算，也不等于普通任务正确率。不能由此宣称 Astra 日常回答普遍隐瞒或行为更不安全。正文只用来说明能力进步不保证思考文字更能揭示判断原因。

## 2026-07-06：在文字以外研究内部表示

来源：[A global workspace in language models](https://www.anthropic.com/research/global-workspace)；[原论文](https://transformer-circuits.pub/2026/workspace/index.html)，Wes Gurnee、Jack Lindsey 等。

实际阅读：官方概览、体育项目替换实验、内部推理与输出的区别；原论文作者贡献与 Limitations and open questions。研究对内部表示进行读取与干预：体育项目例子中替换表示后，模型报告的项目随之改变。说明特定内部活动与输出之间有可实验研究的联系。

限制：不是研究当前 Codex 的全部机制。所用方法受可命名概念、关系结构与读出质量限制，不能称已完整读懂模型，更不能推出人类式意识。

## 继续沿用的早期机制来源

[Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/)，2026-01-23，Michael Bolin。解释模型调用、操作请求与工具结果回传，不将当时 API 和配置细节写成当前所有入口固定实现。

[Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think)，2025-04-03。仅作为解释不一定忠实的历史证据，不再用旧模型数据代替 Astra 的最新结论。

## 写作选择

全文以训练获得的能力、实际调用循环、解释能力的边界推进。Astra 新指令经验自然放入执行与选择的解释中，不另开提示词教程。供应商报价比较是编辑设计的假设，不声称实际分析过报价。两个独立专题仍不展开，纯文字稿完整重写。
