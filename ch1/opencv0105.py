import sys

import cv2


print(cv2.__version__)

img = cv2.imread('test.bmp', cv2.IMREAD_COLOR)

if img is None:
    print("Image load faild")
    sys.exit()


cv2.namedWindow('image', flags=cv2.WINDOW_FULLSCREEN)
cv2.imshow('image',img)

cv2.imwrite("viper.png", img)

conv_img = cv2.imread('viper.png', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image1', flags=cv2.WINDOW_NORMAL)
cv2.imshow('image1',conv_img)




while True:
    if cv2.waitKey() == 27:
        break
    
##key = cv2.waitKey() ##이 함수가 실행되고 끝나야 사진이나 영상 화면에 나타남
## waitKey는 기다릴때 -1 계속 반환 키보드 눌리면 눌린 값 반환
## esc == 27, enter == 13, tab == 9
##print(key) ##waitkey는 키보드 입력값을 asciicode로 return함
## asciicode로 해석하는거 대신 ord('알파벳') 함수로 직접적인 ascii code 몰라도됨

cv2.resizeWindow('image1', 10, 10)  ##애초에 정의된 윈도우가 normalsize로 선언되어 있었어야 함
cv2.moveWindow('image1', 50, 50)

while True:
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows() ##이거는 비필수 특정함수끝나고 꺼지길 원한다면 그때 넣어주면되는 구문
#############
