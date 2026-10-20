from pathlib import Path
import re,html,json,base64
root=Path(__file__).resolve().parents[3]
d=root/'articles/2026-10-ai-kaogong'
src=(d/'article-v9.md').read_text()
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
(d/'article-v9-body.html').write_text(body)
page='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>用 AI 卷考公</title></head><body style="margin:0;background:#ffffff;"><main style="max-width:680px;margin:0 auto;padding:16px 0 48px;">'+body+'</main></body></html>'
(d/'article-v9.html').write_text(page)
print('Generated article-v9.html and article-v9-body.html from article-v9.md')
