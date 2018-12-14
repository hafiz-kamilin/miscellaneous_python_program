#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# class for unix-like getch
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# print instruction
print ("Please enter something: ")
# read user input and save in into x
x = getch()
# print user input saved in x
print(x)