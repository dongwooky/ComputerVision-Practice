# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:44:27 2021

@author: 82106
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

src = cv2.imread('../Data/cv_fc_data/ch03/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['blue', 'green', 'red']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color = c)


cv2.imshow('src', src)
cv2.waitKey(1)

plt.plot(hist)
plt.show()
