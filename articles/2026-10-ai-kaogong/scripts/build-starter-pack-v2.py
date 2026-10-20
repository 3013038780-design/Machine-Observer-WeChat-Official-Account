from pathlib import Path
import re,html,json,hashlib,zipfile,shutil
p=Path(__file__).resolve().parents[1]
v1=p/'starter-pack';d=p/'starter-pack-v2';d.mkdir(exist_ok=True)
for name in ['预设','六张方法卡.md','独立练习记录.csv','公开项目导航.md','先试一道自拟题.txt']:
 src=v1/name;dst=d/name
 if src.is_dir():shutil.copytree(src,dst,dirs_exist_ok=True)
 else:shutil.copyfile(src,dst)
article=(p/'article-v13.md').read_text()
base='https://github.com/3013038780-design/civilserviceexam/'
project='''# Civil Service Exam：现在能用什么，下一步补什么

快照日期：2026-10-20。项目主页：https://github.com/3013038780-design/civilserviceexam

## 它在做什么
把可核查的解题依据整理成“识别信号→具体动作→停止条件→边界”，用不同年份的真题修订，再让学习者在未讲过的题里独立执行。Skills保留方法与教学规则，网站承担阅读和练习，逐题证据记录检验。

## 当前可以分享的成果
- 分类方法与跨年示范已经形成。代码/研究分支的结构化方法有35张卡，其中26个分支有教学结构；这是内容结构数，不是个人掌握数。
- 最近核验的私人线上版有2026副省级行测135题入口、35张方法卡、26个带流程与示范的分支、78道答案分离试用题（67真题、11自拟）。这里说的是上次实际核验的发布状态，本轮没有重新部署私人站点。
- 定义判断与资料分析已有成组逐题处理、失败边界与回查；主旨、排序、填句、插句、下文预测已有不同程度的跨年检验。阅读、选词、逻辑、类比还有扩验工作。
- 申论保留2026副省级五题首答核验、材料映射与初步策略；不是已验证的万能模板。
- 本包提供文章里的三组可独立阅读的示范，解决读者无法登录私人网站的问题。它不是135题完整版。

## 还不能叫完整成品的地方
1. 教学能否让人照着做：用户此前明确反馈流程仍难读。已有内容需要继续验证“先看一题，再模仿一步”的讲法。
2. 当前主攻分类尚未全部检验完成；已有样例不代表所有真实任务都覆盖。
3. 用户无辅助、限时、未讲过题目的表现尚未测，不能证明个人提分。
4. 本地与线上并非完全同步：当前续接记录为本地2007正式来源位置、线上1977，30个来源及下文正反方向新版还未发布。这是来源位置，含同题跨卷，不是2007道独立新题测评。
5. 网站仅所有者访问；公开GitHub供读代码、原创方法和索引，不等于公开在线答题产品。

## 推荐完善顺序
先把一条教学路径做顺：读一道示范→学习者自己说依据→做一道未讲过同类题→记录答案/用时/提示依赖→改难懂步骤。重点是“下次能独立做”，不是加更多页面。
随后按现有OpenSpec顺序补中心排序相关任务、阅读、选词、逻辑、类比，定义复用。2010年为新增研究下限，图推数量继续暂缓。资料政治常识申论保留旧成果，本阶段不自动恢复研究。
再集中同步真正影响作答的规则到私人网站，并按已批准的公开边界提供可分享示范。个人迁移效果单独验收。

## 怎么算一个可分享的教学单元完成
- 有完整、可读的题目与必要材料；题型入口能识别。
- 每个步骤都能从题面找到依据，有停止条件与反例。
- 示范和未讲练习分开，答案默认分离。
- 学习者能复述并独立试；没有真人数据就标“个人迁移待测”。
- 来源和争议可查，公开入口无需私人站点登录。

## 入口
- 分类方法：https://github.com/3013038780-design/civilserviceexam/blob/codex/corpus-strategies/行测分类通用方法.md
- 行测Skill：https://github.com/3013038780-design/civilserviceexam/blob/codex/corpus-strategies/.agents/skills/xingce-strategy/SKILL.md
- 申论Skill：https://github.com/3013038780-design/civilserviceexam/blob/codex/corpus-strategies/.agents/skills/shenlun-strategy/SKILL.md
- 私人站点：https://gongkao-study-studio.easy-tern-3117.chatgpt.site/（当前非公开访问）
'''
(d/'Civil-Service-Exam项目介绍与完善顺序.md').write_text(project)
# Full three case sections copied from the already published article, without full third-party corpora.
def segment(start,end):return article[article.index(start):article.index(end,article.index(start))].strip()
case1=segment('## 一道资料题：','## 言语也能拆？')
case2=segment('## 言语也能拆？','## 复盘 Skill：')
case3=segment('## 申论：','## 最近我也在考公')
review=segment('## 复盘 Skill：','## 申论：')
cases='# 三组真题示范与测试记录\n\n沿用文章已展示的题面、必要材料节选和解释。两个行测例子是已有答案回放，申论是材料片段加工；两道改编精度题、模拟复盘单独标明。不是新一轮盲测或用户成绩。\n\n'+case1+'\n\n'+case2+'\n\n'+review+'\n\n'+case3+'\n'
(d/'三组真题示范与测试.md').write_text(cases)
# Necessary citations and limits accompany the examples.
(d/'资料来源与使用范围.md').write_text('''# 来源与使用范围

日期：2026-10-20。

三组案例来自《AI也开始跟花生十三学考公了》已展示的题目/材料：2026国考副省级行测131、2015国考副省级行测44、2026国考副省级申论第1题。引用题面按项目采用的主版本，资料与申论材料为必要节选；没有附整套原卷或机构解析PDF。示范包含已知答案，不计未见新题。

资料精度变式为原创改编，模拟复盘不是实际考生记录。全部方法执行与数字复核来自既有文章测试，没有新报告跨客户端正确率或个人提分。

六张方法卡、七份通用预设、自拟题、指引与项目介绍为本项目整理。七份预设可复制到文字对话，不代表安装原版教师Skill、读取全部仓库或训练模型权重。

外部项目给原仓库与具体文件链接，详情见导航；教师方法为社区整理，不称官方出品。外部文件、安装脚本、自动写回与第三方题库没有打包。

资料不包含私人学习网站数据、账号、个人笔记或完整题库。完整站点访问限制未改变。资料包可以离线阅读，不依赖站点登录；外部链接和AI对话需要网络及自行准备的工具。

公开项目：https://github.com/3013038780-design/civilserviceexam
文章源稿：https://github.com/3013038780-design/Machine-Observer-WeChat-Official-Account/blob/main/articles/2026-10-ai-kaogong/article-v13.md
测试说明：https://github.com/3013038780-design/Machine-Observer-WeChat-Official-Account/blob/main/articles/2026-10-ai-kaogong/research/skill-method-tests-v1.md
''')
style='''body{margin:0;background:#f3f6f3;color:#27372f;font:16px/1.85 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}main{max-width:820px;margin:auto;background:white;padding:26px 18px 64px}h1{font-size:28px;line-height:1.5;color:#17633f}h2{font-size:22px;color:#17633f;margin:40px 0 18px;border-bottom:1px solid #c7ddcf;padding-bottom:10px}h3{font-size:18px;color:#287a51;margin-top:28px}p{margin:15px 0}a{color:#17633f;overflow-wrap:anywhere}nav,.card{background:#f2f7f3;border-left:4px solid #17633f;padding:14px 16px;margin:20px 0}nav a{display:inline-block;margin:4px 14px 4px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f5f7f5;padding:14px;font:15px/1.8 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif}table{border-collapse:collapse;width:100%;table-layout:fixed;margin:18px 0}th,td{padding:10px 8px;border:1px solid #d5e2d9;vertical-align:top;text-align:left;overflow-wrap:anywhere;font-size:15px}th{background:#f2f7f3;color:#17633f}blockquote{border-left:3px solid #17633f;background:#f5f8f5;padding:10px 16px;margin:18px 0}blockquote p{margin:9px 0}details{margin:20px 0;border:1px solid #c7ddcf;padding:14px 16px;border-radius:4px}summary{color:#17633f;cursor:pointer;font-weight:700}strong{color:#17633f}li{margin:10px 0}code{overflow-wrap:anywhere}hr{margin:36px 0;border:0;border-top:1px solid #c7ddcf}'''
def inline(s):
 tokens=[]
 def hold(m):
  tokens.append('<a href="'+html.escape(m[2],quote=True)+'">'+html.escape(m[1])+'</a>');return '\x00'+str(len(tokens)-1)+'\x00'
 s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',hold,s);s=html.escape(s,quote=False)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s);s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'https?://[^\s<（）()]+',lambda m:'<a href="'+html.escape(html.unescape(m[0]),quote=True)+'">'+m[0]+'</a>',s)
 return re.sub(r'\x00(\d+)\x00',lambda m:tokens[int(m[1])],s)
