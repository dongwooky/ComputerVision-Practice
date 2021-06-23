# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:02:03 2021

@author: 82106
"""
import numpy as np
import cv2

src = cv2.imread('../Data/cv_fc_data/ch03/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

gmin = np.min(src)
gmax = np.max(src)
dst = np.clip((src - gmin) * 255. / (gmax - gmin), 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()