from evdev import InputDevice
from select import select

# look for a /dev/input/by-id/usb...kbd or something similar
DEVICE = "/dev/input/by-id/usb-1a86_e026-event-kbd"

dev = InputDevice(DEVICE)

while True:
    
    r, w, x = select([dev],[],[])

    for event in dev.read():

        if event.type == 1 and event.value==1:
            print("Key:",event.code)
