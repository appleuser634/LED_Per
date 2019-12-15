import board
import neopixel
import time
import random
import threading

pixels = neopixel.NeoPixel(board.D18, 150, auto_write=False)

import sys
import tty
import termios
    
#blue_random is threading process

def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def init_set():
    leds = int(input("LEDS="))
    color = input("COLOR=")
    color = color.split(",")
    color = (int(color[0]),int(color[1]),int(color[2]))
    
    wave = input("Wave?Yes/No=")
    if wave == "Yes":
        speed = float(input("Speed="))
    else:
        speed = 0

    return leds, color, wave, speed


def key_event(leds,color,wave):
    global pixels

    if wave == "No":
        print("Use the SpaceKey to set the animation...")
    elif wave == "Yes":
        print("Use the asdfgh Key to set the wave animation...")

    while True:
        if getch() == " ":
            pixels.fill(color)
            pixels.show()       
        
        elif getch() == "q":
            pixels.fill((0,0,0))
            pixels.show()
            break
           
if __name__ == "__main__":
    #thread_key = threading.Thread(target=key_event)
    leds, color, wave, speed = init_set()
    
    key_event(leds,color,wave)

    #thread_key.start()

