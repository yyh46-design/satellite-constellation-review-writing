"""Audit B20 provenance and counts. This does not validate scientific claims.

Run: python -X utf8 tools/verify_batch.py --write-report
Local article captures are not published. Absent captures are reported as unavailable;
use --require-local-captures to require their presence on the originating workstation.
"""
import argparse, collections, csv, hashlib, json, re, subprocess
from pathlib import Path

B=Path(__file__).resolve().parents[1]
R=B.parents[3]
BASE='51246eb38517c02c877f46e0e4463a494005d1cf'
EXPECTED={'L019','L024','L042','L043','L049','L050','L063'}
PENDING={'L029','L052','L072'}
checks=[]; unavailable=[]; capture_count=0
def ck(value,label):
 if not value: raise AssertionError(label)
 checks.append(label)
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def cr(p):
 with p.open(encoding='utf-8-sig',newline='') as f: return list(csv.DictReader(f))
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def git(*args,input=None): return subprocess.check_output(['git',*args],input=input,cwd=R)
def local_file(path,expected):
 global capture_count
 p=Path(path)
 if not p.is_file(): unavailable.append(path); return False
 ck(sha(p)==expected,'local hash '+p.name); capture_count+=1; return True

parser=argparse.ArgumentParser(); parser.add_argument('--write-report',action='store_true'); parser.add_argument('--require-local-captures',action='store_true'); args=parser.parse_args()
ck((R/'.git').exists(),'repository root discovered')
status=read(B/'BATCH_STATUS.json'); docs=read(B/'READING_CONTENT.json'); sources=read(B/'SOURCE_MANIFEST_B20.json')['sources']; claims=cr(B/'CLAIM_EVIDENCE_B20.csv'); pending=read(B/'UNAVAILABLE_FULLTEXT.json')
ck({s['pool_id'] for s in sources}==EXPECTED and len(sources)==7,'seven distinct original-pool sources')
ck({d['reading_id'] for d in docs}==EXPECTED and len(docs)==7,'seven structured notes')
ck({x['pool_id'] for x in pending}==PENDING and len(pending)==3,'three uncompleted access records')
ck(status['batch_target']==10 and status['completed_body_read_count']==7 and status['unavailable_fulltext_not_counted']==3,'target10 is separate from completed7')
ck(set(status['close_read_ids'])==EXPECTED and set(status['unavailable_fulltext_ids'])==PENDING,'status identifiers agree')
ck(status['original_pool_close_read_cumulative']==37 and status['original_pool_remaining']==43,'original pool 37 completed and 43 remaining')
ck(status['topic_supplement_close_read_cumulative']==60 and status['B11_through_B20_close_read_records']==97,'supplements60 and completed97')
ck(status['claim_count']==35 and status['B11_through_B20_claim_records']==450,'35 new and 450 cumulative claims')
ck(status['pdf_binary_archived_count']==status['pdf_binary_identity_verified_count']==status['actual_visual_page_count']==0,'no binary or image review credit')
ck(not status['human_verified'] and not status['submission_ready'] and not status['manuscript_modified'],'scientific and manuscript boundaries retained')
ck(len(claims)==35 and [c['claim_id'] for c in claims]==[f'C-B20-{n:03d}' for n in range(1,36)],'35 unique ordered claim identifiers')
ck(len({s['identifier'].lower() for s in sources})==7,'DOIs are distinct')
ck(sum(s['pdf_pages'] for s in sources)==status['remote_pdf_total_pages']==140,'seven PDFs total140 physical pages')
byid={s['pool_id']:s for s in sources}; csvclaims={c['claim_id']:c for c in claims}
for d in docs:
 sid=d['reading_id']; s=byid[sid]; identity=read(B/'metadata'/(sid+'_IDENTITY.json')); m=read(B/'metadata'/(sid+'_CROSSREF.json'))
 ck(m['DOI'].lower()==s['identifier'].lower()==d['identifier'].lower(),sid+' DOI identity')
 ck(m['title'][0]==s['title']==d['title'],sid+' formal title identity')
 ck(m['published']['date-parts'][0][0]==s['bibliographic_year']==d['bibliographic_year'],sid+' publication year')
 ck(identity['actual_version']==s['actual_version']==d['actual_version'] and not identity['formal_version_text_compared'],sid+' version boundary')
 ck(not s['source_pdf_archived'] and s['source_pdf_sha256'] is None and not s['source_pdf_byte_identity_verified'] and not s['source_fulltext_committed_to_git'],sid+' no PDF byte identity claim')
 ck(not s['human_verified'] and s['verification_status']=='human_pending',sid+' human review pending')
 note=(B/s['notes_path']).read_text(encoding='utf-8')
 ck(d['question'] in note and d['mechanism'] in note and d['validation'] in note and d['writing_use'] in note,sid+' note matches structured content')
 ck(all(x in note for x in d['limitations']),sid+' limitations retained')
 ck(len(d['claims'])==5,sid+' five claims')
 if local_file(s['local_text_capture_path'],s['local_text_capture_sha256']):
  lines=read(Path(s['local_text_capture_path']))
  ck({x['line'] for x in lines}==set(range(s['web_total_extracted_lines'])),sid+' complete extracted-line capture')
  ck(all(1<=x['pdf_page']<=s['pdf_pages'] for x in lines),sid+' physical page mapping')
 ck(s['web_extracted_line_capture_coverage']==1.0,sid+' capture coverage refers to extracted text')
 for f in s['capture_files']: local_file(f['local_path'],f['sha256'])
 for c in d['claims']:
  h=hashlib.sha256(' '.join(c['text'].split()).encode()).hexdigest(); cc=csvclaims[c['claim_id']]
  ck(h==c['claim_text_sha256']==cc['claim_text_sha256'] and cc['claim_text']==c['text'],c['claim_id']+' exact text hash')
  ck(c['text'] in note and c['claim_id'] in note and c['locator'] in note,c['claim_id']+' visible note and locator')
  ck(c['pages'] and all(1<=p<=s['pdf_pages'] for p in c['pages']) and cc['pdf_physical_pages']==';'.join(map(str,c['pages'])),c['claim_id']+' physical page range')
  ck(cc['pool_id']==sid and cc['source_id']==s['source_id'] and cc['human_verified']=='False',c['claim_id']+' source and review state')

