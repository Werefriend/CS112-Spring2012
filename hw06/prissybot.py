#!/usr/bin/env python


p = "Prissybot:  "

name = raw_input(p+"Enter your name  ")
print p + "Hello there, %s." %(name)

n = "%s:  " %(name)
resp1 = raw_input(n)
print p + 'You mean, "%s," sir!!!1!1' %(resp1)
print p + "How old are you in years, miserable meatsock?"
age = int(raw_input(n))


dog = age * 7
print p + "That means you're %d in dog years. Are you sure you're not a dog?" %(dog)
pause1 = raw_input(n)
print "You know your mother was a dog."
resp2 = raw_input(n)

length = len(resp2)
print p + "Oooh! Look!  Look at the human! %s can make phrases with" %(name), length, "characters."
print p + "What a SPECIAL vertebrate..."
print p + "Do you know what that %d divided by 17283 is," %(length), name + "?"
lengthnum = length/17283.0
vd = raw_input(n)
print p + "It's", lengthnum, ", meatsock."

print p + "What's you're favorite number?"
favorite = int(raw_input(n))

print p + "That's stupid,", name + "."
favorite += 1
print p, favorite, "is obviously superior, you ignorant air-breather."

