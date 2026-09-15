from pathlib import Path
import importlib.util,json,re,zipfile
P=Path(__file__).resolve().parent;A=P.parent.parent;R=A.parent.parent
spec=importlib.util.spec_from_file_location('render',R/'scripts/render.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
t=json.loads((R/'assets/theme.json').read_text())
for key,size in [('h2',20),('h3',18)]:t[key]=f'font-size:{size}px;font-weight:700;color:#17633F;margin:34px 0 16px;line-height:1.6;letter-spacing:0.5px;'
t['img']='display:block;width:100%;max-width:100%;height:auto;margin:22px auto 8px;'
t['a']='color:#287A51;text-decoration:none;overflow-wrap:anywhere;'
s=(A/'article-v4.md').read_text().split('## 正文\n',1)[1]
h=m.render(s,t)
h=re.sub(r'<p[^>]*><strong[^>]*>内容提要：(.*?)</strong></p>',r'<section style="background:#F2F7F3;padding:14px 16px;margin:22px 0;font-size:15px;line-height:1.8;color:#365B46;"><strong>内容提要</strong><br>\1</section>',h,flags=re.S)
h=re.sub(r'\[(\d+)\]',lambda x:f'<sup style="font-size:11px;color:#557366">[{x[1]}]</sup>',h)
a=f'<section id="article" style="{t["container"]}max-width:640px;margin:auto;padding:18px 14px 36px;box-sizing:border-box;"><p style="font-size:13px;color:#557366;letter-spacing:2px">旁观机器</p><h1 style="{t["h1"]}">从汽车到机器人：<br>英伟达的产品用在哪里？</h1>{h}</section>'
(A/'article-v4-body.html').write_text(a)
old=(A/'article-v3.html').read_text();head=old.split('<main>')[0];tail=old.split('</main>',1)[1]
head=head.replace('下载6张图片','下载本版图片').replace('guide-v1-images.zip','report-v4-images.zip').replace('文字与图片综合审阅版','v4 · 实物、软件与任务链修订稿')
(A/'article-v4.html').write_text(head+'<main>'+a+'</main>'+tail)
imgs=[A/x for x in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s)]
with zipfile.ZipFile(A/'report-v4-images.zip','w',zipfile.ZIP_DEFLATED) as z:
 for i in imgs:z.write(i,i.name)
 z.write(P/'manifest.json','manifest.json')
with zipfile.ZipFile(A/'article-v4-package.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in [A/'article-v4.html',A/'article-v4-body.html',A/'article-v4.md',A/'report-v4-images.zip',*imgs]:z.write(f,f.relative_to(A))
print('Generated HTML and packages;',len(imgs),'images;',len(s),'characters with sources')
