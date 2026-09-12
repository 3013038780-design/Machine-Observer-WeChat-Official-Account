# 英伟达产品实际采用情况：公开资料核查

查询日期：2026-09-13。用途：校正文章轻重与措辞，供文字审稿；不把全部研究数据塞入正文。此次为公开资料检索，未购买市场报告，也未取得各软件的统一企业用户调查。覆盖主要产品线，不宣称核查了每个 SKU 或完成全部行业研究。

## 判断

消费级独立显卡有明确的高份额证据；AI 计算硬件有市场领先的估计支持，但最新全球份额的公开口径不够完整。网络设备需要按细分市场判断，不能套用 GPU 份额。软件中 CUDA 的生态规模与 NeMo、NIM、Omniverse 等单项工具的实际采用不能等同。机器人和汽车已有真实产品与客户，但开发者数、合作名单不能换算为装机占比。

以下百分比不可横向相加或直接比较；全球市场资料也不代表中国市场现状。

## 七类产品的证据

| 产品领域 | 可核查证据 | 统计边界与写作判断 |
|---|---|---|
| 消费级显卡及创作 | Steam 2026年8月调查 NVIDIA 72.88%；JPR 2026年第二季度 AIB 出货份额图 NVIDIA 90% | 前者是自愿受访 Steam 设备，后者是当季新增 PC 独立显卡板卡出货。均不能当全部电脑、创作者或 Studio 使用比例。支持游戏显卡领域采用广泛。 |
| 专业图形与工作站 | JPR 发布2025年第四季度工作站市场概况，详细 GPU 厂商份额在完整报告内，公开稿未给出可引用 NVIDIA 比例 | 查到专业整机和应用测试不等于覆盖率。未采用网传专业卡90%等未核实数字；不能搬用消费级 AIB 数字。 |
| 数据中心 AI 计算 | TrendForce 2025-10-30 估计 NVIDIA 在2025年 AI 芯片市场约70% | 属于当时估计；公开稿未明确按数量还是金额。不能称2026年当前份额，更不能解释为70%的企业或数据中心都使用 NVIDIA。仅作带限制的背景，不写成正文硬数据。 |
| 网络与基础设施 | Dell’Oro 2026-09-03：2026年第二季度 AI 后端以太网交换机销售，Celestica 领先，NVIDIA 紧随，Arista 第三 | 是特定网络设备销售排名，不是所有网络设备市场。公开稿未给 NVIDIA 独立百分比；可称该细分领域主要供应商。不能推出 BlueField、ConnectX、NVLink 各自覆盖率。 |
| 边缘、机器人与物理 AI | NVIDIA 2026-08-25 称机器人软件栈有超过300万开发者；公告提及 Wing 已使用 Jetson Orin Nano Super 和 NVIDIA 软件栈 | 厂商生态口径，不是机器人台数、工业机器人份额、Isaac 活跃人数。新 Jetson Orin Nano 2 当时是公布产品，计划2027年上半年供货，不作为已经装机的产品。 |
| 汽车 | Volvo 官方确认 EX90 使用 NVIDIA DRIVE Orin，另有客户支持页介绍核心电脑升级 | 是具体车企车型实际采用的证据，不是所有汽车或所有智能驾驶芯片份额；不能据芯片判断采用 DRIVE AV 全套驾驶软件。本次未获得口径明确的最新全球 NVIDIA 装机百分比。 |
| 软件、模型与云 | NVIDIA GTC2026 材料称 CUDA 生态超过600万开发者；vLLM 官方支持在 NVIDIA GPU 上运行 | 开发者规模不是活跃率或开发者市场份额。未查到 Studio、NeMo、NIM、TensorRT、Omniverse、Isaac、DGX Cloud 可直接横向比较的最新采用率；不能因 GPU 普及就称整套软件普及。 |

## 来源及核查方法

1. [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)。页面标题 August 2026；页面脚本厂商图表 series 最新数据点 NVIDIA72.88、AMD18.68、Intel8.03、Other0.41，合计100%。最小提取数据见 steam-gpu-share-2026-08.json。没有把具体型号的其他分类自行分摊。
2. [JPR：Q2’26 AIB](https://www.jonpeddie.com/news/q226-pc-graphics-aib-shipments-increased-10-from-last-quarter-to-12-million-units/)，2026-09-09。核看原站 Figure2 柱状图：Q2’26 NVIDIA90%、AMD8%、Intel2%。数字经四舍五入，仅用于板卡出货份额。未复用新闻正文其他容易混淆的增长数字。
3. [JPR：Workstation Q4 2025](https://www.jonpeddie.com/news/workstation-volume-shows-robust-gains-in-the-fourth-quarter-of-2025/)，2026-03-02。公开摘要不足以得出 NVIDIA 专业卡占比。
4. [TrendForce：AI server outlook](https://www.trendforce.com/presscenter/news/20251030-12762.html)，2025-10-30。AI chip market share 约70%是2025估计，分母口径未完整公开。较新的[2026-04-08材料](https://www.trendforce.com/presscenter/news/20260408-13003.html)讨论 Blackwell 在 NVIDIA 自身高端产品中的占比，不可替换为 NVIDIA 对整个市场份额。
5. [Dell’Oro：2Q2026 AI back-end networks](https://www.delloro.com/news/ai-back-end-networks-switch-sales-surpass-front-end-networks-for-the-first-time-in-2q2026/)，2026-09-03。采用最新销售排名；不把旧材料 NVIDIA 与 Celestica 合计接近50%写成 NVIDIA 单家公司份额。
6. [NVIDIA：Jetson Orin Nano 2 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Jetson-Orin-Nano-2-Robotics-Computer-to-Redefine-Entry-Level-Edge-AI/default.aspx)，2026-08-25。300万为官方机器人栈开发者口径；注意区分现有客户采用与新产品未来计划。
7. [Volvo：From car to cloud](https://www.volvocars.com/intl/media/press-releases/D3815B71B2EAB931/)，2024年公告，作为具体车型采用事实。不以合作车企数量推算全球装机份额。
8. [NVIDIA GTC2026](https://blogs.nvidia.com/blog/gtc-2026-news/)，2026年3月，CUDA 二十周年段落超过600万开发者，属于厂商提供的生态规模。
9. [vLLM GPU installation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/)。支持 NVIDIA GPU，相关安装涉及 CUDA：这说明可用开源上层工具搭配 NVIDIA 硬件，不能把 vLLM 当作同层 CUDA 替代品。文档证明支持关系，不证明市场占比。

## 对文章的处理

- 开头直接交代覆盖主要产品线，用客户场景作为理解线索。
- 保留完整产品分类，解释篇幅按读者需要安排，不把每类产品描述为市场标准。
- 软件段用 NVIDIA GPU + vLLM 的例子说明可以组合；底层 CUDA 与上层推理工具区分。
- 机器人仿真写为辅助研发的方式，不写成所有项目必经步骤。
- 市场数字先在本研究记录供审阅；缺少统一分母的数据不放进正文作排行榜。
