#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules used in the program
import os

# folders name
a = "folder1"
b = "folder2"
c = "folder3"
d = "folder4"

# create folders
os.makedirs(a)
os.makedirs(b)
os.makedirs(c + '/' + d)

print ("\nDirectory folder1/ created.")
print ("Directory folder2/ created.")
print ("Directory folder3/folder4/ created.")