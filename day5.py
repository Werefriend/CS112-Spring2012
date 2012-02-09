#!/usr/bin/env python

#What is a list? It's a mutable array!! An array has a fixed length.. but you can add to the length of a list!

#names=['bob','fred']

#print names [0]
#print names [1]

#print len(names)

#letters=['a','d','f']
#letters[1:1] = ['b','c']

#print letters
#print letters[-1]


#letters2 = letters

#print letters2


titles =["Hitchiker's Guide to the Galaxy",
         "Restaurant at the End of the Universe",
         "Life the Universe and Everything"]

titles.append("So long and thanks for all the fish")
titles.append("Mostly Harmless")

for title in titles:
                  print title

for i in range(1,11):
    print i
numbers = range(100)
decimals = numbers[:]
for i,n in enumerate(numbers):
    numbers[i] = n*.2
print numbers
