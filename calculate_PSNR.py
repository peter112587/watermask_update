import math
import cv2
import csv
import os
from skimage.metrics import structural_similarity as ssim

def read_png(image_name):
	return cv2.imread(image_name+'.png')

def calculate_psnr(n):
	s = read_png('./PSNR-SSIM-Calculator-for-Images-master/source/s'+n)
	r = read_png('./PSNR-SSIM-Calculator-for-Images-master/recovery/rs'+n)

	height, width, channel = s.shape
	size = height*width

	sb,sg,sr = cv2.split(s)
	rb,rg,rr = cv2.split(r)

	mseb = ((sb-rb)**2).sum()
	mseg = ((sg-rg)**2).sum()
	mser = ((sr-rr)**2).sum()

	MSE = (mseb+mseg+mser)/(3*size)
	psnr = 10*math.log10(255**2/MSE)

	return round(psnr,2)


def SSIM(m):
	s = read_png('./PSNR-SSIM-Calculator-for-Images-master/source/s'+m)
	r = read_png('./PSNR-SSIM-Calculator-for-Images-master/recovery/rs'+m)
	gray_img1 = cv2.cvtColor(s, cv2.COLOR_BGR2GRAY)
	gray_img2 = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
	# 計算 SSIM 值
	ssim_value = ssim(gray_img1, gray_img2)

	return round(ssim_value,2)


def write_csv(n,data):
	with open('./PSNR-SSIM-Calculator-for-Images-master/PSNR-result/'+n+'.csv', 'w', newline='') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow(data)

for i in range(6):
	print("Creating CSV of PSNR-result",i+1,"...",sep="")
	write_csv(str(i+1),[calculate_psnr(str(i+1))])

def write_SSIM_csv(m,data1):
	with open('./PSNR-SSIM-Calculator-for-Images-master/SSIM-result/'+m+'.csv', 'w', newline='') as ssim_myfile:
		wr1 = csv.writer(ssim_myfile, quoting=csv.QUOTE_ALL)
		wr1.writerow(data1)

for j in range(6):
	print("Creating CSV of SSIM-result",j+1,"...",sep="")
	write_SSIM_csv(str(j+1),[SSIM(str(j+1))])

os.system("pause")

