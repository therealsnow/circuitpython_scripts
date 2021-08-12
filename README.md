#CircuitPython
CircuitPython Scripts for RP2040

This is a repo for scripts I have created to run with the RP2040. My current goal is very light weight ducky scripts on python

##Installing CircuitPython to RP2040

1. Download current CircuitPython from https://circuitpython.org/board/raspberry_pi_pico/
	
2. Make sure you have a USB data cable that is in good working order (A charging cable does not necessarily have data lines.)
   With the board unplugged push and hold the BOOTSEL button and plug in the cable. Once a RPI-RP2 drive loads you can release the button.

3. Drag and drop your CircuitPython uf2 file to the removable drive populated from step two. Once installed the microcontroller reboots automatically.
	
4. If all went well CircuitPython has been installed and a new drive will show up labelled CIRCUITPY
	
If for some reason you have challenges you can download the flash_nuke.uf2 in the repo which takes your board back to stock 
