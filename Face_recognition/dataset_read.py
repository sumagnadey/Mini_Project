import cv2
import numpy as np

face_classify = cv2.CascadeClassifier('C:/Users/Sumagna Dey/AppData/Local/Programs/Python/Python38/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def face_cap(val,img):
    gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_classify.detectMultiScale(gs,1.2, 6)
    
    if val:
        for (x,y,w,h) in face:
            crop_img = img[y:y+h,x:x+w]
            return cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    else:
        return None
cap = cv2.VideoCapture(0)
count = 0

while True:
    r, f = cap.read()
    if face_cap(r,f) is not None:
        count+= 1
        face = cv2.resize(face_cap(r,f), (250,250))
        file_path = 'D:/5th/innovative_mini_project/Face_recognition/Data/admin_img' + str(count) + '.jpg'
        cv2.imwrite(file_path, face)
        cv2.putText(face, str(count),(45,45),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),1)
        cv2.imshow('Face Crop', face)
    
    else:
        print("Face not fount")

    if(cv2.waitKey(1) == 13 or count == 150):
        break
cap.release()
cv2.destroyAllWindows()
print("Data Collect successful")