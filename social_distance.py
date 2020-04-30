import cv2
import numpy as np
import math

def position(coordinates):
    (x1, y1, x2, y2) = coordinates[0]
    (x3, y3, x4, y4) = coordinates[1]
    if x2 < x3:
        return "right"
    elif x1 > x4:
        return "left"

#cap = cv2.VideoCapture(0)
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_model = cv2.CascadeClassifier('haarcascade_eye.xml')
counter = 0
image = cv2.imread("two.jpg")
org = (50,50)
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 0, 255)
fontscale = 0.5
thickness = 1

while True:
    #status, image = cap.read()
    if 1 > 0:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cor = model.detectMultiScale(gray, 1.3, 5)
        length = len(face_cor)
        for i in range(length):
            for j in range(i+1, length):
                (x1, y1, w1, h1) = face_cor[i]
                (x3, y3, w2, h2) = face_cor[j]
                x2 = w1+x1
                y2 = h1 + y1
                x4 = w2 + x3
                y4 = h2 + y3
                pos = position([[x1, y1, x2, y2], [x3, y3, x4, y4]])
                if pos == "right":
                    points_on_first_rectangle = [[x2, y2], [x1+w1, y1]]
                    points_on_second_rectangle = [[x3, y3], [x3, y3+h2]]
                else:
                    points_on_first_rectangle = [[x1,y1],[x1, y1+h1]]
                    points_on_second_rectangle = [[x4, y4],[x3+w2, y3]]
                final_small_dist = 100000000
                final_cor = [0,0]
                for f in points_on_first_rectangle:
                    for s in points_on_second_rectangle:
                        distance = math.sqrt((s[0] - f[0])**2 + (s[1] - f[1])**2)
                        #cv2.line(image, tuple(f), tuple(s), (255, 0, 0), 1)
                        #midpoint = ((f[0]+s[0])/2, (f[1]+s[1])/2)
                        #cv2.putText(image, "dist is %s"%str(distance), midpoint, font, fontscale, color, thickness, cv2/LINE_AA)
                        if distance < final_small_dist:
                            final_small_dist = distance
                            final_cor[0] = f
                            final_cor[1] = s

                midpoint = ((final_cor[0][0] + final_cor[1][0])/2, (final_cor[0][1]+final_cor[1][1])/2)
                cv2.line(image, tuple(final_cor[0]), tuple(final_cor[1]),  color, thickness)
                final_small_dist = 3200/(final_small_dist*12)
                cv2.putText(image, "distance between two faces is %sfeet"%str(final_small_dist), midpoint, font, fontscale, color, thickness, cv2.LINE_AA)

            x,y,w,h = face_cor[i]
            image= cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 5)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            eye_cor = eye_model.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eye_cor:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 0, 255), 3)
        count = len(face_cor)
        image = cv2.putText(image, 'total Faces: %d'%count, org, font, fontscale, color, thickness, cv2.LINE_AA)
        cv2.imshow("imae", image)
        k = cv2.waitKey(1)
        if k == 27:
            break
cv2.destroyAllWindows()
#cap.release()
