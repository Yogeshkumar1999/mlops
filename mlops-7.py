import cv2
import numpy as np
cap = cv2.VideoCapture(0)
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_model = cv2.CascadeClassifier('haarcascade_eye.xml')
counter = 0
#image = cv2.imread("family.jpg")
while True:
    status, image = cap.read()
    if status:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cor = model.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face_cor:
            image= cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 5)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            eye_cor = eye_model.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eye_cor:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 0, 255), 3)
        count = len(face_cor)
        org = (50,50)
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 0)
        fontscale = 1
        thickness = 2
        cv2.putText(image, 'total Faces: %d'%count, org, font, fontscale, color, thickness, cv2.LINE_AA)
        cv2.imshow("imae", image)
        k = cv2.waitKey(10)
        if k == 27:
            break
cv2.destroyAllWindows()
cap.release()
