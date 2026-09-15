import fs from 'node:fs/promises';import path from 'node:path';import {pathToFileURL} from 'node:url';
const {chromium}=await import(process.env.MO_PLAYWRIGHT_MODULE||'/Users/olivialee/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.mjs');
const browser=await chromium.launch({executablePath:process.env.MO_CHROME_EXECUTABLE||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const dir=import.meta.dirname;const a=path.resolve(dir,'../..');const pg=await browser.newPage({viewport:{width:720,height:1600},deviceScaleFactor:2});let checks=[];
for(const f of (await fs.readdir(dir)).filter(x=>x.endsWith('.svg')).sort()){
 await pg.goto(pathToFileURL(path.join(dir,f)).href);await pg.evaluate(()=>document.fonts.ready);
 let bounds=await pg.locator('svg').evaluate(svg=>{let bad=[];for(let t of svg.querySelectorAll('text')){let b=t.getBBox();if(b.x<0||b.x+b.width>720||b.y<0||b.y+b.height>svg.viewBox.baseVal.height)bad.push({text:t.textContent,x:b.x,width:b.width})}return bad});
 if(bounds.length)throw new Error(f+JSON.stringify(bounds));
 await pg.locator('svg').screenshot({path:path.join(dir,f.replace('.svg','.png'))});checks.push({file:f,textBounds:'pass',pixelWidth:1440});
}
const html=pathToFileURL(path.join(a,'article-v3.html')).href;
for(const width of [375,390,430,1000]){
 await pg.setViewportSize({width,height:900});await pg.goto(html);await pg.locator('main img').evaluateAll(img=>Promise.all(img.map(i=>i.decode())));
 let c=await pg.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,images:[...document.querySelectorAll('main img')].map(i=>({loaded:i.complete&&i.naturalWidth>0,width:i.clientWidth})),headings:[...document.querySelectorAll('main h2,main h3')].map(n=>n.innerText)}));if(c.scrollWidth>width||c.images.some(i=>!i.loaded))throw Error(JSON.stringify(c));checks.push(c);
 if(width===390){await pg.screenshot({path:path.join(dir,'qa-mobile-top.png')});await pg.locator('main img').nth(0).screenshot({path:path.join(dir,'qa-mobile-figure.png')});await pg.locator('main img').nth(3).scrollIntoViewIfNeeded();await pg.screenshot({path:path.join(dir,'qa-mobile-types.png')});await pg.locator('main img').nth(0).click();if(!await pg.locator('dialog').isVisible())throw Error('zoom failed');await pg.locator('dialog button').click();}
}
await pg.setViewportSize({width:1080,height:1500});await pg.setContent('<html><body style="margin:0;background:#e9eeea;display:grid;grid-template-columns:repeat(3,352px);gap:10px">'+(await fs.readdir(dir)).filter(x=>/^0.*png$/.test(x)).sort().map(f=>'<img style="width:352px" src="'+pathToFileURL(path.join(dir,f)).href+'">').join('')+'</body></html>');await pg.locator('img').evaluateAll(img=>Promise.all(img.map(i=>i.decode())));await pg.screenshot({path:path.join(dir,'qa-contact.png'),fullPage:true});
await fs.writeFile(path.join(dir,'qa-report.json'),JSON.stringify(checks,null,2));await browser.close();console.log('Six PNGs rendered, 4 viewport checks passed, zoom passed.');
