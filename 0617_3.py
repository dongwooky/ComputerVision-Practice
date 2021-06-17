import sys
import numpy as np
import cv2

img = cv2.imread('../Data/cv_fc_data/ch02/hongkong.jpg')

if img is None:
    print('Image load failed!')
    sys.exit()
tm = cv2.TickMeter()
tm.start()

edge = cv2.Canny(img, 50, 150)

tm.stop()
ms = tm.getTimeMilli()

print('Elapsed time: {}ms.'.format(ms))