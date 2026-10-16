# Bộ tài liệu tự bảo vệ dự án EDABK_TriH

Chốt phạm vi kiểm tra: **17/10/2026, Asia/Bangkok**. Đọc theo thứ tự 01 → 02 → 03 để hiểu hệ thống, 05 → 06 để sửa lời trình bày, rồi 07 để luyện. 08 có bản in một trang. 09 là lịch nói trong 30 phút và việc ưu tiên. Chưa bắt đầu hỏi đáp. Khi bạn gõ **bắt đầu luyện Q&A**, hỏi từng câu trong 07, đợi trả lời rồi chấm.

## Mở tài liệu

| File | Nội dung |
|---|---|
| [01 — Bản đồ dự án](<F:/Denso/docs_denso_hack/01_PROJECT_MAP.md>) | Pipeline, module, task và dòng thời gian quyết định |
| [02 — Hiểu ACT](<F:/Denso/docs_denso_hack/02_ACT_EXPLAINED.md>) | Trực giác, CVAE, công thức, cấu hình và train/inference |
| [03 — Input/output và code](<F:/Denso/docs_denso_hack/03_IO_AND_CODE.md>) | Shape, đơn vị, Hz, ví dụ dữ liệu thật, joint/TCP |
| [04 — Bối cảnh và nguồn](<F:/Denso/docs_denso_hack/04_CONTEXT_AND_SOURCES.md>) | Cuộc thi, DENSO và tài liệu gốc đã tra cứu |
| [05 — Giải thích slide](<F:/Denso/docs_denso_hack/05_SLIDE_GUIDE.md>) | Đối chiếu 35 slide nội dung trong bộ 43 slide |
| [06 — Khoảng trống và rủi ro](<F:/Denso/docs_denso_hack/06_GAPS_AND_RISKS.md>) | 26 điểm cần sửa; robot 6/7 trục, Panda và trường hợp MG400 |
| [07 — Ngân hàng Q&A](<F:/Denso/docs_denso_hack/07_QA_BANK.md>) | 60 câu, đáp án, bằng chứng và 10 câu nguy hiểm nhất |
| [08 — Tờ ôn](<F:/Denso/docs_denso_hack/08_CHEAT_SHEET.md>) / [PDF một trang](<F:/Denso/docs_denso_hack/08_CHEAT_SHEET.pdf>) | Sơ đồ, 10 mốc, 5 thuật ngữ, mở đầu và kết thúc |
| [09 — Việc ưu tiên và 30 phút](<F:/Denso/docs_denso_hack/09_PRIORITY_AND_30MIN.md>) | Top 5 việc cần làm và hai phương án chia thời gian |

## Kết luận cần biết trước

**Hiện trạng mới nhất là nhánh joint với MCR, không phải nhánh TCP trên slide.** Ngày 11/10 bạn chọn “Train bằng 7 góc khớp + độ mở kẹp” sau khi phục hồi TCP bằng FK chưa đạt. Ngày 16/10 bạn báo đang ở E25 và yêu cầu tiếp tới tổng E100. Chưa có history/loss E25 hay checkpoint joint mới nhất để đọc trực tiếp trên máy này. Vì vậy “đã tới E25” được ghi là lời báo của người dùng, không biến thành một phép kiểm độc lập. [H/chat:3568](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:3568>) [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) [H/chat:5810](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5810>)

Mốc cuối trong chat là yêu cầu hủy job 14598, sau khi log cho thấy nó đang PENDING vì chờ 14597. Chưa thấy xác nhận scheduler đã hủy, chưa thể khẳng định E100 hoặc đồ thị mới đã hoàn thành. Nguồn: bản chụp chat đã đọc bằng công cụ ứng dụng, [A/latest_thread_snapshot.json:1](<F:/Denso/docs_denso_hack/_audit/latest_thread_snapshot.json:1>), turn `01a14312-93ed-71d2-a33b-93c248bf81d3` và `01a14311-f2d3-7d23-ad82-50d0e782c7e4`.

## Quy ước bằng chứng

| Nhãn | Cách hiểu |
|---|---|
| ✅ Đã làm và có bằng chứng | Có artifact, mã thực thi hoặc log đúng phạm vi. ✅ một thí nghiệm đã chạy không có nghĩa thí nghiệm thành công. |
| 🟡 Làm một phần | Có triển khai/ghi chép nhưng thiếu một mắt xích, phép đo hoặc kiểm độc lập. |
| ⬜ Mới là kế hoạch | Chỉ có đề xuất, hoặc bước tiếp theo chưa có artifact chạy. |
| **CHƯA XÁC MINH** | Không đủ căn cứ kết luận. Ghi kèm nhãn tiến độ phù hợp, không tự mặc định là đã làm hoặc đã thất bại. |

Ưu tiên: artifact đúng run và log thực tế → chat mới nhất của chính bạn → source tương ứng → tài liệu bàn giao → README cũ → slide. Chat giải thích “vì sao”, nhưng một lệnh được đề xuất trong chat không chứng minh nó đã chạy. Các session của approval reviewer có thể chứa bản sao hội thoại, không được đếm là thí nghiệm độc lập.

## Nguồn và cách tra

