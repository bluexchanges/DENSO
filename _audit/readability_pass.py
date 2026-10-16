from pathlib import Path
from collections import Counter
from functools import lru_cache
import re,math,json,sys
O=Path(__file__).parent.parent
sources=[Path('C:/Users/ADMIN/.codex/attachments/f10658a7-e6f0-4f6b-8dca-15fd5a4c5c20/Pasted text.txt'),O/'_audit/slides_extracted.txt']
sources += [O/f'{n}' for n in ['00_README_AND_EVIDENCE.md','01_PROJECT_MAP.md','02_ACT_EXPLAINED.md','03_IO_AND_CODE.md']]
sources += [Path('F:/cfg5_mophong/local_source/docs')/n for n in ['DATA_GUIDE_VI.md','PAPER_ANALYSIS.md','PRETRAINING_VI.md','PIPELINE_GUIDE_VI.md','PROJECT_AUDIT.md','MUJOCO_PANDA_GUIDE_VI.md','PLACEMENT_LOGIC_REVIEW_VI.md']]
freq=Counter()
for p in sources:
    if p.exists():freq.update(w.lower() for w in re.findall(r'[^\W\d_]+',p.read_text(encoding='utf-8-sig')))
extra='''accepted rejected pending profile profiles failure failures input output shape state action actions target targets batch controller learned policy scripted expert robot camera cameras view views slot slots crop cache frozen full train val test loss checkpoint joint TCP ACT MCR CVAE PCA RGB API PLC MES ROI CAPEX OPEX BOM RA CPU GPU CUDA CLI NPY NPZ MP4 JSON XML YAML SHA DENSO EDABK TriH physical AI baseline backbone feature features ResNet ResNet18 ResNet50 Panda MuJoCo Franka FCI IK FK IL RL VLA OpenVLA Diffusion Policy DiffusionAD DROID human timestamp timestamps width gripper measured commanded reference tracking prototype metadata runtime contract rollout rollouts inference posterior prior latent vector token tokens embedding embeddings mask valid normalization dropout temporal ensemble ensembling query queries padding chunks chunking task tasks skill skills architecture encoder decoder video benchmark benchmarked pipeline metric metrics quality success rate rich varied diverse fixed one few shot held out overfit count counts split seed seeds group grouping source repo scope setup time study safety validation smoke step steps seedwise stateful scalar degrees rad radian metre mm m s N Hz DOF Dof epoch E CPU units dataset dataloader data loader torch torchvision factory factorytour tour startup software compute real sim realworld realtime digital twin digitaltwin low high precision body force torque contact tactile head multi modal multimodal software hardware update weights pretrain pretrained pretraining finetune tuning fine tune fine-tune from scratch body causal compression space throughput latency p50 p95 jerk solver workspace watch watchdog versioned model modelbased conditional commands pose proprio forcefeedback forcelimit insert insertion jointzero sign linklength limits flange limits intrinsic extrinsic calibration hand eye hand-eye reject rework repeated duplicate duplicates repeatability datacontract watermark color grey public commercial freecommercial license licensing legal manufacturer rig overhead wages workforce salary engineering staffing lifecycle ownership occupancy audit physical production productionwage costbasis basewage fullyloadedcost rate-limit procedural event afterany Ready Done Busy Fault Done Ready normalized E-stop init stop stopnow instruction recipe part ID partition smoke boundary grid plot plots scenario z beta mu logvar L1 KL rolloutprotocol dataefficiency sampleefficiency heredity performance closed loop open loop fp16 fp32 int8 quantization GPUModel ALOHA menagerie record table preview sources byte bytes storage shared spatial integer float32 float16 float64 int64 int32 array trainable strict snapshot code schema type dtype regex config environment episode episodes classifier component transition filename manuscript timestampage pop python PyTorch Matplotlib history optimizer exact per dimension reconstruction receding horizon reference render renderer desktop research simulated conceptual composite version admission eligibility evaluation innovation applicability maturity originality communication deployment stepwise angle angles worker workers hour hours minutes minute unit samples sample sampling sampler policyencoder posteriorencoder actionhead center resize short q_ref q_measured featureerror taskconditioning zeroshot lowshot zeropadding class ROS MG400 CoppeliaSim sourcecode dataframe call protocol benchmark speedup timestampdelta calculate featurecontract owner engineer time-sheet time-study N-demo OOD qualitycheck timesheet exteroceptive proprioception resample sourcefingerprint initcheckpoint sourcecode act_model_used false true generation generator domain distribution shift data leakage online background unseen actual dynamic dynamics grayscale reduced workflow guideline learning curve taskheldout manual repeat open close samplehold prototyping xưởng kỹ thuật kết quả thực nghiệm chất lượng cổ điển tay máy đa phương thức hệ tọa độ thất bại giới hạn minh họa kế hoạch giả định điện tử đội ngũ chuyên môn nhận thức nghiên cứu xử lý tích hợp giai đoạn học bắt chước kiểm chứng đã phần thiếu điều khiển yêu cầu thành công trực tiếp chính xác thử nghiệm chi phí triển khai nhà máy đồng bộ hiệu chuẩn nguồn dữ liệu thần kinh thông lượng đo lường phân tích giá trị ưu tiên bổ sung nhãn trạng thái đầu vào ra mô hình văn bản ý nghĩa điểm hòa vốn kịch bản lộ trình lịch sử cập nhật chưa xác minh thuyết trình mở đầu kết thúc học thuật quyết định từ chối chấp nhận trích xuất thí nghiệm vật liệu dễ vỡ tự động vị trí nền tảng cách ly bảo trì cảnh báo nghị định đối chiếu nhân công lời nói đọc nhớ giải thích khác biệt tiêu chí quy trình phiên bản trách nhiệm sở hữu tham số nhiệm vụ thao tác linh kiện bimanual fine-grained pretrainedweights few-shottraining'''.split()
extra += '''generalization candidate ablation collect artifact range backup mix accuracy uptime changeover availability cash salary saving completed run report simulate payback appearance orientation PTP eye recalibration retry interface rollback guard enable recovery vision inspection regression bench input robustness robust industrial proof rehearse label sourceprojection sanitycheck header phase forward computational sponsor readonly core policyencoder reward denoising anomaly detection generalist counterpart frequency timebase crosstask byteswarm futurestate samplewise jitter perturbation randomization task_success labelcontroller industrialproof fromscratch act_model_used referencecommand nominal learnerrate robots development head8D state8D head8d taskid recipeid Nrollout unfreeze namespace seed42 alpha beta sourcebase CPP configpath plotprobe taskcode explicit denominator futuretiming htrad hAI Htrad HAItotal schedulertime historyE58TCP E25joint E58TCP newmetrics currtime RH20T branchpipeline oldcheckpoint newcheckpoint chartvalues Bman costmodel sốt quyền sửa chữ kênh lược cử sĩ xã trời thương mại năng suất ròng trừ tuyến anh trăm mãi bốn song lùi mơ hồ quan trắc khẳng phủ đề xin thấp tố vốn hẹp ngôn cứ khoản đĩa miễn đáng bớt ngân khăn kê ăn kém càng đính rút tin lệnh lời lúc giữ toán quần kỷ tham sau cuối bắt đầu lặp '''.split()
for w in extra:freq[w.lower()]+=10
extra += '''claim claims gate takt deadline integration effort basis website maintenance fallback retarget retargeting retargement capacity calendar duration calendarduration setup cost net benefit netbenefit business company baseline study cycle time timestep timestampdelay holdout holdouts hourly rate cashflow pilot successflag hardware hardwaredata platform workforce factory automation FactoryAutomation coreplan Coreplan throughput encode decode encoderstate controllerreference dynamicframe FPT BTC DMVN HUST NTU ICLR KCN Thăng Long Thiên Lộc Kaiserslautern Copilot Phiếu phiếu cử cử nhân thạc sĩ xem mắt ngăn cho khâu khách khác tuổi đặt cược ngưỡng hưởng ích hứa retargetment nghiệm đo ledger launch world công tư phí đọc đồng hồ xử giả script inputstate outputaction pass fail headnode schema mới nguyên căn gốc thấp hậu thiếu cấp vòng hậu vệ tầng ngay thiệu nghệ xước chỉ dưới thu tiếp hợp sắp sẵn thế chuyển sau đánh biến khi giữa tập nặng sâu nền tiến lặp giữ lỗ lỗi trần giảm sửa buổi câu phát gửi nước chính đồ chức mục vụ quả ngẫu nhiên thông thoả thuận sáng tối thể nhô tiền lợi con ngữ tín xác tắc nhân dân sử dụng trì vỡ mở nhả tịnh quay ngắn dài kẹp cảm rất hơn kích thước bù ngang phép đạt hứa lực cần phục hỏng thuộc theo chốt kiểm không chưa đã làm ngoài trong tạo mới cũ năm ngày tháng giờ phút giây bước sót nhất lực mẫu phép và dưới chất khí tầm giới hạn nguồn quý xem giấy thật khi xong phương đo lấy góp tự đi đầy gộp thích ứng công sức dừng nghĩ cơ chia thành đứng nhiều theo mang tổng đọc để nhờ đủ ra thì nêu hết giá tại vậy lương liệu nghĩa bằng đôi chấp nhận mọi giữa phải sử cố báo hẹn ước sau lúc ngay slide scope prototype sponsor sponsorship submission template lowcost no-label paper author tác giả queue đồng nhiệm chứng triển yêu công thức lịch mức bản nguồn testset trainset targetposterior pretrainedvisual backboneforward taskscope taskpilot timelimit cameramask samplestate learnedpolicy multiple independent firstaction first-action zerolatent maskage replicates stagewise datasetcoverage tasksuccess stateprojection bodytext classmethod incremental cost savings cellstate statemachine realtimecontroller user authors package shadowing no-gradient withheld memory pointcloud qref qmeasured lossval priorerror modelpolicy robotpolicy testprotocol toy example case plan trace samplingtime provider static figures diff sourceobject min_rating taskID fields stateprojection same-tick E100 job14598 job14597 afterany userdata''' .split()
for w in extra:freq[w.lower()]+=10
ascii_tech={w.lower() for w in extra if w.isascii()}
vocab={w for w,c in freq.items() if ((any(ord(ch)>127 for ch in w) and len(w)<=8) or w.isascii())}
vocab |= ascii_tech
# Exclude accidental concatenations that appear in old generated notes.
for bad in ['trongsim','dữliệu','côngviệc','thựctế','cóthể','nhómđã','hệthống','chưacó','sốliệu','tậpval','tậptest','tậptrain','môhình','trênslide','chỉđọc','củanhóm','nhánhmới','họcthật','ngoàiđời','theolog','vớitask','đãtrain','lựcđỡ','đúngrun','nếuđổi','đãđo']:
    vocab.discard(bad)
