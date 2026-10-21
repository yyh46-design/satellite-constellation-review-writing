"""Check the five-chapter draft, citation migration and evidence pointers, not scientific readiness."""
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


def digest(data):
    return hashlib.sha256(data).hexdigest()


def js(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    checks = []

    def check(name, condition, detail):
        checks.append({"check": name, "pass": bool(condition), "detail": detail})

    text = (HERE / "REVIEW_CN_v3.4.md").read_text(encoding="utf-8")
    body, bibliography = text.split("## 参考文献\n", 1)
    refs = {int(n): value for n, value in re.findall(r"^(\d+)\. (.+)$", bibliography, re.M)}
    register = rows(HERE / "references/REFERENCE_REGISTER_v3.4.csv")
    changes = rows(HERE / "references/REFERENCE_CHANGES_v3.3_to_v3.4.csv")
    recent = rows(HERE / "references/READING_ADOPTION_REGISTER_97.csv")
    status = js(HERE / "audit/RELEASE_STATUS.json")
    frozen = js(HERE / "audit/FROZEN_INPUTS.json")
    check("agreed_structure", re.findall(r"^## ([1-9]) ", body, re.M) == list("12345") and
          all(value in body for value in ["### 3.1 优化建模与分解求解", "### 3.2 启发式构造、局部搜索与混合求解",
          "### 3.3 学习辅助搜索与活动选择", "### 3.6 轨道构型维持与自主避碰决策",
          "#### 3.6.1 轨道构型演化、维持与重构", "#### 3.6.2 接近筛查、风险评估与安全行动选择",
          "#### 3.6.3 避碰机动及机动后构型与任务恢复"]),
          "Five chapters and agreed three-part orbital chain; algorithm foundation retained")
    check("reference_register", len(refs) == len(register) == 90 and set(refs) == set(range(1, 91)) and
          len({r["stable_id"] for r in register}) == 90 and
          all(refs.get(int(r["v34_number"])) == r["reference_text"] for r in register),
          "90 bibliography entries match unique stable IDs and exact text")
    first = []
    for token in re.findall(r"\[([0-9,，–\- ]+)\]", body):
        for part in re.split(r"[,，]", token):
            ns = [int(n.strip()) for n in re.split(r"[–-]", part)]
            for n in range(ns[0], ns[-1] + 1):
                if n not in first:
                    first.append(n)
    check("citation_order_and_coverage", first == list(range(1, 91)),
          "First appearance order 1..90, with no dangling or uncited bibliography entry")
    check("reference_migration", sum(c["disposition"] == "retained" for c in changes) == 72 and
          sum(c["disposition"] == "not_cited_in_v34" for c in changes) == 8 and
          sum(not c["v33_number"] for c in changes) == 18,
          "72 retained + 18 added = 90; eight V3.3 entries remain in history")
    adopted = [r for r in recent if r["v34_cited"] == "True"]
    check("actual_reading_adoption", len(recent) == len({r["reading_id"] for r in recent}) == 97 and
          len(adopted) == 25 and sum(r["v33_cited"] == "False" for r in adopted) == 13 and
          all(r["source_id"] in {x["stable_id"] for x in register} for r in adopted),
          "97 recent reading records reconciled; 25 cited, including 13 newly used in this draft")
    check("tables", re.findall(r"^\*\*表(\d+) ", body, re.M) == [str(n) for n in range(1, 9)],
          "Eight consecutive table titles")
    widths = []
    current = []
    for line in body.splitlines() + [""]:
        if line.startswith("|"):
            current.append(line.count("|"))
        elif current:
            widths.append(len(set(current)) == 1)
            current = []
    check("table_columns", len(widths) == 8 and all(widths), "Eight complete Markdown tables with consistent columns")
    figures = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", body)
    check("inherited_figures", len(figures) == 4 and all((HERE / p).read_bytes() ==
          (ROOT / "review_writing/manuscripts/v3.3-cn" / p).read_bytes() for p in figures),
          "Four inherited draft PNGs retain their bytes; scientific figure review remains open")
    records = js(HERE / "audit/REVISION_RECORDS.json")
    by_id = {r["record_id"]: r for r in records}
    bindings = rows(HERE / "audit/CLAIM_EVIDENCE_BINDINGS.csv")
    lines = text.splitlines()
    claims = {}
    for file in (ROOT / "review_writing/evidence/reading_batches").glob("B*/CLAIM_EVIDENCE_*.csv"):
        for claim in rows(file):
            if claim.get("claim_id"):
                claims[claim["claim_id"]] = claim
    for number in [82, 84, 86, 87]:
        file = ROOT / f"review_writing/evidence/reading_batches/B07_20261016/READING_NOTES_{number:03d}.md"
        for claim_id in re.findall(r"\|(B07-\d{3}-C\d{2})\|", file.read_text(encoding="utf-8")):
            claims[claim_id] = {"source_id": f"E{number:03d}"}
    claims.update({o["observation_id"]: o for o in js(HERE / "audit/INHERITED_PRIMARY_CLARIFICATIONS.json")})
    claims.update({c["claim_id"]: c for c in js(HERE / "audit/CARA_PRIMARY_PASSAGE_RECORD.json")["claims"]})
    errors = []
    used = set()
    for binding in bindings:
        record = by_id[binding["passage_id"]]
        line = int(binding["manuscript_start_line"]) - 1
        if (digest(record["after_text"].encode()) != binding["passage_sha256"] or
                "\n".join(lines[line:line + len(record["after_text"].splitlines())]) != record["after_text"]):
            errors.append({"passage": record["record_id"], "error": "text_hash_or_line"})
        for cid in filter(None, binding["claim_ids"].split(";")):
            used.add(cid)
            if cid not in claims or claims.get(cid, {}).get("source_id") not in binding["source_ids"].split(";"):
                errors.append({"passage": record["record_id"], "claim": cid, "error": "missing_or_wrong_source"})
    check("passage_evidence", len(bindings) == 44 and not errors and "C-B14-003" not in used,
          {"exact_passages": len(bindings), "errors": errors, "scope": "Text hashes, line pointers and existing source-bound claim IDs only"})
    check("revision_operations", len(records) == len(by_id) and
          sum(r["granularity"] == "change" for r in records) == 47,
          "44 passage records and 47 distinct editorial/structural operations")
    mismatches = [name for name, value in frozen["files"].items() if not (ROOT / name).is_file() or
                  digest((ROOT / name).read_bytes()) != value]
    check("preserved_baselines", not mismatches,
          {"files": len(frozen["files"]), "mismatches": mismatches})
    artifact_errors = []
    for source in js(HERE / "audit/SOURCE_RECHECK.json"):
        path = Path(source["local_original_path"])
        if not path.is_file() or digest(path.read_bytes()) != source["sha256"]:
            artifact_errors.append(source["reading_id"])
        if source.get("local_selected_text_path"):
            selected = Path(source["local_selected_text_path"])
            if not selected.is_file() or digest(selected.read_bytes()) != source["selected_text_sha256"]:
                artifact_errors.append(source["reading_id"] + "_selected_text")
    check("available_primary_artifacts", not artifact_errors,
          {"recent_sources": 25, "errors": artifact_errors, "scope": "Local artifact hashes, not scientific sign-off or new readings"})
    check("honest_status", status["human_verified"] is False and status["submission_ready"] is False and
          status["new_independent_paper_reads"] == status["new_scientific_experiments"] == 0 and
          status["seven_chapter_proposal_adopted"] is False and
          all(r["human_verified"] is False for r in records) and all(b["human_verified"] == "False" for b in bindings),
          "Working draft; no human approval, new experiments, new independent reading or seven-chapter adoption claimed")
    changed = subprocess.check_output(["git", "diff", "--name-only", frozen["base_commit"]], cwd=ROOT, text=True).splitlines()
    untracked = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT, text=True).splitlines()
    check("change_scope", all(p.startswith(PREFIX) for p in changed + untracked), "Only the new V3.4 directory is changed")
    forbidden = [str(p.relative_to(HERE)) for p in HERE.rglob("*") if p.is_file() and
                 (p.suffix == ".pdf" or p.name.endswith("_selected_original_pages.txt"))]
    check("no_primary_fulltext_in_release", not forbidden, {"forbidden_files": forbidden})
    check("text_bytes", all(b"\r\n" not in p.read_bytes() for p in HERE.rglob("*") if p.is_file() and
          p.suffix != ".png" and "__pycache__" not in p.parts), "LF bytes retained for stable evidence hashes")
    report_path = HERE / "VALIDATION_REPORT.json"
    manifest_path = HERE / "SHA256_MANIFEST.json"
    broken = []
    for file in HERE.rglob("*.md"):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|#|codex:)", target):
                continue
            path = (file.parent / target.split("#")[0]).resolve()
            if not path.exists() and not (args.write_report and path in {report_path, manifest_path}):
                broken.append({"file": str(file.relative_to(HERE)), "target": target})
    check("local_markdown_links", not broken, {"broken": broken})
    if args.write_report:
        report = {"status": "PASS" if all(c["pass"] for c in checks) else "FAIL", "date": "2026-10-21",
                  "scope": "Five-chapter structure, references, adoption accounting, provenance pointers and file integrity",
                  "human_verified": False, "submission_ready": False, "checks": checks}
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        files = {p.relative_to(HERE).as_posix(): digest(p.read_bytes()) for p in sorted(HERE.rglob("*"))
                 if p.is_file() and p != manifest_path and "__pycache__" not in p.parts}
        manifest_path.write_text(json.dumps({"algorithm": "SHA-256", "files": files}, ensure_ascii=False, indent=2) + "\n",
                                 encoding="utf-8", newline="\n")
    if manifest_path.is_file():
        actual = {p.relative_to(HERE).as_posix(): digest(p.read_bytes()) for p in HERE.rglob("*")
                  if p.is_file() and p != manifest_path and "__pycache__" not in p.parts}
        check("release_manifest", actual == js(manifest_path)["files"], "All released files match their SHA-256 manifest")
    for result in checks:
        print(("PASS " if result["pass"] else "FAIL ") + result["check"])
        if not result["pass"]:
            print(json.dumps(result["detail"], ensure_ascii=False))
    raise SystemExit(0 if all(c["pass"] for c in checks) else 1)


if __name__ == "__main__":
    main()
