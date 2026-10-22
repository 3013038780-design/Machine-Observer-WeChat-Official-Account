"""Editorial layout of approved v12 text, with original mechanism illustrations."""
from pathlib import Path
import base64, html, json, re
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
T=json.loads((ROOT/'assets/theme.json').read_text())
SOURCE=HERE/'article-v12.md'
ASSETS=HERE/'assets/illustrations-v1'

def inline(text):
 text=html.escape(html.unescape(text),quote=True)
 text=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',lambda m:'<a href="'+m[2]+'" style="color:#60816D;font-size:13px;text-decoration:none;border-bottom:1px solid #C7DDCF;">'+m[1]+'</a>',text)
 return re.sub(r'\*\*(.+?)\*\*',lambda m:'<strong style="'+T['strong']+'">'+m[1]+'</strong>',text)

def illustration(name,caption):
 data=base64.b64encode((ASSETS/(name+'.png')).read_bytes()).decode()
 return '<section style="margin:28px 0 30px;"><img src="data:image/png;base64,'+data+'" alt="'+html.escape(caption)+'" style="display:block;width:100%;height:auto;border-radius:8px;margin:0;"><p style="margin:10px 6px 0;font-size:12px;line-height:1.65;letter-spacing:0.3px;text-align:left;color:#7A8C80;">'+html.escape(caption)+'</p></section>'

blocks=SOURCE.read_text().strip().split('\n\n')
parts=['<section style="'+T['container']+'max-width:640px;margin:0 auto;box-sizing:border-box;">']
num=0
for i,block in enumerate(blocks):
 if block.startswith('# '):
  parts+=['<section style="margin:32px 0 32px;padding:0 4px 26px;border-bottom:1px solid #C7DDCF;"><p style="margin:0 0 18px;font-size:12px;line-height:1.5;letter-spacing:2px;text-align:center;color:#718C7B;">和 Codex 一起工作 · 04</p><h1 style="'+T['h1']+'margin:0 0 22px;">'+inline(block[2:])+'</h1><p style="margin:0;text-align:center;color:#17633F;font-size:13px;line-height:1;letter-spacing:5px;">— · —</p></section>']
 elif block.startswith('## '):
  num+=1
  label=re.sub(r'^[一二三]、','',block[3:])
  parts.append('<section style="margin:44px 0 22px;padding:18px 16px 16px;background:#F2F7F3;border-top:2px solid #17633F;"><p style="margin:0 0 9px;font-size:28px;line-height:1;color:#87A891;font-weight:500;letter-spacing:1px;">'+f'{num:02d}'+'</p><h2 style="font-size:18px;font-weight:bold;line-height:1.55;letter-spacing:0.5px;color:#17633F;margin:0;">'+inline(label)+'</h2></section>')
 elif block.startswith('### '):
  parts.append('<h3 style="'+T['h3']+'border-left:3px solid #287A51;padding-left:10px;">'+inline(block[4:])+'</h3>')
 elif block.startswith('> '):
  parts.append('<blockquote style="margin:24px 0;padding:17px 18px;background:#FAFAFA;border-left:3px solid #91AC99;"><p style="'+T['blockquote_p']+'font-size:16px;color:#496255;">'+inline(block[2:])+'</p></blockquote>')
 elif block=='**一句请求，是这一连串判断和行动的起点。**':
  parts.append('<section style="margin:26px 0;padding:17px 18px;background:#F2F7F3;border-left:3px solid #17633F;"><p style="'+T['p']+'margin:0;">'+inline(block)+'</p></section>')
 elif i==len(blocks)-1:
  parts.append('<section style="margin:30px 0 36px;padding:20px 18px;border-top:1px solid #C7DDCF;border-bottom:1px solid #C7DDCF;background:#FAFAFA;"><p style="'+T['p']+'margin:0;color:#28553C;">'+inline(block)+'</p></section>')
 else:
  parts.append('<p style="'+T['p']+'">'+inline(block)+'</p>')
 if block=='上下文，就是这些来龙去脉。':
  parts.append(illustration('01-context','概念示意｜用途、资料与限制，共同影响它怎样理解任务。'))
 if block.startswith('**它能够自己推进，'):
  parts.append(illustration('02-action-loop','流程示意｜模型提出操作，程序执行，返回结果再进入下一轮判断。'))
 if block.startswith('它当然运行在程序里，'):
  parts.append(illustration('03-blackbox','概念示意｜能核查外部动作，不等于已完整读懂内部判断。'))
parts.append('</section>')
body='\n'.join(parts)
(HERE/'article-v13-body.html').write_text(body)
title=blocks[0][2:]
(HERE/'article-v13.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title></head><body style="margin:0;padding:0 0 24px;background:#ffffff;">'+body+'</body></html>')
print('Generated article-v13.html and article-v13-body.html')
