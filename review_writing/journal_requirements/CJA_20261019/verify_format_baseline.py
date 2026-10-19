"""Read-only checks for the CJA format record; no submission or manuscript rewriting."""
from pathlib import Path
import argparse,csv,hashlib,json,re,subprocess

BASE='922d3d18653ac65a5bafc4e9e3adfb9fc425d091'
PREFIX='review_writing/journal_requirements/CJA_20261019/'
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[3]);p.add_argument('--git',default='git')
p.add_argument('--materials',type=Path);p.add_argument('--manifest-check',action='store_true');p.add_argument('--output',type=Path)
a=p.parse_args();R=a.repo;D=R/PREFIX;checks=[]
def git(*args,input=None):return subprocess.run([a.git,'-C',str(R),*args],input=input,capture_output=True,check=True).stdout
def sha(b):return hashlib.sha256(b).hexdigest()
def get(n):return json.loads((D/n).read_text(encoding='utf-8'))
def ck(n,t):
 assert t,n
 checks.append({'check':n,'pass':True})

rules=get('FORMAT_RULES.json');profile=get('PROJECT_STYLE_PROFILE.json');src=get('SOURCE_ACCESS_REGISTER.json')
ck('26_unique_rules',len(rules['rules'])==26 and len({x['id'] for x in rules['rules']})==26)
ck('evidence_levels_explicit',all(x['evidence_level'] in {'official_template_instruction','official_template_normal_guidance','official_template_example','official_template_observation','publisher_general_guidance','official_form_observation','project_working_choice'} for x in rules['rules']))
ck('not_human_or_submission_approval',rules['human_verified'] is False and rules['submission_authorized'] is False and all(x['human_verified'] is False for x in rules['rules']))
ck('journal_specific_width_and_font',profile['submission_figures']['widths_cm']==[7.5,15] and profile['submission_figures']['font_pt_at_final_size']==7.5)
ck('no_graph_count_or_highlights_claim',profile['graph_count_requirement'] is None and profile['highlights_required']=='unconfirmed' and profile['graphical_abstract_required']=='unconfirmed')
ck('source_downloads_success',len(src['sources'])==9 and all(x['download_success'] for x in src['sources']))
docx=[x for x in src['sources'] if x['file'].endswith('.docx')]
ck('four_template_urls_identical_bytes',len(docx)==4 and {x['sha256'] for x in docx}=={rules['official_template_sha256']} and len({x['url'] for x in docx})==4)
ck('five_source_pages_actually_viewed',src['template_pages_visually_reviewed']==[1,2,3,4,5])
with (D/'V27_FORMAT_GAP_CHECK.csv').open(encoding='utf-8-sig',newline='') as f:gaps=list(csv.DictReader(f))
ck('12_current_draft_items',len(gaps)==12 and len({x['id'] for x in gaps})==12)
md=(R/'review_writing/manuscripts/v2.7-cn/REVIEW_CN_v2.7.md').read_text(encoding='utf-8')
ab=re.sub(r'<!--.*?-->','',md.split('## Abstract\n',1)[1].split('**Keywords',1)[0])
kw=next(s for s in md.splitlines() if s.startswith('**Keywords:**')).split('**Keywords:**',1)[1].strip().split(';')
ck('current_171_words_6_keywords_95_sources',len(ab.split())==171 and len(kw)==6 and len(re.findall(r'^\d+\. ',md.split('## 参考文献\n',1)[1],re.M))==95)

# Verify all baseline files by Git blob content, allowing only checkout LF/CRLF expansion.
tree=[]
for rec in git('ls-tree','-rz',BASE).split(b'\0'):
 if not rec:continue
 meta,path=rec.split(b'\t',1);mode,typ,oid=meta.split();assert typ==b'blob';tree.append((oid.decode(),path.decode('utf-8')))
data=git('cat-file','--batch',input=('\n'.join(oid for oid,path in tree)+'\n').encode());pos=0;hist=[]
for oid,path in tree:
 end=data.index(b'\n',pos);size=int(data[pos:end].split()[2]);blob=data[end+1:end+1+size];pos=end+size+2;current=(R/path).read_bytes()
 ck('unchanged_'+path,current==blob or (b'\0' not in current and current.replace(b'\r\n',b'\n')==blob))
 hist.append({'path':path,'blob_sha256':sha(blob)})
ck('batch_consumed',pos==len(data))
changed=git('diff','--name-only',BASE).decode('utf-8').splitlines()+git('ls-files','--others','--exclude-standard').decode('utf-8').splitlines()
ck('new_format_directory_only',all(x.startswith(PREFIX) for x in changed))
ck('no_source_or_binary_uploads',not any(p.suffix.lower() in {'.doc','.docx','.pdf','.png','.zip','.pyc'} for p in D.rglob('*') if p.is_file()))
if a.materials:
 for x in src['sources']:ck('original_download_hash_'+x['file'],sha((a.materials/x['file']).read_bytes())==x['sha256'])
 inspection=json.loads((a.materials/'WORD_NATIVE_INSPECTION.json').read_text(encoding='utf-8-sig'))
 ck('read_only_source_inspection',all(x['read_only'] is True and x['source_saved'] is False for x in inspection))
 ck('five_rendered_source_pages',all((a.materials/f'template_page_{i}.png').is_file() for i in range(1,6)))
if a.manifest_check:
 m=get('SHA256_MANIFEST.json');byname={x['path']:x for x in m['files']};files={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 ck('exact_manifest_file_set',set(byname)==files)
 for name,h in byname.items():ck('manifest_'+name,sha((D/name).read_bytes())==h['sha256'] and (D/name).stat().st_size==h['bytes'])
res={'status':'PASS','date_client':'2026-10-19','scope':'格式来源、版本身份、现状数量及历史不变性；不是完整投稿合规或人工科学验收','baseline_commit':BASE,'baseline_files_checked':len(hist),'historical_digest':sha(json.dumps(hist,separators=(',',':')).encode()),'checks_passed':len(checks),'checks':checks,'manuscript_changed':False,'figures_changed':False,'new_whole_paper_readings':0,'human_verified':False,'submission_authorized':False}
if a.output:a.output.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in res.items() if k!='checks'},ensure_ascii=True,indent=2))
