# 交付物目录 v3：制作路径与术语核查

查询日期：2026-10-23。对应文件：../deliverable-atlas-v3.md。

## 研究性质与边界

本轮围绕用户要求重做完整参考目录，不撰写文章全文。条目名称、导航分组、示例任务与“优先解释哪些名称”是编辑设计；不是官方分类或普及率调查。

以下一手资料用于核对代表性软件结构、接口和运行环境。打开目录页时只视为范围核查；阅读定义/示例时只支持相应局部判断。没有安装这些工具，没有创建 App、Agent、机器人或工作流，没有调用商业模型接口，没有验证各平台发布规则或宣称全部路线已跑通。候选软件并非唯一或默认推荐。

## 已查来源及可支持的范围

### Agent、模型、工具与知识

- [Anthropic：Building effective agents](https://www.anthropic.com/research/building-effective-agents)。读取定义、工作流与 Agent 区分、执行循环相关段落；支持 G 组采用的工作定义。文章原始发布日期 2024-12-19，页面已有工具变化提示，因此不沿用其历史工具清单判断当前产品功能。模型选择下一步、工具执行与环境反馈是架构说明，不足以保证具体任务成功。
- [Ollama API](https://docs.ollama.com/api/introduction)。读取本地与云端模型调用入口；支持区分云端模型 API、本地模型接口和用户是否需要自行配置云密钥。不是本地模型在任意设备或任意 Agent 上都足够好的证明。
- [Agent Skills](https://agentskills.io/home)。读取目录、SKILL.md、脚本/资料/资产组成；支持 K05 的能力包与宿主区分。未安装或修改任何技能。
- [MCP 架构](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)。读取 host/client/server 与本地/远程运行说明；支持 K06。MCP 服务提供能力，宿主管理模型及使用方式，不将服务本身称作完整 Agent。
- [Dify Knowledge](https://docs.dify.ai/en/cloud/use-dify/knowledge/readme)。读取知识、检索、上下文与回答步骤；支持资料、索引、检索问答的区分。K01—K04 是通用编辑分层，不声称全部采用 Dify，也不声称问答一定无幻觉。

### 消息、自动化与接口

- [Telegram Bot API](https://core.telegram.org/bots/api)。读取 HTTP 接口介绍和消息更新相关入口；支持消息机器人依靠平台接口，不能由“机器人”推出模型依赖。未逐项复核全部方法或版本特性。
- [Slack incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/)。读取向指定地址发送 JSON 消息的说明；支持单向推送不等于消息接收与交互机器人。不是其他平台 webhook 权限的证明。
- [n8n 工作流](https://docs.n8n.io/workflows/)、[导入导出](https://docs.n8n.io/build/manage-workflows/export-and-import.md)。读取节点、连接、执行与 JSON 导入导出；支持 F06 中定义文件与运行平台的区分。导出文件可能含连接信息，归档仍须筛查。
- [Playwright](https://playwright.dev/docs/intro)。读取安装和示例运行范围；作为网页自动化候选，不推定全部桌面应用可由 Playwright 控制。
- [FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/)。读取服务运行、路径、返回和 OpenAPI 说明；支持服务实现、接口文档与运行实例的区分。S01—S06 为自行设计的输入输出示例。
- [GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)。读取工作流与执行机器说明；支持 F07。未配置 CI 或进行部署。
- [Home Assistant automation](https://www.home-assistant.io/docs/automation/)。读取事件、设备、实体与动作说明；支持 F08 的设备自动化作为独立探索对象。未连接家庭设备。

### 应用与扩展

- [MDN PWA 安装](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable)。读取安装与平台差异；支持 W05，不宣称各浏览器能力相同。
- [Xcode](https://developer.apple.com/xcode/)、[Android Studio](https://developer.android.com/studio/intro)。核对开发、构建和设备测试的工具范围；支持 A01/A02 的典型入口，不代表已核查上架资格、账户价格、签名和分发细则。
- [Electron](https://www.electronjs.org/docs/latest/)、[Tauri](https://v2.tauri.app/start/)。读取桌面应用定位及项目/发布入口；仅作为 A05 可选工具链。未作体积、速度或跨平台兼容比较。
- [Chrome 扩展](https://developer.chrome.com/docs/extensions/get-started)、[VS Code 扩展 API](https://code.visualstudio.com/api)。核对宿主扩展与开发入口；支持 P01/P02 的宿主区分。不能推定浏览器扩展、编辑器扩展、办公宏通用。
- 微信小程序[官方框架入口](https://developers.weixin.qq.com/miniprogram/dev/framework/)本次无法打开。A03/A04 保留明确的成果方向，未声称当前账号可发布或任意平台兼容；平台细则需要选定案例后另查。

### 文件、数据、工程和媒体

- [pandas](https://pandas.pydata.org/docs/getting_started/overview.html)、[Pillow](https://pillow.readthedocs.io/en/stable/handbook/overview.html)、[Python sqlite3](https://docs.python.org/3/library/sqlite3.html)。读取各自处理范围与示例入口；为表格数据、图片批处理和本地数据库提供具体工具候选。未运行清洗、格式转换或数据库样例。
- [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)。读取代码、说明、数据和交互计算的组合；支持 D04 的可复现计算工程与静态导出区分。
- [Pandoc](https://pandoc.org/)、[LibreOffice](https://www.libreoffice.org/)。核对文档转换范围及文档、表格、演示工具入口；支持 T 组工具候选，不证明跨格式转换保留全部版式。
- [FFmpeg](https://ffmpeg.org/ffmpeg.html)、[Audacity](https://www.audacityteam.org/)。前者读取转换、流与滤镜目录，后者核对录音/编辑定位；作为媒体处理候选，不宣称 FFmpeg 等于可编辑非线性剪辑工程或全部声音生成能力。
- [Godot 导出](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html)。读取工程与目标平台导出说明；支持游戏源码和可运行版本的区分，不证明特定平台均可无条件发布。
- [QGIS GUI](https://docs.qgis.org/3.44/en/docs/user_manual/introduction/qgis_gui.html)。读取项目、数据图层、处理与界面入口；支持地理工程作为可编辑成果，不证明路线分析或实时导航已实现。
- [FreeCAD 官方仓库](https://github.com/FreeCAD/FreeCAD)。核对参数化三维建模定位与项目入口；仅支持 E02 的候选路线。官网 features 页面本次被拒绝访问。未检验交换格式、装配、打印或 CAM 全链路。
- [KiCad 9 文档](https://docs.kicad.org/9.0/en/introduction/introduction.html)。读取原理图、PCB、Gerber 和项目组件说明；支持电子工程的不同交付组成。使用版本明确的文档，不把 9.0 写成当前最新版本；没有进行电路或生产检查。
- [ROS 2 官方测试文档站：发布与订阅](https://repo.test.ros2.org/en/rolling/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)。主 docs.ros.org 本次受访问保护，改读官方测试站教程的软件包、节点与消息示例；它是开发分支文档，只支持模块结构解释，不采用其发行版提示判断当前最新版本。未运行 ROS 或连接机器人。

## 仍需具体样例核查的路线

- Blender 官网与文档多个入口本次返回抓取失败；目录中的 Blender 为已有研究与常识层面的候选制作路线，不伪称完成当前文档核查。会场/空间案例要另做样例，确认尺寸、材质、视角与交付方式。
- Inkscape 页面被拒绝访问，Scribus 页面受访问保护；未以本次未读页面作能力证据，也未加入它们的具体版本承诺。
- 原生办公插件、设计软件插件、平台轻应用、移动小组件、AR/VR、MIDI、模型微调、加工刀路等仅给通用交付结构，未完成指定软件/设备的实现核验。进入正文时要先选择目标宿主/硬件并补查一手案例。
- 没有核查任何收费、配额或价格；“无需外部 API”只针对所描述基础用法，不是成本、所有功能或全部离线能力承诺。

## 编辑复核结论

1. 新目录保留原表各领域，并补齐具名 Agent、消息机器人与通用软件载体；不因讨论 Agent 就改变全文命题。
2. 网站/App 是形态，Agent 是执行机制，机器人可能是入口/自动化角色；允许在产品中组合，不能将组合重复计为新增独立能力。
3. 全目录同一套五列，技术细节进入参考清单，文章正文之后再按读者认知顺序取舍。
4. 所有条目保持研究/说明状态；没有将未经运行的设计写成已完成产品，也没有将生成代码写成已部署服务。
