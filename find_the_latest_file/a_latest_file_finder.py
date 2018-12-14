#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules being used in the program
import glob
import os

files = glob.glob('findme/*')
# NOTE other case: key = str(max(files , key = os.path.getmtime))
string = str(max(files , key = os.path.getctime))

print ("\n" + string)

# NOTE
#
# os.path.getmtime(path)
# Return the time of last modification of path. The return value is a number giving the number of seconds since the epoch (see the time module). 
# Raise os.error if the file does not exist or is inaccessible.
#
# os.path.getctime(path)
# Return the system’s ctime which, on some systems (like Unix) is the time of the last change, and, on others (like Windows), is the creation time for path. 
# The return value is a number giving the number of seconds since the epoch (see the time module). Raise os.error if the file does not exist or is inaccessible.