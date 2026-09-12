"""Build reviewed v12 text into v13: inline HTML, exact raster tables, image manifest."""
from pathlib import Path
import importlib.util,json,re,html,base64,sys
H=Path(__file__).resolve().parent; R=H.parents[2]; A=H.parent/'assets/v13'; I=A/'images'; C=A/'cards'
for d in [I,C]:d.mkdir(parents=True,exist_ok=True)
sp=importlib.util.spec_from_file_location('render',R/'scripts/render.py');mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
t=json.loads((R/'assets/theme.json').read_text());t['h2']=t['h2'].replace('border-bottom:1px solid #C7DDCF;','').replace('padding-bottom:10px;','');t['img_caption']='text-align:left;font-size:12px;color:#758279;margin:8px 0 22px;line-height:1.6;letter-spacing:0;'
md=(H/'article-v12.md').read_text(); title=md.splitlines()[0][2:]
css='''*{box-sizing:border-box}body{margin:0;background:#fff;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:#243e30}main{width:366px;padding:14px 12px 12px;background:#f5f8f5;border-top:3px solid #17633f}h1{font-size:19px;line-height:1.4;margin:0 0 12px;color:#17633f}p{font-size:14px;line-height:1.55;margin:5px 0}h2{font-size:16px;line-height:1.4;margin:0 0 5px;color:#17633f}.row{padding:10px 0;border-top:1px solid #c7ddcf}.row:first-of-type{border:0}.note{font-size:12px;color:#6c7d70;line-height:1.5;margin-top:10px}.label{font-size:12px;letter-spacing:1px;color:#507b60;margin-bottom:5px}table{width:100%;border-collapse:collapse;table-layout:fixed;font-size:14px;line-height:1.5}th{text-align:left;font-weight:600;color:#17633f;background:#e6efe8}td,th{padding:8px 6px;vertical-align:top;border-bottom:1px solid #c7ddcf;overflow-wrap:anywhere}td:first-child{font-weight:500}tr:last-child td{border-bottom:0}td small{font-size:12px;color:#5d7567;display:block;line-height:1.5;margin-top:4px}img{width:100%;height:auto;display:block}strong{color:#17633f}a{color:inherit;text-decoration:none}.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}.box{padding:10px;background:white;border:1px solid #d6e4da}.arrow{text-align:center;font-size:18px;margin:4px 0;color:#507b60}.footer{font-size:10px;letter-spacing:1px;color:#789281;margin-top:12px}'''
assets=[]
def card(id,title,body,note='',caption=None):
 widths={'16-product-map':[34,66],'18-price-snapshot':[50,25,25],'08-software-layers':[42,58],'12-quote-scope':[31,69]}.get(id)
 if widths:body=body.replace('<table>','<table><colgroup>'+''.join(f'<col style=\"width:{w}%\">' for w in widths)+'</colgroup>',1)
 doc=f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>{css}</style><main><h1>{title}</h1>{body}'+(f'<p class="note">{note}</p>' if note else '')+'<div class="footer">旁观机器 / MACHINE OBSERVER</div></main></html>'
 (C/f'{id}.html').write_text(doc)
 assets.append({'id':id,'kind':'精确排版图表','title':title,'file':f'images/{id}.png','caption':caption or title,'source':'依据已审 v12 正文整理；引用见对应段落'})
 return id