@lru_cache(None)
def split_word(word):
    explicit={
    'dùngMimicGen':'dùng MimicGen','kênhCartesian100Hz':'kênh Cartesian 100 Hz','vàđãcóđườngcongN':'và đã có đường cong N',
    'dươngởmôhìnhtuyến':'dương ở mô hình tuyến','chỉcóhòavốndươngnếuhtrad':'chỉ có hòa vốn dương nếu htrad',
    'tiếtkiệmdươngtừtask16nếunnguyên':'tiết kiệm dương từ task 16 nếu n nguyên','Thaynsovớihàm8n':'Thay n vào hàm 8n',
    'Robotcótiềmnăng':'Robot có tiềm năng','Giảđịnhwage':'Giả định wage','head8Dnhưkhung':'head 8D như khung',
    'MG400là4trụctheohãng':'MG400 là 4 trục theo hãng','Kiểmtrađúngsảnphẩm':'Kiểm tra đúng sản phẩm',
    'restarttheorobotvàxưởng':'restart theo robot và xưởng','kỷluậttimestamp':'kỷ luật timestamp',
    'làmụctiêusẽđobằngđườngcongN':'là mục tiêu sẽ đo bằng đường cong N','Cobottựđộngantoàn':'Cobot tự động an toàn',
    'thờigiancanthiệp':'thời gian can thiệp','đượcxưởngphêduyệt':'được xưởng phê duyệt',
    'Córobotthậtthìmaiđưamodelxuốngchạyngay':'Có robot thật thì mai đưa model xuống chạy ngay',
    'hoặcAIkhôngđạtđộổnđịnhthìnhómsẽđềxuấtphươngántruyềnthốnghoặchybrid':'hoặc AI không đạt độ ổn định thì nhóm sẽ đề xuất phương án truyền thống hoặc hybrid',
    'thaytasklàphảimua':'thay task là phải mua','nhưngcầndesignreward':'nhưng cần design reward',
    'VềsaucóthểnghiêncứuhybridIL':'Về sau có thể nghiên cứu hybrid IL','vàevaluatorđángtincậy':'và evaluator đáng tin cậy',
    'xuốngxưởngngàymaithìchạyluônđượckhông':'xuống xưởng ngày mai thì chạy luôn được không',
    'evaltựđộngz':'eval tự động z','Mộtrecordt':'Một record t','Dựphòngchuyểnslide':'Dự phòng chuyển slide',
    'tăngđộtincậy':'tăng độ tin cậy','tôirútphầnnàocủadeck':'tôi rút phần nào của deck'}
    if word in explicit:return explicit[word]
    lower=word.lower()
    if lower in vocab or len(word)<4:return word
    if word.isascii() and word.isalpha():return word
    if re.fullmatch(r'[A-Z]\d{1,3}',word) or word.isupper():return word
    # Preserve identifiers and uncommon English words unless a complete dictionary split exists.
    n=len(word);dp=[None]*(n+1);dp[0]=(0,[])
    for i in range(n):
        if dp[i] is None:continue
        for j in range(i+1,min(n,i+32)+1):
            piece=lower[i:j];orig=word[i:j]
            known=piece in vocab;number=orig.isdigit();ident=bool(re.fullmatch(r'[A-Z]\d{1,3}',orig))
            if not (known or number or ident):continue
            if len(piece)==1 and not(number or ord(piece)>127 or orig.isupper() or (i>0 and word[i-1].isdigit() and piece in {'d','h','m','s','n','b','g'})):continue
            cost=dp[i][0]+7-math.log(freq.get(piece,3)+1)*.35
            if number:cost+=1
            if dp[j] is None or cost<dp[j][0]:dp[j]=(cost,dp[i][1]+[orig])
    if dp[n] is None or len(dp[n][1])==1:return word
    return ' '.join(dp[n][1])
