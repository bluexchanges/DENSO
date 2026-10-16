# 05 — Giải thích từng slide và câu nên nói

Đã đọc 43 slide, Notes và ảnh render PowerPoint. Chỉ S2 có Notes có text, Notes đó ghi nguồn template và ảnh Copilot, không cung cấp nguồn kinh tế. Các slide chỉ tiêu đề/trang ngăn được bỏ qua:1,3,9,11,20,39,41,43. Còn 35 slide có nội dung được đối chiếu dưới đây. Nguồn gốc: `F:/Denso/Denso-Hack_Presentation-EDABK_TriH.pptx`; bản trích [A/slides_extracted.json:1](<F:/Denso/docs_denso_hack/_audit/slides_extracted.json:1>), ảnh `_audit/slide_renders/`.

**Cách dùng:** học ý nghĩa và bằng chứng, rồi nói bằng lời mình. Câu mẫu là bản sửa trung thực, không phải đọc lại claim trên slide. Mỗi mục Sxx tham chiếu chính slide đã xem; những phần không có log/code được giữ CHƯA XÁC MINH.

**Ba điều phải cập nhật trước:** output nhánh mới là joint/MCR; số demo được chấp nhận không khớp claim 1.000 đạt; kết quả train/TCP transfer không chứng minh generalization. Phần sửa ưu tiên xem 06 và 09.


## Slide 2

**Slide nói gì:** Checklist: ACT đa phương thức, mô phỏng Panda 8 camera, RH20T, 3–6 tháng, vốn 1 tỷ/thay 3 người/lương 15 triệu/hoàn vốn~20 tháng, hướng few-shot và kinh nghiệm tay 6 trục.

**Ý nghĩa thật:** Đây là tóm tắt cam kết của đội. Các kết quả đo, giả định kinh tế và mục tiêu phát triển đang nằm cùng một bảng, nên phải nói riêng từng loại.

**Bằng chứng:** S2/PPTX; [H/chat:3568](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:3568>) [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>); [J/src/models/mcr_act.py:44](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:44>); [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>).

**Trạng thái:** 🟡 Model/mô phỏng có source; 🟡 pretrain joint theo ghi nhận E25; ⬜ few-shot/robot thật/ROI đo thật.

**Câu nên nói (không quá 3 câu):** “Nhóm đã xây dựng pipeline học bắt chước và mô phỏng để kiểm tra bài toán gắp–đặt. Nhánh mới dùng MCR và góc khớp, còn hiệu quả nhà máy và few-shot là mục tiêu cần thử nghiệm. Các số kinh tế là giả định, nhóm sẽ hiệu chỉnh bằng dữ liệu cell thực.”

**Có thể bị hỏi tiếp:** Cụ thể điều gì đã được chứng minh trong mô phỏng: controller hay policy học?

**Kiểm từng dòng:** (1) Không có benchmark chứng minh thích nghi tốt hơn trajectory cố định. (2) Công đoạn DENSO cần nguồn khảo sát. (3) “Dự kiến pretrain” đã cũ so với ghi nhận train mới; cập nhật joint/MCR và mức bằng chứng. (4) 1.000/45=22,22 tháng nếu tính triệu VNĐ, chưa trừ OPEX; ~20 không khớp chính xác. (5) Few-shot là kế hoạch. (6) Kinh nghiệm 6 trục không xác định robot xưởng hoặc robot trong demo. “Tay máy được tài trợ” trên slide chưa có giấy/model xác nhận trong nguồn đã kiểm.


## Slide 4

**Slide nói gì:** Tiểu sử cố vấn Nguyễn Đức Minh: bằng Tiến sĩ 2009,6 năm nghiên cứu tại Kaiserslautern, chức danh và hướng nghiên cứu.

**Ý nghĩa thật:** Giới thiệu năng lực cố vấn, không phải bằng chứng robot policy đạt KPI.

**Bằng chứng:** Chỉ S4 trong PPTX; chưa đối chiếu hồ sơ tổ chức hoặc CV trong lượt audit kỹ thuật này.

**Trạng thái:** 🟡 Thông tin do slide cung cấp; **CHƯA XÁC MINH** từng mốc/chức danh.

**Câu nên nói (không quá 3 câu):** “Nhóm có cố vấn hỗ trợ định hướng nghiên cứu và kiểm tra kỹ thuật. Nhóm chịu trách nhiệm trực tiếp về số liệu thực nghiệm được trình bày.”

**Có thể bị hỏi tiếp:** Cố vấn đã trực tiếp kiểm tra phần nào của dự án?


## Slide 5

**Slide nói gì:** Tiểu sử cố vấn Nguyễn Huy Hoàng, Tiến sĩ 2017, nghiên cứu AI/thị giác.

**Ý nghĩa thật:** Nêu nền chuyên môn, chưa nói mức tham gia, thời lượng mentoring hay bảo chứng kết quả.

**Bằng chứng:** S5; chưa thấy CV/hồ sơ và biên bản review dự án trong repo.

**Trạng thái:** 🟡 **CHƯA XÁC MINH** thông tin lý lịch độc lập và phạm vi đóng góp.

**Câu nên nói (không quá 3 câu):** “Cố vấn hỗ trợ nhóm về phương pháp AI và thị giác. Kết quả của nhóm vẫn được đánh giá bằng log và protocol riêng.”

**Có thể bị hỏi tiếp:** Phần kỹ thuật nào nhóm tự làm và phần nào do cố vấn góp ý?


## Slide 6

**Slide nói gì:** Nghiêm Văn Quang, cử nhân HUST/thạc sĩ NTU và link LinkedIn.

**Ý nghĩa thật:** Giới thiệu cố vấn thực hành, không suy ra đã có kinh nghiệm triển khai robot công nghiệp từ tên trường.

