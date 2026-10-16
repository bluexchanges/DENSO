from doc_helpers import write
rows=[]
def add(n,claim,meaning,evidence,status,say,q,extra=''):
    rows.append(f'## Slide {n}\n\n**Slide nói gì:** {claim}\n\n**Ý nghĩa thật:** {meaning}\n\n**Bằng chứng:** {evidence}\n\n**Trạng thái:** {status}\n\n**Câu nên nói (không quá 3 câu):** {say}\n\n**Có thể bị hỏi tiếp:** {q}\n'+('\n'+extra+'\n' if extra else ''))
add(2,'Checklist: ACT đa phương thức, mô phỏng Panda8camera, RH20T, 3–6 tháng, vốn1tỷ/thay3người/lương15triệu/hoàn vốn~20tháng, hướngfew-shot và kinh nghiệm tay6trục.',
'Đây là tóm tắt cam kết của đội. Các kết quả đo, giả định kinh tế và mục tiêu phát triển đang nằm cùng một bảng, nên phải nói riêng từng loại.',
'S2/PPTX; [[H::3568]] [[H::5754]]; [[J:src/models/mcr_act.py:44]]; [[J:configs/mujoco/panda_three_pegs.json:1]].',
'🟡 Model/mô phỏng có source; 🟡 pretrainjoint theo ghi nhậnE25; ⬜ few-shot/robot thật/ROI đo thật.',
'“Nhóm đã xây dựng pipeline học bắt chước và mô phỏng để kiểm tra bài toán gắp–đặt. Nhánh mới dùng MCR và góc khớp, còn hiệu quả nhà máy và few-shot là mục tiêu cần thử nghiệm. Các số kinh tế là giả định, nhóm sẽ hiệu chỉnh bằng dữ liệu cell thực.”',
'Cụ thể điều gì đã được chứng minh trong mô phỏng: controller hay policy học?',
'**Kiểm từng dòng:** (1) Không có benchmark chứng minh thích nghi tốt hơn trajectory cố định. (2) Công đoạn DENSO cần nguồn khảo sát. (3) “Dự kiến pretrain” đã cũ so với ghi nhận train mới; cập nhật joint/MCR và mức bằng chứng. (4) 1.000/45=22,22 tháng nếu tính triệuVNĐ, chưa trừOPEX; ~20 không khớp chính xác. (5) Few-shot là kế hoạch. (6) Kinh nghiệm6trục không xác định robotxưởng hoặc robot trong demo. “Tay máy được tài trợ” trên slide chưa có giấy/model xác nhận trong nguồn đã kiểm.')
add(4,'Tiểu sử cố vấn Nguyễn Đức Minh: bằngTiến sĩ2009,6năm nghiên cứu tạiKaiserslautern, chức danh và hướng nghiên cứu.',
'Giới thiệu năng lực cố vấn, không phải bằng chứng robot policy đạtKPI.',
'Chỉ S4 trong PPTX; chưa đối chiếu hồ sơ tổ chức hoặc CV trong lượt audit kỹ thuật này.',
'🟡 Thông tin do slide cung cấp; **CHƯA XÁC MINH** từng mốc/chức danh.',
'“Nhóm có cố vấn hỗ trợ định hướng nghiên cứu và kiểm tra kỹ thuật. Nhóm chịu trách nhiệm trực tiếp về số liệu thực nghiệm được trình bày.”',
'Cố vấn đã trực tiếp kiểm tra phần nào của dự án?')
add(5,'Tiểu sử cố vấn Nguyễn Huy Hoàng, Tiến sĩ2017, nghiên cứuAI/thị giác.',
'Nêu nền chuyên môn, chưa nói mức tham gia, thời lượng mentoring hay bảo chứng kết quả.',
'S5; chưa thấy CV/hồ sơ và biên bản review dự án trong repo.',
'🟡 **CHƯA XÁC MINH** thông tin lý lịch độc lập và phạm vi đóng góp.',
'“Cố vấn hỗ trợ nhóm về phương phápAI và thị giác. Kết quả của nhóm vẫn được đánh giá bằng log và protocol riêng.”',
'Phần kỹ thuật nào nhóm tự làm và phần nào do cố vấn góp ý?')
add(6,'Nghiêm Văn Quang, cửnhânHUST/thạcsĩNTU vàlinkLinkedIn.',
'Giới thiệu cố vấn thực hành, không suy ra đã có kinh nghiệm triển khai robot công nghiệp từ tên trường.',
'S6; linkLinkedIn hiện trên slide nhưng chưa dùng làm nguồn xác minh.',
'🟡 Thông tin slide; **CHƯA XÁC MINH** độc lập.',
'“Cố vấn hỗ trợ nhóm rà soát hướng triển khai. Khi nói kinh nghiệm, nhóm chỉ nêu phần có thể chứng minh bằng công việc cụ thể.”',
'Ai sẽ phụ trách tích hợp robot thật và calibration?')
add(7,'Hai thành viên: CPA3,7/4; kinh nghiệm đọcđồnghồ/mứcdầu99%; inferencegiọngnói<1giây; SepAdapter đang phản biệnICLR2027.',
'Đó là thành tích của người/những dự án khác, không phải accuracy99% của ACT gắpchốt.',
'S7; không có báo cáo benchmark, CV hoặc tình trạngreview của các dự án đó trong phạm vi repo đã kiểm.',
'🟡 **CHƯA XÁC MINH** các số99%,<1s,CPA và trạng thái nghiên cứu từ artifact độc lập.',
'“Các thành viên có nền tảngAI và hệ thốngnhúng từ những dự án trước. Số99% thuộc dự án đọcđồnghồ được nêu trên slide, không phải kết quả gắp–đặt của mô hình này.”',
'99% được đo trên bao nhiêu mẫu, metric nào và có liên quan gì tới robot?')
add(8,'Hai thành viênK70, CPA3,73/4 và3,67/4, từng làmML/PID.',
'Giới thiệu nền tảng và khả năng học, chưa chứng minh đội có đủ kỹ năng commissioning/safety.',
'S8; chưa thấy hồ sơ/metric dự án thành viên tương ứng trongrepo.',
'🟡 Thông tin slide chưa xác minh độc lập.',
'“Nhóm đang phát triển năng lựcAI và điều khiển qua dự án. Phần triển khai thật cần phối hợp kỹ sưxưởng và chuyên gia tíchhợp.”',
'Phân công cụ thể ai chịu trách nhiệm data,model,control vàsafety?')
add(10,'Công đoạn trước làm sạch vẫn phụ thuộc con người, linh kiện nhỏ gây mỏi mắt, lỗi và chi phí tăng.',
'Đề xuất một painpoint công nghiệp; ảnhminhhọa không chứng minh tỷlệ thủcông hoặc tỷlệlỗi.',
'S10 và ảnh; chưa thấy khảo sátcell,cycle-time log,phiếureject hoặc quan sát có ngày trongrepo.',
'🟡 Bối cảnh trên slide; **CHƯA XÁC MINH** tại cellDENSO cụ thể.',
'“Nhóm nhắm tới công đoạn gắp và xếp linh kiện nhỏ trước xử lý. Mức độ thủ công, lỗi và năng suất hiện tại cần được xác nhận cùng kỹ sưDENSO để chốt baseline.”',
'Tên công đoạn, mãlinhkiện và takt time hiện tại là gì?')
add(12,'Robot7DOF,ACT nhận8camera+state rồi dự đoán chuỗi hành động; hình là sơ đồACT gốc.',
'Panda có7khớp tay. Kiến trúc trên hình cần chú thích đâu là phần kế thừa và đâu là adapter mới.',
'S12; [[J:src/models/mcr_act.py:44]] [[J:src/models/rh20t_act.py:97]] [[J:configs/mujoco/panda_three_pegs.json:1]].',
'✅ Source model vàPanda; 🟡 vòng điều khiểnjoint end-to-end còn thiếu xác minh.',
'“Nhánh hiện tại dùngPanda7khớp, ảnh nhiều góc và trạng thái khớp. MCR trích đặc trưng rồiACT dự đoán20bước góckhớp+kẹp; nhóm còn phải kiểm tra vòng điều khiểnjoint trongtask.”',
'Các anh dự đoánjoint hayTCP, và đã chạy vòng kín chưa?',
'**Cần sửa hình/chú thích:** ảnhACTgốc/ALOHA không phải kiếntrúc8cameraMCR của nhóm. Thêm MCR ResNet50,maskcamera và state/outputjoint vào caption; không ghi đãthửrobotthật.')
add(13,'Bảng painpoint bằnghình: linh kiện~10mm,dễvỡ,dungsai2mm; học mẫu đểgiảm công setup; phản hồi lực là hướngmởrộng.',
'Slide nói yêu cầu công nghiệp nhưng taskcode làchốtØ6×35mm,lỗØ7 sâu12mm. Hai bài toán chưa được chứng minh tương đương.',
'Ảnh render S13; [[J:configs/mujoco/panda_three_pegs.json:1]]; [[J:src/models/mcr_act.py:137]].',
'🟡 Problem mapping; ⬜ forcefeedback và chứng minh linh kiện dễvỡ.',
'“Mô phỏng hiện dùng chốt chuẩn để kiểm tra kỹ thuật, chưa phải mô hình vật liệu của linh kiện thật. Nhóm chưa học lực kẹp; bước ứng dụng cần xác nhận dung sai, vật liệu và phản hồi tiếp xúc.”',
'Tại sao dùngchốt6mm nếu yêu cầu thật nói10mm,dungsai2mm?',
'S13 là nội dung nằm trong ảnh nên tríchtext banđầu không thấy. Dungsai2mm trên slide không cùng đại lượng với khehởbánkính0,5mm của task; không so trực tiếp để khoe chính xác hơnDENSO.')
add(14,'So sánh robottruyềnthống với hệhọc: táidùng, ítdemo và giảm công triển khai là mục tiêu.',
'Giảthuyết lợiích khi có nhiều biếnthể. Robot truyềnthống cũng có thể táidùngphầncứng,chươngtrình vàvision.',
'S14; chưa có thínghiệm vềgiờcông/baseline; sourceACT tại [[J:src/models/mcr_act.py:44]].',
'⬜ Lợiích so sánh chưa đo; 🟡 Hệhọc đã có nềntriểnkhai.',
'“Nhóm kỳ vọng giảm công cấu hình khi có nhiều biếnthể gắp–đặt liênquan. Với cellcốđịnh, teachpendant vàvisioncổđiển vẫn làbaseline cần đo côngbằng.”',
'Vì sao không chỉ dùngvision nhận vịtrí rồiIK?')
add(15,'Sơ đồbằnghình:camera/state→ACT→Pandagắpđặt→đánhgiá.',
'Đây làluồng mongmuốn; cần phân biệt modulecócode và vòngkín đã chạy.',
'Ảnhrender S15; [[J:src/simulation/panda_env.py:113]] [[J:src/simulation/panda_controller.py:16]] [[J:src/models/mcr_act.py:94]].',
'🟡 Pipeline có nhiều khối, chưa xácminh nối jointMCR→controller mới.',
'“Sơ đồ thể hiện quy trình cần hoàn thiện. Mô phỏng vàevaluator đã có, nhưng adapter observation/actionjoint phải khớp trướckhi gọi đây là learnedpolicy end-to-end.”',
'Khối nào đã chạy thật cùngnhau, khối nào mớiđứngriêng?')
add(16,'Bốn bước pretrainRH20T→demođích→fine-tune→chạy/đánhgiá; dướihình ghi dự đoán pose tay+kẹp.',
'Quy trình học chuyển giao hợp lý ở mức kế hoạch, nhưng mô tảoutputpose thuộc nhánhTCP cũ.',
'[[H::3568]] [[H::5754]] [[J:src/data/cfg5_masked.py:227]] [[J:src/data/sim_demos.py:89]].',
'✅ Quyếtđịnh joint; 🟡 train mới theoE25; 🟡 demođíchTCP đã có; ⬜ fine-tunejoint/rolloutđích xácminh.',
'“Sau lần thửTCP, nhóm đã chuyển sang bảy góc khớp và độ mở kẹp vì có nhãnjoint ghi thật. Do đó phải chuyển cả dữ liệu taskđích và bộ điều khiển sang đúng hợpđồngjoint. Các bướcfine-tune và đánhgiá nhánhmới chưa được coi là xong.”',
'Hai bộdữliệu đều8chiều,tại sao vẫnkhôngfine-tune thẳngđược?',
'**Giải thích sâu:** pretrainjoint: observationt, targetmeasuredq ởt+1…t+20 và futuregrippercommand. DemoTCPđích: measuredTCPstate t, commandedTCP cùngtick pre-step,offset0. Khácđơnvị,ýnghĩa,timing vàstats. KhôngdùngE58TCP làmresumejoint. CVAEposterior dùngtarget khi train; inferz=0. Xem02.')
add(17,'Khẳngđịnh1.000demonstration môphỏng đạt,8viewđồngbộ,randomization màu/nền/đèn/vịtrí/vậtphụ.',
'Đang nói cả sốlượng,chấtlượng vàđộphủ. Phải đối chiếu manifest hơn ảnhsample.',
'[[J:data/splits/pick_place_finetune_manifest.json:1]] [[J:data/splits/pick_place_finetune_splits.json:1]] [[J:src/data/sim_demos.py:68]] [[A:measured_facts.json:1]].',
'✅ Códata/multiviewmanifest; 🟡 claim1.000đềuđạt vàrange randomizationchưa xácminh đầyđủ.',
'“Manifest hiện có913episodeđượcchấpnhận,111mục bịtừchối do thấtbại hoặcvideolỗi. Nhóm cócácprofilebiếnthiên, nhưng cần chốt lại sốdemo dùngđược vàrange randomization trước khi côngbố.”',
'1.000 là sốlầnthử,sốthànhcông,hay sốepisodequa kiểmtra?',
'**Sốaudit:** 913accepted,111rejected,duplicates0; rejected gồm24khôngsuccess,87videolỗi/thiếuframe. Split731/91/91. Profileaccepted:fixed1,varied4,diverse208,rich700. Khônggọi913/1024làsuccessratecontroller vìvideoerrors vàcandidate selection làmđổi mẫu số. Cácprofiletênrich/diverse khôngtựchứngminh mỗi tham sốrandomization vàheldoutOOD.')
add(18,'Rig8RGBcamera=6cốđịnh+2inhand; ACTnhậnảnh+state,rachuỗipose+kẹp,chưadựđoánlực.',
'Kiếntrúc hiện tại cần thaypose bằngjoint; cameraRH20T trênslide làminhhọa,khôngphải rig ngoàiđời đãlắp.',
'[[J:configs/data/cfg5_all8.json:6]] [[J:src/models/mcr_act.py:73]] [[J:src/models/mcr_act.py:137]] [[J:src/simulation/panda_controller.py:16]].',
'✅ Rig/slotcode vàhead8D; 🟡 bridgejoint; ⬜8camera thật/forcepolicy.',
'“Mô phỏng bốtrí sáu camera ngoài vàhai camera trên tay. Nhánhhiệntại dự đoán góckhớp+kẹp, cómask khi camera thiếu và chưa dựđoán lực; cấu hìnhcamera ngoàiđời phải đo chi phí/hiệuchuẩn.”',
'Tại sao cần8camera,giảm xuống2–3camera cóđược không?',
'8slotkhôngphải mọi timestamp có8ảnhhợplệ. MCR dùngsharedbackbone,maskB×8,featureB×8×2048×7×7. Lựcgiớihạn20N trongconfigcontroller không phải forceprediction củaACT.')
add(19,'“Hướngtới few-shot”:pretrainđa dạng→ítdemo mới→mởrộng biếnthể.',
'Địnhhướng vềsampleefficiency, chưa phải kếtquả one-shot/few-shot đã đo.',
'S19; [[H::5754]]; chưa thấyablationN-demo/heldouttask trongartifactđãkiểm.',
'⬜ Few-shot/đa tácvụ cókiểmchứng; 🟡 nềndatađa task.',
'“Few-shot hiện là hướng pháttriển. Nhóm sẽđo success trên cácmức sốdemo vàso sánh có/khôngpretrain với taskmới táchriêng.”',
'Ít làbaonhiêudemo,vàđãcóđườngcongN-demo chưa?',
'RH20T cóone-shot trongtênpaper khônglàmACTcủanhóm tựđộng thànhone-shot. Có104tasktrongpretraindata cũngkhôngchứngminh policyđãlàmđược104task.')
add(21,'Khung giờcông,lấy8h/ngày và250.000VNĐ/h; so cônglậptrình/train/kiểmthử.',
'Đangước tính **engineeringeffort**, khác tiềnlương côngnhânvậnhành ởS2/36.',
'S21; khôngthấybảngchấmcông/báogiá xácnhận250.000đ/h trongrepo.',
'⬜ Giảđịnhkinhtế, chưađolường.',
'“Đây là đơn giágiảđịnh cho côngkỹsư triểnkhai. Nhóm tách khoản này khỏi lươngcôngnhân vận hành vàchưa coi làbáogiáDENSO.”',
'250.000đ/h lấyởđâu,cóbaogồmoverheadkhông?',
'250.000×8=2triệu/ngày; nếu160h/tháng thì40triệu/tháng,nhưng đó làquyđổisốhọc, khôngchứngminh mức lươngngười cụthể. Khôngnhấtthiết mâu thuẫn15triệu nếu khácrole/costbasis,phải ghi rõ.')
add(22,'Teachpendant/độnghọc sovớicollectdata/train/evalIL-RL.',
'Thời gianpháttriển cócấu phầnkhácnhau, chưađủ so sánh chỉGPUtrainhours.',
'S22; [[R:server_train_mcr_current.py:41]] cho thấytrain chỉ làmộtbước, khôngcólogengineeringhours.',
'⬜ So sánhthờigian chưađo.',
'“VớiAI, côngtriểnkhai gồm dữliệu,hiệuchuẩn,huấnluyện và nghiệmthu. Nhóm sẽđo giờlaođộng riêng vớigiờmáychạy để so côngbằng.”',
'Trong8h/bàicủacácanh có gồmcollectdata vàsafetyvalidation không?')
add(23,'Bảngthamkhảo:teach1–8h;IK1–5ngày;vision3–14ngày;IL1–7ngày;RLvàingày–vàituần.',
'Các khoảngdựtoánkhácmứcphạmtácvụ,hệthống; chưa làbenchmark.',
'S23; khôngcó nguồn/time-study ghi trongNotes (Notesrỗng).',
'⬜ Giảđịnh, **CHƯA XÁC MINH** khoảngthờigian.',
'“Bảng này chỉ giúp lập kếhoạch sơbộ. Thời gianthực cần đo trên cùngmộtcell,cùngđộkhó vàcùngtiêuchí nghiệmthu.”',
'Cùngbàigắpchốt,cácanh đãđo từngphươngpháp chưa?',
'Nếu8h/ngày:IK8–40h,vision24–112h,IL8–56h; đây chỉlà quyđổi,khônglà sốđo. Độrộng của các khoảngkhôngchứngminh phươngphápAI nhanhhơn.')
add(24,'Ví dụteachgắpđặt khihardwarecósẵn:30–60phútsetup,30–90phútdạy4–8điểm,15–30phútkẹp,30–120phúttest;headline2–5h.',
'Scopehẹpkhilắpsẵnrobot/gripper,sovớiAI cũngphải giữcùngscope.',
'S24,khôngcótime-study độc lập.',
'⬜ Dựtoán.',
'“Ví dụ này giảđịnh phầncứng đãlắpsẵn. Tổngcácmục là khoảng1,75đến5giờ,làmtròn2–5giờ; khôngđạidiện mọi bài toán.”',
'Cácanh đãtínhthiếtkếgripper,PLC vàvalidationchấtlượng chưa?',
'Min30+30+15+30=105phút=1,75h.Max60+90+30+120=300phút=5h.4–8làsốđiểmdạy,khôngphải4–8giờ.')
add(25,'Đơn giản2–5h,trungbình1–3ngày,phứctạp3–7ngày;10bài nhân10.',
'Phânnhómđộkhólàgiảđịnh,cần địnhnghĩanghiệmthu vàcellphùhợp.',
'S25; khôngcóphânloạitaskđãđo.',
'⬜ Dựtoán.',
'“Nhóm phânnhóm để dựng kịchbảnchi phí. Địnhnghĩađộkhó vàkhoảnggiờ cầnđược xácnhận bằngtaskthật.”',
'Taskchốtcủacácanh thuộcnhómnào vàvìsao?',
'10bàiđơngiản20–50h.Trungbình10–30ngày=80–240h.Phứctạp30–70ngày=240–560h,đều theo8h/ngày.Số16h và40h ởS26 nằmtrongcáckhoảng,tuy nhiên chưacóphépđo chọnchúng.')
add(26,'10bàihỗnhợp:4đơngiản×4h+4trungbình×16h+2phứctạp×40h=160h=20ngày=40triệu;tiêuđề120–200h.',
'Một kịchbản trungtâm cótrọngsố,sauđógiữ trungbình16h/bài đểvẽhòavốn.',
'S26;bằngchứnglàphéptínhtrênslide,khôngphảiartifactnăngsuất.',
'✅ Sốhọcđúng; ⬜ địnhmức/chứngminhthựctế.',
'“160giờ làvídụ từcơcấu4–4–2vàđịnhmức4–16–40giờ. Đây làgiảđịnh lập kếhoạch,nhóm chưađo trên10taskthật.”',
'Tạisaođịnhmứclà4,16,40h vàtạisaođúngtỷlệ4–4–2?',
'16+64+80=160h;160/8=20ngày;160×250.000=40triệu.Khoảng120–200h khôngđược suyra từbảngcốđịnh này,nên cầnghi làrangegiảđịnhriêng hoặc bỏheadlinekhoảng.')
add(27,'Khicónềntảngsẵn,160h truyềnthống sovới80hAI,giảm50%;40vs20triệu.',
'So **marginaleffort** saukhilàmxongplatform;khôngphải totalcost lầnđầu.',
'S27chart;S28/29mớicósetup;chưacótime-study8h/task.',
'✅ Phéptính50%; ⬜ Mứcgiảmđothật.',
'“50% chỉ đúng trong giảđịnh nền tảng đãsẵn vàmỗi bàiAI tốn8giờ. Lầnđầu cầncộng giờsetup nênchưa thểnói tiếtkiệm50% tổngdựán.”',
'Ai trả120giờsetup vàbaogiờdebugdữliệu?',
'(160−80)/160=50%;80×250.000=20triệu.8h/bài làgiảđịnh,khôngphảithờigiantrainingGPU8h đãđo.')
add(28,'DigitalTwin40–80h;IsaacLab/training/sim-to-real40–80h;10bài80h;tổng160–240h.',
'Chi phí nền80–160h cộngcôngbiên80h. Côngcụ trênslidekhácrepo.',
'S28;[[J:src/simulation/panda_env.py:1]] dùngMuJoCo;[[J:requirements-sim-lock.txt:1]].',
'✅ XácminhMuJoCo; ⬜ Địnhmứcgiờ; **CHƯA XÁC MINH** sửdụngIsaacLab.',
'“Dự ánhiệntại dùngMuJoCo. Nhóm sẽsửa têncôngcụ trênslide vàgiữchi phíthiếtlậplàgiảđịnh cầnđo,khôngclaim đãlàmsim-to-real trong80giờ.”',
'Cácanh cócodeIsaacLab ởđâu?',
'40–80+40–80=80–160hsetup;+80=160–240h.Nguồn120h ởS31làgiátrịgiữa80–160,khôngphải sốđo. Khôngđược gọiPandaMenagerie làDigitalTwinđãhiệuchuẩn củacellDENSO.')
add(29,'10bàiđầuAI160–240h,40–60triệu,sovới160h40triệu;vídụsetup120+80=200h.',
'Nhận thẳng chi phíkhởiđầu cóthểcaohơn; thuậnlợiAIcầnsốlượngtaskvàreuse.',
'S29/S28/S21;phéptínhđúngtheogiảđịnh.',
'✅ Sốhọc vàphânbiệtscope; ⬜ kiểmxácnhậngiảđịnh.',
'“Ở10bàiđầu,AI chưa chắc tiếtkiệm giờcông. Kịchbảntrungtâmlà200giờ,caohơn40giờsovớibaseline160giờ.”',
'Vậytại saoDENSOnênđầutưnếu chỉcó10task?',
'160–240h×0,25triệu/h=40–60triệu.Vídụ200h=50triệu,thêm10triệusovớitruyềnthống.Khôngbiếnrange80–160setup thànhcamkếttrầnchi phí.')
add(30,'Lặpbảng10bàihỗnhợp160h/20ngày/40triệu.',
'CùnggiảđịnhS26,khôngphảimộtthínghiệmthứhai.',
'S30,S26.',
'✅ Sốhọc; ⬜ địnhmức.',
'“Đây vẫn làbaseline160giờtừvídụ trước. Nhóm giữ nhấtquán để vẽ tổnggiờtheosốtask.”',
'Nếu10taskđềulàđơngiảnthìđiểmhòavốncòn15không?',
'Cóthểchuyểnslide này thànhbackupđểtiếtkiệm30phút. Nếu baseline4h/taskthấp hơnAI8h/taskthìkhôngcóhòavốn dươngởmôhìnhtuyến tính này.')
add(31,'Htruyềnthống=16n;HAI=120+8n;giờtiếtkiệm=8n−120.',
'Haiđườngthẳngmôhìnhhóaengineeringhours,vớichi phísetupcốđịnh vàmarginalcostkhácnhau.',
'S31;16=160/10trongS26;120nằmgiữa80–160S28;8=80/10S27.',
'✅ Đại số; ⬜ tham sốđo.',
'“n làsốtaskđượctriểnkhai trên nền tảng cóthểtáidùng. Nhóm giảđịnh16giờ/tasktruyềnthống,120giờsetupAIvà8giờ/taskAI; cácđịnhmứccầnđượckiểm bằnglogcôngthật.”',
'Nhưthếnàolàmộttaskvàreuseđượcđếnmức nào?',
'16h làtrungbìnhcủamix4–4–2,chưaphảiđịnhmứctấtcảtask. Côngthứctổngquát:n*=Hsetup/(htrad−hAI),chỉcóhòavốndươngnếuhtrad>hAIvàreuse giữđược.')
add(32,'Hòavốngiờcôngtại15bài:120/(16−8)=15;240h/cách=60triệu.',
'Điểmgiao hai môhình engineeringcost,khôngphảithánghoànvốnvốnrobot.',
'S32;đồthịhòavốnvàcôngthứcS31.',
'✅ Sốhọc; ⬜ Dựbáolợiíchthực.',
'“15bài làđiểmhòavốnvềcôngtriểnkhaitrongkịchbảnnày. Nókhôngnóirobotsẽhoànvốn sau15tháng.”',
'Nếusetup160hhoặcAI12h/taskthìhòavốnởđâu?',
'ThayHsetup160,htrad16,hAI8→20task.ThayHsetup120,hAI12→30task.Tại15:16×15=240h;120+8×15=240h;240×0,25=60triệu.Tại15chỉhòavốn,tiếtkiệmdươngtừtask16nếunnguyên.')
add(33,'Bảngn=10/20/30/50/100 vàtiếtkiệm−10/10/30/70/170triệu.',
'Thaynsovớihàm8n−120,khôngphảikếtquảđo100task.',
'S33,S31.',
'✅ Tấtcảhàngsốhọcđúng; ⬜ Độđúngmôhìnhchi phí.',
'“Cácmốctrongbảnglàprojectiontheocùnggiảđịnh. Khiđổicell,robot hoặcdistributiontask,nền tảngcóthểcầnbổsungsetup nênkhônggiữđườngthẳngmãimãi.”',
'Tại100taskcónhữngchi phítăngthêmnàochưatính?',
'10:(160,200,−40,−10).20:(320,280,40,10).30:(480,360,120,30).50:(800,520,280,70).100:(1600,920,680,170).BốngiátrịmỗihànglàHtrad,HAI,giờtiếtkiệm,triệuVNĐ;khôngbaogồmvốnrobot,OPEX hoặcqualityloss.')
add(34,'10taskđơngiảncóthểdùngteachpendantkinhtếhơn;AIcólợikhireusenhiềutask.',
'Mộtđiềukiệnkinhtếhợplý,nhưngcầnđođộđa dạng vàsamplecost.',
'S34vàmôhìnhS31;chưacóbenchmarknhóm.',
'🟡 Lậpluậnđiềukiện; ⬜ Kếtquảkiểmthực.',
'“NhómkhôngđềxuấtAIchomọicell. Ưutiênlàcáccôngđoạn cóbiếnthểliênquan màtáidùngđượcdữliệu vàphầncứng.”',
'CellDENSOnàocónhiềuđủbiếnthểđểbùsetup?')
add(35,'Thủcônglỗi~2–5%,ca8–10h;robotđộchínhxáccao,24/7,nhanhthíchnghifew-shot.',
'Cácclaimhiệusuất/chấtlượngchưađobịviếtnhưkhả nănghiệnhữu.',
'S35;[[R:epoch5_transfer_probe_14120/report.json:1]] là0/10TCPcũ;nhánhmới chưa cósuccessrate;S19ghi“hướngtới”.',
'⬜ Lỗi2–5%,24/7,accuracycao,few-shotthựcnghiệm **CHƯA XÁC MINH**.',
'“Robotcótiềmnăng giảm thao tác lặplại,nhưngnhómchưađo vận hànhliêntục hay độchínhxác hệhọc. Cácsốlỗithủcông vàkhả năngfew-shot cầnđượcxácnhận bằngpilot.”',
'Chínhhệthốngcácanhđạtbaonhiêuphầntrămthànhcông?',
'Khôngdùng3/3controllerlàmaccuracyACT.24/7là168h/tuầntrênlýthuyết,khôngtươngđươnguptime100%:cònchangeover,nạpphôi,bảotrì,lỗi vàngườigiámsát. Nêndùngavailability/takt/yield đođược.')
add(36,'Thủcôngcóxúcgiác,robotđangpháttriển;claimđếmphântíchlỗitheothờigianthực;chi phílương18–20triệu,robot~1tỷ/bảotrìthấp.',
'SlideghépnănglựcđangcóvớikếhoạchMES/giámsát vàgiảđịnhchi phí.',
'S36;[[J:src/models/mcr_act.py:137]] headjoint/width,chưaforce;[[J:src/simulation/panda_evaluator.py:65]] metricsmôphỏng,khôngMES.',
'🟡 Evaluatormôphỏng; ⬜ forcetaskthật/MES/bảotrìthấp vàbáogiá.',
'“Hệthốnghiệntạichưa học lực kẹp vàchưa chứngminh xử lýlinhkiệndễvỡ. Đếm/lưukếtquảmôphỏngđãcó,nhưngđồngbộdâychuyền/MES vàchi phívậnhànhlàbước triểnkhai tiếp.”',
'Đếmđượcđúngsốlinhkiệnngoàiđời haychỉđếmsuccessflag?',
'BảntómtắtbạnđưanóiS36“chưadựđoánlực”,nhưngslide thựcchỉghi“đangpháttriển”;câuchưadựđoánlựcnằmS18.18–20triệucóthểlàfullyloadedcostkhác15triệubasewageS2,chỉchấpnhậnnếuđịnhnghĩa vànguồnrõràng.1tỷchưacóBOM.')
add(37,'Hệthốnghọclinhkiệnmớinhanh,dễtíchhợptaymáyhiệncócủanhàmáy.',
'Đây làlờihứaretargement,tíchhợp vàsampleefficiency chưađochứng.',
'S37;[[J:src/simulation/panda_controller.py:29]] đanghard-codePanda7joint;chưabiếtrobotxưởng.',
'⬜ Triểnkhai ngang/few-shot; 🟡 codemôphỏngPanda.',
'“Khả năngtáidùng làhướngpháttriển,khôngchỉđổimodelXML. Robotkháccần kiểmđộnghọc,gripper,camera,driver vàtrainlạidữliệuphùhợp.”',
'ChuyểntừPanda7trụcsangrobot6trụccầnđổicụthểgì?',
'Sửalỗichữ“củnhận”,“a nhàmáy”;thay“dễdànglắpđặt”bằng“cầnpilotvàadaptertheorobot”.')
add(38,'Ướctínhhoànvốn16–18tháng,chuyểncôngnhânsangquality.',
'MộtmôhìnhcashflowCAPEX/OPEXkhác hòavốngiờcôngS32.',
'S38/S2/S36,chưa cóBOM hoặcproductionstudy.',
'⬜ ROIgiảđịnh, **CHƯA XÁC MINH** lợiíchtiềnmặtthực.',
'“Hoànvốncần tính theochi phíđầutư vàlợiíchròngmỗitháng. Với15triệu/người vàbangười,phéptínhđơngiảnra22,2tháng;nhóm cần sửa hoặcđịnhnghĩalại giảđịnhđểthốngnhất.”',
'16–18thángđược suyra từkhoảntiếtkiệmnàovàđãtrừbảotrìchưa?',
'1tỷ/(3×15triệu)=22,22tháng.1tỷ/(3×18triệu)=18,52;/(3×20triệu)=16,67tháng,đềuchưaOPEX.Đạt16–18thángcầntiếtkiệmròng55,56–62,5triệu/tháng.Đạt20thángcần50triệu/tháng.Nếuchỉchuyểncôngnhânsangkhâukhác,đókhôngtựđộnglàcashsalarysaving;cầnđooutput/costavoidance thực.')
add(40,'GanttT1–T8:gđ1T1,gđ2T2–T3,gđ3T4–T5,mụctiêuxahơnT6–T8;cácdòngđượclàmsongsong.',
'Tổngcácdurationcủadòng khôngphảicalendarduration. Coreplan5thángnằmtrong3–6thángS2nếuđịnhnghĩascope.',
'ẢnhrenderS40đãkiểm;[[H::5754]] chỉxácnhậntrainingtheolờibáo,chưa hoànthànhrobotthật.',
'🟡 Môphỏng/train; ⬜ Robotthật vàfew-shot;khôngkếtluậnmâuthuẫn8với6thángchỉvì8cột.',
'“KếhoạchcoretronghìnhlàT1đếnT5,vớidựngmôphỏng vàcollect/trainchạysongsongtheogiaiđoạn. T6đếnT8dànhhướngmởrộng;tiếnđộthựccần gắnnghiệmthuphầncứng vàmetric.”',
'Mốcnàođểchuyểngiaiđoạn,hỏngthửnghiệmthìlùiởđâu?',
'Đãxemhình:nghiêncứu1tháng+dựngscene1thángcùngT1;data2tháng+train2thángcùngT2–T3;triểnkhai2tháng+fine-tune2thángcùngT4–T5. Khôngcộngthành10tháng,khôngtựcoiT8làhạncore.Mụctiêuxahơn“họcđaphươngthức”mơhồvìảnh+stateđãđaphươngthức;nênghi“bổsungforce/tactile”nếuđólàýđịnh,chưaxácnhận.')
add(42,'Đãdựngmodel/môphỏng/data,đãpretrainRH20T“đểhọctổngquát”,train/inference“môoverfit”rồichứngminhhọcthật;tiếptheo datađích/robotthật/few-shot.',
'Cótiếntriểnthật,nhưngcâukếtluậngộphọctrêntrain,tổngquáthóa vàtasksuccess.',
'[[R:checkpoints/before_test_20261007_142338/history.json:1]] [[R:epoch5_transfer_probe_14120/report.json:1]] [[H::5754]] [[J:src/data/sim_demos.py:68]].',
'✅ CáckhốivàthửTCPcũ; 🟡 E25jointtheobáo; ⬜ Tổngquáthóa/learnedjointsuccess/robotthật/few-shot.',
'“Nhómđãxâydựngpipeline dữliệu,môphỏng vàthực hiện các lượttrain/validation. LầntransferTCPbanđầucònhạnchế,nênnhómđãchuyểnsangjointvàMCR;nhánh mới cầnđánhgiáclosed-loop. Nhómchưa kếtluậntổngquáthóa haythaythếcôngnhân.”',
'“Họcthật”củacácanhnghĩalàlossgiảm,khớpnhãnhaygắpđượcthật?',
'Sửalỗichữ“hoànhiện”,“môoverfit”,“few-short”.Pretrainđểhọctổngquátlà**mụctiêu**,khônglàkếtquảđãđo. Đãcósmokefine-tuneTCPngày08/10,nhưngchưa thấycompletedrunreport;đừngnóihoàntoànchưachạmdatađích,màcũngđừngnóiđãfine-tunejointxong.')

