#!/usr/bin/env python3
"""
Markdown -> 微信公众号可用 HTML（全部内联样式）。

微信编辑器会剥离 class 和 <style>，只保留标签上的 style="" 内联样式。
本脚本零第三方依赖：自带一个覆盖公众号常用语法的轻量 Markdown 解析器，
再按 assets/theme.json 把样式内联进每个标签。

用法:
    python3 render.py input.md [-o output.html] [-t theme.json]

输出的 HTML 直接复制粘贴进公众号编辑器即可，也可交给 publish.py 发草稿。
"""
import argparse
import html
import json
import os
import re
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_THEME = os.path.join(SKILL_DIR, "assets", "theme.json")


def load_theme(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def sty(theme, key):
    v = theme.get(key, "")
    return f' style="{v}"' if v else ""


# ---------- 行内语法 ----------
def inline(text, theme):
    placeholders = []

    def stash(html_frag):
        placeholders.append(html_frag)
        return f"\x00{len(placeholders)-1}\x00"

    # 1. 行内代码 `code`（先抽出，避免内部被其它规则破坏）
    def repl_code(m):
        return stash(f'<code{sty(theme,"code_inline")}>'
                     f'{html.escape(m.group(1))}</code>')
    text = re.sub(r"`([^`]+?)`", repl_code, text)

    # 转义其余文本
    text = html.escape(text, quote=False)

    # 2. 行内图片 ![alt](url)（独立成行的图片在块级处理，带图注）
    def repl_img(m):
        alt = m.group(1).strip()
        return stash(f'<img src="{m.group(2).strip()}" alt="{alt}"'
                     f'{sty(theme,"img")}/>')
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl_img, text)

    # 3. 链接 [text](url)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{m.group(2).strip()}"{sty(theme,"a")}>'
                  f'{m.group(1)}</a>',
        text,
    )
    # 4. 加粗
    text = re.sub(r"\*\*(.+?)\*\*",
                  lambda m: f'<strong{sty(theme,"strong")}>{m.group(1)}'
                            f'</strong>', text)
    text = re.sub(r"__(.+?)__",
                  lambda m: f'<strong{sty(theme,"strong")}>{m.group(1)}'
                            f'</strong>', text)
    # 5. 斜体
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)",
                  lambda m: f'<em{sty(theme,"em")}>{m.group(1)}</em>', text)
    text = re.sub(r"(?<!_)_(?!_)(.+?)(?<!_)_(?!_)",
                  lambda m: f'<em{sty(theme,"em")}>{m.group(1)}</em>', text)

    # 还原行内代码/图片占位
    for i, frag in enumerate(placeholders):
        text = text.replace(f"\x00{i}\x00", frag)
    return text


