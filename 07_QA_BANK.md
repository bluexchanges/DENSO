# 07 — Ngân hàng 60 câu hỏi giám khảo và trả lời trung thực

Chốt bằng chứng 17/10/2026. Các câu hỏi là dự đoán của mentor, không phải đề do BTC công bố. Câu trả lời mẫu có thể nói trong khoảng 30–60 giây tùy tốc độ; hãy tập bằng đồng hồ, giữ input/output và giới hạn bằng chứng nếu cần rút ngắn. Nguồn web được dẫn truy cập 17/10/2026. Các câu về deployment là kế hoạch, chưa phải tính năng đã lắp.

Hiện trạng xuyên suốt: ✅ controller/evaluator và pipeline; ✅ cache joint MCR theo log; 🟡 người dùng báo E25 nhưng chưa có metric mới; ⬜ learned joint success/robot thật/few-shot/ROI đo thật. Không lấy E58TCP hoặc 3/3 controller để trả lời cho joint MCR mới.

## Cách luyện khi bạn gõ “bắt đầu luyện Q&A”

Hỏi từng câu theo thứ tự A01→J06, chờ bạn trả lời rồi mới chấm. Không đưa ngay đáp án trước khi bạn thử. Chấm 10 điểm: hiểu bản chất 3, đúng dự án/phiên bản 3, bằng chứng 2, trung thực 2. Nêu chỗ sai/thiếu/né tránh, đưa bản sửa ngắn rồi hỏi follow-up khi cần. Không phạt bạn vì chưa có kết quả mà chính tài liệu đánh dấu CHƯA XÁC MINH; chấm cách bạn nhận giới hạn và đề xuất kiểm chứng. Chưa bắt đầu luyện trong lượt tạo tài liệu này.


## A. Ý tưởng và tính mới


### A01

**Câu hỏi:** Các bạn giải quyết bài toán gì, trong một phút?

**Giám khảo muốn kiểm tra:** Hiểu mục tiêu và giới hạn phạm vi.

**Trả lời mẫu (30–60 giây):** Nhóm nhắm tới gắp và đặt linh kiện nhỏ vào khay hoặc khuôn, với mục tiêu giảm công cấu hình khi có các biến thể liên quan. Bài thử hiện tại là Panda trong MuJoCo, đặt ba chốt vào ba lỗ. Nhánh học mới dùng ảnh nhiều camera, trạng thái bảy khớp và độ mở kẹp để dự đoán chuỗi joint. Nhóm đã có mô phỏng, evaluator và pipeline dữ liệu; thành công closed-loop của joint policy và lợi ích trên cell DENSO vẫn phải đo. Vì vậy đây là prototype nghiên cứu có lộ trình pilot, chưa phải sản phẩm đã nghiệm thu.

**Bằng chứng/Con số để dẫn:** [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>) [J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>) [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>); S2/12/42.

**Đừng nói:** “Đã tự động hóa công đoạn DENSO với độ chính xác cao.”

**Câu hỏi tiếp theo có thể bị hỏi:** Công đoạn thật nào, mã linh kiện nào và tiêu chí nghiệm thu là gì?


### A02

**Câu hỏi:** ACT có sẵn, vậy tính mới của nhóm ở đâu?

**Giám khảo muốn kiểm tra:** Phân biệt đóng góp triển khai với phát minh học thuật.

**Trả lời mẫu (30–60 giây):** ACT và MCR là phương pháp của các tác giả, nhóm không nhận là thuật toán mới. Phần nhóm có source là adapter dữ liệu CFG5, căn timestamp, mask camera thiếu, camera identity embedding, cache feature MCR, quản lý contract và evaluator cho task chốt. Giá trị đề xuất là ghép chúng thành một quy trình có thể kiểm tra và thích nghi cho công đoạn cụ thể. Tuy nhiên, tổ hợp đó có tốt hơn baseline hoặc giảm giờ công hay không thì chưa có phép so sánh của nhóm, nên tính mới ứng dụng và hiệu quả vẫn cần chứng minh bằng pilot.

**Bằng chứng/Con số để dẫn:** [J/src/data/cfg5_masked.py:205](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:205>) [J/src/models/rh20t_act.py:34](<F:/cfg5_mophong/local_source_(1)/src/models/rh20t_act.py:34>) [J/src/models/mcr_act.py:44](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:44>); nguồn ACT/MCR trong 04.

**Đừng nói:** “Nhóm sáng chế ACT/CVAE hoặc một foundation model mới.”

**Câu hỏi tiếp theo có thể bị hỏi:** Ablation nào chứng minh adapter của nhóm tạo thêm giá trị?


### A03

**Câu hỏi:** Dự án chỉ có một tay máy, tại sao thuộc Humanoid & Robot?

**Giám khảo muốn kiểm tra:** Mức phù hợp với chủ đề, tránh phóng đại humanoid.

**Trả lời mẫu (30–60 giây):** Nhóm làm nhánh robot manipulation trong chủ đề Humanoid & Robot, không xây dựng một humanoid toàn thân. Panda là nền thử để nghiên cứu quy trình học thao tác và đánh giá trước khi chuyển sang thiết bị được chốt với xưởng. Chủ đề công khai có các hướng học skill từ dữ liệu và tự động hóa linh hoạt, nên bài toán có điểm phù hợp. Nhưng nhóm phải nói rõ phạm vi một tay và chưa giải quyết cân bằng, đi bộ hay phối hợp toàn thân. Nếu BTC yêu cầu một embodiment cụ thể, nhóm sẽ cần điều chỉnh phạm vi và xác nhận với mentor.