**Bằng chứng:** S6; link LinkedIn hiện trên slide nhưng chưa dùng làm nguồn xác minh.

**Trạng thái:** 🟡 Thông tin slide; **CHƯA XÁC MINH** độc lập.

**Câu nên nói (không quá 3 câu):** “Cố vấn hỗ trợ nhóm rà soát hướng triển khai. Khi nói kinh nghiệm, nhóm chỉ nêu phần có thể chứng minh bằng công việc cụ thể.”

**Có thể bị hỏi tiếp:** Ai sẽ phụ trách tích hợp robot thật và calibration?


## Slide 7

**Slide nói gì:** Hai thành viên: CPA3,7/4; kinh nghiệm đọc đồng hồ/mức dầu 99%; inference giọng nói<1 giây; SepAdapter đang phản biện ICLR 2027.

**Ý nghĩa thật:** Đó là thành tích của người/những dự án khác, không phải accuracy 99% của ACT gắp chốt.

**Bằng chứng:** S7; không có báo cáo benchmark, CV hoặc tình trạng review của các dự án đó trong phạm vi repo đã kiểm.

**Trạng thái:** 🟡 **CHƯA XÁC MINH** các số 99%,<1s, CPA và trạng thái nghiên cứu từ artifact độc lập.

**Câu nên nói (không quá 3 câu):** “Các thành viên có nền tảng AI và hệ thống nhúng từ những dự án trước. Số 99% thuộc dự án đọc đồng hồ được nêu trên slide, không phải kết quả gắp–đặt của mô hình này.”

**Có thể bị hỏi tiếp:** 99% được đo trên bao nhiêu mẫu, metric nào và có liên quan gì tới robot?


## Slide 8

**Slide nói gì:** Hai thành viên K70, CPA3,73/4 và3,67/4, từng làm ML/PID.

**Ý nghĩa thật:** Giới thiệu nền tảng và khả năng học, chưa chứng minh đội có đủ kỹ năng commissioning/safety.

**Bằng chứng:** S8; chưa thấy hồ sơ/metric dự án thành viên tương ứng trong repo.

**Trạng thái:** 🟡 Thông tin slide chưa xác minh độc lập.

**Câu nên nói (không quá 3 câu):** “Nhóm đang phát triển năng lực AI và điều khiển qua dự án. Phần triển khai thật cần phối hợp kỹ sư xưởng và chuyên gia tích hợp.”

**Có thể bị hỏi tiếp:** Phân công cụ thể ai chịu trách nhiệm data, model, control và safety?


## Slide 10

**Slide nói gì:** Công đoạn trước làm sạch vẫn phụ thuộc con người, linh kiện nhỏ gây mỏi mắt, lỗi và chi phí tăng.

**Ý nghĩa thật:** Đề xuất một pain point công nghiệp; ảnh minh họa không chứng minh tỷ lệ thủ công hoặc tỷ lệ lỗi.

**Bằng chứng:** S10 và ảnh; chưa thấy khảo sát cell, cycle-time log, phiếu reject hoặc quan sát có ngày trong repo.

**Trạng thái:** 🟡 Bối cảnh trên slide; **CHƯA XÁC MINH** tại cell DENSO cụ thể.

**Câu nên nói (không quá 3 câu):** “Nhóm nhắm tới công đoạn gắp và xếp linh kiện nhỏ trước xử lý. Mức độ thủ công, lỗi và năng suất hiện tại cần được xác nhận cùng kỹ sư DENSO để chốt baseline.”

**Có thể bị hỏi tiếp:** Tên công đoạn, mã linh kiện và takt time hiện tại là gì?


## Slide 12

**Slide nói gì:** Robot 7 DOF, ACT nhận 8 camera+state rồi dự đoán chuỗi hành động; hình là sơ đồ ACT gốc.

**Ý nghĩa thật:** Panda có 7 khớp tay. Kiến trúc trên hình cần chú thích đâu là phần kế thừa và đâu là adapter mới.

**Bằng chứng:** S12; [J/src/models/mcr_act.py:44](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:44>) [J/src/models/rh20t_act.py:97](<F:/cfg5_mophong/local_source_(1)/src/models/rh20t_act.py:97>) [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>).

**Trạng thái:** ✅ Source model và Panda; 🟡 vòng điều khiển joint end-to-end còn thiếu xác minh.

**Câu nên nói (không quá 3 câu):** “Nhánh hiện tại dùng Panda 7 khớp, ảnh nhiều góc và trạng thái khớp. MCR trích đặc trưng rồi ACT dự đoán 20 bước góc khớp+kẹp; nhóm còn phải kiểm tra vòng điều khiển joint trong task.”

**Có thể bị hỏi tiếp:** Các anh dự đoán joint hayTCP, và đã chạy vòng kín chưa?

**Cần sửa hình/chú thích:** ảnh ACT gốc/ALOHA không phải kiến trúc 8 camera MCR của nhóm. Thêm MCR ResNet50, mask camera và state/output joint vào caption; không ghi đã thử robot thật.


## Slide 13

**Slide nói gì:** Bảng pain point bằng hình: linh kiện~10 mm, dễ vỡ, dung sai 2 mm; học mẫu để giảm công setup; phản hồi lực là hướng mở rộng.

**Ý nghĩa thật:** Slide nói yêu cầu công nghiệp nhưng task code là chốt Ø 6×35 mm, lỗ Ø 7 sâu 12 mm. Hai bài toán chưa được chứng minh tương đương.

**Bằng chứng:** Ảnh render S13; [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>); [J/src/models/mcr_act.py:137](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:137>).

**Trạng thái:** 🟡 Problem mapping; ⬜ force feedback và chứng minh linh kiện dễ vỡ.

