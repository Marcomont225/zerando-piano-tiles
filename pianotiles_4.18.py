import win32api
import win32con
import pyautogui
import keyboard
from time import sleep 

def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

sleep(3)
pyautogui.click(1021,442)

while keyboard.is_pressed("1") == False:
    if pyautogui.pixelMatchesColor(919,578,(0,0,0)):
        click(919,578)
    if pyautogui.pixelMatchesColor(988,581,(0,0,0)):
        click(988,581)
    if pyautogui.pixelMatchesColor(1057,581,(0,0,0)):
        click(1057,581)
    if pyautogui.pixelMatchesColor(1132,577,(0,0,0)):
        click(1132,577)