#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# setting up modules used in the program
from matplotlib import pyplot as plt
import numpy as np
import imutils
import glob
import time
import cv2
import os

# source 1: https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/
# source 2: https://github.com/spmallick/learnopencv/tree/master/ColorSpaces/
# source 3: https://docs.opencv.org/3.4.1/df/d9d/tutorial_py_colorspaces.html/
# source 4: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# clear the screen
os.system("cls")
# load image into array
img = cv2.imread("1-bright.jpg", 3)
# record the start time
start = time.time()
# convert image to ycrcb colouring
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# minimum red color range in ycrcb colouring
lower_red = np.array([ 10, 180,  90])
# maximum red color range in ycrcb colouring
upper_red = np.array([145, 230, 115])
# mask all colour except red
mask = cv2.inRange(ycrcb, lower_red, upper_red)
# erode outer pixels of an object in mask 
mask = cv2.erode(mask, None, iterations = 2)
# dilate outer pixels of an object in mask
mask = cv2.dilate(mask, None, iterations = 2)
# append with color
res = cv2.bitwise_and(img,img, mask= mask)
# find contours in the mask
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# initialize (x, y) center of the ball
center = None
# initialize blank picture
circle = np.zeros((480, 640, 3), np.uint8)

# if countour was found
if (len(cnts) > 0):

    # find the largest contour in the mask
    c = max(cnts, key=cv2.contourArea)
    # calculate the minimum enclosing circle
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    # calculate the centroid
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    # if the radius meets a minimum size
    if (radius > 10):

        # draw the circle
        cv2.circle(circle, (int(x), int(y)), int(radius), (255, 255, 255), 2)
        # draw the centroid
        cv2.circle(circle, center, 5, (255, 255, 255), -1)

# calculate the stop time
stop = time.time() - start
# time take
print ("Time taken to draw a circle on red ball: %s [s]." % stop)
# center pinpoint result
print ("The circle's center is located at point x-axis: %s, y-axis: %s.\n" % (center[0], center[1]))
# converted ycrcb image
print (">> ycrcb converted image result is saved as 2-bgr2ycrcb.jpg")
cv2.imwrite("2-bgr2ycrcb.jpg", ycrcb)
# masked red image
print (">> Red masked image result is saved as 3-masked.jpg")
cv2.imwrite("2-masked.jpg", res)
# draw circle image
print (">> Circle image result is saved as 4-circle.jpg")
cv2.imwrite("4-circle.jpg", circle)