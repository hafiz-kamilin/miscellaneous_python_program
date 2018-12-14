#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# class for windows getch
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _GetchWindows()

# print instruction
print ("Please enter something: ")
# read user input and save in into x
x = getch()
# print user input saved in x
print(x)