# 算力生意（上）：英伟达的产品版图

> 内容提要：个人用户需要游戏、创作和本地 AI；企业团队需要设计、研发和部署；云厂商与算力运营商需要组织大规模计算；设备厂商则把计算装进机器人和汽车。英伟达围绕这些需求提供不同产品：从 GPU 等计算部件，到整机与系统，再到开发、部署和仿真软件。客户要完成的工作，决定了这些产品如何组合。

一个玩家购买显卡，是为了让游戏运行得更流畅；一家设计公司配置工作站，是为了让设计师处理复杂项目；一家提供 AI 服务的公司建设计算集群，是为了让大量用户能够持续调用模型。

他们都可能使用英伟达产品，但需要解决的问题不同，买到或使用的东西也不同。

有的人买的是一张卡，有的企业采购整套服务器，还有开发者通过云端使用硬件，同时借助软件工具完成工作。因此，理解英伟达的产品版图，可以先从客户的需求出发，再看这些需求怎样落到具体产品上。

## 一、个人用户：游戏、创作与本地 AI

### 玩家和创作者，用到的是怎样一套电脑

对玩家来说，显卡影响游戏画面的计算与呈现；对视频和三维创作者来说，它可以加速部分制作、渲染和导出工作。GeForce 是英伟达面向个人电脑的主要 GPU 产品家族，RTX 50 系列从 RTX 5050 延伸到 RTX 5090，覆盖不同定位；笔记本还有相应产品，具体规格需与桌面版分别看。[GeForce RTX 50 Series](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/)

