#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up module being used in the program
import b_shared
import os

# clear screen
os.system("cls")

# access variables from custom module
print ("Access variables from python script loaded as module.\n")
print ("b_shared.py int    'a': %s" % b_shared.a)
print ("b_shared.py string 'b': %s" % b_shared.b)
print ("b_shared.py array  'c': %s\n" % b_shared.c)