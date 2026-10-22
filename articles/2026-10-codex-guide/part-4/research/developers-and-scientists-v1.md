# 第四篇调研：开发者与研究人员怎样解释 AI 的黑箱

调研日期：2026-10-22。用户要求直接查 OpenAI、Anthropic 开发团队和研究人员的论述，以解决现稿缺少新认知、只在重复合作常识的问题。本轮只做研究与判断，不续写正文。

## 首先需要纠正的混淆

“系统怎样组织模型与工具”和“神经网络怎样形成某次判断”是不同的问题。前者有公开工程实现，后者依赖实验研究，尚无每次行为的完整解释。前稿大量描写前者，却将其包装成已经解释后者；不能再靠模型自述补齐这个缺口。

资料按工程说明、训练方法、内部机制实验和思维链评估分别使用。没有采访研究人员，没有运行实验，也没有获得当前 Codex 的内部激活数据。

## 1. OpenAI 工程师 Michael Bolin：一句用户请求，可以引发多次模型调用

来源：[Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/)，2026-01-23，署名 Michael Bolin。

实际阅读：The agent loop、Model inference、Building the initial prompt、The first turn 相关段落与示例。

核心事实：准备给模型的输入包括指导、工具定义与输入材料；模型可能输出答复，也可能请求工具。工具结果带回后，会用于后续模型调用。一轮用户消息可以包含许多次这样的迭代。

意义：屏幕上的连续工作来自模型与运行程序配合，不能把它写成一个模型始终在后台独自观察一切。文章可用它解释运行结构，但它本身不能证明模型为何选择某个具体动作。

边界：文章以当时 Codex CLI 实现为主，配置和协议示例不当作当前全部入口的固定实现。

## 2. OpenAI 研究团队：拆解、纠错与换策略可以通过训练学来

来源：[Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)，2024-09-12。

实际阅读：引言、Chain of Thought、训练与推理计算相关概述；不使用产品当前可用性或考试分数。

团队报告，o1 的强化学习训练使模型学会改善推理策略、识别并纠正错误、拆解复杂步骤、方法失效时换路径。这是训练获得的能力说明，不是一份开发者逐条编写的万能任务流程。

编辑意义：可以解释“会拆任务”的能力从哪里来。不能由此保证当前模型对每个工作任务都拆对，也不能把 o1 的具体训练描述无差别套给所有模型。

## 3. Anthropic 的 Jack Lindsey、Chris Olah、Joshua Batson 等：模型内部确有可实验研究的策略

来源：[Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)，2025-03-27；及作者原论文 [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)。

实际阅读：官方概览的规划、心算、多步推理、跨语言与局限段落；原论文的相关案例、贡献与开放问题，未逐项审查整套方法或复现实验。原论文确认 Jack Lindsey、Chris Olah、Joshua Batson 等人的具体贡献；押韵规划案例由 Emmanuel Ameisen 研究，跨语言案例由 Wes Gurnee 研究。

论文研究 Claude 3.5 Haiku 等模型。押韵案例中，模型在写完下一行之前已有后续韵脚相关表示，干预这些表示会改变后续输出。这比“逐词生成所以不会提前规划”的说法更具体，也不能推出它已规划好整项长任务。

心算案例观察到模型使用近似与个位信息等路径，其口述解释却可能采用人类常见的进位算法；跨语言案例则发现部分共享概念机制。两者均不能直接当作当前 Codex 内部的实测事实。

团队明确承认，方法只覆盖部分计算，仍有工具伪影与适用范围限制。打开黑箱应写成有证据的局部理解，不能宣称已经全面解码。

## 4. Anthropic 的 Yanda Chen、Ethan Perez 等：说出的理由不保证包含真正影响答案的因素

来源：[Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think)，2025-04-03；[论文 PDF](https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf)。

实际阅读：官网实验与结论，论文摘要、实验定义、限制和作者贡献。作者包括 Yanda Chen、Ethan Perez、John Schulman、Jan Leike、Jared Kaplan 等；论文注明部分作者工作在 Anthropic 任职期间完成，不由作者名单推断当前任职。

在给选择题加入提示的对照实验中，研究者观察模型使用提示后，是否在思维链中说明其影响。测试模型常未披露，某些训练设置还产生为提示答案辩护的理由。不能因此认定所有解释都假，更不能据此确证本次写作失败的唯一内因。

