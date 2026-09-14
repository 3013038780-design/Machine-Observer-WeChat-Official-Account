# 从汽车到机器人：英伟达产品用途深度调研

研究截止：2026-09-14。状态：研究报告，非公众号正文；候选标题与大纲待审核。

## 一、研究结论

本篇最值得解释的，是英伟达如何参与机器从开发到实际工作的过程。车企需要让车辆识别道路并执行驾驶功能；机器人厂商需要让机器完成移动、抓取等动作；工厂与仓库则需要让设备适应现场流程。围绕这些工作，英伟达提供设备端计算、开发工具、模型和仿真能力。采用其中一层，不能推断采用整套方案。

这条判断有具体证据：奔驰披露同时采用DRIVE计算与驾驶软件；波士顿动力则把Jetson Thor与自己的控制器结合；西门子把Omniverse能力嵌入自身工业软件。三者呈现不同的产品组合，不能写成统一采购流程。[^S01][^S19][^S37]

本文建议沿“谁在完成什么工作”组织，而不是逐个解释缩写。汽车、机器人和工厂不是严格互斥的行业：宝马既制造汽车，也运营工厂；机器人厂商开发设备，仓库企业购买和使用设备。正文必须在角色切换处说明这一点。

研究支持三个更深入的判断：

- **设备上的芯片只是交付的一部分。** 模型、控制软件、传感器、机械结构和集成共同影响结果。
- **仿真能帮助开发和测试，但现实环境仍是检验标准。** 画面逼真不等于接触、摩擦、传感器误差等都准确。
- **演示成功与持续生产存在距离。** 商业应用既看任务成功率，也看速度、维护和接入流程的成本。后两项不是增加一个模型就自然解决的。

这些是对案例、访谈与综述的综合分析，不是已量化的全行业结论。[^S27][^S29]

## 二、车企：开发车辆的驾驶功能

### 任务与产品关系

以辅助驾驶为例，车辆需要处理摄像头等传感器输入，识别环境，计算行驶决策，并通过整车系统执行。这包含计算硬件和不同层级的软件；研发阶段还涉及数据、模型开发和测试。

**Orin、Thor是芯片层面的名称；DRIVE AGX是计算平台及相应开发套件。** 它们不能直接理解为插进汽车的一张游戏显卡。相关芯片集成CPU、GPU等计算单元，开发平台另提供接口和软硬件环境。量产车型使用的控制器配置应以车企和供应商资料为准，不能照搬开发套件规格。[^S03]

软件也需分层：**DriveOS**提供底层软件环境和接口；**DRIVE AV**面向驾驶功能；**Hyperion**是包含计算、传感器等要素的开发与参考平台。它们不是三个同类芯片，也不是车企必须依次购买的套餐。支持某项安全标准或面向某类自动驾驶开发，不等于搭载它的每辆车已经获准无人驾驶。[^S04][^S05]

### 主案例：奔驰，芯片与驾驶软件分别买到了什么

奔驰2026年1月公告明确介绍MB.DRIVE ASSIST PRO使用NVIDIA DRIVE AV软件和DRIVE AGX计算。其定位为SAE Level 2驾驶辅助，不能写成无人驾驶。这一案例适合说明英伟达既能提供计算平台，也能参与上层驾驶软件。公告中的地区推出计划应保留原时点，本轮没有据此确认美国截至9月的实际交付。[^S01]

补充案例可用沃尔沃EX90。加拿大支持页介绍2025款车更换核心计算机、升级双Orin的安排，说明某些功能演进需要实体硬件升级。这支持“软件能力与硬件条件互相约束”，但不支持“所有车型都必须换芯”或“沃尔沃使用奔驰同一套驾驶软件”。[^S02]

### 模型在什么位置

**Alpamayo是自动驾驶研发相关模型与工具体系。** 当前可取得的Alpamayo 2 Super权重于2026年8月发布。它可进入研发流程，不能仅凭模型发布就认定某款量产车已采用。模型商业使用许可也不是车辆道路运行许可。正文可以用一句话介绍该层，型号参数留在附录。[^S06][^S07]

需要保留替代路径。小鹏2026年1月官方材料介绍自研Turing芯片，足以证明车企还会走自研计算路线；但不能推断所有小鹏车型、地区和版本都已切换。这里的Turing也不能与英伟达历史GPU架构混淆。[^S33]

