"""Landscape relationship map: branches are alternatives or complementary parts, never implicit else paths."""
from pathlib import Path
import html,json,math
A=Path(__file__).resolve().parent
G='#17633f'; M='#397a57'; L='#86ad95'; B='#f7faf7'; INK='#243e30'
shapes=[];edges=[];labels=[];registry=[]
def tx(x,y,lines,size=24,color=INK,anchor='middle',weight=400):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{color}" font-size="{size}" font-weight="{weight}">'+''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.45}">{html.escape(l)}</tspan>' for i,l in enumerate(lines))+'</text>'
def box(id,x,y,w,h,title,lines=(),fill='white',size=24,titleSize=26):
 # Enlarge actual typography within the same overall canvas, not just output pixels.
 size=round(size*1.25,1);titleSize=round(titleSize*1.2,1)
 extra=8 if id in ('model-work','software-work','hardware-work','replicas','model-parallel') else 44
 x-=extra/2;w+=extra
 h=max(h,math.ceil(82+max(0,len(lines)-1)*size*1.45))
 shapes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{L}" stroke-width="2"/>')
 color='white' if fill==G else G
 labels.append(tx(x+w/2,y+34,[title],titleSize,color,weight=600))
 if lines:labels.append(tx(x+w/2,y+69,lines,size,'#e2efe5' if fill==G else INK))
 registry.append({'id':id,'x':x,'y':y,'w':w,'h':h,'title':title,'lines':list(lines)})
 return (x,y,w,h)
def line(points,label=None,labelpos=None,dashed=False,arrow=False):
 edges.append('<path d="'+' '.join(('M' if i==0 else 'L')+str(x)+','+str(y) for i,(x,y) in enumerate(points))+f'" fill="none" stroke="{L}" stroke-width="2.5" stroke-linejoin="round"'+(' stroke-dasharray="9 7"' if dashed else '')+(' marker-end="url(#arr)"' if arrow else '')+'/>')
 if label:labels.append(tx(*labelpos,[label],21,M))
def fork(x0,y0,trunk,xends,ys):
 line([(x0,y0),(trunk,y0)]);line([(trunk,min([y0]+ys)),(trunk,max([y0]+ys))])
 for x,y in zip(xends,ys):line([(trunk,y),(x,y)])
def group(x,y,w,h,title):
 shapes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#eef5ef" stroke="#c7ddcf" stroke-width="2"/>')
 labels.append(tx(x+22,y+34,[title],25,G,'start',600))