**Bằng chứng/Con số để dẫn:** S12; [J/src/simulation/panda_controller.py:34](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:34>); [Technology Challenges](https://densohackathon.vn/theme), truy cập 17/10/2026.

**Đừng nói:** “Panda là humanoid” hoặc “chuyển sang mọi humanoid đều giống nhau”.

**Câu hỏi tiếp theo có thể bị hỏi:** Dự án đăng ký H1 hay H3, deliverable cụ thể là gì?


### A04

**Câu hỏi:** Tại sao chọn chốt và khuôn thay vì linh kiện thật?

**Giám khảo muốn kiểm tra:** Hiểu surrogate task và external validity.

**Trả lời mẫu (30–60 giây):** Chốt và lỗ có hình học rõ nên nhóm định nghĩa được thế nào là cắm đúng, chạm đáy, đã nhả và đứng ổn định. Task này giúp kiểm các khối simulation, controller và evaluator mà không cần ngay dữ liệu vật liệu thật. Nó chưa đại diện đầy đủ cho linh kiện dễ vỡ hoặc bề mặt phản xạ của DENSO. Nhóm cần lấy bản vẽ, gripper, dung sai và điều kiện chất lượng của cell đích, rồi xây bài thử tương ứng. Kết quả trên chốt chỉ được báo trong phạm vi chốt, không được suy thành nghiệm thu linh kiện nhà máy.

**Bằng chứng/Con số để dẫn:** [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>) [J/src/simulation/panda_evaluator.py:6](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:6>); S13.

**Đừng nói:** “Chốt nhỏ hơn nên chắc chắn khó hơn mọi linh kiện thật.”

**Câu hỏi tiếp theo có thể bị hỏi:** Sự khác nhau nào giữa chốt mô phỏng và linh kiện dễ vỡ là quan trọng nhất?


### A05

**Câu hỏi:** Tại sao cần tới tám camera?

**Giám khảo muốn kiểm tra:** Lựa chọn thiết kế có đo chi phí/lợi ích hay chỉ sao chép.

**Trả lời mẫu (30–60 giây):** Tám slot hiện xuất phát từ cấu hình camera CFG5 và rig mô phỏng mà nhóm muốn đối chiếu, gồm sáu camera ngoài và hai in-hand. Nhiều góc nhìn có thể giảm che khuất, nhưng đó là lý do thiết kế chứ chưa chứng minh tám camera là tối ưu. Nhánh mới còn xử lý camera thiếu bằng attention mask và camera dropout. Trước triển khai thật, nhóm cần ablation một, hai, ba và tám view trên cùng protocol, đồng thời đo chi phí, calibration, đồng bộ và latency. Nếu ít camera vẫn đạt tiêu chí thì nên giảm rig.

**Bằng chứng/Con số để dẫn:** [J/configs/data/cfg5_all8.json:6](<F:/cfg5_mophong/local_source_(1)/configs/data/cfg5_all8.json:6>) [J/src/models/mcr_act.py:100](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:100>); S18.

**Đừng nói:** “Tám camera luôn chính xác hơn” hoặc “đã có tám camera thật”.

**Câu hỏi tiếp theo có thể bị hỏi:** Camera nào đóng góp nhiều nhất và camera mất thì policy có chạy được không?


### A06

**Câu hỏi:** Tới hôm nay các bạn thực sự đã làm được gì?

**Giám khảo muốn kiểm tra:** Sự trung thực và mức hoàn thiện.

**Trả lời mẫu (30–60 giây):** Nhóm có source môi trường Panda, controller scripted và evaluator; báo cáo controller cũ đạt ba trên ba seed. ACT TCP trước đây đã train và có thử transfer mười episode nhưng không thành công task nào. Sau đó nhóm chuyển sang joint và MCR, cache CFG5 mới đã hoàn tất theo log. Ghi chép ngày 16/10 là người dùng báo đang ở epoch 25 và yêu cầu tiếp tới 100; hiện chưa có history hoặc rollout joint mới để kiểm độc lập. Vì vậy nhóm chưa công bố success rate của policy mới, robot thật hay few-shot như kết quả đã đạt.

**Bằng chứng/Con số để dẫn:** [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>) [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>) [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>); cache log trong 00.

**Đừng nói:** “Mọi phần đã chạy end-to-end” hoặc “ACT đạt 100%”.

**Câu hỏi tiếp theo có thể bị hỏi:** Vậy video demo đang chiếu là controller hay policy, checkpoint nào?


## B. Kỹ thuật ACT/ML


### B01

**Câu hỏi:** Action chunking giải quyết điều gì, K=20 nghĩa là gì?

**Giám khảo muốn kiểm tra:** Hiểu compounding error và deployment.

**Trả lời mẫu (30–60 giây):** ACT dự đoán một đoạn hành động có liên quan từ observation hiện tại, thay vì chỉ một bước. Điều này giúp học sự nhất quán của chuyển động và giảm khó khăn ghép nhiều quyết định nhỏ, nhưng không xóa distribution shift. K20 của nhánh này là hai mươi bước trên grid 10 Hz, tương ứng hai giây nhãn tương lai. Khi triển khai có thể thực hiện cả đoạn, một phần đoạn hoặc hỏi lại mỗi tick rồi ensemble. Những cách đó có độ phản ứng và chi phí khác nhau; nhánh joint mới chưa có executor rollout được xác minh nên nhóm chưa chốt tần số truy vấn thực tế.

**Bằng chứng/Con số để dẫn:** [J/configs/act/rh20t_all8.json:1](<F:/cfg5_mophong/local_source_(1)/configs/act/rh20t_all8.json:1>) [J/src/data/act_dataset.py:115](<F:/cfg5_mophong/local_source_(1)/src/data/act_dataset.py:115>);02 mục 1/6.

**Đừng nói:** “K20 nghĩa là 20 task” hoặc “chunking bảo đảm không tích lũy lỗi”.

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu vật dịch chuyển giữa chunk hai giây thì xử lý thế nào?


### B02

**Câu hỏi:** CVAE và latent z có vai trò gì?

**Giám khảo muốn kiểm tra:** Hiểu cơ chế train, không đọc thuộc tên mô hình.

**Trả lời mẫu (30–60 giây):** CVAE dùng biến ẩn để mô hình hóa khác biệt giữa các chunk hợp lý cho một observation, chẳng hạn cách tiếp cận hoặc nhịp chuyển động. Trong source này, posterior encoder nhận state và action chunk nhãn, tạo mu và log variance 32 chiều, rồi lấy mẫu z bằng reparameterization. Token latent được kết hợp với ảnh và proprio để dự đoán chunk. KL kéo posterior gần prior. Khi inference không có tương lai thật để đưa vào posterior, model dùng z bằng 0. Nhóm không khẳng định mỗi chiều latent có ý nghĩa thao tác dễ diễn giải hoặc đã đo được lợi ích CVAE trên task của mình.

**Bằng chứng/Con số để dẫn:** [J/src/models/mcr_act.py:113](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:113>) [J/third_party/rh20t_act/models/detr/models/detr_vae.py:65](<F:/cfg5_mophong/local_source_(1)/third_party/rh20t_act/models/detr/models/detr_vae.py:65>).

**Đừng nói:** “z là nhãn task có sẵn” hoặc “inference lấy z từ action thật”.

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu bỏ KL hoặc dùng latent ngẫu nhiên thì có thể xảy ra gì?


### B03

**Câu hỏi:** Loss gồm gì và vì sao KL weight bằng 10?

**Giám khảo muốn kiểm tra:** Hiểu mục tiêu tối ưu, normalization và căn cứ hyperparameter.

**Trả lời mẫu (30–60 giây):** Loss là masked L1 giữa chuỗi action dự đoán và nhãn đã chuẩn hóa, cộng 10 lần KL của posterior Gaussian với prior chuẩn trong config nền. L1 chỉ chia cho số phần tử nhãn thật, bỏ padding. KL cộng theo chiều latent rồi trung bình batch. Hệ số 10 kế thừa baseline RH20T ACT; chưa có sweep của nhóm nên không gọi là tối ưu. L1 normalized cũng không phải millimet hay độ. Muốn đánh giá robot phải denormalize, đo lỗi joint và kẹp riêng, rồi đo task success closed-loop.

**Bằng chứng/Con số để dẫn:** [J/src/models/rh20t_act.py:54](<F:/cfg5_mophong/local_source_(1)/src/models/rh20t_act.py:54>) [J/src/models/mcr_act.py:140](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:140>) [J/configs/act/rh20t_all8.json:1](<F:/cfg5_mophong/local_source_(1)/configs/act/rh20t_all8.json:1>).

**Đừng nói:** “Loss 0,1 nghĩa là sai 0,1mm”, hoặc “10 đã được chứng minh tối ưu”.

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu KL rất nhỏ thì có chắc CVAE hoạt động tốt không?


### B04

**Câu hỏi:** Validation loss thấp có giống inference robot không?

**Giám khảo muốn kiểm tra:** Phát hiện target leakage về chế độ posterior.

**Trả lời mẫu (30–60 giây):** Không hoàn toàn giống. Validation hiện gọi model với actions nhãn nên CVAE vẫn lấy posterior, dù đã eval mode và không cập nhật trọng số. Eval chủ yếu tắt dropout và điều khiển các layer theo mode, không tự bỏ target. Inference triển khai không truyền actions và dùng latent 0. Do đó posterior reconstruction thấp là kiểm tra hữu ích nhưng chưa đo đúng chất lượng prior prediction, càng chưa đo rollout. Nhóm cần báo riêng posterior loss, prior z0 error trên held-out và closed-loop success; số E58 cũ không được gán cho joint model mới.

**Bằng chứng/Con số để dẫn:** [J/src/training/pretrain.py:283](<F:/cfg5_mophong/local_source_(1)/src/training/pretrain.py:283>) [J/src/models/mcr_act.py:113](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:113>) [J/src/models/mcr_act.py:125](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:125>).

**Đừng nói:** “Đã model.eval nên chắc chắn z=0 và tương đương robot chạy.”

**Câu hỏi tiếp theo có thể bị hỏi:** Trong hàm forward, điều kiện chọn posterior nằm ở dòng nào?


### B05

**Câu hỏi:** Tám camera đi qua model như thế nào?

**Giám khảo muốn kiểm tra:** Hiểu backbone, tokens và mask.

**Trả lời mẫu (30–60 giây):** Ảnh từng view đi qua cùng một MCR ResNet50, không phải tám mạng độc lập. Sau resize/crop 224, mỗi view có feature 2048×7×7. Conv 1×1 chiếu sang 512 kênh, nối các view và flatten thành 392 visual tokens. Thêm proprio và latent thành 394 token cho policy encoder; decoder dùng 20 query để ra chuỗi 20×8. Camera identity embedding phân biệt view, còn camera_valid che token của view thiếu. Trong frozen training, loader đọc feature dequantized sẵn nên trường images thực ra chứa feature, không phải RGB; inference ảnh mới vẫn phải chạy backbone.

**Bằng chứng/Con số để dẫn:** [J/src/models/mcr_act.py:73](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:73>) [J/src/models/mcr_act.py:129](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:129>) [J/src/models/rh20t_act.py:34](<F:/cfg5_mophong/local_source_(1)/src/models/rh20t_act.py:34>) [J/src/data/feature_cache.py:393](<F:/cfg5_mophong/local_source_(1)/src/data/feature_cache.py:393>).

**Đừng nói:** “Tám camera là tám ResNet” hoặc “có cache nên inference không tính feature”.

**Câu hỏi tiếp theo có thể bị hỏi:** Camera mask khác action padding mask ở đâu?


### B06

**Câu hỏi:** Temporal ensembling có trong model của các bạn không?

**Giám khảo muốn kiểm tra:** Phân biệt kiến trúc model với executor.

**Trả lời mẫu (30–60 giây):** ACT gốc có tùy chọn kết hợp các prediction từ những chunk khác nhau nhưng cùng nhắm tới một thời điểm thực thi. Đây là logic ở executor, không tự xuất hiện chỉ vì model dự đoán chuỗi. Probe TCP E5 của nhóm ghi rõ lấy action đầu mỗi tick 10 Hz, không phải temporal ensemble. Với nhánh joint mới, nhóm chưa có rollout/executor được xác minh để nói đã dùng ensembling. Nếu thêm, cần chốt trọng số, joint limits, xử lý kẹp và đo độ mượt cùng độ phản ứng, chứ không mặc định cứ trung bình là tốt hơn.

**Bằng chứng/Con số để dẫn:** [R/epoch5_transfer_probe_14120/pick_place_000938/rollout_report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/pick_place_000938/rollout_report.json:1>); [ACT eval_bc](https://github.com/tonyzhaozh/act/blob/main/imitate_episodes.py#L225), truy cập 17/10/2026.

**Đừng nói:** “ACT nào cũng đã bật temporal ensemble”, hoặc nói sai thứ tự trọng số gốc.

**Câu hỏi tiếp theo có thể bị hỏi:** Các bạn sẽ so first-action, partial-chunk và ensemble theo metric nào?


## C. Dữ liệu


### C01

**Câu hỏi:** Một nghìn demo đạt trên slide được kiểm chứng thế nào?

**Giám khảo muốn kiểm tra:** Đếm đúng dataset, success và quality filtering.

**Trả lời mẫu (30–60 giây):** Câu đó hiện phải chỉnh lại. Manifest task đích local chấp nhận 913 episode và từ chối 111 mục; trong phần từ chối có 24 mục không success và 87 mục video lỗi hoặc thiếu frame. Split dùng 731 train,91 val,91 test. Những số này chứng minh tập được importer chấp nhận ở phiên bản manifest đó, không chứng minh đã có một nghìn demo đều đạt. Cũng không nên lấy 913 chia 1024 làm success rate robot vì lỗi video và cách chọn candidate ảnh hưởng mẫu số. Nhóm cần chốt manifest, dữ liệu gốc và tiêu chí chất lượng rồi mới công bố lại số lượng.

**Bằng chứng/Con số để dẫn:** [J/data/splits/pick_place_finetune_manifest.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_manifest.json:1>) [J/data/splits/pick_place_finetune_splits.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_splits.json:1>); S17.

**Đừng nói:** “1.000 đều thành công vì slide ghi thế” hoặc “913/1024 là accuracy ACT”.

**Câu hỏi tiếp theo có thể bị hỏi:** Trong 913 accepted, bao nhiêu trajectory độc lập và bao nhiêu chỉ đổi hình ảnh?


### C02

**Câu hỏi:** Nhãn action của CFG5 mới chính xác là gì?

**Giám khảo muốn kiểm tra:** Semantics measured state so với command.

**Trả lời mẫu (30–60 giây):** State đầu vào là bảy joint đo được theo radian và độ mở kẹp đo được theo mét. Mỗi hàng action có cùng bảy joint ghi thật nhưng ghép với gripper command; loader lấy các hàng tương lai offset 1 tick, tối đa 20 tick. Vì thế phần arm là future measured-state target, chưa phải motor command đã được ghi và xác minh. Đây là lựa chọn có nhãn thật khi TCP thiếu, không phải bịa joint bằng FK. Khi điều khiển phải chuyển prediction thành reference có nội suy và giới hạn phù hợp, đồng thời kiểm trễ của plant.

**Bằng chứng/Con số để dẫn:** [J/src/data/cfg5_masked.py:219](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:219>) [J/src/data/act_dataset.py:115](<F:/cfg5_mophong/local_source_(1)/src/data/act_dataset.py:115>) [J/scripts/prepare_cfg5_masked_mcr.py:134](<F:/cfg5_mophong/local_source_(1)/scripts/prepare_cfg5_masked_mcr.py:134>).

**Đừng nói:** “RH20T ghi trực tiếp mọi lệnh động cơ nên model xuất là gửi thẳng.”

**Câu hỏi tiếp theo có thể bị hỏi:** Observation t và targett+1 có ảnh hưởng gì tới gripper command alignment?


### C03

**Câu hỏi:** Các bạn tránh data leakage bằng cách nào?

**Giám khảo muốn kiểm tra:** Hiểu đơn vị split độc lập và normalization.

**Trả lời mẫu (30–60 giây):** CFG5 được chia theo group task, user, calibration trước khi tạo action chunk, để các dữ liệu thuộc cùng group không bị rải sang train và test. Normalization chỉ fit train. Với demo mô phỏng, importer gom theo seed hoặc numeric trajectory giống nhau; profile fixed chỉ train trong split hiện có. Tuy nhiên, group split không tự bảo đảm unseen task hay unseen object position. Muốn chứng minh OOD, cần định nghĩa thêm phạm vi vị trí, ánh sáng hoặc vật thể không xuất hiện trong train và không dùng test để chọn checkpoint hay chỉnh ngưỡng.

**Bằng chứng/Con số để dẫn:** [J/src/data/splits.py:77](<F:/cfg5_mophong/local_source_(1)/src/data/splits.py:77>) [J/src/data/act_dataset.py:10](<F:/cfg5_mophong/local_source_(1)/src/data/act_dataset.py:10>) [J/src/data/sim_demos.py:230](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:230>).

**Đừng nói:** “Chia ngẫu nhiên frame là đủ độc lập” hoặc “có test split nghĩa là đã few-shot”.

**Câu hỏi tiếp theo có thể bị hỏi:** Tại sao hai cửa sổ chồng nhau từ cùng episode không phải hai thử nghiệm độc lập?


### C04

**Câu hỏi:** Vì sao đổi TCP sang joint, có mất dữ liệu cũ không?

**Giám khảo muốn kiểm tra:** Căn cứ quyết định và kiểm soát phiên bản.

**Trả lời mẫu (30–60 giây):** Ghi chép ngày 11/10 cho thấy có episode thiếu TCP thật, còn kiểm chứng phục hồi TCP bằng FK trên phạm vi rộng chưa đạt, có sai lệch góc khoảng 17 độ. Vì vậy người dùng chọn 7 joint và độ mở kẹp từ dữ liệu ghi thật. Sau phục hồi file joint gốc còn đúng 4 episode thiếu được duyệt loại, giữ raw. Quyết định đó tận dụng được 1317 episode với mask camera, nhưng làm checkpoint TCP và demoTCP không tương thích semantics với policy joint. Dữ liệu cũ vẫn có giá trị lịch sử, chỉ không được đổi tên các chiều rồi dùng như joint.

**Bằng chứng/Con số để dẫn:** [H/chat:3568](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:3568>) [H/chat:4276](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:4276>) [R/BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:76](<F:/cfg5_mophong/BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:76>).

**Đừng nói:** “FK đã chuẩn nên tự sinh joint/TCP tùy ý”, hoặc “cùng 8D thì không cần train lại”.

**Câu hỏi tiếp theo có thể bị hỏi:** Bốn episode loại là vì thiếu joint hay vì policy xử lý không tốt?


### C05

**Câu hỏi:** Domain randomization của nhóm gồm gì, đã chứng minh tác dụng chưa?

**Giám khảo muốn kiểm tra:** Tách augmentation khỏi robustness.

**Trả lời mẫu (30–60 giây):** Slide và các profile dữ liệu mô tả biến thiên màu, nền, ánh sáng, vị trí và vật phụ. Manifest có các profile fixed, varied, diverse, rich; ảnh minh họa cho thấy có thay đổi hình ảnh. Tuy nhiên, source generator đúng phiên bản cho toàn bộ tập và range từng tham số chưa được audit đầy đủ trong lượt này. Nhóm chưa có so sánh bật/tắt randomization trên held-out nên chưa khẳng định nó tăng success. Ngoài biến thiên thị giác, cần kiểm ma sát, độ cứng, khối lượng và trễ nếu muốn nói tới sim-to-real cho thao tác tiếp xúc.

**Bằng chứng/Con số để dẫn:** S17; [J/data/splits/pick_place_finetune_splits.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_splits.json:1>); [Tobin2017](https://arxiv.org/abs/1703.06907), truy cập 17/10/2026.

**Đừng nói:** “Đổi màu đủ để giải quyết sim-to-real.”

**Câu hỏi tiếp theo có thể bị hỏi:** Những tham số vật lý nào đã randomize và phân phối được chọn dựa trên đâu?


### C06

**Câu hỏi:** Nhánh mới có bao nhiêu dữ liệu, và mọi episode đều expert thành công không?

**Giám khảo muốn kiểm tra:** Chất lượng và license dữ liệu.

**Trả lời mẫu (30–60 giây):** Log mới xác nhận 1317 episode được cache, split 1053 train,132 val,132 test, tổng 574493 tick. Đó là số episode hợp lệ theo pipeline joint/mask, không phải số task thành công của robot. Nhánh mới bỏ lọc rating để giữ dữ liệu robot thiếu camera, nên có rủi ro đưa cả quỹ đạo chất lượng thấp vào pretrain. Nhóm cần phân tích chất lượng theo task/rating và so sánh phương án lọc trước khi khẳng định lợi ích. Đồng thời cần audit quyền sử dụng các scene C/NC của RH20T trước pilot thương mại, vì công khai không đồng nghĩa không hạn chế.

**Bằng chứng/Con số để dẫn:** [H/chat:4276](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:4276>) [J/scripts/prepare_cfg5_masked_mcr.py:35](<F:/cfg5_mophong/local_source_(1)/scripts/prepare_cfg5_masked_mcr.py:35>); cache log trong 00; [RH20Tlicense](https://rh20t.github.io/), truy cập 17/10/2026.

**Đừng nói:** “1317 demo đều đạt” hoặc “dataset public nên commercial free”.

**Câu hỏi tiếp theo có thể bị hỏi:** Mẫu thất bại có thể làm behavior cloning học hành vi sai như thế nào?


## D. Mô phỏng và sim-to-real


### D01

**Câu hỏi:** Video gắp được có chứng minh ACT đã học không?

**Giám khảo muốn kiểm tra:** Nhận diện scripted oracle và policy.

**Trả lời mẫu (30–60 giây):** Không tự chứng minh. Controller scripted hiện đọc vị trí vật và offset grasp từ simulator để tạo trajectory, nên có thông tin privileged mà policy không nên được nhận. Báo cáo 3/3 seed ghi rõ act_model_used=false. Video đó chứng minh môi trường, controller và evaluator có thể chạy task trong các điều kiện đã thử. Muốn chứng minhACT, cần nạp checkpoint xác định, chỉ đưa ảnh và trạng thái robot, ghi action từ model, rồi báo N rollout và failure theo cùng evaluator. Nhóm sẽ gắn nhãn video rõ để không dùng demo engineering làm kết quả học.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_demo.py:1](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_demo.py:1>) [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>); S15/17.

**Đừng nói:** “Video đẹp nên ACT chắc chắn thành công.”

**Câu hỏi tiếp theo có thể bị hỏi:** Trong info env có object state, làm sao đảm bảo inference không dùng nó?


### D02

**Câu hỏi:** Tỷ lệ thành công hiện tại bao nhiêu, vì sao có0/10?

**Giám khảo muốn kiểm tra:** Trình bày kết quả thất bại đúng phạm vi.

**Trả lời mẫu (30–60 giây):** Có hai kết quả lịch sử rõ: controller scripted 3/3 seed và ACT TCP checkpoint E5 transfer 0/10 episode validation. Probe E5 còn có offline position distance khoảng 66,65 mm và lỗi kẹp khoảng 29,17 mm, cho thấy chưa đáp ứng task chốt nhỏ trong điều kiện đó. Nhóm không dùng kết quả ấy để kết luận nhánh joint MCR mới cũng thất bại, nhưng cũng không được giấu nó. Hiện chưa cóN/N của nhánh mới. Cần làm rollout đúng representation và báo cả error, success, timeout cùng video; chưa có ablation để quy nguyên nhân 0/10 chỉ cho backbone.

**Bằng chứng/Con số để dẫn:** [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>) [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>).

**Đừng nói:** “0/10 không quan trọng” hoặc “chỉ do ResNet nên đổi MCR là xong”.

**Câu hỏi tiếp theo có thể bị hỏi:** Thí nghiệm nào sẽ phân biệt lỗi dữ liệu, output semantics, vision và controller?


### D03

**Câu hỏi:** Các bạn định nghĩa đặt đúng thế nào?

**Giám khảo muốn kiểm tra:** Chất lượng evaluator và tránh false success.

**Trả lời mẫu (30–60 giây):** Task dùng ba chốt Ø 6 mm, dài 35 mm vào lỗ Ø 7 mm, sâu 12 mm. Đặt đúng không chỉ là gần tâm. Evaluator kiểm bao hình học nằm trong lỗ, độ nhô 23±0,5mm, đáy gần mặt đỡ, không xuyên quá mức, nghiêng trong 3 độ, vận tốc nhỏ, đã nhả và có lực đỡ đáy. Điều kiện phải ổn định ít nhất 0,5 giây, đồng thời có lịch sử grasp hai ngón và lift. Task chỉ thành công khi cả ba chốt đạt. Đó là tiêu chí mô phỏng đã cài; quality check ngoài đời vẫn cần phép đo độc lập.

**Bằng chứng/Con số để dẫn:** [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>) [J/src/simulation/panda_evaluator.py:65](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:65>).

**Đừng nói:** “Nhìn vật trong lỗ là đạt”, hoặc lấy tolerance±0,5mm làm MAE policy.

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu chốt nằm lơ lửng hoặc còn được robot giữ thì evaluator có báo thành công không?


### D04

**Câu hỏi:** Sim-to-real gap của các bạn nằm ở đâu?

**Giám khảo muốn kiểm tra:** Hiểu giới hạn simulator.

**Trả lời mẫu (30–60 giây):** Có ít nhất bốn khoảng cách: ảnh và ánh sáng, động học/tool calibration, tiếp xúc vật lý như ma sát/compliance, và thời gian của camera/inference/controller. Mô phỏng có Panda và contact model, nhưng chưa là digital twin đã hiệu chuẩn của cell DENSO. MCR pretrain và randomization là lựa chọn để thử giảm một phần gap, không bảo đảm chuyển thẳng. Nhóm cần chốt robot thật, đo calibration/tracking và latency, thu ít real demo phù hợp rồi đánh giá an toàn theo gate. Trước đó cần learned rollout joint đạt trong mô phỏng; hiện mắt xích ấy còn thiếu xác minh.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_env.py:12](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:12>) [J/src/models/mcr_act.py:25](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:25>);06 mục 4.

**Đừng nói:** “MuJoCo là vật lý thật nên không còn gap.”

**Câu hỏi tiếp theo có thể bị hỏi:** Các bạn đo tham số ma sát và độ cứng của linh kiện thật bằng cách nào?


### D05

**Câu hỏi:** Nếu robot xưởng là 6 trục hoặc 7 trục khác Panda thì làm thế nào?

**Giám khảo muốn kiểm tra:** Khả thi chuyển embodiment.

**Trả lời mẫu (30–60 giây):** Nhóm chưa biết model robot xưởng nên trình bày hai trường hợp. Robot 6 trục nếu xuất joint thường cần state/action 6 joint cộng gripper, cùng dữ liệu, head, stats và driver mới; không bỏ một góc Panda là chạy. Robot 7 trục khác Panda có thể giữ số chiều nhưng joint zero, sign, link length, limits và tool vẫn khác, nên cũng cần retarget hoặc data tương ứng và thử nghiệm. Ngay cả Panda thật cùng loại còn camera, dynamics và safety gap. Nhóm tái dùng pipeline và có thể thử visual weights, chưa cam kết tái dùng nguyên policy joint.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_controller.py:34](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:34>) [J/src/models/rh20t_act.py:71](<F:/cfg5_mophong/local_source_(1)/src/models/rh20t_act.py:71>);06 mục 3.

**Đừng nói:** “Cùng 7 trục là tương thích” hoặc “6 trục chỉ xóa một output”.

**Câu hỏi tiếp theo có thể bị hỏi:** TCP representation có giúp chuyển robot dễ hơn không, và đánh đổi gì?


### D06

**Câu hỏi:** Model chạy tần số bao nhiêu, có điều khiển trực tiếp động cơ không?

**Giám khảo muốn kiểm tra:** Hiểu các tầng thời gian và real-time.

**Trả lời mẫu (30–60 giây):** Lưới dữ liệu và target của nhóm là 10 Hz, chunk 20 bước bằng 2 giây. Môi trường mô phỏng chạy physics dt 1 ms, controller cập nhật reference trong từng substep và evaluator 100 Hz. Những tần số đó khác nhau. Probe TCP cũ hỏi model mỗi tick 10 Hz; nhánh joint mới chưa có latency hay query frequency thực tế được đo. Nếu dùng Panda FCI thật, API có vòng real-time 1 kHz nhưng cần bộ nội suy/tracking phù hợp, không đưa một mạng vision 10 Hz vào vòng motor rồi mặc định đạt deadline. Robot xưởng khác có giao diện và ràng buộc riêng phải kiểm.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_env.py:23](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:23>) [J/src/simulation/panda_controller.py:74](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:74>); [FCI](https://frankarobotics.github.io/docs/overview.html), truy cập 17/10/2026.

**Đừng nói:** “Inference đang 1 kHz vì dt MuJoCo 1 ms” hoặc “0,325 s check là latency online”.

**Câu hỏi tiếp theo có thể bị hỏi:** Các bạn sẽ đo latency capture-to-command và deadline miss như thế nào?


## E. Triển khai tại nhà máy


### E01

**Câu hỏi:** Làm sao đảm bảo an toàn khi đưa AI vào nhà máy?

**Giám khảo muốn kiểm tra:** Trách nhiệm safety và ranh giới prototype.

**Trả lời mẫu (30–60 giây):** Hiện nhóm chưa có xác nhận an toàn của một cell thật. Các giới hạn workspace và rate trong sim chỉ là lớp kỹ thuật, không thay thế risk assessment và hệ thống safety của robot/cell. Kế hoạch pilot cần kỹ sư xưởng chốt guard, interlock, E-stop, quy trình enable/restart và xử lý sự cố theo thiết bị thực. Policy chỉ sinh reference trong phạm vi được cho phép, không nắm chức năng safety. Nhóm sẽ đi qua các gate mô phỏng, bench và pilot có giám sát trước nghiệp thu. Chưa đủ thông số robot và cell nên chưa đưa ra cam kết an toàn chung chung.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>);06 mục 5; [OSHA risk assessment](https://www.osha.gov/otm/section-4-safety-hazards/chapter-4), truy cập 17/10/2026.

**Đừng nói:** “Cobot tự động an toàn” hoặc “AI đã học va chạm nên không cần guard”.

**Câu hỏi tiếp theo có thể bị hỏi:** Khi người vào cell hoặc camera/GPU hỏng, ai ra lệnh dừng?


### E02

**Câu hỏi:** Không dự đoán lực thì kẹp linh kiện dễ vỡ thế nào?

**Giám khảo muốn kiểm tra:** Thành thật về contact-rich manipulation.

**Trả lời mẫu (30–60 giây):** Đầu ra hiện chỉ joint và width nên nhóm chưa chứng minh điều khiển lực trên vật dễ vỡ. Width nhỏ không đồng nghĩa force nhỏ vì còn cơ cấu, độc ứng, tracking và tiếp xúc. Config có force limit nhưng đó là ràng buộc controller trong sim, không là feedback force policy hoặc test vật liệu. Trước pilot cần lựa chọn gripper/tool, đo lực hoặc contact, chốt ngưỡng chất lượng và cơ chế dừng khi kẹt. Nếu task thật đòi lực tinhvi mà hệ thống hiện chưa đáp ứng, nhóm sẽ thu hẹp mục tiêu hoặc bổ sung feedback, không hứa thay người ngay.

**Bằng chứng/Con số để dẫn:** [J/src/models/mcr_act.py:137](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:137>) [J/configs/mujoco/panda_three_pegs.json:1](<F:/cfg5_mophong/local_source_(1)/configs/mujoco/panda_three_pegs.json:1>); S13/18/36.

**Đừng nói:** “Độ mở kẹp chính là lực” hoặc “20 N chắc an toàn với mọi linh kiện”.

**Câu hỏi tiếp theo có thể bị hỏi:** Lực và tỷ lệ hỏng linh kiện sẽ được đo bằng cảm biến/phép thử nào?


### E03

**Câu hỏi:** Hệ thống tích hợp vào PLC/MES hiện có ra sao?

**Giám khảo muốn kiểm tra:** Khả năng vận hành ngoài demo.

**Trả lời mẫu (30–60 giây):** Hiện source có môi trường và metric mô phỏng, chưa có báo cáo integration PLC/MES production. Phần cần thiết kế là cell state machine nhận recipe/partID, kiểm Ready, phát Busy, trả Done hoặc Fault cùng quality result, có timeout và xác nhận từ thiết bị liên quan. Model/checkpoint và calibration phải được version theo recipe. KhiAI không đủ observation hoặc driver lỗi, cell cần đường dừng và fallback do xưởng phêduyệt. Đây là đề xuất triển khai, không phải tính năng đã lắp. Nhóm cần lấy interface list từ kỹ sư DENSO rồi mới cam kết giao thức và chi phí.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_evaluator.py:65](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:65>) [J/src/simulation/panda_env.py:126](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:126>); S36;06 mục 5.

