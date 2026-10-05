from pathlib import Path
import html,re

src=Path('articles/2026-10-codex-guide/part-1/article-v6.md').read_text()
lines=src.splitlines()
out=[]

def inline(s):
    s=html.escape(s, quote=False)
    # links after escape
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" style="color:#17633F;text-decoration:none;border-bottom:1px solid #C7DDCF;">\1</a>', s)
    s=re.sub(r'\*\*([^*]+)\*\*', r'<strong style="font-weight:700;color:#222222;">\1</strong>', s)
    s=re.sub(r'__([^_]+)__', r'<strong style="font-weight:700;color:#17633F;">\1</strong>', s)
    s=re.sub(r'`([^`]+)`', r'<code style="background:#f6f6f6;color:#17633F;padding:2px 5px;border-radius:3px;font-size:14px;font-family:SFMono-Regular,Consolas,monospace;">\1</code>', s)
    return s

i=0
while i<len(lines):
    line=lines[i]
    if not line.strip() or line.startswith('状态：'): i+=1; continue
    if line.startswith('# '):
        out.append('<h1 style="font-size:22px;font-weight:bold;color:#17633F;text-align:center;margin:36px 0 18px;line-height:1.42;letter-spacing:0.5px;">'+inline(line[2:])+'</h1>')
        out.append('<p style="text-align:center;color:#7A9A8A;font-size:13px;letter-spacing:2px;margin:0 0 30px;">和 Codex 一起工作 · 第一篇</p>')
        i+=1; continue
    if line.startswith('## '):
        title=line[3:]
        if title == '资料核验说明':
            out.append('<section style="margin:38px 0 18px;padding:18px 16px;background:#FAFAFA;border-top:2px solid #17633F;"><h2 style="font-size:17px;font-weight:bold;color:#17633F;margin:0 0 14px;line-height:1.42;letter-spacing:0.5px;">'+inline(title)+'</h2>')
        elif title == '资料来源':
            out.append('<h3 style="font-size:16px;font-weight:bold;color:#17633F;margin:22px 0 12px;line-height:1.42;letter-spacing:0.5px;">'+inline(title)+'</h3>')
        else:
            m=re.match(r'^([一二三四五六七八九十]+)、(.*)$', title)
            if m:
                nums={'一':'01','二':'02','三':'03','四':'04','五':'05','六':'06','七':'07','八':'08','九':'09','十':'10'}
                label=nums.get(m.group(1),m.group(1))
                clean=m.group(2)
            else:
                label=''; clean=title
            out.append('<section style="margin:42px 0 20px;padding:12px 14px;background:#F2F7F3;border:1px solid #C7DDCF;border-radius:4px;box-shadow:0 3px 10px rgba(23,99,63,0.06);"><div style="display:table;width:100%;border-collapse:collapse;"><div style="display:table-cell;width:58px;vertical-align:middle;color:#17633F;font-size:34px;font-weight:300;line-height:1;">'+label+'</div><div style="display:table-cell;vertical-align:middle;padding-left:14px;border-left:1px solid #B9D2C2;"><p style="margin:0;color:#17633F;font-size:18px;font-weight:bold;line-height:1.42;letter-spacing:0.5px;">'+inline(clean)+'</p></div></div></section>')
        i+=1; continue
    if line.startswith('### '):
        out.append('<h3 style="font-size:17px;font-weight:bold;color:#287A51;margin:28px 0 14px;line-height:1.42;letter-spacing:0.5px;">'+inline(line[4:])+'</h3>')
        i+=1; continue
    if line.startswith('> '):
        qs=[]
        while i<len(lines) and (lines[i].startswith('> ') or not lines[i].strip()):
            if lines[i].startswith('> '): qs.append('<p style="margin:6px 0;line-height:1.6;color:#5D7569;letter-spacing:0.5px;">'+inline(lines[i][2:])+'</p>')
            i+=1
        out.append('<blockquote style="margin:24px 0;padding:14px 18px;background:#F2F7F3;border-left:3px solid #17633F;color:#5D7569;font-size:15px;border-radius:2px;">'+''.join(qs)+'</blockquote>')
        continue
    if re.match(r'^[-*] ',line):
        items=[]
        while i<len(lines) and re.match(r'^[-*] ',lines[i]):
            items.append('<li style="margin:10px 0;line-height:1.6;letter-spacing:0.5px;">'+inline(lines[i][2:])+'</li>'); i+=1
        out.append('<ul style="margin:18px 0;padding-left:24px;">'+''.join(items)+'</ul>'); continue
    if re.match(r'^\d+\. ',line):
        items=[]
        while i<len(lines) and re.match(r'^\d+\. ',lines[i]):
            text=re.sub(r'^\d+\. ','',lines[i]); items.append('<li style="margin:10px 0;line-height:1.6;letter-spacing:0.5px;">'+inline(text)+'</li>'); i+=1
        out.append('<ol style="margin:18px 0;padding-left:24px;">'+''.join(items)+'</ol>'); continue
    # table
    if i+1<len(lines) and '|' in line and re.match(r'^\s*\|?\s*-+',lines[i+1]):
        headers=[x.strip() for x in line.strip().strip('|').split('|')]
        i+=2; rows=[]
        while i<len(lines) and '|' in lines[i] and lines[i].strip():
            rows.append([x.strip() for x in lines[i].strip().strip('|').split('|')]); i+=1
        cards=[]
        if len(headers)==3 and all(len(row)>=3 for row in rows):
            phases={}
            for n,row in enumerate(rows,1):
                if n in phases:
                    cards.append('<p style="margin:26px 0 10px;padding:7px 10px;border-left:3px solid #287A51;color:#287A51;font-size:14px;font-weight:bold;letter-spacing:1px;">'+phases[n]+'</p>')
                cards.append('<section style="margin:12px 0;padding:15px 16px;background:#F2F7F3;border:1px solid #D8E5DD;border-radius:4px;"><p style="margin:0 0 8px;font-size:16px;color:#17633F;font-weight:bold;"><span style="display:inline-block;margin-right:8px;color:#7A9A8A;font-size:12px;letter-spacing:1px;">'+str(n).zfill(2)+'</span>'+inline(row[0])+'</p><p style="margin:6px 0;line-height:1.6;font-size:15px;color:#333333;">'+inline(row[1])+'</p><p style="margin:8px 0 0;line-height:1.6;font-size:14px;color:#60746A;">'+inline(headers[2])+'：'+inline(row[2])+'</p></section>')
        else:
            for row in rows:
                if len(row)>=2:
                    cards.append('<section style="margin:12px 0;padding:13px 15px;background:#FAFAFA;border:1px solid #D8E5DD;border-left:3px solid #9FC5B0;border-radius:3px;"><p style="margin:0 0 5px;font-size:15px;color:#17633F;font-weight:bold;">'+inline(row[0])+'</p><p style="margin:0;line-height:1.428;font-size:14px;color:#526B5D;">'+inline(row[1])+'</p></section>')
        out.append(''.join(cards)); continue
    if line=='---':
        out.append('<hr style="border:none;border-top:1px solid #C7DDCF;margin:36px 0;">'); i+=1; continue
    # paragraph collect consecutive plain lines
    para=[line]; i+=1
    while i<len(lines) and lines[i].strip() and not re.match(r'^(#|>|[-*] |\d+\. )',lines[i]) and not (i+1<len(lines) and '|' in lines[i] and re.match(r'^\s*\|?\s*-+',lines[i+1])):
        para.append(lines[i]); i+=1
    txt=''.join(para)
    out.append('<p style="margin:18px 0;line-height:1.6;color:#333333;letter-spacing:0.5px;text-align:justify;">'+inline(txt)+'</p>')

