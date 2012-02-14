#!/usr/bin/env python
"""lists.py

A bunch of excercises to see if you understand list comprehensions
"""

# Solve the following problems with one python statement.  It is fine 
# to break up the statement into multiple lines as long as it is only
# one actual command.
#
# This is fine:
#   print [ (x,y) 
#           for x in range(10)
#           for y in range(10) ]
#

# 1. Read a bunch of numbers from the input separated by spaces and 
#    convert them to ints

print "1.", [ int(i) for i in raw_input().split(" ") ]


# 2.  Read another bunch of numbers, convert them, and return the list 
#     of only the first 3

print "2.", [ int(i) for i in raw_input().split(" ") ][:3]


# 3.  Read a bunch of words separated by commas from the command line,
#     remove any excess spaces, and print a list of their lenghts

print "3.", [ len(s.strip()) for s in raw_input().split(",") ]


# 4.  Create a list of every multiple of 3 between 1 and 100 with their 
#     index
#        ex:  [ [0,3], [1,6], [2,9]...]

print "4.", [ (i,v) for i,v in enumerate(range(3,100,3)) ]

# 5. create a list of every card in a deck of card

print "5.", [(s,t) for s in ["spades","hearts","diamonds","clubs"] for t in ["A","2","3","4","5","6","7","8","9","J","Q","K"]]

# 6.  Create a 5 by 5 array filled with zeros

print "6.", [[ 0 for i in range(5) ] for j in range(5) ]

# 7.  Make a list of every perfect square between 1 and 1000

print "7.", [ i**2 for i in range(100) if i**2 < 1000 ]

# 8.  Make a list of every perfect square between 1 and 1000 
#     a different way
import math
print "8.", [ i for i in range(1000) if math.sqrt(i) % 1 == 0 ]

# 9.  List every python file in this directory
import os
print "9.", [ s for s in os.listdir(".") if s.endswith(".py")]

# 10.  Print a list of every pythagorean triple with a side less than
#      or equal to 20.  Don't include duplicates ([3,4,5] == [4,3,5])

print "10.", [ (x,y,z) 
               for x in range(1,21)
               for y in range(1,21)
               for z in range(1,21)
               if x**2 + y**2 == z**2 
                  and x >= y ]
