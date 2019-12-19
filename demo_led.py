import board
import neopixel
import time
import random
import threading

pixels = neopixel.NeoPixel(board.D18, 300, auto_write=False)

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

    for i in range(0,100,3):
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
        
        time.sleep(0.01)
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
        
        
        if start_point >= 299:
            start_point = 0
        
        if start_point2 >= 299:
            start_point2 = 0

        if start_point3 >= 299:
            start_point3 = 0

        if start_point4 >= 299:
            start_point4 = 0

        if start_point5 >= 299:
            start_point5 = 0


        start_point += 1
        start_point3 += 1

        start_point2 += 2
        start_point4 += 2
        start_point5 += 2
        
        pixels.show()
        time.sleep(0.01)
    
    pixels.fill((0,0,0))
    pixels.show()

def blue_random_fake():
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

def fade_func(led_list,color_list,status):
    
    for i,l in enumerate(led_list):
        color = color_list[i]
        if color == "blue" and status == "plus":
            led_list[i] = (0,0,led_list[i][2] + 5)
        elif color == "blue" and status == "min":
            led_list[i] = (0,0,led_list[i][2] - 5)
        elif color == "whbl" and status == "plus":
            led_list[i] = (0,led_list[i][1] + 5,led_list[i][2] + 5)
        elif color == "whbl" and status == "min":
            led_list[i] = (0,led_list[i][1] - 5,led_list[i][2] - 5)
        elif color == "pure" and status == "plus":
            if l[1] <= 90:
                led_list[i] = (0,led_list[i][1] + 5,led_list[i][2] + 5)
            else:
                led_list[i] = (0,led_list[i][1],led_list[i][2] + 5)
        elif color == "pure" and status == "min":
            if l[1] >= 10:
                led_list[i] = (0,led_list[i][1] - 5,led_list[i][2] - 5)
            else:
                led_list[i] = (0,led_list[i][1],led_list[i][2] - 5)
   
    return led_list
    
    
def blue_random():
    global loop_flag

    blue = (0,0,0)
    pure = (0,0,0)
    whbl = (0,0,0)

    led_list = [blue,whbl,pure]
    color_list = ["blue","whbl","pure"]

    while loop_flag:
        
        led_list = [(0,0,0),(0,0,0),(0,0,0)]

        for n in range(50):
            
            s = 0
            led_list = fade_func(led_list,color_list,"plus")
            
            for _ in range(10):
                for l in led_list:
                    print(l)
                    for i in range(5):
                        print(s)
                        pixels[s] = l
                        s += 1

            pixels.show() 
            time.sleep(0.01)
            
            if n % 20 == 0:
                led_list.append(led_list.pop(0))
                color_list.append(color_list.pop(0))

        for n in range(50):

            s = 0
            led_list = fade_func(led_list,color_list,"min")
            for _ in range(10):
                for l in led_list:
                    print(l)
                    for i in range(5):
                        print(s)
                        pixels[s] = l
                        s += 1

            pixels.show()
            time.sleep(0.01)

            if n % 20 == 0:
                led_list.append(led_list.pop(0))
                color_list.append(color_list.pop(0))


def blue_sea(led_list,color_list,start_point):
    print("Called thread1!")
    #5づつ明るさを上げるので50回でMax

    time1 = time.time()

    for n in range(50):
        s = start_point
        led_list = fade_func(led_list,color_list,"plus")
        l = led_list[0]
        for i in range(15):
            pixels[s] = l
            s += 1

        pixels.show()
        time.sleep(0.01)
        
        if n % 16 == 0 and n != 0:
            led_list.append(led_list.pop(0))
            color_list.append(color_list.pop(0))

    for n in range(50):
        s = start_point
        led_list = fade_func(led_list,color_list,"min")
        l = led_list[0]
        for i in range(15):
            pixels[s] = l
            s += 1
            
        pixels.show()
        time.sleep(0.01)

        if n % 16 == 0 and n != 0:
            led_list.append(led_list.pop(0))
            color_list.append(color_list.pop(0))
    
    print("Time:",int(time.time() - time1))  


def fade_func2(l,color,status):
    
    if color == "blue" and status == "plus":
        if l[2] <= 249:
            return (0,0,l[2] + 5)
    elif color == "blue" and status == "min":
        if l[2] >= 5:
            return (0,0,l[2] - 5)
    elif color == "whbl" and status == "plus":
        if l[1] <= 95:
            return (0,l[1] + 5,255)
    elif color == "whbl" and status == "min":
        if l[1] >= 5:
            return (0,l[1] - 5,255)
    elif color == "pure" and status == "plus":
        if l[1] == 0:
            l = (0,100,255)
        if l[1] <= 250:
            return (0,l[1] + 5,255)
    elif color == "pure" and status == "min":
        if l[1] >= 5:
            return (0,l[1] - 5,255)


