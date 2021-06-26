# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:38:20 2021

@author: 82106
"""

import numpy as np
import sys
import cv2

src = cv2.imread('../Data/cv_fc_data/ch03/cropland.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()
    
x, y, w, h = cv2.selectROI(src)

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop = src_ycrcb[y:y+h, x:x+w]

