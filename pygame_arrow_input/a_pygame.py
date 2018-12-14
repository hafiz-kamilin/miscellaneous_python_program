#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# setting up modules used in the program
from pygame.locals import *
import pygame
import time
import os

# initialize pygame
import pygame.display
pygame.display.init()
screen = pygame.display.set_mode((250,250))

# print instruction
print("\nClick on pygame small windows and try pressing the keyboard arrow keys.")
print("To quit press q key.\n")

# loop initialization
loop = True

while loop:

    # get user input to control the rover
    for event in pygame.event.get():
        
        # when the key was pressed down
        if event.type == KEYDOWN:
                
            # register the pressed down key
            user_input = pygame.key.get_pressed()

            # if it is ↑
            if user_input[pygame.K_UP]:
                    
                print("UP")

            # if it is →
            elif user_input[pygame.K_RIGHT]:
                    
                print("RIGHT")

            # if it is ←
            elif user_input[pygame.K_LEFT]:

                print("LEFT")

            # if it is ↓
            elif user_input[pygame.K_DOWN]:

                print("DOWN")
                
            # to end the program press q or x
            elif user_input[pygame.K_q]:
                    
                loop = False
                break

        # key break
        elif event.type == pygame.KEYUP:

            time.sleep(0.1)
            break