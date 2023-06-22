import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"Cursor coordinates: ({x}, {y})")
    time.sleep(0.1)