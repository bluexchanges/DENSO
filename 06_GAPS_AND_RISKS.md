# 06 — Mâu thuẫn, khoảng trống và rủi ro bị hỏi

Đánh giá ngày 17/10/2026, ưu tiên ghi chép mới nhất. Mức **Cao / Trung bình / Thấp** dưới đây là nhận định của mentor về khả năng bị hỏi và hậu quả nếu trả lời sai, không phải xác suất thống kê. “Chưa có bằng chứng” được giới hạn trong source/log/chat đã kiểm, không kết luận một việc chưa từng xảy ra ở mọi nơi.

## 1. Bảng rà soát nghiêm khắc

| ID / vấn đề | Kết luận và bằng chứng | Khả năng hỏi / hậu quả trả lời sai | Sửa slide hoặc câu trả lời trung thực |
|---|---|---|---|
| G01 — Pose tay trên S16/18 so với joint mới | **Xác nhận lệch phiên bản.** Bạn chốt joint ngày 11/10; source dùng 7 joint+width. [H/chat:3568](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:3568>) [J/src/data/cfg5_masked.py:227](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:227>) | Cao / Cao | Sửa output thành “chuỗi góc khớp + độ mở kẹp”; chú thích nhánh TCP là thử nghiệm trước. |
| G02 — Joint policy nối vào API TCP | **Khoảng trống hiện tại.** `observation()` trả TCP 8D; `validate_action()` nhận xyz+wxyz+width. Chưa thấy joint bridge đã chạy. [J/src/simulation/panda_env.py:113](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:113>) [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>) | Cao / Cao | “Model và simulator cùng 8D nhưng khác semantics; nhóm đang hoàn thiện adapter joint trước rollout.” Không chạy trực tiếp nhãn joint qua API TCP. |
| G03 — Demo đích còn TCP, nhánh mới joint | **Chưa tương thích.** `sim_demos.load_trajectory` đọc measured/commanded TCP; nhãn joint lấy 7 góc đo tương lai. [J/src/data/sim_demos.py:89](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:89>) [J/src/data/cfg5_masked.py:237](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:237>) | Cao / Cao | Ghi/đọc joint thật trong demo, chốt offset/units/stats, rồi mới fine-tune. Không nói “chỉ đổi checkpoint”. |
| G04 — “1.000 demonstration mô phỏng đạt” S17 | **Chưa được chứng minh; manifest hiện không khớp.** 913 accepted,111 rejected:24 failure và 87 video lỗi/thiếu frame. [J/data/splits/pick_place_finetune_manifest.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_manifest.json:1>) | Cao / Cao | Ghi “manifest hiện có 913 episode dùng được, đang chuẩn hóa chất lượng”, kèm điều kiện. Không gọi 913/1024 là success rate controller. |
| G05 — Nhóm đã chứng minh học tổng quát S42 | **Vượt bằng chứng.** TCP có train/val; E5 transfer 0/10. Joint mới có lời báo E25, chưa loss/rollout. [R/checkpoints/before_test_20261007_142338/history.json:1](<F:/cfg5_mophong/checkpoints/before_test_20261007_142338/history.json:1>) [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>) [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) | Cao / Cao | “Đã có pipeline và kiểm tra học/inference; còn phải đo generalization và closed-loop của nhánh mới.” |
| G06 — Overfit-test một vài mẫu? | **Chưa thấy một thí nghiệm overfit nhỏ đạt đủ điều kiện.** TCP run lưu có 531 train/66 val, không phải 1 episode. Validation có target posterior. [J/src/training/pretrain.py:283](<F:/cfg5_mophong/local_source_(1)/src/training/pretrain.py:283>) | Cao / Cao | Không tự bịa số mẫu/loss overfit. Tách smoke, posterior reconstruction, prior prediction và rollout. |
| G07 — 100% thành công từ demo? | **Controller 3/3 có thật, ACT cũ 0/10 có thật, nhánh mới chưa có N/N.** [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>) [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>) | Cao / Cao | Mỗi video ghi rõ controller/ACT, checkpoint, seed, điều kiện và N. Không mượn 3/3 làm success của policy. |
| G08 — 20 tháng /16–18 tháng /15 task | **Ba số không cùng mô hình, hai số tháng còn khác giả định.** S2:1000/(3×15)=22,22 tháng; S38 gần case 18–20 triệu/người. S32 là engineering hours. | Cao / Cao | Giữ một bảng giả định rõ. “15 task là hòa vốn công triển khai; payback robot là mô hình tiền riêng, hiện chưa xác nhận.” |
| G09 — Lương 15 /18–20 triệu /250k/h | **Chưa đủ để gọi mâu thuẫn bản chất nếu khác role/cost basis**, nhưng slide chưa giải thích. S21 nói công kỹ sư, S2/36 nói công nhân. | Cao / Cao | Định nghĩa engineering rate, base wage, fully loaded labor riêng và trích nguồn. Nếu cùng role thì phải thống nhất số. |
| G10 — 7 DOF và 6 trục | **Panda mô phỏng 7 khớp xác minh.** Kinh nghiệm 6 trục S2 không tự mâu thuẫn với Panda nhưng gây hiểu nhầm; robot xưởng chưa biết. [J/src/simulation/panda_controller.py:34](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:34>) | Cao / Cao | “Mô phỏng hiện Panda 7 DOF; thiết bị thật sẽ chốt model với xưởng.” Trình bày kế hoạch cho cả 6 và 7 trục ở mục 3. |
| G11 — Isaac Lab S28 | **Repo thực dùng MuJoCo; chưa tìm implementation Isaac Lab** trong nhánh khảo sát. [J/src/simulation/panda_env.py:1](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:1>) [J/requirements-sim-lock.txt:1](<F:/cfg5_mophong/local_source_(1)/requirements-sim-lock.txt:1>) | Cao / Trung bình | Sửa “MuJoCo, pipeline dữ liệu/training và chuẩn bị sim-to-real”. Nếu Isaac chỉ tham khảo thì ghi rõ. |
| G12 — 24/7, độ chính xác cao, lỗi thủ công 2–5% | **Chưa có uptime, takt, reject baseline hay precision của policy mới.** S35 là kỳ vọng. | Cao / Cao | Thay bằng mục tiêu đo; không dùng spec repeatability robot làm accuracy hệ thống. |
| G13 — Linh kiện dễ vỡ và force | **Policy chỉ joint/width, không force head.** Giới hạn 20 N trong config không chứng minh kẹp an toàn trên vật thật. [J/src/models/mcr_act.py:137](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:137>) [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>) | Cao / Cao | “Chưa chứng minh với vật dễ vỡ; cần đo force/contact, thiết kế gripper và thử nghiệm chất lượng.” |
| G14 — Few-shot/đa tác vụ | **Mới là mục tiêu về khả năng.** Có pretrain data nhiều task nhưng chưa task-success benchmark hay N-demo curve/ablation. S19 dùng “hướng tới”. | Cao / Cao | Không nói model đã few-shot. Đề xuất N=5/10/25/50 là protocol, không kết quả. |
| G15 — Pretrain chắc giúp fine-tune | **Chưa có so sánh có/không pretrain** trên cùng task, seed, số demo. MCR paper không kiểm cấu hình nhóm. [J/src/models/mcr_act.py:44](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:44>) | Cao / Cao | “Nhóm chọn pretrain có cơ sở nghiên cứu, lợi ích trên task nhóm còn phải đo.” |
| G16 — Held-out và OOD | **Có split theo group/seed; không tự chứng minh unseen-position/OOD.** [J/src/data/splits.py:77](<F:/cfg5_mophong/local_source_(1)/src/data/splits.py:77>) [J/src/data/sim_demos.py:230](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:230>) | Cao / Cao | Nêu split chính xác và thêm tập evaluation vị trí/ánh sáng/vật chưa thấy; test chỉ dùng sau khóa cấu hình. |
| G17 — Giữ mọi rating trong CFG5 mới | **Có thật.** Script bỏ min_rating, không dùng human; 4 missing joint là ngoại lệ riêng. [J/scripts/prepare_cfg5_masked_mcr.py:35](<F:/cfg5_mophong/local_source_(1)/scripts/prepare_cfg5_masked_mcr.py:35>) | Trung bình / Cao | Nhận rủi ro học quỹ đạo lỗi. Cần phân tích theo quality/task và ablation lọc; không gọi mọi 1317 episode là expert thành công. |
| G18 — Camera thiếu và 8 camera ngoài đời | **Mask được cài và synthetic check đạt; robustness chưa chứng minh.** Log camera có nhiều episode/tick thiếu view. [J/src/models/mcr_act.py:100](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:100>) [H/chat:5394](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5394>) | Cao / Cao | “8 slot là schema, không phải 8 view thật ở mọi tick; cần ablation số view và đo rig ngoài đời.” |
| G19 — MCR INT8/crop ảnh với chốt nhỏ | **Có quantization và center 224 crop**, cache log max feature error≈0,05795; chưa liên hệ task error. [J/src/models/mcr_act.py:25](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:25>) [J/src/data/feature_cache.py:133](<F:/cfg5_mophong/local_source_(1)/src/data/feature_cache.py:133>) | Trung bình / Trung bình | Đo FP32 feature vs INT8 và crop/resize; đừng chuyển feature error thành mm/degree. |
| G20 — 3–6 tháng vs T1–T8 | **Không xác nhận là mâu thuẫn chắc chắn.** Hình S40 core T1–T5, mở rộng T6–T8, công việc song song. | Trung bình / Trung bình | Chú thích core≈5 tháng và phần mở rộng, mốc nghiệm thu; không cộng duration các dòng hoặc chỉ đếm 8 cột. |
| G21 — Vốn 1 tỷ và bảo trì thấp | **Chưa BOM/báo giá/OPEX.** S2/36/38 không ghi cấu phần đầu tư. | Cao / Cao | Dùng kịch bản minh họa, tách CAPEX/OPEX/engineering và giá trị tái dùng robot có sẵn. |
| G22 — Thay 3 công nhân | **Chưa capacity study.** Không biết 3 người song song hay 3 ca; không biết cycle time, yield, loading. | Cao / Cao | “Tiềm năng giảm thao tác thủ công, mức thay thế chỉ tính sau pilot.” Nếu điều chuyển người thì không mặc định là cash saving. |
| G23 — Thời gian 30 phút/lịch 16–17/11 | **30 phút do bạn xác nhận; web mới 17/11 khác bài khởi động 16/11.** [BTC](https://densohackathon.vn/challenges) | Trung bình / Cao | Chốt lịch bằng thông báo đội. 15 phút demo video trên web là giới hạn khác với 30 phút pitch. |
| G24 — License dữ liệu | **Chưa audit quyền thương mại.** RH20T phân biệt C/NC; joint pretrain mới có mở rộng scene. [RH20T](https://rh20t.github.io/) | Trung bình / Cao | Đối chiếu scene/license/weights trước pilot thương mại, không nói “public=free commercial”. |
| G25 — Resume E100/đồ thị đã xong? | **CHƯA XÁC MINH.** Bạn báo E25; cuối chat job14598 còn Pending, sau đó yêu cầu hủy. [A/latest_thread_snapshot.json:1](<F:/Denso/docs_denso_hack/_audit/latest_thread_snapshot.json:1>) | Trung bình / Cao | “Đã chuẩn bị/cài patch theo log, chưa có log xác nhận E100 hay plot mỗi epoch.” Không đổi “lệnh đưa ra” thành “job đã chạy”. |
| G26 — Tự động đếm/MES/truy xuất S36 | **Có metric mô phỏng, chưa chứng minhPLC/MES production integration.** [J/src/simulation/panda_evaluator.py:65](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:65>) | Cao / Cao | Tách simulate logging khỏi kiểm tra quality/phần mềm nhà máy, bổ sung handshake và reject path. |

## 2. Ba mô hình kinh tế cần tách riêng

### A. Engineering effort khi triển khai nhiều task

Theo slide 31: H_trad=16n, H_AI=120+8n. Hòa vốn tại 15 task,240 h/cách. Các hệ số là **giả định**, không có time-study. Công thức tổng quát n*=H_setup/(h_trad−h_AI), chỉ có điểm hòa vốn dương khi h_trad>h_AI và platform thật sự tái sử dụng được.

### B. Payback đầu tư cell robot

`Payback_months = CAPEX / net_benefit_per_month`.

Trong đó net benefit cần tính **lợi ích lao động thực sự tránh được + tăng thông lượng/giảm phế phẩm quy thành tiền − điện/compute/bảo trì/giám sát/downtime**. Không được cộng hai lần lợi ích của cùng một cải tiến. Nếu chỉ chuyển người sang việc khác thì cần báo lợi ích capacity/cost avoidance cụ thể, không ghi giảm chi lương mặc định.

| Giả định minh họa | Tiết kiệm gộp | Payback đơn giản với 1 tỷ |
|---|---:|---:|
|3 người×15 triệu/tháng|45 triệu/tháng|22,22 tháng|
|3 người×18 triệu/tháng|54 triệu/tháng|18,52 tháng|
|3 người×20 triệu/tháng|60 triệu/tháng|16,67 tháng|

Chưa OPEX trong mọi dòng; lợi ích ròng nhỏ hơn gộp sẽ kéo dài payback, nếu giữ các giả định khác. Nếu net benefit≤0 thì chưa có payback hữu hạn theo mô hình này. Đây là tính số minh họa từ slide, không tư vấn đầu tư hoặc dự báo chắc chắn.

### C. Công lập trình tiết kiệm không phải lương công nhân tiết kiệm

250k/h×160 h=40 triệu là engineering cost quy đổi. Không lấy mức này làm lương người vận hành 15 triệu. Muốn nói 18–20 triệu là fully loaded cost cần có nguồn xác nhận, thay vì tự suy bảo hiểm/overhead để vá mâu thuẫn.

**Câu trả lời nên dùng:** “Nhóm tách mô hình tiết kiệm công kỹ sư với mô hình đầu tư thay thao tác thủ công. Điểm 15 task thuộc mô hình thứ nhất; phần tháng payback còn là giả định cần chốt lại lương, OPEX và thông lượng với xưởng.”

## 3. Triển khai thật: cả 6 trục,7 trục và Panda đang mô phỏng

Loại robot xưởng hiện **CHƯA XÁC MINH** theo trả lời của bạn 17/10. Không đặt tên robot hoặc giao diện chỉ dựa vào số trục.

| Tình huống | Có thể tái dùng | Cần thay/kiểm | Không được hứa |
|---|---|---|---|
| **A. Robot 6 trục ở xưởng, khác Panda** | Pipeline đọc ảnh, tư duy chunk/CVAE, split/evaluator design, có thể thử visual weights | Model URDF/MJCF, joint order/limits, state/action dim thường 6+gripper=7 nếu chọn joint, head/projection/stats, data/action semantics mới, driver API/calibration/cell validation | “Bỏ joint thứ 7 rồi chạy”; “giữ head 8D như cũ là được”; sim-to-real trực tiếp joint Panda |
| **B. Robot 7 trục khác Panda** | Có thể giữ kích thước state/head 8D như khung | 7 DOF không đồng nghĩa cùng link length, zero offset, sign/limits, gripper, tool frame, dynamics và appearance; cần retarget/data/fine-tune/driver | “Cùng 7 trục nên checkpoint dùng ngay” |
| **C. Panda/Franka cùng loại với mô phỏng** | Gần hơn về topology, có thể giữ joint order 8D sau khi đối chiếu | Chốt đúng model/firmware/FCI, joint zero/order, tool/load/gripper, camera/time, dynamics, rate/safety; học/thử trên real data phù hợp | “Cùng Panda nên không còn sim-to-real gap”;“model 10 Hz gửi motor tự do” |
| **D. “Tay của tôi” đang nói tới Panda trong repo** | ✅ Xác minh được mô phỏng Panda 7 khớp | Nối observation/executor joint mới vào env cũ TCP, rồi mới đo learned rollout | Gọi mô hình 3D đó là Panda thật đang có trong xưởng |
| **E. Nếu ý bạn là MG400 trong chat/project cũ** | Có thể tái dùng ý tưởng camera IL; chưa xác minh đó là hardware bạn sở hữu | MG400 là 4 trục theo hãng, cần thu hẹp task về workspace/orientation khả thi và representation 4 joint+tool phù hợp | Gọi MG400 là robot 6/7 trục; điều khiển pose 6 DOF tùy ý |

Nguồn Panda hiện tại: [J/src/simulation/panda_controller.py:34](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:34>), [J/mujoco/models/franka_emika_panda/manifest.json:1](<F:/cfg5_mophong/local_source_(1)/mujoco/models/franka_emika_panda/manifest.json:1>). Ví dụ FCI thật hỗ trợ joint/Cartesian và 1 kHz: [Frankaofficial](https://frankarobotics.github.io/docs/overview.html). MG400 4 axes: [Dobotofficial](https://de.dobot-robots.com/products/desktop-four-axis/mg400.html). Truy cập 17/10/2026. Tình huống A/B/E là kế hoạch phân tích, không phần mềm đã triển khai.

TCP là frame/điểm làm việc của dụng cụ, không tự nó là “hệ tọa độ toàn cục”. Cần chọn robot base để mô tả pose, định nghĩa world→base và flange→TCP. Với 7 DOF, cùng TCP pose có thể nhiều nghiệm joint; không ghép một bộ joint Panda sang robot khác chỉ bằng đổi đơn vị.

## 4. Sim-to-real và khả thi rig camera

| Khoảng cách | Hiện có | Cần đo/kiểm trước khi nói đã giải quyết |
|---|---|---|
| Ảnh | 🟡 Simulation và MCR pretrained; crop/JPEG/INT8 | Real image held-out; thay đổi chiếu sáng/phản xạ/occlusion; so ít camera và độ phân giải phù hợp |
| Động học | ✅ Panda Menagerie; TCP ảo và IK | Kích thước/zero/tool calibration thật; tracking error và độ lặp |
| Tiếp xúc | ✅ Contact/friction trong MuJoCo | Friction/compliance/backlash, force khi insert; vật dễ vỡ/xước/biến dạng |
| Thời gian | ✅ Grid 10 Hz và physics 1 kHz mô phỏng | Capture→sync→preproc→GPU→driver latency p50/p95, deadline miss, buffer age |
| Camera 8 view | ✅6external+2 in-hand trong rig source | BOM, không gian lắp, USB/network bandwidth, trigger/PTP hoặc đồng bộ phù hợp, intrinsic/extrinsic, hand-eye calibration và recalibration |
| Thiếu camera | ✅ Attention mask và camera dropout | Ablation mất view, tracking causal age; phương án khi mọi view mất |
| Chất lượng | ✅ Simgeom/contact evaluator | Kiểm tra đúng sản phẩm ở đầu ra, independent vision/sensor/gauge và reject/rework |

Domain randomization hiện là 🟡 bằng chứng profile/ảnh, chưa audit đầy đủ code generator/range. Đổi màu, nềnvàđèn không ngẫu nhiên hóa ma sát, khối lượng, độc ứng hay trễ. Không tự nói D R đã xử lý dynamics gap. Cơ sở nghiên cứu: [Tobin2017](https://arxiv.org/abs/1703.06907), truy cập 17/10/2026.

## 5. An toàn, tích hợp và vận hành

Đây là **kế hoạch tích hợp cần kỹ sư xưởng phê duyệt theo quy trình của họ**, không là chứng nhận hoặc thiết kế an toàn đã hoàn thành. Dùng hướng dẫn chính thức về risk assessment làm nền: [OSHAIndustrialRobotSystems](https://www.osha.gov/otm/section-4-safety-hazards/chapter-4), truy cập 17/10/2026; không coiOSHA là luật/chuẩn nghiệm thu tự động áp dụng cho cell Việt Nam.

| Rủi ro | Khả năng hỏi / hậu quả | Phương án trả lời trung thực và yêu cầu tiếp theo |
|---|---|---|
| Người vào vùng chuyển động, khởi động lại bất ngờ | Cao / Cao | ⬜ Cần RA, toàn cell guard/interlock, E-stop, safe enable/restart theo robot và xưởng; AI không được quyết định chức năng safety. |
| Gắp hụt/rơi vật, kẹp sai | Cao / Cao | 🟡 Sim có grasp/drop flags. ⬜ Real cần xác nhận grasp, đặt và quality; stop/reject có kiểm soát, thử lại giới hạn và gọi người, không retry vô hạn. |
| Kẹt khi insert, vật dễ vỡ | Cao / Cao | ⬜ Chốt force limits/compliance, gripper/tool thiết kế, ngưỡng dừng thử nghiệm; chưa đo lực thật. |
| Ảnh cũ/mất camera/GPU chậm | Cao / Cao | ✅ Data pipeline có maskage. ⬜ Online watchdog giữ/dừng theo interface an toàn của hệ thống; kỷ luật timestamp/deadline; không gửi lệnh mới khi không đủ observation. |
| PLC/MES không đồng bộ | Cao / Cao | ⬜ Cell state machine với Ready/Busy/Done/Fault, partID, recipe/version, quality ack, timeout; hiện tại chưa có integration report. |
| Bảo trì, calibration drift | Trung bình / Cao | ⬜ Lịch kiểm calibration/gripper, versioned model và rollback, golden part test, operator SOP; chi phí chưa đo. |
| Model thay đổi không kiểm soát | Trung bình / Cao | ✅ Checkpoint contract trong train. ⬜ Deployment approval/locked version, held-out regression và rollback; không online learning tự động trên cell thật. |
| Bảo mật dữ liệu/giấy phép | Trung bình / Cao | ⬜ Chốt quyền dataset/weights, hạn chế truy cập và đường truyền theo xưởng; chưa tự gửi data DENSO ra API ngoài. |

## 6. Những câu phải thay ngay

- “Đã chứng minh học thật/tổng quát” → “Đã thực hiện train/validation và một số kiểm tra inference; generalization/closed-loop của nhánh mới cần đánh giá.”
- “ACT gắp đạt 100%” → “Controller scripted đạt 3/3 seed; ACT TCP cũ E5 transfer 0/10; chưa cóN/N của joint mới.”
- “1.000 demo đạt” → “Manifest hiện tại chấp nhận 913 episode; cần chốt chất lượng và phạm vi bộ dữ liệu.”
- “Chỉ thay cánh tay mô phỏng là chạy được” → “Thay robot cần representation, data, calibration, driver và safety validation phù hợp.”
- “Few-shot giúp làm quen nhanh” → “Few-shot là mục tiêu sẽ đo bằng đường cong N-demo và baseline.”
- “Hoàn vốn 16–18 tháng” → “Kịch bản kinh tế phụ thuộc CAPEX/lợi ích ròng; case 15 triệu/người thì 22,2 tháng chưa OPEX.”
- “Có lực kẹp 20 N nên xử lý vật dễ vỡ” → “Policy chưa dự đoán lực; fixed force limit không thay thế thử nghiệm vật liệu.”

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Ba khoảng trống kỹ thuật nghiêm trọng nhất của nhánh joint là gì?
2. Phản biện vì sao 15 task,20 tháng và 16–18 tháng không thể đặt ngang nhau.
3. Nếu robot xưởng 6 trục, giữ được gì và phải thay gì?
4. Vì sao không dùng 3/3 controller hoặc spec repeatability để chứng minh accuracy ACT?
5. Khi bị hỏi safety/few-shot/real robot, nói đãX, chưa Y, kế hoạch Z, nghiệm thu W như thế nào?