**Câu nên nói (không quá 3 câu):** “Mô phỏng hiện dùng chốt chuẩn để kiểm tra kỹ thuật, chưa phải mô hình vật liệu của linh kiện thật. Nhóm chưa học lực kẹp; bước ứng dụng cần xác nhận dung sai, vật liệu và phản hồi tiếp xúc.”

**Có thể bị hỏi tiếp:** Tại sao dùng chốt 6 mm nếu yêu cầu thật nói 10 mm, dung sai 2 mm?

S13 là nội dung nằm trong ảnh nên trích text ban đầu không thấy. Dung sai 2 mm trên slide không cùng đại lượng với khe hở bán kính 0,5mm của task; không so trực tiếp để khoe chính xác hơn DENSO.


## Slide 14

**Slide nói gì:** So sánh robot truyền thống với hệ học: tái dùng, ít demo và giảm công triển khai là mục tiêu.

**Ý nghĩa thật:** Giả thuyết lợi ích khi có nhiều biến thể. Robot truyền thống cũng có thể tái dùng phần cứng, chương trình và vision.

**Bằng chứng:** S14; chưa có thí nghiệm về giờ công/baseline; source ACT tại [J/src/models/mcr_act.py:44](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:44>).

**Trạng thái:** ⬜ Lợi ích so sánh chưa đo; 🟡 Hệ học đã có nền triển khai.

**Câu nên nói (không quá 3 câu):** “Nhóm kỳ vọng giảm công cấu hình khi có nhiều biến thể gắp–đặt liên quan. Với cell cố định, teach pendant và vision cổ điển vẫn là baseline cần đo công bằng.”

**Có thể bị hỏi tiếp:** Vì sao không chỉ dùng vision nhận vị trí rồi IK?


## Slide 15

**Slide nói gì:** Sơ đồ bằng hình: camera/state→ACT→Panda gắp đặt→đánh giá.

**Ý nghĩa thật:** Đây là luồng mong muốn; cần phân biệt module có code và vòngkín đã chạy.

**Bằng chứng:** Ảnh render S15; [J/src/simulation/panda_env.py:113](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:113>) [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>) [J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>).

**Trạng thái:** 🟡 Pipeline có nhiều khối, chưa xác minh nối joint MCR→controller mới.

**Câu nên nói (không quá 3 câu):** “Sơ đồ thể hiện quy trình cần hoàn thiện. Mô phỏng và evaluator đã có, nhưng adapter observation/action joint phải khớp trước khi gọi đây là learned policy end-to-end.”

**Có thể bị hỏi tiếp:** Khối nào đã chạy thật cùng nhau, khối nào mới đứng riêng?


## Slide 16

**Slide nói gì:** Bốn bước pretrain RH20T→demo đích→fine-tune→chạy/đánh giá; dưới hình ghi dự đoán pose tay+kẹp.

**Ý nghĩa thật:** Quy trình học chuyển giao hợp lý ở mức kế hoạch, nhưng mô tả output pose thuộc nhánh TCP cũ.

**Bằng chứng:** [H/chat:3568](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:3568>) [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) [J/src/data/cfg5_masked.py:227](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:227>) [J/src/data/sim_demos.py:89](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:89>).

**Trạng thái:** ✅ Quyết định joint; 🟡 train mới theo E25; 🟡 demo đích TCP đã có; ⬜ fine-tune joint/rollout đích xác minh.

**Câu nên nói (không quá 3 câu):** “Sau lần thử TCP, nhóm đã chuyển sang bảy góc khớp và độ mở kẹp vì có nhãn joint ghi thật. Do đó phải chuyển cả dữ liệu task đích và bộ điều khiển sang đúng hợp đồng joint. Các bước fine-tune và đánh giá nhánh mới chưa được coi là xong.”

**Có thể bị hỏi tiếp:** Hai bộ dữ liệu đều 8 chiều, tại sao vẫn không fine-tune thẳng được?

**Giải thích sâu:** pretrain joint: observation t, target measured q ởt+1…t+20 và future gripper command. Demo TCP đích: measured TCP state t, commanded TCP cùng tick pre-step, offset 0. Khác đơn vị, ý nghĩa, timing và stats. Không dùng E58TCP làm resume joint. CVAE posterior dùng target khi train; infer z=0. Xem 02.


## Slide 17

**Slide nói gì:** Khẳng định 1.000 demonstration mô phỏng đạt,8 view đồng bộ, randomization màu/nền/đèn/vị trí/vật phụ.

**Ý nghĩa thật:** Đang nói cả số lượng, chất lượng và độ phủ. Phải đối chiếu manifest hơn ảnh sample.

**Bằng chứng:** [J/data/splits/pick_place_finetune_manifest.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_manifest.json:1>) [J/data/splits/pick_place_finetune_splits.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_splits.json:1>) [J/src/data/sim_demos.py:68](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:68>) [A/measured_facts.json:1](<F:/Denso/docs_denso_hack/_audit/measured_facts.json:1>).

**Trạng thái:** ✅ Có data/multiview manifest; 🟡 claim 1.000 đều đạt và range randomization chưa xác minh đầy đủ.

**Câu nên nói (không quá 3 câu):** “Manifest hiện có 913 episode được chấp nhận,111 mục bị từ chối do thất bại hoặc video lỗi. Nhóm có các profile biến thiên, nhưng cần chốt lại số demo dùng được và range randomization trước khi công bố.”

**Có thể bị hỏi tiếp:** 1.000 là số lần thử, số thành công, hay số episode qua kiểm tra?

**Số audit:** 913 accepted,111 rejected, duplicates 0; rejected gồm 24 không success,87 video lỗi/thiếu frame. Split 731/91/91. Profile accepted: fixed 1, varied 4, diverse 208, rich 700. Không gọi 913/1024 là success rate controller vì video errors và candidate selection làm đổi mẫu số. Các profile tên rich/diverse không tự chứng minh mỗi tham số randomization và held out OOD.


