import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0)
cap.open(0)

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

while True:
    state, frame = cap.read()

    if not state:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
