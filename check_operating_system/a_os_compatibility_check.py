#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules being used in the program
import os

# Unix-like OS only
if os.name != 'poxis':

    raise Exception("This codes only compatible with Unix-like OS (Linux, MacOS, etc)!")

# Windows NT OS only
if os.name != 'nt':
    
    raise Exception("This codes only compatible with NT based OS (Windows 2000, XP, Vista, 7, 8, 10)!")

# exit gracefully without raising Exception (Unix-like OS only)
if os.name != 'posix':

    print ("This codes only compatible with Unix-like OS (Linux, MacOS, etc)!")
    exit()

# exit gracefully without raising Exception (Windows NT OS only)
if os.name != 'nt':
    
    print ("This codes only compatible with Windows NT based OS (Windows 2000, XP, Vista, 7, 8, 10)!")
    exit()