**Đừng nói:** “Có JSON log nghĩa là đã đồng bộ MES thời gian thực.”

**Câu hỏi tiếp theo có thể bị hỏi:** Cell biết một linh kiện đã đặt đúng và được dây chuyền nhận bằng tín hiệu nào?


### E04

**Câu hỏi:** Robot gắp hụt, làm rơi hoặc đặt kẹt thì xử lý thế nào?

**Giám khảo muốn kiểm tra:** Failure recovery và giới hạn hành vi.

**Trả lời mẫu (30–60 giây):** Trong sim, evaluator có grasp, lift, drop và failure reason để quan sát lỗi, nhưng đó chưa là recovery policy đã được train. Đề xuất pilot là xác nhận grasp/placement bằng tín hiệu phù hợp, dừng có kiểm soát khi lỗi, phân loại part reject hoặc cho phép retry giới hạn khi đã đánh giá an toàn, rồi gọi người nếu lặp lại. Không để model tự thử lại vô hạn hoặc tiếp tục insert khi nghi kẹt. Nhóm cần log loại lỗi, tần suất, thời gian can thiệp và tỷ lệ khôi phục để tính cả KPI và chi phí vận hành.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_evaluator.py:88](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:88>) [J/src/simulation/panda_env.py:147](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:147>);06 mục 5.

