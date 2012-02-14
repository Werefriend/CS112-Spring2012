#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""
#Introduce the game
print "Welcome to Nims.py."
print "Number of stones in pile: 40"
print "Max number of stones per turn: 5"
print "  "


#pile indicates the number of stones left, 
pile = 40
inv = "Invalid number of stones."
player = 1
choice = 0

#begin play and end at 1 or 0 stones in pile
while pile >= 1:
    choice = int(raw_input("%d stones left.  Player %d [1-5]: " %(pile, player)))
    #
    #determine valid input, get good input
    while choice < 1 or choice > pile or choice > 5:
        print inv
        choice = int(raw_input("%d stones left.  Player %d [1-5]: " %(pile, player)))
    pile -= choice
    if player == 2:
        player = 1
    elif player == 1:
        player = 2

#pick a winnahhhhhhhh
if pile == 0:
    print "Player %d wins!!!!1!!1" %(player)
