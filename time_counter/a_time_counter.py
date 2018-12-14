#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up module being used in the program
import time

# record start_time
start = time.time()

while True:

    # current_time - start_time
    print(time.time() - start)

    # if 60 seconds passed
    if time.time() - start > 60:

        # stop
        end = int(time.time() - start)
        print ("\n%d [s] already passed." % end)
        break