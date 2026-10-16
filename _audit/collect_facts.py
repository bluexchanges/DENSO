from pathlib import Path
import json,re,sys,collections
import numpy as np
OUT=Path(__file__).parent
files=[Path('C:/Users/ADMIN/.codex/sessions/2026/09/30/rollout-2026-09-30T07-53-20-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6.jsonl'),Path('C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl')]
messages=[]
for f in files:
    for n,line in enumerate(f.open(encoding='utf-8'),1):
        o=json.loads(line);p=o.get('payload',{})
        if o.get('type')=='response_item' and p.get('type')=='message' and p.get('role') in ('user','assistant'):
            t='\n'.join(c.get('text','') for c in p.get('content',[]) if c.get('type') in ('input_text','output_text'))
            if t.startswith('<environment_context>') or '# AGENTS.md instructions' in t:continue
            messages.append({'file':str(f),'line':n,'timestamp':o.get('timestamp'),'role':p['role'],'text':t})
(OUT/'verified_chat_messages.json').write_text(json.dumps(messages,ensure_ascii=False,indent=2),encoding='utf-8')
for m in messages:
    t=m['text']
    if m['role']=='user' and re.search(r'1000|1.000|MCR_CACHE_READY|MCR_CACHE_SPLITS|epoch.?25|cfg5_joint_mcr_bs256|overfit|FK.*17|17.*FK',t,re.I) and len(t)<18000:
        print('\nSOURCE',m['file'],':',m['line'],m['timestamp'])
        print(t[:2100])
root=Path('F:/cfg5_mophong')
probe=root/'epoch5_transfer_probe_14120/report.json';j=json.loads(probe.read_text())
h=json.loads((root/'checkpoints/before_test_20261007_142338/history.json').read_text());b=min(h,key=lambda x:x['val']['loss'])
results={'old_tcp_best':b,'old_tcp_last_epoch':h[-1]['epoch']+1,'old_e5_rollout':{'episodes':len(j['results']),'successes':sum(x['rollout']['task_success'] for x in j['results']),'offline':j['offline']}}
legacy=root/'local_source/outputs/data_audit/local_preprocess_smoke/pick_place_000042'
results['legacy_sample']={'path':str(legacy),'arrays':{}}
for name in ['images','state','action','timestamps_ms','segment_ids']:
    a=np.load(legacy/(name+'.npy'),mmap_mode='r',allow_pickle=False)
    r={'shape':list(a.shape),'dtype':str(a.dtype)}
    if name!='images':r['first']=a[0].tolist()
    results['legacy_sample']['arrays'][name]=r
raw=root/'local_source_(1)/RH20T_cfg5'
found=None
for sub in [raw/'training_data',raw/'robot_missing_data',raw/'missing_data/robot']:
    if not sub.exists():continue
    for f in sub.rglob('joint.npy'):
        if f.parent.name=='transformed':found=f;break
    if found:break
if found:
    joints=np.load(found,allow_pickle=True).item();grips=np.load(found.with_name('gripper.npy'),allow_pickle=True).item()
    for serial,stream in joints.items():
        if serial not in grips:continue
        ts=next((t for t in sorted(stream) if t in grips[serial]),None)
        if ts is None:continue
        q=np.asarray(stream[ts]);g=grips[serial][ts]
        results['raw_joint_sample']={'path':str(found),'serial':serial,'timestamp_ms':int(ts),'raw_joint_shape':list(q.shape),'first_7_rad':q[:7].tolist(),'gripper_measured_mm':float(g['gripper_info'][0]),'gripper_command_mm':float(g['gripper_command'][0]),'state8_rad_m':np.r_[q[:7],float(g['gripper_info'][0])*.001].tolist()}
        break
(OUT/'measured_facts.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print('\nSAMPLE',json.dumps({k:v for k,v in results.items() if 'sample' in k},ensure_ascii=False,indent=2))
