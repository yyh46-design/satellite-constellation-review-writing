"""Audit B15 identities, locators, links, counting and change scope.

No scientific reproduction, proof verification or safety certification.
--write-report freezes report and package hashes; ordinary runs check them.
Local source availability is reported separately for a clone on another host.
"""
import csv, hashlib, json, posixpath, re, subprocess, sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
B = Path(__file__).resolve().parent.parent
R = B.parents[3]

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    return json.loads(p.read_text(encoding='utf-8'))

def git(*args):
    return subprocess.check_output(['git', '-C', str(R), *args])

def csvread(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def norm(t):
    return re.sub('[^a-z0-9]', '', str(t).lower())

manifest = read(B / 'SOURCE_MANIFEST_B15.json')
data = read(B / 'READING_CONTENT.json')
status = read(B / 'BATCH_STATUS.json')
sources = manifest['sources']
sm = {s['reading_id']: s for s in sources}
claims = csvread(B / 'CLAIM_EVIDENCE_B15.csv')
cm = {c['claim_id']: c for c in claims}
assert len(sources) == len(data) == len(sm) == 10
assert set(sm) == {f'S{n:03d}' for n in range(21, 31)}
assert {d['reading_id'] for d in data} == set(sm)
assert len({s['identifier'].lower() for s in sources}) == 10
assert all(s['source_format'] == 'PDF' for s in sources)
assert sum(s['pdf_pages'] for s in sources) == 189
assert sum(len(s['visual_reviews']) for s in sources) == 35
assert len(claims) == len(cm) == 45 and 'text' not in claims[0]
assert sum(len(d['claims']) for d in data) == 45
assert set(cm) == {f'C-B15-{n:03d}' for n in range(1, 46)}
assert all(not s['human_verified'] and s['verification_status'] == 'human_pending' for s in sources)
assert sum(s['evidence_role'].startswith('multi_') for s in sources) == 4
assert sum(s['evidence_role'].startswith('general_') for s in sources) == 3
assert sum(s['evidence_role'].startswith('single_') for s in sources) == 3
local_sources = local_visuals = 0
missing = []
for d in data:
    sid = d['reading_id']
    s = sm[sid]
    p = Path(s['local_source_path'])
    note = (B / s['notes_path']).read_text(encoding='utf-8')
    assert s['reading_status'] == 'AI_BODY_CLOSE_READ_COMPLETE'
    assert s['source_sha256'] in note and d['actual_title'] in note
    assert s['actual_version'] == d['actual_version']
    assert s['evidence_role'] == d['evidence_role']
    assert s['narrative_body_pages'] == list(range(d['body_pages'][0], d['body_pages'][1] + 1))
    assert all(1 <= n <= s['pdf_pages'] for n in s['narrative_body_pages'])
    if p.exists():
        assert sha(p) == s['source_sha256']
        local_sources += 1
        try:
            from pypdf import PdfReader
            assert len(PdfReader(p).pages) == s['pdf_pages']
        except ImportError:
            pass
    else:
        missing.append(str(p))
    for c in d['claims']:
        reg = cm[c['claim_id']]
        h = hashlib.sha256(' '.join(c['text'].split()).encode('utf-8')).hexdigest()
        assert c['claim_text_sha256'] == reg['claim_text_sha256'] == h
        assert reg['source_id'] == c['source_id'] == s['source_id']
        assert reg['reading_id'] == sid and reg['note_path'] == s['notes_path']
        assert c['text'] in note and c['claim_id'] in note
        assert c['locator'] and c['pages'] and all(1 <= n <= s['pdf_pages'] for n in c['pages'])
        assert reg['pdf_pages'] == ';'.join(map(str, c['pages']))
        assert reg['source_format'] == 'PDF' and reg['human_verified'] == 'False'
    assert set(d['visual_pages']) == {v['pdf_page'] for v in s['visual_reviews']}
    for v in s['visual_reviews']:
        assert 1 <= v['pdf_page'] <= s['pdf_pages']
        assert v['status'] == 'VISUALLY_INSPECTED'
        p = Path(v['local_path'])
        if p.exists():
            assert sha(p) == v['sha256']
            local_visuals += 1
        else:
            missing.append(str(p))
    identity = read(B / 'metadata' / (sid + '_IDENTITY.json'))
    assert identity['source_sha256'] == s['source_sha256'] and not identity['human_verified']
    assert not identity['formal_version_text_compared']
assert len(list(B.glob('READING_S*_CN.md'))) == 10
assert not (B / 'READING_L066_CN.md').exists()
assert len(list((B / 'metadata').glob('*_IDENTITY.json'))) == 10
crossref_files = list((B / 'metadata').glob('*_CROSSREF.json'))
assert len(crossref_files) == 6
for p in crossref_files:
    z = read(p)
    s = sm[p.name.split('_')[0]]
    assert norm(z['title'][0]) == norm(s['title'])
    assert z['DOI'].lower() == s['identifier'].lower()
for sid in ['S025', 'S029']:
    assert not read(B / 'metadata' / (sid + '_IDENTITY.json'))['doi_external_registration_verified']
assert sm['S024']['version_class'] == 'journal_preproof'
for sid, version in {'S022': '2402.09382v4', 'S026': '2309.16698v1', 'S027': '2204.13251v1', 'S030': '2410.03885v1'}.items():
    assert sm[sid]['arxiv_actual_version'] == version

for p in B.glob('*.md'):
    t = p.read_text(encoding='utf-8')
    for label, target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)', t):
        if target.startswith(('http:', 'https:', '#')):
            continue
        q = p.parent / target
        if target == 'VALIDATION_REPORT.json' and '--write-report' in sys.argv:
            continue
        assert q.is_file(), (p.name, target)
        if 'C-B15-' in label:
            first = int(re.search(r'C-B15-(\d{3})', label).group(1))
            nums = [int(n) for n in re.findall(r'(?<!\d)(\d{3})(?!\d)', label)]
            if '至' in label:
                nums = list(range(first, nums[-1] + 1))
            for n in nums:
                cid = f'C-B15-{n:03d}'
                assert cid in cm and cid in q.read_text(encoding='utf-8'), (p.name, cid, target)

