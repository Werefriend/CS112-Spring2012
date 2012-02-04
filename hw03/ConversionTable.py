#!/usr/bin/env python

#gather 5 numbers from user and makes them integers
print "Please input five integers, each less than 256."
first=int(raw_input("First Number:  "))
second=int(raw_input("Second Number:  "))
third=int(raw_input("Third Number:  "))
fourth=int(raw_input("Fourth Number:  "))
fifth=int(raw_input("Fifth Number:  "))

#print data table with initial values and hex/bin values
print repr("Decimal").ljust(12),"|",repr("Binary").ljust(12),"|",repr("Hexadecimal").ljust(12)
l="_"*44
print l
print repr(first).rjust(12),"|",repr(bin(first)).rjust(12),"|",repr(hex(first)).rjust(12)
print l
print repr(second).rjust(12),"|",repr(bin(second)).rjust(12),"|",repr(hex(second)).rjust(12)
print l
print repr(third).rjust(12),"|",repr(bin(third)).rjust(12),"|",repr(hex(third)).rjust(12)
print l
print repr(fourth).rjust(12),"|",repr(bin(fourth)).rjust(12),"|",repr(hex(fourth)).rjust(12)
print l
print repr(fifth).rjust(12),"|",repr(bin(fifth)).rjust(12),"|",repr(hex(fifth)).rjust(12)
