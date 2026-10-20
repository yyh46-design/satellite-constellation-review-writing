"""Read-only checks and derived ledgers for v3.2; no scientific certification.
Run in a local clone. Output paths are new derived records, never old reading logs.
"""
from __future__ import annotations
import argparse
import csv
import difflib
import hashlib
import io
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

BASE = '06bbd4bbfd0dc67662dd19a9fe237927ca5e16b0'
BASE_PATH = 'review_writing/manuscripts/v3.1-cn/REVIEW_CN_v3.1.md'
EXPECTED_BLOB = 'eebcf66e3c80334950f4aa7589307e8882a30e40'
IMAGES = {
    'fig1_service_framework_ai_v2.png': '12a9bf40956381e866289aef8cf67cadf0912f5a',
    'fig2_scale_mechanisms_ai_v2.png': '460f68323f72856b468d84dddde032a1e0ea7c5c',
    'fig3_decision_timing_ai_v2.png': 'f8d951fb2fa0b1f5420e60ff1f49e5086585c47d',
    'fig4_conditional_comparisons_ai_v2.png': 'a8b9f994c563d5bae1bb9b4fff32c2e684080ed2',
}

def blob(data: bytes) -> str:
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()

def read_csv(path: Path) -> list[dict]:
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def citations(text: str) -> list[int]:
    out = []
    for expr in re.findall(r'\[([0-9][0-9,，\s–—-]*)\]', text):
        for part in re.split(r'[,，]', expr):
            ends = re.split(r'[–—-]', part.strip())
            if len(ends) == 1:
                out.append(int(ends[0]))
            elif len(ends) == 2:
                a, b = map(int, ends)
                if a > b:
                    raise ValueError(f'Reversed citation range: {part}')
                out.extend(range(a, b + 1))
            else:
                raise ValueError(f'Invalid citation range: {part}')
    return out

def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(rows)

def run(root: Path, out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    raw = (root / 'REVIEW_CN_v3.2.md').read_bytes()
    text = raw.decode('utf-8-sig').replace('\r\n', '\n')
    body, bibliography = text.split('## 参考文献', 1)
    refs = {int(n): t.strip() for n, t in re.findall(
        r'(?ms)^(\d+)\.\s+(.+?)(?=^\d+\.\s+|\Z)', bibliography)}
    mapping = read_csv(root / 'references/REFERENCE_NUMBER_MAP_v3.1_to_v3.2.csv')
    library = read_csv(root / 'references/SOURCE_LIBRARY_95_BASELINE_v3.1.csv')
    by_id = {row['stable_id']: row for row in library}
    by_n = {int(row['v32_number']): row for row in mapping}
    ids = {row['stable_id'] for row in mapping}
    old_ids = {row['stable_id'] for row in library if row['status'] == 'cited_in_v31'}
    seen = citations(body)
    image_paths = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', body)
    source_counts = Counter(by_id[sid]['kind'] for sid in ids if sid in by_id)
    mismatches = []
    for n, row in by_n.items():
        identity = by_id.get(row['stable_id'], {}).get('identity', '')
        if not identity or identity.lower().rstrip('.') not in refs.get(n, '').lower():
            mismatches.append({'number': n, 'id': row['stable_id'], 'identity': identity})
    checks = {
        'manuscript_git_blob_matches': blob(raw) == EXPECTED_BLOB,
        'five_chapters': len(re.findall(r'^## [1-5] ', body, re.M)) == 5,
        'seven_tables': len(re.findall(r'^\*\*表[1-7] ', body, re.M)) == 7,
        'four_image_references': len(image_paths) == 4,
        'bibliography_1_to_66': sorted(refs) == list(range(1, 67)),
        'all_66_cited': set(seen) == set(range(1, 67)),
        'first_appearance_order': list(dict.fromkeys(seen)) == list(range(1, 67)),
        'mapping_unique': len(mapping) == len(ids) == len(by_n) == 66,
        'all_64_baseline_sources_preserved': old_ids <= ids and len(old_ids) == 64,
        'only_two_library_sources_restored': ids - old_ids == {'E105', 'E107'},
        'library_count_95': len(library) == len(by_id) == 95,
        'remaining_library_count_29': len(set(by_id) - ids) == 29,
        'source_counts_57_9': dict(source_counts) == {'academic': 57, 'engineering': 9},
        'bibliographic_identities_match': not mismatches,
    }
    for name, expected in IMAGES.items():
        p = root / 'assets' / name
        checks['inherited_image_' + name] = p.exists() and blob(p.read_bytes()) == expected
    index = []
    for n, row in sorted(by_n.items()):
        source = by_id[row['stable_id']]
        index.append({**source, **row, 'bibliographic_entry_v32': refs[n],
                      'status_v32': 'cited', 'local_archive_status': 'not_checked_by_this_script'})
    disposition = []
    number_by_id = {r['stable_id']: r['v32_number'] for r in mapping}
    for source in library:
        sid = source['stable_id']
        disposition.append({**source, 'status_v31': source['status'],
                            'v32_number': number_by_id.get(sid, ''),
                            'status_v32': 'cited' if sid in ids else 'retained_not_cited'})
    uses = []
    section = ''
    for line_number, line in enumerate(body.splitlines(), 1):
        if line.startswith('#'):
            section = line.lstrip('# ').strip()
        nums = citations(line)
        if nums:
            uses.append({'line': line_number, 'section': section,
                         'references': ';'.join(map(str, dict.fromkeys(nums))),
                         'stable_ids': ';'.join(dict.fromkeys(by_n[n]['stable_id'] for n in nums)),
                         'text': line, 'scientific_verified': False})
    write_csv(out / 'REFERENCE_INDEX_v3.2.csv', index)
    write_csv(out / 'SOURCE_LIBRARY_95_DISPOSITION_v3.2.csv', disposition)
    write_csv(out / 'CITATION_USE_MAP.csv', uses)
    baseline_note = 'not_available'
    try:
        cp = subprocess.run(['git', 'show', f'{BASE}:{BASE_PATH}'], cwd=root,
                            capture_output=True, check=True, timeout=30)
        baseline = cp.stdout.decode('utf-8-sig').replace('\r\n', '\n')
        diff = difflib.unified_diff(baseline.splitlines(True), text.splitlines(True),
                                   fromfile='v3.1', tofile='v3.2')
        (out / 'v3.1_to_v3.2.diff').write_text(''.join(diff), encoding='utf-8')
        baseline_note = 'fixed_commit_read_successfully'
    except (OSError, subprocess.SubprocessError, UnicodeError) as exc:
        baseline_note = type(exc).__name__ + ': baseline diff unavailable; no substitute used'
    result = {'checks': checks, 'pass': all(checks.values()),
              'manuscript_sha256': hashlib.sha256(raw).hexdigest(),
              'identity_mismatches': mismatches, 'baseline_diff': baseline_note,
              'scope': 'identity and structural consistency only',
              'human_verified': False, 'submission_ready': False,
              'fulltext_readings_added': 0, 'version_pairs_closed': 0,
              'figure_pixel_scientific_check': False, 'word_page_review': False}
    (out / 'VALIDATION.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--out-dir', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.out_dir.resolve() if args.out_dir else root / 'local_verification'
    report = run(root, output)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['pass'] else 1)
