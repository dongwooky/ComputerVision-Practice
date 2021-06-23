# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:47:19 2021

@author: 82106
"""

import sys
import numpy as np
import cv2

src = cv2.imread('../Data/cv_fc_data/ch03/candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()
    
print('src.shape:', src.shape)
print('src.dtype', src.dtype)

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
planes = cv2.split(src_hsv)

cv2.imshow('src', src)
cv2.imshow('planes[0]', planes[0])
cv2.imshow('planes[1]', planes[1])
cv2.imshow('planes[2]', planes[2])
cv2.waitKey()
