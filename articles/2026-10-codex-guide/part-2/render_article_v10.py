"""Render the article's deliberately limited Markdown to inline-styled HTML."""
from pathlib import Path
import base64
import html
import re

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'article-v10.md'
GREEN = '#17633F'
BASE = "font-size:16px;color:#333333;line-height:1.6;letter-spacing:0.5px;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;word-break:break-word;background:#ffffff;padding:0 12px;box-sizing:border-box;max-width:640px;margin:0 auto;"


def embed(path):
    path = Path(path)
    mime = 'image/png' if path.suffix == '.png' else 'image/jpeg'
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()


def inline(text):
    escaped = html.escape(text, quote=True)
    escaped = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', lambda m:
        '<a href="' + m[2] + '" style="color:#17633F;text-decoration:none;border-bottom:1px solid #C7DDCF;">' + m[1] + '</a>', escaped)
    escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong style="font-weight:700;color:#222222;">\1</strong>', escaped)
    escaped = re.sub(r'`([^`]+)`', r'<span style="font-family:monospace;font-size:15px;color:#17633F;">\1</span>', escaped)
    return escaped


def paragraph(text, quote=False, note=False):
    if quote:
        style = 'margin:7px 0;line-height:1.6;color:#496255;letter-spacing:0.5px;text-align:justify;'
    elif note:
        style = 'margin:12px 0;line-height:1.6;color:#718078;font-size:12px;letter-spacing:0.3px;text-align:justify;'
    else:
        style = 'margin:14px 0;line-height:1.6;color:#333333;letter-spacing:0.5px;text-align:justify;'
    content = inline(text)
    if text.startswith('**'):
        content = content.replace('font-weight:700;color:#222222;', 'font-weight:700;color:#17633F;', 1)
    return '<p style="' + style + '">' + content + '</p>'


lines = SOURCE.read_text().splitlines()
title = lines[0][2:]
parts = ['<section style="' + BASE + '">']
brand = ROOT / 'assets/brand/2026-09-12-header-v2/03-retro-terminal.png'
parts.append('<img src="' + embed(brand) + '" alt="旁观机器：复古电脑公众号首图" style="display:block;width:100%;height:auto;margin:0 0 22px;border-radius:3px;">')
parts.append('<h1 style="font-size:22px;font-weight:700;color:#17633F;text-align:center;margin:26px 0 14px;line-height:1.45;letter-spacing:0.5px;">' + inline(title) + '</h1>')
parts.append('<p style="text-align:center;color:#7A9A8A;font-size:13px;letter-spacing:1px;margin:0 0 25px;">和 Codex 一起工作 · 第二篇</p>')
i = 4
section_number = 0
while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
    if line.startswith('## '):
        section_number += 1
        label = re.sub(r'^[一二三四五六七八九十]+、', '', line[3:])
        parts.append('<section style="margin:34px 0 17px;padding:12px 14px;background:#F2F7F3;border:1px solid #C7DDCF;border-radius:4px;"><div style="display:table;width:100%;border-collapse:collapse;"><div style="display:table-cell;width:43px;vertical-align:middle;color:#17633F;font-size:28px;font-weight:400;line-height:1.2;">' + f'{section_number:02d}' + '</div><div style="display:table-cell;vertical-align:middle;padding-left:12px;border-left:1px solid #B9D2C2;"><h2 style="margin:0;color:#17633F;font-size:18px;font-weight:700;line-height:1.5;letter-spacing:0.5px;">' + inline(label) + '</h2></div></div></section>')
        i += 1
    elif line.startswith('### '):
        parts.append('<h3 style="font-size:17px;font-weight:700;color:#287A51;margin:26px 0 12px;line-height:1.5;letter-spacing:0.5px;">' + inline(line[4:]) + '</h3>')
        i += 1
    elif line.startswith('>'):
        quote_lines = []
        while i < len(lines) and (lines[i].startswith('>') or not lines[i].strip()):
            if lines[i].startswith('>'):
                quote_lines.append(lines[i].lstrip('>').strip() or '\n')
            elif i + 1 >= len(lines) or not lines[i + 1].startswith('>'):
                break
            i += 1
        parts.append('<blockquote style="margin:16px 0;padding:10px 15px;background:#F2F7F3;border-left:3px solid #17633F;border-radius:2px;font-size:15px;">' + ''.join(paragraph(q.strip(), quote=True) for q in ' '.join(quote_lines).split('\n') if q.strip()) + '</blockquote>')
    elif line.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[:\- ]+', c) for c in cells):
                rows.append(cells)
            i += 1
        # Present file descriptions vertically for phone reading.
        parts.append('<section style="margin:17px 0;border:1px solid #D8E5DD;border-radius:4px;background:#FAFAFA;">')
        for n, cells in enumerate(rows[1:]):
            separator = 'border-bottom:1px solid #D8E5DD;' if n < len(rows) - 2 else ''
            parts.append('<section style="padding:13px 15px;' + separator + '"><p style="margin:0 0 6px;color:#17633F;font-size:15px;font-weight:700;line-height:1.5;">' + inline(cells[0]) + '</p><p style="margin:0;color:#333333;font-size:15px;line-height:1.6;letter-spacing:0.5px;">' + inline(cells[1]) + '</p></section>')
        parts.append('</section>')
    elif line.startswith('!['):
        match = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        assert match, line
        image_path = HERE / match[2]
        parts.append('<figure style="margin:20px 0 22px;"><img src="' + embed(image_path) + '" alt="' + html.escape(match[1]) + '" style="display:block;width:100%;height:auto;"><figcaption style="margin:8px 0 0;text-align:center;color:#718078;font-size:12px;line-height:1.5;">本文归纳的协作流程，可从当前需要的环节进入</figcaption></figure>')
        i += 1
    elif line.startswith('旁观机器 ·'):
        i += 1
    elif line == '---':
        parts.append('<hr style="border:0;border-top:1px solid #C7DDCF;margin:27px 0 16px;">')
        i += 1
    else:
        para = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '>', '|', '![')) and lines[i].strip() != '---':
            para.append(lines[i].strip())
            i += 1
        text = ' '.join(para)
        parts.append(paragraph(text, note=text.startswith(('资料说明：', '资料核查日期：'))))

parts.append('<p style="margin:28px 0 10px;text-align:center;color:#17633F;font-size:12px;letter-spacing:2px;">旁观机器 · MACHINE OBSERVER</p></section>')
body = '\n'.join(parts)
(HERE / 'upper/article-v10-body.html').write_text(body)
document = '<!doctype html>\n<html lang="zh-CN">\n<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(title) + '</title></head>\n<body style="margin:0;background:#ffffff;padding:18px 0 30px;">\n' + body + '\n</body>\n</html>\n'
(HERE / 'article-v10.html').write_text(document)
print('Created article-v10.html and upper/article-v10-body.html; embedded brand header image.')
