from pathlib import Path
import concurrent.futures, urllib.request, urllib.parse, json, time, re, html

ROOT = Path(__file__).resolve().parent
selection = json.loads((ROOT / 'CANDIDATE_SELECTION_v0.7.json').read_text(encoding='utf-8'))['selected']

def fetch(row):
    doi = row['DOI']
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='')
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'LocalManuscriptBibliographyCheck/0.7'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.load(resp)['message']
            if data['DOI'].lower() != doi.lower():
                raise ValueError('DOI identity mismatch')
            abstract = html.unescape(re.sub('<[^>]+>', ' ', data.get('abstract','')))
            abstract = re.sub(r'\s+', ' ', abstract).strip()
            return {'id':row['ID'], 'doi':doi, 'retrieved_on':'2026-10-10', 'registry_url':url, 'metadata':data, 'registered_abstract':abstract, 'status':'retrieved'}
        except Exception as exc:
            if attempt == 2:
                return {'id':row['ID'],'doi':doi,'status':'unavailable','error':str(exc)}
            time.sleep(2 + attempt * 3)

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
    for item in ex.map(fetch, selection):
        results.append(item)
        (ROOT / 'BIBLIOGRAPHY_ADDITIONS_METADATA_v0.7.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        if len(results) % 10 == 0:
            print(f'Retrieved {len(results)}/{len(selection)}; abstracts {sum(bool(r.get("registered_abstract")) for r in results)}',flush=True)
print(json.dumps({'total':len(results),'retrieved':sum(r['status']=='retrieved' for r in results),'abstracts':sum(bool(r.get('registered_abstract')) for r in results)},ensure_ascii=False),flush=True)
