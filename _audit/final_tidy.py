from pathlib import Path
import re
O=Path(__file__).parent.parent
replace={
'suyra':'suy ra','làmtròn2':'làm tròn 2','ro ad map':'roadmap','margin al':'marginal',
'8 D':'8D','3 D':'3D','7DOF':'7 DOF','vàN':'và N','vàQ&A':'và Q&A','ôtrống':'ô trống',
'traceq_ref':'trace q_ref','ghiN/N':'ghi N/N','dungsai':'dung sai','sim-to-realgap':'sim-to-real gap',
'saukhi':'sau khi','taskAI':'task AI','caseba':'case ba','chứngminhAI':'chứng minh AI',
'trongconfig':'trong config','80 hAI':'80 h AI','head line':'headline','mid point':'midpoint',
'**Chưa.** User báo E25':'**CHƯA XÁC MINH.** Bạn báo E25','cũ0/10':'cũ 0/10',
'16h':'16 h','80h':'80 h','50h':'50 h','40h':'40 h','1,75h':'1,75 h','5h.':'5 h.',
'Hsetup':'H_setup','htrad':'h_trad','hAI':'h_AI','H setup':'H_setup',
'tháng.1 tỷ':'tháng. 1 tỷ','8n.':'8n.','cachejoint':'cache joint',
'khôngphải':'không phải','1000demo':'1000 demo','in hand':'in-hand'}
def tidy(t):
 saved=[]
 def protect(m):saved.append(m[0]);return f'\x01{len(saved)-1}\x02'
 t=re.sub(r'```[\s\S]*?```|`[^`\n]+`|\[[^\]]*\]\(<[^>]+>\)|\[[^\]]*\]\(https?://[^\s]*?\)|https?://[^\s]+',protect,t)
 for a,b in replace.items():t=t.replace(a,b)
 t=re.sub(r'A I(?=\d)',r'AI ',t)
 t=re.sub(r'(?<=[\w])(?=“)',r' ',t)
 t=re.sub(r'(?<=”)(?=[\w])',r' ',t)
 t=re.sub(r'(?<=[A-Za-zÀ-ỹ0-9)])\.(?=[A-ZÀ-Ỹ])',r'. ',t)
 return re.sub('\x01(\d+)\x02',lambda m:saved[int(m[1])],t)
for p in O.glob('*.md'):
 if int(p.name[:2])<4:continue
 p.write_text(tidy(p.read_text(encoding='utf-8')),encoding='utf-8')
p=O/'08_CHEAT_SHEET.md'
t=p.read_text(encoding='utf-8')
t=t.replace('1. Input/output là gì? 2. Vì sao CVAE train khác infer? 3. Controller khác policy ở đâu? 4. Chưa chứng minh điều gì? 5. Bước nghiệm thu tiếp theo là gì?', '1. Input/output là gì?\n2. Vì sao CVAE train khác infer?\n3. Controller khác policy ở đâu?\n4. Chưa chứng minh điều gì?\n5. Bước nghiệm thu tiếp theo là gì?')
p.write_text(t,encoding='utf-8')
print('Final prose spacing repaired; protected citations and code unchanged.')