def blue_sea2(led_list,color_list,start_point):
    
    print("Called blue_sea2!")  
    
    #5づつ明るさを上げるので50回でMax
    for n in range(1,101):
        s = start_point
        l = fade_func2(led_list[0],color_list[0],"plus")
        print(l)
        print("N:",n)
        led_list[0] = l
        print("LED_LIST:",led_list)
        for i in range(15):
            pixels[s] = l
            s += 1

        pixels.show()
        
        if color_list[0] == "blue":
            time.sleep(0.0155)
        elif color_list[0] == "whbl":
            time.sleep(0.04)
        elif color_list[0] == "pure":
            time.sleep(0.025)
        
        if n == 50:
            led_list.append(led_list.pop(0))
            color_list.append(color_list.pop(0))
        elif n == 70:
            led_list.append(led_list.pop(0))
            color_list.append(color_list.pop(0)) 

    print("WILL DOWON!")

    for n in range(1,101):
        s = start_point
        l = fade_func2(led_list[0],color_list[0],"min")
        led_list[0] = l
        print("LED_LIST:",led_list)
        for i in range(15):
            pixels[s] = l
            s += 1

        pixels.show()
 
        if color_list[0] == "blue":
            time.sleep(0.0155)
        elif color_list[0] == "whbl":
            time.sleep(0.04)
        elif color_list[0] == "pure":
            time.sleep(0.025)
        
        if n % 50 == 0 and n != 0:
            led_list.append(led_list.pop(0))
            color_list.append(color_list.pop(0))


def set_random():
    global loop_flag

    blue = (0,0,0)
    whbl = (0,0,0)
    pure = (0,0,0)
    
    #led_list = [blue,whbl,pure]
    #color_list = ["blue","whbl","pure"]

    while loop_flag:
        
        led_list = [blue,whbl,pure]
        color_list = ["blue","whbl","pure"]

        phase1 = [0,30,60,90,120]
        phase2 = [25,45,75,105,135]

        print("Phase1:",phase1)
        print("Phase2:",phase2)
         
        for p1 in phase1:

            start_point = p1
            #blue_sea2(led_list,color_list,start_point)
            thread1 = threading.Thread(target=blue_sea2, args=[[blue,whbl,pure],["blue","whbl","pure"],start_point])
        
            #start_point2 = phase2[k]

            #thread2 = threading.Thread(target=blue_sea2, args=[[blue,whbl,pure],["blue","whbl","pure"],start_point2])
    
            thread1.start()
            print("start thread1",start_point)

            #sleep_time = random.randint(0,10) * 0.1
            #time.sleep(sleep_time)

            #thread2.start()
            #print("start thread2",start_point2)
        
            print("sleep 5s...")

        time.sleep(60)
        
        for p2 in phase2:

            start_point2 = p2
            thread2 = threading.Thread(target=blue_sea2, args=[[blue,whbl,pure],["blue","whbl","pure"],start_point2])
            
            thread2.start()

def blue_flash():
    g = 150
    pixels.fill((0,150,255))

    time.sleep(0.01)
    
    for i in reversed(range(0,255,5)):
        if g >= 5:
            g -= 5
         
        pixels.fill((0,g,255))
        pixels.show()


def blue_pipe():
    global loop_flag
    
    pixels.fill((0,0,255))
    pixels.show()
    
    start_point1 = 0
    start_point2 = 150

    while loop_flag:
        pixels.fill((0,0,255))

        for i in range(50):
            if start_point1 + i <= 299:
                pixels[start_point1 + i] = (0,100,255)
            else:
                start_point1 = 0
                break
        
        for i in range(50):
            if start_point2 - i >= 0:
                print(start_point2 - i)
                pixels[start_point2 - i] = (0,100,255)
            else:
                start_point2 = 300
                break

        start_point1 += 2
        start_point2 -= 2

        pixels.show()
        time.sleep(0.03)

def blue_image():
    global loop_flag

    b = (0,0,0)
    for _ in range(50):
        b = fade_func2(b,"blue","plus")
        pixels.fill(b)
        pixels.show()

        time.sleep(0.05)

    while loop_flag:
         
        l = (0,30,255)
        for i in range(14):
            l = fade_func2(l,"whbl","plus")
            print(l)
            pixels.fill(l) 
            pixels.show()
            time.sleep(0.1)

        for i in range(29):
            l = fade_func2(l,"pure","plus")
            print(l)
            pixels.fill(l)
            pixels.show()
            time.sleep(0.1)
        for i in range(29):
            l = fade_func2(l,"pure","min")
            print(l)
            pixels.fill(l)
            pixels.show()
            time.sleep(0.1)

        for i in range(14):
            l = fade_func2(l,"whbl","min")
            print(l)
            pixels.fill(i)
            pixels.show 
            time.sleep(0.1)

