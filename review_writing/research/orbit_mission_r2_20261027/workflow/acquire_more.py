from pathlib import Path
import urllib.request,json,hashlib,concurrent.futures
from pypdf import PdfReader
OUT=Path(__file__).resolve().parent
rows=[
('N007_MCGRATH','https://strathprints.strath.ac.uk/71130/1/McGrath_Macdonald_JGCD_2020_General_perturbation_method_for_satellite_constellation_deployment.pdf'),
('N008_ZHAO','https://mdpi-res.com/d_attachment/sensors/sensors-24-00631/article_deploy/sensors-24-00631.pdf'),
('N009_SDDIP','https://arxiv.org/pdf/2608.09738v1'),
('N010_FOSTER','https://arxiv.org/pdf/1806.01218v1')]
def get(row):
 sid,url=row; dest=OUT/'sources'/f'{sid}.pdf'; rec={'id':sid,'url':url}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=50) as response,dest.open('wb') as f:
   while chunk:=response.read(262144):f.write(chunk)
  pdf=PdfReader(dest)
  (OUT/'texts'/f'{sid}.txt').write_text(''.join(f'\n\n===== PDF PAGE {i} =====\n'+(p.extract_text() or '') for i,p in enumerate(pdf.pages,1)),encoding='utf-8')
  rec.update(status='FULL_PDF_ACQUIRED_NOT_YET_READ',pages=len(pdf.pages),bytes=dest.stat().st_size,sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
 except Exception as e:rec.update(status='ACCESS_OR_PARSE_FAILED',reason=str(e))
 print(json.dumps(rec),flush=True);return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(get,rows))
(OUT/'SOURCE_ACQUISITION_MORE.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
