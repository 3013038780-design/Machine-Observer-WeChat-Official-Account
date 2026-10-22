# 第四篇补充研究：实践经验与有依据的推荐

查询日期：2026-10-22。用户要求阅读实际经验帖，不能仅按用户提供的例子或功能支持清单组织文章。本轮范围为第一手实践、作者发布的示例/项目和有明确来源的使用者反馈；不将社区观点当作 Codex 的统一实现或性能测试。

## 1. Thariq Shihipar 的 HTML 实践

来源：https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html

实际打开后重定向至 https://claude.dev/blog/using-claude-code-the-unreasonable-effectiveness-of-html/ 。作者署名 Thariq Shihipar，页面日期 2026-05-20。阅读全文相关段落，重点为阅读、比较、交互与 FAQ。

作者主张以 HTML 改善人审阅结果的体验，并承认 Markdown 往往更省 token。这是 Claude Code 使用者/开发者的个人实践，不是 Codex 格式性能比较。不能据此写 HTML 普遍生成更快、成本更低，或模型仅能生成文本。

## 2. 作者公开示例

来源：https://thariqs.github.io/html-effectiveness/

阅读作者示例目录，另打开工程周报与配置编辑示例：
- https://thariqs.github.io/html-effectiveness/11-status-report.html
- https://thariqs.github.io/html-effectiveness/19-editor-feature-flags.html

这些材料说明成果可以承载并排比较、图示、导航与编辑回传，不只是把文字美化。只阅读页面内容，未实际测试拖拽、导出或所有交互功能，不能写成自行验证。

## 3. Codex 用户对命令行工作路径的实践

来源：https://steipete.me/posts/2025/shipping-at-inference-speed

Peter Steinberger，2025-12-28。读取命令行起步、代理直接调用与验证、使用截图和迭代相关段落。

可借用的经验是：把核心操作做成模型可以调用并检查输出的程序，减少人转述和手工操作。其具体模型、配置与产品可用性具有历史性，不采纳为当前推荐；不采用其个人速度倍数或对内部推理的猜测。

## 4. 支持 HTML 报告的实际项目

来源：https://github.com/Lucas-Fong/html-report-stable-base

读取 README 的长报告、演示模式、编辑控制、浏览器检查和导出描述。它提供 Codex 使用场景的实际实现线索，不是效率证明。未安装、运行、审核全部代码，也不把作者自述的导出能力当作已验证兼容性。

## 5. 支持原生 Word 的反向实践

来源：https://github.com/zhongtw1979/codex-formal-docx-workflow

读取 README 中原生 DOCX 编辑、表格排版与检查的工作方式。作者特别关注 HTML 转 Word 的布局问题。这支持将原生 Word 工作流作为有明确格式要求时的另一条路径，不能证明该仓库一定优于其他方案。未运行其技能。

## 6. 不同用户对 HTML 修改负担的反馈

来源：https://www.reddit.com/r/ClaudeCode/comments/1t8vni3/html_markdown_for_claude_code_outputs_thariqs/

打开主题与评论，定位自述从事数据分析的 skep_leo 的反馈：在持续修改报告时，HTML 细节修改给其带来额外负担，偏好先修改 Markdown 再制作展示版本。另有评论报告使用脚本或模板减少生成负担。

这属于个人经验，有任务、版本和使用习惯差异；不能拿投票数或个例当作性能评测。正文若引用应明确是不同使用者的相反体验，技术判断仍由制作与检查机制支撑。

## 7. 减少不必要 DOCX 的使用者反馈

来源：https://www.reddit.com/r/ClaudeAI/comments/1rtpww1/stopped_asking_claude_for_word_docs_and_my/

打开原帖。作者报告把屏幕阅读材料改为 Markdown 后更省事。其“Markdown 是模型原生输出”等解释不能直接采信；没有受控计时，不采用速度、token 或故障泛化结论。这项材料只说明使用场合与交付格式错配值得检查。

## 8. 面向非技术读者的实际教学

来源：https://ailearninghub.law.stanford.edu/codex-without-the-code/plan-build-check/

读取 Plan → Build → Check 页面。它区分具体检查证据与人的使用判断，并给出网页操作验证例子。本篇借用“怎样让结果可以被检查”的解释，不重讲第二篇的规划与协作流程。

## 补查但不作为主要证据的材料

- Blake Crosley：https://blakecrosley.com/blog/html-is-the-format-agents-want 。以对上述观点的延伸分析为主，不当作独立性能验证。
- https://github.com/sunlesshalo/claude-code-md-hook 的搜索摘要含作者承认的读取错误及不同格式波动；未完整复核方法，不使用其 benchmark 数字。
- LinkedIn 转述中“DOCX 是包含 HTML 的压缩包”等说法不采纳。
- 用户要求阅读经验帖，故本轮按其指令拓展非 OpenAI 来源；Claude Code 的实践仅作为可迁移的工作方法线索，不混同 Codex 的产品事实。

## 形成的编辑判断

1. 总命题仍为理解 Codex 的工作机制、据此更好地取得成果；HTML 不替代整篇主题。
2. 对需要人阅读、比较、筛选或交互的报告和解释页，优先推荐 HTML 作为展示与操作界面。这是编辑推荐，不是格式性能排名。
3. 对文字尚在密集修订的材料，Markdown/纯文本是合理的工作底稿；需要正式 Word 修订或交付原生 Office 文件时，优先走相应原生路径。
4. 判断效率要同时看生成、转换、检查与人的理解修改成本。不能由路径看起来直接就断言 HTML 比 Word 普遍更快，也不能因 HTML 多用 token 就忽略它可能减少人的工作。
5. 让 AI 能读资料、调用程序、获得结果并检查，比让它逐个模仿人操作办公软件更值得优先考虑。终端、专用接口与视觉操作按任务选择。
6. 观点必须给默认推荐和适用边界，不能只罗列“都可以”，也不能把用户印象直接升级为结论。