# ---------- 块级语法 ----------
def render(md, theme):
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    i = 0
    n = len(lines)

    def flush_para(buf):
        if buf:
            txt = inline(" ".join(b.strip() for b in buf), theme)
            out.append(f'<p{sty(theme,"p")}>{txt}</p>')

    para = []
    while i < n:
        line = lines[i]

        # 原始 HTML 块透传：以 <section/<div/<table/<figure/<aside 等块级标签开头的连续行
        # 直到遇到空行为止，整段不转义、原样输出。
        # 用于在 markdown 中嵌入手写装饰块（公众号需要的内联样式 div 卡片等）。
        if re.match(r"^\s*<(section|div|table|figure|aside|nav|header|footer|hr|p\s)", line):
            flush_para(para); para = []
            html_block = [line]
            i += 1
            while i < n and lines[i].strip() != "":
                html_block.append(lines[i])
                i += 1
            out.append("\n".join(html_block))
            continue

        # 围栏代码块 ```
        m = re.match(r"^\s*```", line)
        if m:
            flush_para(para); para = []
            code = []
            i += 1
            while i < n and not re.match(r"^\s*```", lines[i]):
                code.append(lines[i]); i += 1
            i += 1  # 跳过结束 ```
            body = html.escape("\n".join(code))
            out.append(f'<pre{sty(theme,"pre")}>'
                       f'<code{sty(theme,"pre_code")}>{body}</code></pre>')
            continue

        # 空行 -> 段落分隔
        if line.strip() == "":
            flush_para(para); para = []
            i += 1
            continue

        # 标题
        h = re.match(r"^(#{1,4})\s+(.*)$", line)
        if h:
            flush_para(para); para = []
            lvl = len(h.group(1))
            tag = f"h{lvl}"
            inner = inline(h.group(2).strip(), theme)
            # h2 用 display:inline-block，外面包 p 以保证换行表现稳定
            if lvl == 2:
                out.append(f'<p style="margin:0;"><{tag}{sty(theme,tag)}>'
                           f'{inner}</{tag}></p>')
            else:
                out.append(f'<{tag}{sty(theme,tag)}>{inner}</{tag}>')
            i += 1
            continue

        # 分割线
        if re.match(r"^\s*([-*_])\s*(\1\s*){2,}$", line):
            flush_para(para); para = []
            out.append(f'<hr{sty(theme,"hr")}/>')
            i += 1
            continue

        # 引用块
        if re.match(r"^\s*>", line):
            flush_para(para); para = []
            quote = []
            while i < n and re.match(r"^\s*>", lines[i]):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            # 引用内部按段落处理
            inner_html = []
            qbuf = []
            for q in quote + [""]:
                if q.strip() == "":
                    if qbuf:
                        inner_html.append(
                            f'<p{sty(theme,"blockquote_p")}>'
                            f'{inline(" ".join(qbuf), theme)}</p>')
                        qbuf = []
                else:
                    qbuf.append(q.strip())
            out.append(f'<blockquote{sty(theme,"blockquote")}>'
                       f'{"".join(inner_html)}</blockquote>')
            continue

        # 表格
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?\s*:?-{2,}", lines[i + 1].replace(" ", "")):
            flush_para(para); para = []
            def cells(row):
                row = row.strip()
                row = row[1:] if row.startswith("|") else row
                row = row[:-1] if row.endswith("|") else row
                return [c.strip() for c in row.split("|")]
            header = cells(line)
            i += 2  # 跳过表头与分隔行
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(cells(lines[i])); i += 1
            thtml = "".join(
                f'<th{sty(theme,"th")}>{inline(c, theme)}</th>' for c in header)
            body = ""
            for r in rows:
                tds = "".join(
                    f'<td{sty(theme,"td")}>{inline(c, theme)}</td>' for c in r)
                body += f"<tr>{tds}</tr>"
            out.append(f'<table{sty(theme,"table")}><thead><tr>{thtml}'
                       f'</tr></thead><tbody>{body}</tbody></table>')
            continue

        # 列表（无序/有序，支持一层缩进嵌套）
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            flush_para(para); para = []
            html_list = parse_list(lines, i, theme)
            out.append(html_list[0])
            i = html_list[1]
            continue

        # 独立成行的图片 -> 块级，带图注，不包 <p>
        im = re.match(r"^\s*!\[([^\]]*)\]\(([^)]+)\)\s*$", line)
        if im:
            flush_para(para); para = []
            alt = im.group(1).strip()
            cap = (f'<p{sty(theme,"img_caption")}>{alt}</p>'
                   if alt else "")
            out.append(f'<img src="{im.group(2).strip()}" alt="{alt}"'
                       f'{sty(theme,"img")}/>{cap}')
            i += 1
            continue

        # 普通段落行
        para.append(line)
        i += 1

    flush_para(para)
    return "\n".join(out)


def parse_list(lines, start, theme, base_indent=0):
    """返回 (html, next_index)。支持一层子列表。"""
    n = len(lines)
    i = start
    items = []
    ordered = None
    while i < n:
        line = lines[i]
        if line.strip() == "":
            # 列表内空行：仅当下一项是【同缩进且同有序性】才视为同一列表续接，
            # 否则结束本列表（避免无序列表吞掉随后的有序列表）。
            nxt = lines[i + 1] if i + 1 < n else ""
            nm = re.match(r"^(\s*)([-*+]|\d+\.)\s+", nxt)
            if nm and len(nm.group(1)) == base_indent and ordered is not None \
                    and bool(re.match(r"\d+\.", nm.group(2))) == ordered:
                i += 1
                continue
            break
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if not m:
            break
        indent = len(m.group(1))
        if indent < base_indent:
            break
        if indent > base_indent:
            # 子列表：附加到上一个 li
            sub_html, i = parse_list(lines, i, theme, indent)
            if items:
                items[-1] += sub_html
            continue
        is_ordered = bool(re.match(r"\d+\.", m.group(2)))
        if ordered is None:
            ordered = is_ordered
        items.append(f'<li{sty(theme,"li")}>'
                     f'{inline(m.group(3).strip(), theme)}')
        i += 1
    tag = "ol" if ordered else "ul"
    lis = "".join(it + "</li>" for it in items)
    return (f'<{tag}{sty(theme,tag)}>{lis}</{tag}>', i)


def main():
    ap = argparse.ArgumentParser(description="Markdown -> 公众号内联样式 HTML")
    ap.add_argument("input", help="输入 .md 文件")
    ap.add_argument("-o", "--output", help="输出 .html（默认同名 .html）")
    ap.add_argument("-t", "--theme", default=DEFAULT_THEME,
                    help="主题 json，默认 assets/theme.json")
    ap.add_argument("--fragment", action="store_true",
                    help="只输出正文片段，不加最外层容器/html骨架")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        md = f.read()
    theme = load_theme(args.theme)

    body = render(md, theme)
    container = (f'<section{sty(theme,"container")}>\n{body}\n</section>')

    if args.fragment:
        result = body
    else:
        result = container

    out = args.output or os.path.splitext(args.input)[0] + ".html"
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"✅ 已生成: {out}")
    print("   预览: 浏览器打开该文件；发布: 复制全文粘贴进公众号编辑器，")
    print("   或运行 scripts/publish.py 推送到草稿箱。")


if __name__ == "__main__":
    main()
