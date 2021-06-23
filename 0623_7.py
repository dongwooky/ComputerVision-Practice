# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:42:26 2021

@author: 82106
"""

import cv2
import sys

src = cv2.imread('../Data/cv_fc_data/ch03/candies.png')

if src is None:
    print("Image load failed!")
    sys.exit()
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')
    
    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)
    
cv2.imshow('src', src)
cv2.namedWindow('dst')

cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar)
cv2.createTrackbar('H_max', 'dst', 80, 179, on_trackbar)

on_trackbar(0)
cv2.waitKey()