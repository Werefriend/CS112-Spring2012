#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

#get input list
nums = input_nums()

#show input list unchanged
print "Before sort:"
print nums

#find minimum, replace successive elements starting with element 0
N = len(nums)
for x in range(N):
    min = x
    for i in range(x+1, N):
        if nums[i] < nums[min]:
            min = i
            nums[x], nums[min] = nums[min], nums[x]

print "After sort:"
print nums
