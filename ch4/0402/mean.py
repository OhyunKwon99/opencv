import sys
import cv2
import numpy as np

src = cv2.imread("/ch4/0402/rose.bmp")

if src is None:
    print('Image load failed')
    sys.exit()
    
kernel = np.array([[1/9, 1/9, 1/9], 
                   [1/9, 1/9, 1/9], 
                   [1/9, 1/9, 1/9]], dtype = np.float64)

dst = cv2.filter2D(src, -1, kernel)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

