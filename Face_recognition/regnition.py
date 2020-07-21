import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

dataset_path = 'D:/5th/innovative_mini_project/Face_recognition/Data/'
files = [face for face in listdir(dataset_path)] # if isfile(join(dataset_path, face))

train_data, labels = [], []
for i , f in enumerate(files):
    image_path = dataset_path + files[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    train_data.append(np.asarray(images))
    labels.append(i)

labels = np.asarray(labels)

model = cv2.face.LBPHFaceRecognizer_create() #Linear binary phase histogram face recognizer

model.train(np.asarray(train_data), labels)
print("Trainin Successful")

face_classify = cv2.CascadeClassifier('C:/Users/Sumagna Dey/AppData/Local/Programs/Python/Python38/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def facedetect(img):
    gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_classify.detectMultiScale(gs,1.2, 6)

    if face == ():
        return img, []
    
    for (x, y, w,h) in face:
        cv2.rectangle(img, (x , y), (x + w,y + h), (0, 0, 255), 2)
        roi = img[y : y + h, x : x + w]
        roi = cv2.resize(roi,(250,250))
    return img, roi

cap = cv2.VideoCapture(0)
while True:
    ret, frm = cap.read()
    image, face = facedetect(frm)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        res = model.predict(face)
        if res[1] < 450:
            confid = int((1 - ((res[1])/250))*100)
            res_str = str(confid) + "% match"
        cv2.putText(image, res_str, (0,100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,0,2))
            
        if confid > 82:
            cv2.putText(image, "Welcome Admin", (250, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,255,0))
            cv2.imshow("Face Recognizer", image)
            
        else:
            cv2.putText(image, "Access Denied", (250, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,0,255))
            cv2.imshow("Face Recognizer", image)
    except:
        cv2.putText(image, "Can't detect face", (250, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(190,120,255))
        cv2.imshow("Face Recognizer", image)
        pass

    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()