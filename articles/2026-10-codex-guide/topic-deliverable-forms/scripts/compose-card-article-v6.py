from pathlib import Path
from collections import Counter
import re,json,hashlib
r=Path(__file__).resolve().parents[1]
s=(r/'article-v5.md').read_text()
source_hash=hashlib.sha256(s.encode()).hexdigest()
old_intro='每组表格留三列：可以拿到什么，具体在哪里用，以及一句可以直接向 AI 提出的要求。左边先认名字，中间看软件、平台和实际文件，右边找一个可以开始的小任务。一行里的不同作品例子不必全部制作，先挑一个就好。'
new_intro='每项成果独立放在一张卡片里：先认名字，再看能做什么、在哪里用、会交付哪些文件，最后是一句可以直接向 AI 提出的要求。同一张卡片里的不同作品例子不必全部制作，先挑一个就好。'
assert old_intro in s
s=s.replace(old_intro,new_intro).replace('表中的软件是一条具体路线','卡片里的软件是一条具体路线').replace('留意自己在哪一行停了下来','留意自己在哪张卡片前停了下来')
records=[];out=[];group=0;heading='';lines=s.splitlines();i=0
special={0:([0,2],[1]),19:([0,2],[1]),20:([0,3],[1,2]),21:([0,1],[2,3]),48:([1],[0]),49:([1,2],[0]),50:([1],[0]),51:([1],[0]),52:([0,2],[1]),53:([0,2,3],[1]),54:([1,2,3],[0])}
def fragments(text):return Counter(t.strip() for t in re.split('[。；]',text) if t.strip())
while i<len(lines):
 line=lines[i]
 if re.match(r'^## [一二三四五六七八九十]+、',line):group+=1;heading=line[3:]
 if not line.startswith('|'):out.append(line);i+=1;continue
 headers=line;assert lines[i+1].startswith('| ---');i+=2
 while i<len(lines) and lines[i].startswith('|'):
  row=[c.strip() for c in lines[i].split('|')[1:-1]];assert len(row)==3
  n=len(records);parts=re.findall(r'[^。]+。?',row[1]);assert len(parts)>=2
  if n in special:
   a,b=special[n];usage=''.join(parts[j] for j in a);delivery=''.join(parts[j] for j in b)
  elif n==37:
   op,sep,files=parts[1].partition('；');assert sep
   usage=parts[0]+op+'。';delivery=files
  elif n==47:
   files,sep,op=parts[1].partition('；');assert sep
   usage=op+parts[2];delivery=parts[0]+files+'。'
  else:usage=parts[0];delivery=''.join(parts[1:])
  assert fragments(row[1])==fragments(usage+delivery),(row[0],row[1],usage,delivery)
  rec={'number':n+1,'group':group,'heading':heading,'name':row[0],'usage':usage,'delivery':delivery,'prompt':row[2],'original':row}
  records.append(rec)
  out.extend([f'### {n+1:02d} {row[0]}','',f'**能做什么 · 在哪里用：** {usage}','',f'**交付内容：** {delivery}','',f'**这样跟 AI 说：** {row[2]}',''])
  i+=1
assert len(records)==58 and group==10
text='\n'.join(out)+'\n'
assert not any(l.startswith('|') for l in text.splitlines())
(r/'article-v6.md').write_text(text)
(r/'assets/cards-v6').mkdir(parents=True,exist_ok=True)
(r/'assets/cards-v6/cards.json').write_text(json.dumps({'date':'2026-10-25','source':'article-v5.md','sourceSha256':source_hash,'cardCount':58,'groupCount':10,'cards':records},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'cards':58,'groups':10,'allOriginalDescriptionsRetained':True,'sourceChars':len(text)},ensure_ascii=False))
