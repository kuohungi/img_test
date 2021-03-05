import cv2
import numpy as np

img = cv2.imread("img/cards.jpg")

width,height = 250,350
#想擷取撲克牌的四個點(畫點線找位置)
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
#想將四個點呈現的位置
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# 圖片扭曲轉換
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()