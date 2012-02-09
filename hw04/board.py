#!/usr/bin/env python

h = int(raw_input("Input a numerical height, please:  "))
w = int(raw_input("Input a numerical height, please:   "))
board = 0
row = "#-"*w


for i in range(h):
    print row[i%2:w+i%2]

