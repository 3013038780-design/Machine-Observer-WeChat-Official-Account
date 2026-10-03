# 六篇系列：当前能力缺口审计

审计日期：2026-10-03（Asia/Shanghai）

这次审计把“用户可能想不到但长期工作必然会遇到”的内容按层级分配到六篇，避免第一篇成为百科，也避免后面的真实落地环节缺失。

| 能力面 | 放入篇目 | 为什么必须覆盖 | 当前资料状态 |
|---|---|---|---|
| Codex / Chat / Work / IDE / CLI / Cloud / Remote | 第一篇 | 先确认在哪里工作、谁能操作什么 | OpenAI 官方资料已部分核查 |
| workspace / project / task / thread / repo / worktree | 第一篇 | 避免把上下文容器和代码载体混成一个“工作” | 待补当前界面术语 |
| Plan / Goal / Queue / Steer / side chat / compaction | 第一、二篇 | 区分路径、结果、旁支和中途纠偏 | 官方资料已部分核查 |
| Voice / 文件 / 图片 / 屏幕 / Computer Use / Record & Replay | 第一、二、六篇 | 输入和操作方式会改变提示词与权限 | 官方资料已发现，需记录版本/地区 |
| AGENTS.md / PLANS.md / README / decision log | 第一、二、六篇 | 长任务不能只依赖聊天历史 | OpenAI 官方 Cookbook 已有案例 |
| Git / GitHub / PR / Actions / release / rollback | 第一、五、六篇 | 成果需要版本管理、审阅和回退 | 待 GitHub 官方与 Codex 集成核查 |
| Skills / Plugins / MCP | 第一、二、三、六篇 | 把流程、工具和外部服务分层 | OpenAI 官方资料已核查 |
| Harness / sandbox / environment / handoff | 第一、三、六篇 | 长运行代理需要环境、状态和恢复机制 | OpenAI Agents API 官方资料已核查 |
| Jev / TypeSafe / 社区 Harness | 第三、四篇 | 新兴决策与评估工作流需要来源和风险边界 | 社区资料，不能写成 Codex 内置能力 |
| Multi-agent / subagents / orchestration | 第三、四、六篇 | 复杂任务可能并行，但需要分工和合并证据 | OpenAI Agents 官方资料已部分核查 |
| Trace / evals / graders / guardrails | 第二、三、六篇 | 不能用一次成功代替稳定性证据 | OpenAI 官方资料已核查 |
| Memory / Scheduled Tasks / background / webhooks | 第一、三、四、六篇 | 长线工作需要持续运行和通知 | 待按产品/API边界拆分 |
| 腾讯云 / 阿里云 | 第五、六篇 | 云资源、价格、地域和责任边界不同 | 待官方文档与计费页核查 |
| 网站 / 域名 / DNS / URL / HTTPS / API 地址 | 第五、六篇 | “放到网上”不是一个动作 | 待官方服务商资料核查 |
| 静态站点 / 前端 / 后端 / 数据库 / 对象存储 / CDN | 第五、六篇 | 不同架构需要不同部署方式和成本 | 待按案例选择范围 |
| 账号、密钥、客户资料、录音、屏幕内容 | 全篇 | AI 能操作的范围也带来数据风险 | 官方安全资料与服务商权限资料待补 |
| 模型、速度、推理、成本、图像、视频工具 | 第一、二、六篇 | 模型和工具是选择条件，不是名词清单 | 待核查当前可用性 |
| 版本、迁移、更新、限额和失败恢复 | 第一、二、三、五、六篇 | 产品和云服务会变化，长期工作要可恢复 | 待建立变更记录模板 |

## 审计结论

原四篇方案能够解释 Codex 和人机协同，但无法完整覆盖“成果怎样进入 GitHub、云、网站和真实网址”。六篇更适合当前主题。第五篇应成为独立的基础设施与发布篇，第六篇再把前五篇串成案例。
