import cv2
img = cv2.imread('mos.png')
img = cv2.resize(img,(63,63))
print(img)

cv2.imwrite('moss.png',img)