## Slide 18

**Slide nói gì:** Rig 8 RGB camera=6 cố định+2 in-hand; ACT nhận ảnh+state, ra chuỗi pose+kẹp, chưa dự đoán lực.

**Ý nghĩa thật:** Kiến trúc hiện tại cần thay pose bằng joint; camera RH20T trên slide là minh họa, không phải rig ngoài đời đã lắp.

**Bằng chứng:** [J/configs/data/cfg5_all8.json:6](<F:/cfg5_mophong/local_source_(1)/configs/data/cfg5_all8.json:6>) [J/src/models/mcr_act.py:73](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:73>) [J/src/models/mcr_act.py:137](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:137>) [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>).

**Trạng thái:** ✅ Rig/slot code và head 8D; 🟡 bridge joint; ⬜8 camera thật/force policy.

**Câu nên nói (không quá 3 câu):** “Mô phỏng bố trí sáu camera ngoài và hai camera trên tay. Nhánh hiện tại dự đoán góc khớp+kẹp, có mask khi camera thiếu và chưa dự đoán lực; cấu hình camera ngoài đời phải đo chi phí/hiệu chuẩn.”

**Có thể bị hỏi tiếp:** Tại sao cần 8 camera, giảm xuống 2–3 camera có được không?

8 slot không phải mọi timestamp có 8 ảnh hợp lệ. MCR dùng shared backbone, maskB×8, feature B×8×2048×7×7. Lực giới hạn 20 N trong config controller không phải force prediction của ACT.


## Slide 19

**Slide nói gì:** “Hướng tới few-shot”: pretrain đa dạng→ít demo mới→mở rộng biến thể.

**Ý nghĩa thật:** Định hướng về sample efficiency, chưa phải kết quả one-shot/few-shot đã đo.

**Bằng chứng:** S19; [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>); chưa thấy ablation N-demo/held-out task trong artifact đã kiểm.

**Trạng thái:** ⬜ Few-shot/đa tác vụ có kiểm chứng; 🟡 nền data đa task.

**Câu nên nói (không quá 3 câu):** “Few-shot hiện là hướng phát triển. Nhóm sẽ đo success trên các mức số demo và so sánh có/không pretrain với task mới tách riêng.”

**Có thể bị hỏi tiếp:** Ít là bao nhiêu demo, và đã có đường cong N-demo chưa?

RH20T có one-shot trong tên paper không làm ACT của nhóm tự động thành one-shot. Có 104 task trong pretrain data cũng không chứng minh policy đã làm được 104 task.


## Slide 21

**Slide nói gì:** Khung giờ công, lấy 8 h/ngày và 250.000VNĐ/h; so công lập trình/train/kiểm thử.

**Ý nghĩa thật:** Đang ước tính **engineering effort**, khác tiền lương công nhân vận hành ởS2/36.

**Bằng chứng:** S21; không thấy bảng chấm công/báo giá xác nhận 250.000đ/h trong repo.

**Trạng thái:** ⬜ Giả định kinh tế, chưa đo lường.

**Câu nên nói (không quá 3 câu):** “Đây là đơn giá giả định cho công kỹ sư triển khai. Nhóm tách khoản này khỏi lương công nhân vận hành và chưa coi là báo giá DENSO.”

**Có thể bị hỏi tiếp:** 250.000đ/h lấy ở đâu, có bao gồm overhead không?

250.000×8=2 triệu/ngày; nếu 160 h/tháng thì 40 triệu/tháng, nhưng đó là quy đổi số học, không chứng minh mức lương người cụ thể. Không nhất thiết mâu thuẫn 15 triệu nếu khácrole/cost basis, phải ghi rõ.


## Slide 22

**Slide nói gì:** Teach pendant/động học so với collect data/train/evalIL-RL.

**Ý nghĩa thật:** Thời gian phát triển có cấu phần khác nhau, chưa đủ so sánh chỉ GPU train hours.

**Bằng chứng:** S22; [R/server_train_mcr_current.py:41](<F:/cfg5_mophong/server_train_mcr_current.py:41>) cho thấy train chỉ là một bước, không có log engineering hours.

**Trạng thái:** ⬜ So sánh thời gian chưa đo.

**Câu nên nói (không quá 3 câu):** “Với AI, công triển khai gồm dữ liệu, hiệu chuẩn, huấn luyện và nghiệm thu. Nhóm sẽ đo giờ lao động riêng với giờ máy chạy để so công bằng.”

**Có thể bị hỏi tiếp:** Trong 8 h/bài của các anh có gồm collect data và safety validation không?


## Slide 23

**Slide nói gì:** Bảng tham khảo: teach 1–8 h; IK1–5 ngày; vision 3–14 ngày; IL1–7 ngày; RL vài ngày–vài tuần.

**Ý nghĩa thật:** Các khoảng dự toán khác mức phạm tác vụ, hệ thống; chưa là benchmark.

**Bằng chứng:** S23; không có nguồn/time-study ghi trong Notes (Notes rỗng).

**Trạng thái:** ⬜ Giả định, **CHƯA XÁC MINH** khoảng thời gian.

**Câu nên nói (không quá 3 câu):** “Bảng này chỉ giúp lập kế hoạch sơ bộ. Thời gian thực cần đo trên cùng một cell, cùng độ khó và cùng tiêu chí nghiệm thu.”

**Có thể bị hỏi tiếp:** Cùng bài gắp chốt, các anh đã đo từng phương pháp chưa?

Nếu 8 h/ngày: IK8–40 h, vision 24–112 h, IL8–56h; đây chỉ là quy đổi, không là số đo. Độ rộng của các khoảng không chứng minh phương pháp AI nhanh hơn.


## Slide 24

