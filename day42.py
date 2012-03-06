#!/usr/bin/env python

color = (255, 10, 30)
people = {'Jonah' : "stupid", 'Alec' : "smelly",'Jack' : "ugly", 'Paul' : "awesome"}
matrix = ["hello", 2.0, 5, [10, 20]]
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
for k,v in eng2sp.items():
    print k,v

print eng2sp['one']

#print matrix
#print matrix[0]
#print matrix[1]
#print matrix[2]
#print matrix[3][0]
#print matrix[3][1]

#where would I use a multidimensional array??
#imagine you have an image of rows and columns... 
#for each tuple pixel, there are a red, green, and blue value

#TUPLES
#a tuple is any two or more things groued together
#unlike a list, these are immutable, meaning not changeable

#DICTIONARIES
#like a list, but the list defines the dictionary by a key, not an order

print len(people)
print people.keys()
print people.values()

s = "Monty Python"
print s[6:12]


