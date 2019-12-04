import board
import neopixel
import time
import random
import threading

pixels = neopixel.NeoPixel(board.D18, 150,auto_write=False)

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

    for i in range(0,255,3):
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
        
        time.sleep(0.1)
        pixels.show()

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


def blue_circle():
    global loop_flag
    
    start_point = 0
    start_point2 = 0
    start_point3 = 15
    start_point4 = 35
    start_point5 = 70
         
    while loop_flag:
        
        pixels.fill((0,0,255))

        for i in range(5):
            pixels[start_point + i] = (0,200,255)
        
        for i in range(5):
            pixels[start_point3 + i] = (0,200,255)

        for i in range(5):
            pixels[start_point2 + i] = (100,0,255)
        
        for i in range(5):
            pixels[start_point4 + i] = (100,0,255)
        
        for i in range(5):
            pixels[start_point5 + i] = (100,0,255)
        
        
        if start_point >= 144:
            start_point = 0
        
        if start_point2 >= 144:
            start_point2 = 0

        if start_point3 >= 144:
            start_point3 = 0

        if start_point4 >= 144:
            start_point4 = 0

        if start_point5 >= 144:
            start_point5 = 0


        start_point += 1
        start_point3 += 1

        start_point2 += 2
        start_point4 += 2
        start_point5 += 2
        
        pixels.show()
        time.sleep(0.01)


def blue_random():
    global loop_flag


    while loop_flag:

        
        for i in range(30,255,5):
             
            r = 0
            if i >= 100:
                g = 100
            else:
                g = i
            b = i

            blue = (r,0,b)
            whbl = (r,g,b)
            
            if i >= 200:
                g = 200
            else:
                g = i

            #pure = (100,0,255)
            pure = (r,g,b)
            
            color_list = [blue,whbl,pure]
            led_list = []
            
            print("COLOR_LIST:",color_list)

            for i in range(5):
                for cl in color_list:
                    led_list.append(cl)
 
            pixel_point = 0
            for color in led_list:
                    
                for i in range(10):
                    pixels[pixel_point] = color
                    pixel_point += 1    
            
                pixels.show()
                time.sleep(0.1)

                
        for i in reversed(range(30,255,5)):
             
            r = 0
            if i >= 200:
                g = i - 200
            else:
                g = 0
            
            b = i

            blue = (r,0,b)
            whbl = (r,g,b)
            
            if i >= 100:
                g = i - 100
            else:
                g = 0

            #pure = (100,0,255)
            pure = (r,g,b)
            
            color_list = [blue,whbl,pure]
            led_list = []
            
            print("COLOR_LIST:",color_list)

            for i in range(5):
                for cl in color_list:
                    led_list.append(cl)
 
            pixel_point = 0
            for color in led_list:
                for i in range(10):
                    pixels[pixel_point] = color
                    pixel_point += 1    
            
            pixels.show()
            time.sleep(0.1)
            
        #color_list.append(color_list.pop(0))
    
        

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
    
    pixels.fill((0,0,0))
    pixels.show()

    while True:
        key = getch()
        if key == "b":
            #soft_flash((0,0,30),"blue")
            #blue_flash()
            thread_bc.start()
        elif key == "r":
            loop_flag = False
            soft_flash((30,0,0),"red")
        elif key == "y":
            soft_flash((30,30,0),"yellow")
        elif key == "w":
            soft_flash((30,30,30),"white")
        elif key == "g":
            soft_flash((0,30,0),"green")
        elif key == "o":
            loop_flag = False
            pixels.fill((0,0,0))
            pixels.show()
        elif key == "h":
            blue_wave()
        elif key == "a":
            random_wave()
        elif key == "j":
            if 250 >= blihtness:
                blihtness += 5
        elif key == "k":
            if blihtness >= lo_blight + 5:
                blihtness -= 5 
        elif key == "q":
            loop_flag = False
            pixels.fill((0,0,0))
            pixels.show()
            break


if __name__ == "__main__":
    thread_key = threading.Thread(target=key_event)
    thread_bc = threading.Thread(target=blue_circle)
    
    thread_key.start()

