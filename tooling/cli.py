#!/usr/bin/env python3
import json, sys, pathlib
FINDINGS = [
    "1_legal_override_debug_backdoor.json",
    "2_character_count_collapse.json",
    "3_policy_doc_hallucination.json",
    "4_refusal_metadata_leak.json",
    "5_gradient_multilingual_combo.json",
]
base = pathlib.Path(__file__).resolve().parents[1] / "findings"
def main():
    ok = True
    for f in FINDINGS:
        p = base / f
        if not p.exists():
            print(f"MISSING: {p}")
            ok = False
            continue
        try:
            data = json.loads(p.read_text())
        except Exception as e:
            print(f"INVALID JSON: {p}: {e}")
            ok = False
            continue
        required = ["title","summary","prompts","expected_behavior","observed_behavior"]
        for k in required:
            if k not in data:
                print(f"MISSING FIELD {k}: {p}")
                ok = False
    print("OK" if ok else "FAIL")
    sys.exit(0 if ok else 1)
if __name__ == "__main__":
    main()
