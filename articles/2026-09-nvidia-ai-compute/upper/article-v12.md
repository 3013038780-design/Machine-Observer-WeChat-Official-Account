# 算力生意（上）：英伟达的产品版图

> 内容提要：个人用户需要游戏、创作和本地 AI；企业团队需要设计、研发和部署；云厂商与算力运营商需要组织大规模计算；设备厂商则把计算装进机器人和汽车。英伟达围绕这些需求提供不同产品：从 GPU 等计算部件，到整机与系统，再到开发、部署和仿真软件。客户要完成的工作，决定了这些产品如何组合。

一个玩家购买显卡，是为了让游戏运行得更流畅；一家设计公司配置工作站，是为了让设计师处理复杂项目；一家提供 AI 服务的公司建设计算集群，是为了让大量用户能够持续调用模型。

他们都可能使用英伟达产品，但需要解决的问题不同，买到或使用的东西也不同。

有的人买的是一张卡，有的企业采购整套服务器，还有开发者通过云端使用硬件，同时借助软件工具完成工作。因此，理解英伟达的产品版图，可以先从客户的需求出发，再看这些需求怎样落到具体产品上。

## 一、个人用户：游戏、创作与本地 AI

### [GeForce RTX 50 Series](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/) [GeForce RTX 笔记本](https://www.nvidia.com/en-us/geforce/laptops/50-series/)

这里先分清两个容易混用的词。**GPU 是 Graphics Processing Unit，即图形处理器；显卡则是包含 GPU、显存、供电等组件的板卡。** GPU 负责计算，显卡将这些组件装在一起，供电脑使

GPU 擅长把适合拆分的运算分配给许多计算单元同时处理。画面渲染有大量这类工作，AI 中的许多计算也适合这种方式，所以同一类产品能同时服务游戏、创作和 AI。[Intel：GPU 与 CPU](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html)

