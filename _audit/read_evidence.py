from pathlib import Path
import sys,json,re
base=Path('F:/cfg5_mophong')
if sys.argv[1]=='read':
    for spec in sys.argv[2:]:
        name,_,span=spec.partition('::');p=base/name
        print('\nFILE',p)
        if not p.exists(): print('MISSING');continue
        lines=p.read_text(encoding='utf-8-sig',errors='replace').splitlines()
        a,b=map(int,span.split('-')) if span else (1,len(lines))
        for n in range(a,min(b,len(lines))+1):print(f'{n}: {lines[n-1]}')
elif sys.argv[1]=='history':
    pat=re.compile(sys.argv[2],re.I)
    hits=json.loads((Path(__file__).parent/'history_hits.json').read_text(encoding='utf-8'))
    for h in hits:
        if 'cfg5' not in h['cwd'].lower() and 'New project' not in h['cwd']: continue
        if h['role']=='user' and pat.search(h['text']):
            print('\nHISTORY',h['file'],h['line'],h['time'],h['role'])
            t=h['text'];m=pat.search(t);print(t[max(0,m.start()-250):m.start()+1800])
elif sys.argv[1]=='json':
    for name in sys.argv[2:]:
        p=base/name;v=json.loads(p.read_text(encoding='utf-8-sig'));print('\nFILE',p)
        if isinstance(v,list): print('LEN',len(v));print(json.dumps(v[:1]+v[-2:],ensure_ascii=False,indent=2)[:8000])
        else: print(json.dumps(v,ensure_ascii=False,indent=2)[:12000])
