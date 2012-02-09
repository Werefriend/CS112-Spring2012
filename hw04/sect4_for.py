#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
total = 0
for value in nums:
    total += value
    
print "1.", total


# 2. Print every even number in nums
print "2. even numbers"

for value in nums:
    if value%2 == 0:
        print value


# 3. Does nums only contain even numbers? 
only_even = True

for evens in nums:
    if evens%2 != 0:
        only_even = False


print "3.",
if only_even:
    print "only even"
else:
    print "some odd"


# 4. Generate a list of every odd number less than 100. Hint: use range()

print "4.", range(1,100,2)

# 5. [ADVANCED]  Multiply each element in nums by its index

for i in range(len(nums)):
    nums[i] *= i
print "5.", nums

