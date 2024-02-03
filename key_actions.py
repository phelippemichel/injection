import ctypes
import time
from key_codes import *

hwnd = ctypes.windll.user32.FindWindowW(0, 'Ravendawn - Pimpolhosz')

def send_message_keyboard(hwnd, key_code):
    ctypes.windll.user32.PostMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    time.sleep(0.1)
    ctypes.windll.user32.PostMessageW(hwnd, WM_KEYUP, key_code, 0)

def moveToMouse(hwnd, x, y):
    x = int(x)
    y = int(y)
    ctypes.windll.user32.PostMessageW(hwnd, WM_MOUSEMOVE, MK_LBUTTON)

def clickMouse(hwnd, x, y, button="Mleft"):
    x = int(x)
    y = int(y)
    if button == "Mleft":
        ctypes.windll.user32.PostMessageW(hwnd, WM_LBUTTONDOWN, 1)
        time.sleep(0.01)
        ctypes.windll.user32.PostMessageW(hwnd, WM_LBUTTONUP, 0)
        return
    ctypes.windll.user32.PostMessageW(hwnd, WM_RBUTTONDOWN, 1)
    time.sleep(0.01)
    ctypes.windll.user32.PostMessageW(hwnd, WM_RBUTTONUP, 0)

while True:
    send_message_keyboard(hwnd, VK_W)