def md(s):
 lines=s.splitlines();out=[];i=0
 while i<len(lines):
  x=lines[i]
  if not x.strip():i+=1;continue
  if x.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    cells=[z.strip() for z in lines[i].strip('|').split('|')]
    if not all(re.fullmatch(r':?-+:?',z) for z in cells):rows.append(cells)
    i+=1
   out.append('<table>'+''.join('<tr>'+''.join('<'+('th' if n==0 else 'td')+'>'+inline(z)+'</'+('th' if n==0 else 'td')+'>' for z in row)+'</tr>' for n,row in enumerate(rows))+'</table>');continue
  if x.startswith('>'):
   parts=[]
   while i<len(lines) and lines[i].startswith('>'):
    t=lines[i][1:].strip()
    if t:parts.append('<p>'+inline(t)+'</p>')
    i+=1
   out.append('<blockquote>'+''.join(parts)+'</blockquote>');continue
  m=re.match(r'^(#{1,4}) (.*)',x)
  if m:level=min(len(m[1])+1,4);out.append(f'<h{level}>'+inline(m[2])+f'</h{level}>')
  elif x=='---':out.append('<hr>')
  else:out.append('<p>'+inline(x)+'</p>')
  i+=1
 return '\n'.join(out)
def shell(title,body):return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+style+'</style></head><body><main>'+body+'</main></body></html>'
# v1 beginner guide stays complete; its text contents are embedded in the single-file reader.
guide=(v1/'从这里开始.html').read_text();guide=re.search(r'<main>([\s\S]+)</main>',guide)[1]
guide=guide.replace('<h1>AI 考公上手包</h1>','<h2>一、零基础上手指引</h2>').replace('v1 · 2026-10-20','v2 · 2026-10-20')
# Preserve all inner anchors from the existing guide, and include a clear navigation back.
nav='<nav><a href="#guide">①怎么开始</a><a href="#catalog">②项目导航</a><a href="#preset">③七份预设</a><a href="#methods">④六张方法卡</a><a href="#cases">⑤三组真题</a><a href="#project">⑥自己的项目</a></nav>'
guide=guide.replace('<h2>六张方法卡：不需要AI就能读</h2>','<h2 id="methods">六张方法卡：不需要AI就能读</h2>')
# Catalog from v1 includes all 13 repositories plus own project.
catalog=(d/'公开项目导航.md').read_text()
# Add scene selection without claiming unperformed installs.
scene='''| 现在要做什么 | 优先看哪种入口 | 怎么开始 |
| --- | --- | --- |
| 学资料速算 | 花生十三、红领巾资料 | 先看具体方法及适用条件，再用02处理自己的题 |
| 学言语读题 | 红领巾言语/选词 | 先读题型对应方法，不一次加载全库 |
| 做完想复盘 | 行测复盘一体版 | 读复盘协议；只想复制试用可先用04 |
| 申论找点组织 | 申论方法整理、申论训练营 | 发完整题干与材料，再用05检查归并依据 |
| 时政整理 | 考公AI导师、青岸等 | 读原说明，保留来源日期；别把入口当自动抓新闻 |
'''
(d/'按场景选择工具.md').write_text('# 按场景选择工具\n\n'+scene+'\n入口与安装支持按原项目说明核对。本包不预装第三方Skill。\n')
# Three demonstrations: question always visible, explanation collapses by default.
def detail_case(title,question,teaching,idx):
 return '<section id="case-'+idx+'"><h3>'+title+'</h3>'+md(question)+'<details class="case-answer"><summary>独立尝试后，展开解法、测试与边界</summary>'+md(teaching)+'</details></section>'
