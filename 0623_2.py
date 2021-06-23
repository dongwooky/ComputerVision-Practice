# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:32:34 2021

@author: 82106
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('../Data/cv_fc_data/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
    
alpha = 3.0
dst = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)
    
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()