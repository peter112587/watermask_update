import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import cv2

# 讀取圖片
img = Image.open('./picture/recontruct_image/rs6.png')
img2 = Image.open('./picture/block/Peppers_block.png')
# 轉換為NumPy數組
img_arr = np.array(img2)

# 計算直方圖
hist, bins = np.histogram(img_arr.ravel(), bins=256)
# 找到出現最多次的像素值以及出現的次數
max_value = np.argmax(hist)
max_count = hist[max_value]

# 打印出现最多的像素值和出现次数
print("出现最多的像素值：", max_value)
print("出现次数：", max_count)

# 繪製直方圖
plt.hist(img_arr.ravel(), bins=256, range=(0, 256), color='r')
plt.show()

# 輸出結果到Excel文件
df = pd.DataFrame({'bin_left': bins[:-1], 'bin_right': bins[1:], 'count': hist})
df.to_excel('./historgram_excel/Peppers_block.xlsx', index=False)