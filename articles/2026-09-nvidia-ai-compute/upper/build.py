"""Render the reviewed Markdown into inline-styled, 135-oriented article HTML."""
from pathlib import Path
import html
import importlib.util
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location('wechat_renderer', ROOT / 'scripts/render.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
theme = json.loads((ROOT / 'assets/theme.json').read_text())
sources = json.loads((HERE.parent / 'research/sources.json').read_text())
source_map = {s['id']: s for s in sources}
md = (HERE / 'article-v1.md').read_text()
title = md.splitlines()[0].removeprefix('# ')
body = renderer.render('\n'.join(md.splitlines()[1:]), theme)

# The inherited renderer wraps h2 in p. Remove that invalid wrapper here.
body = re.sub(r'<p style="margin:0;">(<h2.*?</h2>)</p>', r'\1', body, flags=re.S)

def chapter(match):
    chapter.number += 1
    return (
        '<section style="margin:44px 0 18px;padding:0 0 12px;border-bottom:1px solid #E5C4C0;">'
        f'<p style="margin:0 0 8px;font-size:12px;color:#B91C1C;letter-spacing:2px;line-height:1.5;">'
        f'{chapter.number:02d} / 算力生意</p>'
        f'<h2 style="margin:0;color:#B91C1C;font-size:18px;font-weight:700;line-height:1.55;letter-spacing:0.5px;">{match[1]}</h2>'
        '</section>'
    )
chapter.number = 0
body = re.sub(r'<h2[^>]*>(.*?)</h2>', chapter, body, flags=re.S)

def citation(match):
    s = source_map[match[1]]
    return (f'<a href="{html.escape(s["url"], quote=True)}" '
            f'title="{html.escape(s["title"], quote=True)}" '
            'style="font-size:11px;line-height:1;color:#996b65;text-decoration:none;'
            f'vertical-align:super;letter-spacing:0;">[{s["id"]}]</a>')
body = re.sub(r'〔(\d{2})〕', citation, body)

# Keep comparison tables narrow, with explicit font sizes and no scroll containers.
table_index = 0
def compact_table(match):
    global table_index
    table_index += 1
    table = match[0]
    table = re.sub(r'<table[^>]*>', '<table style="border-collapse:collapse;table-layout:fixed;width:100%;margin:22px 0;font-size:14px;line-height:1.7;letter-spacing:0.2px;word-break:normal;overflow-wrap:anywhere;">', table, count=1)
    table = re.sub(r'<th\b[^>]*>', '<th style="border-bottom:2px solid #E5C4C0;padding:10px 7px;background:#FDF6F5;font-weight:600;text-align:left;color:#B91C1C;font-size:13px;line-height:1.65;vertical-align:top;">', table)
    table = re.sub(r'<td\b[^>]*>', '<td style="border-bottom:1px solid #EAEAEA;padding:11px 7px;text-align:left;font-size:14px;line-height:1.7;color:#333333;vertical-align:top;">', table)
    # Row shading helps scan figures without filling the page with heavy grid lines.
    count = 0
    def stripe(row):
        nonlocal count
        count += 1
        return row[0].replace('<tr>', '<tr style="background:#FAFAFA;">', 1) if count % 2 == 0 else row[0]
    head, rows = table.split('<tbody>', 1)
    table = head + '<tbody>' + re.sub(r'<tr>.*?</tr>', stripe, rows, flags=re.S)
    return table
body = re.sub(r'<table.*?</table>', compact_table, body, flags=re.S)

# A short typographic cover, entirely selectable and copyable into the editor.
header = '''<section style="margin:0 0 30px;padding:24px 0 0;border-top:4px solid #B91C1C;">
<p style="margin:0;font-size:12px;line-height:1.6;letter-spacing:2px;color:#B91C1C;">旁观机器 · MACHINE OBSERVER</p>
<h1 style="font-size:22px;font-weight:700;color:#B91C1C;text-align:center;line-height:1.5;letter-spacing:0.5px;margin:36px 0 30px;">算力生意（上）：<br>英伟达的产品版图</h1>
<p style="margin:0 0 26px;text-align:center;color:#888888;font-size:14px;line-height:1.75;letter-spacing:0.5px;">从个人显卡到机柜系统<br>读懂型号、用途，以及价格的边界</p>
<p style="margin:0;padding:13px 0;border-top:1px solid #EAEAEA;border-bottom:1px solid #EAEAEA;font-size:12px;line-height:1.7;letter-spacing:1px;color:#888888;">资料核查 / 2026.09.12</p>
</section>'''

refs = '<section style="margin:36px 0 14px;padding:18px 16px;background:#FAFAFA;border-top:2px solid #B91C1C;">'
refs += '<p style="margin:0 0 12px;font-size:14px;color:#B91C1C;font-weight:600;letter-spacing:2px;">来源与进一步阅读</p>'
refs += '<p style="margin:0 0 14px;font-size:12px;color:#888888;line-height:1.75;">文内编号可点击查看原始来源。动态网页以实际打开时的信息为准。</p>'
for s in sources:
    refs += (f'<p style="margin:7px 0;font-size:12px;line-height:1.75;letter-spacing:0.2px;color:#777777;">'
             f'{s["id"]} · <a href="{html.escape(s["url"], quote=True)}" '
             f'style="color:#777777;text-decoration:none;border-bottom:1px solid #DDDDDD;">'
             f'{html.escape(s["title"])}</a></p>')
refs += '</section>'
footer = '<p style="margin:28px 0 12px;text-align:center;color:#B91C1C;font-size:12px;line-height:1.7;letter-spacing:2px;">旁观机器 · MACHINE OBSERVER</p>'

container_style = theme['container'] + 'box-sizing:border-box;max-width:640px;margin:0 auto;'
article = f'<section style="{container_style}">\n{header}\n{body}\n{refs}\n{footer}\n</section>'
(HERE / 'article-v1-fragment.html').write_text(article)
document = ('<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(title)}</title></head>'
            '<body style="margin:0;background:#ffffff;padding:24px 0;">'
            f'{article}</body></html>\n')
(HERE / 'article-v1.html').write_text(document)
assert '〔' not in document, 'Unresolved citation'
assert '<style' not in document and '<script' not in document
print(f'Built {chapter.number} sections, {table_index} compact tables, {len(sources)} linked sources.')
