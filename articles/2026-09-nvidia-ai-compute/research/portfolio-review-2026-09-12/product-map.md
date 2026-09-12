# 产品关系研究索引

日期：2026-09-12。编辑分层，不是 NVIDIA 官方分类；不是全部 SKU 或现货清单。来源编号与链接见[sources.md](sources.md)。本表用于防止遗漏、混层和重复，不直接搬进正文。

| 层级 | 家族/代表 | 作用及容易混淆的关系 | 依据 |
|---|---|---|---|
| GPU 产品 | GeForce RTX，桌面/笔记本 | 图形、创作和本地 AI；同名桌面与笔记本规格不能直接互换 | R04 |
| GPU 产品 | RTX PRO，工作站/服务器版本 | 专业图形和 AI；不是一个固定芯片，也不只在工作站使用 | R05、R03 |
| GPU 产品 | 数据中心 H、B、Rubin 等 | 计算加速；训练和推理存在用途交叉，不按字母严格二分 | R03、R12 |
| 架构名称 | Blackwell、Rubin 等 | 描述技术代际或平台语境；不能与整机型号当作同级商品比较 | R03、R04 |
| 计算部件 | Grace、Vera CPU | 通用计算和数据工作，也与 GPU 组合；CPU 不是 GPU 产品线 | R03、R11 |
| 专用加速 | Groq LPU / LPX | 前者处理器、后者系统；官方宣布量产不代表所有客户已经部署 | R22 |
| 基础设施处理器 | BlueField DPU | 网络、存储和安全等基础设施任务 | R09、R12 |
| 网络适配器 | ConnectX | 将系统接入网络，与 DPU 不能简单画等号 | R09、R12 |
| 网络平台 | Spectrum-X、Quantum 系列 | 以太网与 InfiniBand 相关平台；包含不同层级的产品与配套 | R09、R02 |
| 高速互连 | NVLink、NVLink Switch | GPU 互连及交换组件；与显存带宽不同 | R13 |
| 连接配套 | LinkX | 线缆、收发器等；不用升成一章 | R09 |
| 计算平台 | HGX | 多 GPU 底板/平台，与合作伙伴完整服务器区分 | R12 |
| 参考架构 | MGX | 模块化构建系统的方法与设计，不是一块 GPU | R11 |
| 整套系统 | DGX、DGX SuperPOD | 系统与更大规模集成方案，具体边界依产品配置 | R10 |
| 桌面系统 | DGX Spark、DGX Station | 本地 AI 计算系统；DGX 名称不能一律等于机房服务器 | R20、R02 |
| PC 平台 | RTX Spark | 新公布的 PC 平台名称，不是 DGX Spark 别称；具体供货待逐机核对 | R21 |
| 嵌入式平台 | Jetson Orin、Thor | 模块、开发套件与软件生态；不是完整机器人 | R06 |
| 工业边缘平台 | IGX | 工业级边缘 AI；不能省略系统与软件支持语境 | R17 |
| 汽车平台 | DRIVE AGX、Hyperion、DriveOS、DRIVE AV | 硬件、参考平台和软件不同层级的集合，不是成车能力保证 | R07 |
| 基础计算软件 | CUDA Toolkit、cuDNN 等 | 开发工具与加速库；CUDA 核心是另一个硬件概念 | R15、R08 |
| AI 软件 | TensorRT、NIM、NeMo、Dynamo | 推理优化、部署、开发及服务组织等不同任务，不能全部叫模型 | R08、R16 |
| 企业软件 | NVIDIA AI Enterprise、vGPU | 企业软件与虚拟化相关产品；许可证和计费本轮未逐项调查 | R08、R16 |
| 仿真与机器人开发 | Omniverse、Isaac | 平台、库与开发工具，和 Jetson 硬件互有关联 | R18、R19 |
| 模型及配套 | Nemotron、Cosmos、GR00T、Alpamayo | 不同领域的模型、数据或配套工具；不是所有开放模型均由 NVIDIA 原创 | R08、R07、R18、R14 |
| 行业工具入口 | RAPIDS、Clara/BioNeMo、cuLitho、Aerial、Metropolis 等 | 分别服务数据分析与行业任务；目录级覆盖，未逐个核查版本 | R08 |
| 云与运维 | DGX Cloud、DSX OS | 当前页面的内部云环境与对外运维组件关系；不沿用旧商业描述 | R14 |
| 消费软件与服务 | DLSS、Reflex、Studio、GeForce NOW、G-SYNC | 技术、工具、服务与显示生态并存，不是五款 GPU | R04 |

供货状态原则：当前目录收录、正式发布、量产公告、合作伙伴销售和实际现货分别记录；本索引不替代采购查询。
