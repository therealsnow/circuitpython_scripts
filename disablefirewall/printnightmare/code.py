# This is not my original idea full credit goes to PanicAcid & Cribbit
# My code is never pretty and almost always shit
# V1 First attempt at writing print nightmare in circuitpython.


import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

if not 'jobdone.txt' in os.listdir():