intro=r'''
# 05 — Giải thích từng slide và câu nên nói

Đã đọc43slide,Notes vàảnhrenderPowerPoint. ChỉS2cóNotes cótext,Notes đóghi nguồntemplate vàảnhCopilot,khôngcungcấpnguồnkinhtế. Cácslidechỉtiêuđề/trangngănđược bỏqua:1,3,9,11,20,39,41,43. Còn35slidecónộidungđượcđốichiếudướiđây. Nguồngốc: `F:/Denso/Denso-Hack_Presentation-EDABK_TriH.pptx`; bảntrích [[A:slides_extracted.json:1]], ảnh `_audit/slide_renders/`.

**Cáchdùng:** họcýnghĩa vàbằngchứng,rồinóibằnglờimình. Câumẫulàbảnsửatrungthực,khôngphảiđọclạiclaimtrênslide. Mỗi mụcSxxthamchiếuchínhslideđãxem; nhữngphầnkhôngcólog/codeđượcgiữCHƯA XÁC MINH.

**Ba điều phải cập nhật trước:** outputnhánhmớilàjoint/MCR; sốdemođượcchấpnhậnkhôngkhớpclaim1.000đạt; kếtquảtrain/TCPtransferkhôngchứngminhgeneralization. Phầnsửaưu tiênxem06và09.
'''
tail=r'''
## Bảng kiểm toàn bộ số kinh tế trên slide

| Số/claim | Kết luận đối chiếu |
|---|---|
|8h/ngày|Giảđịnhquyđổiđơnvị,khôngphảisốca/taktđothật |
|250.000đ/h|Engineeringcostgiảđịnh,khácproductionwage,chưacónguồn |
|4/16/40h|ĐịnhmứcchọntrongrangeS25,khôngtime-study |
|4–4–2task|Mixminhhọa,khôngphảicơcấutaskDENSOđãkhảosát |
|160h/20ngày/40triệu|Phéptínhđúngtrongmixđó |
|80h/20triệu/50%|ĐúngnếusetupđãcósẵnvàAI8h/task,giảđịnhchưađo |
|80–160hsetup,120htrungtâm|Tổngvàmidpointđúng,khôngphảiquantrắc |
|160–240h/40–60triệulầnđầu|Phéptínhđúng,gồmsetup+80h |
|15task/240h/60triệu|Điểmgiaomôhìnhgiờcông,khôngthángCAPEX |
|−10/10/30/70/170triệuS33|Đúngcôngthức,nềnreusecóđiềukiện |
|15triệu/người,S2|Giảđịnhwage,cầnnóibasehaytotalcost |
|18–20triệu/người,S36|Giảđịnhkhác,cầnthốngnhấtcostbasis |
|1tỷ|ChưaBOM/báogiá,táchrobot/gripper/camera/PC/cell/safety/integration |
|~20thángS2|Sốhọctheo3×15ra22,22,chưatrừOPEX |
|16–18thángS38|Cóthểgầncase3×18–20,chưaOPEX;khôngđúngcase15 |
|24/7,lỗi2–5%,accuracycao|Chưacósốđohệthốnghoặcbaselinecell |

## Những điểm slide thực khác bản tóm tắt ban đầu

1. S13 cólinhkiện~10mm/dungsai2mmvànộidunghướngforcefeedback,nằmbêntrongảnh.
2. S36khôngghinguyênvăncâu“chưadựđoánlựckẹp”;S18mớighiđiềuđó.
3. S40khôngcó8thángcore:kếhoạchcoreT1–T5,mởrộngT6–T8.
4. S17claim1.000đạt,mâu thuẫnít nhấtvớimanifesthiệntại913accepted/111rejected;khôngtựchọn1000làsốđúng.
5. S42dùngngônngữkhẳngđịnh“chứngminh…họcthật”,trongkhi bằngchứngphải táchposteriorloss/priorinference/rollout.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. TạisaophảisửaoutputởS16vàS18?
2. TựtínhtoànbộS26,S31–33vàcasehoànvốnS2/S38.
3. S17đangđếmnhữnggì,cóthểgọilà1.000demođạtchưa?
4. GiảithíchS40màkhôngcộngnhầmdurationcácdòngsongsong.
5. Nóirõbađiềuđãlàm,bađiềuchưachứngminhởS42.
'''
write('05_SLIDE_GUIDE.md',intro+'\n\n'+'\n\n'.join(rows)+tail)
print('Created 05, content slides',len(rows))
