from pathlib import Path
import re,json,hashlib,subprocess
from pypdf import PdfReader
O=Path(__file__).parent.parent
docs=sorted(O.glob('*.md'));errors=[];links=0;cache={}
for p in docs:
 t=p.read_text(encoding='utf-8')
 if t.count('## Tự kiểm tra: 5 câu hỏi tôi nên trả lời được')!=1:errors.append(f'{p.name}: missing self-check')
 if t.count('```')%2:errors.append(f'{p.name}: unbalanced fences')
 if re.search(r'\[\[(?:J|L|R|H|A):',t):errors.append(f'{p.name}: unresolved source marker')
 for raw in re.findall(r'\]\(<([A-Z]:/[^>]+)>\)',t):
  links+=1
  m=re.fullmatch(r'(.*?)(?::(\d+))?',raw);path=Path(m[1]);line=int(m[2]) if m[2] else None
  if not path.is_file():errors.append(f'{p.name}: missing link {raw}');continue
  if line:
   if path not in cache:
    with path.open('rb') as f:cache[path]=sum(1 for _ in f)
   if not 1<=line<=cache[path]:errors.append(f'{p.name}: line out of range {raw}; lines={cache[path]}')
qa=(O/'07_QA_BANK.md').read_text(encoding='utf-8')
qids=re.findall(r'^### ([A-J]\d{2})$',qa,re.M)
if len(qids)!=60 or len(set(qids))!=60:errors.append('Q&A count/unique mismatch')
for label in ['Câu hỏi:','Giám khảo muốn kiểm tra:','Trả lời mẫu (30–60 giây):','Bằng chứng/Con số để dẫn:','Đừng nói:','Câu hỏi tiếp theo có thể bị hỏi:']:
 if qa.count('**'+label+'**')!=60:errors.append('Q&A field mismatch '+label)
sl=(O/'05_SLIDE_GUIDE.md').read_text(encoding='utf-8')
slides=[int(x) for x in re.findall(r'^## Slide (\d+)$',sl,re.M)]
expected=[i for i in range(1,44) if i not in {1,3,9,11,20,39,41,43}]
if slides!=expected:errors.append('Content slide coverage mismatch')
for label in ['Slide nói gì:','Ý nghĩa thật:','Bằng chứng:','Trạng thái:','Câu nên nói (không quá 3 câu):','Có thể bị hỏi tiếp:']:
 if sl.count('**'+label+'**')!=35:errors.append('Slide field mismatch '+label)
protected=json.loads((O/'_audit/protected_hashes.json').read_text(encoding='utf-8-sig'))
hash_results=[]
for item in protected:
 got=hashlib.file_digest(open(item['path'],'rb'),'sha256').hexdigest()
 same=got==item['sha256'];hash_results.append({'path':item['path'],'unchanged':same})
 if not same:errors.append('Protected source changed: '+item['path'])
pdf=PdfReader(O/'08_CHEAT_SHEET.pdf')
if len(pdf.pages)!=1:errors.append('Cheat sheet PDF not one page')
pdftext=pdf.pages[0].extract_text()
for term in ['10 MỐC','5 THUẬT NGỮ','MỞ ĐẦU','KẾT THÚC','TUYỆT ĐỐI','TỰ KIỂM TRA']:
 if term not in pdftext:errors.append('PDF missing section '+term)
git='C:/Users/ADMIN/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/git/cmd/git.exe'
status=subprocess.run([git,'-c','safe.directory=F:/cfg5_mophong','-C','F:/cfg5_mophong','status','--short'],capture_output=True,text=True,check=True).stdout
report={'main_markdown_files':len(docs),'source_and_deliverable_links_checked':links,'qa_questions':len(qids),'content_slides':len(slides),'pdf_pages':len(pdf.pages),'pdf_page_size_pt':list(pdf.pages[0].mediabox),'protected_hashes':hash_results,'git_status_final':status,'errors':errors}
(O/'_audit/validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
