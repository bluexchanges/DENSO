from pathlib import Path
import json,re,hashlib,collections
from PIL import Image,ImageOps,ImageDraw
OUT=Path(__file__).parent
root=Path('F:/cfg5_mophong')
skip={'.git','.venv','.venv-data','__pycache__','RH20T_cfg5','node_modules','assets','training_data','missing_data','robot_missing_data','site-packages'}
files=[]
def walk(p):
    try: children=list(p.iterdir())
    except (OSError,PermissionError):return
    for f in children:
        if f.name in skip:continue
        if f.is_dir():walk(f)
        else:
            files.append({'path':str(f),'bytes':f.stat().st_size})
walk(root)
(OUT/'repo_inventory.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf-8')
selected=[r for r in files if any(t in r['path'] for t in ['history.json','rollout_report','context.json','normalization.json','selection.json','summary.json'])]
(OUT/'artifact_index.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf-8')
source=Path('C:/Users/ADMIN/.codex/sessions/2026/09/30/rollout-2026-09-30T07-53-20-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6.jsonl')
msgs=[]
for n,line in enumerate(source.open(encoding='utf-8'),1):
    o=json.loads(line);p=o.get('payload',{})
    if o.get('type')=='response_item' and p.get('type')=='message' and p.get('role') in ('user','assistant'):
        t='\n'.join(x.get('text','') for x in p.get('content',[]) if x.get('type') in ('input_text','output_text'))
        if t.startswith('<environment_context>') or t.startswith('# AGENTS.md instructions'):continue
        msgs.append({'source':str(source),'line':n,'timestamp':o.get('timestamp'),'role':p['role'],'text':t})
(OUT/'primary_chat_messages.json').write_text(json.dumps(msgs,ensure_ascii=False,indent=2),encoding='utf-8')
print('INVENTORY_FILES',len(files),'PRIMARY_MESSAGES',len(msgs))
for m in msgs:
    if m['role']!='user':continue
    t=m['text']
    if not re.search(r'MCR_CACHE_READY|MCR_CACHE_SPLITS|MCR_TRAIN|epoch.?25|overfit|1000|1.000|bs256|val_loss|train_loss|EPOCH.*loss|Train.*Loss',t,re.I):continue
    if len(t)>20000:continue
    print('\nCHAT',m['timestamp'],f'line={m["line"]}')
    print(t[:2200])
imgs=list((OUT/'slide_renders').glob('*.PNG'))+list((OUT/'slide_renders').glob('*.png'))
imgs={int(re.search(r'(\d+)$',p.stem)[1]):p for p in imgs}
for group in range(3):
    keys=sorted(imgs)[group*16:(group+1)*16]
    if not keys:continue
    sheet=Image.new('RGB',(1280,4*202),'#ddd')
    d=ImageDraw.Draw(sheet)
    for k,i in enumerate(keys):
        im=Image.open(imgs[i]);im.thumbnail((320,180))
        x=(k%4)*320;y=(k//4)*202
        sheet.paste(im,(x,y+22));d.text((x+8,y+4),str(i),fill='black')
    sheet.save(OUT/f'contact_{group+1}.jpg')
protected=[]
for f in [Path('F:/Denso/Denso-Hack_Presentation-EDABK_TriH.pptx'),root/'server_train_mcr_current.py',root/'local_source/docs/DECISIONS.md']:
    protected.append({'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(OUT/'protected_hashes.json').write_text(json.dumps(protected,indent=2),encoding='utf-8')
