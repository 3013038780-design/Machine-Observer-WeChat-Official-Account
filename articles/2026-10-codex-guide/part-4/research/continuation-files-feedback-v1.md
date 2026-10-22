# 第四篇后半篇机制补查

查询日期：2026-10-22。目的：为大纲 v7 的制作、接续和修正提供依据；不做性能测试、不运行子代理、不生成实际文件。

## 已读取的官方资料

1. https://developers.openai.com/blog/run-long-horizon-tasks-with-codex

读取 Why Codex can stay coherent on long tasks、状态与文档相关段落。支持循环中观察、修复与更新状态，以及文件保存进展和依据的作用。不采用实验的小时数、token 或代码量作为用户一般任务承诺；示例文件名不是强制配置。

2. https://developers.openai.com/api/docs/guides/compaction

读取 Overview、Server-side compaction。说明通过较少上下文携带继续所需状态；当前 API 压缩内容可不可读，不能统一说成用户可读摘要。不把 API 参数、触发阈值与具体实现套成所有 Codex 入口的工作方式。

3. https://learn.chatgpt.com/docs/agent-configuration/subagents

读取 Availability、Why subagent workflows help、Triggering subagent workflows。子任务可分别处理材料并返回结果，存在更多模型/工具工作与协调成本。当前本地 Codex 文档要求直接请求或适用规则要求才委派，本轮讨论多代理机制不构成实际启用授权；未调用子代理。

4. https://learn.chatgpt.com/docs/artifacts-viewer?surface=app

读取文件创建、预览、标注与修订相关内容。文档区分不同入口的预览方式，标注区域可成为修订上下文。大纲仅使用“原始文件、用途和定位信息参与修订”的一般事实，不宣称所有客户端都支持同一标注界面。页面夹带的示例演示文本不用于模型产品事实。

## 编辑推导与示例

测算表的可编辑输入与公式、运费变更影响排序/图表/结论，是用于解释关联的假设例子，未实做。由数据或生成逻辑更新关联成果是工作建议，不声称系统自动具备所有文件的依赖追踪或能保证局部修改不影响其他部分。

04 讲中间内容怎样写入成品及保留继续使用的能力；05 讲状态与分工如何支持继续；06 讲反馈怎样定位到该改的数据或文件。验证贴着各自操作出现，不复设验收科普章。
