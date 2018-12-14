#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up module being used in the program
import time
import os

# list of variable need to be shared
a = 0
b = 5

# custom python definition: clear console
def clear_console():

    os.system("cls")

# custom python definition: typical loop
def typical_loop():

    global a
    global b
    print ("Closing the program in...")
    while (a < b):

        print ("%d" %(b - a))
        time.sleep(1)
        a += 1