**Đừng nói:** “AI học được nên sẽ tự sửa mọi lỗi.”

**Câu hỏi tiếp theo có thể bị hỏi:** Retry bao nhiêu lần, điều kiện nào buộc người xử lý và robot ở trạng thái nào?


### E05

**Câu hỏi:** Ai kiểm tra chất lượng và bảo trì sau triển khai?

**Giám khảo muốn kiểm tra:** Lifecycle cost và trách nhiệm vận hành.

**Trả lời mẫu (30–60 giây):** Nhóm chưa có quy trình vận hành production được xưởng phê duyệt. Evaluator mô phỏng dùng vị trí/contact thật trong sim, còn ngoài đời phải chọn phép đo độc lập như vision inspection, gauge hoặc sensor phù hợp với dung sai. Phần bảo trì cần kiểm gripper, camera/calibration, vệ sinh và regression test sau khi thay thiết bị. Model phải có version, rollback và log ảnh/action/quality cần thiết theo quyền dữ liệu. Thời gian và chi phí cho các việc này phải đưa vào OPEX; hiện chưa đo nên nhóm không nói bảo trì thấp hay 24/7 đã được chứng minh.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_evaluator.py:65](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:65>); S35/36;06 mục 5.

**Đừng nói:** “Đầu tư một lần, hầu như không có bảo trì.”

**Câu hỏi tiếp theo có thể bị hỏi:** Sau khi thay camera hoặc ngón kẹp, điều kiện nào cho phép chạy lại?


### E06

**Câu hỏi:** DENSO có cần cho các bạn robot thật ngay không?

**Giám khảo muốn kiểm tra:** Biết đặt gate nghiệm thu và yêu cầu nguồn lực.

