#!/usr/bin/env python

def ftoc(temp):
    cent = temp - 32
    cent *= 5
    cent /= 9
    return cent

num = int(raw_input("Enter a temperature in fahrenheidt: "))
print "In celcius, this is ", ftoc(num)
