from pathlib import Path
import html,json,re,importlib.util
P=Path(__file__).resolve().parent
A=P.parent.parent
G='#17633F'; M='#557366'; L='#D5E5DA'; B='#F2F7F3'; K='#263A31'; O='#BC783D'
def text(x,y,s,size=32,color=K,weight=400,anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(s)}</text>'
def rect(x,y,w,h,fill=B,stroke='none',r=16):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def path(d,color=G,width=4,arrow=False):
 return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"'+(' marker-end="url(#arr)"' if arrow else '')+'/>'
def circle(x,y,r,fill=G):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'
def car(x,y,scale=1,color=G):
 return f'<g transform="translate({x} {y}) scale({scale})">'+rect(0,27,142,48,'white',color,12)+path('M 25 27 L 42 0 H 100 L 121 27',color)+path('M 53 7 V 25 M 90 7 V 25',color,3)+circle(30,76,13,color)+circle(111,76,13,color)+'</g>'
def chip(x,y):
 s=rect(x,y,94,78,'white',G,9)+rect(x+21,y+18,52,42,B,G,3)
 for a in range(12,85,18):s+=path(f'M {x+a} {y-8} v 8 M {x+a} {y+78} v 8',G,3)
 return s

def arm(x,y,pose=0):
 # Illustrative robot arm, not product depiction.
 pts=[[(28,106),(30,60),(84,28),(114,68)],[(28,106),(68,63),(108,94),(114,126)],[(28,106),(40,49),(90,22),(123,44)],[(28,106),(67,51),(133,63),(145,111)]][pose]
 s=rect(x,y+104,60,18,G,r=3)
 d='M '+' L '.join(f'{x+a} {y+b}' for a,b in pts)
 s+=path(d,G,12)
 for a,b in pts[:-1]:s+=circle(x+a,y+b,9,'white')+f'<circle cx="{x+a}" cy="{y+b}" r="9" fill="none" stroke="{G}" stroke-width="4"/>'
 a,b=pts[-1]; s+=path(f'M {x+a-12} {y+b} v 21 h 8 M {x+a+12} {y+b} v 21 h -8',G,4)
 return s

def icon(kind,x,y):
 if kind=='car':return car(x,y,.8)
 if kind=='chip':return chip(x,y)
 if kind=='arm':return arm(x,y,0)
 if kind=='wheel':return rect(x,y+35,120,55,'white',G)+rect(x+24,y,72,35,B,G,5)+circle(x+26,y+94,12)+circle(x+95,y+94,12)
 if kind=='quad':return path(f'M {x+12} {y+30} H {x+102} L {x+120} {y+5} M {x+25} {y+30} l -15 52 M {x+45} {y+30} l 5 52 M {x+85} {y+30} l -10 52 M {x+100} {y+30} l 20 52',G,9)
 if kind=='human':return circle(x+55,y+15,15)+path(f'M {x+55} {y+36} v 43 M {x+21} {y+61} l 34 -22 l 34 22 M {x+55} {y+79} l -25 35 M {x+55} {y+79} l 25 35',G,10)
 if kind=='mobile':return arm(x+10,y-12,0)+rect(x,y+113,140,18,G,r=3)+circle(x+25,y+137,9)+circle(x+114,y+137,9)
 if kind=='air':return path(f'M {x+20} {y+15} L {x+105} {y+80} M {x+105} {y+15} L {x+20} {y+80}',G,6)+''.join(f'<ellipse cx="{x+a}" cy="{y+b}" rx="23" ry="9" fill="{B}" stroke="{G}" stroke-width="3"/>' for a,b in [(20,15),(105,15),(20,80),(105,80)])+rect(x+47,y+32,34,32,G,r=5)
 return ''
def base(n,title,sub,h):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{h}" viewBox="0 0 720 {h}"><defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9" fill="none" stroke="{G}" stroke-width="1.5"/></marker></defs><g font-family="PingFang SC,Microsoft YaHei,sans-serif">'+rect(0,0,720,h,'#FFFFFF',L,0)+rect(28,28,70,42,G,r=6)+text(63,58,f'{n:02}',27,'white',600,'middle')+text(117,61,'旁观机器 · 图解',25,M)+text(32,119,title,38,G,600)+text(32,164,sub,28,M)
def finish(s,name,h,foot):
 s+=path(f'M32 {h-76} H688',L,2)+text(32,h-39,foot,24,M)+'</g></svg>'
 (P/(name+'.svg')).write_text(s)

h=1220;s=base(1,'一次辅助减速，怎样发生','从观察到执行，系统持续获取反馈',h)
for i,(head,lines) in enumerate([('前车减速',['需要观察的，是前车位置和速度变化。']),('获取信息',['摄像头等传感器采集道路信息。']),('计算怎样减速',['车载计算机运行软件，','识别前车并计算需要采取的动作。']),('车辆执行并继续观察',['制动系统执行，系统重新观察距离，','根据变化调整后续动作。'])]):
 y=200+i*228;s+=rect(32,y,656,198)+circle(64,y+38,20)+text(64,y+47,str(i+1),25,'white',600,'middle')+text(100,y+49,head,34,G,600)
 if i==0:s+=car(80,y+82,.65)+car(360,y+82,.65,O)+text(506,y+127,'减速',30,O)
 elif i==1:s+=rect(74,y+86,76,48,'white',G,6)+circle(112,y+110,15)+path(f'M 166 {y+110} L 270 {y+82} M166 {y+110} L270 {y+141}',G,3)+text(300,y+123,'图像、距离等数据',30)
 elif i==2:s+=chip(66,y+88)+text(190,y+113,'识别前车 → 安排行动',29)+text(190,y+156,'信息在这里变成操作计划',28,M)
 else:s+=text(60,y+103,lines[0],29)+text(60,y+149,lines[1],29)
 if i<3:s+=path(f'M360 {y+203} v 19',G,3,True)
s+=text(32,1123,'这是一种功能示意，不代表具体车型配置。',27,M)
finish(s,'01-braking',h,'箭头表示处理过程；下一轮会继续观察道路。')

h=1190;s=base(2,'一辆车，不只一颗芯片','系统组成可以由不同企业共同提供',h)
for i,(title,what,who) in enumerate([('传感器','摄像头、雷达等：采集信息','车企选择并集成不同供应商的设备'),('计算硬件','运行程序，处理传感器数据','可采用供应商芯片，也可自研芯片'),('驾驶软件','识别环境、规划行动','可自研、外购，或与伙伴联合开发'),('车辆控制与执行','把计划落实为转向、制动等动作','需要与整车机械、电子系统配合')]):
 y=200+i*207;s+=rect(32,y,656,188,'white',L)+text(56,y+45,title,34,G,600)+text(56,y+96,what,30)+text(56,y+147,who,28,M)
s+=rect(32,1046,656,57,B)+text(360,1084,'采用英伟达芯片 ≠ 采用整套驾驶软件',29,G,600,'middle')
finish(s,'02-car-layers',h,'这是组成关系，不是四件产品的购买顺序。')

h=1280;s=base(3,'一项驾驶功能，从研发到上车','研发设备与车载设备，承担不同工作',h)
rows=[('明确任务条件','在哪些道路、天气下使用？'),('准备数据与开发软件','整理道路记录，训练模型或编写程序'),('在研发环境中验证','记录数据测试、模拟交通、连接真实硬件'),('在车辆上测试','结合封闭场地和实际道路检查系统'),('投入使用与持续改进','验证软件更新，分析异常与反馈')]
for i,(title,desc) in enumerate(rows):
 y=204+i*172;s+=rect(64,y,608,140,B)+text(88,y+48,title,32,G,600)+text(88,y+99,desc,28)
 if i<4:s+=path(f'M368 {y+148} v16',G,3,True)
s+=path('M57 1048 H25 V240 H55',G,3,True)+text(64,1110,'发现问题，会回到相应环节继续修改。',28,M)+text(64,1154,'训练可用本地或云端；运行须适配车辆。',28,G)
finish(s,'03-development',h,'流程用于理解；实际开发会反复迭代、交叉进行。')

h=1490;s=base(4,'机器人：形态与场景分开看','外形说明结构，场景说明在哪里工作',h)
items=[('arm','机械臂','固定位置操作物体'),('wheel','轮式移动','依靠轮子移动'),('quad','四足','通过四条腿移动'),('human','人形','具有人形结构'),('mobile','移动操作','移动底盘＋机械臂'),('air','空中机器人','在空中执行任务')]
for i,(k,t,d) in enumerate(items):
 x=32+(i%2)*336;y=204+(i//2)*246;s+=rect(x,y,320,228)+(f'<g transform="translate({x+108} {y+14}) scale(.78)">'+icon(k,0,0)+'</g>' if k=='mobile' else icon(k,x+90,y+16))+text(x+160,y+178,t,32,G,600,'middle')+text(x+160,y+215,d,25,M,400,'middle')
s+=text(32,999,'同一形态，可以服务不同场景',32,G,600)
s+=rect(32,1031,225,96,B)+text(144,1090,'轮式移动机器人',27,G,600,'middle')
for j,t in enumerate(['仓库：运送料箱','医院：配送物品','工厂：搬运物料']):
 y=1031+j*102;s+=rect(355,y,333,80,'white',L)+text(377,y+50,t,29)
 s+=path(f'M267 1079 H309 V{y+40} H342',G,3,True)
s+=text(32,1380,'人形不等于通用；工厂也不只使用人形机器人。',26,M)
finish(s,'04-robot-map',h,'入门示例，非全部分类；不表示任何品牌采用关系。')

h=1200;s=base(5,'机器人拿起一个零件','看见、规划、执行与反馈共同完成动作',h)
for i,(head,desc) in enumerate([('找到零件','摄像头提供图像，软件确定目标位置。'),('安排动作','规划机械臂路径，考虑障碍和可达范围。'),('抓取物体','控制器调节关节运动，夹爪接触零件。'),('检查并放置','利用位置、接触等反馈继续调整动作。')]):
 y=200+i*225;s+=rect(32,y,656,203)+arm(70,y+(40 if i==3 else 18),([0,0,1,3][i]))+rect(([224,224,177,208][i]),y+([146,146,150,156][i]),([29,29,16,16][i]),([27,27,16,16][i]),O,r=3)+path(f'M61 {y+175} H270',L,3)+text(310,y+54,head,34,G,600)
 # break descriptive lines at fixed semantic splits
 lines=[['摄像头提供图像，','软件确定目标位置。'],['规划机械臂路径，','考虑障碍与可达范围。'],['控制器调节关节，','夹爪接触零件。'],['利用位置、接触反馈，','继续调整动作。']][i]
 s+=text(310,y+109,lines[0],28)+text(310,y+152,lines[1],28)
 if i<3:s+=path(f'M360 {y+208} v10',G,3,True)
finish(s,'05-pick-place',h,'动作示意，非型号实拍；具体传感器因任务而异。')

h=1410;s=base(6,'英伟达产品，放回系统里看','先分清设备运行与研发工具，再看采用范围',h)
s+=rect(32,202,656,59,G)+text(54,243,'汽车：计算硬件与驾驶软件',31,'white',600)
for y,t,d in [(286,'DRIVE Orin / Thor','车载计算：运行相应程序'),(409,'DriveOS','基础软件：支持程序使用硬件'),(532,'DRIVE AV','驾驶软件：提供相应驾驶功能')]:
 s+=text(54,y+28,t,32,G,600)+text(54,y+76,d,29)+path(f'M54 {y+102} H666',L,2)
s+=rect(32,665,656,59,G)+text(54,706,'机器人：设备端与研发端',31,'white',600)
for y,t,d in [(754,'Jetson → 设备端计算','计算模块，需集成到完整机器'),(877,'Isaac Sim / Lab → 研发','模拟环境、学习与评估工具'),(1000,'Isaac ROS → 应用开发','加速软件包，支持部分感知等功能'),(1123,'GR00T → 模型资源','需要按任务与机器结构进行适配')]:
 s+=text(54,y+28,t,31,G,600)+text(54,y+76,d,29)+path(f'M54 {y+102} H666',L,2)
s+=text(32,1309,'可按需要组合，不代表必须全部购买或采用。',28,G,600)
finish(s,'06-product-roles',h,'此处列示产品角色；具体支持范围按版本确认。')

# article integrates diagrams immediately after their concrete explanation.
s=(A/'article-v2.md').read_text()
s=s.replace('新闻报道式科普稿v2','图解阅读稿v3')
s=s.replace('## 写作提纲','## 写作提纲（归档，不进入HTML正文）')
s=s.replace('这些是功能', '这些是功能')
anchors=[('这一过程解释了为什么', '01-braking','图1｜先看辅助减速的完整过程。'),('#### 车企选择不同的技术组合','02-car-layers','图2｜硬件、软件和车辆执行，是不同的组成部分。'),('英伟达的汽车开发产品也延伸到这一侧','03-development','图3｜开发不是一次完成，测试结果会带来下一轮修改。'),('#### 搬运与抓取，需要不同的技术配合','04-robot-map','图4｜同一形态可以进入不同场景，分类之间存在交叉。'),('这意味着，换一颗更强的芯片','05-pick-place','图5｜用一次抓取看清机械、感知与控制的配合。'),('#### 从实验动作到持续工作','06-product-roles','图6｜把产品名称放回已经认识的系统位置。')]
for anchor,name,caption in anchors:
 s=s.replace(anchor,f'![{caption}](assets/guide-v1/{name}.png)\n\n{caption}\n\n'+anchor,1)
(A/'article-v3.md').write_text(s)
# Use established Markdown inline renderer, override superseded heading decoration.
root=A.parent.parent
spec=importlib.util.spec_from_file_location('renderer',root/'scripts/render.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
print('renderer functions:',[k for k in dir(mod) if k.startswith('render')])
(P/'manifest.json').write_text(json.dumps([{'file':name+'.png','caption':cap,'source':'原创矢量科普示意，非产品实拍'} for _,name,cap in anchors],ensure_ascii=False,indent=2))
theme=json.loads((root/'assets/theme.json').read_text())
theme['h2']='font-size:20px;font-weight:700;color:#17633F;margin:38px 0 18px;line-height:1.55;letter-spacing:0.5px;'
theme['h3']='font-size:18px;font-weight:650;color:#17633F;margin:30px 0 14px;line-height:1.6;letter-spacing:0.5px;'
theme['h4']=theme['h3']
theme['img']='display:block;width:100%;max-width:100%;height:auto;margin:24px auto 8px;'
body=s.split('## 正文\n',1)[1]
body=body.replace('### ','## ').replace('#### ','### ')
# Strip internal source management instructions; preserve all public source URLs.
rendered=mod.render(body,theme)
rendered=re.sub(r'<p[^>]*><strong[^>]*>内容提要：(.*?)</strong></p>',r'<section style="background:#F2F7F3;padding:14px 16px;margin:22px 0;font-size:15px;line-height:1.8;color:#365B46;"><strong style="color:#17633F;">内容提要</strong><br>\1</section>',rendered,flags=re.S)
rendered=re.sub(r'<p[^>]*>(图[1-6]｜.*?)</p>',r'<p style="margin:8px 0 26px;font-size:13px;line-height:1.65;color:#557366;text-align:left;">\1</p>',rendered)
# Superscript source links target numbered source paragraphs without expanding prose.
main,tail=rendered.split('<h2',1) if False else (rendered,'')
rendered=re.sub(r'\[(\d+)\]',lambda m:f'<sup style="font-size:11px;color:#557366;">[{m.group(1)}]</sup>',rendered)
article=f'''<section id="article" style="{theme['container']}max-width:640px;margin:0 auto;padding:18px 14px 36px;box-sizing:border-box;">
<p style="font-size:13px;color:#557366;letter-spacing:2px;margin:14px 0;">旁观机器 · 图解阅读</p>
<h1 style="{theme['h1']}">从汽车到机器人：<br>英伟达的产品用在哪里？</h1>
{rendered}</section>'''
(A/'article-v3-body.html').write_text(article)
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>从汽车到机器人｜旁观机器</title><style>html{background:#eef2ee}body{margin:0}main{max-width:440px;margin:20px auto;background:white;box-shadow:0 8px 32px #173e2910}nav{max-width:640px;margin:16px auto;padding:0 14px;font:13px/1.7 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif;color:#557366}button,a.tool{border:1px solid #c7ddcf;background:white;color:#17633f;padding:7px 12px;border-radius:5px;cursor:pointer;font:inherit;text-decoration:none;display:inline-block;margin:4px 5px 4px 0}img{cursor:zoom-in}dialog{border:0;padding:8px;max-width:96vw;max-height:94vh;background:#fff}dialog::backdrop{background:#16251fcc}dialog img{width:720px;max-width:90vw;height:auto}dialog button{position:sticky;top:0;float:right}@media(max-width:480px){main{margin:0;box-shadow:none}nav{margin:10px auto}html{background:white}}</style></head><body><nav>文字与图片综合审阅版 · 点击图片可放大<br><button onclick="document.querySelector('main').style.maxWidth='440px'">手机宽度</button><button onclick="document.querySelector('main').style.maxWidth='720px'">宽屏阅读</button><a class="tool" href="guide-v1-images.zip" download>下载6张图片</a><span id="copyStatus"></span><br>复制到135后，请用图片包上传并替换图片；本地图片链接不会自动成为公众号素材。</nav><main>'''+article+'''</main><dialog id="zoom"><button onclick="this.parentElement.close()">关闭 ×</button><img alt="放大图解"></dialog><script>document.querySelectorAll('main img').forEach(im=>im.addEventListener('click',()=>{const d=document.getElementById('zoom');d.querySelector('img').src=im.src;d.querySelector('img').alt=im.alt;d.showModal()}));document.getElementById('zoom').addEventListener('click',e=>{if(e.target.tagName==='DIALOG')e.target.close()});</script></body></html>'''
(A/'article-v3.html').write_text(page)
