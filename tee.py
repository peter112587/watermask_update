import cv2
import numpy as np
img = cv2.imread('org_64.png')
sigma = 100
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
#img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
#canny = cv2.Canny(img, 30, 150)

#img = cv2.bitwise_not(img)
usm1 = cv2.threshold(img,40,127,cv2.THRESH_BINARY)[1]
blur_img = cv2.GaussianBlur(usm1, (0, 0), sigma)
usm = cv2.addWeighted(usm1, 1.5, blur_img, -0.5, 0)


# 保存處理後的圖片
cv2.imwrite('transparent_img.png', usm1)
cv2.imshow('wwww', usm)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()