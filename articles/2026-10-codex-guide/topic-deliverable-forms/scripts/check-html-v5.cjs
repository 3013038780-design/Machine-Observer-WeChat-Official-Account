const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
const modules=process.argv[2];const{chromium}=require(path.join(modules,'playwright'));
const root=path.resolve(__dirname,'..');
(async()=>{
 const m=JSON.parse(fs.readFileSync(path.join(root,'assets/tables-v5/manifest.json')));
 const source=fs.readFileSync(path.join(root,'article-v5.md'),'utf8');
 const expectedLinks=[...source.matchAll(/\[[^\]]+\]\((https?:[^)]+)\)/g)].map(x=>x[1]);
 const expected=m.tables.flatMap(t=>t.images.flatMap(im=>im.rows)).map(row=>row.map(v=>v.replace(/\*\*([^*]+)\*\*/g,'$1').replace(/`([^`]+)`/g,'$1')));
 const headers=m.tables.map(t=>t.images.reduce((n,im)=>n+(fs.readFileSync(path.join(root,'assets/tables-v5/source',im.sourceFile),'utf8').match(/<thead>/g)||[]).length,0));
 if(headers.length!==10||headers.some(n=>n!==1))throw Error('Image header mismatch');
 const b=await chromium.launch({headless:true});const p=await b.newPage();const checks=[];const prose={};
 for(const version of ['tables','images']){
  await p.goto(pathToFileURL(path.join(root,`article-v5-${version}.html`)).href);
  await p.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(im=>im.complete?Promise.resolve():new Promise(resolve=>{im.onload=resolve;im.onerror=resolve})));});
  for(const width of [375,390,760,1440]){
   await p.setViewportSize({width,height:900});
   const d=await p.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,tableCount:document.querySelectorAll('table').length,headerCount:document.querySelectorAll('thead').length,rows:[...document.querySelectorAll('tbody tr')].map(tr=>[...tr.cells].map(td=>td.innerText)),overflow:[...document.querySelectorAll('td,th')].filter(el=>el.scrollWidth>el.clientWidth+2||el.scrollHeight>el.clientHeight+2).map(el=>el.innerText),conditions:[...document.querySelectorAll('p')].filter(el=>el.textContent.startsWith('制作与运行条件：')).length,links:[...document.querySelectorAll('a[href]')].map(el=>el.href),footer:(document.body.innerText.match(/旁观机器 · MACHINE OBSERVER/g)||[]).length,h1:document.querySelector('h1').innerText,broken:[...document.images].filter(im=>!im.complete||!im.naturalWidth).length,external:!!document.querySelector('style,script,link[rel=stylesheet]'),bodyFont:parseFloat(getComputedStyle(document.querySelector('section > p[style*="text-align:justify"]')).fontSize),tableFont:document.querySelector('td')?parseFloat(getComputedStyle(document.querySelector('td')).fontSize):16*document.querySelector('img[alt*="："]').getBoundingClientRect().width/360}));
   if(d.overflow.length||d.scrollWidth>width||d.conditions!==10||JSON.stringify(d.links)!==JSON.stringify(expectedLinks)||d.footer!==1||d.broken||d.external||d.bodyFont!==16||d.tableFont>16.1||d.tableFont<15.5)throw Error(JSON.stringify(d));
   if(version==='tables'&&(d.tableCount!==10||d.headerCount!==10||JSON.stringify(d.rows)!==JSON.stringify(expected)))throw Error('Native content mismatch');
   delete d.rows;checks.push({version,...d});
  }
  prose[version]=await p.evaluate(()=>{const c=document.body.cloneNode(true);c.querySelectorAll('table,img').forEach(el=>el.remove());return c.textContent.replace(/\s+/g,' ').trim()});
  await p.setViewportSize({width:390,height:1000});
  for(const[name,n]of[['first',0],['agent',3],['design',6],['engineering',8],['last',9]]){
   await p.locator('h2').nth(n).evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));
   await p.screenshot({path:path.join(root,`qa/html-v5/${version}-${name}-390.png`)});
  }
  await p.setViewportSize({width:760,height:1000});await p.locator('h2').first().evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));
  await p.screenshot({path:path.join(root,`qa/html-v5/${version}-first-760.png`)});
 }
 if(prose.tables!==prose.images)throw Error('Prose differs between versions');
 const result={date:'2026-10-25',checks,rows:58,imageHeadersPerGroup:headers,tableImages:m.imageCount,proseMatches:true,actual135PasteTested:false};
 fs.writeFileSync(path.join(root,'qa/html-v5/content-and-header-check.json'),JSON.stringify(result,null,2));await b.close();
 console.log(JSON.stringify({rows:58,groups:10,images:m.imageCount,links:expectedLinks.length,checks:checks.length,proseMatches:true}));
})().catch(e=>{console.error(e);process.exitCode=1});
