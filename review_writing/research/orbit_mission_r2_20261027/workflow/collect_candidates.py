from pathlib import Path
import urllib.request, urllib.parse, concurrent.futures, json, re, csv, time, hashlib, shutil

OUT=Path(__file__).resolve().parent
REPO=Path(r'D:\SKT727\worktrees\constellation_review_v3510_20261026')
R1=Path(r'D:\SKT727\outputs\constellation_orbit_mission_discussion_r1_20261027')
for d in ['discovery','sources','texts','reading_notes','figures']:(OUT/d).mkdir(exist_ok=True)

queries=[
('Q01','satellite constellation orbit design coverage revisit optimization'),
('Q02','satellite constellation station keeping configuration maintenance perturbation'),
('Q03','satellite differential drag constellation power operational constraints'),
('Q04','reconfigurable Earth observation satellite scheduling orbit maneuver'),
('Q05','satellite constellation deployment natural precession mission time'),
('Q06','satellite formation reconfiguration passive safety sequential optimization'),
('Q07','satellite constellation mission recovery spare reconfiguration'),
('Q08','satellite constellation joint orbit trajectory task planning'),
('Q09','satellite constellation design stationkeeping cost lifetime'),
('Q10','satellite maneuver automation operations low thrust')]

def fetch(url,timeout=35):
    req=urllib.request.Request(url,headers={'User-Agent':'ConstellationReviewResearch/1.0 (metadata retrieval)'})
    with urllib.request.urlopen(req,timeout=timeout) as f:return f.read()

def collect(q):
    qid,query=q
    url='https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':query,'rows':25,'select':'DOI,title,author,published,container-title,type,URL,link,abstract'})
    try:
        data=fetch(url)
        (OUT/'discovery'/f'{qid}_crossref.json').write_bytes(data)
        items=json.loads(data)['message']['items']
        return {'id':qid,'query':query,'url':url,'status':'OK','items':items}
    except Exception as e:return {'id':qid,'query':query,'url':url,'status':'ERROR','reason':str(e),'items':[]}

doi_re=re.compile(r'10\.\d{4,9}/[^\s\"<>|,;]+',re.I)
known=set()
for parent in ['review_writing/evidence','review_writing/literature','review_writing/manuscripts/v3.5.9-cn/references']:
    for p in (REPO/parent).rglob('*'):
        if p.suffix.lower() not in ['.csv','.md','.json']:continue
        try:s=p.read_text(encoding='utf-8-sig')
        except Exception:continue
        known.update(x.rstrip('.)];').lower() for x in doi_re.findall(s))

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(collect,queries))
manifest=[{k:v for k,v in x.items() if k!='items'}|{'result_count':len(x['items'])} for x in results]
(OUT/'discovery'/'QUERY_LOG.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
unique={}
for result in results:
    for x in result['items']:
        doi=x.get('DOI','').lower(); title=(x.get('title') or [''])[0]
        if not doi or not re.search(r'satellite|constellation|spacecraft|formation.flying',title,re.I):continue
        if doi not in unique:
            unique[doi]={'doi':doi,'title':title,'year':(x.get('published',{}).get('date-parts') or [['']])[0][0],
                         'venue':'; '.join(x.get('container-title',[])), 'known_in_project':doi in known,
                         'queries':[],'url':x.get('URL',''),'links':x.get('link',[]),'metadata':x}
        unique[doi]['queries'].append(result['id'])
(OUT/'discovery'/'CROSSREF_DEDUP_CANDIDATES.json').write_text(json.dumps(list(unique.values()),ensure_ascii=False,indent=2),encoding='utf-8')
with (OUT/'discovery'/'CROSSREF_DEDUP_CANDIDATES.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['index','doi','title','year','venue','known_in_project','queries','url']);w.writeheader()
    for i,x in enumerate(unique.values(),1):w.writerow({k:(i if k=='index' else ';'.join(x[k]) if k=='queries' else x[k]) for k in w.fieldnames})
print(json.dumps({'queries':manifest,'unique_candidates':len(unique),'new_metadata_candidates':sum(not x['known_in_project'] for x in unique.values())},ensure_ascii=False,indent=2),flush=True)
for i,x in enumerate(unique.values(),1):
    print(f"{i:03d}\t{'OLD' if x['known_in_project'] else 'NEW'}\t{x['year']}\t{x['doi']}\t{x['title']}",flush=True)
