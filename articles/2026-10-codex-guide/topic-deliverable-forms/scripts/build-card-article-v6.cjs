/* Deterministic typesetting: Markdown -> inline HTML + local table PNGs. */
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const crypto = require('node:crypto');
const args = process.argv.slice(2);
const moduleIndex = args.indexOf('--modules');
const modules = moduleIndex >= 0 ? args[moduleIndex + 1] : null;
const dependency = name => require(modules ? path.join(modules, name) : name);
const { chromium } = dependency('playwright');
const sharp = dependency('sharp');
const root = path.resolve(__dirname, '..');
const repo = path.resolve(root, '../../..');
const sourcePath = path.join(root, 'article-v6.md');
const source = fs.readFileSync(sourcePath, 'utf8');
const theme = JSON.parse(fs.readFileSync(path.join(repo, 'assets/theme.json'), 'utf8'));
const outDir = path.join(root, 'assets/cards-v6');
const qaDir = path.join(root, 'qa/html-v6');
fs.mkdirSync(path.join(outDir, 'source'), { recursive: true });
fs.mkdirSync(qaDir, { recursive: true });
const colors = { accent: theme.accent, green: '#287A51', pale: '#F2F7F3', border: '#C7DDCF' };
const settings = { width: 360, scale: 3, font: 16, lineHeight: 1.45, maxRows: 5, maxHeight: 880, columns: [23, 42, 35] };
const esc = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const plain = value => value.replace(/\*\*([^*]+)\*\*/g, '$1').replace(/`([^`]+)`/g, '$1');
function inline(value) {
  let s = esc(value);
  s = s.replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g, '<a href="$2" style="' + theme.a + '">$1</a>');
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong style="' + theme.strong + '">$1</strong>');
  s = s.replace(/`([^`]+)`/g, '<code style="' + theme.code_inline + '">$1</code>');
  return s;
}
function parse(markdown) {
  const lines = markdown.split(/\r?\n/);
  const blocks = [];
  let heading = '';
  let group = 0;
  for (let i = 0; i < lines.length;) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    if (line.startsWith('标题候选｜')) { i++; continue; }
    if (line.startsWith('# ')) { blocks.push({ type: 'h1', text: line.slice(2) }); i++; continue; }
    if (line.startsWith('### ')) { blocks.push({ type: 'h3', text: line.slice(4) }); i++; continue; }
    if (line.startsWith('## ')) {
      heading = line.slice(3);
      if (/^[一二三四五六七八九十]+、/.test(heading)) group++;
      blocks.push({ type: 'h2', text: heading, group });
      i++; continue;
    }
    if (line.startsWith('|')) {
      const headers = line.split('|').slice(1, -1).map(c => c.trim());
      i += 2;
      const rows = [];
      while (i < lines.length && lines[i].startsWith('|')) {
        const row = lines[i].split('|').slice(1, -1).map(c => c.trim());
        if (row.length !== 3 || row.some(c => !c)) throw new Error('Bad table row: ' + lines[i]);
        rows.push(row); i++;
      }
      blocks.push({ type: 'table', group, heading, headers, rows }); continue;
    }
    if (line.startsWith('> ')) {
      const text = [];
      while (i < lines.length && lines[i].startsWith('> ')) text.push(lines[i++].slice(2));
      blocks.push({ type: 'quote', text: text.join('') }); continue;
    }
    const text = [line]; i++;
    while (i < lines.length && lines[i].trim() && !/^(#|\||> )/.test(lines[i])) text.push(lines[i++]);
    blocks.push({ type: 'p', text: text.join('') });
  }
  return blocks;
}
const raw=parse(source),data=JSON.parse(fs.readFileSync(path.join(outDir,'cards.json'))),blocks=[];
const labels=['能做什么 · 在哪里用','交付内容','这样跟 AI 说'];let cardIndex=0;
for(let i=0;i<raw.length;i++){
 const b=raw[i];
 if(b.type==='h3'){
  const r=data.cards[cardIndex++];if(!r||b.text!==`${String(r.number).padStart(2,'0')} ${r.name}`)throw Error('Card heading mismatch');
  for(let n=0;n<3;n++){const field=raw[++i],prefix=`**${labels[n]}：** `;if(field?.type!=='p'||!field.text.startsWith(prefix)||field.text.slice(prefix.length)!==[r.usage,r.delivery,r.prompt][n])throw Error('Card field mismatch '+r.number)}
  blocks.push({type:'card',card:r});
 }else{if(b.type==='table')throw Error('Unexpected table');blocks.push(b)}
}
if(cardIndex!==58||data.groupCount!==10)throw Error('Unexpected card coverage');
function field(label,text){return `<p style="margin:10px 0 4px;font-size:13px;line-height:1.5;letter-spacing:0;color:#587767;font-weight:600;">${label}</p><p style="margin:0;font-size:16px;line-height:1.65;letter-spacing:0;color:#333;text-align:left;overflow-wrap:anywhere;">${esc(text)}</p>`}
function card(r){return `<section data-card="${r.number}" data-group="${r.group}" style="box-sizing:border-box;margin:0 0 14px;padding:12px 12px 13px;background:#fff;border:1px solid #C7DDCF;border-radius:9px;overflow-wrap:anywhere;"><p style="margin:0 0 8px;font-size:17px;line-height:1.5;font-weight:600;letter-spacing:0;color:#17633F;"><span style="font-size:13px;font-weight:500;color:#739383;">${String(r.number).padStart(2,'0')}</span>　${esc(r.name)}</p><section style="border-top:1px solid #E2EBE5;padding-top:1px;">${field(labels[0],r.usage)}${field(labels[1],r.delivery)}<section style="margin:11px 0 0;padding:9px 10px;background:#F2F7F3;border-radius:4px;"><p style="margin:0 0 4px;font-size:13px;line-height:1.5;letter-spacing:0;color:#587767;font-weight:600;">${labels[2]}</p><p style="margin:0;font-size:16px;line-height:1.65;letter-spacing:0;color:#244C36;text-align:left;overflow-wrap:anywhere;">${esc(r.prompt)}</p></section></section></section>`}
const brandPath=path.join(repo,'assets/brand/2026-09-12-header-v2/03-retro-terminal.png');
const pngSource=(file,embedded)=>embedded?'data:image/png;base64,'+fs.readFileSync(path.join(outDir,file)).toString('base64'):`assets/cards-v6/${file}`;
function article(mode='native',embedded=true){
 const brand=embedded?'data:image/png;base64,'+fs.readFileSync(brandPath).toString('base64'):'assets/header-retro-terminal.png';
 const parts=[`<img src="${brand}" alt="旁观机器品牌首图：复古电脑" style="display:block;width:100%;max-width:100%;height:auto;margin:0 0 18px;border-radius:3px;">`,'<p style="margin:0 0 8px;color:#7A9A8A;font-size:13px;line-height:1.5;text-align:center;letter-spacing:1px;">和 Codex 一起工作 · 第五篇</p>'];
 for(const b of blocks){
  if(b.type==='h1')parts.push(`<h1 style="${theme.h1.replace('margin:36px 0 30px;','margin:20px 0 22px;')}">${inline(b.text)}</h1>`);
  if(b.type==='h2')parts.push(`<h2 style="${theme.h2.replace('margin:44px 0 18px;','margin:32px 0 16px;')}text-wrap:balance;">${inline(b.text)}</h2>`);
  if(b.type==='p'){
   if(b.text==='旁观机器 · MACHINE OBSERVER')continue;
   if(plain(b.text).startsWith('制作与运行条件：'))parts.push(`<section style="margin:16px 0 20px;padding:10px 12px;background:#F2F7F3;border-left:2px solid #287A51;"><p style="margin:0;font-size:16px;line-height:1.75;letter-spacing:0.5px;color:#43594B;text-align:justify;">${inline(plain(b.text)).replace('制作与运行条件：','<strong style="color:#17633F;font-weight:600;">制作与运行条件：</strong>')}</p></section>`);
   else parts.push(`<p style="${theme.p}">${inline(b.text)}</p>`);
  }
  if(b.type==='quote')parts.push(`<blockquote style="margin:18px 0;padding:10px 12px;background:#F2F7F3;border-left:3px solid #17633F;font-size:16px;"><p style="margin:0;font-size:16px;line-height:1.75;letter-spacing:0.5px;color:#43594B;text-align:justify;">${inline(b.text)}</p></blockquote>`);
  if(b.type==='card'){
   if(mode==='native')parts.push(card(b.card));
   else{const file=`${String(b.card.number).padStart(2,'0')}-card.png`;parts.push(`<img src="${pngSource(file,embedded)}" alt="${b.card.number} ${esc(b.card.name)}：纯文字交付物卡片" style="display:block;width:100%;max-width:100%;height:auto;margin:0 0 14px;border:0;">`)}
  }
 }
 parts.push('<p style="margin:28px 0 12px;text-align:center;font-size:12px;line-height:1.6;color:#17633F;letter-spacing:1.5px;">旁观机器 · MACHINE OBSERVER</p>');
 return `<section style="${theme.container}box-sizing:border-box;max-width:384px;margin:0 auto;">${parts.join('\n')}</section>`;
}
const wrap=body=>`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 交付物全景图鉴 · 无图卡片版</title></head><body style="margin:0;padding:14px 0 24px;background:#fff;">${body}</body></html>`;
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
  const c=await browser.newContext({viewport:{width:360,height:1000},deviceScaleFactor:3}),p=await c.newPage();
  fs.mkdirSync(path.join(outDir,'source'),{recursive:true});const images=[];
  for(const r of data.cards){
   const html=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>*{box-sizing:border-box}html,body{width:360px;margin:0;padding:0;background:white}body{font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;-webkit-font-smoothing:antialiased}</style><body>${card(r)}</body></html>`;
   const name=`${String(r.number).padStart(2,'0')}-card`;fs.writeFileSync(path.join(outDir,'source',name+'.html'),html);
   await p.setContent(html);await p.evaluate(()=>document.fonts.ready);
   const check=await p.evaluate(()=>({width:document.body.scrollWidth,height:document.querySelector('[data-card]').getBoundingClientRect().height,imageCount:document.images.length,overflow:[...document.querySelectorAll('p')].filter(el=>el.scrollWidth>el.clientWidth+1||el.scrollHeight>el.clientHeight+1).map(el=>el.textContent)}));
   if(check.width!==360||check.imageCount||check.overflow.length)throw Error(JSON.stringify(check));
   const paragraphs=await p.locator('[data-card] p').allTextContents();for(const text of[r.usage,r.delivery,r.prompt])if(!paragraphs.includes(text))throw Error('Lost card text '+r.number);
   await p.locator('[data-card]').screenshot({path:path.join(outDir,name+'.png')});const info=await sharp(path.join(outDir,name+'.png')).metadata();
   images.push({number:r.number,group:r.group,name:r.name,file:name+'.png',width:info.width,height:info.height,logicalHeight:check.height});
  }
  await c.close();
  const manifest={date:'2026-10-25',source:'article-v6.md',sourceSha256:crypto.createHash('sha256').update(source).digest('hex'),cards:58,groups:10,font:16,lineHeight:1.65,logicalWidth:360,scale:3,noPreviewImages:true,images};
  fs.writeFileSync(path.join(outDir,'manifest.json'),JSON.stringify(manifest,null,2));
  for(const[filename,mode,embedded]of[['article-v6-cards.html','native',true],['article-v6-cards-body.html','native',true],['article-v6-card-images.html','images',true],['article-v6-card-images-body.html','images',true],['article-v6-card-images-linked.html','images',false]]){const body=article(mode,embedded);fs.writeFileSync(path.join(root,filename),filename.includes('-body.')?body:wrap(body))}
  const qa=await browser.newContext({viewport:{width:390,height:1000},deviceScaleFactor:1}),view=await qa.newPage();const checks=[],prose={};
  const expectedLinks=[...source.matchAll(/\[[^\]]+\]\((https?:[^)]+)\)/g)].map(m=>m[1]);
  for(const mode of['cards','card-images']){
   await view.goto(pathToFileURL(path.join(root,`article-v6-${mode}.html`)).href);await view.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(im=>im.complete?Promise.resolve():new Promise(resolve=>{im.onload=resolve;im.onerror=resolve})))});
   for(const width of[375,390,760,1440]){
    await view.setViewportSize({width,height:1000});const check=await view.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,cardCount:document.querySelectorAll('[data-card]').length,images:document.images.length,broken:[...document.images].filter(im=>!im.complete||!im.naturalWidth).length,tables:document.querySelectorAll('table').length,headings:document.querySelectorAll('h2').length,conditions:[...document.querySelectorAll('p')].filter(el=>el.textContent.startsWith('制作与运行条件：')).length,links:[...document.querySelectorAll('a[href]')].map(el=>el.href),external:!!document.querySelector('style,script,link[rel=stylesheet]'),overflow:[...document.querySelectorAll('[data-card] p')].filter(el=>el.scrollWidth>el.clientWidth+1).map(el=>el.textContent),bodyFont:getComputedStyle(document.querySelector('section > p[style*="text-align:justify"]')).fontSize}));
    if(check.scrollWidth>width||check.broken||check.tables||check.headings!==11||check.conditions!==10||check.external||check.overflow.length||check.bodyFont!=='16px'||JSON.stringify(check.links)!==JSON.stringify(expectedLinks)||check.cardCount!==(mode==='cards'?58:0)||check.images!==(mode==='cards'?1:59))throw Error(JSON.stringify(check));
    checks.push({mode,...check});
   }
   if(mode==='cards')for(const r of data.cards){const el=view.locator(`[data-card="${r.number}"]`),texts=await el.locator('p').allTextContents();for(const text of[r.usage,r.delivery,r.prompt])if(!texts.includes(text))throw Error('Native card mismatch '+r.number)}
   prose[mode]=await view.evaluate(()=>{const x=document.body.cloneNode(true);x.querySelectorAll('[data-card],img').forEach(el=>el.remove());return x.textContent.replace(/\s+/g,' ').trim()});
   await view.setViewportSize({width:390,height:1000});await view.evaluate(()=>scrollTo(0,0));await view.screenshot({path:path.join(qaDir,`${mode}-top-390.png`)});
   for(const[name,n]of[['first',0],['agent',3],['design',6],['engineering',8],['last',9]]){await view.locator('h2').nth(n).evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));await view.screenshot({path:path.join(qaDir,`${mode}-${name}-390.png`)})}
   await view.setViewportSize({width:760,height:1000});await view.locator('h2').first().evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));await view.screenshot({path:path.join(qaDir,`${mode}-first-760.png`)});
  }
  if(prose.cards!==prose['card-images'])throw Error('Article prose differs');
  // Review every card through contact sheets; original PNGs remain full resolution.
  for(let i=0;i<images.length;i+=8){const slice=images.slice(i,i+8),thumbs=await Promise.all(slice.map(im=>sharp(path.join(outDir,im.file)).resize({width:240}).png().toBuffer())),meta=await Promise.all(thumbs.map(b=>sharp(b).metadata()));const comps=[];let top=0;for(let row=0;row<4;row++){const height=Math.max(...meta.slice(row*2,row*2+2).map(m=>m.height),0);for(let col=0;col<2;col++){const n=row*2+col;if(n<thumbs.length)comps.push({input:thumbs[n],left:col*250,top})}top+=height+(height?10:0)}await sharp({create:{width:490,height:top,channels:3,background:'#EDF2EE'}}).composite(comps).png().toFile(path.join(qaDir,`contact-${i/8+1}.png`))}
  fs.writeFileSync(path.join(qaDir,'audit.json'),JSON.stringify({date:'2026-10-25',cards:58,groups:10,previewImages:0,originalTextRetained:true,proseMatches:true,checks,actual135PasteTested:false},null,2));await qa.close();
  console.log(JSON.stringify({native:path.join(root,'article-v6-cards.html'),image:path.join(root,'article-v6-card-images.html'),cards:58,groups:10,previewImages:0,checks:checks.length}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
