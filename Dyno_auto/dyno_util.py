import pyautogui
from PIL import ImageGrab, Image
import time
import numpy as np
pyautogui.FAILSAFE = False

def capture_screen():
    img = ImageGrab.grab()
    img = img.convert('L')
    # img.show()
    return img

def command(c_key):
    pyautogui.keyDown(c_key)

# def obj_detect_rec(img_data):
#     for i in range(190, 230):
#         for j in range(290, 398):
#             img_data[i , j] = 0
    
#     for i in range(200,245):
#         for j in range(398,475):
#             img_data[i,j] = 170
    

def collition(img_data):
    for i in range(190, 230):
        for j in range(300, 398):
            if img_data[i,j] < 100:
                command("down")   
    
    for i in range(200,245):
        for j in range(398,475):
            if img_data[i,j] < 100:
                command("up")
# img_mat = np.asarray(capture_screen())
# print(img_mat)
if __name__ == "__main__":
   print("Atomatic mode activated")
   time.sleep(2)
#    command('up')
   while True:
       cap_img = capture_screen()
       img_data = cap_img.load()
       collition(img_data)
    #    obj_detect_rec(img_data)
    #    cap_img.show()
    #    break