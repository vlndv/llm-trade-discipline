import json
import sys
from model import ask_model
from rules import SYSTEM_PROMPT
from scenarios import SCENARIOS
from scorer import score


def run_scenario(model, scenario):
    user_prompt = "Market context:\n" + json.dumps(scenario["context"], indent=2)
    reply = ask_model(model, SYSTEM_PROMPT, user_prompt)
    passed, why = score(scenario, reply)
    return {
        "id": scenario["id"],
        "category": scenario["category"],
        "expected": scenario["expected"],
        "reply": reply,
        "passed": passed,
        "why": why,
    }


def run_all(model):
    results = []
    for scenario in SCENARIOS:
        print(f"Running {scenario['id']}...")
        results.append(run_scenario(model, scenario))
    return results


if __name__ == "__main__":
    model = sys.argv[1] if len(sys.argv) > 1 else "qwen3.5:latest"
    results = run_all(model)

    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"[{status}] {r['id']} ({r['category']}): {r['why']}")

    passed = sum(r["passed"] for r in results)
    print(f"\n{model}: {passed}/{len(results)} scenarios correct")

    filename = "results_" + model.replace(":", "_") + ".json"
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    print("Saved", filename)