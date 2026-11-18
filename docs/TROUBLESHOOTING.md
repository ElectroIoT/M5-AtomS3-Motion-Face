# Troubleshooting

| Problem | What to do |
|---|---|
| No serial port appears | Use a USB-C **data** cable. Hold the screen button while plugging in USB (download mode), release after 2 s, retry. |
| Upload says *Wrong boot mode detected* | Put the device in download mode (hold the button, replug) and flash with `--before no_reset`. |
| Screen is blank after flashing | Unplug and replug USB once. |
| Eyes look the wrong way when tilting | Flip `LOOK_X_SIGN` / `LOOK_Y_SIGN` in `platformio.ini`, rebuild. |
| Gets dizzy too easily / never | Lower or raise `SHAKE_ENERGY` (default 8) in `src/main.cpp`. |
| Always "excited" on a vibrating table | Raise `MOVE_ENERGY` (default 2.5). |
| Falls asleep too fast | Raise `SLEEP_AFTER_MS` (default 25 s). |
| Click does nothing | Click the screen itself (it is the button). A long hold changes colour, not character. |
| Want the first character back | Click until the cat appears, or send `char 0` on the serial console. |
| IMU type prints 0 at boot | Make sure it is the AtomS3 with display and MPU6886, not another variant. |
