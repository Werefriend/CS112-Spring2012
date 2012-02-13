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
ll =[]
for x in raw_input("Enter some digits separated by spaces:  ").split(" "):
    ll.append(int(x))
print "1.", ll


# 2.  Read another bunch of numbers, convert them, and return the list 
#     of only the first 3
binlist =[]
for x in raw_input("Enter some digits separated by spaces:  ").split(" "):
    binlist.append(bin(int(x)))
print "2.", binlist[0:3]


# 3.  Read a bunch of words separated by commas from the command line,
#     remove any excess spaces, and print a list of their lenghts
wordlist = []
for x in raw_input("Enter some words separated by commas:  ").strip(" ").split(","):
    wordlist.append(len(x))
print "3.", wordlist


# 4.  Create a list of every multiple of 3 between 1 and 100 with their 
#     index
#        ex:  [ [0,3], [1,6], [2,9]...]
print "4.", [(x, (x+1)*3) for x in range(33)]

# 5. create a list of every card in a deck of card
print "5.", [(s,t) for s in ["spades","hearts","diamonds","clubs"] for t in ["A","2","3","4","5","6","7","8","9","J","Q","K"]]

# 6.  Create a 5 by 5 array filled with zeros
hh = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]
print "6.",hh 


# 7.  Make a list of every perfect square between 1 and 1000
sq = []
gf = 0
while gf**2 < 1000:
    sq.append(gf**2),
    gf += 1
print "7.", [sq]

# 8.  Make a list of every perfect square between 1 and 1000 
#     a different way
print "8.", []

# 9.  List every python file in this directory
print "9.", []

# 10.  Print a list of every pythagorean triple with a side less than
#      or equal to 20.  Don't include duplicates ([3,4,5] == [4,3,5])
print "10.", []



# I couldn't in good concious include this, but it is fun to 
# figure out/find.

## NOT REQUIRED
# 11.  Print a list of every prime number less than 100
print "11.", []
