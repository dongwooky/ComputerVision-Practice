import sys
import numpy as np
import cv2

cap1 = cv2.VideoCapture('../Data/cv_fc_data/ch02/video1.mp4')
cap2 = cv2.VideoCapture('../Data/cv_fc_data/ch02/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()
    
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS: ', fps)

delay = int(1000 / fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()
    
    if not ret1:
        break
    
    out.write(frame1)
    
    cv2.imshow('frame', frame1)
    cv2.waitKey(delay)
    
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    if not ret1 or not ret2:
        break
    
    dx = int(w * i / effect_frames)
    
    frame = np.zeros((h, w, 3), dtype = np.uint8)
    """
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]
    """
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]
    
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)
    
    
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()
    
    if not ret2:
        break
    
    out.write(frame2)
    
    cv2.imshow('frame', frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()