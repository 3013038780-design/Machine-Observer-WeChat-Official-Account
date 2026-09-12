# v13 配图清单与 135 使用说明

状态：用户于2026-09-13明确要求进入 HTML 与配图阶段；这是排版审阅版，尚未发表。

## 打开和复制

1. 打开 upper/article-v13.html，复制浏览器中渲染好的正文到135，不粘贴 HTML 源码。该文件内嵌全部图片，可单独打开。
2. 图片已按正文顺序编号，images/ 内18张 PNG 可独立上传到135。若复制后图片未自动转存、显示丢失或预览不稳定，在对应位置上传同编号图片替换；不要把本地 file 路径当作公众号远程图片地址。
3. 135-images-v13.zip 解压后打开 article.html 即可本地预览；旁边 images/ 是上传用图片。保留这两个相对位置。
4. 在135手机预览中确认图片已成功上传、表格可点开阅读，以及来源链接的保留情况；本轮已检查浏览器360/390/650像素宽度，未实际测试135粘贴与上传。

正文16px、行高1.75、字距0.5px、两侧12px，沿用绿色主题。章节标题不带装饰编号条和底部分隔线。图表按366px手机正文宽度、3倍像素渲染，正文表格均为PNG；不依靠缩小正文去适配宽表。

## 已完成的图片

| 编号 / 文件 | 类型 | 内容 |
|---|---|---|
| [01-header](images/01-header.png) | 既有品牌图 | 旁观机器 |
| [02-computing-lab](images/02-computing-lab.png) | AI 场景插画 | 计算的不同工作环境 |
| [03-geforce](images/03-geforce.png) | 官方产品图＋说明 | GeForce RTX 5090 |
| [04-online-local](images/04-online-local.png) | 精确排版图表 | AI 在哪里运行？ |
| [05-local-models](images/05-local-models.png) | 精确排版图表 | 可本地运行的模型例子 |
| [06-rtx-pro](images/06-rtx-pro.png) | 官方产品图＋说明 | RTX PRO 6000 Blackwell |
| [07-enterprise-options](images/07-enterprise-options.png) | 精确排版图表 | 企业使用模型的三种方式 |
| [08-software-layers](images/08-software-layers.png) | 精确排版图表 | 这些软件处在不同层级 |
| [09-dgx-spark](images/09-dgx-spark.png) | 官方产品图＋说明 | DGX Spark |
| [10-connections](images/10-connections.png) | 精确排版图表 | 三种传输，连接不同对象 |
| [11-gb200](images/11-gb200.png) | 官方产品图＋说明 | GB200 NVL72 |
| [12-quote-scope](images/12-quote-scope.png) | 精确排版图表 | 看报价，先看交付范围 |
| [13-robot-lab](images/13-robot-lab.png) | AI 场景插画 | 分拣机器人的实验室 |
| [14-jetson](images/14-jetson.png) | 官方产品图＋说明 | Jetson Orin 家族 |
| [15-drive](images/15-drive.png) | 官方产品图＋说明 | DRIVE 车载计算平台 |
| [16-product-map](images/16-product-map.png) | 精确排版图表 | 七块产品，一张版图 |
| [17-glossary](images/17-glossary.png) | 精确排版图表 | 基础概念速查 |
| [18-price-snapshot](images/18-price-snapshot.png) | 精确排版图表 | 两种官方挂牌价样本 |

## 还需要用户找图吗

当前图文版已经配齐，不需要为了完成这版再补图。若想把概念插画换成真实工作现场，优先找下面几类；不建议给每个型号各放一张，避免把文章拉成产品目录。

- 建筑设计场景：设计师电脑中真实的 Revit 建筑模型，能看出“专业电脑处理项目”；应有截图或摄影使用许可。替换计算实验室概念插画中的创作场景，而不是增加一段新论述。
- AI服务器内部：服务器厂商的 GPU 服务器结构图，清楚标出 GPU、CPU、内存与网卡。比机房走廊照片更能解释第三节；可在 Dell PowerEdge 或 NVIDIA HGX 官方文档查找。
- H200 / B200：若需要突出数据中心芯片，选 NVIDIA 对应产品页的单件官方图，明确是模块/板卡而不是整机，不用外形相似的游戏卡代替。
- 机器人真实案例：相机、分拣机械臂、计算模块同时可见的厂商实拍。可替换13号AI插画；不要把厂商宣传的仿真画面标成真实工厂照片。
- 汽车：Volvo EX90 对应车型的官方素材可以补充真实采用案例；目前15号使用的是 NVIDIA 平台概念图，不把它标成任何真实车型。

## 官方产品素材出处

- rtx5090：[官方产品页](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)；[原图地址](https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/graphic-cards/50-series/rtx-5090/geforce-rtx-5090-learn-more-og-1200x630.jpg)。查询日2026-09-13。
- rtxpro6000：[官方产品页](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/)；[原图地址](https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/rtx-pro-6000-blackwell-workstation-edition/nvidia-geforce-rtx-pro-6000-og-1200x630.jpg)。查询日2026-09-13。
- dgxspark：[官方产品页](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)；[原图地址](https://www.nvidia.com/content/dam/en-zz/Solutions/dgx-spark/DGX-Spark-og.jpg)。查询日2026-09-13。
- gb200：[官方产品页](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)；[原图地址](https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/gb200-superchip/gb200-nvl72-og.jpg)。查询日2026-09-13。
- jetson：[官方产品页](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)；[原图地址](https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf22/embedded-systems/jetson-orin/nvidia-jetson-orin-og.jpg)。查询日2026-09-13。
- drive：[官方产品页](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/in-vehicle-computing/)；[原图地址](https://www.nvidia.com/content/dam/en-zz/Solutions/self-driving-cars/in-vehicle-computing/high-performance-in-vehicle-computing-for-autonomous-vehicles-og.jpg)。查询日2026-09-13。

官方图片保留原貌并标明来源；版权归原权利人所有，来源记录不等同于开放许可。配图只用于解释相应产品，不宣称作者拍摄或产品官方授权背书。

## 生成与可编辑来源

- 02与13号场景插画：使用内置 image_gen，提示词保存在 prompts.json。工具未返回模型名称，未断言采用 image2。插画标记为AI概念示意，不用于证明产品外形或实际接线。
- 01号：此前用户选定的复古电脑品牌首图。
- 其余：官方图片加说明或确定性HTML图表，源文件在 cards/，便于调整措辞后重新导出；价格沿用已核查的2026年9月12日网页快照，不冒充本日价格。
- manifest.json 是图片清单；official-sources.json 是原图出处；article-sources.json 是正文65项去重链接。
- 重建：先运行 upper/build-v13.py --prepare，再运行 upper/render-v13.mjs，最后运行 upper/build-v13.py；检查使用 upper/check-v13.mjs。Node脚本允许通过 MO_PLAYWRIGHT_MODULE 与 MO_CHROME_EXECUTABLE 指定本机依赖。
