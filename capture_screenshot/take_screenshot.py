import pyautogui
import time

screen_x, screen_y = pyautogui.size()
start_x, start_y = int(screen_x*.8), int(screen_y*.8)
screenshot = pyautogui.screenshot(region=(start_x, start_y, screen_x-start_x, screen_y-start_y))
screenshot.save('screenshot.png')
