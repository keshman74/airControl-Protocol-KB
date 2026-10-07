# Master Command Registry

Baseline: **v0.4.8 — 204 canonical records**.

All 204 records have been reviewed for structural placement. The CSV shards under `registry/records/` remain the lossless source table, while usable canonical views are distributed into device, protocol and function sections.

Chat-audit documents under `evidence/chat-audits/` are provenance only. A finding discovered during a chat audit must be promoted into the canonical structure; it must never exist only in an audit document.

Original record IDs and evidence statuses are preserved. Do not renumber IDs or silently promote evidence levels.
