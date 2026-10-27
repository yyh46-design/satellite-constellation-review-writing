from pathlib import Path
import urllib.request, json, hashlib, concurrent.futures, shutil
from pypdf import PdfReader

OUT=Path(__file__).resolve().parent
R1=Path(r'D:\SKT727\outputs\constellation_orbit_mission_discussion_r1_20261027')
sources=[
('N001_ROGERS','https://arxiv.org/pdf/2507.09855v2',None),
('N002_PEARL','https://arxiv.org/pdf/2507.10394v3',None),
('N003_CMAS','https://publications.spaceops.org/2025/download_by_id.php?id=0105',None),
('N004_HULL','https://ntrs.nasa.gov/api/citations/20170010724/downloads/20170010724.pdf',R1/'source_copies/HULL2017_NASA.pdf'),
('N005_GAIAS','https://slab.sites.stanford.edu/sites/g/files/sbiybj25201/files/media/file/jgcd2015_gaiasdamico.pdf',R1/'source_copies/GAIAS2015_STANFORD.pdf'),
('N006_MAINTENANCE','https://mdpi-res.com/d_attachment/applsci/applsci-15-04640/article_deploy/applsci-15-04640.pdf',None)]

def acquire(row):
    sid,url,local=row
    target=OUT/'sources'/f'{sid}.pdf'
    record={'id':sid,'url':url}
    try:
        if local and local.exists():shutil.copy2(local,target)
        elif not target.exists():
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=50) as f, target.open('wb') as out:
                while chunk:=f.read(262144):out.write(chunk)
        reader=PdfReader(target)
        if not reader.pages:raise ValueError('no_pages')
        pages=[]
        for n,page in enumerate(reader.pages,1):
            pages.append(f'\n\n===== PDF PAGE {n} =====\n'+(page.extract_text() or ''))
        (OUT/'texts'/f'{sid}.txt').write_text(''.join(pages),encoding='utf-8')
        data=target.read_bytes()
        record.update(status='FULL_PDF_ACQUIRED_NOT_YET_READ',pages=len(reader.pages),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    except Exception as e:record.update(status='ACCESS_OR_PARSE_FAILED',reason=str(e))
    print(json.dumps(record,ensure_ascii=False),flush=True)
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(acquire,sources))
(OUT/'SOURCE_ACQUISITION.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
