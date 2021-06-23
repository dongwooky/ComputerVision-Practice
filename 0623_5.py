# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:16:30 2021

@author: 82106
"""

import cv2

src = cv2.imread('../Data/cv_fc_data/ch03/candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()
    
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()