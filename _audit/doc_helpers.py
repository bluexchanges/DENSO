from pathlib import Path
import re
O=Path(__file__).parent.parent
R=Path('F:/cfg5_mophong')
BASE={'J':R/'local_source_(1)','L':R/'local_source','R':R,'A':O/'_audit','H':Path('C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl')}
def refs(t):
    def f(m):
        tag,path,line=m.groups();p=BASE[tag] if tag=='H' else BASE[tag]/path
        return f'[{tag}/{path or "chat"}:{line}](<{p.as_posix()}:{line}>)'
    return re.sub(r'\[\[([JLRAH]):([^\]]*?):(\d+)\]\]',f,t)
def write(name,t):
    p=O/name
    if p.exists():raise FileExistsError(p)
    p.write_text(refs(t.strip())+'\n',encoding='utf-8')
