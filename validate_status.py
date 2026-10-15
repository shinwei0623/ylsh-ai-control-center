import json, re
from pathlib import Path
d = json.loads(Path(__file__).with_name("status.json").read_text())
assert set(d) == {"schema_version", "updated_at", "summary", "projects"}
assert d["schema_version"] == 1
keys = {"id", "name", "purpose", "status", "stage", "progress", "progress_basis", "blocker", "next", "needs_user", "detail"}
assert len({p["id"] for p in d["projects"]}) == len(d["projects"])
for p in d["projects"]:
    assert set(p) == keys
    assert p["status"] in {"active", "verify", "paused", "complete"}
    assert type(p["needs_user"]) is bool
    assert p["progress"] is None or type(p["progress"]) in (int, float) and 0 <= p["progress"] <= 100
    assert p["progress_basis"]
    assert all(isinstance(v, str) for k,v in p.items() if k not in {"progress", "needs_user"})
s = json.dumps(d, ensure_ascii=False)
assert not re.search(r"https?://|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|AKfy|AIza|ghp_|github_pat_|[A-Za-z0-9_-]{35,}", s), "Sensitive or internal content candidate"
print("PASS: schema, field allowlist and common sensitive-pattern scan. Human review still required.")
