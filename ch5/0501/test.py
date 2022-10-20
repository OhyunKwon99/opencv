
import sys
import numpy as np
import cv2 
src = cv2.imread('E:/goh95/AppData/Local/Programs/opencv/ch5/0501/tekapo.bmp')

if src is None:
    print('Image load failed')
    sys.exit()
    
cv2.imshow('src', src)

cv2.waitKey()
cv2.destroyAllWindows()