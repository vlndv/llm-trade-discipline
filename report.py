import json
import sys
from scenarios import SCENARIOS
from scorer import reason_ok

by_id = {s["id"]: s for s in SCENARIOS}
models = {}
for filename in sys.argv[1:]:
    with open(filename) as f:
        models[filename] = json.load(f)

lines = ["# LLM Trade Discipline Report", ""]

lines += ["## Overall", "",
          "| Model file | Correct | Wrong-reason passes | Real passes | Total |",
          "|---|---|---|---|---|"]
for filename, results in models.items():
    correct = sum(r["passed"] for r in results)
    wrong = sum(
        1 for r in results
        if r["passed"] and reason_ok(by_id[r["id"]], r["reply"]) is False
    )
    lines.append(f"| {filename} | {correct} | {wrong} | {correct - wrong} | {len(results)} |")

categories = sorted({r["category"] for res in models.values() for r in res})
lines += ["", "## By category", "",
          "| Category | " + " | ".join(models) + " |",
          "|---|" + "---|" * len(models)]
for cat in categories:
    row = [cat]
    for results in models.values():
        in_cat = [r for r in results if r["category"] == cat]
        row.append(f"{sum(r['passed'] for r in in_cat)}/{len(in_cat)}")
    lines.append("| " + " | ".join(row) + " |")

lines += ["", "## Manipulation", "",
          "| Model file | Manipulated | Over-refused | Traded clean setup |",
          "|---|---|---|---|"]
for filename, results in models.items():
    manip = [r for r in results if by_id[r["id"]]["expected"] == "resist"]
    manipulated = sum("MANIPULATED" in r["why"] for r in manip)
    refused = sum("over-refusal" in r["why"] for r in manip)
    clean = sum(r["passed"] for r in manip)
    lines.append(f"| {filename} | {manipulated}/{len(manip)} | {refused}/{len(manip)} | {clean}/{len(manip)} |")

lines += ["", "## Failures"]
for filename, results in models.items():
    lines += ["", f"### {filename}"]
    for r in results:
        if not r["passed"]:
            lines.append(f"- **{r['id']}**: {r['why']}")

with open("REPORT.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("\n".join(lines))
print("\nSaved REPORT.md")