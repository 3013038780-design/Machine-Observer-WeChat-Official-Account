# 算力生意（上）：英伟达的产品版图

> 内容提要：英伟达的产品可以沿着“部件—系统—软件”读懂。GeForce、RTX PRO 和数据中心 GPU 各有侧重；CPU 与网络负责配合计算；DGX、Jetson、DRIVE 将部件组成不同用途的设备与平台；CUDA 等软件则让开发者真正用上这些硬件。理解这几层关系，才能看明白型号差异，以及一份报价究竟卖的是什么。

提到英伟达，最熟悉的名字往往是 RTX 4090、RTX 5090。关注 AI 的人还会听到 H100、B200，再往下看，又冒出 GB200、DGX、CUDA、Jetson。

这些名字难记，部分原因是它们根本不在同一个层级：有的是 GPU 型号，有的是组合了处理器的计算模块，有的是整套系统，还有的是软件。

例如，GeForce RTX 5090 是显卡产品；Blackwell 是它采用的架构名称，可以理解为芯片设计的一代技术基础；DGX Spark 则是一台可以放在桌上的 AI 计算机。它们之间的差别，远不止性能高低。[RTX 5090 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/) [DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

沿着组成关系来看，产品版图就清楚多了：先看负责计算和连接的部件，再看这些部件组成的系统，最后看运行在上面的软件。

## 一、计算部件：从 GPU 开始

### GeForce：个人电脑里的图形与 AI 计算

GPU 的英文是 Graphics Processing Unit，中文叫图形处理器。它擅长将适合拆分的运算分配给许多计算单元同时处理。画面渲染需要大量这类计算，AI 模型中的许多运算也适合这种方式，所以 GPU 的用途逐渐从显示图形扩展到 AI 和科学计算。[Intel：GPU 与 CPU](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html)

日常所说的“显卡”，通常是把 GPU、显存、供电等组件装在一起的板卡。**GPU 是其中负责计算的部件，显卡是可以装进电脑的产品。**

GeForce 是英伟达面向个人电脑的主要 GPU 产品家族。以 RTX 50 系列为例，型号从 RTX 5050 延伸到 RTX 5090，覆盖不同预算和性能需求；笔记本也有对应产品，但不能把同名笔记本 GPU 当成桌面卡的原样搬入。它们既服务游戏，也可加速视频制作、三维创作和本地 AI。[GeForce RTX 50 Series](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/)

这里的“本地 AI”，就是让模型在自己的电脑上运行。电脑需要将模型运行所需的数据放进可供处理器访问的内存，再不断读取、运算。于是，除了 GPU 本身有多强，**数据放不放得下、送得够不够快**也会影响结果。

硬盘或固态硬盘负责长期保存程序、素材和模型文件；系统内存是运行程序时使用的临时工作空间；独立显卡上的显存则主要供 GPU 使用。显存既可以放图形数据，也可以放 AI 模型的数据，名字里有“显”，并不意味着它只存画面。[Kingston：内存与存储](https://www.kingston.com/en/blog/pc-performance/difference-between-memory-storage) [IBM：AI 基础设施术语](https://redbooks.ibm.com/docs/MD260021/MD260021.html)

容量与带宽也要分开理解。显存容量说明能放多少数据；显存带宽说明单位时间能在 GPU 与显存之间传输多少数据。容量不够，任务可能无法按原来的方式运行，需要缩减规模或借助其他存储；容量够了，继续增加容量也不等于计算自动加速。

### RTX PRO：给更复杂的专业工作留出空间

RTX PRO 面向设计、工程、影视制作和 AI 开发等专业工作。与 GeForce 相比，部分型号提供更大的显存，配合专业软件认证、企业驱动和支持。软件认证意味着针对特定专业应用进行兼容性验证，方便企业选择和维护设备。[Professional Desktop GPUs](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/)

显存差别可以用一个具体例子理解：桌面 RTX 5090 配备 **32 GB** 显存，RTX PRO 6000 Blackwell Workstation Edition 配备 **96 GB**。当大型三维场景或 AI 任务需要容纳更多数据时，后者能提供更大的空间；它的价值不只是把同一个小任务再算快一些。[RTX 5090 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/) [RTX PRO 6000 工作站版规格](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/)

但“装得下更多”和“跑得更快”是两件事。工作站厂商 Puget Systems 在 Topaz Video 1.6.1 的测试中发现，RTX PRO 5000 Blackwell 的 48 GB 与 72 GB 版本，性能差异小到落在测试误差范围内。在那组任务里，增加显存没有带来明显提速。这个结果说明，专业卡的价值需要结合应用来看，不能只按容量或售价判断。[Topaz Video 1.6.1 Professional GPU Performance Analysis](https://www.pugetsystems.com/labs/articles/topaz-video-1-6-1-professional-gpu-performance-analysis/)

因此，GeForce 与 RTX PRO 的区别，更适合从工作要求理解：前者覆盖个人电脑的图形与计算需求；后者进一步照顾大型项目、专业应用和企业部署。两者能做的工作有交叉，不能简单划成“娱乐卡”和“工作卡”。

### 数据中心 GPU：把计算规模继续做大

当一台电脑装不下任务，或服务需要持续处理大量请求，计算就会进入服务器和数据中心。这里既有 A100、H100、H200 等常见型号，也有 Blackwell 系列的 B200、B300，以及当前官方重点介绍的 Rubin 平台。不同代际会在实际系统中并存。[Data Center](https://www.nvidia.com/en-us/data-center/) [HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/)

数据中心 GPU 的区别不仅在运算能力，也在内存容量、数据传输、设备互连和系统配套。一些产品使用 HBM，即 High Bandwidth Memory，高带宽内存。它通过堆叠等封装技术提供较高的数据传输能力，服务需要频繁读取大量数据的计算。HBM 是内存技术，不是另一种 GPU。[Micron：HBM](https://www.micron.com/products/memory/hbm)

AI 是这里的重要用途。训练通过数据调整模型参数；推理使用模型处理新输入、产生结果；微调是在已有模型基础上继续训练。训练与推理是关键计算活动，但完整 AI 工作还包括数据准备、评估、部署和运行维护。

同一款数据中心 GPU 往往既能训练，也能推理。例如 A100 官方就同时列出这两种用途。L40S 等产品还覆盖图形、视频和 AI 工作。因此，不能把字母背成绝对规则，例如“H、B 只能训练，L 只能推理”。[NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/) [NVIDIA L40S](https://www.nvidia.com/en-us/data-center/l40s/)

到了这一层，更有意义的问题是：模型需要多少内存，要多久给出结果，需要同时服务多少请求，以及任务是否要拆给多张 GPU。产品选择由这些条件共同决定。

### CPU 与网络：让计算持续运行

GPU 需要其他部件配合。CPU 是 Central Processing Unit，中央处理器，负责运行通用程序、组织执行流程和处理许多数据工作。英伟达也有 Grace、Vera 等 CPU 产品。一个 AI 应用里，除了模型计算，还可能包含文件读取、工具调用和程序执行，并非每一步都交给 GPU。[Intel：GPU 与 CPU](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html) [Data Center](https://www.nvidia.com/en-us/data-center/)

当任务分配给多张 GPU，计算途中还要交换数据。如果运算已经完成，却迟迟等不到其他设备的结果，系统就会花时间等待。因此，扩充算力还需要扩充连接能力。

NVLink 用于 GPU 等计算部件之间的高速互连，NVLink Switch 帮助扩展这种连接。服务器还需要网卡和交换机接入更大的计算网络：ConnectX 是网络适配器家族，Spectrum-X 与 Quantum 分别属于以太网和 InfiniBand 相关网络体系。[NVLink and NVLink Switch](https://www.nvidia.com/en-us/data-center/nvlink/) [Networking Products](https://www.nvidia.com/en-us/networking/products/)

BlueField 则属于 DPU，Data Processing Unit，数据处理单元。它可以承担网络、存储和安全方面的部分处理工作，让 CPU 和 GPU 腾出资源执行其他任务。它的用途与负责 AI 运算的 GPU 不同。[HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html)

这也解释了为什么参数表里会出现多种“带宽”：显存带宽描述 GPU 与显存之间的数据传输，GPU 互连带宽描述计算部件之间的交换，网络带宽则涉及更大范围的设备连接。它们位于不同环节，一个数字不能代表整台设备的数据流动能力。

AI 加速器还在继续分化。英伟达已经公布 Groq 3 LPX 量产消息，其中的 LPU 是面向推理的专用处理器，LPX 则是系统名称。这类产品进一步说明，不同计算需求会催生不同硬件；具体优势仍要结合任务与部署条件判断。[Groq 3 LPX Now in Full Production](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)

## 二、系统与专用平台：把部件组合起来

### HGX、MGX、DGX，分别是什么

服务器可以理解为承担服务任务的计算机：它把处理器、内存、存储、网络等组件组合起来，供应用或其他用户使用。GPU 服务器在其中加入计算加速能力，多台服务器再连接成更大的系统。

英伟达的 HGX、MGX 和 DGX，涉及这个组合过程中的不同产品形式。

**HGX 是多 GPU 计算平台。** 以 HGX B300 为例，GPU 和高速互连集成在计算底板上，服务器厂商再围绕它配置 CPU、系统内存、存储和其他组件，形成完整服务器。因此，“采用 HGX 的服务器”不是只有一张 HGX 板。[HGX AI Factory: Components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html)

**MGX 是模块化系统参考架构。** 它为合作厂商提供构建系统的设计基础，让不同计算、网络等模块更容易组合。看到 MGX，可以理解为系统采用了一套模块化设计，而不是又发现一个 GPU 型号。[MGX](https://www.nvidia.com/en-us/data-center/products/mgx/)

**DGX 是英伟达的系统家族。** 其中既有面向数据中心的设备，也有更大的集成方案。DGX SuperPOD 就涉及将计算系统、网络等组织起来的大规模基础设施。它们与单块 GPU 的交付范围不同。[DGX Platform](https://www.nvidia.com/en-us/data-center/dgx-platform/)

GB200 则将 Grace CPU 与 Blackwell GPU 组合成计算单元，GB200 NVL72 进一步将这样的计算单元和互连组织成机柜级系统。这里的“机柜”包含计算设备与连接配套，部署还需要机房的供电和散热条件。[GB200 NVL72 官方介绍](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)

所以，看价格之前需要先确认商品边界：显卡价买到一张卡；服务器价对应一套具体配置；机柜系统价涉及更大范围的设备与配套。将设备安装、供电、冷却并持续运行，也会产生费用。它们共同决定完成工作需要投入多少，而不是所有用户都必须把这些设备各买一遍。

### 桌面 AI 计算机：DGX 也可以放在桌上

DGX Spark 是一个容易让人误会的例子。虽然名字里有 DGX，它却是一台紧凑的桌面 AI 计算机，方便开发者在本地开发、测试和运行模型。它提供的是整台设备，不能把价格直接与一张显卡相比。[DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

这类系统还提醒我们，内存设计并不都相同。DGX Spark 的 CPU 与 GPU 使用统一内存，不能简单套用“电脑内存加独立显卡显存”的理解。容量较大可以帮助容纳模型，但实际速度仍取决于带宽、软件和任务本身。LMSYS 对早期 DGX Spark 的测试就显示，能容纳的模型规模与运行速度需要分别考察。[NVIDIA DGX Spark with SGLang](https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/)

### Jetson、IGX、DRIVE：计算进入设备与汽车

计算也可以发生在摄像头、机器人或汽车附近。这里通常被称为“边缘”：数据在设备所在的位置处理，减少对远端传输与连接条件的依赖。

**Jetson 是面向嵌入式和机器人应用的计算平台。** Orin、Thor 等家族包含计算模块，配合开发套件与软件工具。设备厂商将它们集成进机器人、工业设备等产品，让设备处理传感器数据、运行 AI。Jetson 本身不是一台完整机器人。[Jetson Embedded Systems](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/)

**IGX 面向工业级边缘 AI。** 工厂、医疗等设备需要持续运行，还要处理安全和维护问题。IGX 将工业级硬件与企业软件支持结合起来，部分配置还提供独立的安全处理能力。它着重解决的是设备长期投入使用时的要求。[IGX](https://www.nvidia.com/en-us/edge-computing/products/igx/)

**DRIVE 面向汽车。** DRIVE AGX 提供车载计算开发平台，DriveOS 提供相关软件基础，Hyperion 则涉及计算、传感器等参考设计。整套体系服务汽车开发与车载应用；车辆最终具备什么能力，还取决于整车的软件、传感器、集成和验证。[Autonomous Vehicles](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/)

到这里，硬件的去向已经明确：它可以成为个人电脑中的一张卡，也可以组合成机房系统，或嵌入机器人和汽车。接下来要解决的是，开发者怎样让它们完成具体工作。

## 三、软件与模型：让硬件发挥作用

### CUDA：给开发者使用 GPU 的工具

一块 GPU 有计算能力，软件仍需要把适合的工作安排给它。CUDA 是英伟达的并行计算平台与编程模型；CUDA Toolkit 提供编译、调试和开发所需的工具与库。开发者也可以通过已经支持 GPU 的应用和框架间接使用这些能力。[CUDA Toolkit](https://developer.nvidia.com/cuda/toolkit)

因此，CUDA 的意义不在于让每个用户都学会写 GPU 程序，而在于让软件开发者能够把 GPU 用进更多应用。同样的硬件，应用是否支持、相关计算有没有被优化，都会影响最终表现。

黄仁勋在接受 Ben Thompson 采访时，将加速计算放在应用与软件体系中解释。这是厂商对自身路线的阐述，但也点出了一个实际问题：用户体验到的是整套软件运行的结果，而不是芯片参数表本身。[An Interview With Nvidia CEO Jensen Huang About Accelerated Computing](https://stratechery.com/2026/an-interview-with-nvidia-ceo-jensen-huang-about-accelerated-computing/)

### AI 工具与模型：各自解决不同的问题

在基础计算工具之上，英伟达还提供 AI 开发与部署软件。例如，TensorRT 用于优化推理执行；NIM 将模型运行所需的组件封装成便于部署的服务；NeMo 提供模型开发、定制等相关工具。NVIDIA AI Enterprise 则面向企业软件部署与支持。这些名称描述的用途不同，不能全部叫“英伟达的大模型”。[AI](https://www.nvidia.com/en-us/ai/) [Software](https://www.nvidia.com/en-us/software/)

模型是另一层产物。以 Nemotron 为例，它提供可供开发者使用和继续开发的模型等资源。可以把关系理解为：硬件提供计算资源，工具帮助开发与运行，模型承担识别、理解或生成等具体能力，应用再把这些能力交给用户。[DGX Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/)

### 仿真工具：先在计算机里测试真实世界

Omniverse 提供构建三维和物理仿真应用的库、接口与服务；Isaac 则围绕机器人开发提供工具，其中包括仿真与学习相关组件。它们与 Jetson 的关系，是软件开发工具与设备侧计算平台的配合。[Omniverse](https://www.nvidia.com/en-us/omniverse/) [Isaac](https://developer.nvidia.com/isaac)

例如，开发一个抓取物体的机器人，需要准备数据、训练或调整模型，在仿真和真实环境中验证，再将程序部署到设备上。数据中心系统可以承担训练，仿真软件帮助测试，Jetson 等平台则在机器人上执行任务。部署后产生的问题，还会促使开发者继续修改和验证。

英伟达机器人业务负责人 Deepu Talla 在访谈中强调了这条从数据、训练、仿真到部署的链条。他所描述的，正是这些产品为何会同时出现在一家公司的目录里：机器人所需的计算，不只发生在机器人身体内部。[Deepu Talla About Physical AI and Robotics](https://www.chipstrat.com/p/an-interview-with-nvidias-deepu-talla)

### 云：计算可以通过远端环境提供

这些软硬件也可以运行在云端。云服务商把远端计算资源和软件能力提供给客户，客户未必需要自己购买和维护设备。

DGX Cloud 需要按当前定位理解：截至本文核查日，官方页面将它描述为英伟达用于开发模型、验证系统和运行 AI 的内部云环境，并介绍如何通过云伙伴和相关运维软件向生态输出能力。因此，它不能仅凭“Cloud”这个名字就与所有公有云产品直接归为同一种服务。[DGX Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/)

设备、系统和软件之间的关系，也是理解算力生意的起点。买 GPU，是取得计算部件；买服务器，是取得一套设备；使用云上的计算或模型服务，则涉及另一种交付与收费方式。

阿里云、腾讯云提供的 GPU 资源和模型服务有什么区别，Token 如何计费，所谓 AI 工厂又在组织什么生产过程，留到下篇沿着服务和交易继续展开。

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
