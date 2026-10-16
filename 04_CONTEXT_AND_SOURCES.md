# 04 — Bối cảnh cuộc thi, nhà máy và nguồn đối chiếu

**Ngày truy cập tất cả nguồn dưới đây: 17/10/2026, Asia/Bangkok.** Ưu tiên website BTC, DENSO và tác giả. Thông tin website có thể thay đổi; lịch trình cần đối chiếu email/thông báo dành riêng cho đội. Dẫn nguồn công khai không chứng minh chính hệ thống của nhóm đạt kết quả đó.

## 1. Cuộc thi 2026 và thay đổi lịch đã phát hiện

✅ DENSO Việt Nam và FPT tổ chức mùa 4, ba chủ đề Predictive & Knowledge AI, Humanoid & Robot, Data Utilization; tổng giải thưởng 250 triệu. Nguồn: [thông báo BTC](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu).

| Mốc | Thông báo khởi động/báo chí | Website SPA đang hiển thị khi kiểm tra | Kết luận |
|---|---|---|---|
| Hạn ý tưởng |12/10/2026|13/10/2026,23:59:59GMT+7|Có cập nhật, không lặp lịch cũ như chắc chắn |
| Đánh giá ý tưởng |13–19/10|13–19/10|Giữ nguyên trên phần đã đọc |
| Factory Tour 2 |Không nêu trong đoạn lịch cũ|23/10|Dành Top 10 |
| Thuyết trình chọn Top 5 |16/11|**17/11/2026**|Ưu tiên lịch web mới để chuẩn bị, cần xác nhận thông báo đội |
| Chung kết |02/12|02/12/2026|Cùng mốc |

