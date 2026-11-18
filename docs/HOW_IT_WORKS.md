# How it works

Everything is in [`src/main.cpp`](../src/main.cpp) (M5Unified, no other libraries).

## Motion -> mood

The MPU6886 is read every frame (~60 fps). Two numbers drive everything:

- **energy** - a decaying sum of how much the acceleration changed between samples
  (`energy = energy * 0.93 + jerk`). Gentle handling stays near 0; shaking pushes it past 8.
- **magnitude** - length of the acceleration vector, about 1 g at rest and near 0 in free fall.

| Mood | Trigger | Constant |
|---|---|---|
| Dizzy | energy > 8 (held 2.2 s after the last shake) | `SHAKE_ENERGY` |
| Scared | magnitude < 0.35 g (held 0.9 s) | in `readMotion` |
| Excited | energy > 2.5 (held 0.7 s) | `MOVE_ENERGY` |
| Sleeping | no motion for 25 s (drowsy from 12 s) | `SLEEP_AFTER_MS`, `DROWSY_FROM_MS` |
| Idle | otherwise | |

Priority is Dizzy > Scared > Excited > Sleeping > Idle. Movement wakes it up.

## Eyes follow tilt

The firmware keeps a slow baseline of the acceleration (time constant ~3 s). The eyes look toward
the **difference** from that baseline, so it works however you hold the device, and drifts back to
centre if you keep it tilted. If the eyes look the wrong way, flip
`LOOK_X_SIGN` / `LOOK_Y_SIGN` (see `platformio.ini`). When nothing is tilted it glances around and
blinks at random (sometimes twice).

## Characters

`drawCat`, `drawRobot`, `drawGhost`, `drawCyclops` share the helpers `eye()` and `mouth()` so every
character supports all five moods. To add a character: write a `drawXxx()`, add it to the
`Character` enum and `CHAR_NAMES`, and add a `case` in `draw()`.

Everything is drawn into a 128x128 16-bit off-screen canvas and pushed once per frame, so there is
no flicker.

## Button

`BtnA` is the screen button. The click is read **before** the frame gate in `loop()`, because
M5Unified's click flags only live until the next `M5.update()`.
Click = next character (ring + sparkle "pop"), hold = next colour. Both are saved with `Preferences`.

## Serial console (115200)

| Command | Effect |
|---|---|
| `ver` | print the version |
| `char 0-3` | switch character (cat, robot, ghost, cyclops) |
| `theme 0-5` | switch colour |
| `mood 0-4` / `mood auto` | force a mood (idle, happy, dizzy, scared, sleeping) or go back to the IMU |
| `shot` | send the current frame as raw RGB565 (used by `tools/shot.py`) |

## Tools

`tools/shot.py` takes real screenshots over USB: `python tools/shot.py COM9 gallery docs/screenshots`.
