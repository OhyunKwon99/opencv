import cv2
import sys
import numpy as np
import time

img = np.full((400, 400, 3), 255, np.uint8)
img1 = img
cv2.line(img1, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img1, (50, 60), (150, 160), (0, 0, 128))

cv2.imshow("image", img)
cv2.imshow("img1", img1)
cv2.waitKey()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
## cap.open(1)## 이부분 심한 camera start delay 만들어냄

flag = cap.isOpened()

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

cap.set(cv2.CAP_PROP_FRAME_WIDTH , 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

fps = cap.get(cv2.CAP_PROP_FPS)

if fps == 0.0:
    fps = 30.0

time_per_frame_video = 1/fps
last_time = time.perf_counter()


while True:
    state, frame = cap.read()

    if not state:
        break
    
    
    edge = cv2.Canny(frame, 50, 100)


    ##time counting start
    time_per_frame = time.perf_counter()-last_time
    time_sleep_frame = max(0, time_per_frame_video - time_per_frame)
    time.sleep(time_sleep_frame)

    real_fps = 1.0 / (time.perf_counter()-last_time)
    print(real_fps*30)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    ##print(state) 
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
