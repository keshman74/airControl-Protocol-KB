# Behavior Rules

1. Hardware confirmation is device/firmware specific.
2. Preserve rejected commands and regressions.
3. Do not merge ACS2 with ordinary Linkplay HTTP merely because command strings overlap.
4. ACS2 has HTTP :8000 and HTTPS :8443 transports.
5. A33 TCP :23040 is a broader native protocol, not merely a seek port.
6. Runtime StreamServicesCapability is authoritative for online-service exposure.
7. UPnP service endpoints should be discovered from device description rather than assumed.
8. A31 canonical relative volume semantics: VOL+ -> vol++; VOL- -> vol--.
9. Never store real passwords, OAuth codes, code verifiers, tokens or session credentials in evidence.
