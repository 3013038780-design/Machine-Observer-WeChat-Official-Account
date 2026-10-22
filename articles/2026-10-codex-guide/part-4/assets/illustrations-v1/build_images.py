from pathlib import Path
P=Path(__file__).resolve().parent
GREEN='#17633F'; INK='#204C38'; PALE='#E7F0E9'; MUTED='#86A492'
def svg(content):
 return '<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="600" viewBox="0 0 1080 600"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="#86A492"/></marker></defs><rect width="1080" height="600" rx="24" fill="#F2F7F3"/>'+content+'</svg>'
def text(x,y,t,size=28,color=INK):
 return f'<text x="{x}" y="{y}" text-anchor="middle" fill="{color}" font-size="{size}" font-weight="500" font-family="PingFang SC,Microsoft YaHei,sans-serif">{t}</text>'
def path(d,color=GREEN,width=5,extra=''):
 return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def card(x,y,w,h):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="white" stroke="#C7DDCF" stroke-width="2"/>'
def doc(x,y,scale=1):
 return f'<g transform="translate({x} {y}) scale({scale})"><rect width="76" height="94" rx="7" fill="white" stroke="#17633F" stroke-width="4"/>'+path('M18 24H57M18 43H57M18 62H45',width=4)+'</g>'
# Context: three known inputs enter one task. Abstract representations, not a brain map.
s=''
for x,label in [(90,'用途'),(420,'资料'),(750,'限制')]:
 s+=card(x,58,240,166)
 if label=='用途':
  s+='<circle cx="210" cy="125" r="38" fill="none" stroke="#17633F" stroke-width="4"/><circle cx="210" cy="125" r="22" fill="none" stroke="#86A492" stroke-width="4"/>'+path('M210 125L249 88M231 88H249V106',width=4)
 elif label=='资料':
  s+=doc(511,86,.8)
 else:
  s+=path('M823 104H917M823 133H917M823 161H917',width=4)+'<circle cx="850" cy="104" r="8" fill="#17633F"/><circle cx="890" cy="133" r="8" fill="#17633F"/><circle cx="862" cy="161" r="8" fill="#17633F"/>'
 s+=text(x+120,205,label,40)
 s+=path(f'M{x+120} 242V277Q{x+120} 300 {x+(145 if x==90 else 95)} 300H540V337',MUTED,3,'marker-end="url(#arrow)"') if x!=420 else path('M540 242V337',MUTED,3,'marker-end="url(#arrow)"')
s+=card(340,357,400,168)
s+='<rect x="380" y="395" width="70" height="80" rx="12" fill="#E7F0E9"/>'+path('M395 422H435M395 438H430M395 454H422',width=3)
s+=text(582,424,'同一项任务',40)+text(582,465,'带着背景去判断',32,'#6E8778')
(P/'01-context.svg').write_text(svg(s))
# Loop: model judgment -> execution -> returned evidence; observed info goes back.
s=''
for x,label in [(90,'判断'),(420,'执行'),(750,'返回')]:
 s+=card(x,125,240,245)+text(x+120,338,label,42)
 if label=='判断':
  s+='<rect x="158" y="178" width="104" height="91" rx="14" fill="#E7F0E9"/>'
  for dx,dy in [(180,201),(210,201),(240,201),(180,230),(210,230),(240,230)]:s+=f'<circle cx="{dx}" cy="{dy}" r="5" fill="#17633F"/>'
  s+=path('M175 281H245',width=4)
 elif label=='执行':
  s+='<rect x="483" y="176" width="114" height="98" rx="12" fill="#17633F"/>'+path('M505 201L522 218L505 235M539 237H571',color='#F2F7F3',width=5)
 else:s+=doc(832,180,.95)
for x in [345,675]:s+=path(f'M{x} 247H{x+60}',MUTED,4,'marker-end="url(#arrow)"')
s+=path('M870 393V431Q870 456 845 456H235Q210 456 210 431V393',MUTED,4,'marker-end="url(#arrow)"')
s+=text(540,510,'新结果，带来下一轮判断',36,'#6E8778')
(P/'02-action-loop.svg').write_text(svg(s))
# Visible evidence around opaque learned decision process; no claimed internal architecture.
s=card(65,100,330,396)+text(230,455,'动作可查',40)
s+=doc(126,155,.95)+doc(240,189,.95)
s+=path('M136 309L155 328L186 291M244 342L263 361L294 324',width=5)
s+=path('M429 299H505',MUTED,3, 'stroke-dasharray="6 9"')
s+='<rect x="553" y="100" width="462" height="396" rx="22" fill="#183D2D"/>'
# Layered silhouettes deliberately abstract.
for x,y,r,op in [(635,180,35,.12),(735,194,19,.18),(854,172,43,.09),(927,239,24,.17),(663,303,44,.10),(792,278,52,.09),(880,346,39,.11),(741,358,22,.15)]:
 s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#A9C4AE" opacity="{op}"/>'
s+=text(784,305,'?',110,'#BCD1C0')+text(784,455,'内因仍有未知',40,'#E2EEE5')
(P/'03-blackbox.svg').write_text(svg(s))
print('Built three editable SVG illustrations')