个人用户也可以选择搭载 GeForce RTX 笔记本 GPU 的整机，用于游戏、创作和本地 AI。[GeForce RTX 笔记本](https://www.nvidia.com/en-us/geforce/laptops/50-series/)

这里先分清两个容易混用的词。**GPU 是 Graphics Processing Unit，即图形处理器；显卡则是包含 GPU、显存、供电等组件的板卡。** GPU 负责计算，显卡将这些组件装在一起，供电脑使用。

GPU 擅长把适合拆分的运算分配给许多计算单元同时处理。画面渲染有大量这类工作，AI 中的许多计算也适合这种方式，所以同一类产品能同时服务游戏、创作和 AI。[Intel：GPU 与 CPU](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html)

但显卡不会独自完成全部工作。CPU，即 Central Processing Unit，中央处理器，运行通用程序、组织执行流程；系统内存保存程序正在使用的数据；硬盘或固态硬盘长期保存程序和文件。剪辑视频时，素材需要被读取、处理和输出，GPU 加速的是其中适合它的环节。[Intel：RAM 与处理器](https://www.intel.com/content/www/us/en/learn/what-is-ram-vs-processor.html) [Kingston：内存与存储](https://www.kingston.com/en/blog/pc-performance/difference-between-memory-storage)

软件中的任务由 CPU、GPU 等部件分工处理，并非所有操作都会因为显卡升级而变快。驱动帮助操作系统和应用使用显卡；**NVIDIA Studio 是面向创作者的软硬件配套体系**，包含创作工具、Studio 驱动和相关设备支持。剪辑师仍在使用 Premiere、达芬奇等软件，Studio 提供的是背后的配套，并不是另一款剪辑软件。[NVIDIA Studio 创作者平台](https://www.nvidia.com/en-us/studio/)

### 个人使用 AI 的两种常见方式

个人使用 AI，既可以通过官方网站或应用访问在线服务，也可以将支持本地部署的模型下载到自己的电脑。两种方式的主要区别，在于模型由谁运行、计算资源由谁提供。

**1. 使用在线 AI 服务**

通过 ChatGPT、Kimi 等官方网站或应用，用户可以直接提问、提交资料并获取结果，无需自行安装和维护模型。模型的主要计算在服务商的云端完成，本机主要承担输入、文件传输和结果展示等工作。

视频生成也是如此。例如，通过在线服务使用 Seedance 时，生成任务由云端处理，速度主要取决于服务端的计算与调度。将生成的视频下载到本地后，剪辑、特效和渲染等环节才可能进一步使用本机 GPU。[火山引擎：Seedance API 服务](https://developer.volcengine.com/articles/7628567056649125942)

在线服务省去了模型安装和设备维护，适合日常问答、写作和资料整理。对于这类使用方式，本地显卡通常不是决定模型生成速度的主要因素。

**2. 在本地部署模型**

本地部署是将模型文件和运行软件下载到自己的设备，由本机完成模型计算。支持这种方式的常见模型包括：

| 模型例子 | 主要用途 |
|---|---|
| 通义千问 Qwen，例如 Qwen3 的较小版本 | 对话、文本处理与代码辅助 |
| DeepSeek-R1 的蒸馏版本 | 推理、数学和代码等任务 |
| Stable Diffusion，例如 SDXL | 根据文字生成图片 |

这些模型提供可下载的权重，即模型训练得到的参数，具体使用范围以许可证为准。其中，蒸馏版是学习较大模型能力的较小模型，便于在资源更有限的设备上运行，但不等同于完整在线服务。[Qwen 官方说明](https://github.com/QwenLM/Qwen3) [DeepSeek-R1 官方说明](https://github.com/deepseek-ai/DeepSeek-R1) [SDXL 官方模型页](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)

本地部署主要满足对数据位置、离线使用和模型控制的要求。例如，处理不便上传的资料时，可以让模型与相关工具全部在本地运行；开发者也可以固定模型版本、调整运行参数，或在许可范围内微调模型。离线运行需要提前准备好模型和必要软件，处理过程也不能依赖外部服务。

相应地，用户需要承担设备、配置和维护成本。本地模型的能力与速度受硬件条件限制，长期使用是否更经济，也要综合计算硬件、电费和维护投入。因此，是否部署应由具体需求决定；日常使用在线服务已经能够完成的任务，无须仅为使用 AI 而额外购置显卡。

### 本地模型对计算与内存的要求

模型在本机运行后，处理器性能、内存容量和数据传输能力便会直接影响运行效果。有些模型可以使用 CPU，GPU 则能加速适合并行处理的计算，前提是运行软件支持相应硬件。[Qwen 本地运行说明](https://github.com/QwenLM/Qwen3)

采用独立显卡时，显存用于保存 GPU 运算所需的模型和工作数据。**显存容量决定可以容纳多少数据，显存带宽反映单位时间的数据传输能力。** 系统内存与显存的访问路径不同，不能将两者简单相加，视为同一块高速空间。[IBM：AI 基础设施术语](https://redbooks.ibm.com/docs/MD260021/MD260021.html)

可用显存不足时，任务可能需要缩减规模，或借助其他内存与存储运行，从而增加传输和等待。显存足够以后，继续增加容量也未必提高速度，还要看计算能力、带宽和软件实现。这也是评估本地 AI 设备时，需要结合具体模型与任务，而不能仅参考游戏性能的原因。

这一类客户通常接触的是**显卡或装有 GPU 的整台电脑，以及配套的应用、驱动和工具**。GeForce 是产品家族；Blackwell 等名称描述技术架构。比如 RTX 5090 是采用 Blackwell 架构的具体产品，两者不是两个并列的显卡型号。[RTX 5090 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)

## 二、企业专业团队：把设计和研发项目做出来

企业里的使用者可能是设计师、工程师、研究员或程序员。他们不一定使用同一种设备：专业设计关注项目与软件，模型研发还需要开发环境、实验和部署能力。

### 设计师与工程师：项目变大，设备要求随之变化

建筑师用 Revit 建立建筑模型，机械工程师用 SOLIDWORKS 设计零件和装配结构。随着项目规模扩大，他们需要根据工作要求配置电脑，兼顾处理能力、内存容量和软件运行的稳定性。[Revit 官方介绍](https://www.autodesk.com/products/revit/overview) [SOLIDWORKS 官方介绍](https://www.solidworks.com/product/solidworks-design)

面向这类用途销售的专业电脑，也常被称为“工作站”，既有台式主机，也有笔记本。RTX PRO 则是可以装在这类电脑里的专业 GPU；需要经常携带设备的用户，也可以选择搭载 RTX PRO 笔记本 GPU 的电脑。[专业电脑与普通电脑的区别](https://www.hp.com/us-en/tech-takes/workstations/comparison/workstation-vs-desktop-business.html) [专业笔记本](https://www.nvidia.com/en-us/products/workstations/professional-laptops/)

RTX PRO 的价值包括部分型号提供的大显存，以及专业软件认证、企业驱动与支持。认证意味着针对专业应用进行兼容性验证，帮助企业选择和维护设备。它解决的是项目环境中的具体要求，并不意味着每一家企业都必须使用专业卡。[Professional Desktop GPUs](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/)

例如，桌面 RTX 5090 配备 **32 GB** 显存，RTX PRO 6000 Blackwell Workstation Edition 配备 **96 GB**。当项目需要同时容纳更多数据时，更大的空间可能改变任务能否在本机顺利完成。[RTX 5090 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/) [RTX PRO 6000 工作站版规格](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/)

不过，专业卡的价格和显存容量，不能直接代表每款软件的速度。工作站厂商 Puget Systems 在 Topaz Video 1.6.1 测试中发现，RTX PRO 5000 Blackwell 的 48 GB 与 72 GB 版本表现接近，差异处于测试误差范围内。对那组任务而言，增加显存没有带来明显提速。[Topaz Video 1.6.1 Professional GPU Performance Analysis](https://www.pugetsystems.com/labs/articles/topaz-video-1-6-1-professional-gpu-performance-analysis/)

因此，企业选型需要把项目要求与实际表现放在一起看：先确认能否容纳项目、能否满足软件和维护要求，再比较完成具体工作的效率。

### 研究员与程序员：开发一个 AI 客服助手，需要哪些产品

企业要使用 AI，首先需要决定是购买现成应用，还是自行开发。以客服为例，购买现成客服软件后，企业主要配置业务资料与服务流程；选择自行开发，则需要把客户提问、业务数据查询和模型回答连接起来。

自行开发客服应用时，模型的运行有三种选择：**调用现成模型 API、租用云端算力自行部署，或使用自己的设备部署。**

**第一种，调用阿里云百炼的千问模型 API。** API 就是程序调用接口，企业通过它向阿里云已经运行好的模型发送内容、取得回答，无需自己部署这部分模型服务。[百炼官方介绍](https://help.aliyun.com/zh/model-studio/what-is-model-studio/)

假设客户问：“我的订单什么时候发货？”企业的客服系统先查询这笔订单，得到“已付款，预计明天发货”的记录，再把客户的问题和这条记录发给千问。千问据此生成“您的订单已付款，预计明天发货”的回复，由客服系统显示给客户。**企业系统负责取得订单事实，千问负责根据这些信息生成回答。** 接入模型 API 不会让千问自动知道企业的订单情况，程序员仍需要接通相应的数据查询流程。[模型与应用端工具的分工](https://help.aliyun.com/zh/model-studio/qwen-function-calling)

**第二种，租用阿里云 GPU 云服务器，自行部署千问模型。** 企业租到的是远程计算资源，研发人员需要下载适合的可部署模型版本、安装运行软件并启动模型服务。同样是回答发货问题，客服系统这次把订单信息交给企业自己部署的模型。阿里云负责底层硬件，企业负责所部署模型服务的更新与运行管理。[在 GPU 云服务器上部署 Qwen 的官方示例](https://help.aliyun.com/zh/ecs/user-guide/deploy-qwen3-235b-a22b-on-gpu-accelerated-instances)

这两种方式最终都可以通过 API 接入客服系统，区别在于模型服务由谁部署和维护。**第三种，在企业自己的设备上部署模型，**则还需要企业配置和维护相应硬件。这些方式也可以组合，例如在自己的电脑上开发测试，再部署到租用的云端服务器；具体服务形式与计费将在下篇展开。

下面以选择在自己的设备上开发文字客服助手的团队为例，说明模型、软件和硬件如何配合。团队先选一个可以本地运行的语言模型，再测试回答质量、调整模型，并把它接入客服程序。英伟达除了提供硬件，也提供可供开发者选用的模型，例如 Nemotron 系列；模型的具体版本和使用条件需要与项目匹配。[Nemotron 模型](https://developer.nvidia.com/topics/ai/nemotron)

**调整模型和使用模型，是这个项目中不同的计算任务。** 如果团队用整理好的客服问答样本调整模型参数，让它更好地遵循企业的回复格式与处理要求，这属于训练；在已有模型基础上继续训练，称为微调。模型收到一个新问题并生成回答，则是在进行推理。研发人员在电脑上测试一句回复，已经发生了推理；上线后为客户生成回答，仍然是推理。团队还需要准备数据、评估效果和维护程序，训练与推理并不涵盖项目的全部工作。[NeMo 开发文档](https://docs.nvidia.com/nemo/)

### 软件分别解决调用硬件、调整模型和提供服务的问题

为了开发这个客服助手，研发人员需要能够调整和运行所选模型的软件。若计划使用英伟达 GPU 加速计算，就会接触到 CUDA 及其相关工具。**CUDA 是英伟达的并行计算平台与编程模型；CUDA Toolkit 是相应的开发工具包**，包含编译、调试工具，以及可以直接调用的计算功能。开发者可以直接使用这些工具，也可以通过支持 CUDA 的模型开发框架间接使用 GPU。这套基础能力贯穿训练和推理，也可以用于个人电脑、企业服务器与云端。[CUDA Toolkit](https://developer.nvidia.com/cuda/toolkit)

在这套基础之上，团队可以按项目需要选择更具体的工具。客服助手若需要微调，**NeMo 这套模型开发工具**可以帮助研发人员完成受支持模型的定制与评估。它与前面提到的 Nemotron 有区别：Nemotron 提供模型，NeMo 提供开发和改进模型的工具。[NeMo](https://docs.nvidia.com/nemo/)

当模型已经能够生成合适的回复，下一步是让它高效运行并接入客服程序。**TensorRT 是优化模型推理的软件工具系列**，其中 TensorRT-LLM 面向大语言模型，帮助优化生成回答时的计算执行。**NIM 则提供预先打包好的模型推理服务**：把受支持模型所需的运行组件组织好，并提供程序调用接口。程序员部署相应服务后，客服程序就可以向它发送问题、接收回答。[TensorRT](https://developer.nvidia.com/tensorrt) [NIM](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/)

这些工具可以协作，但不是每个项目都必须依次使用的固定套装；部分 NIM 服务内部就会使用 TensorRT-LLM 等推理引擎。企业如果需要生产环境中的软件支持、安全更新与维护，还可以考虑 NVIDIA AI Enterprise 企业软件平台。[NIM 文档](https://docs.api.nvidia.com/nim/docs/introduction) [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/)

### 根据模型与软件要求配置设备

明确模型和软件方案后，团队需要检查现有电脑能否支持，再决定是否升级设备。软件与硬件也需要结合预算和实测结果反复调整。

**能否运行、运行多快、回答质量如何，是不同的问题。** 部分模型可以通过支持 CPU 的软件运行，例如 llama.cpp；如果软件支持现有设备且内存足够，计算能力较弱可能只是让回答生成得更慢。若运行环境不兼容，或可用内存不足以完成任务，则可能无法运行。模型和计算方式相同时，设备速度慢并不意味着回答质量必然下降；为了适应设备而改用更小的模型或降低计算精度，才可能改变结果质量。[llama.cpp 支持的运行方式](https://github.com/ggml-org/llama.cpp)

微调时，设备除了运行模型，还要保存调整参数所需的数据；推理时，设备需要装下模型并及时生成结果。模型大小、采用的训练方法、输入内容长度以及同时处理的请求数量，都会影响所需的内存和计算能力。因此，设备选型要先看具体工作量，不能仅凭“训练”或“推理”两个词决定买哪张卡。

对于能够在本机完成的实验，企业既可以购买已经配好 RTX PRO 显卡的电脑，也可以为兼容的台式电脑单独购买、安装显卡。DGX Spark 是英伟达推出的一款小型桌面 AI 电脑，已经内置 CPU 和 GPU，可用于本地模型开发、测试和运行，是团队的另一种设备选择。[联想整机配置示例](https://psref.lenovo.com/Product/ThinkStation/ThinkStation_P5) [DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

DGX Spark 采用 CPU 与 GPU 共享的统一内存。它能容纳多大的任务，与任务运行得多快，是不同问题。LMSYS 对早期 DGX Spark 的测试就提示，较大的内存空间不意味着所有模型都能高速运行；带宽和软件实现同样重要。[NVIDIA DGX Spark with SGLang](https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/)

**不同 GPU 的设计各有侧重，用途也有交叉。** 例如，数据中心的 A100 同时支持训练与推理，L40S 则兼顾 AI、图形与视频任务。更大规模的模型或更多并发请求，可能需要服务器乃至多台设备协作；这些配置将在下一节展开。[A100](https://www.nvidia.com/en-us/data-center/a100/) [L40S](https://www.nvidia.com/en-us/data-center/l40s/)

至此，团队使用的产品有了明确分工：模型提供生成回答的能力，电脑中的 GPU 执行计算，开发与部署软件让模型能够被调整、运行并接入应用。客服助手进入正式使用后，如果越来越多客户同时提问，就需要更多计算资源和持续运行的保障。这些工作可以由企业自己的团队承担，也可以通过租用算力或调用模型服务交给相应服务商。接下来从这些资源的提供者出发，看看云厂商与算力运营商如何组织设备、网络和软件。

## 三、云厂商与算力运营商：组织大规模计算

企业可以向腾讯云、阿里云等云厂商租用计算资源。模型实际运行在服务商提供的服务器上，这些服务器部署在数据中心等设施中。服务商负责相应设备和服务的运行，企业则按所选服务承担应用开发或模型部署工作。[腾讯云 GPU 云服务器](https://cloud.tencent.com/product/gpu) [阿里云 GPU 云服务器](https://www.alibabacloud.com/help/en/egs/quick-reference)

经营计算资源、向客户提供算力服务的企业，也常被称为算力运营商，与云厂商的业务可能重叠。**算力中心则是集中部署和运行计算设备的设施**，包含服务器、网络以及供电、散热等配套。部分企业和科研机构也会自建计算集群，供内部研发使用。无论资源对外出租还是内部使用，都需要运维团队管理设备、网络和系统，让研究员与开发者能够持续运行任务。

### 使用者要完成任务，运营者要让资源有效协作

这些计算资源可能用于训练模型、提供推理服务，也可能用于科学计算或图形任务。A100、H100、H200、Blackwell 系列的 B200、B300，以及当前官方介绍的 Rubin 平台，都属于理解数据中心产品时会遇到的名称。不同产品和代际可以服务不同系统需求。[Data Center](https://www.nvidia.com/en-us/data-center/) [HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/)

数据中心 GPU 通常需要放在相应的系统配置中理解：内存容量、带宽、设备间互连和软件配套共同影响任务表现。一些产品采用 HBM，即 High Bandwidth Memory，高带宽内存，通过堆叠等技术支持大量数据传输。HBM 描述内存技术，不是 GPU 的另一个档次。[Micron：HBM](https://www.micron.com/products/memory/hbm)

承接前面的客服助手，运营团队此时面对的仍然是推理，但需要服务更多同时在线的用户。训练任务也可能因模型和数据规模扩大而进入计算集群。两种任务都要考虑设备容量、计算速度与成本，具体配置则取决于各自的工作量。

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


附注：Studio 的官方资料介绍了创作应用、工具与设备支持，本次未查到可靠的最新活跃用户数，本文不据此判断实际使用人数。
