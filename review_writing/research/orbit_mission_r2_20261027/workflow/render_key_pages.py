from pathlib import Path
import pdfplumber,json
p=Path(__file__).resolve().parent
items={'N001_ROGERS':[25],'N002_PEARL':[26,30,31],'N006_MAINTENANCE':[14,15],'N008_ZHAO':[5,6],'N009_SDDIP':[20,23,30],'N010_FOSTER':[11,12,13]}
out=[]
for stem,pages in items.items():
 with pdfplumber.open(p/'sources'/f'{stem}.pdf') as pdf:
  for n in pages:
   f=p/'figures'/f'{stem}_p{n}.png'
   pdf.pages[n-1].to_image(resolution=110).save(f)
   out.append(str(f))
(p/'figures'/'RENDER_MANIFEST.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(len(out),'pages rendered')