Nguồn mới: [Home](https://densohackathon.vn/home), [Competition Rounds](https://densohackathon.vn/challenges), đã đọc sau JavaScript tải trong trình duyệt; nguồn cũ: [bài BTC khi khởi động](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu) và [Tạp chí Công Thương31/07/2026](https://tapchicongthuong.vn/denso-factory-hacks-mua-4--sinh-vien-dinh-hinh-nha-may-tuong-lai-bang-ai-537926.htm). Không suy ra lý do đổi lịch.

Web hiện có một số ngày đăng ký khác nhau giữa Home và tab Round 1; đây là dấu hiệu không nên dùng một snapshot web để quyết định deadline lịch sử của đội. Không tự đổi các ngày trong PPTX gốc.

### Tiêu chí chấm chính thức đã tìm được

Trang [Competition Rounds](https://densohackathon.vn/challenges), **Round 2 → Evaluation Criteria**, công bố thang 0–5 cho từng tiêu chí và lấy điểm trung bình. Năm tiêu chí, diễn giải ngắn:

| Tiêu chí | Giám khảo có thể kiểm ở dự án |
|---|---|
| Tính mới/khác biệt công nghệ | Nhóm đóng góp gì ngoài ACT/MCR có sẵn? |
| Truyền đạt kỹ thuật | Giải thích được CVAE, input/output, đơn vị và giới hạn? |
| Mức độ hoàn thiện | Có model/demo/prototype và báo cáo thực nghiệm tới đâu? |
| Hiểu bài toán kinh doanh | Linh kiện/cell/takt/tổn thất thực tế là gì? |
| Khả thi ứng dụng | Tích hợp, mở rộng và giá trị thực có căn cứ? |

Đây là **rubric 2026 đang công bố**, không phải suy từ mùa trước. Câu hỏi Q&A trong 07 là **dự đoán của mentor**, không phải danh sách câu hỏi BTC công bố. Rubric không đảm bảo ban giám khảo chỉ hỏi năm mục đó.

Round 2 yêu cầu demo video tối đa 15 phút và pitch deck. **30 phút thuyết trình** là giới hạn bạn cung cấp trong chat, không được nhầm với giới hạn video. Source code là mục tùy chọn trên phần yêu cầu đã đọc. Nguồn: [Round2 Overview/Rules](https://densohackathon.vn/challenges).

### Chủ đề robot phù hợp ở đâu?

Trang [Technology Challenges](https://densohackathon.vn/theme) nêu H1 về giảm công huấn luyện, H2 về độ khéo/force–angle, H3 về tự động hóa linh hoạt chi phí thấp. **Suy luận cho đội:** dự án gần H1 ở thu thập dữ liệu/học skill, gần H3 ở gắp linh kiện và ROI. Chưa đủ bằng chứng đáp ứng H2 vì chưa benchmark điều khiển lực/ngón tay. Đề xuất ghi rõ bài toán nhóm đăng ký; không tự nhận làm trọn H1–H3.

FAQ chính thức cho biết mô phỏng được ưu tiên cho H1 và không bắt buộc một công cụ simulation cụ thể. Việc thử robot thật còn phụ thuộc đánh giá success/safety. FAQ cũng nói giai đoạn đầu đội tự nghiên cứu/ước tính, mentor Top 10 hỗ trợ dữ liệu chính xác hơn. **Không thấy FAQ công bố model tay máy ở xưởng hoặc xác nhận chi phí 250.000đ/h của nhóm.** Nguồn: [FAQ](https://densohackathon.vn/qa), đã mở các câu về H1, Robotics và baseline/ROI.

## 2. Các mùa 2023–2025: điều đã xác minh và điều chưa có

| Mùa | Điều có nguồn chính thức | Ý nghĩa cho bài trình bày |
|---|---|---|
|2023|Cuộc thi khởi động 2023, lịch kéo tới 10/01/2024; giải 200 triệu. Mô tả đánh giá đột phá công nghệ và tính thực tiễn nhà máy. [DENSO26/09/2023](https://www.denso.com/vn/vi/news/newsroom/2023/20230901/)|Đừng nhầm năm chung kết với tên mùa |
|2023, đội thắng|BTC 2026 nhìn lại ghi **EDABK-1, HUST**, giải pháp camera chi phí thấp thu dữ liệu sản xuất. [BTC2026](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu)|Thành công gắn bài toán cụ thể, không chỉ chọn model |
|2024|**ETTN, HUST**, AI+IoT giám sát sản xuất. DENSO 2025 nói giải pháp tiếp tục phát triển để hướng triển khai 2026. [DENSO22/09/2025](https://www.denso.com/vn/vi/news/newsroom/2025/hackathon-2025/)|“Hướng triển khai 2026” trong nguồn 2025 không chứng minh đã nghiệm thu |
|2025|**SPARK, UET–VNU**, DiffusionAD phát hiện lỗi không cần dữ liệu gán nhãn theo bài BTC. [BTC2026](https://densohackathon.vn/post/khoi-ong-denso-factory-hacks-2026-kien-tao-nha-may-tuong-lai-voi-ai-robot-va-du-lieu)|DiffusionAD kiểm lỗi khác Diffusion Policy điều khiển robot |
|Đề bài đầy đủ 2024|**Không tìm thấy bản chính thức đầy đủ trong lượt tra cứu**; có mô tả giải pháp thắng từ DENSO|Không tự suy đề bài năm đó từ giải pháp thắng |
|Chủ đề 2025|DENSO nêu dự báo thông minh, vận hành chính xác, sản xuất liên tục. [DENSO2025](https://www.denso.com/vn/vi/news/newsroom/2025/hackathon-2025/)|Đây là chủ đề 2025, không thay ba chủ đề 2026 |

**Suy luận rút ra:** các ví dụ thắng giải đều giải quyết một công đoạn, dữ liệu hoặc lỗi vận hành cụ thể. Vì vậy đội nên trình bày một cell có KPI, protocol đánh giá và đường tích hợp. Không có bằng chứng “dùng ACT được ưu tiên”, “robot thắng hơn dashboard”, hoặc “ROI là tiêu chí có trọng số cao nhất”.

## 3. DENSO Việt Nam và ranh giới kiến thức về nhà máy

✅ Trang công ty DMVN nêu doanh nghiệp ở **Lô E1, KCN Thăng Long, xã Thiên Lộc, Hà Nội**, sản xuất/kinh doanh sản phẩm liên quan động cơ ô tô. Trang có dữ liệu nhân sự mang mốc 2020 nên không dùng như quy mô hiện tại. Nguồn: [DENSO Manufacturing Vietnam](https://www.denso.com/vn/vi/about-us/company-information/dmvn/).

Trang [Linh kiện OEM](https://www.denso.com/vn/vi/business/vietnam-oem/) mô tả một số họ sản phẩm như van VIC và AVS. **Danh mục kinh doanh DENSO không chứng minh từng sản phẩm đều được sản xuất tại cell mà đội khảo sát.** Không tự nói chốt mô phỏng là linh kiện van thật.

🟡 Slide 10/13 nói công đoạn tiền xử lý, linh kiện~10 mm dễ vỡ, dung sai 2 mm. Đây là lời trên slide, chưa có bản vẽ/yêu cầu/đo thời gian tại cell DENSO kèm theo trong repo. Cần lấy mã linh kiện, kích thước/tolerance bản vẽ, hướng đặt, yêu cầu chống xước/bẩn, takt time, số ca và tỷ lệ reject từ mentor. Không tự xác nhận công đoạn tiền rửa hoàn toàn thủ công hoặc lỗi 2–5% chỉ từ ảnh minh họa.

✅ DENSO WAVE có robot 5/6 trục, SCARA, cobot, controller và các ứng dụng lắp ráp/inspection/material handling. Điều này cho thấy công ty đã có nền tự động hóa để so sánh. **Không chứng minh DENSO Việt Nam đang dùng đúng model nào trong cell của đội.** Nguồn: [DENSO WAVE Robotics](https://www.denso-wave.com/en/robot/).

DENSO có chiến lược Factory Automation và giải pháp từ thiết kế tới bảo trì. Từ đó **suy luận** nhóm cần chứng minh giá trị trên toàn vòng đời, không chỉ video gắp đẹp. Nguồn: [Integrated Report2025, Factory Automation](https://www.denso.com/global/en/-/media/Global/about-us/investors/integrated-report_web/2025/pdf-en/081.pdf). Chưa tìm thấy nguồn công khai xác nhận **ACT của nhóm** hoặc **ACT+8 camera+MCR** đã vận hành sản xuất tại DMVN.

## 4. Đối chiếu học thuật/kỹ thuật và cách dùng khi trả lời

| Nguồn gốc | Dùng để giải thích | Không được suy ra |
|---|---|---|
|[ACT,RSS2023](https://roboticsproceedings.org/rss19/p016.html), [codeACT](https://github.com/tonyzhaozh/act)|Action chunks, CVAE, temporal ensemble là nền tảng đã có|Nhóm sáng chế ACT hoặc đạt success của paper |
|[RH20T dataset](https://rh20t.github.io/), [APIconfig](https://github.com/rh20t/rh20t_api/blob/main/configs/configs.json)|CFG5 là Franka, joint 7,2 in-hand serial; schema raw/align|Mọi subset/loader cùng action encoding; bản RLDS cộng đồng không thay schema nhóm |
|[RH20T ACT baseline](https://github.com/rh20t/act_baseline)|Lõi source và cấu hình tham khảo của pipeline|Paper RH20T và pipeline nhóm là cùng thí nghiệm one-shot |
|[MCR,tác giả](https://robots-pretrain-robots.github.io/), [paper](https://arxiv.org/abs/2410.22325), [code](https://github.com/luccachiang/robots-pretrain-robots)|Visual representation pretrain robot, DROID; frozen encoder là lựa chọn có cơ sở|MCR tốt hơn ResNet18 trên task nhóm nếu chưa ablation |
|[MuJoCo docs](https://mujoco.readthedocs.io/en/stable/overview.html), [PandaMenagerie](https://github.com/google-deepmind/mujoco_menagerie/tree/main/franka_emika_panda)|Physics/contact, nguồn robot model|Digital Twin của cell thật đã hiệu chuẩn hoàn chỉnh |
|[DAgger,Ross2011](https://proceedings.mlr.press/v15/ross11a.html)|Distribution shift/compounding error của IL|Nhóm đã triển khai DAgger; source hiện chưa cho thấy |
|[DomainRandomization,Tobin2017](https://arxiv.org/abs/1703.06907)|Randomize mô phỏng là một cách giảm lệch thị giác|Đổi màu/đèn là đủ sim-to-real hoặc đảm bảo generalization |
|[MimicGen](https://mimicgen.github.io/)|Tạo thêm robot demonstrations trong simulator là một hướng nghiên cứu|Nhóm dùng MimicGen; chưa có source chứng minh |
|[DiffusionPolicy](https://diffusion-policy.cs.columbia.edu/)|Sinh action qua denoising, action sequence/receding horizon|Chắc chắn chậm hơn ACT trên hardware/cấu hình nhóm; chưa benchmark |
|[OpenVLA](https://openvla.github.io/)|VLA dùng ảnh/ngôn ngữ/action, mở rộng instruction và tasks|CodeACT hiện có input ngôn ngữ hoặc tự hiểu lệnh văn bản |
|[π0,tác giả](https://www.pi.website/blog/pi0)|Generalist policy kết hợp nền VLM và flow matching action generation|Nhóm đã tích hợp π 0 hoặc VLA luôn tốt hơn task hẹp |
|[FrankaFCI](https://frankarobotics.github.io/docs/overview.html)|API joint/Cartesian và control 1 kHz là ví dụ cho Panda research robot thật|Tay máy ở xưởng là Panda/FCI, hoặc model 10 Hz trực tiếp chạy motor 1 kHz |
|[OSHAIndustrialRobotSystems](https://www.osha.gov/otm/section-4-safety-hazards/chapter-4)|Cần đánh giá rủi ro ở cả integration/operation/maintenance|Đây là chứng nhận an toàn Việt Nam hoặc hệ thống nhóm đã tuân thủ/chứng nhận |

Các kết luận lựa chọn/baseline ở đây là phân tích kỹ thuật của mentor. Nếu muốn nói một giải pháp tốt hơn, cần so cùng dữ liệu/robot/compute và KPI. Không nhập số thành công từ paper vào bảng kết quả nhóm.

### RH20T: camera, tần số và license cần hiểu đúng

Nguồn chính thức công bố RGB 1280×720 ở 10 Hz và bản resize 640×360; có kênh Cartesian 100 Hz trong bảng modality tổng quát. **Dự án resample 10 Hz bằng timestamp**, không dựa số FPS ghi trong MP4 rồi coi mọi stream đồng bộ. CFG5/API xác nhận joint 7, hai in-hand serial 104422070042/135122079702;8 slot cụ thể lấy config nhóm. [Dataset](https://rh20t.github.io/), [configCFG5](https://github.com/rh20t/rh20t_api/blob/main/configs/configs.json).

Trang RH20T phân biệt tập C và NC theo nhóm scene, có điều kiện hạn chế thương mại với phần NC/model học từ đó. **Chưa audit license membership của split joint mới**. Trước pilot thương mại cần đối chiếu scene, license và quyền weights/data với chủ sở hữu; không nói “dataset công khai nên dùng thương mại vô hạn”. Đây là điểm cần xác minh quyền sử dụng theo nguồn, không phải kết luận pháp lý riêng cho dự án. [Điều khoản doRH20T công bố](https://rh20t.github.io/#License).

## 5. Danh mục kiểm tra web và phần chưa tìm thấy

Đã đọcHome, theme, challenges, qa và các bài BTC. Công cụ trích web trả rỗng với SPA nên đã đọc tab vòng 2/criteria/rules trong trình duyệt. URL thử `/rules` không có nội dung đọc được; **route quan sát thật là `/challenges`**, không dựng link thể lệ khác. Đã có rubric 2026 nên không cần lấy rubric 2023 thay thế.

**Không tìm thấy hoặc chưa xác minh:** model robot xưởng; thiết bị thật đã tài trợ cho riêng đội; tolerance 2 mm có văn bản DENSO; baseline lỗi 2–5%; nguồn đo4/16/40 h,120 h,8 h và báo giá 1 tỷ; caseACT/Diffusion Policy triển khai production ở chính DMVN; thí nghiệm few-shot hoặc pretrain ablation của nhóm; đề bài đầy đủ 2024 trong nguồn chính thức đã đọc. Các mục này giữ CHƯA XÁC MINH.

## 6. Cuộc thi quan tâm điều gì → dự án đáp ứng thế nào → còn thiếu gì

| Điều cần chứng minh | Dự án có bằng chứng | Còn thiếu và cách bù |
|---|---|---|
| Tính mới/khác biệt | ✅ Adapter 8 camera, mask, MCR cache, evaluator có code | So sánh với baseline, mô tả đóng góp triển khai thay vì claim thuật toán mới |
| Hiểu kỹ thuật | ✅ Có thể truy input/output, l1/KL, train/infer từ source | Tự giải thích joint/TCP, posterior loss, latency và nhãn proxy |
| Hoàn thiện | ✅ Controller;✅cache;🟡joint train theo báo E25 | Learned joint rollout, metric, video gắn checkpoint, khôi phục lỗi |
| Hiểu nhà máy | 🟡 Slide mô tả công đoạn và linh kiện | Yêu cầu cell/bản vẽ, takt, quality, error baseline, robot model thực |
| Khả thi/kinh tế | 🟡 Có giả định giờ công/ROI | Nhất quán con số, BOM, OPEX, ROI nhạy theo uptime/năng suất; pilot đo thật |
| An toàn/integration | 🟡 Giới hạn mô phỏng/evaluator | RA cho cell thật, interlock, PLC/quality handshake, maintenance và fallback có người phụ trách |

Bằng chứng dự án cho bảng: [J/src/models/mcr_act.py:44](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:44>), [J/src/data/cfg5_masked.py:205](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:205>), [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>), [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>), slide 2/13/21–38. Các thiếu sót cụ thể và thứ tự xử lý nằm ở 06/09.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Lịch web mới khác thông báo khởi động ở hai mốc nào?
2. Năm tiêu chí chấm vòng 2 là gì, đâu là nguồn chính thức?
3. Vì sao biết DENSO có robot không chứng minh robot xưởng là Panda?
4. Phân biệt DiffusionAD, Diffusion Policy và ACT khi nhắc các mùa trước.
5. Chỉ ra một claim kỹ thuật, một claim nhà máy và một claim kinh tế còn thiếu bằng chứng.
