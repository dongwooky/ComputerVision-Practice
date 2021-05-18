import sys
import cv2

cap = cv2.VideoCapture('video1.mp4')

if not cap.isOpened():
    print('video open failed!')
    sys.exit()
    
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)
    
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    edge = cv2.Canny(frame, 50, 150)
    
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    if cv2.waitKey(20) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()