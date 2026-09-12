# 英伟达产品版图：重写前研究报告

状态：研究材料与候选大纲，待用户审阅；不是文章正文，不代表旧稿已经修好。核查日期：2026-09-12。

## 这轮调查回答什么

本轮围绕一个问题展开：英伟达究竟提供哪些类型的产品，它们之间是什么关系，怎样讲才能让非行业读者看懂？

已交叉阅读官方目录、文件和最新公告，管理层及业务负责人访谈，原始评测和行业分析。完整阅读边界见[信源台账](sources.md)。调查覆盖主要产品家族与层级，不声称穷尽历史型号、地区特供版本、全部软件库或所有市场报道。

**主要结论：原稿的问题不只是少写了几类产品，而是把不同层级混在一起。** GPU 是计算部件；GeForce、RTX PRO 是产品家族；Blackwell 是架构名；DGX 是系统家族；CUDA 是计算平台；Isaac 是机器人开发平台。这些名字不能用同一套“从低端到高端”逻辑排序。

建议正文沿产品的组成关系展开：先讲计算与连接部件，再讲组合出的系统和专用平台，最后讲让这些硬件能完成工作的软件与模型。用途用来解释每类产品，不再作为另一套忽然插入的章节分类。具体候选大纲见[outline-v11.md](../../upper/outline-v11.md)。

## 一、用户给出的图能用来做什么

图比原稿覆盖广：它提醒我们补上网络、系统、软件、模型和云。但七个框是制图者的编辑分组，不能当成 NVIDIA 官方唯一分类，更不能称为全部产品清单。年度财报的分部、市场披露和官网产品入口本就采用不同口径；本年最新季度披露还有新的展示口径。[R01](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)；[R02](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027)

