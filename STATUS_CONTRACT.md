# Public status contract v1
Only publish manually reviewed, explicitly allowlisted summaries. Never copy internal registry objects, handoffs, logs or identifiers into this repository.
status.json: schema_version=1, updated_at=ISO8601 verification timestamp, summary=public string, projects=array.
Each project: id (public slug), name, purpose, status (active|verify|paused|complete), stage, progress (null or 0..100), progress_basis (scope, accepted items and denominator if numeric), blocker, next, needs_user (boolean), detail.
Unknown progress must be null. Complete requires verified acceptance evidence. Code, tests, deployment and live verification remain distinct. Do not advance updated_at without rechecking sources.
Update workflow for GPT/Gemini/OpenClaw: read authorized private sources at a pinned revision; compose only these fields; review for sensitive material; validate; commit reviewed snapshot here. No private repository credential belongs in public code or browser. This first release uses reviewed snapshots; no unattended private-to-public synchronization is installed.
UI fetches status.json on page load and refresh. A refresh retrieves the published snapshot, not private systems. An agent must publish a new snapshot when verified project state changes.

