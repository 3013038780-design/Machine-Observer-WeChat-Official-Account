from pathlib import Path
import re,html,json,base64
root=Path(__file__).resolve().parents[3]
d=root/'articles/2026-10-ai-kaogong'
src=(d/'article-v16.md').read_text()
theme=json.loads((root/'assets/theme.json').read_text())
def inline(s):
    tokens=[]
    def hold(m):
        text,url=m.group(1),m.group(2)
        label=html.escape(text)
        if text=='qingan-initiative-civil-service-examination-sprint-coach':
            label='<span style="font-size:13px;line-height:1.75;">qingan-initiative-civil-<br>service-examination-<br>sprint-coach</span>'
        tokens.append('<a href="'+html.escape(url,quote=True)+'" style="'+theme['a']+'">'+label+'</a>')
        return '\x00'+str(len(tokens)-1)+'\x00'
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',hold,s)
    s=html.escape(s,quote=False).replace('&lt;br&gt;','<br>')
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
        is_overview = rows[0] == ['GitHub 项目', '中文名与适用范围']
        cols = '<colgroup><col style="width:46%;"><col style="width:54%;"></colgroup>' if is_overview else ''
        rendered=[]
        for n,row in enumerate(rows):
            typ='th' if n==0 else 'td'
            sty=theme[typ]+'display:table-cell;vertical-align:top;overflow-wrap:anywhere;word-break:break-word;padding:10px 7px;line-height:1.7;letter-spacing:0;text-align:left;'
            if n==0: sty+='text-align:center;'
            elif n%2==0: sty+='background:#F7F9F8;'
            attrs=' scope="col"' if n==0 else ''
            rendered.append('<tr style="display:table-row;">'+''.join('<'+typ+attrs+' style="'+sty+'">'+inline(x)+'</'+typ+'>' for x in row)+'</tr>')
        head='<thead style="display:table-header-group;">'+rendered[0]+'</thead>'
        bodyrows='<tbody style="display:table-row-group;">'+''.join(rendered[1:])+'</tbody>'
        out.append('<table style="'+theme['table']+'display:table;table-layout:fixed;border-collapse:collapse;width:100%;">'+cols+head+bodyrows+'</table>');continue
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
    if line == '**想获取文中整理的资料，关注我，回复「考公AI」即可领取。**':
        out.append('<section style="margin:30px 0 12px;padding:22px 18px;background:#F2F7F3;border:1px solid #C7DDCF;border-left:4px solid #17633F;text-align:center;"><p style="margin:0;color:#17633F;font-size:17px;line-height:1.8;font-weight:bold;">想获取文中整理的资料，关注我，<br>回复<span style="font-size:22px;letter-spacing:2px;">「考公AI」</span>即可领取。</p></section>')
        i+=1;continue
    out.append(tag('p',line,theme['p']));i+=1
body='<section style="'+theme['container']+'">\n'+'\n'.join(out)+'\n</section>'
(d/'article-v16-body.html').write_text(body)
page='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 也开始跟花生十三学考公了</title></head><body style="margin:0;background:#ffffff;"><main style="max-width:680px;margin:0 auto;padding:16px 0 48px;">'+body+'</main></body></html>'
(d/'article-v16.html').write_text(page)
print('Generated article-v16.html and article-v16-body.html from article-v16.md')
