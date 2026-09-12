const { chromium } = await import(process.env.MO_PLAYWRIGHT_MODULE || 'playwright-core');
import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const upper=path.resolve(import.meta.dirname, '..');
const browser=await chromium.launch({executablePath:process.env.MO_CHROME_EXECUTABLE || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const results=[];
for(const width of [360,390,430,1100]){
 const page=await browser.newPage({viewport:{width,height:900},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(path.join(upper,'article-v4.html')).href);
 await page.evaluate(()=>document.fonts.ready);
 const metrics=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,paragraphs:[...document.querySelectorAll('body>section>p')].map(p=>({font:getComputedStyle(p).fontSize,lineHeight:getComputedStyle(p).lineHeight,spacing:getComputedStyle(p).letterSpacing})),overflow:[...document.querySelectorAll('body *')].filter(el=>{const r=el.getBoundingClientRect();return r.width>0&&(r.right>innerWidth+1||r.left< -1)}).map(el=>({tag:el.tagName,text:el.textContent.slice(0,90)})),images:[...document.images].map(el=>({loaded:el.complete&&el.naturalWidth>0,width:el.naturalWidth,height:el.naturalHeight})),accent:getComputedStyle(document.querySelector('h1')).color,badTags:document.querySelectorAll('script,style,iframe').length,links:document.querySelectorAll('a[href]').length,tables:document.querySelectorAll('table').length}));
 results.push({width,...metrics,errors});
 if(width===390){
  await page.screenshot({path:path.join(upper,'qa-v4/mobile-full.png'),fullPage:true});
  await page.screenshot({path:path.join(upper,'qa-v4/mobile-opening.png')});
  for(const [i,name] of [[0,'product-map'],[1,'architecture'],[2,'launch-prices'],[3,'workstations'],[4,'gpu-specs'],[5,'market-quotes']]){
   const el=page.locator('table').nth(i);const y=await el.evaluate(el=>el.getBoundingClientRect().top+scrollY);
   await page.evaluate(y=>scrollTo(0,Math.max(0,y-100)),y);
   await page.screenshot({path:path.join(upper,`qa-v4/mobile-${name}.png`)});
  }
 }
 if(width===1100)await page.screenshot({path:path.join(upper,'qa-v4/desktop-opening.png')});
 await page.close();
}
await browser.close();
await fs.writeFile(path.join(upper,'qa-v4/layout-check.json'),JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify(results.map(({paragraphs,...r})=>({...r,bodyFonts:[...new Set(paragraphs.map(p=>JSON.stringify(p)))]})),null,2));
if(results.some(r=>r.overflow.length||r.errors.length||r.badTags||r.images.some(i=>!i.loaded)))process.exitCode=1;
