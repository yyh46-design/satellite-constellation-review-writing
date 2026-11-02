import json,re,hashlib,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
repo=root.parents[2]
baseline_path="review_writing/discussion/synthesis_refinement_20261101/REVIEW_ROUTE_A_CN.md"
base=(repo/baseline_path).read_text(encoding="utf-8")
new=(root/"REVIEW_CN_CLOSED_LOOP_V1.md").read_text(encoding="utf-8")
mapping=json.loads((root/"CITATION_MAP.json").read_text(encoding="utf-8"))
forward={int(k):v for k,v in mapping["baseline_to_current"].items()}
inverse={v:k for k,v in forward.items()}
def restore(t):
 return re.sub(r"\[(\d+)\]",lambda m:"["+str(inverse.get(int(m[1]),int(m[1])))+"]",t)
def equations(t): return re.findall(r"\$\$[\s\S]*?\$\$",t)
def tables(t): return re.findall(r"(?m)^\|.*(?:\n\|.*)*",t)
def notes(t): return re.findall(r"(?m)^注\d+：[\s\S]*?(?=\n\n|\Z)",t)
def table_norm(t): return restore(t).replace("见3.2.2","见3.3").replace("见4.2","见4.3")
def refs(t):
 return {int(m[1]):m[2].strip() for m in re.finditer(r"(?m)^\[(\d+)\] (.*)$",t)}
body=new.split("# 参考文献")[0]
ordered=list(dict.fromkeys(int(x) for x in re.findall(r"\[(\d+)\]",body)))
br,nr=refs(base),refs(new)
raw=subprocess.check_output(["git","show","5443af406380d55e5daee8b057b1993069b5a087:"+baseline_path],cwd=repo).decode("utf-8")
checks={
"five_chapters":len(re.findall(r"(?m)^# [1-5] ",new))==5,
"references_93":len(nr)==93,
"all_references_cited_in_first_use_order":ordered==list(range(1,94)),
"baseline_89_references_preserved":all(br[k]==nr[forward[k]] for k in br),
"two_equations_unchanged":equations(base)==equations(new) and len(equations(new))==2,
"five_tables_preserved_except_citation_and_section_numbers":[table_norm(x) for x in tables(new)]==tables(base) and len(tables(new))==5,
"five_numeric_notes_preserved":[restore(x) for x in notes(new)]==notes(base) and len(notes(new))==5,
"baseline_content_unchanged":raw.replace("\r\n","\n")==base,
"no_unread_new_candidates_cited":not any(x in body for x in ["Yuan等","Sportelli","2609.13428"]),
"new_mainline_present":"在任务需求变化和运行状态不确定性的影响下，大型卫星星座如何通过轨道设计、任务规划与反馈控制的协同，持续满足任务要求？" in new,
"no_broken_citation_tokens":"undefined" not in new and "[None]" not in new,
}
report={"status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"characters":len(new),"sha256_lf_utf8":hashlib.sha256(new.encode()).hexdigest(),"human_verified":False,"submission_ready":False}
(root/"CHECKS.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2))
if not all(checks.values()):raise SystemExit(1)
