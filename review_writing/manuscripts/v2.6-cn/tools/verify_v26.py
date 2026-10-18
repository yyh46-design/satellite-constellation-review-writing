"""Offline structural checks only; no source access or scientific certification."""
from pathlib import Path
import argparse, csv, hashlib, json, re, xml.etree.ElementTree as ET

def verify(root: Path) -> dict:
    manuscript = root / 'REVIEW_CN_v2.6.md'
    s = manuscript.read_text(encoding='utf-8')
    body, refs = s.split('## 参考文献', 1)
    numbered = [int(n) for n in re.findall(r'^(\d+)\. ', refs, re.M)]
    cited = [int(n) for n in re.findall(r'\[(\d+)\]', body)]
    first = list(dict.fromkeys(cited))
    with (root/'references/REFERENCE_NUMBER_MAP.csv').open(encoding='utf-8-sig', newline='') as f:
        mapping = list(csv.DictReader(f))
    with (root/'references/REFERENCE_INDEX.csv').open(encoding='utf-8-sig', newline='') as f:
        index = list(csv.DictReader(f))
    byn = {int(x['v26']):x['stable_id'] for x in index}
    claim_ids=[]; evidence_mismatches=[]
    for line in body.splitlines():
        m=re.search(r'\[claim:(CN26C\d+)\] \[evidence:([^\]]*)\]',line)
        if not m: continue
        claim_ids.append(m[1]); ids=set(m[2].split(','))
        for n in re.findall(r'\[(\d+)\]',line):
            if byn.get(int(n)) not in ids: evidence_mismatches.append([m[1],int(n)])
    images = re.findall(r'!\[[^\]]*\]\(([^)]+)\)',body)
    for image in images: ET.parse(root/image)
    checks={
        'five_chapters':len(re.findall(r'^## [1-5] ',body,re.M))==5,
        'seven_tables':len(re.findall(r'^\*\*表\d',body,re.M))==7,
        'two_figures':len(images)==2,
        'all_95_sources_cited':set(cited)==set(range(1,96)),
        'first_citation_order':first==list(range(1,96)),
        'reference_list_complete':numbered==list(range(1,96)),
        'source_mapping_95_unique':len(mapping)==95 and len(set(x['stable_source_id'] for x in mapping))==95,
        'source_index_95_unique':len(index)==95 and len(set(byn.values()))==95,
        'claims_unique':len(claim_ids)==151 and len(set(claim_ids))==151,
        'citations_match_evidence_ids':not evidence_mismatches,
    }
    return {'checks':checks,'pass':all(checks.values()),'manuscript_sha256':hashlib.sha256(manuscript.read_bytes()).hexdigest(),'evidence_mismatches':evidence_mismatches,'scientific_verified':False,'human_verified':False,'submission_ready':False}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--out',type=Path)
    a=p.parse_args(); r=verify(a.root.resolve()); out=json.dumps(r,ensure_ascii=False,indent=2); print(out)
    if a.out: a.out.write_text(out+'\n',encoding='utf-8')
    raise SystemExit(0 if r['pass'] else 1)
