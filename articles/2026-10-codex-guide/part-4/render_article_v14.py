"""Render using part 3 final v9 heading cards and brand signature."""
from pathlib import Path
import base64, html, json, re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
THEME = json.loads((ROOT / 'assets/theme.json').read_text())
SOURCE = HERE / 'article-v12.md'

def inline(text):
    text = html.escape(html.unescape(text), quote=True)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', lambda m: '<a href="' + m[2] + '" style="' + THEME['a'] + '">' + m[1] + '</a>', text)
    return re.sub(r'\*\*(.+?)\*\*', lambda m: '<strong style="' + THEME['strong'] + '">' + m[1] + '</strong>', text)

blocks = SOURCE.read_text().strip().split('\n\n')
parts = ['<section style="' + THEME['container'] + 'max-width:640px;margin:0 auto;box-sizing:border-box;">']
brand = ROOT / 'assets/brand/2026-09-12-header-v2/03-retro-terminal.png'
data = 'data:image/png;base64,' + base64.b64encode(brand.read_bytes()).decode()
parts.append('<img src="' + data + '" alt="旁观机器：复古电脑公众号首图" style="display:block;width:100%;height:auto;margin:0 0 22px;border-radius:3px;">')
section_number = 0
for block in blocks:
    if block.startswith('### '):
        parts.append('<h3 style="font-size:17px;font-weight:700;color:#287A51;margin:26px 0 12px;line-height:1.5;letter-spacing:0.5px;">' + inline(block[4:]) + '</h3>')
        continue
    elif block.startswith('## '):
        section_number += 1
        label = re.sub(r'^[一二三]、', '', block[3:])
        parts.append('<section style="margin:34px 0 17px;padding:12px 14px;background:#F2F7F3;border:1px solid #C7DDCF;border-radius:4px;"><div style="display:table;width:100%;border-collapse:collapse;"><div style="display:table-cell;width:43px;vertical-align:middle;color:#17633F;font-size:28px;font-weight:400;line-height:1.2;">' + f'{section_number:02d}' + '</div><div style="display:table-cell;vertical-align:middle;padding-left:12px;border-left:1px solid #B9D2C2;"><h2 style="margin:0;color:#17633F;font-size:18px;font-weight:700;line-height:1.5;letter-spacing:0.5px;">' + inline(label) + '</h2></div></div></section>')
        continue
    elif block.startswith('# '):
        parts.append('<h1 style="font-size:22px;font-weight:700;color:#17633F;text-align:center;margin:26px 0 14px;line-height:1.45;letter-spacing:0.5px;">' + inline(block[2:]) + '</h1>')
        parts.append('<p style="text-align:center;color:#7A9A8A;font-size:13px;letter-spacing:1px;margin:0 0 25px;">和 Codex 一起工作 · 第四篇</p>')
        continue
    elif block.startswith('> '):
        parts.append('<blockquote style="' + THEME['blockquote'] + '"><p style="' + THEME['blockquote_p'] + '">' + inline(block[2:]) + '</p></blockquote>')
        continue
    else:
        tag, text = 'p', block
    parts.append('<' + tag + ' style="' + THEME[tag] + '">' + inline(text) + '</' + tag + '>')
parts.append('<p style="margin:28px 0 10px;text-align:center;color:#17633F;font-size:12px;letter-spacing:2px;">旁观机器 · MACHINE OBSERVER</p></section>')
body = '\n'.join(parts)
(HERE / 'article-v14-body.html').write_text(body)
title = blocks[0][2:]
(HERE / 'article-v14.html').write_text('<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(title) + '</title></head><body style="margin:0;background:#fff;padding:18px 0 30px;">\n' + body + '\n</body></html>\n')
print('Generated article-v14.html and article-v14-body.html')
