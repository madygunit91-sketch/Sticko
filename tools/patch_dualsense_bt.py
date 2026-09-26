#!/usr/bin/env python3
"""Patch the GP2040-CE Bluetooth HID mode into a DualSense-identity test profile.

This prototype intentionally changes *identity* only. It does not implement Sony PS5
authentication or the complete DualSense feature/output report protocol.
"""
from pathlib import Path
import sys

p = Path("src/drivers/hidbt/HIDBTDriver.cpp")
if not p.exists():
    raise SystemExit(f"missing {p}; run this script from the GP2040-CE source root")

s = p.read_text()
repls = {
    'gap_set_local_name("GP2040 Gamepad");': 'gap_set_local_name("Wireless Controller");',
    '.device_name = "GP2040 Gamepad"': '.device_name = "Wireless Controller"',
    'DEVICE_ID_VENDOR_ID_SOURCE_USB, 0x1209, 0x2040, 0x0001);':
        'DEVICE_ID_VENDOR_ID_SOURCE_USB, 0x054C, 0x0CE6, 0x0100);',
}

for old, new in repls.items():
    if old not in s:
        raise SystemExit(f"expected source fragment not found: {old}")
    s = s.replace(old, new, 1)

# Keep a conspicuous marker in the built source so binary/string inspection can
# distinguish this prototype from normal GP2040-CE builds.
needle = '#define __BTSTACK_FILE__ "HIDBTDriver.cpp"\n'
marker = '#define STICKO_DUALSENSE_BT_IDENTITY_TEST 1\n'
if marker not in s:
    if needle not in s:
        raise SystemExit("BTstack source marker location not found")
    s = s.replace(needle, needle + marker, 1)

p.write_text(s)
print("Patched Bluetooth HID identity to Wireless Controller / 054C:0CE6")
