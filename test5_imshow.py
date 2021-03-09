import cv2
import numpy as np

#堆疊圖片
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
        #面積超過多少才畫框線
        print(area)
        if area>500:
            #在contour_img上畫線
            cv2.drawContours(contour_img, cnt, -1, (255, 0, 0), 3)
            #找輪廓弧長 封閉為True
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            #算有多少拐彎點 乘上分辨率
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))           
            #繪製矩形邊框
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)  
            #判斷幾邊形 並標註
            if objCor == 3:ObjectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:ObjectType = "Square"
                else:ObjectType = "Rectangle"
            elif objCor > 4:ObjectType = "Circles"
            else:ObjectType = "None"
            
            cv2.rectangle(contour_img,(x,y),(x+w,y+h),(0,255,0),2)
            #字體位置 字形大小 顏色 縮放
            cv2.putText(contour_img,ObjectType,(x+w//2-10,y+h//2-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)

path = 'img/shapes.png'
img = cv2.imread(path)
contour_img = img.copy()

HSV_img= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lower = np.array([2,44,0])
upper = np.array([179,255,255])
mask = cv2.inRange(HSV_img,lower,upper)
imResult = cv2.bitwise_and(img,img,mask=mask)

#模糊化 值越大越模糊
blur_img = cv2.GaussianBlur(gray_img,(7,7),1)
#邊線
canny_img = cv2.Canny(blur_img,50,50)
getContours(canny_img)
blank_img = np.zeros_like(img)

# cv2.imshow('original',img)
# cv2.imshow('gray',gray_img)
# cv2.imshow('blur',blur_img)
#堆疊 大小設定 排列
stack_img = stackImages(0.6,([img,gray_img,blur_img],[canny_img,contour_img,imResult]))
cv2.imshow('stack',stack_img)

cv2.waitKey(0)
cv2.destroyAllWindows()