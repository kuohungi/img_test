import cv2
import numpy as np

#製作一張圖片(一開始為全黑)
img = np.zeros((512,512,3),np.uint8)
print(img)

#矩陣為著色範圍, 後面數字為顏色(藍 綠 紅)
img[200:300,100:300] = 255,0,0

#畫線 起點 終點 顏色 寬度
#cv2.line(img,(0,0),(200,200),(0,255,0),3)
#畫對角線 終點為 寬 高(shape的第一個值為高 第二個值為寬)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#矩形 寬 高
cv2.rectangle(img,(0,0),(150,250),(0,0,255),2)
#矩形 填充
cv2.rectangle(img,(200,80),(400,150),(0,0,255),cv2.FILLED)
#圓形 中心點, 半徑, 顏色, 厚度
cv2.circle(img,(450,50),30,(255,255,0),5)

#顯示OPENCV字 最後為大小 顏色 線條粗度
cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()