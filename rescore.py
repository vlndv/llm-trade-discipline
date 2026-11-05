import json
import sys
from scenarios import SCENARIOS
from scorer import reason_ok

by_id = {s["id"]: s for s in SCENARIOS}

for filename in sys.argv[1:]:
    with open(filename) as f:
        results = json.load(f)
    flagged = []
    for r in results:
        scenario = by_id.get(r["id"])
        if scenario and r["passed"] and reason_ok(scenario, r["reply"]) is False:
            flagged.append(r["id"])
    print(filename)
    print("  right action, wrong reason:", flagged if flagged else "none")