correction=read(B/'metadata/L043_CORRECTION_IDENTITY.json'); cm=read(B/'metadata/L043_CORRECTION_CROSSREF.json')
ck(correction['identifier'].lower()==cm['DOI'].lower()=='10.2514/1.g006630.c1','correction DOI')
ck(cm['update-to'][0]['DOI'].lower()==byid['L043']['identifier'].lower(),'correction is paired with original')
ck(correction['affected_original_equations']==['35','36','41','42','64','74'],'correction scope retained')
ck(correction['physical_pages']==2 and correction['all_extracted_lines_read']==110 and not correction['counted_as_additional_paper'],'correction two pages and no added paper credit')
ck(cm['published-print']['date-parts'][0][0]==2023 and cm['update-to'][0]['updated']['date-parts'][0][0]==2022,'issue and correction dates remain distinct')
if local_file(correction['local_text_capture_path'],correction['local_text_capture_sha256']):
 t=Path(correction['local_text_capture_path']).read_text(encoding='utf-8')
 ck({int(x) for x in re.findall(r'^L(\d+)@P',t,re.M)}==set(range(110)),'all110 correction extracted lines present')
ck(byid['L042']['bibliographic_year']==2026 and '2025' in byid['L042']['actual_version'],'L042 preprint versus formal-year difference retained')
for x in pending:
 ck(not x['body_read'] and not x['counted_as_completed'] and x['claim_count']==0,x['pool_id']+' uncompleted with zero claims')
 ck(x['pool_id'] not in {c['pool_id'] for c in claims},x['pool_id']+' excluded from claim table')
 if x['local_failure_capture']: local_file(x['local_failure_capture'],x['local_failure_capture_sha256'])

rows=cr(B/'READING_STATUS_80_AFTER_B20.csv'); previous=cr(B.parent/'B19_20261021/READING_STATUS_80_AFTER_B19.csv')
ck(len(rows)==80 and {r['pool_id'] for r in rows}=={f'L{n:03d}' for n in range(1,81)},'80-row original pool snapshot')
counts=collections.Counter(r['reading_status'] for r in rows)
ck(counts=={'AI_BODY_CLOSE_READ_COMPLETE':37,'NOT_CLOSE_READ':42,'PARTIAL_TEXT_READ_NOT_COUNTED':1},'80-row statuses reconcile')
ck({r['pool_id'] for r,p in zip(rows,previous) if r['reading_status']!=p['reading_status']}==EXPECTED,'only seven original-pool completion transitions')
ck(all(r['reading_status']=='NOT_CLOSE_READ' for r in rows if r['pool_id'] in PENDING),'pending three remain subset of42 uncompleted')
ck(next(r for r in rows if r['pool_id']=='L003')['reading_status']=='PARTIAL_TEXT_READ_NOT_COUNTED','L003 remains partial')
supp=cr(B/'SUPPLEMENT_READING_REGISTER_B20.csv'); prevsupp=cr(B.parent/'B19_20261021/SUPPLEMENT_READING_REGISTER_B19.csv')
ck(len(supp)==60 and {r['supplement_id'] for r in supp}=={f'S{n:03d}' for n in range(1,61)},'60 supplements unchanged')
ck([{k:v for k,v in r.items() if k!='note_path'} for r in supp]==[{k:v for k,v in r.items() if k!='note_path'} for r in prevsupp],'supplement data preserved except relative path')
for r in rows+supp:
 if r['note_path']: ck((B/r['note_path']).is_file(),'note resolves '+r.get('pool_id',r.get('supplement_id')))
