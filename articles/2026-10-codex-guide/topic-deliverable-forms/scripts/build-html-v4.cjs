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
const sourcePath = path.join(root, 'article-v4.md');
const source = fs.readFileSync(sourcePath, 'utf8');
const theme = JSON.parse(fs.readFileSync(path.join(repo, 'assets/theme.json'), 'utf8'));
const outDir = path.join(root, 'assets/tables-v4');
const qaDir = path.join(root, 'qa/html-v4');
fs.mkdirSync(path.join(outDir, 'source'), { recursive: true });
fs.mkdirSync(qaDir, { recursive: true });
const colors = { accent: theme.accent, green: '#287A51', pale: '#F2F7F3', border: '#C7DDCF' };
const settings = { width: 360, scale: 3, font: 16, lineHeight: 1.45, maxRows: 5, maxHeight: 880, columns: [25, 28, 47] };
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
const blocks = parse(source);
const tables = blocks.filter(b => b.type === 'table');
if (tables.length !== 18 || tables.reduce((n, t) => n + t.rows.length, 0) !== 119) throw new Error('Unexpected source coverage');

function tableHTML(table, rows, part, total, inlineOnly = false) {
 const cells=rows.map(row=>'<tr>'+row.map((v,i)=>`<td style="font-size:16px;line-height:1.45;letter-spacing:0;text-align:left;vertical-align:top;padding:9px 6px;border:0;border-bottom:1px solid #DCE8E0;word-break:normal;overflow-wrap:anywhere;line-break:strict;color:${i===0?'#17633F':i===2?'#244C36':'#333'};background:${i===2?'#F2F7F3':'#FFFFFF'};font-weight:${i===0?'600':'400'};">${esc(plain(v))}</td>`).join('')+'</tr>').join('');
 const head=['交付物','用途 / 入口','这样跟 AI 说'].map(h=>`<th style="font-size:14px;font-weight:500;line-height:1.45;letter-spacing:0;color:#61746A;text-align:left;vertical-align:middle;padding:9px 6px;border:0;border-bottom:2px solid #287A51;background:#FFFFFF;">${esc(h)}</th>`).join('');
 const cols=settings.columns.map(n=>`<col style="width:${n}%">`).join('');
 const fragment=`<table style="border-collapse:collapse;table-layout:fixed;width:100%;margin:0;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;"><colgroup>${cols}</colgroup>${part === 1 ? '<thead><tr>'+head+'</tr></thead>' : ''}<tbody>${cells}</tbody></table>`;
 if(inlineOnly)return fragment;
 return `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>*{box-sizing:border-box}html,body{margin:0;padding:0;background:white;width:360px}body{-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}.sheet{width:360px}</style></head><body><section class="sheet">${fragment}</section></body></html>`;
}
function balanced(rows, maxRows) {
  const count = Math.ceil(rows.length / maxRows);
  const base = Math.floor(rows.length / count), extra = rows.length % count;
  const chunks = []; let offset = 0;
  for (let i = 0; i < count; i++) {
    const length = base + (i < extra ? 1 : 0);
    chunks.push(rows.slice(offset, offset + length)); offset += length;
  }
  return chunks;
}
async function main() {
  let browser;
  try {
    browser = await chromium.launch({ headless: true });
  } catch (e) {
    const localChrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
    if (!fs.existsSync(localChrome)) throw e;
    browser = await chromium.launch({ headless: true, executablePath: localChrome });
  }
  try {
    const context = await browser.newContext({ viewport: { width: settings.width, height: 900 }, deviceScaleFactor: settings.scale });
    const page = await context.newPage();
    const manifest = { source: 'article-v4.md', sourceSha256: crypto.createHash('sha256').update(source).digest('hex'), settings, imageCount: 0, rowCount: 0, tables: [] };
    let sequence = 0;
    for (const table of tables) {
      let chunks = balanced(table.rows, settings.maxRows);
      // Split any unusually tall chunk without reducing the font or cropping text.
      for (let j = 0; j < chunks.length; j++) {
        await page.setContent(tableHTML(table, chunks[j], j + 1, chunks.length));
        await page.evaluate(() => document.fonts.ready);
        const height = await page.locator('.sheet').evaluate(el => el.getBoundingClientRect().height);
        if (height > settings.maxHeight && chunks[j].length > 1) {
          const middle = Math.ceil(chunks[j].length / 2);
          chunks.splice(j, 1, chunks[j].slice(0, middle), chunks[j].slice(middle)); j--;
        }
      }
      const entry = { group: table.group, heading: table.heading, rowCount: table.rows.length, images: [] };
      for (let j = 0; j < chunks.length; j++) {
        sequence++;
        const filename = `${String(sequence).padStart(2, '0')}-group-${String(table.group).padStart(2, '0')}-${j + 1}.png`;
        const sourceFile = filename.replace(/\.png$/, '.html');
        const html = tableHTML(table, chunks[j], j + 1, chunks.length);
        fs.writeFileSync(path.join(outDir, 'source', sourceFile), html);
        await page.setContent(html);
        await page.evaluate(() => document.fonts.ready);
        const audit = await page.evaluate(() => ({
          width: document.querySelector('.sheet').getBoundingClientRect().width,
          height: document.querySelector('.sheet').getBoundingClientRect().height,
          bodyWidth: document.body.scrollWidth,
          cells: [...document.querySelectorAll('tbody tr')].map(tr => [...tr.cells].map(td => td.innerText)),
          overflow: [...document.querySelectorAll('td,th')].filter(el => el.scrollWidth > el.clientWidth + 2 || el.scrollHeight > el.clientHeight + 2).map(el => el.innerText),
          fontSize: getComputedStyle(document.querySelector('td')).fontSize,
        }));
        if (audit.width !== settings.width || audit.bodyWidth > settings.width || audit.overflow.length) throw new Error('Table overflow: ' + JSON.stringify(audit));
        if (JSON.stringify(audit.cells) !== JSON.stringify(chunks[j].map(r => r.map(plain)))) throw new Error('Table text mismatch');
        await page.locator('.sheet').screenshot({ path: path.join(outDir, filename), animations: 'disabled' });
        const info = await sharp(path.join(outDir, filename)).metadata();
        const image = { filename, sourceFile, part: j + 1, parts: chunks.length, width: info.width, height: info.height, logicalHeight: audit.height, rows: chunks[j], cellAudit: { overflow: audit.overflow.length, fontSize: audit.fontSize } };
        entry.images.push(image); manifest.rowCount += chunks[j].length;
        if (args.includes('--sample')) {
          fs.writeFileSync(path.join(qaDir, 'sample-audit.json'), JSON.stringify(image, null, 2));
          console.log(JSON.stringify({ sample: path.join(outDir, filename), width: info.width, height: info.height, audit }));
          return;
        }
      }
      manifest.tables.push(entry);
    }
    manifest.imageCount = sequence;
    if (manifest.rowCount !== 119) throw new Error('Lost source rows');
    fs.writeFileSync(path.join(outDir, 'manifest.json'), JSON.stringify(manifest, null, 2));
    await context.close();

    const brandPath = path.join(repo, 'assets/brand/2026-09-12-header-v2/03-retro-terminal.png');
    const brandData = fs.readFileSync(brandPath);
    const imageSource = (file, embedded) => embedded ? 'data:image/png;base64,' + fs.readFileSync(path.join(outDir, file)).toString('base64') : `assets/tables-v4/${file}`;
    function article(embedded, native = false) {
      const parts = [];
      const brand = embedded ? 'data:image/png;base64,' + brandData.toString('base64') : 'assets/header-retro-terminal.png';
      parts.push(`<img src="${brand}" alt="旁观机器品牌首图：复古电脑" style="display:block;width:100%;max-width:100%;height:auto;margin:0 0 18px;border-radius:3px;">`);
      for (const block of blocks) {
        if (block.type === 'h1') parts.push(`<h1 style="${theme.h1.replace('margin:36px 0 30px;', 'margin:20px 0 22px;')}">${inline(block.text)}</h1>`);
        if (block.type === 'h2') parts.push(`<h2 style="${theme.h2.replace('margin:44px 0 18px;', 'margin:32px 0 16px;')}text-wrap:balance;">${inline(block.text)}</h2>`);
        if (block.type === 'p') {
          if (block.text === '旁观机器 · MACHINE OBSERVER') continue;
          if (plain(block.text).startsWith('制作与运行条件：')) {
            parts.push(`<section style="margin:16px 0 20px;padding:10px 12px;background:${colors.pale};border-left:2px solid ${colors.green};"><p style="margin:0;font-size:16px;line-height:1.75;letter-spacing:0.5px;color:#43594B;text-align:justify;">${inline(plain(block.text)).replace('制作与运行条件：', '<strong style="color:#17633F;font-weight:600;">制作与运行条件：</strong>')}</p></section>`);
          } else parts.push(`<p style="${theme.p}">${inline(block.text)}</p>`);
        }
        if (block.type === 'quote') parts.push(`<blockquote style="margin:18px 0;padding:10px 12px;background:${colors.pale};border-left:3px solid ${colors.accent};font-size:16px;"><p style="margin:0;font-size:16px;line-height:1.75;letter-spacing:0.5px;color:#43594B;text-align:justify;">${inline(block.text)}</p></blockquote>`);
        if (block.type === 'table') {
          const group = manifest.tables.find(t => t.group === block.group);
          parts.push('<section style="margin:12px 0 16px;">');
          if(native){parts.push(tableHTML(block,block.rows,1,1,true));parts.push('</section>');continue;}
          for (const img of group.images) {
            const alt = `${block.heading} ${img.part}/${img.parts}：` + img.rows.map(r => r[0]).join('、');
            parts.push(`<img src="${imageSource(img.filename, embedded)}" alt="${esc(alt)}" width="${img.width}" height="${img.height}" style="display:block;width:100%;max-width:100%;height:auto;margin:0;border:0;">`);
          }
          parts.push('</section>');
        }
      }
      parts.push('<p style="margin:28px 0 12px;text-align:center;font-size:12px;line-height:1.6;color:#17633F;letter-spacing:1.5px;">旁观机器 · MACHINE OBSERVER</p>');
      return `<section style="${theme.container}box-sizing:border-box;max-width:384px;margin:0 auto;">${parts.join('\n')}</section>`;
    }
    const title = blocks.find(b => b.type === 'h1').text;
    const wrap = body => `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(title)}</title></head><body style="margin:0;padding:14px 0 24px;background:#ffffff;">${body}</body></html>`;
    fs.writeFileSync(path.join(root, 'article-v4-images.html'), wrap(article(true)));
    fs.writeFileSync(path.join(root, 'article-v4-images-body.html'), article(true));
    fs.writeFileSync(path.join(root, 'article-v4-images-linked.html'), wrap(article(false)));
    fs.writeFileSync(path.join(root, 'article-v4-tables.html'), wrap(article(true, true)));
    fs.writeFileSync(path.join(root, 'article-v4-tables-body.html'), article(true, true));
    fs.copyFileSync(brandPath, path.join(root, 'assets/header-retro-terminal.png'));

    const qaContext = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1 });
    const preview = await qaContext.newPage();
    const errors = [];
    preview.on('pageerror', e => errors.push(e.message));
    await preview.goto(pathToFileURL(path.join(root, 'article-v4-images.html')).href);
    await preview.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(im => im.complete ? Promise.resolve() : new Promise(resolve => { im.onload = resolve; im.onerror = resolve; }))); });
    const viewports = [];
    for (const width of [375, 390, 760]) {
      await preview.setViewportSize({ width, height: 844 });
      const data = await preview.evaluate(() => ({ viewport: innerWidth, scrollWidth: document.documentElement.scrollWidth, imageCount: document.images.length, brokenImages: [...document.images].filter(im => !im.complete || !im.naturalWidth).map(im => im.alt), h2Count: document.querySelectorAll('h2').length, bodyFont: getComputedStyle(document.querySelector('section')).fontSize, paragraphLineHeight: getComputedStyle(document.querySelector('section > p[style*="text-align:justify"]')).lineHeight, hasTable: Boolean(document.querySelector('table')), hasExternalStyle: Boolean(document.querySelector('link[rel=stylesheet], style, script')) }));
      if (data.scrollWidth > width || data.brokenImages.length || data.hasTable || data.hasExternalStyle) throw new Error('Article validation failure: ' + JSON.stringify(data));
      viewports.push(data);
    }
    await preview.setViewportSize({ width: 390, height: 844 });
    await preview.evaluate(() => scrollTo(0, 0));
    await preview.screenshot({ path: path.join(qaDir, 'mobile-top-390.png') });
    for (const [name, index] of [['mobile-first-table', 1], ['mobile-agent-table', 4], ['mobile-final-table', 18]]) {
      await preview.locator('h2').nth(index - 1).evaluate(el => scrollTo(0, el.getBoundingClientRect().top + scrollY));
      await preview.screenshot({ path: path.join(qaDir, `${name}-390.png`) });
    }
    await preview.setViewportSize({ width: 760, height: 1000 });
    await preview.evaluate(() => scrollTo(0, 0));
    await preview.screenshot({ path: path.join(qaDir, 'desktop-top-760.png') });
    const allImages = manifest.tables.flatMap(t => t.images);
    // Small contact sheets for reviewing every table layout.
    for (let i = 0; i < allImages.length; i += 8) {
      const subset = allImages.slice(i, i + 8);
      const thumbs = await Promise.all(subset.map(async img => ({ buffer: await sharp(path.join(outDir, img.filename)).resize({ width: 300 }).png().toBuffer(), filename: img.filename })));
      const meta = await Promise.all(thumbs.map(x => sharp(x.buffer).metadata()));
      const rowHeights = [0, 1, 2, 3].map(r => Math.max(...meta.slice(r * 2, r * 2 + 2).map(m => m.height), 0));
      let y = 0; const composites = [];
      for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 2; c++) {
          const n = r * 2 + c;
          if (n < thumbs.length) composites.push({ input: thumbs[n].buffer, left: c * 312, top: y });
        }
        y += rowHeights[r] + (rowHeights[r] ? 10 : 0);
      }
      await sharp({ create: { width: 612, height: y, channels: 3, background: '#E8EFEA' } }).composite(composites).png().toFile(path.join(qaDir, `table-contact-${Math.floor(i / 8) + 1}.png`));
    }
    const audit = { sourceSha256: manifest.sourceSha256, sourceTables: tables.length, rows: manifest.rowCount, tableImages: manifest.imageCount, settings, viewports, pageErrors: errors, checks: ['all table text matches Markdown', 'no table cell overflow', 'all 119 rows retained', '18 exploration groups retained', '375/390/760 widths no horizontal overflow', 'all images load', 'final body uses inline styles only'], actual135PasteTested: false };
    fs.writeFileSync(path.join(qaDir, 'audit.json'), JSON.stringify(audit, null, 2));
    await qaContext.close();
    console.log(JSON.stringify({ html: path.join(root, 'article-v4-images.html'), tableImages: manifest.imageCount, rows: manifest.rowCount, viewports, sourceSha256: manifest.sourceSha256 }));
  } finally { await browser.close(); }
}
main().catch(e => { console.error(e); process.exitCode = 1; });
