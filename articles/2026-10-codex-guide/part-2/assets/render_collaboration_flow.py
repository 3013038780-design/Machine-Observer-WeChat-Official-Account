"""Render the editorial collaboration diagram to SVG and PNG (no AI generation)."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont
import math

HERE = Path(__file__).resolve().parent
W, H, SCALE = 1000, 1820, 2
GREEN, INK, MUTED = '#17633F', '#263C32', '#64766C'
PALE, LINE, WHITE = '#F2F7F3', '#BBD2C4', '#FFFFFF'
FONT = '/System/Library/Fonts/STHeiti Medium.ttc'
canvas = Image.new('RGB', (W * SCALE, H * SCALE), WHITE)
draw = ImageDraw.Draw(canvas)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="white"/>']

def text(x, y, lines, size=34, color=INK):
    lines = lines.split('\n')
    font = ImageFont.truetype(FONT, size * SCALE)
    step = size * 1.42
    start = y - (len(lines) - 1) * step / 2
    for i, line in enumerate(lines):
        cy = start + i * step
        draw.text((x * SCALE, cy * SCALE), line, fill=color, font=font, anchor='mm')
        svg.append(f'<text x="{x}" y="{cy}" font-family="STHeiti, PingFang SC, sans-serif" font-size="{size}" text-anchor="middle" dominant-baseline="central" fill="{color}">{escape(line)}</text>')

def box(x, y, w, h, fill=PALE, stroke=LINE):
    draw.rounded_rectangle((x*SCALE,y*SCALE,(x+w)*SCALE,(y+h)*SCALE),radius=15*SCALE, fill=fill,outline=stroke,width=2*SCALE)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

def diamond(cx, cy, rx=230, ry=70):
    pts=[(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
    draw.polygon([(x*SCALE,y*SCALE) for x,y in pts],fill=WHITE)
    draw.line([(x*SCALE,y*SCALE) for x,y in pts+[pts[0]]],fill=GREEN,width=3*SCALE)
    svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="white" stroke="{GREEN}" stroke-width="3"/>')

def arrow(points, dashed=False, color=GREEN):
    for a,b in zip(points,points[1:]):
        dist=math.dist(a,b)
        if dashed:
            for t in range(0,int(dist),18):
                u,v=t/dist,min(t+10,dist)/dist
                p=(a[0]+(b[0]-a[0])*u,a[1]+(b[1]-a[1])*u)
                q=(a[0]+(b[0]-a[0])*v,a[1]+(b[1]-a[1])*v)
                draw.line([(p[0]*SCALE,p[1]*SCALE),(q[0]*SCALE,q[1]*SCALE)],fill=color,width=3*SCALE)
        else:
            draw.line([(a[0]*SCALE,a[1]*SCALE),(b[0]*SCALE,b[1]*SCALE)],fill=color,width=3*SCALE)
    a,b=points[-2:]
    ang=math.atan2(b[1]-a[1],b[0]-a[0])
    heads=[b]+[(b[0]-15*math.cos(ang+s),b[1]-15*math.sin(ang+s)) for s in [-0.45,0.45]]
    draw.polygon([(x*SCALE,y*SCALE) for x,y in heads],fill=color)
    dash=' stroke-dasharray="10 8"' if dashed else ''
    svg.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{color}" stroke-width="3"{dash}/><polygon points="{" ".join(f"{x},{y}" for x,y in heads)}" fill="{color}"/>')

text(500,65,'一轮人机协作怎样推进',43,GREEN)
text(500,117,'根据当前困难进入；用实际结果决定下一步',25,MUTED)
box(180,165,540,110)
text(450,220,'① 查看材料\n建立当前理解')
arrow([(450,275),(450,320)])
diamond(450,390)
text(450,390,'信息足够\n推进下一步？',31)
arrow([(450,460),(450,520)])
text(485,488,'是',26,GREEN)
box(180,520,540,120)
text(450,580,'③ 明确本轮成果\n标准与分工')
arrow([(680,390),(870,390),(870,450)])
text(805,365,'否',26,GREEN)
box(760,450,220,185)
text(870,540,'② 补关键缺口\n解释 · 调查\n比较 · 试验',26)
arrow([(870,635),(870,680),(740,680),(740,285),(450,285),(450,320)],True)
text(867,706,'补足后再判断',22,MUTED)
arrow([(450,640),(450,725)])
box(180,725,540,115)
text(450,782,'④ 执行工作\n取得检查证据')
arrow([(450,840),(450,895)])
diamond(450,965)
text(450,965,'结果满足\n本轮目标？',31)
arrow([(450,1035),(450,1135)])
text(485,1080,'是',26,GREEN)
box(180,1135,540,120)
text(450,1195,'⑤ 记录成果、证据\n未解决项与下一步')
arrow([(680,965),(870,965),(870,1045)])
text(745,940,'否',26,GREEN)
box(760,1045,220,300)
text(870,1195,'先诊断偏差\n目标问题 → ①\n方法问题 → ③\n实现错误 → ④',24)
text(870,1390,'按原因回到\n相应步骤',24,MUTED)
arrow([(450,1255),(450,1335)])
diamond(450,1405)
text(450,1405,'继续\n下一轮？',31)
arrow([(450,1475),(450,1560)])
text(485,1515,'否',26,GREEN)
box(260,1560,380,85,fill=GREEN,stroke=GREEN)
text(450,1602,'结束当前工作',34,WHITE)
arrow([(220,1405),(95,1405),(95,220),(180,220)],True)
text(144,1380,'是',26,GREEN)
text(500,1710,'当前信息够用就推进，无需一次消除全部未知。',26,MUTED)
text(500,1760,'原创编辑归纳 · 旁观机器',23,MUTED)
svg.append('</svg>')
(HERE/'collaboration-flow-v1.svg').write_text('\n'.join(svg),encoding='utf-8')
canvas.save(HERE/'collaboration-flow-v1.png')
print(f'Rendered {W*SCALE} × {H*SCALE} PNG and editable SVG.')
