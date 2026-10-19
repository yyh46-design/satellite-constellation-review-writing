"""Read-only consistency check for the v3.1 Chinese review delivery.

Run with Python 3 and lxml. The optional local baselines are checked when
available. Full-text evidence and scientific validity are not inferred here.
"""
from pathlib import Path
from lxml import etree as E
import csv, hashlib, json, re, sys, zipfile

D = Path(__file__).resolve().parents[1]
R = D.parents[2]
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W, 'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
RX = re.compile(r'\[([0-9,，、–—\-\s]+)\]')

def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def q(s): return '{' + W + '}' + s
def plain(s): return re.sub(r'\*\*(.+?)\*\*', r'\1', s).replace('`', '')
def readcsv(p):
    with p.open(encoding='utf-8-sig', newline='') as f: return list(csv.DictReader(f))
def expand(s):
    out = []
    for x in re.split('[,，、]', s):
        m = re.fullmatch(r'\s*(\d+)\s*[–—\-]\s*(\d+)\s*', x)
        out.extend(range(int(m[1]), int(m[2]) + 1) if m else [int(x)])
    return out
def ptext(p):
    out = []
    for c in p:
        if c.tag == q('pPr'): continue
        t = ''.join(c.xpath('.//w:t/text()', namespaces=NS)).replace('\u2060', '').replace('\u2011', '–')
        va = c.find(q('rPr') + '/' + q('vertAlign')) if c.tag == q('r') else None
        out.append('[' + t.removeprefix('\u00a0') + ']' if va is not None and va.get(q('val')) == 'superscript' else t)
    return ''.join(out)
def sig(e):
    return (e.tag, tuple(sorted(e.attrib.items())), (e.text or '').strip(), tuple(sig(c) for c in e))

checks = {}
def check(name, condition):
    checks[name] = bool(condition)
    if not condition: raise AssertionError(name)

blocks = load(D / 'MANUSCRIPT_BLOCKS.json')
md = (D / 'REVIEW_CN_v3.1.md').read_text(encoding='utf-8-sig')
check('five_chapters', len(re.findall(r'^## [1-5] ', md, re.M)) == 5)
check('seven_tables', len([b for b in blocks if b['kind'] == 'table']) == 7)
check('four_figures', len(re.findall(r'^!\[图[1-4]\]', md, re.M)) == 4)
check('sixty_four_references', [b['number'] for b in blocks if b['kind'] == 'reference'] == list(range(1, 65)))
first = []
for b in blocks:
    if b['kind'] == 'reference': break
    text = ' '.join(' '.join(row) for row in b['rows']) if b['kind'] == 'table' else b.get('text', '')
    for m in RX.finditer(text):
        for n in expand(m[1]):
            if n not in first: first.append(n)
check('first_appearance_is_1_to_64', first == list(range(1, 65)))

expected = []
for b in blocks:
    if b['kind'] == 'image': continue
    if b['kind'] == 'table': expected.append(['table', [[plain(c) for c in row] for row in b['rows']]])
    elif b['kind'] == 'reference': expected.append(['p', f'[{b["number"]}] ' + b['text']])
    else: expected.append(['p', plain(b['text'])])
with zipfile.ZipFile(D / 'REVIEW_CN_v3.1.docx') as z:
    parts = {n: z.read(n) for n in z.namelist()}
doc = E.fromstring(parts['word/document.xml'])
body = doc.find(q('body'))
actual = []
for c in body:
    if c.tag == q('p') and ptext(c): actual.append(['p', ptext(c)])
    elif c.tag == q('tbl'):
        actual.append(['table', [[ptext(cell.find(q('p'))) for cell in row.findall(q('tc'))] for row in c.findall(q('tr'))]])
check('all_257_word_blocks_equal_manuscript', actual == expected and len(actual) == 257)
check('four_word_drawings', len(doc.xpath('//wp:inline', namespaces=NS)) == 4)
check('sixty_four_reference_bookmarks', sorted(doc.xpath('//w:bookmarkStart/@w:name', namespaces=NS)) == sorted('ref_v31_' + str(n) for n in range(1, 65)))
for p in body.findall(q('p')):
    style = p.find(q('pPr') + '/' + q('pStyle'))
    if style is not None and style.get(q('val')) in ['Title', 'Heading1', 'Heading2', 'Heading3']:
        check('black_heading_' + ptext(p)[:24], all(r.find(q('rPr') + '/' + q('color')).get(q('val')) == '000000' for r in p.findall(q('r'))))