**本节可成立的结论：** 英伟达向车企提供不同深度的技术参与，具体车型采用哪层，需要逐项核查。

## 三、机器人厂商：让机器完成动作

### 从任务解释开发，而不是从“机器人大脑”开始

以取放物品为解释性例子，机器需要识别目标、确定动作，并控制机械结构执行。换一种物体、夹具或工作环境，原有策略未必直接适用。因此，“能运行模型”“模型能给出动作”“设备能稳定完成工作”是不同的验证层次。

**Jetson是面向机器人等设备的嵌入式计算产品家族。** 开发者可以买模块，把它集成进自己的设备，也可以使用开发套件开展实验；两者都不等于带有机械臂、关节和传感器的完整机器人。当前目录涵盖Orin及Thor系列，JetPack则提供相关开发软件。正文不需要把所有功耗和算力列一遍。[^S09][^S10][^S11]

**Isaac是一组机器人开发工具。** Isaac Sim用于搭建模拟环境；Isaac Lab用于机器人学习研究与训练；Isaac ROS提供基于开源ROS 2的加速软件包。它们分别解决问题，不能写成下载Isaac就得到一个通用机器人。ROS 2本身也不是英伟达专有产品。[^S13][^S14]

**GR00T包含机器人模型及参考开发平台。** 具体模型可以接收图像、语言与机器人状态，输出动作相关结果，但还需要面向设备和任务适配。官方取放教程涉及采集示范、整理数据、训练和评估，正好能说明开发过程。教程中的一次成功日志不是工业可靠性证明。[^S15][^S35]

### 主案例：Atlas，各家的技术怎样结合

波士顿动力2025年公告写明，Atlas将Jetson Thor与自身的全身及操作控制器结合，并采用Isaac Lab开展技能研发。这是解释“计算平台与机器人控制并非同一个产品”的清晰证据。2026年1月官方又宣布产品版Atlas及当年部署计划，但计划不能当作已完成的交付清单。[^S19][^S20]

该公司的模型合作还包括Google DeepMind，因此不应从采用Jetson推出整机采用GR00T。正文不必列所有合作商，只需要明确：机器人厂商仍负责自己的机器结构、控制、产品化与集成。

Agility的Digit可作为旁证：公司披露使用Isaac Sim和Isaac Lab开展训练测试，以及机载计算加速。原文没有给出对应芯片具体型号，本篇也不补猜。[^S21]

### 应怎样理解“物理AI”

本文可把这一概念简要解释为：AI参与感知现实环境，并指导车辆、机器人等实体系统行动。它不是所有工业自动化的总称，也不意味着传统控制方法消失。

Cosmos提供世界模型及相关数据能力，可帮助开发涉及环境理解、生成和预测的应用；GR00T则更直接面向机器人行为。Omniverse的仿真与三维工具又是另一层。为避免正文再次变成名字清单，Cosmos可放入开发过程的补充说明，不另开平级章节。[^S17]

还应修正旧式绝对说法：不能写“英伟达从不提供机器人”。2026年公布的GR00T研究参考机器人整合了合作伙伴机械本体、手部与计算软件。准确表述是：英伟达主要提供基础技术与平台，也提供面向研究的集成参考设计；这不等于已销售适用于所有任务的大众消费机器人。[^S16]

## 四、工厂与仓库运营方：让设备适应现场

### 为什么这一节与前两节不同

机器人厂商关心一台设备怎样完成任务；运营方还要考虑设备放在哪里、路线会不会冲突、现有生产线能否配合、停机如何影响流程。同一家车企在这里是工厂运营者，讨论对象由车内功能转为生产现场。

**Omniverse是一组可供开发和集成的库、API与服务。** 它支持三维数据、渲染与仿真等能力；企业可能通过合作伙伴软件使用这些能力，而不是单独购买一款名叫Omniverse的完整工厂管理软件。西门子Teamcenter Digital Reality Viewer是具体例子。[^S18][^S23][^S37]

### 主案例：宝马，先在虚拟产线检查碰撞

宝马Virtual Factory结合生产相关数据和三维环境，用于规划与检查。例如，新车身在产线中移动和转动时，是否会与既有设备碰撞。这个问题比“建立工业元宇宙”更具体，也直接解释了为什么需要虚拟工厂。[^S22]

