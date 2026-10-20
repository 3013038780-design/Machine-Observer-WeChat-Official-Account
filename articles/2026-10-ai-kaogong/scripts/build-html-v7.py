from pathlib import Path
import re,html,json,base64
root=Path(__file__).resolve().parents[3]
d=root/'articles/2026-10-ai-kaogong'
src=(d/'article-v6.md').read_text()
projects=[
('花生十三方法整理','WangJunqing-coder/huasheng13-skill','资料速算、言语、判断等行测方法'),
('考公AI导师','KeWang0622/kaogong-skill','行测、申论、面试、时政等综合辅导'),
('gongkao-practice','Why-com-ui/gongkao-practice.skill','生成练习、仿题、导入题库，含时政'),
('公务员考试备考指南','NanjingHJLP/hjlp-skills','综合备考与专项训练指导'),
('行测复盘一体版','liuyuexi1987/xingce-review-pro','先追问选择依据，再讲题、留复盘记录'),
('申论复盘一体版','liuyuexi1987/shenlun-review-pro','材料解析、作答对照与修改'),
('申论训练营','HuaXiLF/shenlun-trainer','小题提炼、失分分析、训练记录'),
('Hermes教育技能包','hezkvectory/hermes-edu-skills','行测与申论诊断、限时练习、复测'),
('红领巾分模块版','MUMU0208/redscarf-gongkao-skills','言语、填空、资料、判断、数量、错因'),
('七位申论名师方法整理','WangJunqing-coder/shenlun-skill','审题、材料阅读、申论题型方法'),
('白鹭、小马哥、袁东方法整理','coffe-d/Shenlun.skill','申论小题与作文分流'),
('青岸冲刺教练','XiaoSiKe/qingan-initiative-civil-service-examination-sprint-coach','冲刺安排、政治常识记忆与复测'),
('gongkao-distill','hilltahuang/gongkao-distill','按科目、教师整理的方法稿')]
table='## 先看看，考公人的 AI 搭子已经凑了多少\n\n这轮找到的公开入口，先摆一桌。下面列出 **13个外部仓库**，再加上自己的方法库和学习网站；同一项目可能兼做几件事。红领巾分模块版与复盘版有沿革关联，仓库数不等于独立方法体系数。\n\n| 项目，点名字直达 | 主要干什么 |\n| --- | --- |\n'
for name,repo,use in projects: table+=f'| [{name}](https://github.com/{repo}) | {use} |\n'
table+='| [自己的 Skills 与方法库](https://github.com/3013038780-design/civilserviceexam) | 把解题动作整理成能模仿、能检验的方法 |\n| [公考研习室](https://gongkao-study-studio.easy-tern-3117.chatgpt.site/) | 原题、方法、跨年示范和试用，当前私人访问 |\n\n按用途细分的文件链接留在文末，想先看哪一科，可以直接翻过去。\n\n'
src=src.replace('光看项目介绍还不过瘾，直接拿题试。',table+'人齐了。光看介绍还不过瘾，直接拿题试。')
src=src.replace('文章末尾把这几条入口分开列','文末详细索引把这几条入口分开列')
(d/'article-v7.md').write_text(src)
theme=json.loads((root/'assets/theme.json').read_text())
def inline(s):
    tokens=[]
    def hold(m):
        text,url=m.group(1),m.group(2)
        tokens.append('<a href="'+html.escape(url,quote=True)+'" style="'+theme['a']+'">'+html.escape(text)+'</a>')
        return '\x00'+str(len(tokens)-1)+'\x00'
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',hold,s)
    s=html.escape(s,quote=False)
    s=re.sub(r'\*\*(.+?)\*\*',lambda m:'<strong style="'+theme['strong']+'">'+m.group(1)+'</strong>',s)
    s=re.sub(r'`([^`]+)`',lambda m:'<code style="'+theme['code_inline']+'">'+m.group(1)+'</code>',s)
    return re.sub(r'\x00(\d+)\x00',lambda m:tokens[int(m.group(1))],s)
def tag(name,text,style):return f'<{name} style="{style}">{inline(text)}</{name}>'
lines=src.splitlines(); out=[]; i=0
header=root/'assets/brand/2026-09-12-header-v2/03-retro-terminal.png'
if header.exists():out.append('<img alt="旁观机器：复古电脑" src="data:image/png;base64,'+base64.b64encode(header.read_bytes()).decode()+'" style="display:block;width:100%;height:auto;margin:0 0 24px;">')
while i<len(lines):
    line=lines[i]
    if not line.strip():i+=1;continue
    if line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].startswith('|'):
            cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?',x) for x in cells):rows.append(cells)
            i+=1
        rendered=[]
        for n,row in enumerate(rows):
            typ='th' if n==0 else 'td'
            sty=theme[typ]+'text-align:left;vertical-align:top;overflow-wrap:anywhere;word-break:break-word;padding:9px 8px;'
            rendered.append('<tr>'+''.join(tag(typ,x,sty) for x in row)+'</tr>')
        out.append('<table style="'+theme['table']+'table-layout:fixed;">'+''.join(rendered)+'</table>');continue
    if line.startswith('>'):
        ps=[]
        while i<len(lines) and lines[i].startswith('>'):
            t=lines[i][1:].strip()
            if t:ps.append(tag('p',t,theme['blockquote_p']+'color:#333333;font-size:16px;'))
            i+=1
        out.append('<section style="'+theme['blockquote']+'">'+''.join(ps)+'</section>');continue
    m=re.match(r'^(#{1,4}) (.*)',line)
    if m:out.append(tag('h'+str(len(m[1])),m[2],theme['h'+str(len(m[1]))]));i+=1;continue
    if line=='---':out.append('<hr style="'+theme['hr']+'">');i+=1;continue
    if line.startswith('- '):
        items=[]
        while i<len(lines) and lines[i].startswith('- '):items.append(tag('li',lines[i][2:],theme['li']));i+=1
        out.append('<ul style="'+theme['ul']+'">'+''.join(items)+'</ul>');continue
    out.append(tag('p',line,theme['p']));i+=1
body='<section style="'+theme['container']+'">\n'+'\n'.join(out)+'\n</section>'
(d/'article-v7-body.html').write_text(body)
page='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>用 AI 卷考公</title></head><body style="margin:0;background:#ffffff;"><main style="max-width:680px;margin:0 auto;padding:16px 0 48px;">'+body+'</main></body></html>'
(d/'article-v7.html').write_text(page)
print('Generated article-v7.md, article-v7.html, article-v7-body.html; overview: 13 external repositories + 2 own entries')
