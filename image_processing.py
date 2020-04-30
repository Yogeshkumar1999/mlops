import numpy as np
import cv2
import pandas

#image = np.random.randint(0, 125, (255, 255, 3),dtype=np.uint8)
'''
image = cv2.imread("yogesh.png", 1)
print image.shape
main_image = image[200:800, 600:1100]
blank_image = image[200:800, :500]

edited_image = image.copy()
edited_image[200:800, :500] = main_image
edited_image[200:800, 600:1100] = blank_image
cv2.imshow("image", edited_image)
k = cv2.waitKey(0)
if k == 27:
    #cv2.imwrite("new.png", image)
    cv2.destroyAllWindows()
'''
'''
image = cv2.imread("yogesh.png")
image[:,:,2] = 0


cv2.imshow("image", image)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
print image.shape
image.release()
print image.shape
'''
'''
a = np.arange(10).reshape(2,5)

print np.argmax(a)

b = np.array([2,3,34634,12,765,]).reshape(5,1)

print np.argmax(b)
'''
'''
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print type(cap)
cap.release()
cv2.destroyAllWindows()
'''
'''
image = cv2.imread("yogesh.png")

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][2] > 240:
            image[i][j][2] = 0
#new_image = image.copy()
#new_image[10:30, 50:60, 2] = 255
cv2.imshow("image", image)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()


'''
#to increase the intensity of a color
#image[:,:, 1] += 100
image = cv2.imread("yogesh.png")
b, g, r = cv2.split(image)
other_image = image.copy()
image = cv2.merge([r, g, b])
diff_image = cv2.merge([g,b,r])
cv2.imshow("image", image)
cv2.imshow("new_image", other_image)
cv2.imshow('diff', diff_image)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

