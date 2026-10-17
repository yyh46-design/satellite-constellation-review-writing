"""Read-only structural/provenance checks; never a scientific acceptance test."""
from pathlib import Path
import argparse, csv, difflib, hashlib, json, re, subprocess, sys, zipfile
import xml.etree.ElementTree as ET

BASE='78f0e1b2eca09ed7c8df54c9021b3d75d45e58a3'
FROZEN='51be6a1326e8c615ea24f80f1887f16a2e7b02fc'
PREFIX='review_writing/manuscripts/v2.2-cn/'
REMOVED={29,31,32,33,38,40,43,45,46,54,55,56,59,60,63,64,67,68,69,70,75,77,79,80,83,90,94,99,100,103,104,110,112,118}
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[4])
ap.add_argument('--git',default='git')
ap.add_argument('--word',type=Path)
ap.add_argument('--manifest-check',action='store_true')
ap.add_argument('--output',type=Path,help='optional JSON receipt path; no other writes')
a=ap.parse_args();R=a.repo;D=R/PREFIX
def git(*args,input=None):
    return subprocess.run([a.git,'-C',str(R),*args],input=input,capture_output=True,check=True).stdout
def sha(b): return hashlib.sha256(b).hexdigest()
def get(n): return json.loads((D/n).read_text(encoding='utf-8'))
def csvget(n):
    with (D/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
checks=[]
def ck(name,truth,detail=None):
    assert truth, f'{name}: {detail}'
    checks.append({'check':name,'pass':True,**({'detail':detail} if detail is not None else {})})
def clean(s): return re.sub(r'\s*<!--.*?-->','',s).strip()
def norm(s): return re.sub(r'\s+',' ',s.replace('\u2060','').replace('\u00a0',' ')).strip()
def inline(s):
    s=re.sub(r'\[([^\]]+)\]\((https?://[^\s]+)\)',lambda m:m[1],s)
    return norm(s.replace('**',''))

md=(D/'REVIEW_CN_v2.2.md').read_text(encoding='utf-8')
body,bib=md.split('\n## 参考文献\n',1)
S=get('REVISION_SCOPE_AND_COUNTS.json');M=get('SOURCE_MANIFEST_v2.2.json')
sources=M['sources']; byid={s['evidence_id']:s for s in sources}
rows=csvget('REFERENCE_NUMBER_MAP.csv');crows=csvget('CLAIM_EVIDENCE_MAP.csv')
refmap={int(r['稳定来源键']):int(r['新v2.2编号']) for r in rows if r['新v2.2编号']}
ck('source_count',len(sources)==94 and len(byid)==94)
ck('academic_and_engineering_counts',sum(s['kind']=='academic' for s in sources)==84 and sum(s['kind']=='engineering' for s in sources)==10)
ck('reading_basis_counts',sum(s['reading_basis']=='historical_targeted_body_passages' for s in sources)==77 and sum(s['reading_basis']=='B10_targeted_method_and_evaluation_body' for s in sources)==7)
ck('no_abstract_only_academic_basis',all(s['reading_basis'] in {'historical_targeted_body_passages','B10_targeted_method_and_evaluation_body'} for s in sources if s['kind']=='academic'))
ck('explicit_128_identity_map',len(rows)==128 and {int(x['稳定来源键']) for x in rows}==set(range(1,129)))
ck('exact_34_removed', {int(r['稳定来源键']) for r in rows if not r['新v2.2编号']}==REMOVED)
ck('retained_stable_ids',set(refmap)=={int(s['source_key']) for s in sources} and not (set(refmap)&REMOVED))
ck('source_identity_to_number',all(refmap[s['source_key']]==s['new_reference_number'] for s in sources))
seen=list(dict.fromkeys(map(int,re.findall(r'\[(\d+)\]',re.sub(r'<!--.*?-->','',body)))))
ck('first_appearance_order',seen==list(range(1,95)))
entries=re.findall(r'^(\d+)\. (.+)$',bib,re.M)
ck('complete_bibliography', [int(x[0]) for x in entries]==list(range(1,95)))
entries=dict((int(n),t) for n,t in entries)
ck('no_orphan_references',set(entries)==set(seen))
ck('bibliography_identity',all(entries[s['new_reference_number']]==s['bibliography_entry'] for s in sources))
for s in sources:
    if s.get('doi'):ck('doi_in_entry_'+s['evidence_id'],s['doi'].lower() in s['bibliography_entry'].lower())
ck('full_body_claims_are_mapped',len(crows)==132 and len({r['claim_id'] for r in crows})==132)
for r in crows:
    line=md.splitlines()[int(r['line'])-1];t=clean(line)
    ck('claim_hash_'+r['claim_id'],sha(t.encode())==r['text_sha256'])
    refs=list(dict.fromkeys(map(int,re.findall(r'\[(\d+)\]',t))))
    ck('claim_refs_'+r['claim_id'],';'.join(map(str,refs))==r['explicit_new_reference_numbers'])
    ids=r['evidence_ids'].split(';')
    ck('claim_sources_'+r['claim_id'],set(ids)<=set(byid) and all(f'E{x:03}' not in ids for x in REMOVED))
    ck('claim_reference_identity_'+r['claim_id'],set(refs)<={byid[x]['new_reference_number'] for x in ids})
    ck('not_human_verified_'+r['claim_id'],r['human_verified']=='False')
ck('no_unmapped_claim_tags',set(re.findall(r'\[claim:([^\]]+)\]',body))=={r['claim_id'] for r in crows})
reg=get('REVISION_REGISTER_CN.json')['rewritten_or_added_blocks']
ck('rewrite_and_add_counts',sum(x['action']=='rewrite' for x in reg)==35 and sum(x['action']=='add' for x in reg)==9)
ck('chapter_table_figure_counts',len(re.findall(r'^## [1-5] ',body,re.M))==5 and len(re.findall(r'^\*\*表\d',body,re.M))==7 and len(re.findall(r'^!\[',body,re.M))==2)
for p in (D/'assets').glob('*.svg'):
    ck('svg_citations_'+p.name,set(map(int,re.findall(r'\[(\d+)\]',p.read_text(encoding='utf-8'))))<=set(entries))
ck('no_unread_algorithm_labels',not any(x in body for x in ['DRL-LNS','NIMBUS','RPRS','branch-and-price']))
ck('scope_stats_match',S['reference_count']==94 and S['academic_references']==84 and S['claim_blocks']==132 and S['manuscript_md_sha256']==sha((D/'REVIEW_CN_v2.2.md').read_bytes()))
ck('reading_counts_not_inflated',S['new_full_paper_readings_this_turn']==0 and S['original_targeted_academic_count_unchanged']==77 and S['original_academic_remaining_count_unchanged']==34 and S['B10_catalog_external_reads_unchanged']==10)
ck('no_gap_or_version_pair_closure',S['original_fulltext_gaps_closed']==0 and S['formal_version_pairs_closed']==0)
ck('draft_status',S['human_verified'] is False and S['submission_ready'] is False and all(s['human_verified'] is False for s in sources))
ck('english_sync_boundary',S['English_abstract_synchronized'] is True and S['English_full_manuscript_synchronized'] is False)
ck('core_recheck_scope',{x['original_reference'] for x in get('CORE_PASSAGE_RECHECK_20261017.json')['records']}=={18,71,96})
AD=get('B10_ADOPTION_REGISTER.json')
ck('seven_new_external_sources',{x['stable_key'] for x in AD['selected'] if x['stable_key']>121}==set(range(122,129)))
ck('existing_119_not_duplicated',sum(s['source_key']==119 for s in sources)==1 and any(x['candidate_id']=='ALT08' and x['decision']=='reuse_existing_119' for x in AD['selected']))
ck('b10_excluded_candidates',{x['candidate_id'] for x in AD['not_adopted']}=={'ALT04','ALT05','ALT07'})

# Read every historical blob in a single batch; compare bytes, not only Git status.
tree=[]
for record in git('ls-tree','-rz',BASE).split(b'\0'):
    if not record:continue
    meta,path=record.split(b'\t',1);mode,typ,oid=meta.split()
    assert typ==b'blob'
    tree.append((oid.decode(),path.decode('utf-8')))
ck('baseline_path_count',len(tree)==449)
data=git('cat-file','--batch',input=('\n'.join(oid for oid,p in tree)+'\n').encode())
pos=0;hist=[];checkout_eol=[]
for oid,path in tree:
    end=data.index(b'\n',pos);header=data[pos:end].split();size=int(header[2]);blob=data[end+1:end+1+size];pos=end+size+2
    assert (R/path).is_file()
    current=(R/path).read_bytes();same=current==blob
    normalized=(not same and b'\0' not in current and current.replace(b'\r\n',b'\n')==blob)
    ck('immutable_history_content_'+path,same or normalized)
    if normalized:checkout_eol.append(path)
    hist.append({'path':path,'git_blob_sha256':sha(blob),'checkout_sha256':sha(current),'checkout_eol_only':normalized})
ck('batch_consumed_exactly',pos==len(data))
v19path='review_writing/manuscripts/v1.9/REVIEW_CN_v1.9.md'
frozenhash=sha(git('show',FROZEN+':'+v19path))
v19current=(R/v19path).read_bytes()
ck('frozen_v19_git_content',sha(v19current)==frozenhash or sha(v19current.replace(b'\r\n',b'\n'))==frozenhash)
old=git('show',BASE+':review_writing/manuscripts/v2.1-cn/REVIEW_CN_v2.1.md').decode('utf-8')
expected_diff=''.join(difflib.unified_diff(old.splitlines(keepends=True),md.splitlines(keepends=True),fromfile='v2.1-cn/REVIEW_CN_v2.1.md',tofile='v2.2-cn/REVIEW_CN_v2.2.md'))
ck('saved_unified_diff_is_exact',(D/'CHANGES_FROM_v2.1.diff').read_text(encoding='utf-8')==expected_diff)

# A portable, independent Markdown/OOXML content comparison; no Word import needed.
word_details=None
if a.word:
    W={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
    def tag(n):return '{'+W['w']+'}'+n
    expected=[];ls=[clean(x) for x in md.splitlines()];i=0
    while i<len(ls):
        s=ls[i];i+=1
        if not s or s.startswith('!['):continue
        if s.startswith('|'):
            table=[];i-=1
            while i<len(ls) and ls[i].startswith('|'):
                row=ls[i];i+=1
                if re.match(r'^\|\s*-',row):continue
                table.append([inline(x.strip()) for x in row.strip('|').split('|')])
            expected.append(['table',table]);continue
        expected.append(['p',inline(re.sub(r'^#{1,4} ','',s))])
    with zipfile.ZipFile(a.word) as z:
        root=ET.fromstring(z.read('word/document.xml'));actual=[]
        for el in root.find('w:body',W):
            if el.tag==tag('p'):
                t=norm(''.join(x.text or '' for x in el.iter(tag('t'))))
                if t:actual.append(['p',t])
            elif el.tag==tag('tbl'):
                actual.append(['table',[[norm(''.join(t.text or '' for t in cell.iter(tag('t')))) for cell in row.findall('w:tc',W)] for row in el.findall('w:tr',W)]])
        ck('word_complete_text_and_tables_equal_markdown',actual==expected,{'expected_blocks':len(expected),'actual_blocks':len(actual)})
        pics=root.findall('.//wp:docPr',W)
        ck('word_figures_and_alt_text',len(pics)==2 and all(p.get('descr') and p.get('title') for p in pics))
        tabs=root.findall('.//w:tbl',W)
        ck('word_tables_and_repeat_headers',len(tabs)==7 and all(t.find('w:tr/w:trPr/w:tblHeader',W) is not None for t in tabs))
        ck('word_continuous_reference_bookmarks',len(root.findall('.//w:bookmarkStart',W))==94)
        ck('word_no_tracked_edits_or_comments',not root.findall('.//w:ins',W) and not root.findall('.//w:del',W) and not any('comments.xml' in n for n in z.namelist()))
    word_details={'path':str(a.word),'sha256':sha(a.word.read_bytes()),'bytes':a.word.stat().st_size,'text_and_tables_equal':True,'text_blocks':len(expected),'figures':2,'tables':7,'references':94}
    if (D/'WORD_OUTPUT_RECEIPT.json').is_file():
        receipt=get('WORD_OUTPUT_RECEIPT.json')
        ck('word_receipt_hash',receipt['file']['sha256']==word_details['sha256'])
        ck('word_receipt_all_pages_visually_viewed',receipt['page_count']==23 and receipt['actual_visual_review_pages']==list(range(1,24)) and receipt['visual_review_done'] is True)

bad=[p.name for p in D.rglob('*') if p.is_file() and p.suffix.lower() in {'.pdf','.docx','.png','.zip','.pyc'}]
ck('no_third_party_pdf_or_word_binaries_in_repo',not bad,bad)
if a.manifest_check:
    H=get('SHA256_MANIFEST.json');files={x['path']:x for x in H['files']}
    current={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
    ck('manifest_exact_file_set',set(files)==current)
    for n,h in files.items():ck('manifest_hash_'+n,sha((D/n).read_bytes())==h['sha256'] and (D/n).stat().st_size==h['bytes'])
result={'status':'PASS','scope':'structural, citation-identity, historical Git content and local-artifact checks; not scientific/human acceptance','date_client':'2026-10-17','parent_commit':BASE,'historical_paths_checked':len(tree),'historical_content_aggregate_sha256':sha(json.dumps(hist,ensure_ascii=False,separators=(',',':')).encode()),'historical_comparison':'exact blob bytes or CRLF checkout converted to LF; no old files rewritten','checkout_crlf_only_paths':checkout_eol,'frozen_v19_blob_sha256':frozenhash,'frozen_v19_checkout_sha256':sha(v19current),'checks_passed':len(checks),'checks':checks,'word':word_details,'human_verified':False,'submission_ready':False,'push_performed':False}
if a.output:a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=True,indent=2))