**Trả lời mẫu (30–60 giây):** Nhóm nên chốt thông số và interface sớm để không train sai embodiment, nhưng chưa cần đưa policy chưa đánh giá vào cell đang chạy. Trước tiên cần nối joint adapter, kiểm tracking và đo learned rollout trong sim, rồi dùng bench/pilot có giám sát với tiêu chí đã thống nhất. Nguồn cần xưởng cung cấp là model robot, gripper/tool, bản vẽ linh kiện, calibration khả thi, takt và quality baseline. FAQ cũng ưu tiên mô phỏng rồi đánh giá trước khi xác nhận trên robot thật. Nhóm chưa có success/safety gate bằng số của BTC nên sẽ xin chốt với mentor, không tự nhận đã đủ điều kiện.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>); [FAQH1/Robotics](https://densohackathon.vn/qa), truy cập 17/10/2026.

**Đừng nói:** “Có robot thật thì mai đưa model xuống chạy ngay.”

**Câu hỏi tiếp theo có thể bị hỏi:** Điều kiện tối thiểu để chuyển từ sim sang bench là gì?


## F. Hiệu quả kinh tế/ROI


### F01

**Câu hỏi:** Điểm hòa vốn 15 bài toán có ý nghĩa gì?

**Giám khảo muốn kiểm tra:** Hiểu đúng mô hình engineering effort.

**Trả lời mẫu (30–60 giây):** Con số 15 là điểm giao của hai giả định giờ công triển khai: truyền thống 16 n và AI 120+8n. Giải ra 120 chia 8 bằng 15 task, mỗi phương án 240 giờ. Nó không phải 15 tháng hoàn vốn vốn mua robot, cũng không chứng minh đã làm 15 task. Các hệ số 16,120 và 8 chưa có time-study của nhóm. Nếu setup hoặc độ đa dạng task thay đổi, điểm hòa vốn thay đổi; nếu giờ mỗi task AI không thấp hơn baseline thì không có điểm hòa vốn dương theo mô hình này. Nhóm cần đo cùng phạm vi nghiệm thu để thay giả định bằng dữ liệu.

**Bằng chứng/Con số để dẫn:** S26–33;06 mục 2. Các con số là phép tính từ slide, không phải log sản xuất.

**Đừng nói:** “Robot hoàn vốn sau 15 task nên chắc chắn có lợi.”

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu setup 160 giờ hoặc AI 12 giờ/task thì điểm hòa vốn là bao nhiêu?


### F02

**Câu hỏi:** Tại sao slide ghi 20 tháng ở chỗ này,16–18 tháng ở chỗ khác?

**Giám khảo muốn kiểm tra:** Nhất quán số học và sự trung thực.

**Trả lời mẫu (30–60 giây):** Hai phần đang dùng giả định không thống nhất. Với vốn 1 tỷ và ba người 15 triệu mỗi tháng, tiết kiệm gộp 45 triệu nên payback đơn giản khoảng 22,2 tháng, chưa trừ chi phí vận hành. Nếu dùng 18–20 triệu mỗi người thì ra khoảng 18,5–16,7 tháng, gần con số ở slide 38, nhưng vẫn chưa OPEX và chưa chứng minh thay đủ ba người. Nhóm sẽ sửa về một bảng giả định có nguồn, tách lương cơ bản với tổng chi phí lao động và ghi rõ đây là kịch bản, chưa phải kết quả pilot.

**Bằng chứng/Con số để dẫn:** S2/36/38;06 mục 2, phép tính 1000/(3×15),1000/(3×18),1000/(3×20).

**Đừng nói:** Bịa thêm lợi ích để giữ con số cũ, hoặc nói 20 và 16–18 là cùng một phép tính.

**Câu hỏi tiếp theo có thể bị hỏi:** Lợi ích ròng mỗi tháng phải bao nhiêu để đạt 16–18 tháng?


### F03

**Câu hỏi:** 250.000 đồng/giờ có mâu thuẫn với lương 15 triệu/tháng không?

**Giám khảo muốn kiểm tra:** Phân biệt cost basis và vai trò lao động.

**Trả lời mẫu (30–60 giây):** Chưa chắc mâu thuẫn nếu 250.000 đồng/giờ là chi phí kỹ sư phát triển còn 15 triệu là lương công nhân vận hành. Nhưng slide phải định nghĩa rõ, không được dùng luân phiên cho cùng một khoản. 250.000 nhân 160 giờ bằng 40 triệu là quy đổi số học của engineering rate, không phải xác nhận lương một công nhân. Mức 18–20 triệu có thể là một cost basis khác nhưng hiện chưa có nguồn để tự nhận bao gồm bảo hiểm hoặc overhead. Nhóm cần thống nhất với dữ liệu DENSO; trước đó tất cả là giả định.

**Bằng chứng/Con số để dẫn:** S21 ghi công lập trình/huấn luyện/kiểm thử; S2 và 36 ghi nhân công vận hành.

**Đừng nói:** “Tất cả mức lương đó như nhau”, hoặc tự bịa overhead để hợp thức hóa.

**Câu hỏi tiếp theo có thể bị hỏi:** Đơn giá kỹ sư lấy từ báo giá ngoài hay chi phí nội bộ?


### F04

**Câu hỏi:** Các bạn đã giảm 50%giờ công thật chưa?

**Giám khảo muốn kiểm tra:** Tách projection khỏi measurement.

**Trả lời mẫu (30–60 giây):** Chưa có phép đo của nhóm chứng minh giảm 50%. Slide 27 so 160 giờ với 80 giờ sau khi đã có nền tảng, nên số 50%đúng trong giả định marginal effort đó. Khi cộng setup 80–160 giờ,10 task đầu cần 160–240 giờ, có thể bằng hoặc cao hơn truyền thống. Các định mức 4,16,40 giờ và 8 giờ mỗi task đều cần đo cùng cell và cùng tiêu chí nghiệm thu, bao gồm data, calibration, kiểm thử và xử lý lỗi. Nhóm nên công bố mô hình có điều kiện, không dùng đồ thị như kết quả tiết kiệm đã đạt.

**Bằng chứng/Con số để dẫn:** S24–31; chưa thấy time-sheet hoặc baseline study trong repo.

**Đừng nói:** “Đã tiết kiệm 50%tổng chi phí dự án.”

**Câu hỏi tiếp theo có thể bị hỏi:** Cách tính có bao gồm giờ huấn luyện máy tự chạy và giờ kỹ sư can thiệp không?


### F05

**Câu hỏi:** Vốn 1 tỷ bao gồm những gì, nếu robot có sẵn thì tính sao?

**Giám khảo muốn kiểm tra:** BOM và phân biệt sunk cost với incremental cost.

**Trả lời mẫu (30–60 giây):** Hiện slide chưa có BOM hoặc báo giá chứng minh 1 tỷ, nên nhóm chưa bảo vệ được con số như dự toán mua sắm. Cần tách robot/controller, gripper/tool, camera/đồng bộ, PC/GPU, cell/safety, tích hợp, calibration và công nghiệm thu. Nếu dùng robot sẵn có, phân tích quyết định pilot có thể xét chi phí bổ sung, nhưng vẫn cần ghi chi phí cơ hội, khấu hao hoặc cost basis mà DENSO chọn. Nhóm sẽ trình bày riêng case đầu tư mới và case tận dụng thiết bị, không giữ cùng 1 tỷ cho mọi phương án.

**Bằng chứng/Con số để dẫn:** S2/36;06 mục 2/3. Model robot và báo giá hiện CHƯA XÁC MINH.

**Đừng nói:** “1 tỷ là giá tiêu chuẩn của hệ thống” khi chưa có báo giá.

**Câu hỏi tiếp theo có thể bị hỏi:** Khoản nào chiếm nhiều nhất và phương án ít camera tiết kiệm bao nhiêu?


### F06

**Câu hỏi:** Một robot thay ba người có thực tế không?

**Giám khảo muốn kiểm tra:** Thông lượng, số ca và cash saving.

**Trả lời mẫu (30–60 giây):** Đó hiện là giả định chưa có capacity study. Cần biết ba người làm song song hay ba ca, mỗi người xử lý bao nhiêu sản phẩm, robot có cần người cấp phôi/kiểm lỗi và uptime/yield thực tế ra sao. Nếu chỉ điều chuyển họ sang kiểm tra chất lượng thì chưa tự động giảm chi tiền lương; lợi ích có thể là tăng capacity hoặc tránh tuyển thêm, phải lượng hóa riêng. Nhóm cần đo cycle time, thời gian can thiệp, số ca và chất lượng trước khi quy số người thay thế vào payback. Prototype hiện chưa chứng minh điều đó.

**Bằng chứng/Con số để dẫn:** S2/35/38; chưa có production baseline, cycle-time hoặc staffing study của cell trong repo.

**Đừng nói:** “Robot 24/7 nên bằng ba người 8 giờ, chắc chắn thay được.”

**Câu hỏi tiếp theo có thể bị hỏi:** Ai cấp phôi, xử lý reject và bảo trì trong ba ca?


## G. Mở rộng và few-shot


### G01

**Câu hỏi:** Few-shot của các bạn nghĩa là bao nhiêu demo?

**Giám khảo muốn kiểm tra:** Định nghĩa có thể kiểm nghiệm.

**Trả lời mẫu (30–60 giây):** Hiện few-shot là mục tiêu, chưa có số demo đã được chứng minh đủ cho task mới. Nhóm cần định nghĩa task hoặc biến thể mới, tách dữ liệu đánh giá và chạy learning curve theo các mức demo đã khóa, chẳng hạn 5,10,25,50 như một protocol đề xuất. Mỗi mức phải báo success và số lần lặp, so có/không pretrain dưới cùng ngân sách. Chỉ sau đó mới nói mức nào đạt tiêu chí và tiết kiệm dữ liệu bao nhiêu. Không thể lấy chữ one-shot trong tên RH20T hoặc việc có nhiều task pretrain để kết luận model hiện có few-shot.

**Bằng chứng/Con số để dẫn:** S19; chưa cóN-demo curve hoặc task-heldout results trong artifact đã kiểm;02 mục 8.

**Đừng nói:** “Few-shot là một hoặc vài demo và hiện đã làm được” khi chưa có thử nghiệm.

**Câu hỏi tiếp theo có thể bị hỏi:** Tiêu chí nào cho biết 5 demo đã đủ: loss hay task success?


### G02

**Câu hỏi:** Có bằng chứng pretrain RH20T giúp task đích hơn train từ đầu không?

**Giám khảo muốn kiểm tra:** Causal comparison và ablation.

**Trả lời mẫu (30–60 giây):** Hiện chưa có phép so sánh đó của nhóm. Pretrain có cơ sở nghiên cứu và cho phép tận dụng dữ liệu robot, nhưng chưa chứng minh tăng success hoặc giảm số demo trên task chốt. Thử nghiệm cần giữ cùng split, số demo, architecture, compute và protocol, so ACT random với ACT pretrained; nếu muốn đánh giá MCR thì thêm đối chứng backbone riêng. Sau khi khóa cách chọn checkpoint bằng validation mới đánh giá test/rollout. Với nhánh hiện tại còn phải đồng nhất nhãn joint của demo đích trước; so sánh TCP cũ với joint mới không chỉ thay mỗi yếu tố pretrain.

**Bằng chứng/Con số để dẫn:** [J/src/models/mcr_act.py:44](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:44>) [J/src/data/sim_demos.py:89](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:89>);06G03/G15.

**Đừng nói:** “Paper nói tốt nên nhóm đã chứng minh tốt”, hoặc so khác data rồi quy hết cho pretrain.

**Câu hỏi tiếp theo có thể bị hỏi:** Baseline nào phân biệt tác dụng MCR, action representation và số dữ liệu?


### G03

**Câu hỏi:** Dữ liệu có 104 task thì robot đã làm được 104 task chưa?

**Giám khảo muốn kiểm tra:** Phân biệt dataset coverage với competence.

**Trả lời mẫu (30–60 giây):** Chưa. Báo cáo camera/log của nhánh mới nêu dữ liệu từ 104 task, nhưng đó là độ phủ đầu vào, không phải bảng task success của model. Policy còn không có language instruction hay task token được xác minh, nên ảnh/state có thể chưa đủ để phân biệt hai ý định khác nhau trong cùng cảnh. Muốn claim đa tác vụ, cần định nghĩa task conditioning, đánh giá từng task và cả held-out task hoặc biến thể. Hiện nhóm chỉ nên nói pretrain trên dữ liệu đa dạng và mục tiêu thích nghi; chưa dùng số task dataset như số skill đã làm chủ.

**Bằng chứng/Con số để dẫn:** [H/chat:5394](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5394>) [J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>); S19.

**Đừng nói:** “Robot đã biết 104 skill vì train 104 task.”

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu cùng ảnh nhưng yêu cầu đặt vào hai khay khác nhau, model biết ý định từ đâu?


### G04

**Câu hỏi:** Robot hiện có hiểu lệnh ngôn ngữ như VLA không?

**Giám khảo muốn kiểm tra:** Không nhập tính năng chưa có.

**Trả lời mẫu (30–60 giây):** Không thấy input ngôn ngữ trong model ACT hiện có. Interface nhận state, ảnh hoặc feature và mask; target chỉ được dùng khi train. Vì vậy nhóm không nên nói hệ thống hiểu lệnh tự nhiên hay tự phân rã kế hoạch từ câu nói. Nếu bài toán đa tác vụ cần chọn khay hoặc loại linh kiện theo recipe, phải thêm cơ chế conditioning rõ ràng và dữ liệu tương ứng, hoặc tầng điều phối bên ngoài, rồi đánh giá. VLA như OpenVLA/π 0 là các hướng so sánh có ngôn ngữ và action, nhưng nhóm chưa tích hợp và chưa đo chúng trên task này.

**Bằng chứng/Con số để dẫn:** [J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>); [OpenVLA](https://openvla.github.io/), truy cập 17/10/2026.

**Đừng nói:** “Physical AI nghĩa là đã hiểu tiếng Việt hoặc có L L M.”

**Câu hỏi tiếp theo có thể bị hỏi:** Recipe ID có cần đi vào policy không, hay controller chọn model riêng?


### G05

**Câu hỏi:** Muốn giảm số camera để triển khai rẻ hơn thì có cần train lại không?

**Giám khảo muốn kiểm tra:** Khả năng chuyển observation schema.

**Trả lời mẫu (30–60 giây):** Nhánh masked MCR có cơ chế giữ 8 slot và che view thiếu, nên có thể thiết kế thí nghiệm đánh giá một subset camera mà giữ order/schema. Nhưng cơ chế mask không chứng minh một hoặc hai camera đạt chất lượng cần thiết, nhất là khi rig/ánh sáng ngoài đời khác. Nhóm cần thử các subset có ý nghĩa, đo success, latency và khả năng chịu occlusion; có thể cần fine-tune trên phân phối view thực. Nếu đổi camera order hay preprocessing, phải cập nhật contract phù hợp. Mục tiêu là chọn số camera theoKPI và BOM, không giữ 8 vì đã train như thế.

**Bằng chứng/Con số để dẫn:** [J/src/models/mcr_act.py:100](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:100>) [J/src/data/feature_cache.py:35](<F:/cfg5_mophong/local_source_(1)/src/data/feature_cache.py:35>); S18.

**Đừng nói:** “Cứ mask bớt là không ảnh hưởng” hoặc “mask phục hồi ảnh bị mất”.

**Câu hỏi tiếp theo có thể bị hỏi:** Giảm camera nào vẫn nhìn được giai đoạn insertion?


### G06

**Câu hỏi:** Dự án mở rộng sang linh kiện khác bằng cách gì?

**Giám khảo muốn kiểm tra:** Phạm vi chuyển giao và dữ liệu cần bổ sung.

**Trả lời mẫu (30–60 giây):** Nên bắt đầu từ biến thể gần với task đã kiểm, rồi thay đổi từng yếu tố như vị trí, màu, kích thước hoặc hình dạng có kiểm soát. Mỗi biến thể cần tiêu chí grasp/place và dữ liệu phù hợp; vật dễ vỡ hoặc cần lực khác có thể đòi gripper và controller mới, không chỉ fine-tune ảnh. Nhóm kỳ vọng reuse một phần pipeline và representation, nhưng chưa có learning curve hoặc số giờ chuyển đổi đo thật. Sẽ báo rõ phần giữ nguyên, phần phải thu dữ liệu lại, và success trên biến thể chưa thấy thay vì gọi tất cả là few-shot.

**Bằng chứng/Con số để dẫn:** S14/19/37; [J/src/simulation/panda_evaluator.py:6](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:6>);06G14/G15.

**Đừng nói:** “Chỉ thêm vài ảnh là làm được mọi linh kiện mới.”

**Câu hỏi tiếp theo có thể bị hỏi:** Thay kích thước lỗ và vật liệu cùng lúc có còn là cùng task không?


## H. Đội ngũ, tiến độ và rủi ro


### H01

**Câu hỏi:** Nhánh mới đang ở epoch 100 hay đã xong chưa?

**Giám khảo muốn kiểm tra:** Đọc trạng thái mới nhất, không biến kế hoạch thành kết quả.

**Trả lời mẫu (30–60 giây):** Chưa có bằng chứng đã xong E100. Ghi chép 16/10 là người dùng báo đang E25 và yêu cầu tiếp tới tổng 100, kèm đường dẫn joint MCR run. Code chuẩn bị resume đúng checkpoint, giữ optimizer/RNG/runtime và plot sau mỗi epoch. Log cuối chat cho thấy job14598 đang Pending chờ 14597, sau đó người dùng yêu cầu hủy 14598; chỉ có hướng dẫn hủy, chưa có xác nhận scheduler. Vì vậy nhóm cần lấy history, metadata và log mới nhất trước khi nêu epoch/loss hoàn thành. Cũng không dùng history E58 TCP cũ để chứng minh joint E25 hoặc E100.

**Bằng chứng/Con số để dẫn:** [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>) [H/chat:5810](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5810>) [A/latest_thread_snapshot.json:1](<F:/Denso/docs_denso_hack/_audit/latest_thread_snapshot.json:1>) [L/scripts/resume_mcr_with_plots.py:13](<F:/cfg5_mophong/local_source/scripts/resume_mcr_with_plots.py:13>).

**Đừng nói:** “Đã train 100 epoch” vì đã có script 100 epoch.

**Câu hỏi tiếp theo có thể bị hỏi:** Checkpoint joint mới nhất ở đâu, hash gì và lossval/prior bao nhiêu?


### H02

**Câu hỏi:** Ai trong đội chịu trách nhiệm phần nào?

**Giám khảo muốn kiểm tra:** Ownership và khả năng thực thi.

**Trả lời mẫu (30–60 giây):** Slide giới thiệu thành viên nhưng chưa có bảng ownership và nghiệm thu từng phần trong artifact đã kiểm, nên không nên tự gán kinh nghiệm hay nhiệm vụ không có bằng chứng. Trước pitch, đội cần thống nhất người chịu trách nhiệm dữ liệu/split, model/training, simulation/controller và tích hợp/đánh giá; mỗi người phải chỉ được file, log và rủi ro mình nắm. Phần safety/commissioning thật cần phối hợp kỹ sư xưởng. Thành tích của dự án đọc đồng hồ hoặc giọng nói có thể hỗ trợ nền tảng, nhưng không thay cho số liệu robot hiện tại.

**Bằng chứng/Con số để dẫn:** S4–8;01 bảng module; chưa thấy ma trận phân công/biên bản nghiệm thu trong repo đã kiểm.

**Đừng nói:** Bịa tên người phụ trách hoặc lấy 99% của dự án khác làm kết quả robot.

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu người phụ trách training vắng, ai tái lập được checkpoint và protocol?


### H03

**Câu hỏi:** Ba đến sáu tháng hay tám tháng mới xong?

**Giám khảo muốn kiểm tra:** Đọc Gantt và scope.

**Trả lời mẫu (30–60 giây):** Khi xem hình slide 40, core plan nằm ở T1 đến T5: giai đoạn 1 ở T1, giai đoạn 2 ở T2–T3, giai đoạn 3 ở T4–T5; T6–T8 là mục tiêu xa hơn. Các dòng trong một giai đoạn được vẽ song song, nên không cộng thời lượng thành 10 tháng hoặc kết luận mọi việc phải 8 tháng. Cách nói 3–6 tháng có thể phù hợp với core 5 tháng nếu chốt scope và điều kiện. Tuy nhiên hiện chưa nghiệm thu robot thật, nên lộ trình là dự kiến cần gate kỹ thuật và thời gian thiết bị, không cam kết chắc chắn.

**Bằng chứng/Con số để dẫn:** Ảnh S40; S2;05 mục Slide 40.

**Đừng nói:** “T8 chứng minh 8 tháng core” hoặc cộng mọi duration không xét song song.

**Câu hỏi tiếp theo có thể bị hỏi:** Deliverable và metric nào cho phép chuyển từ T3 sang triển khai thật?


### H04

**Câu hỏi:** Tài nguyên và chi phí huấn luyện có quá lớn không?

**Giám khảo muốn kiểm tra:** Biết compute/storage tradeoff.

**Trả lời mẫu (30–60 giây):** Cache frozen đã hoàn thành theo log khoảng 447,07 GiB cho 1317 episode và 574493 tick; đó chủ yếu là spatial feature INT8 và scale FP16, không phải weights ResNet. MCR weights khoảng 94 MB là khoản khác. Cache giúp không decode MP4 và chạy ResNet mỗi epoch frozen, nhưng tốn đĩa và không miễn phí inference online. Giai đoạn full cần JPEG/ảnh và backbone forward lại; không dùng cache cũ khi encoder đã đổi. Nhóm chưa có benchmark train/infer mới đầy đủ nên cần đo throughput, VRAM, storage và tiền GPU thực, không chỉ nói đã dùng A100 nên nhanh.

**Bằng chứng/Con số để dẫn:** Cache log trong 00; [J/src/data/feature_cache.py:353](<F:/cfg5_mophong/local_source_(1)/src/data/feature_cache.py:353>) [J/src/models/mcr_act.py:62](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:62>).

**Đừng nói:** “447 GiB là weights” hoặc “freeze đồng nghĩa không cần tính vision ngoài đời”.

**Câu hỏi tiếp theo có thể bị hỏi:** Với GPU nhỏ hơn hoặc ít camera, latency và throughput thay đổi bao nhiêu?


### H05

**Câu hỏi:** Rủi ro lớn nhất còn lại là gì?

**Giám khảo muốn kiểm tra:** Biết ưu tiên công việc thực tế.

**Trả lời mẫu (30–60 giây):** Rủi ro gần nhất là semantics chưa nối xong: joint policy nhưng demo đích và API env cũ vẫn TCP. Nếu bỏ qua mắt xích này thì shape đúng vẫn có thể điều khiển sai. Kế tiếp là chưa có success rate joint mới và ablation pretrain; chưa thể bảo vệ generalization, few-shot hoặc ROI đo thật. Cuối cùng là chốt robot/cell thật và safety. Nhóm sẽ ưu tiên đóng contract, kiểm tracking và đo rollout trước khi thêm claim mở rộng. Nếu nguồn lực hạn chế thì thu hẹp task pilot và báo rõ phạm vi, không cố trình bày toàn bộ roadmap như đã hoàn thành.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_env.py:113](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:113>) [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>) [J/src/data/sim_demos.py:89](<F:/cfg5_mophong/local_source_(1)/src/data/sim_demos.py:89>);06G01–G03.

**Đừng nói:** “Không có rủi ro lớn, chỉ cần thêm dữ liệu.”

**Câu hỏi tiếp theo có thể bị hỏi:** Kiểm thử nhẹ nào phát hiện saiTCP/joint trước khi chạy cả episode?


### H06

**Câu hỏi:** Trước ngày thuyết trình, các bạn cần làm gì trước?

**Giám khảo muốn kiểm tra:** Tập trung evidence thay vì thêm slide.

**Trả lời mẫu (30–60 giây):** Ưu tiên đầu là chốt một bản snapshot run mới: config, history, checkpoint hash, model representation và trạng thái job. Sau đó sửa các slide lệch phiên bản và con số kinh tế không thống nhất. Về thí nghiệm, nên đóng adapter joint và kiểm nhỏ observation/action/tracking, trước khi chạy rollout có protocol để lấy N/N thật. Đồng thời xác nhận model robot và baseline cell với mentor. Mục đích là có ít kết luận nhưng bảo vệ được, không chạy thêm training dài chỉ để tăng số epoch. Những việc này chưa được chạy thay trong lượt audit chỉ đọc.

**Bằng chứng/Con số để dẫn:** 09 bảng Top 5; [H/chat:5754](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:5754>);06 khoảng trống đã liệt kê.

**Đừng nói:** “Cứ train lâu hơn sẽ giải quyết mọi vấn đề.”

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu chỉ còn một ngày thì bỏ bớt claim nào để giữ pitch trung thực?


## I. So sánh giải pháp


### I01

**Câu hỏi:** Tại sao không dùng teach pendant, vừa rẻ vừa ổn định?

**Giám khảo muốn kiểm tra:** Biết khi nào AI không đáng dùng.

**Trả lời mẫu (30–60 giây):** Với cell cố định, ít mã linh kiện và fixture tốt, teach pendant có thể là lựa chọn kinh tế và dễ nghiệm thu hơn. Nhóm không có bằng chứng ACT thắng trong mọi tình huống. Lý do nghiên cứu IL là task có biến thiên liên quan, kỳ vọng giảm công cấu hình bằng dữ liệu và tái dùng hệ thống. Nhưng cần baseline cùng robot, quality và takt; phải tính collect data, calibration, retrain và recovery. Nếu số task ít hoặc AI không đạt độ ổn định thì nhóm sẽ đề xuất phương án truyền thống hoặc hybrid, không ép AI vào một bài toán đã giải tốt.

**Bằng chứng/Con số để dẫn:** S24–34;04 bảng so sánh; chưa có measured baseline của nhóm.

**Đừng nói:** “Teach pendant lỗi thời” hoặc “thay task là phải mua robot mới”.

**Câu hỏi tiếp theo có thể bị hỏi:** Đối với 10 task đơn giản của DENSO, AI có đáng đầu tư không?


### I02

**Câu hỏi:** Vision cổ điển tìm vật rồi IK thì thiếu gì?

**Giám khảo muốn kiểm tra:** Không dựng đối thủ yếu để làm nổiAI.

**Trả lời mẫu (30–60 giây):** Vision định vị cộng motion planning/IK là baseline rất đáng thử nếu hình học, vật và điều kiện ảnh có thể kiểm soát. Nó thường dễ kiểm lỗi và giải thích. IL có thể hữu ích khi kỹ năng tiếp cận/kẹp/đặt và biến thiên khó viết logic, nhưng đó chỉ là động cơ chọn phương pháp, không phải kết quả đã so sánh. Controller hiện tại của nhóm cũng dùng IK, nhưng đọc object state privileged nên chưa là vision baseline công bằng. Cần một pipeline vision thật với calibration, sau đó so giờ công, success và robustness trên cùng task.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_controller.py:42](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:42>) [J/src/simulation/panda_demo.py:1](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_demo.py:1>); S14.

