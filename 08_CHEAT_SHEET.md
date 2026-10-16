# 08 — Tờ ôn trước khi trình bày

**Mốc 17/10/2026.** Nhánh hiện tại: **joint/MCR**. E25 theo người dùng; chưa có metric/rollout mới để kiểm độc lập.[E1] Bản PDF kèm theo được dàn đúng một trang A4.

**Sơ đồ cần vẽ:** CFG5 joint/RGB → causal 10 Hz + split/train stats → MCR frozen/cache → ACT train → checkpoint → infer z=0 → **joint executor còn cần nối** → Panda/MuJoCo → evaluator. Demo task đích hiện là TCP, cần nhãn joint phù hợp.[E1–E3]

## 10 mốc cần nhớ

| Mốc | Cách nói đúng |
|---|---|
|7 joint + kẹp=8D|Absolute q rad và width m, không TCP pose.[E2]|
|8 slot camera|6 ngoài+2 in-hand; có thể thiếu view, dùng mask.[E2]|
|10 Hz|Grid data/policy; không phải motor Hz đo thật.[E2]|
|K=20|Chunk nhãn 2 giây; không suy ra query frequency.[E2]|
|β=10|L1+10KL trong config nền; chưa KL Sweep.[E2]|
|1317 CFG5 episode|1053 train/132 val/132 test theo log cache.[E1]|
|913 demo accepted|Manifest task đích; không giữ claim 1000 đều đạt.[E3]|
|3/3 và 0/10|Controller 3 seed đạt; TCP ACT E5 transfer 0/10; khác nhánh joint mới.[E3]|
|15 task|Hòa vốn engineering hours, giả định 16 n=120+8n.[E3]|
|22,2 tháng|1 tỷ/(3×15 triệu), chưa OPEX; chưa phải số đo thực tế.[E3]|

## 5 thuật ngữ

**Action chunking:** một observation dự đoán cả đoạn action. **CVAE:** train posterior từ state+target, latent 32; inference z=0. **Imitation learning:** học từ observation/action demo. **Domain randomization:** biến thiên mô phỏng có kiểm soát, chưa bảo chứng robustness. **Sim-to-real:** khoảng cách ảnh, vật lý, động học và timing.[E2/E3]

## Mở đầu 60 giây

“Nhóm EDABK_TriH nghiên cứu robot học gắp–đặt từ dữ liệu để hướng tới giảm công cấu hình khi thay đổi linh kiện. Bài thử hiện tại là Panda trong MuJoCo đặt ba chốt vào khuôn. Nhánh mới dùng MCR trích đặc trưng ảnh nhiều camera, rồi ACT kết hợp với trạng thái khớp để dự đoán chuỗi hành động. Nhóm đã có mô phỏng, evaluator và cache dữ liệu; phần nối joint policy vào task và đánh giá closed-loop còn cần hoàn thiện. Chúng em sẽ tách rõ kết quả controller, thử nghiệm ACT cũ và mục tiêu tiếp theo, rồi trình bày điều kiện để pilot tại DENSO.”[E1–E3]

## Kết thúc 30 giây

“Điểm nhóm muốn chứng minh tiếp là policy học có thể thực hiện task với tỷ lệ thành công, chất lượng và thời gian đo được. Nhóm chưa coi few-shot, robot thật hay ROI là kết quả đã đạt. Bước ưu tiên là chốt contract joint, đo rollout và thống nhất robot cùng baseline cell với kỹ sư DENSO.”[E1/E3]

**Tuyệt đối không nói:** “ACT 100%”; “đã few-shot”; “1000 demo đều đạt”; “loss là mm”; “eval tự động z=0”; “đổi robot là chạy”; “24/7 đã chứng minh”; “15 task=15 tháng”; “E100 xong”; “0/10 là kết quả MCR mới”.

**Căn cứ:** [E1] [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>), [R/BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:19](<F:/cfg5_mophong/BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:19>). [E2] [J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>), [J/configs/act/rh20t_all8.json:1](<F:/cfg5_mophong/local_source_(1)/configs/act/rh20t_all8.json:1>), [J/src/data/cfg5_masked.py:205](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:205>). [E3] [J/data/splits/pick_place_finetune_manifest.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_manifest.json:1>), [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>), [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>), S2/31/38, phân tích trong 06.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Input/output là gì?
2. Vì sao CVAE train khác infer?
3. Controller khác policy ở đâu?
4. Chưa chứng minh điều gì?
5. Bước nghiệm thu tiếp theo là gì?