正文建议不采用大幅降本数字作为开场。宝马所说最高30%的规划成本降幅是预期，范围是生产规划，不是整车成本，也不是独立审计后的全集团实际结果。

### 补充案例：仓库里的叉车与流程

KION与NavVis、NVIDIA的案例说明数字孪生需要现实数据：先获取仓库空间与设备信息，再用于模拟和优化。数字孪生在此可解释为“用于分析实际设施的数字化对应环境”，不是把仓库画得漂亮就完成了。[^S24]

KION在2026年3月介绍了GXO法国仓库的自主工业车辆试点。必须保留“试点”状态；同一公告中另一个涉及IGX Thor的视频监测与装卸项目仍有后续概念验证计划，不能合并为一套已经全面运行的方案。[^S25]

**IGX是面向工业等边缘场景的计算平台，包含软硬件及支持。** “边缘”在这里指靠近设备与现场处理数据。它与Jetson服务范围有交叉，但不能只凭Thor同名就视作可互换产品；具体系统仍取决于接口、软件、支持和集成要求。[^S12]

**本节可成立的结论：** 工业客户购买的是解决现场问题的组合能力，英伟达可能位于设备内部，也可能位于规划和仿真软件内部。

## 五、访谈和研究提供了哪些深度

本轮阅读了三份公开文字访谈，并检查一篇机器人仿真综述的相关章节；没有把会议入口或搜索摘要当作已看完的视频。

| 资料 | 可用观点 | 使用边界 |
|---|---|---|
| Chipstrat采访Deepu Talla | 训练、仿真、设备运行需要配合，机器人落地涉及集成 | NVIDIA高管观点，不能当作独立市占率调查 |
| AIhub采访Ken Goldberg | 学习方法与传统工程结合；成功率和动作时间都影响生产价值 | 研究者兼创业者，存在产业合作背景 |
| McKinsey采访David Reger | 机器人形态应服务任务，真实感知和数据仍重要 | 受访CEO主张，不等于麦肯锡完成了对应实证 |
| 机器人仿真差距综述 | 模拟与现实存在差距，评估需要现实校准 | 作者含高校与NVIDIA，本轮未复现实验 |

据此，正文的行业分析应嵌入具体问题：Atlas案例后解释“成功一次与持续操作的区别”；宝马案例后解释“模型和数据准确性影响验证结果”。不另堆一个观点名言章节。[^S26][^S27][^S28][^S29]

“三类计算”可以作为开发活动的总结，但不能画成每家企业都必须购买三台指定计算机。训练与仿真可使用本地或租用资源，也可以复用已有模型；设备运行与开发资源的组织方式随项目变化。这是本篇的编辑归纳，不是采购处方。

## 六、实际覆盖率：证据能支持到哪里

本轮找到明确客户采用证据，但未找到能统一衡量DRIVE、Jetson、Isaac与Omniverse全行业使用比例的公开统计。它们分别是芯片/平台、软件和工具，分母本就不同。

IFR公开资料中的2024年工业机器人安装量没有记录英伟达软硬件采用比例，不能据此推算市占率。中国智驾芯片报道还存在全阶智驾与城区NOA等分母差异；仅有转载、拿不到原始报告方法的数字，本轮只保存为线索。ADAS供应商排名也不是芯片厂商排名。[^S30]

可以写“奔驰、波士顿动力、宝马等披露了相应采用案例”；暂不能写“绝大多数汽车和机器人都依赖英伟达”“Isaac已成为所有厂商标准工具”。市场覆盖率没有可靠数值，不影响本文解释已验证的产品用途。

## 七、核查中需要保留的冲突与空白

1. **Alpamayo参数口径：** 产品页32B与34B并见；模型卡区分骨干与动作专家。正文省去参数，不能把两个口径做成产品性能差异。[^S06][^S08]
2. **GR00T许可：** 技术博客、代码仓库和模型卡许可表述并不完全一致。代码许可不能替代模型权重许可，正文不写“全部Apache、随意商用”。[^S15][^S35][^S36]
3. **峰值比较：** Jetson Thor的FP4稀疏指标不能与Orin INT8指标直接计算性能提升倍数。未自行跑应用测试。[^S09]
4. **供货与价格：** 目录和发布公告不等于当前库存；本轮没有获取统一官方出厂报价。文章以用途为中心，暂不增加不必要的采购价格表。
5. **商业阶段：** 新模型可下载、产品版宣布制造、客户试点和规模运营应分开标注。历史公告不能自动更新成截至今日全部兑现。
6. **补证线索：** 极氪车型配置、智驾芯片原始统计、GTC会议完整内容尚未形成足够正文证据，不列为已完成阅读的材料。

