from doc_helpers import write
from qa_A_E import qa as first, groups as ga
from qa_F_J import qa as second, groups as gb
intro='''# 07 — Ngân hàng60câu hỏi giám khảo và trả lời trung thực

Chốt bằng chứng17/10/2026. Các câu hỏi là dự đoán của mentor, không phải đề doBTCcông bố. Câu trả lời mẫu có thể nói trong khoảng30–60giây tùy tốc độ; hãy tập bằng đồng hồ, giữ input/output và giới hạn bằng chứng nếu cần rút ngắn. Nguồnweb được dẫn truy cập17/10/2026. Các câu về deployment là kế hoạch, chưa phải tính năng đã lắp.

Hiện trạng xuyên suốt: ✅ controller/evaluator và pipeline; ✅ cachejointMCRtheolog; 🟡 người dùngbáoE25 nhưng chưa cómetric mới; ⬜ learnedjointsuccess/robotthật/few-shot/ROIđothật. Không lấyE58TCPhoặc3/3controller để trả lời cho jointMCRmới.

## Cách luyện khi bạn gõ “bắt đầu luyện Q&A”

Hỏi từng câu theo thứ tựA01→J06, chờ bạn trả lời rồi mới chấm. Không đưa ngay đáp án trước khi bạn thử. Chấm10điểm: hiểu bản chất3, đúng dự án/phiên bản3, bằng chứng2, trung thực2. Nêu chỗ sai/thiếu/né tránh, đưa bản sửa ngắn rồi hỏi follow-up khi cần. Không phạt bạn vì chưa có kết quả mà chính tài liệu đánh dấuCHƯA XÁC MINH; chấm cách bạn nhận giới hạn và đề xuất kiểm chứng. Chưa bắt đầu luyện trong lượt tạo tài liệu này.
'''
allqa=first+second
parts=[intro]
for group,title in ga+gb:
    parts.append(f'## {group}. {title}\n')
    for ident,q,intent,answer,evidence,dont,follow in allqa:
        if not ident.startswith(group):continue
        parts.append(f'### {ident}\n\n**Câu hỏi:** {q}\n\n**Giám khảo muốn kiểm tra:** {intent}\n\n**Trả lời mẫu (30–60giây):** {answer}\n\n**Bằng chứng/Con số để dẫn:** {evidence}\n\n**Đừng nói:** {dont}\n\n**Câu hỏi tiếp theo có thể bị hỏi:** {follow}\n')
parts.append('''## 10 câu nguy hiểm nhất và cách xử lý

| Câu | Nguy hiểm ở đâu | Cách xử lý khi bị ép trả lời ngay |
|---|---|---|
|A06 — Đã làm được gì?|Dễ gộp mọi phiên bản thành một hệ hoàn chỉnh|Nói rõcontroller,TCPcũ,jointmới vàbước chưa cómetric.|
|B04 — Valloss giống inference?|Dễ nhầm evalmode với bỏtarget|Chỉ điều kiệnactions!=None vànêu posterior/prior riêng.|
|C01 — 1.000demođạt?|Sốslidekhôngkhớpmanifest|Đính chính913accepted/111rejected,khôngbiếnthànhsuccessrate.|
|C04 — ĐổiTCP/joint?|Cùng8Dnhưngsainghĩacóthểdẫnđếncontrolsai|Nêu lý dojointthật vàcontract/data/stats phải đổi.|
|D01 — Video chứng minhAI?|Demo scripted cóprivilegedstate|Nhận nhãncontroller vàđưa checkpoint/logriêng nếu làpolicy.|
|D02 — 0/10?|Dễ né thấtbại hoặcđổcho mộtthànhphần|Nói đúngE5TCP10val,khônggánchojointmới,đềxuất phépkiểmnguyênnhân.|
|E01 — Safety?|Trảlời quáđà cóhậuquảnghiêmtrọng|Nhậnchưanghiệmthu,phânrõRA/cellsafety vớiAIreference.|
|F02 — Payback?|Sốhọcsai,lươngvàOPEXkhôngrõ|Tính22,2thángcase15triệu,phânbiệt15task,cầnnetbenefit.|
|G02 — Pretraincógiúp?|Thiếuablation nênkhôngcókếtluậnnhânquả|Nói cócơsở,chưađo,đưa đốichứngcùngcontract/budget.|
|H01 — E100xong?|Lệnh/càiđặt/pendingkhônglàtraininghoànthành|NêuE25theobáo,job14598pendingrồiyêucầuhủy,chưa cóhistorymới.|

Mẫu xử lý chung: **“Hiện nhóm đãX, chưa có bằng chứngY. Bước tiếp theo làZ; nhóm sẽ đánh giá bằngW.”** Xphải cóartifact,Yphải nói thẳng,Zcụthể vàWcómetric/protocol; đừng chỉ nói“sẽcải thiện”.

## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được

1. Trả lờiA06trong60giây màkhônggộpcontroller,TCPvàjoint.
2. Trả lờiB04vàC04bằngshape/semanticscụthể.
3. TínhlạiF01/F02màkhôngnhìnslide.
4. Nhậnmộtgiới hạntrongE01/G02màkhôngnétránhhoặcphủnhậnphầnđãlàm.
5. Chọncâunguyhiểmnhấtvớibạnvàđưamộtlinkbằngchứngđúngrun.
''')
assert len(allqa)==60 and len(set(q[0] for q in allqa))==60
write('07_QA_BANK.md','\n\n'.join(parts))
print('Created 07:',len(allqa),'questions,',len(ga+gb),'groups')
