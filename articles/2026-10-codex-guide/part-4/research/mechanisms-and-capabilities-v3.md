# 第四篇研究：Codex 实际机制、能力与交付路径

查询日期：2026-10-22。性质：官方文档调查与当前环境核查，非跨模型性能评测。

## 阅读与验证边界

本轮使用 OpenAI Docs，更新官方文档汇编；按其目录阅读执行建议、上下文与记忆、子代理、环境、App Server、工具发现、Skills、图像输入/生成、文件工作等相关章节；另打开并定位下方 API/开发者资料中的具体段落。没有逐页阅读全部手册，没有声称审计全部开源代码或模型权重，没有观看完整视频。

手册由官方 helper 获取，状态为 local manual was updated；本机临时缓存为 /var/folders/wf/2jlwzx3x0mgf8wgq6w8nfkl00000gn/T/openai-docs-cache/codex-manual.md。缓存不纳入仓库，不复制第三方全文；仓库保存链接和整理结论。

本会话此前已检查工具目录与工作区依赖，确认文件/代码执行、图像生成、表格和演示编辑、文档会话控制等能力入口；确认本机文档、幻灯片、工作簿、PDF 处理库可被运行时找到。这是接口和依赖核查，不是质量或兼容性验证。本轮只读取文档/能力描述，未新建 Office 文件、运行跨格式对照试验、安装第三方抓取工具或调用额外付费生成接口。

## 研究发现与对应证据

### 1. Codex 的行为来自模型与运行系统的配合

来源：
- https://developers.openai.com/blog/codex-as-a-platform
- https://developers.openai.com/api/docs/guides/agents-api/architecture
- https://learn.chatgpt.com/docs/app-server

阅读范围：运行框架职责、环境与应用的边界，thread/turn/item、工具调用和事件。可确认模型推断、会话状态、工具执行和权限不是同一职责；环境影响能读哪些文件、能跑什么程序。App Server 的协议实现细节不进入正文。Agents API 的托管部署不能套成所有桌面行为。

编辑意义：先用一小段解释一次请求为什么会引起多步动作，不重新列产品地图。能力描述必须同时说当前信息与工具条件，不能用一句“我是大模型”解释整个系统。

### 2. 当前上下文是工作输入，不等于用户拥有的全部信息

来源：
- https://learn.chatgpt.com/docs/prompting
- https://learn.chatgpt.com/docs/image-inputs
- https://learn.chatgpt.com/docs/environments/modes
- https://developers.openai.com/api/docs/guides/compaction
- https://learn.chatgpt.com/docs/customization/memories

阅读范围：输入材料与环境、图像输入、压缩机制、记忆适用范围。上下文会涉及请求、指导、已引入的文件内容和工具结果；本地/云端资料不会自动完全互通。压缩用于以较少 token 携带关键状态，不能称作完全遗忘；当前 API 压缩项可含不可读内部状态，也不宜统一叫“给人看的摘要”。跨会话记忆存在条件与控制，不能笼统说永远没有记忆，也不能当成完整档案。

编辑意义：讲清存在、可访问、已读取的差别；建议给有效材料的入口和用途，而不是无限贴资料。正式写作避免枚举私有系统提示或承诺产品精确内部拼接顺序。

### 3. 任务理解包含推断，具体失败原因不能凭自述确证

来源：
- https://learn.chatgpt.com/docs/learn/best-practices
- https://developers.openai.com/api/docs/guides/reasoning

阅读范围：目的、相关背景、约束、完成条件、复杂任务规划；推理模型的公开使用说明。文档能支持提供重要背景和验证标准的建议，不能证明某次遗漏的唯一心理原因。主张“更聪明的提示词保证成功”或“英文一定更好”均缺证据。

编辑意义：区分确定要求、推断和待验证假设。让 AI 根据用途调查专业方法属于协作要求，不是由文档证明它次次会成功。对用户缺少专业方法时，应由 AI 先研究推荐，不要求人先列出完整流程。

### 4. 工具和技能存在一个被发现、被选中、被实际调用的过程

来源：
- https://developers.openai.com/api/docs/guides/tools
- https://developers.openai.com/plugins/guides/optimize-metadata
- https://developers.openai.com/blog/skills-agents-sdk
- https://learn.chatgpt.com/docs/customization/overview

阅读范围：工具定义、动态加载、元数据与调用；Skill 渐进读取。Skills 通常先提供 name/description 等元数据，选中后才读完整说明，引用/脚本进一步按需读取。某些工具定义也可按需加载；具体取决于集成，不统一宣称所有工具都以同一方式发现。

编辑意义：已安装不等于本轮已经使用；工具发现失败、方法判断不足、执行失败应分开。只引用第三篇的 Skill/MCP 名称，不重写安装和目录。对重复漏用的能力，检查触发描述或任务路由，比反复逐步提示更有针对性；仍须用任务验证。

### 5. 某些未触发能力确实受到显式调用规则影响

来源：
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/agent-approvals-security

阅读范围：子代理触发、工作分配、权限继承与审批。当前文档注明本地 Codex 在直接请求或适用的 AGENTS.md/Skill 指令要求时委派子代理。不能将这一规则泛化成所有工具都必须点名。子代理带来额外模型/工具工作与协调成本，不保证更快。

