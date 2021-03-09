import cv2
#不太準確版本
faceCascade = cv2.CascadeClassifier('img/haarcascade_frontalface_default.xml')
img = cv2.imread('img/lena.png')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray_img,1.1,2)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()