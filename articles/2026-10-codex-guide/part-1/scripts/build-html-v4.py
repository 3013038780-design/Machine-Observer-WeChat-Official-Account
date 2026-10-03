from pathlib import Path
import html,re

src=Path('articles/2026-10-codex-guide/part-1/article-v4.md').read_text()
lines=src.splitlines()
out=[]

def inline(s):
    s=html.escape(s, quote=False)
    # links after escape
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" style="color:#17633F;text-decoration:none;border-bottom:1px solid #C7DDCF;">\1</a>', s)
    s=re.sub(r'\*\*([^*]+)\*\*', r'<strong style="font-weight:bold;color:#17633F;">\1</strong>', s)
    s=re.sub(r'`([^`]+)`', r'<code style="background:#f6f6f6;color:#17633F;padding:2px 5px;border-radius:3px;font-size:14px;font-family:SFMono-Regular,Consolas,monospace;">\1</code>', s)
    return s

i=0
while i<len(lines):
    line=lines[i]
    if not line.strip() or line.startswith('状态：'): i+=1; continue
    if line.startswith('# '):
        out.append('<h1 style="font-size:22px;font-weight:bold;color:#17633F;text-align:center;margin:36px 0 18px;line-height:1.5;letter-spacing:0.5px;">'+inline(line[2:])+'</h1>')
        out.append('<p style="text-align:center;color:#7A9A8A;font-size:13px;letter-spacing:2px;margin:0 0 30px;">和 Codex 一起工作 · 第一篇</p>')
        i+=1; continue
    if line.startswith('## '):
        out.append('<h2 style="font-size:18px;font-weight:bold;color:#17633F;margin:44px 0 18px;display:block;line-height:1.55;border-bottom:1px solid #C7DDCF;padding-bottom:10px;letter-spacing:0.5px;">'+inline(line[3:])+'</h2>')
        i+=1; continue
    if line.startswith('### '):
        out.append('<h3 style="font-size:17px;font-weight:bold;color:#287A51;margin:28px 0 14px;line-height:1.5;letter-spacing:0.5px;">'+inline(line[4:])+'</h3>')
        i+=1; continue
    if line.startswith('> '):
        qs=[]
        while i<len(lines) and (lines[i].startswith('> ') or not lines[i].strip()):
            if lines[i].startswith('> '): qs.append('<p style="margin:6px 0;line-height:1.75;color:#5D7569;letter-spacing:0.5px;">'+inline(lines[i][2:])+'</p>')
            i+=1
        out.append('<blockquote style="margin:24px 0;padding:14px 18px;background:#F2F7F3;border-left:3px solid #17633F;color:#5D7569;font-size:15px;border-radius:2px;">'+''.join(qs)+'</blockquote>')
        continue
    if re.match(r'^[-*] ',line):
        items=[]
        while i<len(lines) and re.match(r'^[-*] ',lines[i]):
            items.append('<li style="margin:10px 0;line-height:1.75;letter-spacing:0.5px;">'+inline(lines[i][2:])+'</li>'); i+=1
        out.append('<ul style="margin:18px 0;padding-left:24px;">'+''.join(items)+'</ul>'); continue
    if re.match(r'^\d+\. ',line):
        items=[]
        while i<len(lines) and re.match(r'^\d+\. ',lines[i]):
            text=re.sub(r'^\d+\. ','',lines[i]); items.append('<li style="margin:10px 0;line-height:1.75;letter-spacing:0.5px;">'+inline(text)+'</li>'); i+=1
        out.append('<ol style="margin:18px 0;padding-left:24px;">'+''.join(items)+'</ol>'); continue
    # table
    if i+1<len(lines) and '|' in line and re.match(r'^\s*\|?\s*-+',lines[i+1]):
        headers=[x.strip() for x in line.strip().strip('|').split('|')]
        i+=2; rows=[]
        while i<len(lines) and '|' in lines[i] and lines[i].strip():
            rows.append([x.strip() for x in lines[i].strip().strip('|').split('|')]); i+=1
        cards=[]
        for n,row in enumerate(rows,1):
            cards.append('<section style="margin:14px 0;padding:16px;background:#F2F7F3;border:1px solid #D8E5DD;border-radius:3px;"><p style="margin:0 0 10px;font-size:16px;color:#17633F;font-weight:bold;">'+str(n).zfill(2)+' · '+inline(row[0])+'</p><p style="margin:6px 0;line-height:1.75;font-size:15px;color:#333333;">'+inline(row[1])+'</p><p style="margin:8px 0 0;line-height:1.75;font-size:14px;color:#60746A;">留下的结果：'+inline(row[2])+'</p></section>')
        out.append(''.join(cards)); continue
    if line=='---':
        out.append('<hr style="border:none;border-top:1px solid #C7DDCF;margin:36px 0;">'); i+=1; continue
    # paragraph collect consecutive plain lines
    para=[line]; i+=1
    while i<len(lines) and lines[i].strip() and not re.match(r'^(#|>|[-*] |\d+\. )',lines[i]) and not (i+1<len(lines) and '|' in lines[i] and re.match(r'^\s*\|?\s*-+',lines[i+1])):
        para.append(lines[i]); i+=1
    txt=''.join(para)
    out.append('<p style="margin:18px 0;line-height:1.75;color:#333333;letter-spacing:0.5px;text-align:justify;">'+inline(txt)+'</p>')

body=''.join(out)
intro='<section style="margin:24px 0 30px;padding:18px 16px;background:#F2F7F3;border-top:2px solid #17633F;"><p style="margin:0 0 10px;font-size:13px;color:#17633F;font-weight:bold;letter-spacing:2px;">本篇导读</p><p style="margin:0;font-size:15px;line-height:1.75;color:#526B5D;">从一个手机小游戏的想法出发，看懂产品入口、工作空间、执行环境、录制回放和可复用能力，以及怎样判断一项工作真正完成。</p></section>'
pos=body.index('</p>')+4
body=body[:pos]+intro+body[pos:]

# Style source note section distinct
body=body.replace('<h2 style="font-size:18px;font-weight:bold;color:#17633F;margin:44px 0 18px;display:block;line-height:1.55;border-bottom:1px solid #C7DDCF;padding-bottom:10px;letter-spacing:0.5px;">资料说明</h2>', '<section style="margin:38px 0 18px;padding:18px 16px;background:#FAFAFA;border-top:2px solid #17633F;"><h2 style="font-size:17px;font-weight:bold;color:#17633F;margin:0 0 14px;line-height:1.5;letter-spacing:0.5px;">资料说明</h2>')
# close source card before final body end: easiest locate last source paragraph and append section close at end of body (sources are end)
body += '</section><p style="margin:32px 0 10px;text-align:center;color:#17633F;font-size:12px;letter-spacing:2px;">旁观机器 · MACHINE OBSERVER</p>'
html_doc='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Codex 到底是什么：从聊天到交付的完整工作地图</title></head><body style="margin:0;background:#ffffff;padding:18px 0 30px;"><section style="font-size:16px;color:#333333;line-height:1.75;letter-spacing:0.5px;font-family:-apple-system,BlinkMacSystemFont,\'PingFang SC\',\'Hiragino Sans GB\',\'Microsoft YaHei\',sans-serif;word-break:break-word;background:#ffffff;padding:0 12px;box-sizing:border-box;max-width:640px;margin:0 auto;">'+body+'</section></body></html>'
Path('articles/2026-10-codex-guide/part-1/article-v4.html').write_text(html_doc)
