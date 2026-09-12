import fs from 'node:fs/promises';import path from 'node:path';import {pathToFileURL} from 'node:url';
const {chromium}=await import(process.env.MO_PLAYWRIGHT_MODULE || '/Users/olivialee/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.mjs');
const h=import.meta.dirname,a=path.resolve(h,'../assets/v13');
const manifest=JSON.parse(await fs.readFile(path.join(a,'manifest.json'),'utf8'));
const gallery=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>旁观机器 · v13 配图</title><style>body{margin:24px;background:#eef3ef;color:#17633f;font:16px/1.6 -apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif}h1{font-size:24px}.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}.item{background:white;padding:12px}img{width:100%;height:auto}h2{font-size:16px;margin:0 0 10px}p{font-size:12px}</style><h1>旁观机器 · 18 张文章配图</h1><p>点击图片打开原尺寸 PNG。编号对应文章顺序；表格与示意图为精确排版，场景插画为 AI 生成。</p><div class="gallery">${manifest.map(x=>`<section class="item"><h2>${x.id} · ${x.title}</h2><a href="${x.file}"><img src="${x.file}" alt="${x.title}"></a><p>${x.kind}</p></section>`).join('')}</div></html>`;
await fs.writeFile(path.join(a,'gallery.html'),gallery);
const browser=await chromium.launch({executablePath:process.env.MO_CHROME_EXECUTABLE || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const page=await browser.newPage({viewport:{width:390,height:844},deviceScaleFactor:1});
await page.goto(pathToFileURL(path.join(h,'article-v13.html')).href);await page.evaluate(()=>document.fonts.ready);await page.locator('img').evaluateAll(imgs=>Promise.all(imgs.map(x=>x.decode())));
const report={};
for(const width of [360,390,650]){await page.setViewportSize({width,height:844});report[width]=await page.evaluate(()=>({scrollWidth:document.documentElement.scrollWidth,viewport:innerWidth,images:[...document.images].length,brokenImages:[...document.images].filter(x=>!x.complete||!x.naturalWidth).length,tables:document.querySelectorAll('table').length,styles:document.querySelectorAll('style').length,scripts:document.scripts.length,chapterBorders:[...document.querySelectorAll('h2')].map(e=>getComputedStyle(e).borderBottomWidth)}));if(report[width].scrollWidth>width||report[width].brokenImages||report[width].tables)throw Error('Layout failure '+width);}
await page.setViewportSize({width:390,height:844});await page.screenshot({path:'/tmp/v13-mobile-top.png'});
await page.locator('img[alt="企业使用模型的三种方式"]').scrollIntoViewIfNeeded();await page.screenshot({path:'/tmp/v13-mobile-options.png'});
await page.locator('img[alt="DGX Spark"]').scrollIntoViewIfNeeded();await page.screenshot({path:'/tmp/v13-mobile-spark.png'});
await fs.writeFile(path.join(a,'layout-check.json'),JSON.stringify(report,null,2)+'\n');await fs.writeFile('/tmp/v13-rendered-text.txt',await page.locator('article').innerText());
await page.setViewportSize({width:1200,height:1000});await page.goto(pathToFileURL(path.join(a,'gallery.html')).href);await page.locator('img').evaluateAll(imgs=>Promise.all(imgs.map(x=>x.decode())));await page.screenshot({path:'/tmp/v13-gallery.png',fullPage:true});
await browser.close();console.log(JSON.stringify(report));