**Đừng nói:** “IK không xử lý được gắp–đặt” hoặc “controller oracle chính là camera+vision baseline”.

**Câu hỏi tiếp theo có thể bị hỏi:** Baseline vision có được dùng cùng camera và cùng ngân sách tuning không?


### I03

**Câu hỏi:** ACT khác behavior cloning thuần thế nào?

**Giám khảo muốn kiểm tra:** Hiểu ACT là IL/BC và đóng góp cụ thể.

**Trả lời mẫu (30–60 giây):** ACT vẫn là học bắt chước từ demonstration theo hướng behavior cloning. Khác với baseline một bước cơ bản, nó dự đoán chunk action, dùng Transformer để kết hợp observation và CVAE cho latent khi train; temporal ensembling là tùy chọn executor trong ACT gốc. Nó không tự tương tác với môi trường để tối ưu reward như RL. Chunking có thể giúp nhất quán chuỗi và giảm bớt khó khăn chân trời, nhưng vẫn bị distribution shift. Để biết mức lợi của ACT trong dự án, cần so CNN/MLP BC một bước với cùng data, budget và rollout protocol; nhóm chưa có phép so đó.

**Bằng chứng/Con số để dẫn:** [J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>) [J/src/data/act_dataset.py:115](<F:/cfg5_mophong/local_source_(1)/src/data/act_dataset.py:115>);02; ACT paper trong 04.

