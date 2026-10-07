# airControl Protocol Knowledge Base

Canonical shared knowledge base for airControl-compatible devices, protocols, services, projects and research chats.

## Rule
Before researching or implementing a device function:
1. Check `INDEX.md`.
2. Check `registry/COMPATIBILITY.md`.
3. Check the relevant `functions/` page.
4. Prefer `CONFIRMED` evidence over `DOCUMENTED` or `EXPERIMENTAL`.
5. Never replace a confirmed implementation with an experimental one without hardware testing.
6. Add every new verified finding to this KB.

## Evidence statuses
- `CONFIRMED` — hardware/practically verified.
- `CAPTURED` — observed in a real network/protocol capture.
- `DOCUMENTED` — described by a source/API but not yet hardware-verified here.
- `IMPLEMENTED` — present in project code; verification may still be required.
- `EXPERIMENTAL` — reverse-engineered hypothesis or incomplete research.
- `REJECTED` — tested and known not to work in the stated context.

## Security
Never commit real tokens, passwords, cookies, session credentials or private identifiers. Use `<REDACTED>`.