body=''.join(out)
intro='<section style="margin:24px 0 30px;padding:18px 16px;background:#F2F7F3;border-top:2px solid #17633F;"><p style="margin:0 0 10px;font-size:13px;color:#17633F;font-weight:bold;letter-spacing:2px;">本篇导读</p><p style="margin:0;font-size:15px;line-height:1.6;color:#526B5D;">以手机小游戏为例，说明产品分工、执行环境、项目组织、协作控制和验收边界。</p></section>'
pos=body.index('</p>')+4
body=body[:pos]+intro+body[pos:]

# Style source note section distinct
body=body.replace('<h2 style="font-size:18px;font-weight:bold;color:#17633F;margin:44px 0 18px;display:block;line-height:1.425;border-bottom:1px solid #C7DDCF;padding-bottom:10px;letter-spacing:0.5px;">资料说明</h2>', '<section style="margin:38px 0 18px;padding:18px 16px;background:#FAFAFA;border-top:2px solid #17633F;"><h2 style="font-size:17px;font-weight:bold;color:#17633F;margin:0 0 14px;line-height:1.42;letter-spacing:0.5px;">资料说明</h2>')
# close source card before final body end: easiest locate last source paragraph and append section close at end of body (sources are end)
body += '</section><p style="margin:32px 0 10px;text-align:center;color:#17633F;font-size:12px;letter-spacing:2px;">旁观机器 · MACHINE OBSERVER</p>'
html_doc='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>用 Codex 完成长线工作：产品、环境与协作方式</title></head><body style="margin:0;background:#ffffff;padding:18px 0 30px;"><section style="font-size:16px;color:#333333;line-height:1.6;letter-spacing:0.5px;font-family:-apple-system,BlinkMacSystemFont,\'PingFang SC\',\'Hiragino Sans GB\',\'Microsoft YaHei\',sans-serif;word-break:break-word;background:#ffffff;padding:0 12px;box-sizing:border-box;max-width:640px;margin:0 auto;">'+body+'</section></body></html>'
Path('articles/2026-10-codex-guide/part-1/article-v6.html').write_text(html_doc)
