import pyautogui
import time

curr_pos = pyautogui.position()

while True:
    new_pos = pyautogui.position()
    if curr_pos != new_pos:
        print(f"Cursor coordinates: (x={new_pos[0]}, y={new_pos[1]})")
        time.sleep(.1)
        curr_pos = new_pos
