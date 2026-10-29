# DEV-A31
Known stack: Linkplay HTTP :80 + MCU TCP :8899. Confirmed functions include status, volume, mute, URL playback, source switching, USB list, network configuration and native multiroom. EQ has its own MCU/TCP backend; do not merge it blindly with A98 EQ.

## Service/debug SSH :24678/TCP
- **Status:** CONFIRMED on tested A31 hardware/firmware `4.6.415156`.
- **Transport:** SSH over TCP port `24678`.
- **Purpose:** service/debug shell used for firmware research and maintenance. This is **not** the public Linkplay user/control API and must not be assumed available on every A31 firmware/build.
- **Tested username:** `admin`.
- **Credential:** intentionally not stored in the public KB; use the credential from the controlled test/evidence context.
- **Connection:** `ssh -p 24678 admin@<A31-IP>`.
- Successful authentication reached the device BusyBox `ash` shell. This access was used during A31 firmware research, including inspection of `/proc/mtd`, `/vendor`, and `/mnt`.
- **Security:** do not expose TCP/24678 to the Internet; restrict service/debug SSH to a trusted local/service network.

## Native KNX integration
- [A31 native KNXnet/IP multicast receiver + verified Mute readback](NATIVE_KNX.md) — **CONFIRMED on A31 hardware**, including [V6E firmware-installed autonomous cold-boot Native KNX v0.11](../../evidence/hardware/A31-RAKOIT-SILENT-NATIVE-KNX-V6E-HW-VERIFIED-2026-10-30.md) on spare A31 `192.168.0.29`. Earlier v0.6–v0.10 manual `/tmp` tests remain historical baselines.
