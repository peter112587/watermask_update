import cv2
from point import Point
from block import Block
from image import Image
import numpy as np
import logging

class MsaImage:
    '''
        W: 圖檔寬
        H: 圖檔高
        cols: block 寬
        rows: block 高
    '''
    W: int
    H: int    
    _cols: int
    _rows: int
    locates = []
    blocks = [tuple]


    def __init__(self, filename:str) -> None:
        '''
            filename: 檔名
            x: block 寬
            y: block 高 
        '''
        self.image = cv2.imread(filename=filename)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

        self.W = self.image.shape[0]
        self.H = self.image.shape[1]

    @property
    def cols(self) ->int:
        return self._cols

    @cols.setter    
    def cols(self, x: int):
        self._cols = x

    @property
    def rows(self) ->int :
        return self._rows        


    @rows.setter
    def rows(self, y: int):
        self._rows = y    

    def get_block(self,index)->Block:
        ''' 傳回第 index 個 block 的物件'''
        x: int = self.locates[index].x
        y: int = self.locates[index].y
        
        #block 為一個 cols X rows 大小的block
        block = [[0 for x in range(self.cols)] for y in range(self.rows)]
        for i in range(x, x + self.cols):
            for j in range(y, y + self.rows):
                 
                if (x+self.cols<self.W)>0 and (y+self.rows<self.H):
                    block[i - x][j - y] = self.image[i][j]
                else:
                    continue    
        block_obj = Block(block)  
        block_obj.x= x
        block_obj.y= y     
        return block_obj        


    def set_block(self,index:int,block:Block)->Image:
        '''將block 塞回第index 位置'''
        s =64
        ratio = self.W // s
        x = index//ratio #更改 512/128 = 4
        y = index%ratio #更改
        print(f'(x,y)=({x},{y})')
        for i in range(self.cols):
            for j in range(self.rows):
                self.image[(x)*s+i][(y)*s+j]= block[j][i]

        return self.image        
   
    def get_block_locate(self) -> list:
        ''' 將一張影像依 NXN 大小分割成小的block,
            並把位置記錄在p的物件，位置從(0,0),(0,N),(0,2N)...開始
            存放在locates 的list 
            return locates list
        '''

        self.locates = []
        for i in range(0, self.W, self.cols):
            for j in range(0, self.H, self.rows):
                p = Point(i, j)
                self.locates.append(p)
        return self.locates
    

    def to_binary_image(self) ->Image:
        '''將圖轉為binary'''
        #sigma = 1.5   
        blur_img = cv2.GaussianBlur(self.image, (11, 11), sigmaX=100, sigmaY=100) 
        self.image = cv2.addWeighted(self.image, 2, blur_img, 0.5, 0)

        height, width = self.image.shape[:2]
        img_bw = np.array(self.image).reshape(height, width)
        img_bw = abs(img_bw/255)
        #img_bw = np.where(img_bw >= 250, 1, 0)
        

           
        #blur_img = cv2.GaussianBlur(self.image, (0, 0), sigma)
        #img_bw = cv2.addWeighted(self.image, 2, blur_img, 1.5, 0)
        #GrayImage = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        #img_bw = cv2.threshold(img_bw,48,50,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]#255 黑色 0 白色
        #kernel = np.ones((5, 5), np.uint8)
        #img_bw = cv2.morphologyEx(img_bw, cv2.MORPH_CLOSE, kernel)
        #img_bw = cv2.bitwise_not(img_bw) 
        #threshold =48
        #img_bw[img_bw<threshold]=0
        #img_bw[img_bw == 50] = 1
        
        return img_bw
    
    def carrier_image_with_secret_data(self) ->Image:
        self.image

    @classmethod
    def reconstruct_image(cls,blocks,cols=64,rows =64, w=2,h=2)->Image:
        dst: Image
        dst = np.zeros([rows,cols],dtype=int)
        for block in blocks:
            x = block.x
            y = block.y
            for i in range(w):
                for j in range(h):
                    dst[x*w+i][y*h+j] = block.block[i][j]
        print(type(dst))    
        cv2.imwrite('watermarker.png',dst)
        # dst = cv2.imread('watermarker.png')
        # dst = cv2.GaussianBlur(dst, (0, 0), sigmaX=1, sigmaY=1)
        return dst                    
    
    