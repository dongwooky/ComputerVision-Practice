# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:44:27 2021

@author: 82106
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

src = cv2.imread('../Data/cv_fc_data/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
    
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('src', src)
cv2.waitKey(1)

plt.plot(hist)
plt.show()

src = cv2.imread('lenna.bmp')
