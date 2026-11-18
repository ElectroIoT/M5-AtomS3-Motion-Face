# Publishing to M5Burner

How to share this firmware in [M5Burner](https://docs.m5stack.com/en/uiflow/m5burner/publish)
(*USER CUSTOM > Publish*, logged in with an M5Stack community account).

> **Do not use M5Burner's "Export" on your own AtomS3.** Export reads the whole flash from the
> device, including anything stored on it. Upload the clean `-full.bin` from the Releases page
> instead: it is built from source and its settings area (NVS) is blank.

## Fields

| Field | Value |
|---|---|
| Name | `AtomS3 Motion Face` |
| Version | `v1.0.0` |
| Device Type | `ATOMS3` (AtomS3 with display + MPU6886; not AtomS3 Lite) |
| Github | `https://github.com/ElectroIoT/M5-AtomS3-Motion-Face` |
| FirmWare | `M5-AtomS3-Motion-Face-v1.0.0-full.bin` (single image, flashed at `0x0`) |
| Cover | [`docs/images/m5burner_cover.png`](images/m5burner_cover.png) (800 x 600) |

## Description (paste as is)

```text
A little character lives on your M5Stack AtomS3 screen and reacts to how you move it.

- 4 animated characters: Cat, Robot, Boo the ghost and Cyclops
- Tilt it and the eyes follow; they blink and glance around on their own
- Move it and it gets happy and bounces
- Shake it and it gets dizzy (spiral eyes, orbiting stars)
- Drop it (free fall) and it gets scared
- Leave it still and it gets drowsy, then falls asleep with floating Zzz
- Click the screen button for the next character (pop animation), hold for a new colour
- Remembers your character and colour after power off. No Wi-Fi, no setup.

Needs the AtomS3 with display and MPU6886 (not AtomS3 Lite).
Source, guide and serial test commands: see the GitHub link.
```

## Version description (markdown, paste as is)

```markdown
## v1.0.0 - first release

- 4 animated characters: **Cat**, **Robo**, **Boo** (ghost), **Cyclo** (cyclops)
- Reacts to the MPU6886 motion sensor: tilt = eyes follow, move = happy, shake = dizzy, drop = scared, still = drowsy then asleep (Zzz)
- Click the screen button = next character (pop animation), hold = new colour (6 themes)
- Remembers your character and colour after power off
- No Wi-Fi, no setup. For the **AtomS3 with display + MPU6886** (not AtomS3 Lite)

Source, guide and serial test commands: https://github.com/ElectroIoT/M5-AtomS3-Motion-Face
```

## Making the image (maintainers)

```bash
pio run
python ~/.platformio/packages/tool-esptoolpy/esptool.py --chip esp32s3 merge_bin \
  -o release/M5-AtomS3-Motion-Face-vX.Y.Z-full.bin --flash_mode dio --flash_freq 80m --flash_size 8MB \
  0x0 .pio/build/atoms3/bootloader.bin \
  0x8000 .pio/build/atoms3/partitions.bin \
  0xe000 ~/.platformio/packages/framework-arduinoespressif32/tools/partitions/boot_app0.bin \
  0x10000 .pio/build/atoms3/firmware.bin
```

Before uploading, check the image holds no personal data, for example
`grep -c -a "<your Wi-Fi name>" release/*.bin` must print `0` (this firmware never touches Wi-Fi).
