from pathlib import Path
import re,json
o=Path(__file__).parent.parent
j=json.loads((o/'_audit/readability_preview.json').read_text(encoding='utf-8'))
print('SUSPECT SPLITS')
for r in j['changes']:
 t=r['to']
 if re.search(r'(?:^| )(?:[a-z]{1,2})(?: |$)',t) and not re.search(r'\b(?:mm|rad|val|IL|RL)\b',t):print(r['from'],'=>',t)
print('REMAINING SHORT COMBINED WORDS')
for p in o.glob('*.md'):
 if int(p.name[:2])<4:continue
 t=p.read_text(encoding='utf-8')
 t=re.sub(r'```[\s\S]*?```|`[^`\n]+`|\[[^\]]*\]\(<[^>]+>\)|\[[^\]]*\]\(https?://[^\s]*?\)|https?://[^\s]+','',t)
 ws=sorted(set(w for w in re.findall(r'[^\W_]+',t) if len(w)>=4 and any(ord(ch)>127 for ch in w) and (re.match(r'^(trong|chưa|không|của|đã|và|có|nếu|theo|suy|đổi|ở|là|chỉ|để|chờ|như|ghi|một|hai|bằng|đơn|dung)',w) and w not in {'trong','không','theo','như','chỉ','chờ'})))
 print(p.name,ws)