**Slide nói gì:** Ví dụ teach gắp đặt khi hardware có sẵn:30–60 phút setup,30–90 phút dạy 4–8 điểm,15–30 phút kẹp,30–120 phút test; headline 2–5 h.

**Ý nghĩa thật:** Scope hẹp khi lắp sẵn robot/gripper, so với AI cũng phải giữ cùng scope.

**Bằng chứng:** S24, không có time-study độc lập.

**Trạng thái:** ⬜ Dự toán.

**Câu nên nói (không quá 3 câu):** “Ví dụ này giả định phần cứng đã lắp sẵn. Tổng các mục là khoảng 1,75 đến 5 giờ, làm tròn 2–5 giờ; không đại diện mọi bài toán.”

**Có thể bị hỏi tiếp:** Các anh đã tính thiết kế gripper, PLC và validation chất lượng chưa?

Min 30+30+15+30=105 phút=1,75 h. Max 60+90+30+120=300 phút=5 h.4–8 là số điểm dạy, không phải 4–8 giờ.


## Slide 25

**Slide nói gì:** Đơn giản 2–5h, trung bình 1–3 ngày, phức tạp 3–7 ngày;10 bài nhân 10.

**Ý nghĩa thật:** Phân nhóm độ khó là giả định, cần định nghĩa nghiệm thu và cell phù hợp.

**Bằng chứng:** S25; không có phân loại task đã đo.

**Trạng thái:** ⬜ Dự toán.

**Câu nên nói (không quá 3 câu):** “Nhóm phân nhóm để dựng kịch bản chi phí. Định nghĩa độ khó và khoảng giờ cần được xác nhận bằng task thật.”

**Có thể bị hỏi tiếp:** Task chốt của các anh thuộc nhóm nào và vì sao?

10 bài đơn giản 20–50 h. Trung bình 10–30 ngày=80–240 h. Phức tạp 30–70 ngày=240–560 h, đều theo 8 h/ngày. Số 16 h và 40 h ở S26 nằm trong các khoảng, tuy nhiên chưa có phép đo chọn chúng.


## Slide 26

**Slide nói gì:** 10 bài hỗn hợp:4 đơn giản×4h+4 trung bình×16 h+2 phức tạp×40 h=160 h=20 ngày=40 triệu; tiêu đề 120–200 h.

**Ý nghĩa thật:** Một kịch bản trung tâm có trọng số, sau đó giữ trung bình 16 h/bài để vẽ hòa vốn.

**Bằng chứng:** S26; bằng chứng là phép tính trên slide, không phải artifact năng suất.

**Trạng thái:** ✅ Số học đúng; ⬜ định mức/chứng minh thực tế.

**Câu nên nói (không quá 3 câu):** “160 giờ là ví dụ từ cơ cấu 4–4–2 và định mức 4–16–40 giờ. Đây là giả định lập kế hoạch, nhóm chưa đo trên 10 task thật.”

**Có thể bị hỏi tiếp:** Tại sao định mức là 4,16,40 h và tại sao đúng tỷ lệ 4–4–2?

16+64+80=160 h;160/8=20 ngày;160×250.000=40 triệu. Khoảng 120–200 h không được suy ra từ bảng cố định này, nên cần ghi là range giả định riêng hoặc bỏ headline khoảng.


## Slide 27

**Slide nói gì:** Khi có nền tảng sẵn,160 h truyền thống so với 80 h AI, giảm 50%;40 vs 20 triệu.

**Ý nghĩa thật:** So **marginal effort** sau khi làm xong platform; không phải total cost lần đầu.

**Bằng chứng:** S27 chart; S28/29 mới có setup; chưa có time-study 8 h/task.

**Trạng thái:** ✅ Phép tính 50%; ⬜ Mức giảm đo thật.

**Câu nên nói (không quá 3 câu):** “50% chỉ đúng trong giả định nền tảng đã sẵn và mỗi bài AI tốn 8 giờ. Lần đầu cần cộng giờ setup nên chưa thể nói tiết kiệm 50% tổng dự án.”

**Có thể bị hỏi tiếp:** Ai trả 120 giờ setup và bao giờ debug dữ liệu?

(160−80)/160=50%;80×250.000=20 triệu.8 h/bài là giả định, không phải thời gian training GPU 8 h đã đo.


## Slide 28

**Slide nói gì:** Digital Twin 40–80 h; Isaac Lab/training/sim-to-real 40–80 h;10 bài 80 h; tổng 160–240 h.

**Ý nghĩa thật:** Chi phí nền 80–160 h cộng công biên 80 h. Công cụ trên slide khác repo.

**Bằng chứng:** S28;[J/src/simulation/panda_env.py:1](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:1>) dùng MuJoCo;[J/requirements-sim-lock.txt:1](<F:/cfg5_mophong/local_source_(1)/requirements-sim-lock.txt:1>).

**Trạng thái:** ✅ Xác minh MuJoCo; ⬜ Định mức giờ; **CHƯA XÁC MINH** sử dụng Isaac Lab.

**Câu nên nói (không quá 3 câu):** “Dự án hiện tại dùng MuJoCo. Nhóm sẽ sửa tên công cụ trên slide và giữ chi phí thiết lập là giả định cần đo, không claim đã làm sim-to-real trong 80 giờ.”

**Có thể bị hỏi tiếp:** Các anh có code Isaac Lab ở đâu?

40–80+40–80=80–160 h setup;+80=160–240 h. Nguồn 120 h ở S31 là giá trị giữa 80–160, không phải số đo. Không được gọi Panda Menagerie là Digital Twin đã hiệu chuẩn của cell DENSO.


## Slide 29

**Slide nói gì:** 10 bài đầu AI 160–240 h,40–60 triệu, so với 160 h 40 triệu; ví dụ setup 120+80=200 h.

**Ý nghĩa thật:** Nhận thẳng chi phí khởi đầu có thể cao hơn; thuận lợi AI cần số lượng task và reuse.

