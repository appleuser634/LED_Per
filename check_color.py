import board
import neopixel
import time
import random
import threading

pixels = neopixel.NeoPixel(board.D18, 150)

import sys
import tty
import termios
    
def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def fade_light():
    
    light_active = [0 for i in range(60)]
    light_levels = [0 for i in range(60)]
    
    r_strip = 29
    l_strip = 3
    
    r_center = 29
    l_center = 30

    while light_levels.count(255) < 60:
        
        print("levels:",light_levels.count(255))
        
        print("r_strip:",r_strip)
        print("l_strip:",l_strip)
        
        print("light_active r:",light_active[r_strip])
        print("light_active l:",light_active[l_strip])

        light_active[r_strip] = 1
        light_active[l_strip] = 1
        
        while True:
            if light_active[r_center] == 1:
                if light_levels[r_center] <= 250:
                    light_levels[r_center] += 10
                pixels[r_center] = (light_levels[r_center],0,0)
                print("r led:",(light_levels[r_center],0,0))
                r_center -= 1 
            if light_active[l_center] == 1:
                if light_levels[l_center] <= 250:
                    light_levels[l_center] += 10
                pixels[l_center] = (light_levels[l_center],0,0)
                print("l led:",(light_levels[l_center],0,0))
                l_center += 1
            else:
                r_center = 29
                l_center = 30
                break
        
        if r_strip > 0: 
            r_strip -= 1
        if l_strip < 59:
            l_strip += 1

def soft_flash(level,color):
    r_center = 74
    l_center = 75
    for i in range(75):
        pixels[r_center] = level
        pixels[l_center] = level
        
        r_center -= 1
        l_center += 1

    time.sleep(0.1)

    for i in range(75,255,5):
        print(i)

        if color == "blue":
            pixels.fill((0,0,i))
        elif color == "red":
            pixels.fill((i,0,0))
        elif color == "yellow":
            pixels.fill((i,i,0))
        elif color == "white":
            pixels.fill((i,i,i))
        elif color == "green":
            pixels.fill((0,i,0))

def random_wave():
    
    for i in range(5):
        
        for j in range(4,60,4):

            r_point = random.randint(j-4,j)
            o_point = random.randint(j-4,j)

            pixels[r_point] = (255,0,0)
            pixels[o_point] = (255,155,0)

        time.sleep(0.2)
        pixels.fill((0,0,0))


blihtness = 120
lo_blight = 50
strong = False
loop_flag = True

def blue_wave():
    global blihtness,lo_blight,strong
   
    time1 = time.time()
    while loop_flag:
        for i in range(lo_blight,blihtness,5):
            pixels.fill((0,i,i))
            time.sleep(0.08)
        print(60 * round(time.time() - time1,1))
        time1 = time.time()
        print("MAX:",blihtness)
        for i in reversed(range(lo_blight,blihtness,5)):
            pixels.fill((0,i,i))
            time.sleep(0.1)
    
    for i in range(lo_blight,blihtness,5):
        pixels.fill((0,i,i))
        time.sleep(0.08)
    
    for i in reversed(range(0,blihtness,5)):
        pixels.fill((0,i,i))
        time.sleep(0.1)

def blue_random():
    
    blue = (0,0,255)
    whbl = (0,100,255)
    pure = (0,200,255)
    
    led_list = []
    for i in range(5):
        led_list.append([blue,whbl,pure])
    
    pixel_point = 0
    for led in led_list:
        for color in led:
            for i in range(10):
                   pixels[pixel_point] = color
                   pixel_point += 1     
    
        

def blue_flash():
    g = 150
    pixels.fill((0,150,255))

    time.sleep(0.01)
    
    for i in reversed(range(0,255,5)):
        if g >= 5:
            g -= 5
            
        pixels.fill((0,g,i))

def key_event():
    global loop_flag,blihtness,lo_blight

    r = 0 
    g = 0
    b = 0

    while True:
        key = getch()
        if key == "a":
            if 254 >= r:
                r += 1
        elif key == "b":
           if 254 >= g:
                g += 1
        elif key == "c":
           if 254 >= b:
                b += 1
        elif key == "e":
            if r >= 1:
                r -= 1
        elif key == "f":
            if g >= 1:
                g -= 1
        elif key == "v":
            if b >= 1:
                b -= 1
        elif key == "a":
            print("BGR;",(r,g,b))
        elif key == "q":
            loop_flag = False
            break

        pixels.fill((r,g,b))


if __name__ == "__main__":
    thread_key = threading.Thread(target=key_event)
    thread_bw = threading.Thread(target=blue_wave)
    
    thread_key.start()

