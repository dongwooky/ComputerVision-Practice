# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:08:12 2021

@author: 82106
"""

import cv2

ref = cv2.imread('../Data/cv_fc_data/ch03/kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('../Data/cv_fc_data/ch03/kidst2.png', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()
    
ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)