def tri_blue():
    global loop_flag 

    while loop_flag:

        for i in range(0,100,5):
            
            if loop_flag == False:
                break

            n = 0
            for _ in range(20):
                for _ in range(5):
                    pixels[n] = (0,0,255)
                    n += 1
                for _ in range(5):
                    if i <= 50:
                        pixels[n] = (0,i,255)
                        n += 1
                    else:
                        pixels[n] = (0,50,255)
                        n += 1
                for _ in range(5):
                    pixels[n] = (0,i,255)
                    n += 1

            pixels.show()
         
        time.sleep(0.1)
        print("Max Light!")
        
        for i in reversed(range(0,100,5)):
            if loop_flag == False:
                break

            n = 0
            for _ in range(20):
                for _ in range(5):
                    pixels[n] = (0,0,255)
                    n += 1
                for _ in range(5):
                    if i - 50 >= 0:
                        pixels[n] = (0,i - 50,255)
                        n += 1
                    else:
                        pixels[n] = (0,0,255)
                        n += 1
                for _ in range(5):
                    pixels[n] = (0,i,255)
                    n += 1

            pixels.show()
        
        print("Min Linght!")

def random_blue():
    
    color_set = [(0,0,255),(0,50,255),(0,100,255)]
    
    n = 0
    for _ in range(60):
        
        color = random.randint(0,2)

        for _ in range(5):
            pixels[n] = color_set[color]
            n += 1
    
    pixels.show()

def ending():
    
    for i in reversed(range(0,155)):    
        
        flash_point = [random.randint(0,299) for i in range(20)]
        flash_point2 = [random.randint(0,299) for i in range(20)]
    
        for l in flash_point:
            pixels[l] = (i,i,i)
        for l in flash_point2:
            pixels[l] = (0,i,i)

        pixels.show()
        time.sleep(0.01)
        pixels.fill((0,0,0))

def key_event():
    global loop_flag,blihtness,lo_blight,preset_n
    
    pixels.fill((0,0,0))
    pixels.show()

    time.sleep(2)
    while True:
        
        key = getch()

        if key == "a":
            if preset_n >= 0:
                preset_n -= 1
                preset_con()

        elif key == "b":
            if preset_n <= 8:
                preset_n += 1
                preset_con()
        
        elif key == "c":
            loop_flag = False
            blue_flash()
            loop_flag = True
            preset_con()

        elif key == "q":
            pixels.fill((0,0,0))
            pixels.show()
            break
        
        #if key == "b":
            #soft_flash((0,0,30),"blue")
            #blue_flash()
        #    thread_bc.start()
        #elif key == "r":
        #    loop_flag = False
        #    soft_flash((30,0,0),"red")
        #elif key == "m":
        #    blue_random()
        #elif key == "v":
        #    blue_pipe()
        #elif key == "n":
        #    blue_flash()
        #elif key == "c":
            #soft_flash((0,0,30),"blue")
            #thread_bf.start()
        #    loop_flag = False
        #    blue_flash()
        #    loop_flag = True
        #    blue_circle()

        #elif key == "w":
        #    soft_flash((30,30,30),"white")
        #elif key == "g":
        #    soft_flash((0,30,0),"green")
        #elif key == "o":
        #    loop_flag = False
        #    pixels.fill((0,0,0))
        #    pixels.show()
        #elif key == "h":
        #    blue_wave()
        #elif key == "a":
            #random_wave()
       #     set_random()
        #elif key == "j":
        #    if 250 >= blihtness:
        #        blihtness += 5
        #elif key == "k":
        #    if blihtness >= lo_blight + 5:
        #        blihtness -= 5 
        #elif key == "q":
        #    loop_flag = False
        #    pixels.fill((0,0,0))
        #    pixels.show()
        #    break


def preset_con():
    global preset_n,loop_flag

    preset = ["1","3","1","2","6","5","1","1","4"]

    if preset[preset_n] == "1":
        loop_flag = False
        time.sleep(1)
        loop_flag = True
        thread_bt = threading.Thread(target=tri_blue)
        thread_bt.start()
    elif preset[preset_n] == "2":
        loop_flag = False
        time.sleep(1)
        loop_flag = True 
        thread_bc = threading.Thread(target=blue_circle)
        thread_bc.start()
        #blue_circle()
    elif preset[preset_n] == "3":
        loop_flag = False
        pixels.fill((0,255,255))
        pixels.show()
    elif preset[preset_n] == "4":
        loop_flag = False
        time.sleep(1)
        ending()
    elif preset[preset_n] == "5":
        loop_flag = False
        soft_flash(30,"red")
    elif preset[preset_n] == "6":
        loop_flag = False
        time.sleep(0.5)
        random_blue()
    
if __name__ == "__main__":
    thread_key = threading.Thread(target=key_event)
    #thread_bc = threading.Thread(target=blue_circle)
    #thread_bf = threading.Thread(target=blue_flash)
    
    preset_n = -1
    thread_key.start()