| Mã | Vị trí thực và phạm vi |
|---|---|
| J | `F:/cfg5_mophong/local_source_(1)/`: bản làm việc mới của nhánh masked joint/MCR. Một số config generated và cache vẫn chỉ có trên server. |
| L | `F:/cfg5_mophong/local_source/`: source gốc, metadata TCP lịch sử, có bổ sung resume/plot ngày 16/10. Không coi cả thư mục đều mới hoặc đều cũ. |
| R | `F:/cfg5_mophong/`: repo, các bundle, snapshot server và checkpoint/report lịch sử. |
| H | File JSONL nối tiếp chat `Check cfg5_mophong connection`, đường dẫn đầy đủ có trong mỗi link H. Tên file bắt đầu 09/10 nhưng nội dung kéo dài tới 16/10. |
| A | `F:/Denso/docs_denso_hack/_audit/`: trích xuất chỉ đọc và kiểm tra nhẹ của lượt này. |
| Sxx | Slide xx của PPTX gốc. Các ảnh PowerPoint render nằm trong `_audit/slide_renders/SlideXX.PNG`. |

Đã tìm 138 JSONL trong `~/.codex/sessions/` và `archived_sessions/`, bỏ session hiện tại khi lọc ban đầu. Không thấy `~/.codex/history.jsonl` hoặc `F:/Denso/.codex/`. Đã dùng công cụ ứng dụng xác nhận project **1** trỏ tới `F:/cfg5_mophong` và đọc đúng chat **Check cfg5_mophong connection**. Chỉ các đoạn liên quan được dùng cho kết luận; chỉ mục tìm kiếm không phải chứng cứ mọi kết quả đều thuộc dự án. [A/history_index.json:1](<F:/Denso/docs_denso_hack/_audit/history_index.json:1>) [A/verified_chat_messages.json:1](<F:/Denso/docs_denso_hack/_audit/verified_chat_messages.json:1>)

Đã trích text, bảng, Notes của **43 slide**, chỉ slide 2 có Notes có nội dung. Đã xuất ảnh bằng PowerPoint ở chế độ read-only và nhìn ba contact sheet cùng các slide kỹ thuật/lộ trình. S13 và S15 là nội dung hình ảnh nên không được bỏ sót chỉ vì trích text không thấy. [A/slides_extracted.json:1](<F:/Denso/docs_denso_hack/_audit/slides_extracted.json:1>)

Đã kiểm kê 2.027 file ngoài môi trường, Git và payload raw lớn, ở cả source/snapshot/bundle. Danh sách đầy đủ: [A/repo_inventory.json:1](<F:/Denso/docs_denso_hack/_audit/repo_inventory.json:1>). Đây không phải đếm toàn bộ file raw, không phải audit toàn bộ dataset. Chỉ đọc một record joint/gripper thật, một sample processed TCP cũ bằng memmap và metadata/report nhỏ. Không chạy train, không chạy rollout mới, không tải weights.

## Sổ mốc bằng chứng

| Mốc | Bằng chứng | Kết luận được phép |
|---|---|---|
| Chọn joint | [H/chat:3568](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:3568>) | ✅ Quyết định đổi representation; không đọc 8D TCP thành 8D joint. |
| Light preprocessing | [H/chat:4276](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:4276>) | ✅ Log 1.317 episode, split 1.053/132/132. |
| Cache frozen hoàn tất | `C:/Users/ADMIN/.codex/attachments/3f547c62-83dd-4c2a-9b49-d2d2377ac57c/Pasted text.txt`, 4 dòng cuối; [R/BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:19](<F:/cfg5_mophong/BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:19>) | ✅ 574.493 tick, ~447,07 GiB feature + scale trên server; không phải số demo thành công. |
| MCR freeze | [J/outputs/mcr_checks/mcr_real_local_check.json:1](<F:/cfg5_mophong/local_source_(1)/outputs/mcr_checks/mcr_real_local_check.json:1>) | ✅ Synthetic plumbing check, 0 backbone trainable, 73.493.449 ACT trainable. |
| Tiếp E25 → E100 | [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) [H/chat:5810](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5810>); [L/scripts/resume_mcr_with_plots.py:13](<F:/cfg5_mophong/local_source/scripts/resume_mcr_with_plots.py:13>) | 🟡 Báo cáo E25, đã chuẩn bị resume, chưa có loss/rollout mới. |
| Controller cũ | [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>) | ✅ 3/3 seeds 42/43/44, `act_model_used=false`. |
| ACT TCP E5 transfer | [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>) | ✅ Đã chạy 10 val rollout, 0/10 thành công; không phải nhánh MCR joint hiện tại. |
| TCP E58 | [R/checkpoints/before_test_20261007_142338/history.json:1](<F:/cfg5_mophong/checkpoints/before_test_20261007_142338/history.json:1>) | ✅ min val loss 0,19734495 ở E58 trong 78 epoch lưu; là posterior loss của run TCP cũ. |
| Demo task đích | [J/data/splits/pick_place_finetune_manifest.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_manifest.json:1>); [J/data/splits/pick_place_finetune_splits.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_splits.json:1>) | ✅ Manifest chấp nhận 913, từ chối 111, split 731/91/91; chưa xác minh “1.000 demo đều đạt”. |

## Giới hạn còn giữ nguyên

Chưa có model robot thật, báo giá BOM, đặc tả cell DENSO, force/torque feedback ngoài đời, success rate mới của joint policy, ablation pretrain/few-shot, hoặc log E25 đầy đủ. Không tự truy cập hay chạy lệnh trên server. Giới hạn 30 phút lấy từ câu trả lời trực tiếp của bạn trong chat này. Những bước thử nghiệm được nêu trong tài liệu là **đề xuất cho bạn chạy sau**, không phải lệnh đã thực hiện.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Nguồn nào cho biết hướng hiện tại là joint?
2. Vì sao một báo cáo ngày 13/10 có thể đã cũ vào 16/10?
3. Tại sao ✅ một rollout đã chạy vẫn có thể là 0/10?
4. Metadata local chứng minh được và không chứng minh được điều gì trên server?
5. Khi không có bằng chứng, tôi phải diễn đạt thế nào?
