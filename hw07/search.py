#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

#get input and order it
inpnums = input_nums()
nums = sorted(inpnums)
print "I have sorted your numbers like so:"
print nums

#determine search query, define minimum, maximum
x = int(raw_input("Which number should I find: "))
low = 0
high = len(nums) - 1

#find middle, test if it's the query.
#if not, half the results and try again in the correct half
while high >= low:
    mid = (high+low) / 2
    if nums[mid] == x:
        break
    elif x > nums[mid]:
       low = mid + 1
    else:
        high = mid - 1

#display the query and location or an error message
if nums[mid] == x:
    print "Found", x, "at", mid
else:
    print "Could not find", x
