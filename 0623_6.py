# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:49:51 2021

@author: 82106
"""

import numpy as np
import cv2

def on_level_changed(pos):
    global img
    
    level = pos * 16
    level = np.clip(level, 0, 255)
    
    img[:, :] = level
    cv2.imshow('image', img)
    
img = np.zeros((480, 640), np.uint8)

cv2.imshow('image', img)
cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)

cv2.waitKey()
cv2.destroyAllWindows()