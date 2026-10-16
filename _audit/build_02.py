from doc_helpers import write
write('02_ACT_EXPLAINED.md',r'''
# 02 — ACT, từ trực giác tới đúng model trong dự án

Mốc hiện trạng: 17/10/2026. **Học nhánh joint/MCR trước.** TCP/ResNet18 ở cuối dùng để hiểu lịch sử, không phải input/output hiện tại. Các đoạn giải thích cơ chế là kiến thức/phân tích kỹ thuật; nhãn ✅ chỉ xác nhận source/log, không xác nhận policy đã giải được task.

## 1. Tại sao dự đoán một action chunk?

Hình dung bạn dạy người mới gắp chốt. Nếu mỗi lần chỉ nói một chuyển động rất nhỏ, người đó dễ giật, do dự và đi chệch đường mẫu. Bạn có thể dạy một đoạn chuyển động có liên quan: tiếp cận, hạ xuống, đóng kẹp. ACT dùng một quan sát hiện tại để dự đoán **K hành động liên tiếp**. K là số bước thời gian, không phải số tác vụ và không nhất thiết trùng các pha grasp/lift/place. Trong nhánh này K=20 trên lưới 10 Hz, tương ứng chân trời nhãn **2 giây**. [[J:configs/act/rh20t_all8.json:1]] [[J:src/data/act_dataset.py:115]]

Behavior cloning một bước học từ các trạng thái expert thường đi qua. Khi robot dự đoán hơi sai, trạng thái kế tiếp có thể nằm ngoài vùng dữ liệu. Model lại dự đoán ở trạng thái lạ, sai số có thể tiếp tục tăng: **compounding error**. Chunking giảm số lần phải ghép các quyết định nhỏ thành một chuỗi nhất quán, nhưng không bảo đảm loại bỏ lệch distribution. Nếu thực thi cả đoạn dài mà không nhìn lại, robot còn phản ứng chậm với vật dịch chuyển. [ACT paper](https://roboticsproceedings.org/rss19/p016.html), [phân tích distribution shift của DAgger](https://proceedings.mlr.press/v15/ross11a.html), truy cập 17/10/2026.

Ba chính sách thực thi khác nhau:

| Cách dùng chunk | Tần số model nếu action tick 10 Hz | Đổi lại |
|---|---|---|
| Chạy đủ 20 action rồi hỏi lại | 0,5 Hz, **chỉ là phép tính nếu chọn cách này** | Tiết kiệm inference nhưng 2 s không cập nhật quan sát |
| Mỗi tick hỏi lại và lấy action đầu | 10 Hz mục tiêu | Quan sát mới thường xuyên, bỏ phần lớn chunk ở deployment |
| Mỗi tick hỏi lại và temporal ensemble | 10 Hz mục tiêu | Kết hợp dự đoán chồng nhau, cần bộ nhớ và quy tắc trọng số |

✅ Transfer probe TCP E5 cũ dùng cách thứ hai, report ghi rõ z=0 và first action mỗi tick 10 Hz. ⬜ Nhánh joint mới: **chưa có rollout để xác minh cách thực thi chunk và latency**. Không được suy ra “đang chạy 0,5 Hz” chỉ từ chunk_size. [[R:epoch5_transfer_probe_14120/pick_place_000938/rollout_report.json:1]]

## 2. Phân biệt ACT gốc, upstream sử dụng và adapter của nhóm

| Phần | ACT/ALOHA gốc | Dự án đang dùng |
|---|---|---|
| Nguồn thuật toán | Zhao, Kumar, Levine, Finn, RSS 2023 | Kế thừa ACT qua `rh20t/act_baseline`, commit `107ce1287a46be3a1a7ea954f8bbdec3bb103288` |
| Robot/output | Cấu hình gốc ALOHA hai tay, state/action 14D trong code chính thức | Panda một tay, 7 góc khớp + width = 8D ở nhánh hiện tại |
| Thị giác | ResNet18 trong code ACT chính thức | MCR pretrained ResNet50, frozen trước, 8 slot camera |
| Multiview | Feature ảnh được đưa vào Transformer | Thêm camera identity embedding và attention mask cho camera thiếu |
| Loss | Reconstruction + KL | Masked L1 đúng valid elements + 10×KL |
| Thực thi | Có tùy chọn temporal aggregation trong repo gốc | Probe TCP dùng first-action mỗi tick; joint mới chưa có chứng cứ executor |
| Kết quả | Kết quả paper trên setup tác giả | Không mượn success rate paper làm success rate của nhóm |

Nguồn: [ACT gốc](https://github.com/tonyzhaozh/act), [RH20T baseline](https://github.com/rh20t/act_baseline), truy cập 17/10/2026; [[J:configs/act/rh20t_all8.json:1]] [[J:src/models/rh20t_act.py:34]] [[J:src/models/mcr_act.py:44]].

✅ Đóng góp triển khai có source: kiểm schema/timestamp, masked views, train-only statistics, camera embedding, MCR adapter và cache INT8, freeze BN, checkpoint contract, evaluator task. **CHƯA XÁC MINH tính mới học thuật** của tổ hợp này; không nói nhóm sáng chế ACT hoặc sáng chế MCR.

## 3. Kiến trúc thật của nhánh MCR

Ký hiệu: B=batch, V=8 slot camera, d=512, K=20, D_a=D_s=8, d_z=32. Giá trị kiến trúc lấy từ config nền và source adapter; metadata checkpoint E25 trên server vẫn cần kiểm để xác nhận không override. [[J:configs/act/rh20t_all8.json:1]] [[J:third_party/rh20t_act/models/detr/models/detr_vae.py:65]]

```mermaid
flowchart TD
  RGB["RGB B x 8 x 3 x 360 x 640 uint8"] --> PP["float/255, resize short256\ncenter224, ImageNet normalize"]
  PP --> RN["MCR ResNet50 shared cho từng view\nfrozen weights và BN"]
  RN --> F["B x 8 x 2048 x 7 x 7\nhoặc đọc feature cache đã dequantize"]
  F --> PROJ["Conv1x1: 2048 → 512\nB x 512 x 7 x 56"]
  PROJ --> TOK["392 visual tokens\n2D position + camera identity + view mask"]
  S["state chuẩn hóa B x 8\nq1..q7 rad + width m"] --> ST["Linear 8 → 512\nproprio token"]
  S --> CV["CVAE encoder lúc có target\nCLS + state + 20 action tokens"]
  A["nhãn B x 20 x 8\nis_pad B x 20"] --> CV
  CV --> Z["mu, logvar B x 32\nz=mu+std*epsilon khi train"]
  ZERO["Inference: z=zeros B x 32"] --> ZP["Linear32 → 512\nlatent token"]
  Z --> ZP
  TOK --> ENC["Transformer encoder\n394 token gồm visual + state + latent"]
  ST --> ENC
  ZP --> ENC
  ENC --> DEC["Transformer decoder\n20 learned temporal queries"]
  DEC --> HEAD["Linear512 → 8\nchuỗi B x 20 x 8"]
```

### 3.1. Backbone và 8 camera

`extract_features()` gộp batch và view, chạy **cùng một ResNet50**, rồi tách lại view. Không có 8 ResNet độc lập phải học riêng. Camera thiếu không chạy như ảnh quan sát thật; feature slot đó được điền 0, mask false. Mỗi view ra 2048×7×7. Sau Conv1×1, nối theo chiều rộng thành 512×7×56, flatten ra 392 visual tokens. [[J:src/models/mcr_act.py:73]] [[J:src/models/mcr_act.py:129]]

Camera identity embedding giúp Transformer phân biệt cùng vị trí pixel nhưng đến từ camera khác. Positional encoding 2D mô tả vị trí trên feature map, không tự thay thế calibration hình học. Camera serial/order phải giữ đúng giữa cache, train và inference. [[J:src/models/rh20t_act.py:34]]

**8 slot không có nghĩa mọi sample có đủ 8 ảnh thật.** Missing-camera mask B×8 biến thành mask cho 392 visual tokens, thêm 2 token state/latent không bị che, tổng B×394. Camera dropout chỉ train: che thêm một phần view thật nhưng giữ ít nhất một view; đây là augmentation, không phục hồi thông tin đã mất. [[J:src/models/mcr_act.py:100]] [[J:src/models/mcr_act.py:177]]

MCR xử lý resize cạnh ngắn 256 rồi center crop 224. Nó không đơn giản resize ảnh 640×360 thành 224×224 bằng bóp méo tỷ lệ. Crop có thể làm mất chi tiết chốt hoặc vùng ảnh ngoài rìa; lợi ích pretrained phải được đo trên task của mình. [[J:src/models/mcr_act.py:25]]

### 3.2. CVAE là gì, và latent z có phải “ý định” không?

Một quan sát có thể đi cùng nhiều tương lai hợp lý: tiếp cận hơi lệch trái/phải, đóng kẹp sớm/muộn. Nếu chỉ ép một hàm dự đoán trung bình, chuyển động có thể thiếu nhất quán. CVAE cho phép một biến ẩn **z** điều kiện hóa cách sinh cả chunk. Gọi z là “mã phong cách quỹ đạo” giúp trực giác, nhưng **không khẳng định từng chiều latent có ý nghĩa con người hiểu được**.

Trong source, CVAE encoder nhận **state hiện tại và chunk action nhãn**, không nhận ảnh vào nhánh encoder posterior này. Chuỗi có CLS + state + K action token: (B,22,512), đổi sang (22,B,512). Lấy output CLS, Linear512→64 rồi tách **mu và logvar**, mỗi tensor (B,32). Nhãn padding bị zero và attention-mask. [[J:src/models/mcr_act.py:113]]

\[
q_\phi(z\mid s_t,A_t)=\mathcal N(\mu_\phi,\operatorname{diag}(\sigma_\phi^2)),\quad
\sigma=\exp(\tfrac12\log\sigma^2),\quad
z=\mu+\sigma\odot\epsilon,\quad\epsilon\sim\mathcal N(0,I).
\]

Đó là **reparameterization trick**: randomness ở epsilon, vẫn truyền gradient qua mu/sigma. Trong source `logvar` nghĩa log variance, không phải standard deviation. z chiếu thành token 512D để kết hợp với ảnh/state trong mạng dự đoán. [[J:third_party/rh20t_act/models/detr/models/detr_vae.py:17]] [[J:src/models/mcr_act.py:123]]

### 3.3. Transformer và learned queries

Transformer encoder trộn token ảnh với proprio và latent. Decoder có K learned queries, mỗi query đại diện một slot tương lai. Decoder dự đoán cả chunk bằng một forward pass, không phải vòng tự hồi quy “dự đoán action1 rồi đưa action1 vào để dự đoán action2”. Action head chiếu hidden512 thành8. [[J:src/models/rh20t_act.py:97]] [[J:third_party/rh20t_act/models/detr/models/detr_vae.py:50]] [[J:third_party/rh20t_act/models/detr/models/transformer.py:43]]

Đừng lẫn **Transformer encoder của CVAE** với **Transformer encoder trong policy**. Chúng có nhiệm vụ khác nhau. Nhánh CVAE cần target để học latent; policy encoder dùng observation và latent để dự đoán target. Tại inference, chỉ bỏ nhánh posterior; backbone, policy encoder, decoder và action head vẫn chạy.

## 4. Loss, KL weight và normalization

Với mask m_bk=1 khi nhãn thật, D=8:

\[
L_{L1}=\frac{\sum_{b,k,d}m_{bk}|\hat a_{bkd}-a_{bkd}|}{8\sum_{b,k}m_{bk}},\qquad
L_{KL}=\frac1B\sum_b\frac12\sum_j(\mu_{bj}^2+\exp(\ell_{bj})-1-\ell_{bj}),
\]

\[
L=L_{L1}+\beta L_{KL},\qquad \beta=10 \text{ trong config nền.}
\]

✅ Source tính L1 chỉ trên valid entries rồi chia số phần tử thật, không chia cả phần padding. KL cộng theo 32 chiều latent rồi mean theo batch. Như vậy chunk gần cuối không có nhãn giả bị tính như thật. [[J:src/models/rh20t_act.py:54]] [[J:src/models/mcr_act.py:140]] [[J:configs/act/rh20t_all8.json:1]]

L1 được tính trên action **đã chuẩn hóa**, vì q và width có đơn vị/thang đo khác nhau. 0,1 normalized loss không phải 0,1 mm hay 0,1 rad. Để báo số vật lý, phải denormalize rồi tính MAE joint rad/độ và width mm riêng. Chuẩn hóa từng chiều theo mean/std **train**, có std floor 1e−4; val/test không tham gia fit. [[J:src/data/act_dataset.py:10]] [[J:src/data/act_dataset.py:119]]

KL giữ posterior không tùy ý rời prior N(0,I), để inference với latent prior có cơ sở hơn. Nếu beta quá thấp, model có thể dựa quá nhiều vào latent chỉ suy ra được khi thấy target. Nếu quá cao, posterior có thể gần prior đến mức decoder bỏ qua z: **posterior collapse** là một khả năng cần kiểm, không phải kết luận chỉ nhìn KL nhỏ. Cần so reconstruction/prior inference và ablation.

**Vì sao beta=10?** Config kế thừa lựa chọn của RH20T ACT baseline; chưa thấy sweep KL của nhóm. Nói “chọn baseline có sẵn rồi cần kiểm thực nghiệm”, không nói “10 là tối ưu cho nhà máy”. [Lệnh baseline của tác giả](https://github.com/rh20t/act_baseline#pretrain-on-rh20t), truy cập 17/10/2026.

Ví dụ số học minh họa, không phải loss đã đo: L1=0,08, KL=0,002 thì total=0,10. Cần xem cả ba thành phần; total giảm có thể do KL giảm trong khi độ chính xác action chưa tốt.

## 5. Train, validation và inference khác nhau ở đâu?

| Chế độ | Có target đưa vào model? | z | Update weights? | Ý nghĩa |
|---|---|---|---|---|
| Train | Có | Sample posterior từ state+nhãn chunk | Có | Tối ưu L1+KL |
| Validation qua `run_epoch` | Có | Vẫn posterior vì `actions` khác None | Không, eval/inference_mode | Đo reconstruction khách quan với split val, nhưng chưa giống deployment |
| Inference thật | Không | **0**, prior mean | Không | Quan sát → prediction mà không nhìn nhãn |
| Plot probe mới | Không khi dự đoán | 0 | Không | Đo vài đoạn val cố định, không đại diện toàn val |

`model.eval()` tắt dropout và thay mode BN; **không tự khiến CVAE dùng z=0 nếu vẫn truyền actions**. Điều kiện source là `actions is not None`. Đây là câu hỏi bẫy quan trọng nhất khi giải thích validation loss. [[J:src/training/pretrain.py:283]] [[J:src/models/mcr_act.py:113]] [[L:src/evaluation/mcr_epoch_plots.py:1]]

Inference z=0 không phải lấy posterior mu của mẫu test, vì lúc đó không có nhãn tương lai. z=0 cũng không bằng “output=0”, do state và ảnh vẫn điều kiện hóa prediction. Không có bằng chứng nhóm đã dùng sampling nhiều z để chọn quỹ đạo tốt nhất.

## 6. Temporal ensembling có dùng không?

Temporal ensembling trộn nhiều dự đoán cho **cùng thời điểm thực thi t**, được sinh từ các chunk bắt đầu ở các thời điểm khác nhau:

\[
a_t=\sum_{i\in\mathcal I_t}\bar w_i\hat a_{t\mid t_i},\quad
\bar w_i=\frac{e^{-\lambda i}}{\sum_j e^{-\lambda j}}.
\]

Trong code ACT gốc `eval_bc`, k=0,01 và thứ tự i lấy theo các hàng populated trong bộ nhớ prediction; không tự diễn giải i là “độ mới” rồi tuyên bố luôn ưu tiên prediction mới. Có thể xem trực tiếp [imitate_episodes.py, eval_bc](https://github.com/tonyzhaozh/act/blob/main/imitate_episodes.py#L225), truy cập 17/10/2026.

✅ ACT gốc có tùy chọn này. ✅ Report E5 của nhóm ghi first-action mỗi tick nên không phải temporal ensemble. ⬜ Joint policy mới **CHƯA XÁC MINH executor**. Không tìm thấy một executor ensemble đã được chứng minh chạy trong source simulation khảo sát. Nếu làm ensemble TCP thì quaternion không nên cộng tuyến tính rồi mặc định là rotation đúng; joint cũng cần xử lý wrap/limits và tín hiệu kẹp. Đây là yêu cầu thiết kế tiếp theo, chưa phải code đã thêm.

## 7. Bảng tham số: đã biết gì, ảnh hưởng khi đổi

“Nền” là giá trị đọc từ config/source, không thay cho metadata E25. Số runtime mới chưa đọc được phải giữ dấu hỏi.

| Tham số | Giá trị có căn cứ | Ý nghĩa / hệ quả khi đổi |
|---|---|---|
| state/action dim | 8/8, joint7+width | Đổi số khớp cần head/state projection, stats và dữ liệu mới |
| K / chunk_size | 20 | K dài tăng horizon/decoder slot, có thể khó học và phản ứng chậm nếu chạy open-loop |
| policy grid | 10 Hz | Δt=100 ms; đổi Hz làm đổi thời gian vật lý của chunk và semantics nhãn |
| raw RGB | 640×360, 8 slot | Chi phí render/camera; không phải spatial feature size |
| MCR input | 224×224 sau resize/crop | Đổi crop ảnh hưởng thông tin chốt và contract cache |
| MCR output | 2048×7×7/view | Spatial representation; không global-average thành một vector duy nhất |
| hidden dim | 512 nền | Sức chứa và chi phí attention/FFN tăng khi tăng d |
| policy enc/dec | 4/7 nền | Độ sâu encoder/decoder; không có ablation số layer |
| CVAE encoder | dùng enc_layers=4 nền | 22 token cho K20; không phải ảnh 8 view |
| nheads | 8 nền | Mỗi head có 512/8=64 chiều; hidden phải chia hết heads |
| FFN | 3200 nền | Chi phí MLP mỗi token |
| latent dim | 32 source | Mu/logvar mỗi cái32; không được gọi32 loại thao tác |
| KL weight | 10 nền | Điều chỉnh tradeoff reconstruction/prior regularization |
| ACT dropout | 0,1 cấu hình đã chọn | Regularization train, tắt eval |
| camera dropout | 0,1 đã chọn | Training-only additional masking, vẫn ≥1 view thật |
| lr ACT | 1e−5 mặc định trainer | Runtime E25 cần đọc checkpoint; tăng có thể học nhanh hoặc mất ổn định |
| lr backbone | 0 frozen; 1e−6 CLI full mặc định | Frozen cache chỉ đúng nếu backbone không đổi |
| optimizer | AdamW, weight_decay 1e−4 nền | Không phải RL optimizer; cần giữ state khi resume |
| batch | tên run mới có `bs256`; **thực tế CHƯA XÁC MINH từ runtime** | Batch16 là default CLI cũ, không phải giá trị chắc chắn của E25 |
| workers | **CHƯA XÁC MINH E25** | Số tiến trình đọc dữ liệu, không tăng chất lượng model trực tiếp |
| epochs | E25 theo bạn, target tổng E100 | Chưa xác nhận E100 đã chạy xong; epoch không phải task success |
| std floor | 1e−4 nền | Tránh chia std nhỏ; không giải quyết sai đơn vị |
| age cap | 150 ms nền | Causal sample-and-hold, stale camera mask, không nội suy ảnh tương lai |
| feature quantization | INT8 + scale FP16/view/channel | Dequantize gần đúng; tiết kiệm dung lượng, chưa ablation độ chính xác gắp |

Nguồn bảng: [[J:configs/act/rh20t_all8.json:1]] [[J:configs/data/cfg5_all8.json:1]] [[J:src/models/mcr_act.py:25]] [[R:server_train_mcr_current.py:41]] [[R:BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:93]] [[H::5810]]. Đường đúng để chốt runtime là `latest.pt` joint → `metadata.model_config`, `metadata.data_config`, `runtime`, `contract`, `history.json`; không lấy toàn bộ từ một README bất kỳ.

## 8. RH20T pretrain → task đích: tương thích tới đâu?

### Hai việc “pretrain” khác nhau

1. ✅ **MCR pretrained của tác giả**: encoder ảnh học từ DROID. Nhóm tải weights, kiểm SHA, freeze. Không phải nhóm tự pretrain MCR từ đầu. [MCR chính thức](https://robots-pretrain-robots.github.io/), [code tác giả](https://github.com/luccachiang/robots-pretrain-robots), truy cập 17/10/2026.
2. 🟡 **ACT pretrain joint của nhóm**: học trên CFG5 bằng encoder MCR cố định. E25 theo bạn; loss/rollout mới chưa có artifact local. ACT phần điều khiển khởi tạo mới khi đổi joint. [[H::5754]] [[J:docs/PREPROCESSING_MCR_JOINT_MASKED_CHI_TIET_VI.md:27]]

### Ma trận tương thích bắt buộc

| Trục | CFG5 joint/MCR hiện tại | Demo task đích trong importer | Đã xử lý hay còn thiếu? |
|---|---|---|---|
| State | 7 measured joint rad + measured width m | xyz m + quaternion wxyz + measured width m | **Không khớp**; cần ghi/đọc joint thật của demo và stats đúng joint |
| Action arm | Joint đo ở tick tương lai, absolute | TCP command cùng tick, absolute | **Không khớp semantics lẫn representation**; không nạp cùng shape8 rồi fine-tune |
| Gripper | Future recorded command width m | Same-tick controller width m | Offset1 so với offset0; phải chọn contract và kiểm target thời gian |
| Target offset | +1 tick =100 ms | 0 tick pre-step | Đã có config biểu diễn khác nhau ở nhánh cũ; joint migration chưa hoàn tất |
| Camera | 8 slot, có missing mask | 8 view mô phỏng đầy đủ theo metadata | Order khớp serial chưa chứng minh distribution ảnh và calibration đời thực khớp |
| Hz | Grid10 Hz | Controller/demo10 Hz | Tương thích grid, không chứng minh mọi timestamp raw hoàn hảo |
| Frame | Joint gắn robot; FK/TCP cần base/tool định nghĩa | TCP base/world theo scene, tool ảo | Chưa xác minh transform tool thực; bỏ FK không xóa sim-to-real gap |
| Labels | Không lọc rating ở nhánh mới | Chỉ nhận success=true | Có thể có quỹ đạo lỗi trong pretrain mới, cần phân tích chất lượng |
| Normalization | Train stats split1053/132/132 | TCP stats của nhánh E58 cũ được giữ | Không dùng stats TCP cho joint dù cùng8D |

Nguồn: [[J:src/data/cfg5_masked.py:205]], [[J:src/data/act_dataset.py:68]], [[J:src/data/sim_demos.py:68]], [[J:configs/data/pick_place_finetune8.json:24]], [[J:src/data/sim_demos.py:308]].

Để fine-tune joint có ý nghĩa: ghi q đo hiện tại và q command/reference đúng định nghĩa từ demo, kiểm joint order và units, chốt offset, split theo seed/trajectory, fit/inherit joint stats bằng một quy tắc ghi rõ, rồi so sánh **có/không pretrain trên cùng task, cùng số demo và cùng protocol**. Đây là ⬜ kế hoạch thí nghiệm; chưa có bằng chứng pretrain giúp giảm demo hay tăng success.

**Không dùng FK để biến một chuỗi TCP nhãn thành joint duy nhất.** IK có thể nhiều nghiệm với Panda7DOF; dùng IK tái tạo cần chọn nhánh nghiệm, kiểm continuity/limits và tracking. Tốt nhất ghi joint từ simulator trong lúc tạo demo. Cũng không nạp E58 TCP vào joint chỉ vì kích thước head khớp; các chiều đã đổi nghĩa.

## 9. “Overfit test” hiện có nghĩa gì?

Overfit sanity check đúng nghĩa thường chọn một hoặc vài episode, học thật kỹ chúng, rồi kiểm **prior inference z=0** và closed-loop trên chính điều kiện đó. Nó trả lời “pipeline có học/bắt chước được mẫu không”, chưa trả lời “có tổng quát hóa không”. Một forward/backward smoke chỉ kiểm luồng tính toán, chưa phải overfit đạt.

| Bằng chứng thực tế | Con số | Kết luận |
|---|---|---|
| TCP training lịch sử | 531 train episode, 58.313 sample; 66 val, 6.214 sample ở run lưu | Không phải một/few-episode overfit experiment |
| TCP best E58 | train loss0,0549384, val loss0,19734495; lịch sử78 epoch | Train thấp hơn val; chưa suy ra task success hoặc prior error từ posterior loss |
| E5 TCP transfer | 10 val episode, 4.962 observation; prior L1≈0,3682195, vị trí≈66,65 mm, góc≈24,04°, kẹp≈29,17 mm; rollout0/10 | Thử transfer cũ thất bại trên phạm vi đó; không phải kết quả MCR/joint mới |
| MCR/joint E25 mới | Bạn báo E25; **loss, số sample/epoch và success chưa xác minh** | Không dùng loss TCP để điền vào chỗ trống joint |
| Đồ thị val mới | Code probe cố định có triển khai | Chưa có log `MCR_EPOCH_PLOTS_OK` để xác nhận output run đã sinh |

Nguồn: [[R:checkpoints/before_test_20261007_142338/history.json:1]], [[R:epoch5_transfer_probe_14120/report.json:1]], [[H::5754]], [[L:src/evaluation/mcr_epoch_plots.py:1]]. Các observation và action window overlap, nên 4.962 observation không phải 4.962 thí nghiệm robot độc lập.

Sửa S42 thành: “Nhóm đã xây dựng pipeline, thực hiện train/validation và kiểm tra inference ở các nhánh đã ghi nhận. Kết quả transfer ban đầu còn hạn chế; nhánh joint/MCR mới đang được huấn luyện và cần đánh giá closed-loop. Chưa kết luận tổng quát hóa.”

## 10. Nói với giám khảo bằng 30 giây

> ACT là mô hình học bắt chước dự đoán một đoạn hành động tương lai từ ảnh và trạng thái robot. Trong nhánh mới của nhóm, MCR ResNet50 trích đặc trưng các camera, ACT kết hợp với bảy góc khớp và độ mở kẹp để dự đoán chunk 20 bước. Khi train, CVAE dùng nhãn tương lai để học latent và loss gồm L1 cộng KL. Khi chạy, nhóm đặt latent bằng không và chỉ dùng quan sát. Hiện nhóm có pipeline dữ liệu và đang huấn luyện nhánh joint; thành công gắp–đặt bằng nhánh này còn cần đo.

Thời lượng thực phụ thuộc tốc độ nói. Nếu quá 30 giây, bỏ câu mô tả loss, giữ input/output, chunk và giới hạn kết quả. Căn cứ: source model/loader và chat mới nêu trên.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Vẽ hai encoder khác nhau trong ACT và nói encoder nào cần target.
2. Vì sao eval mode vẫn có thể dùng posterior z, còn inference phải z=0?
3. Tính K20 ở10Hz ra thời gian và giải thích tại sao chưa suy ra model query frequency.
4. Viết L1 có padding mask, KL Gaussian và giải thích beta10 có căn cứ gì.
5. Vì sao không fine-tune thẳng demo TCP8D vào model joint8D?
''')
print('Created 02')
