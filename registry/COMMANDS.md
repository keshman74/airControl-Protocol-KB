# Master Command Registry

Current canonical ledger: **221 records**.

- v0.4.8 baseline: records **1–204**
- saved-chat audit increment: records **205–214**
- current-chat/A33M V1.2 normalization: records **215–221**

The CSV shards under `registry/records/` are the lossless source table, while usable canonical views are distributed into device, protocol and function sections.

Chat-audit documents under `evidence/chat-audits/` are provenance only. A finding discovered during a chat audit must be promoted into the canonical structure; it must never exist only in an audit document.

Original record IDs and evidence statuses are preserved. Do not renumber IDs or silently promote evidence levels.