**Bằng chứng:** S29/S28/S21; phép tính đúng theo giả định.

**Trạng thái:** ✅ Số học và phân biệt scope; ⬜ kiểm xác nhận giả định.

**Câu nên nói (không quá 3 câu):** “Ở 10 bài đầu, AI chưa chắc tiết kiệm giờ công. Kịch bản trung tâm là 200 giờ, cao hơn 40 giờ so với baseline 160 giờ.”

**Có thể bị hỏi tiếp:** Vậy tại sao DENSO nên đầu tư nếu chỉ có 10 task?

160–240 h×0,25 triệu/h=40–60 triệu. Ví dụ 200 h=50 triệu, thêm 10 triệu so với truyền thống. Không biến range 80–160 setup thành cam kết trần chi phí.


## Slide 30

**Slide nói gì:** Lặp bảng 10 bài hỗn hợp 160 h/20 ngày/40 triệu.

**Ý nghĩa thật:** Cùng giả định S26, không phải một thí nghiệm thứ hai.

**Bằng chứng:** S30, S26.

**Trạng thái:** ✅ Số học; ⬜ định mức.

**Câu nên nói (không quá 3 câu):** “Đây vẫn là baseline 160 giờ từ ví dụ trước. Nhóm giữ nhất quán để vẽ tổng giờ theo số task.”

**Có thể bị hỏi tiếp:** Nếu 10 task đều là đơn giản thì điểm hòa vốn còn 15 không?

Có thể chuyển slide này thành backup để tiết kiệm 30 phút. Nếu baseline 4 h/task thấp hơn AI 8 h/task thì không có hòa vốn dương ở mô hình tuyến tính này.


## Slide 31

**Slide nói gì:** H truyền thống=16n; HAI=120+8n; giờ tiết kiệm=8n−120.

**Ý nghĩa thật:** Hai đường thẳng mô hình hóa engineering hours, với chi phí setup cố định và marginal cost khác nhau.

**Bằng chứng:** S31;16=160/10 trong S26;120 nằm giữa 80–160S28;8=80/10S27.

**Trạng thái:** ✅ Đại số; ⬜ tham số đo.

**Câu nên nói (không quá 3 câu):** “n là số task được triển khai trên nền tảng có thể tái dùng. Nhóm giả định 16 giờ/task truyền thống,120 giờ setup AI và 8 giờ/task AI; các định mức cần được kiểm bằng log công thật.”

**Có thể bị hỏi tiếp:** Như thế nào là một task và reuse được đến mức nào?

16 h là trung bình của mix 4–4–2, chưa phải định mức tất cả task. Công thức tổng quát: n*=H_setup/(h_trad−h_AI), chỉ có hòa vốn dương nếu h_trad>h_AI và reuse giữ được.


## Slide 32

**Slide nói gì:** Hòa vốn giờ công tại 15 bài:120/(16−8)=15;240 h/cách=60 triệu.

**Ý nghĩa thật:** Điểm giao hai mô hình engineering cost, không phải tháng hoàn vốn vốn robot.

**Bằng chứng:** S32; đồ thị hòa vốn và công thức S31.

**Trạng thái:** ✅ Số học; ⬜ Dự báo lợi ích thực.

**Câu nên nói (không quá 3 câu):** “15 bài là điểm hòa vốn về công triển khai trong kịch bản này. Nó không nói robot sẽ hoàn vốn sau 15 tháng.”

**Có thể bị hỏi tiếp:** Nếu setup 160 h hoặc AI 12 h/task thì hòa vốn ở đâu?

Thay H_setup 160, h_trad 16, h_AI 8→20 task. Thay H_setup 120, h_AI 12→30 task. Tại 15:16×15=240 h;120+8×15=240 h;240×0,25=60 triệu. Tại 15 chỉ hòa vốn, tiết kiệm dương từ task 16 nếu n nguyên.


## Slide 33

**Slide nói gì:** Bảngn=10/20/30/50/100 và tiết kiệm−10/10/30/70/170 triệu.

**Ý nghĩa thật:** Thay n vào hàm 8n−120, không phải kết quả đo 100 task.

**Bằng chứng:** S33, S31.

**Trạng thái:** ✅ Tất cả hàng số học đúng; ⬜ Độ đúng mô hình chi phí.

**Câu nên nói (không quá 3 câu):** “Các mốc trong bảng là projection theo cùng giả định. Khi đổi cell, robot hoặc distribution task, nền tảng có thể cần bổ sung setup nên không giữ đường thẳng mãi mãi.”

**Có thể bị hỏi tiếp:** Tại 100 task có những chi phí tăng thêm nào chưa tính?

10:(160,200,−40,−10).20:(320,280,40,10).30:(480,360,120,30).50:(800,520,280,70).100:(1600,920,680,170). Bốn giá trị mỗi hàng là Htrad, HAI, giờ tiết kiệm, triệu VNĐ; không bao gồm vốn robot, OPEX hoặc quality loss.


## Slide 34

**Slide nói gì:** 10 task đơn giản có thể dùng teach pendant kinh tế hơn; AI có lợi khi reuse nhiều task.

**Ý nghĩa thật:** Một điều kiện kinh tế hợp lý, nhưng cần đo độ đa dạng và sample cost.

**Bằng chứng:** S34 và mô hình S31; chưa có benchmark nhóm.

**Trạng thái:** 🟡 Lập luận điều kiện; ⬜ Kết quả kiểm thực.

**Câu nên nói (không quá 3 câu):** “Nhóm không đề xuất AI cho mọi cell. Ưu tiên là các công đoạn có biến thể liên quan mà tái dùng được dữ liệu và phần cứng.”

**Có thể bị hỏi tiếp:** Cell DENSO nào có nhiều đủ biến thể để bù setup?