def rows(items):return ''.join(f'<div class="row"><h2>{h}</h2><p>{p}</p></div>' for h,p in items)
def table(head,rs):return '<table><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in r)+'</tr>' for r in rs)+'</tbody></table>'
card('04-online-local','AI 在哪里运行？',rows([('在线 AI 服务','电脑提交输入、展示结果<br>模型的主要计算在服务商云端完成'),('本地模型','下载模型和运行软件<br>由自己的设备完成模型计算')]),'在线服务与本地部署各有用途，不能仅凭本机显卡判断云端生成速度。')
card('07-enterprise-options','企业使用模型的三种方式',rows([('调用模型 API','例：接入阿里云百炼的千问服务<br><strong>服务商运行模型</strong>；企业连接业务数据与应用。'),('租云端算力，自行部署','例：租用云端 GPU 服务器运行 Qwen<br><strong>服务商提供设备资源</strong>；企业部署、维护模型。'),('使用自己的设备部署','例：在企业自有电脑或服务器运行模型<br><strong>企业配置设备</strong>，并负责模型与应用。')]),'三种方式可以组合；API 是接口形式，并非某一种部署方式的专属名称。')
card('08-software-layers','这些软件处在不同层级',table(['产品','主要作用'],[['CUDA / Toolkit','使用 GPU 的基础平台与开发工具'],['NeMo','开发、定制和评估受支持模型'],['TensorRT / TensorRT-LLM','优化模型推理执行'],['NIM','打包好的模型推理服务'],['AI Enterprise','企业软件平台及相应支持']]),'不是依次必选的套装。上层工具也可采用 vLLM 等开源方案；使用 NVIDIA GPU 不等于使用其全部软件。')
card('10-connections','三种传输，连接不同对象',rows([('显存 ↔ GPU','显存保存模型和工作数据。<br>显存带宽反映这里的数据传输能力。'),('GPU ↔ GPU','多个 GPU 协作时交换数据。<br>英伟达提供 NVLink 等互连能力。'),('服务器 ↔ 服务器','跨设备分配任务、传输数据。<br>涉及网卡、交换机和服务器网络。')]),'不同环节的带宽不能合成一个数字。示意按功能分层，不是所有系统的固定拓扑。')
card('12-quote-scope','看报价，先看交付范围',table(['报价对象','需要核对什么'],[['GPU 板卡','具体型号、数量；现有服务器是否兼容'],['GPU 服务器','是否实际包含 GPU，以及 CPU、内存、硬盘、网卡、电源'],['机柜系统','计算设备、互连、配电、冷却组件及安装范围']]),'另行确认：机房改造、模型部署与后续维护。支持安装 GPU，不等于报价已经包含 GPU。')
card('16-product-map','七块产品，一张版图',table(['领域','本文涉及的产品'],[['个人图形与创作','GeForce RTX、Studio'],['专业图形与电脑','RTX PRO'],['数据中心计算','A / H / B、Rubin；Grace / Vera；HGX / MGX / DGX'],['网络与互连','NVLink、ConnectX、Spectrum-X、Quantum、BlueField'],['边缘与机器人','Jetson、IGX、Isaac'],['汽车','DRIVE AGX、DriveOS、Hyperion'],['软件、模型与云','CUDA、NeMo、TensorRT、NIM、Nemotron、Omniverse、DGX Cloud']]),'按功能整理，部分产品跨领域使用；不同层级不代表必须配套采购。')
# Preserve all existing table text; combine name and expansion for a phone-friendly two-column glossary.
tables=re.findall(r'^\|.*\n\|[-: |]+\n(?:\|.*(?:\n|$))+',md,re.M)
assert len(tables)==3,len(tables)
for i,(raw,id,heading) in enumerate(zip(tables,['05-local-models','17-glossary','18-price-snapshot'],['可本地运行的模型例子','基础概念速查','两种官方挂牌价样本'])):
 rr=[[html.escape(c.strip()) for c in line.strip().strip('|').split('|')] for line in raw.strip().splitlines()]
 head,rs=rr[0],rr[2:]
 if i==1:head=['名称与英文','作用'];rs=[[r[0]+'<small>'+r[1]+'</small>',r[2]] for r in rs]
 note=['提供可下载权重，使用范围以具体许可证为准。','统一内存设备不能简单按独立显卡的方式划分。','2026年9月12日，美国 NVIDIA 商城网页快照。均显示缺货；不是出厂价，税费与运费未确认。'][i]
 card(id,heading,table(head,rs),note)
# Product artwork is shown whole, with factual caption outside the original image.
products=[('03-geforce','rtx5090','GeForce RTX 5090','桌面显卡：需要装入兼容的电脑使用。'),('06-rtx-pro','rtxpro6000','RTX PRO 6000 Blackwell','Workstation Edition · 专业显卡，不是一台完整电脑。'),('09-dgx-spark','dgxspark','DGX Spark','图右侧的小型主机是 DGX Spark，已内置 CPU 与 GPU；左侧笔记本展示连接使用的场景。'),('11-gb200','gb200','GB200 NVL72','液冷机柜系统；与单张显卡属于不同交付层级。'),('14-jetson','jetson','Jetson Orin 家族','包括计算模块与开发套件；具体形态按型号区分。'),('15-drive','drive','DRIVE 车载计算平台','用于车载计算开发与集成；图为 NVIDIA 官方平台示意。')]
for id,key,heading,desc in products:
 card(id,heading,f'<img src="../originals/{key}.jpg"><p style="margin-top:10px">{desc}</p>','原图：NVIDIA 官方产品页；图片按原比例展示，不代表产品之间的实际尺寸。')
 assets[-1]['kind']='官方产品图＋说明';assets[-1]['source']=key
for id,kind,title_,file,cap in [('01-header','既有品牌图','旁观机器','images/01-header.png',''),('02-computing-lab','AI 场景插画','计算的不同工作环境','images/02-computing-lab.png','个人电脑、专业创作与服务器环境｜AI 概念插画'),('13-robot-lab','AI 场景插画','分拣机器人的实验室','images/13-robot-lab.png','视觉识别、设备计算与仿真环境｜AI 概念插画，非实物接线图')]:
 assets.append({'id':id,'kind':kind,'title':title_,'file':file,'caption':cap,'source':'品牌已选素材' if kind=='既有品牌图' else '内置 image_gen，提示词见 prompts.json'})
