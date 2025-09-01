#!/usr/bin/env python3

import time
import sys
from dataclasses import dataclass

import numpy as np
import cv2
import mss
import pyautogui
import keyboard

pyautogui.FAILSAFE = True  # move mouse to a corner to abort


@dataclass
class ROI:
    left: int
    top: int
    width: int
    height: int

    @property
    def bbox(self):
        return {"left": self.left, "top": self.top, "width": self.width, "height": self.height}


def get_mouse_pos():
    x, y = pyautogui.position()
    return int(x), int(y)


def calibrate_roi():
    print("[Calibrate] Place mouse at TOP-LEFT of detection region, press '1'.")
    while True:
        if keyboard.is_pressed('1'):
            x1, y1 = get_mouse_pos()
            print(f"[Calibrate] Top-left set: ({x1}, {y1})")
            time.sleep(0.25)
            break
        time.sleep(0.01)

    print("[Calibrate] Place mouse at BOTTOM-RIGHT of detection region, press '2'.")
    while True:
        if keyboard.is_pressed('2'):
            x2, y2 = get_mouse_pos()
            print(f"[Calibrate] Bottom-right set: ({x2}, {y2})")
            time.sleep(0.25)
            break
        time.sleep(0.01)

    if x2 <= x1 or y2 <= y1:
        raise ValueError("Invalid ROI corners. Bottom-right must be greater than top-left.")

    roi = ROI(left=x1, top=y1, width=x2 - x1, height=y2 - y1)
    print(f"[Calibrate] ROI: left={roi.left} top={roi.top} width={roi.width} height={roi.height}")
    return roi


def count_dark_pixels(img_gray: np.ndarray, thresh: int) -> int:
    # Obstacles are darker than the desert background
    _, bin_img = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY_INV)
    return int(np.count_nonzero(bin_img))


def main():
    print("Chrome dino must be visible in the foreground.")
    print("Hotkeys: '1' set top-left, '2' set bottom-right, SPACE start, 'p' pause/resume, 'q' quit.\n")

    try:
        roi = calibrate_roi()
    except Exception as e:
        print(f"Calibration error: {e}")
        sys.exit(1)

    # Sensitivity parameters
    dark_threshold = 120        # 0-255. Lower means only very dark pixels trigger
    pixel_trigger = max(roi.width * roi.height // 30, 120)  # trigger when enough dark pixels appear
    cooldown_ms = 120           # minimum ms between jumps
    sample_interval_ms = 8      # capture cadence

    print(f"[Params] dark_threshold={dark_threshold}  pixel_trigger={pixel_trigger}  "
          f"cooldown_ms={cooldown_ms}  sample_interval_ms={sample_interval_ms}")
    print("Adjust in code if needed.\n")

    print("Press SPACE to start the bot.")
    while True:
        if keyboard.is_pressed('space'):
            time.sleep(0.25)
            break
        if keyboard.is_pressed('q'):
            print("Exiting.")
            return
        time.sleep(0.01)

    paused = False
    last_jump_ts = 0.0

    with mss.mss() as sct:
        print("Running. 'p' to pause/resume. 'q' to quit.")
        while True:
            if keyboard.is_pressed('q'):
                print("Quit requested.")
                break

            if keyboard.is_pressed('p'):
                paused = not paused
                print("Paused." if paused else "Resumed.")
                time.sleep(0.3)  # debounce

            if paused:
                time.sleep(0.05)
                continue

            # Grab frame
            frame = np.array(sct.grab(roi.bbox))
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

            # Count dark pixels
            dark_count = count_dark_pixels(gray, dark_threshold)

            # Decide to jump
            now = time.time()
            if dark_count >= pixel_trigger and (now - last_jump_ts) * 1000.0 >= cooldown_ms:
                pyautogui.press('space')
                last_jump_ts = now

            time.sleep(sample_interval_ms / 1000.0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")