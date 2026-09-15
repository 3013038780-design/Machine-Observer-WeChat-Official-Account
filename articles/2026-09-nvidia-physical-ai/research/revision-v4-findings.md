# v4 补充调查与全文审读

查询日期：2026-09-15。目标是回应实景缺失、研究浅、判断不清、产品范围不显著四项反馈。本轮未做产品实测，也未取得客户现场访问或独立采购数据；不能称为行业全覆盖调查。

## 证据与取舍

| 阅读材料 | 实际阅读范围 | 可进入正文的内容 | 不作出的推断 |
|---|---|---|---|
| [Mercedes-Benz](https://group.mercedes-benz.com/technology/autonomous-driving/driving/mb-drive-assist-pro.html) | 2026-01-07公告正文 | DRIVE AGX与DRIVE AV，Level 2 | 不推断所有市场交付状态；不沿用网页TOPS表述错误 |
| [DriveWorks](https://developer.nvidia.com/drive/driveworks) | 传感器接入、记录回放、图像处理模块 | 工具的具体输入和用途 | 不等同驾驶功能或整车系统 |
| [DRIVE目录](https://developer.nvidia.com/drive) | 数据整理、模型、NuRec、AlpaSim、AGX栏目 | 研发链条中的产品关系 | 未验证厂商效率倍数、模型优劣或客户全套采用 |
| [FoundationPose原始项目](https://github.com/NVlabs/FoundationPose) | README方法与输入条件 | 位姿估计需要物体模型或参考图像等信息 | 不把识别位置等同完整抓取；研究实现与部署包不混为同版本 |
| [Isaac机械臂参考架构](https://nvidia-isaac-ros.github.io/v/release-4.0/reference_workflows/isaac_for_manipulation/reference_architecture.html) | release4.0，环境、机器人结构、目标、规划、实机组件 | cuMotion在机械臂任务中的角色 | 不宣称必用Jetson；不复述未复现的性能对比 |
| [Intrinsic CEO署名文章](https://www.intrinsic.ai/blog/posts/unlocking-new-value-in-industrial-automation-with-ai) | NVIDIA、Google DeepMind及自研三部分，重点前者 | 2024年TRUMPF任务原型、仿真数据与抓取开发 | NVIDIA原型不能扩成其他演示归属或工厂规模部署 |
| [Boston Dynamics](https://bostondynamics.com/news/boston-dynamics-expands-collaboration-with-nvidia/) | 2025-03-18正文及Atlas照片 | Jetson与自有控制结合、Isaac Lab研发采用 | 不把2025照片当2026所有版本；不以外观判断内部芯片 |
| [Isaac Lab](https://developer.nvidia.com/isaac/lab) | 工作方式与学习方法、文档入口 | 仿真学习任务与开发环境 | 不宣称用了Lab就采用整套NVIDIA硬件 |
| [宇树官方项目](https://github.com/unitreerobotics/unitree_sim_isaaclab) | README任务、数据采集与验证流程 | 中国企业具体研发采用记录 | 不推断全部量产能力及机载硬件 |
| [Ken Goldberg访谈](https://aihub.org/2026/09/01/combining-cultures-from-code-to-canvas-an-interview-with-ken-goldberg/) | 传统控制与学习、工业吞吐部分 | 同时看成功率与耗时；方法结合 | 不采用未经统一口径的数据规模估算，不声称自行采访 |
| [GR00T模型卡](https://huggingface.co/nvidia/GR00T-N1.7-3B) | 输入输出、模型用途 | 模型与仿真软件属于不同资源 | 不把下载模型视为直接获得通用机器人 |

此前汽车/机器人基础资料继续沿用既有来源台账。本轮正文未新增芯片性能、价格、市场占比数字。

## 编辑判断及其根据

- 产品并不少：计算平台之外，已有数据接入、位姿估计、路径规划、仿真和学习等可调用工具。判断依据是文档中的可辨认工作对象，不是产品名称数量。
- 芯片采用不能推出软件采用：奔驰列出硬件及驾驶软件；Atlas保留自有控制；宇树材料证明开发工具使用。三者所证明的采用层级不同。
- 复用开发能力是产品组合的意义：根据数据工具、抓取原型与模拟流程所做的编辑分析，并非已量化的客户节省成本结论。
- 工业价值要回到工作结果：用Goldberg的成功率与耗时观点连接工序，避免仅保留泛化免责声明。

## 范围边界

已查看IGX与Isaac更广目录，但正文没有为凑型号而展开IGX、Holoscan、OSMO、Newton等。当前稿是一篇解释汽车驾驶辅助与机器人操作/移动研发的科普，不是英伟达全部工业产品目录。Token、AI工厂经营及价格仍属后续文章。

公开资料足以说明产品功能与若干采用案例；不足以给出所有汽车/机器人厂商的真实软件使用率。未把发布稿中的合作名单当作市场份额，也未把2024原型写成2026规模生产。

## 图片与检查

- 七张正文图：两张既有原创关系图，五张官方素材（其中Atlas为实物照片，ET7为车型展示图，Jetson为产品展示，另外两张为软件界面和仿真输出）。未使用AI生成图冒充实拍。
- 全部素材已逐张打开检查；文件、原始URL、页面、性质与权利状态在assets/report-v4/manifest.json。引用来源不等于取得额外转载授权。
- 375、390、430、1000px浏览器宽度检查：无页面横向溢出，七图均加载，图片放大可用。已检查手机截图并缩短冗长图注。
- 135实际粘贴未测试；需上传图片。HTML、body片段、离线包和图片包已生成。
- 文字仍待用户审阅，不标定稿。旧v3保留。
