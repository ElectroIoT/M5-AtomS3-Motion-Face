<p align="center">
  <img src="docs/images/banner.svg" alt="M5 AtomS3 Motion Face" width="100%">
</p>

<p align="center">
  <b>A tiny animated character for the M5Stack AtomS3 that reacts to how you move it.</b><br>
  Tilt &middot; move &middot; shake &middot; drop &middot; leave it alone &mdash; 4 characters, no Wi-Fi, no setup
</p>

<p align="center">
  <a href="https://electroiot.github.io/M5-AtomS3-Motion-Face/flasher/"><b>Install in your browser</b></a> &middot;
  <a href="docs/FLASHING.md">Flashing guide</a> &middot;
  <a href="#how-it-reacts">How it reacts</a> &middot;
  <a href="docs/HOW_IT_WORKS.md">How it works</a> &middot;
  <a href="docs/M5BURNER.md">M5Burner</a>
</p>

<p align="center">
  <img src="docs/images/tour.gif" alt="Tour of the four characters (real device screenshots)" width="256">
</p>

## Characters

All pictures are real screenshots taken from the device over USB (`tools/shot.py`).

| | Idle | Happy (moved) | Dizzy (shaken) | Scared (dropped) | Asleep |
|---|:---:|:---:|:---:|:---:|:---:|
| **Cat** | <img src="docs/screenshots/cat_idle.png" width="110"> | <img src="docs/screenshots/cat_happy.png" width="110"> | <img src="docs/screenshots/cat_dizzy.png" width="110"> | <img src="docs/screenshots/cat_scared.png" width="110"> | <img src="docs/screenshots/cat_sleeping.png" width="110"> |
| **Robo** | <img src="docs/screenshots/robot_idle.png" width="110"> | <img src="docs/screenshots/robot_happy.png" width="110"> | <img src="docs/screenshots/robot_dizzy.png" width="110"> | <img src="docs/screenshots/robot_scared.png" width="110"> | <img src="docs/screenshots/robot_sleeping.png" width="110"> |
| **Boo** | <img src="docs/screenshots/ghost_idle.png" width="110"> | <img src="docs/screenshots/ghost_happy.png" width="110"> | <img src="docs/screenshots/ghost_dizzy.png" width="110"> | <img src="docs/screenshots/ghost_scared.png" width="110"> | <img src="docs/screenshots/ghost_sleeping.png" width="110"> |
| **Cyclo** | <img src="docs/screenshots/cyclops_idle.png" width="110"> | <img src="docs/screenshots/cyclops_happy.png" width="110"> | <img src="docs/screenshots/cyclops_dizzy.png" width="110"> | <img src="docs/screenshots/cyclops_scared.png" width="110"> | <img src="docs/screenshots/cyclops_sleeping.png" width="110"> |

## How it reacts

| You do | It does |
|---|---|
| Tilt it | the eyes follow the tilt (works however you hold it) |
| Leave it | blinks, glances around, occasionally double-blinks |
| Move it | happy `^ ^` eyes, open mouth, bounces, ears/arms wiggle |
| **Shake it** | **dizzy**: spiral eyes, wobble, orbiting stars |
| Drop it (free fall) | **scared**: huge eyes, shaking, sweat drop |
| Still for ~12 s | gets drowsy, eyelids droop |
| Still for ~25 s | **asleep**: eyes closed, breathing, floating Zzz |
| Click the screen | **next character** with a pop animation |
| Hold the screen | new colour (6 themes) |

Your character and colour are remembered after power off.

## Install

- **Browser (easiest):** open the [web installer](https://electroiot.github.io/M5-AtomS3-Motion-Face/flasher/) in Chrome or Edge.
- **M5Burner:** search *AtomS3 Motion Face* (device type ATOMS3).
- **esptool:** `esptool.py --chip esp32s3 --port COM9 write_flash 0x0 M5-AtomS3-Motion-Face-v1.0.0-full.bin` from the [Releases](../../releases) page.
- **PlatformIO:** `git clone`, then `pio run -t upload`.

Details and download-mode tips: [docs/FLASHING.md](docs/FLASHING.md).

## Hardware

| | |
|---|---|
| Board | [M5Stack AtomS3](https://docs.m5stack.com/en/core/AtomS3) (ESP32-S3, 8 MB flash) - the version **with the display** |
| Display | 0.85" 128x128 colour LCD (drawn flicker-free from a 16-bit canvas) |
| Motion sensor | MPU6886 (accelerometer used; gyro not needed) |
| Button | the screen itself (`BtnA`) |

Libraries: [M5Unified](https://github.com/m5stack/M5Unified) (pulls in M5GFX). Nothing else.

## Tuning & test console

Sensitivity constants are at the top of [`src/main.cpp`](src/main.cpp) (`SHAKE_ENERGY`, `MOVE_ENERGY`,
`SLEEP_AFTER_MS`). A serial console (115200) lets you force any character or mood for testing,
and `tools/shot.py` captures real screenshots - see [docs/HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md).
Problems? [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).

## Repository

```
src/main.cpp        the whole firmware
platformio.ini      build config (m5stack-atoms3)
tools/shot.py       screenshots / gallery / GIF over USB
docs/               guides, images, screenshots, web installer (docs/flasher)
```

Maintainers: release images are attached to GitHub Releases; M5Burner steps are in
[docs/M5BURNER.md](docs/M5BURNER.md).

## License

MIT - see [LICENSE](LICENSE).
