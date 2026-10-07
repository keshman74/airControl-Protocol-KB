# Multiroom

Seed page. Add commands through the registry and link evidence here.

## Canonical topology rules
- `RULE-LP-MR-ROLE-PARSING`: Linkplay topology stores `master_ip` and `master_uuid`; a populated `master_ip` identifies a slave and resolves it to the real master. UI selection/cache is not topology truth.
- `RULE-MULTIROOM-FAMILY-SEPARATION`: A33 ACS2 multiroom and A31/A97/A98 Linkplay native multiroom are separate protocol families. Cross-family grouping remains unverified.


## AudioCast / possible DLNA-UPnP interoperability path
- WiiM OpenAPI exposes a distinct `audio_cast` subsystem: `audio_cast:scan_speaker`, `audio_cast:get_speaker_list`, `audio_cast:speaker_get_transcode_profile`, `audio_cast:speaker_get_transcode_buffer_time`, `audio_cast:speaker_set_volume:<speaker>:<0..100>`, and `audio_cast:speaker_set_password:<...>`. The source marks these endpoints deprecated and does not identify the wire protocol used toward the target speaker.
- `getNewAudioOutputHardwareMode` reports `audiocast: 0|1` independently of hardware output and Bluetooth-source output. `getActiveSoundCardOutputMode` likewise exposes `audioCast` separately from the active hardware sound-card mode.
- **USER-OBSERVED / PROTOCOL-UNVERIFIED:** the native WiiM application presents AudioCast as sending audio to compatible UPnP/DLNA devices. This observation is useful evidence of intended function, but the current OpenAPI does not itself prove the target transport is DLNA/UPnP.
- **RESEARCH CANDIDATE:** investigate AudioCast as a possible interoperability bridge for cross-family multiroom, especially A97/A98 -> A33 if A33 can act as a compatible DLNA/UPnP renderer. This is **NOT CONFIRMED MULTIROOM SUPPORT** and must not override `RULE-MULTIROOM-FAMILY-SEPARATION` until hardware/capture tests prove discovery, target selection, stream transport, synchronization/latency and control behavior.