changes=Counter();unknown=Counter()
def repair(t):
    saved=[]
    def protect(m):saved.append(m.group());return f'\u0001{len(saved)-1}\u0002'
    t=re.sub(r'```[\s\S]*?```|`[^`\n]+`|\[[^\]]*\]\(<[^>]+>\)|\[[^\]]*\]\(https?://[^\s]*?\)|https?://[^\s]+',protect,t)
    def fix(m):
        w=m.group();s=split_word(w)
        if s!=w:changes[(w,s)]+=1
        elif any(ord(ch)>127 for ch in w) and len(w)>8:unknown[w]+=1
        return s
    t=re.sub(r'[^\W_]+',fix,t)
    t=t.replace('hồi顾','nhìn lại')
    t=re.sub('\u0001(\d+)\u0002',lambda m:saved[int(m[1])],t)
    return t
drafts={}
for p in sorted(O.glob('*.md')):
    if int(p.name[:2])<4:continue
    drafts[p]=repair(p.read_text(encoding='utf-8'))
(O/'_audit/readability_preview.json').write_text(json.dumps({'changes':[{'from':a,'to':b,'count':c} for (a,b),c in changes.most_common()],'unknown':unknown.most_common()},ensure_ascii=False,indent=2),encoding='utf-8')
print('CHANGES',sum(changes.values()),'UNIQUE',len(changes),'UNKNOWN',len(unknown))
for (a,b),c in changes.most_common(110):print(a,'=>',b,c)
print('UNRESOLVED',unknown.most_common(65))
if '--apply' in sys.argv:
    for p,t in drafts.items():p.write_text(t,encoding='utf-8')
    print('APPLIED',len(drafts))