图中也有交叉：RTX PRO Server Edition 服务服务器；Isaac 和 Omniverse 属于软件平台，同时服务机器人或工业场景；DGX Spark 是桌面系统，不能因为含 DGX 就一律放进机房。把交叉关系讲清楚，比坚持凑齐七块更重要。[R05](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/)；[R18](https://developer.nvidia.com/isaac)；[R19](https://www.nvidia.com/en-us/omniverse/)；[R20](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

此外，当前资料已经涉及图中没有单独交代的 Grace/Vera CPU、MGX、HGX、Groq LPU/LPX，以及 RTX Spark 等。这里应补的是“它是什么”，不必把每个新名字都升成正文一章。最新公告也不能直接当成客户普遍可购买、可部署的证据。[R03](https://www.nvidia.com/en-us/data-center/)；[R11](https://www.nvidia.com/en-us/data-center/products/mgx/)；[R12](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html)；[R21](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Microsoft-Reinvent-Windows-PCs-for-the-Age-of-Personal-AI/default.aspx)；[R22](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)

## 二、重新理解产品关系

### GPU 不是只做一种工作的卡

GeForce 面向个人电脑的图形、创作和本地 AI；专业 GPU 更强调专业应用与企业部署需要；数据中心 GPU 在内存、互连、形态和配套上服务不同规模的计算。产品线与用途相关，但不是严格的“消费卡只能游戏、数据中心卡只能训练”分工。[R04](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/)；[R05](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/)；[R03](https://www.nvidia.com/en-us/data-center/)

正文需要解释显存与带宽，因为这能帮助理解差别：容量关乎能同时容纳多少工作数据；带宽关乎数据传输速度；计算能力关乎运算速度。三者共同影响任务表现，不能把任何一个数字写成万能排序。具体型号的统一内存与独立显存还要分开。应用实测提供了这种解释所需的约束。[R31](https://www.pugetsystems.com/labs/articles/topaz-video-1-6-1-professional-gpu-performance-analysis/)；[R33](https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/)

### GPU 之外还有计算和连接部件

CPU 运行通用程序、处理流程与数据工作；DPU 承担一部分网络、存储和安全基础设施工作；网络适配器、交换机和互连把设备连起来。它们不是性能较弱的 GPU，也不是买了 GPU 就可以忽略的附件。[R11](https://www.nvidia.com/en-us/data-center/products/mgx/)；[R09](https://www.nvidia.com/en-us/networking/products/)；[R12](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html)

“带宽”必须说明是谁与谁之间：GPU 读取显存、GPU 之间交换数据、服务器之间通信，是不同位置的能力。NVLink 与以太网/InfiniBand 不能只按一个数字混排。正文只解释这些关系，协议细节留作查阅。[R13](https://www.nvidia.com/en-us/data-center/nvlink/)；[R09](https://www.nvidia.com/en-us/networking/products/)

新出现的 LPU 也说明，AI 加速器不只有 GPU 一种。NVIDIA 已公布 Groq 3 LPX 量产信息；应区分 LPU 处理器与 LPX 系统。其优势与适用条件仍需结合工作负载判断，不采用公告中的性能倍数作为独立结论。[R22](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)；[R27](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands)

### 芯片、底板、服务器与机柜不是同一件商品

HGX 提供多 GPU 计算平台，合作伙伴在此基础上构建系统；MGX 是模块化系统参考架构；DGX 是 NVIDIA 的系统家族。这三个名称不是 GPU 的三个档次。报价时尤其不能拿一块计算底板、一个完整服务器和机柜系统当成同类产品比较。[R12](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html)；[R11](https://www.nvidia.com/en-us/data-center/products/mgx/)；[R10](https://www.nvidia.com/en-us/data-center/dgx-platform/)

也不能简化为“每个用户都需要显卡、服务器和机柜一起买”：个人电脑不必配服务器，桌面 AI 系统不必放机柜，机柜也不是一个空壳就等于机柜级计算系统。正文应先把形态解释清楚，价格才能有意义。

### 机器人和汽车平台需要软硬件一起解释

Jetson、IGX 和 DRIVE 是专用平台范围，不能都叫显卡。Jetson 用于设备侧 AI；IGX 强调工业级边缘部署；DRIVE 面向汽车开发和车载计算。说明用途即可，不能把芯片宣传的自动驾驶等级写成采用它的车辆已经具备该能力。[R06](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/)；[R17](https://www.nvidia.com/en-us/edge-computing/products/igx/)；[R07](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/)

机器人工作还包含数据、训练、仿真验证和部署。Deepu Talla 访谈能帮助说明这些环节如何关联，却不能替整个行业证明机器人已经解决可靠性问题。**“训练和推理是两种关键计算活动”可以写；“AI 只有两类工作”不能写。**[R26](https://www.chipstrat.com/p/an-interview-with-nvidias-deepu-talla)

### 软件不是最后附上的品牌清单

CUDA 及工具库帮助开发者使用 GPU；推理、部署和模型开发工具解决不同的软件任务；Omniverse、Isaac 等提供仿真或领域开发能力；模型又是另一类产物。正文应按用途解释关系，每类选少数代表，不连列十几个缩写。[R15](https://developer.nvidia.com/cuda/toolkit)；[R16](https://www.nvidia.com/en-us/ai/)；[R18](https://developer.nvidia.com/isaac)；[R19](https://www.nvidia.com/en-us/omniverse/)

云部分尤其要重新核查。当前 DGX Cloud 官方页面明确描述 NVIDIA 内部的 AI 开发与运行环境，并介绍通过合作伙伴和 DSX OS 输出经验的关系。不能照搬旧文章，把它简单写成另一家阿里云或腾讯云；也不能仅凭这个页面宣布历史商业产品全部停办。[R14](https://www.nvidia.com/en-us/data-center/dgx-cloud/)

## 三、深度文章、访谈和测试到底改变了哪些判断

| 阅读材料 | 有用的判断 | 不能据此推出什么 |
|---|---|---|
| Ben Thompson 对黄仁勋的访谈 | 加速应用需要软件与计算体系，CPU 仍有作用 | 管理层对平台优势的阐述不是第三方性能证明 |
| Dwarkesh、Lex 的相关访谈章节 | 云伙伴关系、架构取舍和系统协同值得解释 | 不能把采访中的未来愿景写成普遍现状 |
| Deepu Talla 访谈 | 机器人开发涉及数据、训练、仿真和部署 | 不能把部署端芯片等同于完整机器人技术 |
| SemiAnalysis 的公开分析 | 推理硬件涉及延迟、容量和吞吐取舍 | 没有读取付费模型，不能引用其未见预测 |
| Puget 的专业应用测试 | 专业定位、显存容量和应用速度是不同维度 | 更贵或更多显存不等于所有软件都更快 |
| StorageReview 与 LMSYS 的 Spark 测试 | 软件版本、并行方法和请求条件会影响结果 | 一个榜单不适用于所有模型和负载 |
| ServeTheHome、Tom’s Hardware | 架构与真实系统形态可补充产品目录 | 厂商数据和受邀演示不能冒充独立复测 |

来源：[R23](https://stratechery.com/2026/an-interview-with-nvidia-ceo-jensen-huang-about-accelerated-computing/)；[R24](https://www.dwarkesh.com/p/jensen-huang)；[R25](https://lexfridman.com/jensen-huang-transcript/)；[R26](https://www.chipstrat.com/p/an-interview-with-nvidias-deepu-talla)；[R27](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands)；[R30](https://www.pugetsystems.com/labs/articles/nvidia-rtx-pro-6000-blackwell-workstation-content-creation-review/)；[R31](https://www.pugetsystems.com/labs/articles/topaz-video-1-6-1-professional-gpu-performance-analysis/)；[R32](https://www.storagereview.com/review/nvidia-dgx-spark-cluster-review-distributed-inference-on-dell-gigabyte-and-hp)；[R33](https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/)；[R28](https://www.servethehome.com/diving-deeper-on-nvidias-vera-cpu-new-architectural-details-and-spec-cpu-2026-benchmarks/)；[R29](https://www.tomshardware.com/tech-industry/artificial-intelligence/behind-the-scenes-at-nvidias-engineering-superlab-vera-rubin-nvl72-running-openai-workloads-800vdc-demonstrated-and-more)。

这些研究用于约束文章判断，不是每段插一条“业内人士认为”。有意义的深度是解释差别为什么存在、结论在什么条件下成立。例如专业卡段落，可以用具体应用测试提醒读者“专业功能与任务表现要分开看”；没有必要插入和产品关系无关的资本开支议论。

## 四、价格核查与本轮边界

本轮复核了两个美国官方商城主商品页面，作为价格口径样本：GeForce RTX 5090 显示 **1,999 美元**；RTX PRO 6000 Blackwell Workstation Edition 显示 **16,000 美元**。两页均显示缺货，未验证结账和税运费。这些是核查日网页挂牌价，不是出厂批发价，也不保证可以买到。[R35](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/nvidia-geforce-rtx-5090/)；[R36](https://marketplace.nvidia.com/en-us/enterprise/laptops-workstations/nvidia-rtx-pro-6000-blackwell-workstation-edition/)

本轮没有完成全部型号的美国渠道询价、企业议价、云计费与税费核查。没有可靠公开出厂价时应写“未查到官方公开出厂价”，不能填媒体估算来补齐表格。正文大纲确认后再针对实际保留的型号建立价格附表；历史稿件报价不能自动继承为最新价格。

## 五、证据冲突和暂不采用的内容

- 官方来源也会出现页面错误。HGX 文档部分 CPU 行明显混入带宽字段；Marketplace 的关联商品卡片出现与专业产品目录不一致的显存信息。只采用无冲突且与具体产品对应的字段，错误表格不进入文章。
- Puget 最新 Topaz 测试的发布/更新日期字段有先后异常；测试软件也不是查询日最新版本。保留它对该版本的观察，不标成“最新软件性能”。
- 年报、发布会、当前目录分别说明历史业务、宣布计划和当前页面展示，不能把三者拼成一个无日期的“全系列”。
- 本轮没有逐个核查出口许可、地区供货、产品图片真伪，也没有获得所有企业采购价格。因而不交付“全球完整现货清单”或“全部芯片性能排名”。
- “七块就是全部”“H/B 只训练，L/T 只推理”“采用 DRIVE 就实现某等级自动驾驶”“大显存必然更快”等判断均不采用。

## 六、如何进入写作

接下来交给用户审核的是大纲及写作逻辑，而不是排版后的长文。正文只承担“建立产品关系、解释主要区别”这一件事；型号清单、规格口径与价格放查阅材料。下篇再展开云厂商、Token 交易及 AI 工厂运营。

[产品关系表](product-map.md)是研究索引，不要求读者阅读或背诵；[候选大纲](../../upper/outline-v11.md)才是建议的阅读路径。大纲尚未批准，未生成新正文、HTML 或图表。