assets.sort(key=lambda x:x['id']);(A/'manifest.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2)+'\n')
if '--prepare' in sys.argv:print('Prepared',len(assets),'assets');sys.exit()
assetmap={x['id']:x for x in assets}
def markdown_image(id):
 a=assetmap[id];return f'\n\n![{a["caption"] or a["title"]}](../assets/v13/{a["file"]})\n\n'
# Insert only after complete paragraphs, maintaining the approved argument and wording.
anchors={'02-computing-lab':'本文以这些用户的工作为线索','03-geforce':'对玩家来说，显卡影响','04-online-local':'个人使用 AI，既可以','06-rtx-pro':'例如，桌面 RTX 5090 配备','07-enterprise-options':'这两种方式最终都可以通过 API','08-software-layers':'这些工具可以协作','09-dgx-spark':'对于能够在本机完成的实验','10-connections':'这里的“带宽”也有了不同对象','11-gb200':'以 GB200 为例','12-quote-scope':'这些条件也决定了一份报价','13-robot-lab':'假设一家企业开发分拣机器人','14-jetson':'**Jetson 是英伟达','15-drive':'**DRIVE AGX 是','16-product-map':'因此，设备厂商购买的可以是'}
for id,start in anchors.items():
 pattern=r'(^'+re.escape(start)+r'[^\n]+)';md,n=re.subn(pattern,lambda m:m[0]+markdown_image(id),md,count=1,flags=re.M);assert n==1,id
(H/'article-v13.md').write_text(md)
# Only the HTML replaces the three text tables with exact PNGs.
for raw,id in zip(tables,['05-local-models','17-glossary','18-price-snapshot']):md=md.replace(raw,markdown_image(id))
refs=[];index={}
def cite(m):
 label,url=m.groups()
 if url not in index:index[url]=len(refs)+1;refs.append({'number':len(refs)+1,'title':label,'url':url})
 return f'〔{index[url]:02}〕'
md=re.sub(r'(?<!!)\[([^\]]+)\]\((https?://[^)]+)\)',cite,md)
body=mod.render('\n'.join(md.splitlines()[1:]),t)
# Titles are already inside the PNG; keep only explanatory AI scene captions below images.
for item in assets:
 if item['kind'] not in ('AI 场景插画','既有品牌图'):
  body=body.replace('<p style=\"'+t['img_caption']+'\">'+html.escape(item['caption'])+'</p>','')
body=re.sub(r'<p style="margin:0;">(<h2.*?</h2>)</p>',r'\1',body,flags=re.S)
body=re.sub(r'〔(\d+)〕',lambda m:f'<a href="{html.escape(refs[int(m[1])-1]["url"],quote=True)}" style="font-size:11px;color:#668573;text-decoration:none;vertical-align:super;letter-spacing:0;">[{m[1]}]</a>',body)
header=f'<img src="../assets/v13/images/01-header.png" alt="旁观机器" style="width:100%;height:auto;display:block;margin:0 0 20px;"><h1 style="{t["h1"]}">算力生意（上）：<br>英伟达的产品版图</h1>'
refhtml='<section style="margin:36px 0 20px;padding:14px 12px;background:#F5F8F5;"><p style="font-size:14px;font-weight:600;color:#17633F;margin:0 0 12px;">来源与进一步阅读</p>'
for s in refs:refhtml+=f'<p style="font-size:12px;line-height:1.6;letter-spacing:0;margin:7px 0;color:#607568;">[{s["number"]:02}] <a href="{html.escape(s["url"],quote=True)}" style="color:#607568;text-decoration:none;">{html.escape(s["title"])}</a></p>'
refhtml+='<p style="font-size:12px;line-height:1.6;color:#748579;margin:14px 0 0;">产品实物与平台图片来源：NVIDIA 官方产品页。场景插画由 AI 生成；图表依据正文整理。</p></section>'
fragment='<section style="'+t['container']+'">'+header+body+refhtml+'</section>'
def embed(m):
 p=(H/m[1]).resolve();assert p.is_file(),p
 return 'src="data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()+'"'
embedded=re.sub(r'src="(\.\./assets/v13/images/[^\"]+)"',embed,fragment)
def doc(f):return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title></head><body style="margin:0;background:#f1f3f1;"><article style="max-width:650px;margin:0 auto;background:#fff;padding:18px 0 30px;">'+f+'</article></body></html>'
(H/'article-v13.html').write_text(doc(embedded));(H/'article-v13-fragment.html').write_text(embedded);(H/'article-v13-local.html').write_text(doc(fragment));(A/'article-sources.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
print('Built article-v13 HTML:',len(assets),'images,',len(refs),'source links')