data_marker='这是资料分析里的熟人局：';data_q=case1[case1.index('**2026年'):case1.index(data_marker)]
data_teach=case1[case1.index(data_marker):]
verbal_start=case2.index('**2015年');verbal_cut=case2.index('如果只看主题词')
verbal_q=case2[verbal_start:verbal_cut];verbal_teach=case2[verbal_cut:]+'\n\n'+review
st=case3[case3.index('**2026年'):case3.index('250字，材料里')]
material=case3[case3.index('> 走进'):case3.index('真正该留下')]
shen_q=st+'\n\n给定资料1必要节选（中间省略部分句子）：\n\n'+material
shen_teach=case3[case3.index('真正该留下'):]
case_body='<h2 id="cases">五、三组真题：先看题，再展开解法</h2><p>这是文章的教学示范回放，不是新盲测。每组先显示原题，讲解默认折叠；资料与申论只引用本题所需材料节选。</p>'
case_body+=detail_case('资料分析 · 2026国考副省级行测131',data_q,data_teach,'data')
case_body+=detail_case('下文预测 · 2015国考副省级行测44',verbal_q,verbal_teach,'verbal')
case_body+=detail_case('申论材料加工 · 2026国考副省级申论1',shen_q,shen_teach,'shenlun')
case_body+='<p><a href="独立练习记录.csv">打开独立练习记录模板</a> · <a href="先试一道自拟题.txt">另试一道原创自拟题</a></p>'
guide_part,preset_rest=guide.split('<h2 id="preset">',1)
preset_part,method_rest=preset_rest.split('<h2 id="methods">',1)
method_part,help_rest=method_rest.split('<h2 id="skills">',1)
help_part=help_rest.split('<h2>这个包包含什么</h2>',1)[0]
content='<h1>AI考公资料包 · 完整阅读版</h1><p>旁观机器 · v2 · 2026-10-20</p><div class="card"><strong>只打开这一个文件，也能读完六部分。</strong><p>指引、七份可复制预设、方法卡、工具导航、三组真题与项目介绍都在本页。完整解压后再打开，浏览器可直接读，不需要私人网站账号。</p></div>'+nav+'<section id="guide">'+guide_part+'</section>'
content+='<h2 id="catalog">二、公开项目导航：按用途挑</h2>'+md(scene)+md(catalog)
content+='<h2 id="preset">三、'+preset_part+'<h2 id="methods">四、'+method_part
content+=case_body+'<h2 id="project">六、我的项目：Civil Service Exam</h2>'+md(project)
content+='<h2 id="skills">'+help_part
content+='<h2>资料来源与范围</h2>'+md((d/'资料来源与使用范围.md').read_text())+'<p><a href="#guide">回到上手指引</a></p>'
(d/'00-从这里开始.html').write_text(shell('AI考公资料包·完整阅读版',content))
(d/'三组真题示范与测试.html').write_text(shell('三组真题示范与测试',case_body))
(d/'Civil-Service-Exam项目介绍.html').write_text(shell('Civil Service Exam 项目介绍与完善顺序',md(project)))
(d/'README.txt').write_text('''AI考公资料包·完整阅读版 v2

【第一步】完整解压文件夹。
【第二步】用浏览器打开“00-从这里开始.html”。六部分内容都在这一页，无需先打开Markdown，也无需私人网站登录。
【第三步】七份预设也另存在“预设”文件夹，可直接复制；练习记录在CSV文件。

包含：零基础指引、公开项目导航、七份预设、六张方法卡、三组真题示范与已有测试、Civil Service Exam项目成果与完善顺序。
本包是整理后的学习资料与通用对话指令，不是所有第三方Skill的自动安装包。真题仅为文章已展示的三组题/必要节选，未含整套课程、原卷或私人站点数据。
外部链接与AI对话需要联网；本页本身可离线阅读。
''')
# All full original quote lines in the article's three examples must be retained in the case file.
for part in [case1,case2,case3]:
 for line in re.findall(r'^>.*$',part,re.M):assert line in cases
manifest=[]
for f in sorted(d.rglob('*')):
 if f.is_file() and f.name!='文件清单.json':manifest.append({'path':f.relative_to(d).as_posix(),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(d/'文件清单.json').write_text(json.dumps({'version':'v2','date':'2026-10-20','files':manifest},ensure_ascii=False,indent=2)+'\n')
zip_path=p/'assets/AI考公资料包-完整阅读版-v2.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(d.rglob('*')):
  if f.is_file():z.write(f,'AI考公资料包-完整阅读版-v2/'+f.relative_to(d).as_posix())
print(json.dumps({'zip':str(zip_path),'files':len(manifest)+1,'bytes':zip_path.stat().st_size,'single_file_reader':True},ensure_ascii=False))
