"""Evidence-aware marketing method triage, not verification or causal attribution."""
import json
from pathlib import Path
from urllib.parse import urlparse

WEIGHTS={"evidence_strength":.30,"relevance":.30,"novelty":.10,"transferability":.15,"source_reliability":.15}

def evaluate(record):
    required=("id","method","source_url","source_author","source_channel","published_at","observed_at","verification_status","primary_kpi","test_days")
    missing=[name for name in required if name not in record]
    if missing: raise ValueError("Missing: "+", ".join(missing))
    parsed=urlparse(record["source_url"])
    if parsed.scheme not in ("https","http") or not parsed.netloc: raise ValueError("Invalid source URL")
    for field in WEIGHTS:
        if not isinstance(record.get(field),int) or isinstance(record.get(field),bool) or not 1<=record[field]<=5:
            raise ValueError(f"{field} must be integer 1..5")
    score=round(sum(record[f]*w for f,w in WEIGHTS.items())*20,1)
    return {"id":record["id"],"method":record["method"],"triage_score":score,
      "source_url":record["source_url"],"source_author":record["source_author"],
      "published_at":record["published_at"],"observed_at":record["observed_at"],
      "verification_status":record["verification_status"],
      "recommended_status":"requires_evidence_review" if record["evidence_strength"]<4 else "qualified_for_independent_review",
      "primary_kpi":record["primary_kpi"],"hypothesis":f"Testing {record['method']} may improve {record['primary_kpi']}.",
      "experiment_spec":{"duration_days":record["test_days"],"control":"predefined comparable group or baseline","success_threshold":"must be specified before activation",
         "safeguards":["require approval for public execution","pause for tracking loss","stop on policy breach"],
         "decision":"adopt, iterate, reject, or extend with reason"}}

def rank(records):
    return sorted((evaluate(r) for r in records),key=lambda x:(-x["triage_score"],x["id"]))

if __name__=="__main__":
    root=Path(__file__).resolve().parents[1]
    records=json.loads((root/"fixtures/synthetic_tactics.json").read_text())
    print(json.dumps({"synthetic":True,"results":rank(records)},indent=2))
