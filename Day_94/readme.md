# Google Dinosaur Game Auto-Player

This script automates playing the Google Chrome Dinosaur Game (chrome://dino) by detecting obstacles on screen and simulating key presses.

## Features

* Pixel-based obstacle detection using screen capture.
* Manual calibration of detection region of interest (ROI).
* Adjustable sensitivity parameters for detection.
* Simple hotkey controls.

## Requirements

Install dependencies:

```bash
pip install mss opencv-python numpy pyautogui keyboard
```

## Usage

1. Open the Chrome dino game (navigate to `chrome://dino`).
2. Run the script:

   ```bash
   python dino_bot.py
   ```
3. Calibration:

   * Move mouse to **top-left** of the detection region, press `1`.
   * Move mouse to **bottom-right** of the detection region, press `2`.
   * The region should cover a stripe just ahead of the dinosaur’s nose/feet.
4. Press `SPACE` to start the bot.

## Controls

* `1`: Set top-left corner of ROI.
* `2`: Set bottom-right corner of ROI.
* `SPACE`: Start bot after calibration.
* `p`: Pause/Resume.
* `q`: Quit.

## Parameters (edit in code)

* `dark_threshold`: Grayscale threshold for detecting dark pixels (default 120).
* `pixel_trigger`: Minimum number of dark pixels to trigger a jump.
* `cooldown_ms`: Minimum milliseconds between jumps.
* `sample_interval_ms`: Delay between screen captures.

## Notes

* Ensure Chrome dino game window is visible in the foreground.
* The bot relies on pixel colors. Adjust `dark_threshold` and ROI size if detection fails.
* To stop safely, move the mouse cursor to a screen corner (PyAutoGUI failsafe).
