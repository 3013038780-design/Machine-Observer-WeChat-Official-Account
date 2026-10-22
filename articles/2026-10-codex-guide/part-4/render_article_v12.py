"""Render the user's approved text using the repository's inline theme."""
from pathlib import Path
import html, json, re

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
for block in blocks:
    if block.startswith('### '):
        tag, text = 'h3', block[4:]
    elif block.startswith('## '):
        tag, text = 'h2', block[3:]
    elif block.startswith('# '):
        tag, text = 'h1', block[2:]
    elif block.startswith('> '):
        parts.append('<blockquote style="' + THEME['blockquote'] + '"><p style="' + THEME['blockquote_p'] + '">' + inline(block[2:]) + '</p></blockquote>')
        continue
    else:
        tag, text = 'p', block
    parts.append('<' + tag + ' style="' + THEME[tag] + '">' + inline(text) + '</' + tag + '>')
parts.append('</section>')
body = '\n'.join(parts)
(HERE / 'article-v12-body.html').write_text(body)
title = blocks[0][2:]
(HERE / 'article-v12.html').write_text('<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(title) + '</title></head><body style="margin:0;padding:0 0 36px;background:#ffffff;">\n' + body + '\n</body></html>\n')
print('Generated article-v12.html and article-v12-body.html')
