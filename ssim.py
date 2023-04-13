from skimage.metrics import structural_similarity as ssim
import cv2

# 讀取兩個 512x512 的圖像
img1 = cv2.imread("4.png")
img2 = cv2.imread("r4.png")

# 轉換為灰度圖像
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 計算 SSIM 值
ssim_value = ssim(gray_img1, gray_img2)

# 輸出 SSIM 值
print("SSIM value is", ssim_value)