**Đừng nói:** “ACT không phải BC” hoặc “ACT tự học thông qua phần thưởng”.

**Câu hỏi tiếp theo có thể bị hỏi:** Nếu bỏ chunk và CVAE thì baseline được thiết kế ra sao?


### I04

**Câu hỏi:** Tại sao không dùng RL để robot tự học?

**Giám khảo muốn kiểm tra:** Tradeoff dữ liệu, reward, compute và safety.

**Trả lời mẫu (30–60 giây):** RL có thể học qua tương tác và tối ưu mục tiêu, nên là một hướng có giá trị, nhưng cần design reward, khám phá và rất nhiều thử nghiệm. Với thao tác insert và vật dễ vỡ, thử trên robot thật còn thêm rủi ro; trong sim thì policy có thể tận dụng sai khác vật lý. Nhóm đã có trajectory ghi thật và controller demo, nên chọn IL làm điểm bắt đầu dễ kiểm hơn theo phạm vi. Chưa có benchmark để kết luận RL kém hơn. Về sau có thể nghiên cứu hybrid IL+RL, sau khi có baseline, safety và evaluator đáng tin cậy; hiện chưa triển khai hướng đó.

**Bằng chứng/Con số để dẫn:** [J/src/data/cfg5_masked.py:205](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:205>) [J/src/simulation/panda_evaluator.py:65](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_evaluator.py:65>); S22/23.

**Đừng nói:** “RL không dùng được trong nhà máy” hoặc “IL không cần kiểm tra an toàn”.

**Câu hỏi tiếp theo có thể bị hỏi:** Reward không cho phép robot kê chốt để ăn điểm giả sẽ định nghĩa thế nào?


### I05

**Câu hỏi:** Tại sao không chọn Diffusion Policy?

**Giám khảo muốn kiểm tra:** So sánh phương pháp có căn cứ, không claim tốc độ vô chứng.

**Trả lời mẫu (30–60 giây):** Diffusion Policy cũng học từ demo và có thể sinh chuỗi action thông qua các bước denoising, nên là baseline phù hợp cho multimodal action. ACT của nhóm đã có nền source và CVAE/chunking, còn độ phức tạp deploy cần đo trên hardware thật. Không nên khẳng định mọi Diffusion Policy đều chậm hơn ACT, vì còn sampler, số bước và tối ưu implementation. Nhóm chưa so cùng task nên chỉ nói rõ tradeoff và kế hoạch đánh giá success, latency, data efficiency với cùng observation/action contract. DiffusionAD của đội thắng 2025 là anomaly detection, không phải Diffusion Policy robot.

