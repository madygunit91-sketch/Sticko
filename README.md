# Sticko — GP2040-CE Pico 2 W Bluetooth Controller Prototype

This repository builds an experimental Raspberry Pi Pico 2 W firmware from the GP2040-CE Bluetooth work in PR #1575.

The first prototype intentionally keeps the scope narrow:

- Pico 2 W / RP2350
- Bluetooth Classic HID using BTstack
- Bluetooth device name: `Wireless Controller`
- Bluetooth PnP identity: Sony `054C:0CE6`
- DualSense-style *simple* Bluetooth HID input layout for sticks, D-pad, 14 buttons, and digital L2/R2
- Existing GP2040-CE input processing and Web Config remain the base

## Important limitation

This is a compatibility/research prototype, **not native PS5 authentication**. A VID/PID, product name, and HID report format do not provide Sony authentication credentials. The build is intended first for PC/Android host testing.

## Build

Run the GitHub Actions workflow **Build Pico2W DualSense BT Prototype**. It clones the pinned GP2040-CE Bluetooth branch, applies `tools/patch_dualsense_bt.py`, builds the Web Config assets, then builds the Pico2W UF2.

## Pairing

Select the existing **HID BT** input mode in GP2040-CE. The patched build changes that Bluetooth mode into the DualSense-style test profile. It should advertise as `Wireless Controller`.

Hold **Start + Select for 3 seconds while disconnected** to clear the saved Bluetooth pairing, inherited from the upstream HID BT implementation.

## USB

GP2040-CE v0.7.12 already supports USB VID/PID overrides for supported USB modes. Setting `054C:0CE6` changes USB identity only; it does not make the USB report protocol a complete native DualSense implementation.
