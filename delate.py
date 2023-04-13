import cv2
from msaLib import MsaImage
from block import Block


location_block = 19 #第幾個block
cover_image = MsaImage('5.png')  #原圖
#從1.png 中取63 X 63 的區塊
cover_image.rows=63
cover_image.cols=63
locates = cover_image.get_block_locate()

#從cover_image取第 index 個block 存成 watermark_area，要做浮水印的區域
watermark_area = cover_image.get_block(location_block) 
watermark_area.block_to_image('F16.png')

# 加載機密影像
secret_img1 = cv2.imread('F16.png', cv2.IMREAD_GRAYSCALE)
secret_img2 = cv2.imread('F16.png', cv2.IMREAD_GRAYSCALE)
secret_width, secret_height = secret_img1.shape


# 加載載體影像
carrier_img = cv2.imread('5.png', cv2.IMREAD_GRAYSCALE)
carrier_width, carrier_height = carrier_img.shape

# 將機密影像轉換為二進制字符串
binary_secret_data1 = ''
binary_secret_data2 = ''
for y in range(secret_height):
    for x in range(secret_width):
        # 獲取像素值
        pixel1 = secret_img1[y, x]
        pixel2 = secret_img2[y, x]
        # 將像素值轉換為二進制
        binary_pixel1 = format(pixel1, '08b')
        binary_pixel2 = format(pixel2, '08b')
        # 添加到二進制字符串中
        binary_secret_data1 += binary_pixel1
        binary_secret_data2 += binary_pixel2

# 將二進制數據嵌入到載體影像中
index = 0
for y in range(0,carrier_height):
    for x in range(254,carrier_width):
        # 檢查是否還有數據需要嵌入
        if index < len(binary_secret_data1) and index < len(binary_secret_data2):
            # 獲取像素值
            pixel = carrier_img[y, x]
            # 將像素值轉換為二進制
            binary_pixel = format(pixel, '08b')
            # 將數據嵌入到最低有效位
            new_binary_pixel = binary_pixel[:-2] + binary_secret_data1[index] + binary_secret_data2[index]
            new_pixel = int(new_binary_pixel, 2)
            carrier_img[y, x] = new_pixel
            index += 1
            print("總數:",index)
        else:
            break

# 保存嵌入數據的影像
cv2.imwrite('rs5.png', carrier_img)