pool = csvread(B / 'READING_STATUS_80_AFTER_B15.csv')
previous = csvread(B.parent / 'B14_20261020/READING_STATUS_80_AFTER_B14.csv')
assert len(pool) == 80
assert sum(x['reading_status'] == 'AI_BODY_CLOSE_READ_COMPLETE' for x in pool) == 20
assert sum(x['reading_status'] == 'NOT_CLOSE_READ' for x in pool) == 60
for now, old in zip(pool, previous):
    for k in old:
        if k != 'note_path':
            assert now[k] == old[k], (now['pool_id'], k)
    if old['note_path']:
        assert now['note_path'] == posixpath.normpath('../B14_20261020/' + old['note_path'])
        assert (B / now['note_path']).is_file()
supp = csvread(B / 'SUPPLEMENT_READING_REGISTER_B15.csv')
assert len(supp) == 30 and {s['supplement_id'] for s in supp} == {f'S{n:03d}' for n in range(1, 31)}
assert sum(s['batch'] == 'B15_20261020' for s in supp) == 10
for s in supp:
    assert (B / s['note_path']).is_file()
previous_supp = csvread(B.parent / 'B14_20261020/SUPPLEMENT_READING_REGISTER_B14.csv')
for now, old in zip(supp[:20], previous_supp):
    for k in old:
        if k != 'note_path':
            assert now[k] == old[k]
assert status['original_pool_close_read_this_batch'] == 0
assert status['original_pool_close_read_cumulative'] == 20 and status['original_pool_remaining'] == 60
assert status['topic_supplement_close_read_this_batch'] == 10
assert status['topic_supplement_close_read_cumulative'] == 30
assert status['B11_through_B15_close_read_records'] == 50
assert status['pdf_files_acquired_and_read'] == 10 and status['pdf_total_pages'] == 189
assert status['actual_visual_page_count'] == 35 and status['claim_count'] == 45
assert not status['manuscript_modified'] and not status['human_verified']
assert status['multi_spacecraft_papers'] == 4 and status['general_multi_agent_foundation_papers'] == 3
assert status['single_controlled_spacecraft_foundation_papers'] == 3

dedup = read(B / 'DEDUP_CHECK.json')
assert not dedup['matches'] and not dedup['prior_source_matches']
assert dedup['prior_B11_B12_B13_B14_sources_checked'] == 40
registers_rechecked = 0
for reg in dedup['registers']:
    p = Path(reg['path'])
    if p.exists():
        assert sha(p) == reg['sha256']
        registers_rechecked += 1
        t = p.read_text(encoding='utf-8-sig')
        for s in sources:
            ids = [s['identifier']]
            if s['arxiv_actual_version']:
                ids.append(s['arxiv_actual_version'].split('v')[0])
            assert not any(i.lower() in t.lower() for i in ids)
            assert norm(s['title']) not in norm(t)
prior_sources = []
for prevbatch in ['B11_20261020', 'B12_20261020', 'B13_20261020', 'B14_20261020']:
    z = read(B.parent / prevbatch / ('SOURCE_MANIFEST_' + prevbatch[:3] + '.json'))
    prior_sources += z['sources']
    for old in z['sources']:
        old_title = old.get('title', old.get('actual_title', ''))
        old_ids = [str(old.get(k, '')).lower() for k in ['identifier', 'actual_identifier', 'formal_doi']]
        for s in sources:
            assert norm(s['title']) != norm(old_title)
            assert s['identifier'].lower() not in old_ids
