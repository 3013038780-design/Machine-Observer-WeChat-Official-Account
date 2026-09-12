// Render exact reviewed table text to compact, high-resolution PNGs and embed into v8.
const { chromium }=await import(process.env.MO_PLAYWRIGHT_MODULE || 'playwright-core');
import fs from 'node:fs/promises';
import path from 'node:path';
const here=import.meta.dirname, out=path.join(here,'table-images-v8');
await fs.mkdir(out,{recursive:true});
const source=await fs.readFile(path.join(here,'article-v7.html'),'utf8');
const tables=[...source.matchAll(/<table\b[\s\S]*?<\/table>/g)].map(m=>m[0]);
const specs=[['01-product-map',[24,35,41]],['02-architecture',[32,68]],['03-components',[40,60]],['04-geforce-prices',[40,28,32]],['05-metrics',[35,65]],['06-workstations',[64,36]],['07-gpu-specs',[31,36,33]],['08-market-prices',[58,42]]];
if(tables.length!==specs.length)throw Error('Unexpected table count');
const browser=await chromium.launch({executablePath:process.env.MO_CHROME_EXECUTABLE || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const page=await browser.newPage({viewport:{width:366,height:1000},deviceScaleFactor:3});
let document=source, fragment=await fs.readFile(path.join(here,'article-v7-fragment.html'),'utf8');
const manifest=[];
for(let i=0;i<tables.length;i++){
 const [name,widths]=specs[i];
 const css=`body{margin:0;background:white;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif}table{width:366px!important;margin:0!important;table-layout:fixed!important;border-collapse:collapse!important;letter-spacing:0!important}th,td{padding:7px 6px!important;line-height:1.5!important;font-size:14px!important;vertical-align:top!important;overflow-wrap:anywhere!important}th{font-size:13px!important;padding:8px 6px!important}strong{font-weight:600!important}${widths.map((w,j)=>`tr>*:nth-child(${j+1}){width:${w}%;box-sizing:border-box}`).join('')}`;
 const html=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>${css}</style><body>${tables[i]}</body></html>`;
 await fs.writeFile(path.join(out,name+'.html'),html);
 await page.setContent(html);await page.evaluate(()=>document.fonts.ready);
 const table=page.locator('table');
 const text=await table.innerText(), box=await table.boundingBox();
 if(await page.evaluate(()=>document.documentElement.scrollWidth>366))throw Error('Overflow '+name);
 const png=await table.screenshot({path:path.join(out,name+'.png')});
 const alt=text.replace(/\s+/g,' ').replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;');
 const image=`<img src="data:image/png;base64,${png.toString('base64')}" alt="${alt}" style="display:block;width:100%;max-width:366px;height:auto;margin:18px auto;border:0;">`;
 document=document.replace(tables[i],image);fragment=fragment.replace(tables[i],image);
 manifest.push({file:name+'.png',cssWidth:366,cssHeight:box.height,pixelWidth:png.readUInt32BE(16),pixelHeight:png.readUInt32BE(20),text});
}
await browser.close();
await fs.writeFile(path.join(out,'manifest.json'),JSON.stringify(manifest,null,2)+'\n');
await fs.writeFile(path.join(here,'article-v8.html'),document);
await fs.writeFile(path.join(here,'article-v8-fragment.html'),fragment);
await fs.copyFile(path.join(here,'article-v7.md'),path.join(here,'article-v8.md'));
console.log(JSON.stringify(manifest.map(({text,...m})=>m),null,2));
