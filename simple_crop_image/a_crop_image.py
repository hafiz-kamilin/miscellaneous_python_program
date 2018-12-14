#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules being used in the program
import matplotlib.pyplot as plt
import cv2

# load the image
original = cv2.imread("image/original.jpg")
# crop the image [height_to_be_cropped:original_height width_to_be_cropped:original_width]
cropped = original[200:226, 200:400]
cv2.imwrite('image/cropped.jpg', cropped)

# plot
plt.subplot(2, 1, 1)
plt.imshow(original)
plt.subplot(2, 1, 2)
plt.imshow(cropped)
plt.show()