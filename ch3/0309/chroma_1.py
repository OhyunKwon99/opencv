import sys 
import numpy as np
import cv2

#배경 동영상 로드
cap2 = cv2.VideoCapture("raining.mp4")
if not cap2.isOpened():
    print('video open failed!')
    sys.exit()
    
#녹색 배경 동영상 로드
cap1 = cv2.VideoCapture('woman.mp4') #괄호안에 0이면 노트북 캠으로 대체

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()
    

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
#프레임 수치 저장
print('frame_cnt1', frame_cnt1)
print('frame_cnt2', frame_cnt2)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))

h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)


#합성여부 플레그
do_composit = False

#전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()
    
    if not ret1: #영상이 모두 재생되면 더이상 불러올 프레임이 없어 break 로 loop탈출
        break
    
    
    #합성여부가 True일때만 합성
    if do_composit is True:
        ret2, frame2 = cap2.read()
        
        if not ret2:
            break #영상이 모두 재생되면 더이상 불러올 프레임이 없어 break 로 loop탈출
    
        frame2 = cv2.resize(frame2, (w, h))
        
        #HSV 색공간으로 변환, 녹색영역을 검출하여 합성에 사용
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        ## frame1의 mask 부분만 떄서 frame2에 붙힘  
        cv2.copyTo(frame2, mask, frame1)
        
    cv2.imshow('frame',frame1)

    #프레임 사이사이 시간을 정확히 계산하여 delay부여
    key = cv2.waitKey(delay)
    
    # 스페이스바로 합성여부 플레그 토글
    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()   
        