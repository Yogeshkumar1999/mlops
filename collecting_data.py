import cv2
import numpy as np
import os

path = os.getcwd()
print path
isDir = os.path.isdir("%s/yogesh"%path)
if not isDir:
    os.system("mkdir yogesh")
cap = cv2.VideoCapture(0)
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

counter = 0
while True:
    status, image = cap.read()
    if status:
        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cor = model.detectMultiScale(grey_image, 1.3, 5)
        if len(face_cor) > 0:
            counter += 1
            x, y, w, h = face_cor[0]
            cropped_image = grey_image[y-15:y+h+15, x-15:x+w+15]
            #cv2.rectangle(grey_image, (x, y), (x+w, y+h), (0,255,0), 5)
            if cropped_image.any():
                cv2.imshow("image", cv2.resize(cropped_image, (200, 200)))
                cv2.imwrite("%s/yogesh/yogesh_%d.jpg"%(path, counter), cropped_image)
            #cv2.imshow("image", grey_image)
        k = cv2.waitKey(1)
        if k == 27:
            break

cv2.destroyAllWindows()
cap.release()



