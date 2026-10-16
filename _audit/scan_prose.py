from pathlib import Path
from collections import Counter
import re
o=Path(__file__).parent.parent
c=Counter()
for p in o.glob('*.md'):
 if int(p.name[:2])<4:continue
 t=p.read_text(encoding='utf-8')
 t=re.sub(r'```[\s\S]*?```|`[^`\n]+`|\[[^\]]*\]\(<[^>]+>\)|\[[^\]]*\]\(https?://[^\s]*?\)|https?://[^\s]+','',t)
 c.update(re.findall(r'\b[A-Za-z][A-Za-z0-9]{7,}\b',t))
print('\n'.join(f'{w}: {n}' for w,n in c.most_common()))
