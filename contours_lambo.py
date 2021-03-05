import cv2
import numpy as np

# 堆疊圖片
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#擷取邊線並繪製
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(contour_img,cnt,-1,(255,0,0),3)
        
path = 'img/lambo.png'
img = cv2.imread(path)
imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


lower = np.array([0,110,153])
upper = np.array([19,240,255])

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 遮罩
mask = cv2.inRange(imgHSV,lower,upper)
# 著原色
imResult = cv2.bitwise_and(img,img,mask=mask)

#模糊化 值越大越模糊
blur_img = cv2.GaussianBlur(gray_img,(7,7),1)
#輪廓
canny_img = cv2.Canny(mask,50,50)
#邊線
contour_img = imResult.copy()
getContours(canny_img)


imgStack = stackImages(0.6,([img,canny_img],[contour_img,imResult]))
cv2.imshow("Stacked Images", imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()