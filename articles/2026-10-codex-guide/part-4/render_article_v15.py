"""Render user-supplied v15 text with established title cards and restrained variations."""
from pathlib import Path
import base64, html, json, re
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
T=json.loads((ROOT/'assets/theme.json').read_text())
blocks=(HERE/'article-v15.md').read_text().strip().split('\n\n')
series=blocks[0]
title=blocks[1][3:]
def inline(text):
 text=html.escape(text,quote=True)
 text=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',lambda m:'<a href="'+m[2]+'" style="'+T['a']+'">'+m[1]+'</a>',text)
 return re.sub(r'\*\*(.+?)\*\*',lambda m:'<strong style="'+T['strong']+'">'+m[1]+'</strong>',text)
def para(text,style=''):
 return '<p style="'+T['p']+style+'">'+inline(text)+'</p>'
def subheading(text,style=''):
 return '<h3 style="'+T['h3']+style+'">'+inline(text)+'</h3>'
def heading_card(number,label):
 return '<section style="margin:34px 0 17px;padding:12px 14px;background:#F2F7F3;border:1px solid #C7DDCF;border-radius:4px;"><div style="display:table;width:100%;border-collapse:collapse;"><div style="display:table-cell;width:43px;vertical-align:middle;color:#17633F;font-size:28px;font-weight:400;line-height:1.2;">'+number+'</div><div style="display:table-cell;vertical-align:middle;padding-left:12px;border-left:1px solid #B9D2C2;"><h2 style="margin:0;color:#17633F;font-size:18px;font-weight:700;line-height:1.5;letter-spacing:0.5px;">'+inline(label)+'</h2></div></div></section>'
parts=['<section style="'+T['container']+'max-width:640px;margin:0 auto;box-sizing:border-box;">']
brand=ROOT/'assets/brand/2026-09-12-header-v2/03-retro-terminal.png'
data=base64.b64encode(brand.read_bytes()).decode()
parts.append('<img src="data:image/png;base64,'+data+'" alt="旁观机器：复古电脑公众号首图" style="display:block;width:100%;height:auto;margin:0 0 22px;border-radius:3px;">')
parts.append('<h1 style="font-size:22px;font-weight:700;color:#17633F;text-align:center;margin:26px 0 14px;line-height:1.45;letter-spacing:0.5px;">'+inline(title)+'</h1>')
parts.append('<p style="text-align:center;color:#7A9A8A;font-size:13px;letter-spacing:1px;margin:0 0 25px;">'+inline(series)+'</p>')
i=2
while i<len(blocks):
 b=blocks[i]
 if b=='---':
  i+=1;continue
 if b=='旁观机器 · MACHINE OBSERVER':
  parts.append('<p style="margin:28px 0 10px;text-align:center;color:#17633F;font-size:12px;letter-spacing:2px;">'+b+'</p>');i+=1;continue
 m=re.match(r'^## (\d{2}) (.+)$',b)
 if m:
  parts.append(heading_card(m[1],m[2]));i+=1;continue
 if b.startswith('### 第一层') or b.startswith('### 第二层') or b.startswith('### 第三层'):
  parts.append('<section style="margin:22px 0;padding:15px 16px;background:#FAFAFA;border:1px solid #DCE6DF;border-radius:4px;">'+subheading(b[4:],'margin:0 0 12px;')+para(blocks[i+1],'margin:0 0 12px;')+para(blocks[i+2],'margin:0;')+'</section>');i+=3;continue
 if b.startswith('### 任务'):
  parts.append('<section style="margin:26px 0;padding:0 0 0 14px;border-left:2px solid #C7DDCF;">'+subheading(b[4:],'margin:0 0 12px;')+para(blocks[i+1],'margin:0 0 12px;')+para(blocks[i+2],'margin:0;')+'</section>');i+=3;continue
 if b.startswith('### '):
  parts.append(subheading(b[4:]));i+=1;continue
 if b.startswith('> '):
  parts.append('<blockquote style="'+T['blockquote']+'"><p style="'+T['blockquote_p']+'font-size:16px;">'+inline(b[2:])+'</p></blockquote>');i+=1;continue
 if b.startswith('**第一棒'):
  steps=[]
  while i<len(blocks) and re.match(r'^\*\*第[一二三四]棒',blocks[i]):
   steps.append(para(blocks[i],'margin:0 0 16px;' if len(steps)<3 else 'margin:0;'));i+=1
  parts.append('<section style="margin:24px 0;padding:2px 0 2px 16px;border-left:3px solid #91B09B;">'+''.join(steps)+'</section>');continue
 if b.startswith('- '):
  items=[line[2:] for line in b.splitlines()]
  parts.append('<section style="margin:22px 0;padding:4px 15px;background:#FAFAFA;border:1px solid #E0E8E2;border-radius:4px;"><ul style="margin:12px 0;padding-left:19px;">'+''.join('<li style="'+T['li']+'">'+inline(x)+'</li>' for x in items)+'</ul></section>');i+=1;continue
 if re.match(r'^1\. ',b):
  items=[re.sub(r'^\d+\. ','',line) for line in b.splitlines()]
  parts.append('<ol style="'+T['ol']+'">'+''.join('<li style="'+T['li']+'">'+inline(x)+'</li>' for x in items)+'</ol>');i+=1;continue
 if b.startswith('**一句请求，') or b.startswith('**理解 AI 的工作方式，'):
  parts.append('<section style="margin:24px 0;padding:14px 16px;background:#F2F7F3;border-left:3px solid #17633F;">'+para(b,'margin:0;')+'</section>');i+=1;continue
 if b.startswith('相关资料：'):
  parts.append(para(b,'font-size:13px;color:#718078;text-align:left;'));i+=1;continue
 parts.append(para(b));i+=1
parts.append('</section>')
body='\n'.join(parts)
(HERE/'article-v15-body.html').write_text(body)
(HERE/'article-v15.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title></head><body style="margin:0;background:#fff;padding:18px 0 30px;">'+body+'</body></html>')
print('Generated article-v15.html and article-v15-body.html')
