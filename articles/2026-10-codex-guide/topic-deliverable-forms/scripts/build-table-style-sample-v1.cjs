const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
const base=process.argv[2];
const {chromium}=require(path.join(base,'playwright'));
const root=path.resolve(__dirname,'..');
const output=path.join(root,'assets/table-style-sample-v1');
fs.mkdirSync(output,{recursive:true});
const original=JSON.parse(fs.readFileSync(path.join(root,'assets/tables-v2/manifest.json'),'utf8')).tables[0].images[0];
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const plain=s=>s.replace(/\*\*([^*]+)\*\*/g,'$1').replace(/`([^`]+)`/g,'$1');
const rows=original.rows.map(row=>'<tr>'+row.map((s,i)=>`<td class="c${i}">${esc(plain(s))}</td>`).join('')+'</tr>').join('');
const html=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>
*{box-sizing:border-box}html,body{margin:0;padding:0;width:360px;background:white}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;-webkit-font-smoothing:antialiased}
table{width:360px;table-layout:fixed;border-collapse:collapse}
th{font-size:14px;font-weight:500;line-height:1.45;color:#61746A;text-align:left;padding:9px 6px;border-bottom:2px solid #287A51}
td{font-size:16px;line-height:1.45;text-align:left;vertical-align:top;padding:9px 6px;border-bottom:1px solid #DCE8E0;word-break:normal;overflow-wrap:anywhere;line-break:strict;color:#333}
.c0{font-weight:600;color:#17633F}.c2{background:#F2F7F3;color:#244C36}
</style><body><table><colgroup><col style="width:25%"><col style="width:28%"><col style="width:47%"></colgroup><thead><tr><th>交付物</th><th>用途 / 入口</th><th>这样跟 AI 说</th></tr></thead><tbody>${rows}</tbody></table></body></html>`;
fs.writeFileSync(path.join(output,'sample-source.html'),html);
(async()=>{const browser=await chromium.launch({headless:true});const context=await browser.newContext({viewport:{width:360,height:900},deviceScaleFactor:3});const page=await context.newPage();await page.setContent(html);await page.evaluate(()=>document.fonts.ready);const audit=await page.evaluate(()=>({width:document.querySelector('table').getBoundingClientRect().width,rows:[...document.querySelectorAll('tbody tr')].map(tr=>[...tr.cells].map(td=>td.innerText)),overflow:[...document.querySelectorAll('td,th')].filter(el=>el.scrollWidth>el.clientWidth+1||el.scrollHeight>el.clientHeight+1).map(el=>el.innerText),font:getComputedStyle(document.querySelector('td')).fontSize}));if(audit.overflow.length||JSON.stringify(audit.rows)!==JSON.stringify(original.rows.map(row=>row.map(plain))))throw Error('Sample validation failed');await page.locator('table').screenshot({path:path.join(output,'sample-new.png')});
const imageData=file=>'data:image/png;base64,'+fs.readFileSync(file).toString('base64');
const imageTag=file=>`<img src="${imageData(file)}" style="display:block;width:100%;height:auto;border:0" alt="网站交付物三列样张">`;
const compare=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>三列表格样张对比</title><body style="margin:0;background:#fff"><section style="box-sizing:border-box;max-width:384px;margin:0 auto;padding:18px 12px;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif;color:#333;font-size:16px;line-height:1.75"><h1 style="font-size:20px;color:#17633F;margin:0 0 12px">三列表格样张对比</h1><p style="margin:0 0 18px">同样三项内容、同样 16px 表格字号，比较线条、颜色和层级。</p><h2 style="font-size:18px;color:#17633F;margin:20px 0 12px">新样张 · 减轻格子感</h2><p style="margin:0 0 16px">浏览器里可以放文章，也可以放一个能筛选、比较、计算的小作品。先从最容易打开的入口开始。</p>${imageTag(path.join(output,'sample-new.png'))}<p style="font-size:14px;color:#61746A;margin:12px 0 28px">只留横向分隔，弱化表头，交办示例用浅绿底区分；取消图内重复分组名。</p><h2 style="font-size:18px;color:#17633F;margin:20px 0 12px">原版 · 排版 v2</h2>${imageTag(path.join(root,'assets/tables-v2',original.filename))}</section></body></html>`;
fs.writeFileSync(path.join(root,'table-style-comparison-v1.html'),compare);
await page.setViewportSize({width:390,height:844});await page.goto(pathToFileURL(path.join(root,'table-style-comparison-v1.html')).href);await page.screenshot({path:path.join(output,'comparison-mobile-390.png')});
fs.writeFileSync(path.join(output,'audit.json'),JSON.stringify(audit,null,2));await browser.close();console.log(JSON.stringify(audit));})();
