from pathlib import Path
import importlib.util,json,re,html
P=Path(__file__).resolve().parent;A=P.parent;R=A.parent.parent
sp=importlib.util.spec_from_file_location('render',R/'scripts/render.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
t=json.loads((R/'assets/theme.json').read_text());t['h2']='font-size:18px;font-weight:700;color:#17633F;margin:40px 0 18px;line-height:1.55;letter-spacing:0.5px;';t['a']='color:#287A51;text-decoration:none;overflow-wrap:anywhere;'
s=(A/'article-v2.md').read_text();s=re.sub(r'^候选标题｜.*\n','',s,flags=re.M)
# Source addresses remain visible and become clickable.
s=re.sub(r'^(https?://\S+)[ \t]*$',lambda q:'['+q[1]+']('+q[1]+')',s,flags=re.M)
main,sources=s.split('## 来源',1)
b=m.render(main,t)
st=dict(t);st['p']='margin:14px 0;font-size:13px;line-height:1.7;color:#557366;text-align:left;overflow-wrap:anywhere;letter-spacing:0;';b+=m.render('## 来源'+sources,st)
b=re.sub(r'<p[^>]*><strong[^>]*>内容提要：(.*?)</strong></p>',r'<section style="background:#F2F7F3;color:#365B46;padding:14px 16px;margin:24px 0;font-size:15px;line-height:1.8;letter-spacing:0.5px;"><strong style="color:#17633F;">内容提要</strong><br>\1</section>',b,flags=re.S)
b=re.sub(r'\[(\d+)\]',r'<sup style="font-size:11px;line-height:0;color:#557366;">[\1]</sup>',b)
# Renderer h2 wrapper is unnecessary; use valid standalone heading blocks.
b=re.sub(r'<p style="margin:0;">(<h2.*?</h2>)</p>',r'\1',b,flags=re.S)
article='<section id="article" style="'+t['container']+'max-width:680px;box-sizing:border-box;margin:0 auto;padding:20px 12px 40px;"><p style="font-size:12px;color:#557366;letter-spacing:2px;margin:8px 0 22px;">旁观机器</p>'+b+'</section>'
(A/'article-v2-body.html').write_text(article)
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>一文读懂汽车辅助驾驶｜旁观机器</title><style>*{box-sizing:border-box}body{margin:0;background:#eef2ef;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif}nav{max-width:680px;margin:16px auto;padding:0 12px;color:#557366;font-size:13px;line-height:1.7}button{font:inherit;color:#17633f;background:white;border:1px solid #c7ddcf;border-radius:5px;padding:7px 12px;margin:5px 6px 5px 0;cursor:pointer}main{max-width:440px;margin:18px auto 40px;background:white;box-shadow:0 6px 30px #173e2910}#status{display:block;min-height:23px}@media(max-width:480px){body{background:white}main{margin:0;box-shadow:none}nav{margin:10px auto}}@media print{nav{display:none}body{background:white}main{max-width:none;margin:0;box-shadow:none}}</style></head><body><nav>文字审读版 v2 · 绿色排版 · 复制后可粘贴至135<br><button id="mobile">手机宽度</button><button id="wide">宽屏阅读</button><button id="copy">复制排版正文</button><span id="status" aria-live="polite"></span></nav><main>'''+article+'''</main><script>const main=document.querySelector('main');document.querySelector('#mobile').onclick=()=>main.style.maxWidth='440px';document.querySelector('#wide').onclick=()=>main.style.maxWidth='720px';document.querySelector('#copy').onclick=async()=>{const a=document.querySelector('#article'),s=document.querySelector('#status');try{await navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([a.outerHTML],{type:'text/html'}),'text/plain':new Blob([a.innerText],{type:'text/plain'})})]);s.textContent='已复制排版正文，可粘贴到135。'}catch(e){const r=document.createRange();r.selectNodeContents(a);const sel=getSelection();sel.removeAllRanges();sel.addRange(r);s.textContent='正文已选中，请按 ⌘C（Windows：Ctrl+C）复制。'}};</script></body></html>'''
(A/'article-v2.html').write_text(page);print('Built preview and inline body')