## Slide 35

**Slide nói gì:** Thủ công lỗi~2–5%, ca8–10h; robot độ chính xác cao,24/7, nhanh thích nghi few-shot.

**Ý nghĩa thật:** Các claim hiệu suất/chất lượng chưa đo bị viết như khả năng hiện hữu.

**Bằng chứng:** S35;[R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>) là0/10 TCP cũ; nhánh mới chưa có success rate; S19 ghi “hướng tới”.

**Trạng thái:** ⬜ Lỗi 2–5%,24/7, accuracy cao, few-shot thực nghiệm **CHƯA XÁC MINH**.

**Câu nên nói (không quá 3 câu):** “Robot có tiềm năng giảm thao tác lặp lại, nhưng nhóm chưa đo vận hành liên tục hay độ chính xác hệ học. Các số lỗi thủ công và khả năng few-shot cần được xác nhận bằng pilot.”

**Có thể bị hỏi tiếp:** Chính hệ thống các anh đạt bao nhiêu phần trăm thành công?

Không dùng 3/3 controller làm accuracy ACT.24/7 là 168 h/tuần trên lý thuyết, không tương đương uptime 100%: còn changeover, nạpphôi, bảo trì, lỗi và người giám sát. Nên dùng availability/takt/yield đo được.


## Slide 36

**Slide nói gì:** Thủ công có xúc giác, robot đang phát triển; claim đếm phân tích lỗi theo thời gian thực; chi phí lương 18–20 triệu, robot~1 tỷ/bảo trì thấp.

**Ý nghĩa thật:** Slide ghép năng lực đang có với kế hoạch MES/giám sát và giả định chi phí.

**Bằng chứng:** S36;[J/src/models/mcr_act.py:137](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:137>) head joint/width, chưa force;[J/src/simulation/panda_evaluator.py:65](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:65>) metrics mô phỏng, không MES.

**Trạng thái:** 🟡 Evaluator mô phỏng; ⬜ force task thật/MES/bảo trì thấp và báo giá.

**Câu nên nói (không quá 3 câu):** “Hệ thống hiện tại chưa học lực kẹp và chưa chứng minh xử lý linh kiện dễ vỡ. Đếm/lưu kết quả mô phỏng đã có, nhưng đồng bộ dây chuyền/MES và chi phí vận hành là bước triển khai tiếp.”

**Có thể bị hỏi tiếp:** Đếm được đúng số linh kiện ngoài đời hay chỉ đếm success flag?

Bản tóm tắt bạn đưa nói S36 “chưa dự đoán lực”, nhưng slide thực chỉ ghi “đang phát triển”; câu chưa dự đoán lực nằm S18.18–20 triệu có thể là fully loaded cost khác 15 triệu base wage S2, chỉ chấp nhận nếu định nghĩa và nguồn rõ ràng.1 tỷ chưa có BOM.


## Slide 37

**Slide nói gì:** Hệ thống học linh kiện mới nhanh, dễ tích hợp tay máy hiện có của nhà máy.

**Ý nghĩa thật:** Đây là lời hứa retargeting, tích hợp và sample efficiency chưa đo chứng.

**Bằng chứng:** S37;[J/src/simulation/panda_controller.py:29](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:29>) đanghard-code Panda 7 joint; chưa biết robot xưởng.

**Trạng thái:** ⬜ Triển khai ngang/few-shot; 🟡 code mô phỏng Panda.

**Câu nên nói (không quá 3 câu):** “Khả năng tái dùng là hướng phát triển, không chỉ đổi model XML. Robot khác cần kiểm động học, gripper, camera, driver và train lại dữ liệu phù hợp.”

**Có thể bị hỏi tiếp:** Chuyển từ Panda 7 trục sang robot 6 trục cần đổi cụ thể gì?

Sửa lỗi chữ “củnhận”,“a nhà máy”; thay “dễ dàng lắp đặt” bằng “cần pilot và adapter theo robot”.


## Slide 38

**Slide nói gì:** Ước tính hoàn vốn 16–18 tháng, chuyển công nhân sang quality.

**Ý nghĩa thật:** Một mô hình cash flow CAPEX/OPEX khác hòa vốn giờ công S32.

**Bằng chứng:** S38/S2/S36, chưa có BOM hoặc production study.

**Trạng thái:** ⬜ ROI giả định, **CHƯA XÁC MINH** lợi ích tiền mặt thực.

**Câu nên nói (không quá 3 câu):** “Hoàn vốn cần tính theochi phí đầu tư và lợi ích ròng mỗi tháng. Với 15 triệu/người và ba người, phép tính đơn giản ra 22,2 tháng; nhóm cần sửa hoặc định nghĩa lại giả định để thống nhất.”

**Có thể bị hỏi tiếp:** 16–18 tháng được suy ra từ khoản tiết kiệm nào và đã trừ bảo trì chưa?

1 tỷ/(3×15 triệu)=22,22 tháng. 1 tỷ/(3×18 triệu)=18,52;/(3×20 triệu)=16,67 tháng, đều chưa OPEX. Đạt 16–18 tháng cần tiết kiệm ròng 55,56–62,5 triệu/tháng. Đạt 20 tháng cần 50 triệu/tháng. Nếu chỉ chuyển công nhân sang khâu khác, đó không tự động là cash salary saving; cần đo output/cost avoidance thực.


## Slide 40

**Slide nói gì:** GanttT1–T8: gđ 1 T1, gđ 2 T2–T3, gđ 3 T4–T5, mục tiêu xa hơn T6–T8; các dòng được làm song song.

**Ý nghĩa thật:** Tổng các duration của dòng không phải calendar duration. Core plan 5 tháng nằm trong 3–6 tháng S2 nếu định nghĩa scope.

