from doc_helpers import write
write('08_CHEAT_SHEET.md',r'''
# 08 — Tờ ôn trước khi trình bày

**Mốc17/10/2026.** Nhánh hiện tại: **joint/MCR**. E25 theo người dùng; chưa có metric/rollout mới để kiểm độc lập.[E1] BảnPDF kèm theo được dàn đúng một trangA4.

**Sơ đồ cần vẽ:** CFG5joint/RGB → causal10Hz + split/trainstats → MCRfrozen/cache → ACTtrain → checkpoint → inferz=0 → **jointexecutor còn cần nối** → Panda/MuJoCo → evaluator. Demo taskđích hiện làTCP, cần nhãn joint phù hợp.[E1–E3]

## 10 mốc cần nhớ

| Mốc | Cách nói đúng |
|---|---|
|7joint + kẹp=8D|Absoluteq rad vàwidthm, khôngTCPpose.[E2]|
|8slotcamera|6ngoài+2inhand; có thể thiếuview, dùngmask.[E2]|
|10Hz|Griddata/policy; khôngphảimotorHzđothật.[E2]|
|K=20|Chunknhãn2giây; khôngsuyraqueryfrequency.[E2]|
|β=10|L1+10KL trongconfig nền; chưaKLSweep.[E2]|
|1317CFG5episode|1053train/132val/132test theo logcache.[E1]|
|913demoaccepted|Manifesttaskđích; không giữclaim1000đềuđạt.[E3]|
|3/3 và0/10|Controller3seedđạt; TCPACTE5transfer0/10; khácnhánhjointmới.[E3]|
|15task|Hòa vốnengineeringhours, giảđịnh16n=120+8n.[E3]|
|22,2tháng|1tỷ/(3×15triệu),chưaOPEX; khôngđãđo.[E3]|

## 5 thuật ngữ

**Actionchunking:** mộtobservationdựđoáncảđoạnaction. **CVAE:** trainposterior từstate+target,latent32; inferencez=0. **Imitationlearning:** học từobservation/actiondemo. **Domainrandomization:** biếnthiênmôphỏng cókiểmsoát,chưabảochứngrobustness. **Sim-to-real:** khoảngcáchảnh,vậtlý,độnghọc vàtiming.[E2/E3]

## Mở đầu60giây

“NhómEDABK_TriHnghiêncứu robot học gắp–đặt từ dữ liệu để hướng tới giảm công cấu hình khi thay đổi linh kiện. Bài thử hiện tại là Panda trong MuJoCo đặt ba chốt vào khuôn. Nhánh mới dùng MCR trích đặc trưng ảnh nhiều camera, rồi ACT kết hợp với trạng thái khớp để dự đoán chuỗi hành động. Nhóm đã có mô phỏng, evaluator và cache dữ liệu; phần nối joint policy vào task và đánh giá closed-loop còn cần hoàn thiện. Chúng em sẽ tách rõ kết quả controller, thử nghiệmACTcũ và mục tiêu tiếp theo, rồi trình bày điều kiện để pilot tạiDENSO.”[E1–E3]

## Kết thúc30giây

“Điểm nhóm muốn chứng minh tiếp là policy học có thể thực hiện task với tỷ lệ thành công, chất lượng và thời gian đo được. Nhóm chưa coi few-shot, robot thật hay ROI là kết quả đã đạt. Bước ưu tiên là chốt contract joint, đo rollout và thống nhất robot cùng baselinecell với kỹ sưDENSO.”[E1/E3]

**Tuyệt đối không nói:** “ACT100%”; “đãfew-shot”; “1000demođềuđạt”; “losslàmm”; “evaltựđộngz=0”; “đổirobotlàchạy”; “24/7đãchứngminh”; “15task=15tháng”; “E100xong”; “0/10làkếtquảMCRmới”.

**Căn cứ:** [E1] [[H::5754]], [[R:BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:19]]. [E2] [[J:src/models/mcr_act.py:94]], [[J:configs/act/rh20t_all8.json:1]], [[J:src/data/cfg5_masked.py:205]]. [E3] [[J:data/splits/pick_place_finetune_manifest.json:1]], [[L:outputs/controller_evaluation/summary.json:1]], [[R:epoch5_transfer_probe_14120/report.json:1]], S2/31/38, phân tích trong06.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Input/output là gì? 2. Vì saoCVAEtrainkhácinfer? 3. Controllerkhácpolicyởđâu? 4. Chưa chứngminhđiềugì? 5. Bướcnghiệmthutiếptheolàgì?
''')