tables = body.findall(q('tbl'))
check('all_headers_repeat', all(t.find(q('tr') + '/' + q('trPr') + '/' + q('tblHeader')) is not None for t in tables))
check('header_kept_with_data', all(p.find(q('pPr') + '/' + q('keepNext')) is not None for t in tables for p in t.find(q('tr')).findall(q('tc') + '/' + q('p'))))
check('no_fixed_table_row_height', not doc.xpath('//w:trHeight', namespaces=NS))
check('no_tracked_insertions_or_deletions', not doc.xpath('//w:ins|//w:del', namespaces=NS))
check('no_zotero_field_claim', not re.search(r'ZOTERO|CSL_CITATION', parts['word/document.xml'].decode()))
supers = doc.xpath('//w:r[w:rPr/w:vertAlign[@w:val="superscript"]]', namespaces=NS)
check('word_citations_superscript_without_square_brackets', len(supers) > 100 and all('[' not in ''.join(r.xpath('.//w:t/text()', namespaces=NS)) for r in supers))

index = readcsv(D / 'references/REFERENCE_INDEX_v3.1.csv')
library = readcsv(D / 'references/SOURCE_LIBRARY_95_DISPOSITION.csv')
check('source_index_unique_and_continuous', len(index) == len({r['stable_id'] for r in index}) == 64 and [int(r['v31_number']) for r in index] == list(range(1, 65)))
check('ninety_five_sources_retained', len(library) == len({r['stable_id'] for r in library}) == 95)
check('uncited_31_not_in_final_bibliography', sum(r['status'] == 'retained_in_library_not_cited_in_v31' for r in library) == 31)
check('55_academic_9_engineering', sum(r['kind'] == 'academic' for r in index) == 55 and sum(r['kind'] != 'academic' for r in index) == 9)
claims = readcsv(D / 'CLAIM_EVIDENCE_MAP.csv')
check('208_claim_records', len(claims) == 208)
check('claims_and_sources_keep_human_verification_false', all(r['human_verified'] == 'False' for r in index + library + claims))

baseline = load(D / 'BASELINE_PROVENANCE.json')
baseword = Path(baseline['source_word'])
baseline_result = {'source_word_available': baseword.is_file(), 'optional_local_baselines_checked': 0}
if baseword.is_file():
    check('source_word_unchanged', sha(baseword) == baseline['source_word_sha256'])
    with zipfile.ZipFile(baseword) as z: old = {n: z.read(n) for n in z.namelist()}
    check('source_package_parts_preserved', set(old) == set(parts) and {n for n in old if old[n] != parts[n]} == {'word/document.xml', 'docProps/core.xml'})
    check('source_section_geometry_preserved', sig(E.fromstring(old['word/document.xml']).find(q('body') + '/' + q('sectPr'))) == sig(body.find(q('sectPr'))))
for group in ['tracked_baseline_sha256', 'preserved_local_baseline_sha256']:
    for path, digest in baseline[group].items():
        p = R / path
        if p.is_file():
            check('baseline_unchanged:' + path, sha(p) == digest)
            baseline_result['optional_local_baselines_checked'] += 1

rule_dirs = [R / 'review_writing/discussion' / n for n in ['algorithm_refinement_20261019', 'algorithm_refinement_v1_1_20261019', 'algorithm_refinement_v1_2_20261019']]
broken = []
for directory in [D] + rule_dirs:
    for p in directory.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8-sig')):
            if '://' in target or target.startswith('#'): continue
            if not (p.parent / target.split('#')[0]).exists(): broken.append([str(p.relative_to(R)), target])
check('local_markdown_links_resolve', not broken)
manifest_results = []
for directory in [D] + rule_dirs:
    manifest = directory / 'SHA256_MANIFEST.json'
    if not manifest.exists(): continue
    data = load(manifest)
    for item in data['files']:
        p = directory / item['path']
        check('manifest:' + p.relative_to(R).as_posix(), p.is_file() and sha(p) == item['sha256'] and p.stat().st_size == item['bytes'])
    manifest_results.append({'directory': directory.relative_to(R).as_posix(), 'files': len(data['files'])})
receipt = load(D / 'WORD_OUTPUT_RECEIPT.json')
check('word_sha_matches_receipt', sha(D / 'REVIEW_CN_v3.1.docx') == receipt['sha256'])
check('not_submission_ready', receipt['submission_ready'] is False and receipt['human_verified'] is False)
report = {'status': 'PASS', 'check_count': len(checks), 'all_checks_passed': all(checks.values()), 'manuscript_blocks': len(actual), 'source_counts': {'academic': 55, 'engineering': 9}, 'baseline_check': baseline_result, 'manifest_results': manifest_results, 'visual_review_done': receipt['visual_review_done'], 'page_count': receipt['page_count'], 'human_verified': False, 'submission_ready': False, 'checks': checks}
print(json.dumps(report, ensure_ascii=False, indent=2))