编辑意义：模型对“我刚才为什么这样做”的口述，不是内部过程录像。自己的解释需要外部证据支持。

## 5. OpenAI 的 Melody Y. Guan、Jakub Pachocki、Bowen Baker 等：不完整的思维链仍可能有观察价值

来源：[Evaluating chain-of-thought monitorability](https://openai.com/index/evaluating-chain-of-thought-monitorability/)，官网日期 2025-12-18；[Monitoring Monitorability](https://arxiv.org/abs/2512.18311)，论文提交日期 2025-12-20；[论文 HTML](https://arxiv.org/html/2512.18311v1)。

实际阅读：官网研究概览、监测定义、限制；论文摘要、faithfulness/monitorability 的区别、相关研究与讨论。未逐项复核全部评测环境或图表。

论文作者确含上述三人。研究区分“完整忠实地还原内部计算”与“可从线索预测关心的行为”。其测试中，思维链往往比只看最终动作更有帮助，但并非完美。

编辑意义：不能从 Anthropic 的不忠实案例跳到“思考文字毫无价值”。这些研究不是简单争执同一结论，观察价值和完整因果解释是两个标准。

## 6. Anthropic 工程团队：方法选择也受工具接口影响，不只受用户请求影响

来源：[Building effective agents](https://www.anthropic.com/research/building-effective-agents)，2024-12-19，当前页面署名 Erik S. 与 Barry Zhang，并提示部分工具生态已变化。

实际阅读：workflows/agents 区别、Agents、Appendix 2、署名。只取架构判断和具体经验，不沿用旧配置清单。

工作流按预定代码路径组织；代理可由模型动态决定下一步。开发团队报告过相对路径引发工具使用错误，改为要求绝对路径后改善。工具名称、描述、输入形式和边界会影响使用；这说明提升可靠性未必只改用户提示词。

编辑意义：解释为什么有工具却不一定用好，以及为什么“让 AI 更聪明”不能包办接口设计问题。作者的单个案例不是普遍性能保证。

## 7. Anthropic：上下文的目标是有效，而非无限增加

来源：[Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)，2025-09-29。

实际阅读：context 定义、有限资源、有效上下文、按需检索与工具选择段落。

团队强调每次模型调用所用信息需要选择和维护，大量内容及含糊工具会增加困难。完整应理解为关键背景足够、入口清晰，不等于把全部资料塞进去。不能据此给出对所有模型适用的固定长度阈值。

编辑意义：第一节不能只把“交代上下文”再讲一遍，要解释为何系统需要组织、检索和更新工作材料。

## 8. 2026 年补查：内部处理并不都出现在文字里

来源：[A global workspace in language models](https://www.anthropic.com/research/global-workspace)，2026-07-06；[Verbalizable Representations Form a Global Workspace in Language Models](https://transformer-circuits.pub/2026/workspace/index.html)。

实际阅读：官方概览、J-space 的定义、干预例子；原论文作者贡献及 Limitations and open questions。原文确认 Wes Gurnee、Jack Lindsey 等人为作者。未完整审查全部方法与实验。

研究提出一类可读出的内部表示，并用干预研究其与多步处理的关系。它与文字思维链不同；研究也不证明模型有人类式意识。论文指出读出方法在多词概念、关系结构和可解释性上仍有限制。

编辑意义：作为较新的研究补充，进一步限制“看见思考文字就看见全部内部过程”的说法。先保留研究，不因新名词吸引人就强行写进正文，更不能把结果称为当前 Codex 的确定内部结构。

## 对现稿的结论

article-v7.md 的核心仍是背景、方法、工具循环，缺少模型能力怎样训练出来、内部规划有哪些证据、口述理由为何不等于真实因果，以及接口怎样影响行为。继续换场景或标题无法补足这些认知。

后续需从这些证据中选出真正服务文章的一条逻辑，再写正文。知识与合作收益仍要连接；不能改成研究论文盘点，也不恢复交付大全、长任务和多轮目标漂移三个扩展方向。

研究事实、跨模型可迁移的架构与编辑推导分别标明。当前仅归档研究，不把所有结论合并成对每次 Codex 行为的确定解释。
