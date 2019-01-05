#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# source 1: https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/
# source 2: https://github.com/spmallick/learnopencv/tree/master/ColorSpaces/
# source 3: https://docs.opencv.org/3.4.1/df/d9d/tutorial_py_colorspaces.html/
# source 4: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# setting up modules used in the program
import numpy as np
import imutils
import time
import cv2

# capture video from webcam
cap = cv2.VideoCapture(0)
# set video width to 640 pixels
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# set video height to 480 pixels
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# minimum red color range in ycrcb colouring
lower_red = np.array([ 10, 160, 110])
# maximum red color range in ycrcb colouring
upper_red = np.array([145, 180, 120])

while True:

    # calculate start time
    start = time.time()
    # capture frame-by-frame
    ret, frame = cap.read()
    # convert the raw frame into a format understandable by opencv
    bgr = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    # mirror the frame corresponding to y-axis
    flip = cv2.flip(bgr, 1)

    # convert frame coloring to ycrcb
    ycrcb = cv2.cvtColor(flip, cv2.COLOR_BGR2YCrCb)
    # mask all colour except red
    mask = cv2.inRange(ycrcb, lower_red, upper_red)
    # erode outer pixels of an object in mask 
    mask = cv2.erode(mask, None, iterations = 2)
    # dilate outer pixels of an object in mask
    mask = cv2.dilate(mask, None, iterations = 2)

    # find contours in the mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # initialize (x, y) center of the ball
    center = None

    # if countour was found
    if (len(cnts) > 0):

        # find the largest contour in the mask
        c = max(cnts, key = cv2.contourArea)
        # calculate the minimum enclosing circle
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        # calculate the centroid
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # if the radius meets a minimum size
        if (radius > 10):

            # draw the circle
            cv2.circle(flip, (int(x), int(y)), int(radius), (255, 255, 255), 2)
            # draw the centroid
            cv2.circle(flip, center, 5, (255, 255, 255), -1)
            # center pinpoint result
            print ("The circle's center is located at point x-axis: %s, y-axis: %s." % (center[0], center[1]))

    # calculate end time
    end = time.time() - start
    print ("Time taken to process 1 frame is %.6f [s]" % end)

    # Display the resulting frame
    cv2.imshow("Real time red circle tracking, to quit press [q].", flip)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