dedup=read(B/'DEDUP_CHECK.json')
ck(dedup['prior_B11_through_B19_source_records_checked']==90 and not dedup['prior_body_read_matches'],'no duplicate of90 prior source records')
ck(len(dedup['registers'])==4 and dedup['new_supplement_count']==0,'four registration sources checked')
for reg in dedup['registers']: local_file(reg['path'],reg['sha256'])
oldcounts=read(B.parent/'B19_20261021/BATCH_STATUS.json')
ck(oldcounts['original_pool_close_read_cumulative']+7==37 and oldcounts['B11_through_B19_claim_records']+35==450,'cumulative deltas agree with B19')

frozen=read(B/'FROZEN_BASELINE_SHA256.json'); ck(frozen['base_commit']==BASE and frozen['prior_batch_file_count']==660,'660 prior batch files frozen')
for p,h in frozen['frozen_files'].items():
 actual=sha(R/p)
 ck(actual==h or (p in frozen['checkout_CRLF_normalization_paths'] and actual==frozen['git_blob_sha256'][p]),'frozen checkout '+p)
specs=''.join(BASE+':'+p+'\n' for p in frozen['git_blob_sha256']).encode(); raw=git('cat-file','--batch',input=specs); off=0
for p,h in frozen['git_blob_sha256'].items():
 end=raw.index(b'\n',off); size=int(raw[off:end].split()[-1]); content=raw[end+1:end+1+size]; off=end+size+2
 ck(hashlib.sha256(content).hexdigest()==h,'Git baseline '+p)
 ck(content==(R/p).read_bytes().replace(b'\r\n',b'\n') if p in frozen['checkout_CRLF_normalization_paths'] else content==(R/p).read_bytes(),'Git checkout normalization '+p)
ck(frozen['manuscript_sha256']=='c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15','frozen v3.2 manuscript hash')
prefix=B.relative_to(R).as_posix()+'/'
changed=git('diff','--name-only',BASE).decode().splitlines()
ck(all(p.startswith(prefix) for p in changed),'tracked changes confined to B20')
for p in B.rglob('*'):
 if p.is_file():
  ck(p.suffix.lower() not in {'.pdf','.html','.raw'},'no source fulltext binary '+p.name)
  ck(b'\r\n' not in p.read_bytes(),'LF package bytes '+p.name)
if args.require_local_captures: ck(not unavailable,'all local captures available')
manifest_path=B/'SHA256_MANIFEST.json'
if not args.write_report:
 manifest=read(manifest_path)
 actual={p.relative_to(B).as_posix():sha(p) for p in B.rglob('*') if p.is_file() and p!=manifest_path}
 ck(actual==manifest['files'],'complete package SHA256 manifest')
if args.write_report:
 report=dict(batch='B20_20261021',result='PASS',scope='File identity, evidence bindings, counts, baseline preservation; not scientific or visual approval',check_count=len(checks),completed_sources=7,uncompleted_fulltext=3,new_claims=35,prior_batch_files_verified=660,frozen_files_verified=len(frozen['frozen_files']),local_provenance_files_verified=capture_count,local_provenance_files_unavailable=unavailable,original_pool_completed=37,original_pool_remaining=43,supplement_completed=60,human_verified=False,submission_ready=False)
 dump(B/'VALIDATION_REPORT.json',report)
 files={p.relative_to(B).as_posix():sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p!=manifest_path}
 dump(manifest_path,dict(batch='B20_20261021',algorithm='SHA256',file_count=len(files),files=files,scope='All package files except this self-referential manifest; this is not a source-PDF identity manifest'))
print(json.dumps(dict(result='PASS',checks=len(checks),completed=7,uncompleted=3,claims=35,local_provenance_files_verified=capture_count,local_provenance_files_unavailable=len(unavailable),human_verified=False),ensure_ascii=False))
