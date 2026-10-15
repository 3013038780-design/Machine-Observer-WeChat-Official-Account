"""Render part 3 Markdown into self-contained inline-styled HTML."""
from pathlib import Path
import base64, html, re

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "article-v6.md"
BASE = "font-size:16px;color:#333333;line-height:1.6;letter-spacing:0.5px;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;word-break:break-word;background:#ffffff;padding:0 12px;box-sizing:border-box;max-width:640px;margin:0 auto;"

def inline(text):
    escaped = html.escape(text, quote=True)
    escaped = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" style="color:#17633F;text-decoration:none;border-bottom:1px solid #C7DDCF;">\1</a>', escaped)
    escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong style="font-weight:700;color:#17633F;">\1</strong>', escaped)
    escaped = re.sub(r'(?<!\\w)\\b(AGENTS\\.md|PLANS\\.md|GOALS\\.md|build-log\\.md)\\b', r'<span style="font-family:monospace;font-size:14px;color:#17633F;">\1</span>', escaped)
    return escaped

def p(text, quote=False, note=False):
    if quote:
        style = 'margin:7px 0;line-height:1.6;color:#496255;letter-spacing:0.5px;text-align:justify;'
    elif note:
        style = 'margin:12px 0;line-height:1.6;color:#718078;font-size:12px;letter-spacing:0.3px;text-align:justify;'
    else:
        style = 'margin:14px 0;line-height:1.6;color:#333333;letter-spacing:0.5px;text-align:justify;'
    return '<p style="' + style + '">' + inline(text) + '</p>'

lines = SOURCE.read_text().splitlines()
title = lines[0][2:]
parts = ['<section style="' + BASE + '">']
brand = ROOT / "assets/brand/2026-09-12-header-v2/03-retro-terminal.png"
data = 'data:image/png;base64,' + base64.b64encode(brand.read_bytes()).decode()
parts.append('<img src="' + data + '" alt="旁观机器：复古电脑公众号首图" style="display:block;width:100%;height:auto;margin:0 0 22px;border-radius:3px;">')
parts.append('<h1 style="font-size:22px;font-weight:700;color:#17633F;text-align:center;margin:26px 0 14px;line-height:1.45;letter-spacing:0.5px;">' + inline(title) + '</h1>')
parts.append('<p style="text-align:center;color:#7A9A8A;font-size:13px;letter-spacing:1px;margin:0 0 25px;">和 Codex 一起工作 · 第三篇</p>')

i = 3
section_number = 0
while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
    if line.startswith("```"):
        code_lines = []
        i += 1
        while i < len(lines) and not lines[i].strip().startswith("```"):
            code_lines.append(lines[i])
            i += 1
        assert i < len(lines), "Unclosed code fence"
        i += 1
        parts.append('<pre style="margin:18px 0;padding:12px;background:#F2F7F3;border:1px solid #D8E5DD;white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px;line-height:1.65;color:#24533B;"><code style="font-family:Menlo,Consolas,monospace;">' + html.escape(chr(10).join(code_lines)) + '</code></pre>')
        continue
    if line.startswith("## "):
        section_number += 1
        label = re.sub(r'^\d+\s+', '', line[3:])
        parts.append('<section style="margin:34px 0 17px;padding:12px 14px;background:#F2F7F3;border:1px solid #C7DDCF;border-radius:4px;"><div style="display:table;width:100%;border-collapse:collapse;"><div style="display:table-cell;width:43px;vertical-align:middle;color:#17633F;font-size:28px;font-weight:400;line-height:1.2;">' + f'{section_number:02d}' + '</div><div style="display:table-cell;vertical-align:middle;padding-left:12px;border-left:1px solid #B9D2C2;"><h2 style="margin:0;color:#17633F;font-size:18px;font-weight:700;line-height:1.5;letter-spacing:0.5px;">' + inline(label) + '</h2></div></div></section>')
        i += 1
        continue
    if line.startswith("### "):
        parts.append('<h3 style="font-size:17px;font-weight:700;color:#287A51;margin:26px 0 12px;line-height:1.5;letter-spacing:0.5px;">' + inline(line[4:]) + '</h3>')
        i += 1
        continue
    if line.startswith(">"):
        quotes = []
        while i < len(lines) and lines[i].strip().startswith(">"):
            quotes.append(lines[i].strip()[1:].strip())
            i += 1
        parts.append('<blockquote style="margin:16px 0;padding:10px 15px;background:#F2F7F3;border-left:3px solid #17633F;border-radius:2px;font-size:15px;">' + ''.join(p(q, quote=True) for q in quotes) + '</blockquote>')
        continue
    if line.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not all(re.fullmatch(r"[:\- ]+", c) for c in cells):
                rows.append(cells)
            i += 1
        parts.append('<section style="margin:17px 0;border:1px solid #D8E5DD;border-radius:4px;background:#FAFAFA;">')
        for n, cells in enumerate(rows[1:]):
            border = "border-bottom:1px solid #D8E5DD;" if n < len(rows[1:]) - 1 else ""
            parts.append('<section style="padding:13px 15px;' + border + '"><p style="margin:0 0 6px;color:#17633F;font-size:15px;font-weight:700;line-height:1.5;">' + inline(cells[0]) + '</p><p style="margin:0;color:#333;font-size:15px;line-height:1.6;letter-spacing:0.5px;">' + inline(cells[1]) + '</p></section>')
        parts.append('</section>')
        continue
    if line.startswith("旁观机器 ·"):
        i += 1
        continue
    if line == "---":
        parts.append('<hr style="border:0;border-top:1px solid #C7DDCF;margin:27px 0 16px;">')
        i += 1
        continue
    if line.startswith("- ") or re.match(r"^\d+\. ", line):
        ordered = bool(re.match(r"^\d+\. ", line))
        items = []
        while i < len(lines):
            current = lines[i].strip()
            if ordered and not re.match(r"^\d+\. ", current):
                break
            if not ordered and not current.startswith("- "):
                break
            items.append(re.sub(r"^(?:- |\d+\. )", "", current))
            i += 1
        tag = "ol" if ordered else "ul"
        parts.append('<' + tag + ' style="margin:16px 0;padding-left:24px;color:#333;">' + ''.join('<li style="margin:8px 0;line-height:1.6;letter-spacing:0.5px;">' + inline(x) + '</li>' for x in items) + '</' + tag + '>')
        continue
    para = []
    while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", ">", "|", "- ", "```")) and not re.match(r"^\d+\. ", lines[i].strip()) and lines[i].strip() != "---":
        para.append(lines[i].strip())
        i += 1
    assert para, f"Unsupported Markdown at line {i + 1}"
    text = " ".join(para)
    parts.append(p(text, note=text.startswith("资料核查日期")))

parts.append('<p style="margin:28px 0 10px;text-align:center;color:#17633F;font-size:12px;letter-spacing:2px;">旁观机器 · MACHINE OBSERVER</p></section>')
body = "\n".join(parts)
(HERE / "upper").mkdir(exist_ok=True)
(HERE / "upper/article-v6-body.html").write_text(body)
doc = '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(title) + '</title></head><body style="margin:0;background:#fff;padding:18px 0 30px;">' + body + '</body></html>'
(HERE / "article-v6.html").write_text(doc)
print("created article-v6.html and upper/article-v6-body.html")
