import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

# 读取图像
img = cv2.imread('./picture/recontruct_image/rs1.png')

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算直方图
hist = cv2.calcHist([gray], [0], None, [255], [0, 255])

# 找到出现最多的像素值和出现次数
max_value = np.argmax(hist)
max_count = hist[max_value]

# 打印出现最多的像素值和出现次数
print("出现最多的像素值：", max_value)
print("出现次数：", max_count)


# 绘制直方图
plt.hist(gray.ravel(), 255, [0, 255])

# 显示图形
plt.show()