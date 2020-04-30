import cv2
import os
import numpy as np
import pickle
import webbrowser as wb

path = os.getcwd()
path = os.path.join(path, 'yogesh')
onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

training_data, lable = [], []

for i, files in enumerate(onlyfiles):
    image_path = os.path.join(path, files)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    training_data.append(np.asarray(image, dtype=np.uint8))
    lable.append(i)

print training_data
print lable
Labels = np.asarray(lable, dtype=np.int32)
all1 = dir(cv2)


model=cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(training_data), np.asarray(Labels))
print "model trained"
print model
#pickle.dump(model, 'face_reocgnition.pkl')

cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    status, image = cap.read()
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        results = model.predict(gray)
        print results
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)

        if confidence > 86:
            cv2.putText(image, "Hey yogesh", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            #break

        else:
            cv2.putText(image, "i dont know", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
#wb.open('https://www.google.com/')



            
        
        

