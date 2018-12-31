#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# setting up modules used in the program
import numpy as np
import argparse
import glob
import cv2

# source 1: https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/
# source 2: https://github.com/spmallick/learnopencv/tree/master/ColorSpaces/

# mouse callback function
def showpixelvalue(event, x, y, flags, param):

    global img, combinedresult, placeholder
    
    if event == cv2.EVENT_MOUSEMOVE:

        # get the value of pixel from the location of mouse in (x,y)
        bgr = img[y,x]

        # convert the bgr pixel into other colro formats
        ycb = cv2.cvtColor(np.uint8([[bgr]]),cv2.COLOR_BGR2YCrCb)[0][0]
        lab = cv2.cvtColor(np.uint8([[bgr]]),cv2.COLOR_BGR2Lab)[0][0]
        hsv = cv2.cvtColor(np.uint8([[bgr]]),cv2.COLOR_BGR2HSV)[0][0]
        
        # create an empty placeholder for displaying the values
        placeholder = np.zeros((img.shape[0], 400, 3), dtype = np.uint8)

        # fill the placeholder with the values of color spaces
        cv2.putText(placeholder, "BGR {}".format(bgr), (20, 70), cv2.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(placeholder, "HSV {}".format(hsv), (20, 140), cv2.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(placeholder, "YCrCb {}".format(ycb), (20, 210), cv2.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(placeholder, "LAB {}".format(lab), (20, 280), cv2.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv2.LINE_AA)
        
        # combine the two results to show side by side in a single image
        combinedresult = np.hstack([img,placeholder])
        
        cv2.imshow("[p] previous image, [n] next image, [esc] quit.", combinedresult)


if __name__ == '__main__' :
    
    global img

    # load the image and setup the mouse callback function
    files = glob.glob("*.jpg")
    files.sort()
    print(files)
    img = cv2.imread(files[0])
    img = cv2.resize(img,(400,400))
    cv2.imshow("[p] previous image, [n] next image, [esc] quit.", img)

    # Create an empty window
    cv2.namedWindow("[p] previous image, [n] next image, [esc] quit.")
    # Create a callback function for any event on the mouse
    cv2.setMouseCallback("[p] previous image, [n] next image, [esc] quit.", showpixelvalue)
    i = 0

    while(1):

        k = cv2.waitKey(1) & 0xFF
        # check next image in the folder

        if k == ord(b'n'):

            i += 1
            img = cv2.imread(files[i%len(files)])
            img = cv2.resize(img,(400,400))
 
        # check previous image in folder
        elif k == ord(b'p'):

            i -= 1
            img = cv2.imread(files[i%len(files)])
            img = cv2.resize(img,(400,400))

        # quit
        elif k == 27:

            cv2.destroyAllWindows()
            break