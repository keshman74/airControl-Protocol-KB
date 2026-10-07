# Attach a New Project or Chat

## New project — minimum 1 record
Add one row to `PROJECTS.md`:
`PRJ-ID | repository | local path | role`

Then create in that project:
`docs/PROTOCOL.md`

Recommended content:
```md
# Protocol dependency
Canonical KB: airControl-Protocol-KB
Project ID: PRJ-...
Functions: volume, playback, discovery, ...
Rule: prefer CONFIRMED; never silently replace confirmed behavior.
New verified findings must be contributed back to the KB.
```

## New research chat — minimum 1 record
Add one row to `CHATS.md`:
`CHAT-ID | scope | KB targets`

At the start of the chat use:
```text
Canonical KB: airControl-Protocol-KB
Chat ID: CHAT-...
Before researching: check INDEX, COMPATIBILITY and relevant function.
Every new finding must have status + device + protocol + evidence.
```

This keeps onboarding lightweight: one registry row plus one pointer file.
