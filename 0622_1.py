import sys
import numpy as np
import cv2

src = cv2.imread('../Data/cv_fc_data/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.add(src, 100)

#dst = src + 100

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()