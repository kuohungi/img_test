import cv2
import numpy as np



#原型
img = cv2.imread('img/jojo.jpg')

#高 寬 rgb(3):(560,640,3)
print(img.shape)

#調整大小(寬, 高)
imgResize = cv2.resize(img,(300,250))
#剪裁(高, 寬)
imgCropped = img[0:250,50:300]

cv2.imshow('pic',img)
cv2.imshow('resize', imgResize)
cv2.imshow('crop', imgCropped)


#灰階
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#線條, 
canny_img = cv2.Canny(img,100,200)
#模糊
blur_img = cv2.GaussianBlur(gray_img,(7,7),0)

kernel = np.ones((5,5),np.uint8)

#擴張
dialation_img = cv2.dilate(canny_img,kernel,iterations=1)
#侵蝕
eroded_img = cv2.erode(dialation_img,kernel,iterations=1)

#印出
cv2.imshow('pic', img)
cv2.imshow('gray', gray_img)
cv2.imshow('canny', canny_img)
cv2.imshow('blur', blur_img)
cv2.imshow('dialation', dialation_img)
cv2.imshow('eroded', eroded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
