import sys
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print('camera open failed!')
    sys.exit()
    
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

