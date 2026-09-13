from pathlib import Path
import html,json
A=Path(__file__).resolve().parent
G='#17633f'; LINE='#629779'; LIGHT='#eef5ef'
def text(x,y,lines,size=21,color='#244a33',weight=400):
 return f'<text x="{x}" y="{y}" text-anchor="middle" fill="{color}" font-size="{size}" font-weight="{weight}">'+''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.4}">{html.escape(l)}</tspan>' for i,l in enumerate(lines))+'</text>'
def node(x,y,lines,w=220,h=94,kind='box'):
 if kind=='q':shape=f'<path d="M{x},{y-h/2} L{x+w/2},{y} L{x},{y+h/2} L{x-w/2},{y} Z" fill="#e5f0e6" stroke="{G}" stroke-width="2"/>'
 else:shape=f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="8" fill="white" stroke="#8eb49a" stroke-width="2"/>'
 return shape+text(x,y-(len(lines)-1)*14+7,lines,20 if kind=='q' else 19,weight=500 if kind=='q' else 400)
def edge(points,label='',lx=None,ly=None):
 s='<path d="'+' '.join(('M' if i==0 else 'L')+str(x)+','+str(y) for i,(x,y) in enumerate(points))+f'" fill="none" stroke="{LINE}" stroke-width="2.4" marker-end="url(#arrow)"/>'
 if label:s+=f'<rect x="{lx-21}" y="{ly-20}" width="42" height="29" rx="4" fill="#f8fbf8"/>'+text(lx,ly,[label],18,G,600)
 return s
def right(y,label='是'):return edge([(330,y),(405,y)],label,370,y-10)
def down(y,y2,label='否'):return edge([(205,y+57),(205,y2-57)],label,226,(y+y2)/2+5)
def q(y,lines):return node(205,y,lines,250,114,'q')
def leaf(y,lines,h=108):return node(505,y,lines,200,h)
def header(title,subtitle):return '<rect width="620" height="80" rx="8" fill="'+G+'"/>'+text(310,32,[title],26,'white',600)+text(310,61,[subtitle],17,'#dfefe4')
P=header('个人用户','范围：游戏、创作与个人 AI')
P+=q(180,['只使用在线 AI 服务？'])+right(180)+leaf(180,['ChatGPT、Kimi等','模型主要在云端运行','无需为此专门升级显卡'])
P+=down(180,380)+q(380,['本地任务主要是','游戏或内容创作？'])+right(380)+leaf(380,['GeForce 系列','Studio 工具与驱动','结合所用应用选择'])
P+=down(380,580)+q(580,['现有设备运行模型','已满足需求？'])+right(580)+leaf(580,['沿用现有设备','无需仅为换代而升级'])
P+=edge([(205,637),(205,752)],'否',226,702)+node(205,815,['调整模型或运行设置','也可评估升级设备','关注容量、带宽与软件适配'],310,126)
E=header('企业专业团队','范围：专业设计与 AI 应用')
E+=q(180,['当前主要任务','是专业设计？'])+right(180)+leaf(180,['按专业应用配置电脑','RTX PRO 是一种选择','关注项目与稳定性要求'])
E+=down(180,380)+q(380,['现成 AI 应用','能满足业务需要？'])+right(380)+leaf(380,['使用现成应用','配置资料与业务流程','对接系统并测试效果'])
E+=down(380,580)+q(580,['自行开发时，需要','自己部署模型吗？'])+right(580,'否')+leaf(580,['调用模型 API','服务商负责运行模型','企业连接业务与应用'])
E+=down(580,780,'是')+q(780,['已有适合部署的','自有计算设备？'])+right(780)+leaf(780,['可在自有设备部署','专业电脑或服务器等','按实际模型测试'])
E+=edge([(205,837),(205,900)],'否',226,874)+node(205,953,['租用云端算力','或购置合适设备'],270,106)
# Both self-hosted resource routes lead to the same optional model customization decision.
E+=edge([(505,834),(505,1045),(205,1045),(205,1103)])+edge([(205,1006),(205,1103)])
E+=q(1160,['模型需要训练','或微调吗？'])+right(1160)+leaf(1160,['选用开发与训练工具','NeMo 是一种选择','可微调受支持模型'])
E+=edge([(205,1217),(205,1335)],'否',226,1275)+edge([(505,1214),(505,1310),(205,1310),(205,1335)])
E+=node(205,1410,['部署推理并接入应用','CUDA 可支撑训练与推理','TensorRT、NIM 等按需选用','也可采用其他适配工具'],320,150)
C=header('云厂商与算力运营商','范围：组织资源，提供计算服务')
C+=q(180,['单台设备能满足','当前计算需求？'])+right(180)+leaf(180,['先采用单机方案','CPU、GPU、内存','与存储共同工作'])
C+=down(180,380)+q(380,['单个模型需要','跨多个 GPU 运行？'])+right(380)+leaf(380,['模型或计算任务拆分','需要 GPU 间通信','NVLink 等互连能力'])
C+=edge([(205,437),(205,502)],'否',226,480)+node(205,559,['可增加模型副本','把请求分给不同设备'],270,114)
C+=edge([(505,434),(505,671),(205,671),(205,722)])+edge([(205,616),(205,722)])
C+=node(205,800,['多设备组织与通信','HGX：多 GPU 平台','MGX：参考架构','DGX：系统家族'],300,156)
C+=text(450,930,['两种扩展方法','也可以结合使用'],17,'#687f6b')
# Single-machine and multi-device services both require reliability work.
C+=edge([(205,878),(205,1030)])+edge([(605,180),(613,180),(613,1000),(205,1000),(205,1030)])
C+=node(205,1120,['持续运行与服务保障','调度 · 监测 · 故障恢复','按用量调整资源','兼顾响应速度与利用率'],320,180)
parts={'personal':(P,980),'enterprise':(E,1560),'cloud':(C,1290)}
def svg(body,w,h):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker></defs><rect width="100%" height="100%" fill="#f8fbf8"/><g font-family="PingFang SC,Microsoft YaHei,sans-serif">{body}</g></svg>'
for k,(p,h) in parts.items():(A/f'{k}.svg').write_text(svg('<g transform="translate(16,16)">'+p+'</g>'+text(326,h-16,['是／否表示当前任务条件；示例产品均非唯一方案。'],16,'#687f6b'),652,h))
root=node(1000,90,['英伟达的产品版图','你要解决哪类计算问题？'],490,122)
for x,label in [(326,'个人使用'),(1000,'企业项目'),(1674,'提供算力')]:root+=edge([(1000,151),(1000,189),(x,189),(x,220)])+text(x,211,[label],18,G)
master=root+''.join('<g transform="translate('+str(x)+',230)">'+p+'</g>' for x,(p,h) in zip([16,690,1364],parts.values()))
master+=text(1000,1840,['按任务逐层判断，再组合硬件、软件与系统。','同一客户可以进入多条分支；不必采用英伟达的整套产品。'],23,G)
(A/'full.svg').write_text(svg(master,2000,1905))
(A/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>条件分支导图</title><body style="margin:0;background:#f8fbf8"><img src="full.svg" style="width:100%;height:auto"></body></html>')
print('Generated full SVG and three branch details')