**Bằng chứng/Con số để dẫn:** [DiffusionPolicyofficial](https://diffusion-policy.cs.columbia.edu/), truy cập 17/10/2026;04 và 02.

**Đừng nói:** “Diffusion Policy chắc chắn chậm”, hoặc lấy DiffusionAD làm benchmark robot.

**Câu hỏi tiếp theo có thể bị hỏi:** Các bạn giữ action horizon, số demo và compute như thế nào khi so sánh?


### I06

**Câu hỏi:** OpenVLA hoặc π 0 có phải lựa chọn tốt hơn không?

**Giám khảo muốn kiểm tra:** Phạm vi generalist so với task hẹp và ngân sách.

**Trả lời mẫu (30–60 giây):** VLA hướng tới kết hợp ảnh, ngôn ngữ và action cho nhiều task, nhưng không có nghĩa tự động đạt chính xác cao ở một cell insert cụ thể. ACT nhóm hiện không nhận ngôn ngữ, task scope hẹp hơn và cần baseline đúng data. Dùng VLA sẽ cần hợp đồng action, robot, camera, data fine-tune và compute tương ứng; nhóm chưa triển khai hoặc đo trên setup này. Vì vậy không kết luận VLA kém hơn hoặc tốt hơn chỉ từ quy mô model. Nếu cell cần nhiều recipe/lệnh ngôn ngữ, đó là động cơ để thử generalist policy, sau khi một baseline manipulation đã được kiểm.

**Bằng chứng/Con số để dẫn:** [OpenVLA](https://openvla.github.io/),[π0](https://www.pi.website/blog/pi0), truy cập 17/10/2026;[J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>).

**Đừng nói:** “ACT hiện tại là VLA” hoặc “model càng lớn thì tự khắc chính xác hơn”.

**Câu hỏi tiếp theo có thể bị hỏi:** Lệnh ngôn ngữ thêm giá trị gì với cell chỉ làm một loại linh kiện?


## J. Câu hỏi bẫy


### J01

**Câu hỏi:** Có phải các bạn đang lấy controller demo để giả là AI?

**Giám khảo muốn kiểm tra:** Sự trung thực của bằng chứng.

**Trả lời mẫu (30–60 giây):** Nếu chỉ chiếu video controller mà không ghi nhãn thì đúng là dễ gây hiểu nhầm, nên nhóm phải sửa cách trình bày. Báo cáo controller đã ghiact_model_used=false và đọc privileged state; nhóm chỉ dùng nó chứng minh môi trường và logic đánh giá. Kết quả học phải đi với checkpoint, inference input và N rollout riêng. Bằng chứng TCP trước đây có0/10 transfer, còn joint MCR mới chưa cóN/Nđể công bố. Nhóm sẽ nêu cả giới hạn và thất bại đó, không dùng kết quả scripted để thay thế kết quả policy.

**Bằng chứng/Con số để dẫn:** [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>) [J/src/simulation/panda_demo.py:1](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_demo.py:1>) [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>).

**Đừng nói:** Né câu hỏi, nói “controller cũng là AI”, hoặc giấu0/10.

**Câu hỏi tiếp theo có thể bị hỏi:** Cho xem log khẳng định action trong video đến từ checkpoint nào. 


### J02

**Câu hỏi:** Các bạn chỉ chép code và không hiểu model thì sao?

**Giám khảo muốn kiểm tra:** Ownership trí tuệ và khả năng giải thích.

**Trả lời mẫu (30–60 giây):** Nhóm dùng nền tảng mã nguồn của tác giả và cần ghi công rõ, không nhận ACT hoặc MCR là phát minh của mình. Cách bảo vệ là giải thích được data contract, shape, units, CVAE train/infer, mask và giới hạn kết quả, rồi chỉ được adapter/evaluator nào nhóm xây dựng. Việc có code chạy hoặc nhận hỗ trợ từ công cụ không thay thế hiểu biết đó. Nếu một phần chưa nắm hoặc chưa đo, nhóm nên nói rõ và đưa kế hoạch kiểm, thay vì diễn giải theo sơ đồ gốc sai với nhánh joint MCR hiện tại.

**Bằng chứng/Con số để dẫn:** [J/src/models/rh20t_act.py:17](<F:/cfg5_mophong/local_source_(1)/src/models/rh20t_act.py:17>) [J/src/models/mcr_act.py:94](<F:/cfg5_mophong/local_source_(1)/src/models/mcr_act.py:94>) [J/src/data/cfg5_masked.py:205](<F:/cfg5_mophong/local_source_(1)/src/data/cfg5_masked.py:205>);02/03.

**Đừng nói:** “Chúng em tự viết toàn bộ ACT/MCR” hoặc đọc thuật ngữ để né shape/units.

**Câu hỏi tiếp theo có thể bị hỏi:** Giải thích một sample đi từ joint.npy tới prediction và actuator. 


### J03

**Câu hỏi:** Số 99%trong slide có phải kết quả robot không?

**Giám khảo muốn kiểm tra:** Không chuyển thành tích dự án khác thành metric robot.

**Trả lời mẫu (30–60 giây):** Không. Số 99%ở slide 7 thuộc kinh nghiệm dự án đọc đồng hồ/mức dầu được nêu cho một thành viên, không phải success rate ACT gắp chốt. Trong phạm vi audit này cũng chưa có báo cáo độc lập xác minh metric đó nên cần chuẩn bị nguồn nếu giữ trên slide. Với robot, nhóm phải báo đúng kết quả controller và learned policy riêng, kèm số episode, task và điều kiện. Nhóm không có một con số 99%cho policy joint mới và sẽ không dùng thành tích cá nhân để lấp chỗ trống kết quả thí nghiệm.

**Bằng chứng/Con số để dẫn:** S7; [L/outputs/controller_evaluation/summary.json:1](<F:/cfg5_mophong/local_source/outputs/controller_evaluation/summary.json:1>) [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>);05S7.

**Đừng nói:** “Đội từng làm 99%nên robot này cũng đủ tin cậy99%.”

**Câu hỏi tiếp theo có thể bị hỏi:** 99%đó là accuracy, F1 hay MAE, đo ở đâu?


### J04

**Câu hỏi:** Nếu đem xuống xưởng ngày mai thì chạy luôn được không?

**Giám khảo muốn kiểm tra:** Nhận giới hạn deploy, không lùi sang khẩu hiệu.

**Trả lời mẫu (30–60 giây):** Chưa thể hứa chạy production ngày mai. Nhánh mới còn cần joint observation/executor phù hợp, demo đích đúng nhãn và learned rollout có số liệu; loại robot xưởng cũng chưa được chốt. Các bước tiếp là khóa config/checkpoint, kiểm nhỏ tracking và limits, đánh giá sim, rồi bench/pilot có giám sát cùng kỹ sư xưởng với yêu cầu quality/safety. Nhóm có thể trình bày source, dữ liệu và roadmap cụ thể ngay, nhưng không đổi một prototype thành sản phẩm sẵn sàng chỉ vì có tay máy. Nếu cần demo sớm phải ghi rõ phạm vi scripted hoặc learned.

**Bằng chứng/Con số để dẫn:** [J/src/simulation/panda_env.py:113](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_env.py:113>) [J/src/simulation/panda_controller.py:16](<F:/cfg5_mophong/local_source_(1)/src/simulation/panda_controller.py:16>);06G01–G03/G10.

**Đừng nói:** “Chỉ đổi model XML là deploy được.”

**Câu hỏi tiếp theo có thể bị hỏi:** Gate đầu tiên có thể hoàn thành trong một ngày là gì?


### J05

**Câu hỏi:** Loss giảm nhưng robot không gắp được, các bạn đã thành công chưa?

**Giám khảo muốn kiểm tra:** Phân biệt optimization với task competence.

**Trả lời mẫu (30–60 giây):** Nhóm chỉ có thể nói thành công ở bước tối ưu hoặc kiểm pipeline nếu loss giảm đúng protocol; chưa thành công nhiệm vụ robot. Offline loss có thể thấp vì target posterior, dữ liệu dễ, label proxy hoặc normalization, trong khi closed-loop gặp state khác và controller mismatch. Cần prior z=0 error, action tracking và rollout để phân loại nguyên nhân. Bằng chứng E5 transfer trước đây 0/10 cho thấy không nên đồng nhất hai loại kết quả. Nhóm sẽ báo riêng từng tầng và dùng task success cùng chất lượng/chu kỳ để quyết định nghiệm thu, không đổi định nghĩa thành công theo metric đang đẹp.

**Bằng chứng/Con số để dẫn:** [J/src/training/pretrain.py:283](<F:/cfg5_mophong/local_source_(1)/src/training/pretrain.py:283>) [R/epoch5_transfer_probe_14120/report.json:1](<F:/cfg5_mophong/epoch5_transfer_probe_14120/report.json:1>);02 mục 5/9.

**Đừng nói:** “Loss xuống là đã chứng minh robot biết làm” hoặc “0/10 vẫn là thành công task”.

**Câu hỏi tiếp theo có thể bị hỏi:** Bạn sẽ kiểm nguyên nhân nào trước, theo thứ tự nào?


### J06

**Câu hỏi:** Điểm nào trong slide các bạn phải đính chính ngay?

**Giám khảo muốn kiểm tra:** Chủ động sửa claim và không che mâu thuẫn.

**Trả lời mẫu (30–60 giây):** Ba điểm cần sửa ngay là output pose ở slide 16/18 thành joint theo nhánh mới, claim một nghìn demo đạt theo manifest hiện chấp nhận 913, và câu “chứng minh học thật/tổng quát” ở slide 42 cho đúng mức bằng chứng. Phần kinh tế cũng cần thống nhất mô hình: case ba người 15 triệu với vốn 1 tỷ ra 22,2 tháng trước OPEX, còn 15 task là hòa vốn engineering hours. Nhóm sẽ giữ các hướng few-shot, robot thật và 24/7 như mục tiêu có gate, không đưa thành kết quả. Những sửa này làm bản pitch sát dữ liệu hơn và giúp giám khảo đánh giá đúng tiến độ.

**Bằng chứng/Con số để dẫn:** [H/chat:3568](<C:/Users/ADMIN/.codex/sessions/2026/10/09/rollout-2026-10-09T02-26-45-01a0efcd-3cdf-7091-9e7f-d7a9b07cc2c6_01a11cfb-7bc7-7242-b892-5079ec9af8d1.jsonl:3568>) [J/data/splits/pick_place_finetune_manifest.json:1](<F:/cfg5_mophong/local_source_(1)/data/splits/pick_place_finetune_manifest.json:1>); S2/16/17/18/35/38/42;06.

**Đừng nói:** “Các con số chỉ minh họa nên không cần nhất quán.”

**Câu hỏi tiếp theo có thể bị hỏi:** Sau khi sửa claim, giá trị chính còn lại của dự án là gì?


## 10 câu nguy hiểm nhất và cách xử lý

| Câu | Nguy hiểm ở đâu | Cách xử lý khi bị ép trả lời ngay |
|---|---|---|
|A06 — Đã làm được gì?|Dễ gộp mọi phiên bản thành một hệ hoàn chỉnh|Nói rõ controller, TCP cũ, joint mới và bước chưa có metric.|
|B04 — Valloss giống inference?|Dễ nhầm eval mode với bỏ target|Chỉ điều kiện actions!=None và nêu posterior/prior riêng.|
|C01 — 1.000 demo đạt?|Số slide không khớp manifest|Đính chính 913 accepted/111 rejected, không biến thành success rate.|
|C04 — Đổi TCP/joint?|Cùng 8D nhưng sai nghĩa có thể dẫn đến control sai|Nêu lý do joint thật và contract/data/stats phải đổi.|
|D01 — Video chứng minh_AI?|Demo scripted có privileged state|Nhận nhãn controller và đưa checkpoint/log riêng nếu là policy.|
|D02 — 0/10?|Dễ né thất bại hoặc đổ cho một thành phần|Nói đúng E5 TCP 10 val, không gán cho joint mới, đề xuất phép kiểm nguyên nhân.|
|E01 — Safety?|Trả lời quáđà có hậu quả nghiêm trọng|Nhận chưa nghiệm thu, phân rõ RA/cell safety với AI reference.|
|F02 — Payback?|Số học sai, lương và OPEX không rõ|Tính 22,2 tháng case 15 triệu, phân biệt 15 task, cần net benefit.|
|G02 — Pretrain có giúp?|Thiếu ablation nên không có kết luận nhân quả|Nói có cơ sở, chưa đo, đưa đối chứng cùng contract/budget.|
|H01 — E100 xong?|Lệnh/cài đặt/pending không là training hoàn thành|Nêu E25 theo báo, job14598 pending rồi yêu cầu hủy, chưa có history mới.|

Mẫu xử lý chung: **“Hiện nhóm đãX, chưa có bằng chứng Y. Bước tiếp theo làZ; nhóm sẽ đánh giá bằng W.”** X phải có artifact, Y phải nói thẳng, Z cụ thể và W có metric/protocol; đừng chỉ nói “sẽcải thiện”.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Trả lời A06 trong 60 giây mà không gộp controller, TCP và joint.
2. Trả lời B04 và C04 bằng shape/semantics cụ thể.
3. Tính lại F01/F02 mà không nhìn slide.
4. Nhận một giới hạn trong E01/G02 mà không né tránh hoặc phủ nhận phần đã làm.
5. Chọn câu nguy hiểm nhất với bạn và đưa một link bằng chứng đúng run.