编辑意义：对“需要提醒才会做”做具体诊断：没判断到、没发现、条件不足、缺授权或有触发约束，不统一归咎提示词或安全。本文研究未启用子代理，用户要求深入研究本身不被当作明确委派指令。

### 6. 工具循环带来真实反馈，程序可以承担确定性处理

来源：
- https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
- https://developers.openai.com/api/docs/guides/tools-shell
- https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling

阅读范围：计划、编辑、工具执行、观察、修复和继续；shell 调用与返回；程序协调工具、筛选和聚合结果的推荐场景。

可确认：模型提出操作，执行器/工具完成动作并返回；程序能承担筛选、去重、汇总和检查。一次查找可直接调用工具，适合程序处理的多结果任务可先处理再返回较小结果。API 的具体 V8/Node 环境差别不进入普通读者正文。

编辑意义：代码既是开发成果，也可以是制作其他成果的临时工作工具。终端常用源于命令可组合、重复与反馈明确；没有依据说它永远最快或是模型有心理偏好。原生接口、浏览器和图像观察各有作用。

### 7. 获取文本、看到页面、理解可编辑对象是不同路径

来源：
- https://developers.openai.com/api/docs/guides/file-inputs
- https://learn.chatgpt.com/docs/artifacts-viewer
- https://learn.chatgpt.com/docs/image-inputs

阅读范围：文件类型处理与预览。Responses API 的 input_file 文档区分 PDF 的文字/页面图像、其他文档的文字提取，以及表格增强流程。该说明只适用于这个 API 输入路径，不能断言桌面上传 Word 一律看不到图表，因为桌面还可以用工具渲染或读取。

编辑意义：文字提取成功不能说明版面被检查；截图能说明视觉，不能替代可编辑数据与公式。提供原始文件和目标样式各有价值，不作“所有任务只给纯文本”的建议。

### 8. 交付能力应按制作路径解释，不能按后缀排名

公开来源：
- https://learn.chatgpt.com/docs/use-chatgpt
- https://learn.chatgpt.com/docs/artifacts-viewer
- https://learn.chatgpt.com/docs/image-generation
- https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling

本地补充阅读（当前安装版本，不能泛化为所有账户默认实现）：
- documents/26.1017.22136/skills/documents/SKILL.md：DOCX 渲染检查流程。
- presentations/26.1017.22136/skills/presentations/SKILL.md：Spaces、Google、PPTX 不同目的地的路径。
- spreadsheets/26.1017.22136/skills/spreadsheets/SKILL.md：结构与公式检查、重算、渲染和导出。
- pdf/26.1017.22136/skills/pdf/SKILL.md：提取、程序生成、表单和渲染检查。

编辑分组（非官方能力分类）：

| 制作方式 | 可以说明的成果 | 关键条件与核查 |
| --- | --- | --- |
| 直接写文本或结构化内容 | 文章、代码、JSON、CSV、SQL、SVG 等 | 语义、结构、引用或语法；执行型内容要进一步运行 |
| 用代码处理数据或生成文件 | 清洗后的数据、统计图、文档、表格、演示、PDF、批处理结果 | 依赖和计算引擎、公式/数据校验、导出与渲染 |
| 通过专用模型/工具生成媒体 | 图片及其他条件具备时的媒体素材 | 当前工具、素材与使用约束、实际结果检查；不把视频或配音列为本会话已验证能力 |
| 编辑已有应用或在线对象 | 在线工作簿、演示、页面、已有文档 | 连接、权限、对象结构与修改是否实际生效 |
| 制作交互或可执行系统 | 网页、交互图表、脚本、应用项目或服务代码 | 构建/运行与完整用户路径；第五篇再展开部署 |

分类允许交叉：同一份报告可结合程序计算、图片工具、文档生成与页面检查。它用于解释路径，不把可生成性当作质量、原生兼容性或所有账户支持的保证。

### 9. 效率的瓶颈不只有模型输出速度

来源：
- https://learn.chatgpt.com/docs/learn/best-practices
- https://learn.chatgpt.com/docs/agent-configuration/speed
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling

阅读范围：任务范围、模型/推理设置、并行与协调、工具编排。官方资料支持不同执行路径与设置会影响速度和资源；本轮不作模型性能排名、不引用付费倍率，也未进行计时评测。

编辑判断：总交付时间要计入调查、工具等待、生成、检查及人的提醒与返工。更长推理不自动修复缺数据、错方法和缺渲染；堆工具或代理也不等于效率。先识别任务的主要不确定性，在关键方法/代表性页面处做小样验证，属于需在实际任务中验证的建议。

## 核心修正

1. 从“MD/HTML 更拿手”改为“不同制作与检查路径的比较”，不做无证据格式排名。
2. 从“终端最舒服”改为“可组合、可运行、有反馈的路径在适用任务上的价值”，同时解释专用接口与视觉观察。
3. 从“提醒不足就是提示词问题”改为逐环节检查任务判断、发现、条件、触发和执行。
4. 从独立的记忆/反馈章节改为把它们分别放入上下文与执行循环；避免重复第三篇与第二篇。
5. 从“公开其心里话”改为“解释公开机制和可观察动作”，不承诺披露完整内部思维过程。

## 研究未能回答的内容

无法公开确认每次模型选择的完整内部原因；无法证明当前各格式的相对质量与制作时间；本轮未对所有账户和产品入口作功能实测。遇到这些问题，正文保留适用条件或采用明确标识的说明性例子，不伪装成测试结论。