# Column headings and overall root.
labels.append(tx(48,54,['算力生意（上） · 全文逻辑框架'],31,G,'start',600))
labels.append(tx(48,94,['从使用者展开任务与方案，再看硬件、软件和系统怎样配合'],23,M,'start'))
box('root',35,949,260,144,'英伟达的产品版图',['谁使用？做什么？','产品怎样配合？'],G,23,25)
for y in [369,1003,1738]:line([(295,1021),(322,1021),(322,y),(355,y)])
# Three pale bands organize reading without replacing the graph branches.
# PERSONAL
box('personal',355,318,200,102,'个人用户',['使用现成能力'],G,23,26)
box('games',650,165,220,90,'游戏与创作',[],size=23)
box('personal-ai',650,437,220,90,'个人使用 AI',[])
fork(555,369,601,[650,650],[210,482])
box('geforce',1000,135,340,132,'图形与计算硬件',['GeForce 显卡／笔记本 GPU','按具体应用和任务选择'],size=23)
box('studio',1430,135,380,132,'应用与创作配套',['剪辑、渲染等应用调用 GPU','Studio 提供工具与驱动'],size=23)
line([(870,210),(950,210),(950,201),(1000,201)])
line([(1340,201),(1430,201)],'配合',(1385,178))
box('components',1950,132,520,170,'电脑中的分工',['CPU：通用程序与执行流程','GPU：适合并行处理的计算','内存／显存：工作数据；存储：文件'],size=23)
line([(1810,201),(1950,201)],'共同工作',(1880,178))
box('names',2590,132,590,170,'三个名称对应不同层级',['GeForce：产品家族','Blackwell：技术架构','RTX 5090：具体型号'],size=23)
line([(2470,215),(2590,215)],'辨认产品',(2530,192),dashed=True)
box('online',1000,348,340,110,'在线服务',['ChatGPT、Kimi','Seedance 等'],size=22)
box('local',1000,534,340,110,'本地部署',['下载模型与运行软件'],size=23)
fork(870,482,945,[1000,1000],[403,589])
labels.append(tx(937,331,['两种方式可按需使用'],21,M))
box('online-result',1430,340,610,126,'主要计算在服务商云端',['本机主要提交输入与展示结果','升级本地显卡通常不直接加快云端生成'],size=23)
line([(1340,403),(1430,403)])
box('local-model',1430,526,610,126,'可部署模型 ＋ 适配的运行软件',['例如 Qwen、DeepSeek 蒸馏版、SDXL','具体版本、许可证与设备要求需匹配'],size=23)
line([(1340,589),(1430,589)])
box('local-fit',2140,526,440,126,'结合任务判断设备是否够用',['容量、计算能力、带宽','以及软件对硬件的支持'],size=23)
line([(2040,589),(2140,589)])
box('keep',2810,390,365,95,'已满足需求',['沿用现有设备'],size=23)
box('adjust',2810,547,365,132,'尚不满足需求',['调整模型或运行设置','也可升级或更换设备'],size=23)
fork(2580,589,2690,[2810,2810],[437,613])
labels.append(tx(2750,414,['如果'],21,M));labels.append(tx(2750,590,['如果'],21,M))
# ENTERPRISE
box('enterprise',355,952,200,102,'企业专业团队',['完成设计与研发'],G,22,25)
box('design',650,793,220,90,'专业设计',[])
box('enterprise-ai',650,1085,220,90,'使用 AI 应用',[])
fork(555,1003,601,[650,650],[838,1130])
box('apps',1000,769,340,128,'专业应用',['Revit：建筑模型','SOLIDWORKS：零件与装配'],size=23)
box('workstation',1430,769,440,128,'按项目要求配置专业电脑',['RTX PRO 是可选的专业显卡','台式与笔记本形态需分别看'],size=23)
box('design-needs',1980,769,575,128,'选型依据',['项目规模、内存容量、应用兼容性','稳定性、维护与专业软件支持'],size=23)
line([(870,838),(1000,838)]);line([(1340,833),(1430,833)]);line([(1870,833),(1980,833)])
box('buy-app',1000,965,340,108,'购买现成应用',['主要配置、对接与测试'],size=23)
box('develop-app',1000,1190,340,96,'自行开发应用',[])
fork(870,1130,945,[1000,1000],[1019,1238])
box('api',1450,962,370,110,'方案一 · 调用模型 API',['服务商运行模型','企业接入业务数据与应用'],size=22)
box('cloud-self',1450,1131,370,110,'方案二 · 租算力自行部署',['服务商提供计算资源','企业部署与维护模型服务'],size=22)
box('own-self',1450,1300,370,110,'方案三 · 使用自有设备',['企业负责设备与模型服务','也可与云端方案结合'],size=22)
fork(1340,1238,1400,[1450,1450,1450],[1017,1186,1355])
labels.append(tx(1430,1101,['三种方案并列展开'],21,M))
# A separate coordinated group for self-deployment, not a mandatory software chain.
group(1950,1040,920,378,'自行部署时：模型、软件、设备相互配合')
box('model-work',1970,1115,270,270,'模型与工作',['选择与评估模型','按需训练／微调','运行推理','Nemotron 等模型资源'],size=20,titleSize=24)
box('software-work',2260,1115,285,270,'软件工具',['CUDA：计算基础','NeMo：模型定制','TensorRT：推理优化','NIM：打包推理服务','按需选择，非固定套装'],size=20,titleSize=24)
box('hardware-work',2565,1115,285,270,'计算设备',['自有或云端资源','专业电脑、DGX Spark','或 GPU 服务器','按模型与软件要求选型'],size=20,titleSize=24)
# Two self-hosting solutions converge into a coordinated resource group.
line([(1820,1186),(1890,1186),(1890,1230),(1950,1230)])
line([(1820,1355),(1890,1355),(1890,1230)])
# All ways lead to the usable application, while API bypasses self-hosting work.
box('ready-app',2990,1120,265,165,'可用的企业应用',['例如客服助手','连接业务事实','处理请求并生成回复'],size=22,titleSize=25)
line([(1820,1017),(2925,1017),(2925,1170),(2990,1170)])
line([(1340,1019),(1363,1019),(1363,931),(3122,931),(3122,1120)])
labels.append(tx(2240,986,['模型 API 路径：无需自行部署这部分模型服务'],21,M))
line([(2870,1230),(2990,1230)])
# CLOUD: complementary components, NOT sequential yes/no tasks.
box('provider',355,1687,200,102,'算力服务提供者',['云厂商／运营商'],G,22,23)
box('provide-task',650,1683,220,110,'持续提供算力',['组织与运行资源'],size=22,titleSize=24)
line([(555,1738),(650,1738)])
cap=[('compute',1487,'计算能力',['处理模型与程序']),('network',1624,'通信与连接',['设备之间交换数据']),('system',1761,'系统组织',['把部件组织成设备']),('operations',1898,'运行管理',['让服务持续可用'])]
for id,y,title,sub in cap:box(id,1000,y,300,105,title,sub,size=22,titleSize=25)
fork(870,1738,945,[1000]*4,[y+52 for _,y,_,_ in cap])
labels.append(tx(1148,1460,['以下四方面共同支撑服务'],22,M))
box('compute-products',1430,1487,895,122,'CPU、GPU、内存与存储',['GPU：A100／H100／H200、B200／B300、Rubin 等','CPU：Grace／Vera；显存技术包括 HBM 等'],size=22,titleSize=24)
box('network-products',1430,1624,895,122,'互连、网卡、交换网络与 DPU',['NVLink；ConnectX；Spectrum-X；Quantum InfiniBand','BlueField 分担部分网络、存储与安全处理'],size=22,titleSize=24)
box('system-products',1430,1761,895,122,'平台、参考架构与完整系统',['HGX：多 GPU 平台；MGX：模块化参考架构；DGX：系统家族','GB200 NVL72：液冷机柜系统；SuperPOD：集群方案'],size=22,titleSize=24)
box('operations-work',1430,1898,895,122,'调度、监测、恢复与资源调整',['结合响应速度、处理量与设备利用率设置运行方式','DGX Cloud 是英伟达自身 AI 研发与运行环境的例子'],size=22,titleSize=24)
for _,y,_,_ in cap:line([(1300,y+52),(1430,y+52)])
# Optional scaling methods in parallel; combine them when the workload needs it.
group(2480,1490,775,325,'规模扩大：两种方法可以结合')
box('replicas',2500,1565,345,210,'增加模型副本',['部署多组模型实例','把不同请求分发过去','服务更多并发请求'],size=22,titleSize=25)
box('model-parallel',2870,1565,365,210,'多个 GPU 分担模型',['拆分模型或计算任务','各设备之间交换数据','多卡副本也可部署多组'],size=22,titleSize=25)
line([(2325,1541),(2410,1541),(2410,1515),(2480,1515)],dashed=True)
box('service',2580,1870,610,140,'共同支撑可用的计算服务',['对外租用计算资源，或提供托管模型服务','自建集群的企业与科研机构也面对这些工作'],size=22,titleSize=27)
# Join the complementary rows visibly, terminating at service.
line([(2370,1539),(2370,1980)])
for _,y,_,_ in cap:line([(2325,y+52),(2370,y+52)])
line([(2370,1940),(2580,1940)])
# The optional expansion box supports the same service.
line([(2867,1815),(2867,1870)],dashed=True)
# Legend: semantics are explicit; no arrows imply a compulsory product journey.
labels.append(tx(48,2080,['读图：分叉表示并列选择或组成部分；汇合表示共同支撑；虚线表示按需扩展或补充说明。'],23,G,'start',500))
labels.append(tx(48,2120,['同一用户可涉及多个场景。产品是示例，可结合其他厂商硬件、开源工具与云服务；不必整套采用。'],22,M,'start'))
labels.append(tx(3215,2120,['旁观机器'],23,G,'end',600))
def svg(view=None):
 vb=view or (0,0,3300,2160);x,y,w,h=vb
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}"><defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="{L}"/></marker></defs><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{B}"/><g font-family="PingFang SC,Microsoft YaHei,sans-serif">'+''.join(edges+shapes+labels)+'</g></svg>'
(A/'full.svg').write_text(svg())
for name,view in [('personal',(315,118,2965,580)),('enterprise',(315,743,2965,690)),('provider',(315,1425,2965,620))]:(A/(name+'.svg')).write_text(svg(view))
(A/'nodes.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
(A/'preview.html').write_text('''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>全文逻辑关系图</title><body style="margin:0;background:#f7faf7"><a href="full.svg"><img src="full.svg" style="display:block;width:100%;height:auto" alt="全文逻辑关系图"></a></body></html>''')
print('Created landscape map with',len(registry),'nodes')
