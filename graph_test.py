import pyautogui
import time

time.sleep(3)
for i in range(100):
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('left')