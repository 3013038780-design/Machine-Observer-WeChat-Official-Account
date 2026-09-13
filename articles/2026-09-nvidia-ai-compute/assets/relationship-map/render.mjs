import fs from 'node:fs/promises';import path from 'node:path';import {pathToFileURL} from 'node:url';
const {chromium}=await import('/Users/olivialee/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.mjs');
const b=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});const p=await b.newPage({deviceScaleFactor:1.5});const out=import.meta.dirname;
for(const n of ['full','personal','enterprise','provider']){await p.goto(pathToFileURL(path.join(out,n+'.svg')).href);await p.evaluate(()=>document.fonts.ready);await p.locator('svg').screenshot({path:path.join(out,n+'.png')});}
await b.close();console.log('Rendered overview and three detail images');
