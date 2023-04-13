import cv2

cover_img = cv2.imread('1.png')
sc_img = cv2.imread('block_64.png')

for i in range(0,63):
    for j in range(0,63):
        cover_img[0][j+255] = sc_img[i][j]


cv2.imwrite('r1.png', cover_img)
cv2.imshow('img',cover_img)
cv2.waitKey(0)
cv2.destroyAllWindows()