## 八、建议文章取舍

正文重点保留DRIVE、Jetson、Isaac、Omniverse四组名称，围绕三个客户任务解释。DriveOS、Alpamayo、GR00T、Cosmos、IGX按解释需要出现，其他配置和参数进入资料附录。汽车与机器人都涉及模型，但不要重复一遍前篇的训练/推理基础课。

Token如何计费、云服务如何出售推理能力、AI工厂如何运营，留给另一篇。本文里的实体工厂指生产与物流现场，不能与AI工厂的算力设施隐喻混用。

下一阶段按待审大纲写完整纯文字稿，再核查最终入稿的每条数字、案例状态和引用。当前研究资料不等于已批准的文章。

## 参考来源

以下列出本报告采用来源；其余线索与阅读限制见sources.md。

[^S01]: Mercedes-Benz Group，[MB.DRIVE ASSIST PRO: Navigation and driving assistance merge](https://group.mercedes-benz.com/technology/autonomous-driving/driving/mb-drive-assist-pro.html)。2026-01-07；查询：2026-09-14。

[^S02]: Volvo Cars，[Upgrading your EX90 with a new core computer](https://www.volvocars.com/en-ca/support/topic/521df97778e745b59da7a40ec0b7ac6f/cfb088af0b44449a32dd1f562cbc7391/47d2c97fd33effd3c0a8cc3718c999b7-ee74549933d85020c0a83205327890cd-8664b2fa77a7e089c0a8296870d1a409/)。动态支持页；查询：2026-09-14。

[^S03]: NVIDIA，[DRIVE AGX Developer Kits](https://developer.nvidia.com/drive/agx)。动态产品页；查询：2026-09-14。

[^S04]: NVIDIA，[NVIDIA DRIVE OS](https://developer.nvidia.com/drive/os)。动态产品页；查询：2026-09-14。

[^S05]: NVIDIA，[Development Platform for Robotaxis and L4 Autonomous Vehicles](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/drive-hyperion/)。动态产品页；查询：2026-09-14。

[^S06]: NVIDIA / Hugging Face，[Alpamayo 2 Super Model Card](https://huggingface.co/nvidia/Alpamayo2-Super)。权重发布2026-08-04；查询：2026-09-14。

[^S07]: Jessica Soares / NVIDIA，[NVIDIA Alpamayo 2 Super ... Now Available for Commercial Use](https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/)。2026-08-04；查询：2026-09-14。

[^S08]: NVIDIA，[High-Performance Compute for Robotaxis & Autonomous Vehicles](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/in-vehicle-computing/)。动态产品页；查询：2026-09-14。

[^S09]: NVIDIA，[Jetson Thor](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)。动态产品页；查询：2026-09-14。

[^S10]: NVIDIA，[Jetson AGX Thor Developer Kit User Guide: Introduction](https://docs.nvidia.com/jetson/agx-thor-devkit/user-guide/latest/)。latest动态文档；查询：2026-09-14。

[^S11]: NVIDIA，[NVIDIA Jetson Modules](https://developer.nvidia.com/embedded/jetson-modules)。动态目录；查询：2026-09-14。

[^S12]: NVIDIA，[IGX Enterprise-Ready Platform](https://developer.nvidia.com/igx)。动态文档；查询：2026-09-14。

[^S13]: NVIDIA，[Isaac - AI Robot Development Platform](https://developer.nvidia.com/isaac/)。动态目录；查询：2026-09-14。

[^S14]: NVIDIA，[NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab)。动态产品页；查询：2026-09-14。

[^S15]: Edith Llontop、Brandon Neel / NVIDIA，[Develop Humanoid Robot Policies End-to-End with NVIDIA Isaac GR00T](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)。2026-07-07；查询：2026-09-14。

[^S16]: NVIDIA，[NVIDIA Announces NVIDIA Isaac GR00T Reference Humanoid Robot for Academic Research](https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design)。2026-05-31；查询：2026-09-14。

[^S17]: NVIDIA，[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)。动态目录；查询：2026-09-14。

[^S18]: NVIDIA，[Develop Physical AI Applications: NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)。动态目录；查询：2026-09-14。

[^S19]: Boston Dynamics，[Boston Dynamics Expands Collaboration with NVIDIA](https://bostondynamics.com/news/boston-dynamics-expands-collaboration-with-nvidia/)。2025-03-18；查询：2026-09-14。

[^S20]: Boston Dynamics，[Boston Dynamics Unveils New Atlas Robot to Revolutionize Industry](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/)。2026-01-05；查询：2026-09-14。

[^S21]: Agility，[Agility Robotics Expands Relationship with NVIDIA](https://www.agilityrobotics.com/content/agility-robotics-expands-relationship-with-nvidia)。2025-03-18；查询：2026-09-14。

[^S22]: Moritz Schmerbeck / BMW Group，[BMW Group scales Virtual Factory](https://www.press.bmwgroup.com/global/article/detail/T0450699EN/bmw-group-scales-virtual-factory)。2025-06-11；查询：2026-09-14。

[^S23]: Siemens，[Siemens and NVIDIA in strategic partnership](https://www.siemens.com/en-us/company/artificial-intelligence/siemens-nvidia-partnership/)。动态页，含2026年7月条目；查询：2026-09-14。

[^S24]: KION，[How KION, NavVis, and NVIDIA are Collaborating on Industrial Digital Twins](https://www.kiongroup.com/en/Newsroom/Story-Categories/Innovation/Article/How-KION-NavVis-and-NVIDIA-are-Collaborating-on-Industrial-Digital-Twins.html?storyid=61568)。2026-02-11；查询：2026-09-14。

[^S25]: KION，[KION brings physical AI into live warehouse operations at GTC 2026](https://www.kiongroup.com/en/Press/Press-Releases/Press-Releases-Detail.html?id=1099696911&title=KION+brings+physical+AI+into+live+warehouse+operations+at+GTC+2026+in+San+Jos%EF%BE%83%EF%BD%A9,+California&type=corporate)。2026-03-16；查询：2026-09-14。

[^S26]: Austin Lyons / Chipstrat，[An Interview with Nvidia's Deepu Talla About Physical AI and Robotics](https://www.chipstrat.com/p/an-interview-with-nvidias-deepu-talla)。2026-05-25；查询：2026-09-14。

[^S27]: Ella Scallan / AIhub，[Combining cultures, from code to canvas: an interview with Ken Goldberg](https://aihub.org/2026/09/01/combining-cultures-from-code-to-canvas-an-interview-with-ken-goldberg/)。2026-09-01；查询：2026-09-14。

[^S28]: Christian Jansen采访David Reger / McKinsey，[The robotics tipping point: Physical AI and the race to scale](https://www.mckinsey.com/industries/industrials/our-insights/the-robotics-tipping-point-physical-ai-and-the-race-to-scale)。2026-04-22；查询：2026-09-14。

[^S29]: Elie Aljalbout等，[The Reality Gap in Robotics: Challenges, Solutions, and Best Practices](https://arxiv.org/html/2510.20808v1)。arXiv v1 2025-10-23；文内注明2026综述；查询：2026-09-14。

[^S30]: International Federation of Robotics，[Global Robot Demand in Factories Doubles Over 10 Years](https://ifr.org/ifr-press-releases/global-robot-demand-in-factories-doubles-over-10-years)。2025-09-25，统计2024年；查询：2026-09-14。

[^S33]: XPENG，[AI in Motion: XPENG Unveils Physical AI Vision and its G6 Air at 2026 Singapore Motorshow](https://www.xpeng.com/pressroom/news/019bc56e17389bc16cb78a028c710035)。2026-01-08；查询：2026-09-14。

[^S35]: NVIDIA / Hugging Face，[GR00T-N1.7-3B Model Card](https://huggingface.co/nvidia/GR00T-N1.7-3B)。动态模型卡；查询：2026-09-14。

[^S36]: NVIDIA / GitHub，[Isaac-GR00T repository](https://github.com/NVIDIA/Isaac-GR00T)。动态main；查询：2026-09-14。

[^S37]: Siemens，[Introducing Teamcenter Digital Reality Viewer](https://blogs.sw.siemens.com/teamcenter/introducing-teamcenter-digital-reality-viewer/)。页面日期见原文；查询：2026-09-14。
