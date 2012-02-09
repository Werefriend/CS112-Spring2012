#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if n%2 == 0:
    print "1.", "%d is even." %(n)
else:
    print "1.", "%d is odd." %(n)

# 2. If n is odd, double it
if n%2 == 1:
    n*=2

print "2.", n


# 3. If n is evenly divisible by 3, add four
if n%3 == 0:
    n += 4
print "3.", n


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

lettergrade = "A"
if grade < 90:
    lettergrade = "B"
if grade < 80:
    lettergrade = "C"
if grade < 70:
    lettergrade = "D"
if grade < 60:
    lettergrade = "F"
print "4.", lettergrade