**Bằng chứng:** Ảnh render S40 đã kiểm;[H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) chỉ xác nhận training theo lời báo, chưa hoàn thành robot thật.

**Trạng thái:** 🟡 Mô phỏng/train; ⬜ Robot thật và few-shot; không kết luận mâu thuẫn 8 với 6 tháng chỉ vì 8 cột.

**Câu nên nói (không quá 3 câu):** “Kế hoạch core trong hình là T1 đến T5, với dựng mô phỏng và collect/train chạy song song theo giai đoạn. T6 đến T8 dành hướng mở rộng; tiến độ thực cần gắn nghiệm thu phần cứng và metric.”

**Có thể bị hỏi tiếp:** Mốc nào để chuyển giai đoạn, hỏng thử nghiệm thì lùi ở đâu?

Đã xem hình: nghiên cứu 1 tháng+dựng scene 1 tháng cùng T1; data 2 tháng+train 2 tháng cùng T2–T3; triển khai 2 tháng+fine-tune 2 tháng cùng T4–T5. Không cộng thành 10 tháng, không tự coi T8 là hạn core. Mục tiêu xa hơn “học đa phương thức” mơ hồ vì ảnh+state đã đa phương thức; nên ghi “bổ sung force/tactile” nếu đó là ý định, chưa xác nhận.


## Slide 42

**Slide nói gì:** Đã dựng model/mô phỏng/data, đã pretrain RH20T “để học tổng quát”, train/inference “mô overfit” rồi chứng minh học thật; tiếp theo data đích/robot thật/few-shot.

**Ý nghĩa thật:** Có tiến triển thật, nhưng câu kết luận gộp học trên train, tổng quát hóa và task success.

**Bằng chứng:** [R/checkpoints/before_test_20261007_142338/history.json:1](<F:/cfg5_mophong/checkpoints/before_test_20261007_142338/history.json:1>) [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>) [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) [J/src/data/sim_demos.py:68](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:68>).

**Trạng thái:** ✅ Các khối và thử TCP cũ; 🟡 E25 joint theo báo; ⬜ Tổng quát hóa/learned joint success/robot thật/few-shot.

**Câu nên nói (không quá 3 câu):** “Nhóm đã xây dựng pipeline dữ liệu, mô phỏng và thực hiện các lượt train/validation. Lần transfer TCP ban đầu còn hạn chế, nên nhóm đã chuyển sang joint và MCR; nhánh mới cần đánh giá closed-loop. Nhóm chưa kết luận tổng quát hóa hay thay thế công nhân.”

**Có thể bị hỏi tiếp:** “Học thật” của các anh nghĩa là loss giảm, khớp nhãn hay gắp được thật?

Sửa lỗi chữ “hoàn hiện”,“mô overfit”,“few-short”.Pretrain để học tổng quát là**mục tiêu**, không là kết quả đã đo. Đã có smoke fine-tune TCP ngày 08/10, nhưng chưa thấy completed run report; đừng nói hoàn toàn chưa chạm data đích, mà cũng đừng nói đã fine-tune joint xong.

## Bảng kiểm toàn bộ số kinh tế trên slide

| Số/claim | Kết luận đối chiếu |
|---|---|
|8 h/ngày|Giả định quy đổi đơn vị, không phải số ca/takt đo thật |
|250.000đ/h|Engineering cost giả định, khác production wage, chưa có nguồn |
|4/16/40 h|Định mức chọn trong range S25, không time-study |
|4–4–2 task|Mix minh họa, không phải cơ cấu task DENSO đã khảo sát |
|160 h/20 ngày/40 triệu|Phép tính đúng trong mix đó |
|80 h/20 triệu/50%|Đúng nếu setup đã có sẵn và AI 8 h/task, giả định chưa đo |
|80–160 h setup,120 h trung tâm|Tổng và midpoint đúng, không phải quan trắc |
|160–240 h/40–60 triệu lần đầu|Phép tính đúng, gồm setup+80 h |
|15 task/240 h/60 triệu|Điểm giao mô hình giờ công, không tháng CAPEX |
|−10/10/30/70/170 triệu S33|Đúng công thức, nền reuse có điều kiện |
|15 triệu/người, S2|Giả định wage, cần nói base hay total cost |
|18–20 triệu/người, S36|Giả định khác, cần thống nhất cost basis |
|1 tỷ|Chưa BOM/báo giá, tách robot/gripper/camera/PC/cell/safety/integration |
|~20 tháng S2|Số học theo 3×15 ra 22,22, chưa trừ OPEX |
|16–18 tháng S38|Có thể gần case 3×18–20, chưa OPEX; không đúng case 15 |
|24/7, lỗi 2–5%, accuracy cao|Chưa có số đo hệ thống hoặc baseline cell |

## Những điểm slide thực khác bản tóm tắt ban đầu

1. S13 có linh kiện~10 mm/dung sai 2 mm và nội dung hướng force feedback, nằm bên trong ảnh.
2. S36 không ghi nguyên văn câu “chưa dự đoán lực kẹp”; S18 mới ghi điều đó.
3. S40 không có 8 tháng core: kế hoạch core T1–T5, mở rộng T6–T8.
4. S17 claim 1.000 đạt, mâu thuẫn ít nhất với manifest hiện tại 913 accepted/111 rejected; không tự chọn 1000 là số đúng.
5. S42 dùng ngôn ngữ khẳng định “chứng minh…học thật”, trong khi bằng chứng phải tách posterior loss/prior inference/rollout.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Tại sao phải sửa output ở S16 và S18?
2. Tự tính toàn bộ S26, S31–33 và case hoàn vốn S2/S38.
3. S17 đang đếm những gì, có thể gọi là 1.000 demo đạt chưa?
4. Giải thích S40 mà không cộng nhầm duration các dòng song song.
5. Nói rõ ba điều đã làm, ba điều chưa chứng minh ở S42.
