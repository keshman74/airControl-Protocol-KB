# DEV-A31
Known stack: Linkplay HTTP :80 + MCU TCP :8899. Confirmed functions include status, volume, mute, URL playback, source switching, USB list, network configuration and native multiroom. EQ has its own MCU/TCP backend; do not merge it blindly with A98 EQ.

## Native KNX integration
- [A31 native KNXnet/IP multicast receiver + verified Mute readback](NATIVE_KNX.md) — **CONFIRMED on A31 hardware (v0.6/v0.7)**. Standalone manually launched MIPS32 ELF from `/tmp`; no permanent firmware installation or autostart yet.
