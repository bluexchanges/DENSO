from doc_helpers import write
write('06_GAPS_AND_RISKS.md',r'''
# 06 — Mâu thuẫn, khoảng trống và rủi ro bị hỏi

Đánh giá ngày 17/10/2026, ưu tiên ghi chép mới nhất. Mức **Cao / Trung bình / Thấp** dưới đây là nhận định của mentor về khả năng bị hỏi và hậu quả nếu trả lời sai, không phải xác suất thống kê. “Chưa có bằng chứng” được giới hạn trong source/log/chat đã kiểm, không kết luận một việc chưa từng xảy ra ở mọi nơi.

## 1. Bảng rà soát nghiêm khắc

| ID / vấn đề | Kết luận và bằng chứng | Khả năng hỏi / hậu quả trả lời sai | Sửa slide hoặc câu trả lời trung thực |
|---|---|---|---|
| G01 — Pose tay trên S16/18 so với joint mới | **Xác nhận lệch phiên bản.** Bạn chốt joint ngày11/10; source dùng7joint+width. [[H::3568]] [[J:src/data/cfg5_masked.py:227]] | Cao / Cao | Sửa output thành “chuỗi góc khớp + độ mở kẹp”; chú thích nhánhTCP là thử nghiệm trước. |
| G02 — Joint policy nối vào API TCP | **Khoảng trống hiện tại.** `observation()` trảTCP8D; `validate_action()` nhậnxyz+wxyz+width. Chưa thấy joint bridge đã chạy. [[J:src/simulation/panda_env.py:113]] [[J:src/simulation/panda_controller.py:16]] | Cao / Cao | “Model và simulator cùng8D nhưng khác semantics; nhóm đang hoàn thiện adapter joint trước rollout.” Không chạy trực tiếp nhãnjoint qua API TCP. |
| G03 — Demo đích còn TCP, nhánh mới joint | **Chưa tương thích.** `sim_demos.load_trajectory` đọcmeasured/commandedTCP; nhãn joint lấy7góc đo tương lai. [[J:src/data/sim_demos.py:89]] [[J:src/data/cfg5_masked.py:237]] | Cao / Cao | Ghi/đọc joint thật trong demo, chốt offset/units/stats, rồi mới fine-tune. Không nói “chỉ đổi checkpoint”. |
| G04 — “1.000 demonstration mô phỏng đạt” S17 | **Chưa được chứng minh; manifest hiện không khớp.** 913accepted,111rejected:24failure và87video lỗi/thiếu frame. [[J:data/splits/pick_place_finetune_manifest.json:1]] | Cao / Cao | Ghi “manifest hiện có913episode dùng được, đang chuẩn hóa chất lượng”, kèm điều kiện. Không gọi913/1024 là success rate controller. |
| G05 — Nhóm đã chứng minh học tổng quát S42 | **Vượt bằng chứng.** TCP có train/val; E5transfer0/10. Joint mới có lời báoE25, chưa loss/rollout. [[R:checkpoints/before_test_20261007_142338/history.json:1]] [[R:epoch5_transfer_probe_14120/report.json:1]] [[H::5754]] | Cao / Cao | “Đã có pipeline và kiểm tra học/inference; còn phải đo generalization và closed-loop của nhánh mới.” |
| G06 — Overfit-test một vài mẫu? | **Chưa thấy một thí nghiệm overfit nhỏ đạt đủ điều kiện.** TCP run lưu có531train/66val, không phải1episode. Validation cótargetposterior. [[J:src/training/pretrain.py:283]] | Cao / Cao | Không tự bịa sốmẫu/loss overfit. Tách smoke, posterior reconstruction, prior prediction và rollout. |
| G07 — 100% thành công từ demo? | **Controller3/3 có thật, ACT cũ0/10 có thật, nhánh mới chưa có N/N.** [[L:outputs/controller_evaluation/summary.json:1]] [[R:epoch5_transfer_probe_14120/report.json:1]] | Cao / Cao | Mỗi video ghi rõcontroller/ACT, checkpoint, seed, điều kiện vàN. Không mượn3/3 làm success của policy. |
| G08 — 20tháng /16–18tháng /15task | **Ba số không cùng mô hình, hai số tháng còn khác giả định.** S2:1000/(3×15)=22,22tháng; S38 gầncase18–20triệu/người. S32làengineeringhours. | Cao / Cao | Giữ một bảng giả định rõ. “15task là hòa vốn công triển khai; payback robot là mô hình tiền riêng, hiện chưa xác nhận.” |
| G09 — Lương15 /18–20triệu /250k/h | **Chưa đủ để gọi mâu thuẫn bản chất nếu khác role/costbasis**, nhưng slide chưa giải thích. S21nói côngkỹsư, S2/36nói côngnhân. | Cao / Cao | Định nghĩa engineeringrate, basewage, fullyloadedlabor riêng và trích nguồn. Nếu cùng role thì phải thống nhất số. |
| G10 — 7DOF và6trục | **Panda mô phỏng7khớp xác minh.** Kinh nghiệm6trục S2 không tự mâu thuẫn vớiPanda nhưng gây hiểu nhầm; robotxưởng chưa biết. [[J:src/simulation/panda_controller.py:34]] | Cao / Cao | “Mô phỏng hiệnPanda7DOF; thiết bị thật sẽ chốt model với xưởng.” Trình bày kế hoạch cho cả6và7trục ở mục3. |
| G11 — Isaac Lab S28 | **Repo thực dùngMuJoCo; chưa tìm implementationIsaacLab** trong nhánh khảo sát. [[J:src/simulation/panda_env.py:1]] [[J:requirements-sim-lock.txt:1]] | Cao / Trung bình | Sửa “MuJoCo, pipeline dữ liệu/training và chuẩn bịsim-to-real”. NếuIsaac chỉ tham khảo thì ghi rõ. |
| G12 — 24/7, độ chính xác cao, lỗi thủ công2–5% | **Chưa có uptime, takt, reject baseline hay precision của policy mới.** S35là kỳ vọng. | Cao / Cao | Thay bằng mục tiêu đo; không dùngspec repeatability robot làmaccuracy hệthống. |
| G13 — Linh kiện dễ vỡ và force | **Policy chỉjoint/width, không forcehead.** Giới hạn20N trongconfig không chứng minh kẹp an toàn trên vật thật. [[J:src/models/mcr_act.py:137]] [[J:configs/mujoco/panda_three_pegs.json:1]] | Cao / Cao | “Chưa chứng minh với vật dễvỡ; cần đo force/contact, thiết kếgripper và thử nghiệm chất lượng.” |
| G14 — Few-shot/đa tác vụ | **Mới là mục tiêu về khả năng.** Có pretraindata nhiều task nhưng chưa task-success benchmark hay N-demo curve/ablation. S19dùng “hướng tới”. | Cao / Cao | Không nói model đã few-shot. Đề xuấtN=5/10/25/50làprotocol, không kết quả. |
| G15 — Pretrain chắc giúp fine-tune | **Chưa có so sánh có/khôngpretrain** trên cùng task, seed, sốdemo. MCRpaper không kiểm cấu hình nhóm. [[J:src/models/mcr_act.py:44]] | Cao / Cao | “Nhóm chọn pretrain có cơ sở nghiên cứu, lợi ích trên task nhóm còn phải đo.” |
| G16 — Held-out và OOD | **Có split theo group/seed; không tự chứng minh unseen-position/OOD.** [[J:src/data/splits.py:77]] [[J:src/data/sim_demos.py:230]] | Cao / Cao | Nêu split chính xác và thêm tập evaluation vịtrí/ánh sáng/vật chưa thấy; test chỉ dùng sau khóa cấu hình. |
| G17 — Giữ mọi rating trong CFG5 mới | **Có thật.** Script bỏmin_rating, không dùnghuman; 4missingjoint là ngoại lệ riêng. [[J:scripts/prepare_cfg5_masked_mcr.py:35]] | Trung bình / Cao | Nhận rủi ro học quỹ đạo lỗi. Cần phân tích theoquality/task và ablation lọc; không gọi mọi1317episode là expert thành công. |
| G18 — Camera thiếu và8camera ngoài đời | **Mask được cài và synthetic check đạt; robustness chưa chứng minh.** Logcamera có nhiều episode/tick thiếuview. [[J:src/models/mcr_act.py:100]] [[H::5394]] | Cao / Cao | “8slot là schema, không phải8view thật ởmọitick; cần ablation sốview và đo rig ngoài đời.” |
| G19 — MCR INT8/crop ảnh với chốt nhỏ | **Có quantization vàcenter224crop**, cachelogmaxfeatureerror≈0,05795; chưa liên hệ task error. [[J:src/models/mcr_act.py:25]] [[J:src/data/feature_cache.py:133]] | Trung bình / Trung bình | ĐoFP32feature vsINT8 và crop/resize; đừng chuyểnfeatureerror thànhmm/degree. |
| G20 — 3–6tháng vsT1–T8 | **Không xác nhận là mâu thuẫn chắc chắn.** HìnhS40coreT1–T5, mởrộngT6–T8, công việc song song. | Trung bình / Trung bình | Chú thíchcore≈5tháng và phần mởrộng, mốc nghiệmthu; không cộngdurationcácdòng hoặc chỉđếm8cột. |
| G21 — Vốn1tỷ vàbảotrìthấp | **ChưaBOM/báogiá/OPEX.** S2/36/38không ghi cấuphầnđầu tư. | Cao / Cao | Dùngkịchbảnminhhọa, táchCAPEX/OPEX/engineering và giátrịtáidùngrobotcósẵn. |
| G22 — Thay3côngnhân | **Chưa capacitystudy.** Không biết3ngườisongsong hay3ca;không biếtcycletime,yield,loading. | Cao / Cao | “Tiềm năng giảm thao tác thủ công, mức thaythế chỉ tính sau pilot.” Nếuđiềuchuyểnngườithìkhôngmặcđịnhlàcashsaving. |
| G23 — Thời gian30phút/lịch16–17/11 | **30phút do bạn xác nhận; webmới17/11 khácbàikhởiđộng16/11.** [BTC](https://densohackathon.vn/challenges) | Trung bình / Cao | Chốt lịch bằng thôngbáođội. 15phútdemo video trênweb làgiớihạnkhác với30phútpitch. |
| G24 — License dữ liệu | **Chưaaudit quyềnthươngmại.** RH20TphânbiệtC/NC; jointpretrain mới có mởrộngscene. [RH20T](https://rh20t.github.io/) | Trung bình / Cao | Đối chiếu scene/license/weights trướcpilot thươngmại, khôngnói“public=freecommercial”. |
| G25 — ResumeE100/đồ thị đã xong? | **Chưa.** UserbáoE25; cuối chatjob14598cònPending, sauđóyêucầuhủy. [[A:latest_thread_snapshot.json:1]] | Trung bình / Cao | “Đãchuẩnbị/cài patchtheolog, chưa cólogxácnhậnE100 hayplotmỗi epoch.” Khôngđổi“lệnhđưa ra”thành“jobđãchạy”. |
| G26 — Tự độngđếm/MES/truyxuấtS36 | **Cómetricmôphỏng, chưa chứng minhPLC/MES production integration.** [[J:src/simulation/panda_evaluator.py:65]] | Cao / Cao | Táchsimulate logging khỏi kiểmtraquality/phầnmềmnhàmáy, bổsung handshake và rejectpath. |

## 2. Ba mô hình kinh tế cần tách riêng

### A. Engineering effort khi triển khai nhiều task

Theo slide31: H_trad=16n, H_AI=120+8n. Hòa vốn tại15task,240h/cách. Các hệ số là **giả định**, không có time-study. Công thức tổngquát n*=H_setup/(h_trad−h_AI), chỉ có điểm hòa vốn dương khi h_trad>h_AI và platform thật sự tái sử dụng được.

### B. Payback đầu tư cell robot

`Payback_months = CAPEX / net_benefit_per_month`.

Trong đó netbenefit cần tính **lợi ích lao động thực sự tránh được + tăng thông lượng/giảm phế phẩm quy thành tiền − điện/compute/bảo trì/giám sát/downtime**. Không được cộng hai lần lợi ích của cùng một cải tiến. Nếu chỉ chuyển người sangviệc khác thì cần báo lợiíchcapacity/costavoidance cụthể, không ghi giảmchi lương mặc định.

| Giả định minh họa | Tiết kiệm gộp | Payback đơn giản với1tỷ |
|---|---:|---:|
|3người×15triệu/tháng|45triệu/tháng|22,22tháng|
|3người×18triệu/tháng|54triệu/tháng|18,52tháng|
|3người×20triệu/tháng|60triệu/tháng|16,67tháng|

Chưa OPEX trong mọi dòng; lợi íchròng nhỏ hơn gộp sẽ kéo dài payback, nếugiữcácgiảđịnhkhác. Nếu netbenefit≤0 thì chưa có payback hữu hạn theo môhình này. Đây là tính số minh họa từ slide, không tưvấnđầu tư hoặc dựbáo chắcchắn.

### C. Công lập trình tiết kiệm không phải lương công nhân tiết kiệm

250k/h×160h=40triệu làengineeringcostquyđổi. Không lấy mức này làm lươngngười vận hành15triệu. Muốn nói18–20triệu làfullyloadedcost cần cónguồn xácnhận, thay vì tựsuy bảo hiểm/overhead để vá mâu thuẫn.

**Câu trả lời nên dùng:** “Nhóm tách mô hình tiết kiệm công kỹsư với mô hình đầu tư thay thao tácthủcông. Điểm15task thuộc môhìnhthứnhất; phần thángpayback còn làgiảđịnh cần chốt lại lương,OPEX và thônglượngvớixưởng.”

## 3. Triển khai thật: cả6trục,7trục vàPanda đang mô phỏng

Loại robot xưởng hiện **CHƯA XÁC MINH** theo trả lời của bạn17/10. Không đặt tênrobot hoặc giao diện chỉ dựa vào sốtrục.

| Tình huống | Có thể tái dùng | Cần thay/kiểm | Không được hứa |
|---|---|---|---|
| **A. Robot6trục ởxưởng, khácPanda** | Pipeline đọcảnh, tưduy chunk/CVAE, split/evaluator design, cóthể thửvisualweights | ModelURDF/MJCF, jointorder/limits, state/actiondim thường6+gripper=7nếu chọnjoint,head/projection/stats,data/action semantics mới,driverAPI/calibration/cellvalidation | “Bỏjointthứ7rồi chạy”; “giữhead8Dnhưcũlàđược”;sim-to-realtrực tiếpjointPanda |
| **B. Robot7trục khácPanda** | Cóthểgiữkíchthướcstate/head8Dnhưkhung | 7DOFkhôngđồngnghĩa cùnglinklength,zerooffset,sign/limits,gripper,toolframe,dynamics vàappearance; cầnretarget/data/fine-tune/driver | “Cùng7trụcnêncheckpointdùngngay” |
| **C. Panda/Franka cùngloạivớimôphỏng** | Gần hơn về topology, cóthểgiữjointorder8D saukhiđốichiếu | Chốtđúngmodel/firmware/FCI, jointzero/order,tool/load/gripper,camera/time,dynamics,rate/safety; học/thửtrênrealdata phùhợp | “CùngPandanênkhôngcònsim-to-realgap”;“model10Hzgửimotortựdo” |
| **D. “Taycủatôi” đangnóitớiPanda trongrepo** | ✅ Xác minh được mô phỏngPanda7khớp | Nốiobservation/executorjointmới vàoenvcũTCP,rồimớiđolearnedrollout | Gọi môhình3Dđó làPanda thật đangcótrongxưởng |
| **E. Nếu ýbạnlàMG400 trongchat/projectcũ** | Cóthểtáidùngý tưởngcameraIL; chưaxácminhđó làhardwarebạn sởhữu | MG400là4trụctheohãng,cần thu hẹptask vềworkspace/orientationkhảthi vàrepresentation4joint+tool phùhợp | GọiMG400làrobot6/7trục;điềukhiểnpose6DOFtùyý |

NguồnPanda hiện tại: [[J:src/simulation/panda_controller.py:34]], [[J:mujoco/models/franka_emika_panda/manifest.json:1]]. Ví dụFCI thật hỗtrợjoint/Cartesian và1kHz: [Frankaofficial](https://frankarobotics.github.io/docs/overview.html). MG4004axes: [Dobotofficial](https://de.dobot-robots.com/products/desktop-four-axis/mg400.html). Truy cập17/10/2026. TìnhhuốngA/B/E làkếhoạchphântích, khôngphầnmềmđãtriểnkhai.

TCP làframe/điểmlàmviệc củadụngcụ, khôngtựnó là“hệtọađộtoàncục”. Cầnchọnrobotbaseđểmôtảpose, địnhnghĩaworld→base vàflange→TCP. Với7DOF,cùngTCPposecóthểnhiềunghiệmjoint; khôngghépmộtbộjointPanda sangrobotkhácchỉbằngđổiđơnvị.

## 4. Sim-to-real và khả thi rig camera

| Khoảng cách | Hiện có | Cần đo/kiểm trước khi nói đã giải quyết |
|---|---|---|
| Ảnh | 🟡 Simulation vàMCRpretrained;crop/JPEG/INT8 | Realimageheldout;thayđổichiếusáng/phảnxạ/occlusion;soítcamera vàđộphângiảiphùhợp |
| Động học | ✅ PandaMenagerie;TCPảo vàIK | Kíchthước/zero/toolcalibrationthật;trackingerror vàđộlặp |
| Tiếp xúc | ✅ Contact/frictiontrongMuJoCo | Friction/compliance/backlash,force khiinsert; vật dễvỡ/xước/biếndạng |
| Thời gian | ✅ Grid10Hz vàphysics1kHzmôphỏng | Capture→sync→preproc→GPU→driverlatencyp50/p95,deadline miss,bufferage |
| Camera8view | ✅6external+2inhandtrongrigsource | BOM,khônggianlắp,USB/networkbandwidth,trigger/PTPhoặcđồngbộphùhợp,intrinsic/extrinsic,hand-eyecalibrationvàrecalibration |
| Thiếucamera | ✅ Attentionmask vàcameradropout | Ablationmấtview,trackingcausalage;phươngán khi mọi viewmất |
| Chấtlượng | ✅ Simgeom/contactevaluator | Kiểmtrađúngsảnphẩm ởđầura,independentvision/sensor/gauge vàreject/rework |

Domainrandomization hiện là 🟡 bằng chứngprofile/ảnh, chưa audit đầy đủ codegenerator/range. Đổi màu,nềnvàđèn khôngngẫunhiênhóama sát,khốilượng,độcứnghaytrễ. KhôngtựnóiDRđãxửlýdynamicsgap. Cơ sở nghiên cứu: [Tobin2017](https://arxiv.org/abs/1703.06907), truycập17/10/2026.

## 5. An toàn, tích hợp và vận hành

Đây là **kế hoạch tích hợp cần kỹsưxưởng phê duyệt theo quy trình của họ**, không là chứngnhận hoặc thiết kế an toàn đã hoàn thành. Dùng hướng dẫnchínhthức về riskassessment làm nền: [OSHAIndustrialRobotSystems](https://www.osha.gov/otm/section-4-safety-hazards/chapter-4), truycập17/10/2026; không coiOSHA là luật/chuẩnnghiệmthu tựđộngápdụng cho cellViệtNam.

| Rủi ro | Khả năng hỏi / hậu quả | Phương án trả lời trung thực và yêu cầu tiếp theo |
|---|---|---|
| Người vào vùng chuyển động, khởi động lại bất ngờ | Cao / Cao | ⬜ CầnRA,toàncellguard/interlock,E-stop,safeenable/restarttheorobotvàxưởng;AIkhôngđượcquyếtđịnh chức năngsafety. |
| Gắp hụt/rơi vật, kẹp sai | Cao / Cao | 🟡 Simcógrasp/dropflags. ⬜ Real cầnxácnhậngrasp,đặtvàquality;stop/reject cókiểmsoát,thửlạigiớihạnvàgọingười,khôngretryvôhạn. |
| Kẹt khi insert, vật dễ vỡ | Cao / Cao | ⬜ Chốtforcelimits/compliance,gripper/toolthiếtkế,ngưỡngdừngthửnghiệm;chưađolựcthật. |
| Ảnh cũ/mấtcamera/GPU chậm | Cao / Cao | ✅ Datapipelinecómaskage. ⬜ Onlinewatchdog giữ/dừngtheointerfacean toàncủahệthống;kỷluậttimestamp/deadline;khônggửilệnhmới khikhôngđủobservation. |
| PLC/MES không đồng bộ | Cao / Cao | ⬜ Cellstate machine vớiReady/Busy/Done/Fault,partID,recipe/version,qualityack,timeout;hiệntạichưacóintegrationreport. |
| Bảo trì, calibration drift | Trung bình / Cao | ⬜ Lịchkiểmcalibration/gripper,versionedmodelvàrollback,goldenparttest,operatorSOP;chi phíchưađo. |
| Model thay đổi không kiểm soát | Trung bình / Cao | ✅ Checkpointcontracttrongtrain. ⬜ Deploymentapproval/lockedversion,heldoutregression vàrollback;khôngonlinelearningtựđộng trêncellthật. |
| Bảo mật dữ liệu/giấy phép | Trung bình / Cao | ⬜ Chốtquyềndataset/weights,hạnchếtruycậpvàđườngtruyềntheoxưởng;chưatựgửidataDENSOraAPIngoài. |

## 6. Những câu phải thay ngay

- “Đã chứng minh học thật/tổng quát” → “Đã thực hiện train/validation và một số kiểm tra inference; generalization/closed-loop của nhánh mới cần đánh giá.”
- “ACT gắp đạt100%” → “Controller scripted đạt3/3seed; ACTTCPcũE5transfer0/10; chưa cóN/Ncủa joint mới.”
- “1.000demođạt” → “Manifest hiệntại chấpnhận913episode; cần chốt chấtlượng vàphạmvi bộ dữliệu.”
- “Chỉ thay cánh tay mô phỏng là chạy được” → “Thayrobot cầnrepresentation,data,calibration,driver vàsafetyvalidation phùhợp.”
- “Few-shot giúp làm quen nhanh” → “Few-shot làmụctiêusẽđobằngđườngcongN-demo vàbaseline.”
- “Hoàn vốn16–18tháng” → “Kịch bảnkinhtếphụthuộcCAPEX/lợiíchròng; case15triệu/ngườithì22,2thángchưaOPEX.”
- “Có lực kẹp20N nên xử lý vật dễvỡ” → “Policychưa dựđoánlực; fixedforcelimitkhôngthay thếthửnghiệmvậtliệu.”

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Ba khoảng trống kỹ thuật nghiêm trọng nhất của nhánh joint là gì?
2. Phản biện vì sao15task,20tháng và16–18tháng không thể đặt ngang nhau.
3. Nếu robotxưởng6trục, giữ được gì và phải thay gì?
4. Vì sao không dùng3/3controller hoặc spec repeatability để chứng minh accuracyACT?
5. Khi bị hỏi safety/few-shot/realrobot, nói đãX,chưaY,kếhoạchZ,nghiệmthuW nhưthế nào?
''')
print('Created 06')
