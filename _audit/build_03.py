from doc_helpers import write
write('03_IO_AND_CODE.md',r'''
# 03 — Input/output từng khối, đơn vị và tần số

Đọc bảng này theo **hai luồng**: nhánh học hiện tại là joint/MCR; demo mô phỏng và controller đã kiểm có API TCP. Chưa có bằng chứng hai API đã nối đúng. Dấu `?` là **CHƯA XÁC MINH**, không phải giá trị mặc định. Các shape là theo source trừ ví dụ số thực ở mục 5.

## 1. Hợp đồng của nhánh joint/MCR

V=8, K=20, Ds=Da=8, latent32. Một observation không có batch: thêm B ở đầu khi DataLoader xếp batch. 10Hz là lưới dữ liệu/policy chọn trong dự án, không đồng nhất với Hz motor robot thật. [[J:configs/data/cfg5_all8.json:6]] [[J:src/data/cfg5_masked.py:267]]

| Thành phần và trạng thái | Input: tên, kiểu, shape, đơn vị, Hz | Xử lý | Output và ai tiêu thụ | File/hàm |
|---|---|---|---|---|
| Camera/rig CFG5 ✅ | `color.mp4`, timestamps mỗi serial; ảnh 640×360×3; time ms. RGB raw có tần số công bố10Hz nhưng timestamp từng stream vẫn phải kiểm | Chọn frame gần nhất **không sau tick**, tuổi≤150ms nền; thiếu/stale thì mask | RGB8slot `(8,360,640,3)` uint8, `camera_valid(8)` bool; cache builder dùng ở10Hz grid | [[J:src/data/cfg5_masked.py:253]], `past_indices` ở [[J:src/data/cfg5.py:46]] |
| Joint/kẹp raw ✅ | `joint.npy[serial][timestamp]` vector14 ở mẫu đã đọc; lấy7 đầu rad. `gripper_info[0]`, `gripper_command[0]` mm; raw frequency theo timestamps | Chọn stream thật ưu tiên037522062165, lấy past state, đổi width×0,001 | `state(T,8)` float32 `[q1…q7,g_measured]`, `action(T,8)` `[q1…q7,g_command]`, width m; light builder | [[J:src/data/cfg5_masked.py:205]] |
| Light preprocessing ✅ log server | Raw state/camera/time, metadata | Split group task/user/calib, seed42; tạo segment khi gap, bỏ đúng4 episode thiếu joint được duyệt | `timestamps_ms(T)` int64, `segment_ids(T)` int32, `frame_indices(T,8)` int64, `camera_valid(T,8)` bool, numeric; normalization train | [[J:scripts/prepare_cfg5_masked_mcr.py:19]] [[H::4276]] |
| MCR image preprocessing ✅ | RGB `(N,3,H,W)` uint8; N là số view thật qua batch; không có đơn vị vật lý | `/255`, resize cạnh ngắn256, center crop224, ImageNet mean/std | float32 `(N,3,224,224)` dimensionless → shared ResNet50 | [[J:src/models/mcr_act.py:25]] |
| MCR feature extractor ✅ synthetic/log cache | RGB batch `(B,8,3,H,W)` + `camera_valid(B,8)` | Backbone pretrained freeze weights+BN; chỉ chạy view thật, điền0 view thiếu | float feature `(B,8,2048,7,7)` → cache hoặc policy | [[J:src/models/mcr_act.py:73]]; [[J:outputs/mcr_checks/mcr_real_local_check.json:1]] |
| Feature recorder/cache ✅ log server | Feature float, light numeric/masks, backbone/transform contract | INT8 per-view/channel với scaleFP16; SHA/episode metadata; frozen stage không lưu JPEG | `features(T,8,2048,7,7)` int8, `scales(T,8,2048,1,1)` float16; state/action/time/mask; FeatureACTDataset dùng | [[J:src/data/feature_cache.py:133]] [[J:src/data/staged_mcr.py:1]] |
| Dataset/DataLoader ✅ source | Cache+split1053/132/132+train stats. Frozen stage không đọc MP4 | state/action normalize, lấy future offset1, chunk không vượt segment; dequantize feature | `images(B,8,2048,7,7)` float32 (**tên images nhưng chứa feature**), `state(B,8)` float32, `actions(B,20,8)` float32, `is_pad(B,20)` bool, `camera_valid(B,8)` bool, episode/time → trainer | [[J:src/data/act_dataset.py:109]] [[J:src/data/feature_cache.py:393]] |
| ACT train 🟡 run E25 theo bạn | State/features/actions/is_pad/camera_valid như trên; SGD updates/s chưa đo | Posterior encoder tạo z32; visual projection512, policy encoder/decoder, L1+10KL | dict `loss,l1,kl` scalar; `prediction(B,20,8)` normalized; valid counts → optimizer/history/checkpoint | [[J:src/models/mcr_act.py:94]] [[R:server_train_mcr_current.py:155]] [[H::5754]] |
| ACT inference ✅ code, ⬜ latest robot rollout | RGB+joint state đúng stats hoặc feature đúngcontract; **không target/is_pad**; tần số thực chưa đo | eval/inference_mode, z=0, model forward | normalized `(B,20,8)` → denormalize bằng **joint stats**; output absolute joint rad+widthm | [[J:src/models/mcr_act.py:125]] |
| Action→joint tracking ⬜ nối mới | Denormalized `(20,8)`; joint order/limits/timestamps | Cần executor chọn action/chunk, giới hạn position/speed/accel/jerk, nội suy đúng controller | Joint reference + width → simulator/robot driver | **CHƯA XÁC MINH implementation đã chạy**; controller hiện có ở bảng2 vẫn TCP |
| Đánh giá joint policy ⬜ result | Rollout observation thật và simulator privileged state chỉ cho scorer | Evaluator grasp/lift/place; nhiều episode độc lập, metric và timeout | success N/N, cycle time, failure type, joint/width error → báo cáo | Evaluator có ở [[J:src/simulation/panda_evaluator.py:65]], chưa thấy report rollout joint mới |

Scale shape lấy từ `features.abs().amax((-2,-1), keepdim=True)` và `FEATURE_SHAPE=(8,2048,7,7)` trong source cache. Đây là per-channel scale giữ hai chiều không gian=1, không phải một hệ số chung cho toàn ảnh. [[J:src/data/feature_cache.py:133]] [[J:src/models/mcr_act.py:152]]

## 2. Luồng demo/controller đã có, hiện vẫn TCP

| Thành phần và trạng thái | Input | Xử lý | Output / người dùng tiếp | File/hàm |
|---|---|---|---|---|
| MuJoCo + Panda ✅ | Scene XML+config, state vật lý q/qvel;7 arm joint+2 finger joint vật lý | Physics dt0,001s =1kHz; actuator+contact; render8camera khi cần | `obs.images(8,360,640,3)` uint8; `obs.state(8)` **TCP xyz,wxyz,width**, `timestamp_s` float; info chứa metric/privileged states | [[J:src/simulation/panda_env.py:12]] [[J:src/simulation/panda_env.py:113]] |
| Controller sinh demo ✅ | `env.object_states()`3object, TCP7, width, config; policy tick10Hz | Script chọn pha approach/descend/grasp/lift/transfer/insert/release; đọc offset vật privileged | Action TCP `(8)` tuyệt đối m+quaternion+widthm → PandaEnv.step | [[J:src/simulation/panda_demo.py:1]] |
| Bộ ghi demo hàng loạt 🟡 | Quan sát+command chung pre-step tick, metadata/profile/success | Importer chứng minh schema nguồn, nhưng generator cho toàn tập chưa truy nguyên đầy đủ | Theo schema:8MP4+timestamps, `robot_trajectory.npz`, `metadata.json`, `scene_config.json` → sim importer | [[J:src/data/sim_demos.py:68]]; **CHƯA XÁC MINH source recorder đã tạo hết913/1000** |
| Bộ ghi demo đơn ✅ | Callback ảnh+info sau step, trace | MP4 preview/result/trace; không mặc định là export8video training | `controller_demo.mp4`, result.json/trace.json → xem kỹ thuật | [[J:scripts/run_pick_place_demo.py:1]] |
| Sim Dataset cũ ✅ | NPZ state/command TCP `(T,8)` và8MP4 đồngtick10Hz | Chỉ success=true, split seed/trajectory trước chunks, target offset0 | RGB float normalized + TCPstate8 + command chunk20×8 → fine-tune TCP cũ | [[J:src/data/sim_demos.py:68]] [[J:configs/data/pick_place_finetune8.json:24]] |
| Action→TCP controller ✅ | Action8 xyz+wxyz+width,10Hz target | Validate finite/workspace/quaternion/width; giới hạn translation2,5cm/step; DLS IK; substep rate-limitjoint | `target_q(7)`rad; actuator1…7 position references; gripper ctrl=width/0,08×255 | [[J:src/simulation/panda_controller.py:16]] [[J:src/simulation/panda_controller.py:64]] |
| Bộ kiểm tra đặt đúng ✅ | 3object positions/axes/speeds, contacts(3,2), robot_touching(3), supportforce(3)N, TCP,width,dt | Chấm geometry+history+release/support/stability; chạy100Hz trong1kHzphysics | metrics perobject/task; reward=#placed/3, terminated/truncated → env/client/report | [[J:src/simulation/panda_env.py:108]] [[J:src/simulation/panda_evaluator.py:65]] |

**Input policy không được chứa privileged object_states.** Oracle dùng object state để tạo nhãn là hợp lệ cho data generation, nhưng lấy chính thông tin đó khi báo “ACT chỉ nhìn ảnh” sẽ làm sai thí nghiệm. `PandaEnv.info()` có privileged state nên cần kiểm caller sử dụng thế nào. [[J:src/simulation/panda_env.py:126]]

## 3. Sơ đồ kèm shape

```mermaid
flowchart LR
  C["RGB uint8\n8 x 360 x 640 x 3"] --> R["MCR preproc+ResNet50\n8 x 2048 x 7 x 7"]
  R --> Q["INT8 cache + FP16 scale\ntrain: đọc lại float32"]
  Q --> F["Feature batch\nB x 8 x 2048 x 7 x 7"]
  S["q1..q7 rad + g_measured m\nB x 8, normalize"] --> P["ACT\ntrain posterior z32\ninfer z=0"]
  F --> P
  MV["camera_valid\nB x 8 bool"] --> P
  A["train only\nactions B x 20 x 8\nis_pad B x 20"] --> P
  P --> O["prediction B x 20 x 8\nnormalized"]
  O --> DN["joint stats inverse\nrad + width m"]
  DN -. "cần nối mới" .-> E["joint chunk executor\nq_ref7 + width"]
  E -.-> SIM["Panda physics\ndt1ms"]
  SIM -. "cần joint observation adapter" .-> S
```

Trong inference thật, cache feature **của observation trước** không được tái dùng thay observation mới. Chỉ reuse backbone weights/transform; mỗi ảnh mới phải tính feature mới, trừ khi có cơ chế cache đúng timestamp. Frozen cache là tối ưu training trên dữ liệu đã ghi, không làm robot miễn phí inference ngoài đời.

## 4. Action là gì? Năm câu phải trả lời chính xác

1. **Nhánh hiện tại: góc khớp, absolute.** Các phần tử đầu là q1…q7 ghi thật, không có phép trừ q_t trong `timeline`, nên target không phải Δq hay torque. [[J:src/data/cfg5_masked.py:227]]
2. **Gripper là width liên tục, đơn vị mét.** Có command thường ở hai mức trong demo, nhưng representation không phải Boolean open/close. Số0,04 là40mm, không phải4% lực. [[J:src/data/cfg5_masked.py:225]] [[J:configs/mujoco/panda_three_pegs.json:1]]
3. **Arm labels CFG5 là future measured-state proxy.** Đã đo tư thế robot tương lai ≠ motor/controller command được ghi; plant có trễ nên cần adapter tracking và thời gian. Gripper lấy command riêng. [[J:scripts/prepare_cfg5_masked_mcr.py:134]]
4. **IK hiện có ở TCP controller.** Nếu joint policy xuất q_ref đúng robot và driver nhận joint, đường đó không cần IK từ pose. FK vẫn dùng để kiểm TCP/workspace, không biến joint thành “tọa độ x,y,z”. [[J:src/simulation/panda_controller.py:42]]
5. **10Hz model/data ≠1kHz physics/control.** Env gọi target mỗi0,1s, rồi100substep; mỗisubstep cập nhật rate-limit reference và physics. Evaluator100Hz. Đây là lịch mô phỏng, chưa xác minh servo rate/latency robot ở xưởng. [[J:src/simulation/panda_env.py:23]] [[J:src/simulation/panda_controller.py:74]]

## 5. Ví dụ thật đã đọc nhẹ

### 5.1. Một record joint CFG5 thật, nhánh mới

Nguồn: `F:/cfg5_mophong/local_source_(1)/RH20T_cfg5/training_data/task_0001/task_0001_user_0007_scene_0001_cfg_0005/transformed/joint.npy` cùng `gripper.npy`. Script chỉ đọc một record, không preprocess toàn bộ. Kết quả có thể tra lại tại [[A:measured_facts.json:1]].

```text
serial = 036422060215
timestamp_ms = 1640002326912
raw_joint_shape = (14,)       # không phải robot 14 khớp
q_rad = [0.03644249, 0.35039160, 0.00037409,
         -1.74086845, 0.01593763, 1.79177034, 0.83809847]
gripper_measured_mm = 0.01
gripper_command_mm = 0.0
state8 = [q_rad..., 0.00001]  # width m sau đổi đơn vị
```

Đây là record ở serial đầu tiên script tìm thấy để minh họa schema, **không tuyên bố đó là stream được `timeline()` chọn cho episode**; code ưu tiên037522062165 nếu hợp lệ. Chỉ 7 phần tử đầu được dùng. Không lấy số width rất nhỏ này làm bằng chứng robot đo chính xác10µm hoặc đạt dung sai10µm.

Chưa có feature cache joint mới trên local để in nguyên một `FeatureACTDataset[0]` của run E25. Shape của batch mới trong mục1 được truy từ source và synthetic check, không giả danh tensor đã đọc từ cache server.

### 5.2. Một sample processed thật của nhánh TCP cũ

Nguồn: [[L:outputs/data_audit/local_preprocess_smoke/pick_place_000042/episode.json:1]]. Memmap chỉ đọc header và hàng đầu:

```text
images: (4,8,360,640,3) uint8
state : (4,8) float32
action: (4,8) float32
timestamps_ms: (4,) int64, first=0
segment_ids: (4,) int32, first=0

state[0]  ≈ [0.433633, 0, 0.438879, 0, 1, -1.746e-8, 0, 0.080000]
action[0] ≈ [0.431710,-0.001977,0.431540,0,1,0,0,0.040000]
```

Trong **ví dụ cũ này**, 3 số đầu là vị trí TCP mét,4 số tiếp là quaternionwxyz, cuối widthm; state là đo được, action là command. Tệp chỉ4ticksmoke, không phải4demo và không là cache MCR. Đây là minh họa thật cho lý do cùng8D nhưng không thể hoán đổi với ví dụ joint phía trên. [[A:measured_facts.json:1]]

## 6. Đồng bộ, chuẩn hóa và các mask

| Vấn đề | Quy tắc đã thấy trong source | Ý nghĩa |
|---|---|---|
| Causal alignment | timestamp nguồn≤tick, không lấy frame tương lai | Tránh observation nhìn thấy tương lai so với nhãn |
| Stale view | Quá150ms theo config nền → maskfalse | 10Hz data có thể thiếu frame, không giả timestamp hoàn hảo |
| Stale state | Tick không có state đủ mới bị loại | Không bịa joint0 |
| Gap | Tách segment, chunk không bắc cầu gap | Không học bước nhảy không tồn tại |
| `camera_valid` | True=ảnh thật hợp lệ | Dùng attention, shapeB×8 |
| `is_pad` | True=nhãn không tồn tại | Dùng CVAE attention/loss, shapeB×20 |
| Stats | Fit train split, không fit val/test | Tránh data leakage |
| Action inverse | `a_phys = a_norm * std_action + mean_action` | Stats phải đúng representation/checkpoint |

Nguồn: [[J:src/data/cfg5_masked.py:267]] [[J:src/data/act_dataset.py:10]] [[J:src/data/act_dataset.py:109]]. 150ms là tolerance stale, **không phải latency inference đã đo**.

## 7. Chỗ code cần hoàn thiện, chưa sửa trong lượt này

⬜ Adapter observation joint: đọc đúng7joint+measuredwidth từ MuJoCo thay stateTCP. ⬜ Ghi nhãn joint demo và chuẩn hóa đúng. ⬜ Executor gửi joint reference thay `env.step()` TCP cũ. ⬜ Kiểm joint order, giới hạn, timing, tracking, pause/timeout. ⬜ Report learned rollout joint và video có checkpointID. Cùng shape8 là lý do các lỗi semantics có thể qua được kiểm shape, cần kiểm giá trị/đơn vị và một chuyển động biết trước.

Các việc này là đề xuất dựa trên chỗ lệch source hiện có, **không phải thay đổi đã thực hiện**. Thư mục source vẫn được giữ nguyên.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Nói tên và shape tất cả tensor của một batch frozenMCR.
2. `images` trong batch mới thực ra chứa gì, khác ảnhRGB ở đâu?
3. Đổi0,01mm sang mét, rồi nói vì sao không phải độ chính xác đã đo.
4. Phân biệt camera_valid với is_pad và target offset1 với offset0.
5. Model xuấtjoint8D mà gọi `PandaEnv.step()` hiện có thì lỗi về ý nghĩa ở đâu?
''')
print('Created 03')
