# 09 — Việc ưu tiên và kịch bản 30 phút

Giới hạn 30 phút do bạn cung cấp trong chat 17/10. Lịch thuyết trình trên web hiện 17/11/2026, khác thông báo khởi động 16/11; cần chốt lại bằng thông báo đội. [Vòng thi chính thức](https://densohackathon.vn/challenges), truy cập 17/10/2026. Đừng nhầm với demo video tối đa 15 phút.

## Top 5 việc nên làm trước ngày thuyết trình

Thời gian dưới đây là **ước lượng của mentor cho công việc**, không phải số đo hay cam kết hoàn thành. Lượt này chỉ tạo tài liệu, không chạy các thí nghiệm đó.

| Ưu tiên | Việc cụ thể | Thời gian ước lượng | Đầu ra có thể kiểm |
|---|---|---|---|
|1|**Chốt snapshot nhánh joint mới và sửa claim slide.** Lấy metadata/config/history/log/checkpoint hash đúng run; xác minh E25/E100/job14597/14598. Sửa S12/16/18/42 cho joint MCR, S17 cho số demo, S28 MuJoCo, S2/35–38 cho ROI/claim chưa đo.|2–4 giờ nếu truy cập được artifact; sửa slide 1–2 giờ riêng|Một bảng status gắn checkpoint/contract, một bộ slide nhất quán; nếu thiếu log thì giữ CHƯA XÁC MINH. |
|2|**Đóng khoảng trống joint/TCP bằng kiểm tra nhẹ trước.** Chốt state/action/offset/stats, ghi joint demo phù hợp; viết/kiểm observation joint, executor joint, unit/limits và tracking. Không đưa output joint qua env TCP cũ.|0,5–2 ngày kỹ thuật, có thể lâu hơn nếu thiếu generator/data|Một record t→target có giá trị/đơn vị rõ; trace q_ref/q_measured/width, timestamp; không cần train dài để phát hiện semantics lỗi. |
|3|**Lấy một báo cáo learned joint rollout thật.** Chọn checkpoint qua validation; development rollout với seed đã khóa, ghi N/N, failure reason, cycle time, clip/timeout và video. Sau khi chốt protocol mới dùng test cuối.|Chuẩn bị 0,5 ngày; compute tùy thời gian episode/inference, **không dự báo throughput chưa đo**|Tối thiểu một pilot có N khác seed báo đúng phạm vi; nếu chạy 10 episode thì chỉ nói 10 episode, không gọi industrial proof. |
|4|**Chốt robot xưởng, yêu cầu quality và baseline chi phí cùng mentor.** Model 6/7 trục, gripper/API, camera/tool calibration, takt, linh kiện/dung sai, force, ca/nhân công, BOM/OPEX.|Soạn bảng 30–60 phút; buổi làm việc 30–60 phút; thời gian chờ phụ thuộc xưởng|Đặc tả 1 cell và ma trận 6 trục/7 trục; nguồn cho dữ liệu kinh tế; safety/quality gate có người phụ trách. |
|5|**Nếu còn thời gian, làm ablation nhỏ thay vì thêm claim.** Sau khi dữ liệu joint/rollout đúng, so có/không pretrain hoặc subset camera; chọn một câu hỏi đủ scope. Tập pitch và Q&A sau khi chốt con số.|Thiết kế 2–4 giờ; runtime theo pilot thực, có thể vượt một ngày; luyện 2 buổi×60–90 phút|Một so sánh cùng data/budget/protocol hoặc ghi rõ chưa có; mỗi người tự vẽ sơ đồ và trả lời câu khó không né tránh. |

Nguồn ưu tiên: [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) [H/chat:5810](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5810>), [J/src/simulation/panda_env.py:113](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:113>), [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>), [J/src/data/sim_demos.py:89](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:89>), [J/data/splits/pick_place_finetune_manifest.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_manifest.json:1>), [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>).

Nếu chỉ còn một ngày: làm ưu tiên 1 và bảng yêu cầu cell ở4; kiểm contract ở2 trong phạm vi ngắn; **không bỏ qua kiểm semantics để chạy robot hoặc train nặng**. Chưa có rollout thì báo trung thực là chưa có, kèm plan, không lấy số controller thay thế.

## Đề xuất chia 30 phút

Chưa biết 30 phút bao gồm Q&A hay không. Chuẩn bị hai phiên bản, không cần chờ câu trả lời để tập:

| Phần | Nếu 30 phút gồm Q&A: nói 20 phút+10 phút Q&A | Nếu 30 phút chỉ pitch |
|---|---:|---:|
|Mở đầu, team rất ngắn, problem cell/S2/10/13|3 phút|4 phút|
|Pipeline, mới/cũ, ACT, input/output/S12/15/16/18|6 phút|8 phút|
|Dữ liệu/quality/split/S17/19|3 phút|4 phút|
|Kết quả và giới hạn/controller, TCP cũ, joint mới/S42|3 phút|4 phút|
|Kinh tế một mô hình giờ công, một case payback/S29/31–34/38|2,5 phút|4 phút|
|Robot 6/7 trục, safety, lộ trình/gate/S40|2 phút|4 phút|
|Kết thúc|0,5 phút|1 phút|
|Dự phòng chuyển slide/trục trặc|Đã gộp trong các đoạn, nên rehearse 19–20 phút|1 phút|

Các cột là **đề xuất phân bổ**, không phải thể lệ BTC. Tổng pitch 20 phút hoặc 30 phút đúng cột tương ứng. Không đọc hết 43 slide với cùng thời lượng. S4–8 rút gọn 20–40 giây nếu cần; S23–28/S30/S33 dùng backup để giải thích khi được hỏi, nhưng vẫn học đủ theo 05.

## Thứ tự trình bày để tránh nhầm phiên bản

1. Nêu task và tiêu chí thật của mô phỏng; chưa đồng nhất với linh kiện DENSO.
2. Đưa sơ đồ joint MCR hiện tại; trình bày rõ hai điểm cần nối ở demo đích và controller.
3. Nêu kết quả theo run: controller 3/3; E5 TCP transfer 0/10; cache 1317; joint E25 theo báo, chưa metric mới.
4. Giải thích hướng đo tiếp và baseline. Sau đó mới trình bày lợi ích kỳ vọng, giả định kinh tế và roadmap.

Tất cả con số bước 3 có nguồn trong 00/01; không xem chúng là cùng một run hoặc cùng model. Lịch sử thiết kế là cách giải thích vì sao nhóm đổi hướng, không là lý do để bỏ qua lỗi không đạt.

## Bộ bằng chứng nên mở sẵn khi pitch

- Bảng hiện trạng và link checkpoint/config đúng run; nếu chưa có thì chỉ ra ô trống.
- Hai ảnh/sơ đồ phân biệt TCP 8D và joint 8D, từ 03.
- Báo cáo N/N cùng seed, video có label controller/learned và checkpoint ID.
- Manifest 913 accepted/111 rejected và split 731/91/91 của TCP demo; split joint 1053/132/132 khác tập đó.
- Bảng giả định kinh tế: engineering rate, wage, CAPEX, OPEX, mẫu số thay người; không lấy giá trị của paper làm kết quả đội.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Nếu chỉ còn 24 giờ, việc nào giúp tăng độ tin cậy nhất?
2. Gate nào phải đạt trước khi báo một learned rollout?
3. Nếu Q&A nằm trong 30 phút, tôi rút phần nào của deck?
4. Tôi có mở được bằng chứng cho từng con số định nói không?
5. Một người khác trong đội có thể giải thích lại joint/TCP và ROI đúng như tôi không?
