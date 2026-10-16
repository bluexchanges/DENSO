from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from xml.sax.saxutils import escape
O=Path(__file__).parent.parent
for name,file in [('Arial','arial.ttf'),('Arial-Bold','arialbd.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial',boldItalic='Arial-Bold')
W,H=595.276,841.89
c=canvas.Canvas(str(O/'08_CHEAT_SHEET.pdf'),pagesize=(W,H))
c.setTitle('EDABK_TriH - Tờ ôn DENSO - 17/10/2026')
c.setAuthor('EDABK_TriH - Tài liệu mentor dựa trên kiểm tra nguồn')
navy=HexColor('#183448');teal=HexColor('#087E8B');gray=HexColor('#475569')
style=ParagraphStyle('body',fontName='Arial',fontSize=10.1,leading=13.5,textColor=navy,spaceAfter=0)
def para(text,x,y,w,size=None,leading=None,color=None):
 s=ParagraphStyle('p',parent=style,fontSize=size or style.fontSize,leading=leading or style.leading,textColor=color or navy)
 p=Paragraph(text,s);_,h=p.wrap(w,H);p.drawOn(c,x,y-h);return y-h
def section(text,x,y,w):
 c.setFillColor(teal);c.roundRect(x,y-19,w,19,3,fill=1,stroke=0)
 para('<b>'+text+'</b>',x+7,y-3,w-14,9.4,12,HexColor('#FFFFFF'))
 return y-26
c.setFillColor(navy);c.rect(0,H-8,W,8,fill=1,stroke=0)
y=H-29
y=para('<b>HIỂU ĐÚNG TRƯỚC KHI BẢO VỆ</b>',30,y,W-60,18.5,23)
y=para('EDABK_TriH | DENSO Factory Hacks 2026 | Bản chốt 17/10/2026',30,y-4,W-60,9,12,gray)
y=para('<b>Hiện tại: joint + MCR.</b> Bạn báo E25; chưa có log xác nhận E100 hay success rate của policy mới. [1]',30,y-7,W-60,9.1,12)
y-=10
c.setFillColor(HexColor('#EDF6F7'));c.roundRect(30,y-60,W-60,60,5,fill=1,stroke=0)
para('<b>SƠ ĐỒ PHẢI VẼ ĐƯỢC</b><br/>CFG5 RGB + joint → căn timestamp 10 Hz / split / train stats → MCR frozen → ACT<br/>→ checkpoint → inference z=0 → <b>joint executor CÒN CẦN NỐI</b> → Panda/MuJoCo → evaluator<br/>Demo task đích hiện dùng TCP: phải có nhãn joint phù hợp trước khi fine-tune. [1-3]',39,y-6,W-78,8.7,11.6)
top=y-72;gap=16;cw=(W-60-gap)/2;x1=30;x2=30+cw+gap
yl=section('10 MỐC CẦN NHỚ',x1,top,cw)
numbers=[
('7 joint + kẹp = 8D','q tuyệt đối (rad), độ mở (m); khác TCP. [2]'),
('8 slot camera','6 ngoài + 2 in-hand; thiếu view dùng mask. [2]'),
('10 Hz','Grid dữ liệu; chưa phải Hz motor thật. [2]'),
('K = 20','Chunk nhãn 2 giây; khác query frequency. [2]'),
('β = 10','L1 + 10 KL ở config nền; chưa KL sweep. [2]'),
('1.317 episode CFG5','Split 1.053 train / 132 val / 132 test. [1]'),
('913 demo accepted','Manifest task đích; không nói 1.000 đều đạt. [3]'),
('3/3 và 0/10','Controller 3/3; ACT TCP E5 cũ 0/10. [3]'),
('15 bài toán','Hòa vốn giờ công: 16n = 120 + 8n. [4]'),
('22,2 tháng','1 tỷ / (3 × 15 triệu), chưa trừ OPEX. [4]')]
for a,b in numbers:
 yl=para('<b>'+a+'</b><br/>'+b,x1,yl,cw,9.65,12.8)-5
yl=section('5 THUẬT NGỮ PHẢI GIẢI THÍCH',x1,yl-2,cw)
terms=[('Action chunking','Một observation dự đoán cả đoạn action.'),('CVAE','Train posterior từ state + target; latent 32. Inference dùng z=0.'),('Imitation learning','Học từ observation/action của demo.'),('Domain randomization','Biến thiên mô phỏng có kiểm soát; cần đo robustness.'),('Sim-to-real','Lệch ảnh, vật lý, động học và timing. [2-3]')]
for a,b in terms:yl=para('<b>'+a+':</b> '+b,x1,yl,cw,9.5,12.5)-4
yr=section('MỞ ĐẦU - KHOẢNG 60 GIÂY',x2,top,cw)
yr=para('“Nhóm EDABK_TriH nghiên cứu robot học gắp-đặt từ dữ liệu để hướng tới giảm công cấu hình khi thay đổi linh kiện. Bài thử hiện tại là Panda trong MuJoCo đặt ba chốt vào khuôn. Nhánh mới dùng MCR trích đặc trưng ảnh nhiều camera, rồi ACT kết hợp trạng thái khớp để dự đoán chuỗi hành động. Nhóm đã có mô phỏng, evaluator và cache dữ liệu; phần nối joint policy vào task và đánh giá closed-loop còn cần hoàn thiện. Chúng em sẽ tách rõ kết quả controller, thử nghiệm ACT cũ và mục tiêu tiếp theo, rồi trình bày điều kiện để pilot tại DENSO.” [1-3]',x2,yr,cw)-11
yr=section('KẾT THÚC - KHOẢNG 30 GIÂY',x2,yr,cw)
yr=para('“Điểm nhóm muốn chứng minh tiếp là policy học thực hiện task với tỷ lệ thành công, chất lượng và thời gian đo được. Nhóm chưa coi few-shot, robot thật hay ROI là kết quả đã đạt. Bước ưu tiên là chốt contract joint, đo rollout và thống nhất robot cùng baseline cell với kỹ sư DENSO.” [1-4]',x2,yr,cw)-11
yr=section('TUYỆT ĐỐI KHÔNG NÓI',x2,yr,cw)
yr=para('“ACT 100%”; “đã few-shot”; “1.000 demo đều đạt”; “loss là mm”; “eval tự động z=0”; “đổi robot là chạy”; “24/7 đã chứng minh”; “15 task = 15 tháng”; “E100 xong”; “0/10 là MCR mới”.',x2,yr,cw,9.8,13)-11
yr=section('TỰ KIỂM TRA - 5 CÂU HỎI',x2,yr,cw)
yr=para('1. Input/output từng khối là gì?<br/>2. Vì sao CVAE train khác inference?<br/>3. Controller khác learned policy ở đâu?<br/>4. Điều gì còn chưa chứng minh?<br/>5. Gate kiểm chứng tiếp theo là gì?',x2,yr,cw,9.5,13)
bottom=min(yl,yr)
assert bottom>103, f'Body overlaps reference area: {bottom}'
c.setStrokeColor(HexColor('#CBD5E1'));c.line(30,97,W-30,97)
foot='''<b>Căn cứ (đường dẫn và link đầy đủ: 08_CHEAT_SHEET.md):</b> R=F:/cfg5_mophong; J=R/local_source_(1); L=R/local_source.<br/>
[1] Chat “Check cfg5_mophong connection”, 16/10, turn 01a142f9-2676-7cd2-96dd-bda02e19979e; R/BAN_GIAO_CODEX_CFG5_MCR_2026-10-13.md:19.<br/>
[2] J/src/models/mcr_act.py:94; J/configs/act/rh20t_all8.json:1; J/src/data/cfg5_masked.py:205.<br/>
[3] J/data/splits/pick_place_finetune_manifest.json:1; L/outputs/controller_evaluation/summary.json:1; R/epoch5_transfer_probe_14120/report.json:1.<br/>
[4] PPTX gốc, slide 2/31/38; phép tính và giả định được phân tích trong 06_GAPS_AND_RISKS.md. Đây là ước tính, chưa phải ROI đo thật.'''
para(foot,30,89,W-60,6.8,9,gray)
c.showPage();c.save()
print({'pdf':str(O/'08_CHEAT_SHEET.pdf'),'body_bottom_pt':bottom,'pages':1})