但显卡不会独自完成全部工作。CPU，即 Central Processing Unit，中央处理器，运行通用程序、组织执行流程；系统内存保存程序正在使用的数据；硬盘或固态硬盘长期保存程序和文件。剪辑视频时，素材需要被读取、处理和输出，GPU 加速的是其中适合它的环节。[Intel：RAM 与处理器](https://www.intel.com/content/www/us/en/learn/what-is-ram-vs-processor.html) [Kingston：内存与存储](https://www.kingston.com/en/blog/pc-performance/difference-between-memory-storage)

软件配套也从这里出现。驱动帮助操作系统和应用使用显卡；NVIDIA Studio 则围绕创作应用提供工具与驱动支持。对于剪辑师和设计师，这些配套的意义是让熟悉的软件用上 GPU，而不只是再多一个产品名称。[NVIDIA Studio 创作者平台](https://www.nvidia.com/en-us/studio/)

### 想在电脑上运行 AI，为什么要看显存

个人用户也可以把模型放在本地运行，用来生成内容、处理资料或尝试开发。这时，限制任务的不只是 GPU 的计算速度，还有数据能否放得下、读取是否足够快。

独立显卡上的显存主要供 GPU 使用。它可以存放画面数据，也可以存放模型运行所需的数据。**显存容量回答“能放多少”，显存带宽回答“单位时间能传多少”。** 系统内存与显存则服务不同的访问路径，不能简单相加后当成同一块高速空间。[IBM：AI 基础设施术语](https://redbooks.ibm.com/docs/MD260021/MD260021.html)

如果任务需要的数据超出可用显存，可能要缩减任务规模，或借助其他内存与存储来运行；即使能运行，也可能增加传输和等待。反过来，当显存已经够用，再增加容量也未必更快。

这就是为什么，同一张 GeForce 显卡既能玩游戏，也能运行一定规模的 AI 任务，但不能仅凭它在游戏中的表现推算所有模型的运行速度。软件、数据规模和计算方式都会改变结果。

这一类客户通常接触的是**显卡或装有 GPU 的整台电脑，以及配套的应用、驱动和工具**。GeForce 是产品家族；Blackwell 等名称描述技术架构。比如 RTX 5090 是采用 Blackwell 架构的具体产品，两者不是两个并列的显卡型号。[RTX 5090 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)

## 二、企业专业团队：把设计和研发项目做出来

企业里的使用者可能是设计师、工程师、研究员或程序员。他们不一定使用同一种设备：专业设计关注项目与软件，模型研发还需要开发环境、实验和部署能力。

### 设计师与工程师：项目变大，设备要求随之变化

建筑设计、工程建模和影视制作可能涉及大型场景、复杂素材与指定的专业软件。工作站就是面向这类专业工作的计算机；RTX PRO 则是可以用于其中的专业 GPU 产品家族，并有面向其他部署形态的版本。需要携带设备工作的团队，还可以选择搭载 RTX PRO 笔记本 GPU 的移动工作站。[专业笔记本与移动工作站](https://www.nvidia.com/en-us/products/workstations/professional-laptops/)

RTX PRO 的价值包括部分型号提供的大显存，以及专业软件认证、企业驱动与支持。认证意味着针对专业应用进行兼容性验证，帮助企业选择和维护设备。它解决的是项目环境中的具体要求，并不意味着每一家企业都必须使用专业卡。[Professional Desktop GPUs](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/)

例如，桌面 RTX 5090 配备 **32 GB** 显存，RTX PRO 6000 Blackwell Workstation Edition 配备 **96 GB**。当项目需要同时容纳更多数据时，更大的空间可能改变任务能否在本机顺利完成。[RTX 5090 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/) [RTX PRO 6000 工作站版规格](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/)

不过，专业卡的价格和显存容量，不能直接代表每款软件的速度。工作站厂商 Puget Systems 在 Topaz Video 1.6.1 测试中发现，RTX PRO 5000 Blackwell 的 48 GB 与 72 GB 版本表现接近，差异处于测试误差范围内。对那组任务而言，增加显存没有带来明显提速。[Topaz Video 1.6.1 Professional GPU Performance Analysis](https://www.pugetsystems.com/labs/articles/topaz-video-1-6-1-professional-gpu-performance-analysis/)

因此，企业选型需要把项目要求与实际表现放在一起看：先确认能否容纳项目、能否满足软件和维护要求，再比较完成具体工作的效率。

### 研究员与程序员：从计算资源到开发工具

假设一个团队要开发文档识别应用。研究员需要准备数据、选择模型并评估效果；程序员需要把模型接入应用，让文件输入、计算执行和结果返回连成完整流程。这是一个说明分工的例子，实际团队可能由同一个人承担多项工作。

他们首先需要计算资源。较小的实验可以在本地电脑或工作站上进行，也可以使用 DGX Spark 这样的桌面 AI 计算机。**DGX Spark 是整台设备，RTX PRO 则是 GPU 产品家族**，两者不能按“哪张卡更强”来比较。[DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

DGX Spark 还采用 CPU 与 GPU 共享的统一内存。它能容纳多大的任务，与任务运行得多快，是不同问题。LMSYS 对早期 DGX Spark 的测试就提示，较大的内存空间不意味着所有模型都能高速运行；带宽和软件实现同样重要。[NVIDIA DGX Spark with SGLang](https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/)

有了硬件，还需要让程序调用它。**CUDA 是英伟达的并行计算平台与编程模型；CUDA Toolkit 是其中用于开发的工具包，包含编译、调试和加速库等工具。** 加速库可以理解为已经实现好的计算功能，开发者能够调用它们，减少从头编写底层程序的工作。[CUDA Toolkit](https://developer.nvidia.com/cuda/toolkit)

研究员或程序员既可以直接编写相关代码，也可以通过支持 GPU 的框架和应用间接使用 CUDA。CUDA 不属于某一种客户，也不限于一台工作站；它可以出现在个人电脑、企业服务器和云端的开发环境里。

当团队进入模型开发和上线阶段，还会遇到其他配套。训练用数据调整模型参数；微调是在已有模型基础上继续训练；推理则用模型处理新的输入。这些是 AI 工作中的关键活动，周围还有数据处理、评估和维护。

英伟达的 NeMo 提供模型开发、定制等工具，TensorRT 用于优化推理执行，NIM 将模型运行所需的组件封装为便于部署的服务。它们分别帮助开发者完成不同工作。NVIDIA AI Enterprise 则提供面向企业的相关软件与支持。[AI](https://www.nvidia.com/en-us/ai/)

模型本身又是一类资源，例如 Nemotron 系列。于是，一个研发团队使用的可能同时包括：**一台计算机、机器里的 GPU、CUDA 等工具，以及要开发或运行的模型。** 这些产品处在不同层级，却服务同一个项目。[DGX Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/)

团队把应用做出来以后，如果要让更多人持续使用，问题就会从“本机能否完成实验”扩大到“整套服务能否稳定运行”。

## 三、云厂商与算力运营商：组织大规模计算

云厂商、算力运营商，以及自建计算集群的企业和科研机构，需要管理大量计算资源。研究员和开发者在上面提交任务，运维团队则负责设备、网络和系统的持续运行。

算力中心是这些设施集中部署和运行的地方。它与“企业”不是互斥的客户类别：一家企业可以自建算力中心，也可以租用云上的资源。

### 使用者要完成任务，运营者要让资源有效协作

这些客户可能需要训练模型、提供推理服务，也可能运行科学计算或图形任务。A100、H100、H200、Blackwell 系列的 B200、B300，以及当前官方介绍的 Rubin 平台，都属于理解数据中心产品时会遇到的名称。不同产品和代际可以服务不同系统需求。[Data Center](https://www.nvidia.com/en-us/data-center/) [HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/)

数据中心 GPU 通常需要放在相应的系统配置中理解：内存容量、带宽、设备间互连和软件配套共同影响任务表现。一些产品采用 HBM，即 High Bandwidth Memory，高带宽内存，通过堆叠等技术支持大量数据传输。HBM 描述内存技术，不是 GPU 的另一个档次。[Micron：HBM](https://www.micron.com/products/memory/hbm)

训练和推理也不能严格按型号字母划线。A100 同时支持训练与推理，L40S 还覆盖图形、视频与 AI 等工作。运营者需要看实际任务，再决定怎样配置资源。[NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/) [NVIDIA L40S](https://www.nvidia.com/en-us/data-center/l40s/)

比如，一个服务希望尽快回答单个请求，另一个服务希望同时处理更多请求，二者的运行安排可能不同。CoreWeave 的部署文档就要求根据真实请求测试并发设置，权衡响应速度与整体处理量。[CoreWeave：推理扩容](https://docs.coreweave.com/products/inference/scaling)

增加 GPU 数量有时能扩大容量，但如果计算之间需要频繁交换数据，连接速度也会影响效果。

针对不同服务要求，专用加速硬件也在发展。英伟达已公布 Groq 3 LPX 量产信息，其中的 LPU 是面向推理的专用处理器，LPX 是系统名称。它展示了针对特定计算需求设计硬件的方向；具体表现仍应在相应任务和部署条件下比较。[Groq 3 LPX Now in Full Production](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)

### 运维团队面对的是完整系统

CPU 在这里继续负责通用程序、数据与执行流程。英伟达的 Grace、Vera 是 CPU 产品；BlueField 则属于 DPU，Data Processing Unit，数据处理单元，承担部分网络、存储和安全处理工作。它们与 GPU 各有分工。[Data Center](https://www.nvidia.com/en-us/data-center/) [HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html)

多张 GPU 还需要高速互连。NVLink 与 NVLink Switch 连接计算部件；ConnectX 网络适配器、Spectrum-X 以太网平台和 Quantum InfiniBand 网络产品，则参与更大范围的设备通信。[NVLink and NVLink Switch](https://www.nvidia.com/en-us/data-center/nvlink/) [Networking Products](https://www.nvidia.com/en-us/networking/products/)

对于运维团队，这些名字对应一个很实际的问题：GPU 算完自己的部分以后，能否及时取得其他设备的数据？等待越多，计算资源就越难被充分利用。这也使**显存带宽、GPU 互连带宽、服务器网络带宽**成为不同指标，分别描述不同位置的数据传输能力。

系统采购中常见的 HGX、MGX、DGX，也各有含义。**HGX 是多 GPU 计算平台**，服务器厂商围绕它配置 CPU、内存、存储等，形成完整设备。

**MGX 是模块化系统参考架构**，为厂商设计和组合系统提供基础。

**DGX 是英伟达的系统家族**，DGX SuperPOD 则涉及更大规模的集成方案。[HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) [MGX](https://www.nvidia.com/en-us/data-center/products/mgx/) [DGX Platform](https://www.nvidia.com/en-us/data-center/dgx-platform/)

再看 GB200：它将 Grace CPU 与 Blackwell GPU 组合成计算单元；GB200 NVL72 将这些计算单元与互连组织成机柜级系统。**GPU 是部件，计算单元是组合，服务器与机柜系统则包含更完整的配置。** 部件越来越多，系统对供电、散热和运行维护的要求也随之增加。[GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)

这时再比较报价，才有明确对象：显卡价对应一张卡；服务器价要看整机配置；机柜系统价要看设备和配套范围。把它们安装好、运行起来并完成任务，还需要相应的机房条件与运营投入。

### 服务规模扩大，软件配套也在延伸

研发阶段的工具会继续进入生产环境，但运营团队还需要管理任务、监测设备、处理故障。计算能力最终通过整套硬件和软件交付给使用者，而不是把多张 GPU 放在一起就自然成为服务。

云上的产品还要看实际提供者与服务范围。截至本文核查日，DGX Cloud 官方页面将其描述为英伟达内部的 AI 开发与运行环境，并介绍与云伙伴及相关运维软件的关系。它不能仅凭“Cloud”这个名字，就与所有云厂商的对外服务直接等同。[DGX Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/)

客户可以通过不同形式取得这些能力：使用远端计算资源、自行部署模型，或调用已经部署好的服务。

## 四、设备与汽车厂商：把计算能力装进产品

对机器人、工业设备和汽车厂商来说，计算不仅发生在办公室或机房，也发生在正在执行任务的设备上。产品需要读取传感器数据，作出判断，并与设备的其他系统配合。

### 产品工程师需要设备侧计算平台

Jetson 面向嵌入式和机器人应用，Orin、Thor 等家族提供计算模块，配合开发套件和软件。模块是供厂商集成的计算组件，开发套件帮助工程师开发与测试；最终机器人还需要传感器、执行机构以及整机软件等。[Jetson Embedded Systems](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/)

这种在数据产生的位置附近运行计算的方式，通常称为边缘计算。它让设备可以在本地处理部分任务，减少对远端传输与连接条件的依赖。

工业设备还要考虑持续运行、安全和维护。IGX 将工业级硬件与企业软件支持结合起来，部分配置提供独立安全处理能力，服务工业等边缘部署要求。[IGX](https://www.nvidia.com/en-us/edge-computing/products/igx/)

汽车厂商则会遇到 DRIVE：DRIVE AGX 提供车载计算开发平台，DriveOS 提供软件基础，Hyperion 涉及计算和传感器等参考设计。车辆最终能完成什么驾驶任务，还取决于整车软件、传感器、集成与验证。[Autonomous Vehicles](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/)

因此，这类客户使用的是**可集成的硬件模块、开发平台及软件配套**，并不是购买一张显卡就获得一台完整机器人或一套成车能力。

### 研发团队还需要训练与仿真

假设一家企业开发抓取物体的机器人。算法团队需要准备数据、训练或调整模型；仿真与测试人员需要检查它在不同条件下的表现；产品工程师再把程序部署到设备上，并继续验证实际效果。

这条过程会同时用到前面讲过的多种产品：数据中心系统承担训练，仿真软件帮助测试，设备侧计算平台运行任务。**客户始终是开发机器人的企业，但它的产品组合跨越部件、系统和软件。**

Omniverse 提供三维与物理仿真应用所需的库、接口和服务；Isaac 围绕机器人开发提供仿真、学习等工具。它们与 Jetson 配合，服务从研发到部署的不同环节。[Omniverse](https://www.nvidia.com/en-us/omniverse/) [Isaac](https://developer.nvidia.com/isaac)

英伟达机器人业务负责人 Deepu Talla 在访谈中强调了数据、训练、仿真和部署之间的联系。这解释了为什么设备厂商除了购买机器内部的计算模块，还可能需要机房中的计算资源与仿真工具：把设备做出来之前，就有大量计算工作需要完成。[Deepu Talla About Physical AI and Robotics](https://www.chipstrat.com/p/an-interview-with-nvidias-deepu-talla)

从个人电脑到企业研发，再到算力运营与设备制造，英伟达的产品随着客户的工作而组合。个人可能通过现成应用使用 GPU，开发者借助软件工具安排计算，运营团队管理整套系统，设备厂商则把计算集成进自己的产品。

**读懂这张版图，要同时看清谁在使用，以及使用的是哪一层产品。** 这也为理解下一步的算力交易建立了基础：阿里云、腾讯云怎样提供计算与模型服务，Token 如何计费，AI 工厂怎样组织设备与运行过程，将在下篇接着讨论。

---

## 附：基础概念速查

| 名称 | 英文及含义 | 在本文中的作用 |
|---|---|---|
| CPU | Central Processing Unit，中央处理器 | 运行通用程序，组织执行流程并处理数据 |
| GPU | Graphics Processing Unit，图形处理器 | 加速适合并行处理的图形、AI 等计算 |
| 系统内存 | 通常所说的 RAM：Random Access Memory，随机存取存储器 | 程序运行时的工作空间 |
| 显存 | VRAM：Video Random Access Memory | 供 GPU 使用的内存，存放图形或计算所需数据 |
| 显存带宽 | Memory bandwidth | GPU 与显存之间单位时间的数据传输能力 |
| GPU 互连带宽 | GPU interconnect bandwidth | GPU 之间交换数据的能力 |
| DPU | Data Processing Unit，数据处理单元 | 处理部分网络、存储和安全基础设施任务 |

系统内存与 GPU 内存的划分依设备设计而异；采用统一内存的系统不能按独立显卡的方式简单相加。[Intel：GPU 与 CPU](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html) [Intel：RAM 与处理器](https://www.intel.com/content/www/us/en/learn/what-is-ram-vs-processor.html) [IBM：AI 基础设施术语](https://redbooks.ibm.com/docs/MD260021/MD260021.html) [HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) [NVLink and NVLink Switch](https://www.nvidia.com/en-us/data-center/nvlink/)

## 附：两种官方价格口径样本

查询日期：2026年9月12日，美国官方商城。这里是网页挂牌价，不是出厂批发价；页面均显示缺货，税费、运费及实际成交价未确认。

| 具体商品 | 页面挂牌价 | 买到的层级 |
|---|---|---|
| GeForce RTX 5090 | 1,999 美元 | 桌面显卡 |
| RTX PRO 6000 Blackwell Workstation Edition | 16,000 美元 | 专业工作站显卡 |

来源：[GeForce RTX 5090 marketplace](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/nvidia-geforce-rtx-5090/) [RTX PRO 6000 Blackwell Workstation Edition marketplace](https://marketplace.nvidia.com/en-us/enterprise/laptops-workstations/nvidia-rtx-pro-6000-blackwell-workstation-edition/)。这两项只能展示具体商品的公开价格，不能据此推算服务器或机柜成本。数据中心设备应按完整配置取得报价；本次核查未获得这些系统可直接套用的官方公开出厂价。
