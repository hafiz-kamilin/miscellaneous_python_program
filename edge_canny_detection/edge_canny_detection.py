#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# source: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

# setting up modules used in the program
from matplotlib import pyplot as plt
import numpy as np
import cv2

# open and applying edge canny detection
img = cv2.imread('old.jpg', 0)
edges = cv2.Canny(img, 200, 300)

# save the new image
cv2.imwrite('new.jpg', edges)

# plotting the result
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Grayscale Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Canny Detection Filter'), plt.xticks([]), plt.yticks([])

plt.show()