assert len(prior_sources) == 40

duplicate = read(B / 'DUPLICATE_RECHECK.json')
assert duplicate['reading_id'] == 'L066' and duplicate['new_close_read_credit'] == 0
assert duplicate['original80_increment'] == 0 and duplicate['prior_batch'] == 'B12_20261020'
assert (B / duplicate['prior_note']).is_file()
old_l066 = next(s for s in prior_sources if s['source_id'] == duplicate['prior_source_id'])
assert duplicate['prior_source_sha256'] == old_l066['source_sha256']
recheck_path = Path(duplicate['local_recheck_path'])
duplicate_hash_checked = False
if recheck_path.exists():
    assert sha(recheck_path) == duplicate['source_sha256']
    root = ET.fromstring(recheck_path.read_bytes())
    eq = root.find('.//disp-formula[@id="' + duplicate['equation_id'] + '"]')
    assert eq is not None and eq.findtext('label') == '(51)'
    ns = {'m': 'http://www.w3.org/1998/Math/MathML'}
    matrix = [[int(''.join(td.itertext()).replace('−', '-')) for td in tr.findall('m:mtd', ns)] for tr in eq.findall('.//m:mtable/m:mtr', ns)]
    assert duplicate['matrix_as_encoded'] == matrix
    assert duplicate['row_sums'] == [sum(row) for row in matrix]
    duplicate_hash_checked = True
acq = read(B / 'ACQUISITION_LOG.json')
assert set(acq['selected_source_ids']) == set(sm)
assert acq['excluded_duplicate_rechecks'] == ['L066']
assert len(acq['successful_or_last_attempt_records']) == 11

prefix = 'review_writing/evidence/reading_batches/B15_20261020/'
delta = git('diff', '--name-only', manifest['base_commit']).decode().splitlines()
outside = [x for x in delta if not x.startswith(prefix)]
assert not outside, outside
untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
assert all(x.startswith(prefix) for x in untracked)
baseline = 'review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md'
assert sha(R / baseline) == 'c9d1af6f12d412897a1434ddf082101b2db7491274fb0425896a3f01c7db5a15'
assert hashlib.sha256(git('show', manifest['base_commit'] + ':' + baseline)).hexdigest() == sha(R / baseline)
inherited = []
for prevbatch in ['B11_20261020', 'B12_20261020', 'B13_20261020', 'B14_20261020']:
    paths = git('ls-tree', '-r', '--name-only', manifest['base_commit'], '--', 'review_writing/evidence/reading_batches/' + prevbatch).decode().splitlines()
    for rel in paths:
        assert hashlib.sha256(git('show', manifest['base_commit'] + ':' + rel)).hexdigest() == sha(R / rel)
    inherited += paths
files = [p for p in B.rglob('*') if p.is_file()]
assert not [p for p in files if p.suffix.lower() in ['.pdf', '.png', '.jpg', '.jpeg', '.txt', '.xml', '.pyc']]
report = dict(status='PASS' if not missing else 'PACKAGE_PASS_LOCAL_SOURCE_RECHECK_INCOMPLETE', batch='B15_20261020', sources=10, claims=45, pdf_pages=189, local_original_source_hashes_checked=local_sources, local_visual_hashes_checked=local_visuals, missing_local_files=missing, excluded_duplicate_recheck='L066: already close-read in B12; zero increment', duplicate_XML_hash_checked=duplicate_hash_checked, original80_pool_after_batch={'close_read': 20, 'not_close_read': 60}, separate_topic_supplements_cumulative=30, B11_through_B15_close_read_records=50, prior_B11_B12_B13_B14_inherited_files_unchanged=len(inherited), dedup_register_hashes_rechecked=registers_rechecked, manuscript_sha256_unchanged=sha(R / baseline), outside_batch_tracked_changes=outside, human_verified=False, scope='File identity, evidence links, locators, counting and change scope only; no reproduction, proof or scientific correctness certificate')
if '--write-report' in sys.argv:
    (B / 'VALIDATION_REPORT.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    hashes = {str(p.relative_to(B)).replace('\\', '/'): sha(p) for p in B.rglob('*') if p.is_file() and p.name != 'SHA256_MANIFEST.json'}
    (B / 'SHA256_MANIFEST.json').write_text(json.dumps(hashes, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
else:
    hashes = read(B / 'SHA256_MANIFEST.json')
    for rel, h in hashes.items():
        assert sha(B / rel) == h, rel
    assert set(hashes) == {str(p.relative_to(B)).replace('\\', '/') for p in files if p.name != 'SHA256_MANIFEST.json'}
    report['package_hashes_checked'] = len(hashes)
print(json.dumps(report, ensure_ascii=False, indent=2))
