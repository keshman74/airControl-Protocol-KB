# Transport Detection

Current application rule/evidence:
- A31 / `UP2STREAM_PRO_V4` → Linkplay HTTP
- A97 / `ALLWINNER-R328` → HTTPS
- A98 / WiiM-family → HTTPS
- A33 / ACS2 family → separate ACS2/native protocol stack

Transport detection must be centralized and reused by projects rather than independently guessed.

## 4STREAM client variant
RULE-4STREAM-HTTP-SECURITY: normalized http → HTTP80; secure status → HTTPS443; secure + gc4aVer-presence flag → HTTPS4443. Missing/unknown security defaults to http in the parser. This is APK behavior, not a universal family transport map. [Details](../protocols/linkplay-http-https/4STREAM-2026-10-24.md#httphttps-endpoint-selection).
