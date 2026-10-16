from doc_helpers import write
write('04_CONTEXT_AND_SOURCES.md',r'''
# 04 — Bối cảnh cuộc thi, nhà máy và nguồn đối chiếu

**Ngày truy cập tất cả nguồn dưới đây: 17/10/2026, Asia/Bangkok.** Ưu tiên website BTC, DENSO và tác giả. Thông tin website có thể thay đổi; lịch trình cần đối chiếu email/thông báo dành riêng cho đội. Dẫn nguồn công khai không chứng minh chính hệ thống của nhóm đạt kết quả đó.

## 1. Cuộc thi 2026 và thay đổi lịch đã phát hiện

✅ DENSO Việt Nam và FPT tổ chức mùa4, ba chủ đề Predictive & Knowledge AI, Humanoid & Robot, Data Utilization; tổng giải thưởng250triệu. Nguồn: [thông báo BTC](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu).

| Mốc | Thông báo khởi động/báo chí | Website SPA đang hiển thị khi kiểm tra | Kết luận |
|---|---|---|---|
| Hạn ý tưởng |12/10/2026|13/10/2026,23:59:59GMT+7|Có cập nhật, không lặp lịch cũ như chắc chắn |
| Đánh giá ý tưởng |13–19/10|13–19/10|Giữ nguyên trên phần đã đọc |
| Factory Tour2 |Không nêu trong đoạn lịch cũ|23/10|DànhTop10 |
| Thuyết trình chọnTop5 |16/11|**17/11/2026**|Ưu tiên lịch web mới để chuẩn bị, cần xác nhận thông báo đội |
| Chung kết |02/12|02/12/2026|Cùng mốc |

Nguồn mới: [Home](https://densohackathon.vn/home), [Competition Rounds](https://densohackathon.vn/challenges), đã đọc sau JavaScript tải trong trình duyệt; nguồn cũ: [bài BTC khi khởi động](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu) và [Tạp chí Công Thương31/07/2026](https://tapchicongthuong.vn/denso-factory-hacks-mua-4--sinh-vien-dinh-hinh-nha-may-tuong-lai-bang-ai-537926.htm). Không suy ra lý do đổi lịch.

Web hiện có một số ngày đăng ký khác nhau giữa Home và tabRound1; đây là dấu hiệu không nên dùng một snapshot web để quyết định deadline lịch sử của đội. Không tự đổi các ngày trong PPTX gốc.

### Tiêu chí chấm chính thức đã tìm được

Trang [Competition Rounds](https://densohackathon.vn/challenges), **Round2 → Evaluation Criteria**, công bố thang0–5 cho từng tiêu chí và lấy điểm trung bình. Năm tiêu chí, diễn giải ngắn:

| Tiêu chí | Giám khảo có thể kiểm ở dự án |
|---|---|
| Tính mới/khác biệt công nghệ | Nhóm đóng góp gì ngoàiACT/MCR có sẵn? |
| Truyền đạt kỹ thuật | Giải thích đượcCVAE, input/output, đơn vị và giới hạn? |
| Mức độ hoàn thiện | Có model/demo/prototype và báo cáo thực nghiệm tới đâu? |
| Hiểu bài toán kinh doanh | Linh kiện/cell/takt/tổn thất thực tế là gì? |
| Khả thi ứng dụng | Tích hợp, mở rộng và giá trị thực có căn cứ? |

Đây là **rubric2026 đang công bố**, không phải suy từ mùa trước. Câu hỏiQ&A trong07 là **dự đoán của mentor**, không phải danh sách câu hỏiBTC công bố. Rubric không đảm bảo ban giám khảo chỉ hỏi năm mục đó.

Round2 yêu cầu demo video tối đa15phút và pitch deck. **30phút thuyết trình** là giới hạn bạn cung cấp trong chat, không được nhầm với giới hạn video. Source code là mục tùy chọn trên phần yêu cầu đã đọc. Nguồn: [Round2 Overview/Rules](https://densohackathon.vn/challenges).

### Chủ đề robot phù hợp ở đâu?

Trang [Technology Challenges](https://densohackathon.vn/theme) nêu H1 về giảm công huấn luyện, H2 về độ khéo/force–angle, H3 về tự động hóa linh hoạt chi phí thấp. **Suy luận cho đội:** dự án gầnH1 ở thu thập dữ liệu/học skill, gầnH3 ở gắp linh kiện vàROI. Chưa đủ bằng chứng đáp ứngH2 vì chưa benchmark điều khiển lực/ngón tay. Đề xuất ghi rõ bài toán nhóm đăng ký; không tự nhận làm trọnH1–H3.

FAQ chính thức cho biết mô phỏng được ưu tiên choH1 và không bắt buộc một công cụ simulation cụ thể. Việc thử robot thật còn phụ thuộc đánh giá success/safety. FAQ cũng nói giai đoạn đầu đội tự nghiên cứu/ước tính, mentorTop10 hỗ trợ dữ liệu chính xác hơn. **Không thấy FAQ công bố model tay máy ở xưởng hoặc xác nhận chi phí250.000đ/h của nhóm.** Nguồn: [FAQ](https://densohackathon.vn/qa), đã mở các câu vềH1, Robotics và baseline/ROI.

## 2. Các mùa2023–2025: điều đã xác minh và điều chưa có

| Mùa | Điều có nguồn chính thức | Ý nghĩa cho bài trình bày |
|---|---|---|
|2023|Cuộc thi khởi động2023, lịch kéo tới10/01/2024; giải200triệu. Mô tả đánh giá đột phá công nghệ và tính thực tiễn nhà máy. [DENSO26/09/2023](https://www.denso.com/vn/vi/news/newsroom/2023/20230901/)|Đừng nhầm năm chung kết với tên mùa |
|2023, đội thắng|BTC2026 hồi顾 ghi **EDABK-1, HUST**, giải pháp camera chi phí thấp thu dữ liệu sản xuất. [BTC2026](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu)|Thành công gắn bài toán cụ thể, không chỉ chọn model |
|2024|**ETTN,HUST**, AI+IoT giám sát sản xuất. DENSO2025 nói giải pháp tiếp tục phát triển để hướng triển khai2026. [DENSO22/09/2025](https://www.denso.com/vn/vi/news/newsroom/2025/hackathon-2025/)|“Hướng triển khai2026” trong nguồn2025 không chứng minh đã nghiệm thu |
|2025|**SPARK, UET–VNU**, DiffusionAD phát hiện lỗi không cần dữ liệu gán nhãn theo bàiBTC. [BTC2026](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu)|DiffusionAD kiểm lỗi khác Diffusion Policy điều khiển robot |
|Đề bài đầy đủ2024|**Không tìm thấy bản chính thức đầy đủ trong lượt tra cứu**; có mô tả giải pháp thắng từDENSO|Không tự suy đề bài năm đó từ giải pháp thắng |
|Chủ đề2025|DENSO nêu dự báo thông minh, vận hành chính xác, sản xuất liên tục. [DENSO2025](https://www.denso.com/vn/vi/news/newsroom/2025/hackathon-2025/)|Đây là chủ đề2025, không thay ba chủ đề2026 |

**Suy luận rút ra:** các ví dụ thắng giải đều giải quyết một công đoạn, dữ liệu hoặc lỗi vận hành cụ thể. Vì vậy đội nên trình bày một cell cóKPI, protocol đánh giá và đường tích hợp. Không có bằng chứng “dùngACT được ưu tiên”, “robot thắng hơn dashboard”, hoặc “ROI là tiêu chí có trọng số cao nhất”.

## 3. DENSO Việt Nam và ranh giới kiến thức về nhà máy

✅ Trang công tyDMVN nêu doanh nghiệp ở **LôE1,KCNThăngLong,xãThiênLộc,HàNội**, sản xuất/kinh doanh sản phẩm liên quan động cơ ô tô. Trang có dữ liệu nhân sự mang mốc2020 nên không dùng như quy mô hiện tại. Nguồn: [DENSO Manufacturing Vietnam](https://www.denso.com/vn/vi/about-us/company-information/dmvn/).

Trang [Linh kiện OEM](https://www.denso.com/vn/vi/business/vietnam-oem/) mô tả một số họ sản phẩm như vanVIC vàAVS. **Danh mục kinh doanhDENSO không chứng minh từng sản phẩm đều được sản xuất tại cell mà đội khảo sát.** Không tự nói chốt mô phỏng là linh kiện van thật.

🟡 Slide10/13 nói công đoạn tiền xử lý, linh kiện~10mm dễ vỡ, dung sai2mm. Đây là lời trên slide, chưa có bản vẽ/yêu cầu/đo thời gian tại cellDENSO kèm theo trong repo. Cần lấy mã linh kiện, kích thước/tolerance bản vẽ, hướng đặt, yêu cầu chống xước/bẩn, takt time, sốca và tỷ lệreject từ mentor. Không tự xác nhận công đoạn tiền rửa hoàn toàn thủ công hoặc lỗi2–5% chỉ từ ảnh minh họa.

✅ DENSO WAVE có robot5/6trục,SCARA,cobot,controller và các ứng dụng lắp ráp/inspection/materialhandling. Điều này cho thấy công ty đã có nền tự động hóa để so sánh. **Không chứng minh DENSO Việt Nam đang dùng đúng model nào trong cell của đội.** Nguồn: [DENSO WAVE Robotics](https://www.denso-wave.com/en/robot/).

DENSO có chiến lượcFactoryAutomation và giải pháp từ thiết kế tới bảo trì. Từ đó **suy luận** nhóm cần chứng minh giá trị trên toàn vòng đời, không chỉ video gắp đẹp. Nguồn: [Integrated Report2025, Factory Automation](https://www.denso.com/global/en/-/media/Global/about-us/investors/integrated-report_web/2025/pdf-en/081.pdf). Chưa tìm thấy nguồn công khai xác nhận **ACT của nhóm** hoặc **ACT+8camera+MCR** đã vận hành sản xuất tạiDMVN.

## 4. Đối chiếu học thuật/kỹ thuật và cách dùng khi trả lời

| Nguồn gốc | Dùng để giải thích | Không được suy ra |
|---|---|---|
|[ACT,RSS2023](https://roboticsproceedings.org/rss19/p016.html), [codeACT](https://github.com/tonyzhaozh/act)|Action chunks,CVAE,temporal ensemble là nền tảng đã có|Nhóm sáng chếACT hoặc đạt success của paper |
|[RH20T dataset](https://rh20t.github.io/), [APIconfig](https://github.com/rh20t/rh20t_api/blob/main/configs/configs.json)|CFG5 làFranka, joint7,2inhand serial; schema raw/align|Mọi subset/loader cùng action encoding; bảnRLDS cộng đồng không thay schema nhóm |
|[RH20T ACT baseline](https://github.com/rh20t/act_baseline)|Lõi source và cấu hình tham khảo của pipeline|PaperRH20T và pipeline nhóm là cùng thí nghiệmone-shot |
|[MCR,tác giả](https://robots-pretrain-robots.github.io/), [paper](https://arxiv.org/abs/2410.22325), [code](https://github.com/luccachiang/robots-pretrain-robots)|Visualrepresentation pretrain robot,DROID; frozenencoder là lựa chọn có cơ sở|MCR tốt hơnResNet18 trên task nhóm nếu chưaablation |
|[MuJoCo docs](https://mujoco.readthedocs.io/en/stable/overview.html), [PandaMenagerie](https://github.com/google-deepmind/mujoco_menagerie/tree/main/franka_emika_panda)|Physics/contact, nguồn robot model|DigitalTwin của cell thật đã hiệu chuẩn hoàn chỉnh |
|[DAgger,Ross2011](https://proceedings.mlr.press/v15/ross11a.html)|Distribution shift/compounding error củaIL|Nhóm đã triển khaiDAgger; source hiện chưa cho thấy |
|[DomainRandomization,Tobin2017](https://arxiv.org/abs/1703.06907)|Randomize mô phỏng là một cách giảm lệch thị giác|Đổi màu/đèn là đủ sim-to-real hoặc đảm bảo generalization |
|[MimicGen](https://mimicgen.github.io/)|Tạo thêm robot demonstrations trong simulator là một hướng nghiên cứu|Nhóm dùngMimicGen; chưa có source chứng minh |
|[DiffusionPolicy](https://diffusion-policy.cs.columbia.edu/)|Sinh action qua denoising, actionsequence/recedinghorizon|Chắc chắn chậm hơnACT trên hardware/cấu hình nhóm; chưabenchmark |
|[OpenVLA](https://openvla.github.io/)|VLA dùng ảnh/ngônngữ/action, mở rộng instruction và tasks|CodeACT hiện có input ngônngữ hoặc tự hiểu lệnh văn bản |
|[π0,tác giả](https://www.pi.website/blog/pi0)|Generalistpolicy kết hợp nềnVLM và flowmatching actiongeneration|Nhóm đã tích hợpπ0 hoặcVLA luôn tốt hơn task hẹp |
|[FrankaFCI](https://frankarobotics.github.io/docs/overview.html)|API joint/Cartesian và control1kHz là ví dụ choPanda researchrobot thật|Tay máy ở xưởng làPanda/FCI, hoặc model10Hz trực tiếp chạy motor1kHz |
|[OSHAIndustrialRobotSystems](https://www.osha.gov/otm/section-4-safety-hazards/chapter-4)|Cần đánh giá rủi ro ở cả integration/operation/maintenance|Đây là chứng nhận an toàn ViệtNam hoặc hệ thống nhóm đã tuân thủ/chứng nhận |

Các kết luận lựa chọn/baseline ở đây là phân tích kỹ thuật của mentor. Nếu muốn nói một giải pháp tốt hơn, cần so cùng dữ liệu/robot/compute vàKPI. Không nhập số thành công từpaper vào bảng kết quả nhóm.

### RH20T: camera, tần số và license cần hiểu đúng

Nguồn chính thức công bố RGB1280×720 ở10Hz và bảnresize640×360; có kênhCartesian100Hz trong bảng modality tổng quát. **Dự án resample10Hz bằng timestamp**, không dựa sốFPS ghi trongMP4 rồi coi mọi stream đồngbộ. CFG5/API xác nhậnjoint7, haiinhand serial104422070042/135122079702;8slot cụthể lấy config nhóm. [Dataset](https://rh20t.github.io/), [configCFG5](https://github.com/rh20t/rh20t_api/blob/main/configs/configs.json).

TrangRH20T phân biệt tậpC vàNC theo nhómscene, có điều kiện hạn chế thương mại với phầnNC/model học từ đó. **Chưa audit license membership của splitjoint mới**. Trước pilotthươngmại cần đối chiếu scene,license và quyềnweights/data với chủ sở hữu; không nói “dataset công khai nên dùng thương mại vô hạn”. Đây là điểm cần xác minh quyền sử dụng theo nguồn, không phải kết luận pháp lý riêng cho dự án. [Điều khoản doRH20T công bố](https://rh20t.github.io/#License).

## 5. Danh mục kiểm tra web và phần chưa tìm thấy

Đã đọcHome,theme,challenges,qa và các bàiBTC. Công cụ trích web trảrỗng vớiSPA nên đã đọc tab vòng2/criteria/rules trong trình duyệt. URL thử `/rules` không có nội dung đọc được; **routequan sát thật là `/challenges`**, không dựng link thểlệ khác. Đã có rubric2026 nên không cần lấy rubric2023 thay thế.

**Không tìm thấy hoặc chưa xác minh:** modelrobotxưởng; thiết bị thật đã tài trợ cho riêngđội; tolerance2mm có văn bảnDENSO; baseline lỗi2–5%; nguồn đo4/16/40h,120h,8h vàbáogiá1tỷ; caseACT/DiffusionPolicy triểnkhai production ở chínhDMVN; thí nghiệm few-shot hoặc pretrainablation của nhóm; đềbài đầyđủ2024 trongnguồnchínhthức đã đọc. Các mục này giữCHƯA XÁC MINH.

## 6. Cuộc thi quan tâm điều gì → dự án đáp ứng thế nào → còn thiếu gì

| Điều cần chứng minh | Dự án có bằng chứng | Còn thiếu và cách bù |
|---|---|---|
| Tínhmới/khácbiệt | ✅ Adapter8camera,mask,MCRcache,evaluator cócode | So sánh vớibaseline, mô tả đónggóp triểnkhai thay vì claim thuậttoánmới |
| Hiểukỹthuật | ✅ Có thể truy input/output,l1/KL,train/infer từsource | Tự giải thíchjoint/TCP,posteriorloss,latency vànhãnproxy |
| Hoànthiện | ✅ Controller;✅cache;🟡jointtrain theo báoE25 | Learnedjointrollout,metric,video gắncheckpoint,khôi phục lỗi |
| Hiểunhàmáy | 🟡 Slidemôtả côngđoạn vàlinhkiện | Yêucầu cell/bảnvẽ,takt,quality,errorbaseline,robotmodel thực |
| Khảthi/kinhtế | 🟡 Có giảđịnh giờcông/ROI | Nhấtquán con số,BOM,OPEX,ROI nhạy theo uptime/năngsuất;pilotđothật |
| An toàn/integration | 🟡 Giớihạn môphỏng/evaluator | RA cho cellthật,interlock,PLC/qualityhandshake,maintenance vàfallback có người phụtrách |

Bằng chứng dự án cho bảng: [[J:src/models/mcr_act.py:44]], [[J:src/data/cfg5_masked.py:205]], [[L:outputs/controller_evaluation/summary.json:1]], [[H::5754]], slide2/13/21–38. Các thiếu sót cụ thể vàthứtự xửlý nằmở06/09.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Lịchweb mới khác thôngbáokhởiđộng ởhai mốc nào?
2. Nămtiêuchí chấmvòng2 làgì,đâu lànguồnchínhthức?
3. Vìsao biếtDENSO córobot không chứngminh robotxưởng làPanda?
4. PhânbiệtDiffusionAD,DiffusionPolicy vàACT khi nhắc cácmùatrước.
5. Chỉra mộtclaim kỹthuật,mộtclaim nhàmáy vàmộtclaimkinhtế còn thiếu bằngchứng.
''')
print('Created 04')
