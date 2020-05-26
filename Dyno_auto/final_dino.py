import pyautogui
from PIL import ImageGrab, Image
import time
import numpy as np
pyautogui.FAILSAFE = False

def capture_screen():
    img = ImageGrab.grab()
    img = img.convert('L')
    return img

def command(c_key):
    pyautogui.keyDown(c_key)
    return

def obj_detect_rec(img_data):
    for i in range(190, 230):
        for j in range(290, 395):
            img_data[i , j] = 171
    
    for i in range(215,300):
        for j in range(397,447):
            img_data[i,j] = 0
    

def cactus_detect(img_data):
    for i in range(217,307):
        for j in range(397,450):
            if img_data[i,j] < 95:
                return True
    return False

def bird_detect(img_data):
    for i in range(190, 230):
        for j in range(290, 397):
            if img_data[i,j] < 95:
                return True
    return False

if __name__ == "__main__":
   print("Atomatic mode is going to activated")
   
   time.sleep(3)
   while True:
        cap_img = capture_screen()
        img_data = cap_img.load()
        if cactus_detect(img_data):
            command("up")
        if bird_detect(img_data):
            command("down")
        # obj_detect_rec(img_data)
        # cap_img.show()
        # break