write('09_PRIORITY_AND_30MIN.md',r'''
# 09 — Việc ưu tiên và kịch bản30phút

Giới hạn30phút do bạn cung cấp trong chat17/10. Lịch thuyết trình trênweb hiện17/11/2026, khác thôngbáokhởiđộng16/11; cần chốt lại bằng thôngbáođội. [Vòng thi chính thức](https://densohackathon.vn/challenges), truycập17/10/2026. Đừng nhầm với demo video tốiđa15phút.

## Top5việc nên làm trước ngày thuyết trình

Thời gian dưới đây là **ước lượng của mentor cho công việc**, không phải số đo hay cam kết hoàn thành. Lượt này chỉ tạo tài liệu, không chạy các thí nghiệm đó.

| Ưu tiên | Việc cụ thể | Thời gian ước lượng | Đầu ra có thể kiểm |
|---|---|---|---|
|1|**Chốt snapshot nhánhjointmới và sửa claim slide.** Lấy metadata/config/history/log/checkpoint hash đúngrun; xácminhE25/E100/job14597/14598. SửaS12/16/18/42chojointMCR, S17cho sốdemo, S28MuJoCo, S2/35–38choROI/claimchưađo.|2–4giờ nếu truycậpđượcartifact; sửa slide1–2giờ riêng|Một bảngstatus gắncheckpoint/contract, một bộslide nhấtquán; nếu thiếulog thì giữCHƯA XÁC MINH. |
|2|**Đóng khoảng trốngjoint/TCP bằng kiểm tra nhẹ trước.** Chốt state/action/offset/stats, ghi joint demo phùhợp; viết/kiểmobservationjoint,executorjoint,unit/limits vàtracking. Không đưaoutputjointquaenvTCPcũ.|0,5–2ngày kỹthuật, cóthểlâuhơnnếuthiếugenerator/data|Mộtrecordt→target cógiátrị/đơnvị rõ; traceq_ref/q_measured/width,timestamp; không cầntrain dài để phát hiệnsemanticslỗi. |
|3|**Lấy một báo cáo learnedjointrollout thật.** Chọncheckpoint qua validation; developmentrollout với seed đãkhóa, ghiN/N,failurereason,cycle time,clip/timeout vàvideo. Saukhichốtprotocol mới dùngtestcuối.|Chuẩnbị0,5ngày; compute tùythời gianepisode/inference, **khôngdựbáothroughputchưađo**|Tối thiểumộtpilot cóNkhácseed báođúng phạmvi; nếuchạy10episode thìchỉnói10episode, khônggọiindustrialproof. |
|4|**Chốt robotxưởng, yêu cầuquality vàbaselinechi phí cùngmentor.** Model6/7trục,gripper/API,camera/toolcalibration,takt,linhkiện/dungsai,force,ca/nhâncông,BOM/OPEX.|Soạnbảng30–60phút; buổilàmviệc30–60phút; thờigianchờ phụthuộcxưởng|Đặc tả1cell vàma trận6trục/7trục; nguồnchodữliệukinh tế; safety/qualitygatecóngườiphụtrách. |
|5|**Nếu còn thời gian, làm ablation nhỏ thay vì thêmclaim.** Saukhidữliệujoint/rolloutđúng, so có/khôngpretrain hoặcsubsetcamera; chọnmộtcâuhỏiđủscope. Tập pitch vàQ&A saukhichốtcon số.|Thiếtkế2–4giờ; runtime theo pilot thực, cóthểvượtmộtngày; luyện2buổi×60–90phút|Một so sánhcùngdata/budget/protocol hoặcghirõchưacó; mỗi người tựvẽsơđồ vàtrảlờicâu khókhôngnétránh. |

Nguồn ưu tiên: [[H::5754]] [[H::5810]], [[J:src/simulation/panda_env.py:113]], [[J:src/simulation/panda_controller.py:16]], [[J:src/data/sim_demos.py:89]], [[J:data/splits/pick_place_finetune_manifest.json:1]], [[R:epoch5_transfer_probe_14120/report.json:1]].

Nếu chỉ còn một ngày: làmưu tiên1 vàbảngyêucầucell ở4; kiểmcontract ở2 trongphạmvingắn; **khôngbỏquakiểmsemantics đểchạyrobot hoặctrainnặng**. Chưa córolloutthìbáotrungthựclàchưacó,kèmplan,khônglấysốcontroller thaythế.

## Đề xuất chia30phút

Chưa biết30phút bao gồmQ&Ahaykhông. Chuẩn bịhai phiên bản, không cần chờ câu trả lời để tập:

| Phần | Nếu30phút gồmQ&A: nói20phút+10phútQ&A | Nếu30phút chỉpitch |
|---|---:|---:|
|Mởđầu,teamrấtngắn,problemcell/S2/10/13|3phút|4phút|
|Pipeline,mới/cũ,ACT,input/output/S12/15/16/18|6phút|8phút|
|Dữliệu/quality/split/S17/19|3phút|4phút|
|Kếtquảvàgiớihạn/controller,TCPcũ,jointmới/S42|3phút|4phút|
|Kinh tếmộtmôhìnhgiờcông,mộtcasepayback/S29/31–34/38|2,5phút|4phút|
|Robot6/7trục,safety,lộtrình/gate/S40|2phút|4phút|
|Kếtthúc|0,5phút|1phút|
|Dựphòngchuyểnslide/trục trặc|Đãgộptrongcácđoạn,nênrehearse19–20phút|1phút|

Các cột là **đề xuất phân bổ**, khôngphảithểlệBTC. Tổngpitch20phút hoặc30phút đúngcột tươngứng. Khôngđọchết43slide với cùngthờilượng. S4–8rútgọn20–40giây nếu cần; S23–28/S30/S33dùngbackupđểgiảithíchkhiđượchỏi,nhưngvẫnhọcđủtheo05.

## Thứ tự trình bày để tránh nhầm phiên bản

1. Nêu task và tiêu chí thật của môphỏng; chưa đồngnhất vớilinhkiệnDENSO.
2. Đưa sơđồjointMCRhiệntại; trìnhbày rõ haiđiểmcầnnối ởdemođích vàcontroller.
3. Nêu kếtquảtheorun: controller3/3; E5TCPtransfer0/10; cache1317; jointE25theobáo,chưametricmới.
4. Giải thích hướng đo tiếp vàbaseline. Sau đó mới trìnhbàylợiíchkỳvọng,giảđịnhkinhtế vàroadmap.

Tất cả con số bước3có nguồn trong00/01; khôngxemchúnglàcùngmộtrun hoặc cùngmodel. Lịch sửthiết kế làcáchgiảithíchvìsaonhómđổihướng,khônglàlýdođể bỏqualỗikhôngđạt.

## Bộ bằng chứng nên mở sẵn khi pitch

- Bảnghiện trạng vàlinkcheckpoint/config đúngrun; nếu chưa có thìchỉra ôtrống.
- Hai ảnh/sơđồphânbiệtTCP8D vàjoint8D,từ03.
- BáocáoN/N cùngseed,videocólabelcontroller/learned vàcheckpointID.
- Manifest913accepted/111rejected vàsplit731/91/91 củaTCPdemo; splitjoint1053/132/132khác tậpđó.
- Bảnggiảđịnhkinhtế:engineeringrate,wage,CAPEX,OPEX,mẫu sốthayngười; khônglấygiátrịcủapaperlàmkếtquảđội.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Nếu chỉcòn24giờ,việcnàogiúp tăngđộtincậy nhất?
2. Gate nào phải đạttrước khi báo mộtlearnedrollout?
3. NếuQ&Anằmtrong30phút,tôirútphầnnàocủadeck?
4. Tôi cómởđượcbằngchứngcho từngcon sốđịnhnói không?
5. Mộtngườikháctrongđội cóthểgiảithíchlạijoint/TCP vàROIđúngnhưtôi không?
''')
print('Created 08 and09')
