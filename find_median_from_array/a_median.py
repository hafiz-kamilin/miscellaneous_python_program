#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# define way to find middle of a list in array
def median_list(array):

    # sort array
    array.sort()

    # divide array length by 2 to find middle number position
    middle = float(len(array)) / 2

    # if middle number is whole number (array with odd number length)
    if (middle.is_integer() == False):

        return array[int(middle - 0.5)]

    # if middle number is not whole number (array with even number length)
    elif (middle.is_integer() == True):

        return ((array[int(middle)] + array[int(middle - 1)]) / 2)

# data list (odd number length)
odd1 = 4
odd2 = 3
odd3 = 1
odd4 = 2
odd5 = 5

# data list (even number length)
even1 = 6
even2 = 4
even3 = 2
even4 = 1
even5 = 3
even6 = 5

# arrange data in array (odd number length) without sorting
odd_array = [odd1, odd2, odd3, odd4, odd5]

# arrange data in array (even number length) without sorting
even_array = [even1, even2, even3, even4, even5, even6]

# find median
median_odd_array = median_list(odd_array)
median_even_array = median_list(even_array)

# median
print ("\nMedian for odd number length of array contain [4, 3, 1, 2, 5] is %s." % median_odd_array)
print ("Median for even number length of array contain [6, 4, 2, 1, 3, 5] is %s." % median_even_array)