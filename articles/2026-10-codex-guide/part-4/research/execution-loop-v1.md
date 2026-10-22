# 正文 v6 的执行机制来源

查询日期：2026-10-22。沿用 mechanisms-and-capabilities-v3.md，并补查直接解释 Codex 内部循环的一手文章。范围为机制阅读，没有运行文章内的假设订单任务。

## 本轮打开的来源

- https://openai.com/index/unrolling-the-codex-agent-loop/
  - Michael Bolin，2026-01-23。重点为 The agent loop、Building the initial prompt 与工具定义。支持模型可以输出工具调用、执行结果返回后用于后续模型调用、一轮用户请求可含多次迭代。文章聚焦当时 Codex CLI 的实现，不把特定请求地址、版本配置、完整提示拼装顺序当成当前所有入口固定细节。
- https://openai.com/index/unlocking-the-codex-harness/
  - Celia Chen，2026-02-04。重点为 core threads 与客户端事件连接。正文只用它支持运行系统组织操作、状态与界面进展，不展开 JSON-RPC 与协议细节。
- https://developers.openai.com/api/docs/guides/tools
  - 工具用途与调用的一般说明。正文只说明操作与输入要求，不声称每项工具均以同样方式提前加载，也不把 API 行为当作全部桌面产品功能。
- https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
  - 重点为观察、修复与继续的循环，不使用实验运行时长、代码量或配置作效率承诺，不展开长任务章节。

## 场景与判断边界

三个月订单、字段含义、重复记录、货币符号与待确认值均为假设教学设计。未读取用户真实订单，未实际计算收入或生成表格，不把举例写成已经完成的案例。

模型选择原因只按公开机制与示例中可解释的依据描述，不宣称读取了完整私有思维。对主动调查、诊断与如实交付的要求是合作判断，不是保证每轮一定正确的产品承诺。
