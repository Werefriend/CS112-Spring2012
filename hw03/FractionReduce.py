#!usr/bin/env python

print "I will reduce improper fractions for you."
num=int(raw_input("Please input a numerator value:  "))
denom=int(raw_input("Please input a denominator value:  "))

newnum=num%denom
whole=num/denom

print whole,str(newnum)+"/"+str(denom)

