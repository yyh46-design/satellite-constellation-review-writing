"""Check manuscript references, provenance and preserved inputs; not scientific sign-off."""
import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
PREFIX = HERE.relative_to(ROOT).as_posix() + "/"
checks = []


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def check(name, condition, detail):
    checks.append({"check": name, "pass": bool(condition), "detail": detail})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    manuscript = (HERE / "REVIEW_CN_v3.3.md").read_text(encoding="utf-8")
    body, bibliography = manuscript.split("## 参考文献\n", 1)
    refs = {int(n): text for n, text in re.findall(r"^(\d+)\. (.+)$", bibliography, re.M)}
    register = rows(HERE / "references/REFERENCE_REGISTER_v3.3.csv")
    mapping = rows(HERE / "references/REFERENCE_NUMBER_MAP_v3.2_to_v3.3.csv")
    sources = read_json(HERE / "references/ADDED_SOURCE_MANIFEST.json")["sources"]
    revisions = read_json(HERE / "audit/REVISION_RECORDS.json")
    bindings = rows(HERE / "audit/CLAIM_EVIDENCE_BINDINGS.csv")
    frozen = read_json(HERE / "audit/FROZEN_INPUTS.json")
    status = read_json(HERE / "audit/RELEASE_STATUS.json")
    observations = read_json(HERE / "audit/PRIMARY_SOURCE_CLARIFICATIONS.json")
    check("reference_register", len(refs) == len(register) == 80 and
          set(refs) == set(range(1, 81)) and len({r["stable_id"] for r in register}) == 80 and
          all(refs.get(int(r["v33_number"])) == r["reference_text"] for r in register),
          "80 numbered entries match unique stable IDs and exact bibliography text")
    seen = []
    citations = []
    for token in re.findall(r"\[([0-9,，–\- ]+)\]", body):
        for part in re.split(r"[,，]", token):
            bounds = [int(n.strip()) for n in re.split(r"[–-]", part)]
            nums = list(range(bounds[0], bounds[-1] + 1))
            citations.extend(nums)
            seen.extend(n for n in nums if n not in seen)
    check("citation_order_and_coverage", seen == list(range(1, 81)) and
          all(n in refs for n in citations), "First appearance is 1..80; no uncited or dangling reference")
    old = (ROOT / "review_writing/manuscripts/v3.2-cn/REVIEW_CN_v3.2.md").read_text(encoding="utf-8")
    old_refs = {int(n): text for n, text in re.findall(r"^(\d+)\. (.+)$", old.split("## 参考文献\n", 1)[1], re.M)}
    check("old_bibliography_preserved", len(mapping) == len(old_refs) == 66 and
          all(old_refs[int(m["v32_number"])] == refs[int(m["v33_number"])] for m in mapping),
          "All 66 original reference entries retained verbatim; numeric citations remapped")
    check("new_sources", len(sources) == 14 and
          {s["source_id"] for s in sources} == {r["stable_id"] for r in register if r["origin"] != "V3_2_RETAINED"} and
          all((ROOT / s["note_path"]).is_file() and (ROOT / s["old_reading_manifest"]).is_file() for s in sources),
          "14 reused readings have existing notes and prior source manifests")
    check("structure", re.findall(r"^## ([1-5]) ", body, re.M) == list("12345") and
          re.findall(r"^\*\*表(\d+) ", body, re.M) == [str(i) for i in range(1, 9)] and
          all(heading in body for heading in ["#### 3.6.1", "#### 3.6.2", "#### 3.6.3", "#### 4.4.4"]),
          "Five chapters, eight consecutive tables, and added safety/recovery subsections")
    figures = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", body)
    check("inherited_figures", len(figures) == 4 and all(
          (HERE / f).is_file() and (HERE / f).read_bytes() ==
          (ROOT / "review_writing/manuscripts/v3.2-cn" / f).read_bytes() for f in figures),
          "Four inherited PNGs retain original bytes; no publication or scientific sign-off implied")
    table_widths = []
    current = []
    for line in body.splitlines() + [""]:
        if line.startswith("|"):
            current.append(line.count("|"))
        elif current:
            table_widths.append(len(set(current)) == 1)
            current = []
    check("markdown_tables", len(table_widths) == 8 and all(table_widths), "Eight tables have consistent column counts")
    by_id = {r["passage_id"]: r for r in revisions}
    lines = manuscript.splitlines()
    check("revision_records", len(by_id) == len(revisions) == 42 and all(
          digest(r["after_text"].encode()) == r["after_text_sha256"] and
          r["after_text"] in manuscript for r in revisions), "42 unique revisions retain exact adopted text and hashes")
    claims = {}
    for path in (ROOT / "review_writing/evidence/reading_batches").glob("B*/CLAIM_EVIDENCE_*.csv"):
        for claim in rows(path):
            if claim.get("claim_id"):
                claims[claim["claim_id"]] = claim
    claims.update({o["observation_id"]: o for o in observations})
    evidence_ok = len(bindings) == 25
    used_claims = set()
    for binding in bindings:
        record = by_id[binding["passage_id"]]
        line = int(binding["manuscript_start_line"]) - 1
        evidence_ok &= (digest(record["after_text"].encode()) == binding["passage_sha256"] and
                        "\n".join(lines[line:line + len(record["after_text"].splitlines())]) == record["after_text"])
        source_ids = set(binding["source_ids"].split(";"))
        for cid in filter(None, binding["reading_claim_ids"].split(";")):
            used_claims.add(cid)
            evidence_ok &= cid in claims and claims.get(cid, {}).get("source_id") in source_ids
    check("evidence_bindings", evidence_ok and "C-B14-003" not in used_claims,
          "25 exact manuscript passages match lines/hashes and existing claim or clarification IDs; broad old S011 claim excluded")
    frozen_errors = [name for name, sha in frozen["files"].items()
                     if not (ROOT / name).is_file() or digest((ROOT / name).read_bytes()) != sha]
    check("frozen_inputs", len(frozen["files"]) == 731 and not frozen_errors,
          {"preserved_files": len(frozen["files"]), "mismatches": frozen_errors})
    rechecks = read_json(HERE / "audit/SOURCE_RECHECK.json")
    local_missing = []
    local_bad = []
    for source in rechecks:
        for key, hash_key in [("local_original_path", "sha256"), ("local_selected_text_path", "selected_text_sha256")]:
            path = Path(source[key])
            if not path.is_file():
                local_missing.append(str(path))
            elif digest(path.read_bytes()) != source[hash_key]:
                local_bad.append(str(path))
    check("local_primary_artifacts", len(rechecks) == 14 and not local_bad,
          {"sources": len(rechecks), "mismatches": local_bad, "unavailable_on_this_machine": local_missing,
           "scope": "Hashes of locally available original artifacts and selected passages; absence on another machine is reported, not a reading claim"})
    check("honest_release_status", status["human_verified"] is False and status["submission_ready"] is False and
          status["new_independent_paper_reads"] == status["new_scientific_experiments"] == 0 and
          all(r["human_verified"] is False for r in revisions + rechecks + sources) and
          all(b["human_verified"].lower() == "false" for b in bindings),
          "Working draft; no new independent reading, science experiment or author sign-off credited")
    changed = subprocess.check_output(["git", "diff", "--name-only", frozen["base_commit"]], cwd=ROOT, text=True).splitlines()
    untracked = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT, text=True).splitlines()
    check("change_scope", all(name.startswith(PREFIX) for name in changed + untracked), "All changes confined to the new V3.3 directory")
    check("no_primary_fulltext_committed", not list(HERE.rglob("*.pdf")) and not list(HERE.rglob("*_selected_original_pages.txt")),
          "No original PDFs or full source extraction included in release directory")
    check("text_line_endings", all(b"\r\n" not in path.read_bytes() for path in HERE.rglob("*")
          if path.is_file() and path.suffix != ".png" and "__pycache__" not in path.parts), "Text files retain LF bytes for stable evidence hashes")
    report_path = HERE / "VALIDATION_REPORT.json"
    manifest_path = HERE / "SHA256_MANIFEST.json"
    if args.write_report:
        report = {"status": "PASS" if all(c["pass"] for c in checks) else "FAIL", "date": "2026-10-21",
                  "scope": "Document structure, reference consistency, evidence locators, preserved baseline and file integrity only",
                  "human_verified": False, "submission_ready": False, "checks": checks}
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        manifest = {path.relative_to(HERE).as_posix(): digest(path.read_bytes()) for path in sorted(HERE.rglob("*"))
                    if path.is_file() and path != manifest_path and "__pycache__" not in path.parts}
        manifest_path.write_text(json.dumps({"algorithm": "SHA-256", "files": manifest}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    if manifest_path.is_file():
        expected = read_json(manifest_path)["files"]
        actual = {path.relative_to(HERE).as_posix(): digest(path.read_bytes()) for path in HERE.rglob("*")
                  if path.is_file() and path != manifest_path and "__pycache__" not in path.parts}
        check("release_manifest", actual == expected, "All release files except the manifest itself match their recorded SHA-256")
    for result in checks:
        print(("PASS " if result["pass"] else "FAIL ") + result["check"])
    raise SystemExit(0 if all(c["pass"] for c in checks) else 1)


if __name__ == "__main__":
    main()
